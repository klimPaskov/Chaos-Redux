# Event 018 super-event audio production handoff

## Final disposition

Audio research, rights repair, production, and downstream documentation are complete for all three Event 018 Oth-Kesh super-event roles. Three distinct source recordings are preserved, rights-checked, edited into 60-to-120-second musical arcs, and exported as paired 44.1 kHz stereo WAV files.

Detailed provenance, licence evidence, musical rationale, attribution, edit parameters, and hashes live in:

- `docs/super_events/018_resources_found/audio_research.md`
- `docs/assets/018_resources_found/audio_manifest.md`
- `docs/assets/018_resources_found/source/audio/license_evidence/README.md`

## Stable identifier map

| Role | Visible slot | Audio ID | Final WAV | Final WAV | Stable underlying sound ID |
| --- | ---: | ---: | --- | --- | --- |
| `THE OTH-KESH HOST RISES` | `82` | `54` | `sound/018_resources_found/super_event_54_oth_kesh_emergence.wav` | `sound/018_resources_found/super_event_54_oth_kesh_emergence.wav` | `chaosx_super_event_resources_found_oth_kesh_emergence_track` |
| `THE DEEP WAR CROSSES THE SEAS` | `83` | `55` | `sound/018_resources_found/super_event_55_deep_war_crosses_seas.wav` | `sound/018_resources_found/super_event_55_deep_war_crosses_seas.wav` | `chaosx_super_event_resources_found_deep_war_crosses_seas_track` |
| Conditional `THE LAST DEPTH IS SEALED` | `84` | `56` | `sound/018_resources_found/super_event_56_last_depth_sealed.wav` | `sound/018_resources_found/super_event_56_last_depth_sealed.wav` | `chaosx_super_event_resources_found_last_depth_sealed_track` |

The duration and rights repair changed no ID, helper, wrapper, sound ID, runtime filename, or visible-slot pairing.

## Final source and rights map

### ID 54 - Oth-Kesh emergence

- Selection: Mussorgsky, `IV. Bydło - Sempre moderato, pesante`, *Pictures at an Exhibition*; Skidmore College Orchestra.
- Source page: <https://commons.wikimedia.org/wiki/File:Modest_Mussorgsky_-_pictures_at_an_exhibition_-_iv._bydlo_-_sempre_moderato%2C_pesante.ogg>
- Rights: public-domain composition; Musopen worldwide public-domain release and unconditional use grant, confirmed by Wikimedia VRTS ticket `2008012110017088`.
- Preserved source: `docs/assets/018_resources_found/source/audio/mussorgsky_bydlo_musopen_vrts_original.ogg`
- Source interval: `00:24.000-02:18.750`; `0.250 s` zero tail; final `115.000000 s`.
- Source SHA-256: `87da8f6bc6a03900ce0eac2879e7b027de707d1173c1cadc82db1caa081a88d4`.

### ID 55 - cross-sea world end

- Selection: Brahms, Symphony No. 1 in C minor, Op. 68, I. `Un poco sostenuto - Allegro`; Czech National Symphony Orchestra / Musopen Symphony Orchestra.
- Source page: <https://commons.wikimedia.org/wiki/File:Brahms,_Symphony_No._1_in_C_Minor,_Op._68_-_I._Un_poco_sostenuto_-_Allegro.ogg>
- Licence: <https://creativecommons.org/publicdomain/zero/1.0/>
- Rights: public-domain composition; recording CC0 1.0 Universal, including worldwide copyright and neighbouring-rights waiver to the extent allowed by law.
- Preserved source: `docs/assets/018_resources_found/source/audio/brahms_symphony_1_i_musopen_cc0_original.ogg`
- Source interval: `08:40.000-10:29.750`; `0.250 s` zero tail; final `110.000000 s`.
- Source SHA-1: `6ad72b00ca5032cbe5aa06aea80c70c82533bb90`, matching the Commons structured checksum.
- Source SHA-256: `f86f1df2f97b79c9bc92dac63b0da1bf868675005af4fe9c05ab886291af9b95`.
- Superseded research source: the United States Air Force Debussy recording remains preserved but is not wired because its affirmative rights basis was U.S.-specific.

### ID 56 - eligible global defeat

