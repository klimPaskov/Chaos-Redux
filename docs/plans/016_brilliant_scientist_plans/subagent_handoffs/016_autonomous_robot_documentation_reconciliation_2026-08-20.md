# Autonomous Robot documentation reconciliation

Date: 2026-08-20

## Disposition

The shared Autonomous Robot package is installed and reusable under the provider-neutral identifiers `autonomous_robot`, `autonomous_robot_equipment`, and `autonomous_robot_equipment_1`.

The current runtime includes `autonomous_robot_entity` at scale 0.8, snow and desert entity clones, one mesh, eight real skeletal actions, three PDX textures, purpose-built operational and weaponization technology icons, equipment art, large and on-map counters, six registered sound definitions, and five positional entity sound consumers.

Event 019 provider 505 grants the shared robot operational technology to the released derivative before installing its public package, which makes the advertised formation and isolated equipment production reachable.

## Reviewed documentation

- `docs/assets/shared_robot_system/models_3d/autonomous_robot/manifest.json` already records `production_complete_runtime_wired` and `installed_static_validation_complete_live_validation_pending`; no edit was required.
- `docs/assets/shared_robot_system/models_3d/autonomous_robot/manifest.md` already records installed runtime wiring and the selection-audio limitation; no edit was required.
- `docs/assets/shared_robot_system/models_3d/autonomous_robot/runtime/crosswalk.md` already records the installed entity, actions, textures, counters, and action-sound consumers; no edit was required.
- `docs/plans/016_brilliant_scientist_plans/016_event19_generic_unit_family_3d_model_backlog.md` already uses the generic robot identifiers and separates the installed robot package from the remaining model backlog; no edit was required.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_project_reuse_identifier_map.md` already marks its pre-implementation observations as superseded and maps Robotics to the generic runtime identifiers; no edit was required.
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md` was corrected where its old no-model paragraph still claimed that no Event 016 model package was accepted and counted the installed robot among future work.
- `docs/assets/shared_robot_system/models_3d/autonomous_robot/runtime/handoff.md` now distinguishes the production worker's historical ownership boundary from the installed parent-owned runtime state.

## Validation evidence

All 41 Git LFS-managed robot runtime assets from commit `ae7d2fd67` were materialized in the working tree and checked to ensure none remained as pointer text. Representative installed hashes match the accepted handoff: robot operational technology icon `BF54FE656D4B976EC0F2B5CCE0597A73A7E7DA61044C2F0D2AFAD7AE48ABAF0`, weaponization icon `B6151923274EBBC9669DED555BDEEFD292E78AB0A8DAC7807DA32F228F7B2FD4`, and mesh `694352C5778E608120474773728317EFA776572A2EBE0175F70B67AE7825F3C5`.

Fresh HOI4 MCP technology explanations for the robot operational and weaponization technologies, Portal Warfare pair, Clone Formations, Clone Infantry access, and both Mengele refinement technologies returned without missing-sprite diagnostics after materialization.

## Remaining blockers

- The selection cue is registered but has no provider-neutral per-subunit selection consumer. It must not replace a country's ordinary infantry voices as a fallback.
- Live model scale, shader, action transition, sound-mix, and counter presentation acceptance remains user-owned.
- The dedicated probability audit is recorded in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_autonomous_robot_probability_audit_2026-08-20.md`. The reusable seven-family random-technology pool has exact MCP scenario evidence; the Event 019 manual dynamic-array selector remains outside the installed adapter's normalized-pool support.
- Portal Raider, paleogenetic, xenobiological, alien-interface, and temporal runtime model packages retain their individual rejected or queued dispositions.
