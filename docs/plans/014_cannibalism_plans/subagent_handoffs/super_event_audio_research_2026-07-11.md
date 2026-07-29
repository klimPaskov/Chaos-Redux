# Event 014 super-event audio subagent handoff

## Disposition

Audio research and production are complete for all four requested Event 014 roles. Four unique source recordings were acquired from authoritative Wikimedia Commons file pages, their published SHA-1 values were verified locally, and final WAV derivatives were produced.

The detailed rights record, cue rationale, hashes, attribution, and rejection log live in:

- `docs/super_events/014_cannibalism/audio_research.md`

This subagent did not edit sound definitions, sound definitions, event script, scripted localisation, ordinary localisation, GUI, GFX, spreadsheets, or the music track list. The parent agent owns final registration and wiring.

## Final identifier map

| Role | Proposed display/audio ID | Final WAV | Final WAV | Stable underlying sound ID |
| --- | ---: | --- | --- | --- |
| Hannibal reveal | `49` | `sound/014_cannibalism/super_event_49_hannibal_reveal.wav` | `sound/014_cannibalism/super_event_49_hannibal_reveal.wav` | `chaosx_super_event_cannibalism_hannibal_reveal_track` |
| Ordinary Hannibal world-end | `50` | `sound/014_cannibalism/super_event_50_hannibal_world_end.wav` | `sound/014_cannibalism/super_event_50_hannibal_world_end.wav` | `chaosx_super_event_cannibalism_hannibal_world_end_track` |
| Wendigo Hannibal world-end | `53` | `sound/014_cannibalism/super_event_53_wendigo_hannibal_world_end.wav` | `sound/014_cannibalism/super_event_53_wendigo_hannibal_world_end.wav` | `chaosx_super_event_cannibalism_wendigo_world_end_track` |
| Eligible global defeat aftermath | `52` | `sound/014_cannibalism/super_event_52_global_defeat_aftermath.wav` | `sound/014_cannibalism/super_event_52_global_defeat_aftermath.wav` | `chaosx_super_event_cannibalism_global_defeat_aftermath_track` |

ID `51` was rejected after the repository explorer found the Holy Realm's `Mandala of Nations` already using that visible super-event slot. The Wendigo package was renamed to `53`. At the final handoff check, `49`, `50`, `52`, and `53` had no existing audio-helper or visible-super-event text references. The live audio helper catalogue reached `48`. The parent must repeat this check immediately before editing shared registries.

## Selected source and rights map

### ID 49 - Hannibal reveal

- Selection: Saint-Saëns, `Danse macabre, Op. 40`; Philadelphia Symphony Orchestra, Leopold Stokowski; 29 April 1925.
- Composition rights: public domain; Saint-Saëns died in 1921 and the work dates to 1874.
- Recording rights: Commons marks the pre-1926 publication public domain in the United States under the Classics Protection and Access Act; the 1925 publication is also beyond the European 70-year neighbouring-rights term.
- Source page: <https://commons.wikimedia.org/wiki/File:PhiladelphiaSymphonyOrchestra-DanseMacabre.ogg>
- Preserved source: `docs/assets/014_cannibalism/source_audio/hannibal_reveal_danse_macabre_stokowski_1925_source.ogg`
- Source SHA-1: `66aaedc1e25a0bfbbcc010397145f528d9184b1a`
- Source SHA-256: `5da52fa63c374fa3744886548aa74786128cdd4760b976194b22f22f30c69820`

### ID 50 - ordinary Hannibal world-end

- Selection: Wagner, `Siegfried's Funeral March and Finale`; United States Marine Band, Col. John R. Bourgeois; 8-11 December 1981.
- Composition rights: public domain; Wagner died in 1883.
- Recording rights: Commons separately marks the official U.S. Marine Band recording public domain as a U.S. federal-government work.
- Jurisdiction note: this is a U.S.-federal public-domain basis, not a worldwide CC0 dedication. It matches the repository's established treatment of official U.S. federal band recordings.
- Source page: <https://commons.wikimedia.org/wiki/File:Siegfrieds_funeral_march_and_finale.ogg>
- Preserved source: `docs/assets/014_cannibalism/source_audio/hannibal_world_end_siegfried_funeral_march_us_marine_band_source.ogg`
- Source SHA-1: `934030f52a701bc1098926caefb4da1512d6ab72`
- Source SHA-256: `68124de4da401be0e07b2e2d637347e1a981b5cafa6ead74b5cd43f6becc6e41`

