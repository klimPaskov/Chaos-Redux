# Rigid Weapon Attachment Tool Handoff — 2026-08-22

## Scope and result

Implemented adapter version `1.8.0` operation `attach_rigid_weapon_from_checkpoint`, exposed as MCP tool `chaosx_blender_hoi4_attach_rigid_weapon_from_checkpoint` and client method `BlenderAdapterClient.attach_rigid_weapon_from_checkpoint`.

The operation appends exactly one explicitly named local `MESH` object from one job-root-relative source `.blend` checkpoint into a distinct job-root-relative target rig `.blend`, rigidly bone-parents it, and saves a third job-root-relative output checkpoint plus `blender/reports/<target_object_name>_rigid_attachment.json`.

No gameplay, asset-job, runtime, or `author_humanoid_actions` files or behavior were changed.

## Files changed

- `.tools/3d_pipeline/adapter/blender_worker.py`
- `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py`
- `.tools/3d_pipeline/blender_client.py`
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`
- `.tools/3d_pipeline/config/dependencies.lock.json`
- `.tools/3d_pipeline/tests/test_rigid_weapon_attachment_tool.py`
- `.tools/3d_pipeline/tests/blender_rigid_weapon_attachment_integration.py`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/rigid_weapon_attachment_tool_handoff_2026-08-22.md`

## Public contract

Required MCP fields:

- `job_id`
- `source_blend_rel`
- `target_blend_rel`
- `output_blend_rel`
- `source_object_name`
- `target_object_name`
- `target_armature_name`
- `parent_bone_name`

Optional bounded fields:

- `create_weapon_bone_name = ""`
- `translation = [0.0, 0.0, 0.0]`
- `rotation_euler_degrees = [0.0, 0.0, 0.0]`
- `scale = [1.0, 1.0, 1.0]`
- `collision_policy = "reject"`, with the only alternative `replace_prior_attachment`
- `action_name = ""`
- `render_views = ["three_quarter"]`

The Event 016 recovery inputs fit this generic contract: source checkpoint `blender/checkpoints/recovery_3d_weapon_assembled.blend`, source/target object name `alien_infantry_laser_rifle`, and an explicit provider-rig target checkpoint, armature, hand bone, optional `weapon` bone, alignment vectors, and proof action supplied by the caller.

## Fail-closed behavior

- Rejects absolute, traversal, non-job-root, non-`.blend`, same-source/target/output, and unsafe-name inputs.
- Opens the source checkpoint independently and rejects linked libraries, absent/duplicate named objects, non-meshes, linked object/data, parent/child dependencies, constraints, object-referencing modifiers, animation data, and shape keys.
- Uses Blender library append with one requested object and verifies the object datablock count increases by exactly one.
- Rejects target linked libraries, missing or non-armature target, missing explicit parent bone, and unsafe collisions.
- `replace_prior_attachment` may remove only a mesh carrying the operation's `chaosx_rigid_weapon_attachment` marker. A pre-existing requested weapon bone may be reused only when it carries the operation's marker and retains the requested parent hand bone.
- Optional bone creation makes one explicit deform bone parented to the explicit existing hand/weapon bone. It never adds keys.
- Translation, Euler rotation, and scale accept only explicit finite three-number vectors with bounded magnitudes and positive scale.

## Report and retention evidence

The structured report includes source, target, and output SHA-256 hashes; source geometry; collision disposition; armature and bone parenting; created-bone status; explicit alignment; weapon world transform and bounds; action and existing-bone retention snapshots; output checkpoint/report paths; and animation policy.

Action retention hashes every action's paths, indices, keyframe coordinates, interpolation, range, curve count, and keyframe count before and after attachment. Existing bone parent, deform, rest head/tail, and rest matrix data are compared exactly, excluding only the explicitly created weapon bone.

When `action_name` is supplied, the worker requires distinct start, middle, and end frames, samples weapon world transforms/bounds and bone-relative matrices at all three phases, measures invariant world-space weapon edge lengths, renders the requested view at each phase, and rejects relative-matrix or rigid-edge drift over `1e-5`. The target rig's original active action is restored before saving. The operation contains no `bpy.data.actions.new` or `keyframe_insert` call.

## Validation

- Focused Python tests passed `4/4`: registration/version alignment, MCP wrapper schema AST, no animation authoring in the worker operation, and client payload forwarding using the Event 016 rifle/checkpoint names.
- Python compilation passed for worker, MCP wrapper, client, and focused tests; both JSON configuration files parsed successfully.
- A Blender `5.1.2` synthetic integration passed using source object `alien_infantry_laser_rifle`, an explicit `Armature`/`RightHand`, creation of one `weapon` bone, a three-frame provider-action analogue, three front-view renders, exact action retention, exact existing-bone retention, one new bone, invariant bone-relative matrix, invariant weapon edge lengths, and output checkpoint/report creation in an automatically removed temporary directory.
- Live `tools/list` exposed `chaosx_blender_hoi4_attach_rigid_weapon_from_checkpoint` with 15 properties and exactly the eight required fields listed above. One earlier repeat encountered the adapter route's intermittent stdio teardown (`exit=0` after logging `ListToolsRequest` but no JSON-RPC response); the subsequent bounded retry returned the complete successful schema receipt.
- Dependency-lock SHA-256 values match the current MCP wrapper, worker, client, and adapter config bytes.

## Remaining parent work and risks

The parent or model worker should call the operation against the selected provider-rig checkpoint with the exact armature, hand bone, alignment, and proof action after its job lane is released. This subtask deliberately did not mutate the Event 016 asset job or choose alignment values.

No fallback or simplification was used. The only unperformed validation is an actual Event 016 checkpoint invocation, because the assigned scope explicitly prohibited edits to asset jobs; the Blender integration exercised the same object name and full rigid/action-proof path in an isolated temporary job.
