# Event 011 Secret Alliance GFX handoff

Scope note: this handoff records the final Event 011 sprites wired by the parent implementation, including generated event art, Dossier Board assets, static icons, achievement icons, and imagegen-backed animation sheets.

Primary feature `.gfx` file for decisions, ideas, and icon-like UI sprites: `interface/011_secret_alliance.gfx`
Achievement `.gfx` file: `interface/chaosx_achievements.gfx`

## Event images and Dossier Board sprites

| Sprite | Final DDS path | Notes |
| --- | --- | --- |
| `GFX_report_event_secret_alliance_meeting` | `gfx/event_pictures/011_secret_alliance/report_event_secret_alliance_meeting.dds` | hidden compact report |
| `GFX_report_event_secret_alliance_courier` | `gfx/event_pictures/011_secret_alliance/report_event_secret_alliance_courier.dds` | expansion report |
| `GFX_report_event_secret_alliance_sabotage` | `gfx/event_pictures/011_secret_alliance/report_event_secret_alliance_sabotage.dds` | patron pressure report |
| `GFX_news_event_secret_alliance_reveal` | `gfx/event_pictures/011_secret_alliance/news_event_secret_alliance_reveal.dds` | public reveal news |
| `GFX_super_event_secret_alliance_reveal` | `gfx/super_events/super_event_secret_alliance_reveal.dds` | super-event slot `28` |
| `GFX_secret_alliance_board_bg` | `gfx/interface/secret_alliance/secret_alliance_board_bg.dds` | `620x270` Dossier Board panel |
| `GFX_secret_alliance_member_unknown` | `gfx/interface/secret_alliance/secret_alliance_member_unknown.dds` | Dossier Board member state |
| `GFX_secret_alliance_member_known` | `gfx/interface/secret_alliance/secret_alliance_member_known.dds` | Dossier Board member state |
| `GFX_secret_alliance_evidence_meter` | `gfx/interface/secret_alliance/secret_alliance_evidence_meter.dds` | base meter, with `25`, `50`, `75`, and `100` fill variants |
| `GFX_secret_alliance_pressure_meter` | `gfx/interface/secret_alliance/secret_alliance_pressure_meter.dds` | base meter, with `25`, `50`, `75`, and `100` fill variants |
| `GFX_secret_alliance_preparedness_meter` | `gfx/interface/secret_alliance/secret_alliance_preparedness_meter.dds` | base meter, with `25`, `50`, `75`, and `100` fill variants |

## Decision category and decision icons

| Sprite | Final DDS path | Size |
| --- | --- | --- |
| `GFX_decision_category_secret_alliance_dossier` | `gfx/interface/decisions/secret_alliance/decision_category_secret_alliance_dossier.dds` | `52x40` |
| `GFX_decision_secret_alliance_dossier` | `gfx/interface/decisions/secret_alliance/decision_secret_alliance_dossier.dds` | `32x32` |
| `GFX_decision_secret_alliance_trace_pouches` | `gfx/interface/decisions/secret_alliance/decision_secret_alliance_trace_pouches.dds` | `32x32` |
| `GFX_decision_secret_alliance_turn_courier` | `gfx/interface/decisions/secret_alliance/decision_secret_alliance_turn_courier.dds` | `32x32` |
| `GFX_decision_secret_alliance_radio_net` | `gfx/interface/decisions/secret_alliance/decision_secret_alliance_radio_net.dds` | `32x32` |
| `GFX_decision_secret_alliance_guard_rail` | `gfx/interface/decisions/secret_alliance/decision_secret_alliance_guard_rail.dds` | `32x32` |
| `GFX_decision_secret_alliance_harden_plants` | `gfx/interface/decisions/secret_alliance/decision_secret_alliance_harden_plants.dds` | `32x32` |
| `GFX_decision_secret_alliance_quiet_talks` | `gfx/interface/decisions/secret_alliance/decision_secret_alliance_quiet_talks.dds` | `32x32` |
| `GFX_decision_secret_alliance_exit_offer` | `gfx/interface/decisions/secret_alliance/decision_secret_alliance_exit_offer.dds` | `32x32` |
| `GFX_decision_secret_alliance_safehouses` | `gfx/interface/decisions/secret_alliance/decision_secret_alliance_safehouses.dds` | `32x32` |
| `GFX_decision_secret_alliance_war_case` | `gfx/interface/decisions/secret_alliance/decision_secret_alliance_war_case.dds` | `32x32` |

Suggested snippet:

