# Event 006 super-event 23 audio revalidation — 2026-09-05

Status: fail-closed audio handoff. Slot `23` remains unselected, unregistered, and unwired.

Scope: bounded source, licensing, provenance, technical-format, and tone revalidation for ordinary Event 006 super-event/audio ID `23`, **The League of New States**.

This pass does not edit event scripts, gameplay, scripted localisation, `.gfx`, sound definitions, the canonical music catalogue, spreadsheets, slot dispatch, or firing logic.

## Decision

The accepted Jeremiah Clarke / London Brass Players recording of *A Trumpet Voluntary* remains blocked for United States and worldwide redistribution because the exact 1948 recording and 1949 first release have no verified recording-rights permission or rights-holder waiver in the accepted evidence.

The recording was not downloaded, processed, or wired.

The strongest currently preserved replacement candidate is **Alte Kameraden**, composed by Carl Teike and recorded by the Anker-Orchester in Berlin between 1905 and 1910.

The Public Domain Project item record explicitly identifies this exact recording item and records `Pdch=1 January 1993`, `Pdeu=1 January 1993`, `Pdusa=1 January 1998`, and `Pdint=1 January 2023`, with `{{PD-EU}}` applied to the item.

The matching Wikimedia Commons record identifies the same title, composer, performer, and recording window and carries `{{Cc-zero-project}} {{Pd-old-70}}` with a source link back to the Public Domain Project item.

This is a rights-complete **conditional research candidate**, not an approved replacement: the parent/user must explicitly reopen the accepted selection, perform a human audition, and accept the source-based jurisdiction finding before runtime promotion.

## Current ASSET-005 consumer and fail-closed state

ASSET-005 is the league-formation super-event image family `GFX_super_event_006_asset_005_league_formation` rendered by the shared super-event presentation system.

The image and text dispatch for display slot `23` are registered, but slot-23 audio, sound wrappers, and firing reachability remain intentionally absent.

Static revalidation on 2026-09-05 found `sound/006_independence_wave/` containing only `super_event_24_every_border_a_casus_belli.wav`.

The bounded `sound/chaosx_sound.asset` scan contains `chaosx_super_event_24_track` and its six wrapper soundeffects but no `chaosx_super_event_23_track` or slot-23 wrappers.

The bounded `music/chaosx_music_track_list.html` scan contains the Event 006 audio-catalogue row for ID `24` and no promoted row for ID `23`.

No `global.current_super_event_audio_id = 23` assignment or slot-23 firing path was introduced by this pass.

## Candidate record

| Field | Verified value |
| --- | --- |
| Super-event | `23` — The League of New States |
| Suggested audio ID | `23` only after explicit replacement approval; no assignment was made |
| Suggested base sound definition | `chaosx_super_event_23_track` if selected; no definition was edited |
| Track title | *Alte Kameraden* |
| Composer | Carl Teike (1864–1922) |
| Performer / recording source | Anker-Orchester; no conductor identified in the source record |
| Recording and release window | Berlin (German Reich), between 1905 and 1910; source metadata records 1910 as the performance year |
| Source duration | `204.522667 s` (`3:24.523`) |
| Candidate duration | `110.000000 s` (`1:50.000`) |
| Candidate WAV format | PCM signed 16-bit little-endian, 44.1 kHz, stereo |
| Suggested use | League proclamation, charter ratification, and the first durable union of small states |
| Suitability | Medium pending human audition; structured period march supports a public institution, but its German military-march association may read as more national or martial than pluralistic |
| License confidence | High for the exact item under the reviewed Public Domain Project `PD-INT 2023` record, with a jurisdiction and archive-freshness caveat; this is not a signed modern rights-holder waiver |

## Source and license receipts

Primary item record: <https://pool.publicdomainproject.org/index.php?title=Anker-5387-10815&oldid=38672&action=raw>.

Public Domain Project item page: <https://pool.publicdomainproject.org/index.php?title=Anker-5387-10815>.

Legitimate lossless source endpoint: <https://pool.publicdomainproject.org/audio/flac/anker/anker-5387-10815.flac>.

Legitimate Ogg source endpoint: <https://pool.publicdomainproject.org/audio/ogg/anker/anker-5387-10815.ogg>.

Wikimedia Commons file record: <https://commons.wikimedia.org/w/index.php?title=File:CC0-CH_-_Anker-Orchester_-_Alte_Kameraden_-_Carl_Teike_-_Anker-5387-10815.flac&oldid=1231725899>.

Wikimedia Commons raw description: <https://commons.wikimedia.org/w/index.php?title=File:CC0-CH_-_Anker-Orchester_-_Alte_Kameraden_-_Carl_Teike_-_Anker-5387-10815.flac&oldid=1231725899&action=raw>.

CC-ZERO-PROJECT explanation: <https://commons.wikimedia.org/w/index.php?title=Template:Cc-zero-project/i18n/en&action=raw>.

