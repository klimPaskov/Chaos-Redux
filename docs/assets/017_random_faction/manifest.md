# Event 017 Random Faction Asset Manifest

Event id: `017`
Event slug: `random_faction`
Runtime sprite registry: `interface/017_random_faction.gfx`
Achievement sprite registry: `interface/chaosx_achievements.gfx`
Canonical prompt record: `docs/assets/017_random_faction/prompts/icon_and_animation_prompts.md`
Asset audit: 2026-07-10

## Source Mode

All assets in the final runtime table use generated source art created through the built-in `$imagegen` workflow. Their original generated PNGs or source atlases are preserved under `docs/assets/017_random_faction/source/`, and the animation source frames are preserved under their animation packages. Deterministic processing is limited to chroma-key alpha removal, crop/fit, shared-scale anchor normalization, exact-size resizing, contact-sheet assembly, exact RGBA frame-sheet assembly, GIF preview creation, grayscale achievement variants, the standard not-eligible overlay, and DDS export.

Decision, decision-category, idea, and achievement art are separate asset-type sources. The package does not satisfy one icon type by resizing, recoloring, padding, or lightly editing another icon type. Every final icon within a group has a unique source-art hash.

Animation source frames come from generated source atlases with eight separately drawn frame states, then are sliced into source frames before deterministic processing. No final animation was made by moving, scaling, rotating, warping, blurring, recoloring, or filtering one still image. Both sequences use 64x64 frames, eight unique source states, 512x64 horizontal sheets, 8 FPS playback, centered anchors, looping, and `play_on_show = yes`.

Achievement not-eligible variants copy the matching grey achievement icon and composite the standard repository achievement cross overlay on top. They do not use a red tint or red filter on the base icon. The overlay source was present when these variants were made and is visible in the completed not-eligible files and review sheet; the skill reference-asset directory that contained it was later removed from the current tree.

Every row in the final runtime table has source mode `$imagegen` and asset status `converted` or later. Runtime wiring status is documented in `gfx_handoff.md`.

## Final Runtime Assets

| Sprite or group | Type | Source | Processed PNG | Final DDS | Size |
|---|---|---|---|---|---|
| `GFX_report_event_random_faction_cabinet` | report image | `docs/assets/017_random_faction/source/report_event_random_faction_cabinet_source.png` | `docs/assets/017_random_faction/processed_png/report_event_random_faction_cabinet.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_cabinet.dds` | 210x176 |
| `GFX_report_event_random_faction_border` | report image | `docs/assets/017_random_faction/source/report_event_random_faction_border_source.png` | `docs/assets/017_random_faction/processed_png/report_event_random_faction_border.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_border.dds` | 210x176 |
| `GFX_report_event_random_faction_liaison` | report image | `docs/assets/017_random_faction/source/report_event_random_faction_liaison_source.png` | `docs/assets/017_random_faction/processed_png/report_event_random_faction_liaison.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_liaison.dds` | 210x176 |
| `GFX_report_event_random_faction_regional_cascade` | report image | `docs/assets/017_random_faction/source/report_event_random_faction_regional_cascade_source.png` | `docs/assets/017_random_faction/processed_png/report_event_random_faction_regional_cascade.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_regional_cascade.dds` | 210x176 |
| `GFX_decision_category_random_faction_bloc_pressure` | decision category icon | `docs/assets/017_random_faction/source/decision_category_random_faction_bloc_pressure_source.png` | `docs/assets/017_random_faction/processed_png/decision_category_random_faction_bloc_pressure.png` | `gfx/interface/decisions/017_random_faction/decision_category_random_faction_bloc_pressure.dds` | 32x32 |
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
- Not-eligible achievement red-cross overlay review sheet: `docs/assets/017_random_faction/contact_sheets/achievement_not_eligible_red_cross_contact_sheet.png`
- Decision source contact sheet: `docs/assets/017_random_faction/contact_sheets/decision_source_contact_sheet.png`
- Animation contact sheets and GIF previews under `docs/assets/017_random_faction/animations/*/previews/`
- Package DDS copies under `docs/assets/017_random_faction/dds/`
- Canonical prompt record: `docs/assets/017_random_faction/prompts/icon_and_animation_prompts.md`

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

## Animation Audit

- Bloc-pressure seal: eight unique source PNG hashes; processed alpha bounds occupy roughly 49-50x55-56 pixels inside each 64x64 frame; all eight sheet cells are exact RGBA copies of the corresponding processed frames; static fallback equals frame 000; preview GIF contains eight states plus one review-only repeated rest frame.
- Border warning: eight unique source PNG hashes; processed alpha bounds occupy roughly 42-45x55-56 pixels inside each 64x64 frame; all eight sheet cells are exact RGBA copies of the corresponding processed frames; static fallback equals frame 000; preview GIF contains eight states plus one review-only repeated rest frame.
- Both runtime sheets and static fallbacks are 32-bit uncompressed DDS with A8R8G8B8 masks, real transparent unused pixels, and no visible chroma fringe.
- The animated border warning is used instead of a static-only warning treatment because the real frame-authored amber-to-red sequence communicates low neutrality resilience clearly; its frame-000 static fallback is still included.

## Reference and Reproducibility Notes

- The required decision, idea, report, and achievement examples were inspected through the preserved `docs/assets/017_random_faction/contact_sheets/reference_contact_sheet.png` created while those reference folders existed.
- The original reference folders under `.agents/skills/chaos-redux-event-assets/assets/` and the achievement overlay source were deleted from the current tree after the package was produced. Their absence does not affect the final runtime assets, but those historical inputs must be restored before regenerating achievement not-eligible variants from scratch.
- The original source commit did not retain verbatim built-in imagegen tool-call text. The canonical production prompts are recorded in `docs/assets/017_random_faction/prompts/icon_and_animation_prompts.md` without claiming to be verbatim transcripts.

Blocked assets: none.

Simplifications or substituted assets: none.
