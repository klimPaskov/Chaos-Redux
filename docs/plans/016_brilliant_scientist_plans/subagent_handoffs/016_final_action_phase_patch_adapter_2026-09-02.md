# Existing-action phase patch adapter

## Scope

The parent authorized this bounded capability under the accepted no-regeneration closure's manual action-recovery exception.
It does not change the general 3D skill's provider-first animation policy for other work.
The capability clones an exact existing native action into a new target action and replaces only explicit caller-declared bone channels in a new sibling checkpoint.
It does not generate geometry, rebuild a rig, edit weights/materials, retime an action, run an unrestricted script, export a final action, or wire runtime consumers.

The Alien inspector released the no-new-call boundary, and worker/MCP/client integration is complete.
The focused and existing fast regressions pass, and both worker and parent native runs passed after the parent's source review, operation registration, and version-lock refresh to `1.10.19`.
No production action is created or approved by this tooling task.

## Approved declarative contract

The operation is named `patch_existing_humanoid_action_phases`.
It requires `blend_rel`, `checkpoint_rel`, `expected_source_sha256`, `expected_action_sha256`, `target_armature_name`, `source_action_name`, `target_action_name`, `semantic_role`, `source_fps`, `source_fps_base`, `frame_start`, `frame_end`, `phase_frames`, `allowed_bones`, `motion_bone_chain`, and `bone_patches`.
The checkpoint paths must be job-relative `.blend` paths without traversal; output must be a new sibling of the source, never an overwrite.
The source checkpoint SHA-256 binds the immutable input bytes.
The source action hash is the existing `inspect_scene.inspected_action_sha256` native curve fingerprint, not an exported `.anim` file hash.
The exact stored native FPS/FPS-base pair and original action frame range must match the caller's values and remain unchanged.

Supported roles and ordered phase names are:

- `attack` and `support_attack`: `ready`, `aim`, `discharge`, `recoil`, `recovery`.
- `defend`: `guard_start`, `guard_hold`, `guard_release`.
- `retreat`: `disengage`, `withdrawal`, `recovery`.

Training is intentionally outside the approved capability scope and remains unchanged.
Phase frames must be distinct ordered integers inside the original action range.
The caller supplies a unique exact bone allowlist and matching `bone_patches` mapping.
Each bone patch supplies `location` and/or `rotation_quaternion` as ordered lists of `{frame, value}` objects.
Every supplied channel includes both original action endpoints and every named phase frame.
Only those declared full channels are replaced on the cloned action; all undeclared channels and every original action remain exact.
Every native key insertion must report success, and each resulting declared scalar curve must contain exactly the requested frame/value sequence after the explicit values pass through native float storage.
The comparison uses those exact native stored values rather than a loose tolerance or an invented replacement curve.
Declared target channels use explicit linear interpolation; no generic sine, motion preset, scale channel, object-level transform channel, or free-form expression is accepted.

Quaternion values must be finite, nonzero, and normalized within `1e-5`; invalid values are rejected rather than silently normalized, and accepted values are stored as supplied through native key insertion.
Source/action/target identity collisions, malformed keys, unsupported channels, unsupported constraints/drivers/NLA, and identity-only or root-only edits fail closed.
At least one genuinely changed local bone channel must belong to a non-root bone.
Retreat additionally requires a caller-declared contiguous non-root bone chain rather than root transport alone.
Every member of that two-through-16-bone chain must have a genuinely changed local channel at a named phase.
The implementation does not require arbitrary all-bone motion or hardcode human bone names onto mechanical/nonhuman anatomy.

The exact source action must have one unambiguous local slot/layer/strip/channel bag and keyed bone-location/quaternion channels only.
Sampled curves, curve modifiers, duplicate curve paths/indices, source object-transform or scale channels, source NLA/drivers, linked data, constrained poses, and REST display are rejected.
The exact rig and every mesh bound to it must be local working objects, not protected/reference targets.
The rig must be unparented; each bound mesh must be unparented or object-parented to that rig, with exactly one active Armature modifier and no shape keys or mesh/object/datablock animation.
This intentionally rejects unsupported dependencies rather than editing or converting them.

Input limits are 64 named bones, 512 vector keys per channel, 4,096 vector keys across the request, 4,096 source scalar curves, 16 bound meshes totaling one million vertices, and 32 observed bone-parented locator Empties.
Each source FPS value is an integer from one through 1,000, its finite FPS-base value is positive and no greater than 1,000, and the stored native pair must match exactly.
Frames are integers between zero and one million; finite location coordinates are bounded within plus/minus one million units.

