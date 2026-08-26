# Alien infantry V13 runtime handoff

Status: **the accepted Meshy V13 provider package and its static engine-facing runtime registrations are present; effect-locator binding, strict audio-role coverage, MCP/live consumer evidence, and live in-game acceptance remain open**.

This handoff is the runtime companion to `attempts/v13_firearm_preset/final_manifest.md` and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/alien_infantry_v13_firearm_preset_handoff_2026-08-26.md`. The provider package was routed through `chaosx_3d_model_pipeline`; provider evidence, static runtime registration, and live consumer acceptance are separate gates.

## Current provider evidence

Meshy 7 generation `01a03dc3-905a-7d02-aba6-05500f877b97` retained the integrated right-hand pistol, remesh `01a03dc9-8951-79ad-bc08-ae94ad607dfe` supplied the accepted geometry route, and rig `01a03dcf-f0ba-7b67-b769-5a2678b03a40` supplied the 24-bone rig. Seven distinct Meshy preset actions were exported through io_pdx_mesh and reimported from their actual `.anim` bytes with the final `.mesh`.

The final provider evidence is a 59,999-triangle mesh, seven genuine actions, and three packed DDS maps; exact task IDs, hashes, reimport requests, and proof artifacts remain in `attempts/v13_firearm_preset/final_manifest.md` and `provider_lineage.json`.

The accepted action roles are `idle` action 0, `move` action 692, `laser_attack` action 223, `defend` action 89, `support_attack` action 234, `retreat` action 685, and `death` action 183. No role is represented by a semantic alias, transform-only clip, manually attached firearm, or Blender-authored replacement motion.

## Promoted engine-facing files

Commit `0e724fb8a` promoted byte-identical provider exports into the engine-facing runtime tree:

- `gfx/models/units/alien_infantry/alien_infantry.mesh`.
- `gfx/models/units/alien_infantry/alien_infantry_idle.anim`.
- `gfx/models/units/alien_infantry/alien_infantry_move.anim`.
- `gfx/models/units/alien_infantry/alien_infantry_laser_attack.anim`.
- `gfx/models/units/alien_infantry/alien_infantry_defend.anim`.
- `gfx/models/units/alien_infantry/alien_infantry_support_attack.anim`.
- `gfx/models/units/alien_infantry/alien_infantry_retreat.anim`.
- `gfx/models/units/alien_infantry/alien_infantry_death.anim`.
- `gfx/models/units/alien_infantry/alien_infantry_diffuse.dds`.
- `gfx/models/units/alien_infantry/alien_infantry_normal.dds`.
- `gfx/models/units/alien_infantry/alien_infantry_specular.dds`.
- `gfx/entities/alien_infantry.gfx`.
- `gfx/entities/alien_infantry.asset`.
- `gfx/models/units/alien_infantry/animation_alien_infantry.asset`.

The static entity registration is `alien_infantry_entity` with `alien_infantry_mesh` at scale `0.8`, and it exposes distinct idle, move, attack, defend, support-attack, retreat, training, wounded, and death states. Training uses the registered idle action and wounded uses the registered defend action because the subunit is not trainable and no separate provider clips were requested.

The static entity also references `alien_infantry_laser_fire`, `alien_infantry_move`, `alien_infantry_idle`, and `alien_infantry_death` at the current handoff timings. These references prove source-level registration only; they do not prove positional playback or live in-game acceptance.

The source/provider evidence remains under `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/`, while the runtime consumers point to the promoted `gfx` and `sound` paths rather than to the evidence tree.

## Effect-point and audio boundary

No supported Meshy or Blender-authored muzzle locator exists. The locked adapter exposes no locator-create operation, the rig has no muzzle bone, and the fused cyan muzzle cap is visual evidence only; no origin, hand point, or inferred locator may substitute for the missing authored point.

`alien_laser_muzzle_particle` and `alien_laser_muzzle_flash` are registered definitions, but they remain intentionally unbound until a provider- or adapter-supported runtime effect point is available.

Sourced CC0 audio evidence and static definitions cover laser discharge, movement, idle, and death only. Per-subunit selection and acknowledgement remain blocked by tag-wide vanilla consumers, and no defensible sourced impact or special-action candidate was accepted; no synthesized or placeholder audio is used.

The current visual timing crosswalk is laser attack frame 145 / 4.8000 seconds, support attack frame 50 / 1.6333 seconds, move contacts at frames 1 and 19, retreat contacts at frames 1 and 16, idle one-shot on state entry, and death onset at frame 1 with a future impact candidate near frame 80 / 2.6333 seconds. These timings are handoff evidence and static event references, not proof of positional playback or a completed effect/audio binding.

## Parent-owned acceptance

The parent owns final review of the promoted entity, GFX, animation, sound, effect-point, and gameplay consumers, any remaining locator/effect binding, strict audio-role decisions, and live in-game validation.

No live game acceptance is claimed, and no HOI4 MCP render or consumer comparison replaces that evidence. The promotion handoff records the bounded MCP timeout and the remaining live-consumer limitation.

Historical V8, V10, V11, KayKit, and Quaternius records remain retained as evidence-only documents and must not trigger a new production route; the V13 manifest and promotion handoff are the current package authority.

## 2026-08-26 revalidation note

The locked Meshy route reconfirmed the accepted generation, remesh, rig, and all seven preset-action tasks as `SUCCEEDED`. The locked Blender adapter reimported the final `.mesh` with each final `.anim` again, and the restored provider FBX hashes match all seven action-provenance records. Firearm and death evidence still passes; the unsupported muzzle locator/effect binding, strict audio-role gaps, and parent-owned live consumer acceptance remain unchanged.
