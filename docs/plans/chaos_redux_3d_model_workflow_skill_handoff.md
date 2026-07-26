# Chaos Redux 3D Model Workflow Skill Handoff

## Scope

This bounded maintenance pass created the reusable 3D model workflow skill and
added its context-free subagent routing. It did not implement a provider client,
Blender adapter, pilot job, runtime registration, or in-game validation. The
overall 3D workflow is not complete.

## Changed files

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` — new reusable skill.
- `.agents/skills/chaos-redux-subagents/SKILL.md` — added the
  `chaosx_3d_model_pipeline` route and concise ownership/evidence rules.
- `docs/plans/chaos_redux_3d_model_workflow_skill_handoff.md` — this handoff.

No gameplay, model, texture, GFX, entity, localisation, spreadsheet, or pilot job
file was edited. Other working-tree changes in the subagent skill, including
unrelated asset/portrait wording and formatting changes, were preserved rather
than rewritten; only the 3D route was added in this pass.

## Sources read

Read completely before editing:

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `docs/specs/chaos_redux_3d_model_workflow_planning_package/proposed_skill/chaos-redux-3d-model-pipeline/SKILL.md`
- `docs/specs/chaos_redux_3d_model_workflow_planning_package/proposed_subagent/chaosx_3d_model_pipeline.toml`
- `docs/specs/chaos_redux_3d_model_workflow_planning_package/00_source_register.md`
- `docs/specs/chaos_redux_3d_model_workflow_planning_package/10_repo_integration_plan.md`
- `docs/specs/chaos_redux_3d_model_workflow_planning_package/11_implementation_backlog.md`
- `C:/Users/klimp/.codex/skills/.system/skill-creator/SKILL.md`

Repository and reference review also covered:

- The offline Paradox wiki core-page headings required by `AGENTS.md`.
- Full offline `Graphical asset modding - Hearts of Iron 4 Wiki.md` and
  `Entity modding - Hearts of Iron 4 Wiki.md` pages, plus relevant character,
  interface, and scripted-GUI page headings.
- Relevant vanilla documentation excerpts for entity/model inspection, including
  `documentation/console_commands_documentation.md` and
  `documentation/effects_documentation.md`; the installed documentation folder
  has no dedicated Meshy, Blender, or `io_pdx_mesh` guide.
- Existing Chaos Redux model precedents:
  `gfx/entities/chaosx_buildings.gfx` and
  `gfx/entities/chaosx_buildings.asset`.
- The committed legacy `.agents/skills/blender-pdx-modeling/SKILL.md` and its
  `references/blender-pdx-modeling.md` and
  `references/chaos-redux-integration-todo.md` files, checked for overlap.

## Routing decisions

- Created a separate skill because 3D geometry, skeletal rigs/actions, PDX export,
  and reimport evidence are a distinct workflow from the existing 2D asset skill.
- The committed legacy Blender skill was a narrower modeling/reference and TODO
  workflow; it did not cover the proposed provider lineage, one-image gate,
  deterministic job package, dependency lock, checkpoint evidence, or full PDX
  export/reimport handoff. Its pre-existing deletion in the shared worktree was
  preserved and it was not restored.
- Kept broad source provenance, texture/DDS conventions, and coverage ownership in
  `chaos-redux-event-assets`; the new skill cross-references it instead of copying
  its full asset rules.
- Routed only bounded model production to `chaosx_3d_model_pipeline`.
- Required `fork_context=false`, exact job/output/handoff paths, asset profile,
  named vanilla references, action roles, credit/attempt limits, dependency locks,
  and forbidden simplifications in the parent prompt.
- Allowed only source/reference handling, provider candidates and lineage, Blender
  checkpoints, bounded geometry/material/rig/action work, model textures, PDX
  exports, QA/reimport evidence, manifests, crosswalk rows, and handoffs.
- Explicitly forbade gameplay, GFX, `.asset`, entity, localisation, spreadsheet,
  and runtime wiring from the subagent. Runtime source edits, live consumers,
  in-game evidence, and the overall completion claim remain parent-owned.
- Kept the exactly-one-image Meshy rule and explicitly disallowed multi-view boards,
  turnarounds, collages, and extra Meshy inputs.
- Added deterministic staging under
  `docs/assets/<owner_id>_<owner_slug>/models_3d/<asset_slug>/`, with a single
  `reference/meshy_input.png` and preserved provider/Blender/export evidence.
- Required provider task lineage, credit records, checksums, protected Blender
  checkpoints, PDX export logs, and reimport/parser evidence or an explicit gap.
- Treated provider, Blender, adapter, `io_pdx_mesh`, and viewer capabilities as
  installation/verification dependencies. No live MCP/tool identifier was
  invented, no package was installed, and viewer routes remain read-only.

## Validation performed

- Confirmed the target skill was absent before creation and exists at the requested
  path after the patch.
- Confirmed the new skill has valid `name`/`description` frontmatter and is 344
  lines, below the skill-creator guidance limit of 500 lines.
- Did not run `init_skill.py`: this delegation required the exact single
  repository `SKILL.md` output and `apply_patch` edits, while initialization would
  create extra template/UI metadata outside the requested scope. Used the official
  `quick_validate.py` check instead.
- Searched existing repo skills for 3D/Meshy/`io_pdx_mesh` overlap before creating
  the skill and reviewed the committed legacy Blender skill; no existing active
  skill covered the full requested workflow.
- Inspected the final changed-file diff with `git diff` and checked the touched
  paths for forbidden gameplay/model/GFX/entity/localisation/spreadsheet edits.
- No paid provider call, package installation, Blender execution, model export,
  runtime registration, or in-game validation was performed in this maintenance
  pass.
- No commit or staging was left behind; the parent can integrate these scoped
  files without capturing the shared worktree's unrelated changes.

## Source-package conflicts and parent-owned blockers

- The integration plan proposes edits to `AGENTS.md` and
  `chaos-redux-event-assets`; this delegation explicitly limited ownership to the
  new skill, subagent routing, and this handoff, so those files were not changed.
  `AGENTS.md` remains authoritative.
- The proposed skill/subagent describe official Meshy and Blender capabilities, but
  no installed live provider/Blender MCP inventory was available in this bounded
  pass. The new skill therefore requires parent-side installation/schema/version
  verification and does not pretend those routes are callable.
- The parent still owns `.codex/agents/chaosx_3d_model_pipeline.toml` registration,
  dependency locks and adapters, local profile calibration, job schemas and
  artifact vault, actual provider/Blender work, pilots, final `.gfx`/`.asset`/
  entity/gameplay wiring, runtime crosswalk completion, and in-game evidence.
- No Technology Tree Viewer or other unrelated viewer capability is assumed; if
  the parent needs one and it is not discovered, record it as absent and requiring
  installation/verification rather than inventing a tool name.
