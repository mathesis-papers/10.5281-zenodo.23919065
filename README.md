# Alikhani–Griswold, Section 4(3): connected graphs with domination root −4

**Authors:** Haobo Ma, Wenlin Zhang

We answer Section 4, item 3 of Alikhani and Griswold's On the Integer Domination Root Conjecture by constructing connected graphs with domination root −4 and unbounded order. Joining r copies of their 33-vertex graph through vertices adjacent to leaves gives a connected graph on 33r vertices whose domination polynomial is the rth power of the original polynomial. The root −4 has multiplicity exactly r, and the copies can be joined along a path with maximum degree seven. A mixed construction gives examples of every order at least 35, with maximum degree seven and cycle rank four. We give a complete set-bijection proof, an exact finite calculation for the base graph, and the scope of the corresponding Lean declarations.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23919066](https://doi.org/10.5281/zenodo.23919066)
- Concept DOI: [https://doi.org/10.5281/zenodo.23919065](https://doi.org/10.5281/zenodo.23919065)
- License: CC-BY-4.0
- Version: 1
- Mathesis record: [alikhani-griswold-2026-connected-minus-four-family](https://mathesis-omega-research.apps.chrono-ai.fun/papers/alikhani-griswold-2026-connected-minus-four-family?version=1)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Alikhani–Griswold, Section 4(3): connected graphs with domination root −4. Mathesis, version 1. https://doi.org/10.5281/zenodo.23919066

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Lemma (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/a87bdf39e4517497a9773c0c724243bc700c5bb1/D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.lean) | No public receipt |
| Theorem (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/a87bdf39e4517497a9773c0c724243bc700c5bb1/D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.lean) | No public receipt |
| Corollary (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/a87bdf39e4517497a9773c0c724243bc700c5bb1/D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/10.5281-zenodo.23919065/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/10.5281-zenodo.23919065/alikhani-griswold-2026-connected-minus-four-family/zh/) · [Read in English](https://papers.trureturing.org/10.5281-zenodo.23919065/alikhani-griswold-2026-connected-minus-four-family/en/)

[Slides](https://papers.trureturing.org/10.5281-zenodo.23919065/alikhani-griswold-2026-connected-minus-four-family/slides/) ([sources](books/alikhani-griswold-2026-connected-minus-four-family/slides/)) · [Videos](https://papers.trureturing.org/10.5281-zenodo.23919065/alikhani-griswold-2026-connected-minus-four-family/films/) ([sources](books/alikhani-griswold-2026-connected-minus-four-family/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/10.5281-zenodo.23919065/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `support-join` | variant | `D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.reassembly` |
| `path-family` | variant | `D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.result` |
| `unbounded-order` | same | `D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.result` |
| `every-order` | variant | `D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.result` |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/alikhani-griswold-2026-connected-minus-four-family/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