```txt
spriteTypes = {
	spriteType = { name = "GFX_decision_category_secret_alliance_dossier" texturefile = "gfx/interface/decisions/secret_alliance/decision_category_secret_alliance_dossier.dds" }
	spriteType = { name = "GFX_decision_secret_alliance_dossier" texturefile = "gfx/interface/decisions/secret_alliance/decision_secret_alliance_dossier.dds" }
	spriteType = { name = "GFX_decision_secret_alliance_trace_pouches" texturefile = "gfx/interface/decisions/secret_alliance/decision_secret_alliance_trace_pouches.dds" }
	spriteType = { name = "GFX_decision_secret_alliance_turn_courier" texturefile = "gfx/interface/decisions/secret_alliance/decision_secret_alliance_turn_courier.dds" }
	spriteType = { name = "GFX_decision_secret_alliance_radio_net" texturefile = "gfx/interface/decisions/secret_alliance/decision_secret_alliance_radio_net.dds" }
	spriteType = { name = "GFX_decision_secret_alliance_guard_rail" texturefile = "gfx/interface/decisions/secret_alliance/decision_secret_alliance_guard_rail.dds" }
	spriteType = { name = "GFX_decision_secret_alliance_harden_plants" texturefile = "gfx/interface/decisions/secret_alliance/decision_secret_alliance_harden_plants.dds" }
	spriteType = { name = "GFX_decision_secret_alliance_quiet_talks" texturefile = "gfx/interface/decisions/secret_alliance/decision_secret_alliance_quiet_talks.dds" }
	spriteType = { name = "GFX_decision_secret_alliance_exit_offer" texturefile = "gfx/interface/decisions/secret_alliance/decision_secret_alliance_exit_offer.dds" }
	spriteType = { name = "GFX_decision_secret_alliance_safehouses" texturefile = "gfx/interface/decisions/secret_alliance/decision_secret_alliance_safehouses.dds" }
	spriteType = { name = "GFX_decision_secret_alliance_war_case" texturefile = "gfx/interface/decisions/secret_alliance/decision_secret_alliance_war_case.dds" }
}
```

## Idea icons and icon-like UI sprites

| Sprite | Final DDS path | Size | Notes |
| --- | --- | --- | --- |
| `GFX_idea_secret_alliance_coldness` | `gfx/interface/ideas/secret_alliance/idea_secret_alliance_coldness.dds` | `64x64` | spirit icon |
| `GFX_idea_secret_alliance_subversion` | `gfx/interface/ideas/secret_alliance/idea_secret_alliance_subversion.dds` | `64x64` | spirit icon |
| `GFX_idea_secret_alliance_counter_office` | `gfx/interface/ideas/secret_alliance/idea_secret_alliance_counter_office.dds` | `64x64` | spirit icon |
| `GFX_idea_secret_alliance_public_hostility` | `gfx/interface/ideas/secret_alliance/idea_secret_alliance_public_hostility.dds` | `64x64` | spirit icon |
| `GFX_secret_alliance_pact_emblem` | `gfx/interface/secret_alliance/secret_alliance_pact_emblem.dds` | `64x64` proposed | matrix did not specify faction-logo width, this pass kept the emblem in icon-like UI scope |
| `GFX_secret_alliance_founder_badge` | `gfx/interface/secret_alliance/secret_alliance_founder_badge.dds` | `32x32` proposed | dossier-board badge |
| `GFX_secret_alliance_patron_badge` | `gfx/interface/secret_alliance/secret_alliance_patron_badge.dds` | `32x32` proposed | dossier-board badge |
| `GFX_secret_alliance_wavering_badge` | `gfx/interface/secret_alliance/secret_alliance_wavering_badge.dds` | `32x32` proposed | dossier-board badge |

## Achievement icons

Use the unprefixed DDS files that match the Event 011 achievement ids. They were overwritten from the imagegen-backed icon package after review so the live `gfx/achievements/` filenames match `common/achievements/chaos_redux_achievements.txt`.

Per achievement key `<key>`, wire:

```txt
spriteType = { name = "GFX_achievement_<key>" texturefile = "gfx/achievements/<key>.dds" }
spriteType = { name = "GFX_achievement_<key>_grey" texturefile = "gfx/achievements/<key>_grey.dds" }
spriteType = { name = "GFX_achievement_<key>_not_eligible" texturefile = "gfx/achievements/<key>_not_eligible.dds" }
```

Event 011 keys:

- `secret_alliance_open_file`
- `secret_alliance_empty_chairs`
- `secret_alliance_no_one_came`
- `secret_alliance_border_knife`
- `secret_alliance_patron_exposed`
- `secret_alliance_counter_pact`
- `secret_alliance_alone_against_room`
- `secret_alliance_last_signature`
- `secret_alliance_clean_reveal`
- `secret_alliance_war_case`

## Parent-completed animation work

The icon worker did not complete these during its static pass. The parent implementation pass later replaced the discarded drafts with imagegen source sheets, processed frames, preview GIFs, static fallbacks, and validated horizontal DDS sheets. They are wired through `interface/011_secret_alliance.gfx`.

| Sprite | Frames | Final DDS path | Static fallback |
| --- | ---: | --- | --- |
| `GFX_secret_alliance_radio_pulse` | 8 | `gfx/interface/animated/secret_alliance/secret_alliance_radio_pulse_sheet.dds` | `GFX_secret_alliance_radio_pulse_static` |
| `GFX_secret_alliance_seal_crack` | 10 | `gfx/interface/animated/secret_alliance/secret_alliance_seal_crack_sheet.dds` | `GFX_secret_alliance_seal_crack_static` |
| `GFX_secret_alliance_border_warning` | 8 | `gfx/interface/animated/secret_alliance/secret_alliance_border_warning_sheet.dds` | `GFX_secret_alliance_border_warning_static` |
