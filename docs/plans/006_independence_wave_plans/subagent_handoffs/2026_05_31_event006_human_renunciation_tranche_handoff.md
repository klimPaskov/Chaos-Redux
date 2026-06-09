# Event 006 Human Renunciation Tranche Handoff

Implemented a bounded Human Renunciation route, achievement, and super-event package for Event 006 Independence Wave. This tranche does not claim full Event 006 completion.

## Gameplay and UI Files Changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/national_focus/006_independence_wave_focus.txt`
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

## Added Route and Achievement IDs

- Focus: `independence_wave_no_appeal_to_mankind`
- Congress decision: `independence_wave_bind_strange_cooperation`
- Trigger helpers:
  - `has_independence_wave_human_renunciation_power_base`
  - `can_independence_wave_bind_strange_cooperation`
  - `can_independence_wave_show_human_renunciation_super_event`
- Effect helpers:
  - `independence_wave_focus_no_appeal_to_mankind`
  - `independence_wave_bind_strange_cooperation_effect`
  - `independence_wave_show_human_renunciation_super_event`
- Achievement: `cr_human_renunciation`
- Super-event slot: `53`

## Behavior

The revealed strange route now has a doctrine finisher after `independence_wave_border_office_of_absence`. It requires Event 006 strange reveal, enough controlled states, and no public-registry restoration. Completing it marks `chaosx_iw_anti_mankind_route_locked` and `chaosx_iw_human_renunciation_doctrine`.

The New States Congress can then bind strange cooperation with another independent Event 006 strange country. The link marks `chaosx_iw_strange_cooperation_link` on both sides and re-checks the Human Renunciation super-event gate.

The `cr_human_renunciation` achievement requires Event 006 independent strange origin, doctrine lock, doctrine finisher proof, strange cooperation, enough controlled states, no public-registry restoration, and no world-end bypass shortcut.

## Super-Event Package

- Sprite: `GFX_super_event_independence_wave_human_renunciation`
- Image: `gfx/super_events/super_event_independence_wave_human_renunciation.dds`
- Music: `music/super_event_independence_wave_human_renunciation.ogg`
- Sound channel: `sound/chaosx_super_event_independence_wave_human_renunciation.wav`
- Sound definition: `chaosx_super_event_independence_wave_human_renunciation_track`
- Music ids: `chaosx_super_event_53_0_5` through `chaosx_super_event_53_3_0`
- Sound ids: `chaosx_super_event_53_sound_0_5` through `chaosx_super_event_53_sound_3_0`
- Text keys: `super_event.53.t`, `.q`, `.a`, `.d`

## Asset and Research Handoffs Used

- `2026_05_31_event006_human_renunciation_icon_handoff.md`
- `2026_05_31_event006_human_renunciation_super_event_text_handoff.md`
- `2026_05_31_event006_human_renunciation_super_event_audio_handoff.md`
- `2026_05_31_event006_human_renunciation_super_event_image_handoff.md`

The achievement icon, super-event image, and audio files were created by subagents. No country flag assets were needed or edited.

## Validation

- Brace balance passed for touched script, interface, localisation-helper, music, and sound files.
- Unsupported raw inclusive operator scan found no `<=` or `>=` in touched Event 006 surfaces.
- Localisation BOM checks passed for touched localisation files.
- No `:0` localisation keys were found in touched localisation files.
- `git diff --check` passed for the touched Event 006 tranche paths.
- `identify`/`file` validated:
  - `cr_human_renunciation` PNG/DDS triplet at `64x64`
  - Human Renunciation super-event PNG/DDS at `457x328`
- `ffprobe` validated Human Renunciation OGG and WAV as stereo `44100 Hz`, duration `83.035057`.

## Remaining Work

- League-war achievement and a real war/peace victory proof system remain follow-up work.
- Broader Event 006 completion still needs the queued package depth, remaining super-events, catalog/spreadsheet alignment, final audits, and unresolved improvement-loop follow-up items.
- The audio subagent created commit `e639ab0e` for the Human Renunciation audio package. The parent tranche is not committed because the Event 006 goal remains incomplete and the worktree contains mixed prior Event 005/Event 006 changes.
