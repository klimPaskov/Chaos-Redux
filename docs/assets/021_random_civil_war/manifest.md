# Event 021 Random Civil War asset manifest

Status: implementation-ready visual package for the `Needs Testing` release state.

This manifest covers the forty active Event 021-owned runtime textures wired through `interface/021_random_civil_war.gfx`.
The complete row-level source, processed-PNG, runtime-DDS, dimension, alpha, repair, and consumer evidence is maintained in `docs/events/021_random_civil_war/owned_asset_crosswalk.md` and `validation/visual_asset_audit_2026-09-01.md`.
The six Event 006 package families reused by Event 021 are separately owned and remain in `validation/reused_event006_asset_audit_2026-09-02.md`.

## Production record

The scene and icon masters use official ImageGen native-alpha generation where the consumer requires transparent unused canvas, with the original source PNG retained under `source_png/` and the processed PNG retained under `processed_png/`.
The documented achievement alpha repairs use the recorded border-connected transparency fallback where required, and the original candidates remain preserved under the validation folders.
No background-removal fallback was used for the five dedicated prompt-backed icon sources listed under `prompts/`.
The required visual directions and prompt constraints are recorded in `docs/specs/021_random_civil_war_specs/021_random_civil_war_asset_prompt.md`, while the accepted source-specific prompt text is retained in `prompts/` and the visual audit.

Every runtime DDS was inspected at native size, checked for the established one-level BGRA contract, and compared pixel-for-pixel with its processed PNG.
The review contact sheets are `contact_sheets/icon_artist_021_missing_icons_contact_sheet.png`, `contact_sheets/icon_artist_021_contrast_review.png`, and the achievement review sheets under `validation/alpha_edge_repair_2026-09-02/contact_sheet/`.
No runtime reference points into `docs/assets/`.

## Runtime inventory

| Family | Count | Sprite and consumer record | Runtime location | Size |
| --- | ---: | --- | --- | --- |
| Opening report | 1 | `GFX_report_event_021_random_civil_war_opening`; `chaosx.nr21.2` through `.9` | `gfx/event_pictures/021_random_civil_war/` | 210x176 |
| Multi-front and Global Fracture news | 2 | `GFX_news_event_021_multi_front_war` for `chaosx.news.211`; `GFX_news_event_021_global_fracture` for `chaosx.news.212` | `gfx/event_pictures/021_random_civil_war/` | 397x153 |
| Decision category | 2 | `GFX_decision_category_picture_021_civil_war` and `GFX_decision_category_021_civil_war_crisis`; `event021_civil_war_crisis_category` | `gfx/interface/decisions/021_random_civil_war/` | 114x101 and 52x40 |
| Decision icons | 11 | `GFX_decision_event021_secure_arsenals`, `GFX_decision_event021_capital_defense`, `GFX_decision_event021_loyalty_review`, `GFX_decision_event021_depot_seizure`, `GFX_decision_event021_relief_corridor`, `GFX_decision_event021_emergency_settlement`, `GFX_decision_event021_reconstruction`, `GFX_decision_event021_priority_front`, `GFX_decision_event021_monitor_border`, `GFX_decision_event021_support_government`, and `GFX_decision_event021_support_opposition`; consumers are listed in the crosswalk | `gfx/interface/decisions/021_random_civil_war/` | 32x32 |
| Mission icons | 3 | `GFX_mission_event021_hold_capital`, `GFX_mission_event021_secure_rail`, and `GFX_mission_event021_settlement_terms`; `event021_hold_the_capital_mission`, `event021_secure_rail_spine_mission`, and `event021_hold_settlement_terms_mission` | `gfx/interface/decisions/021_random_civil_war/` | 32x32 |
| Idea icons | 3 | `GFX_idea_021_fractured_command`, `GFX_idea_021_war_torn_administration`, and `GFX_idea_021_unsettled_settlement` | `gfx/interface/ideas/021_random_civil_war/` | 64x64 |
| Achievement triplets | 18 | `GFX_achievement_021_random_civil_war_hold_the_center`, `..._no_state_left_behind`, `..._a_flag_of_our_own`, `..._war_within_a_war`, `..._the_terms_hold`, and `..._fractals_of_sovereignty`, each with completed, `_grey`, and `_not_eligible` states | `gfx/achievements/` | 64x64 |

## Deliberate non-assets

No Event 006 replacement portrait, generic flag, faction emblem, animated asset, scripted GUI panel, 3D asset, super-event image, or audio package is introduced by Event 021.
Event 006 owns its identity, leader, portrait, flag, focus, and route assets.
Optional Event 006 and strange-incident report art were not added because the implemented consumers reuse the audited opening/news families and do not require a separate final runtime consumer.

The reused Event 006 portrait and provenance blockers remain explicitly recorded and are not silently substituted.
