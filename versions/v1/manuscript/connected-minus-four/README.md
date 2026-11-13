# Connected graphs with domination root −4

This note answers Alikhani–Griswold, *On the Integer Domination Root Conjecture*, arXiv:2608.00109v1, Section 4, item 3.

## Main result

For every integer r ≥ 1, joining r copies of the source graph through their leaf-support vertices along a path gives a connected graph G_r with 33r vertices, 37r − 1 edges, maximum degree seven and D(G_r,x) = D(H,x)^r. The root −4 has multiplicity exactly r. A second family has 33r + 2 vertices and polynomial x(x + 2)D(H,x)^r.

Joining H, a copies of K2 and b copies of P3 by their leaf-support vertices gives T_(a,b) with 33 + 2a + 3b vertices, 36 + 2a + 3b edges and polynomial D(H,x)[x(x+2)]^a[x(x²+3x+1)]^b. Thus every order n ≥ 35 has a connected example with maximum degree seven, cycle rank four and simple root −4. Each of these graphs has exactly the integer roots 0, −2 and −4. The endpoint R_0 = K2 is excluded from that classification.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use an ordinary LaTeX distribution:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is included in `note.tex`; there are no external bibliography or figure dependencies.

## Exact finite calculations

Python 3.10 or later, standard library only:

```sh
python3 verify.py > calculated.json
python3 -c 'import json; assert json.load(open("calculated.json")) == json.load(open("verification.json"))'
```

`graph.json` contains the 36 factual edges from Section 2 of the source paper. The checker enumerates 608 component subsets and 4096 core/root states, reconstructs all coefficients of the base polynomial, checks its factorization, obtains D(H,−4) = 0 and D′(H,−4) = 1100417597440000, and verifies complete polynomials for 97 small support joins on at most 12 vertices. Testing the 18 signed divisors of the constant coefficient 36 of the monic factor Q18 establishes that the integer roots of the base and both families are exactly 0, −2 and −4.

## Proof coverage

The support-join polynomial identity, connectedness, degree bound and root multiplicities have written proofs in the note. The finite checker establishes the specifically enumerated base and small examples.

Pinned formal source: https://github.com/the-omega-institute/trureturing/blob/a87bdf39e4517497a9773c0c724243bc700c5bb1/D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.lean

Within `D5.S3.Combinatorics.Graph.Domination.MinusFourReassembly`, `reassembly` proves the general integer-weight component identity; `zero_of_messages` proves the corresponding implication from exact message values and a zero core sum; `result` proves connected graphs of arbitrarily large order with domination evaluation zero at −4. These formal statements concern integer evaluations; the stronger all-polynomial support-join identity is the written lemma in the note.

## Attribution and license

Creators, in order: Haobo Ma (ChronoAI Pte Ltd, Singapore); Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore).

The new note and checker are licensed CC BY 4.0 (`cc-by-4.0`): https://creativecommons.org/licenses/by/4.0/

The source graph and its original root are due to Saeid Alikhani and Max Griswold. The support-edge argument is a special case of the irrelevant-edge results of Kotek, Preen, Simon, Tittmann and Trinks, Electronic Journal of Combinatorics 19(3) (2012), P47, doi:10.37236/2475. Attribution does not change the license of those cited works.
