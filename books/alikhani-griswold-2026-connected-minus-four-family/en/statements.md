# Precise statements and proofs

“Lemma 1”, “Theorem 2”, and “Corollary 3” below are the original manuscript's numbers; this book numbers environments separately. Write $V(G)$ and $E(G)$ for vertices and edges, $N_G(w)$ for the neighbors of $w$, and $\mathcal D(G)$ for all ordinary dominating subsets. Define

$$
D(G,x)=\sum_{S\in\mathcal D(G)}x^{|S|}\in\mathbb Z[x].
$$

Throughout, $H$ is the 33-vertex graph fully specified in the [appendix](appendix.md). It is connected, has 36 edges and maximum degree seven; vertex 4 has degree two and vertex 5 has sole neighbor 4. Its root $-4$ is simple and its integer roots are exactly $0,-2,-4$.

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.lemma #support-join title="Leaf-support joining (source Lemma 1)" status="written-proof" proof="pf-support-join" doi="10.5281/zenodo.23919066" source="Lemma 1, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/203" mathesis="collected:alikhani-griswold-2026-connected-minus-four-family:1:s1"}
Let $H_1,\ldots,H_r$ be vertex-disjoint finite simple graphs with specified vertices $v_i,w_i$ satisfying $N_{H_i}(w_i)=\{v_i\}$. Let $F$ be any simple graph on $\{1,\ldots,r\}$. Form $J_F$ from their disjoint union by adding $v_iv_j$ for each $ij\in E(F)$. Then

$$
\mathcal D(J_F)=\{S_1\cup\cdots\cup S_r:S_i\in\mathcal D(H_i)\},
$$

$$
D(J_F,x)=\prod_{i=1}^rD(H_i,x).
$$

If $r\geq1$ and every $H_i$ and $F$ are connected, $J_F$ is connected.
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

