# Rejected Meshy rig `01a03317`

Status: rejected in full. No checkpoint, included action, or processed export derived from this rig is approved for runtime use.

## Lineage and cost

- Accepted input geometry task: `01a02a86-de73-734c-ab7d-58447aa331ae`.
- Immutable accepted input GLB: `provider/downloads/source_authorized_original_pose_01a02a86.glb`.
- Accepted input SHA-256: `285F8CB50975AB094CE846773A46FDE87CB8F0098C17AA9644A987D1B1CC28FD`.
- Rejected rig task: `01a03317-0d73-7a59-b336-2a9ab1bc2c0d`.
- Provider result: succeeded technically, rejected by geometry and component QA.
- Credits consumed: 5.
- Rigged GLB SHA-256: `CB55C4931AEAB689192C61705B7BDA650822136DE385FA490EC5BCC85BCD7812`.

## Raw-provider diagnosis

The failure exists in the protected provider rig GLB before normalization, topology reduction, action processing, or PDX export. Adapter inspection request `034cf8288f2345d885ade9c74c819762` opened `blender/source/cannibal_feast_guard_rigged_01a03317_provider_source.blend` and rendered the raw provider scene.

The provider artifact contains a separate mesh named `Icosphere`. It has 42 vertices, no vertex groups, and no armature modifier. Its raw dimensions are approximately `1.902 x 2.000 x 2.000`, large enough to engulf the character's lower body. This object is already visible as the catastrophic sphere/blob in the raw front and three-quarter views. The weighted character mesh `char1` is separate and has 24 bone groups, so the blob is not caused by Blender weight normalization or by an animation action.

The provider rig also fails the locked component requirement: both oversized cleavers from the accepted original-pose geometry are not preserved as two clearly readable weapons in the raw rigged result.

## Evidence

- `blender/previews/cannibal_feast_guard_rigged_raw_01a03317_front.png`
- `blender/previews/cannibal_feast_guard_rigged_raw_01a03317_side.png`
- `blender/previews/cannibal_feast_guard_rigged_raw_01a03317_rear.png`
- `blender/previews/cannibal_feast_guard_rigged_raw_01a03317_three_quarter.png`
- `blender/previews/cannibal_feast_guard_rigged_01a03317_front.png`
- `blender/reports/cannibal_feast_guard_rigged_01a03317_prepare.json`
- `provider/downloads/rigged_01a03317.glb`
- `provider/downloads/rigged_01a03317.glb.manifest.json`

## Rejection boundary

The standard numbered Blender checkpoints written during the rejected preparation pass are not approved checkpoints. No action may be imported, retargeted, or exported from this skeleton. The included walk and run artifacts are retained only as paid-call evidence and are not accepted animation sources.

No local deletion of the sphere, weapon reconstruction, or local replacement rig is permitted as a substitute. Recovery must begin again from the immutable accepted original-pose GLB and must pass raw multi-angle provider inspection with both cleavers intact before Blender processing.
