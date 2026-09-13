# Event 31 Random Terror super-event audio handoff

Handoff date: 2026-08-29.

The audio package supplies two unique, rights-cleared musical recordings for Event 31 Random Terror. The parent owns final sound-definition edits, super-event slots, event wiring, localisation, and workbook alignment.

Final text role alignment: the reveal title is `The False Revelation` and the defeat aftermath title is `The Broken Claim`.

## Delivered files

| Role | Final WAV | Duration | Format | SHA-256 |
|---|---|---:|---|---|
| The False Revelation reveal | `sound/031_random_terror/super_event_104_false_revelation_reveal.wav` | 110.000 s | PCM16 stereo 44,100 Hz | `8701046C4C7A72FED2AFF7B567ABAD36D43E10BEE2469A3C2C64E487B4FFAA25` |
| The Broken Claim defeat aftermath | `sound/031_random_terror/super_event_105_false_revelation_defeat_aftermath.wav` | 110.000 s | PCM16 stereo 44,100 Hz | `98F8AB8AA53F91F0402CAEE45A83EDA3803FE8B77CC9E2498335E7B28BEED1C0` |

Both final files are in the event-scoped runtime folder and are within the requested one to two minute range.

## Preserved source files

| Role | Original source | Source URL | Source SHA-256 | Rights confidence |
|---|---|---|---|---|
| Reveal | `docs/super_events/031_random_terror/audio_sources/modest_mussorgsky_night_on_bald_mountain.commons.ogg` | [Wikimedia Commons source page](https://commons.wikimedia.org/wiki/File:Modest_Mussorgsky_-_night_on_bald_mountain.ogg) and direct file `https://upload.wikimedia.org/wikipedia/commons/c/ca/Modest_Mussorgsky_-_night_on_bald_mountain.ogg` | `F0C7F3CD9DC3B746FD8080860012BA152B99760021431F127070A2825D2CEFC9` | High for composition and recording license. Medium for unnamed recorder metadata. |
| Defeat aftermath | `docs/super_events/031_random_terror/audio_sources/erik_satie_gymnopedie_no_1.commons.ogg` | [Wikimedia Commons source page](https://commons.wikimedia.org/wiki/File:Gymnopedie_No._1..ogg) and direct file `https://upload.wikimedia.org/wikipedia/commons/b/b7/Gymnopedie_No._1..ogg` | `13E4E03797169392166B9F11D9BF9C421C022B48AD87D9B10BD441CE068502DA` | High for composition and recording license. |

The preserved source formats are Ogg Vorbis stereo 48,000 Hz at 733.200 seconds for Mussorgsky and Ogg FLAC stereo 22,050 Hz at 204.799546 seconds for Satie.

## Rights and attribution

### Reveal

Track: `Night on Bald Mountain`, Modest Petrovich Mussorgsky.

Composition source: [IMSLP](https://imslp.org/wiki/Night_on_Bald_Mountain_%28Mussorgsky%2C_Modest%29).

Composition rights: Public domain. The source page identifies the 1886 work and the composer who died in 1881. The commonly circulated 1886 revision is also outside modern copyright terms because Nikolay Rimsky-Korsakov died in 1908.

Recording source: Musopen through Wikimedia Commons. The file page records a worldwide public-domain release and a courtesy request for Musopen attribution in derived or commercial works.

Suggested attribution: `Modest Mussorgsky, Night on Bald Mountain, recording released to the public domain by Musopen, source via Wikimedia Commons. Edited for Chaos Redux.`

### Defeat aftermath

Track: `Gymnopédie No. 1`, Erik Satie.

Composition source: [IMSLP](https://imslp.org/wiki/Gymnop%C3%A9die_No.1_%28Satie%2C_%C3%89ric%29).

Composition rights: Public domain. The work was published in 1888 and Satie died in 1925.

Recording source: Teknopazzo own work through Wikimedia Commons.

Recording rights: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

Suggested attribution: `Erik Satie, Gymnopédie No. 1, recording by Teknopazzo, CC0 1.0, source via Wikimedia Commons. Edited for Chaos Redux.`

## Mechanical transformation receipts

The reveal derivative used the opening 110.000 seconds, +1.0 dB fixed gain, a 0.20 second fade-in, a 4.00 second fade-out from 106.000 seconds, 44,100 Hz resampling, stereo conversion, and signed PCM16 WAV output.

The defeat derivative used the opening 110.000 seconds, -2.0 dB fixed gain, a 0.20 second fade-in, a 4.00 second fade-out from 106.000 seconds, 44,100 Hz resampling, stereo conversion, and signed PCM16 WAV output.

The original files remain unchanged. No time stretch, pitch shift, loop, synthetic layer, oscillator, test tone, drone, sound-effect bed, or added effect was used.

The conversion tool was FFmpeg 8.1.1.

## Implemented IDs and parent wiring

The source filenames retain the research package's provisional `104` and `105` stems. The parent rechecked the live super-event display and playback registries after concurrent event packages occupied the intervening slots. The first collision-free pair is `114` and `115`, and those IDs are now authoritative for both display and settings-aware playback.

| Role | Implemented display/playback ID | Base sound ID | Runtime path |
|---|---:|---|---|
| Reveal | `114` | `chaosx_super_event_random_terror_false_revelation_reveal_track` | `sound/031_random_terror/super_event_104_false_revelation_reveal.wav` |
| Defeat aftermath | `115` | `chaosx_super_event_115_track` | `sound/031_random_terror/super_event_105_false_revelation_defeat_aftermath.wav` |

Implemented reveal wrapper IDs: `chaosx_super_event_114_sound_0_5`, `chaosx_super_event_114_sound_1_0`, `chaosx_super_event_114_sound_1_5`, `chaosx_super_event_114_sound_2_0`, `chaosx_super_event_114_sound_2_5`, and `chaosx_super_event_114_sound_3_0`.

Implemented defeat wrapper IDs: `chaosx_super_event_115_sound_0_5`, `chaosx_super_event_115_sound_1_0`, `chaosx_super_event_115_sound_1_5`, `chaosx_super_event_115_sound_2_0`, `chaosx_super_event_115_sound_2_5`, and `chaosx_super_event_115_sound_3_0`.

Each wrapper should use the current `0.67`, `1.33`, `2.00`, `2.67`, `3.33`, and `4.00` volume pattern, `max_audible = 1`, and `max_audible_behaviour = fail`.

`random_terror_emit_super_event` sets `global.current_super_event_audio_id` from the accepted role ID and calls `play_current_super_event_audio = yes` through the shared settings-aware helper for each human country.

Canonical catalogue rows for `The False Revelation` and `The Broken Claim` are present in `music/chaosx_music_track_list.html` with final playback IDs `114` and `115`. The rows carry the source title, composer, recording source, duration, license, source hash, final hash, and attribution text from this handoff.

## Blockers and uncertainties

No source-rights, registry, format, or settings-wiring blocker remains. Both final WAVs are delivered and wired.

The parent collision audit found one display sprite each for slots `114` and `115`, one definition for each of the twelve Event 31 volume wrappers, and no other Event 31 consumer of either playback ID. The source WAV names remain unchanged because filenames do not define the playback registry.

The final text researcher selected `The False Revelation` and `The Broken Claim`. The parent should merge the audio note into the full super-event research note and keep the audio roles aligned with those titles.

The Night on Bald Mountain Commons metadata does not name the recorder and only tentatively identifies the orchestra. This does not block use because the recording license is explicitly documented as a worldwide Musopen public-domain release.

Research-worker changed-scope statement: the research pass did not edit sound definitions, event scripts, localisation, or workbook files. Parent integration subsequently updated the sound registry, Event 31 constants and dispatch, localisation, super-event sprites, and music catalogue.
