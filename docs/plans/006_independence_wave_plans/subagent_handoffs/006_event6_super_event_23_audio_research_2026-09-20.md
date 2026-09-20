# Event 006 super-event 23 audio research — 2026-09-20

Status: **rights-cleared candidate produced; runtime slot 23 remains unselected and unwired.**

Scope: bounded audio research and candidate production for Event 006, Independence Wave, super-event 23, **The League of New States**.

This pass does not edit `sound/chaosx_sound.asset`, `music/chaosx_music_track_list.html`, event scripts, localisation, `.gfx`, GUI, gameplay, central-admission logic, or spreadsheets.

## Decision

The accepted Jeremiah Clarke / London Brass Players recording remains blocked for the intended United States and worldwide redistribution.

The strongest candidate whose composition and recording rights are both supported by an explicit source license is **The Enola Foam March** by Peet Hudson / Peter Hudson, the creator's own orchestral recording, published from Wikimedia Commons under **CC BY-SA 4.0**.

The original source was already preserved in the temporary Event 006 audio workspace and was not overwritten.

A fresh 110-second game-ready PCM WAV was derived under the same temporary workspace.

This is a candidate handoff, not an approval to replace the accepted Clarke selection or to wire audio ID `23`.

## Recommended candidate: The Enola Foam March

| Field | Verified value |
| --- | --- |
| Suggested super-event use | Slot `23`, one-shot cue for league proclamation, charter ratification, and the first durable union of small states |
| Suggested audio ID | `23` only after parent acceptance; no runtime assignment was made |
| Suggested base sound definition | `chaosx_super_event_23_track` only if selected; no definition was edited |
| Track title | *The Enola Foam March*; embedded audio title is *Enola Foam March* |
| Creator / composer | Peet Hudson, also identified as Peter Hudson and Commons user `Peeeeet` |
| Performer / recording source | The creator's own digital orchestral recording; no separate performer, label, or third-party recording source is claimed in the reviewed source record |
| Source page | <https://commons.wikimedia.org/wiki/File:The_Enola_Foam_March.flac> |
| Stable source description | <https://commons.wikimedia.org/w/index.php?title=File%3AThe_Enola_Foam_March.flac&action=raw> |
| Direct source file | <https://upload.wikimedia.org/wikipedia/commons/e/e9/The_Enola_Foam_March.flac> |
| Creator profile | <https://commons.wikimedia.org/wiki/User:Peeeeet> |
| License | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) |
| License terms | Redistribution and adaptation, including commercial use, are permitted with attribution, a license link, an indication of changes, and ShareAlike-compatible distribution without additional restrictions on the audio |
| License confidence | **High for the identified composition and recording on the reviewed source record**, because the uploader identifies the file as own work and the source explicitly applies `self|cc-by-sa-4.0`; this is a source-evidence assessment, not legal advice |
| Required attribution | `Peet Hudson, “The Enola Foam March”; creator's own recording; source: Wikimedia Commons; licensed CC BY-SA 4.0; edited 110-second excerpt by Chaos Redux.` |
| Source duration | `175.776000 s` |
| Final candidate duration | `110.000000 s` |
| Fit | Structured orchestral-march pacing supports a public institutional proclamation and distinguishes the League from slot-24's militarized escalation cue |
| Fit risk | The source description's WWII-style and slight Klezmer framing can read as more period-military or culturally specific than the accepted legalist brass-and-organ concept; human audition and parent tone approval remain required |

### Separate rights review

Composition rights are supported by the creator's own-work declaration and the creator-applied CC BY-SA 4.0 license for the original 2012 composition.

Recording rights are supported by the same creator's own-work declaration for the digital orchestral recording and the same CC BY-SA 4.0 license.

No separate label, publisher, performer, or third-party recording license was identified in the reviewed source record.

The source FLAC contains an embedded cover-image stream, but the final WAV maps only the audio stream and carries no cover image.

