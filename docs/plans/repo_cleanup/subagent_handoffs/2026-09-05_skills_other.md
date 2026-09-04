# Other skills documentation review

Date: 2026-09-05.
Disposition: implemented within the parent-authorized documentation cleanup scope, pending parent review and commit.
Acceptance basis: the parent assigned a bounded review of six named skills, permitted verified reference and prose corrections, and explicitly protected workflow permissions, source rules, provider rules, and engine rules.
No gameplay, assets, localisation, workbook, configuration, generated role, or helper implementation was changed.
No commits, sync scripts, engine calls, provider calls, live QA, game launch, RunPod operation, or deletion were performed.

## Documents reviewed and dispositions

| Document | Disposition | Change and evidence |
| --- | --- | --- |
| `.agents/skills/chaos-redux-debug-playtest/SKILL.md` | implemented | Replaced the obsolete `fork_context=false` argument with `fork_turns="none"` and named Codex `collaboration.spawn_agent`. The exposed collaboration schema and shared subagent skill confirm that argument. The explicit invocation and capability gates are preserved. |
| `.agents/skills/chaos-redux-frame-animation/SKILL.md` | implemented | Replaced five prose semicolons with sentence punctuation. All frame, transparency, source, fallback, routing, engine, cleanup, and approval requirements are preserved. |
| `.agents/skills/chaos-redux-mtth/SKILL.md` | implemented | Full review completed with no edit. The source and probability rules remain unchanged. |
| `.agents/skills/chaos-redux-state-ledgers/SKILL.md` | implemented | Replaced prose and list-ending semicolons with periods. All transfer, conservation, array, reception, privacy, map, lifecycle, and validation requirements are preserved. |
| `.agents/skills/chaos-redux-super-events/SKILL.md` | implemented | Both retired quote and cultural-remark role names now point to `chaosx_super_event_text_researcher`, matching its canonical TOML and the shared routing skill. Fixed two sentence-capitalization errors, a missing period, one unnecessary comma, and prose semicolons. Source, copyright, audio, duration, reuse, approval, and wiring rules are unchanged. |
| `.agents/skills/xlsx/SKILL.md` | implemented | Corrected all three recalculation command examples to `.agents/skills/xlsx/recalc.py` from the mod root. Replaced the unsupported installation assumption with a `soffice` PATH check. Described the helper's existing Windows branch and its unenforced Windows timeout. Retained formula recalculation, formula preservation, XLSX authority, and CSV export requirements. Preserved semicolons inside the quoted Excel number-format syntax. |
| `docs/plans/repo_cleanup/subagent_handoffs/2026-09-05_skills_other.md` | implemented | This handoff records the bounded changes, evidence, protected conflicts, and remaining review limits. |

No skill was created.
The super-event routing correction already agrees with `AGENTS.md` and `chaos-redux-subagents`, so those surfaces need no follow-up routing edit for this batch.

## Full reads and supporting evidence

Fully read each of the six owned `SKILL.md` files before editing.
Fully read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `C:/Users/klimp/.codex/skills/.system/skill-creator/SKILL.md`.
Read the following matching canonical role files in full as documentation references, without invoking their production workflows:

- `.codex/agents/chaosx_skill_maintainer.toml`
- `.codex/agents/chaosx_ai_probability_auditor.toml`
- `.codex/agents/chaosx_scripted_system_architect.toml`
- `.codex/agents/chaosx_icon_artist.toml`
- `.codex/agents/chaosx_generated_event_art.toml`
- `.codex/agents/chaosx_portrait_creator.toml`
- `.codex/agents/chaosx_asset_source_researcher.toml`
- `.codex/agents/chaosx_3d_model_pipeline.toml`
- `.codex/agents/chaosx_super_event_text_researcher.toml`
- `.codex/agents/chaosx_super_event_audio_researcher.toml`
- `.codex/agents/chaosx_spreadsheet_doc_worker.toml`

Fully read `.agents/skills/xlsx/recalc.py`, `.tools/export_event_catalog_csv.py`, and the official skill creator's `scripts/quick_validate.py`.
Verified that `recalc.py` is absent from the mod root and present at the corrected skill-local path.
`Get-Command soffice` returned no command in this shell, so LibreOffice invocation and recalculation remain unverified.
The helper source has platform branches for Windows, Linux, and macOS, while its timeout wrapper is only applied outside Windows.
Opened the eleven required offline wiki core pages and consulted their opening reference material.
Read installed vanilla `documentation/script_concept_documentation.md` in full and inventoried the documentation directory.
This was not a full engine documentation or implementation audit.

