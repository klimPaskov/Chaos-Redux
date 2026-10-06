> Current parent status: 50 reviewed DDS textures installed and independently pixel-verified; all42 active focus canvases94x86. Legacy Warroom normal/shine aliases remain on Home Guard pending explicit exception to the user .gfx rule. Worker staging statements below are historical. Final MCP/live acceptance pending.

# Baltic Event 005 GFX Handoff

The 45 final DDS candidates are staged under `docs/assets/005_soviet_collapse/gfx_fix_baltic/final_dds/gfx/interface/goals/005_soviet_collapse/`; they have not been copied into runtime `gfx/`. The source PNGs, processed PNGs, full DDS round trips, contact sheets, and row-level crosswalk remain in this package.

## Exact consumers and staged paths

All 45 staged DDS candidates are 94x86. Their native DDS files use the repository converter and pass the strict 128-byte uncompressed BGRA header and PNG-to-DDS pixel-equality checks in `notes/dds_validation_final.json`.

| GFX sprite(s) | Focus ID / purpose | Staged runtime-relative DDS path(s) |
| --- | --- | --- |
| `GFX_baltic_soviet_collapse_home_guard_staff` | Registered Baltic home-guard alias. | `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_home_guard_staff.dds` |
| `GFX_baltic_soviet_collapse_restoration_pact` | Registered Baltic restoration-pact alias. | `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_restoration_pact.dds` |
| `GFX_focus_baltic_soviet_collapse_pan_baltic_war_room` | Focus `baltic_soviet_collapse_pan_baltic_war_room`; shared maps, signals, and reserve forces. | `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_pan_baltic_war_room.dds` |
| `GFX_baltic_soviet_collapse_pan_baltic_war_room` and `_shine` | Legacy alias for the same war-room art. | Proposed separate path: `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_pan_baltic_war_room.dds` |
| `GFX_focus_baltic_soviet_collapse_baltic_defense_compact` | Focus `baltic_soviet_collapse_baltic_defense_compact`; Baltic League Defense charter. | `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_baltic_defense_compact.dds` |
| `GFX_focus_baltic_soviet_collapse_tallinn_riga_vilnius_rotation` | Focus `baltic_soviet_collapse_tallinn_riga_vilnius_rotation`; rotating compact chair. | `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_tallinn_riga_vilnius_rotation.dds` |
| `GFX_baltic_soviet_collapse_german_border_pressure` and `GFX_focus_baltic_soviet_collapse_german_border_pressure` | Focus `baltic_soviet_collapse_german_border_pressure`; southwest border pressure. | `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_german_border_pressure.dds`; `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_german_border_pressure.dds` |
| `GFX_focus_baltic_soviet_collapse_estonian_forest_coast_guard` | Focus `baltic_soviet_collapse_estonian_forest_coast_guard`; coastal batteries and forest posts. | `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_estonian_forest_coast_guard.dds` |
| `GFX_baltic_soviet_collapse_scandinavian_listening_mission` and `GFX_focus_baltic_soviet_collapse_scandinavian_listening_mission` | Focus `baltic_soviet_collapse_scandinavian_listening_mission`; northern contacts and guarded witnesses. | `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_scandinavian_listening_mission.dds`; `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_scandinavian_listening_mission.dds` |
| `GFX_baltic_soviet_collapse_british_naval_observers` and `GFX_focus_baltic_soviet_collapse_british_naval_observers` | Focus `baltic_soviet_collapse_british_naval_observers`; port and coast-guard inspection. | `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_british_naval_observers.dds`; `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_british_naval_observers.dds` |
| `GFX_baltic_soviet_collapse_baltic_recognition_dossier` and `GFX_focus_baltic_soviet_collapse_baltic_recognition_dossier` | Focus `baltic_soviet_collapse_baltic_recognition_dossier`. | `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_baltic_recognition_dossier.dds`; `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_baltic_recognition_dossier.dds` |
| `GFX_baltic_soviet_collapse_sponsor_fleet_rights` and `GFX_focus_baltic_soviet_collapse_sponsor_fleet_rights` | Focus `baltic_soviet_collapse_sponsor_fleet_rights`; limited fleet rights for aid. | `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_sponsor_fleet_rights.dds`; `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_sponsor_fleet_rights.dds` |
| `GFX_baltic_soviet_collapse_foreign_advisers_under_baltic_law` and `GFX_focus_baltic_soviet_collapse_foreign_advisers_under_baltic_law` | Focus `baltic_soviet_collapse_foreign_advisers_under_baltic_law`; advisers operate under Baltic statutes. | `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_foreign_advisers_under_baltic_law.dds`; `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_foreign_advisers_under_baltic_law.dds` |
| `GFX_baltic_soviet_collapse_the_port_economy` | Customs, guarded warehouses, and port supplies. | `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_the_port_economy.dds` |

The paired direct and focus aliases for Scandinavian Listening Mission, British Naval Observers, Baltic Recognition Dossier, Sponsor Fleet Rights, and Foreign Advisers Under Baltic Law have identical current decoded source pixels and receive separate DDS outputs at their existing registered paths. All 25 normalized focus textures retain their registered basenames and need no focus registry edit.

## Twenty-five existing focus textures normalized

These previously accepted focus illustrations were 100x88 in the mixed-size 42-node tree. Each staged replacement keeps the exact registered path and subject art, fits the visible artwork proportionally inside a transparent 94x86 canvas, and cleans only confirmed chroma-colored alpha-edge pixels. Alpha remains unchanged; every final DDS round trips pixel-for-pixel.

