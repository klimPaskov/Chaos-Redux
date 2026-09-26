# Event 021 missing decision-icon master candidates

Date: 2026-09-25.

Disposition: `implemented`; both generated candidates were individually parent-reviewed and promoted as dated replacements on 2026-09-25. The absent original source PNGs remain unavailable and are not claimed as recovered.

## Scope and authority

The user's 2026-09-25 request explicitly authorized auditing and repairing Event 021 visual assets and specifically requested two versioned candidate source-master packages because their original ImageGen PNGs are absent. The accepted task boundary was the isolated root `docs/assets/021_random_civil_war/recovery_candidates_2026-09-25/icons/` and this handoff file.

## Candidate crosswalk

| Candidate | Decision | Sprite | Required runtime DDS path | Candidate DDS path | Status |
| --- | --- | --- | --- | --- | --- |
| `event021_reconstruct_administration_v01` | `event021_reconstruct_administration` | `GFX_decision_event021_reconstruction` | `gfx/interface/decisions/021_random_civil_war/decision_021_reconstruction.dds` | `docs/assets/021_random_civil_war/recovery_candidates_2026-09-25/icons/decision_021_reconstruct_administration_v01/candidate_dds/gfx/interface/decisions/021_random_civil_war/decision_021_reconstruction.dds` | `promoted` |
| `event021_open_relief_corridor_v01` | `event021_open_relief_corridor` | `GFX_decision_event021_relief_corridor` | `gfx/interface/decisions/021_random_civil_war/decision_021_relief_corridor.dds` | `docs/assets/021_random_civil_war/recovery_candidates_2026-09-25/icons/decision_021_open_relief_corridor_v01/candidate_dds/gfx/interface/decisions/021_random_civil_war/decision_021_relief_corridor.dds` | `promoted` |

## Production and evidence

The canonical Vanilla reference contact sheet at `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/decisions/contact_sheet.png` was inspected before individual references. Its 15 decision references are predominantly `33x32`; the explicitly provided active candidate surfaces are `32x32`. The individual Vanilla references `decision_bol_reintegrate_acre_state.png`, `decision_generic_disband_irregulars.png`, and `decision_border_war.png` were inspected from that same canonical folder.

The current decoded runtime reference PNGs were inspected at `docs/assets/021_random_civil_war/validation/full_runtime_audit/decision_021_reconstruction.png` and `decision_021_relief_corridor.png`. Their SHA-256 values match the corresponding active processed PNGs exactly: reconstruction `F073B2707435AB9C8E23A9B40E5482BB3420BCE4E4CD6615BA8F2D85BE99E9B5`; relief corridor `EC484C981A7FCA001EA771FE9A9FD82C43E5CC99BB78F205A68D91A50B75B68`.

Each subject received a separate built-in ImageGen generation through `image_gen__imagegen`, with its current decoded runtime image as a motif-only reference and the canonical Vanilla contact sheet as a style-only reference. Both prompts requested true RGBA transparency in the initial call. Each `1254x1254` source master has zero-alpha corners and nonzero alpha; the retained candidate source is byte-identical to the tool output. No background removal, chroma key, opaque canvas, or fallback was used.

