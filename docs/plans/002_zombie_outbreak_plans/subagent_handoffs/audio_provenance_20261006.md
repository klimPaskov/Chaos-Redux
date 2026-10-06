# Audio Provenance Handoff — Event 002 Zombie Outbreak

Disposition: source provenance is confirmed for super-event IDs 1 and 5. IDs 2, 3, and 6 have source pages with usable rights statements, but their original audio bytes and runtime matches remain unresolved. No runtime WAV, sound definition, event, localisation, or other wiring was changed.

## Confirmed rows

| ID and cue | Sound definition | Source archive and rights | Runtime evidence and edit timeline |
| --- | --- | --- | --- |
| 1 — Undead? | `chaosx_super_event_zombies_track` | `docs/assets/002_zombie_outbreak/source_audio/rimsky_korsakov_scheherazade_i_archive_original.mp3`; 19,953,265 bytes; SHA-1 `f8f5d1744c8e64fb905c36897dc4db130d0e0064`; SHA-256 `437af712f594e92bb1abaf863a8709c66894e93611a17c5c13b02ee1b4c71b1b`. Composition is public domain; Internet Archive marks the 1942 source Public Domain and its Commons recording file is CC0 1.0. | Runtime `sound/002_zombie_outbreak/super_event_1_zombies.wav`; 105.000000 seconds; SHA-256 `753778951e4ab1fc6f72ae54a00c5be8bdc1c8cca527de9e9f9ba0c1cf3aceac`. Opening `00:00.000-01:45.000`, entry/exit fades, stereo 44.1 kHz PCM16. Correlation confirms offset `0.000 s`, with `0.998199` at `00:40` and `0.997459` at `01:15`; an early fade-in window at `00:10` gives `0.957256`. |
| 5 — The Dead Are Buried | `chaosx_super_event_zombies_defeat_track` | `docs/assets/002_zombie_outbreak/source_audio/handel_royal_fireworks_rejoicing_archive_original.mp3`; 3,216,864 bytes; SHA-1 `39bccf51a21ee753474796c3640621def052d8e5`; SHA-256 `80e353c2a2ad1b1850b2d291444ec55a66eb0f306b993eed2f0fcc270f9184aa`. Handel’s composition is public domain; the Paul Ayres recording is CC0 1.0 per Internet Archive and Commons. | Runtime `sound/002_zombie_outbreak/super_event_5_zombies_defeat.wav`; 98.633741 seconds; SHA-256 `20fb149df2aee1de553e3080ce1b2070cec080ac53f285ebf67daef56d662389`. The opening aligns at source offset `0.000 s`, with fades; coefficients are `0.997126` at `00:08`, `0.996889` at `00:35`, and `0.997235` at `01:10`. The source duration is 98.742857 seconds, leaving a 0.109116 second difference at the end. |

## Unresolved source rows

| ID and cue | Exact source record and rights | Local record and status |
| --- | --- | --- |
| 2 — The Alliance of Man | The Commons page identifies the John William Steffe melody and Julia Ward Howe lyrics, arranged by Eric Richards, performed by the United States Air Force Band Airmen of Note, official U.S. Air Force employee production, Public Domain in the United States, and Public Domain Mark 1.0; composition date 1861. Page revision `1030745773`; remote file metadata is 6,322,760 bytes and SHA-1 `1acfc958af0455849032cf0e405a38f5a051e2b0`. | Runtime `sound/002_zombie_outbreak/super_event_2_alliance_of_man.wav`, 89.978776 seconds, SHA-256 `181c48a3e69b94cd0fb0f805af18c90a565eb7b9d4475dcb92d4ab03c8f023ec`. No local source bytes and no source/runtime comparison. |
| 3 — Zombie Apocalypse | The Commons page describes Membeth’s own Gregorian *Dies Irae* recording and a worldwide public-domain release by its copyright holder. Page revision `1205385897`; remote file metadata is 6,562,097 bytes and SHA-1 `d13e914db3016ab43bcb89c695e501ac8fd19605`. | Runtime `sound/002_zombie_outbreak/super_event_3_zombie_apocalypse.wav`, 95.000000 seconds, SHA-256 `a3fb7d844507f05cbc277d845f24e9d561dce508adaef77a0c163edc8524867d`. No local source bytes and no source/runtime comparison. |
| 6 — Wendigo | The Commons page identifies the Musopen Symphony Orchestra recording of Smetana’s *Vltava* and CC0 1.0 for the recording file; Smetana composed the work in 1874 and died in 1884. Page revision `955954082`; remote file metadata is 20,531,794 bytes and SHA-1 `a0025fa04c0774296d2528a44b68e6a6938b2ae3`. The current Musopen piece page is `https://musopen.org/music/25719-ma-vlast-vltava-the-moldau/`. | Runtime `sound/002_zombie_outbreak/super_event_6_wendigo.wav`, 105.000000 seconds, SHA-256 `dc01cd34cf253c3d76fb275389247cd830b161988a68077908ad1a3153a7dda5`. No local source bytes and no source/runtime comparison. |

The source/runtime WAV hashes and definitions above are evidence records only; the parent owns runtime acceptance and wiring. Source file metadata, license links, and per-row notes are in `docs/assets/002_zombie_outbreak/source_audio/source_manifest.md`.

## Retrieval and verification limits

The initial Commons original-file request returned HTTP 429 with a bot-traffic notice. The command stopped at that response before saving a Commons file; I did not retry or work around the limit. IDs 1 and 5 were recovered from the directly linked Internet Archive originals and independently matched against the runtime WAVs. IDs 2, 3, and 6 remain unresolved at the byte and waveform-evidence level. The USAF source link from the Commons page did not return accessible page content in the web fetch. The Musopen track page is readable, but its direct request returned a JavaScript/Cloudflare challenge.

The precise next action is to retrieve the exact Commons original files for IDs 2, 3, and 6 once the 429 has cleared, validate the downloaded files against the recorded Commons SHA-1 values, and compare decoded PCM to the existing runtime WAVs before marking those rows verified. If that exact source path becomes unavailable, parent review is required before selecting another recording.

## Files changed and force-add list

- `docs/assets/002_zombie_outbreak/source_audio/rimsky_korsakov_scheherazade_i_archive_original.mp3`
- `docs/assets/002_zombie_outbreak/source_audio/handel_royal_fireworks_rejoicing_archive_original.mp3`
- `docs/assets/002_zombie_outbreak/source_audio/source_manifest.md`
- `docs/super_events/super_event_audio_packages.md`
- `docs/plans/002_zombie_outbreak_plans/subagent_handoffs/audio_provenance_20261006.md`

No files were staged or committed.
