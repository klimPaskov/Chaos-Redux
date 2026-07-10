# Event 011 Secret Alliance final asset register

Status: complete and wired. The detailed source, prompt, conversion, dimensions, alpha, contact-sheet, and validation ledgers remain in `manifest.md` and `manifest_icons_ui_animation.md`. This register is the gameplay-facing map of every final visual and audio package.

## Event, news, and super-event art

Registered in `interface/011_secret_alliance.gfx` unless noted.

| Use | Sprite | Final DDS |
| --- | --- | --- |
| First pattern report | `GFX_report_event_011_secret_alliance_first_pattern` | `gfx/event_pictures/011_secret_alliance/report_event_first_pattern.dds` |
| Missing courier report | `GFX_report_event_011_secret_alliance_missing_courier` | `gfx/event_pictures/011_secret_alliance/report_event_missing_courier.dds` |
| Machine sabotage report | `GFX_report_event_011_secret_alliance_machine_sabotage` | `gfx/event_pictures/011_secret_alliance/report_event_machine_sabotage.dds` |
| Safehouse raid report | `GFX_report_event_011_secret_alliance_safehouse_raid` | `gfx/event_pictures/011_secret_alliance/report_event_safehouse_raid.dds` |
| Border survey report | `GFX_report_event_011_secret_alliance_border_survey` | `gfx/event_pictures/011_secret_alliance/report_event_border_survey.dds` |
| Political attack report | `GFX_report_event_011_secret_alliance_political_attack` | `gfx/event_pictures/011_secret_alliance/report_event_political_attack.dds` |
| Turned channel report | `GFX_report_event_011_secret_alliance_turned_channel` | `gfx/event_pictures/011_secret_alliance/report_event_turned_channel.dds` |
| Public coalition news | `GFX_news_event_011_secret_alliance_public_coalition` | `gfx/event_pictures/011_secret_alliance/news_event_public_coalition.dds` |
| Reveal super-event | `GFX_super_event_011_secret_alliance_public_reveal` | `gfx/super_events/011_secret_alliance/super_event_public_reveal.dds` |

The super-event sprite is registered in `interface/chaosx_super_events.gfx`.

## Counter-network UI and faction emblem

| Use | Sprite | Final DDS |
| --- | --- | --- |
| Counter-network panel | `GFX_011_secret_alliance_counter_network_panel` | `gfx/interface/011_secret_alliance/counter_network_panel.dds` |
| Evidence frame/fill | `GFX_011_secret_alliance_evidence_meter_frame`, `GFX_011_secret_alliance_evidence_meter_fill` | `gfx/interface/011_secret_alliance/evidence_meter_{frame,fill}.dds` |
| Preparedness frame/fill | `GFX_011_secret_alliance_preparedness_meter_frame`, `GFX_011_secret_alliance_preparedness_meter_fill` | `gfx/interface/011_secret_alliance/preparedness_meter_{frame,fill}.dds` |
| Four-state suspect sheet | `GFX_011_secret_alliance_suspect_card_states` | `gfx/interface/011_secret_alliance/suspect_card_states.dds` |
| Recent operation | `GFX_011_secret_alliance_status_recent_operation` | `gfx/interface/011_secret_alliance/status_recent_operation.dds` |
| Turned channel | `GFX_011_secret_alliance_status_turned_channel` | `gfx/interface/011_secret_alliance/status_turned_channel.dds` |
| False lead | `GFX_011_secret_alliance_status_false_lead` | `gfx/interface/011_secret_alliance/status_false_lead.dds` |
| War pressure | `GFX_011_secret_alliance_status_war_pressure` | `gfx/interface/011_secret_alliance/status_war_pressure.dds` |
| Anti-target faction emblem | `GFX_011_secret_alliance_faction_emblem` | `gfx/interface/011_secret_alliance/faction_anti_target_pact_emblem.dds` |

## Decision and idea icons

The two category sprites are `GFX_decision_category_011_secret_alliance_foreign_interference` and `GFX_decision_category_011_secret_alliance_coalition_crisis`.

