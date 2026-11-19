<style>pre:has(> code[class*="typst"]) { display: none; }</style>

# Sources and references

1. Haobo Ma and Wenlin Zhang. *Alikhani–Griswold, Section 4(3): connected graphs with domination root −4*. Version 1, 2026. **Version DOI: [10.5281/zenodo.23919066](https://doi.org/10.5281/zenodo.23919066)**. Concept DOI: [10.5281/zenodo.23919065](https://doi.org/10.5281/zenodo.23919065). This explanation, talk, and film concern that version. Lemma 1, Theorem 2, and Corollary 3 share one counter in the original manuscript. The public [PDF](https://zenodo.org/api/records/23919066/files/note-v1.pdf/content) and [source](https://zenodo.org/api/records/23919066/files/source-v1.zip/content) are licensed CC BY 4.0.
2. S. Alikhani and M. Griswold. *On the Integer Domination Root Conjecture*. [arXiv:2608.00109v1](https://arxiv.org/abs/2608.00109v1), 2026. Section 4, item 3 asks the infinite-family question; the Section 2 edge list, Theorem 2.1, and Corollary 2.2 supply the base graph and its simple root.
3. T. Kotek, J. Preen, F. Simon, P. Tittmann and M. Trinks. *Recurrence relations and splitting formulas for the domination polynomial*. Electronic Journal of Combinatorics **19**(3), P47, 2012. [DOI:10.37236/2475](https://doi.org/10.37236/2475). Definition 3.9 and Theorem 3.11 supply the earlier irrelevant-edge theory used here.

Formal proof links lead directly to public Lean source: [unbounded order](lean:D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.result), [reassembly](lean:D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.reassembly), and [message transfer](lean:D5/S3/Combinatorics/Graph/Domination/MinusFourReassembly.zero_of_messages). Each supports its own precise statement. Contribution links for the manuscript's three fuller statements are in [Precise statements and proofs](statements.md).

```{=typst}
#pagebreak()
```
