# Temporary event asset workspace skill-policy audit handoff

Date: 2026-08-09  
Auditor: `/root/event_temp_assets_skill_policy`  
Scope: reusable skill policy only; no Event 018 gameplay, assets, runtime files, or cleanup action

## Result

The requested lifecycle rule is explicit across the event, asset, animation, super-event, and subagent-routing skills. One narrow addition was needed in the 3D model skill because its event-owned job-root template prohibited runtime references into `docs/assets/` but did not explicitly define temporary-workspace retention, durable promotion, and deletion.

## Existing policy proof

- `.agents/skills/chaos-redux-subagents/SKILL.md:146-148` assigns event-scoped evidence to temporary `docs/assets/<event_id>_<event_slug>/`, retains it for active, blocked, review, and acceptance work, requires durable promotion and runtime-reference checks, and assigns cleanup to the parent.
- `.agents/skills/chaos-redux-events/SKILL.md:714-735,757` requires temporary source, processed preview, manifest, crosswalk, and handoff evidence, permanent promotion before completion, engine-facing runtime placement, no runtime reference into `docs/assets/`, and deletion of the complete event workspace.
- `.agents/skills/chaos-redux-event-assets/SKILL.md:134-145,536-568,1487-1516` defines the temporary event workspace, manifest, promotion, final runtime placement, deletion, absent-folder completion state, and the separate durable portrait archive exception.
- `.agents/skills/chaos-redux-frame-animation/SKILL.md:240-255,468-470` defines temporary animation evidence and requires durable frame and sprite facts to be promoted before deleting the event workspace.
- `.agents/skills/chaos-redux-super-events/SKILL.md:499,633,727` applies the same lifecycle to super-event image/audio evidence and records the permanent replacement for a deleted temporary manifest.
- `.agents/skills/chaos-redux-event-planning/SKILL.md:1753-1763` keeps plans as working handoffs and promotes accepted design into specs; it does not own asset production, so no asset-workspace rule was added there.
- `.agents/skills/chaos-redux-comfyui/SKILL.md:10-16` covers portraits only; its durable portrait-source archive is an explicit exception and must not be deleted with a temporary event workspace.

## Narrow skill change

Updated `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:130` with one reusable paragraph for event-owned model jobs. It now identifies `docs/assets/<event_id>_<event_slug>/models_3d/<asset_slug>/` as temporary evidence, retains it through active/blocked/review/acceptance states, requires promotion of durable provenance, licensing, checksums, QA/reimport, crosswalk, and runtime-handoff facts, requires engine-facing runtime placement and no runtime references into `docs/assets/`, and deletes the complete event workspace only after genuine event completion. Skill-local references, durable portrait archives, and unrelated event workspaces remain protected.

No Event 018 identifier, one-off asset name, private history, or temporary implementation decision was added to any skill.

## Workspace observation and boundary

`docs/assets/018_resources_found/` is currently absent, so this audit did not delete or alter an Event 018 workspace. Other event workspaces under `docs/assets/` were left untouched. The parent remains responsible for deciding whether any active or blocked event workspace may be removed after its own completion evidence and runtime-reference review.

## Changed files

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`
- `docs/plans/018_resources_found_plans/subagent_handoffs/event_temp_assets_skill_policy_2026-08-09.md`

No other skill was changed. Existing unrelated dirty hunks and deletions were preserved. No files were staged and no commit was created.

## Blockers and uncertainty

No policy conflict or tooling blocker was found. The only deliberate judgment was to patch the 3D skill because its direct job-root instructions lacked the lifecycle paragraph already present in the other asset-owning skills.
