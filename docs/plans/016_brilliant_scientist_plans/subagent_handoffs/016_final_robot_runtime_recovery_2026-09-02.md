# Event016 autonomous robot runtime recovery

Date: 2026-09-02

Owner: `shared_robot_system/models_3d/autonomous_robot`

Status: `BLOCKED_CAPABILITY_REVIEW` after a bounded attack phase-patch was rejected before save; no action, mesh, material, sound, counter, runtime, lock, or configuration mutation was performed in this pass.

## Binding and ownership

This is an existing-geometry recovery under the Event016 final completion contract, not a new model-generation task.

The immutable source lineage is `blender/checkpoints/03_rig_approved.blend`; the bounded working candidate is `blender/checkpoints/manual_recovery_2026_08_27.blend`.

The user binding expressly permits manual rig, weight, weapon, action, contact, locator, effect, export, and reimport recovery on this geometry, while forbidding regeneration, remesh, provider/image calls, geometry substitution, export-only action substitution, static or transform-only motion, semantic aliases, and silent firing.

Parent-owned surfaces remain `gfx/entities/autonomous_robot.asset`, `gfx/entities/autonomous_robot.gfx`, sound definitions and wiring, gameplay, and adapter/config/lock files.

The only intended documentation output from this pass is this handoff under the assigned Event016 plan folder.

## Gate and dependency evidence

The mandatory `MESHY_API_KEY` presence gate passed without exposing the key; no Meshy balance, generation, download, remesh, rig, convert, or animation call was made.

The repository dependency lock is `.tools/3d_pipeline/config/dependencies.lock.json`; the schema lock is `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`; the adapter config is `.tools/3d_pipeline/config/blender_hoi4_adapter.json`.

The lock and config now resolve `chaosx_blender_hoi4` version `1.10.19`.

The locked adapter source/config hashes are `chaosx_blender_hoi4_mcp.py=2011F13EFF2887A67C52A1662381EC7CBE2146132B13B1122285F5E86D2FF935`, `blender_worker.py=5C8DF03BF75355BE60CAFE1CE7C300025A07449FB327383A0CC89B1C0F11FE40`, `blender_client.py=ADA7C52EB14AE7A48AEB4D7369E4464E1AA3F447878EB989A0EBCDEA7C6A99A8`, `normalization_convergence.py=91AC1D4BA9BE4D39AB4697F9044060A9F119A8998E1DADA8F4A8E6F58A5F9ED5`, and `blender_hoi4_adapter.json=121580FAFFC6FE2DE059F5F6E35E6DFEEF9941F2D11A60F9AC3042185F3636B0`.

The locked Blender build is `5.1.2` commit `ec6e62d40fa9`, the required socket is `127.0.0.1:9876`, and `io_pdx_mesh` is locked to version `0.91.0`, release `0.91`, SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.

The fresh-process locked-client health request id was `9918e366b348444aa4023dbacba362a6`; its response verified Blender `5.1.2`, the loaded io_pdx_mesh extension, and live adapter version `1.10.19`.

The attached interactive MCP surface was stale, but the approved fresh-process client invokes the locked wrapper and resolves the 1.10.19 adapter source, including the new hash-bound `patch_existing_humanoid_action_phases` route alongside `author_locator`, `promote_accepted_reimport`, `retime_animation_action`, `offset_action_root`, `export_animation`, and `reimport_export`.

The route-refresh blocker is cleared for read-only work and one explicitly parent-authorized attack attempt; no mutation-capable operation has written a checkpoint.

## Existing lineage and immutable geometry evidence

The source checkpoint SHA-256 is `1FDA838E30356ECA6D44833DACE951AB4731CE4078D084E888FEC966E80947EF`.

The manual candidate checkpoint SHA-256 is `FEB2BB03E2DE7EAF84547C0864500C821A7DDD05A0BEE1958948C969F2BDB25D`.

The existing candidate mesh `export/manual_recovery_2026_08_27.mesh` is SHA-256 `7CF3963091865FB61DE22F93A23893728C0A109775CA4D2DEA4CDF4513181D10`.

The candidate has 29,971 triangles, 15,123 vertices, 24 bones, existing integrated arm machineguns, and exporter locators named `muzzle` and `muzzle_left`.

The candidate normalized source geometry height is approximately `7.3518247604` against the required vanilla source height `7.3518242835`; runtime entity scale `0.8` is applied once by the parent-owned entity.

