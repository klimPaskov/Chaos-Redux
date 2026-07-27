# Event 006 portrait shelf completeness re-audit

Date: 2026-07-27

Scope: durable pre-DDS source portrait shelf only.

## Result

The shelf now contains **49** byte-copied pre-resize source-derived HOI4 repaint masters and **83** normalized `156x210` PNGs. The added master is the withdrawn IW-093 Asante/Prempeh II ImageGen repaint from `iw093_asante_prempeh_ii_2026_07_18/source_png/portrait_DOX_prempeh_ii_imagegen_master.png`.

Shelf copy:

`docs/assets/006_independence_wave/portraits_generated_png/pre_resize_source_repaints/2026_07_18/iw093_asante_prempeh_ii/DOX_prempeh_ii_identity_preserve_imagegen_master_withdrawn.png`

The source and shelf copy are byte-identical at SHA-256 `5f4769bb6a290a0399cd4190757f2821e82b1ebe9d059f3e6f5ca8997f5ad86d`, with dimensions `1080x1456`, RGB mode, and 2,600,109 bytes. It remains withdrawn evidence only; it is not a runtime DDS, `.gfx` reference, character admission, or package attestation.

## Audit method

The Event 006 asset metadata was scanned for every `source_kind: real` portrait source whose generated output is a large ImageGen/repaint/master PNG. The scan found 49 such masters, and all 49 hashes are now represented under `pre_resize_source_repaints/`. Raw archival photographs, exact crops, review/contact sheets, normalized PNGs, fictional/collective portraits, flags, icons, and DDS files remain outside the pre-resize master count by design.

The normalized shelf remains `83` PNGs, all `156x210`; no advisor, dossier, commander-thumbnail, `_small`, or runtime-only derivative was added. `PRE_RESIZE_MANIFEST.md`, `MANIFEST.md`, and the shelf README are the current count and provenance authorities.

## Disposition

**PASS as evidence-shelf completeness; no runtime promotion.** The source-only portrait workflow remains unchanged: unchanged attributed archival source, explicit crop, identity-preserving HOI4 repaint, deterministic normalization, independent audit, and only then DDS wiring. Candidate, rejected-style, withdrawn, research-hold, and `needs_user_review` rows remain fail-closed.