Public Domain Project copyright-term note: <https://pool.publicdomainproject.org/index.php?title=Copyright_term_(Copyright)>.

The PDD raw item record returned HTTP 200 on 2026-09-05 with `Content-Type: audio/flac` for the lossless endpoint and `Content-Length: 111691902`.

The PDD Ogg endpoint returned HTTP 200 on 2026-09-05 with `Content-Type: audio/ogg` and `Content-Length: 23339477`.

The Commons raw description returned HTTP 200 on 2026-09-05 with `Content-Type: text/x-wiki; charset=UTF-8` and `Content-Length: 3002`.

The normalized fresh PDD raw response is byte-equivalent to the preserved local receipt with SHA-256 `204BE0259DCA9E77736D083EEFA23394D50EC1717E8195A9A606CCB860A4FC90`.

The normalized fresh Commons raw response is byte-equivalent to the preserved local receipt with SHA-256 `0A866E68EA42F3E6DBCEA0C2AE8646E0FF59FC1946439B928B1482C4CB0013DB`.

The PDD homepage currently states that the site is no longer maintained but that existing music files and information remain online.

That notice lowers provenance freshness but does not contradict the stable item record, which is preserved with its oldid, source URLs, and checksums.

The Commons `Cc-zero-project` marker describes the Wikimedia CH collection publication route and is not treated as a new legal CC0 dedication from the recording owner.

The recording-rights basis used here is the item-level PDD public-domain determination, including the explicit international date, rather than an unsupported inference from the composition's age or the Commons marker alone.

Composition and recording rights were checked separately.

Teike died in 1922, and the source record identifies the composition as public domain.

The same exact recording item carries the PDD `PD-INT 2023` determination, so no separate modern performer or label permission was identified in the reviewed source record.

This remains a source-based rights finding rather than legal advice, and a distributor should recheck local recording terms if distributing in a jurisdiction not covered by the source determination.

No legal attribution is required by the stated public-domain terms.

Courtesy attribution to retain if selected: `Carl Teike, “Alte Kameraden”; Anker-Orchester, recording c. 1905–1910; source: Public Domain Project / Wikimedia Commons; public domain under the source record; edited 110-second excerpt by Chaos Redux.`

## Preserved source and candidate files

The original downloaded sources remain unchanged under the temporary Event 006 audio workspace.

| File | Format / decoded properties | Bytes | SHA-1 | SHA-256 |
| --- | --- | ---: | --- | --- |
| `docs/assets/006_independence_wave/super_events/audio/source/Alte_Kameraden_Anker-Orchester_Carl_Teike_1905-1910.flac` | FLAC, stereo, 192 kHz, source metadata 24-bit, `204.522667 s` | `111,691,902` | `F8C461C5D732631690D36910AF69E3D6D6B08482` | `5BD73736F50EB2DAF46545FB2FF2C73240C2EA2ED4246EF7A0EBF5536885B045` |
| `docs/assets/006_independence_wave/super_events/audio/source/Alte_Kameraden_Anker-Orchester_Carl_Teike_1905-1910.ogg` | Ogg Vorbis, stereo, 192 kHz, `204.522667 s` | `23,339,477` | `4B05EBF76D0C9018712AC3CEAE6F391EC334301C` | `48B7744B7620AC794E2FE09A441D21149F8477AFC7A91CAC49D7199106F9F462` |
| `docs/assets/006_independence_wave/super_events/audio/source/Alte_Kameraden_PublicDomainProject_Anker-5387-10815_oldid38672.raw.txt` | Preserved PDD raw item record, normalized receipt verified 2026-09-05 | `1,931` | `EAE16848EEFFA65FB93FAE637821D7D3AAE8B6D9` | `204BE0259DCA9E77736D083EEFA23394D50EC1717E8195A9A606CCB860A4FC90` |
| `docs/assets/006_independence_wave/super_events/audio/source/Alte_Kameraden_Commons_oldid1231725899.raw.txt` | Preserved Commons raw file description, normalized receipt verified 2026-09-05 | `3,002` | `B4A89945AA8DA6A7460C82ADA119DF860D84BAB6` | `0A866E68EA42F3E6DBCEA0C2AE8646E0FF59FC1946439B928B1482C4CB0013DB` |
| `docs/assets/006_independence_wave/super_events/audio/candidate/super_event_23_alte_kameraden_110s_candidate.wav` | PCM S16LE, stereo, 44.1 kHz, `110.000000 s` | `19,404,348` | `3CF071F2E036F19436F924B07D5771A4600AD28F` | `C261E01261D5DA78EE55FBA5D14F0747EA670495C8357E1CADA13465D33D0EF5` |
| `docs/assets/006_independence_wave/super_events/audio/candidate/super_event_23_alte_kameraden_110s_candidate.ogg` | Ogg Vorbis audition derivative, stereo, 44.1 kHz, `110.000000 s` | `3,157,396` | `13C45609FCB7E2A42FCD89AE5C5BFDFC6AA5C3CF` | `9B61E98CE78215D9E59AD9F807C7AFE4C460B3347283EBA8297465C2A24D5822` |

