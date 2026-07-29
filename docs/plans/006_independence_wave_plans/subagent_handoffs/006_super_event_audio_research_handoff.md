# Event 006 super-event audio research handoff

Date: 2026-07-14

> Superseded production status, 2026-07-16: this is the preserved pre-production
> research handoff. Its instructions to create, register, and fire 6002 are
> complete. Use `docs/super_events/006_independence_wave/research.md`
> and `docs/assets/006_independence_wave/super_events/audio/production_manifest.md`
> for current runtime and checksum authority. Audio 6001 remains blocked.

Mode: bounded research and permitted-source preservation only. No final audio conversion, gameplay edit, interface edit, localisation edit, workbook edit, or spec edit was made.

## Result

The two-track package is **not complete**:

- `6001`, *A Trumpet Voluntary*: blocked because the accepted 1948/1949 London Brass Players recording lacks a United States public-domain tag, CC0 dedication, or rights-holder permission. The source was not downloaded and must not be processed or wired.
- `6002`, *1812 Overture*: source identity, U.S. federal public-domain basis, direct URL, checksum, stream profile, exact excerpt, fades, loudness plan, final paths, and wiring identifiers were verified. This research handoff created no derivative; the parent later produced and wired both final derivatives.

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

## Parent closeout of the original next actions

1. Treat `6001` as blocked. Obtain explicit permission/waiver covering the exact recording in the United States, or ask the user for approval to reopen track selection. Do not silently substitute a recording.
2. Completed: produced `6002` from the preserved Opus original using the exact final-110-second interval `10:44.641-12:34.641`, a `1.5 s` fade-in, a `2.0 s` fade-out, dynamics-preserving two-pass normalization to `-18 LUFS`, and `44.1 kHz` delivery.
3. Completed: created both derivatives:
   - `sound/006_independence_wave/super_event_006_02_every_border_a_casus_belli.wav`
   - `sound/006_independence_wave/super_event_006_02_every_border_a_casus_belli.wav`
4. Completed: validated decoded duration, channel count, sample rate, integrated loudness, true peak, and SHA-256 for both derivatives.
5. Completed: registered music names `chaosx_super_event_6002_<suffix>`, raw sound `chaosx_super_event_independence_wave_every_border_a_casus_belli_track`, and sound wrappers `chaosx_super_event_6002_sound_<suffix>` for the six established volume suffixes.
6. Completed: added `chaosx_super_event_6002_sound_1_5` to the music track list with zero random-play chance and wired the dangerous-milestone publisher to the existing settings-aware FIFO and playback helper.

## Meaningful checks performed

- Local Marine Band SHA-1 matches the Commons original exactly.
- FFprobe identifies a decodable Ogg Opus, `48 kHz`, stereo source of approximately `754.6475 s`.
- Analysis of the exact retained interval found `-13.78 LUFS`, `-0.05 dBTP`, and `16.3 LU`; the planned linear pass measured `-18.0 LUFS`, `-4.3 dBTP`, and `16.2 LU` at `44.1 kHz` without flattening the source dynamics.
- No retained-interval silence of at least `0.25 s` at `-50 dBFS` was detected.
- At research time, audio IDs 6001 and 6002 and their dynamic asset names were absent from the registered audio surface; that finding reserved the collision-free IDs. Audio 6002 is now registered and consumed.
- The current settings helper already constructs the numeric sound identifier from `global.current_super_event_audio_id`; no new helper branch is needed.

## Simplifications, omissions, and blockers

- The requested final two-track package could not be completed because `6001` failed rights verification.
- No fallback or substitute was used.
- Final WAV production and source wiring were parent-owned and intentionally not performed by this research subagent; the parent later completed them for 6002.
- The `6002` rights basis is U.S. federal public domain, not a worldwide CC0 dedication; this caveat is documented rather than hidden.
