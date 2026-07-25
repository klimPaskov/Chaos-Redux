# Event 013 Natural Disasters asset retention manifest

Status: runtime package verified; source archive incomplete.

Audit date: 2026-07-26.

This manifest records the authoritative live files and the remaining provenance gap for Event 013. It does not claim that deleted source masters have been restored.

## Retention state

| Package | Status | Authoritative location | Notes |
| --- | --- | --- | --- |
| Report art | Present | `gfx/event_pictures/013_natural_disasters/` | 25 report textures are registered by `interface/013_natural_disasters.gfx`. |
| News art | Present | `gfx/event_pictures/013_natural_disasters/` | 25 news textures are registered by `interface/013_natural_disasters.gfx`. |
| Decision and category art | Present | `gfx/interface/decisions/013_natural_disasters/` | Disaster-specific category pictures and response icons are registered by `interface/013_natural_disasters.gfx`. |
| Idea art | Present | `gfx/interface/ideas/013_natural_disasters/` | Event 013 aftermath and recovery ideas are registered by the live interface definitions. |
| Abnormal GUI art | Present | `gfx/interface/013_natural_disasters/` | Static panel, marker, badge, and recovery-progress sprites are live. |
| Abnormal frame animation | Present | `gfx/interface/animated/013_natural_disasters/` | Every wired animated sprite has a paired static fallback; GIFs are review-only and are not referenced by gameplay. |
| Super-event images | Present | `gfx/super_events/013_natural_disasters/` | Six slots are registered in `interface/chaosx_super_events.gfx`. |
| Achievement icons | Present | `gfx/achievements/` | Event 013 achievement states are registered in `interface/chaosx_achievements.gfx`. |
| Super-event audio | Present | `music/013_natural_disasters/`, `sound/013_natural_disasters/` | Six OGG/WAV pairs are registered for slots 67-72; provenance and uniqueness are documented in `docs/super_events/013_natural_disasters_super_event_audio_production.md`. |
| Source and processed masters | Missing | `docs/assets/013_natural_disasters/` | The former 1,035-file archive was removed by commit `60853561d`; source frames, source PNGs, previews, build metadata, and the former GFX handoff are not present in the current tree. |

## Live animation pairs

The accepted Event 013 GUI uses frame-sheet animation with static fallbacks. The live pairs are registered in `interface/013_natural_disasters.gfx` and reside under `gfx/interface/animated/013_natural_disasters/`:

- `natural_disaster_warning_pulse`
- `natural_disaster_tsunami_countdown`
- `natural_disaster_storm_corridor_track`
- `natural_disaster_skyfall_alarm`
- `natural_disaster_eruption_ashfall`
- `013_tsunami_path_ribbon`
- `013_storm_corridor_path_ribbon`
- `013_rupture_wave_overlay`
- `013_meteor_rain_overlay`
- `013_impact_pulse_overlay`
- `013_disaster_card_frame_warning`
- `013_disaster_card_frame_impact`
- `013_ash_plume_overlay`

## Provenance and handoff references

- `docs/events/013_natural_disasters.md` — runtime wiring and player-facing asset ownership.
- `docs/plans/013_natural_disasters_plans/013_asset_audit.md` — accepted package audit and unresolved archive note.
- `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-10_event013_static_asset_completion_handoff.md` — static identity and registration handoff.
- `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-10_event013_abnormal_animation_asset_handoff.md` — frame-sheet/static fallback handoff.
- `docs/super_events/013_natural_disasters_super_event_audio_production.md` — source, rights, edit, hash, and uniqueness evidence for the six audio tracks.

## Required closure action

The source archive remains an explicit blocker for full asset-provenance completion. Restore the deleted archive or obtain an approved repository-wide retention decision before changing this manifest's source-master status to `Present`.
