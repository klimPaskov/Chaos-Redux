# Event 006 super-event 6001 audio rights decision

> Superseded identifier note (2026-08-06): live Event 006 uses ordinary super-event ID 23 for League of New States and ID 24 for Every Border a Casus Belli. Any legacy 6001/6002 labels below are historical audit references only.

Research date: 2026-08-02.

Scope: bounded audio-rights research for Event 006 super-event `6001`, The League of New States. No sound definition, event, localisation, `.gfx`, GUI, or spreadsheet file was edited. No replacement was wired.

## Decision

The accepted `6001` selection remains blocked and has no implementation-safe audio path. The accepted recording is Jeremiah Clarke's *A Trumpet Voluntary* performed by the London Brass Players with Harry Mortimer (trumpet), Reginald Foort (organ), and George Weldon (conductor), recorded 8 November 1948 and first released in 1949. Its Commons page identifies a Swiss Public Domain Project/CC-ZERO-PROJECT source, but it does not provide a United States public-domain tag, CC0 dedication, or rights-holder permission for this exact pre-1972 recording. The United States recording-rights term therefore remains a material blocker under the approved brief.

The strongest same-composition alternative is legally redistributable but is not approved for this super-event: Fehufanga's 2022 own harpsichord recording is clearly marked CC BY-SA 3.0, but it replaces the accepted brass-and-organ ceremonial timbre and requires attribution, change notice, and ShareAlike treatment. The Event 006 brief explicitly requires parent/user approval before reopening the accepted selection, so this candidate is evidence only and must not be wired or represented as final.

## Accepted recording (still blocked)