The required axes remain `-Y` forward and `+Z` up, with source feet on the `Z=0` plane and PDX material textures at `1024` dimensions.

The fresh-process read-only scene inspection request id was `a96023b4a1a344c9a78a306597cf3120`.

The checkpoint contains exactly one working mesh object `char1.003` with one active Armature modifier consuming `autonomous_robot_rig`; no separate weapon object is present, so the two integrated machineguns are fused into the existing deforming mesh and must be preserved through action recovery.

The scene has exactly one 24-bone armature named `autonomous_robot_rig`, no negative-scale objects, no scale F-curves, and 15,123 vertices with four influences each, no zero-weight vertices, no non-bone groups, and no vertices over four influences.

Both existing locators are bone-parented Empties but are not yet registered for export: `muzzle` is parented to `autonomous_robot_rig/RightHand`, and `muzzle_left` is parented to `autonomous_robot_rig/LeftHand`; both report `owner_job=null` and `registered_for_export=false`.

At attack preview frame 25, the unregistered locator origins are approximately `muzzle=(0.427745,-2.378733,6.119273)` and `muzzle_left=(-0.445071,-2.362624,6.126625)` in source space, while the corresponding hand-bone tails are near Z `5.2685` and `5.2723`; exporter-supported locator re-authoring with measured bone-local transforms is therefore still required before firing proof.

Spatial read-only deformation samples at attack frame 25 found 780 vertices in a right-arm zone and 827 in a left-arm zone; sampled weights are dominated by the matching shoulder/arm/forearm/hand chains, with topology and all action data unchanged. Because the weapons are fused, this is retention evidence for the arm-mounted region, not a separately named gun-object proof.

The candidate reimport reports preserve the 29,971-triangle mesh and 1,973 open-edge count without degenerates, negative scale, or non-manifold regressions; those are geometry facts, not action-semantic approval.

The old runtime mesh and action bytes remain a separate historical/provider line and must not be mixed with the manual candidate by export-only substitution.

## Read-only action fault diagnosis

All eight manual candidate `.anim` text dumps report `fps = 30.0`; the current review found no 24-FPS requirement in the Event016 contract or the applicable skills. The 24-FPS values belong to older provider-line metadata and crosswalk text, so the native 30-FPS candidate must be preserved unless the actual runtime binding profile proves another rate.

The current candidate action hashes are:

| Role | Candidate file SHA-256 | Current evidence | Recovery implication |
| --- | --- | --- | --- |
| `idle` | `C493E81B2240271B339C0B4DF74E1AC9A44AFE4292FCBEF6A7FAEFEC73102CA2` | 0–48 at 30 FPS; 6 arm/hand quaternion bones; about 1.78° maximum rotation; actual-byte reimport exists | Preserve native FPS pending binding-profile proof; keep as a mechanical scanning loop only if it remains distinct from defend. |
| `move` | `703556A40151EF25469F7AB758B42DC49E50514B0E8C4CDAF2DF091D64DB584C` | 0–48 at 30 FPS; 16 arm/leg quaternion bones; about 10.17° maximum rotation; no actual-byte reimport proof | Preserve native FPS pending binding-profile proof; grounded loop audit and actual-byte reimport are required. |
| `attack` | `169E21176F3B98E8D56EA3F371E3B5643543833869C66A6B39616CF1869502C8` | 0–48 at 30 FPS; 6 arm/hand quaternion bones; about 1.81° maximum rotation; metadata discharge frame 25; actual-byte reimport exists | Current motion does not prove aim, discharge, recoil, and recovery; substantive twin-gun repair is required, with retiming only if the actual binding profile demands it. |
| `defend` | `C493E81B2240271B339C0B4DF74E1AC9A44AFE4292FCBEF6A7FAEFEC73102CA2` | Byte-identical to idle; 0–48 at 30 FPS; about 1.78° maximum rotation | Rejected as a distinct accepted role; create a separate defensive stance/motion without masquerading idle. |
| `support_attack` | `4C0B0B04AFBE16D8E2A9CB7CE0212D8FA4B72C89807B9BED54C30577E11396DE` | 0–36 at 30 FPS; 6 arm/hand quaternion bones; about 1.81° maximum rotation; metadata discharge frame 19; no actual-byte reimport proof | Current motion does not prove supporting dual-gun fire; substantive repair and reimport are required, with retiming only if the actual binding profile demands it. |
| `retreat` | `8FB492C36BB61AD28F6B985E11CC549B3D294E8009B9B60AC4328EDA3A0B00AF` | 0–48 at 30 FPS; 6 arm/hand quaternion bones; about 1.82° maximum rotation; no actual-byte reimport proof | Requires genuine backward/withdrawal locomotion, not a firearm-path or semantic alias; preserve native FPS pending binding-profile proof. |
| `training` | `920CE805C81F75BE47EC5D408C2355D0AE912D5657319D3E1506978EAEF3FB62` | 0–48 at 30 FPS; 8 arm quaternion bones; about 2.98° maximum rotation; no actual-byte reimport proof | Requires a substantive mechanical systems/weapon drill loop; preserve native FPS pending binding-profile proof. |
| `death` | `4FC1CF58C3ECC7969397D0B3387626A1621A9BCD296D88D1EE0D6ACD2CEAFF13` | 0–48 at 30 FPS; all 24 bones; about 54.43° maximum rotation; actual-byte reimport exists | Impact/collapse/settle validation is required; preserve native FPS pending binding-profile proof. |

