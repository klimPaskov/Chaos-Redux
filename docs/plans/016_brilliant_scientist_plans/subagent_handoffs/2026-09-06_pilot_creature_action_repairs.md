# Pilot creature action repairs

Status: requested 3D action repairs and corrected gloss DDS derivatives complete; parent runtime promotion and source-to-runtime hash verification completed on 2026-09-08; overall package acceptance remains blocked by the inherited limitations listed below.
Disposition: implemented in the current runtime under the accepted user-authorized Blender repair scope; runtime evidence is reconciled in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/2026-09-08_pilot_creature_runtime_integration.md`.
Authoring model: GPT-6-astra.
New Meshy calls, estimated credits and consumed credits: 0.

The accepted scope is `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md`.
This repair preserves existing fictional game creature geometry, dedicated rigs, valid actions, model textures, sourced audio and counter packages.
All new action names and checkpoints are siblings of the accepted sources.
No runtime, entity, GFX, sound definitions, gameplay, shared adapter or dependency files are owned by this worker.
The parent owns runtime copies, bindings, source-to-runtime hash comparison, visual acceptance and commits.

## Paleogenetic creature

Job root: `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature`.
Accepted source: `blender/checkpoints/current_locked_2026_09_04_material_working.blend`, SHA-256 `328BB6010887526CFECC2216C466125834339A51271D340A0D09D76F4B240813`.
Accepted mesh: `export/current_locked_2026_09_04_material/chaosx_paleogenetic_creature.mesh`, SHA-256 `050C0B461050D86203C80A08C8E84C942BDB518B187BD59E7AD1BEBE7E0ECEF7`.
Dedicated rig: `paleogenetic_creature_rig`, 20 bones using their original XYZ Euler channels.
Final authored checkpoint: `blender/checkpoints/stalk_blender_repair_20260906.blend`, SHA-256 `9C35AB68B60CFFB0EC0C0732B212A7AEBC3F6054CD8050BBA49BD6F3AA4A210C`.

The seven accepted promoted roles are idle, move, attack, defend, support_attack, retreat and death.
Charge and roar had duplicate payloads and wounded duplicated defend.
Stalk had a distinct payload but actual-byte baseline reimport and frame 13/37 pose inspection showed stationary legs and feet apart from common vertical motion; it is also replaced.
New actions are `paleogenetic_creature_<role>_blender_repair_20260906` for charge, roar, wounded and stalk.
These four roles plus the seven preserved roles cover the eleven requested semantics.

| Role | Authored phases at 24 FPS | Loop | Intended motion |
| --- | --- | --- | --- |
| charge | ready 0, compress 6, drive 18, brake 36, recovery 48 | no | Forward body compression, alternating leg drive, four-arm counter swing, braking and recovery. |
| roar | ready 0, inhale 12, vocal peak 24, release 36, recovery 48 | no | Chest, neck and head extension with distinct four-arm flare and release. |
| wounded | ready 0, impact 8, recoil 16, brace 30, recovery 48 | no | Asymmetric recoil, protective left-arm curl, right-arm brace and staggered recovery. |
| stalk | left contact 0, left passing 12, right contact 24, right passing 36, loop end 48 | yes | Cautious alternating foot placements, low torso lean, head scan and independent forelimb movement. |

The body remains 14,928 vertices and 29,999 triangles, with four normalized influences per vertex and no zero-weight vertices in the accepted source.
The existing small boundary-edge limitation is retained: 59 edges in 15 closed boundary components, with no new topology repair in this action-only scope.
The calibrated source height is 7.3518238068; accepted entity scale 1.35 gives effective height 9.9249627827, 1.6875 times the vanilla infantry effective height.
Axes remain -Y forward and +Z up.

Current runtime consumer: `paleogenetic_creature`, entity `chaosx_paleogenetic_creature_entity` and alias `paleogenetic_creature_entity`.
The parent should bind the four distinct action exports without replacing the seven accepted roles or the accepted mesh/material files.
Source and package provenance remain in `job.yaml`, `manifest.md`, `runtime/handoff.md` and `evidence/pilot_blender_repair_20260906/immutable_source_ledger.json`.
The CC0 Mutant Cook source by Gman2099 at <https://opengameart.org/content/mutant-cook> remains non-shipping evidence.
Historical Meshy 7 generation task `01a0427d-0a5f-746f-8270-f64b4ba409c1` and rejected rig task `01a04285-34b0-7d0f-b256-e2c3f0048d67` are preserved lineage, with no provider call in this repair.

The existing CC0 Monster Sound Effects 2 source by Ogrebane at <https://opengameart.org/content/monster-sound-effects-2> remains unchanged.
Role-specific audition, trimming and selection consumer isolation remain the existing audio blockers; this worker created no audio.
Suggested synchronization follows the named phases above: charge steps 6/18/30/42, roar onset 12 and peak 24, wound impact 8, stalking contacts 0/24.
Use times measured from source frame 0; the equivalent reimport frame is source frame +1.
Existing bespoke counter tokens remain `GFX_unit_paleogenetic_creature_icon_medium` and `GFX_unit_paleogenetic_creature_icon_medium_white`, with their accepted large 152×42 and map 60×12 two-frame strips preserved.

## Xenobiological assault organism

Job root: `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism`.
Accepted source: `blender/checkpoints/07_materials_pdx.blend`, SHA-256 `DBBB4DD2ADE5AB794327E78BD899BE604DCDD1BE85D70C1DF4F4F2DA122C9884`.
Accepted mesh: `export/final/xenobiological_assault_organism.mesh`, SHA-256 `5561F2ED172359508605B1A1944EC62B8CCC35C04C4DECFE58F1B2CA19900781`.
Dedicated rig: `xenobiological_assault_rig`, 24 bones using their original XYZ Euler channels.
Final authored checkpoint: `blender/checkpoints/retreat_blender_repair_20260906.blend`, SHA-256 `87FAAEFDA6FD173971A8962114D6DD9CA721027F0A4E674D8B63F06A1AD01C82`.

The eight accepted roles idle, crawl, move, attack, defend, leap, wounded and death remain preserved.
New actions are `xenobiological_assault_organism_<role>_blender_repair_20260906` for support_attack and retreat, completing the ten requested semantics after validation.

| Role | Authored phases at 24 FPS | Loop | Intended motion |
| --- | --- | --- | --- |
| support_attack | brace 0, track 12, left primary-claw contact 24, right primary-claw contact 36, recovery 48 | no | Alternating forward primary-claw strikes, upper shoulder-claw guards, thorax twist, head tracking and antenna response. |
| retreat | disengage 0, withdrawal 12, loop recovery 48; alternate step at 36 | yes | Backward stepping through six leg bones while claws guard forward and the head scans. |

Numeric rest-basis review corrected the draft primary-arm rotation signs before Blender authoring so the strikes reach toward world -Y.
At the left contact, the primary claw tip advances from Y -0.693 to -2.267; the right contact advances its tip to Y -2.193.
The body remains 14,994 vertices and 30,000 triangles, with four normalized influences per vertex, no zero-weight vertices and no boundary, degenerate or nonmanifold faces in the accepted source.
Source height 9.514125824 with accepted entity scale 0.8 gives effective height about 7.61130066, 1.294117647 times the vanilla infantry effective height.
Axes remain -Y forward and +Z up.

Runtime identifiers should follow `chaosx_xenobiological_assault_<role>` for the two new bindings, with existing mesh `chaosx_xenobiological_assault_mesh` and entity `chaosx_xenobiological_assault_entity`.
The accepted actual-byte reimport shows tan chitin, pale skull, black claws and red eyes; the native material checkpoint's chrome-looking preview is not the material acceptance view.
Keep the original accepted packed DDS maps and use the actual-byte mesh reimports for material review.
The CC-BY 3.0 Insect Humanoid source by tidbit at <https://opengameart.org/content/insect-humanoid> remains non-shipping evidence; historical provider task receipts were already missing and are not reconstructed or invented here.

Existing licensed cicada, hiss, thud and joint-crack originals and PCM16 mono 44.1 kHz derivatives remain unchanged.
Synchronization handoff: support primary contacts at source frames 24/36 (1.0/1.5 seconds), preparatory joint motion at 12 (0.5 seconds), retreat foot contacts at 12/36 (0.5/1.5 seconds), with ambient loop continuous.
Auditory review and final consumer isolation remain parent-owned existing limitations.
The accepted bespoke green large and map counter strips remain unchanged; hashes are in the preserved payload and inherited package ledgers.

## Evidence and validation limits

Each package owns `evidence/pilot_blender_repair_20260906/` with immutable source hashes, accepted payload hashes, baseline geometry/material/rig/weight inspection, native action channel inventory, numeric rest-bone matrices, manual pose tables, hash-bound requests and exact adapter receipts.
Authored checkpoints use explicit bone locations and native rotations, linear keys at deliberate role phases, closed endpoint poses for loops, and in-place horizontal motion with a per-frame vertical ground correction.
Every authored frame measures its lowest point at Z 0.001 within floating-point tolerance; all six changed roles also pass actual-byte reimport grounding at frames 1, 13, 25, 37 and 49, with additional charge/wounded/strike/retreat phase evidence.
The locked wrapper route is `.tools/3d_pipeline/wrappers/run_blender_hoi4_adapter.cmd`, called through `BlenderAdapterClient.call` when the session tool catalog is stale.
Successful author calls used adapter 1.10.22, Blender 5.1.2 build `ec6e62d40fa9`, and the repository-selected io_pdx_mesh route.
Source-lock mismatches during shared adapter edits correctly prevented subsequent operations until parent re-lock.
The first xenobiological export wrote animation bytes but failed its automatically named report because the path exceeded the Windows path limit; its error is preserved under request `bc6b9a8624014489b7e40516d5ece571` and reported to the parent-owned adapter recovery worker.

The offline core wiki pages, Graphical asset modding, Entity modding and Unit modding were consulted alongside installed vanilla infantry/cavalry entities and relevant documentation.
Skills used: chaos-redux-3d-model-pipeline, chaos-redux-event-assets and chaos-redux-subagents.
No skill or shared tool/config file was changed by this worker.
No Hearts of Iron IV session was launched and no in-game completion is claimed.
No requested 3D role was simplified, omitted or replaced with an alias.
All original action exports remain unchanged, and the six replacements have unique payload hashes and genuine articulated motion.
The following final evidence supersedes the earlier in-progress export/report status.

## Final selected files and technical acceptance

Each new action is 24 FPS, source frames 0–48 inclusive, 49 exported samples, with a 2.0-second first-to-last sample span; imported frame numbers are source +1.
Loop closure is required and verified for paleo stalk and xeno retreat; charge, roar, wounded and support attack are one-shot actions with rest recovery.
Horizontal root translation is in-place; the authored per-frame vertical contact correction survives actual-byte export/reimport.

| Package | Role | Selected job-relative export | Bytes | SHA-256 |
| --- | --- | --- | --- | --- |
| paleogenetic_creature | charge | `export/actions_blender_repair_20260906/paleo_charge.anim` | 30443 | `30B3354CB0DD10E6E8966B89314B4EEAC3AA554D97ABB7E24824447EE578BC1B` |
| paleogenetic_creature | roar | `export/actions_blender_repair_20260906/paleo_roar.anim` | 26515 | `C5961F8131DFC20BCF8F6E308B1761E9D49686A9712C482B3AA236B626885AC8` |
| paleogenetic_creature | wounded | `export/actions_blender_repair_20260906/paleo_wounded.anim` | 30443 | `EBBE735DD8020170EDC36A41797461026F18AFE7AB0F463A63747A6CD9925F62` |
| paleogenetic_creature | stalk | `export/actions_blender_repair_20260906/paleo_stalk.anim` | 30443 | `0D66C4FA90662CC8DEF31A0E7995CAC004CA18BCCF15A50A87CB2E704A20DE72` |
| xenobiological_assault_organism | support_attack | `export/actions_blender_repair_20260906/xeno_support_attack.anim` | 32998 | `34C6915426CB5D7F9F5D922509049ED592CD807DC803A4345BBAB4A6EA590592` |
| xenobiological_assault_organism | retreat | `export/actions_blender_repair_20260906/xeno_retreat.anim` | 38890 | `ED6F53F0D48720737C0E4A9B978E1EE3508A85E847C7D31F1213273D82B226D1` |

The final action manifests are `evidence/pilot_blender_repair_20260906/action_manifest_blender_repair_20260906.json` in each job.
They record exact source checkpoints/hashes, new native-action hashes, frame/FPS/loop data, bone motion, original mesh hash, reimport checkpoint/hash, phase records, preview paths and author/export/reimport request IDs.
The paleogenetic comparison preserves all 53 baseline payloads, all 20 rest-bone matrices and Euler modes, original mesh/material data and vertex weights, every original action name and the inspected original native-action hash.
The xenobiological comparison preserves all 16 baseline payloads, all 24 rest-bone matrices and Euler modes, original mesh/material data and vertex weights, every original action name and the inspected original native-action hash.
Sources, provider maps, meshes and all old runtime actions remain immutable; new material derivatives are separate outputs.

Actual-byte ground ranges across the five standard samples are paleo charge 0.0009995364–0.0010001976, roar 0.0009996567–0.0009999014, wounded 0.0009996076–0.0009998586, stalk 0.0009997077–0.0009998605; xeno support attack 0.0009988572–0.0009991042 and retreat 0.0009987110–0.0009990279.
Additional joint-origin comparison against authored named phases has maximum error 0.00000190735 for paleo and 0.00000286103 for xeno.
The importer reconstructs display-bone tail lengths, so validation compares bone joint origins and actual deformed mesh views rather than treating imported display tails as authored endpoints.
Xeno support distal-claw joints reach Y -1.84034 at frame 25 on the left and -1.78130 at frame 37 on the right while foot joint XY positions remain fixed.
Xeno retreat swaps left/right foot-joint Y positions -0.75372 and +1.07796 between frames 13 and 37, with closed endpoint geometry and bone-key poses.
The expanded charge sheet contains frames 1/7/13/19/25/37/49 and shows the alternating stride phases; the wounded phase sheet contains exact impact, recoil and brace samples 1/9/17/31/49.
Detailed metrics are `actual_limb_metrics_blender_repair_20260906.json` beside the manifests.

## Corrected engine gloss textures

The parent explicitly added source-preserving correction of the old specular alpha convention during this repair.
Installed vanilla `gfx/FX/pdxmesh.shader` reads specular alpha as glossiness; both old package spec alphas tracked provider roughness.
The selected derivatives use R=0, G=32, B=provider metallic, A=255 minus provider roughness, with grayscale source channels resized once to the existing 1024-square budget before packing.
The immutable generation provider maps, base color and packed normal remain unchanged.
Repository `pack_pdx_material.py` and the skill-owned `convert_to_dds.py` produced the derivatives; strict one-level 32-bit BGRA headers, dimensions, payload length, exact decoded PNG equality, B metallic equality and A inversion equality pass.

| Package | Selected specular DDS matching the mesh binding | SHA-256 |
| --- | --- | --- |
| paleogenetic_creature | `export/material_blender_repair_20260906/paleogenetic_creature_spec.dds` | `2E13A6E4A76678D954989BD706A9872F8E59F297B1F8AA51517C4F4745AF138A` |
| xenobiological_assault_organism | `export/material_blender_repair_20260906/texture_specular.dds` | `972CAE334C8D2E016AE9CF042CE159E63FE85DE3640E0621F11F492A4766AB12` |

Each DDS is 4,194,432 bytes.
The same sibling material folder contains an exact byte copy of the accepted mesh and its unchanged diffuse/normal maps; `material_copy_provenance_blender_repair_20260906.json` records every copy.
Final material reimport used adapter 1.10.24 with `stage_default_textures=False`, preventing the old job-default map from overwriting the selected derivative.
Requests `661947b9d9174311aa5bf8bcaf245828` and `df4aebf82c6846a09a400ca29169ef10` retain and hash-record the selected paleo and xeno DDS files respectively.
Their sampled animation bounds exactly equal the corresponding prior action proofs.
The proof checkpoints are `blender/checkpoints/reimport_p_gloss_blender_repair_20260906.blend` and `blender/checkpoints/reimport_x_gloss_blender_repair_20260906.blend`.
The importer may feed packed alpha directly into Principled roughness; that preview convention is distinct from the engine gloss channel and cannot override the installed shader evidence.
New material views were reviewed for preserved diffuse identity, body shape and action deformation; they are not a claim of identical in-game lighting.

## Parent copy and binding contract

Each job now owns `evidence/pilot_blender_repair_20260906/runtime_copy_manifest_blender_repair_20260906.json`.
The manifests select 15 paleogenetic files covering mesh, three textures and eleven actions, and 14 xenobiological files covering mesh, three textures and ten actions.
They specify exact repository source paths, destination paths, SHA-256, bytes, entity/pdxmesh scales, animation names, roles, frames and source-to-import offsets.
Paleo destinations remain `gfx/models/units/paleogenetic_creature/`; the four new registrations follow `chaosx_paleogenetic_creature_<role>_animation` and the existing entity conventions.
Xeno destinations use the isolated `gfx/models/units/xenobiological_assault_organism/` folder so its generic DDS basenames cannot collide with another model.
Xeno registrations follow the inherited `chaosx_xenobiological_assault_<role>` names, `chaosx_xenobiological_assault_mesh`, `chaosx_xenobiological_assault_entity` and conventional `xenobiological_assault_organism_entity` alias for the parent-selected `sprite = xenobiological_assault_organism` consumer.
The parent should preserve existing accepted action loop bindings and use the explicit new loop policies in the manifest.
At manifest creation, five paleo destination payloads require changes (four actions and specular DDS); all fourteen xeno payloads require initial copying.
No runtime file has been copied by this worker.
On 2026-09-08 the parent copy was audited: all 15 paleogenetic and all 14 xenobiological destinations match the selected source SHA-256 values and byte counts, and the old blocked-role and roughness-alpha rows are superseded by this handoff plus the runtime-integration report.

## Final limits and remaining parent work

The requested creature action repairs and gloss derivatives have no remaining tool or asset-production blocker.
The Windows export-report failure was resolved by the parent-published adapter 1.10.24: xeno support export request `8282e96e0b964d6cb8031ef1ed380509` and retreat `7b12e3a56cb04670afcd54c785e6a0d9` both completed with clean receipts and unchanged animation bytes.
Final live discovery returned the reviewed 1.10.24 route and its reimport option; `dependency_final_blender_repair_20260906.json` and `live_tools_final_blender_repair_20260906.json` preserve lock/schema evidence.
The Blender bridge was independently reachable at 127.0.0.1:9876; Blender 5.1.2 build ec6e62d40fa9 and the repository-selected io_pdx_mesh 0.91.0 route were used.
The archive and deployed modernization are distinguished by the inherited dependency and parent reconciliation records, rather than falsely described as identical source files.
No required held object or firearm was declared or found missing for these two accepted creature identities; no geometry substitution or component omission was used.
The historical paleo boundary limitation, paleo audio-role audition/derivative gaps, xeno historical provider-receipt gaps and final auditory/consumer isolation limits remain explicit inherited package issues.
Existing licensed audio and bespoke counter packages were preserved; parent sound wiring should use the updated phase times above after the existing audio-role acceptance work.
No new sound was generated, no counter was replaced and no provider credit was spent.
All revised 3D roles are implemented without semantic aliases; no requested 3D simplification was made.
Documentation and runtime-hash reconciliation are recorded in the 2026-09-08 integration report; final audio/consumer acceptance and the user-owned live consumer check remain outside this worker completion claim.