- Track: *A Trumpet Voluntary* (also known as *The Prince of Denmark's March*).
- Composer: Jeremiah Clarke (1674-1707; historically misattributed to Henry Purcell).
- Performer/recording source: London Brass Players; Harry Mortimer, trumpet; Reginald Foort, organ; George Weldon, conductor.
- Recording facts: 8 November 1948, EMI Studio No. 1, Abbey Road, London; first release 1949, Columbia DX 1536, matrix CAX 10357.
- Source page: <https://commons.wikimedia.org/wiki/File:CC0-CH_-_London_Brass_Players_-_A_Trumpet_Voluntary_-_Jeremiah_Clarke_-_Columbia-dx1536-cax10357.flac>.
- Direct original: <https://upload.wikimedia.org/wikipedia/commons/7/75/CC0-CH_-_London_Brass_Players_-_A_Trumpet_Voluntary_-_Jeremiah_Clarke_-_Columbia-dx1536-cax10357.flac>.
- Commons duration: `167.5730416667 s`; Commons SHA-1: `6320e3d289d959acf0a871d1bea3cfa7b3d3b7fa`.
- Rights verdict: composition public domain; recording not cleared for United States redistribution. The Commons page's `CC-PD-Mark`/Public Domain Project context is not a United States recording-right waiver, and the page itself requires a United States public-domain basis.
- Held editorial plan: excerpt `00:23.000-02:13.000` (110 seconds), fade-in `1.5 s`, fade-out `2.0 s` beginning at excerpt second `108.0`, one-shot playback.
- Reserved future runtime path: `sound/006_independence_wave/super_event_006_01_league_of_new_states.wav`.
- Reserved future audio ID: `6001`.
- No source was downloaded, analyzed, converted, or assigned a sound ID for this recording.

## Legally usable candidate, not approved for 6001

- Track: *Jeremiah Clarke - Prince of Denmarks March Harpsichord*.
- Composer: Jeremiah Clarke; recording by Fehufanga, own work, played on a Silbermann harpsichord sample set using GrandOrgue.
- Source page: <https://commons.wikimedia.org/wiki/File:Jeremiah_Clarke_-_Prince_of_Denmarks_March_Harpsichord.wav>.
- Direct original: <https://upload.wikimedia.org/wikipedia/commons/b/bd/Jeremiah_Clarke_-_Prince_of_Denmarks_March_Harpsichord.wav>.
- License: <https://creativecommons.org/licenses/by-sa/3.0/> (CC BY-SA 3.0); the source page states own work and names Fehufanga.
- License confidence: high for the recording license and uploader provenance; medium for downstream mod packaging because any adapted derivative must retain attribution, identify changes, and satisfy ShareAlike.
- Source date and duration: 17 August 2022; `108.135329 s`.
- Downloaded source path (research evidence only): `docs/assets/006_independence_wave/super_events/audio/source/Jeremiah_Clarke_-_Prince_of_Denmarks_March_Harpsichord.wav`.
- Downloaded source bytes: `38,150,188`.
- Downloaded source SHA-256: `8C35F2ED5405AAA2DB02A93017759CD4AD290017ED37B7DD134FF4390F910F22`.
- Downloaded source SHA-1: `62DCF8C444D8DFF8C71BFB77033773CB7C5C29F4`.
- Source technical profile: RIFF/WAV, PCM float little-endian (`pcm_f32le`), 44.1 kHz, 2 channels, `108.135329 s`; the source reports an unknown channel-layout label but decodes as stereo.
- Measured loudness profile: `-32.54 LUFS` integrated, `-16.33 dBTP` true peak, `4.50 LU` LRA, `-42.75 LUFS` threshold.
- Suitability: legally usable with attribution and ShareAlike, but not implementation-safe for the approved `6001` package because the recording is harpsichord-only and does not preserve the accepted brass-and-organ ceremonial character. Selection change requires explicit parent/user approval.
- Attribution if later approved: `Jeremiah Clarke - Prince of Denmark's March, performed/recorded by Fehufanga, Wikimedia Commons, CC BY-SA 3.0; adapted by Chaos Redux with trim/fades/loudness normalization.` Include the license URL and a change notice.

## Other same-composition findings

- `Marcha del príncipe de Dinamarca, Jeremiah Clarke.ogg`: <https://commons.wikimedia.org/wiki/File:Marcha_del_pr%C3%ADncipe_de_Dinamarca,_Jeremiah_Clarke.ogg>. Commons marks the file `PD-US`, but the page describes a Hauptwerk recording without naming a recording performer and credits only Jeremiah Clarke; `74.280 s` is also materially shorter than the held 110-second cue. The recording-right basis is therefore not sufficiently documented for implementation despite the template.
- `Clarke Trumpet Voluntary.ogg`: <https://commons.wikimedia.org/wiki/File:Clarke_Trumpet_Voluntary.ogg>. Orgelputzer's own recording is marked CC BY-SA 4.0, `133.903673 s`, but the page does not identify the instrument and the take is not the accepted brass-and-organ sound. Any adapted derivative would require attribution, change notice, and ShareAlike.
- Period recordings found on Internet Archive were rejected when item metadata supplied no usable license or rights statement, regardless of composition age or tonal similarity.

## Conversion requirements if a replacement is explicitly approved

Do not run this conversion unless the parent/user approves replacing the accepted brass-and-organ recording with the Fehufanga take or another cleared source.

1. Preserve the downloaded original and its SHA-256 before editing.
2. Trim the candidate to a maximum of 110 seconds; for the 108.135329-second source, retain the complete take or trim only its ending after approval.
3. Apply a `1.5 s` fade-in and `2.0 s` fade-out, preserving musical phrasing and avoiding a hard cut.
4. Loudness-normalize conservatively to approximately `-18 LUFS`, retaining the source's low `4.50 LU` dynamics; the measured two-pass `loudnorm` pass reaches `-18.05 LUFS` and `-1.80 dBTP`.
5. Deliver a 44.1 kHz stereo PCM S16LE WAV for the HOI4 runtime pipeline and, if requested by the parent workflow, a quality-preserving Ogg Vorbis derivative. The WAV/OGG derivatives must carry the CC BY-SA 3.0 attribution and change notice.
6. Store a future final WAV at `sound/006_independence_wave/super_event_006_01_league_of_new_states.wav`; do not create that runtime file until approval.

## Future wiring handoff (only after clearance and approval)

- Keep reserved super-event display slot `23` and audio ID `6001`.
- Register one unique raw sound name, preferably `chaosx_super_event_6001_track`, pointing to the approved final WAV.
- Register six settings wrappers named `chaosx_super_event_6001_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, and `_3_0`, following the existing `max_audible = 1` and `max_audible_behaviour = fail` pattern.
- Set `global.current_super_event_audio_id = 6001` only when slot 23 owns the visible window and call the existing settings-aware `play_current_super_event_sound = yes` helper.
- Add a canonical `music/chaosx_music_track_list.html` row naming the actual title, creator/performer, source URL, license, duration, attribution, and Event 006 super-event ID `6001`.
- Keep the accepted London Brass Players provenance and any approved replacement provenance separate; do not describe the candidate as the accepted track.

## Final status

No implementation-safe path exists for 6001 in this pass. The exact accepted recording remains rights-blocked, and the only clearly licensed same-composition candidate changes the approved instrumentation and carries ShareAlike obligations. No fallback, substitute, final `.wav`, final `.ogg`, sound definition, wrapper, runtime ID assignment, or gameplay wiring was created.
