# Event 006 super-event 23 audio candidate handoff — 2026-08-29

Status: rights-cleared candidate prepared for parent review; slot `23` remains unselected and unwired.

This handoff does not replace the accepted London Brass Players recording in the Event 006 specification.

The accepted London recording remains blocked for United States redistribution because its recording-rights basis is not verified.

The candidate below preserves the accepted work, composer, audio role, and 110-second production shape, but it is a different recording and therefore requires explicit parent/user approval before any runtime promotion.

## Candidate summary

| Field | Candidate value |
| --- | --- |
| Super-event | `23` — The League of New States |
| Audio ID / display slot | `23` |
| Suggested sound definition ID | `chaosx_super_event_23_track` if and only if this replacement is approved; no definition was edited |
| Track title | `A Trumpet Voluntary (The Prince of Denmark's March)` |
| Composer | Jeremiah Clarke (the accepted work; the source page identifies the alternate title) |
| Performer / recording source | Orgelputzer; the Commons page declares an own arrangement and own recording, but does not state the instrumentation |
| Source recording date | The Commons file page dates the recording/file to 2023; upload history records 21 January 2023 |
| Source duration | `133.903673 s` decoded from the preserved Ogg source |
| Candidate duration | `110.000000 s` decoded from both final derivatives |
| Candidate use | Formal league proclamation, covenant ratification, and the first durable union of small states |
| Rights disposition | Recording: CC BY-SA 4.0 self-release; composition: public-domain Jeremiah Clarke work |
| License confidence | Medium-high for the recording based on the live self-release declaration and Commons license metadata; lower than a named institutional or creator-profile waiver because the uploader profile is absent |

## Rights and source evidence

The live Wikimedia Commons file page was checked on 2026-08-29 at revision `861713497`.

The current file description states that the source is the uploader's own arrangement and own recording and carries `{{self|cc-by-sa-4.0}}`.

Commons API metadata reports `CC BY-SA 4.0` and `Creative Commons Attribution-Share Alike 4.0` for the same file.

The uploader's Commons account has no profile page, so the self-authorship assertion is strong direct platform evidence but not independently identity-verified.

The composition is Jeremiah Clarke's public-domain work, commonly titled *The Prince of Denmark's March* or *A Trumpet Voluntary*.

CC BY-SA 4.0 permits redistribution and adaptation, including commercial use, when the project gives appropriate credit, links the license, indicates changes, and licenses adaptations under the same terms.

Required attribution text for this candidate:

