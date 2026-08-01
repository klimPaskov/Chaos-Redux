# IW-173 HAW Samuel Wilder King portrait audit v45

**Date:** 2026-08-01

**Reviewer:** Independent Chaos Redux sourced visual asset auditor v45.

**Scope:** Final strict recheck of the repaired IW-173 HAW Samuel Wilder King portrait review renderer and its candidate/reference panels. No runtime, DDS, `.gfx`, localisation, gameplay, character, roster, advisor, dossier, commander, or operative file was edited.

## Outcome

**PASS for the strict 4x evidence renderer.** The regenerated review sheet is complete, has the corrected header rectangle bounds, and preserves the candidate and role-reference panels at exact 4x nearest-neighbour scale. The portrait remains evidence-only until the parent makes the explicit HAW consumer decision and performs DDS conversion and `.gfx` wiring.

## Evidence

| Check | Status | Evidence |
| --- | --- | --- |
| Renderer source | **PASS** | `tools/create_review_sheet.py`, SHA-256 `2f3580adba0143535798ff86d1eaf6092f09b17b9f2602863c3993e33162859a`. The header rectangle now ends at `y + HEADER_H - 1`, so it cannot overwrite the first panel pixel row. |
| Review output | **PASS** | `review_sheets/HAW_samuel_wilder_king_source_raw_candidate_references_4x.png`, 2088x1974 RGB, SHA-256 `e8ef39ee88184eda8899903b2fba2db390ebdcbc6d7aa781cfcd83ffa56ff8c1`. The output height fully contains both rows. |
| Candidate 4x panel | **PASS** | The 156x210 RGBA candidate `processed_png/portrait_HAW_samuel_wilder_king.png` is enlarged to 624x840 with `Image.Resampling.NEAREST`; the centered panel compares byte-for-byte equal to the corresponding review-sheet pixels. |
| Stauning 4x panel | **PASS** | `portraits/leaders/den_thorvald_stauning.png` is enlarged to 624x840 with nearest-neighbour; the centered review panel compares byte-for-byte equal. |
| Mannerheim 4x panel | **PASS** | `portraits/leaders/fin_carl_mannerheim.png` is enlarged to 624x840 with nearest-neighbour and alpha-composited onto the documented `(9,12,16)` panel background; the review panel compares byte-for-byte equal after that expected composition. Its source alpha range is `(249,255)`. |
| Header overwrite regression | **PASS** | The first pixel row of each candidate/reference panel remains intact after the corrected `x + CELL_W - 1`, `y + HEADER_H - 1` rectangle bounds. No clipped identity region or interpolation pass was found. |
| Metadata synchronization | **NEEDS UPDATE** | `metadata/HAW_samuel_wilder_king_manual_export_v1.json` still records the previous review hash `1294633e24b82e00dc6c3259e384be6da89ed6df5c824b05d1add8fa4077f90f` rather than the regenerated v45 hash above. This is a documentation/provenance sync note, not a failure of the rendered panels. Update the metadata hash before treating the package record as fully current. |

## Existing portrait gates reaffirmed

The unchanged Commons/Hawaiʻi State Archives source and U.S. House role evidence remain valid; the exact crop JSON still records `decoded_pixels_equal=true`; the source-locked ImageGen repaint, current manual export metadata, 156x210 candidate, durable ComfyUI PNG/TXT pair, ownership/collision search, and no-advisor-art boundary remain as recorded in v44. No DDS exists and no runtime consumer is registered.

**Simplifications, omissions, and blockers:** No visual simplification or source substitution was made. The v45 renderer check passes. Only the manual metadata's stale review-sheet hash requires a documentation update; DDS conversion, `.gfx` wiring, and runtime admission remain intentionally unperformed and outside this audit scope.
