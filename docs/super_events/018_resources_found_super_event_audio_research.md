# Event 018 Resources Found super-event audio research

## Scope and final status

This package supplies three unique, real musical recordings for the accepted Event 018 super-event roles associated with the Oth-Kesh Host (`DHO`):

- visible slot `82`, audio ID `54`: `THE OTH-KESH HOST RISES`
- visible slot `83`, audio ID `55`: `THE DEEP WAR CROSSES THE SEAS`
- visible slot `84`, audio ID `56`: conditional global or near-global defeat, `THE LAST DEPTH IS SEALED`

The source and rights pages were rechecked on 2026-07-12. Composition rights and recording rights were evaluated separately. Exact source downloads and frozen licence evidence are preserved under `docs/assets/018_resources_found/source/audio/`. Final OGG files are unique 60-to-120-second, 44.1 kHz stereo Vorbis cues with matching 44.1 kHz stereo signed 16-bit PCM WAV files.

The duration repair did not change visible slots, audio IDs, helper IDs, sound wrappers, base sound IDs, or runtime filenames. ID `55` was replaced at its stable paths because the former United States Air Force recording had only a U.S.-federal public-domain basis. Its replacement recording is CC0 1.0 and supplies worldwide redistribution and adaptation rights.

## Final identifier disposition

| Role | Visible slot | Audio ID | Final stem | Stable sound-track ID |
| --- | ---: | ---: | --- | --- |
| Oth-Kesh emergence | `82` | `54` | `super_event_54_oth_kesh_emergence` | `chaosx_super_event_resources_found_oth_kesh_emergence_track` |
| Cross-sea world end | `83` | `55` | `super_event_55_deep_war_crosses_seas` | `chaosx_super_event_resources_found_deep_war_crosses_seas_track` |
| Eligible global defeat | `84` | `56` | `super_event_56_last_depth_sealed` | `chaosx_super_event_resources_found_last_depth_sealed_track` |

## Recommendation summary

| Role | Selected recording | Source duration | Retained programme interval | Final duration | Recording-rights basis |
| --- | --- | ---: | ---: | ---: | --- |
| Oth-Kesh emergence | Mussorgsky, *Bydło*; Skidmore College Orchestra | `139.008000 s` | `00:24.000-02:18.750` | `115.000000 s` | Musopen worldwide public-domain release and unconditional grant, confirmed by Wikimedia VRTS |
| Cross-sea world end | Brahms, Symphony No. 1, I. `Un poco sostenuto - Allegro`; Czech National Symphony Orchestra / Musopen Symphony Orchestra | `909.216000 s` | `08:40.000-10:29.750` | `110.000000 s` | CC0 1.0 Universal recording |
| Eligible global defeat | Chopin, Prelude in E minor, Op. 28 No. 4; Ivan Ilić | `109.814422 s` | `00:00.450-01:49.200` | `109.000000 s` | CC BY 3.0 recording |

Each programme interval is followed by a `0.250 s` zeroed tail included in the final duration. All three selections are structured performances by identified musicians. None is a generated cue, MIDI render, synthesized mockup, drone, oscillator, test tone, sound-effect bed, modern commercial recording, or YouTube-only source.

## 1. Audio ID 54 - THE OTH-KESH HOST RISES

### Source identity

