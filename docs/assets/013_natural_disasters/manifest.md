# Event 013 Natural Disasters asset retention manifest

Status: runtime package and source archive verified.

Audit date: 2026-07-26.

This manifest records the authoritative live files and the retained source and provenance package for Event 013.

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
| Source and processed masters | Present | `docs/assets/013_natural_disasters/` | The retained archive contains 1,035 files covering source frames, processed frames, source and processed PNGs, DDS packages, previews, build metadata, prompts, audio analysis, and the GFX handoff. |

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
- `docs/plans/013_natural_disasters_plans/013_asset_audit.md` — accepted package audit and restored archive disposition.
- `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-10_event013_static_asset_completion_handoff.md` — static identity and registration handoff.
- `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-10_event013_abnormal_animation_asset_handoff.md` — frame-sheet/static fallback handoff.
- `docs/super_events/013_natural_disasters_super_event_audio_production.md` — source, rights, edit, hash, and uniqueness evidence for the six audio tracks.

## Retention verification

The source archive was restored from the pre-cleanup Event 013 tree at commit `60853561d^` without overwriting this retention manifest. Runtime-facing DDS, GFX, GUI, localisation, and gameplay files remain unchanged by the restoration.
