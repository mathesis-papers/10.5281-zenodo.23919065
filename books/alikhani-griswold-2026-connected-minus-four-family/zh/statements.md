<style>pre:has(> code[class*="typst"]) { display: none; }</style>

# 精确陈述与证明

下列“引理 1”“定理 2”“推论 3”均指原论文编号；本书环境另有自动编号。$V(G)$ 和 $E(G)$ 分别为顶点集、边集，$N_G(w)$ 是 $w$ 的邻居集。记 $\mathcal D(G)$ 为全部普通支配集，定义

$$
D(G,x)=\sum_{S\in\mathcal D(G)}x^{|S|}\in\mathbb Z[x].
$$

$H$ 始终指[附录](appendix.md)中完整指定的 33 点图。它连通，有 36 条边，最大度七；顶点 4 的度为二，顶点 5 的唯一邻居为 4；$-4$ 是单根，整数根恰好为 $0,-2,-4$。

```{=typst}
#block(breakable: false)[
```

::: {.lemma #support-join title="叶支撑连接（原文引理 1）" status="written-proof" proof="pf-support-join" doi="10.5281/zenodo.23919066" source="Lemma 1, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/203" mathesis="collected:alikhani-griswold-2026-connected-minus-four-family:1:s1"}
设 $H_1,\ldots,H_r$ 为顶点互不相交的有限简单图，每个图指定 $v_i,w_i$，满足 $N_{H_i}(w_i)=\{v_i\}$。$F$ 是指标集 $\{1,\ldots,r\}$ 上的任意简单图。在不交并中，对每条 $ij\in E(F)$ 加边 $v_iv_j$，所得图记为 $J_F$。则

$$
\mathcal D(J_F)=\{S_1\cup\cdots\cup S_r:S_i\in\mathcal D(H_i)\},
$$

$$
D(J_F,x)=\prod_{i=1}^rD(H_i,x).
$$

若 $r\geq1$ 且所有 $H_i$ 和 $F$ 连通，则 $J_F$ 连通。
:::

```{=typst}
]
```

::: {.proof #pf-support-join}
依原文引理 1。若 $S$ 支配 $J_F$，令 $S_i=S\cap V(H_i)$。叶子 $w_i$ 的邻居没有变化，故 $w_i\in S_i$ 或 $v_i\in S_i$。两种情况都使 $v_i$ 在 $H_i$ 内被支配。其他顶点没有外部邻居，故同样在 $H_i$ 内被支配。于是 $S_i\in\mathcal D(H_i)$。反方向因为没有删除旧边而成立。限制与并集互逆，并满足 $|S|=\sum_i|S_i|$。将权重 $x^{|S|}=\prod_i x^{|S_i|}$ 求和，得整系数多项式恒等式。连通性由每个顶点到其支撑顶点的路径，再接上 $F$ 中的路径得到。$r=1$ 时不加边；若采用 $r=0$ 的约定，则空图唯一的支配集为空集，空积为 1，不作连通断言。
:::

```{=typst}
#block(breakable: false)[
```

::: {.theorem #path-family title="有界度路径族（原文定理 2）" status="written-proof" proof="pf-path-family" doi="10.5281/zenodo.23919066" source="Theorem 2, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/204" mathesis="collected:alikhani-griswold-2026-connected-minus-four-family:1:s2"}
对每个整数 $r\geq1$，存在连通有限简单图 $G_r$，满足

$$
|V(G_r)|=33r,
$$

$$
D(G_r,x)=D(H,x)^r.
$$

根 $-4$ 的重数恰为 $r$；可使边数为 $37r-1$，最大度为七。因此对每个 $N\in\mathbb N$，都有这样的图，其顶点数严格大于 $N$。
:::

```{=typst}
]
```

::: {.proof #pf-path-family}
依原文定理 2。取 $r$ 份 $H$，在每份中指定 $v_i=4,w_i=5$，令连接图 $F=P_r$。由 [@support-join] 得连通性与多项式恒等式。写 $D(H,x)=(x+4)A(x)$，$A(-4)\ne0$，则 $D(G_r,x)=(x+4)^r A(x)^r$，重数恰为 $r$。边数为 $36r+(r-1)$。支撑顶点从度二增至至多四，其他顶点不变，故顶点 12 保持度七并给出最大度。$r=1$ 时 $G_1=H$，所有公式仍成立。给定 $N$，取 $r=N+1$，则 $33r>N$。不同的 $r$ 给出不同阶，故这些图两两不同构。
:::

```{=typst}
#block(breakable: false)[
```

::: {.corollary #unbounded-order title="连通图的无界阶结论" lean="D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.result" mathesis="collected:alikhani-griswold-2026-connected-minus-four-family:1:s2"}
对每个自然数 $N$，存在自然数 $n>N$ 以及顶点集为 $\operatorname{Fin}(n)$ 的简单图 $G$，使 $G$ 连通且

$$
\sum_{S\in\mathcal D(G)}(-4)^{|S|}=0.
$$
:::

```{=typst}
]
```

::: proof
这是原文定理 2 的无界阶推论单独陈述，对应所引形式定理的完整结论。上述路径族已给出书面推导；形式证明采用另一构造 $R_r$：把 $r$ 份 $H$ 的顶点 4 接到新中心 $h$，再给 $h$ 加叶子 $p$。把 $hp$ 视为额外的 $K_2$ 零件，可由叶支撑连接得

$$
|V(R_r)|=33r+2,
$$

$$
D(R_r,x)=x(x+2)D(H,x)^r.
$$

取 $r=N+1\geq1$，在 $-4$ 处为零，且顶点数超过 $N$；有限顶点重编号为 $\operatorname{Fin}(33r+2)$ 不改变连通性或支配集大小。$r=0$ 时只有 $K_2$，其值为 8，故这里必须取正的 $r$。所引定理并不附带路径族的重数、边数或度数结论。
:::

```{=typst}
#block(breakable: false)[
```

::: {.corollary #every-order title="每个至少 35 的阶（原文推论 3）" status="written-proof" proof="pf-every-order" doi="10.5281/zenodo.23919066" source="Corollary 3, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/205" mathesis="collected:alikhani-griswold-2026-connected-minus-four-family:1:s3"}
每个整数 $n\geq35$ 都是某个连通有限简单图的阶。该图可取最大度七、循环秩四，支配多项式以 $-4$ 为单根，且整数支配根恰好为 $0,-2,-4$。
:::

```{=typst}
]
```

::: {.proof #pf-every-order}
依原文推论 3。取一份 $H$、$a\geq0$ 份 $K_2$、$b\geq0$ 份 $P_3$。支撑点分别取 $H$ 的顶点 4、$K_2$ 的一端、$P_3$ 的中点，再将这些支撑点沿路径连接。由 [@support-join] 得连通图 $T_{a,b}$，且

$$
|V(T_{a,b})|=33+2a+3b,
$$

$$
|E(T_{a,b})|=36+2a+3b.
$$

边数计算使用零件内部的 $36+a+2b$ 条边与连接零件的 $a+b$ 条边。多项式为

$$
\begin{aligned} D(T_{a,b},x)&=D(H,x)\\ &\quad\cdot[x(x+2)]^a[x(x^2+3x+1)]^b. \end{aligned}
$$

两个新增因子在 $-4$ 处分别为 8 和 $-20$，因此 $-4$ 仍为单根。$x^2+3x+1$ 的判别式为五，没有整数根，其他新增整数根只有 $0,-2$，已包含在 $H$ 的整数根中。循环秩为 $|E|-|V|+1=4$。所有支撑点的度至多为四，原有度七顶点不变，所以最大度七。奇数 $n\geq35$ 取 $b=0,a=(n-33)/2$；偶数 $n\geq36$ 取 $b=1,a=(n-36)/2$，均为非负整数。这覆盖全部 $n\geq35$。
:::

## 参与后续形式化

原文引理、定理、推论分别对应[叶支撑多项式连接](https://github.com/the-omega-institute/trureturing-requests/issues/203)、[路径族与精确重数](https://github.com/the-omega-institute/trureturing-requests/issues/204)、[每个至少 35 的阶](https://github.com/the-omega-institute/trureturing-requests/issues/205)三个共享请求。后两项可复用第一项；每阶构造并不依赖复制 $r$ 份的路径族定理。贡献者在自己的 fork 中完成聚焦的证明，再按[上游贡献规则](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)直接向 `dev` 提交。请求给出公开原文、已有形式证明和精确剩余目标。