> Jeremiah Clarke, *A Trumpet Voluntary (The Prince of Denmark's March)*; arrangement and recording by Orgelputzer; licensed under CC BY-SA 4.0 via Wikimedia Commons.

Source page: <https://commons.wikimedia.org/wiki/File:Clarke_Trumpet_Voluntary.ogg>

Source-page raw wikitext: <https://commons.wikimedia.org/w/index.php?title=File%3AClarke_Trumpet_Voluntary.ogg&action=raw>

Direct downloaded media: <https://upload.wikimedia.org/wikipedia/commons/e/e2/Clarke_Trumpet_Voluntary.ogg>

License deed: <https://creativecommons.org/licenses/by-sa/4.0/>

## Preserved source and final files

The original downloaded source is preserved before conversion at:

`docs/assets/006_independence_wave/super_events/audio/source/Clarke_Trumpet_Voluntary.ogg`

| File | Format and decoded properties | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `docs/assets/006_independence_wave/super_events/audio/source/Clarke_Trumpet_Voluntary.ogg` | Ogg Vorbis, 44.1 kHz, stereo, `133.903673 s` | `2,463,223` | `5F6065B7E83F2A952816142D58419FB1F1BEBFF1D61F9141624C94301745C783` |
| `docs/assets/006_independence_wave/super_events/audio/candidate/super_event_23_clarke_trumpet_voluntary_110s_candidate.wav` | PCM signed 24-bit little-endian, 44.1 kHz, stereo, `110.000000 s` | `29,106,506` | `9D6DCE7D1DB197A4B68C1092610DFA31B1C7F8FBF93172476AA03AFD116EE584` |
| `docs/assets/006_independence_wave/super_events/audio/candidate/super_event_23_clarke_trumpet_voluntary_110s_candidate.ogg` | Ogg Vorbis, 44.1 kHz, stereo, `110.000000 s` | `2,130,679` | `B9FDDC1C6BAF8AEB9830DFCA8D45D6C66FD19A6A984F00069A2EE7507F5DD883` |

The source and candidate files are stored under the event asset workspace, which is intentionally ignored by the repository's normal asset ignore rule; the tracked handoff is the provenance and wiring boundary.

## Editing and conversion

1. Downloaded the current Commons original from the direct URL above and preserved it without modification.

2. Removed the measured `0.52746 s` leading silence and selected source interval `0.52746` through `110.52746 s` for the accepted 110-second cue shape.

3. Applied a `1.5 s` fade-in and a `2 s` fade-out beginning at candidate second `108`.

4. Ran FFmpeg `loudnorm` in two passes with targets `I=-18 LUFS`, `TP=-2 dBTP`, `LRA=11`, and `linear=true`.

5. Pass one measured `input_i=-13.86 LUFS`, `input_tp=+0.19 dBTP`, `input_lra=11.00 LU`, `input_thresh=-24.25 LUFS`, and `target_offset=+0.51 LU`.

6. Wrote the game-ready archival derivative as PCM signed 24-bit, 44.1 kHz, stereo WAV and embedded title, composer, artist, source, license, and edit metadata.

7. Encoded the delivery candidate as Ogg Vorbis quality 6 at 44.1 kHz stereo and carried the same provenance metadata into the Ogg comments.

8. FFprobe confirms both candidates decode to exactly `110.000000 s` at 44.1 kHz stereo; the WAV reports 24-bit PCM.

9. FFmpeg EBU R128 measurement of the final Ogg decode reports `-18.1 LUFS`, `-3.9 dBFS` true peak, and `11.2 LU` loudness range.

No DDS step applies to audio.

## Fit and audition gate

This is the strongest newly verified recording candidate for preserving the accepted Clarke work and the audience-facing *A Trumpet Voluntary* identity while avoiding the blocked London recording.

Its ceremonial composition and 110-second edit fit the league's formal proclamation, arbitration, and mutual-covenant reveal.

The recording is a 2023 self-release rather than a period recording, and the source page does not identify the instrument or ensemble.

Human audition is therefore required before selection to confirm that its timbre reads as a ceremonial league proclamation rather than a private keyboard or synthetic rendering.

The earlier *The Enola Foam March* and *Toujours en Tête* files remain research-only alternatives and were not replaced, selected, or wired by this handoff.

## Parent integration boundary

If the parent/user explicitly selects this candidate, copy the WAV derivative to the reserved runtime path `sound/006_independence_wave/super_event_23_league_of_new_states.wav` or the final parent-approved equivalent, then create the parent-owned base sound and settings-aware wrappers for audio ID `23`.

The parent must also add the attribution text above to the project audio provenance and update the parent-owned catalogue/registry surfaces.

Until that explicit selection and audition occur, do not add a sound definition, wrapper, catalogue row, dispatcher assignment, or firing path for ID `23`.

## Remaining blockers

- The accepted London Brass Players recording is still blocked for United States/worldwide redistribution; this candidate does not cure that accepted-selection blocker without explicit approval.
- This is a replacement recording, so the accepted specification's user-selection gate remains open.
- Human audition of the final candidate is still open because the source page does not state instrumentation and this worker cannot claim tonal fit from metadata alone.
- CC BY-SA 4.0 attribution and ShareAlike obligations must remain attached to any promoted derivative.
- The uploader's absent Commons profile leaves a residual identity-confidence caveat; obtain a direct rights confirmation if project policy requires stronger evidence than the file's self-release declaration.

No gameplay, sound definition, super-event, localisation, GUI, catalogue, or registry file was edited.
