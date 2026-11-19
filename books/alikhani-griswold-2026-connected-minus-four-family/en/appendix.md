# Appendix: the 33-vertex starting point

This appendix supplies the base facts used in [@path-family] and [@every-order]. The graph $H$ is due to S. Alikhani and M. Griswold, Section 2, Theorem 2.1 and Corollary 2.2. Section 2 of the present paper recalculates it by splitting dominating sets. We specify the graph, finite sum, and factorization here.

## Full specification of the graph

The vertices are $0,1,\ldots,32$. Each row lists a smaller endpoint and all its larger neighbors, so every undirected edge appears once. Internal paths in each piece reach the four-cycle $0,1,2,3,0$, proving connectedness. Counting the listed edges gives 36. Vertex 12 has seven neighbors $0,1,13,14,15,16,17$; every other degree is at most seven. Vertex 4 has precisely neighbors 0 and 5, and vertex 5 has sole neighbor 4.

<section hidden="hidden">

```{=typst}
#block(width: 100%, breakable: false)[
#align(center)[
```

</section>

| Smaller endpoint | Larger neighbors |
| --- | --- |
| 0 | 1, 3, 4, 12 |
| 1 | 2, 12, 18 |
| 2 | 3, 6, 8, 10, 18, 21 |
| 3 | 21, 24 |
| 4 | 5 |
| 6 | 7 |
| 8 | 9 |
| 10 | 11 |
| 12 | 13, 14, 15, 16, 17 |
| 18 | 19, 20 |
| 21 | 22, 23 |
| 24 | 25, 26 |
| 26 | 27 |
| 27 | 28 |
| 28 | 29, 31 |
| 29 | 30 |
| 31 | 32 |

<section hidden="hidden">

```{=typst}
]]
```

</section>

## Reassemble small pieces

Remove the core $C=\{0,1,2,3\}$ to leave eight pieces $B_i$. Each root $a_i$ has an internal leaf. Let $I_i$ be its neighbors in the core and define

$$
M_i(b;x)=\sum_{\substack{T\in\mathcal D(B_i)\\\boldsymbol1_{a_i\in T}=b}}x^{|T|}.
$$

Here $b\in\{0,1\}$; $b=1$ means that the root is selected, and $b=0$ that it is omitted. The table values are finite subset sums given by this formula.

<section hidden="hidden">

```{=typst}
#block(width: 100%, breakable: false)[
#align(center)[
```

</section>

| Root | Piece vertices | $I_i$ | $M_i(0;-4)$ | $M_i(1;-4)$ |
| --- | --- | --- | --- | --- |
| 4 | 4–5 | $\{0\}$ | -4 | 12 |
| 6 | 6–7 | $\{2\}$ | -4 | 12 |
| 8 | 8–9 | $\{2\}$ | -4 | 12 |
| 10 | 10–11 | $\{2\}$ | -4 | 12 |
| 12 | 12–17 | $\{0,1\}$ | -1024 | 972 |
| 18 | 18–20 | $\{1,2\}$ | 16 | -36 |
| 21 | 21–23 | $\{2,3\}$ | 16 | -36 |
| 24 | 24–32 | $\{3\}$ | 5888 | -20736 |

<section hidden="hidden">

```{=typst}
]]
```

</section>

For $Z\subseteq C$ and a set of root indices $A\subseteq\{1,\ldots,8\}$, let $c(Z,A)=1$ if each core vertex is selected in $Z$, adjacent to $Z$, or belongs to $I_i$ for some $i\in A$; otherwise let it be zero. Then

$$
P(A;x)=\prod_{i=1}^8M_i(\boldsymbol1_{i\in A};x).
$$

$$
D(H,x)=\sum_{Z\subseteq C}x^{|Z|}\sum_{A\subseteq\{1,\ldots,8\}}c(Z,A)P(A;x).
$$

This is a complete finite formula: the edge table determines every term. The leaf argument again explains it. Restrict a dominating set to each $B_i$; the root's leaf guarantees internal domination of the root, and nonroot vertices have no outside neighbors. The remaining condition is exactly coverage of the core, $c(Z,A)=1$. Conversely, local choices satisfying these conditions assemble to a dominating set. Restriction and assembly are inverse, and cardinalities add, preserving weights.

There are $4\cdot2^2+2^6+2\cdot2^3+2^9=608$ component subsets to consider, and $2^4\cdot2^8=4096$ core/root states. Grouping by $|Z|$ gives the following five contributions at $x=-4$:

<section hidden="hidden">

```{=typst}
#block(width: 100%, breakable: false)[
#align(center)[
```

</section>

| $|Z|$ | Total contribution |
| --- | --- |
| 0 | 27135603376128 |
| 1 | −148575803670528 |
| 2 | 121440200294400 |
| 3 | −323840534118400 |
| 4 | 323840534118400 |

<section hidden="hidden">

```{=typst}
]]
```

</section>

The first three sum to zero, and the last two cancel, giving $D(H,-4)=0$. Keeping $x$ in the same sum gives

$$
\begin{aligned} D(H,x)&=x^{11}(x+2)(x+4)\\ &\quad\cdot(x^2+3x+1)Q_{18}(x). \end{aligned}
$$

The coefficients below, in increasing degree, specify all of $Q_{18}$ so that the integer-root claim does not depend on an unspecified polynomial.

<section hidden="hidden">

```{=typst}
#block(width: 100%, breakable: false)[
#align(center)[
```

</section>

| $j$ | $[x^j]Q_{18}$ |
| --- | --- |
| 0 | 36 |
| 1 | 573 |
| 2 | 4295 |
| 3 | 20061 |
| 4 | 65228 |
| 5 | 156593 |
| 6 | 287750 |
| 7 | 414314 |
| 8 | 474341 |
| 9 | 435134 |
| 10 | 320426 |
| 11 | 188808 |
| 12 | 88298 |
| 13 | 32314 |
| 14 | 9049 |
| 15 | 1871 |
| 16 | 269 |
| 17 | 24 |
| 18 | 1 |

<section hidden="hidden">

```{=typst}
]]
```

</section>

The source gives $D'(H,-4)=1100417597440000\ne0$, also obtained by differentiating the displayed factorization at $-4$. Thus the root is simple. Since $Q_{18}$ is monic with constant term 36, any integer root must be a signed divisor of 36. Horner substitution into the coefficient table gives the following signs; every entry is nonzero.

<section hidden="hidden">

```{=typst}
#block(width: 100%, breakable: false)[
#align(center)[
```

</section>

| $d$ | $Q_{18}(-d)$ sign | $Q_{18}(d)$ sign |
| --- | --- | --- |
| 1 | + | + |
| 2 | − | + |
| 3 | − | + |
| 4 | + | + |
| 6 | + | + |
| 9 | + | + |
| 12 | + | + |
| 18 | + | + |
| 36 | + | + |

<section hidden="hidden">

```{=typst}
]]
```

</section>

The quadratic factor has discriminant five and no integer roots. The remaining displayed factors therefore give exactly the integer roots $0,-2,-4$. The finite decomposition sum corresponds to [Lean's reassembly identity](lean:D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.reassembly). The [message-transfer theorem](lean:D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.zero_of_messages) requires the table entries to be the exact messages and the covered core sum to be zero. The final unbounded-order proof checks those messages and cancellation at $-4$ for this graph. The full polynomial, derivative, and integer-root deduction above follow the manuscript's written calculation; they are not added to the conclusion of that final formal theorem.
