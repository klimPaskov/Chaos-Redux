# Event 006 asset-clearance handoff: IW-093 and IW-098

Date: 2026-07-26

Status: **partial / fail-closed**. This handoff records source and processing evidence only. It does not admit either package to runtime, create a DDS, wire a portrait or flag, or create advisor icons.

## Scope

- IW-093 Asante, tag `DOX`, state 274 (Kumasi), reservation group `RG-GHANA-ASANTE`, historical leader candidate Prempeh II.
- IW-098 Sokoto, tag `SOK`, state 902, reservation group `RG-NIGERIA-COARSE`, historical leader roster candidates Hasan, Siddiq, Dikko, and Bello.

## IW-093 evidence produced

The source researcher identified the TNA `CO 1069-44-12` 1935 Prempeh II photograph and recorded it as an OGL source candidate. The immutable source master is [CO_1069-44-12_prempeh_ii_1935.jpg](../../../assets/006_independence_wave/iw093_iw098_asset_clearance_2026_07_26/source/DOX/CO_1069-44-12_prempeh_ii_1935.jpg), SHA-256 `98a1109e23751f0ad64d970044c1c1eca3040333d7e16da357804b484587f144`.

The exact head-and-shoulders crop is [DOX_prempeh_ii_archival_crop.png](../../../assets/006_independence_wave/iw093_iw098_asset_clearance_2026_07_26/crops/DOX/DOX_prempeh_ii_archival_crop.png), with JSON equality evidence in [DOX_prempeh_ii_archival_crop.json](../../../assets/006_independence_wave/iw093_iw098_asset_clearance_2026_07_26/metadata/DOX/DOX_prempeh_ii_archival_crop.json). The recorded crop rectangle is `(105, 5, 275, 234)` in the 393x563 source, and the decoded crop/output pixels compare equal.

The source-locked HOI4-style ImageGen repaint is [DOX_prempeh_ii_identity_preserve_imagegen.png](../../../assets/006_independence_wave/iw093_iw098_asset_clearance_2026_07_26/repaints/DOX/DOX_prempeh_ii_identity_preserve_imagegen.png), 1083x1453 RGB, SHA-256 `4e2c3c22380aa52eda941169381403e126baed938fb6646c99b475d022f2bd8a`. The deterministic normalized candidate is [portrait_DOX_prempeh_ii_156x210.png](../../../assets/006_independence_wave/iw093_iw098_asset_clearance_2026_07_26/processed_png/DOX/portrait_DOX_prempeh_ii_156x210.png), SHA-256 `638d0a5ca4be40ceb29e5896575711b8c36f68f444f2edee19f1efc06d57e175`.

Processing metadata records the canonical vanilla leader references `den_thorvald_stauning.png` and `fin_carl_mannerheim.png`, the exact source hash, deterministic seed payload, and `status: candidate_requires_visual_approval`. The review sheet is [portrait_DOX_prempeh_ii_review.png](../../../assets/006_independence_wave/iw093_iw098_asset_clearance_2026_07_26/review_sheets/DOX/portrait_DOX_prempeh_ii_review.png).

The raw repaint master and normalized candidate were copied to the requested reference shelf:

- `docs/assets/006_independence_wave/portraits_generated_png/pre_resize_source_repaints/2026_07_26/iw093_iw098_asset_clearance_v1/DOX_prempeh_ii_identity_preserve_imagegen.png`
- `docs/assets/006_independence_wave/portraits_generated_png/source_candidates/iw093_iw098_asset_clearance_2026_07_26/portrait_DOX_prempeh_ii_156x210.png`

The shelf manifests record both copies as reference-only and explicitly pending the independent likeness/style/provenance gate.

## IW-098 status

No IW-098 source package is cleared by this handoff. An existing Muhammadu Dikko source candidate is OGL but remains in a rejected-style/reference package. A Hasan/Bayero 1934 London Zoo candidate has a rights/date conflict that must be resolved before use, and no defensible Siddiq source was established. No Sokoto repaint, normalized portrait, flag, DDS, or runtime wiring is promoted.

## Flags and prohibited outputs

No historical flag geometry was admitted and no ImageGen flat flag package was produced in this bounded handoff. A future flag must be a clean, flat historical design informed by a verified source, not flag artwork, fabric, or a painterly scene. No advisor icons were created or promoted for Event 006.

## Required next gate

Before any Event 006 runtime use, an independent reviewer must compare the unchanged source, exact crop, raw repaint, normalized candidate, and vanilla references and record separate likeness, HOI4-style, provenance, and rights verdicts. A `PASS` is required before DDS conversion and `.gfx`/character wiring. IW-098 remains blocked until each roster member has a cleared source or the registry package is explicitly held back.
