# Event 006 scene-art style repair manifest

- Status: all five requested assets are complete, installed at their existing runtime DDS paths, and independently reviewed by the parent on 2026-10-06.
- Scope: one Event006 report image and four already-registered decision-category pictures received a style repair while keeping their scene identities, sprite names, consumers, and dimensions.
- Source mode: native ImageGen edits of existing fictional alternate-history art; no image is claimed to be a real historical photograph.
- Acceptance basis: the parent authorized the five listed repairs and explicitly accepted the existing iw043/iw058 picture surfaces despite their attached state-puzzle scripted GUI, with the `picture` registrations and GUI attachments preserved.
- Reference boundary: only the canonical report and decision-category-picture families under `.agents/skills/chaos-redux-event-assets/assets/gfx_references/` were inspected; the category reference was used for style only and no reference pixels were reused.

## Runtime coverage

| Sprite | Runtime DDS and size | Registration and consumer | Source, preview, and final hashes |
|---|---|---|---|
| `GFX_report_event_006_country_opening` | `gfx/event_pictures/006_independence_wave/report_event_006_country_opening.dds`, 210x176 | `interface/006_independence_wave_small_assets.gfx`; report-event image | ImageGen source `source_png/report_event_006_country_opening_imagegen_source.png`, SHA-256 `5a64ecdd0c5d0ca9891da9a394e09aa8e017c48a4d95b31544ca0f168557f424`; preview `processed_png/report_event_006_country_opening.png`, SHA-256 `9d74ad1bce21446de0a5a8c07823b3e7e93a98d03a9d7f80aacc0aaf24213feb`; DDS SHA-256 `0cc433e3d93d96ce1197943769d813bfbb8607dc4dddb0c035e3a63a2025c844` |
| `GFX_decision_cat_picture_independence_wave_iw043_middle_volga_congress` | `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw043_middle_volga_congress.dds`, 114x101 | `interface/visual_consistency_repair.gfx`; `picture` entry in `common/decisions/categories/006_independence_wave_categories.txt` | ImageGen source `source_png/decision_cat_picture_independence_wave_iw043_middle_volga_congress_imagegen_source.png`, SHA-256 `4fb921ce95477d719528afcbb3f6ff6e9e3fdc5377a6fa1c920f8c91fb525788`; preview `processed_png/decision_cat_picture_independence_wave_iw043_middle_volga_congress.png`, SHA-256 `dc25a0aa0c19ad8ccbdfebe047234edbf2f8ed87989c207b15c09905416ebdeb`; DDS SHA-256 `446ac5e127b3a5b05ddad4c9aa09acb3a27ace1777189985d30318d0176e41c2` |
| `GFX_decision_cat_picture_independence_wave_iw058_council_of_communities` | `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw058_council_of_communities.dds`, 114x101 | `interface/visual_consistency_repair.gfx`; `picture` entry in `common/decisions/categories/006_independence_wave_categories.txt` | ImageGen source `source_png/decision_cat_picture_independence_wave_iw058_council_of_communities_imagegen_source.png`, SHA-256 `6f9f4edaf04263ab2ad51d5cbf2bbaec34cdbb6d10aa99e39ec2b11b37cf8c03`; preview `processed_png/decision_cat_picture_independence_wave_iw058_council_of_communities.png`, SHA-256 `8b8857b8de87695d150b122e94791a6b6e0955fadea9f2cdaeedeb0ae3312605`; DDS SHA-256 `796773a8bfe85fdbb711b2d8f44b6b3a545195b208373574761a45549ae87158` |
| `GFX_decision_cat_picture_independence_wave_iw093_asante_compact` | `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw093_asante_compact.dds`, 114x101 | `interface/visual_consistency_repair.gfx`; `picture` entry in `common/decisions/categories/006_independence_wave_categories.txt` | Selected ImageGen source `source_png/decision_cat_picture_independence_wave_iw093_asante_compact_imagegen_source_refined.png`, SHA-256 `28db8fd0f85900accfb29732976754b20ed2baf58b2c1d6a511eb9c65f0aa503`; preview `processed_png/decision_cat_picture_independence_wave_iw093_asante_compact.png`, SHA-256 `a4a0df91e34e8bea4a78dafbcb499066fdc606d0908821f7c900ca24d731162b`; DDS SHA-256 `3030b17ad1333a2f68951f3fd93aa76528e9dc92fd49848f16dcfe6a722d3919` |
| `GFX_decision_cat_picture_independence_wave_iw098_sokoto_compact` | `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw098_sokoto_compact.dds`, 114x101 | `interface/visual_consistency_repair.gfx`; `picture` entry in `common/decisions/categories/006_independence_wave_categories.txt` | ImageGen source `source_png/decision_cat_picture_independence_wave_iw098_sokoto_compact_imagegen_source.png`, SHA-256 `c6b550601aa1b331a5ce0074716f1738c59976c30db2db710e7aafa1c4e93f0b`; preview `processed_png/decision_cat_picture_independence_wave_iw098_sokoto_compact.png`, SHA-256 `05a6f2d0325074c7af15a1d1bcd233d2ea9fee0b1cdf75f45b415843b5c89059`; DDS SHA-256 `7299ea5ee237e5398fc423e21dff01b78b00291e88b03aece0351db6b9d143dd` |

