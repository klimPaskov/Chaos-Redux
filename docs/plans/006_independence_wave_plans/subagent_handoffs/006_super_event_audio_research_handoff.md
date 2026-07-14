# Event 006 super-event audio research handoff

Date: 2026-07-14

Mode: bounded research and permitted-source preservation only. No final audio conversion, gameplay edit, interface edit, localisation edit, workbook edit, or spec edit was made.

## Result

The two-track package is **not complete**:

- `6001`, *A Trumpet Voluntary*: blocked because the accepted 1948/1949 London Brass Players recording lacks a United States public-domain tag, CC0 dedication, or rights-holder permission. The source was not downloaded and must not be processed or wired.
- `6002`, *1812 Overture*: source identity, U.S. federal public-domain basis, direct URL, checksum, stream profile, exact excerpt, fades, loudness plan, final paths, and wiring identifiers are verified. The original source is preserved; no derivative was created.

Full evidence and production details are in `docs/plans/006_independence_wave_plans/super_event_research/006_super_event_audio_verification.md`.

## Files added

- `docs/assets/006_independence_wave/super_events/audio/source/1812_Overture_-_United_States_Marine_Band.opus`
  - bytes: `12,999,461`
  - SHA-1: `760e68775d9625542eaecfdc863efd7fe50853e4`
  - SHA-256: `93c141a2e5782385e8a9b53f5f622afcb604da6f361fe1ca2e160ea4bfe92d3d`
  - source page: <https://commons.wikimedia.org/wiki/File:1812_Overture_-_United_States_Marine_Band.opus>
  - direct original: <https://upload.wikimedia.org/wikipedia/commons/6/66/1812_Overture_-_United_States_Marine_Band.opus>
- `docs/plans/006_independence_wave_plans/super_event_research/006_super_event_audio_verification.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_super_event_audio_research_handoff.md`

No London Brass Players source file was added. Its Commons remote SHA-1 is `6320e3d289d959acf0a871d1bea3cfa7b3d3b7fa`, but there is intentionally no local checksum.

## Parent-owned next actions

1. Treat `6001` as blocked. Obtain explicit permission/waiver covering the exact recording in the United States, or ask the user for approval to reopen track selection. Do not silently substitute a recording.
2. If continuing the unblocked half, produce `6002` from the preserved Opus original using the exact final-110-second interval `10:44.641-12:34.641`, a `1.5 s` fade-in, a `2.0 s` fade-out, dynamics-preserving two-pass normalization to `-18 LUFS`, and `44.1 kHz` delivery.
3. Create both later derivatives:
   - `music/006_independence_wave/super_event_006_02_every_border_a_casus_belli.ogg`
   - `sound/006_independence_wave/super_event_006_02_every_border_a_casus_belli.wav`
4. Post-validate decoded duration, channel count, sample rate, integrated loudness, true peak, and SHA-256 for both derivatives.
5. Register music names `chaosx_super_event_6002_<suffix>`, raw sound `chaosx_super_event_independence_wave_every_border_a_casus_belli_track`, and sound wrappers `chaosx_super_event_6002_sound_<suffix>` for the six established volume suffixes.
6. Add `chaosx_super_event_6002_1_5` to the music track list with zero random-play chance, set `global.current_super_event_audio_id = 6002` at the correct super-event firing site, and call the existing settings-aware helper. The helper itself already supports this ID dynamically.

## Meaningful checks performed

- Local Marine Band SHA-1 matches the Commons original exactly.
- FFprobe identifies a decodable Ogg Opus, `48 kHz`, stereo source of approximately `754.6475 s`.
- Analysis of the exact retained interval found `-13.78 LUFS`, `-0.05 dBTP`, and `16.3 LU`; the planned linear pass measured `-18.0 LUFS`, `-4.3 dBTP`, and `16.2 LU` at `44.1 kHz` without flattening the source dynamics.
- No retained-interval silence of at least `0.25 s` at `-50 dBFS` was detected.
- Audio IDs `6001` and `6002`, their dynamic asset names, and both proposed final OGG paths are absent from the current registered audio surface; the present maximum registered audio ID is `56`.
- The current settings helper already constructs numeric music and sound identifiers from `global.current_super_event_audio_id`; no new helper branch is needed.

## Simplifications, omissions, and blockers

- The requested final two-track package could not be completed because `6001` failed rights verification.
- No fallback or substitute was used.
- Final OGG/WAV production and all source wiring remain parent-owned and were intentionally not performed.
- The `6002` rights basis is U.S. federal public domain, not a worldwide CC0 dedication; this caveat is documented rather than hidden.
