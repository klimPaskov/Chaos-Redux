# Event 017 Random Faction Asset Manifest

Event id: `017`
Event slug: `random_faction`
Runtime sprite registry: `interface/017_random_faction.gfx`

## Source Mode

Static icons, achievements, event pictures, category picture, and animation frames use generated source art created through the built-in `$imagegen` workflow and partial Event 17 asset subagent output. The asset subagent stalled before landing final runtime DDS files, so the main implementation pass completed deterministic processing locally. Processing was limited to chroma-key alpha removal, crop/fit, exact-size resizing, contact-sheet assembly, frame-sheet assembly, GIF preview creation, and DDS export.

Animation source frames come from generated source atlases with separately drawn frame states, then are sliced into source frames before deterministic processing. No final animation was made by moving, scaling, rotating, warping, blurring, recoloring, or filtering one still image.

Achievement not-eligible variants reuse the matching grey achievement icon and apply a centered red cross overlay. They do not use a red tint or red filter on the base icon.

## Final Runtime Assets

| Sprite or group | Type | Source | Processed PNG | Final DDS | Size |
|---|---|---|---|---|---|
| `GFX_report_event_random_faction_cabinet` | report image | `docs/assets/017_random_faction/source/report_event_random_faction_cabinet_source.png` | `docs/assets/017_random_faction/processed_png/report_event_random_faction_cabinet.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_cabinet.dds` | 210x176 |
| `GFX_report_event_random_faction_border` | report image | `docs/assets/017_random_faction/source/report_event_random_faction_border_source.png` | `docs/assets/017_random_faction/processed_png/report_event_random_faction_border.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_border.dds` | 210x176 |
| `GFX_report_event_random_faction_liaison` | report image | `docs/assets/017_random_faction/source/report_event_random_faction_liaison_source.png` | `docs/assets/017_random_faction/processed_png/report_event_random_faction_liaison.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_liaison.dds` | 210x176 |
| `GFX_report_event_random_faction_regional_cascade` | report image | `docs/assets/017_random_faction/source/report_event_random_faction_regional_cascade_source.png` | `docs/assets/017_random_faction/processed_png/report_event_random_faction_regional_cascade.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_regional_cascade.dds` | 210x176 |
| `GFX_decision_category_random_faction_bloc_pressure` | decision icon | `docs/assets/017_random_faction/source/decision_category_random_faction_bloc_pressure_source.png` | `docs/assets/017_random_faction/processed_png/decision_category_random_faction_bloc_pressure.png` | `gfx/interface/decisions/017_random_faction/decision_category_random_faction_bloc_pressure.dds` | 32x32 |
| `GFX_decision_random_faction_stabilize_alignment` | decision icon | `docs/assets/017_random_faction/source/decision_random_faction_stabilize_alignment_source.png` | `docs/assets/017_random_faction/processed_png/decision_random_faction_stabilize_alignment.png` | `gfx/interface/decisions/017_random_faction/decision_random_faction_stabilize_alignment.dds` | 32x32 |
| `GFX_decision_random_faction_liaison` | decision icon | `docs/assets/017_random_faction/source/decision_random_faction_liaison_source.png` | `docs/assets/017_random_faction/processed_png/decision_random_faction_liaison.png` | `gfx/interface/decisions/017_random_faction/decision_random_faction_liaison.dds` | 32x32 |
| `GFX_decision_random_faction_opposition` | decision icon | `docs/assets/017_random_faction/source/decision_random_faction_opposition_source.png` | `docs/assets/017_random_faction/processed_png/decision_random_faction_opposition.png` | `gfx/interface/decisions/017_random_faction/decision_random_faction_opposition.dds` | 32x32 |
| `GFX_decision_random_faction_neutrality_council` | decision icon | `docs/assets/017_random_faction/source/decision_random_faction_neutrality_council_source.png` | `docs/assets/017_random_faction/processed_png/decision_random_faction_neutrality_council.png` | `gfx/interface/decisions/017_random_faction/decision_random_faction_neutrality_council.dds` | 32x32 |
| `GFX_decision_random_faction_border_posts` | decision icon | `docs/assets/017_random_faction/source/decision_random_faction_border_posts_source.png` | `docs/assets/017_random_faction/processed_png/decision_random_faction_border_posts.png` | `gfx/interface/decisions/017_random_faction/decision_random_faction_border_posts.dds` | 32x32 |
| `GFX_decision_random_faction_observers` | decision icon | `docs/assets/017_random_faction/source/decision_random_faction_observers_source.png` | `docs/assets/017_random_faction/processed_png/decision_random_faction_observers.png` | `gfx/interface/decisions/017_random_faction/decision_random_faction_observers.dds` | 32x32 |
| `GFX_decision_random_faction_neutrality_press` | decision icon | `docs/assets/017_random_faction/source/decision_random_faction_neutrality_press_source.png` | `docs/assets/017_random_faction/processed_png/decision_random_faction_neutrality_press.png` | `gfx/interface/decisions/017_random_faction/decision_random_faction_neutrality_press.dds` | 32x32 |
| `GFX_decision_random_faction_staff_mission` | decision icon | `docs/assets/017_random_faction/source/decision_random_faction_staff_mission_source.png` | `docs/assets/017_random_faction/processed_png/decision_random_faction_staff_mission.png` | `gfx/interface/decisions/017_random_faction/decision_random_faction_staff_mission.dds` | 32x32 |
| `GFX_decision_random_faction_radio_networks` | decision icon | `docs/assets/017_random_faction/source/decision_random_faction_radio_networks_source.png` | `docs/assets/017_random_faction/processed_png/decision_random_faction_radio_networks.png` | `gfx/interface/decisions/017_random_faction/decision_random_faction_radio_networks.dds` | 32x32 |
| `GFX_decision_random_faction_corridor` | decision icon | `docs/assets/017_random_faction/source/decision_random_faction_corridor_source.png` | `docs/assets/017_random_faction/processed_png/decision_random_faction_corridor.png` | `gfx/interface/decisions/017_random_faction/decision_random_faction_corridor.dds` | 32x32 |
| `GFX_decision_random_faction_commitment` | decision icon | `docs/assets/017_random_faction/source/decision_random_faction_commitment_source.png` | `docs/assets/017_random_faction/processed_png/decision_random_faction_commitment.png` | `gfx/interface/decisions/017_random_faction/decision_random_faction_commitment.dds` | 32x32 |
| `GFX_random_faction_bloc_pressure_bg` | decision category picture | `docs/assets/017_random_faction/source/random_faction_bloc_pressure_bg_source.png` | `docs/assets/017_random_faction/processed_png/random_faction_bloc_pressure_bg.png` | `gfx/interface/decisions/017_random_faction/random_faction_bloc_pressure_bg.dds` | 114x101 |
| `GFX_idea_random_faction_alignment_shock` | idea icon | `docs/assets/017_random_faction/source/idea_random_faction_alignment_shock_source.png` | `docs/assets/017_random_faction/processed_png/idea_random_faction_alignment_shock.png` | `gfx/interface/ideas/017_random_faction/idea_random_faction_alignment_shock.dds` | 64x64 |
| `GFX_idea_random_faction_border_pressure` | idea icon | `docs/assets/017_random_faction/source/idea_random_faction_border_pressure_source.png` | `docs/assets/017_random_faction/processed_png/idea_random_faction_border_pressure.png` | `gfx/interface/ideas/017_random_faction/idea_random_faction_border_pressure.dds` | 64x64 |
| `GFX_idea_random_faction_bloc_polarization` | idea icon | `docs/assets/017_random_faction/source/idea_random_faction_bloc_polarization_source.png` | `docs/assets/017_random_faction/processed_png/idea_random_faction_bloc_polarization.png` | `gfx/interface/ideas/017_random_faction/idea_random_faction_bloc_polarization.dds` | 64x64 |
| `GFX_idea_random_faction_neutrality_exhaustion` | idea icon | `docs/assets/017_random_faction/source/idea_random_faction_neutrality_exhaustion_source.png` | `docs/assets/017_random_faction/processed_png/idea_random_faction_neutrality_exhaustion.png` | `gfx/interface/ideas/017_random_faction/idea_random_faction_neutrality_exhaustion.dds` | 64x64 |
| `GFX_idea_random_faction_liaison_mission` | idea icon | `docs/assets/017_random_faction/source/idea_random_faction_liaison_mission_source.png` | `docs/assets/017_random_faction/processed_png/idea_random_faction_liaison_mission.png` | `gfx/interface/ideas/017_random_faction/idea_random_faction_liaison_mission.dds` | 64x64 |
| `GFX_achievement_017_random_faction_four_doors` triplet | achievement icons | `docs/assets/017_random_faction/source/017_random_faction_four_doors_source.png` | `docs/assets/017_random_faction/processed_png/017_random_faction_four_doors*.png` | `gfx/achievements/017_random_faction_four_doors*.dds` | 64x64 |
| `GFX_achievement_017_random_faction_hold_the_line` triplet | achievement icons | `docs/assets/017_random_faction/source/017_random_faction_hold_the_line_source.png` | `docs/assets/017_random_faction/processed_png/017_random_faction_hold_the_line*.png` | `gfx/achievements/017_random_faction_hold_the_line*.dds` | 64x64 |
| `GFX_achievement_017_random_faction_crowded_border` triplet | achievement icons | `docs/assets/017_random_faction/source/017_random_faction_crowded_border_source.png` | `docs/assets/017_random_faction/processed_png/017_random_faction_crowded_border*.png` | `gfx/achievements/017_random_faction_crowded_border*.dds` | 64x64 |
| `GFX_achievement_017_random_faction_liaison_web` triplet | achievement icons | `docs/assets/017_random_faction/source/017_random_faction_liaison_web_source.png` | `docs/assets/017_random_faction/processed_png/017_random_faction_liaison_web*.png` | `gfx/achievements/017_random_faction_liaison_web*.dds` | 64x64 |
| `GFX_achievement_017_random_faction_frontier_commitment` triplet | achievement icons | `docs/assets/017_random_faction/source/017_random_faction_frontier_commitment_source.png` | `docs/assets/017_random_faction/processed_png/017_random_faction_frontier_commitment*.png` | `gfx/achievements/017_random_faction_frontier_commitment*.dds` | 64x64 |
| `GFX_achievement_017_random_faction_not_everyone` triplet | achievement icons | `docs/assets/017_random_faction/source/017_random_faction_not_everyone_source.png` | `docs/assets/017_random_faction/processed_png/017_random_faction_not_everyone*.png` | `gfx/achievements/017_random_faction_not_everyone*.dds` | 64x64 |
| `GFX_random_faction_bloc_pressure_seal_static` | animated static fallback | `docs/assets/017_random_faction/source/random_faction_bloc_pressure_seal_source_atlas.png` | `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/processed_frames/random_faction_bloc_pressure_seal_static.png` | `gfx/interface/animated/017_random_faction/random_faction_bloc_pressure_seal_static.dds` | 64x64 |
| `GFX_random_faction_bloc_pressure_seal_animated` | 8-frame animation sheet | `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/source_frames/` | `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/sheets/random_faction_bloc_pressure_seal_sheet.png` | `gfx/interface/animated/017_random_faction/random_faction_bloc_pressure_seal_sheet.dds` | 512x64 |
| `GFX_random_faction_border_warning_static` | animated static fallback | `docs/assets/017_random_faction/source/random_faction_border_warning_source_atlas.png` | `docs/assets/017_random_faction/animations/random_faction_border_warning/processed_frames/random_faction_border_warning_static.png` | `gfx/interface/animated/017_random_faction/random_faction_border_warning_static.dds` | 64x64 |
| `GFX_random_faction_border_warning_animated` | 8-frame animation sheet | `docs/assets/017_random_faction/animations/random_faction_border_warning/source_frames/` | `docs/assets/017_random_faction/animations/random_faction_border_warning/sheets/random_faction_border_warning_sheet.png` | `gfx/interface/animated/017_random_faction/random_faction_border_warning_sheet.dds` | 512x64 |

