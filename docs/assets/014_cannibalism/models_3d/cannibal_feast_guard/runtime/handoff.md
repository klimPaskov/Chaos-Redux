# Cannibal Feast Guard runtime handoff

Package status: complete; parent runtime wiring and live consumer validation pending.

## Proposed runtime paths

Copy from this package into `gfx/models/units/014_cannibalism/cannibal_feast_guard/` without changing bytes:

- `export/mesh/cannibal_feast_guard.mesh`
- all eight `export/anim/cannibal_feast_guard_*.anim`
- `textures/dds/texture_0.dds`
- `textures/dds/texture_specular.dds`
- `textures/dds/texture_normal.dds`

Proposed stable identifiers:

- entity: `cannibal_feast_guard_entity`
- mesh object/runtime stem: `cannibal_feast_guard`
- actions: `cannibal_feast_guard_idle`, `cannibal_feast_guard_move`, `cannibal_feast_guard_attack`, `cannibal_feast_guard_defend`, `cannibal_feast_guard_support_attack`, `cannibal_feast_guard_retreat`, `cannibal_feast_guard_training`, `cannibal_feast_guard_death`

Use installed `gfx/entities/units_infantry.asset#infantry_rifle_entity` as the entity precedent and apply scale `0.8` exactly once. Source geometry was calibrated against `gfx/models/units/western_european_infantry.mesh#polySurface106` at height `7.351824797689915`, forward `-Y`, up `+Z`.

## Action policy and sound sync

- Loop idle, move, retreat, and training. Treat attack, support attack, and death as one-shots; hold death final pose. Defend may be held or consumer-controlled.
- Bind the sourced movement WAV at move/retreat footfall phases near frames 1 and 22.
- Bind the sourced weapon swish near attack frames 28 and 56 and impact near frame 84. For support attack, use swish near frame 94 and impact near frame 140.
- Bind the death vocal across frames 14–42. Selection/acknowledgement remains a voice consumer rather than an honest per-subunit sound.
- Audio provenance, licences, hashes, and transformations are in `evidence/audio_sources/ffprobe_and_hash_receipt.json`.

## Counter consumers

Register the existing bespoke counter files and tokens documented by `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_cannibal_counter_art_handoff.md`:

- `GFX_unit_cannibal_feast_guard_icon_medium`
- `GFX_unit_cannibal_feast_guard_icon_medium_white`
- `GFX_unit_cannibal_feast_guard_icon_small`

Parent owns file copies, `.asset`/entity definitions, GFX and sound definitions, action binding, live consumer inspection, and in-game validation. This package does not claim those steps.
