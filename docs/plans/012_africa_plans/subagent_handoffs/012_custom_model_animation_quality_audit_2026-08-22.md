# Repo Explorer Handoff

# Event 012 Custom Model Animation Quality Audit — 2026-08-22

> Disposition: `superseded` for the elephant portion (2026-08-27). The explicit user direction recorded in [the vanilla-elephantry reuse handoff](012_africa_elephant_vanilla_elephantry_reuse_2026-08-27.md) replaces the custom elephant runtime path.
>
> Treat the elephant-specific counts, rows, paths, findings, and recovery recommendations below as historical evidence only; they do not authorize custom model, entity, skeletal-action, sound, or counter work. Use [Event 012 armoured elephant warfare](../../../events/012_africa/elephant_warfare.md), [Event 012 elephant visual disposition](../../../systems/3d_model_pipeline/chaosx_africa_elephant_model.md), and [the vanilla-elephantry reuse handoff](012_africa_elephant_vanilla_elephantry_reuse_2026-08-27.md) as the current source-of-truth documents.
>
> The remaining strange-force audit is retained as historical evidence and remains outside this elephant disposition. Retention or deletion of the approximately 340 MB evidence package remains an owner decision outside this documentation-only pass.

## Scope read

- Parent task: Audit the runtime skeletal animation packages for the eight Event 012 Africa strange-force models and the shared elephant model.
- Explicit constraints: This was a read-only audit. Runtime gameplay, model, animation, GFX, entity, evidence, and documentation files were not edited, and no commit was created.
- Files or ids requested: gfx/models/units/012_africa_*, gfx/models/units/chaosx_elephants, matching animation .asset and entity .asset/.gfx files, and docs/assets/012_africa/models_3d/*.
- Skills or docs read: AGENTS.md; .agents/skills/chaos-redux-3d-model-pipeline/SKILL.md; .agents/skills/chaos-redux-event-assets/SKILL.md; .agents/skills/chaos-redux-subagents/SKILL.md; the relevant offline Paradox wiki pages under paradox_wiki/; the vanilla documentation files script_concept_documentation.md, effects_documentation.md, and triggers_documentation.md; the local 3D pipeline README, Meshy schema lock, dependency lock, asset profiles, and adapter configuration.
- Artifact URIs: No HOI4 MCP artifact URI was produced because the installed HOI4 Agent Tools route does not serve skeletal 3D model inspection. The local evidence paths below are the authoritative audit artifacts.
- Acceptance rule used: PASS requires a verified meshy_animate or explicitly approved professional animation source with source task/action lineage, Blender import/retarget evidence, actual .anim reimport evidence, and role-appropriate visual evidence. A runtime .anim file or an export report alone is not sufficient.
- HOI4 Agent Tools note: No focus, GUI, map, event, technology, or weighted-logic surface was in this 3D-animation-only audit, so no such route was applicable.

## Primary findings

- Historical audit inventory: nine pre-reuse runtime model packages exposed 46 required animation files, with five each for eight strange-force models and six for the custom elephant model.
- Historical audit finding: none of the 46 pre-reuse action surfaces had verified provider-action or professional-source lineage; the six custom elephant actions are not current requirements under vanilla reuse.
- All 40 actions in the eight existing evidence packages are explicitly labeled with the forbidden Blender-authored policy blender-authored-semantic-skeletal-action-no-scale-channels.
- The eight packages do have exported .anim files and structural reimport files, but their validation records use the generic action name io_pdx_rigAction and sample only three bounds frames rather than the required five loop phases or role-specific attack/death phases.
- The eight packages contain only Meshy 6 image-to-3D geometry requests. Their evidence roots contain no meshy_animate task, action id, provider animation response, or professional-source receipt.
- Before the reuse decision, the expected elephant evidence root docs/assets/012_africa/models_3d/elephant_shared_base/ was absent. The historical audit reported a runtime elephant mesh and six .anim files, but the current runtime does not use this custom package.
- No action-phase visual evidence was found in the historical audit. Each of the eight non-elephant packages had seven static geometry previews only, and the custom elephant had no package preview root.

## Compact counts

| Surface | Count | Classification | Reason |
| --- | ---: | --- | --- |
| Strange-force runtime packages | 8 | REDO | Every action report uses the forbidden Blender-authored policy. |
| Strange-force runtime actions | 40 | REDO | Runtime files and exports exist, but no approved provider/professional source is proven. |
| Strange-force actions needing additional grounding review in their existing reports | 26 | REDO | Secondary report status is needs_grounding_review; the other 14 still fail source provenance. |
| Historical custom elephant actions | 6 | SUPERSEDED | The pre-reuse runtime files and missing evidence root are retained as historical audit evidence; vanilla `elephantry` is the current visual path. |
| Historical custom-runtime actions overall | 46 | N/A after reuse | The count includes six custom elephant actions that are no longer current requirements; the remaining 40 strange-force actions retain their historical REDO finding. |
| Historical evidence package missing at audit time | 1 | ARCHIVAL | `elephant_shared_base` was absent from the historical audit workspace and is not a current acceptance dependency. |

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| gfx/entities/012_africa_strange_forces.asset | Runtime state-to-animation bindings for all eight strange-force entities. | Gorilla 6-17, Pan 21-34, Stone 38-49, Riverborn 53-65, Forest 69-81, Oracle 85-97, Disaster 101-114, and Plague 118-131. |
| gfx/entities/012_africa_strange_forces.gfx | Runtime mesh and animation type registrations for all eight strange-force models. | The eight pdxmesh blocks and animation registrations span lines 4-82. |
| gfx/models/units/animation_012_africa_strange_forces.asset | Maps the 40 semantic animation types to the actual runtime .anim files. | Gorilla 5-9, Pan 11-15, Stone 17-21, Forest 23-27, Oracle 29-33, Riverborn 35-39, Disaster 41-45, and Plague 47-51. |
| Historical pre-reuse `gfx/entities/chaosx_elephants.asset` | Historical state-to-animation bindings for the custom elephant entity. | Attack/defend/support_attack 10-34, move 37-42, deploy 45-50, supply_load 53-59, retreat 62-67, death 70-76, idle/training 79-90. |
| Historical pre-reuse `gfx/entities/chaosx_elephants.gfx` | Historical custom elephant mesh and animation registration. | The pdxmesh block and six animation types are at lines 4-21; the registration is retired from active loading. |
| Historical pre-reuse `gfx/models/units/chaosx_elephants/animation_chaosx_elephants.asset` | Historical mapping of the custom elephant animation types to .anim files. | Six definitions span lines 3-30; vanilla `elephantry` is the current visual path. |
| docs/assets/012_africa/models_3d/*/job.yaml | Package action lists, geometry provider model, geometry task id, FPS, and claimed reimport glob. | Eight jobs identify Meshy 6 geometry tasks and five required actions each; for example disaster_wardens lines 3-22 and gorilla_heavy_infantry lines 4-28. |
| docs/assets/012_africa/models_3d/*/provider/requests/image_to_3d_attempt_1.json | Direct provider request evidence. | Requests identify Meshy 6 image_to_3d with GLB/FBX or T-pose geometry output, not animation. Disaster lines 2-7 are representative; plague uses the nested arguments at lines 2-27. |
| docs/assets/012_africa/models_3d/*/blender/reports/creature_action_*.json | Direct action-authoring evidence for the eight existing packages. | All 40 reports use the forbidden policy. Disaster idle lines 2, 5-7, and 765-768 are representative. |
| docs/assets/012_africa/models_3d/*/blender/reports/retime_animation_*.json | Shows the later FPS retime route and whether a provider action or rig was created. | Disaster idle lines 15-19 report new_provider_call false, new_rig_created false, and source_fps 24 to target_fps 30. |
| docs/assets/012_africa/models_3d/*/export/anim/*.anim and *.txt | Actual exported animation bytes and parser text. | There are 40 exported .anim files and 40 parser text files across the eight packages. Parser text records FPS, frame count, bone count, and channels, but not a provider source id. |
| docs/assets/012_africa/models_3d/*/validation/reimport_*_runtime.json | Structural reimport evidence for the eight packages. | There are 40 files. Every one reports actions = io_pdx_rigAction, three animation-bounds samples, a proof_blend, and no warnings. Disaster idle lines 2-5, 6-61, 65, and 151 are representative. |
| docs/assets/012_africa/models_3d/*/blender/previews/ | Visual evidence inventory. | Each of the eight packages has exactly seven static front/left/rear/right/three_quarter/top/underside geometry images and no action-phase image. |
| docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_shared_model_2026-08-05.md | Historical pre-reuse elephant package handoff. | Lines 3 and 7-14 retain the claimed package root, six actions, custom 17-bone rig, and Meshy task id; the handoff is superseded by the linked vanilla-reuse sources. |
| .tools/3d_pipeline/config/meshy_tool_schema.lock.json | Current locked provider action contract. | meshy_animate requires rig_task_id and action_id at lines 152-155; the verified pilot action ids listed at lines 163-167 are idle 0, attack 4, and death 8. |
| .tools/3d_pipeline/config/asset_profiles.json | Stale profile route that conflicts with the current no-manual-animation policy. | The nonhumanoid profile still declares authoring_route = blender_authored_skeletal at lines 286-321. |

## Runtime/action matrix

| Runtime model and runtime files | Required and present actions | Provider/action lineage | Blender route and current report result | Reimport evidence | Visual evidence | Class and geometry/rig reuse |
| --- | --- | --- | --- | --- | --- | --- |
| 012_africa_gorilla_heavy_infantry; gfx/models/units/012_africa_gorilla_heavy_infantry/ | chaosx_gorilla_idle, move, attack, recovery, death; all five are present and registered by animation_012_africa_strange_forces.asset 5-9. | Meshy 6 geometry task 019fd7f3-6f53-73d5-a5d3-1f46256b2759 in job.yaml 4-5 and the image_to_3d request; no action task or professional source id. | creature_action_*.json all use blender-authored-semantic-skeletal-action-no-scale-channels; attack, death, idle, and move are needs_grounding_review, recovery is pass. | Five exported .anim files, five parser files, five validation JSON files, and five reimport .blend files exist. Validation still names io_pdx_rigAction and samples three bounds frames. | Seven static geometry previews; no attack, recovery, locomotion, death, or reimport motion render. | REDO. Existing Meshy6 GLB/FBX and the 17-bone custom rig are candidates for retargeting, not accepted final source. |
| 012_africa_pan_sappers; gfx/models/units/012_africa_pan_sappers/ | chaosx_pan_idle, move, sabotage, construction, death; all five are present and registered at animation_012_africa_strange_forces.asset 11-15. | Meshy 6 geometry task 019fd7f9-ee23-7510-82c6-7685ec2e3089 in job.yaml 3-4 and the image_to_3d request; no action task or professional source id. | All action reports use the forbidden Blender-authored policy; sabotage and idle are needs_grounding_review, death/construction/move are pass. | Five exported .anim files, parser files, validations, and reimport .blend files exist, with the same generic action and three-sample limitation. | Seven static geometry previews only. | REDO. Preserve the existing geometry/rig for a provider retarget attempt after the Meshy7/custom-rig route is verified. |
| 012_africa_stone_cohorts; gfx/models/units/012_africa_stone_cohorts/ | chaosx_stone_idle, move, attack, collapse_recovery, death; all five are present and registered at animation_012_africa_strange_forces.asset 17-21. | Meshy 6 geometry task 019fd7ae-83a0-792c-8a2e-c1199c678f6d in job.yaml 3-4 and the image_to_3d request; no action task or professional source id. | All action reports use the forbidden Blender-authored policy; attack, death, idle, and move are needs_grounding_review, collapse_recovery is pass. | Five exported .anim files, parser files, validations, and reimport .blend files exist, with the same generic action and three-sample limitation. | Seven static geometry previews only. | REDO. Existing custom rig is a candidate target, but its Meshy6 origin does not satisfy the current Meshy7 geometry route by itself. |
| 012_africa_riverborn; gfx/models/units/012_africa_riverborn/ | chaosx_riverborn_idle, move, attack, water_transition, death; all five are present and registered at animation_012_africa_strange_forces.asset 35-39. | Meshy 6 geometry task 019fd806-2e78-78aa-8876-fca8862d729d in job.yaml 3-4 and the image_to_3d request; no action task or professional source id. | All action reports use the forbidden Blender-authored policy; attack and death are needs_grounding_review, water_transition/idle/move are pass. | Five exported .anim files, parser files, validations, and reimport .blend files exist, with the same generic action and three-sample limitation. | Seven static geometry previews only. | REDO. Try to retain the current geometry and custom rig for approved retargeting; regenerate or re-rig only if the verified provider route rejects it. |
| 012_africa_forest_giants; gfx/models/units/012_africa_forest_giants/ | chaosx_forest_giant_idle, move, attack, concealment_emergence, death; all five are present and registered at animation_012_africa_strange_forces.asset 23-27. | Meshy 6 geometry task 019fd806-1803-7d29-9e52-82c49d6c7a2d in job.yaml 3-4 and the image_to_3d request; no action task or professional source id. | All action reports use the forbidden Blender-authored policy; attack, death, idle, and move are needs_grounding_review, concealment_emergence is pass. | Five exported .anim files, parser files, validations, and reimport .blend files exist, with the same generic action and three-sample limitation. | Seven static geometry previews only. | REDO. The existing custom 17-bone rig is a reuse candidate, but nonhumanoid Meshy7 animation compatibility is not proven. |
| 012_africa_oracle_recon; gfx/models/units/012_africa_oracle_recon/ | chaosx_oracle_idle, move, recon, observation, death; all five are present and registered at animation_012_africa_strange_forces.asset 29-33. | Meshy 6 geometry task 019fd806-23e2-7ecf-88e9-4d8e9e884a80 in job.yaml 3-4 and the image_to_3d request; no action task or professional source id. | All action reports use the forbidden Blender-authored policy; all five are needs_grounding_review. | Five exported .anim files, parser files, validations, and reimport .blend files exist, with the same generic action and three-sample limitation. | Seven static geometry previews only. | REDO. Preserve geometry/rig provisionally; obtain a real recon/observation action source rather than aliasing one motion. |
| 012_africa_disaster_wardens; gfx/models/units/012_africa_disaster_wardens/ | chaosx_disaster_warden_idle, move, rescue, containment, death; all five are present and registered at animation_012_africa_strange_forces.asset 41-45. | Meshy 6 geometry task 019fd806-39bf-7d2c-9c77-5dd1cad77011 in job.yaml 3-4 and the image_to_3d request; no action task or professional source id. | All action reports use the forbidden Blender-authored policy; death is needs_grounding_review, the other four are pass, but pass is not source acceptance. | Five exported .anim files, parser files, validations, and reimport .blend files exist, with the same generic action and three-sample limitation. | Seven static geometry previews only. | REDO. Review whether rescue is intentionally shared by combat and deploy; under the no-semantic-alias rule, distinct role sources may be required. |
| 012_africa_plague_carriers; gfx/models/units/012_africa_plague_carriers/ | chaosx_plague_carrier_idle, move, deploy, release_containment, death; all five are present and registered at animation_012_africa_strange_forces.asset 47-51. | Meshy 6 geometry task 019fd7b5-ab43-7715-8dc8-d4a3bc8fcabe in job.yaml 3-4 and the nested image_to_3d request lines 8-27; no action task or professional source id. | All action reports use the forbidden Blender-authored policy; death/deploy/idle/move are needs_grounding_review, release_containment is pass. | Five exported .anim files, parser files, validations, and reimport .blend files exist, with the same generic action and three-sample limitation. | Seven static geometry previews only. | REDO. Review whether deploy being used for combat and deploy is an unacceptable semantic alias; obtain distinct provider/professional roles if required. |
| Historical pre-reuse `chaosx_elephants`; `gfx/models/units/chaosx_elephants/` | Historical audit observed `chaosx_elephant_idle`, move, deploy, supply_load, attack, and impact .anim files registered by `animation_chaosx_elephants.asset` lines 3-30. | Only the historical handoff claims Meshy task 019fd212-8909-765a-a4f0-70294b8ff7f3 at `012_africa_elephant_shared_model_2026-08-05.md:13`; no provider request/response, rig task id, action id, Blender action report, or professional-source receipt survived under the expected root. | Historical `UNVERIFIABLE` finding; the custom registration is retired and no current authoring route is required. | No evidence-root export parser, validation JSON, or reimport .blend survived; runtime files alone did not establish reimport proof. | No elephant evidence preview root survived. | `SUPERSEDED` by vanilla `elephantry`; do not recover or regenerate this package as a current Event 012 target. |

## Existing patterns

- The eight strange-force packages follow a common candidate path: Meshy 6 image-to-3D GLB/FBX, Blender custom rig, authored action checkpoint, FPS retime, PDX export, and reimport validation.
- Each of those packages has a reported 17-bone custom armature and provider source downloads, so the existing geometry and rig can be retained as a provisional retarget target rather than discarded immediately.
- The action report pattern is internally consistent about its forbidden source policy, even when the manifest and retime reports describe the output as complete.
- The runtime entity pattern mirrors vanilla state-to-animation wiring, including standard attack/defend/support_attack, retreat, idle, and training state reuse.
- Non-standard role reuse needs separate review. Disaster binds rescue to combat and deploy, plague binds deploy to combat and deploy, and pan binds construction to deploy and supply_load. Those bindings may be normal engine state sharing, but they are not proof of distinct substantive motions and conflict with the stated no-semantic-alias acceptance rule unless explicitly approved.
- Every package manifest calls the motion “four authored skeletal actions” while listing five actions and the filesystem contains five action reports, exports, validations, and reimport checkpoints. This is stale evidence metadata.

## Geometry and rig reuse decision

- Disaster wardens, forest giants, gorilla heavy infantry, oracle recon, pan sappers, plague carriers, riverborn, and stone cohorts each have Meshy 6 GLB/FBX downloads and a reported custom 17-bone rig under provider/downloads and blender/reports/creature_rig.json. These are reusable candidates for a verified provider-action retarget pass, not accepted final animation packages.
- Reuse should be attempted only after a live locked Meshy7 route confirms that the existing custom nonhumanoid skeleton can receive the provider action. The locked meshy_animate contract requires a rig_task_id and action_id, neither of which is present in these packages.
- If Meshy7 cannot animate the custom nonhumanoid rig, use an explicitly approved professional creature source and retarget it in Blender, or regenerate/rerig through the authorized route. Do not hand-key a replacement, apply a whole-rig transform, freeze a static pose, or alias another semantic role.
- The elephant row records the pre-reuse audit state only; the explicit 2026-08-27 decision supersedes recovery or regeneration and routes `chaosx_elephant` to vanilla `elephantry`. No custom elephant action work is queued.
- Meshy 6 is also not the current locked geometry acceptance route. The current skill requires Meshy 7 for image-to-3D, so all existing Meshy 6 geometry is a source candidate only.

## Vanilla or reference precedents

- Vanilla C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset:12-39 demonstrates the normal entity state-to-animation mapping and separate attack, support_attack, retreat, death, idle, and training roles.
- Vanilla C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_cavalry.asset:94-107 demonstrates a nonhumanoid horse entity with explicit idle, move, attack, support_attack, retreat, training, and attachment states.
- Vanilla C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/animation.asset:29-53 demonstrates animation type names mapped to actual .anim files.
- These vanilla files prove the engine wiring shape only. They do not prove provider action lineage or make a static/procedural Blender action acceptable.

## Likely edit order for the parent

1. Keep the eight strange-force packages out of animation-quality PASS and runtime activation until every required role has approved source lineage and visual evidence; the superseded elephant package is not part of this gate.
2. Do not recover or regenerate the superseded elephant package; retain its provenance and validate only the vanilla `elephantry` consumer when the parent performs live validation.
3. For one pilot creature, obtain a verified Meshy7 meshy_animate action using a recorded rig_task_id and action_id, or obtain explicit approval for a professional source if the provider library cannot cover the nonhumanoid role.
4. Retarget and clean only the approved source in Blender, preserving substantive source motion and applying only permitted contact, root, scale, bake, and export operations.
5. Repeat for every semantic role, including distinct special roles where runtime bindings currently reuse one action for combat and deploy or for deploy and supply_load.
6. Reimport the actual exported .anim files against the exported mesh and retain parser output, hashes, and proof blends.
7. Add role-appropriate rendered evidence: first, quarter, middle, three-quarter, and last for loops; aim/discharge/recoil/recovery for attack; and collapse/impact/settling for death.
8. Synchronize manifests, runtime handoffs, action names, FPS, reimport counts, provider ids, and runtime hashes only after the action package passes the evidence gate.

## Validation checks

- Confirm historical runtime presence and exact semantic coverage for the eight strange-force packages with: Get-ChildItem gfx/models/units/012_africa_* -Recurse -File -Filter *.anim; the superseded elephant path is intentionally excluded.
- Confirm historical runtime bindings and semantic aliases for the eight strange-force packages with: rg -n 'state =|animation =|pdxmesh =' gfx/entities/012_africa_strange_forces.asset; do not treat the retired elephant entity file as a current consumer.
- Confirm every action has an approved provider or professional source id with: rg -n -i 'meshy_animate|provider.?action|action.?task|professional.?source|action_id|rig_task_id' docs/assets/012_africa/models_3d.
- Confirm no forbidden authoring policy remains with: rg -n 'blender-authored|authoring_route.*blender_authored|whole.?rig|static.?pose|semantic.?alias' docs/assets/012_africa/models_3d .tools/3d_pipeline/config/asset_profiles.json.
- Confirm provider requests are action requests rather than geometry-only requests by inspecting provider/requests and provider/responses for every package and requiring an action task/action id paired with the geometry task.
- Parse every approved exported .anim through the locked io_pdx_mesh route and require the semantic action name, expected frame rate, expected frame range, armature, root policy, and export checksum in the report.
- Require five sampled loop phases and role-specific non-loop phase evidence, then compare decoded poses or actor bounds rather than relying on a static preview or three bounds samples.
- Hash every runtime .anim against the approved export and record the runtime path in the handoff.
- Reconcile all manifest claims of four actions or four reimports against the actual five-action package shape before parent integration.
- Do not verify or recreate the superseded elephant evidence root as an acceptance gate; it is archival/non-promoted, and retention or deletion is an owner decision.

## Risks and blockers

### Confirmed blockers

- No verified Meshy action or professional-source lineage existed for the 40 strange-force actions in this historical audit; custom elephant actions are no longer required under vanilla reuse.
- All 40 existing strange-force action reports explicitly identify Blender-authored semantic skeletal actions, which the current pipeline policy forbids as final motion.
- The historical elephant evidence root was absent even though runtime files and a dated handoff claimed it existed; this is no longer a current blocker because custom elephant visuals are not required.
- The eight evidence packages use Meshy 6 geometry requests, while the current skill requires Meshy 7 for geometry acceptance.
- The locked meshy_animate schema requires rig_task_id and action_id, but the eight package jobs record only image-to-3D geometry task ids; the superseded elephant package has no surviving machine-readable job, which is archival context rather than a current dependency.
- No action visual evidence proves loop phases, attack phases, death phases, or creature ground-contact behavior.
- Package metadata is contradictory: manifests and handoffs claim four actions or four reimports while five of each actually exist, and some blocker notes claim that provider/export work never occurred despite the present artifacts.
- The forest dependency note says its gate failed before provider request or export at docs/assets/012_africa/models_3d/forest_giants/evidence/dependency_route_blocker.md:5-9 and 41-55, while the same package contains Meshy requests, Blender reports, exports, and runtime files.
- The gorilla dependency note confirms meshy_animate is only a declared tool and says no paid provider task was started at docs/assets/012_africa/models_3d/gorilla_heavy_infantry/evidence/dependency_verification.md:13-14 and 42-45, which does not explain the existing Meshy6 geometry and action artifacts.
- The pan blocker explicitly says no provider task, Blender mutation, or export occurred at docs/assets/012_africa/models_3d/pan_sappers/evidence/dependency_route_blocker.md:3-5, while the package has five authored reports and exports.
- The stone intake blocker says animation-critical operations were unavailable and work stopped before export at docs/assets/012_africa/models_3d/stone_cohorts/validation/intake_blocker.md:7-9, which conflicts with its present runtime candidate and reimport files.

### Ordinary risks

- Meshy animation compatibility with these custom nonhumanoid 17-bone rigs is not established by repository evidence and must be checked on the locked live route before batch work.
- Runtime state aliases may hide missing substantive roles, especially rescue combat/deploy, plague deploy combat/deploy, and pan construction deploy/supply_load.
- Existing retime reports claim an “existing provider action” while also reporting new_provider_call false and no provider action artifact is present. This is lineage contradiction, not provider evidence.
- Idle action reports are 24 FPS while job manifests and exported parser files are 30 FPS, so the source and final timing contract must be revalidated after redo.
- The nonhumanoid profile still contains authoring_route = blender_authored_skeletal, which is stale against the current no-manual-animation rule and can reintroduce the same failure if not corrected by the implementation owner.

## Recommended next action

Keep the eight strange-force runtime model packages blocked from animation PASS. Do not recover or regenerate the superseded elephant evidence package; the parent should validate the vanilla `elephantry` consumer separately, then run one representative strange-force creature through the verified Meshy7 `meshy_animate` or explicitly approved professional-source route with complete action lineage, reimport, and five-phase visual evidence before batching the remaining 39 actions.