## Evidence and acceptance boundary

The report includes original/output checkpoint hashes, native source/target action hashes, exact scene preservation fingerprints, full target-action reopen equality, changed bones/channels/key counts, native FPS, per-phase local and posed bone matrices, existing bone-parented locator world matrices, and measured evaluated mesh minimum-height/bounds samples.
Temporary action/frame/pose changes used for sampling are restored before saving the new sibling.
The new target action is retained with a fake user but does not replace the originally active action; a subsequent approved export must select its exact target name explicitly.
Original geometry, topology, normals, UVs, weights, material/image data, object transforms, rest bones, source actions, and source checkpoint bytes remain protected by before/after fingerprints.
The only omitted action in the original-scene comparison is the explicitly named newly added target; that target receives its own complete preservation check.
The pre-save original-scene fingerprint must match exactly; after reopen, only the previously approved disappearance of independently proven unconsumed/unretained/unprotected local orphan material data is permitted and separately recorded.
All retained materials/images and all original geometry, rigs, object state, actions, and scene sections still compare exactly.
Target fingerprints that alias any original existing action are rejected.

Numerically different phase poses are necessary evidence but do not prove role-appropriate aim, muzzle discharge, recoil, contact, defensive protection, or backward locomotion.
The `1e-6` maximum local-basis matrix-component difference is only a numerical identity threshold, not a semantic amplitude target.
Shooting roles require non-root articulation in ready-to-aim, discharge-to-recoil, and recoil-to-recovery transitions; defend and retreat require non-root articulation in both of their adjacent transitions.
Defend's guard-hold pose must additionally differ from the original source action at that phase.
The report must retain `semantic_acceptance: false` for parent review of the actual motion.
Measured minimum height is not automatic foot-contact approval.
Existing locator observations do not register, move, or approve those locators.
The report marks `manual_or_procedural_replacement_authored: true` and `procedural_generator_used: false` to distinguish explicit authorized manual key data from a generic procedural motion generator.
Source provenance is retained and the manual patch has explicit derivative provenance rather than claiming untouched provider authorship.

## Files and fast tests

- `.tools/3d_pipeline/adapter/blender_worker.py`: declarative validation, cloned-channel patch, preservation, sampling, save/reopen evidence, and dispatch.
- `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py`: exact new operation schema and forwarding.
- `.tools/3d_pipeline/blender_client.py`: exact client forwarding.
- `.tools/3d_pipeline/tests/test_action_phase_patch.py`: focused validation/schema contracts.
- `.tools/3d_pipeline/tests/blender_action_phase_patch_integration.py`: synthetic native four-role success and immutable-failure scenarios.
- This handoff.

The parent owns operation registration, version/configuration, source-lock refresh, production role design, production approval, runtime bindings, and final review.
No staging or commit is authorized for this worker.

All 88 fast tests passed on the final integrated source:

- `python -B -m unittest discover -s .tools/3d_pipeline/tests -p test_action_phase_patch.py -q`: 13 tests, 2.157 seconds.
- `python -B -m unittest discover -s .tools/3d_pipeline/tests -p test_mesh_region_inspection.py -q`: 14 tests, 2.155 seconds.
- `python -B -m unittest discover -s .tools/3d_pipeline/tests -p test_reimport_promotion_contract.py -q`: 29 tests, 8.861 seconds.
- `python -B -m unittest discover -s .tools/3d_pipeline/tests -p test_locator_adapter_contract.py -q`: 32 tests, 7.154 seconds.

The source freeze candidates are LF-only.
Worker SHA-256 is `5C8DF03BF75355BE60CAFE1CE7C300025A07449FB327383A0CC89B1C0F11FE40`; MCP SHA-256 is `2011F13EFF2887A67C52A1662381EC7CBE2146132B13B1122285F5E86D2FF935`; client SHA-256 is `ADA7C52EB14AE7A48AEB4D7369E4464E1AA3F447878EB989A0EBCDEA7C6A99A8`.
The fast test SHA-256 is `991E707B74C1256B002EA2CE305766DB3B03D18CC8E9ACABE115B3C6ECC46875`; native fixture SHA-256 is `719D8C557D46A45A027A361D0EDE01CC55AA0B2CD0C60DACDDFA6AF2E3678224`.

## Native fixture gate