- Selection: Chopin, Prelude in E minor (Largo), Op. 28 No. 4; Ivan Ilić, piano; Paris, October 2005.
- Source page: <https://commons.wikimedia.org/wiki/File:Ivan_Ili%C4%87-Chopin_Prelude_Opus_28_n.4.ogg>
- Licence: <https://creativecommons.org/licenses/by/3.0/>
- Rights: public-domain composition; recording CC BY 3.0.
- Preserved source: `docs/assets/018_resources_found/source/audio/chopin_prelude_op28_no4_ivan_ilic_original.ogg`
- Source interval: `00:00.450-01:49.200`; `0.250 s` zero tail; final `109.000000 s`.
- Source SHA-256: `c64c302948b73e251478b4e4a9e44d0e92ceec2e34f95e02d6c1130420dcd7cf`.
- Mandatory treatment: credit Chopin and Ilić, link the source and CC BY 3.0, state the excerpt/fade/gain/encoding changes, add no incompatible restriction, and avoid implied endorsement.

## Final technical verification

All six outputs decode, are stereo, use exactly 44,100 Hz, and are 60-to-120 seconds. OGG outputs are Vorbis. WAV outputs are signed 16-bit little-endian PCM. Every edit reaches digital zero through a quarter-sine fade and ends with a `0.250 s` zeroed tail.

| Audio ID | OGG duration / LUFS / dBTP / LRA | WAV duration / LUFS / dBTP / LRA | OGG SHA-256 | WAV SHA-256 |
| ---: | --- | --- | --- | --- |
| `54` | `115.000000 / -19.21 / -2.05 / 19.50` | `115.000000 / -19.20 / -2.15 / 19.50` | `88d3b749fd51bcc106daf352ae9791c51d3452e7bce9a01ebf8971dad57385c0` | `daf27599720d281eaa96fe828dc38337553026054b634a57d652a41236050575` |
| `55` | `110.000000 / -18.47 / -2.27 / 18.50` | `110.000000 / -18.44 / -2.26 / 18.60` | `b6888c95658dafbf40dd822550d05c505e9a653ce4daa01191e00a6500c28215` | `f0ee745abfbe432cd26b37ad14fb800ab4bcbf77e442eb11d06f8f8f991e1266` |
| `56` | `109.000000 / -21.86 / -2.32 / 14.20` | `109.000000 / -21.88 / -2.27 / 14.20` | `b1131b009a715c20598bf720d485c05038d583accbc1e46744dbc182d1f7631e` | `9be248a28861b96a8c454ab729af8d710727c2b3289eb4820efa98b1cba8fcc9` |

The three final WAV file hashes and decoded-PCM hashes are mutually unique. ID `56` intentionally remains quieter because its complete piano dynamic range was preserved without compression or limiting.

## Runtime and catalogue alignment

- `music/chaosx_super_event_music.asset` still points every ID `54`-`56` helper to the exact stable OGG filename.
- `sound/chaosx_sound.asset` still points every base sound and wrapper to the exact stable WAV filename.
- `music/chaosx_super_event_music.txt` still contains one representative zero-chance helper per cue.
- `localisation/english/chaosx_music_l_english.yml` identifies ID `55` as Brahms rather than the superseded Debussy source.
- `music/chaosx_music_track_list.html`, `docs/super_events/super_event_audio_packages.md`, `docs/assets/018_resources_found/manifest.md`, and `docs/events/018_resources_found/overview.md` carry the active sources, rights, and durations.

## Files added or replaced

Preserved source and evidence:

- `docs/assets/018_resources_found/source/audio/brahms_symphony_1_i_musopen_cc0_original.ogg`
- `docs/assets/018_resources_found/source/audio/license_evidence/README.md`
- nine HTML evidence snapshots under `docs/assets/018_resources_found/source/audio/license_evidence/`

Final music and sound files were replaced in place at the six stable paths listed above. Primary audio documentation and all Event 018 downstream catalogue/attribution records were updated. The superseded Debussy source master was retained for audit history.

## Blockers, simplifications, and unresolved rights risk

There are no audio-production blockers, simplifications, fallbacks, placeholders, generated cues, reused final tracks, or unresolved distribution-rights caveats. ID `56` remains conditional on satisfying CC BY 3.0; the required attribution and change notice are present in the active manifest, research note, and shared audio package record. No commit was created.
