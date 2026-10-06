# Processing Decisions and Boundary Checks

## Previously reviewed chroma repairs

The current direct DDS files for the nine Event 005 Baltic sprites in `notes/previous_review_match.json` match the accepted `output_sha256` values in `docs/plans/gfx_fix_2026-10/final_contact_sheet_index.json`. The comparison covers `final_contact_sheets/005_1.png` tiles 4, 6, 8, 10, 11, 12, 14, 17, and 19. Their current alpha-edge measurement has zero magenta and zero green pixels under the review threshold. The severity-1 direct fringe rows other than German Border Pressure were retained unchanged; Scandinavian Listening Mission was reframed for its separate top-edge crop.

## Top-edge crop repairs

The five affected icon families share identical decoded source pixels between direct and focus aliases. The final processed images were uniformly resized to 90x81 with premultiplied RGBA Lanczos and centered at `(2,2)` on a transparent 94x86 canvas. The nonzero-alpha bounds are 2–4 px from every edge. This produces an overall 4–5 px reduction and avoids distorting the medallions.

## Confirmed exterior chroma residue

A 3x smooth preview on checker, dark, and light backgrounds exposed 18 low-alpha chroma-classified pixels across the five reframed icons and the German Border Pressure replacement. Every changed pixel had alpha 1–6. The RGB value alone was replaced from the nearest eroded opaque, non-chroma interior pixel using SciPy `distance_transform_edt`; alpha was asserted unchanged. Exact coordinates and before/after RGBA values are in `notes/edge_color_repair.json`. Final `gfx.py alpha` reports zero chroma-edge pixels for all 13 modified PNGs.

## Port Economy edge

The shared `.tools/gfx/gfx.py defringe` command was evaluated on the direct Port Economy source. Its nearest-interior RGB propagation altered the entire semi-transparent painted shadow; the 3x comparison made the icon softer, so that output remains an unselected candidate at `processed_png/baltic_soviet_collapse_the_port_economy.png` with its output record in `notes/port_economy_defringe.json`. The selected repair applies exactly one square alpha erosion with a zero-padded 3x3 minimum filter and leaves every RGB byte unchanged. The selected output is `processed_png/baltic_soviet_collapse_the_port_economy_alpha_erosion1.png`; its nonzero-alpha bounds are `[4,3,90,83]` on 94x86, and the comparison is `contact_sheets/qa_port_economy_alpha_only.png`.

## Alpha and frame QA

Generated subjects use native ImageGen alpha and all four unused source corners are fully transparent. The selected Pan-Baltic edit branch restores the complete laurel inside source alpha bounds `[116,91,1195,1105]` before scaling to 94x86; no transparency removal or opaque background edit was used. The Tallinn-Riga-Vilnius rotation’s open interior between three civic seals is intentional composition space, not an accidental hole. Final PNG alpha/size results are in `notes/alpha_audit_final.json` and `notes/size_audit_final.json`; final DDS header and round-trip checks are in `notes/dds_validation_final.json`.

## Candidate branches

Restoration Pact iterations R1, R1 edit1, R2, R2 edit1, and selected R3 are retained under `source_png/imagegen/` and `prompts/`. Pan-Baltic iterations P1, P2, P2 edit1, and selected P2 edit2 are retained the same way. The full prompt, source hash, tool output path, branch parent, and decision are in `notes/candidate_lineage.md`.
