# Event 006 super-event 23 audio research v115

Research date: 2026-08-06.

Scope: revalidate a legally usable source candidate for Event 006, **The League of New States**, under the current ordinary super-event/audio identifier `23`. This handoff covers source identity, composition and recording rights, preserved-source checksums, technical suitability, and the parent-owned wiring boundary. It does not edit event scripts, gameplay, scripted localisation, `.gfx`, sound definitions, the music catalogue, or spreadsheets.

## Decision status

The accepted Jeremiah Clarke / London Brass Players recording of *A Trumpet Voluntary* remains blocked. The composition is public domain, but the exact 1948 recording released in 1949 still has no verified United States redistribution permission or waiver. It was not downloaded or processed.

The strongest replacement candidate is **Defilier-Marsch** by Carl Faust, performed by the Anker-Orchester. The Public Domain Project source record marks the composition and historical recording public domain internationally (`PD-INT`, effective 1 January 2010), and Wikimedia Commons preserves the matching source metadata. The candidate is suitable for copying, editing, and redistribution when that source determination is accepted, but it is not a signed modern CC0 waiver.

Candidate status is **USER REVIEW REQUIRED**. The parent must audition the excerpt, accept the period German military-march association for a pluralistic league proclamation, and confirm that the Public Domain Project's international public-domain determination is sufficient for the intended distribution jurisdictions. No runtime file, sound identifier, wrapper, catalogue row, or firing package was created in this pass.

Runtime wiring therefore **cannot be closed** without an explicit candidate-selection and jurisdiction decision. No unapproved fallback was used.

## Current ordinary-23 surface inspection

The current sound surface was inspected only to establish the parent handoff boundary.

| Surface | Current finding |
| --- | --- |
| `sound/chaosx_sound.asset` | No `chaosx_super_event_23_track` or `chaosx_super_event_23_sound_*` names are registered. Audio `24` is the existing Event 006 precedent. |
| Event 006 audio `24` wrappers | Six settings-volume wrappers use volumes `0.67`, `1.33`, `2.00`, `2.67`, `3.33`, and `4.00`; each retains `max_audible = 1` and `max_audible_behaviour = fail`. |
| `music/chaosx_music_track_list.html` | No ordinary audio-`23` row exists. This pass intentionally did not add one. |
| Candidate files | Source and derivative remain under `docs/assets/006_independence_wave/super_events/audio/`; they are research evidence and not runtime consumers. |

The established one-shot pattern implies no loop flag for the eventual ordinary-23 wrappers. Do not add a loop or concatenate the march unless the parent receives a separate approval.

## Candidate identity and provenance

- Track title: *Defilier-Marsch*.
- Composer: Carl Faust (1825–1892).
- Performer and recording source: Anker-Orchester, Berlin, German Reich.
- Recording metadata: first release and recording between 1905 and 1910; the source record lists 1910 as the performance year.
- Genre/content: structured military/parade march, not a generated tone, oscillator, drone, stinger, sound effect, or texture bed.
- Wikimedia Commons source page, stable revision reviewed for this handoff: <https://commons.wikimedia.org/w/index.php?title=File:CC0-CH_-_Anker-Orchester_-_Defilier-Marsch_-_Carl_Faust_-_Anker-5387-10819.flac&oldid=1127396843>.
- Public Domain Project record: <http://pool.publicdomainproject.org/index.php?title=Anker-5387-10819>.
- Legitimate lossless download: <https://pool.publicdomainproject.org/audio/flac/anker/anker-5387-10819.flac>.
- Legitimate Ogg mirror: <https://pool.publicdomainproject.org/audio/ogg/anker/anker-5387-10819.ogg>.
- Commons source field: `{{Pdproject/source_url|Anker-5387-10819}}`.

## Composition and recording rights

Composition and recording rights were assessed separately.

### Composition

The Commons and Public Domain Project records identify Carl Faust as 1825–1892 and apply `Pd-old-70`. The Public Domain Project record lists the item under `PD-INT` from 1 January 2010. On that source record, the composition is public domain internationally.

### Recording

The Public Domain Project record also lists this historical Anker-Orchester recording under `PD-INT` from 1 January 2010. The Commons permission field carries `{{Cc-zero-project}} {{Pd-old-70}}`. `Cc-zero-project` identifies the collection's source marker; it is not by itself a signed modern `CC0` dedication. The rights conclusion rests on the dated Public Domain Project international public-domain determination plus the matching Commons source metadata.

- License: Public Domain Project `PD-INT` public-domain determination from 2010; Wikimedia Commons `Cc-zero-project` collection record.
- License confidence: **high** when the Public Domain Project determination is accepted; **not absolute** because the evidence is an archival/project rights record rather than a rights-holder-signed waiver.
- Usage terms: copying, adaptation, distribution, and game-mod packaging are permitted under the source public-domain determination; no legal attribution is required by that determination.
- Courtesy attribution: `Carl Faust, Defilier-Marsch; Anker-Orchester, recording c. 1905–1910; source Public Domain Project / Wikimedia Commons; public domain; edited excerpt.`
- Jurisdiction note: the parent must confirm that the source-record international basis is acceptable for the intended release jurisdictions before runtime promotion.

## Preserved source and checksums

The immutable source and an Ogg mirror were already preserved by the preceding candidate pass and were re-read for this handoff.

### FLAC source

