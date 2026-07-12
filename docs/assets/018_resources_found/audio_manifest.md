# Event 018 Resources Found super-event audio manifest

## Package status

Three unique real-recording cues are preserved and converted for the Event 018 Oth-Kesh super-events. The stable pairings remain visible slots `82`-`84` and audio IDs `54`-`56`; no runtime identifier, helper family, wrapper, or filename changed during the duration and rights repair.

The final OGG durations are `115.000000 s`, `110.000000 s`, and `109.000000 s`. Every OGG is Vorbis, 44.1 kHz, stereo, and within the source prompt's 60-to-120-second range. Matching runtime WAV files contain the same edits as 44.1 kHz stereo signed 16-bit PCM.

## Active source manifest

| Audio ID | Role | Preserved source | Original profile | Source SHA-1 | Source SHA-256 |
| ---: | --- | --- | --- | --- | --- |
| `54` | Oth-Kesh emergence | `docs/assets/018_resources_found/source/audio/mussorgsky_bydlo_musopen_vrts_original.ogg` | Vorbis, 48 kHz stereo, `139.008000 s`, `2,771,284` bytes | `d445e58a5e251e6e5b53550875967cda770b3bcd` | `87da8f6bc6a03900ce0eac2879e7b027de707d1173c1cadc82db1caa081a88d4` |
| `55` | Cross-sea world end | `docs/assets/018_resources_found/source/audio/brahms_symphony_1_i_musopen_cc0_original.ogg` | Vorbis, 48 kHz stereo, `909.216000 s`, `20,432,979` bytes | `6ad72b00ca5032cbe5aa06aea80c70c82533bb90` | `f86f1df2f97b79c9bc92dac63b0da1bf868675005af4fe9c05ab886291af9b95` |
| `56` | Eligible global defeat | `docs/assets/018_resources_found/source/audio/chopin_prelude_op28_no4_ivan_ilic_original.ogg` | Vorbis, 44.1 kHz stereo, `109.814422 s`, `1,371,608` bytes | `c4ae6453ba25612c130e6d332bb210bec1aafb6c` | `c64c302948b73e251478b4e4a9e44d0e92ceec2e34f95e02d6c1130420dcd7cf` |

The downloaded ID `55` master exactly matches the Wikimedia Commons structured SHA-1 (`6ad72b00ca5032cbe5aa06aea80c70c82533bb90`). The superseded Debussy master remains preserved at `docs/assets/018_resources_found/source/audio/debussy_la_mer_iii_usaf_original.mp3` with SHA-256 `65c3e891cde5a486742681bb5490309393cc33546d5b129878fa7a50a2fa139b`; it is retained only as rejected research history and has no runtime use.

## Rights and attribution manifest

