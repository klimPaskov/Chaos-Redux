# Event 31 Random Terror audio research

Research date: 2026-08-29.

## Archive verification on 2026-09-05

Disposition: the research and conversion record is retained, with source-archive recovery blocked by two missing originals.
The original OGG paths listed below are absent, and a filename search including ignored files under `docs/`, `sound/`, and `music/` found no matching originals.
The two runtime WAVs match their recorded SHA-256 values and each has a 110.000-second, stereo, 44,100 Hz, 16-bit PCM header.
These file checks confirm the supplied derivatives' identity and format, but cannot reproduce the source-to-WAV conversion without the archived originals.
Recover the exact source bytes matching the recorded original hashes, or record a separately reviewed replacement source and conversion lineage before treating the source archive as complete.

The licensing assessment, catalogue baseline, provisional IDs, and proposed wiring below describe the 2026-08-29 research tranche.
This documentation review did not revalidate online licensing, playback-ID allocation, sound registration, event wiring, or live playback.
The titles remain research selections whose final placement belongs to the event owner.

## Research scope

Final text role: the reveal title is `The False Revelation` and the defeat aftermath title is `The Broken Claim`, as selected by the Event 31 text research handoff.

This note covers the two audio roles requested for Event 31 Random Terror. The reveal cue is for The False Revelation's first public appearance and terminal campaign announcement. The aftermath cue is for liberation, loss, reconstruction, surviving cells, and uncertainty after the final state is broken.

No sound definition, event script, localisation file, or workbook file was edited in this tranche.

## Repository reuse audit

The current `music/chaosx_music_track_list.html` and `sound/chaosx_sound.asset` were inspected before external sourcing.

Before this package, the catalogue's numeric super-event playback entries ended at `103`. It contains Erik Satie's `Gnossienne No. 1` for Event 044 and Modest Mussorgsky's `Pictures at an Exhibition: IV. Bydło` for Event 054, but it contained no `Gymnopédie No. 1` or `Night on Bald Mountain` entry.

Existing `Dies irae` and `Dido's Lament` entries were not reused because a new Event 031 package requires two unique final recordings.

The current catalogue includes documented legacy or attribution-incomplete entries. None of those files was used as a source or final cue.

## Candidate review

| Candidate | Source page | Composition rights | Recording rights | Source duration | Decision |
|---|---|---|---|---:|---|
| Modest Mussorgsky, `Night on Bald Mountain` | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Modest_Mussorgsky_-_night_on_bald_mountain.ogg) | Public domain composition. The source page credits Mussorgsky and identifies the 1886 work. | Worldwide public-domain release by Musopen, confirmed on the Wikimedia Commons file page. | 12:13.200 | Selected for the reveal. |
| Erik Satie, `Gymnopédie No. 1` | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Gymnopedie_No._1..ogg) | Public domain composition. The work was published in 1888 and Satie died in 1925. | CC0 1.0 recording by Teknopazzo, identified as own work on the source page. | 03:24.800 | Selected for the defeat aftermath. |
| Ludwig van Beethoven, `Symphony No. 7 in A major, Op. 92, II. Allegretto` | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:JOHN_MICHEL_CELLO-BEETHOVEN_SYMPHONY_7_Allegretto.ogg) | Public domain composition. | CC BY-SA 3.0 cello recording by John Michel. The terms permit editing with attribution and ShareAlike, but the 11 minute solo reduction is less exact for the restrained aftermath role than the selected Satie recording. | 11:00 | Considered and not selected. |

## Selected cue 1: The False Revelation reveal

### Musical identity and rights

Track title: `Night on Bald Mountain`, also known as `Night on the Bare Mountain`.

Composer: Modest Petrovich Mussorgsky, 1839 to 1881.

