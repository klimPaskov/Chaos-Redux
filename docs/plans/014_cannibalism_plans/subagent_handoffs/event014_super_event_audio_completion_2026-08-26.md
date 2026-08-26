# Event 014 super-event audio completion handoff — 2026-08-26

## Status

Audio research, rights verification, source preservation, OGG conversion, WAV decoding, runtime metadata verification, hash recording, and uniqueness review are complete for the four requested Event 014 super-events.

Each role now has a preserved source recording, a final Vorbis OGG derivative, and a final game-ready signed 16-bit PCM WAV decoded mechanically from that OGG. Both runtime formats are exactly 44,100 Hz stereo, with one distinct musical recording per role and durations from 114 to 120 seconds.

Sound-definition registration, settings-volume wrappers, event dispatch, and any existing WAV wiring remain parent-owned and were not edited here.

The machine-readable evidence receipt is [ffprobe_and_hash_receipt.json](../../../assets/014_cannibalism/audio/super_events/ffprobe_and_hash_receipt.json).

## Final role map

| Super-event role | ID | Track | Creator or composer | Performer or recording source | Final OGG | Final WAV | Suggested sound definition id |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| Hannibal Lecter reveal | `49` | `Danse macabre, Op. 40` | Camille Saint-Saëns | Philadelphia Symphony Orchestra; Leopold Stokowski | `sound/014_cannibalism/super_event_49_hannibal_reveal.ogg` | `sound/014_cannibalism/super_event_49_hannibal_reveal.wav` | `chaosx_super_event_cannibalism_hannibal_reveal_track` |
| Ordinary Hannibal worldwide victory/world-end | `50` | `Siegfried's Funeral March and Finale` from `Götterdämmerung` | Richard Wagner; transcriptions by Howard Bowlin and John R. Bourgeois | United States Marine Band; Col. John R. Bourgeois | `sound/014_cannibalism/super_event_50_hannibal_world_end.ogg` | `sound/014_cannibalism/super_event_50_hannibal_world_end.wav` | `chaosx_super_event_cannibalism_hannibal_world_end_track` |
| Eligible global defeat aftermath | `52` | `Élégie, Op. 24` | Gabriel Fauré | Hans Goldstein, cello; Eli Kalman, piano | `sound/014_cannibalism/super_event_52_global_defeat_aftermath.ogg` | `sound/014_cannibalism/super_event_52_global_defeat_aftermath.wav` | `chaosx_super_event_cannibalism_global_defeat_aftermath_track` |
| Wendigo Hannibal worldwide victory/world-end | `53` | `Peer Gynt Suite No. 1, Op. 46 - II. The Death of Aase` | Edvard Grieg | Musopen Symphony | `sound/014_cannibalism/super_event_53_wendigo_hannibal_world_end.ogg` | `sound/014_cannibalism/super_event_53_wendigo_hannibal_world_end.wav` | `chaosx_super_event_cannibalism_wendigo_world_end_track` |

The rejected visible slot `51` is not used because it belongs to the Holy Realm's existing super-event.

## Track packages

### ID 49 — reveal

