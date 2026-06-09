# Event 006 First League Super-Event Wiring Handoff

## Scope completed

- Wired Event 006 First League super-event slot `52`.
- Added `independence_wave_super_event.first_league` and `visible_days` constants.
- Added the `can_independence_wave_show_first_league_super_event` gate.
- Added the `independence_wave_emit_super_event` and `independence_wave_show_first_league_super_event` effects.
- Tightened compact faction admission so ledgered compact members are only added when the founder actually leads a faction.
- Re-checks the one-shot super-event gate when the compact secretariat is recognized.
- Registered image, music, sound, scripted localisation, event localisation, and docs for the First League package.

## Gameplay identifiers

- Super-event id: `52`
- One-shot global flag: `independence_wave_first_league_super_event_fired`
- Image sprite: `GFX_super_event_independence_wave_first_league`
- Music ids: `chaosx_super_event_52_0_5`, `chaosx_super_event_52_1_0`, `chaosx_super_event_52_1_5`, `chaosx_super_event_52_2_0`, `chaosx_super_event_52_2_5`, `chaosx_super_event_52_3_0`
- Sound ids: `chaosx_super_event_52_sound_0_5`, `chaosx_super_event_52_sound_1_0`, `chaosx_super_event_52_sound_1_5`, `chaosx_super_event_52_sound_2_0`, `chaosx_super_event_52_sound_2_5`, `chaosx_super_event_52_sound_3_0`
- Sound definition: `chaosx_super_event_independence_wave_first_league_track`
- Localisation keys: `super_event.52.t`, `super_event.52.q`, `super_event.52.a`, `super_event.52.d`

## Asset and research handoffs reviewed

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_event006_first_league_super_event_text_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_event006_first_league_super_event_image_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_event006_first_league_super_event_audio_handoff.md`

## Validation run

- Brace balance passed for the touched script, `.gfx`, music, and sound asset files.
- Unsupported operator scan found no `<=` or `>=` in the touched Event 006 script and asset files.
- Localisation BOM check passed for `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/chaosx_music_l_english.yml`.
- Localisation `:0` scan found no matches in the touched localisation files.
- Asset file checks confirmed:
  - `gfx/super_events/super_event_independence_wave_first_league.dds`: `457x328` DDS
  - `music/super_event_independence_wave_first_league.ogg`: Vorbis stereo `44100 Hz`
  - `sound/chaosx_super_event_independence_wave_first_league.wav`: PCM stereo `44100 Hz`
- Vanilla precedent check found `add_to_faction = ROOT` patterns in vanilla decision files.
- No files under `gfx/flags`, `common/countries`, or `history/countries` were changed by this wiring pass.

## Remaining risks

- The Event 006 source-spec pack is still incomplete. This handoff covers only the First League super-event tranche.
- The selected Holst audio handoff records a residual longer-term jurisdiction caveat outside U.S. and life-plus-70 contexts.
- Broad final audits, spreadsheet alignment, remaining country packages, scripted GUI work, animations, and closure improvement-loop review remain outstanding.