Composition source: [IMSLP Night on Bald Mountain](https://imslp.org/wiki/Night_on_Bald_Mountain_%28Mussorgsky%2C_Modest%29).

Composition rights assessment: Public domain. The Wikimedia source page identifies the 1886 work and credits Mussorgsky. The commonly circulated 1886 revision is also outside modern copyright terms because its associated arranger Nikolay Rimsky-Korsakov died in 1908. The source recording page marks the musical work as public domain.

Performer and recording source: The Wikimedia metadata tentatively says Skidmore College Orchestra and does not identify the recorder. The rights-bearing source is Musopen.

Recording source page: [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Modest_Mussorgsky_-_night_on_bald_mountain.ogg).

Musopen source page: [Musopen music library](https://musopen.org/).

Direct download URL: `https://upload.wikimedia.org/wikipedia/commons/c/ca/Modest_Mussorgsky_-_night_on_bald_mountain.ogg`.

Recording license: Public domain worldwide release by Musopen as recorded on the Wikimedia Commons page. The page reproduces Musopen's request for courtesy attribution in commercial or derived works.

Usage terms: Use, edit, share, and distribute the derivative for the mod. Include a courtesy credit to Musopen and retain the source page link. No endorsement is implied by the use of this composition or recording.

License confidence: High for composition and recording rights. Medium for the exact performer name because the Commons metadata says the orchestra might be Skidmore College Orchestra and does not identify a recorder.

Recording date: Not stated on the source page.

Original downloaded source: `docs/super_events/031_random_terror/audio_sources/modest_mussorgsky_night_on_bald_mountain.commons.ogg`.

Original source SHA-256: `F0C7F3CD9DC3B746FD8080860012BA152B99760021431F127070A2825D2CEFC9`.

Original source format: Ogg Vorbis, stereo, 48,000 Hz, 733.200 seconds, 12,865,200 bytes.

Attribution text: `Modest Mussorgsky, Night on Bald Mountain, recording released to the public domain by Musopen, source via Wikimedia Commons. Edited for Chaos Redux.`

### Final derivative

Suggested super-event use: The False Revelation, the first public appearance and terminal global campaign announcement.

Why it fits: The low-register orchestral opening and processional escalation give the reveal an immediate sense of coercive ceremony and approaching catastrophe. The cue is structured orchestral music rather than a drone or sound-effect bed, and the excerpt leaves enough room for the public uncertainty in the final text.

Final runtime path: `sound/031_random_terror/super_event_104_false_revelation_reveal.wav`.

Final duration: 110.000 seconds, or 01:50.

Final SHA-256: `8701046C4C7A72FED2AFF7B567ABAD36D43E10BEE2469A3C2C64E487B4FFAA25`.

Final format: PCM signed 16-bit little-endian, stereo, 44,100 Hz, 19,404,078 bytes.

Transformation recipe: Decode the preserved OGG source with FFmpeg 8.1.1, take the opening 110.000 seconds, apply a fixed +1.0 dB gain, apply a 0.20 second fade-in, apply a 4.00 second fade-out beginning at 106.000 seconds, resample to 44,100 Hz, convert to stereo PCM16, and write the WAV. No time stretch, pitch shift, loop, synthetic layer, oscillator, or added sound effect was used.

The fixed gain leaves the measured final sample peak at approximately -3.1 dBFS. The source is retained unchanged.

## Selected cue 2: The False Revelation defeat aftermath

### Musical identity and rights

Track title: `Gymnopédie No. 1`.

Composer: Erik Satie, 1866 to 1925.

Composition source: [IMSLP Gymnopédie No. 1](https://imslp.org/wiki/Gymnop%C3%A9die_No.1_%28Satie%2C_%C3%89ric%29).

Composition rights assessment: Public domain. The source page dates the work to 1888 and identifies Satie. The composition is outside the applicable life-plus-term period and was published in the nineteenth century.

Performer and recording source: Teknopazzo, identified on the Wikimedia Commons page as the creator of the own-work recording.

Recording source page: [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Gymnopedie_No._1..ogg).

Direct download URL: `https://upload.wikimedia.org/wikipedia/commons/b/b7/Gymnopedie_No._1..ogg`.

Recording license: [CC0 1.0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).

Usage terms: Copy, edit, adapt, and distribute the derivative without attribution or ShareAlike obligations. Retaining a courtesy credit to Teknopazzo and the source link is recommended for provenance.

License confidence: High for the recording and composition. The Commons page identifies the uploader's own work and applies CC0 1.0 to the file.

Recording date: Not stated on the source page. The 2010 file-history entry is an upload date, not a claimed performance date.

Original downloaded source: `docs/super_events/031_random_terror/audio_sources/erik_satie_gymnopedie_no_1.commons.ogg`.

Original source SHA-256: `13E4E03797169392166B9F11D9BF9C421C022B48AD87D9B10BD441CE068502DA`.

Original source format: Ogg FLAC, stereo, 22,050 Hz, 204.799546 seconds, 6,502,597 bytes.

Attribution text: `Erik Satie, Gymnopédie No. 1, recording by Teknopazzo, CC0 1.0, source via Wikimedia Commons. Edited for Chaos Redux.`

### Final derivative

Suggested super-event use: The Broken Claim, the reflective liberation and reconstruction announcement after the global final state is broken.

Why it fits: The spare piano pulse, recurring phrases, and restrained harmonic motion convey relief that is real but incomplete. It supports survivors, damaged public life, and vigilance without becoming a clean victory march or making a claim about what the entity was.

Final runtime path: `sound/031_random_terror/super_event_105_false_revelation_defeat_aftermath.wav`.

Final duration: 110.000 seconds, or 01:50.

Final SHA-256: `98F8AB8AA53F91F0402CAEE45A83EDA3803FE8B77CC9E2498335E7B28BEED1C0`.

Final format: PCM signed 16-bit little-endian, stereo, 44,100 Hz, 19,404,078 bytes.

Transformation recipe: Decode the preserved OGG FLAC source with FFmpeg 8.1.1, take the opening 110.000 seconds, apply a fixed -2.0 dB gain, apply a 0.20 second fade-in, apply a 4.00 second fade-out beginning at 106.000 seconds, resample to 44,100 Hz, convert to stereo PCM16, and write the WAV. No time stretch, pitch shift, loop, synthetic layer, oscillator, or added sound effect was used.

The fixed gain leaves the measured final sample peak at approximately -2.5 dBFS. The source is retained unchanged.

## Proposed wiring handoff

The following IDs extend the catalogue baseline that ended at playback audio ID `103`. The parent must perform a live super-event registry collision check before accepting `104` and `105`. No display slot number was guessed in this research tranche.

| Role | Proposed playback audio ID | Proposed base sound definition ID | Final runtime file |
|---|---:|---|---|
| False Revelation reveal | `104` | `chaosx_super_event_random_terror_false_revelation_reveal_track` | `sound/031_random_terror/super_event_104_false_revelation_reveal.wav` |
| False Revelation defeat aftermath | `105` | `chaosx_super_event_random_terror_false_revelation_defeat_aftermath_track` | `sound/031_random_terror/super_event_105_false_revelation_defeat_aftermath.wav` |

Proposed reveal volume wrappers are `chaosx_super_event_104_sound_0_5`, `chaosx_super_event_104_sound_1_0`, `chaosx_super_event_104_sound_1_5`, `chaosx_super_event_104_sound_2_0`, `chaosx_super_event_104_sound_2_5`, and `chaosx_super_event_104_sound_3_0`.

Proposed aftermath volume wrappers are `chaosx_super_event_105_sound_0_5`, `chaosx_super_event_105_sound_1_0`, `chaosx_super_event_105_sound_1_5`, `chaosx_super_event_105_sound_2_0`, `chaosx_super_event_105_sound_2_5`, and `chaosx_super_event_105_sound_3_0`.

Each wrapper should use the existing volume pattern of `0.67`, `1.33`, `2.00`, `2.67`, `3.33`, and `4.00`, with `max_audible = 1` and `max_audible_behaviour = fail`, and should point to its role's base sound definition.

The parent should set `global.current_super_event_audio_id` to the accepted playback ID and call `play_current_super_event_sound = yes` through the settings-aware helper for each role.

The canonical catalogue rows for `The False Revelation` and `The Broken Claim` are recorded in `music/chaosx_music_track_list.html` with provisional playback IDs `104` and `105`. The parent must replace those IDs and wrapper names if the live registry assigns different values. Each row retains the source title, composer, recording source, duration, license, source checksum, final checksum, and attribution text recorded here.

## Open blockers and uncertainties

There is no audio rights blocker. Both selected recordings have a documented composition-rights basis and a documented recording license that permits the mechanical derivatives supplied here.

Live display-slot assignment was not available in the audio-only source set. The parent must inspect the live super-event registry and replace the provisional numeric IDs and wrapper names if `104` or `105` collide.

The final text researcher selected `The False Revelation` and `The Broken Claim`. The parent should merge these audio facts into the full super-event research note and keep the audio roles aligned with those titles.

The Mussorgsky source page does not identify a recorder and only tentatively identifies the Skidmore College Orchestra. This is a provenance uncertainty, not a rights blocker, because the source page records Musopen's worldwide public-domain release and the Wikimedia permission record.
