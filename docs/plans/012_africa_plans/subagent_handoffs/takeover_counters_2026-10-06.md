# Event012 counter repair handoff

Status: `implemented` for the six approved NATO frame-2 repairs and three newly prepared v2 large normal frames. Candidate DDS files, processed PNGs, prompts, hashes, and sheets remain staged for parent review before runtime promotion.
The gorilla and disaster map-frame brightening findings are resolved in the current source and those two textures were preserved byte-for-byte.

## Scope and ownership

This handoff covers only the eight counter tickets in `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` lines 551-560.
The six large/map stone, forest, and Oracle frame-2 repairs remain staged in candidate v1, and three complete large v2 strips now replace their normal frames while preserving the approved v1 frame-2 pixels.
No runtime DDS was overwritten and no `.gfx`, gameplay, localisation, model, audio, country, history, or spreadsheet file was edited.
The exact registered sprites and requested texture destinations remain unchanged in `interface/012_africa_strange_force_counters.gfx`.

## Eight ticket dispositions

| Plan row | Sprite | Disposition | Evidence or file hash |
|---|---|---|---|
| 551 | `GFX_unit_stone_cohorts_icon_medium` | `needs_user_review` v2 candidate; v2 Stone-warrior bust normal frame; approved stacked-stone NATO frame 2 preserved pixel-for-pixel. | Original SHA-256 `d94e7bdf5baf96d113290b0e6e95dd8c2806260ac915bb928212b16ec758971d`; candidate DDS `docs/assets/012_africa_counter_repairs/dds_candidate_v2/unit_stone_cohorts_icon.dds` SHA-256 `d4382461db69081d73aa023a4e9da2fc990dbba137ce78f13499504cae5553c1`; intended runtime path `gfx/interface/counters/divisions_large/unit_stone_cohorts_icon.dds`. |
| 552 | `GFX_unit_forest_giants_icon_medium` | `needs_user_review` v2 candidate; v2 tree-headed giant/axe normal frame; approved tree-and-axe NATO frame 2 preserved pixel-for-pixel. | Original SHA-256 `fbe279a142283186df9f61cb76a76a88ba3f6d395f181b4efcfb500e925875d9`; candidate DDS `docs/assets/012_africa_counter_repairs/dds_candidate_v2/unit_forest_giants_icon.dds` SHA-256 `29db9d3936abb88c72ef864b22befed6a02d00de775bc7114331cd7ee19d04ee`; intended runtime path `gfx/interface/counters/divisions_large/unit_forest_giants_icon.dds`. |
| 553 | `GFX_unit_oracle_recon_icon_medium` | `needs_user_review` v2 candidate; v2 hooded seer normal frame; approved eye-and-radar NATO frame 2 preserved pixel-for-pixel. | Original SHA-256 `96a6f7753b48e381a4fefc3f145968fbe02491b4f3cf468eeed543586a410cdd`; candidate DDS `docs/assets/012_africa_counter_repairs/dds_candidate_v2/unit_oracle_recon_icon.dds` SHA-256 `c62c8461d7e54d798018fd49bd06c6fdbf432056f3f7cbdc91efb3b1f36dd8a7`; intended runtime path `gfx/interface/counters/divisions_large/unit_oracle_recon_icon.dds`. |
| 554 | `GFX_unit_oracle_recon_icon_medium_white` | `implemented`; Frame 1 dark-smudge finding resolved in current source and preserved; frame 2 replaced with a compact eye-and-radar field. | Original SHA-256 `ff64e9cd648d84213523c96a4af189013ecc4ef95fb5b408253e480f1981f640`; candidate DDS `docs/assets/012_africa_counter_repairs/dds_candidate_v1/onmap_unit_oracle_recon_icon.dds` SHA-256 `339e91aa8837c0f6282223ed7e96e070ec0ffb1012c7830d7afebd2f287cff46`; intended runtime path `gfx/interface/counters/divisions_small/onmap_unit_oracle_recon_icon.dds`. |
| 557 | `GFX_unit_stone_cohorts_icon_medium_white` | `implemented`; Frame 1 preserved; frame 2 role glyph replaced with a compact stacked-stone field. The original field already had a box. | Original SHA-256 `24927ccca2fb38faefa5f7ed03e77be5cd09870054319aee556d7fea5dc76212`; candidate DDS `docs/assets/012_africa_counter_repairs/dds_candidate_v1/onmap_unit_stone_cohorts_icon.dds` SHA-256 `d930e5d0073eda7f10ddfd362876cff1622941f1c882143e7f9dadc5e8029e28`; intended runtime path `gfx/interface/counters/divisions_small/onmap_unit_stone_cohorts_icon.dds`. |
| 558 | `GFX_unit_forest_giants_icon_medium_white` | `implemented`; Frame 1 preserved; frame 2 role glyph replaced with a compact tree-and-axe field. The original field already had a box. | Original SHA-256 `0fde63344c5954aa9ecbf46d73f88c8ce429c2402be011d096bba50b12431971`; candidate DDS `docs/assets/012_africa_counter_repairs/dds_candidate_v1/onmap_unit_forest_giants_icon.dds` SHA-256 `d3e3fbb838c8ae6de0bc4191bd25938d6cab36860e13dcbf8a7985c7ac8a7769`; intended runtime path `gfx/interface/counters/divisions_small/onmap_unit_forest_giants_icon.dds`. |
| 559 | `GFX_unit_gorilla_heavy_infantry_icon_medium_white` | `resolved in current source`; Resolved in current source and left unchanged; the light-grey frame 1 is clear at native and 4x size. | Current source SHA-256 `1742b805f388629580cb564e6abeae15cacb2201df625afa47b9725071141e3f` at `gfx/interface/counters/divisions_small/onmap_unit_gorilla_heavy_infantry_icon.dds`. |
| 560 | `GFX_unit_disaster_wardens_icon_medium_white` | `resolved in current source`; Resolved in current source and left unchanged; the light-grey frame 1 is clear at native and 4x size. | Current source SHA-256 `d77af531d1330a7bb15556fe9a072fb6f480406b168c6d552b36166294ef465b` at `gfx/interface/counters/divisions_small/onmap_unit_disaster_wardens_icon.dds`. |

