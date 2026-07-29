# Event 020 Black Plague super-event audio manifest

This manifest records the preserved source downloads, licensing evidence, edited derivatives, hashes, and proposed playback identifiers for the two Rat King super-events. The files are audio-only assets; runtime wiring remains parent-owned. The accepted runtime uses one final WAV per super-event under `sound/020_black_plague/`, registration in `sound/chaosx_sound.asset`, and the settings-aware sound helper. Source OGG files remain under `docs/assets/` as provenance.

## Source evidence

| Candidate | Source page | Source file | Source duration | Source stream | Source SHA-1 | Source SHA-256 | Rights decision |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| Kevin MacLeod, `Gregorian Chant` | <https://commons.wikimedia.org/wiki/File:KevinMacLeod_-_Gregorian_Chant.ogg> (frozen page revision: <https://commons.wikimedia.org/w/index.php?title=File:KevinMacLeod_-_Gregorian_Chant.ogg&oldid=1044292914>) | `docs/assets/020_black_plague/source_audio/kevin_macleod_gregorian_chant_commons_original.ogg` | 194.000000 s | Ogg Vorbis, 44,100 Hz, stereo | `3462dd0732223ee7b7815f8fb04a55415b3bf673` | `d4ec1fe983170ab5f315a54770fdcb0e43992e41166d194a3ae8a1e01041a804` | Selected for coronation. CC BY 3.0 recording/composition with named author and explicit adaptation rights. |
| `Dies irae` | <https://commons.wikimedia.org/wiki/File:Dies.irae.ogg> (frozen page revision: <https://commons.wikimedia.org/w/index.php?title=File:Dies.irae.ogg&oldid=1205385897>) | `docs/assets/020_black_plague/source_audio/dies_irae_membeth_commons_original.ogg` | 434.000952 s | Ogg Vorbis, 44,100 Hz, stereo | `d13e914db3016ab43bcb89c695e501ac8fd19605` | `a94c57586d3215a4ecb67a5eb9701b387be39bef2f53abaa3e3b2214a2e9472e6` | Selected for world end. Membeth released the recording worldwide to the public domain. The medieval sequence is public domain; exact historical authorship is not a recording-rights condition. |

Saved source-page HTML, Creative Commons legal code, and MediaWiki API metadata are in `docs/assets/020_black_plague/source_audio/evidence/`.

## Final derivatives

| Proposed audio ID | Super-event role | Runtime WAV | Duration | WAV SHA-256 | Loudness |
| ---: | --- | --- | ---: | --- | --- |
| 101 | Rat King coronation | `sound/020_black_plague/super_event_101_rat_king_coronation.wav` | 110.000000 s | `4b717c9744c4a9a3c4ecf5997d55b8a8f1a708226e3d47a3c1fc2f9cd4425722` | `-19.9 LUFS`, `5.3 LU LRA` |
| 102 | Rat King world end | `sound/020_black_plague/super_event_102_rat_king_world_end.wav` | 103.650000 s | `7240f9bddc19955fde7c56ef9d15381d87a84ba7ce39f6c5bf3663b67ab0221f` | `-20.3 LUFS`, `11.7 LU LRA` |

Both runtime files are signed 16-bit PCM WAV, stereo, exactly 44,100 Hz. The WAV RIFF comments carry the title, artist, source/licence notice, and edit notice. The settings-aware sound wrappers should reference these single mastered files; no per-volume derivative copies are needed.

## Conversion ledger

### Audio ID 101, Rat King coronation

- Source window: `0.608345` through `110.608345` seconds of the 194-second source; the source's initial 0.608345-second silence was removed.
- Processing: FFmpeg `loudnorm=I=-20:TP=-2:LRA=11`, 1.5-second fade-in, 6-second fade-out from source-relative 104 seconds, stereo 16-bit PCM render, and output conversion to 44,100 Hz WAV.
- The final cue is an excerpt of a continuous chant-style fantasy processional. The fade avoids an abrupt cut while keeping the coronation's court/ritual transformation legible.
- Required attribution: `Kevin MacLeod, “Gregorian Chant”; source via Wikimedia Commons and SoundCloud; Creative Commons Attribution 3.0. Edited, faded, loudness-normalized, resampled, and excerpted by Chaos Redux.` Include the source and licence links and state that changes were made. Do not imply Kevin MacLeod endorses the mod.

### Audio ID 102, Rat King world end

- Source window: `0.905760` through `104.555760` seconds of the 434.000952-second source. The source's initial 0.905760-second silence was removed, and the excerpt ends at the first long chant pause (the source pause begins at approximately 104.560726 seconds).
- Processing: FFmpeg `loudnorm=I=-20:TP=-2:LRA=11`, 1.5-second fade-in, 6-second fade-out from source-relative 97.65 seconds, stereo 16-bit PCM render, and output conversion to 44,100 Hz WAV.
- The excerpt keeps the opening *Dies irae* sequence through a natural musical pause, giving the terminal takeover ritual weight without dragging the full 7:14 recording into the super-event.
- Attribution is not required by the Commons public-domain dedication. Courtesy credit is recommended: `Gregorian chant, “Dies irae”; recording by Membeth; source via Wikimedia Commons; public domain. Edited, faded, loudness-normalized, resampled, and excerpted by Chaos Redux.`

## Proposed registry keys (parent-owned wiring)

The current audio folders, catalogue, and docs contain no `101` or `102` playback IDs. The parent should still collision-scan the final shared constants before committing. Keep display-slot numbers separate from playback IDs as described by `music/chaosx_music_track_list.html`.

For sound playback, add:

- `chaosx_super_event_rat_king_coronation_track` -> `020_black_plague/super_event_101_rat_king_coronation.wav`;
- `chaosx_super_event_101_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, and `_3_0`, each wrapping the coronation track at volumes `0.67`, `1.33`, `2.00`, `2.67`, `3.33`, and `4.00`;
- `chaosx_super_event_rat_king_world_end_track` -> `020_black_plague/super_event_102_rat_king_world_end.wav`; and
- `chaosx_super_event_102_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, and `_3_0`, each wrapping the world-end track at the same volume ladder.

When the parent sets `global.current_super_event_audio_id`, use `101` for the coronation branch and `102` for the world-end branch, then dispatch through the existing settings-aware sound helper. The canonical audio catalogue remains `music/chaosx_music_track_list.html`; the parent owns both row updates with the final display-slot IDs and the source/rights text above. This package deliberately does not edit any registry or wiring file.

## Rejected or secondary candidates

- `De profundis.ogg` (Rick Dechance / Peirigill, CC BY-SA variants) was the accepted research lead but was not selected because the Commons record leaves the author field blank and does not clearly identify the composition/recording rights split. It remains a useful fallback candidate only after the parent approves medium-confidence provenance.
- `Rorate Caeli ~ Gregorian Chant.ogg` (Inritter, CC BY-SA 4.0) has a clear recording licence but a less direct coronation fit and no stronger metadata than the selected Kevin MacLeod cue. It was not downloaded.
- Existing repository audio sources and the canonical `music/chaosx_music_track_list.html` catalogue were checked, along with `sound/chaosx_sound.asset`. No already-approved unused recording matched the Event 020 role while preserving the required unique-track rule, so no repository recording was reused.

## Open scope

The optional Rat King defeat-aftermath super-event is not included because the accepted implementation must first retain its long/global-war eligibility gate. If that branch remains, commission a third unique lament or memorial track and repeat this evidence, conversion, and registry process; do not reuse IDs 101 or 102.
