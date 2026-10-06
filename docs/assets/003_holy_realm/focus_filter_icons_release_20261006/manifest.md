# Event 003 Holy Realm focus-search filter icon package

Status: Complete; all twelve transparent icon assets were accepted by the parent after review of the whole-package native and enlarged contact sheets on 2026-10-06.

The package covers only the twelve parent-registered Event003 Holy Realm focus-search filter sprites.

Each icon is original, fictional gameplay-symbolic artwork generated with the official built-in ImageGen tool and genuine transparent background; no real religious seal, state emblem, copied vanilla icon, or fallback background removal was used.

Each source PNG is preserved separately from its 27x27 processed PNG, docs-folder DDS candidate, and installed runtime DDS.

## Consumer and reference

The consumer is the focus-search toolbar at 27x27 with unused canvas transparent; each sprite uses one static frame.

The exact vanilla family, source dimensions, alpha behavior, offline wiki citation, and source lookup evidence are recorded in [reference_evidence.md](notes/reference_evidence.md).

The canonical general national-focus reference contact sheet and the exact installed vanilla filter reference contact sheets are review material only; none of their artwork appears in the generated final assets.

The parent-provided `interface/003_holy_realm_focus_filter_icons.gfx` remains unchanged and its twelve existing sprite-to-path pairs were verified against the installed DDS paths.

## Processing and validation

Every original ImageGen PNG has decoded RGBA alpha extrema 0..255, transparent outer corners, and a nonzero-alpha subject bbox inset from the source canvas edge.

For each source, the exact nonzero-alpha bounding box was cropped without deleting pixels inside it; the crop was aspect-fitted within 23x23 using Pillow Image.Resampling.LANCZOS on premultiplied RGBA, then centered on a transparent 27x27 canvas.

Every processed PNG and candidate/runtime DDS retains alpha extrema 0..255; all twelve DDS files decode as exact 27x27 RGBA pixel matches to their processed PNG, use a strict 128-byte one-level uncompressed BGRA header, are 3044 bytes, and declare zero mipmaps.

Every runtime DDS SHA-256 equals the accepted docs-folder candidate SHA-256, and each runtime sprite name/path pair matches the existing parent-owned GFX definition.

The per-asset crop boxes, source and target alpha bounds, resampling dimensions and positions, source/prompt/PNG/DDS hashes, decoded dimensions, GFX path checks, and candidate/runtime hash equality are in [processing_metadata.json](notes/processing_metadata.json).

## Assets

