# Event 012 Africa four-role super-event audio final handoff

Prepared: 2026-08-09. Scope: final audio research, source/licence evidence, final WAV audit, and role-specific handoff for exactly four Event 012 super-event roles. No gameplay, event, localisation, sound-definition, soundeffect, or registry file was edited.

## Delivered role set

| Role | Slot / audio ID | Track | Runtime WAV | Duration | Final SHA-256 | Raw sound name |
| --- | ---: | --- | --- | ---: | --- | --- |
| Africa is one | `101 / 58` | John Bartmann, *West in Africa* | `sound/012_africa/super_event_58_africa_is_one.wav` | `110.000 s` | `BB938151020C98CAD5530212B2142DF63F78FE2804EC2DC20F5ABAA020E52C51` | `chaosx_super_event_africa_is_one_track` |
| Scramble response | `102 / 59` | Beethoven, Symphony No. 3, II. *Marcia funebre*; Czech National Symphony Orchestra / Musopen Symphony | `sound/012_africa/super_event_59_scramble_response.wav` | `115.000 s` | `0229ED012EC10597E8782FF6E66D8FF2648BE0DF83C77D9A1C7F47467DFC7931` | `chaosx_super_event_scramble_response_track` |
| Continental wars | `103 / 60` | Brahms, Symphony No. 4, IV. *Allegro energico e passionato - Più allegro*; Musopen Symphony | `sound/012_africa/super_event_60_continental_wars.wav` | `115.000 s` | `ED719D6BFBE4FDA4866FAA802BD6A3C115A1983219764EAEDD5699BAE0EBF598` | `chaosx_super_event_continental_wars_track` |
| The World | `104 / 61` | John Bartmann, *African Moon* | `sound/012_africa/super_event_61_the_world.wav` | `116.000 s` | `88D1F7595AA49753C033DEE81BD9552E5FAED5694F1B99E114DA6642575433CD` | `chaosx_super_event_the_world_track` |

All four files are unique one-shot stereo PCM16 WAVs at 44,100 Hz. Full source pages, source files, evidence copies, final evidence WAVs, source hashes, final hashes, decoded PCM fingerprints, edit records, and rights notes are in `docs/assets/012_africa/super_events/audio_final/manifest.md` and its adjacent `sources/`, `evidence/`, and `final/` directories.

## Rights and source summary

Roles 1 and 4 use John Bartmann's *West in Africa* and *African Moon*. The archived Free Music Archive pages and Wikimedia Commons mirrors identify both recordings as CC0 1.0. The preserved source SHA-256 values are `B557044F2A318081D6DDBA710A2F7F29460D57454BB16D09F7B21770CDC7AA4A` and `A93E1EF4BBAE1C4A5D8EF02ABB01A13C493983E4E18F9A784151450541FFF989`; source durations are `174.168980 s` and `144.504966 s`.

Roles 2 and 3 use the revision-pinned Musopen FLAC masters for Beethoven's Eroica funeral march and Brahms Symphony No. 4 finale. The local SHA-1 values match the published Commons checksums: `E8BCBC56A4D293A4DC4271F3A5E4C5DFFD9A78C7` and `6FA57BD809341AC4B2C4B13F956CC19A91070E48`. The local SHA-256 values are `5CE7B5542CE9BD2798CA38861CF3DE7341573158448122443BE5A880F730F82D` and `A180D289DD7F7297110E3411BECFDA382A88F773159BDAACA0562235639CCCB0`. The frozen pages identify the compositions as public domain and the Musopen recordings as worldwide public-domain releases with an unconditional fallback grant where a waiver is ineffective.

Composition rights and recording rights were considered separately for every role. Licence confidence is high for all four because the source pages are archived, revision-pinned where applicable, and accompanied by local checksums. Courtesy attribution and edit/change notices remain in the manifest even where no legal attribution is required.

## Production and audit disposition

The existing role 2 and role 3 production derivatives were retained byte-for-byte after source re-archival and checksum verification. They remain at `-20.0 LUFS / -1.6 dBFS` true peak and `-19.0 LUFS / -3.2 dBFS` true peak, respectively, with the documented 115-second windows and phrase-safe fades.

The role 1 and role 4 runtime derivatives were re-derived from the archived CC0 OGG masters because the prior files were too hot (`-15.6 LUFS`, approximately `0 dBFS` true peak) and ended on nonzero samples without a documented safety fade. The replacement pass applies `-3.5 dB` gain, a `0.100 s` qsin fade-in, and a `3.000 s` or `5.000 s` qsin fade-out while preserving the approved first `110.000 s` or `116.000 s` source window. The resulting cues measure `-19.2 LUFS / -3.5 dBFS` true peak and `-19.1 LUFS / -3.3 dBFS` true peak and have exact target durations.

The final files were checked with FFprobe for PCM16, stereo, 44,100 Hz, and exact durations. An FFmpeg-decoded PCM SHA-256 scan of all 59 `sound/*/super_event*.wav` files found zero duplicate groups; the four Event 012 decoded fingerprints are recorded in the manifest.

## Wrapper and parent integration handoff

`sound/chaosx_sound.asset` already contains one base sound and six settings-volume `soundeffect` wrappers for each of IDs `58`, `59`, `60`, and `61`. The wrapper names are `chaosx_super_event_<audio_id>_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, and `_3_0`; each points to its role's raw sound and uses the established `max_audible = 1` / `max_audible_behaviour = fail` pattern. No registry or sound-definition edit was made here.

`music/chaosx_music_track_list.html` already has rows for all four role IDs. The parent should reconcile its role 1/4 edit/hash wording with this final manifest, then perform any required final catalogue or wiring review. The settings-aware playback and event-side audio ID selection remain parent-owned.

## Files and ignored-asset note

- Tracked handoff: `docs/plans/012_africa_plans/subagent_handoffs/012_africa_super_audio_final_2026-08-09.md`.
- Event-scoped manifest: `docs/assets/012_africa/super_events/audio_final/manifest.md`.
- Archived source pages/evidence: `docs/assets/012_africa/super_events/audio_final/evidence/`.
- Archived source masters: `docs/assets/012_africa/super_events/audio_final/sources/`.
- Final evidence WAV copies: `docs/assets/012_africa/super_events/audio_final/final/`.
- `docs/assets/` is ignored by Git. Force-add the source/evidence/final archive if those binaries and HTML records are intended to be committed; the tracked handoff remains usable without staging the ignored workspace.

## Simplifications, omissions, and blockers

No source, role, or track was substituted, reused, generated, or left as a placeholder. No gameplay or registry wiring was changed. The parent still owns final review of the catalogue rows, settings-aware playback call sites, and any required force-add of the ignored binary evidence workspace.
