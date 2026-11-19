# Connecting graphs without changing the count

Can a network grow arbitrarily large, stay connected, and keep the same number $-4$ as a root of its counting polynomial? Haobo Ma and Wenlin Zhang answer yes. They link $r$ copies of a known 33-vertex network into a chain, obtaining a connected graph on $33r$ vertices in which the root $-4$ occurs exactly $r$ times. With two- and three-vertex attachments, they also obtain **every order $n\geq35$**, with no vertex having more than seven neighbors.

This answers Section 4, item 3 of S. Alikhani and M. Griswold's *On the Integer Domination Root Conjecture*. Their 33-vertex example is the starting point. The new explanation is how to turn that example into infinitely many connected ones while preserving the entire counting polynomial product. See [Version 1 of the paper](https://doi.org/10.5281/zenodo.23919066).

## Start with three choices

Think of a graph as stations joined by lines. Choose stations at which to place devices. A choice **dominates** the graph if each station either has a device or is next to one. Our graphs are finite, undirected, and have neither loops nor repeated edges. The graph must be connected; the chosen stations need not form a connected group.

For a graph consisting of a single edge, called $K_2$, label the ends $a,b$.

<section hidden="hidden">

```{=typst}
#block(width: 100%, breakable: false)[
#align(center)[
```

</section>

| Choice | Coverage | Weight |
| --- | --- | --- |
| $\{a\}$ | $a$ covers both | $x$ |
| $\{b\}$ | $b$ covers both | $x$ |
| $\{a,b\}$ | Both chosen | $x^2$ |

<section hidden="hidden">

```{=typst}
]]
```

</section>

The **domination polynomial** adds one term for every dominating choice. A choice of $k$ vertices contributes $x^k$, so

$$
D(K_2,x)=2x+x^2=x(x+2).
$$

At $x=1$ this counts three choices. At $x=-4$ it gives $-4-4+16=8$. Negative inputs assign signed weights; they do not mean negative numbers of choices. Saying that $-4$ is a root means that these signed weights cancel exactly.

Alikhani and Griswold's graph $H$ has 33 vertices and 36 edges, with $D(H,-4)=0$. Its root $-4$ is **simple**: the factor $x+4$ occurs exactly once in $D(H,x)$. We use this known starting point; the [appendix](appendix.md) supplies the full graph data, a decomposition calculation, and the simple-root check.

## Disconnected is easy; connected is the obstacle

In two separate graphs, a choice covers the whole graph exactly when it covers each part. Choice sizes add, so weights multiply, and the polynomials multiply too. Thus $r$ disjoint copies of $H$ already give $D(H,x)^r$.

But adding connecting edges can create new valid choices. Two isolated vertices must both be selected, giving $x^2$. Join them by an edge and either singleton works too: the polynomial becomes $x^2+2x$. Arbitrary connecting edges do not preserve the count.

## A leaf protects the attachment point

A vertex with exactly one neighbor is a **leaf**. Write $w$ for the leaf and $v$ for its sole neighbor, called its support. To cover $w$, a dominating choice must select $w$ or $v$. Either way, $v$ is already covered inside its original graph.

Now add edges only between supports in different graphs, leaving their leaves untouched. Why can this produce no new dominating choices? Restrict a dominating choice in the joined graph to one original piece:

1. Its leaf forces the attachment point $v$ to be covered internally.
2. Every other vertex has gained no outside neighbor, so its coverage must also come from inside that piece.
3. The restricted choice therefore dominates the original piece. Conversely, combining dominating choices from the pieces always dominates the joined graph.

Restriction and union undo each other, preserving the total number of selected vertices. The result preserves **the entire polynomial**, not just its value at $-4$. This is a special case of the irrelevant-edge theory of Kotek, Preen, Simon, Tittmann and Trinks; the paper supplies this direct proof for the case it needs.

The film draws the leaf, support, and new edge in sequence, then explains the polynomial product. Each outlined block represents a whole original graph, not a graph with only the few visible vertices.

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.film src="001-leaf-support"}
How one leaf makes a connecting edge preserve dominating choices; English narration with aligned English and Chinese subtitles.
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

## One copy, one more factor

In $H$, vertex 5 is a leaf whose only neighbor is vertex 4. Take $r\geq1$ copies of $H$ and join their vertices 4 along a path, obtaining $G_r$. The path makes the graph connected; the leaf argument gives

$$
D(G_r,x)=D(H,x)^r.
$$

If $D(H,x)=(x+4)A(x)$ with $A(-4)\ne0$, then

$$
D(G_r,x)=(x+4)^r A(x)^r.
$$

The root therefore has multiplicity exactly $r$. For $r=2$ there are 66 vertices and a double root; for $r=3$ there are 99 vertices and a triple root. Different vertex counts force nonisomorphic graphs, so these really are infinitely many examples.

We can track edges too. Each copy has 36, and the path adds $r-1$, giving $37r-1$. Vertex 4 originally has degree two and gains at most two neighbors. Every other degree stays unchanged, including degree seven at vertex 12. Thus the maximum degree is **exactly seven**, without a central station accumulating ever more neighbors.

## Filling every size after 34

One $H$ supplies 33 vertices. A single-edge piece $K_2$ adds two, and a three-vertex path $P_3$ adds three. Use an endpoint of $K_2$ and the middle vertex of $P_3$ as supports; each has its own leaf.

The path $P_3$ has one dominating singleton (the middle), three dominating pairs, and one dominating triple. Hence

$$
D(P_3,x)=x+3x^2+x^3=x(x^2+3x+1).
$$

At $-4$, these two small pieces contribute $8$ and $-20$, both nonzero. They neither remove the existing root nor increase its multiplicity.

<section hidden="hidden">

```{=typst}
#block(width: 100%, breakable: false)[
#align(center)[
```

</section>

| Desired order | Pieces to add |
| --- | --- |
| Odd $n\geq35$ | $(n-33)/2$ copies of $K_2$ |
| Even $n\geq36$ | One $P_3$ and $(n-36)/2$ copies of $K_2$ |

<section hidden="hidden">

```{=typst}
]]
```

</section>

For example, 35 vertices use $H+K_2$, 36 use $H+P_3$, and 37 use $H+2K_2$. Here the plus sign means disjoint pieces followed by edges between their supports. Arrange the supports along a path; the maximum degree stays seven.

The resulting graph has three more edges than vertices, so its **cycle rank**, the number of independent cycles in a connected graph, is $|E|-|V|+1=4$. These tree attachments lengthen the network without adding independent cycles. The known factorization of $D(H,x)$ also shows that its integer roots remain exactly $0,-2,-4$. The [precise statements and proofs](statements.md) give the full deduction.

## The answer and the formal evidence

The [Lean theorem on connected graphs of unbounded order](lean:D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.result) states that for every threshold $N$, some connected graph has more than $N$ vertices and ordinary domination polynomial zero at $-4$. Its witnesses use an additional hub and leaf, giving $33r+2$ vertices. The paper gives written proofs of the $33r$-vertex path family, exact multiplicities, degree bounds, and every-order construction. The [next chapter](statements.md) presents those statements and their evidence separately.

This argument answers the infinite-family question. It does not determine the minimum possible order or classify integer domination roots across all graphs. The recipe does not cover 34 vertices; that is a boundary of this recipe, not a nonexistence proof. The academic talk follows the same chain of ideas, with longer calculations in its appendix.

::: {.slides src="seminar"}
Aligned Chinese and English academic presentations: from three choices to infinitely many connected examples.
:::
