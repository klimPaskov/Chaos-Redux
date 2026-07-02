# Event 011 Secret Alliance Icon and Animation Manifest

Date: `2026-07-01`

Scope:

- Generated final decision/category icons, idea icons, achievement triplets, and animated UI sidecar assets for Event 011 Secret Alliance.
- Used `$imagegen` generated source atlases and source sheets, copied from `C:/Users/klimp/.codex/generated_images/019f1e69-9c4c-72c2-a724-92a6608ec517/`.
- Local processing was limited to copying source art, grid slicing, chroma-key alpha cleanup, crop/fit/resize, achievement disabled variants, frame-sheet assembly, GIF/contact previews, DDS export, and validation.
- Did not edit `.gfx`, `.gui`, gameplay, localisation, achievements script, decisions, ideas, focus, spreadsheet, or event files.

Reference folders inspected:

- `.agents/skills/chaos-redux-event-assets/assets/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/achievements`
- Existing Event 014/015 icon and achievement package folders.
- Existing Event 013/014/015 animated asset package folders.

Reference and review sheets:

- `docs/assets/011_secret_alliance/reference_contact_sheets/ref_decisions.png`
- `docs/assets/011_secret_alliance/reference_contact_sheets/ref_ideas.png`
- `docs/assets/011_secret_alliance/reference_contact_sheets/ref_achievements.png`
- `docs/assets/011_secret_alliance/generated_source_review.png`
- `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_decision_icons_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_idea_icons_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_achievement_icons_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_achievement_variants_contact.png`

Validation:

- `docs/assets/011_secret_alliance/validation_summary.txt`
- 50 runtime DDS dimension/alpha checks passed.
- Decision/category DDS files are `32x32` with transparent corners.
- Idea DDS files are `64x64` with transparent corners.
- Achievement DDS triplets are `64x64` and fully opaque.
- Animated sheet DDS files match `frame_width * 8` by `frame_height`; static fallbacks match their frame sizes.

## Source Atlases

| Source | Selected generated file | Use |
| --- | --- | --- |
| `source_png/secret_alliance_decision_atlas_source.png` | `ig_032a3de12c03035c016a453a3fcd548191b128a232049d9db8.png` | 9 decision/category icon sources |
| `source_png/secret_alliance_idea_atlas_source.png` | `ig_0026b4018b878c25016a453a7d06b08191a53263787bc8a085.png` | 7 idea icon sources |
| `source_png/secret_alliance_achievement_atlas_source.png` | `ig_0026b4018b878c25016a453ab6bbb48191aff1e7c65f73b6aa.png` | 8 achievement completed icon sources |
| `source_png/secret_alliance_evidence_pulse_sheet_source.png` | `ig_0026b4018b878c25016a453b0ba68c8191bd812cac695ebb85.png` | 8 evidence pulse source frames |
| `source_png/secret_alliance_readiness_warning_sheet_source.png` | `ig_0026b4018b878c25016a453b3cedc88191b35d354ab1a1846c.png` | 8 readiness warning source frames |
| `source_png/secret_alliance_exposed_card_glow_sheet_source.png` | `ig_0026b4018b878c25016a453b6f9510819190c903c6a97c8b5a.png` | 8 exposed card glow source frames |
| `source_png/secret_alliance_war_countdown_ticker_sheet_source.png` | `ig_0026b4018b878c25016a453bb9750881918faeac129195cc3a.png` | 8 war countdown ticker source frames |
| `source_png/secret_alliance_hidden_protocol_overlay_sheet_source.png` | `ig_0026b4018b878c25016a453c0ad54881919526e488d71569b3.png` | 8 hidden protocol overlay source frames |

## Decision And Category Icons

Runtime folder: `gfx/interface/decisions/011_secret_alliance/`

