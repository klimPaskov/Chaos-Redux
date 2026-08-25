# No-manual-simple-animation skill handoff

Status: reusable documentation and canonical-agent routing updated; no final animation was produced or promoted.

## Exact changes

- Updated `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` with a skeletal animation source gate requiring verified Meshy `meshy_animate` motion or an explicitly user-approved professional animation source for every required role. It forbids manually keyed or simple procedural Blender actions, whole-rig transforms, transform-only clips, static-pose aliases, semantic role reuse, and local replacement motion. It limits Blender to source-action import, retargeting, non-destructive cleanup, contact or root correction, scale normalization, baking, sound synchronization, validation, PDX export, and reimport, and requires substantive attack or fire and articulated death evidence across role-appropriate frames.
- Rewrote the provider failure, humanoid recovery, armed fused-mesh, and action-validation passages in `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` so failed or missing roles require authorized Meshy regeneration, re-rigging, or re-animation, or an approved professional source, otherwise the role is blocked. The local humanoid adapter is documented as skeleton preparation or approved-source processing only, never as a final animation source.
- Updated `.tools/3d_pipeline/README.md` in the skeletal source gate, armed recovery, fused-mesh, death, family-batch, and creature sections to match the same source lineage, evidence, and no-manual-motion policy.
- Updated `.agents/skills/chaos-redux-subagents/SKILL.md` in `### 3D model routing` so the routed worker processes approved action sources only and never routes `author_humanoid_actions` or another local adapter operation as final motion.
- Updated `.codex/agents/chaosx_3d_model_pipeline.toml` description, Meshy tool policy, owned scope, Meshy rules, and animation rules to remove the failed-provider Blender-authored-action route and require verified `meshy_animate` or explicitly approved professional source actions.
- Updated `.agents/skills/chaos-redux-event-assets/SKILL.md` in `### 3D model package handoff` so its animated-unit guidance also requires approved source actions and limits Blender to non-destructive processing, with missing roles blocked instead of locally authored.

## Validation

- The official `skill-creator` quick validator was run for `.agents/skills/chaos-redux-3d-model-pipeline`, `.agents/skills/chaos-redux-subagents`, and `.agents/skills/chaos-redux-event-assets`.
- The canonical agent file was parsed with Python `tomllib` after editing.
- A targeted non-vendored skills, agent, and 3D README search found no remaining instruction that permits `author_humanoid_actions`, `blender_failure_recovery_humanoid_v1`, missing-action Blender authoring, or simple final skeletal animation. Matches in the updated policy are prohibitions or allowed-source references, not permissions.

## Remaining legacy executable surface

The adapter operation remains present by explicit scope preservation and is not a permitted final-animation route. The unmodified executable/configuration references are `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py` (`chaosx_blender_hoi4_author_humanoid_actions`), `.tools/3d_pipeline/adapter/blender_worker.py` (`author_humanoid_actions`), `.tools/3d_pipeline/blender_client.py`, `.tools/3d_pipeline/run_pilot.py`, `.tools/3d_pipeline/config/blender_hoi4_adapter.json`, `.tools/3d_pipeline/config/dependencies.lock.json`, `.codex/config.toml`, and the generated `.tools/3d_pipeline/reports/environment_report.json`. These are legacy implementation, route-lock, runner, allowlist, or evidence surfaces and require a separate code/configuration change before the operation can be removed or made source-safe; this documentation task does not authorize editing them.

A broader repository search still finds historical planning/specification examples and earlier handoff evidence that name the legacy adapter route. Those non-executable records remain outside this bounded documentation change and must not be treated as current worker routing; update them separately if they are promoted back into an active workflow.

No gameplay, asset, adapter, client, runner, configuration, dependency-lock, report, or `.qoder/**` file was edited, and no Git commit was created.
