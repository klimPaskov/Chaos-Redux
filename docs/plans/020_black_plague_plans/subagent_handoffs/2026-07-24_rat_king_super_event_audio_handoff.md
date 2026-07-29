# Event 020 Rat King super-event audio handoff

## Scope

This handoff covers only the licensed audio research and production requested for the Rat King coronation and Rat King world-end super-events. It does not edit gameplay, event scripts, localisation, GFX, GUI, sound definitions, sound definitions, or spreadsheets.

## Produced files

- Preserved source downloads:
  - `docs/assets/020_black_plague/source_audio/kevin_macleod_gregorian_chant_commons_original.ogg`
  - `docs/assets/020_black_plague/source_audio/dies_irae_membeth_commons_original.ogg`
- Source-page HTML, licence legal code, and Commons API metadata:
  - `docs/assets/020_black_plague/source_audio/evidence/kevin_macleod_gregorian_chant_commons_source.html`
  - `docs/assets/020_black_plague/source_audio/evidence/dies_irae_membeth_commons_source.html`
  - `docs/assets/020_black_plague/source_audio/evidence/cc_by_3_0_legalcode.html`
  - `docs/assets/020_black_plague/source_audio/evidence/cc0_1_0_legalcode.html`
  - `docs/assets/020_black_plague/source_audio/evidence/commons_audio_api.json`
- Final mastered files:
  - `sound/020_black_plague/super_event_101_rat_king_coronation.wav`
  - `sound/020_black_plague/super_event_101_rat_king_coronation.wav`
  - `sound/020_black_plague/super_event_102_rat_king_world_end.wav`
  - `sound/020_black_plague/super_event_102_rat_king_world_end.wav`
- Manifest and research note:
  - `docs/assets/020_black_plague/audio_manifest.md`
  - `docs/super_events/020_black_plague/research.md`

## Rights and selection

### Coronation / proposed playback ID 101

Kevin MacLeod's `Gregorian Chant` is a 194-second SoundCloud-origin recording imported to Commons with the author/composer named and CC BY 3.0 explicitly stated. A 110-second opening excerpt is used. Attribution, a licence link, and a modification notice are required. Source SHA-1 is `3462dd0732223ee7b7815f8fb04a55415b3bf673`; source SHA-256 is `d4ec1fe983170ab5f315a54770fdcb0e43992e41166d194a3ae8a1e01041a804`.

Final WAV: `sound/020_black_plague/super_event_101_rat_king_coronation.wav`, 110.000000 seconds, 44,100 Hz stereo, SHA-256 `28d891720ccfeb2a2d8a41c0972fe5d88b895d7191365bf98071b33accc78db0`.

Final WAV: `sound/020_black_plague/super_event_101_rat_king_coronation.wav`, 110.000000 seconds, 44,100 Hz stereo signed 16-bit PCM, SHA-256 `4b717c9744c4a9a3c4ecf5997d55b8a8f1a708226e3d47a3c1fc2f9cd4425722`.

### World end / proposed playback ID 102

Membeth's `Dies irae` is a 434.000952-second Gregorian chant recording released to the worldwide public domain. The medieval Requiem sequence is public domain; the historical composer attribution is not needed for the recording licence. A 103.65-second excerpt ending at the first long musical pause is used. Attribution is optional but courtesy credit is recommended. Source SHA-1 is `d13e914db3016ab43bcb89c695e501ac8fd19605`; source SHA-256 is `a94c57586d3215a4ecb67a5eb9701b387be39bef2f53abaa3e3b2214a2e9472e6`.

Final WAV: `sound/020_black_plague/super_event_102_rat_king_world_end.wav`, 103.650000 seconds, 44,100 Hz stereo, SHA-256 `b9b03f7a977170a2cda47e056b8ebc7afb428d6776802ac30603c65525521709`.

Final WAV: `sound/020_black_plague/super_event_102_rat_king_world_end.wav`, 103.650000 seconds, 44,100 Hz stereo signed 16-bit PCM, SHA-256 `7240f9bddc19955fde7c56ef9d15381d87a84ba7ce39f6c5bf3663b67ab0221f`.

## Processing and validation

Both sources were downloaded from Wikimedia Commons' `Special:FilePath` endpoint and preserved unchanged. FFmpeg rendered stereo signed 16-bit PCM with `loudnorm=I=-20:TP=-2:LRA=11`, 1.5-second fade-in, 6-second fade-out, and 44,100 Hz output conversion. OGG Vorbis quality 6 files were encoded from the processed WAV files. `ffprobe` confirms both OGGs and both WAVs are stereo at exactly 44,100 Hz, with final durations 110.000000 and 103.650000 seconds. `ebur128` measures `-19.9 LUFS` for coronation and `-20.3 LUFS` for world end.

The files contain musical recordings rather than generated tones, noise beds, drones, stingers, or oscillator placeholders. A SHA-256 comparison against every existing `.ogg` and `.wav` under `music/` and `sound/` returned zero duplicates for all four Event 020 derivatives. The repository's current audio definitions and catalogue contain no IDs `101` or `102`; parent must collision-scan the final shared constants before committing.

## Parent wiring keys

Add six settings-scaled sound wrappers for audio IDs `101` and `102`:

- `chaosx_super_event_rat_king_coronation_track` -> `020_black_plague/super_event_101_rat_king_coronation.wav`;
- `chaosx_super_event_101_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, `_3_0`;
- `chaosx_super_event_rat_king_world_end_track` -> `020_black_plague/super_event_102_rat_king_world_end.wav`; and
- `chaosx_super_event_102_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, `_3_0`.

Use `global.current_super_event_audio_id = 101` for the coronation branch and `102` for the world-end branch, then call the settings-aware playback helper. Keep display slots separate from playback IDs and add both rows to `music/chaosx_music_track_list.html`.

## Remaining risks and omissions

- The optional Rat King defeat-aftermath audio package is intentionally not produced until the parent confirms the branch's global, long-war eligibility gate remains in the accepted implementation.
- Display-slot numbers are not assigned here; the parent owns collision scanning and final slot choice.
- No sound definitions were edited, so these tracks are not yet wired in-game.
- The final Event 020 package still needs text, image, GFX, event trigger, settings-aware dispatch, catalogue, and event-doc integration. These are not audio blockers, but they must be completed before claiming the super-events are complete.

## No commit

No commit was created from this shared worktree. The parent should review this handoff, the manifest, and the two final audio paths with the rest of the Event 020 changes and commit the cohesive plan as one unit.