## Generation and processing lineage

- The report source was edited from the existing selected Event006 opening scene and uses the canonical report reference only for broad archival photographic tone; it retains the gathering, doorway, officials, listeners, blank sheet, and period security group without claiming a real photograph.
- The report source was processed with the default settings of `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`, which created the 210x176 tilted report card and transparent corners.
- The report output has 7.93% zero-alpha pixels, and its complete alpha plane is pixel-identical to the existing `report_event_006_asset_001_wave_summary` mask, as well as the inspected Event006 asset002, asset003, and form03 masks.
- Each category image was edited from its existing runtime picture using the canonical vanilla category picture as a style reference only; the outputs keep full opaque backgrounds, warm sepia treatment, a thin paper edge, and a soft vignette.
- Category previews were fitted to 114x101 with Lanczos resampling and a restrained contrast adjustment; the interior IW058 and IW093 scenes received gentle shadow lifts with gamma values 0.84 and 0.92 respectively, while IW043 and IW098 used gamma 1.0.
- IW093 candidate001 added two unexplained crossed foreground rods; its source SHA-256 is `3cf79aeeea5e14f549bb9573beced4ceb0248e646c1115bd3f73decba16d97c1`, and a focused ImageGen edit created selected candidate002 with SHA-256 `28db8fd0f85900accfb29732976754b20ed2baf58b2c1d6a511eb9c65f0aa503` by removing them and restoring the tiled courtyard floor.
- The retained candidate lineage and parent-selected final are shown in `contact_sheets/iw093_candidate_lineage.png`.
- ImageGen prompts and generated output paths are recorded in `prompts/`; the untouched pre-edit runtime DDS copies and their PNG decodes are retained in `snapshots/` and `source_png/`.

## Pre-edit runtime snapshots

| Original runtime DDS | Captured pre-edit SHA-256 |
|---|---|
| `gfx/event_pictures/006_independence_wave/report_event_006_country_opening.dds` | `91b565fb48d4b880dc1af5303b2f26e92a14233dbb26bbb35e900cd2b223e351` |
| `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw043_middle_volga_congress.dds` | `49efe1aaba7635e4c3ed5c154e8ad09d7f1991b2dd8417e5722204e5abdbb39f` |
| `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw058_council_of_communities.dds` | `7278f290818b263c1eb012cb978366db653f1458c755c22b86085700e7b7afc4` |
| `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw093_asante_compact.dds` | `c5f5a82dd5a98a9cb7d29eb496d472a8536bcaa3ca54ecb1b12b4664a9140db1` |
| `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_independence_wave_iw098_sokoto_compact.dds` | `71cff81ea00608b3ec1fd8717198b92b26fe33ed069132ac3c966bfb31976b11` |

## DDS and visual review evidence

- All five outputs were converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` to one-level 32-bit BGRA DDS files at the registered native dimensions.
- DDS round-trip decoding matched every processed PNG pixel-for-pixel; the report DDS is 147,968 bytes and each 114x101 category DDS is 46,184 bytes.
- The report DDS preserved alpha from 0 through 255 and the same 7.93% zero-alpha card mask; all four category DDS files are fully opaque with alpha 255 throughout.
- The native before/source/preview/DDS comparison and alpha view are in `contact_sheets/event006_scenes_native_review.png`.
- The smooth 4x edge and alpha-mask inspection is in `contact_sheets/event006_scenes_4x_edges.png`.
- The parent independently reviewed those sheets and approved the five existing runtime replacements on 2026-10-06.

## Scope and completion

- The five approved DDS files were installed at the same registered texture paths, after confirming each runtime file still matched its captured pre-edit SHA-256.
- Sprite names, `.gfx` definitions, category `picture` entries, and the iw043/iw058 `scripted_gui = independence_wave_formable_state_puzzle_scripted_gui` attachments remain unchanged.
- No GFX, GUI, gameplay, localisation, flag, portrait, event, focus, decision, history, or spreadsheet source was edited.
- No background-removal fallback, substitute scene, or simplification was used.
- No live-game render was performed; the parent owns final wiring review and the user owns live-game validation.