## Parent-authorized G5 normal-frame follow-up

Parent authorization basis: the follow-up task states that G5 brings the faint/detailed large normal frames into scope and explicitly requests three original v2 normal-frame sources.
The selected normal-frame source lineage is in `docs/assets/012_africa_counter_repairs/evidence/normal_frame_v2_candidate_lineage.json`.
Forest and Oracle use the selected middle and bottom cells from `source_png/imagegen/counter_normal_v2_atlas_v1.png`, SHA-256 `d146e1ede4aede686cd3d75eb7741ea1e06bc5db37c1848a9af8312e6ad21ad8`; the exact ImageGen request is `prompts/counter_normal_v2_atlas_v1.json`.
Stone uses the separate transparent warrior-bust source `source_png/imagegen/stone_normal_v2_generation_v2.png`, SHA-256 `f19da7c3b2e87fbb57b851ffc937480fad5ae97612c4313454f133c652be51c8`; its exact ImageGen request is `prompts/stone_normal_v2_generation_v2.json`.
Forest and Oracle use two cells from the generated transparent atlas `source_png/imagegen/counter_normal_v2_atlas_v1.png`; Forest reads as a compact tree/axe mass, and Oracle reads as a hooded seer bust.
All three v2 normal bodies map their luminance rank to RGB colors sampled from the canonical Vanilla infantry normal frame, with fully opaque body pixels and antialiased contour edges; palette, alpha, source, crop, and hash evidence is in `evidence/normal_frame_v2_processing.json`.
All three v2 frame-2 images remain pixel-identical to the approved candidate-v1 NATO fields; all six map and small normal frames remain unchanged.
The final DDS-native-plus-4x comparison sheet is `docs/assets/012_africa_counter_repairs/contact_sheets/final_dds_large_frames_v2_native_4x.png`.
## Reference evidence

