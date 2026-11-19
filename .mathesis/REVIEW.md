# 陈述与 Lean 精确比较

比较基于公开第 1 版论文（版本 DOI：10.5281/zenodo.23919066），不修改 catalog 状态。原文共享定理计数器依次为引理 1、定理 2、推论 3；两个 s2 环境分别解释完整结果及其中已精确形式化的推论。

实际读取书本完整钉版 `8a24ea4e79de962725aab9d9b49cc605fcc211d8` 的 `MinusFourReassembly.lean`、其 `Golden/Frozen/state/...lean.json` 和 Blueprint，以及直接相关的 `LocalDominatingStemBoundReplication.lean`。冻结表把公开 reassembly、zero_of_messages、result 列为 theorem；同时保留已证明的私有 support_replication_evaluation、support_replication_connected、family_of_root，不将“非公开”误写成“未证明”。本地锁最初只是无关示例的选定索引；通过安装的 `tbook pin --refresh` 在同一提交刷新后才判断引用。另读取原论文所引完整提交 `a87bdf39e4517497a9773c0c724243bc700c5bb1` 的同一 Lean 文件，与书本钉版文件逐字节一致。未构建 Lean 或下载完整库。

定向检索覆盖 domination、minus-four、leaf/support、replication、irrelevant-edge；公共递归树响应被截断，因此不声称穷尽整个上游。相关实际源文件足以判明下述候选声明的范围；不以本地索引缺条目证明全库不存在。公共证据直接链接 [所钉 Lean 源码](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.lean)。

| Result | Verdict | Compared declaration | Commit | Scope |
| --- | --- | --- | --- | --- |
| support-join | variant | D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.reassembly | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原文引理 1 要求任意有限简单零件、每个支撑点有保留的叶子，以及任意指标图 F；结论是支配集的大小保持双射、Z[x] 中多项式乘积和非空连通性。reassembly 对任意满足显式局部图律的核心/分支分解、任意整数 x 证明求值重组，不是这个任意支撑点连接的多项式陈述。已有私有 support_replication_evaluation 只处理带中心和叶子的复制构造；不把它说成缺少证明。请求 203 补公开通用多项式连接接口与对应双射。空族积为 1，不作连通断言。 |
| path-family | variant | D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原文定理 2 对每个 r>=1 同时断言 33r 阶路径族、37r-1 边、最大度七、多项式幂与根的精确重数 r，并推出无界阶。result 完整证明最后一个无界阶结论，证明中的私有复制恒等式给出 33r+2 阶中心构造的整数求值；并未陈述 33r 阶路径族、Z[x] 恒等式、精确重数或度数。因此整体判 variant；其准确可复用结论在 unbounded-order 同一 s2 节点中另列 same。请求 204 只补剩余精确族性质，复用请求 203 与基图单根。r=1 无新边。 |
| unbounded-order | same | D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原文定理 2 的最后一个推论单独陈述，仍映射原 s2，不另造 catalog 节点。任意自然数 N，存在自然数 n>N 和 Fin(n) 上的连通简单图 G，普通支配子集的 (-4)^card 整数和为零；与 result 第 571-572 行完整量词、域、严格界和结论相同。证明采用 33(N+1)+2 阶中心/叶子构造；该 same 环境不带路径族度数、重数或每阶性质，不申请重复证明。 |
| every-order | variant | D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原文推论 3 对每个整数 n>=35 要求连通、最大度七、循环秩四、-4 单根、整数根恰为 0,-2,-4。result 只有无界阶存在性，既不覆盖每个 n，也不包含这些约束。请求 205 复用请求 203、H 的单根/整数根与 K2/P3 因子，独立于 r 份 H 的路径族。n=35 和 n=36 分别是奇偶边界，a,b 可为零；不声称 n=34 不存在。 |

## 请求与公开来源

检查创建前全部 202 个开放与关闭共享问题，按 DOI、对象和数学结论去重，无匹配范围。分别登记 203、204、205；每个只登记一次，双语共用标记与 URL。公开依据为已验证版本 DOI 及其公开源 ZIP，而非尚未发布的本书章节。203 的通用连接是 204 和 205 的实际先决条件；205 不依赖 204 的复制族。已精确覆盖的无界阶推论不登记新请求。采用贡献者 fork 直接向上游 dev 提交的既有路线，不改变准入、CI 或积分。

`stage=complete` 表示章节与 claim 映射齐备，不表示视频已渲染、读者产物已构建或出版已通过。源准备后的真实构建与逐页检查由本次操作者执行，外部运行记录保存具体状态。