The hashes for `move`, `retreat`, `training`, and `death` above identify the current candidate inventory; the subsequent export pass must recalculate them after any authorized recovery.

The manual recovery script diagnosis is consistent with the bytes: robot firearm roles were baked through a shared hand-target path with only a bounded `0.09`-unit recoil, and `defend` used the same firearm-baked path as idle.

The old candidate metadata labels attack discharge at frame 25 and support discharge at frame 19 at 30 FPS, but those labels are not accepted phase evidence because the keyed motion does not show the required stages.

Fresh-process native Blender action inspection produced curve fingerprints `idle=59BA84E48899603CB2486D7CD65D30261FB771DD9F9F450EA0AF73D6075F8D14`, `defend=59BA84E48899603CB2486D7CD65D30261FB771DD9F9F450EA0AF73D6075F8D14`, `attack=D6082761EC6069BDFA494BF6973285A0FA376AC42843D6343B456535010FFE3A`, and `support_attack=97BB2C54072F3722EEDE826129A0D9F1A773F2302CAC17E646F18F02C981E252`.

The native curve fingerprints confirm the action-level idle/defend alias independently of the identical exported `.anim` bytes.

The locked `author_humanoid_actions` operation is not a suitable robot phase-repair route. Its exact payload accepts only `blend_rel`, `checkpoint_rel`, optional role-to-action `action_names`, `fps`, and `fused_weapon_grip`.

Its worker implementation creates only `idle`, `move`, `attack`, and `death`, uses fixed frame lists `[0,12,24,36,48]`, `[0,6,12,18,24]`, `[0,8,16,24,32]`, and `[0,12,24,36]`, and drives each role from generic sine or linear phase values.

Its attack path applies one sinusoidal phase across spine, head, shoulders, arms, forearms, hands, and upper legs; it has no explicit ready/aim/discharge/recoil/recovery inputs, no support or defend role, no locator/effect/audio binding, and no weapon-specific contact validation.

Calling that operation would overwrite existing actions with generic procedural motion and would violate the robot requirement for substantive, role-distinct firearm and defensive semantics; it must not be used as the final repair.

## Parent-authorized attack phase attempt

The 1.10.19 declarative route was read from the locked client and worker before use. Its exact payload requires the source and target checkpoint siblings, both source and native-action SHA-256 values, one exact local source action, native FPS/FPS base, explicit role phases, an exact allowed-bone set, an optional retreat chain, and explicit per-channel frame/value keys; it never retimes or regenerates geometry.

The measured attack plan preserves the native `30 FPS`, action range `0..48`, and the existing ready pose. The explicit phase frames are `ready=0`, `aim=12`, `discharge=24`, `recoil=28`, and `recovery=40`, with endpoint key `48`; the worker requires every declared channel to include both endpoints and every phase frame.