### Preserved source and final candidate

| File | Format / duration | Bytes | SHA-1 | SHA-256 |
| --- | --- | ---: | --- | --- |
| `docs/assets/006_independence_wave/super_events/audio/source/The_Enola_Foam_March.flac` | FLAC, stereo, 48 kHz, `175.776000 s` | `14,162,067` | `33ED1D6F253F4BB05AA24CA1536AFCFE0B771A0B` | `34A26DF75C96DCFCE953E400DA9DAD2F4E9B61837EFD87FEF61CBD4B0614D547` |
| `docs/assets/006_independence_wave/super_events/audio/final/super_event_23_enola_foam_march_110s.wav` | PCM S16LE WAV, stereo, 44.1 kHz, `110.000000 s` | `19,404,212` | `4360DA6F476C1EC6F9CC3C3DCAF0930ACD24A1C4` | `2892F43CD393F2CA7FEED12FB8A841F9C7C6CA8784F28E2A39DC0AD3B9CECBFF` |

The earlier research derivative remains preserved at `docs/assets/006_independence_wave/super_events/audio/candidate/super_event_23_enola_foam_march_110s_candidate.wav` with SHA-1 `59837EA458A0F5DCE27947FA61D808B332BFA117` and SHA-256 `701C59F92F13A6E477AE9209168F910DCAC0A960B64EB1DE427BF4672B80A2ED`.

### Conversion evidence

1. The preserved FLAC source was decoded as stereo 48 kHz audio with duration `175.776000 s`.
2. The source interval `2.028812 s` through `112.028812 s` was selected, removing the documented leading silence and producing a 110-second one-shot excerpt.
3. A `1.5 s` fade-in was applied at excerpt time `0.000 s`.
4. A `2.0 s` fade-out was applied from excerpt time `108.000 s` through `110.000 s`.
5. FFmpeg loudness normalization targeted `-18 LUFS`, `-2 dBTP`, and `11 LU` LRA.
6. Post-conversion measurement reported approximately `-18.01 LUFS` integrated loudness, `-2.00 dBTP`, and `3.90 LU` LRA.
7. The output was resampled to 44.1 kHz and encoded as stereo PCM signed 16-bit little-endian WAV.
8. FFprobe revalidation confirmed `pcm_s16le`, stereo, 44.1 kHz, 16-bit, and exactly `110.000000 s`.
9. No generated tone, oscillator, ambience bed, drone, stinger, loop, or synthetic replacement was added.

## Candidate comparison