## Review Files

- Static contact sheet: `docs/assets/017_random_faction/contact_sheets/event17_processed_static_contact_sheet.png`
- Not-eligible achievement review sheet: `docs/assets/017_random_faction/contact_sheets/achievement_not_eligible_red_cross_contact_sheet.png`
- Decision source contact sheet: `docs/assets/017_random_faction/contact_sheets/decision_source_contact_sheet.png`
- Animation contact sheets and GIF previews under `docs/assets/017_random_faction/animations/*/previews/`
- Package DDS copies under `docs/assets/017_random_faction/dds/`

## Validation

- `gfx\achievements\017_random_faction_crowded_border.dds	64x64	OK`
- `gfx\achievements\017_random_faction_crowded_border_grey.dds	64x64	OK`
- `gfx\achievements\017_random_faction_crowded_border_not_eligible.dds	64x64	OK`
- `gfx\achievements\017_random_faction_four_doors.dds	64x64	OK`
- `gfx\achievements\017_random_faction_four_doors_grey.dds	64x64	OK`
- `gfx\achievements\017_random_faction_four_doors_not_eligible.dds	64x64	OK`
- `gfx\achievements\017_random_faction_frontier_commitment.dds	64x64	OK`
- `gfx\achievements\017_random_faction_frontier_commitment_grey.dds	64x64	OK`
- `gfx\achievements\017_random_faction_frontier_commitment_not_eligible.dds	64x64	OK`
- `gfx\achievements\017_random_faction_hold_the_line.dds	64x64	OK`
- `gfx\achievements\017_random_faction_hold_the_line_grey.dds	64x64	OK`
- `gfx\achievements\017_random_faction_hold_the_line_not_eligible.dds	64x64	OK`
- `gfx\achievements\017_random_faction_liaison_web.dds	64x64	OK`
- `gfx\achievements\017_random_faction_liaison_web_grey.dds	64x64	OK`
- `gfx\achievements\017_random_faction_liaison_web_not_eligible.dds	64x64	OK`
- `gfx\achievements\017_random_faction_not_everyone.dds	64x64	OK`
- `gfx\achievements\017_random_faction_not_everyone_grey.dds	64x64	OK`
- `gfx\achievements\017_random_faction_not_everyone_not_eligible.dds	64x64	OK`
- `gfx\event_pictures\017_random_faction\report_event_random_faction_border.dds	210x176	OK`
- `gfx\event_pictures\017_random_faction\report_event_random_faction_cabinet.dds	210x176	OK`
- `gfx\event_pictures\017_random_faction\report_event_random_faction_liaison.dds	210x176	OK`
- `gfx\event_pictures\017_random_faction\report_event_random_faction_regional_cascade.dds	210x176	OK`
- `gfx\interface\animated\017_random_faction\random_faction_bloc_pressure_seal_sheet.dds	512x64	OK`
- `gfx\interface\animated\017_random_faction\random_faction_bloc_pressure_seal_static.dds	64x64	OK`
- `gfx\interface\animated\017_random_faction\random_faction_border_warning_sheet.dds	512x64	OK`
- `gfx\interface\animated\017_random_faction\random_faction_border_warning_static.dds	64x64	OK`
- `gfx\interface\decisions\017_random_faction\decision_category_random_faction_bloc_pressure.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\decision_random_faction_border_posts.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\decision_random_faction_commitment.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\decision_random_faction_corridor.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\decision_random_faction_liaison.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\decision_random_faction_neutrality_council.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\decision_random_faction_neutrality_press.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\decision_random_faction_observers.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\decision_random_faction_opposition.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\decision_random_faction_radio_networks.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\decision_random_faction_stabilize_alignment.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\decision_random_faction_staff_mission.dds	32x32	OK`
- `gfx\interface\decisions\017_random_faction\random_faction_bloc_pressure_bg.dds	114x101	OK`
- `gfx\interface\ideas\017_random_faction\idea_random_faction_alignment_shock.dds	64x64	OK`
- `gfx\interface\ideas\017_random_faction\idea_random_faction_bloc_polarization.dds	64x64	OK`
- `gfx\interface\ideas\017_random_faction\idea_random_faction_border_pressure.dds	64x64	OK`
- `gfx\interface\ideas\017_random_faction\idea_random_faction_liaison_mission.dds	64x64	OK`
- `gfx\interface\ideas\017_random_faction\idea_random_faction_neutrality_exhaustion.dds	64x64	OK`

Blocked assets: none.