| Sprite | Source PNG | Processed PNG | Runtime DDS | Size | Status |
| --- | --- | --- | --- | --- | --- |
| `GFX_decision_category_secret_alliance_dossier` | `docs/assets/011_secret_alliance/source_png/decision_category_secret_alliance_dossier_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_category_secret_alliance_dossier.png` | `gfx/interface/decisions/011_secret_alliance/decision_category_secret_alliance_dossier.dds` | `32x32` | complete |
| `GFX_decision_secret_alliance_courier` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_courier_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_courier.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_courier.dds` | `32x32` | complete |
| `GFX_decision_secret_alliance_rail_guard` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_rail_guard_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_rail_guard.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_rail_guard.dds` | `32x32` | complete |
| `GFX_decision_secret_alliance_expose` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_expose_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_expose.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_expose.dds` | `32x32` | complete |
| `GFX_decision_secret_alliance_backchannel` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_backchannel_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_backchannel.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_backchannel.dds` | `32x32` | complete |
| `GFX_decision_secret_alliance_border_watch` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_border_watch_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_border_watch.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_border_watch.dds` | `32x32` | complete |
| `GFX_decision_secret_alliance_factory_shield` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_factory_shield_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_factory_shield.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_factory_shield.dds` | `32x32` | complete |
| `GFX_decision_secret_alliance_false_leak` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_false_leak_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_false_leak.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_false_leak.dds` | `32x32` | complete |
| `GFX_decision_secret_alliance_strike_first` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_strike_first_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_strike_first.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_strike_first.dds` | `32x32` | complete |

## Idea Icons

Runtime folder: `gfx/interface/ideas/011_secret_alliance/`

