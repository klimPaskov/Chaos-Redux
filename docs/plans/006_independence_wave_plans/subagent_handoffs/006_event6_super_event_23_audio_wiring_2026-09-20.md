# Event 006 slot-23 audio wiring handoff

Status: implemented at source level on 2026-09-20; whole Event 006 remains HOLD / PARTIAL.

## Decision basis

The user approved the pending project decisions with “i approve everything” on 2026-09-20.

That approval selects *The Enola Foam March* by Peet Hudson / Peter Hudson, the creator's own orchestral recording preserved on Wikimedia Commons under CC BY-SA 4.0.

The approval does not clear the former London Brass Players recording of *A Trumpet Voluntary*, which remains excluded because United States redistribution rights were not verified.

## Source and runtime evidence

- Source: `docs/assets/006_independence_wave/super_events/audio/source/The_Enola_Foam_March.flac`
- Source SHA-256: `34A26DF75C96DCFCE953E400DA9DAD2F4E9B61837EFD87FEF61CBD4B0614D547`
- Source URL: `https://commons.wikimedia.org/wiki/File:The_Enola_Foam_March.flac`
- License URL: `https://creativecommons.org/licenses/by-sa/4.0/`
- Attribution: `Peet Hudson, “The Enola Foam March”; creator's own recording; source: Wikimedia Commons; licensed CC BY-SA 4.0; edited 110-second excerpt by Chaos Redux.`
- Runtime WAV: `sound/006_independence_wave/super_event_23_enola_foam_march_110s.wav`
- Runtime SHA-256: `2892F43CD393F2CA7FEED12FB8A841F9C7C6CA8784F28E2A39DC0AD3B9CECBFF`
- Runtime profile: PCM S16LE, stereo, 44.1 kHz, 110.000000 seconds, approximately -18.01 LUFS and -2.00 dBTP.

No perceptual human audition or live-game playback claim is made by this handoff.

## Source wiring

- `sound/chaosx_sound.asset` defines `chaosx_super_event_23_track` and the six settings-volume wrappers from `chaosx_super_event_23_sound_0_5` through `chaosx_super_event_23_sound_3_0`.
- The first durable formal league threshold calls `independence_wave_publish_league_formation` from `independence_wave_mark_league_durable` in `common/scripted_effects/006_independence_wave_effects.txt`.
- The publisher records Event 006 history payload `independence_wave_league_super_event.history_payload` and submits display slot 23 plus audio ID 23 to `natural_disaster_emit_super_event`.
- Event Log title and detail selectors use `independence_wave.history.league_formation.title` and `independence_wave.history.league_formation.description`.
- `music/chaosx_music_track_list.html` contains the slot-23 catalogue row with source, license, attribution, duration, and runtime hash.

## Validation

- `ffprobe` confirms PCM signed 16-bit little-endian audio, stereo, 44.1 kHz, and 110.000000 seconds.
- The copied runtime hash matches the prepared final derivative.
- `python -B .tools/audit_localisation_static.py` reports zero parse errors, duplicate keys, missing BOMs, encoding artifacts, or undefined Event roots; its repository-wide undefined-binding and dead-key findings are pre-existing baseline findings.
- Event 006 allocator, flag, and country-API audits pass after the source change.
- Read-only `hoi4.event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and zero skipped sources; the artifact records the workspace-wide deferred helper/lifecycle analysis boundary.
- The matching read-only `hoi4.event_render` overview returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics and zero skipped sources; it remains structural evidence rather than live execution proof.

## Remaining limits

This wiring tranche does not claim whole-event completion, complete package admission, typed probability evidence, dynamic scripted-GUI acceptance, FSM portrait rights, or live-game validation.

The ignored `docs/assets/` production manifest and generated-scene manifests were updated in the local event workspace and remain uncommitted by repository policy.
