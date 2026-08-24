# Rejected Meshy signed-URL recovery rig `01a0332e`

Status: rejected in full. No checkpoint, included action, or processed export derived from this rig is approved for runtime use.

## Lineage and cost

- Accepted input geometry task: `01a02a86-de73-734c-ab7d-58447aa331ae`.
- Immutable accepted input GLB: `provider/downloads/source_authorized_original_pose_01a02a86.glb`.
- Accepted input SHA-256: `285F8CB50975AB094CE846773A46FDE87CB8F0098C17AA9644A987D1B1CC28FD`.
- Recovery input mode: fresh official `assets.meshy.ai` signed GLB URL obtained from the accepted task and passed to `meshy_rig` only in memory.
- Rejected recovery rig task: `01a0332e-173b-7b4d-8f3e-2eb4d027323f`.
- Provider result: succeeded technically in 43 seconds after 5 status polls, rejected by raw geometry and component QA.
- Credits consumed: 5.
- Rigged GLB SHA-256: `EBBC3E4ADA4B5160487993CD3CEAE11D1CC1C1762931ED99C5F194F10FCC7982`.
- Rigged FBX SHA-256: `C741BED9A1A290E6924E37B046AFA3757CFA4C35895599F0EDB32A2D49120159`.

## Raw-provider diagnosis

Adapter inspection request `f537ab5e3f2c476199a17708f5c60e2d` opened the protected provider source checkpoint `blender/source/cannibal_feast_guard_rigged_01a0332e_provider_source.blend` before accepting any processed checkpoint.

The signed-URL recovery reproduces the first rejected rig defect exactly. The raw provider scene contains a standalone mesh named `Icosphere` with 42 vertices, zero vertex groups, zero armature modifiers, and dimensions approximately `1.902 x 2.000 x 2.000`. The raw front preview shows the character's upper torso perched behind this giant sphere. The weighted `char1` mesh is separate and has 24 bone groups with no zero-weight vertices. The catastrophic shape therefore exists in the provider artifact and is not caused by Blender normalization, topology repair, PDX conversion, or action deformation.

The raw result also fails the locked component requirement because both oversized cleavers are absent or unreadable. The scene statistics match the first rejected task's two-mesh structure, demonstrating a repeat provider incompatibility rather than task-ID input mode or a Blender import anomaly.

## Evidence

- `blender/previews/cannibal_feast_guard_rigged_raw_01a0332e_front.png`
- `blender/previews/cannibal_feast_guard_rigged_raw_01a0332e_left.png`
- `blender/previews/cannibal_feast_guard_rigged_raw_01a0332e_rear.png`
- `blender/previews/cannibal_feast_guard_rigged_raw_01a0332e_right.png`
- `blender/previews/cannibal_feast_guard_rigged_raw_01a0332e_three_quarter.png`
- `blender/previews/cannibal_feast_guard_rigged_raw_01a0332e_top.png`
- `blender/previews/cannibal_feast_guard_rigged_raw_01a0332e_underside.png`
- `blender/reports/cannibal_feast_guard_rigged_01a0332e_prepare.json`
- `provider/downloads/rigged_01a0332e.glb`
- `provider/downloads/rigged_01a0332e.glb.manifest.json`
- `provider/downloads/rigged_01a0332e.fbx`
- `provider/downloads/rigged_01a0332e.fbx.manifest.json`

## Included walk/run lineage

The provider's free walk and run GLB, FBX, and armature artifacts were downloaded and checksummed immediately. They are retained only as provider-call evidence because their owning rig failed raw geometry and component QA. They are not accepted final action sources and were not advanced to Blender action processing.

## Recovery boundary

The accepted original-pose GLB has now failed Meshy rigging twice as a provider input: once by `input_task_id` and once by fresh official signed `model_url`. A third identical rig attempt is forbidden. No animation credits were spent on either rejected skeleton.

The package cannot proceed without an explicitly approved changed recovery design. Safe candidates are a newly accepted rig-suitable geometry that visibly retains both cleavers before rigging, or an explicitly approved local skeleton-preparation and professional motion-source transfer plan that still supplies substantive distinct external skeletal motion for every final role. No local sphere deletion, weapon reconstruction, static action, transform-only action, semantic alias, or locally authored replacement motion is approved.
