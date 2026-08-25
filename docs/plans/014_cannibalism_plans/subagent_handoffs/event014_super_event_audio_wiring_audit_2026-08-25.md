# Event 014 super-event audio wiring audit — 2026-08-25

## Disposition

The parent-owned Event 014 super-event audio integration is complete at the source and asset boundary. This is an integration audit, not a claim that the Event 014 goal is complete: four custom 3D unit packages remain outside the installed runtime set and live in-game validation remains user-owned.

## Accepted role and ID map

| Role | Visible slot and audio id | Base sound definition | Final WAV |
| --- | ---: | --- | --- |
| Hannibal Lecter public reveal | `49` | `chaosx_super_event_cannibalism_hannibal_reveal_track` | `sound/014_cannibalism/super_event_49_hannibal_reveal.wav` |
| Ordinary Hannibal Lecter world end | `50` | `chaosx_super_event_cannibalism_hannibal_world_end_track` | `sound/014_cannibalism/super_event_50_hannibal_world_end.wav` |
| Eligible global defeat aftermath | `52` | `chaosx_super_event_cannibalism_global_defeat_aftermath_track` | `sound/014_cannibalism/super_event_52_global_defeat_aftermath.wav` |
| Wendigo Hannibal Lecter world end | `53` | `chaosx_super_event_cannibalism_wendigo_world_end_track` | `sound/014_cannibalism/super_event_53_wendigo_hannibal_world_end.wav` |

ID `51` remains outside Event 014 because it is assigned to the Holy Realm's existing visible super-event.

## Source and runtime evidence

- `sound/chaosx_sound.asset` contains one base `sound` definition for each accepted track and six settings-volume wrappers per id (`0_5`, `1_0`, `1_5`, `2_0`, `2_5`, `3_0`). Each wrapper points to the matching base track and uses `max_audible = 1` with `max_audible_behaviour = fail`.
- `common/script_constants/014_cannibalism_constants.txt` maps the reveal, ordinary world-end, defeat aftermath, and Wendigo world-end roles to `49`, `50`, `52`, and `53`.
- `common/scripted_effects/014_cannibalism_effects.txt` sets `global.current_super_event_audio_id`, sets the matching `super_event_visible` value for fourteen days, and calls the existing settings-aware `play_current_super_event_audio` helper for human-player countries in each of the four guarded emitters.
- The helper in `common/scripted_effects/chaosx_settings_effects.txt` delegates to `play_current_super_event_sound` and then to the dynamic volume-token wrapper, so Event 014 does not bypass the settings volume control.
- Reveal requires `cannibalism_reveal_complete` and is one-shot. The ordinary terminal requires the ordinary world-end flag and shared `world_end`; the Wendigo terminal requires the Wendigo world-end flag and shared `world_end`; the defeat aftermath requires recorded eligibility, completed reveal, and no shared `world_end`. Each emitter has its own emitted guard.
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` maps all four visible slots to title, quote, remark, description, and image getters. `interface/chaosx_super_events.gfx` registers four distinct Event 014 images.
- `music/chaosx_music_track_list.html` contains rows for all four final WAVs with title, composer/performer, source, rights, duration, and super-event id. The source and licensing record is `docs/super_events/014_cannibalism/audio_research.md`.

## WAV verification

FFprobe on 2026-08-25 reported `pcm_s16le`, `44100 Hz`, two channels, and these durations: ID 49 `114.000 s`, ID 50 `120.000 s`, ID 52 `116.001 s`, and ID 53 `118.000 s`. All are distinct musical recordings, not generated tones, drones, or placeholder cues. ID 52 retains its documented CC BY-SA 2.0 attribution and share-alike requirement.

## Remaining boundary

No audio-definition or super-event dispatch patch is required by this audit. Remaining Event 014 blockers are the documented Bone Riders compound horse/rider route, Island Reavers Meshy HTTP 402, Scavenger Warband user-review/action/audio gate, Network Cadre provider-action gate, and user-owned live runtime validation. Meshy balance was `10` credits on this continuation, below the paid generation/action work required to close those packages.
