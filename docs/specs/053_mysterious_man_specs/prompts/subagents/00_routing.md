# Event 53 Subagent Routing

Every project subagent must be invoked with `fork_context=false` and a complete prompt.

## Relevant implementation agents

| Order | Agent | Role |
| ---: | --- | --- |
| 1 | `chaosx_repo_explorer` | Map the existing Event 53 namespace, owner APIs, source-event bookkeeping, vanilla precedents, and implementation order |
| 2 | `chaosx_scripted_system_architect` | Implement or review the Event 53 owner-side constants, triggers, effects, transaction state, demand engine, registry, and receipts |
| 3 | `chaosx_generated_event_art` | Produce the five report-event scenes |
| 4 | `chaosx_ai_probability_auditor` | Audit target, demand, package, interval, and affordability selection through the mandatory MCP workflow |
| 5 | `chaosx_localisation_auditor` | Review and patch all Event 53 player-facing text after implementation |
| 6 | `chaosx_documentation_curator` | Reconcile specifications, implementation docs, adapter status, handoffs, and source-of-truth state after a long implementation tranche |
| 7 | `chaosx_spreadsheet_doc_worker` | Update the authoritative workbook after final in-game wording exists |
| 8 | `chaosx_event_completion_auditor` | Compare every accepted requirement with the final implementation |
| 9 | `chaosx_improvement_loop_planner` | Perform a closure review and reject unnecessary broad expansion unless implementation exposed a new gap |

## Agents not required by the accepted design

The accepted event does not create a focus tree, country package, decision category, dedicated scripted GUI, character portrait, icon family, 3D model, or super-event. The matching agents should not be spawned for Event 53 unless the user later expands scope.

The autonomous debug-playtest skill remains explicit-invocation-only and is not part of this implementation route.
