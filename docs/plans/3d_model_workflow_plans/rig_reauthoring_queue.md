# Rig and action re-authoring queue

Every repository Python path that created or edited bones, skin weights, or keyframes has been deleted from the 3D pipeline, and the pipeline policy now permits none.
The rigs, weight sets, and actions that those scripts produced remain in the shipped job evidence and runtime packages, so each affected model is queued here for genuine re-authoring live in Blender.
Nothing in this queue is deleted or unwired: the assets keep working until a re-authored replacement passes the acceptance rules and the parent wires it.

Acceptance basis: the user directed that no repository script may rig a model, that the shortcut scripts be removed, and that the models whose rigs and actions came from them be queued for re-authoring.
This document is the queue; it does not itself accept or reject any existing asset.

## Why these models are queued

The removed scripts generated skeletons from declarative specs, transferred or rewrote skin weights by rule, and synthesized, retimed, re-grounded, patched, or imported keyframes.
Work produced that way is exactly the shortcut output the policy forbids, so a re-authored result must be produced live in Blender and must satisfy the no-shortcuts rule in `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`.

## Evidence method

A job is listed when its evidence under `docs/assets/**` contains an executed-request marker (`"operation": "<removed operation>"`) or a report filename built from a removed operation name.
Files that merely echo the adapter's whole operation registry are not counted as proof by themselves.
Reported classes are derived from the specific removed operations found in that job's evidence, so a job listed for actions alone is not claimed to have a script-generated rig.

## Queued models (20)

| Job root | Removed operations found in executed evidence | Implicated artifacts | Evidence files |
| --- | --- | --- | --- |
| `002_zombie_outbreak/models_3d/zombies` | `author_measured_creature_action`, `author_measured_creature_rig`, `repair_explicit_skin`, `repair_explicit_skin_batch` | rig, skin weights, actions | 105 |
| `012_africa/models_3d/disaster_wardens` | `author_creature_action`, `author_creature_rig`, `correct_action_grounding`, `retime_animation_action` | rig, actions | 21 |
| `012_africa/models_3d/forest_giants` | `attach_rigid_component`, `author_creature_action`, `author_creature_rig`, `author_measured_creature_action`, `author_measured_creature_rig`, `correct_action_grounding`, `import_animation_action`, `retime_animation_action` | rig, actions, component assembly / scale | 114 |
| `012_africa/models_3d/gorilla_heavy_infantry` | `attach_rigid_component`, `author_creature_action`, `author_creature_rig`, `author_measured_creature_action`, `author_measured_creature_rig`, `correct_action_grounding`, `inspect_fitted_humanoid_source`, `retime_animation_action` | rig, actions, component assembly / scale, rig-source inspection only | 122 |
| `012_africa/models_3d/oracle_recon` | `author_creature_action`, `author_creature_rig`, `correct_action_grounding`, `import_animation_action`, `offset_action_root`, `retime_animation_action` | rig, actions | 113 |
| `012_africa/models_3d/pan_sappers` | `attach_rigid_component`, `author_creature_action`, `author_creature_rig`, `author_measured_creature_action`, `author_measured_creature_rig`, `correct_action_grounding`, `ground_existing_action`, `retime_animation_action`, `segment_creature_components` | rig, actions, component assembly / scale | 131 |
| `012_africa/models_3d/plague_carriers` | `attach_rigid_component`, `author_creature_action`, `author_creature_rig`, `author_measured_creature_action`, `author_measured_creature_rig`, `correct_action_grounding`, `retime_animation_action`, `segment_creature_components` | rig, actions, component assembly / scale | 87 |
| `012_africa/models_3d/riverborn` | `attach_rigid_component`, `author_creature_action`, `author_creature_rig`, `author_measured_creature_action`, `author_measured_creature_rig`, `correct_action_grounding`, `ground_existing_action`, `retime_animation_action`, `segment_creature_components` | rig, actions, component assembly / scale | 76 |
| `012_africa/models_3d/stone_cohorts` | `attach_rigid_component`, `author_creature_action`, `author_creature_rig`, `author_measured_creature_action`, `author_measured_creature_rig`, `correct_action_grounding`, `retime_animation_action` | rig, actions, component assembly / scale | 122 |
| `014_cannibalism/models_3d/cannibal_bone_guard` | `correct_action_grounding` | actions | 8 |
| `014_cannibalism/models_3d/cannibal_feast_cohort` | `correct_action_grounding` | actions | 8 |
| `014_cannibalism/models_3d/cannibal_island_reavers` | `correct_action_grounding` | actions | 8 |
| `014_cannibalism/models_3d/cannibal_march_predation_column` | `correct_action_grounding` | actions | 8 |
| `014_cannibalism/models_3d/cannibal_scavenger_warband` | `correct_action_grounding` | actions | 8 |
| `014_cannibalism/models_3d/cannibal_siege_eaters` | `correct_action_grounding` | actions | 8 |
| `016_brilliant_scientist/models_3d/alien_infantry` | `attach_rigid_component`, `author_measured_creature_action`, `author_measured_creature_rig`, `collapse_identity_leaf_joints`, `inspect_fitted_humanoid_source` | rig, skin weights, actions, component assembly / scale, rig-source inspection only | 63 |
| `020_black_plague/models_3d/rat_ground_unit_shared` | `correct_action_grounding`, `import_animation_action`, `retime_animation_action` | actions | 128 |
| `chaos_warfare_system/models_3d/chaos_assault_battalion` | `attach_rigid_component`, `author_measured_creature_action`, `correct_action_grounding`, `ground_existing_action`, `preview_explicit_skin_selection` | skin weights, actions, component assembly / scale | 157 |
| `shared_clone_system/models_3d/clone_infantry` | `attach_rigid_component`, `author_fitted_humanoid_action`, `author_fitted_humanoid_rig`, `author_measured_creature_action`, `author_measured_creature_rig`, `correct_action_grounding`, `inspect_fitted_humanoid_source`, `offset_action_root` | rig, actions, component assembly / scale, rig-source inspection only | 108 |
| `shared_robot_system/models_3d/autonomous_robot` | `attach_rigid_component`, `author_measured_creature_action`, `author_measured_creature_rig`, `correct_action_grounding`, `ground_existing_action`, `import_animation_action`, `patch_existing_humanoid_action_phases`, `retime_animation_action` | rig, actions, component assembly / scale | 138 |