- **Title:** `Danse macabre, Op. 40`.
- **Composer:** Camille Saint-Saëns.
- **Performer:** Philadelphia Symphony Orchestra under Leopold Stokowski.
- **Recording identity:** Victor 6505-A/B, recorded 29 April 1925, masters CVE-27929 and CVE-27930.
- **Source URL:** https://upload.wikimedia.org/wikipedia/commons/7/76/PhiladelphiaSymphonyOrchestra-DanseMacabre.ogg
- **Source page:** https://commons.wikimedia.org/wiki/File:PhiladelphiaSymphonyOrchestra-DanseMacabre.ogg
- **Local rights evidence:** `docs/assets/014_cannibalism/audio/super_events/evidence/wikimedia_danse_macabre_rights.html`.
- **License and usage:** The source page marks the sound recording public domain in the United States under its PD-US-record-expired determination because it was published before 1 January 1926; the 1874 composition is public domain. Use is accepted under this U.S./source-country rights basis, with courtesy credit recommended.
- **License confidence:** High, with the stated U.S. jurisdiction note.
- **Attribution text:** `Camille Saint-Saëns, Danse macabre, Op. 40; Philadelphia Symphony Orchestra, Leopold Stokowski, conductor; recorded 29 April 1925, Victor 6505; source via Wikimedia Commons and the Internet Archive; public-domain composition and recording; edited excerpt.`
- **Original downloaded source:** `docs/assets/014_cannibalism/audio/super_events/sources/danse_macabre_stokowski_1925_source.ogg`.
- **Source duration:** `419.082449 s`.
- **Source SHA-1:** `66aaedc1e25a0bfbbcc010397145f528d9184b1a`.
- **Source SHA-256:** `5da52fa63c374fa3744886548aa74786128cdd4760b976194b22f22f30c69820`.
- **Final archive derivative:** `docs/assets/014_cannibalism/audio/super_events/final/super_event_49_hannibal_reveal.ogg`.
- **Final runtime derivative:** `sound/014_cannibalism/super_event_49_hannibal_reveal.ogg`.
- **Final duration:** `114.000000 s`.
- **Final SHA-1:** `e653b8bfe7ae205bef4ae208f0c41743a984835a`.
- **Final SHA-256:** `fac763355657a5797ffba69b3348381fd46235cbe911cb10888257a835483b10`.
- **Editing and conversion:** Retained source interval `00:00.000-01:54.000`, applied a `0.25 s` fade-in and `6.00 s` fade-out, loudness-normalized, and encoded as stereo Vorbis OGG at 44.1 kHz for a one-shot cue.
- **Fit and pacing:** The disciplined macabre dance gives the reveal ritual, predatory intelligence, and controlled motion instead of generic horror ambience; its immediate opening supports the public command reveal.
- **Suggested use:** Event 014 super-event slot `49`, Hannibal Lecter public reveal.
- **Uncertainty:** The recording-rights statement is explicitly U.S.-jurisdiction based; no unresolved source or runtime gate remains under the current package policy.

### ID 50 — ordinary world-end

- **Title:** `Siegfried's Funeral March and Finale` from `Gotterdammerung`.
- **Composer:** Richard Wagner; funeral march transcription by Howard Bowlin and finale transcription by John R. Bourgeois.
- **Performer:** United States Marine Band; Col. John R. Bourgeois, director.
- **Recording identity:** Recorded 8-11 December 1981 at Lisner Auditorium, Washington, D.C.
- **Source URL:** https://upload.wikimedia.org/wikipedia/commons/7/7d/Siegfrieds_funeral_march_and_finale.ogg
- **Source page:** https://commons.wikimedia.org/wiki/File:Siegfrieds_funeral_march_and_finale.ogg
- **Local rights evidence:** `docs/assets/014_cannibalism/audio/super_events/evidence/wikimedia_siegfrieds_funeral_march_rights.html`.
- **License and usage:** The 1876 composition is public domain, and the source page marks the official United States Marine Band recording public domain as a work of the U.S. federal government. Use is accepted under that U.S. federal-work rights basis, with courtesy credit recommended.
- **License confidence:** High, with the stated U.S. federal-jurisdiction note.
- **Attribution text:** `Richard Wagner, Siegfried's Funeral March and Finale from Götterdämmerung; United States Marine Band, Col. John R. Bourgeois, director; recorded 8-11 December 1981; public-domain composition and U.S. federal-government recording; source via Wikimedia Commons; edited excerpt.`
- **Original downloaded source:** `docs/assets/014_cannibalism/audio/super_events/sources/siegfrieds_funeral_march_us_marine_band_source.ogg`.
- **Source duration:** `629.603265 s`.
- **Source SHA-1:** `934030f52a701bc1098926caefb4da1512d6ab72`.
- **Source SHA-256:** `68124de4da401be0e07b2e2d637347e1a981b5cafa6ead74b5cd43f6becc6e41`.
- **Final archive derivative:** `docs/assets/014_cannibalism/audio/super_events/final/super_event_50_hannibal_world_end.ogg`.
- **Final runtime derivative:** `sound/014_cannibalism/super_event_50_hannibal_world_end.ogg`.
- **Final duration:** `120.000000 s`.
- **Final SHA-1:** `3d19b028e7804773b23b55d02f5cfd51f54f9a4f`.
- **Final SHA-256:** `7daa11d5e45ad000e1b6c995a12b1509f3f58c5a7843a4d3ae1ef748b343686b`.
- **Editing and conversion:** Retained source interval `02:31.539-04:31.539` after a musical pause, applied a `0.25 s` fade-in and `6.00 s` fade-out, loudness-normalized, and encoded as stereo Vorbis OGG at 44.1 kHz for a one-shot cue.
- **Fit and pacing:** The funeral march supplies military mass, procession, and terminal finality without becoming a victory fanfare; the retained build suits organized worldwide consumption.
- **Suggested use:** Event 014 ordinary Hannibal worldwide victory and world-end slot `50`.
- **Uncertainty:** The recording-rights statement is explicitly U.S.-federal-jurisdiction based; no unresolved source or runtime gate remains under the current package policy.

