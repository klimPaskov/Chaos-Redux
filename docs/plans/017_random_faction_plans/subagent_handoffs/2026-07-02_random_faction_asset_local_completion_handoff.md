# Event 017 Random faction asset local completion handoff

Date: 2026-07-02
Owner: parent implementation pass after Event 17 asset subagent stall/shutdown

## Scope

The Event 17 asset subagent did not land final runtime DDS files. The parent pass completed the asset package locally from generated source art and partial source-output context, then wired the runtime sprite surfaces.

## Files and surfaces

- Runtime sprite registry: `interface/017_random_faction.gfx`
- Achievement sprite registry: `interface/chaosx_achievements.gfx`
- Asset manifest: `docs/assets/017_random_faction/manifest.md`
- GFX handoff: `docs/assets/017_random_faction/gfx_handoff.md`
- Processing tool: `docs/assets/017_random_faction/_tooling/process_random_faction_assets.py`
- Runtime DDS outputs:
  - `gfx/event_pictures/017_random_faction/*.dds`
  - `gfx/interface/decisions/017_random_faction/*.dds`
  - `gfx/interface/ideas/017_random_faction/*.dds`
  - `gfx/interface/animated/017_random_faction/*.dds`
  - `gfx/achievements/017_random_faction*.dds`

## Animated surfaces

- `GFX_random_faction_bloc_pressure_seal_animated` is visible on `random_faction_convene_neutrality_council`.
- `GFX_random_faction_border_warning_animated` is visible on `random_faction_reinforce_border_posts` and `random_faction_guarantee_corridor_mission`.
- Both animations use separate generated source-frame states assembled into 8-frame sheets; final animation is not transform-only.

## Validation

- Runtime DDS dimensions are recorded in `docs/assets/017_random_faction/gfx_handoff.md`.
- The processed package includes static contact sheets, animation contact sheets, GIF previews, source frames, frame sheets, and runtime DDS copies.
- No blocked runtime asset path remains in the manifest or GFX handoff.

## Remaining risk

- No live in-game animation playback capture was produced in this pass. Static registration, runtime DDS existence, dimensions, and decision icon references were checked by file evidence.
