# Shared scripted GUI skill handoff

Disposition: implemented for the skill and routing package; parent review, generated-agent synchronization, and commit remain parent-owned.
Acceptance basis: the parent assigned the user's request to extract a dedicated scripted GUI skill, require reference images before implementation, strengthen visual/usability acceptance, and update routing while preserving event-worker ownership boundaries.
The parent reviewed the draft and requested that the visible-value limit remain scoped to simultaneous values on the current surface/state and that context-specific scope support be verified from installed documentation and consumers.
Those corrections are included.

## Created

- `.agents/skills/chaos-redux-scripted-gui/SKILL.md`: focused workflow for reference-first design, native element mapping, acceptance evidence, live MCP schema discovery, explicit fixtures, inspect/render/rewrite/matched before-and-after review, content budgets, ownership, and completion.
- `.agents/skills/chaos-redux-scripted-gui/references/visual-review.md`: detailed checklist for glyph centering on both axes, icon/label grouping, spacing, alignment, symmetry, painted versus logical versus usable bounds, scale, clipping, hitboxes, z-order, state behavior, background coverage, and usable information hierarchy.
- This handoff.

## Updated and exact owned sections

| File | Task-owned change |
| --- | --- |
| `AGENTS.md` | Added the scripted GUI skill in Repo Skills, redirected the event UI worker's layout owner, and updated the concise GUI MCP infrastructure bullet for references and matching before/after review. |
| `.agents/skills/chaos-redux-decisions-missions/SKILL.md` | Added the introductory GUI routing link; replaced the Scripted GUI decision categories and mechanic windows section with presentation choice/routing plus the retained gameplay action-integrity contract. |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | Redirected layout ownership, extended the Event UI worker gate with reference paths or production assignment and acceptance basis, and clarified matched-scenario evidence without inventing a comparison tool. |
| `.agents/skills/chaos-redux-events/SKILL.md` | Updated the dedicated GUI implementation paragraph to use the new skill, reference images, and mapping; kept shared interfaces parent-owned. |
| `.agents/skills/chaos-redux-event-planning/SKILL.md` | Added the reference/native-mapping handoff before the existing dedicated event UI worker paragraph and redirected its layout contract. |
| `.agents/skills/chaos-redux-event-assets/SKILL.md` | Added reference-first/native-functional-element guidance and painted/usable bounds to Decision category and scripted GUI visual packs. |
| `.codex/agents/chaosx_event_ui_worker.toml` | Updated required reading, reference/acceptance inputs, reference-before-source workflow, matching evidence, visual-contract delegation, handoff, and completion owner references. |
| `.codex/agents/chaosx_decision_mission_auditor.toml` | Added conditional required reading for scripted GUI layout inspection/repair and reference/matched-scenario evidence. |
| `docs/systems/hoi4_agent_tools_mcp_integration.md` | Updated Existing workflow ownership for the GUI skill and added the production-render acceptance requirement in Rendering limits. |

Gameplay, costs, affordability, requirements, payment, AI, cleanup, and balance remain in the decisions skill.
The dedicated event UI worker remains restricted to a named event-owned UI; no shared interface becomes worker-owned through these routing changes.
No gameplay, actual GUI, GFX, localisation, generated agent, or runtime configuration files were edited by this skill-maintenance subagent.
Other skill and agent files were left unchanged by this subagent, including `chaosx_improvement_loop_planner.toml` and `chaosx_repo_explorer.toml`.

## Evidence and checks

Read official `skill-creator`, repository guidance, the required offline wiki pages, GUI-specific snapshot material, installed scripted GUI documentation, relevant vanilla documentation, and the vanilla paranoia meter's separate native GUI/scripted-GUI consumers.
Checked the registered `hoi4_agent_tools` command in `.codex/config.toml` and discovered the actual exposed `mcp__hoi4_agent_tools__hoi4_gui_inspect`, `mcp__hoi4_agent_tools__hoi4_gui_render`, and `mcp__hoi4_agent_tools__hoi4_gui_rewrite` schemas.
Read the installed production package's `docs/gui.md` for explicit fixtures, generated scenarios, glyph-bound expectations, and fidelity reporting.
The exposed render schema has `comparisonScenario`; no separate GUI comparison tool was discovered or invented.

The parent supplied live route findings while forward-testing the skill on an authorized GUI repair: initial broad inspection timed out, later production inspection succeeded, and visible off-center label warnings could coexist with a passing validation flag.
The skill therefore requires actual image/diagnostic review and preserves exact sourceRevision/scenarioId/artifact identities, not a latest-filename assumption.
Parent-confirmed schema caveats are included: narrow inspect needs paired windowName/scenario, fixtureChoices is not a scenario field, exact regression fixtures disable generation, global selected-state renders can activate mutually exclusive tabs, patch mode accepts exact scalar ranges, and expectedSourceHash belongs to patch mode rather than source mode.
This handoff does not claim this subagent implemented or validated that live GUI repair.

The official `skill-creator/scripts/quick_validate.py` accepted the new skill.
The modified agent TOMLs parsed successfully with the installed `tomli` parser.
The original gameplay action rules remain represented in the decision-owned section; the extracted layout guidance is represented in the new skill and its linked visual checklist.
Parent review supplied a realistic behavior check; the live repair's final evidence remains in the parent task.

## Parent integration and concurrent edits

Exact pre-edit bytes were preserved under `C:\Users\klimp\AppData\Local\Temp\chaos-redux-scripted-gui-skill-20260905`, using repository-relative paths.
Several files already had staged and unstaged changes, and concurrent work changed some files after these snapshots.
The baseline-to-current review diff is not exclusively this task: isolate only the owned sections listed above when staging or committing.
In particular, later changes in assets, planning, events, and the untouched improvement-loop planner TOML must not be attributed to this subagent.
An independently filtered `authored-gui-skill-only.patch` beside the byte backups includes only the reviewed task-owned routing hunks and the three new files.
It excludes unrelated baseline-to-current changes; the parent should check applicability against its chosen temporary index because concurrent commits may change patch context.

Regenerate agent mirrors through the existing `.tools/sync/sync_qoder_agents.py` and `.tools/sync/sync_cursor_agents.py` scripts after reviewing canonical TOML changes; do not hand-edit generated files.
Parent handles synchronization, final review, and the task-scoped commit.

## Simplifications, omissions, and blockers

No requested skill rule was omitted or replaced with a fallback.
The skill package is complete; no current blocker prevents reviewing or using it.
Generated-agent synchronization and commit are intentionally left with the parent as assigned.
Tool schema exposure and documentation checks do not establish live-game behavior; visible GUI completion and any remaining MCP/runtime uncertainty belong to the parent repair evidence.
