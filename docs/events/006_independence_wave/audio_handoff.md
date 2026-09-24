# Event 006 super-event audio handoff

This document is the durable Event 006 audio handoff for ordinary super-event slots `23` and `24`. It records runtime wiring and provenance already present in the repository. It does not claim perceptual audition or live-game playback.

## Slot 23 — The League of New States

| Field | Value |
| --- | --- |
| Runtime WAV | `sound/006_independence_wave/super_event_23_enola_foam_march_110s.wav` |
| Audio id and base sound | `23`; `chaosx_super_event_23_track` |
| Settings wrappers | `chaosx_super_event_23_sound_0_5`, `chaosx_super_event_23_sound_1_0`, `chaosx_super_event_23_sound_1_5`, `chaosx_super_event_23_sound_2_0`, `chaosx_super_event_23_sound_2_5`, `chaosx_super_event_23_sound_3_0` |
| Source | *The Enola Foam March* by Peet Hudson / Peter Hudson, creator's own orchestral recording |
| Source URL | <https://commons.wikimedia.org/wiki/File:The_Enola_Foam_March.flac> |
| License | CC BY-SA 4.0; attribution, source and license links, edit notice, and ShareAlike-compatible redistribution are required |
| Preserved source | `docs/assets/006_independence_wave/super_events/audio/source/The_Enola_Foam_March.flac` |
| Runtime format | PCM signed 16-bit little-endian, 44.1 kHz, stereo |
| Runtime duration | 110.000000 seconds |
| Runtime SHA-256 | `2892F43CD393F2CA7FEED12FB8A841F9C7C6CA8784F28E2A39DC0AD3B9CECBFF` |
| Catalogue | `music/chaosx_music_track_list.html`, slot `23` row |

The selected source was approved by the user on 2026-09-20. The former London Brass Players recording remains excluded because United States redistribution rights were not verified. The runtime base sound and six wrappers are registered in `sound/chaosx_sound.asset`. The first durable formal League submits display slot `23` and audio ID `23` to the shared settings-aware FIFO through `independence_wave_publish_league_formation`.

## Slot 24 — Every Border a Casus Belli

| Field | Value |
| --- | --- |
| Runtime WAV | `sound/006_independence_wave/super_event_24_every_border_a_casus_belli.wav` |
| Audio id and base sound | `24`; `chaosx_super_event_24_track` |
| Settings wrappers | `chaosx_super_event_24_sound_0_5`, `chaosx_super_event_24_sound_1_0`, `chaosx_super_event_24_sound_1_5`, `chaosx_super_event_24_sound_2_0`, `chaosx_super_event_24_sound_2_5`, `chaosx_super_event_24_sound_3_0` |
| Source | *1812 Overture, Op. 49* by Pyotr Ilyich Tchaikovsky; United States Marine Band recording conducted by Col. Jason K. Fettig and transcribed by MGySgt Donald Patterson |
| Source URL | <https://commons.wikimedia.org/wiki/File:1812_Overture_-_United_States_Marine_Band.opus> |
| Rights basis | Public-domain composition and United States federal-government transcription, performance, and recording basis as recorded in the production manifest |
| Preserved source | `docs/assets/006_independence_wave/super_events/audio/source/1812_Overture_-_United_States_Marine_Band.opus` |
| Runtime format | PCM signed 16-bit little-endian, 44.1 kHz, stereo |
| Runtime duration | 109.992517 seconds |
| Runtime SHA-256 | `3A7C58C94016EDA80842E328DEBC3D00B2D1755085F0C87F580AAAB3B4E0BC08` |
| Catalogue | `music/chaosx_music_track_list.html`, slot `24` row |

The dangerous milestone submits display slot `24` and audio ID `24` to the shared settings-aware FIFO through `independence_wave_publish_danger_milestone`. The base sound and six wrappers are registered in `sound/chaosx_sound.asset`. The production manifest records the accepted 110-second excerpt, fade, normalization, source checksum, and final checksum.

## Runtime contract and validation limits

Both packages use one-shot audio with `max_audible = 1` and `max_audible_behaviour = fail`. The shared dispatcher assigns `global.current_super_event_audio_id` when the queued entry owns the visible super-event window and then uses the existing settings-aware sound helper. No direct bypass of the settings volume path is used.

The source and catalogue records are aligned with the current runtime paths and ordinary slot identifiers. Human perceptual audition, live firing, and save/load behavior remain unverified because the user owns live Hearts of Iron IV validation. No generated test tone, primitive waveform, placeholder cue, or unlicensed replacement is used in either completed source-wired package.

