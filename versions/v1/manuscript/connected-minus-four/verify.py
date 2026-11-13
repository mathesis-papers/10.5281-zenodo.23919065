import itertools
import json
from pathlib import Path


def add_polynomials(first, second):
    result = [0] * max(len(first), len(second))
    for index, value in enumerate(first):
        result[index] += value
    for index, value in enumerate(second):
        result[index] += value
    return result


def multiply_polynomials(first, second):
    result = [0] * (len(first) + len(second) - 1)
    for first_degree, first_value in enumerate(first):
        for second_degree, second_value in enumerate(second):
            result[first_degree + second_degree] += first_value * second_value
    return result


def evaluate(polynomial, value):
    total = 0
    for coefficient in reversed(polynomial):
        total = total * value + coefficient
    return total


def closed_neighborhoods(order, edges):
    neighborhoods = [1 << vertex for vertex in range(order)]
    for first, second in edges:
        assert 0 <= first < order and 0 <= second < order and first != second
        neighborhoods[first] |= 1 << second
        neighborhoods[second] |= 1 << first
    return neighborhoods


def dominating(order, edges, subset):
    neighborhoods = closed_neighborhoods(order, edges)
    covered = 0
    for vertex in range(order):
        if subset & (1 << vertex):
            covered |= neighborhoods[vertex]
    return covered == (1 << order) - 1


def exhaustive_polynomial(order, edges):
    neighborhoods = closed_neighborhoods(order, edges)
    polynomial = [0] * (order + 1)
    for subset in range(1 << order):
        covered = 0
        for vertex in range(order):
            if subset & (1 << vertex):
                covered |= neighborhoods[vertex]
        if covered == (1 << order) - 1:
            polynomial[subset.bit_count()] += 1
    return polynomial


def branch_messages(vertices, root, edges):
    labels = {vertex: index for index, vertex in enumerate(vertices)}
    internal_edges = [(labels[first], labels[second]) for first, second in edges
                      if first in labels and second in labels]
    messages = [[0] * (len(vertices) + 1) for state in range(2)]
    neighborhoods = closed_neighborhoods(len(vertices), internal_edges)
    for subset in range(1 << len(vertices)):
        covered = 0
        for vertex in range(len(vertices)):
            if subset & (1 << vertex):
                covered |= neighborhoods[vertex]
        if covered == (1 << len(vertices)) - 1:
            state = int(bool(subset & (1 << labels[root])))
            messages[state][subset.bit_count()] += 1
    return messages


def base_polynomial(data):
    edges = [tuple(edge) for edge in data['edges']]
    core = data['core']
    branches = data['branches']
    partition = core + [vertex for branch in branches for vertex in branch['vertices']]
    assert sorted(partition) == list(range(data['order']))
    assert len(edges) == len(set(tuple(sorted(edge)) for edge in edges)) == 36
    neighborhoods = closed_neighborhoods(data['order'], edges)
    assert max(neighborhood.bit_count() - 1 for neighborhood in neighborhoods) == 7
    assert neighborhoods[4].bit_count() - 1 == 2
    for branch in branches:
        root, leaf = branch['root'], branch['leaf']
        assert neighborhoods[leaf] == (1 << leaf) | (1 << root)
        for vertex in branch['vertices']:
            if vertex != root:
                allowed = sum(1 << item for item in branch['vertices'])
                assert neighborhoods[vertex] & ~allowed == 0
        actual_incidence = [vertex for vertex in core if neighborhoods[root] & (1 << vertex)]
        assert actual_incidence == branch['incidence']
        allowed = sum(1 << item for item in branch['vertices'] + branch['incidence'])
        assert neighborhoods[root] & ~allowed == 0
    reached = {0}
    while True:
        expanded = reached | {vertex for vertex in range(data['order'])
                              if any(neighborhoods[item] & (1 << vertex) for item in reached)}
        if expanded == reached:
            break
        reached = expanded
    assert len(reached) == data['order']
    messages = [branch_messages(branch['vertices'], branch['root'], edges) for branch in branches]
    polynomial = [0] * (data['order'] + 1)
    cancellation_by_core_size = [0] * (len(core) + 1)
    for core_subset in range(1 << len(core)):
        selected_core = sum(1 << vertex for index, vertex in enumerate(core)
                            if core_subset & (1 << index))
        for root_subset in range(1 << len(branches)):
            selected = selected_core | sum(1 << branch['root'] for index, branch in enumerate(branches)
                                          if root_subset & (1 << index))
            if not all(neighborhoods[vertex] & selected for vertex in core):
                continue
            contribution = [0] * core_subset.bit_count() + [1]
            for index in range(len(branches)):
                state = int(bool(root_subset & (1 << index)))
                contribution = multiply_polynomials(contribution, messages[index][state])
            polynomial = add_polynomials(polynomial, contribution)
            cancellation_by_core_size[core_subset.bit_count()] += evaluate(contribution, -4)
    return polynomial, messages, cancellation_by_core_size


