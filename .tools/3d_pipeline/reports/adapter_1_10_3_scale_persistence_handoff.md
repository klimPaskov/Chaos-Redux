# Blender HOI4 adapter 1.10.3 scale-persistence handoff

## Regression

Provider humanoid FBX actions can contain armature-object scale curves in addition to pose-bone scale curves.
The repository job profile identifies these candidates as `humanoid_unit`, while the preparation worker previously enabled humanoid scale cleanup only for the legacy `humanoid` identifier.
Normalization therefore measured the requested height while the armature scale was temporarily overridden, but a later dependency-graph evaluation restored the keyed provider scale before the checkpoint was saved.

## Resolution

The worker recognizes both humanoid identifiers and removes provider scale channels before normalization.
After the final checkpoint is saved, the worker reopens it, remeasures working world bounds, and fails closed if the persisted height differs from the requested target.
The persistence report records the reopened height, tolerance, armature world scale, and measured geometry.

## Regression coverage

The synthetic Blender regression exports and reimports an FBX with a `0.01` armature scale, keyed object and pose scale channels, a weighted mesh, a bone-parented accessory, and a non-scale action channel.
It requests a `7.3518242835` mesh height, reopens the saved preparation checkpoint, performs the real io_pdx_mesh export-scale bake, reimports the exported PDX mesh, and verifies the target height, hierarchy, weights, accessory, action preservation, identity export armature scale, and absence of scale curves.

The Event 014 package remains rejected until its owner reruns preparation from immutable provider inputs through adapter 1.10.3 and records fresh checkpoint, export, and reimport evidence.
