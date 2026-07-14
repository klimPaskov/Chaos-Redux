# Event 016 super-event audio research handoff

Status: complete for the audio-research and Event 016-owned OGG scope. The subagent commit hash is supplied in the parent return because a commit cannot include its own hash.

## Delivered package

- Full rights, fit, attribution, mastering, loudness, hash, and integration research: `docs/super_events/016_brilliant_scientist_super_event_audio_research.md`.
- Source and evidence index: `docs/super_events/source_audio/016_brilliant_scientist/README.md`.
- Six source masters plus frozen Commons revisions, API metadata, upstream Archive.org evidence, and license legal code: `docs/super_events/source_audio/016_brilliant_scientist/`.
- Six final game-ready OGGs: `music/016_brilliant_scientist/`.

All six required packages are retained. R1 removal was rejected. R7 is preserved: Laboratory World is administrative conquest/integration; Strategic Singularity is the vulnerable multi-year denied-victory device that crosses the shared chaos threshold and then commits canonical Fallout.

## Parent-assigned IDs

These IDs were supplied by the parent after a live collision scan; they were not reserved by the audio researcher. Event 020 owns IDs 85 through 87.

| ID | Package | Event 016 OGG | World-end scenario |
| ---: | --- | --- | ---: |
| 88 | International recognition | `music/016_brilliant_scientist/super_event_88_international_recognition.ogg` | — |
| 89 | Kruger State formation | `music/016_brilliant_scientist/super_event_89_kruger_state_formation.ogg` | — |
| 90 | Global Kruger threat | `music/016_brilliant_scientist/super_event_90_global_kruger_threat.ogg` | — |
| 91 | Laboratory World | `music/016_brilliant_scientist/super_event_91_laboratory_world.ogg` | 11 |
| 92 | Strategic Singularity | `music/016_brilliant_scientist/super_event_92_strategic_singularity.ogg` | 12 |
| 93 | Qualifying defeat aftermath | `music/016_brilliant_scientist/super_event_93_qualifying_defeat_aftermath.ogg` | — |

## Six selections and rights

| ID | Selection | Performer/source | Recording rights |
| ---: | --- | --- | --- |
| 88 | Debussy, *Première Arabesque* | Patrizia Prati, live at the Museum of Romanticism, Madrid | CC BY-SA 4.0; derivative remains CC BY-SA 4.0 |
| 89 | Brahms, *Academic Festival Overture*, Op. 80 | Skidmore College Orchestra / Musopen | Worldwide public-domain dedication plus unconditional fallback grant; courtesy attribution retained |
| 90 | Wagner, *Ride of the Valkyries* | Ulm Philharmonic; James Allen Gähres; 2014 | EFF Open Audio License 1.0; attribution and same-license derivative required |
| 91 | Halvorsen, *Passacaglia on a Theme by Handel* | Roxana Pavel Goldstein and Elias Goldstein; Pandora Music / ibiblio | CC BY-SA 2.0; derivative remains CC BY-SA 2.0 |
| 92 | Mahler, Symphony No. 5, movement II | Peabody Symphony Orchestra / Archive.org | CC0 1.0 |
| 93 | Chopin, Nocturne Op. 9 No. 1 | Vadim Chaimovich / Musopen | CC0 1.0 |

The underlying six compositions are public domain. Exact attribution text and change notices are in the research note and embedded in the final OGG Vorbis comments.

## Final technical properties

Each file is Ogg Vorbis, `115.000000 s`, `44,100 Hz`, stereo. No compression or limiting was used.

| ID | Loudness / peak / LRA | OGG SHA-256 |
| ---: | --- | --- |
| 88 | `-19.7 LUFS / -3.8 dBTP / 9.5 LU` | `c2db8fa30ed1576f6c68545ef62dd122f004ff193fe22a9de4406d6fa672a248` |
| 89 | `-24.0 LUFS / -2.3 dBTP / 18.1 LU` | `f0d37937dff3cd605c71afe5fced67d31fdb2775142c84c13f8a70d4ad06f8be` |
| 90 | `-19.8 LUFS / -5.5 dBTP / 6.7 LU` | `286dfd0339dda76bdc368240e523c0e87286f03816e92089031c3941c2bc8b60` |
| 91 | `-20.9 LUFS / -2.9 dBTP / 9.9 LU` | `e333ba54bb4e2e5508360b207352d912b187a38ede8bf2dbe309c9f32d4bffb1` |
| 92 | `-21.1 LUFS / -2.2 dBTP / 19.3 LU` | `2665fcb7605ae84cad2a6729ce338adfa169123b16499dcf8891ad18526991d0` |
| 93 | `-20.5 LUFS / -5.1 dBTP / 12.5 LU` | `42d9cb2173ef4024d1c8f9a9ab140b0f8cc2cd53f1c1a4009ee982b9f0983b7d` |

The quieter integrated level for ID 89 preserves the large natural range of the solemn Brahms opening without peak limiting. All files decode successfully; encoded-file hashes and decoded-PCM hashes are mutually unique.

## Parent wiring checklist

1. In `music/chaosx_super_event_music.asset`, add six definitions per ID using names `chaosx_super_event_<ID>_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, and `_3_0`, all pointing to the corresponding Event 016 OGG.
2. Use definition volumes `0.67`, `1.33`, `2.00`, `2.67`, `3.33`, and `4.00` in that order. Do not create six OGG copies.
3. In `music/chaosx_super_event_music.txt`, add one representative zero-chance row per track using `chaosx_super_event_<ID>_1_5`.
4. If the implementation uses the sound channel, reproduce the documented source edit into a matching Event 016 WAV and add the base sound plus `chaosx_super_event_<ID>_sound_<suffix>` wrappers. Do not generate a WAV by decoding the lossy final OGG when the preserved source and exact edit chain are available.
5. Set `global.current_super_event_audio_id` to the matching parent-assigned ID and use the existing settings-aware playback helper.
6. Add the six rows to `music/chaosx_music_track_list.html` with their visible super-event IDs, titles, performers, final durations, paths, and rights.
7. Keep the two terminal routes distinct in trigger/effect wiring: ID 91 accompanies world-end scenario 11; ID 92 accompanies scenario 12 and the threshold-then-Fallout sequence.

## Validation evidence

- Every preserved source byte count and SHA-1 matches its frozen publisher API record.
- The Mahler source is conclusively movement II: frozen Archive.org metadata names `02.PSO020103-Mahler-5-II.ogg` and matches the Commons byte count and SHA-1 despite the Commons credit hyperlink selecting movement IV.
- A repository-wide source-byte scan found no matching source outside the Event 016 archive.
- A repository title/performer scan found no prior use. The only matching Wagner work text is an Event 013 rejection of a different 1921 Edison recording; Event 016 uses the distinct, openly licensed 2014 Ulm performance.
- Every final file is exactly `115.000000 s`, Ogg Vorbis, `44,100 Hz`, stereo, and includes source/license/change metadata.

## Scope boundary and blockers

No shared music asset, station, sound, localisation, GUI, gameplay, specification, workbook, or catalog file was edited. No numeric reservation was made by this subagent; filenames use the IDs later supplied by the parent. No sound-channel WAV was requested or produced in the OGG-only subtask.

There is no rights, source-download, mastering, or Event 016-owned file blocker. Shared wiring and any WAV mirror remain parent-owned integration work, not a fallback or simplification of the delivered audio-research scope.
