# Famine and Migration Mechanics Subagent Routing

All project subagent definitions supplied in `subagents.zip` were fully read before this routing plan was written.

Every project subagent must be spawned with `fork_context=false`. The parent prompt must point to the extracted source spec folder and include every needed constraint.

## Mandatory implementation and audit route

| Subagent | Route | Timing | Main output |
| --- | --- | --- | --- |
| `chaosx_repo_explorer` | Required | Before implementation edits | Complete repository, wiki, vanilla, MCP, and touched-file map |
| `chaosx_scripted_system_architect` | Required | After exploration and before broad helper implementation | Shared adapter, registry, variable, constant, and exact-transfer architecture plus bounded patches |
| `chaosx_ai_probability_auditor` | Required | Before weighted patches and again after patches | Named baseline scenarios, probability evidence, and mandatory comparisons |
| `chaosx_decision_mission_auditor` | Required | After decision and mission implementation | Category lifecycle, cost, mission, AI, cleanup, clutter, and exploit audit plus bounded fixes |
| `chaosx_localisation_auditor` | Required | After broad visible text exists | Key coverage, scripted localisation, dynamic text, tone, tooltip, and encoding audit plus bounded fixes |
| `chaosx_icon_artist` | Required | After stable asset IDs and consumers are locked | Gameplay icon and supported texticon package |
| `chaosx_generated_event_art` | Required for generic report art | After report-image briefs and final sizes are locked | Period-authentic generated report images, processed outputs, manifest, and handoff |
| `chaosx_documentation_curator` | Required | After major implementation and subagent handoffs | Source-of-truth map, plan dispositions, permanent docs reconciliation, and resume packet if needed |
| `chaosx_improvement_loop_planner` | Required | Near completion after a meaningful implementation tranche | Expansion addendum or closure handoff. The previous plan must be resolved before another pass. |
| `chaosx_event_completion_auditor` | Required as a shared-system audit | Final read-only audit | Spec-versus-implementation coverage and all blockers or simplifications |
| `chaosx_spreadsheet_doc_worker` | Required after implementation facts are final | After localisation and docs settle | Authoritative workbook update and CSV export |

## Conditional route

| Subagent | Route | Condition |
| --- | --- | --- |
| `chaosx_asset_source_researcher` | Conditional | Use for archival report images or real historical picture requirements with rights and provenance. |
| `chaosx_skill_maintainer` | Conditional | Use if implementation creates a reusable famine, migration, exact-transfer, or active-registry workflow that belongs in a project skill. |
| `chaosx_country_package_auditor` | Conditional | Use only if a downstream event or historical profile changes a specific country's starting package, ideas, leaders, units, or playable setup. Neither mechanic creates a country. |
| `chaosx_focus_tree_auditor` | Conditional | Use only if implementation adds or changes country focus hooks. Neither mechanic requires a focus tree. |

## Explicitly excluded route

| Subagent | Reason |
| --- | --- |
| `chaosx_event_ui_worker` | The accepted design uses separate famine and migration decision categories with separate compact report headers. The worker is restricted to a dedicated GUI owned by one named event and must not unite these mechanics in a shared UI. |
| `chaosx_portrait_creator` | The system creates no character or portrait requirement. |
| `chaosx_3d_model_pipeline` | The system creates no custom unit, building, vehicle, creature, or 3D map entity. |
| `chaosx_super_event_text_researcher` | The accepted system design does not create a super-event. Historical and report text belongs to ordinary presentation seams; no incident-event layer exists. |
| `chaosx_super_event_audio_researcher` | The accepted system design does not create a super-event audio package. |

## Asset routing split

- `chaosx_icon_artist` owns decision, category, state-modifier, achievement, and supported Deaths icons.
- `chaosx_generated_event_art` owns generic fictional or dynamic report scenes.
- `chaosx_asset_source_researcher` owns archival images that must show real historical material.
- The parent owns final non-portrait GFX, GUI, gameplay, docs, and catalog wiring.

## Weighted-logic rule

Any patch to an AI weight, MTTH, random selection, destination pool, route pool, political-outcome pool, or decision score requires this order:

1. `chaosx_ai_probability_auditor` baseline with named scenarios.
2. Parent or owning patch agent applies the accepted change.
3. `chaosx_ai_probability_auditor` runs `hoi4.probability_compare` against the same scenarios.

## Handoff paths

Use:

```text
docs/plans/famine_and_migration_system_plans/subagent_handoffs/
```

Every patch handoff must list changed files, identifiers, before and after behavior, task-specific validation, skipped meaningful validation, remaining risks, and parent follow-up.

Plan-only outputs from the improvement loop belong under:

```text
docs/plans/famine_and_migration_system_plans/
```

Accepted design must be folded into the source spec folder before final completion.
