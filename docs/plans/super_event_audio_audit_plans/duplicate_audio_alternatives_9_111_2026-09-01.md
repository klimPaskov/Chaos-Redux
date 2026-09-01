# Supplemental audio handoff: playback 9 and playback 111

Date: 2026-09-01. Scope: source-rights and suitability comparison only. This note does not change sound definitions, runtime WAVs, catalogue entries, or event files.

## Decision summary

| Playback | Role | Recommendation | Exact staged master | Confidence and remaining gate |
|---|---|---|---|---|
| 9 | The Final Silence | **ACCEPT first-pass Lingyin Temple chant as primary.** Reject Shika no Tōne as the primary despite its excellent shakuhachi fit because its PDM/PD-Japan-audio basis is not an explicit worldwide CC0/CC BY/CC BY-SA grant. | `docs/assets/003_holy_realm/source_audio/duplicate_audio_replacements_2026-09-01/derived_staging/super_event_9_final_silence_thermonuclear.wav` | High suitability and safer redistribution basis under uploader-owned CC BY-SA 3.0; preserve attribution and ShareAlike. The parent audit still owns the required final corpus fingerprint gate. |
| 111 | The Hidden Hand Becomes a State | **ACCEPT Rachmaninoff, Piano Concerto No. 2 in C minor, Op. 18, I. Moderato, Musopen performance.** Rights, identity, and role suitability are independently confirmed. | `docs/assets/039_murder_mystery/source_audio/duplicate_audio_replacements_2026-09-01/derived_staging/super_event_111_assassin_state_reveal.wav` | High confidence. The measured piano control and accumulating orchestral pressure suit a clandestine movement becoming a disciplined territorial state and then open war. The parent audit still owns the required final corpus fingerprint gate. |

No new download, conversion, or fingerprint pass was performed in this supplemental handoff, per the parent instruction to conclude from the preserved first-pass package. The first-pass staged masters above are the exact files to retain; no runtime wiring is made here.

## Playback 9 candidates

### Primary: Chanting at Lingyin Temple, Hangzhou

- Source page: [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Chanting_at_Lingyin_Temple,_Hangzhou.ogg); preserved page evidence: `docs/assets/003_holy_realm/source_audio/duplicate_audio_replacements_2026-09-01/evidence/09_chanting_lingyin_temple_hangzhou_commons_page.html`.
- Preserved source: `docs/assets/003_holy_realm/source_audio/duplicate_audio_replacements_2026-09-01/source/chanting_lingyin_temple_hangzhou.ogg`.
- Creator/recording: uploader LouiseBrown1981, temple chant recorded at Lingyin Temple, Hangzhou.
- Rights: uploader-owned CC BY-SA 3.0 as recorded in the first-pass evidence; attribution and ShareAlike are required. The devotional chant is culturally grounded and does not identify a modern copyrighted score; retain the archived page and do not remove the attribution trail.
- Source profile and checksum: Vorbis, 44.1 kHz, mono, 63.246803 s, SHA-256 `C026AD65E0D306B8A0D88A7CEDD2B2AA0BBFDE672958889BBD891A222121E9BE`.
- Staged profile and checksum: 44.1 kHz stereo signed PCM16 WAV, 63.188005 s, SHA-256 `26BAA65E2095BC3A96DE73CF7B3B406AC42730FF5E06B9CC52CE7C7222A19DD7`.
- Measured staged loudness: mean `-21.9 dB`, peak `-7.3 dB`; no clipping observed.
- First-pass edit summary: a structured near-complete excerpt was rendered to stereo PCM16/44.1 kHz with clean fades and no looping or synthetic material. The first-pass conversion is preserved and was not rerun here.
- Suggested sound id: `chaosx_super_event_final_silence_terminal_track`.
- Suitability: the human devotional cadence and temple acoustics let the cue move from the last command into cessation and stillness, while remaining distinct from the Heart Sutra recording used by playback 8.
- Suggested attribution/change notice: `Chanting at Lingyin Temple, Hangzhou`, uploader LouiseBrown1981, Wikimedia Commons, CC BY-SA 3.0; edited to a short stereo excerpt with fades.

### Rejected cultural alternate: Shika no Tōne

