# Event 020 Rat King defeat-aftermath audio handoff

## Scope

This handoff covers the optional global Rat King defeat-aftermath super-event in display slot 087. It contains one licensed musical recording, its preserved source evidence, the mastered runtime WAV, and the promoted playback identifiers. The producer did not edit events, decisions, scripted effects, localisation, GFX, GUI, or shared sound definitions; the parent tranche now records the sound/music wiring.

The defeat branch remains parent-owned. The parent must retain the accepted long/global-war eligibility gate and complete live playback/consumer validation for this cue.

## Produced files

- Preserved source recording:
  - `docs/assets/020_black_plague/source_audio/dido_aeneas_ukr_32_a1_commons_original.ogg`
- Source evidence:
  - `docs/assets/020_black_plague/source_audio/evidence/dido_aeneas_ukr_32_commons_source.html`
  - `docs/assets/020_black_plague/source_audio/evidence/dido_aeneas_ukr_32_commons_api.json`
  - `docs/assets/020_black_plague/source_audio/evidence/cc_by_sa_4_0_legalcode.html`
- Final mastered file:
  - `sound/020_black_plague/super_event_087_rat_king_defeat_aftermath.wav`
- Related audio records:
  - `docs/assets/020_black_plague/audio_manifest.md`
  - `docs/super_events/020_black_plague/research.md`
  - `music/chaosx_music_track_list.html`

## Selected recording and rights

- Super-event: 087, optional Rat King global defeat aftermath.
- Role: defeat aftermath / memorial / unstable recovery.
- Track title: `Dido's Lament` (the Commons file is `Dido&Aeneas-ukr-32(air&choir).ogg`).
- Composer/work: Henry Purcell, `Dido and Aeneas`, public-domain composition.
- Performer and recording source: 2 March 2014 premiere recording, uploaded as an own-work recording by Wikimedia Commons user `A1`; the Commons category identifies the uploader as Andriy Bondarenko. The file metadata does not name a full cast or venue, so no more specific performer credit is asserted here.
- Source URL: <https://commons.wikimedia.org/wiki/File:Dido%26Aeneas-ukr-32(air%26choir).ogg>
- Frozen source-page revision: <https://commons.wikimedia.org/w/index.php?title=File:Dido%26Aeneas-ukr-32%28air%26choir%29.ogg&oldid=665006997>
- Direct download used: <https://upload.wikimedia.org/wikipedia/commons/7/7b/Dido%26Aeneas-ukr-32%28air%26choir%29.ogg>
- Recording licence: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0). The licence permits sharing and adaptation with attribution, a licence link, a change notice, and distribution of the adapted recording under the same or a compatible licence.
- Composition rights: Purcell died in 1695; the underlying opera and aria are public domain. This does not replace the separate CC BY-SA 4.0 recording licence.
- Licence confidence: high for the source-file licence and composition status; medium for performer identity because the page names uploader `A1` and the category associates Andriy Bondarenko but does not provide a full cast list.
- Required attribution: `Henry Purcell, “Dido's Lament” from Dido and Aeneas; 2 March 2014 premiere recording by A1 (Wikimedia Commons; category credits Andriy Bondarenko), CC BY-SA 4.0. Edited, faded, loudness-normalized, resampled, and excerpted by Chaos Redux.` Include the source and licence links, and do not imply endorsement.

## Duration and hashes

- Preserved source duration: 200.588895833333 seconds, 48,000 Hz stereo Ogg Vorbis.
- Preserved source size: 3,250,871 bytes.
- Preserved source SHA-1: `98037d0395d789c3771ffa7f4ca21ce4c90fdba0` (matches the Commons API).
- Preserved source SHA-256: `D5CD478D298C964123D47869BC3298730DB2BC40AFD2E48361B845F5A4749AB3`.
- Final duration: 115.000000 seconds.
- Final format: stereo signed 16-bit PCM WAV, exactly 44,100 Hz.
- Final SHA-256: `9F97F8A9CEB8A94884D27E4EC74E3C0BE1EA300B1B9E3187688AEDD16F5E39EF`.
- Final loudness: `-19.6 LUFS` integrated, `4.5 LU` LRA, `-9.5 dBFS` true peak.