- Local path: `docs/assets/006_independence_wave/super_events/audio/source/CC0-CH_Anker-Orchester_Defilier-Marsch_Carl-Faust_Anker-5387-10819.flac`.
- Size: `111203362` bytes.
- Container/codec: FLAC, stereo, 192,000 Hz, 32-bit decoded samples.
- Duration: `203.669333` seconds.
- SHA-256: `5E34AEE847FBA828565D60B94E2D8099402632D7CA118733DB03293A9759F45E`.
- SHA-1: `A8E803BE908B5DCCD2316CB1A01AF23AB4429B5B`.

### Ogg mirror

- Local path: `docs/assets/006_independence_wave/super_events/audio/source/Defilier-Marsch_Anker-Orchester_Carl-Faust_1905-1910.ogg`.
- Size: `24444579` bytes.
- Container/codec: Ogg Vorbis, stereo, 192,000 Hz.
- Duration: `203.669333` seconds.
- SHA-256: `708D01150EF558353E4AABAF2020F061317360C5A63990CD3175DA15A2DC371E`.
- SHA-1: `99BD61CC2D991A268C41BBE126B5E8C7B7CDFD8D`.

## Research derivative and technical suitability

The following derivative is **not** a runtime asset. It is retained only so the parent can audition a bounded candidate without touching the immutable source.

- Candidate path: `docs/assets/006_independence_wave/super_events/audio/candidate/super_event_23_defilier_marsch_110s_candidate.wav`.
- Candidate size: `19404160` bytes.
- Container/codec: RIFF/WAV, PCM signed 16-bit little-endian.
- Sample rate/layout: 44,100 Hz, stereo.
- Decoded duration: `110.000000` seconds.
- SHA-256: `3FA6324F6AF551818F65076956464FE7638423F3114BA9E45B2D81EF6DD3FFF2`.
- SHA-1: `E22C71D32F089E6E7024EDB3934C2B076B18436E`.
- Embedded tags: title `Defilier-Marsch`, artist `Anker-Orchester`, date `1905`, genre `March music`.
- Loop metadata: none; the intended playback mode is one-shot with no loop.
- Silence check: no interval of at least `0.25 s` below `-50 dBFS` was found in the retained derivative.
- Loudness readback: approximately `-18.0 LUFS` integrated, `5.0 LU` loudness range, and `-2.0 dBTP` true-peak field in FFmpeg's `ebur128` report.

### Editing and conversion record

1. The FLAC and Ogg originals were preserved unchanged before derivative work.
2. The first 110.000 seconds were selected provisionally for a one-shot excerpt.
3. A 1.5-second fade-in and a 2.0-second fade-out beginning at excerpt time 108.000 seconds were applied.
4. Two-pass linear loudness normalization targeted `-18 LUFS` with a `-2 dBTP` ceiling while preserving the source dynamics.
5. The result was resampled to 44.1 kHz and encoded as stereo PCM S16LE WAV.
6. FFprobe and FFmpeg readback confirmed the candidate duration, stream format, loudness, and decodability.

The first 110 seconds have not been certified as a phrase-safe musical boundary by listening. The parent must audition the opening and fade endpoint before approving the derivative.

### Volume suitability

The derivative leaves headroom at the source level and does not bake in extra gain. If selected, it can use the established six settings-aware wrappers with volumes `0.67`, `1.33`, `2.00`, `2.67`, `3.33`, and `4.00`, retaining `max_audible = 1` and `max_audible_behaviour = fail`. The nominal `1.5` setting is the recommended first audition; the parent should not add an additional gain stage during promotion.

## Super-event fit and pacing

The steady brass/orchestral parade pulse makes a newly ratified league audible as a public institutional procession rather than a routine faction popup. A continuous 110-second one-shot gives the super-event window a complete ceremonial arc without looping or concatenating a march section.

The main risk is political valence. The Berlin/German period-march context and military title can read as national or militarist rather than pluralistic or mutually defensive. Suitability is **high for musical structure and source evidence, medium for the League's political/tonal fit** until the parent listens and accepts that association.

## Parent-owned promotion and wiring boundary

Only after explicit selection and jurisdiction approval should the parent:

1. Copy or re-derive the accepted excerpt to `sound/006_independence_wave/super_event_23_league_of_new_states.wav`.
2. Register base sound `chaosx_super_event_23_track` and wrappers `chaosx_super_event_23_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, and `_3_0` using the established volume pattern.
3. Keep the one-shot/no-loop behavior and preserve `max_audible = 1` with `max_audible_behaviour = fail`.
4. Use ordinary audio ID `23`, set `global.current_super_event_audio_id` through the existing settings-aware path, and call `play_current_super_event_sound = yes`.
5. Add the ordinary-23 row to `music/chaosx_music_track_list.html` with the source, rights basis, attribution, duration, and derivative facts.
6. Wire the slot-23 firing/dispatch package and perform parent-owned integration checks.

None of these promotion or wiring actions were performed here.

## Blockers and exact runtime disposition

1. **Original accepted recording blocked:** the 1948/1949 London Brass Players recording still lacks verified United States redistribution rights.
2. **Candidate selection pending:** *Defilier-Marsch* is a rights-cleared research candidate, not an approved replacement. Human listening and political/tonal acceptance are required.
3. **Jurisdiction confirmation pending:** the candidate relies on the Public Domain Project's `PD-INT` source determination, not a separately signed worldwide CC0 waiver.
4. **Phrase-boundary confirmation pending:** the 110-second opening and fade endpoint need human audition.
5. **Runtime absent:** ordinary audio ID `23`, its base sound, six wrappers, catalogue row, and firing/playback assignment remain absent by design.

The Event 006 League package is therefore **incomplete and cannot claim runtime audio closure**. Promoting the candidate without the listed decisions would be an unapproved fallback, so no such promotion was made.