| Candidate | Composition rights | Recording rights / source | Duration and evidence | Verdict for slot 23 |
| --- | --- | --- | --- | --- |
| *A Trumpet Voluntary*, Jeremiah Clarke; London Brass Players | Composition public domain | 1948 recording, first released 1949; Commons/PDD labels do not provide a verified United States recording-right waiver or rights-holder permission | `167.5730416667 s`; remote Commons SHA-1 `6320e3d289d959acf0a871d1bea3cfa7b3d3b7fa`; source intentionally not downloaded | **Blocked.** Do not process or wire without an exact-recording United States/worldwide permission or waiver. |
| **The Enola Foam March**, Peet Hudson | Own 2012 composition under the creator's CC BY-SA 4.0 self-publication | Own digital orchestral recording under the same explicit CC BY-SA 4.0 source record | Source `175.776000 s`; source SHA-256 `34A26DF75C96DCFCE953E400DA9DAD2F4E9B61837EFD87FEF61CBD4B0614D547`; final WAV `110.000000 s`, SHA-256 `2892F43CD393F2CA7FEED12FB8A841F9C7C6CA8784F28E2A39DC0AD3B9CECBFF` | **Recommended rights-cleared candidate.** Parent must accept the composition change, attribution, edit notice, ShareAlike treatment, and musical tone. |
| *Toujours en Tête* / *Defileermars van het Regiment Infanterie Johan Willem Friso*, S.P. van Leeuwen | 1961 composition; not treated as public domain; rights rely on the Ministry/VRT permission record represented on Commons | Koninklijke Militaire Kapel “Johan Willem Friso”; Commons `Mindef` record applies CC BY-SA 4.0, but the official music URL recorded by Commons currently returns 404 and the exact composition/recording coverage is not independently explicit | Source `145.946122 s`; source SHA-256 `99CBD948C3066B7919BF75EB385736EDF81A500486284F857C6B06A1CF885D57`; prior 110-second candidate SHA-256 `7C2B417332309386E6FE1343F34520D9D67A754E6050EDD4E7CEE92D47B16680` | **Not fully closed.** Retain as research evidence only; do not promote without recovering a current official source or a more explicit recording/composition permission. |
| *Jeremiah Clarke - Prince of Denmark's March Harpsichord*, Jeremiah Clarke; Fehufanga | Composition public domain | Fehufanga's own recording, explicitly CC BY-SA 3.0 | Source `108.135329 s`; source SHA-1 `62DCF8C444D8DFF8C71BFB77033773CB7C5C29F4`, SHA-256 `8C35F2ED5405AAA2DB02A93017759CD4AD290017ED37B7DD134FF4390F910F22` | **Rights-clear but not preferred.** Harpsichord-only timbre does not preserve the approved brass-and-organ concept; no new derivative was made in this pass. |
| *Alte Kameraden*, Carl Teike; Anker-Orchester | Composition public domain | Public Domain Project / Commons archive determination; exact early recording is preserved, but the archive is no longer maintained and the record is weaker than a direct creator or government CC license | Source `204.522667 s`; source SHA-256 `5BD73736F50EB2DAF46545FB2FF2C73240C2EA2ED4246EF7A0EBF5536885B045`; prior 110-second candidate SHA-256 `C261E01261D5DA78EE55FBA5D14F0747EA670495C8357E1CADA13465D33D0EF5` | **Conditional only.** Strong ceremonial structure, but higher archive/jurisdiction uncertainty and a strong German military-march association. |

## Runtime state and exact remaining gate

The runtime file `sound/006_independence_wave/super_event_23_league_of_new_states.wav` does not exist.

The bounded scan found no slot-23 base sound, settings-wrapper family, catalogue row, or runtime audio assignment in `sound/chaosx_sound.asset` or `music/chaosx_music_track_list.html`.

The recommended Enola candidate clears the source-license evidence gate, but slot 23 is not complete because the accepted Clarke recording has not been cleared and the parent has not yet accepted a replacement composition and its CC BY-SA distribution treatment.

The next owner must audition the final WAV, confirm that the WWII/Klezmer framing fits the pluralistic League reveal, decide whether the mod can carry CC BY-SA 4.0 attribution and ShareAlike-compatible audio terms, and then either accept the replacement for parent-owned runtime wiring or reject it and leave slot 23 blocked.

If accepted, the parent should use the proposed base id `chaosx_super_event_23_track`, the six settings-aware wrapper ids `chaosx_super_event_23_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, and `_3_0`, and the runtime path `sound/006_independence_wave/super_event_23_league_of_new_states.wav` only after completing the separate wiring and catalogue changes.

## Files changed in this pass

- Added `docs/assets/006_independence_wave/super_events/audio/final/super_event_23_enola_foam_march_110s.wav`.
- Added this handoff at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_super_event_23_audio_research_2026-09-20.md`.
- Preserved source `docs/assets/006_independence_wave/super_events/audio/source/The_Enola_Foam_March.flac` was read and hashed but not modified.
- No sound definition, canonical music catalogue, event, localisation, `.gfx`, GUI, gameplay, central-admission, or spreadsheet file was changed.

Disposition: **slot 23 remains runtime-unselected and unwired; The Enola Foam March is a produced, rights-cleared candidate pending parent acceptance and human audition.**