## Editing and conversion

The source was preserved unchanged before editing. FFmpeg decoded the 48 kHz stereo Vorbis source, kept the opening 115 seconds, applied `loudnorm=I=-20:TP=-2:LRA=11`, a 1.5-second fade-in, and a 6-second fade-out beginning at 109 seconds, then rendered stereo signed 16-bit PCM at 44,100 Hz. The final WAV carries title, artist, source/licence, and edit-notice metadata. No generated tone, oscillator, drone, noise bed, stinger, or placeholder was used.

The first 115 seconds provide a continuous vocal-and-orchestral lament with enough musical structure for a super-event window. The fade-out avoids cutting the source's longer aria abruptly; the parent may retime the excerpt only if a different phrase boundary is verified and the source hash remains unchanged.

## Promoted runtime identifiers

- Playback audio ID: `103` (IDs 101 and 102 are the existing Rat King coronation and world-end cues).
- Base sound definition: `chaosx_super_event_rat_king_defeat_aftermath_track` -> `020_black_plague/super_event_087_rat_king_defeat_aftermath.wav`.
- Settings-volume wrappers:
  - `chaosx_super_event_103_sound_0_5`
  - `chaosx_super_event_103_sound_1_0`
  - `chaosx_super_event_103_sound_1_5`
  - `chaosx_super_event_103_sound_2_0`
  - `chaosx_super_event_103_sound_2_5`
  - `chaosx_super_event_103_sound_3_0`
- Wrapper volume ladder: `0.67`, `1.33`, `2.00`, `2.67`, `3.33`, `4.00`, matching the existing Event 020 super-event pattern. The wrapper prefix follows playback ID `103`; display slot `087` remains the visual super-event ID.
- Runtime handoff: the parent tranche sets `global.current_super_event_audio_id = 103` and dispatches through the existing settings-aware `play_current_super_event_sound = yes` helper. No bypass is authorized.

## Why it fits

The defeat aftermath needs memory, cost, and an unsettled return to ordinary life rather than another coronation or terminal chant. Purcell's lament supplies a clear grief register, sustained vocal lines, and a restrained pulse that can sit under a memorial image or reports of emptied warrens. The aria's historical context is a ruler's death and the consequences that remain afterward, which maps cleanly to the Rat King's fall while leaving room for the campaign's unstable recovery. It is distinct from Event 020 audio IDs 101 (`Gregorian Chant`) and 102 (`Dies irae`) and from the repository's existing final files.

Suitability rating: high for a reflective defeat aftermath; medium for a branch that is intended to feel victorious or celebratory. Keep the title/description focused on survival, absence, and vigilance so the cue's lament does not read as an unrelated opera excerpt.

## Catalogue and documentation handoff

The canonical catalogue row records the final WAV, audio ID 103, source title, composer, recording source, 01:55 duration, CC BY-SA 4.0 terms, and the required attribution/change notice. The Event 020 audio manifest and research note repeat the source paths, hashes, conversion, promoted identifiers, and parent-owned gate/validation boundary.

## Remaining risks and blockers

- The parent must confirm that super-event 087 still has the approved long/global-war eligibility gate before claiming completion and run live playback/consumer validation.
- The promoted base sound definition, six settings-volume wrappers, `global.current_super_event_audio_id`, and settings-aware playback call are present in `sound/chaosx_sound.asset` and the parent-owned resolver path.
- CC BY-SA 4.0 requires the adapted WAV and any redistribution of the recording to retain compatible share-alike terms. Preserve this handoff and the source/legal evidence with the release documentation.
- The source page's performer metadata is limited to uploader `A1` and a category-level Andriy Bondarenko credit; use the uncertainty note above rather than inventing a cast or venue.

No fallback, generated cue, or unlicensed recording was used.
