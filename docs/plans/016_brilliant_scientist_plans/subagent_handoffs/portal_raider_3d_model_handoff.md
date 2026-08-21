# Portal Raider 3D model production handoff

> Current documentation disposition, 2026-08-09: the Portal Raider model/entity package remains rejected and unwired after the failed semantic generation task. Portal Raider counter art is complete and wired separately through `interface/portal_raider_system.gfx`; runtime model/entity, actions, and sounds still require user-approved paid recovery. No model or whole Event 016 completion is claimed.

Status: **blocked at the semantic generation gate; package incomplete**.

The complete evidence package is at `docs/assets/shared_portal_raider_system/models_3d/portal_raider/`. The single authorized legacy Meshy task `019fe7dc-382e-7dc2-a7aa-8d57ff8d3d89` technically succeeded and consumed 30 credits, but the generated model omitted the mandatory ray rifle. Multi-view Blender evidence confirms the omission. The job permits zero extra recovery credits and zero extra paid attempts, so no further generation, remesh, retexture, rig, conversion, or animation call was made.

## Completed evidence and preparation

- dependency, route, Blender 5.1.2, adapter 1.2.2, and io_pdx_mesh 0.91.0 verification
- exactly one immutable ImageGen reference and provenance record
- immediate GLB/FBX provider download with checksums and complete request/response/task lineage
- protected Blender source, working checkpoints, six usable inspection views, topology/scale/material/rig report, and vanilla infantry calibration
- legally reusable sourced audio originals and mechanically normalized mono 44.1 kHz PCM candidates for selection, six movement variations, idle electrical, ray attack, impact, portal arrival, and death
- installed-vanilla large/small counter definition and DDS inspection, decoded evidence, sampled green palette, and exact icon-artist brief
- runtime requirement crosswalk and explicit blockers

## Provider and scale facts

- starting balance 314; estimated generation 20; consumed 30; recorded final balance 284
- input SHA-256 `9670EA470735AB87679741C9E6D110199E1BE15388624E480597AC4A80B733A3`
- GLB SHA-256 `C2A195A51C55AE58DEDFCC9400A6F9AC6554F64345D67D079DE86D28CCE55BC5`
- FBX SHA-256 `B952BF824884BDF5CE0A9E4AE4C631DB4CA1903FCD4BC5F91138DCDA6BC0AFBD`
- vanilla mesh `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`
- vanilla entity `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset#infantry_entity`
- calibrated source height 7.3518242835; entity scale 0.8; effective runtime height 5.8814594268; forward `-Y`; up `+Z`

## Blocked requirements

- accepted complete geometry with one ray rifle
- packed PDX materials and DDS outputs
- humanoid armature, audited weights, and provider rig mapping
- real 24 FPS idle, move, attack, defend, support_attack, retreat, guard, wounded, death, and portal_arrival actions
- action-specific root/contact/deformation review and exact audio frame synchronization
- io_pdx_mesh `.mesh`/`.anim` export and actual reimport proof
- source-to-runtime hash synchronization
- bespoke counter art outputs from `chaosx_icon_artist`
- parent gameplay, sound, entity, GFX, and localisation wiring and live consumer validation

## Required decision

Ask the user whether to authorize one additional failure-recovery Meshy 7 generation. Do not reuse the prior planned-attempt budget. If approved, state the new credit and attempt ceiling explicitly, then resume from generation while preserving this rejected task as immutable evidence.

No unapproved fallback or simplification was used. No in-game completion is claimed.
