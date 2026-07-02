# Event 011 Secret Alliance Icon and Animation Handoff

Date: `2026-07-01`

Agent scope:

- Produced final generated icon and animation sidecar assets only.
- Used `chaos-redux-event-assets`, `chaos-redux-frame-animation`, and `$imagegen`.
- Did not edit `.gfx`, `.gui`, gameplay, localisation, achievement definitions, decision files, idea files, event files, focus files, spreadsheets, or vanilla files.

Package roots:

- Asset package: `docs/assets/011_secret_alliance/`
- Manifest: `docs/assets/011_secret_alliance/manifest.md`
- GFX handoff: `docs/assets/011_secret_alliance/gfx_handoff.md`
- Validation: `docs/assets/011_secret_alliance/validation_summary.txt`
- Processing tool: `docs/assets/011_secret_alliance/_tooling/process_secret_alliance_assets.py`

Reference analysis completed:

- `.agents/skills/chaos-redux-event-assets/assets/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/achievements`
- Existing Event 013/014/015 animated asset package folders.
- Existing Event 014/015 achievement/icon package folders.

Review sheets:

- `docs/assets/011_secret_alliance/reference_contact_sheets/ref_decisions.png`
- `docs/assets/011_secret_alliance/reference_contact_sheets/ref_ideas.png`
- `docs/assets/011_secret_alliance/reference_contact_sheets/ref_achievements.png`
- `docs/assets/011_secret_alliance/generated_source_review.png`
- `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_decision_icons_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_idea_icons_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_achievement_icons_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_achievement_variants_contact.png`

## Runtime Icon Files

Decision/category icons, all `32x32`, transparent:

| Sprite | Runtime DDS |
| --- | --- |
| `GFX_decision_category_secret_alliance_dossier` | `gfx/interface/decisions/011_secret_alliance/decision_category_secret_alliance_dossier.dds` |
| `GFX_decision_secret_alliance_courier` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_courier.dds` |
| `GFX_decision_secret_alliance_rail_guard` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_rail_guard.dds` |
| `GFX_decision_secret_alliance_expose` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_expose.dds` |
| `GFX_decision_secret_alliance_backchannel` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_backchannel.dds` |
| `GFX_decision_secret_alliance_border_watch` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_border_watch.dds` |
| `GFX_decision_secret_alliance_factory_shield` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_factory_shield.dds` |
| `GFX_decision_secret_alliance_false_leak` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_false_leak.dds` |
| `GFX_decision_secret_alliance_strike_first` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_strike_first.dds` |

Idea icons, all `64x64`, transparent:

