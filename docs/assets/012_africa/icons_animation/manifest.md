# Event 012 Africa Icon and Animation Manifest

Date: 2026-06-16
Scope: source package only inside `docs/assets/012_africa/icons_animation/`
Naming status: all sprite names, DDS paths, and `.gfx` file names below are proposed values because no parent-provided names were supplied.

## Parent wiring update, 2026-06-17

The main implementation copied the three static fallback DDS files into `gfx/interface/animated/012_africa/`, registered them in `interface/012_africa.gfx`, and placed them under animated overlays in `interface/012_africa_scripted_gui.gui`. The final wired animated sprite names are `GFX_africa_authority_atlas_seal_loop`, `GFX_africa_charter_league_banner_pulse`, and `GFX_africa_bestiary_warning_loop`; the fallback sprite names are `GFX_africa_authority_atlas_seal_static`, `GFX_africa_charter_league_banner_static`, and `GFX_africa_bestiary_warning_static`.

## Proposed `.gfx` split

- `interface/012_africa_icons.gfx`
- `interface/012_africa_ui_seals.gfx`
- `interface/012_africa_achievements.gfx`
- `interface/012_africa_animated_icons.gfx`

## Static icon set

All static icons have:

- source PNG in `static/`
- processed PNG derivatives in `static/`
- DDS previews in `dds/`
- transparent background for focus, idea, decision-category, emblem, and UI seal assets

| Theme | Proposed focus sprite | Focus PNG/DDS | Proposed idea sprite | Idea PNG/DDS | Proposed decision-category sprite | Decision PNG/DDS | Intended `.gfx` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Political Congress | `GFX_focus_africa_political_congress` | `africa_political_congress_focus_94x86.png` / `.dds` | `GFX_idea_africa_political_congress` | `africa_political_congress_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_political_congress` | `africa_political_congress_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| Industry Logistics | `GFX_focus_africa_industry_logistics` | `africa_industry_logistics_focus_94x86.png` / `.dds` | `GFX_idea_africa_industry_logistics` | `africa_industry_logistics_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_industry_logistics` | `africa_industry_logistics_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| Military Forces | `GFX_focus_africa_military_forces` | `africa_military_forces_focus_94x86.png` / `.dds` | `GFX_idea_africa_military_forces` | `africa_military_forces_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_military_forces` | `africa_military_forces_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| Charter League Diplomacy | `GFX_focus_africa_charter_league_diplomacy` | `africa_charter_league_diplomacy_focus_94x86.png` / `.dds` | `GFX_idea_africa_charter_league_diplomacy` | `africa_charter_league_diplomacy_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_charter_league_diplomacy` | `africa_charter_league_diplomacy_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| Authority Atlas | `GFX_focus_africa_authority_atlas` | `africa_authority_atlas_focus_94x86.png` / `.dds` | `GFX_idea_africa_authority_atlas` | `africa_authority_atlas_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_authority_atlas` | `africa_authority_atlas_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| Archive of Old Seats | `GFX_focus_africa_archive_old_seats` | `africa_archive_old_seats_focus_94x86.png` / `.dds` | `GFX_idea_africa_archive_old_seats` | `africa_archive_old_seats_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_archive_old_seats` | `africa_archive_old_seats_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| Regional Integration | `GFX_focus_africa_regional_integration` | `africa_regional_integration_focus_94x86.png` / `.dds` | `GFX_idea_africa_regional_integration` | `africa_regional_integration_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_regional_integration` | `africa_regional_integration_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| Liberation War Office | `GFX_focus_africa_liberation_war_office` | `africa_liberation_war_office_focus_94x86.png` / `.dds` | `GFX_idea_africa_liberation_war_office` | `africa_liberation_war_office_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_liberation_war_office` | `africa_liberation_war_office_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| Scramble for Africa | `GFX_focus_africa_scramble_for_africa` | `africa_scramble_for_africa_focus_94x86.png` / `.dds` | `GFX_idea_africa_scramble_for_africa` | `africa_scramble_for_africa_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_scramble_for_africa` | `africa_scramble_for_africa_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| Sponsor Paths | `GFX_focus_africa_sponsor_paths` | `africa_sponsor_paths_focus_94x86.png` / `.dds` | `GFX_idea_africa_sponsor_paths` | `africa_sponsor_paths_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_sponsor_paths` | `africa_sponsor_paths_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| High-Chaos Bestiary | `GFX_focus_africa_high_chaos_bestiary` | `africa_high_chaos_bestiary_focus_94x86.png` / `.dds` | `GFX_idea_africa_high_chaos_bestiary` | `africa_high_chaos_bestiary_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_high_chaos_bestiary` | `africa_high_chaos_bestiary_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| Post-Unification World Order | `GFX_focus_africa_world_order_route` | `africa_world_order_route_focus_94x86.png` / `.dds` | `GFX_idea_africa_world_order_route` | `africa_world_order_route_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_world_order_route` | `africa_world_order_route_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |
| Charter League Emblem Concept | `GFX_focus_africa_charter_league_emblem` | `africa_charter_league_emblem_focus_94x86.png` / `.dds` | `GFX_idea_africa_charter_league_emblem` | `africa_charter_league_emblem_idea_64x64.png` / `.dds` | `GFX_decision_category_africa_charter_league_emblem` | `africa_charter_league_emblem_decision_category_32x32.png` / `.dds` | `interface/012_africa_icons.gfx` |

