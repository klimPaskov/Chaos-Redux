# Remaining role instruction review (2026-09-05)

The initial review below covers all 17 assigned Codex role TOMLs.
The viewer-availability follow-up at the end records the additional four-file correction.
The initial review changed only `developer_instructions` in `chaosx_3d_model_pipeline.toml` and `chaosx_event_ui_worker.toml`.
No skills, AGENTS.md, configuration settings, generated roles, gameplay, assets, catalog files, or permissions were edited by this worker.
No commit or generator was run.

## Changes

- `.codex/agents/chaosx_3d_model_pipeline.toml:15`: replaced the obsolete `fork_context=false` argument with the currently exposed Codex `collaboration.spawn_agent` argument `fork_turns="none"`, while retaining the fully explicit parent-input contract and distinguishing Qoder/Cursor runtime isolation.
- `.codex/agents/chaosx_3d_model_pipeline.toml:186`: assigned live consumer testing to the user and evidence review/completion ownership to the parent.
- `.codex/agents/chaosx_event_ui_worker.toml:68` and `:79`: made the same user-testing/parent-review distinction in the forbidden-scope and handoff requirements.

These changes preserve all mandatory artifact, MCP, reimport, runtime, and completion evidence requirements.
The shared AGENTS.md/subagent skill owns general isolation guidance, so no duplicate isolation paragraph was added to the other roles.
No spec-location-as-approval correction was demonstrated in these owned prompts.

## Full reads

Read each of these documents in full before editing.
The AGENTS.md and subagent skill reads preceded concurrent updates by their assigned owners.
The following list is the full-read ledger, not an inventory offered as reading evidence.

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `C:/Users/klimp/.codex/skills/.system/skill-creator/SKILL.md`
- `.codex/agents/chaosx_3d_model_pipeline.toml`
- `.codex/agents/chaosx_ai_probability_auditor.toml`
- `.codex/agents/chaosx_asset_source_researcher.toml`
- `.codex/agents/chaosx_country_package_auditor.toml`
- `.codex/agents/chaosx_decision_mission_auditor.toml`
- `.codex/agents/chaosx_event_completion_auditor.toml`
- `.codex/agents/chaosx_event_ui_worker.toml`
- `.codex/agents/chaosx_focus_tree_auditor.toml`
- `.codex/agents/chaosx_generated_event_art.toml`
- `.codex/agents/chaosx_icon_artist.toml`
- `.codex/agents/chaosx_improvement_loop_planner.toml`
- `.codex/agents/chaosx_portrait_creator.toml`
- `.codex/agents/chaosx_scripted_system_architect.toml`
- `.codex/agents/chaosx_skill_maintainer.toml`
- `.codex/agents/chaosx_spreadsheet_doc_worker.toml`
- `.codex/agents/chaosx_super_event_audio_researcher.toml`
- `.codex/agents/chaosx_super_event_text_researcher.toml`

Consulted opening and introductory excerpts from all eleven required offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding (`paradox_wiki/<page> - Hearts of Iron 4 Wiki.md`).
These were excerpt consultations, not full-page reads.
No engine syntax or behavior change was attempted.
No engine-behavior conclusion or vanilla-documentation validation is claimed.

## Validation and protected fields

Parsed all 17 current owned TOMLs and their parent-provided baseline copies using the installed Python `tomli` parser.
The initial `tomllib` import was unavailable in the default Python.
The installed `tomli` rerun succeeded without installing anything.
Compared every parsed field outside `developer_instructions` against `C:/Users/klimp/.codex/visualizations/2026/09/04/01a06e33-dc56-78e3-a787-850360234143/documentation_review/batch01_baseline/files/.codex/agents/`.
Every such field matched, including names, descriptions, models, reasoning efforts, sandbox modes, and nickname lists.
The remaining 15 owned TOMLs also retained their baseline `developer_instructions` values.
Reviewed the two-file diff: it contains exactly the four instruction-line replacements listed above.
Key gates, source restrictions, provider restrictions, paid-operation authorization, limits, and allowlist-related prose remain unchanged.

The current collaboration tool schema directly documents `fork_turns="none"` as passing no parent history.
`collaboration.spawn_agent` is exposed separately from `ALL_TOOLS`.
No agent was spawned for verification.
`ALL_TOOLS` metadata exposes the `mcp__hoi4_agent_tools__hoi4_*` inspection/render/compare families, including `mcp__hoi4_agent_tools__hoi4_tech_inspect`, `mcp__hoi4_agent_tools__hoi4_tech_render`, and `mcp__hoi4_agent_tools__hoi4_tech_compare`, plus Meshy and Blender adapter routes.
Metadata inspection establishes tool exposure only, not service health, engine behavior, or standalone viewer installation.
No engine MCP operation, rewrite, provider call, game, or desktop operation was performed.

