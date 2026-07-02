# Event 014 Cannibalism Generated-Art Gap Pass Handoff

Date: 2026-07-01

Scope: regenerated Event 014 non-icon assets that were still procedural or lacked imagegen provenance after the completed generated-art sidecar. This pass used `$imagegen` built-in generation only for source art. No gameplay, localisation, decision, focus, spreadsheet, interface `.gfx`, or completed sidecar-owned final assets were edited.

## Source Mode

All new source art was generated with `$imagegen` and copied from:

`C:/Users/klimp/.codex/generated_images/019f1e1b-4514-7242-8913-2d24cb1245f1/`

Generation was appropriate because these assets depict fictional alternate-history war-horror report scenes, super-event scenes, and fictional CBL/CBL_LAST_TABLE flags. Prompts avoided real gore photographs, real victims, extremist symbols, celebrity likenesses, readable generated text, modern props, and procedural/simple-shape fallback art.

One initial `spread` raw generation was not selected after prompt revision. The selected `report_event_cannibalism_spread` source is the later symbolic rail-depot ration-scandal image.

## Final Event Images

Suggested `.gfx` target: parent should wire these in the existing Event 014 event-image `.gfx` file or the repo's current Event 014 image registry. This subagent did not edit `.gfx`.

| Sprite | Final DDS | Source PNG | Processed PNG | Notes |
|---|---|---|---|---|
| `GFX_report_event_cannibalism_spread` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_spread.dds` | `docs/assets/014_cannibalism/generated_art_sources/report_event_cannibalism_spread_source.png` | `docs/assets/014_cannibalism/generated_art_processed/report_event_cannibalism_spread.png` | Report image, 210x176 |
| `GFX_report_event_cannibalism_contained` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_contained.dds` | `docs/assets/014_cannibalism/generated_art_sources/report_event_cannibalism_contained_source.png` | `docs/assets/014_cannibalism/generated_art_processed/report_event_cannibalism_contained.png` | Report image, 210x176 |
| `GFX_report_event_cannibalism_failure` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_failure.dds` | `docs/assets/014_cannibalism/generated_art_sources/report_event_cannibalism_failure_source.png` | `docs/assets/014_cannibalism/generated_art_processed/report_event_cannibalism_failure.png` | Report image, 210x176 |
| `GFX_report_event_cannibalism_commune` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_commune.dds` | `docs/assets/014_cannibalism/generated_art_sources/report_event_cannibalism_commune_source.png` | `docs/assets/014_cannibalism/generated_art_processed/report_event_cannibalism_commune.png` | Report image, 210x176 |
| `GFX_report_event_cannibalism_world_end` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_world_end.dds` | `docs/assets/014_cannibalism/generated_art_sources/report_event_cannibalism_world_end_source.png` | `docs/assets/014_cannibalism/generated_art_processed/report_event_cannibalism_world_end.png` | Report image, 210x176 |
| `GFX_report_event_cannibalism_defeat` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_defeat.dds` | `docs/assets/014_cannibalism/generated_art_sources/report_event_cannibalism_defeat_source.png` | `docs/assets/014_cannibalism/generated_art_processed/report_event_cannibalism_defeat.png` | Report image, 210x176 |
| `GFX_report_event_cannibalism_network` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_network.dds` | `docs/assets/014_cannibalism/generated_art_sources/report_event_cannibalism_network_source.png` | `docs/assets/014_cannibalism/generated_art_processed/report_event_cannibalism_network.png` | Separate visible report image for the global network reveal; distinct from `super_event_cannibalism_network` |
| `GFX_super_event_cannibalism_islands` | `gfx/super_events/014_cannibalism/super_event_cannibalism_islands.dds` | `docs/assets/014_cannibalism/generated_art_sources/super_event_cannibalism_islands_source.png` | `docs/assets/014_cannibalism/generated_art_processed/super_event_cannibalism_islands.png` | Super-event image, 457x328 |
| `GFX_super_event_cannibalism_world_end` | `gfx/super_events/014_cannibalism/super_event_cannibalism_world_end.dds` | `docs/assets/014_cannibalism/generated_art_sources/super_event_cannibalism_world_end_source.png` | `docs/assets/014_cannibalism/generated_art_processed/super_event_cannibalism_world_end.png` | Super-event image, 457x328 |
| `GFX_super_event_cannibalism_defeat` | `gfx/super_events/014_cannibalism/super_event_cannibalism_defeat.dds` | `docs/assets/014_cannibalism/generated_art_sources/super_event_cannibalism_defeat_source.png` | `docs/assets/014_cannibalism/generated_art_processed/super_event_cannibalism_defeat.png` | Super-event image, 457x328 |

## Final Flags

Flags are engine lookup assets and should not need `.gfx` sprite definitions. Each flag has normal, medium, and small TGA outputs:

- `CBL_communism`
- `CBL_democratic`
- `CBL_fascism`
- `CBL_neutrality`
- `CBL_LAST_TABLE`
- `CBL_LAST_TABLE_communism`
- `CBL_LAST_TABLE_democratic`
- `CBL_LAST_TABLE_fascism`
- `CBL_LAST_TABLE_neutrality`

Final paths follow the HOI4 flag convention:

- `gfx/flags/<flag>.tga`
- `gfx/flags/medium/<flag>.tga`
- `gfx/flags/small/<flag>.tga`

Processed previews follow:

- `docs/assets/014_cannibalism/generated_art_processed/flag_<flag>_82x52.png`
- `docs/assets/014_cannibalism/generated_art_processed/flag_<flag>_41x26.png`
- `docs/assets/014_cannibalism/generated_art_processed/flag_<flag>_10x7.png`

Source files follow:

- `docs/assets/014_cannibalism/generated_art_sources/flag_<flag>_source.png`

## Contact Sheets

- `docs/assets/014_cannibalism/generated_art_contact_sheets/event014_generated_gap_pass_contact_sheet.png`
- `docs/assets/014_cannibalism/generated_art_contact_sheets/event014_flag_final_sizes_contact_sheet.png`
- `docs/assets/014_cannibalism/generated_art_contact_sheets/event014_raw_generated_order_contact_sheet.png`

## Manifest

Updated:

- `docs/assets/014_cannibalism/generated_art_sources/generated_art_manifest.md`

The manifest includes prompt provenance, source paths, processed paths, final game paths, target dimensions, and source-mode rationale.

## Validation Notes

- Report DDS outputs checked at 210x176.
- Super-event DDS outputs checked at 457x328.
- Representative flag TGAs checked at 82x52, 41x26, and 10x7.
- All written flag TGAs use 24-bit uncompressed data with descriptor `0`, meaning bottom-left origin rather than top-origin.
- No `.gfx` files were edited.
- No required gap-pass asset remains procedural or non-imagegen-derived.

## Remaining Risks

- Parent still needs to wire or verify `.gfx` definitions for the report and super-event sprites, especially `GFX_report_event_cannibalism_network`.
- The 10x7 flag variants are necessarily coarse; the final-size contact sheet shows the exact in-game-scale result for review.