Only the canonical skill reference root was used: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/gfx_references`.
The large-counter contact sheet was inspected first at `units/land/counters_large/contact_sheet.png`, followed by `units/land/counters_large/unit_infantry_icon.png`; the map-counter contact sheet was inspected first at `units/land/map_counters/contact_sheet.png`, followed by `units/land/map_counters/onmap_infantry.png`.
The canonical catalog identifies these sources as Vanilla HOI4 at `CATALOG.md` lines 383 and 395.
Installed Vanilla `interface/subuniticons.gfx` defines `GFX_unit_infantry_icon_medium` at line 46 and `GFX_unit_infantry_icon_medium_white` at line 199, each with `noOfFrames = 2` and the exact large/map DDS paths.
Installed Vanilla infantry DDS hashes, canonical reference PNG/contact-sheet hashes, consumer paths, frame bounds, and the unchanged mod `.gfx` hash are recorded in `evidence/reference_evidence.json`.

## Production and validation

Candidate lineage, rejected variants, and focused edit dispositions are recorded in `docs/assets/012_africa_counter_repairs/evidence/candidate_lineage.json`. The selected native-alpha atlas is `source_png/imagegen/counter_glyph_atlas_v3.png`; its exact ImageGen request is `prompts/counter_glyph_atlas_v3.json` and its SHA-256 is `8d0db7b732fb96a58d11968e0b4fadbc873a236b7789cd35d6236b2516a3c863`.
The frame-2 role fields remain at 49x27 large and 25x12 map sizes; the new v2 normal frames use opaque-body painted silhouettes centered within the Vanilla 76x42 frame footprint.
The six approved frame-2 candidates in v1 and the three v2 large strips pass strict 128-byte BGRA header validation, exact dimensions and payload lengths, Pillow decoding, and pixel equality with their processed PNGs; reports are `evidence/dds_strict_roundtrip.json` and `evidence/dds_strict_roundtrip_v2.json`.
The `.tools/gfx/gfx.py counter` audit reports no findings for all three complete v2 large strips and all three small candidates; all v2 frame-2 fields match the approved v1 pixel data.
The v2 large alpha audit reports no ghosted frames or alpha findings; its compact normal-frame visible bounds are Stone [24,10)-[51,35), Forest [22,12)-[52,32), and Oracle [22,12)-[52,34).
The previously recorded small Oracle, gorilla, and disaster frame-1 source layers remain unchanged; their stale dark-smudge and dark-gray table findings are resolved in current source.

## Review package

The large DDS-decoded native-plus-4x sheet is `contact_sheets/final_dds_large_frames_v2_native_4x.png`; the small sheet remains `contact_sheets/final_dds_small_frames_native_4x.png`.
The selected source crops and normal-frame layers are shown in `contact_sheets/normal_selected_sources_v2.png`; the native-alpha atlas and Stone defringe comparison are `contact_sheets/normal_source_atlas_checker.png` and `contact_sheets/stone_normal_defringe_v2.png`; lineage is in `evidence/normal_frame_v2_candidate_lineage.json`.
The asset manifest is `docs/assets/012_africa_counter_repairs/manifest.md` and its sprite mapping handoff is `docs/assets/012_africa_counter_repairs/gfx_handoff.md`.
No live game validation was performed; parent promotion and user live-game validation remain pending.

## Parent promotion

The parent reviewed the native/4x v2 large sheet and the v1 small sheet and installed the three large v2 and three small v1 strips.
Each runtime source still matched its recorded original hash before the install, and every installed hash matched its reviewed candidate.
The two existing gorilla/disaster map strips were preserved after direct review.
The final durable crosswalk and generation lineage are `docs/plans/012_africa_plans/takeover_counter_inventory_2026-10-06.json`.
Source, processing, strict DDS and contact-sheet evidence remain in the task asset workspace while live acceptance is pending.
Earlier no-install statements describe the producer handoff before this parent promotion.