Processing preserved alpha using premultiplied-alpha Lanczos downsampling from the original square source to `28x28`, placed at `(2,2)` in a transparent `32x32` canvas. The original source remains untouched. Each 32x32 PNG was converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` to its exact target texture basename under the versioned candidate folder.

Strict DDS checks passed for both candidates: `DDS ` magic, 124-byte header, one level, `32x32` dimensions, expected 32-bit BGRA masks, zero mipmaps, texture caps, and exact `4224`-byte length. Decoded DDS pixels are exactly equal to the processed PNG pixels. Source, processed PNG, and DDS round-trip edge reviews were inspected on both light and dark checkerboards. The combined contact sheet includes each active runtime reference, source master over light and dark checkerboards, smooth processed preview, and processed/DDS round-trips over light and dark checkerboards: `docs/assets/021_random_civil_war/recovery_candidates_2026-09-25/icons/review/event021_missing_decision_icon_masters_v01_contact_sheet.png` (`2144x696`, SHA-256 `59302B40CFF28BC1740AE94908AE1A5ACEe27A995BCE165C118178505CBA96BE`). No clipped edges, matte, halo, coloured spill, fake checkerboard, or unintended transparent hole was observed.

The reconstruction candidate reads as a compact civic entrance with visible scaffold repair. The relief-corridor candidate reads as a marked civilian aid crate beside a raised striped passage barrier; it contains no weapons or armed-support motif.

The candidate manifest is `docs/assets/021_random_civil_war/recovery_candidates_2026-09-25/icons/manifest.md`. Exact prompts and source-mode notes are in each package's `prompts/` folder. Source, processed PNG, candidate DDS, decoded round-trip, and review paths and hashes are enumerated in the manifest.

Files created under the candidate root:

- Reconstruction source: `decision_021_reconstruct_administration_v01/source_png/decisions/decision_021_reconstruct_administration.png`.
- Reconstruction prompt: `decision_021_reconstruct_administration_v01/prompts/decision_021_reconstruct_administration_v01.md`.
- Reconstruction processed preview: `decision_021_reconstruct_administration_v01/processed_png/decisions/decision_021_reconstruct_administration.png`.
- Reconstruction candidate DDS: `decision_021_reconstruct_administration_v01/candidate_dds/gfx/interface/decisions/021_random_civil_war/decision_021_reconstruction.dds`.
- Reconstruction DDS readback: `decision_021_reconstruct_administration_v01/dds_roundtrip_png/decision_021_reconstruction_roundtrip.png`.
- Relief-corridor source: `decision_021_open_relief_corridor_v01/source_png/decisions/decision_021_open_relief_corridor.png`.
- Relief-corridor prompt: `decision_021_open_relief_corridor_v01/prompts/decision_021_open_relief_corridor_v01.md`.
- Relief-corridor processed preview: `decision_021_open_relief_corridor_v01/processed_png/decisions/decision_021_open_relief_corridor.png`.
- Relief-corridor candidate DDS: `decision_021_open_relief_corridor_v01/candidate_dds/gfx/interface/decisions/021_random_civil_war/decision_021_relief_corridor.dds`.
- Relief-corridor DDS readback: `decision_021_open_relief_corridor_v01/dds_roundtrip_png/decision_021_relief_corridor_roundtrip.png`.
- Each versioned package's `review/` folder contains source-edge, processed-PNG, and DDS-readback checkerboard views; the combined review sheet is `review/event021_missing_decision_icon_masters_v01_contact_sheet.png`.
- Candidate manifest: `manifest.md`.
- Separate parent handoff: `docs/plans/021_random_civil_war_plans/subagent_handoffs/event021_missing_icon_masters_candidate_2026-09-25.md`.

The previous reconstruction DDS (`E2473D4F491153F3F23C967E887616A9C91C87BF74D8145EE3919EDF578AF46B`) and relief-corridor DDS (`E908A55EF7B10B510BA3737F9D8C828E914CE408F1BD93D2E85B7B137EC44CB3`) were backed up under `docs/assets/021_random_civil_war/validation/pre_generated_replacement_promotion_2026-09-25/` before replacement. The active DDS files now match the candidate hashes exactly.

## Parent review and promotion

The parent opened both source masters, processed previews, and DDS round-trips individually, in addition to the retained light/dark checkerboard edge reviews. The civic reconstruction entrance and the civilian-aid crate beside the raised striped passage barrier are legible at 32x32, preserve genuine alpha, and remain distinct from armed-support imagery.

The parent copied byte-identical source and processed PNGs to separately named dated paths in the canonical `source_png/` and `processed_png/` trees and copied each standard-converter DDS to the exact existing runtime path. Independent header checks confirmed `32x32`, one-level 32-bit BGRA, expected masks and pitch, texture caps, and exact `4224`-byte lengths. Active DDS SHA-256 values are reconstruction `276937666187a8dfc16911b4e303b7aecc690954ba3d3e09f72ab12a07346ae5` and relief corridor `e519fca3a44f5139680de6694ee4111e33b00a7ac915c8b54fc2fc5a612c3207`.

The permanent source, processed, and runtime paths and hashes are listed in `docs/events/021_random_civil_war/owned_asset_crosswalk.md`. Actual in-game decision-list rendering remains a user-owned test.
