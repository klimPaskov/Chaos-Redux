# Famine and Migration System Handoff Dispositions

This file records the parent review of every project-subagent handoff used to implement the shared famine and migration system.

## Repository exploration

Source: `docs/plans/famine_and_migration_system_plans/repo_exploration.md`

Disposition: partially accepted.

Accepted findings:

- Reuse `apply_exact_state_civilian_population_loss` and `apply_state_population_loss_without_recruitable_manpower_gain` from `common/scripted_effects/chaosx_dynamic_effects.txt`.
- Use the shared event-log, cluster, scenario, achievement-registry, scoped-hook, and workbook surfaces identified in the report.
- Treat Event 149 as absent source rather than an implemented event chain.
- Record the Event MCP large-workspace projection limitation as a validation blocker where it recurs.

Rejected or superseded findings:

- The Deaths owners are resolved as `common/script_constants/chaos_meter_constants.txt`, `common/scripted_effects/chaos_meter_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt`, and `localisation/english/chaosx_chaos_meter_l_english.yml`.
- Air Cleanliness owners are resolved through `common/scripted_effects/fallout_consolidated_effects.txt` and its paired trigger/constants surfaces.
- Condemnation owners are resolved through `common/script_constants/condemnation_sanctions_constants.txt`, `common/scripted_effects/condemnation_sanctions_effects.txt`, and `common/scripted_triggers/condemnation_sanctions_triggers.txt`.
- Camp and genocide owners are resolved through `common/scripted_effects/camp_repression_rework_effects.txt`, `common/scripted_effects/genocide_crisis_effects.txt`, and their paired trigger and constants files.
- `chaosx_ai_probability_auditor` is callable in this runtime. The claimed tool blocker is rejected.
- Event 149 requires no additional design decision. The binding specification authorizes retirement and absorption, forbids a replacement event ID, and forbids an event-pacing weight.
- Missing roots 118, 120, and 131 are catalog/integration gaps, not permission to invent event sources. Event 013 remains the current volcano/disaster owner.

## Pre-change AI probability audit

Source: `docs/plans/famine_and_migration_system_plans/ai_probability_baseline.md`

Disposition: accepted.

The audit proves that Event 149 and all shared famine/migration weighted surfaces are absent before implementation. All twenty named scenarios are retained as unresolved baseline cases. The owner patch must define complete pools and scenario inputs, then the same scenario IDs must be rerun through `hoi4.probability_compare` before balance or completion can be claimed.

## Map inspection

Source: HOI4 MCP artifact `map-inspect.de30e4f6849d41e0.json` for representative historical-profile states 7, 113, 195, 271, 295, 335, 671, and 935.

Disposition: accepted with an unrelated map-validation blocker.

The inspection resolved all eight requested state records and passed province definitions, bitmap geometry, state and strategic-region membership, adjacency, supply, and railway checks. The workspace-wide locator pass also reported pre-existing invalid floating-harbor/building positions in `map/buildings.txt`, with diagnostics truncated after 1,999 retained entries and 2,654 omitted errors. This system will not edit map geometry or claim that those unrelated locator errors are resolved.