The candidate WAV is an audition derivative outside the runtime sound folder and is not a runtime final until the parent accepts the replacement.

## Editing and conversion record

1. The preserved FLAC source was probed as stereo 192 kHz FLAC with decoded duration `204.522667 s`.
2. Leading silence from `0.000000` through `1.070708 s` was detected at `-50 dBFS` with a `0.25 s` minimum interval.
3. Source time `1.070708 s` through `111.070708 s` was selected, removing only the detected lead-in and producing a 110-second one-shot excerpt.
4. A `1.5 s` fade-in was applied at candidate time `0.000 s`.
5. A `2.0 s` fade-out was applied beginning at candidate time `108.000 s`.
6. A two-pass EBU R128-style loudness pass targeted `-18 LUFS`, `-2 dBTP`, and `11 LU` target range.
7. The candidate was resampled to 44.1 kHz and encoded as stereo PCM S16LE WAV.
8. A separate Vorbis quality-6 Ogg audition derivative was encoded from the candidate WAV.
9. No loop, concatenation, generated tone, oscillator, drone, stinger, sound-effect layer, noise bed, or synthetic replacement was added.

FFprobe confirmed the candidate WAV as `pcm_s16le`, 44.1 kHz, stereo, 16-bit, and exactly `110.000000 s`.

FFprobe confirmed the audition Ogg as Vorbis, 44.1 kHz, stereo, and exactly `110.000000 s`.

The source FLAC, source Ogg, candidate WAV, and candidate Ogg each decoded to null with FFmpeg exit code `0` on 2026-09-05.

Candidate WAV loudness readback measured approximately `-17.9 LUFS` integrated loudness, `4.1 LU` loudness range, and `-2.0 dBTP` true peak.

The candidate WAV metadata identifies `Alte Kameraden`, Carl Teike, Anker-Orchester, the 1910 source date, the PDD/Commons source, the `PD-INT 2023` determination, the 110-second edit, the fades, and its not-wired research status.

## Super-event fit and audition gate

The source is an intentional structured musical recording with a stable ceremonial march pulse and period band/orchestral timbre.

It can support a public charter proclamation and first durable international institution while remaining distinct from Event 006 audio `24`.

The early twentieth-century acoustic character is compatible with the 1930s campaign setting.

The German military-march identity may read as national parade music rather than a pluralistic league, so suitability remains **medium pending human audition**.

The parent should audition the Ogg derivative at the opening, the central transition around `00:40–01:05`, and the final cadence and fade around `01:38–01:50`.

No perceptual human audition is claimed by this pass.

The candidate has no phrase-safe loop point claim and is intended as a one-shot cue.

## Parent-owned promotion boundary

Only after explicit parent/user selection, human audition approval, and jurisdiction acceptance may the parent copy `docs/assets/006_independence_wave/super_events/audio/candidate/super_event_23_alte_kameraden_110s_candidate.wav` to `sound/006_independence_wave/super_event_23_league_of_new_states.wav`.

The parent then owns base sound `chaosx_super_event_23_track`, wrappers `chaosx_super_event_23_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, and `_3_0`, the catalogue row, the slot-23 audio ID assignment, and settings-aware playback/firing wiring.

The permanent audio record must preserve the actual title, Carl Teike, Anker-Orchester, PDD and Commons URLs, the `PD-INT 2023` determination, the courtesy attribution, the 110-second edit notice, and the final runtime checksum.

Until those gates close, slot `23`, audio ID `23`, its wrappers, and its firing/playback assignment must remain absent from runtime.

## Remaining blockers and disposition

1. The accepted London Brass Players recording still lacks verified United States and worldwide redistribution permission for the exact recording.
2. The parent/user must explicitly select *Alte Kameraden* or another separately rights-cleared replacement before any runtime promotion.
3. Human audition is still required for timbre, period fit, pluralistic-league tone, phrase arc, and the final fade.
4. The PDD media pool is no longer maintained, so the oldid, raw receipt, source checksum, and jurisdiction caveat must remain attached to any promoted package.
5. The PDD `PD-INT 2023` result is a source-based archive determination rather than a signed modern rights-holder waiver, so the intended distribution jurisdictions require parent review.

Disposition: **conditional rights-complete candidate prepared; accepted cue remains blocked; parent selection, human audition, and jurisdiction review required; ASSET-005 remains fail-closed and slot 23 remains absent from runtime.**

## Files changed by this pass

- Added `docs/plans/006_independence_wave_plans/subagent_handoffs/006_super_event_23_audio_revalidation_2026-09-05.md`.
- No audio binaries were changed because the preserved source and game-format candidate already passed the bounded revalidation.
- No sound definition, event, gameplay, localisation, `.gfx`, catalogue, or firing file was changed.