| Filter ID / sprite | Intended symbol | ImageGen source and exact prompt | Processed PNG | Docs DDS candidate | Runtime DDS and SHA-256 equality |
| --- | --- | --- | --- | --- | --- |
| `FOCUS_FILTER_THR_PEACE` / `GFX_FOCUS_FILTER_THR_PEACE` | Olive branch for peace. | `source_png/filter_thr_peace_source_v1.png` (SHA-256 `62009a221b6f70f06f283b30d4b29496f5ef2b5f1f73b6ed4433422143b4a52a`); `prompts/filter_thr_peace_prompt.txt` | `processed_png/filter_thr_peace_27x27.png` (SHA-256 `ec3d8f7e287948b7156505548df8bf417eb934f62f0a6bf5cc58acfe7bd12af0`) | `dds/filter_thr_peace.dds` (SHA-256 `d779157595d6fa0277ae457b0dbf1fae0927d567a7e68bb3720ecd3ed6860f85`) | `gfx/interface/focusview/filter/003_holy_realm/filter_thr_peace.dds` (same SHA-256: `d779157595d6fa0277ae457b0dbf1fae0927d567a7e68bb3720ecd3ed6860f85`) |
| `FOCUS_FILTER_THR_FINAL_SILENCE_PRESSURE` / `GFX_FOCUS_FILTER_THR_FINAL_SILENCE_PRESSURE` | Missile warhead with a compact blast plume for nuclear warning and pressure. | `source_png/filter_thr_final_silence_pressure_source_v1.png` (SHA-256 `409ec9af579abf7e80fee26f7f2ed94c3e4cb6777dc74c96a91b4a320cb90e73`); `prompts/filter_thr_final_silence_pressure_prompt.txt` | `processed_png/filter_thr_final_silence_pressure_27x27.png` (SHA-256 `3240488c9a4660ffdf1f79e669341033118bbeaa7e70e13c073e8c0f927c2846`) | `dds/filter_thr_final_silence_pressure.dds` (SHA-256 `c17d0922d756430a073d2602945da1c243bffe2f66e920b77685b559ec6534bd`) | `gfx/interface/focusview/filter/003_holy_realm/filter_thr_final_silence_pressure.dds` (same SHA-256: `c17d0922d756430a073d2602945da1c243bffe2f66e920b77685b559ec6534bd`) |
| `FOCUS_FILTER_THR_MANDALA_INTEGRATION` / `GFX_FOCUS_FILTER_THR_MANDALA_INTEGRATION` | Three territory shapes linked through a central junction. | `source_png/filter_thr_mandala_integration_source_v1.png` (SHA-256 `d2a33d894ae4d5ab6f46f732276beeb4adfb4f536b3f102204923aa1dea2955b`); `prompts/filter_thr_mandala_integration_prompt.txt` | `processed_png/filter_thr_mandala_integration_27x27.png` (SHA-256 `1f026babc90730d3cef5acac0ac6390928ef81d97ec87d577a0db96ed2675d3e`) | `dds/filter_thr_mandala_integration.dds` (SHA-256 `305df146c88989b0ab68e56b40e0e527d454251243b7a0ae58c45cca4357f479`) | `gfx/interface/focusview/filter/003_holy_realm/filter_thr_mandala_integration.dds` (same SHA-256: `305df146c88989b0ab68e56b40e0e527d454251243b7a0ae58c45cca4357f479`) |
| `FOCUS_FILTER_HOLY_REALM_MEDITATION` / `GFX_FOCUS_FILTER_HOLY_REALM_MEDITATION` | Seated figure in quiet meditation. | `source_png/filter_holy_realm_meditation_source_v1.png` (SHA-256 `1a655e00634fae13c2643da22de845b95bc43c2b66ab5b47fcb1f81330b24f49`); `prompts/filter_holy_realm_meditation_prompt.txt` | `processed_png/filter_holy_realm_meditation_27x27.png` (SHA-256 `f00a87b70e7e946683aa3f591824fd9fa2d2c278f063fcb0ae9173991e23c3e8`) | `dds/filter_holy_realm_meditation.dds` (SHA-256 `384d40e1a853a311161bd4eaccae7cb0900b1151ca456bbb54d63278533fa398`) | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_meditation.dds` (same SHA-256: `384d40e1a853a311161bd4eaccae7cb0900b1151ca456bbb54d63278533fa398`) |
| `FOCUS_FILTER_HOLY_REALM_SANCTUARY` / `GFX_FOCUS_FILTER_HOLY_REALM_SANCTUARY` | Mountain peak sheltering a small stone arch. | `source_png/filter_holy_realm_sanctuary_source_v1.png` (SHA-256 `5e2f248d9aa34298982565406b98506dd48ea689da77f0b45e1360a5a043e5e1`); `prompts/filter_holy_realm_sanctuary_prompt.txt` | `processed_png/filter_holy_realm_sanctuary_27x27.png` (SHA-256 `dce98959fa4bea9111affd48efa045ae230261594bd87455bc867c1f5dc68fae`) | `dds/filter_holy_realm_sanctuary.dds` (SHA-256 `6f2b6c8deaa92d1bf1b1ed7bc50bbcdb223b256a3f81da51faadb45f208730ad`) | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_sanctuary.dds` (same SHA-256: `6f2b6c8deaa92d1bf1b1ed7bc50bbcdb223b256a3f81da51faadb45f208730ad`) |
| `FOCUS_FILTER_HOLY_REALM_ANTI_CHAOS` / `GFX_FOCUS_FILTER_HOLY_REALM_ANTI_CHAOS` | Order shield with a straight pillar and balanced bars. | `source_png/filter_holy_realm_anti_chaos_source_v1.png` (SHA-256 `d27a0ce96d0addd2e68f5bbdf6ac243b4bd68839e10b266db975e6668e60388c`); `prompts/filter_holy_realm_anti_chaos_prompt.txt` | `processed_png/filter_holy_realm_anti_chaos_27x27.png` (SHA-256 `73c087bc58b51efc1befda3d07546d32ed0fceae5e45b2dcedac6418cb530635`) | `dds/filter_holy_realm_anti_chaos.dds` (SHA-256 `e219a5e9618a7dac25d4f8c6d37e88f5fdcfa5336fa0dd68b946b3d03afea0a8`) | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_anti_chaos.dds` (same SHA-256: `e219a5e9618a7dac25d4f8c6d37e88f5fdcfa5336fa0dd68b946b3d03afea0a8`) |
| `FOCUS_FILTER_HOLY_REALM_BODHI` / `GFX_FOCUS_FILTER_HOLY_REALM_BODHI` | Oil lamp with a clear flame for understanding. | `source_png/filter_holy_realm_bodhi_source_v1.png` (SHA-256 `f6323fa2ff500ae79b924fc3353001815c0d829725b177df2c09ed2253f30db4`); `prompts/filter_holy_realm_bodhi_prompt.txt` | `processed_png/filter_holy_realm_bodhi_27x27.png` (SHA-256 `9014e35a74bb0a794a8816898bcdf4497d6cefa772e4fb6eca6153497da91979`) | `dds/filter_holy_realm_bodhi.dds` (SHA-256 `8752b1617eef3338950dd5d91dc0c5b1c118c7ffb695b7dee9ec5d2dcb2bcb37`) | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_bodhi.dds` (same SHA-256: `8752b1617eef3338950dd5d91dc0c5b1c118c7ffb695b7dee9ec5d2dcb2bcb37`) |
| `FOCUS_FILTER_HOLY_REALM_TEACHING` / `GFX_FOCUS_FILTER_HOLY_REALM_TEACHING` | Open blank book for teaching. | `source_png/filter_holy_realm_teaching_source_v1.png` (SHA-256 `9388358742c2b4ccd9670be76dedff49d13517233d3af7aafe327881ad9b6792`); `prompts/filter_holy_realm_teaching_prompt.txt` | `processed_png/filter_holy_realm_teaching_27x27.png` (SHA-256 `e1c965db3ad22818782e85dcb5d94e2e9bf6e6f3a0d491d3d96f0d314a9371a1`) | `dds/filter_holy_realm_teaching.dds` (SHA-256 `58730b846a770be8990b9408cf8dc3314ecff9c7211c2dd97e642bc669e852ff`) | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_teaching.dds` (same SHA-256: `58730b846a770be8990b9408cf8dc3314ecff9c7211c2dd97e642bc669e852ff`) |
| `FOCUS_FILTER_HOLY_REALM_GOVERNANCE` / `GFX_FOCUS_FILTER_HOLY_REALM_GOVERNANCE` | Three delegates seated in council behind a table. | `source_png/filter_holy_realm_governance_source_v1.png` (SHA-256 `9da5d10c2b9122c537b206f1b629b7a499a80a7b9e2fd992a479aa25872009a9`); `prompts/filter_holy_realm_governance_prompt.txt` | `processed_png/filter_holy_realm_governance_27x27.png` (SHA-256 `1ddb2d069bccd1febde6b9bfabac7fa996f6b32712884394878de6acf67212b3`) | `dds/filter_holy_realm_governance.dds` (SHA-256 `acb05f5cefb9789d4e1013ddeab0879b4e21907a98e98defc62a64d1891a68d5`) | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_governance.dds` (same SHA-256: `acb05f5cefb9789d4e1013ddeab0879b4e21907a98e98defc62a64d1891a68d5`) |
| `FOCUS_FILTER_HOLY_REALM_COMPACT` / `GFX_FOCUS_FILTER_HOLY_REALM_COMPACT` | Two parties clasping hands in agreement. | `source_png/filter_holy_realm_compact_source_v1.png` (SHA-256 `380e17a317baaf4aaea97798698cd68a1e750d443994919c76a98b4f580d36cc`); `prompts/filter_holy_realm_compact_prompt.txt` | `processed_png/filter_holy_realm_compact_27x27.png` (SHA-256 `18366792a7b4c5c0270f7c46c6f296d9ec03e0dc2efee4eff88720b66f1a3189`) | `dds/filter_holy_realm_compact.dds` (SHA-256 `b090b5550ad655c10a6a9b417ffd97b2de5b1df1e3a65e0b66f2983c7c5b46b8`) | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_compact.dds` (same SHA-256: `b090b5550ad655c10a6a9b417ffd97b2de5b1df1e3a65e0b66f2983c7c5b46b8`) |
| `FOCUS_FILTER_HOLY_REALM_NIRVANA` / `GFX_FOCUS_FILTER_HOLY_REALM_NIRVANA` | Hollow flame-wisp above calm ripples for quiet release. | `source_png/filter_holy_realm_nirvana_source_v1.png` (SHA-256 `654417cc937023dad7a29812744d5ed8205d75f83fd21c25678d7b3a3b4ac3d7`); `prompts/filter_holy_realm_nirvana_prompt.txt` | `processed_png/filter_holy_realm_nirvana_27x27.png` (SHA-256 `59c8e1dcfd5371f5a5c3009f93c337eb4948c65183e57e2e17ce59be73123826`) | `dds/filter_holy_realm_nirvana.dds` (SHA-256 `06c2cc3950703cac401c2e90d03eefa23830f5e99326a04fe393193a57e48e9f`) | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_nirvana.dds` (same SHA-256: `06c2cc3950703cac401c2e90d03eefa23830f5e99326a04fe393193a57e48e9f`) |
| `FOCUS_FILTER_HOLY_REALM_HIDDEN` / `GFX_FOCUS_FILTER_HOLY_REALM_HIDDEN` | Closed, tied scroll partly covered by a veil. | `source_png/filter_holy_realm_hidden_source_v1.png` (SHA-256 `5c8c21e846ac507158bdee72a9e1e44458788995cde1f7953ac665f7ff6a0d5a`); `prompts/filter_holy_realm_hidden_prompt.txt` | `processed_png/filter_holy_realm_hidden_27x27.png` (SHA-256 `da1b88a6074aa966bd15116d282c912eb53e0f38dafbb557b39f60764f89fd4f`) | `dds/filter_holy_realm_hidden.dds` (SHA-256 `54db2b587c6e6b458316be0459a9a2bf97c9b9ababd30149931239d1897ec2aa`) | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_hidden.dds` (same SHA-256: `54db2b587c6e6b458316be0459a9a2bf97c9b9ababd30149931239d1897ec2aa`) |

## Review sheets

The native-size PNG/DDS comparison is [focus_filters_native_27x27.png](contact_sheets/focus_filters_native_27x27.png).

The enlarged source-crop/processed-PNG/DDS comparison is [focus_filters_enlarged_4x_comparison.png](contact_sheets/focus_filters_enlarged_4x_comparison.png).

The exact vanilla filter reference contact sheets are [vanilla_filter_reference_sheet.png](contact_sheets/vanilla_filter_reference_sheet.png) and [vanilla_filter_reference_detail.png](contact_sheets/vanilla_filter_reference_detail.png).

The contact-sheet SHA-256 values are recorded in [contact_sheet_hashes.json](notes/contact_sheet_hashes.json).

## Status and handoff

All twelve asset rows are complete; parent visual acceptance and exact runtime-path installation are recorded in the metadata and handoff.

The asset package has no production blocker; no live-game session was run as part of this asset production task.


## Exact archive file list

All 57 files retained under this manifest's archive root:

- `contact_sheets/focus_filters_enlarged_4x_comparison.png`
- `contact_sheets/focus_filters_native_27x27.png`
- `contact_sheets/vanilla_filter_reference_detail.png`
- `contact_sheets/vanilla_filter_reference_sheet.png`
- `dds/filter_holy_realm_anti_chaos.dds`
- `dds/filter_holy_realm_bodhi.dds`
- `dds/filter_holy_realm_compact.dds`
- `dds/filter_holy_realm_governance.dds`
- `dds/filter_holy_realm_hidden.dds`
- `dds/filter_holy_realm_meditation.dds`
- `dds/filter_holy_realm_nirvana.dds`
- `dds/filter_holy_realm_sanctuary.dds`
- `dds/filter_holy_realm_teaching.dds`
- `dds/filter_thr_final_silence_pressure.dds`
- `dds/filter_thr_mandala_integration.dds`
- `dds/filter_thr_peace.dds`
- `gfx_handoff.md`
- `manifest.md`
- `notes/contact_sheet_hashes.json`
- `notes/processing_metadata.json`
- `notes/reference_evidence.md`
- `processed_png/filter_holy_realm_anti_chaos_27x27.png`
- `processed_png/filter_holy_realm_bodhi_27x27.png`
- `processed_png/filter_holy_realm_compact_27x27.png`
- `processed_png/filter_holy_realm_governance_27x27.png`
- `processed_png/filter_holy_realm_hidden_27x27.png`
- `processed_png/filter_holy_realm_meditation_27x27.png`
- `processed_png/filter_holy_realm_nirvana_27x27.png`
- `processed_png/filter_holy_realm_sanctuary_27x27.png`
- `processed_png/filter_holy_realm_teaching_27x27.png`
- `processed_png/filter_thr_final_silence_pressure_27x27.png`
- `processed_png/filter_thr_mandala_integration_27x27.png`
- `processed_png/filter_thr_peace_27x27.png`
- `prompts/filter_holy_realm_anti_chaos_prompt.txt`
- `prompts/filter_holy_realm_bodhi_prompt.txt`
- `prompts/filter_holy_realm_compact_prompt.txt`
- `prompts/filter_holy_realm_governance_prompt.txt`
- `prompts/filter_holy_realm_hidden_prompt.txt`
- `prompts/filter_holy_realm_meditation_prompt.txt`
- `prompts/filter_holy_realm_nirvana_prompt.txt`
- `prompts/filter_holy_realm_sanctuary_prompt.txt`
- `prompts/filter_holy_realm_teaching_prompt.txt`
- `prompts/filter_thr_final_silence_pressure_prompt.txt`
- `prompts/filter_thr_mandala_integration_prompt.txt`
- `prompts/filter_thr_peace_prompt.txt`
- `source_png/filter_holy_realm_anti_chaos_source_v1.png`
- `source_png/filter_holy_realm_bodhi_source_v1.png`
- `source_png/filter_holy_realm_compact_source_v1.png`
- `source_png/filter_holy_realm_governance_source_v1.png`
- `source_png/filter_holy_realm_hidden_source_v1.png`
- `source_png/filter_holy_realm_meditation_source_v1.png`
- `source_png/filter_holy_realm_nirvana_source_v1.png`
- `source_png/filter_holy_realm_sanctuary_source_v1.png`
- `source_png/filter_holy_realm_teaching_source_v1.png`
- `source_png/filter_thr_final_silence_pressure_source_v1.png`
- `source_png/filter_thr_mandala_integration_source_v1.png`
- `source_png/filter_thr_peace_source_v1.png`