| Focus ID | Before | Processed PNG | Staged DDS |
| --- | --- | --- | --- |
| `baltic_soviet_collapse_military_border_government` | 100x88 | `processed_png/goal_005_focus_military_border_government_normalized_edgeclean_94x86.png` | `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_military_border_government.dds` |
| `baltic_soviet_collapse_no_retreat_from_the_capital` | 100x88 | `processed_png/goal_005_focus_no_retreat_from_the_capital_normalized_edgeclean_94x86.png` | `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_no_retreat_from_the_capital.dds` |
| `baltic_soviet_collapse_coastal_defense_batteries` | 100x88 | `processed_png/goal_005_focus_coastal_defense_batteries_normalized_edgeclean_94x86.png` | `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_coastal_defense_batteries.dds` |
| `baltic_soviet_collapse_the_border_front_at_home` | 100x88 | `processed_png/goal_005_focus_the_border_front_at_home_normalized_edgeclean_94x86.png` | `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_the_border_front_at_home.dds` |
| `baltic_soviet_collapse_volunteer_rifle_societies` | 100x88 | `processed_png/goal_005_focus_volunteer_rifle_societies_normalized_edgeclean_94x86.png` | `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_volunteer_rifle_societies.dds` |
| `baltic_soviet_collapse_university_volunteer_lists` | 100x88 | `processed_png/goal_005_focus_university_volunteer_lists_normalized_edgeclean_94x86.png` | `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_university_volunteer_lists.dds` |
| `baltic_soviet_collapse_the_port_economy` | 100x88 | `processed_png/goal_005_focus_the_port_economy_normalized_edgeclean_94x86.png` | `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_the_port_economy.dds` |

The full 42-focus source-to-output map is `notes/focus_tree_42_crosswalk.json`. Before normalization the tree had 17 94x86 and 25 100x88 files; afterward all 42 focus textures are 94x86. The originals and preflight hashes remain preserved in `source_dds/live/`, `source_png/runtime_decoded/`, and `notes/focus_tree_42_source_snapshots.json`.

## One pending legacy path correction

`interface/005_soviet_collapse.gfx` currently maps both the normal and `_shine` legacy Pan-Baltic War Room sprites to `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_home_guard_staff.dds`. The separately registered focus-tree sprite already points at its own `focus_005_baltic_soviet_collapse_pan_baltic_war_room.dds` path.

After reviewing the staged direct Pan-Baltic DDS, point both legacy entries at the new path below:

```text
GFX_baltic_soviet_collapse_pan_baltic_war_room      -> gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_pan_baltic_war_room.dds
GFX_baltic_soviet_collapse_pan_baltic_war_room_shine -> gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_pan_baltic_war_room.dds
```

No sprite identifier changes are needed. No `.gfx` size or frame adjustment is needed for the staged 94x86 assets; the legacy alias texture-path correction is the only identified wiring change.

## Previously resolved rows

The seven non-German severity-1 direct sprites remain at their current accepted runtime paths: Military Border Government, No Retreat from the Capital, Latvian Port Guard Boards, Coastal Defense Batteries, The Border Front at Home, Volunteer Rifle Societies, and University Volunteer Lists. Their direct DDS hashes match the previous accepted `final_contact_sheet_index.json` outputs and their edge counts are zero. All 25 separate focus aliases that were 100x88 before this pass are staged as normalized 94x86 textures.

The focus `GFX_focus_baltic_soviet_collapse_latvian_port_guard_boards` also has no remaining magenta/green edge pixels, so it needs no replacement asset.

## Full-tree texture-size result

All 42 registered Baltic focus consumers now resolve to 94x86 textures. The before/after consumer map is `notes/focus_tree_42_crosswalk.json`; all 25 normalized outputs are listed in `notes/focus_100x88_normalization_all25.json`. The full-tree before/after sheets show the exact 42-node set at `contact_sheets/full_42_baltic_focus_tree_before.jpg` and `contact_sheets/full_42_baltic_focus_tree_after_final.jpg`.

## Wiring and parent review

The direct aliases live in `interface/005_soviet_collapse.gfx`; the Baltic focus icons live in `interface/005_soviet_collapse_focus_icons.gfx`; the corresponding focus blocks are in `common/national_focus/005_soviet_collapse_republics.txt`; and player-facing title/description keys are in `localisation/english/005_soviet_collapse_l_english.yml`. This asset subagent did not edit those files.

Review the narrow before/after sheets `contact_sheets/before_native.png` and `contact_sheets/after_native_final.png`, the full-tree pair `contact_sheets/full_42_baltic_focus_tree_before.jpg` and `contact_sheets/full_42_baltic_focus_tree_after_final.jpg`, and the normalized-focus checks `contact_sheets/focus_100x88_all25_final_native_contrast.jpg` and `contact_sheets/focus_100x88_all25_final_enlarged_checker.jpg` before promotion. The first-seven and remaining-18 normalization comparisons are `contact_sheets/focus_seven_normalization_final_contrast.jpg`, `contact_sheets/focus_seven_normalization_final_enlarged_checker.jpg`, and `contact_sheets/focus_remaining18_normalization_before_after.jpg`. `contact_sheets/mcp_baltic_focus_tree_before.png` is the baseline read-only tree raster; the new icons are staged and were not wired for a post-change engine raster.

The direct Pan-Baltic legacy path is pending parent review and the parent-side `.gfx` update. All other independent asset outputs are staged with source, processing, contrast, and strict DDS evidence. All 42 focus DDS consumers are now consistent at 94x86; the only integration dependency is the parent-owned Pan-Baltic direct alias correction.