### ID 52 — global defeat aftermath

- **Title:** `Élégie, Op. 24`.
- **Composer:** Gabriel Fauré.
- **Performer:** Hans Goldstein, cello; Eli Kalman, piano.
- **Recording identity:** Performance dated 3 June 2006 at the Michael Fields Agriculture Institute; Al Goldstein collection in Pandora Music at ibiblio.
- **Source URL:** https://upload.wikimedia.org/wikipedia/commons/e/ef/Faure_-_Elegie.ogg
- **Source page:** https://commons.wikimedia.org/wiki/File:Faure_-_Elegie.ogg
- **Local rights evidence:** `docs/assets/014_cannibalism/audio/super_events/evidence/wikimedia_faure_elegie_rights.html` and `docs/assets/014_cannibalism/audio/super_events/evidence/cc_by_sa_2_0_deed.html`.
- **License and usage:** The composition is public domain; the recording is licensed CC BY-SA 2.0 through the source's EFF Open Audio License / CC BY-SA 2.0 statement. The derivative may be shared and adapted with appropriate credit, license link, change notice, and share-alike treatment.
- **License confidence:** High, provided the attribution and share-alike notice below travel with the derivative.
- **Attribution text:** `Gabriel Fauré, Élégie, Op. 24; Hans Goldstein (cello) and Eli Kalman (piano), Michael Fields Agriculture Institute, 3 June 2006; source via Wikimedia Commons / Pandora Music at ibiblio. Recording licensed CC BY-SA 2.0: https://creativecommons.org/licenses/by-sa/2.0/. Chaos Redux excerpted, faded, resampled where required, and loudness-normalized the recording. The adapted OGG is distributed under CC BY-SA 2.0.`
- **Original downloaded source:** `docs/assets/014_cannibalism/audio/super_events/sources/faure_elegie_goldstein_kalman_source.ogg`.
- **Source duration:** `425.669796 s`.
- **Source SHA-1:** `6d57244d2133c2968ab96508441ed08a134f240e`.
- **Source SHA-256:** `f4256bdccdc7d7ac0e547f571c6e8137b8de8cbdd604bada417a7cb89ab5ccc0`.
- **Final archive derivative:** `docs/assets/014_cannibalism/audio/super_events/final/super_event_52_global_defeat_aftermath.ogg`.
- **Final runtime derivative:** `sound/014_cannibalism/super_event_52_global_defeat_aftermath.ogg`.
- **Final duration:** `116.001043 s`.
- **Final SHA-1:** `fc21d76297406031ee5e785d29e363b5d1abeac9`.
- **Final SHA-256:** `fd43c2fc6f558c44bdfda468e336195ae5a73f6adf024959d0c2fa3c95c48199`.
- **Editing and conversion:** Removed the opening `3.146712 s` silence, retained the next `116.000 s`, applied a `0.25 s` fade-in and `6.00 s` fade-out, loudness-normalized, and encoded as stereo Vorbis OGG at 44.1 kHz for a one-shot cue.
- **Fit and pacing:** The cello-and-piano elegy stays human-scale and wounded, supporting identification, burial, testimony, and relief after defeating the network without a triumphal reset.
- **Suggested use:** Event 014 eligible global defeat aftermath slot `52`.
- **Uncertainty:** No unresolved rights or runtime gate remains if the CC BY-SA 2.0 attribution, change notice, license link, and share-alike treatment are retained.

### ID 53 — Wendigo world-end

