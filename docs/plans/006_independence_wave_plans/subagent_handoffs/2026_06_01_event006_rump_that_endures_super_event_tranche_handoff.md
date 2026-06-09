# Event 006 Rump That Endures Super-Event Tranche Handoff

## Summary

Implemented `The Rump That Endures` as Event 006 super-event slot `58`.

Gameplay now records each host's pre-wave controlled-state count before the release effect, then checks the surviving host after release. The super-event fires only in chaos tier IV/V when a host that did not begin as a one-state country survives at one or two controlled states after at least four release losses in the current wave. This keeps the Event 006 host-survival rule explicit: the wave can humiliate and shrink a host, but it does not delete it.

## Gameplay Wiring

- Added `independence_wave_prepare_host_wave_tracking`.
- Called the tracking helper before `independence_wave_reserve_host_survival_state` and `release = PREV`.
- Added `can_independence_wave_show_rump_that_endures_super_event`.
- Added `independence_wave_show_rump_that_endures_super_event`.
- `independence_wave_mark_host_aftermath` now checks the slot `58` gate after host aftermath tracking, capital-survival tracking, major-host partition tracking, and the host capital mission activation.
- The trigger excludes the world-end bypass, requires a living host, uses the existing per-wave release-loss count, and uses `independence_wave_host_pre_wave_controlled_states` to reject countries that were already one-state before the wave.

## Presentation Wiring

- Added sprite routing for `GFX_super_event_independence_wave_rump_that_endures`.
- Added scripted localisation routing for image, title, quote, remark, and description for slot `58`.
- Added music assets `chaosx_super_event_58_0_5` through `chaosx_super_event_58_3_0`.
- Added soundeffects `chaosx_super_event_58_sound_0_5` through `chaosx_super_event_58_sound_3_0`.
- Added sound definition `chaosx_super_event_independence_wave_rump_that_endures_track`.
- Added music localisation for all six slot `58` music ids.
- Added super-event localisation keys `super_event.58.t`, `super_event.58.q`, `super_event.58.a`, and `super_event.58.d`.
- Updated Event 006 docs and the super-event audio package documentation.
- Updated the post-focus improvement addendum so it no longer lists Rump as unwired.

## Subagent Handoffs

- Text handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_01_event006_rump_that_endures_super_event_text_handoff.md`
- Image handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_01_event006_rump_that_endures_super_event_image_handoff.md`
- Audio handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_01_event006_rump_that_endures_super_event_audio_handoff.md`

## Assets

- Final image: `gfx/super_events/super_event_independence_wave_rump_that_endures.dds`
- Processed preview: `docs/assets/006_independence_wave/super_events/rump_that_endures/processed_png/super_event_independence_wave_rump_that_endures_457x328.png`
- Image package manifest: `docs/assets/006_independence_wave/super_events/rump_that_endures/manifest.md`
- Final music: `music/super_event_independence_wave_rump_that_endures.ogg`
- Final sound-channel file: `sound/chaosx_super_event_independence_wave_rump_that_endures.wav`
- Preserved audio source: `docs/plans/006_independence_wave_plans/source_audio/2026_06_01_wikimedia_chopin_prelude_op28_no4_porticodoro_source.ogg`

## Text and Rights

- Title: `The Rump That Endures`
- Quote: Edmund Burke, `Reflections on the Revolution in France`
- Button: `The seal is not dead.`
- Audio source: Chopin, `Prelude in E Minor, Op. 28 No. 4`, recording by Porticodoro / SmartCGArt Media Productions via Wikimedia Commons, licensed `CC BY 3.0`.
- Image source mode: generated Event 006 super-event art package, selected variant B.

## Validation

- Brace balance is zero for touched script, GFX, music, and sound files.
- No `<=` or `>=` operators were added.
- Localisation files keep UTF-8 BOM encoding.
- No `:0` localisation keys were added.
- `git diff --check` passes for the touched text files.
- Final DDS identifies as `457x328`.
- Processed PNG identifies as `457x328`.
- Final OGG decodes cleanly with `ffmpeg -v error`.
- Final OGG and WAV both probe at `123.860000s`.
- Rump image, audio, text, and parent tranche handoffs are present.

## Simplifications, Omissions, and Blockers

- No gameplay fallback was used.
- No country flag assets, country files, history files, or Event 005 systems were edited.
- No simplification was made inside this slot-58 tranche.
- A clean standalone commit was not created from the parent workspace because the Event 006 base files are already part of a large dirty/untracked worktree with earlier Event 006 and unrelated Event 005 work. Staging this tranche alone would require separating changes inside files that already contain prior uncommitted work.
