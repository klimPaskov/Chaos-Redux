# Event 006 League War Tranche Handoff

Date: 2026-05-31

## Scope

Implemented the Event 006 League War achievement and super-event package as a bounded tranche.

This pass does not touch country flag assets. It adds one achievement icon package, one super-event image package, one audio package, and the script wiring needed to prove a real League War lifecycle.

## Gameplay Identifiers

- Achievement: `cr_league_war_victory`
- Achievement title: `The Charter Held`
- Super-event slot: `54`
- Super-event title: `The Charter Is Armed`
- Script constant: `independence_wave_super_event.league_war`
- Member threshold constant: `independence_wave_achievement.league_war_members_required`
- War-start flags and targets:
  - `chaosx_iw_league_war_active`
  - `chaosx_iw_league_war_active_founder`
  - `chaosx_iw_league_war_enemy_target`
  - `event_target:chaosx_iw_league_war_founder`
  - `event_target:chaosx_iw_league_war_enemy`
- Victory flags:
  - `chaosx_iw_league_war_victory_confirmed`
  - `chaosx_iw_league_war_founders_remained_free`

## Behavior

`common/on_actions/006_independence_wave_on_actions.txt` records a League War when an independent Event 006 League founder with at least four counted league members or mutual guarantees enters a qualifying war against a major, recent host, or patron actor.

The war-start proof uses `on_war_relation_added`. The victory proof uses enemy capitulation or peace-conference loss. The failure proof watches founder/member capitulation, puppet status, and annexation. Puppeting sets `chaosx_iw_puppet_status_ever`; ordinary defeat does not, so puppet tracking remains semantically narrow.

The super-event fires once when the League War is recorded. The achievement requires confirmed victory and founding-member freedom proof.

## Files Changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/on_actions/006_independence_wave_on_actions.txt`
- `common/achievements/chaos_redux_achievements.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `interface/chaosx_achievements.gfx`
- `interface/chaosx_super_events.gfx`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `localisation/english/chaosx_music_l_english.yml`
- `music/chaosx_super_event_music.txt`
- `music/chaosx_super_event_music.asset`
- `sound/chaosx_sound.asset`
- `docs/events/006_independence_wave.md`
- `docs/systems/custom_achievements.md`
- `docs/super_events/super_event_audio_packages.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md`

Asset outputs:

- `gfx/achievements/cr_league_war_victory.dds`
- `gfx/achievements/cr_league_war_victory_grey.dds`
- `gfx/achievements/cr_league_war_victory_not_eligible.dds`
- `gfx/super_events/super_event_independence_wave_league_war.dds`
- `music/super_event_independence_wave_league_war.ogg`
- `sound/chaosx_super_event_independence_wave_league_war.wav`
- `docs/assets/006_independence_wave/achievement_icons/`
- `docs/assets/006_independence_wave/super_events/league_war/`
- `docs/plans/006_independence_wave_plans/source_audio/2026_05_31_sellenick_marche_indienne_us_marine_band_source.ogg`

Subagent handoffs:

- `2026_05_31_event006_league_war_icon_handoff.md`
- `2026_05_31_event006_league_war_super_event_text_handoff.md`
- `2026_05_31_event006_league_war_super_event_image_handoff.md`
- `2026_05_31_event006_league_war_super_event_audio_handoff.md`

## Validation

Passed:

- Brace balance for touched script, interface, music, and sound files.
- No `<=` or `>=` in touched script/localisation/docs surfaces checked for this tranche.
- Localisation BOM check for touched English localisation files: all `efbbbf`.
- No `:0` localisation keys in touched English localisation files.
- `git diff --check`.
- Achievement icon DDS triplet: `64x64`.
- League War super-event image DDS and processed PNG: `457x328`.
- League War audio files:
  - `music/super_event_independence_wave_league_war.ogg`: OGG, 113.100363 seconds.
  - `sound/chaosx_super_event_independence_wave_league_war.wav`: WAV, 113.100363 seconds.

## Remaining Risks

- The implementation intentionally records only the first active League War for the one-shot super-event and achievement proof.
- Final Event 006 completion is still not claimed. Remaining Event 006 gaps include the other queued super-events, package depth, GUI/value display, catalog/event-detail alignment, and final completion audit.

## Skills And Subagents

Skills used by parent: `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-super-events`, `chaos-redux-subagents`.

Subagents used with `fork_context=false`:

- `chaosx_icon_artist`
- `chaosx_generated_event_art`
- `chaosx_super_event_text_researcher`
- `chaosx_super_event_audio_researcher`