The exact declared bone keys are `Spine01`, `Spine02`, `LeftShoulder`, `RightShoulder`, `LeftArm`, `RightArm`, `LeftForeArm`, `RightForeArm`, `LeftHand`, and `RightHand`; `motion_bone_chain` is empty for attack. The phase deltas were derived from locked `mesh_region` rest/pose matrices in Blender bone-local basis, not from a sine generator: `Spine01` X `[0,2.5,3,-4.5,-1,0]` degrees, `Spine02` X `[0,3.5,4.5,-6,-1.5,0]`, left/right shoulders Z `[-3,-4,+7,+1.5]` and `[+3,+4,-7,-1.5]` degrees over aim/discharge/recoil/recovery, left/right arms X `[4,5,-9,-2]`, left/right forearms X `[5,6,-12,-3]`, and left/right hands X `[2,3,-7,-2]`; every sequence returns to zero at endpoint `48`.

The full explicit quaternion payload is preserved in the job-owned request evidence `logs/adapter/a257908d583744398537838a832ef30b.json`; its source action is `autonomous_robot_attack`, source native-action SHA is `D6082761EC6069BDFA494BF6973285A0FA376AC42843D6343B456535010FFE3A`, and target action is `autonomous_robot_attack_phase_patch_2026_09_02` in sibling checkpoint `blender/checkpoints/manual_recovery_2026_08_27_attack_phase_patch_2026_09_02.blend`.

The first request `logs/adapter/9b0024d5abbd4e3aacc275b9116e9f6b.json` was rejected before mutation because the caller mistakenly supplied `source_action_name=autonomous_robot`; no output existed. The corrected request id `a257908d583744398537838a832ef30b` selected the exact native action and was also rejected before mutation with `Source action has unsupported object, scale, or non-quaternion bone channels`; no output checkpoint exists and the source SHA remains `FEB2BB03E2DE7EAF84547C0864500C821A7DDD05A0BEE1958948C969F2BDB25D`.

The individual offending curve paths are not returned by the current read-only `inspect_scene` response. The rejection is consistent with the existing recovery source: `recover_existing_units.py` sets every pose bone to `XYZ` while creating non-firearm actions, then runs the firearm IK/NLA bake without restoring quaternion mode. Thus the baked firearm actions can retain `rotation_euler` curves even though `io_pdx_mesh` exports their evaluated poses as quaternion samples. This is a source-pipeline diagnosis supported by the exact worker error, not a claim that an unexposed path list was observed.

The minimum additional capability is an exact-hash-bound sibling operation that reads one existing action, converts only its Euler pose curves to explicit quaternion pose curves while preserving evaluated transforms at every native frame, removes unsupported scale/object channels, preserves source action provenance and all untouched actions, then returns the offending and converted path inventory. Only after that conversion can the existing explicit phase payload be retried; no adapter/config/lock change is requested in this pass.

The read-only source-phase render set uses the same adapter camera and front view at native frames `0`, `12`, `24`, `28`, `40`, and `48`: `blender/previews/autonomous_robot_attack_source_ready_2026_09_02_front.png` SHA-256 `F0E249E7B2E49C59179591B4CEB9D1243D5960E28A94CAC183C0ED15233377AE`, `autonomous_robot_attack_source_aim_2026_09_02_front.png` SHA-256 `32C3EDF19E6BAD7D99D4775BF5C46A2499085442CEA05CFE7D21C4562AF59BC9`, `autonomous_robot_attack_source_discharge_2026_09_02_front.png` SHA-256 `7A8DE2589684E81E4D377F8B985C8FBF26EC6DCB3FA47ECF2F331604B45F7203`, `autonomous_robot_attack_source_recoil_2026_09_02_front.png` SHA-256 `E1DE46763D4084DEEE1E965FC5D79F09444A8105BB28B2FDF85A4561F519F4E1`, `autonomous_robot_attack_source_recovery_2026_09_02_front.png` SHA-256 `43E99A9C0AC20201C61D414924657D84FD1C71E00957D55276D14BB8AA5B685C`, and `autonomous_robot_attack_source_endpoint_2026_09_02_front.png` SHA-256 `EE078CEBEF858E270AA621CA9B790F3065329C8BE1199B2255C32B48C025E1A3`. The corresponding successful inspect request IDs are `20edb9b41260432183ba65e0ee1bfeff` (ready), `03c5ad2aaa964714b189d15aa764b8aa` (aim), `81735175ae3f4460abf9a76cb6e5f7a6` (discharge), `b8c5b3d18f48423a9d8739ac1374a59f` (recoil), `31f9212a2cf3448e96f41b24e4639923` (recovery), and `907ad5971a7c45909b17a163c412ffe7` (endpoint).