- **Work:** `IV. Bydło - Sempre moderato, pesante`, from *Pictures at an Exhibition*
- **Composer:** Modest Mussorgsky (1839-1881)
- **Performer:** Skidmore College Orchestra
- **Exact performance date:** not stated by the rights-confirmed source
- **Canonical selected-source and rights page:** [Wikimedia Commons, Musopen/VRTS copy](https://commons.wikimedia.org/wiki/File:Modest_Mussorgsky_-_pictures_at_an_exhibition_-_iv._bydlo_-_sempre_moderato%2C_pesante.ogg)
- **Performer-identification copy:** [Wikimedia Commons, Skidmore College Orchestra/FMA copy](https://commons.wikimedia.org/wiki/File:Skidmore_College_Orchestra_-_07_-_IV_Bydlo_Sempre_moderato_pesante.ogg)
- **Public Domain Mark:** <https://creativecommons.org/publicdomain/mark/1.0/>
- **Musopen VRTS permission record:** Wikimedia VRTS ticket `2008012110017088`, linked on the selected source page
- **Preserved source:** `docs/assets/018_resources_found/source/audio/mussorgsky_bydlo_musopen_vrts_original.ogg`
- **Original technical profile:** Vorbis, 48,000 Hz, stereo, `139.008000 s`, `2,771,284` bytes
- **Source SHA-256:** `87da8f6bc6a03900ce0eac2879e7b027de707d1173c1cadc82db1caa081a88d4`

### Performer-identity verification

The selected 2008 Commons page gives the work and Musopen rights record but directs readers to Musopen for performer information. A later Commons import identifies the same recording as Skidmore College Orchestra. The later copy adds `1.258685 s` of leading silence and uses a 44.1 kHz transcode. After removing that silence and matching sample rates, FFmpeg `apsnr` comparison over 136 seconds measured `173.133 dB` on the left channel and `172.588 dB` on the right. This is effectively identical programme audio, so the performer credit is supported by audio identity rather than title similarity.

### Rights verification

- **Composition:** public domain. Mussorgsky died in 1881; *Pictures at an Exhibition* dates to 1874.
- **Recording:** the selected Commons page records that Musopen released the recording into the public domain worldwide and, where waiver is not legally possible, grants anyone the right to use it for any purpose without conditions. Wikimedia records VRTS confirmation of the rights-holder communication.
- **Attribution requirement:** none imposed by the stated grant. Courtesy credit is retained.
- **Confidence:** high.
- **Uncertainty retained:** the exact performance date is not established and is not represented as known.

### Editorial fit and processing

The earlier 34-second cadence was too short for the source brief. The final 115-second edit begins in the deliberate tread, carries the movement's sustained growth into its heaviest mass, and follows the energy back toward the natural ending. It presents an organized polity arriving in force rather than a brief monster-attack sting.

- Retained source `00:24.000-02:18.750` (`24.000-138.750 s`; `114.750 s` of programme).
- Applied a `1.500 s` quarter-sine fade-in.
- Applied a `5.000 s` quarter-sine fade-out from final-cue time `109.750 s` through `114.750 s`.
- Added `0.250 s` of digital zero after the fade for replay and accidental-loop safety.
- Applied fixed `-2.6 dB` gain; no dynamic compression or limiting.
- Resampled 48 kHz to 44.1 kHz with SoXr precision 28.
- Exported PCM s16le WAV, then encoded the matching OGG at Vorbis quality 6.
- Final OGG: `music/018_resources_found/super_event_54_oth_kesh_emergence.ogg`
- Final WAV: `sound/018_resources_found/super_event_54_oth_kesh_emergence.wav`

### Courtesy attribution

> Modest Mussorgsky, *Pictures at an Exhibition* - `IV. Bydło (Sempre moderato, pesante)`; performed by Skidmore College Orchestra; recording released by Musopen into the public domain worldwide, with unconditional use granted where waiver is unavailable; source and VRTS permission record via Wikimedia Commons. Chaos Redux excerpted `00:24.000-02:18.750`, applied quarter-sine fades, fixed gain, a zeroed tail, resampled to 44.1 kHz, and encoded OGG/WAV derivatives.

## 2. Audio ID 55 - THE DEEP WAR CROSSES THE SEAS

### Source identity

- **Work:** Symphony No. 1 in C minor, Op. 68, I. `Un poco sostenuto - Allegro`
- **Composer:** Johannes Brahms (1833-1897)
- **Performer:** Czech National Symphony Orchestra; published by the source as Musopen Symphony Orchestra
- **Source page author field:** Musopen Symphony Orchestra
- **Embedded artist metadata:** Czech National Symphony Orchestra
- **Canonical source and file-specific licence page:** [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Brahms,_Symphony_No._1_in_C_Minor,_Op._68_-_I._Un_poco_sostenuto_-_Allegro.ogg)
- **Direct original file:** <https://upload.wikimedia.org/wikipedia/commons/a/a7/Brahms%2C_Symphony_No._1_in_C_Minor%2C_Op._68_-_I._Un_poco_sostenuto_-_Allegro.ogg>
- **CC0 deed:** <https://creativecommons.org/publicdomain/zero/1.0/>
- **CC0 legal code:** <https://creativecommons.org/publicdomain/zero/1.0/legalcode>
- **Preserved source:** `docs/assets/018_resources_found/source/audio/brahms_symphony_1_i_musopen_cc0_original.ogg`
- **Original technical profile:** Vorbis, 48,000 Hz, stereo, `909.216000 s`, `20,432,979` bytes
- **Source SHA-1:** `6ad72b00ca5032cbe5aa06aea80c70c82533bb90`, matching the Commons structured checksum
- **Source SHA-256:** `f86f1df2f97b79c9bc92dac63b0da1bf868675005af4fe9c05ab886291af9b95`

### Rights verification

- **Composition:** public domain. Brahms died in 1897; the symphony was completed and premiered in 1876.
- **Recording:** the Commons file page applies Creative Commons CC0 1.0 Universal to the recording.
- **Worldwide grant:** CC0 waives copyright and related or neighbouring rights worldwide to the extent allowed by law and permits copying, modification, distribution, and performance for any purpose, including commercial use.
- **Attribution requirement:** none under CC0. Courtesy credit is retained to preserve identity and provenance.
- **Confidence:** high. The preserved file's SHA-1 exactly matches the source page, and the file-specific licensing block and structured licence data both identify CC0.
- **Identity note:** `Czech National Symphony Orchestra / Musopen Symphony Orchestra` is used because the file's embedded artist metadata and the Commons author field use those two names for the same recording. This does not affect the file-specific CC0 grant.

### Editorial fit and processing

The retained passage begins with a quieter repeated figure, grows in weight and range, and reaches a broad full-orchestra statement. Its internal crescendo maps directly to the campaign transition from distant resource-centre ruptures to an organized global advance. The ending is faded from the ensemble peak to make a deliberate terminal cutoff, not an arbitrary splice.

- Retained source `08:40.000-10:29.750` (`520.000-629.750 s`; `109.750 s` of programme).
- Applied a `1.500 s` quarter-sine fade-in.
- Applied a `6.000 s` quarter-sine fade-out from final-cue time `103.750 s` through `109.750 s`.
- Added `0.250 s` of digital zero after the fade for replay and accidental-loop safety.
- Preserved source level and dynamics; no gain change, compression, or limiting.
- Resampled 48 kHz to 44.1 kHz with SoXr precision 28.
- Exported PCM s16le WAV, then encoded the matching OGG at Vorbis quality 6.
- Final OGG: `music/018_resources_found/super_event_55_deep_war_crosses_seas.ogg`
- Final WAV: `sound/018_resources_found/super_event_55_deep_war_crosses_seas.wav`

### Courtesy attribution

> Johannes Brahms, Symphony No. 1 in C minor, Op. 68 - I. `Un poco sostenuto - Allegro`; performed by the Czech National Symphony Orchestra and published as the Musopen Symphony Orchestra recording; source via Wikimedia Commons. Recording dedicated under CC0 1.0 Universal: https://creativecommons.org/publicdomain/zero/1.0/. Chaos Redux excerpted `08:40.000-10:29.750`, applied quarter-sine fades and a zeroed tail, resampled to 44.1 kHz, and encoded OGG/WAV derivatives. No endorsement is implied.

### Superseded Debussy candidate

The former ID `55` candidate was Claude Debussy's *La mer*, III. `Dialogue du vent et de la mer`, arranged by Lawrence Odom and performed by the United States Air Force Band. Its official U.S.-federal public-domain basis was well documented but did not provide the clean worldwide grant required for a distributable mod. The source remains preserved at `docs/assets/018_resources_found/source/audio/debussy_la_mer_iii_usaf_original.mp3` for audit history, but no final file, localisation string, catalogue row, or runtime definition identifies or uses it.

## 3. Audio ID 56 - THE LAST DEPTH IS SEALED

### Source identity

- **Work:** Prelude in E minor (Largo), Op. 28 No. 4
- **Composer:** Frédéric Chopin (1810-1849)
- **Performer:** Ivan Ilić, piano
- **Performance date and place:** Paris, October 2005
- **Canonical source and rights page:** [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Ivan_Ili%C4%87-Chopin_Prelude_Opus_28_n.4.ogg)
- **Original upstream note:** initially uploaded by Ivan Ilić to his IMSLP user page
- **Recording licence:** [Creative Commons Attribution 3.0 Unported](https://creativecommons.org/licenses/by/3.0/)
- **Preserved source:** `docs/assets/018_resources_found/source/audio/chopin_prelude_op28_no4_ivan_ilic_original.ogg`
- **Original technical profile:** Vorbis, 44,100 Hz, stereo, `109.814422 s`, `1,371,608` bytes
- **Source SHA-256:** `c64c302948b73e251478b4e4a9e44d0e92ceec2e34f95e02d6c1130420dcd7cf`

### Rights verification

- **Composition:** public domain. Chopin died in 1849 and composed the prelude in 1838-1839.
- **Recording:** the Commons licensing block, structured copyright data, and licence category identify CC BY 3.0.
- **Worldwide use:** CC BY 3.0 permits sharing and adaptation in any medium for any purpose when its conditions are met.
- **Attribution:** mandatory. Credit the composer and performer, link the source and CC BY 3.0, state the changes, impose no incompatible restrictions, and avoid implied endorsement.
- **Confidence:** high.
- **Metadata note:** one ancillary metadata line on Commons links to a BY-SA URL, but the actual licensing block, structured licence field, and category consistently specify CC BY 3.0; this package follows the explicit file-page licence.

### Editorial fit and processing

Using nearly the complete performance restores the intended reflective arc: sustained tension, a withdrawal into exposed rests, and separated closing chords. The cue records burial, survival, and reconstruction rather than a triumphant victory.

- Retained source `00:00.450-01:49.200` (`0.450-109.200 s`; `108.750 s` of programme).
- Applied a `1.250 s` quarter-sine fade-in.
- Applied a `5.000 s` quarter-sine fade-out from final-cue time `103.750 s` through `108.750 s`.
- Added `0.250 s` of digital zero after the fade for replay and accidental-loop safety.
- Applied fixed `+6.5 dB` gain; no dynamic compression or limiting.
- Retained the source 44.1 kHz rate.
- Exported PCM s16le WAV, then encoded the matching OGG at Vorbis quality 6.
- Final OGG: `music/018_resources_found/super_event_56_last_depth_sealed.ogg`
- Final WAV: `sound/018_resources_found/super_event_56_last_depth_sealed.wav`

### Required attribution and change notice

> Frédéric Chopin, Prelude in E minor (Largo), Op. 28 No. 4; performed by Ivan Ilić, Paris, October 2005; source via Wikimedia Commons / IMSLP. Recording licensed CC BY 3.0: https://creativecommons.org/licenses/by/3.0/. Chaos Redux excerpted `00:00.450-01:49.200`, applied quarter-sine fades, fixed gain, and a zeroed tail, and encoded OGG/WAV derivatives. No endorsement by Ivan Ilić is implied.

## Technical verification

All final files decode successfully, report two channels at exactly 44,100 Hz, and fall within 60 to 120 seconds. OGG outputs are Vorbis; WAV outputs are signed 16-bit little-endian PCM. Loudness and true-peak values below were measured after delivery encoding with FFmpeg's EBU R128 / `loudnorm` analyser.

| Audio ID | File type | Duration | Codec | Integrated loudness | True peak | LRA | SHA-256 |
| ---: | --- | ---: | --- | ---: | ---: | ---: | --- |
| `54` | OGG | `115.000000 s` | Vorbis | `-19.21 LUFS` | `-2.05 dBTP` | `19.50 LU` | `88d3b749fd51bcc106daf352ae9791c51d3452e7bce9a01ebf8971dad57385c0` |
| `54` | WAV | `115.000000 s` | PCM s16le | `-19.20 LUFS` | `-2.15 dBTP` | `19.50 LU` | `daf27599720d281eaa96fe828dc38337553026054b634a57d652a41236050575` |
| `55` | OGG | `110.000000 s` | Vorbis | `-18.47 LUFS` | `-2.27 dBTP` | `18.50 LU` | `b6888c95658dafbf40dd822550d05c505e9a653ce4daa01191e00a6500c28215` |
| `55` | WAV | `110.000000 s` | PCM s16le | `-18.44 LUFS` | `-2.26 dBTP` | `18.60 LU` | `f0ee745abfbe432cd26b37ad14fb800ab4bcbf77e442eb11d06f8f8f991e1266` |
| `56` | OGG | `109.000000 s` | Vorbis | `-21.86 LUFS` | `-2.32 dBTP` | `14.20 LU` | `b1131b009a715c20598bf720d485c05038d583accbc1e46744dbc182d1f7631e` |
| `56` | WAV | `109.000000 s` | PCM s16le | `-21.88 LUFS` | `-2.27 dBTP` | `14.20 LU` | `9be248a28861b96a8c454ab729af8d710727c2b3289eb4820efa98b1cba8fcc9` |

The intentionally lower integrated level on ID `56` preserves the piano's complete rise, rests, and decay while keeping the true peak below `-2 dBTP`; forcing it to `-18 LUFS` would require compression or limiting. No such dynamic flattening was introduced.

### Preserved-source hashes

| Source path | Bytes | SHA-1 | SHA-256 | Disposition |
| --- | ---: | --- | --- | --- |
| `docs/assets/018_resources_found/source/audio/mussorgsky_bydlo_musopen_vrts_original.ogg` | `2,771,284` | `d445e58a5e251e6e5b53550875967cda770b3bcd` | `87da8f6bc6a03900ce0eac2879e7b027de707d1173c1cadc82db1caa081a88d4` | Active ID `54` master |
| `docs/assets/018_resources_found/source/audio/brahms_symphony_1_i_musopen_cc0_original.ogg` | `20,432,979` | `6ad72b00ca5032cbe5aa06aea80c70c82533bb90` | `f86f1df2f97b79c9bc92dac63b0da1bf868675005af4fe9c05ab886291af9b95` | Active ID `55` master |
| `docs/assets/018_resources_found/source/audio/chopin_prelude_op28_no4_ivan_ilic_original.ogg` | `1,371,608` | `c4ae6453ba25612c130e6d332bb210bec1aafb6c` | `c64c302948b73e251478b4e4a9e44d0e92ceec2e34f95e02d6c1130420dcd7cf` | Active ID `56` master |
| `docs/assets/018_resources_found/source/audio/debussy_la_mer_iii_usaf_original.mp3` | `20,145,174` | `f9a3972c623beae59a6aab9bf0a8430adcacdb5f` | `65c3e891cde5a486742681bb5490309393cc33546d5b129878fa7a50a2fa139b` | Superseded ID `55` research source; not wired |

### Decoded-audio uniqueness hashes

The three final OGGs were decoded through FFmpeg to 44.1 kHz stereo PCM s16le and hashed independently of their Vorbis container bytes.

| Audio ID | Decoded PCM SHA-256 |
| ---: | --- |
| `54` | `4ab371aa335a3689413a71739284e0041b8d49f366bca0a32ea594e126eb31b1` |
| `55` | `17d07bdeae93b40ecd5a5b3276943149de05b2eca187aef8bea981ecbd002eaa` |
| `56` | `40dd0c8bed140da0f2039c3a631c89b50b1e3ddae52c01d058fb3bd30951bd7b` |

The three file hashes and decoded PCM hashes are mutually unique. Repository title/source searches found no other use of the selected Brahms movement. The final repository-wide OGG file-hash scan found no duplicate of any Event 018 delivery file.

## Licence-evidence archive

Frozen source-page, deed, and legal-code snapshots, with their own SHA-256 values, are indexed in:

`docs/assets/018_resources_found/source/audio/license_evidence/README.md`

This archive contains the VRTS-confirmed ID `54` rights page and performer page, the ID `55` Commons file page plus CC0 deed and legal code, and the ID `56` Commons file page plus CC BY 3.0 deed and legal code.

## Candidate disposition and uniqueness decisions

- ID `54` retained the VRTS-confirmed Musopen *Bydło* recording because its grant is worldwide and its long crescendo/withdrawal arc directly supports emergence.
- ID `55` rejected the former United States Air Force *La mer* source because its affirmative recording-rights basis was limited to U.S. federal law rather than a worldwide waiver or licence.
- Beethoven's *Egmont Overture* CC0 recording was rejected because the same programme recording is already assigned elsewhere in the repository.
- Holst's *Mars, the Bringer of War* was rejected because it is already assigned to Fury audio ID `30`.
- Brahms's Fourth Symphony finale remained rejected because earlier research found conflicting performer metadata; the selected Brahms First Symphony file instead has a file-specific CC0 grant and an exact source checksum.
- ID `56` retained Ivan Ilić's Chopin recording because CC BY 3.0 supplies worldwide sharing/adaptation rights and the full performance fits the aftermath role when complete attribution and change notice are carried forward.
- Event 014's Saint-Saëns, Wagner, Grieg, and Fauré selections were not reused.
- YouTube-only, provenance-unclear, modern commercial, generated, MIDI-rendered, and transform-only candidates were rejected by the brief.

## Runtime and downstream wiring verification

Stable integration remains:

- `music/chaosx_super_event_music.asset`: six helper variants for each audio ID point to the unchanged Event 018 OGG filenames.
- `music/chaosx_super_event_music.txt`: one zero-chance representative helper remains registered for each cue.
- `sound/chaosx_sound.asset`: stable base sounds and six wrapper variants for each audio ID point to the unchanged Event 018 WAV filenames.
- `localisation/english/chaosx_music_l_english.yml`: ID `55` helper labels identify the Brahms replacement.
- `music/chaosx_music_track_list.html`: the three rows identify the active sources, rights, and `01:55` / `01:50` / `01:49` durations.
- `docs/super_events/super_event_audio_packages.md`: the Event 018 package carries the final sources, edits, and required CC BY attribution.

The exact visible/audio pairs remain:

- `82` / `54`: `THE OTH-KESH HOST RISES`
- `83` / `55`: `THE DEEP WAR CROSSES THE SEAS`
- `84` / `56`: conditional `THE LAST DEPTH IS SEALED`

## Blockers, simplifications, and unresolved rights risk

There are no audio-production blockers, fallbacks, placeholders, generated cues, reused final tracks, or unresolved distribution-rights caveats. IDs `54` and `55` have worldwide public-domain/CC0 grants. ID `56` is globally redistributable under CC BY 3.0 when its attribution, source and licence links, change notice, no-additional-restrictions rule, and no-endorsement treatment are retained; those terms are fully recorded in every active attribution surface.