- Source page: [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Shikanotoone.ogg); frozen revision [oldid 1156564930](https://commons.wikimedia.org/w/index.php?title=File:Shikanotoone.ogg&oldid=1156564930); direct source [Shikanotoone.ogg](https://upload.wikimedia.org/wikipedia/commons/3/3e/Shikanotoone.ogg).
- Preserved source: `docs/assets/003_holy_realm/source_audio/alternatives_9_111/source/shikanotoone.ogg`.
- Preserved page evidence: `docs/assets/003_holy_realm/source_audio/alternatives_9_111/evidence/shikanotoone_commons_page.html`.
- Identity: *Shika no Tōne*, a Kinko-ryū honkyoku shakuhachi performance attributed to Araki Kodō III (1879–1935), issued as Victor 13029; source page identifies a 6:15 recording.
- Rights: Commons marks the composition and original recording as public domain under PDM/PD-Japan-audio, but the same page warns that the underlying work may remain protected in Japan and does not provide the explicit worldwide CC0/CC BY/CC BY-SA recording grant required for this package.
- Source profile and checksum: Vorbis, 44.1 kHz, stereo, 375.089138 s, SHA-256 `42C83D3612F44C0A8CDA29E60444030CB92FD50B7BFB4B6F7F84F7C352A5ED49`.
- Verdict: **BLOCKED as primary on rights confidence**, not on cultural or musical suitability. It is a strong fallback only if a rights specialist separately clears worldwide redistribution and the composition-status warning.

### Secondary rights alternate: Buddhist prayer in Nepal

- Source page: [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Buddhist_prayer_in_Nepal.ogg); frozen revision [oldid 1180920643](https://commons.wikimedia.org/w/index.php?title=File:Buddhist_prayer_in_Nepal.ogg&oldid=1180920643); direct source [Buddhist_prayer_in_Nepal.ogg](https://upload.wikimedia.org/wikipedia/commons/d/d1/Buddhist_prayer_in_Nepal.ogg).
- Preserved source: `docs/assets/003_holy_realm/source_audio/alternatives_9_111/source/buddhist_prayer_in_nepal.ogg`.
- Preserved page evidence: `docs/assets/003_holy_realm/source_audio/alternatives_9_111/evidence/buddhist_prayer_in_nepal_commons_page.html`.
- Identity: Davide Mauro field recording of a Buddhist prayer in a temple in Pokhara, Nepal, recorded 2015-04-20; 146.449683 s, Vorbis 44.1 kHz stereo, SHA-256 `6A8E86FA1C21CE9C90AE2819222ED51811F7A1F31640B87E1E6C405948D7BAF2`.
- Rights: CC BY-SA 4.0 International for the recording, requiring Davide Mauro attribution and ShareAlike. The prayer tradition and exact composition are unnamed, so composition identity and structured musical pacing are less defensible than Lingyin.
- Verdict: defensible recording-rights alternate, but **not selected** because the unnamed composition and field-recording structure leave greater identity/suitability uncertainty.

## Playback 111 candidates

### Primary: Rachmaninoff Piano Concerto No. 2, I. Moderato

- Source page: [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Sergei_Rachmaninoff_-_piano_concerto_no._2_in_c_minor,_op._18_-_i._moderato.ogg); frozen revision [oldid 1227006013](https://commons.wikimedia.org/w/index.php?title=File:Sergei_Rachmaninoff_-_piano_concerto_no._2_in_c_minor,_op._18_-_i._moderato.ogg&oldid=1227006013); direct source [Musopen Ogg](https://upload.wikimedia.org/wikipedia/commons/6/63/Sergei_Rachmaninoff_-_piano_concerto_no._2_in_c_minor%2C_op._18_-_i._moderato.ogg).
- Preserved source: `docs/assets/039_murder_mystery/source_audio/duplicate_audio_replacements_2026-09-01/source/rachmaninoff_piano_concerto_2_i_moderato_musopen.ogg`.
- Preserved page evidence: `docs/assets/039_murder_mystery/source_audio/duplicate_audio_replacements_2026-09-01/evidence/111_rachmaninoff_piano_concerto_2_i_moderato_musopen_commons_page.html` and the independent supplemental capture `docs/assets/039_murder_mystery/source_audio/alternatives_9_111/evidence/rachmaninoff_piano_concerto_2_i_moderato_commons_page.html`.
- Identity: Sergei Rachmaninoff (1873–1943), *Piano Concerto No. 2 in C minor, Op. 18*, I. *Moderato*, Musopen performance; source duration 654.408 s, Vorbis stereo 48 kHz, SHA-256 `6DD6E2945F72619FA30FBD328B99FE7D82B239238BCBA8CEF58DC6903F611E2C`.
- Rights: the composition is public domain under the Commons publication analysis, and the Musopen performance is released as public domain worldwide with Commons VRTS confirmation (ticket `#2008012110017088`). Musopen requests courtesy attribution and does not permit direct resale of the recording; those terms do not block redistribution as a mod excerpt. Preserve the source credit and identify the excerpt/edit.
- Staged profile and checksum: 44.1 kHz stereo signed PCM16 WAV, 110.000000 s, SHA-256 `9533170D0E6D051B1FE0070C55F45BEAB278A389620D59784AF48E580982A50C`.
- Measured staged loudness: mean `-20.5 dB`, peak `-1.5 dB`; no clipping observed.
- First-pass edit summary: a 110-second structured excerpt was rendered to 44.1 kHz stereo PCM16 WAV with clean fades and no looping or synthetic material. The first-pass conversion is preserved and was not rerun here.
- Suggested sound id: `chaosx_super_event_assassin_state_reveal_track`.
- Suitability: the restrained solo-piano opening gives the hidden hand procedural intent, while the orchestral expansion supplies disciplined escalation into territorial control and open war without the existing Brahms *Tragic Overture* identity.
- Suggested attribution/change notice: `Sergei Rachmaninoff, Piano Concerto No. 2 in C minor, Op. 18, I. Moderato; Musopen performance, Wikimedia Commons; public-domain recording/composition; edited to a 110-second excerpt with fades.`

### Rejected alternate: Liszt Totentanz

- Source page: [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Liszt_Totentanz.ogg); frozen revision [oldid 773380926](https://commons.wikimedia.org/w/index.php?title=File:Liszt_Totentanz.ogg&oldid=773380926); direct source [Liszt_Totentanz.ogg](https://upload.wikimedia.org/wikipedia/commons/5/59/Liszt_Totentanz.ogg).
- Preserved page evidence: `docs/assets/039_murder_mystery/source_audio/alternatives_9_111/evidence/liszt_totentanz_commons_page.html`; the first-pass source is preserved at `docs/assets/003_holy_realm/source_audio/duplicate_audio_replacements_2026-09-01/source/liszt_totentanz_neal_odoan.ogg`.
- Identity and rights: Franz Liszt, *Totentanz – Paraphrase über Dies irae* (S126), Neal O'Doan piano/orchestra recording; Liszt's composition is public domain and the recording is CC BY-SA 2.0 under the EFF Open Audio License, requiring attribution and ShareAlike.
- Verdict: musically defensible and rights-clear, but **rejected for playback 111** because the same source/recording is selected for playback 12 in this batch. Reusing it would violate the one-track-per-super-event uniqueness rule and make the alternate non-independent.

## Preserved files and risks

- New isolated alternatives: the Shika no Tōne and Buddhist Prayer source/evidence pairs under `docs/assets/003_holy_realm/source_audio/alternatives_9_111/`, plus the Rachmaninoff and Liszt evidence captures under `docs/assets/039_murder_mystery/source_audio/alternatives_9_111/evidence/`.
- Selected first-pass masters remain under their original `duplicate_audio_replacements_2026-09-01/derived_staging/` paths listed above; this note intentionally does not copy, rename, or re-encode them.
- The primary remaining operational gate is the parent-owned decoded-audio fingerprint comparison against every registered `sound/**/*.asset` WAV and against the two selected masters; this supplemental note makes no new fingerprint claim because the parent explicitly stopped further processing.
- ID9 has the lower residual rights risk with Lingyin CC BY-SA 3.0, but attribution/ShareAlike must travel with the mod package and the current Commons license notice should be rechecked before public release.
- ID111 has no identified rights or suitability blocker; retain the Commons VRTS evidence and Musopen courtesy credit, and do not substitute the playback-12 Liszt recording.