The source contact sheet is `blender/previews/autonomous_robot_attack_source_phase_contact_2026_09_02.png` SHA-256 `A4F9D73B53A9FE18159760310B04BD5BFDCA59B43CB6A93645ED8B5C68091F35`. Visual review shows the body, fused machineguns, hand continuity, and ground contact retained, but no readable brace-to-aim, discharge, articulated recoil, or recovery separation at these frames; this agrees with the small native attack fingerprint motion and is why the source action is not accepted as final.

There is no target-phase render or target checkpoint to review: `manual_recovery_2026_08_27_attack_phase_patch_2026_09_02.blend` was never created because request `a257908d583744398537838a832ef30b` failed before mutation. The source contact sheet is evidence of the intact candidate and the missing target is an explicit unresolved gate, not a target-action alias.

The existing `validation/reimport_manual_recovery_2026_08_27_autonomous_robot_attack.json` proof is retained as historical actual-byte reimport evidence only. It imports the exported `.anim` into a fresh `io_pdx_rigAction`/`io_pdx_rig` scene and therefore cannot serve as the patch source: it does not preserve the candidate’s `autonomous_robot_rig` identity, working-object flags, or exporter locator registration, and using it as runtime input would violate the existing-geometry lineage boundary.

## Proposed seven-plus-role phase and reimport crosswalk

This is a review plan, not an approval or a claim that any replacement action exists.

| Asset/role | Planned native-FPS phase evidence | Required exporter/reimport proof | Status now |
| --- | --- | --- | --- |
| Mesh | Existing two-arm MG geometry, `muzzle` and `muzzle_left` locator retention, normalized source height, `-Y/+Z`, entity `0.8` once | Exported mesh hash, locator world positions, material map audit, mesh reimport | Existing mesh geometry is viable; locator parent/world proof is missing. |
| Idle | Distinct mechanical scan with small head/torso/arm articulation and grounded in-place loop | Native-FPS frame 0/quarter/mid/three-quarter/last inspection and actual-byte reimport | Candidate exists and must remain distinct from defend; do not retime on stale metadata. |
| Move | Heavy grounded march with alternating legs, weight transfer, servo/footfall contacts, in-place root | Native-FPS loop/contact inspection plus actual-byte reimport | Candidate is more articulated than upper-body roles but unproven after export. |
| Attack | Ready/aim, both guns align through the retained muzzle locators, discharge, visible arm/weapon recoil, recovery | Exact measured discharge frame, `muzzle`/`muzzle_left` locator proof, particle/light/sound crosswalk, native-FPS actual-byte reimport | Blocked by substantive motion and route capability. |
| Defend | Distinct guarded defensive stance and protective motion, non-firing unless separately justified | Byte-distinct action hash, multi-frame defensive pose/contact inspection, native-FPS actual-byte reimport | Rejected because current bytes equal idle. |
| Support attack | Distinct supporting dual-MG firing sequence with its own aim/discharge/recoil/recovery timing | Exact measured support discharge frame, both locator proof, effect/audio crosswalk, native-FPS actual-byte reimport | Blocked by substantive motion and route capability. |
| Retreat | Genuine backward/withdrawal march with grounded alternating legs and in-place root policy | Native-FPS loop/contact inspection and actual-byte reimport | Candidate is upper-body dominated and not accepted. |
| Training | Distinct mechanical systems/weapon drill with articulated arms and readable repeated phases | Native-FPS loop inspection and actual-byte reimport | Candidate is too small in amplitude for acceptance without review. |
| Death | Impact, articulated collapse, and settling/shutdown with grounded contact | Native-FPS multi-phase inspection and actual-byte reimport | Candidate has substantive motion but remains unapproved. |

No retime is proposed at this stage. If the actual binding profile explicitly requires another FPS, derive the conversion from the measured source rate through the locked adapter and verify the resulting export rather than rounding frame numbers in documentation.

For attack and support, discharge frame and normalized event time must be selected from the repaired export at the proven binding FPS, not inherited from the stale metadata or current runtime `0.3333` event.

## Exact capability needs after route refresh

1. Re-run the locked adapter health check and confirm live version `1.10.19`, all locked source hashes, Blender `5.1.2`, socket reachability, and io_pdx_mesh `0.91.0` before any checkpoint call.

2. Use read-only `inspect_scene` on the manual candidate to report mesh object, armature, all 24 bones, action metrics, weapon object names, locator parentage/world transforms, material slots, scale/orientation, and frame-rate metadata. The current response does not expose individual action curve paths, which is the specific diagnostic gap encountered here.

