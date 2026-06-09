# Event 006 First Old Name Super-Event Tranche Handoff

## Scope

Implemented the Event 006 `First Old Name` super-event package for the first historical-return Independence Wave release.

No country flags, country files, history files, or Event 005 files were edited.

## Files changed

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

- `gfx/super_events/super_event_independence_wave_first_old_name.dds`
- `music/super_event_independence_wave_first_old_name.ogg`
- `sound/chaosx_super_event_independence_wave_first_old_name.wav`
- `docs/assets/006_independence_wave/super_events/first_old_name/`
- `docs/plans/006_independence_wave_plans/source_audio/2026_05_31_wikimedia_god_of_our_fathers_usaf_heritage_band_source.mp3`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_first_old_name_super_event_text_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_first_old_name_super_event_image_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_first_old_name_super_event_audio_handoff.md`

## Identifiers

- Super-event slot: `55`
- Constant: `constant:independence_wave_super_event.first_old_name`
- Trigger: `can_independence_wave_show_first_old_name_super_event`
- Effect: `independence_wave_show_first_old_name_super_event`
- Fired from: first `chaosx_iw_historical_return_package` country marked with `chaosx_iw_first_old_name_country`
- Sprite: `GFX_super_event_independence_wave_first_old_name`
- Image: `gfx/super_events/super_event_independence_wave_first_old_name.dds`
- Music ids: `chaosx_super_event_55_0_5` through `chaosx_super_event_55_3_0`
- Soundeffects: `chaosx_super_event_55_sound_0_5` through `chaosx_super_event_55_sound_3_0`
- Sound track: `chaosx_super_event_independence_wave_first_old_name_track`
- Localisation: `super_event.55.t`, `.q`, `.a`, `.d`

## Behavior

When the first valid Event 006 historical-return release is marked, the system sets the existing first-old-name achievement flags and immediately attempts to show the slot-55 super-event. The gate requires Independence Wave origin, historical-return package proof, first-old-name country proof, independence, and no Event 005 origin/successor flags.

The presentation uses `An Old Name Returns`, a Giuseppe Mazzini quote from `To the Young Men of Italy`, generated archive/map-office art, and a public-domain United States Air Force Band recording of `God of Our Fathers`.

## Validation

- Brace balance is zero for touched script, interface, music, and sound files.
- No `<=` or `>=` operators were found in touched Event 006 script, localisation, interface, music, sound, or docs files.
- `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/chaosx_music_l_english.yml` both retain UTF-8 BOM (`efbbbf`).
- No `:0` localisation keys were found in the touched localisation files.
- `git diff --check` passed.
- `gfx/super_events/super_event_independence_wave_first_old_name.dds` and the processed PNG both validate at `457x328`.
- `music/super_event_independence_wave_first_old_name.ogg` probes as Ogg audio with duration `91.428571`.
- `sound/chaosx_super_event_independence_wave_first_old_name.wav` probes as WAV audio with duration `91.428571`.
- Final image, music, sound, asset manifest, and GFX handoff files are present and non-empty.

## Remaining gaps

Great Partition Week, First Impossible State, and The Rump That Endures remain unwired Event 006 super-event candidates. Event 006 overall remains incomplete because package depth, scripted GUI/value display, catalog alignment, final audits, and remaining package/formable surfaces are still queued.