The 17 unique decision sprites use the root `GFX_decision_011_secret_alliance_` and the suffixes `compare_traffic`, `trace_courier`, `compare_sabotage`, `compartmentalize`, `secure_industry`, `harden_border`, `quiet_approach`, `security_guarantee`, `feed_false_plans`, `turn_member`, `disrupt_conference`, `border_intercept`, `release_dossier`, `emergency_mobilization`, `preempt_coalition`, `offer_separate_terms`, and `strike_depots`. Their files use the same suffixes under `gfx/interface/decisions/011_secret_alliance/decision_*.dds`.

The seven unique idea sprites use the root `GFX_idea_011_secret_alliance_` and the suffixes `unexplained_interference`, `compromised_channels`, `hardened_networks`, `public_coalition_pressure`, `known_enemy_plans`, `coalition_opening_coordination`, and `fractured_coalition`. Their files use the same suffixes under `gfx/interface/ideas/011_secret_alliance/idea_*.dds`.

The one-year `secret_alliance_retained_counterintelligence` aftermath idea deliberately uses `GFX_idea_011_secret_alliance_hardened_networks`. It represents retained methods from the same counter-network program, so this is an explicit same-system visual reuse rather than a missing or placeholder asset.

## Evolution III warning animation

- Animated sprite: `GFX_011_secret_alliance_coalition_closure_warning_animated`
- Sheet: `gfx/interface/011_secret_alliance/coalition_closure_warning_sheet.dds`
- Format: eight distinct 128x96 frames, 1024x96 sheet, 8 FPS, looped
- Source frames: `docs/assets/011_secret_alliance/animations/coalition_closure_warning/source_frames/`
- Processed frames: `docs/assets/011_secret_alliance/animations/coalition_closure_warning/processed_frames/`
- Preview: `docs/assets/011_secret_alliance/animations/coalition_closure_warning/previews/coalition_closure_warning_preview.gif`
- Static fallback sprite: `GFX_011_secret_alliance_coalition_closure_warning`
- Static fallback: `gfx/interface/011_secret_alliance/coalition_closure_warning_static.dds`

The animation is frame-authored: every source frame is a separate generated visual state. The fallback is registered alongside it but is not used as a transform-only substitute for the animation.

## Achievement art

The six icon triplets are registered in `interface/chaosx_achievements.gfx`. Each root below has normal, `_grey`, and `_not_eligible` sprites and matching DDS files under `gfx/achievements/`.

- `GFX_achievement_011_secret_alliance_the_empty_chair`
- `GFX_achievement_011_secret_alliance_every_thread`
- `GFX_achievement_011_secret_alliance_their_man_in_the_room`
- `GFX_achievement_011_secret_alliance_divide_the_table`
- `GFX_achievement_011_secret_alliance_surrounded_not_buried`
- `GFX_achievement_011_secret_alliance_two_giants_one_grave`

## Reveal audio

- Unique audio ID: `43`
- Work: `Revelation` by William Paris Chambers
- Performance: United States Marine Band, directed by Col. John R. Bourgeois
- Recording status: United States federal-government public-domain recording, documented in the audio handoff
- Final music: `music/011_secret_alliance/super_event_43_public_reveal.ogg`
- Final sound mirror: `sound/011_secret_alliance/super_event_43_public_reveal.wav`
- Sound source ID: `chaosx_super_event_secret_alliance_public_reveal_track`
- Settings-aware variants: `chaosx_super_event_43_{0_5,1_0,1_5,2_0,2_5,3_0}` and matching sound effects
- Source preservation: `docs/assets/011_secret_alliance/source_audio/revelation_us_marine_band_commons_source.ogg`
- Music catalogue: `music/chaosx_music_track_list.html` records The Pact Unmasked, audio ID `43`, `Revelation`, the United States Marine Band performance, duration `01:26`, and verified public-domain status

The package is unique to Event 011. No reused track, generated tone, placeholder, or unlicensed audio remains.

## Completion evidence

The asset validation covers final dimensions, single-mip BGRA/B8G8R8A8 DDS output, transparency, sheet slicing, distinct animation frames, six achievement triplets, and absence of visible chroma-key residue. The source and processed contact sheets are under `docs/assets/011_secret_alliance/contact_sheets/`.
