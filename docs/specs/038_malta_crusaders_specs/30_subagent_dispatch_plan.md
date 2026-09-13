# Subagent dispatch plan

## Runtime status

This planning environment did not expose the Chaos Redux project subagent runner or the repository MCP servers. No named project subagent was executed, no repository file was edited, and no MCP evidence was fabricated. The `prompts/` folder contains context-complete prompts for the parent implementation agent to dispatch in Codex, Qoder, or Cursor with the repository and configured tools available.

Every project subagent must receive a self-contained prompt with no inherited thread context. In Codex, use `fork_context=false`. In Qoder and Cursor, use the generated hyphen-case agent definition and retain the same explicit prompt.

## Dispatch order

| Phase | Agent | Prompt | Mode | Dependency | Required output |
| --- | --- | --- | --- | --- | --- |
| 1 | parent implementation agent | `prompts/01_master_implementation_prompt.md` | implementation owner | full spec pack | accepted implementation plan and task ledger |
| 2 | `chaosx_repo_explorer` | `prompts/02_repo_explorer_prompt.md` | read-only | none | file map, tag and identity risks, precedents, MCP route status, edit order |
| 3 | `chaosx_scripted_system_architect` | `prompts/03_scripted_system_architect_prompt.md` | bounded patch | repo explorer and locked state/tag strategy | Event 38 constants, helpers, ledgers, contracts, handoff |
| 4 | `chaosx_ai_probability_auditor` | `prompts/09_ai_probability_auditor_baseline_prompt.md` | read-only | proposed weighted surfaces exist | named baseline scenarios and MCP evidence |
| 5 | parent plus event implementation | master prompt | implementation | phases 2 to 4 | baseline event, release, country, unit registrations, mechanics |
| 6 | `chaosx_event_ui_worker` | `prompts/04_event_ui_worker_prompt.md` | bounded event-owned GUI patch | accepted council GUI IDs and gameplay helpers | MCP before and after GUI evidence plus handoff |
| 7 | `chaosx_focus_tree_auditor` | `prompts/05_focus_tree_auditor_prompt.md` | active audit and small patch | implemented tree | focus MCP evidence, route coverage, bounded fixes, handoff |
| 8 | `chaosx_decision_mission_auditor` | `prompts/06_decision_mission_auditor_prompt.md` | active audit and small patch | decisions and missions exist | objective, cost, AI, cleanup, clutter, exploit audit and handoff |
| 9 | `chaosx_country_package_auditor` | `prompts/07_country_package_auditor_prompt.md` | active audit and small patch | country packages exist | package matrix audit, bounded corrections, handoff |
| 10 | asset agents | prompts 11 to 17 | production or research | stable identifiers, consumers, final briefs | final files, manifests, handoffs, blockers |
| 11 | `chaosx_localisation_auditor` | `prompts/08_localisation_auditor_prompt.md` | active audit and small patch | visible implementation complete | wording, key, dynamic text, encoding, cross-surface audit |
| 12 | `chaosx_ai_probability_auditor` | `prompts/10_ai_probability_auditor_compare_prompt.md` | read-only | all weighted patches final | mandatory same-scenario probability comparison |
| 13 | `chaosx_improvement_loop_planner` | `prompts/18_improvement_loop_planner_prompt.md` | plan-only | one meaningful implementation tranche complete | one improvement addendum or closure handoff |
| 14 | parent implementation agent | master prompt | implementation | disposition of improvement addendum | implement, promote, queue, or reject with reason |
| 15 | `chaosx_spreadsheet_doc_worker` | `prompts/20_spreadsheet_worker_prompt.md` | workbook only | implementation wording and facts final | authoritative XLSX update and CSV export |
| 16 | `chaosx_documentation_curator` | `prompts/21_documentation_curator_prompt.md` | documentation only | long implementation and handoffs complete | source-of-truth reconciliation and resume packet |
| 17 | `chaosx_event_completion_auditor` | `prompts/19_completion_auditor_prompt.md` | read-only | final candidate state | spec-versus-implementation audit |
| 18 | parent implementation agent | master prompt | implementation and review | all blocking findings resolved | final completion report or explicit incomplete report |

## Asset dispatch split

Use each asset specialist only for its exact family:

- `chaosx_asset_source_researcher` handles real or archival non-portrait sources and historical symbol research.
- `chaosx_generated_event_art` handles fictional scenes, flags after research, faction emblems, panels, and full-canvas event art.
- `chaosx_icon_artist` handles focus, idea, decision, mission, technology, achievement, GUI icons, state pieces, and all custom counters.
- `chaosx_portrait_creator` handles every portrait, including archival source placeholders and authorized fictional high-Chaos identities.
- `chaosx_3d_model_pipeline` handles Meshy 7 geometry, textures, rigs, skeletal actions, source-only unit sound research, counter handoff requirements, exports, and reimport evidence.
- `chaosx_super_event_text_researcher` handles quote and cultural remark verification.
- `chaosx_super_event_audio_researcher` handles licensed musical cue research, download, conversion, and audio handoff.

Do not give one asset agent the mixed inventory.

## Probability ownership

Any patch to AI weights, `ai_chance`, MTTH modifiers, random lists, target weights, strategy factors, focus selection, decision selection, relic outcomes, order demands, side assignment, or route choice requires this sequence:

1. baseline read-only audit with named scenarios
2. owner-applied patch
3. read-only `hoi4.probability_compare` against the same scenarios

The probability auditor does not choose the intended balance target and does not patch source.

## Improvement-loop disposition

Only one unresolved Event 38 improvement addendum may exist at a time. After the planner returns:

- implement it and merge accepted design into the specs
- promote it into the specs without implementation only when explicitly queued and reported
- reject it with a reason
- accept a closure handoff and stop broad expansion

Do not dispatch a second planner pass while the first remains unresolved.

## Mandatory handoffs

Every patch-capable subagent writes to:

```text
docs/plans/038_malta_crusaders_plans/subagent_handoffs/
```

The handoff must list changed files, identifiers, behavior before and after, task-specific validation, skipped meaningful validation, remaining risks, and parent follow-up. Use `templates/subagent_handoff_template.md`.

Asset handoffs remain in the Event 38 temporary asset workspace during production, then their durable facts move into permanent documentation before cleanup.

## Parent review gates

The parent must reject a handoff that:

- edits outside the granted surface
- invents a fallback
- omits changed identifiers
- lacks required MCP evidence for focus, GUI, map, event, technology, or probability work
- treats source-only review as engine evidence when the MCP route was available
- creates an unauthorized asset family
- uses generated or substituted faces for grounded people
- reuses counters or unit audio without source and consumer proof
- omits AI or cleanup from a playable system
- calls a package complete while its final consumer is absent

## Completion authority

No subagent owns the Event 38 completion claim. The parent must review the final repository state, all handoffs, all unresolved plans, all assets, the workbook export, MCP evidence, and the completion audit. The final report must identify every remaining simplification, omission, fallback, blocker, or skipped meaningful validation.