## Unresolved conflicts and limits

- **Generated-role consistency blocked:** AGENTS.md's “Canonical source” rule requires running both synchronization scripts, while its “Anti-interference rules” require leaving `.qoder/**` and generated `.cursor/agents/**` untouched during Codex sessions.
  The parent expressly required leaving synchronization blocked, so generated roles were not updated or represented as consistent.
- **Protected 3D reading order:** `.codex/agents/chaosx_3d_model_pipeline.toml:9-10` requires the Meshy key gate before AGENTS.md, parent prompt, and repository intake, while AGENTS.md requires offline wiki consultation before repository-file access.
  The parent expressly required preserving the key gate.
  It remains unchanged.
- **Super-event reading exclusions:** `.codex/agents/chaosx_super_event_audio_researcher.toml:12` and `.codex/agents/chaosx_super_event_text_researcher.toml:12` explicitly prohibit reading AGENTS.md, offline wiki pages, and vanilla documents.
  This conflicts with repository required reading and remains unchanged for parent review.
- **Spreadsheet reading exclusion:** `.codex/agents/chaosx_spreadsheet_doc_worker.toml:11` explicitly excludes offline wiki and vanilla reading, and its allowed-input list excludes AGENTS.md.
  The shared subagent skill also expresses this narrow reading policy.
  Resolving that policy conflict is outside this patch.
- **Asset reading-list ambiguity:** `.codex/agents/chaosx_asset_source_researcher.toml:11-15` says “Read only” the asset prompt, skill sections, reference root, and named package files without listing AGENTS.md or the required wiki pages.
  Generated-art and icon prompts likewise give narrow input lists at line 11, but do not state the same explicit AGENTS.md prohibition as the two super-event researchers.
  These input-policy passages remain unchanged.
- **Probability scope wording resolved in the gameplay skill batch:** the initial review found “complex or balance-sensitive” qualifiers in the focus and decision auditor prompts, while AGENTS.md required the probability route for every in-scope weighted surface.
  The [gameplay skill handoff](2026-09-05_skills_gameplay_docs.md) records the subsequent alignment with that existing requirement and preserves the probability auditor's read-only role.
  No probability behavior or balance target was changed.
- **Standalone viewer wording resolved by follow-up:** the initial review preserved the four absence claims.
  The follow-up below replaces them with conditional verification guidance.
  Standalone viewer installation and service health remain unverified.

No simplifications were introduced into the repaired instructions.
The role-prompt edits are complete within the assigned boundary.
Generated-runtime propagation and the listed policy conflicts remain unresolved.

## Viewer-availability follow-up

Disposition: implemented within the parent-authorized instruction cleanup.
The four role prompts require separate verification of standalone Technology Tree Viewer availability, distinguish tool exposure from service health, and record verified absence as a package gap.
Each points to the existing MCP evidence section of `chaos-redux-subagents` without duplicating its tool list.
Read-only viewer use and unavailable-route blocker requirements remain intact.

Fully read the current versions of the following before editing this follow-up:

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `C:/Users/klimp/.codex/skills/.system/skill-creator/SKILL.md`
- `.codex/agents/chaosx_3d_model_pipeline.toml`
- `.codex/agents/chaosx_country_package_auditor.toml`
- `.codex/agents/chaosx_improvement_loop_planner.toml`
- `.codex/agents/chaosx_skill_maintainer.toml`
- `docs/plans/repo_cleanup/subagent_handoffs/2026-09-05_remaining_roles.md`

The four TOMLs listed above and this existing handoff are the exact follow-up changed-file set.
The prior 3D isolation and live-testing edits were preserved.
The existing improvement-planner and skill-maintainer changes were preserved outside the exact viewer assertion replacements.
No other role, skill, AGENTS.md, generated file, or configuration was edited by this follow-up.

Current `ALL_TOOLS` metadata verifies the technology inspection, rendering, and comparison routes already named in the initial evidence section.
The metadata describes technology tools as read-only and does not establish service health or standalone viewer installation.
No engine MCP operation, provider call, paid operation, generator, commit, or game operation was performed.

Parsed all four before-and-after TOMLs with installed `tomli` and compared every field outside `developer_instructions` against both the immediate pre-edit content and the parent-provided baseline copies.
Names, descriptions, models, reasoning efforts, sandbox modes, and nickname lists matched both comparisons.
For each role, reversing its single exact viewer assertion replacement reproduced the immediate pre-edit bytes, proving all other prose, code, quotations, source rules, provider rules, spending authorization, permissions, access restrictions, engine rules, policies, and gates were preserved.
No simplifications were introduced.
Service health, standalone viewer installation, generated-runtime propagation, and the other previously listed policy conflicts remain unresolved within this documentation-only scope.
