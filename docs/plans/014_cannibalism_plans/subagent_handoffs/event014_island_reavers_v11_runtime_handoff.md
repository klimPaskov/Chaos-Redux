# Event 014 Island Reavers v11 runtime handoff

This handoff records the accepted Island Reavers Meshy 7 and Blender HOI4 adapter package used by the parent runtime wiring. It supersedes the earlier insufficient-funds and geometry-only receipts without deleting their evidence.

## Provider lineage

- Approved designed-artwork source remains the exact parent-approved reference in `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/refs/original/meshy_input.png`.
- Meshy image-to-3d geometry task: `01a034bb-7129-716b-bc17-177ca0eb9a1a`.
- Meshy remesh task: `01a03967-eaff-72d3-a8a9-2ec3efa29a15`, succeeded at the required 300,000-face ceiling; downloaded `provider/downloads/meshy_v11_remesh_geometry.glb`, SHA-256 `B22CAE16CCBA53815D09FE5958ECF4C7154494CA058D8F1AA83907A369F5FC53`.
- Meshy rig task: `01a0396c-09fc-7026-b5b3-1210dbfa2f1c`, succeeded with provider walking/running coverage; downloaded `provider/downloads/rigged_model.fbx`, SHA-256 `2336A5D8680DC2FEB21B011B556F968A323693F35652CDBAF9F328E727FE0F7B`.
- Adapter version: `chaosx_blender_hoi4` 1.10.14 with Blender 5.1.2 and `io_pdx_mesh` loaded.

The persisted working mesh is 29,999 triangles, 24 bones, no non-manifold or degenerate faces, four-or-fewer normalized influences per vertex, and a persisted 7.3518247604 m mesh height against the read-only vanilla Western European infantry calibration. The runtime entity remains at scale `0.8`.

## Skeletal actions

All eight actions are provider-derived Meshy skeletal clips. They were imported by explicit source action name and SHA receipt, retimed from 30 FPS to 24 FPS, grounded with the adapter's per-frame root-contact policy, exported through `io_pdx_mesh`, and reimport-proven against the same mesh. No local body motion was authored and no transform-only replacement was used.

| Role | Meshy task | Source action | Runtime export | Frame span at 24 FPS |
| --- | --- | --- | --- | --- |
| idle | `01a0396e-24ee-7094-9898-c9d149dd10c7` | `CrouchLookAroundBow` | `exports/cannibal_island_reavers_idle.anim` | 0–141 |
| move | `01a03987-99c2-7466-9331-7e137e06d65b` | `Spear_Walk_inplace` | `exports/cannibal_island_reavers_move.anim` | 0–28 |
| attack | `01a0396e-2f74-709c-9d18-5be95d19d8ed` | `Archery_Shot` | `exports/cannibal_island_reavers_attack.anim` | 0–121 |
| defend | `01a0396e-3381-709d-ba5c-892f1f23fd77` | `Archery_Aim_with_Lateral_Scan` | `exports/cannibal_island_reavers_defend.anim` | 0–121 |
| support_attack | `01a0396e-37d7-709f-8aa0-b24744cf83fb` | `Archery_Shot_3` | `exports/cannibal_island_reavers_support_attack.anim` | 0–18 |
| retreat | `01a0398a-221a-7986-8b7d-e198c37f4657` | `Walk_Fight_Back_inplace` | `exports/cannibal_island_reavers_retreat.anim` | 0–43 |
| training | `01a0396e-419e-7c2b-8131-3246ccc371ef` | `Lower_Weapon_Look_Raise` | `exports/cannibal_island_reavers_training.anim` | 0–126 |
| death | `01a0396e-456a-7c2d-bb57-7df7c1dada62` | `Shot_and_Fall_Forward` | `exports/cannibal_island_reavers_death.anim` | 0–54 |

The first provider candidates for move (`01a0396e-2af5-709b-b259-33852dd5fce9`, action 524) and retreat (`01a0396e-3ccc-70a4-ad9f-3edd76ebb688`, action 545) failed the adapter's source-motion retention gate because their root-heavy source peaks transferred below ten percent. Their rejection receipts are retained in `evidence/animation_provenance/superseded_move_cautious_crouch.json` and `superseded_retreat_bow_walk.json`. The two replacement clips are still Meshy actions on the same accepted rig, not local substitutes.

The final Blender checkpoints are `blender/checkpoints/v11_runtime_sanitized.blend` and the per-role export-coordinate checkpoints `blender/checkpoints/v11_export_coordinate_<role>.blend`. Reimport proofs are recorded as `reimport_v11_<role>` under the adapter logs/reports.

## Engine-facing handoff

The parent-owned runtime files now consume the package through:

- `gfx/models/units/014_cannibalism/cannibal_island_reavers/` for the mesh, eight `.anim` files, and three DDS material maps.
- `gfx/models/units/014_cannibalism/cannibal_island_reavers/animation_cannibal_island_reavers.asset` for stable animation names.
- `gfx/entities/014_cannibalism_units.gfx` for the `cannibal_island_reavers_mesh` registration and `output_unwrapped.002` mesh stream.
- `gfx/entities/014_cannibalism_units.asset` for the idle, movement, attack, support, retreat, training, and death states with sourced Island Reavers sound effects.
- Existing three-surface bespoke counters remain the consumers `GFX_unit_cannibal_island_reavers_icon_medium`, `GFX_unit_cannibal_island_reavers_icon_medium_white`, and `GFX_unit_cannibal_island_reavers_icon_small`.

Source-derived Island Reavers audio is already installed under `sound/014_cannibalism/units/cannibal_island_reavers/` and declared in `sound/014_cannibalism_units_sound.asset`; format is 44,100 Hz mono PCM s16le. Live in-game playback and save-state consumer validation remain parent/user-owned and are not claimed by this handoff.