- **Title:** `Peer Gynt Suite No. 1, Op. 46 - II. The Death of Aase`.
- **Composer:** Edvard Grieg.
- **Performer:** Musopen Symphony.
- **Recording identity:** 2012 Musopen performance.
- **Source URL:** https://upload.wikimedia.org/wikipedia/commons/3/35/Grieg_-_Peer_Gynt_Suite_No._1%2C_Op._46_-_II._The_Death_of_Aase_%28Musopen_Symphony%29.flac
- **Source page:** https://commons.wikimedia.org/wiki/File:Grieg_-_Peer_Gynt_Suite_No._1,_Op._46_-_II._The_Death_of_Aase_(Musopen_Symphony).flac
- **Local rights evidence:** `docs/assets/014_cannibalism/audio/super_events/evidence/wikimedia_death_of_aase_rights.html`.
- **License and usage:** The source page identifies the Musopen recording as released into the public domain worldwide, with unconditional use where a waiver is not legally possible; the composition is public domain.
- **License confidence:** High.
- **Attribution text:** `Edvard Grieg, Peer Gynt Suite No. 1, Op. 46 - II. The Death of Aase; Musopen Symphony (2012); public-domain composition and recording; source via Wikimedia Commons and Musopen; edited excerpt.`
- **Original downloaded source:** `docs/assets/014_cannibalism/audio/super_events/sources/death_of_aase_musopen_symphony_source.flac`.
- **Source duration:** `273.797167 s`.
- **Source SHA-1:** `b7abad25034bc4dce173af0feea99c12b4e9d419`.
- **Source SHA-256:** `5010b1911dd02d63731c21cb6ecd7914a7cdb17acf844a6418264716ce562335`.
- **Final archive derivative:** `docs/assets/014_cannibalism/audio/super_events/final/super_event_53_wendigo_hannibal_world_end.ogg`.
- **Final runtime derivative:** `sound/014_cannibalism/super_event_53_wendigo_hannibal_world_end.ogg`.
- **Final duration:** `118.000000 s`.
- **Final SHA-1:** `282244cf1ee72a60b0cbcd3e3033ce661a4fa71d`.
- **Final SHA-256:** `5435e88eab6dd2f792ae50f2a8f4c387009d0cca0a2088607a70a117ad2c0abe`.
- **Editing and conversion:** Removed `1.046312 s` of opening silence, retained the next `118.000 s`, applied a `0.25 s` fade-in and `6.00 s` fade-out, resampled the 48 kHz FLAC source to 44.1 kHz, loudness-normalized, and encoded as stereo Vorbis OGG for a one-shot cue.
- **Fit and pacing:** The sparse string lament makes this branch cold, funeral, and terminal rather than a louder copy of the ordinary world-end; it contains no borrowed Indigenous chant, language, or ceremonial element.
- **Suggested use:** Event 014 transformed/Wendigo Hannibal worldwide victory and world-end slot `53`.
- **Uncertainty:** No unresolved source, rights, or runtime gate remains.

## Runtime metadata evidence

The receipt was generated with FFprobe `N-123778-g3b55818764-20260331` and FFmpeg `N-123778-g3b55818764-20260331` on 2026-08-26 and records source, OGG, and WAV hashes plus stream metadata.

All four runtime OGGs report `format_name=ogg`, `codec_name=vorbis`, `sample_rate=44100`, `channels=2`, and `channel_layout=stereo`.

| ID | Runtime OGG duration | Codec | Sample rate | Channels | Bytes | SHA-256 |
| ---: | ---: | --- | ---: | ---: | ---: | --- |
| `49` | `114.000000 s` | Vorbis | `44100 Hz` | 2 | `1,316,907` | `fac763355657a5797ffba69b3348381fd46235cbe911cb10888257a835483b10` |
| `50` | `120.000000 s` | Vorbis | `44100 Hz` | 2 | `2,317,426` | `7daa11d5e45ad000e1b6c995a12b1509f3f58c5a7843a4d3ae1ef748b343686b` |
| `52` | `116.001043 s` | Vorbis | `44100 Hz` | 2 | `2,260,755` | `fd43c2fc6f558c44bdfda468e336195ae5a73f6adf024959d0c2fa3c95c48199` |
| `53` | `118.000000 s` | Vorbis | `44100 Hz` | 2 | `2,313,524` | `5435e88eab6dd2f792ae50f2a8f4c387009d0cca0a2088607a70a117ad2c0abe` |

The four archive final OGGs and four runtime sound OGGs are byte-identical mirrors, verified by SHA-256 and recorded as `archive_mirror_sha256_equal=true` in the receipt.