3. Use a bounded saved working duplicate under the robot job root; never edit `03_rig_approved.blend` and never overwrite the current candidate before preserving a checkpoint hash.

4. Use the now-exposed `patch_existing_humanoid_action_phases` only after the source action has been converted into the route’s accepted quaternion-only curve schema. The first 1.10.19 attempt proves that explicit phases are available but fail closed on the candidate’s unsupported source channels; the current operation does not perform that conversion.

5. If the 1.10.19 worker exposes no bounded quaternion-conversion capability, stop for parent review rather than inventing an unrestricted Blender route or producing transform-only actions. The user binding authorizes manual recovery, but it does not authorize bypassing the repository adapter.

6. Use `retime_animation_action` only if the actual binding profile proves a non-native FPS requirement and only after substantive action approval; it must change sample time without replacing motion.

7. Use the locked `author_locator` capability to prove the existing exporter-supported `muzzle` and `muzzle_left` locators, their parent attachment, and their world positions at the exact attack/support discharge frames.

8. Use `correct_action_grounding` with the declared in-place contact policy only after motion is substantive; root correction may not become a replacement action.

9. Use `prepare_export_coordinate_checkpoint`, `export_animation`, `export_mesh`, and `reimport_export` for every accepted role and the final mesh. Use `promote_accepted_reimport` only after all hashes, semantic phases, materials, locators, and actual-byte reimports are approved.

10. Preserve the current robot mesh, integrated guns, weights, materials, counters, and sourced audio originals; no Meshy/provider/image operation is part of this recovery.

## Minimal missing capability proposal

The current locked adapter now exposes an explicit phase-patch operation, but the existing candidate cannot reach it because the attack source action contains unsupported channels. The missing operation is a bounded source-channel conversion/inspection step, not a request for generic action authoring.

If the parent approves a narrow adapter enhancement, the minimum safe addition is an exact-hash-bound quaternion conversion of one existing action on a new checkpoint sibling, followed by the already-locked `patch_existing_humanoid_action_phases` route.

The conversion payload should require `blend_rel`, `checkpoint_rel`, expected source/action SHA-256 values, `target_armature_name`, one exact source action, an explicit target action name, native `fps`/FPS base, frame range, and a declared `preserve_evaluated_pose=true` policy. It must return the individual source curve paths, channel kinds, converted paths, and source/target action fingerprints before any phase patch is attempted.

The existing phase-patch payload requires `blend_rel`, `checkpoint_rel`, `target_armature_name`, `source_action_name`, `target_action_name`, `semantic_role`, native `fps`, explicit `frame_start` and `frame_end`, `phase_frames`, an explicit allowed bone list, and a caller-supplied per-bone keyframe patch rather than a free-form script.

For `attack` and `support_attack`, `phase_frames` must contain `ready`, `aim`, `discharge`, `recoil`, and `recovery`; the patch must key at least `Spine01`, `Spine02`, `Head`, both shoulder/arm/forearm/hand chains, and any explicitly retained weapon-bone channels, with discharge and recoil visibly distinct in both arms.

For `defend`, `phase_frames` must contain at least `guard_start`, `guard_hold`, and `guard_release`, and the resulting action fingerprint must differ from idle while remaining non-firing.

For `retreat` and `training`, the operation should accept role-specific explicit phase maps only when read-only review rejects their current native actions; it must not alias move, idle, attack, or support.

The operation must reject geometry, mesh-topology, material, armature-bone, and weight changes; reject scale channels, whole-rig translation/rotation as the sole motion, missing phase keys, duplicate target action names, and action patches outside the named arm/hand/spine scope; and preserve the source checkpoint byte-for-byte.

Its report must include source and output checkpoint hashes, preserved mesh topology/material/weight fingerprints, changed bones and keyed-frame counts, per-phase pose summaries, both locator world matrices at the discharge frame, ground-contact samples, root policy, native FPS, and an explicit `manual_or_procedural_replacement_authored` field distinguishing the authorized explicit phase patch from a generic procedural replacement.

The conversion is a capability request only; no adapter source, lock, config, or action file was changed, and no further call should be made until the parent reviews and approves the contract. The existing phase-patch contract was already invoked once with the parent’s explicit attack-only authorization and rejected before mutation as recorded above.

## Runtime effect and audio wiring handoff

