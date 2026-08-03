# IW-030 JovanoviÄ‡ Znaci 8889 repaint-processing handoff

Date: 2026-08-03

Scope owner: sourced visual portrait asset worker.

## Outcome

Processed the already researched grounded Montenegro source only: `source_masters/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942.jpg`. The unchanged 2083x1380 source and exact crop `[1040,500,1490,1200]` were retained. A source-locked ImageGen edit produced a 1080x1456 RGB HOI4-style repaint, and a deterministic Pillow cover-crop/Lanczos export produced a 156x210 RGBA candidate. No advisor art, DDS, `.gfx`, character, history, event, localisation, readiness, attestation, or gameplay files were edited.

## Changed or added evidence

- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/repaints_raw/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_hoi4_repaint_v1.png` — raw ImageGen repaint, 1080x1456 RGB, SHA-256 `e3e2b2367dddc071b8e5d706a1297add703bf8b528f3510b9e6fbb0dab0c4696`.
- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/prompts/mnt_blazo_jovanovic_znaci_8889_hoi4_repaint_v1.txt` — exact source-locked edit prompt, SHA-256 `0feef49d07e98f836e40d1501f7d87e46dac08a2329e7d9d258a27b1517772f1`.
- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/processed_candidates/portrait_MNT_blazo_jovanovic_znaci_8889_156x210_candidate.png` — deterministic candidate, 156x210 RGBA, SHA-256 `ad02d6e2826bbae21760cd937a33d740d8405a231610553e86d36228608795eb`.
- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/processed_candidates/portrait_MNT_blazo_jovanovic_znaci_8889_156x210_candidate.json` — crop/resize command, source linkage, role references, dimensions, and hashes.
- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/review/mnt_blazo_jovanovic_znaci_8889_review_native_2026_08_03.png` — native comparison sheet.
- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/review/mnt_blazo_jovanovic_znaci_8889_review_4x_nearest_2026_08_03.png` — 4x nearest-neighbour comparison sheet.
- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/audit/mnt_blazo_jovanovic_znaci_8889_independent_review_2026_08_03.md` — independent parent review record.
- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/manifest.md` — source/provenance, status, review, and runtime-boundary addendum.
- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/gfx_handoff.md` — parent-owned sprite handoff addendum; no DDS path assigned.
- `docs/assets/006_independence_wave/portraits_generated_png/portrait_MNT_blazo_jovanovic_znaci_8889_hoi4_master.png` — original-size shelf copy, 1080x1456 RGB, same SHA-256 as raw repaint; reference-only.
- `docs/assets/006_independence_wave/portraits_generated_png/MANIFEST.md`, `PRE_RESIZE_MANIFEST.md`, and `README.md` — shelf inventory and evidence-only status updated to 81 masters.

The unchanged source and crop already present in the workspace remain authoritative:

- Source master SHA-256 `919393b924cee9c6de3d1e1fd4e864b4ffed387a3fe60fd52c43bc58b6d682a4`.
- Exact crop SHA-256 `e96c730d6d82702ea2937c1ff3bfa46b9d998921784aae2bf5be435a336cd737`.
- Crop equality proof: `crop_metadata/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942_crop_v2.json`, `decoded_pixels_equal=true`.

## Independent review and gate state

Parent agent `/root` independently reviewed the native and 4x sheets:

- likeness: `PASS_visual_identity`
- HOI4 style: `PASS_hoi4_leader_style`
- provenance/rights: `NEEDS_USER_REVIEW` due to the Commons/Znaci creator-versus-unknown-photographer discrepancy and the unresolved `PD-Yugoslavia` acceptance.

The candidate is therefore `needs_user_review`, not complete. No DDS conversion or runtime admission is authorized by this handoff. Existing durable ComfyUI pair `docs/assets/portraits/006_independence_wave/portrait_MNT_blazo_jovanovic.png` plus `.txt` remains tied to the established character basename; no new runtime basename is introduced for this source variant.

## Parent-owned promotion safety

Safe for a later parent-owned runtime promotion only after the remaining provenance/rights review and complete MNT roster admission pass. If admitted, the parent must preserve the exact stable `MNT_blazo_jovanovic` sprite/texture contract or assign and document a new stable DDS basename, convert only the independently reviewed 156x210 PNG with the repository converter, and keep the raw source, crop proof, review sheets, and manifest facts. Until then, the shelf copy and evidence candidate must remain non-runtime.

## Commit boundary

The scoped commit includes only the IW-030 JovanoviÄ‡ Znaci 8889 evidence, portrait-shelf inventory updates, and this handoff. Unrelated worktree edits from other agents were left untouched.
