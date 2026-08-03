# IW-030 Jovanović Znaci 8889 portrait review

Review package date: 2026-08-03.

## Evidence compared

- Unchanged archival master: `source_masters/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942.jpg` (2083x1380, SHA-256 `919393b924cee9c6de3d1e1fd4e864b4ffed387a3fe60fd52c43bc58b6d682a4`).
- Exact identity crop: `source_crops/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942_head_shoulders_v2.png` (450x700, crop `[1040,500,1490,1200]`, SHA-256 `e96c730d6d82702ea2937c1ff3bfa46b9d998921784aae2bf5be435a336cd737`, equality proof `crop_metadata/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942_crop_v2.json`).
- Raw source-locked ImageGen repaint: `repaints_raw/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_hoi4_repaint_v1.png` (1080x1456 RGB, SHA-256 `e3e2b2367dddc071b8e5d706a1297add703bf8b528f3510b9e6fbb0dab0c4696`).
- Deterministic candidate: `processed_candidates/portrait_MNT_blazo_jovanovic_znaci_8889_156x210_candidate.png` (156x210 RGBA, SHA-256 `ad02d6e2826bbae21760cd937a33d740d8405a231610553e86d36228608795eb`; metadata is adjacent JSON).
- Role-specific style references: canonical leader family `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png` and `afg_mohammed_zahir_shah.png` (both 156x210).
- Native comparison sheet: `review/mnt_blazo_jovanovic_znaci_8889_review_native_2026_08_03.png`.
- 4x nearest-neighbour comparison sheet: `review/mnt_blazo_jovanovic_znaci_8889_review_4x_nearest_2026_08_03.png`.

## Gate records

| Gate | Status | Evidence / note |
| --- | --- | --- |
| Source identity and crop linkage | `PASS_source_locked` | Commons/Znaci record names Jovanović as the lower-row moustached subject; exact decoded-pixel crop equality is recorded in the v2 JSON. |
| Likeness / identity preservation | `NEEDS_USER_REVIEW` | Producer pre-screen sees the same moustache, cap, brow, nose, eye spacing, jaw, age, expression, and head angle in the raw repaint and candidate. This is not an independent approval. |
| HOI4 painted leader style | `NEEDS_USER_REVIEW` | Producer pre-screen finds restrained painted brushwork, dark neutral vignette, controlled contrast, and readable 156x210 silhouette against the canonical leader references. This is not an independent approval. |
| Provenance / source rights | `NEEDS_USER_REVIEW` | Commons marks the Savo Orović/Znaci item `PD-Yugoslavia`; the package retains the creator/unknown-photographer metadata discrepancy and requires parent rights acceptance. |
| Technical candidate | `PASS_deterministic_processing` | RGB cover crop `[0,1,1080,1455]`, Lanczos resize, RGBA PNG export; dimensions and hashes are in the adjacent processing JSON. |
| DDS/runtime admission | `BLOCKED_pending_independent_review_and_rights` | No DDS was converted and no `.gfx`, character, history, event, localisation, or gameplay file was edited. |

## Independent reviewer record

The producer is not authorized to approve the likeness or style gates. Parent agent `/root` (or another named reviewer) must inspect the native and 4x sheets and record a separate verdict for likeness, HOI4 style, and provenance/rights before any DDS conversion or runtime promotion. Until that record is added, this portrait remains `needs_user_review` and is safe only as evidence for a later parent-owned promotion decision.

Reviewer: `/root`

Review date: `2026-08-03`

Independent likeness verdict: `PASS_visual_identity`

Independent style verdict: `PASS_hoi4_leader_style`

Independent provenance/rights verdict: `NEEDS_USER_REVIEW`

The native and 4x sheets preserve the subject's moustache, cap, brow, nose, eye spacing, jaw, age, expression, and head angle while translating the source into the restrained painted leader treatment used by the supplied vanilla references. The image remains evidence-only because the source-rights/creator metadata discrepancy is not a parent-authorized admission decision.

## Runtime boundary

The original-size shelf copy `docs/assets/006_independence_wave/portraits_generated_png/portrait_MNT_blazo_jovanovic_znaci_8889_hoi4_master.png` is reference-only. It is not a 156x210 portrait, DDS, or runtime texture. The existing durable ComfyUI pair `docs/assets/portraits/006_independence_wave/portrait_MNT_blazo_jovanovic.png` and `.txt` remains tied to the existing character basename; no new durable pair or new runtime basename is introduced by this source variant while admission is pending.