The direct vanilla precedent is `gfx/entities/units_infantry.asset#infantry_2_entity` and its machine-gun entities, where firing events carry `node="muzzle"`, `mg_muzzle_particle`, `mg_muzzle_smoke_particle`, `mg_muzzle_flash`, and an MG sound at the action event time.

The current parent-owned robot entity has only sound events: attack and support attack both use `autonomous_robot_dual_mg_attack_sfx` at normalized `0.3333`; no node, particle, or light event is present.

After action evidence exists, the parent should bind one firing event per retained locator (`muzzle` and `muzzle_left`) at the measured discharge phase, with muzzle flash particle, smoke particle, light, and the sourced dual-MG sound, while preserving the existing entity scale and animation identifiers.

The existing source audio package is documented in `evidence/audio/source_plan.md` and `evidence/audio/source_ledger.md`.

The selected exact-weapon source is Lubini, `MG 42 (Solo) WW2.wav`, source page `https://freesound.org/people/Lubini/sounds/338242/`, CC BY 4.0; the archived preview is `evidence/audio/original/mg42_solo_ww2_hq_preview.mp3` SHA-256 `F95EB1B9FE8E5889D56BD68CA602472B751FA3D287E708F229DFF0827BD6F9FC`.

The current dual-MG derivative is `evidence/audio/derived/autonomous_robot_dual_mg_attack.ogg` SHA-256 `B4FC7793C3D66A9415552BD3044BC40DC3809D911E2EF4186E3D55632E5BEB41`; its proposed burst start at frame 8 is not accepted until the repaired attack/support actions are measured.

The remaining sourced roles are selection acknowledgement, movement servo, idle loop, footfall/armored impact, and death/destruction, with original and derived hashes recorded in the audio ledger; no synthesized or placeholder sound is permitted.

Selection acknowledgement remains a capability-limited parent-owned consumer: vanilla infantry voice selection is country/original-tag based rather than a per-subunit entity hook. The package must not replace global infantry voices or masquerade idle as selection; the lack of a proven per-subunit selection hook is an explicit engine capability exclusion, not by itself a blocker for the supported roles.

## Counter and material boundary

Existing bespoke counter art is retained and must not be regenerated.

The large counter is `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds` SHA-256 `147CF90C3D053947640F7865F1DADE6D8FFABA99942E8401ED4575D53DB61B09`.

The on-map counter is `gfx/interface/counters/divisions_small/onmap_unit_autonomous_robot_icon.dds` SHA-256 `BDEB527F8A73494B918ADEC27C26AEC97C299F51AD00D2DA2946A37A278EDD4B`.

The installed vanilla definition `interface/subuniticons.gfx`, matching vanilla medium-tank/mechanized and on-map reference families, sampled green palette, frame sizes, alpha behavior, and counter handoff are documented in `evidence/counter/validation/reference_inspection.md` and `evidence/counter/gfx_handoff.md`.

No material or counter mutation is authorized in this recovery pass.

## Unresolved gates and parent work

The live route is verified at 1.10.19 through the approved fresh-process wrapper client; the attached interactive MCP registration remains stale but was not used. No worker process is currently in flight.

The manual candidate must first pass the missing quaternion-only source-channel conversion, then receive a substantive, byte-distinct defend action and genuine attack/support aim-discharge-recoil-recovery semantics. The attack phase plan is concrete, but the target sibling checkpoint does not yet exist.

All eight actions require export and actual-byte reimport evidence at the FPS proven by the actual binding profile; the current candidate is native 30 FPS, and current actual-byte reimports cover only idle, attack, and death, which are not final semantic approvals.

The existing locator names need exporter-supported registration and parent/world-position proof at attack/support discharge frames.

Parent-owned runtime entity effects, exact particle/light nodes, normalized sound timing, GFX/runtime promotion, and live consumer validation remain pending.

The old job manifest and historical Meshy6/provider claims remain lineage history; they must not be used to justify regeneration or to claim the manual candidate is runtime-complete.

The current exact capability blocker is the worker’s fail-closed rejection of native `rotation_euler`/other unsupported source channels in `autonomous_robot_attack`; individual paths are not exposed by `inspect_scene`, and no conversion operation is currently available. Parent review is required before any adapter change or further action call.

No credits were estimated or consumed in this pass, no provider task id exists for this pass, and no final runtime promotion is claimed.