## UI seals and headers

| Asset | Proposed sprite | PNG/DDS | Dimensions | Intended `.gfx` | Notes |
| --- | --- | --- | --- | --- | --- |
| Visible Values seal | `GFX_africa_visible_values_ui_seal` | `africa_visible_values_ui_seal_128x128.png` / `.dds` | 128x128 | `interface/012_africa_ui_seals.gfx` | Decision header or scripted GUI ornament |
| Authority Atlas UI seal | `GFX_africa_authority_atlas_ui_seal` | `africa_authority_atlas_ui_seal_128x128.png` / `.dds` | 128x128 | `interface/012_africa_ui_seals.gfx` | Decision header or scripted GUI ornament |

## Achievements

| Asset | Proposed sprite | PNG/DDS variants | Dimensions | Intended `.gfx` |
| --- | --- | --- | --- | --- |
| Unification achievement | `GFX_achievement_africa_unification` | `africa_achievement_unification_64x64`, `africa_achievement_unification_grey_64x64`, `africa_achievement_unification_not_eligible_64x64` | 64x64 | `interface/012_africa_achievements.gfx` |
| Archive achievement | `GFX_achievement_africa_archive` | `africa_achievement_archive_64x64`, `africa_achievement_archive_grey_64x64`, `africa_achievement_archive_not_eligible_64x64` | 64x64 | `interface/012_africa_achievements.gfx` |

## Animated sprite packages

All animated sets have:

- separate generated source frames in `frames/<asset_name>/`
- processed PNG frames at exact target frame size
- static fallback PNG in `static/`
- frame-sheet PNG in `previews/`
- frame-sheet DDS in `dds/`
- preview GIF in `previews/`
- contact sheet PNG in `previews/`

| Asset | Proposed animated sprite | Proposed static fallback sprite | Frame size | Frame count | Sheet PNG/DDS | Sheet size | FPS | Loop | `play_on_show` | Intended `.gfx` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Authority Atlas seal loop | `GFX_africa_authority_atlas_seal_anim` | `GFX_africa_authority_atlas_seal_static` | 128x128 | 4 | `authority_atlas_seal_loop_sheet.png` / `.dds` | 512x128 | 8 | yes | yes | `interface/012_africa_animated_icons.gfx` |
| Charter League banner pulse | `GFX_africa_charter_league_banner_anim` | `GFX_africa_charter_league_banner_static` | 160x96 | 4 | `charter_league_banner_pulse_sheet.png` / `.dds` | 640x96 | 8 | yes | yes | `interface/012_africa_animated_icons.gfx` |
| Bestiary warning loop | `GFX_africa_bestiary_warning_anim` | `GFX_africa_bestiary_warning_static` | 96x96 | 4 | `bestiary_warning_loop_sheet.png` / `.dds` | 384x96 | 10 | yes | yes | `interface/012_africa_animated_icons.gfx` |

## Reference folders inspected

- `.agents/skills/chaos-redux-event-assets/assets/focuses`
- `.agents/skills/chaos-redux-event-assets/assets/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/achievements`

## Source and processing notes

- All generated heraldry stayed fictional or symbolic. No real historical human-polity emblem was invented here.
- All animation loops were built from separate generated source frames, not transforms of a single still.
- DDS previews were produced locally under `dds/` because this task forbids writing final game-asset folders.

## Exact missing blockers

- Original subagent pass did not edit `.gfx`, `.gui`, focus, idea, decision, event, or localisation files. The parent follow-up above wires the three animated Congress-panel packages and their static fallbacks.
- The generated Charter League banner loop has mild silhouette drift between frames because each frame is a separate source image. It is package-complete, but should receive human review before final in-game wiring if strict emblem lock is required.
