# Event 025 subagent routing plan

## Routing rule

Every project custom subagent must be spawned with `fork_context=false` and a context-complete prompt.

The parent remains responsible for design authority, final source changes, integration, documentation alignment, validation, and completion claims.

## Pre-implementation

| Order | Subagent | Mode | Purpose | Package prompt |
| ---: | --- | --- | --- | --- |
| 1 | `chaosx_repo_explorer` | Read-only | Map current Event 025, Event 016, Event 036, GUI, log, super-event, achievement, and helper surfaces | `prompts/025_repo_explorer_prompt.md` |
| 2 | `chaosx_improvement_loop_planner` | Plan-only | Independently confirm closure or write a focused accepted addendum | `prompts/025_improvement_loop_planner_prompt.md` |
| 3 | `chaosx_scripted_system_architect` | Narrow patch-capable | Design and implement reusable registry, reward, and arbitration helpers | `prompts/025_scripted_system_architect_prompt.md` |
| 4 | `chaosx_ai_probability_auditor` | Read-only | Establish named baseline weighted and timing evidence | `prompts/025_ai_probability_auditor_prompt.md` |

## Implementation and assets

| Subagent | Mode | Purpose | Prompt |
| --- | --- | --- | --- |
| `chaosx_event_ui_worker` | Event-owned GUI patch | Build and visually validate the Expedition Board | `prompts/025_event_ui_worker_prompt.md` |
| `chaosx_asset_source_researcher` | Asset research | Find period Antarctic reference sources | `prompts/025_asset_source_researcher_prompt.md` |
| `chaosx_generated_event_art` | Asset production | Create super-event, news, report, GUI, sector, and non-icon animation art | `prompts/025_generated_event_art_prompt.md` |
| `chaosx_icon_artist` | Asset production | Create GUI, route, outpost, action, idea, and achievement icons | `prompts/025_icon_artist_prompt.md` |
| assigned art subagent | Asset production | Create accepted real-frame animation sheets and fallbacks | `prompts/025_animation_asset_prompt.md` |
| `chaosx_super_event_text_researcher` | Read-only research | Verify title direction, quote, and cultural remark | `prompts/025_super_event_text_researcher_prompt.md` |
| `chaosx_super_event_audio_researcher` | Audio production and research | Source, verify, convert, and document the unique super-event music | `prompts/025_super_event_audio_researcher_prompt.md` |

## Post-implementation audits

| Order | Subagent | Mode | Purpose | Prompt |
| ---: | --- | --- | --- | --- |
| 1 | `chaosx_ai_probability_auditor` | Read-only | Compare every weighted patch with baseline scenarios | `prompts/025_ai_probability_auditor_prompt.md` |
| 2 | `chaosx_decision_mission_auditor` | Small patch-capable | Audit action quality, costs, AI, cleanup, and exploits | `prompts/025_decision_mission_auditor_prompt.md` |
| 3 | `chaosx_localisation_auditor` | Small patch-capable | Audit every visible text surface and dynamic key | `prompts/025_localisation_auditor_prompt.md` |
| 4 | `chaosx_event_completion_auditor` | Read-only | Compare final repository state with every accepted requirement | `prompts/025_event_completion_auditor_prompt.md` |
| 5 | `chaosx_documentation_curator` | Documentation-only patch | Reconcile specs, plans, handoffs, docs, evidence, and resume state | `prompts/025_documentation_curator_prompt.md` |
| 6 | `chaosx_spreadsheet_doc_worker` | Workbook-only patch | Update authoritative XLSX and regenerate CSV exports | `prompts/025_spreadsheet_prompt.md` |

## Parent implementation prompt

Use:

- `prompts/025_coding_prompt.md` for the full coding agent
- `prompts/025_goal_prompt.md` for the bounded project goal

## Deliberately unused subagents

### Country package auditor

No country is created, released, restored, or transformed.

### Focus tree auditor

No focus tree is created or modified.

### Portrait creator

No named leader, commander, operative, advisor, or scientist portrait is required.

### 3D model pipeline

No map entity, unit model, aircraft model, building model, counter, or skeletal action has a direct Event 025 consumer.

### Skill maintainer

The planning task did not reveal a new reusable workflow that is not already covered by the current event, decision, GUI, asset, animation, super-event, and improvement skills. A future implementation may use the maintainer if a repeated technical pattern emerges.

## Audit-patch-compare requirement

Any change to AI weights, MTTH, random lists, target weights, or other probability-bearing logic must follow:

1. baseline probability auditor
2. owner patch
3. probability compare with the same named scenarios

No patch-capable auditor may bypass this cycle.

## Handoff requirement

Every patch-capable subagent writes a handoff under:

`docs/plans/025_alien_technology_in_antarctica_plans/subagent_handoffs/`

Every handoff lists changed files, identifiers, before and after behavior, meaningful validation, skipped evidence, remaining gaps, and parent follow-up.