## Baseline preservation and validation

Compared the owned skills with the supplied dirty baseline under `C:/Users/klimp/.codex/visualizations/2026/09/04/01a06e33-dc56-78e3-a787-850360234143/documentation_review/skills_batch02_baseline/files` and reviewed the final scoped Git diff.
The debug skill already lacked the old generic `.agents/skills/hoi4-autonomous-debug-playtest/SKILL.md` reading requirement when this worker began.
That pre-existing deletion is preserved and is not attributed to this worker.
The debug skill through section 25 matches the supplied baseline text, including its description, invocation gate, capability gate, launch flow, logs, saves, and testing rules.
All fenced examples match the baseline except the three intentionally corrected XLSX command paths.
The MTTH skill is unchanged from the baseline.
The official `quick_validate.py` accepted all six skills.
Validation reviewed documentation structure, command resolution, routing identifiers, and preservation of protected content.
It does not prove engine behavior, live service health, viewer installation, or successful spreadsheet recalculation.

The exposed tool inventory contains the seven probability routes `mcp__hoi4_agent_tools__hoi4_probability_inspect`, `mcp__hoi4_agent_tools__hoi4_probability_evaluate`, `mcp__hoi4_agent_tools__hoi4_probability_sweep`, `mcp__hoi4_agent_tools__hoi4_probability_simulate`, `mcp__hoi4_agent_tools__hoi4_probability_sequence`, `mcp__hoi4_agent_tools__hoi4_probability_compare`, and `mcp__hoi4_agent_tools__hoi4_probability_render`.
This is tool-exposure evidence only.
No service-health or standalone Technology Tree Viewer installation claim is made.
No MCP surface rule or probability rule was changed.

## Protected conflicts and review limits

| Status | Exact conflict or limitation | Disposition |
| --- | --- | --- |
| unresolved | The debug skill sections 6, 8, 27, and 29 instruct agent launch, log inspection, relaunch, and live verification. `AGENTS.md` section 4 rule 16 assigns all in-game testing to the user, forbids agent game launch, and forbids searching for logs that the user has not supplied. | Preserved both sides. This documentation-maintenance task does not invoke the live QA skill or resolve its permission conflict. |
| unresolved | Debug section 26 says specialist subagents remain optional. `AGENTS.md` requires specialty routes and baseline/patch/compare auditing for applicable weighted surfaces. | Preserved the existing optionality wording because specialist and probability permissions were protected. Only the obsolete spawn argument changed. |
| unresolved | Debug section 13 prefers a CSV export for read-only coverage planning when one exists. `AGENTS.md` requires the XLSX as authoritative source and forbids a stale CSV as source of truth. | Preserved the debug rule. The skill does not establish CSV freshness, and this batch did not inspect catalog contents or run exports. |
| unresolved | `.codex/agents/chaosx_super_event_audio_researcher.toml` prefers 1 to 3 minutes unless the parent gives a stronger constraint. The super-event skill prefers 1 to 2 minutes and limits the final file to 2 minutes unless the user explicitly approves longer. | Preserved duration and approval rules in both files. Parent prompts must carry the applicable existing constraint. No audio was selected or changed. |
| unresolved | Frame-animation section 4 requires a blocker or permission for a narrow exploration pass when no precedent exists, and section 18 requires parent-authorized exploration. | Preserved this explicit approval language. This batch neither executes exploration nor changes that protected gate. |
| blocked for execution | `soffice` is not exposed on this shell's PATH, and the recalculation helper does not enforce its timeout on Windows. | Documented the verified helper limitation without running LibreOffice, editing its profile, or changing the helper. No workbook recalculation was needed for this documentation task. |
| unresolved | The debug startup list names `text.og`. | No active logs were searched to infer a replacement. The filename remains unverified and unchanged. |

The six skills' transitive engine examples, asset reference libraries, live shortcut, game logs, workbook values, runtime helpers, source websites, provider locks, and external applications were not comprehensively revalidated.
The other audit roles referenced by the debug skill were not separately reviewed because their implementation and specialty rules were outside this batch.
No provider, source, spending, model, reasoning, permission, access, safety, engine, or probability policy was relaxed.
No implementation simplification or fallback was introduced.
Parent review and the parent-owned commit remain outstanding.
