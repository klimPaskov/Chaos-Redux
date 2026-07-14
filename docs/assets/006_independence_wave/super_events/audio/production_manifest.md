# Event 006 super-event audio production manifest

Production date: 2026-07-14

## Cleared production

`Every Border a Casus Belli` uses the accepted final 110 seconds of
Tchaikovsky's *1812 Overture, Op. 49*, in the 2019 United States Marine Band
recording conducted by Colonel Jason K. Fettig and transcribed by Master
Gunnery Sergeant Donald Patterson. Wikimedia Commons identifies the
composition as public domain and the transcription, performance, and recording
as United States federal-government works. The exact rights and source evidence
remain recorded in
`docs/plans/006_independence_wave_plans/super_event_research/006_super_event_audio_verification.md`.

Preserved source:

- `docs/assets/006_independence_wave/super_events/audio/source/1812_Overture_-_United_States_Marine_Band.opus`
- SHA-256: `93C141A2E5782385E8A9B53F5F622AFCB604DA6F361FE1CA2E160EA4BFE92D3D`
- accepted interval: `644.641` through `754.641`, exactly 110 seconds
- fade-in: 1.5 seconds
- fade-out: 2 seconds, beginning at excerpt second 108
- loudness process: two-pass linear loudness normalization targeting `-18 LUFS`

Final runtime derivatives:

| Runtime file | Format | Decoded duration | Loudness | True peak | LRA | SHA-256 |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `music/006_independence_wave/super_event_006_02_every_border_a_casus_belli.ogg` | Ogg Vorbis, 44.1 kHz, stereo | `109.992517 s` | `-18.05 LUFS` | `-3.81 dBTP` | `16.40 LU` | `6B62C5AFA03E83C5BEB7D36E203E41BDC1EE51AEDD89269410A48BA0FCBC0DF0` |
| `sound/006_independence_wave/super_event_006_02_every_border_a_casus_belli.wav` | PCM signed 16-bit little-endian, 44.1 kHz, stereo | `109.992517 s` | `-18.00 LUFS` | `-4.27 dBTP` | `16.30 LU` | `3A7C58C94016EDA80842E328DEBC3D00B2D1755085F0C87F580AAAB3B4E0BC08` |

Wiring identifiers:

- music assets: `chaosx_super_event_6002_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, and `_3_0`;
- station representative: `chaosx_super_event_6002_1_5`, zero random chance;
- raw sound: `chaosx_super_event_independence_wave_every_border_a_casus_belli_track`;
- sound wrappers: `chaosx_super_event_6002_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, and `_3_0`;
- one-shot playback; wrapper collision policy is `max_audible = 1` with `max_audible_behaviour = fail`.

The gameplay firing effect must set `global.current_super_event_audio_id = 6002`
only at the accepted dangerous coordinated-bloc threshold, immediately before
the existing settings-aware super-event playback helper.

## Held production

`The League of New States` remains held. The accepted London Brass Players
recording of *A Trumpet Voluntary* has no verified United States redistribution
right. Audio ID `6001`, its source, derivatives, assets, wrappers, and playback
assignment remain deliberately absent. No substitute or fallback recording was
used.