| Sprite | Source PNG | Processed PNG | Runtime DDS | Size | Status |
| --- | --- | --- | --- | --- | --- |
| `GFX_idea_secret_alliance_dossier_pressure` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_dossier_pressure_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_dossier_pressure.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_dossier_pressure.dds` | `64x64` | complete |
| `GFX_idea_secret_alliance_counter_network` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_counter_network_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_counter_network.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_counter_network.dds` | `64x64` | complete |
| `GFX_idea_secret_alliance_protocol_discipline` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_protocol_discipline_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_protocol_discipline.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_protocol_discipline.dds` | `64x64` | complete |
| `GFX_idea_secret_alliance_patron_liaisons` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_patron_liaisons_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_patron_liaisons.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_patron_liaisons.dds` | `64x64` | complete |
| `GFX_idea_secret_alliance_exposed_signatory` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_exposed_signatory_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_exposed_signatory.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_exposed_signatory.dds` | `64x64` | complete |
| `GFX_idea_secret_alliance_war_coordination` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_war_coordination_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_war_coordination.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_war_coordination.dds` | `64x64` | complete |
| `GFX_idea_secret_alliance_credibility_restored` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_credibility_restored_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_credibility_restored.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_credibility_restored.dds` | `64x64` | complete |

## Achievements

Runtime folder: `gfx/achievements/`

Each achievement has completed, `_grey`, and `_not_eligible` DDS variants.

| Achievement id | Source PNG | Runtime DDS triplet | Size | Status |
| --- | --- | --- | --- | --- |
| `secret_alliance_empty_chair` | `docs/assets/011_secret_alliance/source_png/secret_alliance_empty_chair_source.png` | `gfx/achievements/secret_alliance_empty_chair.dds`, `gfx/achievements/secret_alliance_empty_chair_grey.dds`, `gfx/achievements/secret_alliance_empty_chair_not_eligible.dds` | `64x64` | complete |
| `secret_alliance_all_names` | `docs/assets/011_secret_alliance/source_png/secret_alliance_all_names_source.png` | `gfx/achievements/secret_alliance_all_names.dds`, `gfx/achievements/secret_alliance_all_names_grey.dds`, `gfx/achievements/secret_alliance_all_names_not_eligible.dds` | `64x64` | complete |
| `secret_alliance_three_knocks` | `docs/assets/011_secret_alliance/source_png/secret_alliance_three_knocks_source.png` | `gfx/achievements/secret_alliance_three_knocks.dds`, `gfx/achievements/secret_alliance_three_knocks_grey.dds`, `gfx/achievements/secret_alliance_three_knocks_not_eligible.dds` | `64x64` | complete |
| `secret_alliance_lone_target` | `docs/assets/011_secret_alliance/source_png/secret_alliance_lone_target_source.png` | `gfx/achievements/secret_alliance_lone_target.dds`, `gfx/achievements/secret_alliance_lone_target_grey.dds`, `gfx/achievements/secret_alliance_lone_target_not_eligible.dds` | `64x64` | complete |
| `secret_alliance_counter_protocol` | `docs/assets/011_secret_alliance/source_png/secret_alliance_counter_protocol_source.png` | `gfx/achievements/secret_alliance_counter_protocol.dds`, `gfx/achievements/secret_alliance_counter_protocol_grey.dds`, `gfx/achievements/secret_alliance_counter_protocol_not_eligible.dds` | `64x64` | complete |
| `secret_alliance_wrong_room` | `docs/assets/011_secret_alliance/source_png/secret_alliance_wrong_room_source.png` | `gfx/achievements/secret_alliance_wrong_room.dds`, `gfx/achievements/secret_alliance_wrong_room_grey.dds`, `gfx/achievements/secret_alliance_wrong_room_not_eligible.dds` | `64x64` | complete |
| `secret_alliance_no_patrons` | `docs/assets/011_secret_alliance/source_png/secret_alliance_no_patrons_source.png` | `gfx/achievements/secret_alliance_no_patrons.dds`, `gfx/achievements/secret_alliance_no_patrons_grey.dds`, `gfx/achievements/secret_alliance_no_patrons_not_eligible.dds` | `64x64` | complete |
| `secret_alliance_paid_in_promises` | `docs/assets/011_secret_alliance/source_png/secret_alliance_paid_in_promises_source.png` | `gfx/achievements/secret_alliance_paid_in_promises.dds`, `gfx/achievements/secret_alliance_paid_in_promises_grey.dds`, `gfx/achievements/secret_alliance_paid_in_promises_not_eligible.dds` | `64x64` | complete |

## Animated UI Assets

Runtime folder: `gfx/interface/animated/011_secret_alliance/`

| Asset | Static sprite | Animated sprite | Frame count | Frame size | Sheet size | Static DDS | Sheet DDS | Preview |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `secret_alliance_evidence_pulse` | `GFX_secret_alliance_evidence_pulse_static` | `GFX_secret_alliance_evidence_pulse_animated` | 8 | `64x64` | `512x64` | `gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_pulse_static.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_pulse_sheet.dds` | `animations/secret_alliance_evidence_pulse/previews/secret_alliance_evidence_pulse_preview.gif` |
| `secret_alliance_readiness_warning` | `GFX_secret_alliance_readiness_warning_static` | `GFX_secret_alliance_readiness_warning_animated` | 8 | `64x64` | `512x64` | `gfx/interface/animated/011_secret_alliance/secret_alliance_readiness_warning_static.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_readiness_warning_sheet.dds` | `animations/secret_alliance_readiness_warning/previews/secret_alliance_readiness_warning_preview.gif` |
| `secret_alliance_exposed_card_glow` | `GFX_secret_alliance_exposed_card_glow_static` | `GFX_secret_alliance_exposed_card_glow_animated` | 8 | `96x64` | `768x64` | `gfx/interface/animated/011_secret_alliance/secret_alliance_exposed_card_glow_static.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_exposed_card_glow_sheet.dds` | `animations/secret_alliance_exposed_card_glow/previews/secret_alliance_exposed_card_glow_preview.gif` |
| `secret_alliance_war_countdown_ticker` | `GFX_secret_alliance_war_countdown_ticker_static` | `GFX_secret_alliance_war_countdown_ticker_animated` | 8 | `128x32` | `1024x32` | `gfx/interface/animated/011_secret_alliance/secret_alliance_war_countdown_ticker_static.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_war_countdown_ticker_sheet.dds` | `animations/secret_alliance_war_countdown_ticker/previews/secret_alliance_war_countdown_ticker_preview.gif` |
| `secret_alliance_hidden_protocol_overlay` | `GFX_secret_alliance_hidden_protocol_overlay_static` | `GFX_secret_alliance_hidden_protocol_overlay_animated` | 8 | `96x96` | `768x96` | `gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_protocol_overlay_static.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_protocol_overlay_sheet.dds` | `animations/secret_alliance_hidden_protocol_overlay/previews/secret_alliance_hidden_protocol_overlay_preview.gif` |

Blocked assets: none.

Needs user review: none flagged by this pass.
