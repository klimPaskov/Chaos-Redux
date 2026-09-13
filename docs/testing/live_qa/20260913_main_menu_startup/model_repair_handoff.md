# Main-menu model repairs

The parent owns the installed runtime package and its main-menu acceptance.
The original model worker was stopped when the user prohibited Astra subagents.
Its completed identity-alias checkpoint and preservation evidence were retained; the parent subsequently exported, reimported, reviewed, and installed the mesh and all seven actions without resuming that worker.

## Alien infantry

The original mesh exceeded the engine's 50-bone palette with 52 bones.
The repaired rig aliases only the two identity leaf joints `RightToeBase` and `LeftToeBase` to their corresponding feet.
The operation rejects nonidentity leaf joints and preserves the root, weapon attachment, fingers, and all remaining joints.
Across seven genuine actions, 703 samples at half-frame intervals show a maximum vertex component difference of 2.980232238769531e-7 and no retained-bone or weapon-locator matrix difference.
The actual old and new runtime mesh comparison preserves eight streams, 55,150 triangles, positions, normals, UVs, triangle indices, bounds, and material bindings; tangent differences remain below 1.8e-7.
Both objects use the same 50-bone skeleton.

The parent exported Idle, Move, LaserAttack, Defend, SupportAttack, Retreat, and Death from the repaired checkpoint and independently reimported all seven matching animations.
Existing runtime filenames, action consumers, and DDS files remain in use.
No action was replaced with a still pose or removed.

Evidence: `model_evidence/alias_operation_result.json`, `alias_scene_root_review.json`, `alias_export_mesh_result.json`, `alias_export_animation_results.json`, `alias_reimport_results.json`, `alien_runtime_preservation_check.json`, and `alien_runtime_install_receipt.json`.
Byte backups: `baseline/alien_install/`.

## Shader and texture registration

Six robot material overrides use the vanilla base shader `PdxMeshAdvanced`, allowing the engine to append its own `Skinned` suffix once.
The original double suffix caused failed shader lookup.
The six streams, 29,262 triangles, and 22-bone skeleton were preserved.
Nine DDS files with globally colliding generic names were renamed to unit-specific names with identical file bytes, and their existing GFX consumers were updated.

The parent additionally repaired embedded material filenames in 17 registered meshes, resolving 945 diffuse, normal, and specular references to the exact already-bound unit textures.
Each rewritten mesh was reopened and compared after reversing only those string substitutions in memory.
All other parsed fields, including geometry, skeleton, skinning, UVs, and shader values, were identical.
Unregistered meshes were not inferred into the runtime package.

Evidence: `model_evidence/material_override_validation.json`, `texture_rename_receipt.json`, and `embedded_texture_repair_receipt.json`.
Byte backups: `baseline/models/` and `baseline/models_embedded/`.

## Tool boundary and acceptance limits

The locked Blender adapter CLI reported version 1.10.49 and verified the installed Blender 5.1.2/io_pdx_mesh 0.91 runtime before the parent's exports.
The cached exposed MCP health route still reported 1.10.48, so it was not used to invoke the new identity-alias operation.
The completed checkpoint was consumed through the verified 1.10.49 adapter CLI and standard export/reimport operations.
The original worker's narrowly published adapter/config/lock changes remain part of the source-review ledger.

This handoff proves package preservation and export/reimport acceptance.
Fresh startup logs and the final main-menu screenshots provide the engine loading evidence in the run report.
It does not claim map placement, campaign combat, audio playback, or animation appearance in a campaign.
No model geometry, action, or material was simplified.
