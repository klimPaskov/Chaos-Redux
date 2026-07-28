# Fallout successor B7 USA icon manifest

Status: candidate package produced and parent-registered. Eleven dedicated fictional USA continuity icons have source PNGs, chroma-keyed evidence, runtime-sized RGBA previews, final DDS files, and a review contact sheet. Runtime loading is not claimed. The shelter-registry pair is marked `needs_user_review` because ImageGen introduced a visible `B7` plate despite the no-text constraint.

Source mode: official built-in ImageGen on a flat `#00ff00` chroma-key background, followed by `remove_chroma_key.py` and deterministic alpha-bbox fitting. Exact verbatim prompt transcript was not retained after the interrupted batch. The visual briefs and source-to-runtime crosswalk below are the available provenance record. No vanilla pixels, County Fair content, Zombie Apocalypse asset, audio, sprite, or path was reused.

Canonical references inspected before generation: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas/contact_sheet.png` plus their member PNGs. References were style review only.

## Focus sprites

| Runtime sprite | Source PNG | Processed PNG | Runtime DDS | Target | Status |
| --- | --- | --- | --- | --- | --- |
| `GFX_goal_fallout_usa_federal_continuity_ledger` | `source_png/focus_federal_continuity_ledger_source.png` | `processed_png/focus_federal_continuity_ledger.png` | `gfx/interface/goals/fallout_successor_b7_usa/federal_continuity_ledger.dds` | 94x86 RGBA/BGRA | candidate |
| `GFX_goal_fallout_usa_shelter_registry` | `source_png/focus_shelter_registry_source.png` | `processed_png/focus_shelter_registry.png` | `gfx/interface/goals/fallout_successor_b7_usa/shelter_registry.dds` | 94x86 RGBA/BGRA | needs_user_review (visible `B7` plate) |
| `GFX_goal_fallout_usa_supply_corridors` | `source_png/focus_supply_corridors_source.png` | `processed_png/focus_supply_corridors.png` | `gfx/interface/goals/fallout_successor_b7_usa/supply_corridors.dds` | 94x86 RGBA/BGRA | candidate |
| `GFX_goal_fallout_usa_guard_compacts` | `source_png/focus_guard_compacts_source.png` | `processed_png/focus_guard_compacts.png` | `gfx/interface/goals/fallout_successor_b7_usa/guard_compacts.dds` | 94x86 RGBA/BGRA | candidate |
| `GFX_goal_fallout_usa_bilateral_reconstruction` | `source_png/focus_bilateral_reconstruction_source.png` | `processed_png/focus_bilateral_reconstruction.png` | `gfx/interface/goals/fallout_successor_b7_usa/bilateral_reconstruction.dds` | 94x86 RGBA/BGRA | candidate |
| `GFX_goal_fallout_usa_continental_radio_net` | `source_png/focus_continental_radio_net_source.png` | `processed_png/focus_continental_radio_net.png` | `gfx/interface/goals/fallout_successor_b7_usa/continental_radio_net.dds` | 94x86 RGBA/BGRA | candidate |
| `GFX_goal_fallout_usa_federal_reconstruction` | `source_png/focus_federal_reconstruction_source.png` | `processed_png/focus_federal_reconstruction.png` | `gfx/interface/goals/fallout_successor_b7_usa/federal_reconstruction.dds` | 94x86 RGBA/BGRA | candidate |

## Idea sprites

| Runtime sprite | Source PNG | Processed PNG | Runtime DDS | Target | Status |
| --- | --- | --- | --- | --- | --- |
| `GFX_idea_fallout_usa_federal_continuity_ledger` | `source_png/idea_federal_continuity_ledger_source.png` | `processed_png/idea_federal_continuity_ledger.png` | `gfx/interface/ideas/fallout_successor_b7_usa/federal_continuity_ledger.dds` | 60x68 RGBA/BGRA | candidate |
| `GFX_idea_fallout_usa_shelter_registry` | `source_png/idea_shelter_registry_source.png` | `processed_png/idea_shelter_registry.png` | `gfx/interface/ideas/fallout_successor_b7_usa/shelter_registry.dds` | 60x68 RGBA/BGRA | needs_user_review (visible `B7` plate) |
| `GFX_idea_fallout_usa_guard_compact` | `source_png/idea_guard_compact_source.png` | `processed_png/idea_guard_compact.png` | `gfx/interface/ideas/fallout_successor_b7_usa/guard_compact.dds` | 60x68 RGBA/BGRA | candidate |
| `GFX_idea_fallout_usa_federal_reconstruction` | `source_png/idea_federal_reconstruction_source.png` | `processed_png/idea_federal_reconstruction.png` | `gfx/interface/ideas/fallout_successor_b7_usa/federal_reconstruction.dds` | 60x68 RGBA/BGRA | candidate |

## Continuity project decision sprites

The decision layer uses aliases registered by the parent implementation. Each
alias points to a dedicated USA continuity icon already listed above, so no
Zombie Apocalypse sprite, file, or path enters the Fallout package.

| Runtime sprite | Backing DDS | Decision surface | Status |
| --- | --- | --- | --- |
| `GFX_decision_category_fallout_usa_continuity_projects` | `gfx/interface/goals/fallout_successor_b7_usa/federal_continuity_ledger.dds` | Category | candidate |
| `GFX_decision_fallout_usa_depot_belt_repair` | `gfx/interface/goals/fallout_successor_b7_usa/supply_corridors.dds` | Inland depot repair | candidate |
| `GFX_decision_fallout_usa_guard_muster` | `gfx/interface/goals/fallout_successor_b7_usa/guard_compacts.dds` | Guard muster | candidate |
| `GFX_decision_fallout_usa_lakes_charter` | `gfx/interface/goals/fallout_successor_b7_usa/bilateral_reconstruction.dds` | Great Lakes charter | candidate |
| `GFX_decision_fallout_usa_radio_sweep` | `gfx/interface/goals/fallout_successor_b7_usa/continental_radio_net.dds` | Radio sweep | candidate |
| `GFX_decision_fallout_usa_reconstruction_drive` | `gfx/interface/goals/fallout_successor_b7_usa/federal_reconstruction.dds` | Federal reconstruction | candidate |

## Processing and validation

- All source masters are RGB PNGs with chroma-key backgrounds. All processed previews are RGBA with transparent corners and alpha range 0 through 255.
- Focus previews are 94x86 and idea previews are 60x68, matching the established Chaos Redux icon footprints.
- All eleven DDS files were produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. Headers validate 32-bit uncompressed BGRA with `pf_flags 0x41`, masks `0xff0000/0xff00/0xff/0xff000000`, and the target dimensions.
- Review sheet: `contact_sheets/b7_usa_icons_contact_sheet.png`.
- Parent-owned `.gfx` registration is present in `interface/fallout_successor_b7_usa.gfx` and maps all eleven runtime names to these DDS files.
- The two shelter-registry candidates remain `needs_user_review` because the generated art contains a visible `B7` plate. This package is not an independent visual-approval claim.
