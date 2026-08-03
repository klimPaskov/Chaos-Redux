# IW-182 GZX Newfoundland portrait source handoff — 2026-08-03

## Decision

**SAFE SOURCE / RUNTIME HOLD.** A defensible male 1936-compatible Newfoundland civic subject and archival source were found, downloaded, cropped, and repainted. The source is safe for the grounded source pipeline and evidence retention, but it is not safely promotable to DDS or runtime until the parent resolves the source page’s rights warning and obtains an independent likeness/style/provenance PASS.

The package is not blocked for lack of identity evidence. It is held on rights/audit gates. No generic, generated, post-period, or invented substitute was used.

## Selected subject

- **Person:** William Richard Howley (1875–1941).
- **1936-compatible office:** Vice-Chairman of the Newfoundland Commission of Government from 26 February 1936 to 1937; Commissioner for Justice and Attorney General from 16 February 1934 to 1937.
- **Identity classification:** grounded historical Newfoundland officeholder; source mode `grounded_source_only`.
- **Role rationale:** the accepted IW-182 research row requires a sourced real male officeholder or authentic archival institution for the provisional government. Howley is an exact Commission-of-Government officeholder during the package’s 1936 baseline.

## Source and rights evidence

- **Archive:** National Portrait Gallery, London, Bassano Ltd whole-plate film negative, item `x152735`.
- **Source page:** <https://commons.wikimedia.org/wiki/File:William_R._Howley_in_1937.jpg>.
- **Direct media URL used:** <https://i0.wp.com/upload.wikimedia.org/wikipedia/commons/8/81/William_R._Howley_in_1937.jpg>.
- **Source date:** 15 April 1937.
- **Commons template:** `PD-UK-Unknown`.
- **Rights caveat:** Commons warns that third parties have asserted possible skill-and-labour or mechanical-reproduction claims in some jurisdictions. This is a public-domain basis, not an unconditional worldwide licence.
- **Source disposition:** `SAFE_SOURCE_HOLD_NEEDS_USER_REVIEW`.

Role corroboration is recorded in [William R. Howley](https://en.wikipedia.org/wiki/William_Richard_Howley) and [Newfoundland and Labrador Heritage, “The Commission of Government, 1934–1949”](https://www.heritage.nf.ca/articles/politics/commission-government.php).

## Produced evidence

- Immutable master: `docs/assets/006_independence_wave/gzx_newfoundland_portrait_source_research_2026_08_03/source_masters/GZX_william_r_howley_1937.jpg` (609x800 RGB, SHA-256 `3a806245b589fa14c1010d0be88dee565f6498f8cf97b4685f89bd0de78aaf49`).
- Exact head-and-shoulders crop: `source_crops/GZX_william_r_howley_1937_head_shoulders.png` (514x704 RGB, SHA-256 `56781ee7fab4c00b81371c2fd21bf719fb4980701320907da6184e68d87db69d`).
- Crop JSON equality proof: `crop_metadata/GZX_william_r_howley_1937_head_shoulders.json`, `decoded_pixels_equal=true`, half-open `[52, 54, 566, 758]`.
- Source-locked HOI4 repaint: `repaints_raw/GZX_william_r_howley_hoi4_repaint_v1.png` (1071x1468 RGB, SHA-256 `8ef9ef3a0fd212a93afe5261bde29db2bc0e287f02de94c7271bf359d7f433db`).
- Flat original-size shelf copy: `docs/assets/006_independence_wave/portraits_generated_png/GZX_william_r_howley_identity_preserve.png` (byte-identical to raw repaint; reference-only).
- Durable ComfyUI pair: `docs/assets/portraits/006_independence_wave/portrait_GZX_william_r_howley.png` and matching `portrait_GZX_william_r_howley.txt`; proposed basename, `comfyui_replacement_pending`, no runtime reference.
- Deterministic candidate: `repaints_processed/portrait_GZX_william_r_howley_156x210_candidate.png` (156x210 RGBA, SHA-256 `60fc1018d54b24b818994e0cd2eaff82b3ac175e1406944df0139be7316a3100`).
- Full-chain native/4x review: `review/GZX_william_r_howley_source_raw_candidate_references_4x.png`.
- Candidate comparison contact sheet: `review/GZX_newfoundland_portrait_candidates_contact_sheet.png`.
- Generation record and prompt: `prompts/GZX_william_r_howley_identity_preserve_imagegen.md`.
- Processing metadata: `processing_metadata/portrait_GZX_william_r_howley_156x210.json`.

## Alternatives and rejection evidence

- David Murray Anderson (1934) is a five-person Government House group photo; selecting him requires a group crop and the image is less specific to a Newfoundland civic office.
- Richard Squires (1921 LOC) has the clearest public-domain/“no known restrictions” basis but is fifteen years pre-baseline and does not depict the 1936 Commission office.
- Frederick C. Alderdice (1927 book portrait) is public-domain but nine years pre-baseline and lower-detail.

The contact sheet retains all three as comparison evidence; none is a substitute for Howley.

## Parent actions required

1. Decide whether the NPG/Commons rights warning is acceptable for the target distribution jurisdiction.
2. Assign a unique GZX character key and exact runtime basename if the portrait is admitted.
3. Have an independent reviewer compare source, exact crop, raw repaint, processed candidate, and vanilla leader references at native and 4x nearest-neighbour scale.
4. Record separate likeness, style, and provenance verdicts and reviewer/date.
5. If all gates pass, convert the approved 156x210 PNG with the repository converter, validate the DDS, confirm the durable ComfyUI pair uses the exact final runtime basename (rename both files together if needed), and wire `.gfx` in the parent-owned scope.

## Scope confirmation

No event, country, character, localisation, `.gfx`, gameplay, or spreadsheet files were edited. No DDS was created because the real-person portrait gate requires independent PASS and the rights warning remains unresolved.