The four final WAVs below were decoded from the accepted runtime OGGs with `-map_metadata 0:s:0 -vn -ar 44100 -ac 2 -c:a pcm_s16le` and are the files intended for the base sound definitions.

| ID | Final WAV | Duration | Codec | Sample format | Sample rate | Channels | Bytes | SHA-1 | SHA-256 |
| ---: | --- | ---: | --- | --- | ---: | ---: | ---: | --- | --- |
| `49` | `sound/014_cannibalism/super_event_49_hannibal_reveal.wav` | `114.000000 s` | `pcm_s16le` | `s16` | `44100 Hz` | 2 | `20,109,914` | `977d786d50e95a6ffa8aee1d177432d5c5ca34be` | `9d90fd24f917290b84b967f59cc486e65952b892abe3b32d2b2e6780be43f806` |
| `50` | `sound/014_cannibalism/super_event_50_hannibal_world_end.wav` | `120.000000 s` | `pcm_s16le` | `s16` | `44100 Hz` | 2 | `21,168,314` | `f3f63ad2ffd36410d704726200265883ee99db0d` | `60782048cbcaa203859943177b88a531d3e56786a91ea3fc9413981fc340a055` |
| `52` | `sound/014_cannibalism/super_event_52_global_defeat_aftermath.wav` | `116.001043 s` | `pcm_s16le` | `s16` | `44100 Hz` | 2 | `20,462,934` | `cb66da26dd4a78a7be96fc8d2f3fec73a6d41e0b` | `490f802b74a1d0643ad3ccd33147375ab00d274bfa7224241eb00f36ef290d7c` |
| `53` | `sound/014_cannibalism/super_event_53_wendigo_hannibal_world_end.wav` | `118.000000 s` | `pcm_s16le` | `s16` | `44100 Hz` | 2 | `20,815,532` | `bc2394d188ed1ff2fc08a28653e5c509339e1fab` | `709a6403b512b851ff6a0cdf921237c458ba438373764e4de16d09532d3e354b` |

Source-to-derived lineage is preserved as `source recording -> accepted edited OGG -> mechanically decoded PCM WAV`; the source and OGG hashes, OGG-to-WAV command, and final WAV hashes are all recorded in the receipt.

## Uniqueness and archive audit

The four final OGG SHA-256 values and the four final WAV SHA-256 values are each mutually unique.

A byte-identity scan across 63 super-event audio files and 251 audio files under `music/` and `sound/` found no external match for any of the four final OGGs or four final WAVs.

No default soundtrack, reused Event 014 cue, generated test tone, oscillator, beep, noise bed, drone, stinger, or placeholder recording is present in this package.

The event-scoped audio workspace contains exactly four preserved source recordings, four final OGG archive derivatives, the FFprobe/hash receipt, and five local rights-evidence pages; the four final WAVs live in the runtime sound folder.

No download archive, extraction cache, rejected candidate, or duplicate candidate remains.

The two copies of each final OGG are intentional: the `docs/assets/.../final/` copy is the provenance mirror and the `sound/014_cannibalism/` copy is the accepted OGG runtime candidate. Each accepted OGG also has one final PCM WAV runtime derivative.

## Parent wiring handoff

For each ID, the parent should register the suggested base sound definition id and point it to the final runtime WAV, add the required settings-volume wrappers, and keep `global.current_super_event_audio_id` aligned with the visible slot before calling the settings-aware playback helper.

The parent should carry the ID 52 CC BY-SA 2.0 attribution, license link, change notice, and share-alike statement into the permanent attribution surface.

The prior WAV hashes are retained in the receipt for auditability; the four runtime WAV paths now contain the requested OGG-decoded PCM derivatives and are ready for the parent-owned WAV sound definitions.

The older permanent note `docs/super_events/014_cannibalism/audio_research.md` still contains historical `docs/assets/014_cannibalism/source_audio/` paths; this completion handoff and its receipt record the current `docs/assets/014_cannibalism/audio/super_events/` package paths, so the parent should reconcile that note during final catalogue and wiring review.

## Simplifications, omissions, and blockers

No audio fallback, placeholder, reused track, uncertain source, or unlicensed candidate was used.

No source, rights, hash, or runtime metadata gate is open for the four OGG candidates or their final WAV derivatives.

Sound definitions, settings wrappers, event/script dispatch, canonical catalogue edits, and live in-game playback remain outside this bounded handoff and require parent integration.