## What re-authoring must produce

Re-authoring replaces the queued rig, weights, or actions with work produced in a live Blender session, then re-runs the export and reimport proof and updates the job checkpoint, runtime copy, and manifest for that artifact.
The replacement holds to the same rules as any new work: a complete anatomy-appropriate bone set, deliberately authored weights reviewed on the deformed mesh, real role motion with foot, prop, and weapon contacts verified, decoded or reimported proof of the delivered bytes, and no reuse of another model's evidence.
A queued model whose replacement cannot be produced to that standard stays `blocked` or `needs_user_review`; it is never closed with a shortcut.

## Naming that still refers to the removed scripts

42 plan and handoff documents under `docs/plans/` still describe work performed with the removed operations.
They are historical records of what was done, and they are superseded by this queue and by the pipeline policy; they are not implementation instructions and must not be replayed.

- `002_zombie_outbreak_zombies_plans/subagent_handoffs/2026-09-12_necrotic_geometry_actions.md` — `repair_explicit_skin`
- `002_zombie_outbreak_zombies_plans/subagent_handoffs/2026-09-12_undead_zombie_geometry_actions.md` — `preview_explicit_skin_selection`
- `002_zombie_outbreak_zombies_plans/subagent_handoffs/2026-09-12_variant_adapter_capability_brief.md` — `repair_explicit_skin`
- `002_zombie_outbreak_zombies_plans/subagent_handoffs/chaosx_3d_model_pipeline_handoff.md` — `correct_action_grounding`
- `002_zombie_outbreak_zombies_plans/subagent_handoffs/wendigo_zombies_meshy_package_handoff.md` — `author_creature_action`, `author_creature_rig`
- `002_zombie_outbreak_zombies_plans/subagent_handoffs/zombies_3d_pipeline_20260919.md` — `repair_explicit_skin`
- `010_death_ghost_hosts_plans/subagent_handoffs/chaosx_3d_model_pipeline_handoff.md` — `correct_action_grounding`, `import_animation_action`, `offset_action_root`, `retime_animation_action`
- `012_africa_plans/subagent_handoffs/012_africa_model_pan_sappers_2026-08-06.md` — `correct_action_grounding`, `import_animation_action`, `offset_action_root`, `retime_animation_action`
- `012_africa_plans/subagent_handoffs/012_africa_model_riverborn_2026-08-06.md` — `author_creature_action`, `author_creature_rig`, `author_locomotion_action`, `calibrate_creature_scale`, `correct_action_grounding`, `offset_action_root`, `segment_creature_components`
- `012_africa_plans/subagent_handoffs/012_africa_model_stone_cohorts_2026-08-06.md` — `author_creature_action`, `author_creature_rig`, `author_locomotion_action`, `calibrate_creature_scale`, `correct_action_grounding`, `import_animation_action`, `offset_action_root`, `retime_animation_action`, `segment_creature_components`
- `012_africa_plans/subagent_handoffs/012_africa_pan_sappers_meshy7_redo.md` — `author_creature_rig`
- `012_africa_plans/subagent_handoffs/012_africa_plague_carriers_meshy7_redo.md` — `author_creature_action`, `author_creature_rig`, `segment_creature_components`
- `012_africa_plans/subagent_handoffs/disaster_wardens_action_redo_blocked_2026-08-22.md` — `correct_action_grounding`, `import_animation_action`, `retime_animation_action`
- `014_cannibalism_plans/subagent_handoffs/event014_bone_riders_paid_v9.md` — `calibrate_creature_scale`, `correct_action_grounding`, `import_animation_action`, `retime_animation_action`, `segment_creature_components`
- `014_cannibalism_plans/subagent_handoffs/event014_cannibal_3d_model_family_handoff.md` — `author_humanoid_actions`
- `014_cannibalism_plans/subagent_handoffs/event014_cannibal_bone_guard_3d_handoff.md` — `author_humanoid_rig`
- `014_cannibalism_plans/subagent_handoffs/event014_network_cadre_final_v8.md` — `import_animation_action`
- `016_brilliant_scientist_plans/subagent_handoffs/016_armed_humanoid_adapter_recovery_skill_update_2026-08-22.md` — `author_humanoid_actions`, `author_humanoid_rig`
- `016_brilliant_scientist_plans/subagent_handoffs/016_clone_infantry_runtime_closure_2026-09-05.md` — `author_humanoid_actions`, `patch_existing_humanoid_action_phases`
- `016_brilliant_scientist_plans/subagent_handoffs/016_clone_runtime_repair_2026-09-06.md` — `author_measured_creature_rig`, `preview_explicit_skin_selection`, `repair_explicit_skin`
- `016_brilliant_scientist_plans/subagent_handoffs/016_final_action_phase_patch_adapter_2026-09-02.md` — `patch_existing_humanoid_action_phases`
- `016_brilliant_scientist_plans/subagent_handoffs/016_final_alien_muzzle_recovery_2026-09-02.md` — `import_animation_action`
- `016_brilliant_scientist_plans/subagent_handoffs/016_final_muzzle_adapter_capability_2026-09-02.md` — `import_animation_action`
- `016_brilliant_scientist_plans/subagent_handoffs/016_final_portal_preserved_weapon_intake_2026-09-02.md` — `segment_creature_components`
- `016_brilliant_scientist_plans/subagent_handoffs/016_final_robot_runtime_recovery_2026-09-02.md` — `author_humanoid_actions`, `correct_action_grounding`, `offset_action_root`, `patch_existing_humanoid_action_phases`, `recover_existing_units`, `retime_animation_action`
- `016_brilliant_scientist_plans/subagent_handoffs/016_no_manual_simple_animation_skill_update_2026-08-22.md` — `author_humanoid_actions`
- `016_brilliant_scientist_plans/subagent_handoffs/2026-08-27_manual_existing_mesh_rig_recovery_final.md` — `recover_existing_units`
- `016_brilliant_scientist_plans/subagent_handoffs/2026-09-05_temporal_guard_runtime_closure.md` — `correct_action_grounding`, `patch_existing_humanoid_action_phases`
- `016_brilliant_scientist_plans/subagent_handoffs/2026-09-05_xenobiological_assault_runtime_closure_tranche7.md` — `author_creature_action`, `author_creature_rig`, `author_humanoid_actions`, `author_humanoid_rig`, `author_locomotion_action`, `calibrate_creature_scale`, `correct_action_grounding`, `import_animation_action`, `import_bvh_animation_action`, `retime_animation_action`, `segment_creature_components`
- `016_brilliant_scientist_plans/subagent_handoffs/animation_processing_mcp_tools_handoff_2026-08-22.md` — `correct_action_grounding`, `import_animation_action`, `retime_animation_action`
- `016_brilliant_scientist_plans/subagent_handoffs/clone_infantry_3d_model_handoff.md` — `offset_action_root`, `retime_animation_action`
- `016_brilliant_scientist_plans/subagent_handoffs/handoff016_creature_runtime_repair_2026-09-06.md` — `author_measured_creature_action`
- `016_brilliant_scientist_plans/subagent_handoffs/repository_custom_model_animation_inventory_2026-08-22.md` — `author_locomotion_action`
- `016_brilliant_scientist_plans/subagent_handoffs/rigid_weapon_attachment_tool_handoff_2026-08-22.md` — `author_humanoid_actions`
- `016_brilliant_scientist_plans/subagent_handoffs/xenobiological_assault_meshy7_handoff_2026-08-27.md` — `segment_creature_components`
- `018_resources_found_plans/subagent_handoffs/event018_cave_monster_meshy7_nonhumanoid_blocker_2026-08-22.md` — `author_creature_action`, `author_creature_rig`
- `020_black_plague_plans/subagent_handoffs/2026-08-22_event020_plague_rat_animation_recovery.md` — `import_animation_action`
- `020_black_plague_plans/subagent_handoffs/2026-08-24_event020_rat_animation_sound_handoff.md` — `import_animation_action`, `retime_animation_action`
- `020_black_plague_plans/subagent_handoffs/2026-08-24_event020_rat_quaternius_walk_bind_blocker.md` — `import_animation_action`
- `020_black_plague_plans/subagent_handoffs/2026-08-24_event020_runtime_checkpoint_retarget_blocker.md` — `import_animation_action`, `retime_animation_action`
- `3d_model_workflow_plans/2026-09-06_adapter_recovery_handoff.md` — `attach_rigid_component`, `author_measured_creature_action`, `author_measured_creature_rig`, `ground_existing_action`, `preview_explicit_skin_selection`
- `chaos_warfare_system_plans/subagent_handoffs/2026-09-06_chaos_assault_battalion_blender_repair.md` — `attach_rigid_component`, `ground_existing_action`
