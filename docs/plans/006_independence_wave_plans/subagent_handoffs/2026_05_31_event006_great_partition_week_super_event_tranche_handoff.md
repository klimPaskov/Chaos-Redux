# Event 006 Great Partition Week Super-Event Tranche Handoff

## Scope

Implemented the Event 006 `Great Partition Week` super-event package for high-chaos mass-wave release proof.

No country flags, country files, history files, or Event 005 files were edited. Generated art used neutral map pins and did not create country flag assets.

## Files changed

- `events/006_independence_wave.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `interface/chaosx_super_events.gfx`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_music_l_english.yml`
- `music/chaosx_super_event_music.txt`
- `music/chaosx_super_event_music.asset`
- `sound/chaosx_sound.asset`
- `docs/events/006_independence_wave.md`
- `docs/super_events/super_event_audio_packages.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md`

## Files created by subagents

- `gfx/super_events/super_event_independence_wave_great_partition_week.dds`
- `music/super_event_independence_wave_great_partition_week.ogg`
- `sound/chaosx_super_event_independence_wave_great_partition_week.wav`
- `docs/assets/006_independence_wave/super_events/great_partition_week/`
- `docs/plans/006_independence_wave_plans/source_audio/2026_05_31_fma_loyalty_freak_music_waiting_tttt_source.mp3`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_great_partition_week_super_event_text_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_great_partition_week_super_event_image_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_great_partition_week_super_event_audio_handoff.md`

## Identifiers

- Super-event slot: `56`
- Constant: `constant:independence_wave_super_event.great_partition_week`
- Trigger: `can_independence_wave_show_great_partition_week_super_event`
- Effect: `independence_wave_show_great_partition_week_super_event`
- Current-wave proof flags: `independence_wave_current_wave_special_package`, `independence_wave_current_wave_major_host_partitioned`
- Sprite: `GFX_super_event_independence_wave_great_partition_week`
- Image: `gfx/super_events/super_event_independence_wave_great_partition_week.dds`
- Music ids: `chaosx_super_event_56_0_5` through `chaosx_super_event_56_3_0`
- Soundeffects: `chaosx_super_event_56_sound_0_5` through `chaosx_super_event_56_sound_3_0`
- Sound track: `chaosx_super_event_independence_wave_great_partition_week_track`
- Localisation: `super_event.56.t`, `.q`, `.a`, `.d`

## Behavior

The resolver clears current-wave special-package and major-host partition proof before each Event 006 wave. Successful releases set the special-package proof when they carry city, railway, historical-return, local-polity, or strange package signals. Hosts set major partition proof when a major loses at least four releases in that wave while remaining alive.

After the release loop, slot `56` can fire only when the current wave is chaos tier IV or V, releases at least eight countries, includes a special package, and either affects three hosts or partitions a major host. The gate also blocks world-end bypass state and repeats.

## Validation

- Brace balance is zero for touched event, script, interface, music, and sound files.
- No `<=` or `>=` operators were found in touched Event 006 script, localisation, interface, music, sound, or docs files.
- `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/chaosx_music_l_english.yml` both retain UTF-8 BOM (`efbbbf`).
- No `:0` localisation keys were found in the touched localisation files.
- `git diff --check` passed.
- `gfx/super_events/super_event_independence_wave_great_partition_week.dds` and the processed PNG both validate at `457x328`.
- `music/super_event_independence_wave_great_partition_week.ogg` probes as Ogg audio with duration `174.567007`.
- `sound/chaosx_super_event_independence_wave_great_partition_week.wav` probes as WAV audio with duration `174.567007`.
- Final image, music, sound, asset manifest, and GFX handoff files are present and non-empty.

## Remaining gaps

First Impossible State and The Rump That Endures remain unwired Event 006 super-event candidates. Event 006 overall remains incomplete because package depth, scripted GUI/value display, catalog alignment, final audits, and remaining package/formable surfaces are still queued.