def support_join(order, edges, copies, host_edges):
    result = [(copy * order + first, copy * order + second)
              for copy in range(copies) for first, second in edges]
    result.extend((first * order, second * order) for first, second in host_edges)
    return copies * order, result


def small_controls():
    controls = []
    assert exhaustive_polynomial(2, [(0, 1)]) == [0, 2, 1]
    assert exhaustive_polynomial(3, [(0, 1), (0, 2)]) == [0, 1, 3, 1]
    for order, edges, maximum_copies in [
        (2, [(0, 1)], 4),
        (3, [(0, 1), (0, 2)], 3),
        (4, [(0, 1), (0, 2), (2, 3)], 3),
    ]:
        factor = exhaustive_polynomial(order, edges)
        for copies in range(1, maximum_copies + 1):
            host_pairs = list(itertools.combinations(range(copies), 2))
            expected = [1]
            for copy in range(copies):
                expected = multiply_polynomials(expected, factor)
            for host_mask in range(1 << len(host_pairs)):
                host_edges = [edge for index, edge in enumerate(host_pairs) if host_mask & (1 << index)]
                joined_order, joined_edges = support_join(order, edges, copies, host_edges)
                assert exhaustive_polynomial(joined_order, joined_edges) == expected
                controls.append({'base_order':order, 'copies':copies, 'host_mask':host_mask})
    assert exhaustive_polynomial(2, [(0, 1)]) != [0, 0, 1]
    return {'host_instances':len(controls), 'maximum_vertices':12,
            'missing_leaf_control':'Joining two isolated vertices changes x^2 to x^2+2x.'}


def main():
    directory = Path(__file__).resolve().parent
    data = json.loads((directory / 'graph.json').read_text())
    polynomial, messages, grouped = base_polynomial(data)
    expected = [0] * 11 + [288, 5664, 52522, 305133, 1244812, 3790459, 8945790,
                            16782136, 25467963, 31644123, 32441211, 27555245,
                            19412673, 11324236, 5445556, 2142406, 681729, 172534,
                            33879, 4970, 512, 33, 1]
    assert polynomial == expected
    quotient = [36, 573, 4295, 20061, 65228, 156593, 287750, 414314, 474341,
                435134, 320426, 188808, 88298, 32314, 9049, 1871, 269, 24, 1]
    integer_candidates = [sign * divisor for divisor in range(1, 37)
                          if 36 % divisor == 0 for sign in [-1, 1]]
    assert all(evaluate(quotient, candidate) != 0 for candidate in integer_candidates)
    factored = [0] * 11 + [1]
    for factor in [[2, 1], [4, 1], [1, 3, 1], quotient]:
        factored = multiply_polynomials(factored, factor)
    assert factored == polynomial
    assert evaluate(polynomial, -4) == 0
    derivative = [degree * polynomial[degree] for degree in range(1, len(polynomial))]
    assert evaluate(derivative, -4) != 0
    omitted = [evaluate(pair[0], -4) for pair in messages]
    selected = [evaluate(pair[1], -4) for pair in messages]
    assert omitted == [-4, -4, -4, -4, -1024, 16, 16, 5888]
    assert selected == [12, 12, 12, 12, 972, -36, -36, -20736]
    assert sum(grouped) == 0
    output = {'base_order':data['order'], 'base_edges':len(data['edges']),
              'base_maximum_degree':7, 'attachment_support_degree':2,
              'coefficients_in_increasing_degree':polynomial,
              'base_evaluation_minus_four':evaluate(polynomial, -4),
              'base_derivative_minus_four':evaluate(derivative, -4),
              'base_minus_four_multiplicity':1, 'omitted_root_messages':omitted,
              'selected_root_messages':selected, 'core_size_contributions':grouped,
              'branch_subsets':sum(1 << len(branch['vertices']) for branch in data['branches']),
              'core_root_states':1 << (len(data['core']) + len(data['branches'])),
              'factorization':'x^11 (x+2) (x+4) (x^2+3x+1) Q18(x)',
              'quotient_integer_root_candidates':integer_candidates,
              'base_integer_roots':[-4, -2, 0],
              'small_controls':small_controls(),
              'coverage':{'finite_checks':'The base polynomial, root messages, simple root, and the listed small support joins.',
                          'written_proofs':'Support-edge invariance and the all-r connected families.'}}
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