::: {.proof #pf-support-join}
Following source Lemma 1, let $S$ dominate $J_F$ and put $S_i=S\cap V(H_i)$. The neighbors of the leaf $w_i$ have not changed, so $w_i\in S_i$ or $v_i\in S_i$. Either case dominates $v_i$ inside $H_i$. Every other vertex has no outside neighbor and is therefore also dominated internally. Hence $S_i\in\mathcal D(H_i)$. The converse holds because no original edge was removed. Restriction and union are inverse and satisfy $|S|=\sum_i|S_i|$. Sum the weights $x^{|S|}=\prod_i x^{|S_i|}$ to obtain the identity in $\mathbb Z[x]$. For connectedness, follow a path inside a piece to its support, then paths between supports in $F$. At $r=1$ no edge is added. With the empty-family convention $r=0$, the empty graph has the empty set as its sole dominating set and the product is 1; there is no connectedness assertion in that case.
:::

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.theorem #path-family title="Bounded-degree path family (source Theorem 2)" status="written-proof" proof="pf-path-family" doi="10.5281/zenodo.23919066" source="Theorem 2, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/204" mathesis="collected:alikhani-griswold-2026-connected-minus-four-family:1:s2"}
For every integer $r\geq1$ there is a connected finite simple graph $G_r$ with

$$
|V(G_r)|=33r,
$$

$$
D(G_r,x)=D(H,x)^r.
$$

The root $-4$ has multiplicity exactly $r$. The graphs can be chosen with $37r-1$ edges and maximum degree seven. Consequently, for every $N\in\mathbb N$ there is such a graph of order strictly greater than $N$.
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

::: {.proof #pf-path-family}
Following source Theorem 2, use $r$ copies of $H$, set $v_i=4,w_i=5$ in each copy, and take $F=P_r$. Result [@support-join] gives connectedness and the polynomial identity. Write $D(H,x)=(x+4)A(x)$ with $A(-4)\ne0$; then $D(G_r,x)=(x+4)^r A(x)^r$, proving exact multiplicity $r$. The edge count is $36r+(r-1)$. Supports rise from degree two to at most four, while every other vertex is unchanged; vertex 12 retains degree seven and attains the maximum. For $r=1$, $G_1=H$ and all formulas still hold. Given $N$, choose $r=N+1$ to get $33r>N$. Different values of $r$ give different orders and hence nonisomorphic graphs.
:::

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.corollary #unbounded-order title="Connected graphs of unbounded order" lean="D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.result" mathesis="collected:alikhani-griswold-2026-connected-minus-four-family:1:s2"}
For every natural number $N$, there are a natural number $n>N$ and a simple graph $G$ on $\operatorname{Fin}(n)$ such that $G$ is connected and

$$
\sum_{S\in\mathcal D(G)}(-4)^{|S|}=0.
$$
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

::: proof
This separates the unbounded-order consequence of source Theorem 2 and states the complete conclusion of the linked formal theorem. The path family above gives a written deduction. The formal proof uses a different construction $R_r$: join vertex 4 of each of $r$ copies of $H$ to a new hub $h$, and add a new leaf $p$ at $h$. Regard $hp$ as an additional $K_2$ piece. Leaf-support joining gives

$$
|V(R_r)|=33r+2,
$$

$$
D(R_r,x)=x(x+2)D(H,x)^r.
$$

Choose $r=N+1\geq1$. The value at $-4$ is zero and the order exceeds $N$. Relabeling the finite vertex set as $\operatorname{Fin}(33r+2)$ preserves connectivity and dominating-set sizes. At $r=0$ the graph is $K_2$ and the value is 8, so positive $r$ is essential here. The cited theorem does not assert the path family's multiplicity, edge count, or degree bound.
:::

<section hidden="hidden">

```{=typst}
#block(breakable: false)[
```

</section>

::: {.corollary #every-order title="Every order at least 35 (source Corollary 3)" status="written-proof" proof="pf-every-order" doi="10.5281/zenodo.23919066" source="Corollary 3, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/205" mathesis="collected:alikhani-griswold-2026-connected-minus-four-family:1:s3"}
Every integer $n\geq35$ is the order of a connected finite simple graph with maximum degree seven, cycle rank four, and simple domination root $-4$. Its integer domination roots are exactly $0,-2,-4$.
:::

<section hidden="hidden">

```{=typst}
]
```

</section>

::: {.proof #pf-every-order}
Following source Corollary 3, take one $H$, $a\geq0$ copies of $K_2$ and $b\geq0$ copies of $P_3$. Use vertex 4 of $H$, one endpoint of each $K_2$, and the middle of each $P_3$ as supports, then join all supports along a path. Result [@support-join] gives a connected graph $T_{a,b}$ with

$$
|V(T_{a,b})|=33+2a+3b,
$$

$$
|E(T_{a,b})|=36+2a+3b.
$$

For the edges, add the $36+a+2b$ internal edges and $a+b$ connecting edges. Its polynomial is

$$
\begin{aligned} D(T_{a,b},x)&=D(H,x)\\ &\quad\cdot[x(x+2)]^a[x(x^2+3x+1)]^b. \end{aligned}
$$

The new factors evaluate to 8 and $-20$ at $-4$, so the root stays simple. The quadratic $x^2+3x+1$ has discriminant five and no integer roots; the only other added integer roots are $0,-2$, already roots of $H$. The cycle rank is $|E|-|V|+1=4$. All supports have degree at most four, and the original degree-seven vertex is unchanged, so the maximum degree is seven. For odd $n\geq35$ choose $b=0,a=(n-33)/2$; for even $n\geq36$ choose $b=1,a=(n-36)/2$. These are nonnegative integers and cover all $n\geq35$.
:::

## Contributing the remaining formal statements

The original lemma, theorem, and corollary have separate shared requests for [leaf-support polynomial joining](https://github.com/the-omega-institute/trureturing-requests/issues/203), [the path family and exact multiplicity](https://github.com/the-omega-institute/trureturing-requests/issues/204), and [every order at least 35](https://github.com/the-omega-institute/trureturing-requests/issues/205). The last two can reuse the joining lemma; the every-order construction does not depend on the repeated-copy path-family theorem. Work in a contributor fork and submit a focused PR directly to upstream `dev` under its [existing contribution rules](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md). Each request links the public source, existing formal prerequisites, and exact remaining target.