### ID 53 - Wendigo Hannibal world-end

- Selection: Grieg, `Peer Gynt Suite No. 1 - II. The Death of Aase`; Musopen Symphony; 2012.
- Composition rights: public domain; Grieg died in 1907.
- Recording rights: Commons states that Musopen released it to the public domain worldwide and grants unconditional use where a waiver is not legally possible.
- Source page: <https://commons.wikimedia.org/wiki/File:Grieg_-_Peer_Gynt_Suite_No._1,_Op._46_-_II._The_Death_of_Aase_(Musopen_Symphony).flac>
- Preserved source: `docs/assets/014_cannibalism/source_audio/wendigo_world_end_death_of_aase_musopen_symphony_source.flac`
- Source SHA-1: `b7abad25034bc4dce173af0feea99c12b4e9d419`
- Source SHA-256: `5010b1911dd02d63731c21cb6ecd7914a7cdb17acf844a6418264716ce562335`

### ID 52 - eligible global defeat aftermath

- Selection: Fauré, `Élégie, Op. 24`; Hans Goldstein, cello; Eli Kalman, piano; 3 June 2006.
- Composition rights: public domain; the work dates to 1883 and Fauré died in 1924.
- Recording rights: CC BY-SA 2.0, through the source's EFF Open Audio License / CC BY-SA 2.0 interchange statement.
- Mandatory terms: credit the performers and source, link <https://creativecommons.org/licenses/by-sa/2.0/>, state the excerpt/fade/normalization changes, and distribute the adapted WAV under CC BY-SA 2.0 or a compatible license.
- Source page: <https://commons.wikimedia.org/wiki/File:Faure_-_Elegie.ogg>
- Preserved source: `docs/assets/014_cannibalism/source_audio/global_defeat_aftermath_faure_elegie_goldstein_kalman_source.ogg`
- Source SHA-1: `6d57244d2133c2968ab96508441ed08a134f240e`
- Source SHA-256: `f4256bdccdc7d7ac0e547f571c6e8137b8de8cbdd604bada417a7cb89ab5ccc0`

## Final technical verification

All files decode, are stereo, and use exactly 44,100 Hz. OGG outputs are Vorbis; WAV outputs are signed 16-bit little-endian PCM.

| ID | OGG duration / LUFS / dBTP | WAV duration / LUFS / dBTP | OGG SHA-256 | WAV SHA-256 |
| ---: | --- | --- | --- | --- |
| 49 | `114.000 s / -17.90 / -1.71` | `114.000 s / -17.92 / -1.80` | `1f30b1126ba6d307bc6393ad3558e880325652559a10f25fdbf2dfe1a5355bde` | `13a4c3ab32f7aa1f872c7ef901e3ecdc7c792eb1a3bd2e402450a5b1a2945da8` |
| 50 | `120.000 s / -18.05 / -2.76` | `120.000 s / -18.02 / -2.77` | `96509e15bd81ecc18599cadafb7a5f1144eaa8757d6efe029d1054a898ecb595` | `cfd732f5caffcac483fa251d014565836fd976cabe4d173411b811e7e6a71192` |
| 53 | `118.000 s / -18.05 / -3.71` | `118.000 s / -18.04 / -3.71` | `0dd6b181cdf12af77b961456d4cbd622dc164b7e8e45d91657bc5fccedf92d90` | `15dc2210349bb7e4b76f4ecdc8cc7512fb4f7c8a1e7a3bdfa6bfc9f7a8177128` |
| 52 | `116.100 s / -18.04 / -1.58` | `116.001 s / -18.05 / -1.80` | `205b3d8fee98efe51ac1c00d17caa621a0e5e506d66599eec50ccab1ba03ab3b` | `cebf8acf354b0d8c29d8b3bb02218b0804ba4d49da1d535e4cc71450619bb456` |