| Sprite | Runtime DDS |
| --- | --- |
| `GFX_idea_secret_alliance_dossier_pressure` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_dossier_pressure.dds` |
| `GFX_idea_secret_alliance_counter_network` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_counter_network.dds` |
| `GFX_idea_secret_alliance_protocol_discipline` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_protocol_discipline.dds` |
| `GFX_idea_secret_alliance_patron_liaisons` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_patron_liaisons.dds` |
| `GFX_idea_secret_alliance_exposed_signatory` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_exposed_signatory.dds` |
| `GFX_idea_secret_alliance_war_coordination` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_war_coordination.dds` |
| `GFX_idea_secret_alliance_credibility_restored` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_credibility_restored.dds` |

Achievement triplets, all `64x64`, opaque:

| Achievement id | Completed | Grey | Not eligible |
| --- | --- | --- | --- |
| `secret_alliance_empty_chair` | `gfx/achievements/secret_alliance_empty_chair.dds` | `gfx/achievements/secret_alliance_empty_chair_grey.dds` | `gfx/achievements/secret_alliance_empty_chair_not_eligible.dds` |
| `secret_alliance_all_names` | `gfx/achievements/secret_alliance_all_names.dds` | `gfx/achievements/secret_alliance_all_names_grey.dds` | `gfx/achievements/secret_alliance_all_names_not_eligible.dds` |
| `secret_alliance_three_knocks` | `gfx/achievements/secret_alliance_three_knocks.dds` | `gfx/achievements/secret_alliance_three_knocks_grey.dds` | `gfx/achievements/secret_alliance_three_knocks_not_eligible.dds` |
| `secret_alliance_lone_target` | `gfx/achievements/secret_alliance_lone_target.dds` | `gfx/achievements/secret_alliance_lone_target_grey.dds` | `gfx/achievements/secret_alliance_lone_target_not_eligible.dds` |
| `secret_alliance_counter_protocol` | `gfx/achievements/secret_alliance_counter_protocol.dds` | `gfx/achievements/secret_alliance_counter_protocol_grey.dds` | `gfx/achievements/secret_alliance_counter_protocol_not_eligible.dds` |
| `secret_alliance_wrong_room` | `gfx/achievements/secret_alliance_wrong_room.dds` | `gfx/achievements/secret_alliance_wrong_room_grey.dds` | `gfx/achievements/secret_alliance_wrong_room_not_eligible.dds` |
| `secret_alliance_no_patrons` | `gfx/achievements/secret_alliance_no_patrons.dds` | `gfx/achievements/secret_alliance_no_patrons_grey.dds` | `gfx/achievements/secret_alliance_no_patrons_not_eligible.dds` |
| `secret_alliance_paid_in_promises` | `gfx/achievements/secret_alliance_paid_in_promises.dds` | `gfx/achievements/secret_alliance_paid_in_promises_grey.dds` | `gfx/achievements/secret_alliance_paid_in_promises_not_eligible.dds` |

## Animated UI Assets

All animations have eight generated source frames, eight processed frames, a horizontal sheet PNG, final sheet DDS, static fallback PNG/DDS, contact sheet, preview GIF, `brief.md`, and `frame_plan.md`.

| Asset | Static sprite | Animated sprite | Frame count | Frame size | Sheet size | FPS | Static DDS | Sheet DDS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `secret_alliance_evidence_pulse` | `GFX_secret_alliance_evidence_pulse_static` | `GFX_secret_alliance_evidence_pulse_animated` | 8 | `64x64` | `512x64` | 8 | `gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_pulse_static.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_pulse_sheet.dds` |
| `secret_alliance_readiness_warning` | `GFX_secret_alliance_readiness_warning_static` | `GFX_secret_alliance_readiness_warning_animated` | 8 | `64x64` | `512x64` | 8 | `gfx/interface/animated/011_secret_alliance/secret_alliance_readiness_warning_static.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_readiness_warning_sheet.dds` |
| `secret_alliance_exposed_card_glow` | `GFX_secret_alliance_exposed_card_glow_static` | `GFX_secret_alliance_exposed_card_glow_animated` | 8 | `96x64` | `768x64` | 8 | `gfx/interface/animated/011_secret_alliance/secret_alliance_exposed_card_glow_static.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_exposed_card_glow_sheet.dds` |
| `secret_alliance_war_countdown_ticker` | `GFX_secret_alliance_war_countdown_ticker_static` | `GFX_secret_alliance_war_countdown_ticker_animated` | 8 | `128x32` | `1024x32` | 8 | `gfx/interface/animated/011_secret_alliance/secret_alliance_war_countdown_ticker_static.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_war_countdown_ticker_sheet.dds` |
| `secret_alliance_hidden_protocol_overlay` | `GFX_secret_alliance_hidden_protocol_overlay_static` | `GFX_secret_alliance_hidden_protocol_overlay_animated` | 8 | `96x96` | `768x96` | 8 | `gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_protocol_overlay_static.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_protocol_overlay_sheet.dds` |

Animation package folders:

- `docs/assets/011_secret_alliance/animations/secret_alliance_evidence_pulse/`
- `docs/assets/011_secret_alliance/animations/secret_alliance_readiness_warning/`
- `docs/assets/011_secret_alliance/animations/secret_alliance_exposed_card_glow/`
- `docs/assets/011_secret_alliance/animations/secret_alliance_war_countdown_ticker/`
- `docs/assets/011_secret_alliance/animations/secret_alliance_hidden_protocol_overlay/`

## Suggested Wiring

- Suggested `.gfx` file: `interface/011_secret_alliance.gfx`
- Static animation sprites should be used as fallback sprites when the scripted GUI element is hidden, unsupported, or animation is not active.
- Animated sprites should use `frameAnimatedSpriteType` with `noOfFrames = 8`, `animation_rate_fps = 8`, `looping = yes`, and `play_on_show = yes`.
- Ready-to-copy sprite snippets are in `docs/assets/011_secret_alliance/gfx_handoff.md`.

## Validation Notes

- `docs/assets/011_secret_alliance/validation_summary.txt` reports `50 DDS dimension/alpha checks passed.`
- Visual review passed for generated reference/source/contact sheets and all five animation contact sheets.
- The animation motion is source-frame based: source sheets were generated by `$imagegen`, then sliced into one source PNG per frame. Local processing did not create the visual changes by shifting, scaling, rotating, warping, recoloring, blurring, or filter-only pulsing a single still image.

## Blockers And Review Flags

- Blockers: none.
- Needs user review: none flagged by this pass.
- Uncertainty: target `.gui` file and final state trigger names are implementation-owned and were not inspected in this asset-only pass.
- Dimension note: `96x64`, `128x32`, and `96x96` animated sizes were selected from Event 015 UI-sidecar patterns because the Event 011 parent request did not provide exact dimensions for those three surfaces.