The exact native command was `C:/Program Files/Blender Foundation/Blender 5.1/blender.exe --background --factory-startup --python-exit-code 1 --python .tools/3d_pipeline/tests/blender_action_phase_patch_integration.py`.
The parent registered and relocked `1.10.19`, then ran `.tools/3d_pipeline/verify_environment.py` without a provider probe; it returned exit code zero with `findings: []`.
The parent-owned adapter configuration SHA-256 was `121580FAFFC6FE2DE059F5F6E35E6DFEEF9941F2D11A60F9AC3042185F3636B0`.
The fixture creates a disposable four-vertex mesh, three-bone rig, existing native action, existing collision action, and a bone-parented locator.
It tests all four approved roles with explicit source-preserving key data, including a distinct supporting-fire timing map and a two-bone retreat chain.
It checks exact untouched scene fingerprints, the original action and frame binding, native FPS, exact supplied target channel values and interpolation, a separate new-action reopen fingerprint, phase pose/ground/locator observations, and source immutability.
Failure cases include wrong FPS, wrong source/action hashes, duplicate target action, path escape, invalid quaternion, root-only patch, identity-only patch, and source NLA.
The fixture is not an animation-quality or production-asset acceptance substitute.

### Native results and earlier fixture correction

The first pre-registration test correctly rejected constant scale curves inherited from the shared locator fixture's setup.
The fixture was corrected by omitting those synthetic scale curves before creating its immutable source checkpoint.
No scale track was removed from a production model, and the worker's scale-channel rejection was not relaxed.
The next pre-registration run passed in 2.8304 seconds with the three exact parent-reviewed source hashes pinned and all unchanged production dependency hashes verified.
That test mode was explicitly authorized by the parent and reported `reviewed_unregistered_candidate: true`; it was not a registered-production-route acceptance claim.

The final fixture additionally supports the exact registered `1.10.19` mode, where every source hash must match the registered lock and the three reviewed implementation hashes remain independently pinned.
The worker's registered run returned exit code zero in 3.5519 seconds under Blender `5.1.2`, build `ec6e62d40fa9`.
The parent's independent registered run returned exit code zero in 3.8817 seconds.
Both reported `status: pass`, `reviewed_unregistered_candidate: false`, `fixture_only: true`, and `production_asset_acceptance: false`.

Both runs produced the same source-action and four distinct target-action fingerprints:

| Fixture action | Native curve SHA-256 |
| --- | --- |
| Source | `687B356C7143A35087B87DDAB31056103239EA30FF3BF1543061986732A60059` |
| Attack | `461E994260690F1A0CDA128F41BA8B31365CDE51BBFF3B78425733E1F55B9313` |
| Support attack | `12DE141F2D5EB61BEB3ACA0E24BAB865D63BAF5CE3E379FE9AF1B85186738FC5` |
| Defend | `D75FD051F88EDA03F2E4CB57CA372FE22152B1246DDB0E8EB79F98B4406B1485` |
| Retreat | `DBDCF42E327E61C62000879A53B53EED6BDAB0AED155C87E4D7D9A411EB7C924` |

Each target's complete native action record survived save/reopen exactly, and each full original-scene preservation comparison passed.
The fixture verified stored native key values, unchanged original source/collision actions, undeclared channels, restored source action slot/frame/pose, the unchanged `30/1.0` FPS pair, and unchanged source bytes.
All nine rejection paths passed without creating an output checkpoint: wrong FPS, source hash mismatch, action hash mismatch, existing target action, path traversal, invalid quaternion, identity-only patch, root-only patch, and NLA.
The worker-run temporary source SHA-256 was `7D81BFDF467FA2378486030841B737FFD8EAC7A88C517E8583A135A46AB6271A`; the parent-run temporary source SHA-256 was `A32FF40A07B128C208C00AC99CF194105C72FF063BA5C211450D75F0CC135A55`.
These are separate disposable fixture checkpoints, not Robot assets or production action hashes.

## Final boundary

The adapter capability and its synthetic regression proof are complete, with no production checkpoint opened or modified by this worker.
Production key design, twin-gun/guard/withdrawal semantics, weapon and ground contacts, locator recovery, actual `.anim` exports and reimports, sound/effect timing, runtime wiring, and final acceptance remain parent-owned.
Training and geometry regeneration remain excluded.
No simplification was substituted for an unsupported case; the restrictions above fail closed.
The `chaos-redux-3d-model-pipeline` skill governed preservation and evidence separation, with only the parent's explicit manual recovery exception applied to this capability.
No shared configuration, dependency lock, runtime asset, staging operation, or commit was authored by this worker.