The ID 52 OGG container reports `0.099 s` of Vorbis end padding beyond the PCM mirror. The shared musical excerpt and fade are unchanged.

The four final WAV hashes are mutually unique and do not duplicate any other OGG currently under `music/`.

## Parent-agent wiring checklist

1. Re-scan the shared tree for `49`, `50`, `52`, and `53` before changing definitions.
2. Register the four WAV files in `sound/chaosx_sound.asset` with the six settings-scaled helper variants per ID.
3. Add representative zero-chance entries to `sound/chaosx_sound.asset`.
4. Register the four WAV files and six sound-effect wrappers per ID in `sound/chaosx_sound.asset`.
5. Wire the settings-aware dispatcher and Event 014 call sites to the stable sound-track IDs listed above.
6. Keep the visual `super_event_visible` slots aligned with the accepted Event 014 text/image package; do not reuse `51`.
7. Update `music/chaosx_music_track_list.html` with composer, performer, source, rights, cue, and duration details.
8. Carry the exact CC BY-SA 2.0 attribution, license link, change notice, and share-alike statement for ID 52 into the final project attribution surface.
9. Update the final Event 014 super-event documentation, implementation report, and any manifest that records numeric IDs.

Expected helper families:

- `chaosx_super_event_49_sound_0_5` through `chaosx_super_event_49_sound_3_0` and `chaosx_super_event_49_sound_0_5` through `chaosx_super_event_49_sound_3_0`
- `chaosx_super_event_50_sound_0_5` through `chaosx_super_event_50_sound_3_0` and `chaosx_super_event_50_sound_0_5` through `chaosx_super_event_50_sound_3_0`
- `chaosx_super_event_52_sound_0_5` through `chaosx_super_event_52_sound_3_0` and `chaosx_super_event_52_sound_0_5` through `chaosx_super_event_52_sound_3_0`
- `chaosx_super_event_53_sound_0_5` through `chaosx_super_event_53_sound_3_0` and `chaosx_super_event_53_sound_0_5` through `chaosx_super_event_53_sound_3_0`

## Rejected-source note

The 1953 Louis Fourestier / Concerts Colonne recording of `Danse macabre` was removed after the source page's U.S. pre-1972-recording warning was reviewed. A `Night on Bald Mountain` candidate was also removed because the performer credit was uncertain. Neither rejected source remains in the package.

## Files created by this subagent

Documentation:

- `docs/super_events/014_cannibalism/audio_research.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/super_event_audio_research_2026-07-11.md`

Preserved sources:

- `docs/assets/014_cannibalism/source_audio/hannibal_reveal_danse_macabre_stokowski_1925_source.ogg`
- `docs/assets/014_cannibalism/source_audio/hannibal_world_end_siegfried_funeral_march_us_marine_band_source.ogg`
- `docs/assets/014_cannibalism/source_audio/wendigo_world_end_death_of_aase_musopen_symphony_source.flac`
- `docs/assets/014_cannibalism/source_audio/global_defeat_aftermath_faure_elegie_goldstein_kalman_source.ogg`

Final music:

- `sound/014_cannibalism/super_event_49_hannibal_reveal.wav`
- `sound/014_cannibalism/super_event_50_hannibal_world_end.wav`
- `sound/014_cannibalism/super_event_53_wendigo_hannibal_world_end.wav`
- `sound/014_cannibalism/super_event_52_global_defeat_aftermath.wav`

Final sound mirrors:

- `sound/014_cannibalism/super_event_49_hannibal_reveal.wav`
- `sound/014_cannibalism/super_event_50_hannibal_world_end.wav`
- `sound/014_cannibalism/super_event_53_wendigo_hannibal_world_end.wav`
- `sound/014_cannibalism/super_event_52_global_defeat_aftermath.wav`

## Blockers, simplifications, and omissions

There are no audio-production or licensing blockers under the recorded repository policy. All four requested roles are complete, unique, and packaged. No fallback, placeholder, reused track, generated cue, or rights-unclear substitute was used.

The only remaining work is the parent-owned registration and integration listed above. No gameplay or definition file was modified by this subagent.
