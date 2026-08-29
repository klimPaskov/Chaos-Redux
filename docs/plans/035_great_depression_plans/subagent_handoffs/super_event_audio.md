# Event 035 super-event audio handoff

## Result

The audio research worker selected and prepared a unique cue for Event 035 Evolution III, The Second Great Depression.

The cue is Frédéric Chopin's *Funeral March in C minor, Op. posth. 72 no. 2*, performed by Aya Higuchi in a Musopen recording hosted on Wikimedia Commons.

The composition is public domain and the specific recording file is dedicated under CC0 1.0 Universal.

The cue is a strong fit for the first worldwide economic contraction because its measured processional character communicates collective loss of work, trade, and industrial momentum without implying a military victory or physical apocalypse.

## Files delivered

| Role | Path | SHA-256 |
| --- | --- | --- |
| Preserved original source OGG | `docs/assets/035_great_depression/source_audio/chopin_funeral_march_op72_no2_aya_higuchi_cc0_original.ogg` | `2e3d83683bbc12e12459a8ded6afcdb4c3553de8c987b9a3fba79f8b9fc36936` |
| Processed OGG candidate | `docs/assets/035_great_depression/processed_audio/super_event_106_second_great_depression.ogg` | `06da7f6233073a76c32ba892ec743f77309b6e8d7ee53913b11ee652008ecb56` |
| Commons source-page evidence | `docs/assets/035_great_depression/source_evidence/commons_funeral_march_chopin_op72_no2_oldid_1263010345.html` | `3d04623d96b2996dfd4c0654090d5659b16090ac35437f582ef2c6729555c741` |
| CC0 deed evidence | `docs/assets/035_great_depression/source_evidence/cc0_1_0_deed_en.html` | `4ceb8ae6835f2f5263caa0e39c9e1adca9469686c267475049b33521dabbe339` |
| CC0 legal-code evidence | `docs/assets/035_great_depression/source_evidence/cc0_1_0_legalcode_en.html` | `001e3d1c905c18b1d034b34200cc952026abb38457c2294c23eaef7f6bda64df` |

The preserved source is `5,691,110` bytes with SHA-1 `f7625d58ed63900419dda16a97839a9367dc5e11`, exactly matching the checksum published on the Commons file page.

The processed candidate is `115.000000 s`, OGG/Vorbis, stereo, `44,100 Hz`, nominal `192 kb/s`, and decodes successfully with FFmpeg.

## Provenance and rights

- Source page: <https://commons.wikimedia.org/wiki/File:Funeral_March_Chopin_Op_72_2.ogg>
- Frozen source revision: <https://commons.wikimedia.org/w/index.php?title=File:Funeral_March_Chopin_Op_72_2.ogg&oldid=1263010345>
- Direct download: <https://upload.wikimedia.org/wikipedia/commons/3/3f/Funeral_March_Chopin_Op_72_2.ogg>
- Upstream work page: <https://musopen.org/music/616-funeral-march-in-c-minor-op-posth-72-no-2/>
- Recording licence: <https://creativecommons.org/publicdomain/zero/1.0/deed.en>
- Composition: public-domain Frédéric Chopin work, composed in 1827 and published posthumously in 1855.
- Recording: Aya Higuchi performance, file-specific CC0 1.0 Universal dedication on Wikimedia Commons.
- Attribution: not legally required by CC0. Courtesy credit is recommended and is embedded in the candidate metadata and research note.

Suggested courtesy attribution:

> Frédéric Chopin, *Funeral March in C minor, Op. posth. 72 no. 2*, performed by Aya Higuchi, source recording via Wikimedia Commons and Musopen, dedicated under CC0 1.0 Universal. Chaos Redux excerpted the recording, applied fades and loudness processing, and encoded a 44.1 kHz stereo Vorbis derivative. No endorsement is implied.

## Proposed identifier map

| Runtime concept | Proposed value |
| --- | --- |
| Playback audio ID | `106` |
| Base sound definition | `chaosx_super_event_great_depression_second_great_depression_track` |
| Settings-aware wrapper family | `chaosx_super_event_106_sound_0_5` through `chaosx_super_event_106_sound_3_0` |
| Candidate stem | `super_event_106_second_great_depression` |
| Parent global selector | `global.current_super_event_audio_id = 106` |
| Parent playback helper | `play_current_super_event_sound = yes` |
| Display slot | Must be allocated by the parent. Current slot-35 wrappers belong to Event 010 Death. |

## Edit recipe

The original source is preserved.

The candidate removes the first `0.802875 s` of silence, retains source time `00:00.802875` through `01:55.802875`, applies a `1.5 s` fade-in and a `5 s` fade-out, normalizes toward `-18 LUFS`, resamples to stereo `44,100 Hz`, and encodes OGG/Vorbis quality `6`.

Measured candidate values are `-17.1 LUFS` integrated loudness, `11.6 LU` LRA, and `-1.4 dBFS` true peak.

## Parent-owned wiring

The following files and systems were intentionally left untouched:

- `sound/chaosx_sound.asset`
- `music/chaosx_music_track_list.html`
- super-event sound or visibility definitions
- event script and trigger effects
- scripted localisation and player-facing localisation

The parent must decide the unused display slot, register the base sound and six wrappers, reconcile the candidate OGG with the current WAV-based sound-definition convention if necessary, set the global audio ID, call the settings-aware helper, and add the canonical catalogue row.

The expected current-convention runtime WAV path is `sound/035_great_depression/super_event_106_second_great_depression.wav`, but this worker did not create that runtime file because the requested deliverable was the OGG candidate and the scope forbids sound wiring.

## Validation and remaining risk

- Source SHA-1 matches the Commons page checksum.
- Source and derivative are distinct files with preserved provenance.
- Candidate duration is exactly 115 seconds, within the requested one-to-two-minute shape.
- Candidate is a structured musical performance, not a generated tone, drone, stinger, sound effect, or noise bed.
- No current runtime catalogue or sound definition uses this work, recording, or proposed playback ID `106`.
- No rights blocker remains for the selected source.

Remaining integration risks are the unresolved display-slot allocation and the repository's current WAV sound-definition convention.

Full provenance, candidate comparison, source evidence hashes, format inspection, and the proposed catalogue row are in `docs/assets/035_great_depression/super_event_audio_research.md`.

