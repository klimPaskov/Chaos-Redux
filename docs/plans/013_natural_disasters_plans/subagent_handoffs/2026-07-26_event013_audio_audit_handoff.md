# Event 013 audio package audit handoff

Date: 2026-07-26

Subagent: `chaosx_super_event_audio_researcher`

Skill used: `chaos-redux-super-events` (audio research and validation sections)

## Scope and disposition

This audit covered the Event 013 audio source archive, six event-scoped OGG/WAV pairs, the Event 013 audio manifest, the permanent super-event audio production record, and the narrow audio-registration crosswalk needed for runtime handoff. No shared sound or music definition, event script, gameplay file, localisation file, GFX file, GUI file, or UI file was edited. Final media files were not changed because the existing derivatives passed the current metadata and hash checks.

## Final Event 013 media

The six completed super-events remain mapped to UI slots 67-72 and audio IDs 37-42. Every final OGG and WAV is stereo, 44.1 kHz, one-shot material between 110 and 118 seconds. The exact source paths, source SHA-256 values, final hashes, wrapper names, and representative station song IDs are recorded in `docs/super_events/013_natural_disasters_super_event_audio_production.md` and `docs/assets/013_natural_disasters/audio_manifest.md`.

| Audio ID | Role | Final duration | Final OGG SHA-256 | Final WAV SHA-256 | Source archive file |
| ---: | --- | ---: | --- | --- | --- |
| 37 | No Firm Ground | 118 s | `189AF2FD28DEFD122CDF80CA0CCBF34317268148B3379C0BEE382285F17346A8` | `1D527BAD4BC93D77AC4265D4791D3B8ADABBA88C38C745F9A7623D554B6B7CFF` | `audio_source/earth_rupture_grieg_mountain_king_source.flac` |
| 38 | Ash at Noon | 115 s | `3744B32D01E4F6DA4660ECCC556A35FD871855CDA28F4CF0C84AB00C01883A84` | `5C0669A5E5700C9F8A14F5E691AB721A683EAF4C360A5487A78CDD2D48FCD7B3` | `audio_source/massive_eruption_pathetique_iv_source.ogg` |
| 39 | The Burning Firmament | 118 s | `560106A9D5490EBD11903BD420A2988E923B83033E168F6639F930D175A10D4B` | `D6332C56AD1604FDFA418B7EEB7711B44F91CC5877A7289CB9F77E53EA606F06` | `audio_source/skyfall_mahler_2_v_source.ogg` |
| 40 | The Fretful Elements | 115 s | `4E6C3AFAC403CD7AA2B6257CD83F0AD85AA951FEA2D6A3A08C0A1C3B7D0DC289` | `1CF8B7F4051F730041FDB9A2CE3184DC8C4B318696F82F7072CC9C6865AD8399` | `audio_source/storm_corridor_william_tell_source.mp3` |
| 41 | Old Stories Cease to Be Incredible | 110 s | `87F058595719F13F52799AFBC3C6410E807784AD96B1D52FEB684A5DB7E45939` | `513AD867D5E457D4DFEC77BC5542CEC451C2490DA878B90F6975BA829773DA58` | `audio_source/abnormal_disaster_age_coriolan_source.flac` |
| 42 | Below the Stone | 115 s | `E3077C188F5F06F563311CFC7C4B2DF21A55729D7E42A5B103AD8E1AEB88228F` | `0426957E0DD2832C0A97DA0A98E3E76A39F08C90F78492D509022128CDF344E9` | `audio_source/delayed_tsunami_hebrides_source.flac` |

## Rights and provenance

The canonical Commons pages were re-opened on 2026-07-26. IDs 37, 38, 39, 41, and 42 have public-domain compositions and recording pages that state worldwide public-domain or CC0/unrestricted-use terms. ID 40's Commons page identifies the Marine Corps recording as a U.S. federal-government work made in official duties and marks it public domain in the United States; it is not a worldwide CC0 dedication. The preserved ID 40 source is the archived official-site MP3 whose local SHA-256 is recorded above; the Commons page and archived upstream URL are both retained in the production record. Courtesy attribution is documented even where the stated license does not require it.

The superseded ID 37 Egmont source remains in the archive for collision history only. It is not referenced by any live final path and must not be treated as the selected track.

## Uniqueness validation

The current repository has 56 `music/**/super_event_*.ogg` files and 56 `sound/**/super_event_*.wav` files. A SHA-256 grouping pass found no exact duplicate in either format, and each Event 013 file has zero same-hash matches outside its own path. The archived minimum-offset Chromaprint comparison covers the harder OGG/WAV alternate-encoding case: the superseded ID 37/Soviet14 pair scored `0.993730-0.994434`, while final Event 013 maxima against the registered non-Event-013 catalogue were `0.572875-0.596505`. No final Event 013 cue remains in the confirmed reuse cluster.

## Runtime wiring handoff

The shared registration audit confirms, without editing those files, that each ID has six music variants (`chaosx_super_event_<id>_0_5` through `_3_0`), one representative station entry (`chaosx_super_event_<id>_1_5`), one Event013-specific raw sound wrapper, and six sound-effect variants (`chaosx_super_event_<id>_sound_0_5` through `_3_0`). The raw wrappers point to the matching WAV stems, and the music variants point to the matching OGG stems. The parent implementation owns the final event-side setter and `global.current_super_event_audio_id` call-chain check; the production record states that the common `play_current_super_event_audio` helper is used for settings-aware playback.

## Soviet Collapse cleanup disposition

The clearly unreferenced audio set already removed from the accepted scope is IDs 16 and 19-27: 20 files consisting of the matching OGG/WAV stems `super_event_16_northern_signals_break`, `super_event_19_map_larger_than_union`, `super_event_20_steppe_beyond_history`, `super_event_21_corridors_decide`, `super_event_22_bread_state`, `super_event_23_league_of_equal_republics`, `super_event_24_steppe_federation`, `super_event_25_baltic_league`, `super_event_26_caucasus_league`, and `super_event_27_eastern_buffer_coalition` under `music/005_soviet_collapse/` and `sound/005_soviet_collapse/`. The current narrow scan finds no remaining media, station entry, sound registration, or HTML catalogue row for those IDs. IDs 14, 15, 17, and 18 remain present; ID 17 is intentionally not deleted because its gameplay helper caller was outside this audio-only audit boundary.

## Files changed by this audit

- `docs/super_events/013_natural_disasters_super_event_audio_production.md`
- `docs/assets/013_natural_disasters/audio_manifest.md`
- `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-26_event013_audio_audit_handoff.md`

## Remaining risks

- ID 40 is clearly documented as a U.S. federal public-domain recording on the Commons page, but the grant is jurisdiction-specific rather than an affirmative worldwide CC0 license. Replacing it is only necessary if the project adopts a worldwide-license-only policy.
- This subagent did not run the game or inspect gameplay setter call chains; the parent owns live-engine/runtime acceptance. The audio registration and settings-helper handoff is complete at the narrow audio boundary.
- The original research snapshot intentionally retains historical “not acquired/not wired” blocker text. Its closure banner points to the permanent production record and this audit handoff as the current source of truth.