| Audio ID | Exact source | Creator / performer | Source and rights | Required treatment |
| ---: | --- | --- | --- | --- |
| `54` | Mussorgsky, *Pictures at an Exhibition* - `IV. Bydło` | Modest Mussorgsky; Skidmore College Orchestra | [VRTS-confirmed Commons source](https://commons.wikimedia.org/wiki/File:Modest_Mussorgsky_-_pictures_at_an_exhibition_-_iv._bydlo_-_sempre_moderato%2C_pesante.ogg); public-domain composition; Musopen recording released worldwide into the public domain with an unconditional use grant where waiver is unavailable | No mandatory attribution stated; retain courtesy credit, source, and edit notice. Performer identity is corroborated by the [Skidmore-labelled copy](https://commons.wikimedia.org/wiki/File:Skidmore_College_Orchestra_-_07_-_IV_Bydlo_Sempre_moderato_pesante.ogg). |
| `55` | Brahms, Symphony No. 1 in C minor, Op. 68: I. `Un poco sostenuto - Allegro` | Johannes Brahms; Czech National Symphony Orchestra, published as Musopen Symphony Orchestra | [Commons source and file-specific licence](https://commons.wikimedia.org/wiki/File:Brahms,_Symphony_No._1_in_C_Minor,_Op._68_-_I._Un_poco_sostenuto_-_Allegro.ogg); public-domain composition; recording under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) | No attribution required by CC0; retain courtesy credit, source, CC0 link, and edit notice. CC0 supplies the required worldwide waiver of copyright and related or neighbouring rights. |
| `56` | Chopin, Prelude in E minor, Op. 28 No. 4 | Frédéric Chopin; Ivan Ilić, piano | [Commons source](https://commons.wikimedia.org/wiki/File:Ivan_Ili%C4%87-Chopin_Prelude_Opus_28_n.4.ogg); public-domain composition; recording under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) | Credit Chopin and Ilić, link the source and CC BY 3.0, identify the excerpt/fade/gain/resampling/encoding changes, impose no incompatible restrictions, and avoid implied endorsement. |

Frozen source-page, deed, and legal-code snapshots are indexed in `docs/assets/018_resources_found/source/audio/license_evidence/README.md`.

## Edit manifest

Each edit uses a quarter-sine fade from or to digital zero and ends with a `0.250 s` zeroed tail. The tail makes replay and accidental looping click-safe while preserving one-shot presentation. Fixed gain was used instead of dynamic compression so the musical arcs remain intact.

| Audio ID | Retained programme interval | Fade and zero-tail treatment | Delivery processing | Cue rationale |
| ---: | --- | --- | --- | --- |
| `54` | `00:24.000-02:18.750` (`114.750 s`) | `1.500 s` in; `5.000 s` out from final-cue time `109.750`; `0.250 s` zero tail | Fixed `-2.6 dB` gain; SoXr resample 48 kHz to 44.1 kHz at precision 28; PCM s16le WAV; Vorbis quality-6 OGG from that WAV | The long central-to-closing arc begins in a deliberate tread, grows into the movement's heaviest mass, and recedes into a natural ending: organized emergence rather than a short stinger. |
| `55` | `08:40.000-10:29.750` (`109.750 s`) | `1.500 s` in; `6.000 s` out from final-cue time `103.750`; `0.250 s` zero tail | No gain change or compression; SoXr resample 48 kHz to 44.1 kHz at precision 28; PCM s16le WAV; Vorbis quality-6 OGG from that WAV | A quiet repeated figure accumulates weight and orchestral breadth until a full symphonic statement overwhelms it, matching the deep war's transition from distant ruptures to organized global advance. |
| `56` | `00:00.450-01:49.200` (`108.750 s`) | `1.250 s` in; `5.000 s` out from final-cue time `103.750`; `0.250 s` zero tail | Fixed `+6.5 dB` gain; 44.1 kHz delivery; PCM s16le WAV; Vorbis quality-6 OGG from that WAV | Nearly the complete performance preserves tension, withdrawal, exposed rests, and closing chords, keeping the aftermath reflective and costly rather than triumphal. |

Final durations, including the zeroed tails, are `115.000000 s` for ID `54`, `110.000000 s` for ID `55`, and `109.000000 s` for ID `56`.

## Final-file manifest

| Audio ID | Final music file | Duration / bytes | OGG loudness / true peak / LRA | OGG SHA-256 | Final sound mirror | Duration / bytes | WAV loudness / true peak / LRA | WAV SHA-256 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| `54` | `music/018_resources_found/super_event_54_oth_kesh_emergence.ogg` | `115.000000 s` / `2,350,682` | `-19.21 LUFS / -2.05 dBTP / 19.50 LU` | `88d3b749fd51bcc106daf352ae9791c51d3452e7bce9a01ebf8971dad57385c0` | `sound/018_resources_found/super_event_54_oth_kesh_emergence.wav` | `115.000000 s` / `20,286,078` | `-19.20 LUFS / -2.15 dBTP / 19.50 LU` | `daf27599720d281eaa96fe828dc38337553026054b634a57d652a41236050575` |
| `55` | `music/018_resources_found/super_event_55_deep_war_crosses_seas.ogg` | `110.000000 s` / `2,093,243` | `-18.47 LUFS / -2.27 dBTP / 18.50 LU` | `b6888c95658dafbf40dd822550d05c505e9a653ce4daa01191e00a6500c28215` | `sound/018_resources_found/super_event_55_deep_war_crosses_seas.wav` | `110.000000 s` / `19,404,078` | `-18.44 LUFS / -2.26 dBTP / 18.60 LU` | `f0ee745abfbe432cd26b37ad14fb800ab4bcbf77e442eb11d06f8f8f991e1266` |
| `56` | `music/018_resources_found/super_event_56_last_depth_sealed.ogg` | `109.000000 s` / `1,884,444` | `-21.86 LUFS / -2.32 dBTP / 14.20 LU` | `b1131b009a715c20598bf720d485c05038d583accbc1e46744dbc182d1f7631e` | `sound/018_resources_found/super_event_56_last_depth_sealed.wav` | `109.000000 s` / `19,227,678` | `-21.88 LUFS / -2.27 dBTP / 14.20 LU` | `9be248a28861b96a8c454ab729af8d710727c2b3289eb4820efa98b1cba8fcc9` |

All six final files decode successfully. The three OGG file hashes and decoded-PCM hashes are mutually unique; none matches another repository OGG by file hash. The quieter integrated level on ID `56` is intentional and follows from retaining its full piano dynamic range without peak limiting or compression.

## Attribution text

Courtesy credit for audio ID `54`:

> Modest Mussorgsky, *Pictures at an Exhibition* - `IV. Bydło (Sempre moderato, pesante)`; performed by Skidmore College Orchestra; recording released by Musopen into the public domain worldwide, with unconditional use granted where waiver is unavailable; source and VRTS permission record via Wikimedia Commons. Chaos Redux excerpted `00:24.000-02:18.750`, applied quarter-sine fades, fixed gain, a zeroed tail, resampled to 44.1 kHz, and encoded OGG/WAV derivatives.

Courtesy credit for audio ID `55`:

> Johannes Brahms, Symphony No. 1 in C minor, Op. 68 - I. `Un poco sostenuto - Allegro`; performed by the Czech National Symphony Orchestra and published as the Musopen Symphony Orchestra recording; source via Wikimedia Commons. Recording dedicated under CC0 1.0 Universal: https://creativecommons.org/publicdomain/zero/1.0/. Chaos Redux excerpted `08:40.000-10:29.750`, applied quarter-sine fades and a zeroed tail, resampled to 44.1 kHz, and encoded OGG/WAV derivatives. No endorsement is implied.

Required credit for audio ID `56`:

> Frédéric Chopin, Prelude in E minor (Largo), Op. 28 No. 4; performed by Ivan Ilić, Paris, October 2005; source via Wikimedia Commons / IMSLP. Recording licensed CC BY 3.0: https://creativecommons.org/licenses/by/3.0/. Chaos Redux excerpted `00:00.450-01:49.200`, applied quarter-sine fades, fixed gain, and a zeroed tail, and encoded OGG/WAV derivatives. No endorsement by Ivan Ilić is implied.

## Live wiring map

| Visible slot | Audio ID | Music helpers | Sound wrappers | Base sound |
| ---: | ---: | --- | --- | --- |
| `82` | `54` | `chaosx_super_event_54_0_5` through `chaosx_super_event_54_3_0` | `chaosx_super_event_54_sound_0_5` through `chaosx_super_event_54_sound_3_0` | `chaosx_super_event_resources_found_oth_kesh_emergence_track` |
| `83` | `55` | `chaosx_super_event_55_0_5` through `chaosx_super_event_55_3_0` | `chaosx_super_event_55_sound_0_5` through `chaosx_super_event_55_sound_3_0` | `chaosx_super_event_resources_found_deep_war_crosses_seas_track` |
| `84` | `56` | `chaosx_super_event_56_0_5` through `chaosx_super_event_56_3_0` | `chaosx_super_event_56_sound_0_5` through `chaosx_super_event_56_sound_3_0` | `chaosx_super_event_resources_found_last_depth_sealed_track` |

The live `.asset` definitions still reference the exact stable Event 018 filenames above. Production has no fallback, placeholder, generated cue, reused final track, or unresolved distribution-rights caveat. ID `56` remains attribution-dependent under CC BY 3.0, and the complete required credit and change notice are retained here and in the shared audio package record.
