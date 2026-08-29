# Famine and Migration Mechanics Planning Package

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

This folder is the source design package for a shared Chaos Redux system. It is not an event and it has no event ID.

> **Superseded incident-layer note (2026-08-25):** Any historical wording in this package about incident events, event-option probability, `famine_incident.1`, `migration_incident.1`, `fm_*`, or combined `famine_migration_*` planning IDs is superseded. The two register helpers are accounting/presentation seams only, the incident event files and constants were deliberately deleted, and current runtime names are separate `famine_*`, `migration_*`, or narrow neutral primitives.

The design joins four related gameplay layers:

1. State food security and famine severity.
2. Exact civilian population losses recorded through the shared Deaths system.
3. Internal displacement, cross-border flight, evacuation, deportation, reception, return, and integration.
4. Occupation, atrocity, outbreak, bombing, nuclear, environmental, diplomatic, and event adapters that feed the same shared model.

The central design rule is that famine and migration remain dynamic. Historical cases provide pressure profiles, triggers, policy patterns, and regional memory. They never impose a fixed death total or a fixed migration total.

## Intended extraction path

Extract this top-level folder into:

```text
docs/specs/famine_and_migration_system_specs/
```

The implementation agent should place working subagent plans and audit handoffs under:

```text
docs/plans/famine_and_migration_system_plans/
```

## Source specification files

- `famine_and_migration_system_spec_part_1_core.md`
- `famine_and_migration_system_spec_part_2_famine_food_security.md`
- `famine_and_migration_system_spec_part_3_displacement_migration_return.md`
- `famine_and_migration_system_spec_part_4_deaths_occupation_atrocity.md`
- `famine_and_migration_system_spec_part_5_historical_profiles.md`
- `famine_and_migration_system_spec_part_6_decisions_ai_presentation.md`
- `famine_and_migration_system_spec_part_7_cross_system_connections.md`
- `famine_and_migration_system_spec_part_8_balance_acceptance.md`

## Supporting design records

- `famine_and_migration_system_research_bibliography.md`
- `famine_and_migration_system_historical_profiles.csv`
- `famine_and_migration_system_integration_matrix.csv`
- `famine_and_migration_system_death_reason_ownership.csv`
- `famine_and_migration_system_probability_scenarios.csv`
- `famine_and_migration_system_decision_map.csv`
- `famine_and_migration_system_asset_matrix.csv`
- `famine_and_migration_system_input_manifest.csv`
- `famine_and_migration_system_output_manifest.csv`
- `famine_and_migration_system_implementation_surface_map.md`
- `famine_and_migration_system_subagent_routing.md`
- `famine_and_migration_system_subagent_execution_status.md`
- `famine_and_migration_system_improvement_loop_closure.md`

## Implementation prompt files

- `famine_and_migration_system_asset_prompt.md`
- `famine_and_migration_system_achievement_prompt.md`
- `famine_and_migration_system_decision_mission_prompt.md`
- `famine_and_migration_system_coding_prompt.md`
- `famine_and_migration_system_goal_prompt.md`

Context-complete prompts for the relevant project subagents are under `subagent_prompts/`.

## Non-negotiable design outcomes

- Famine is a state system with visible severity and meaningful deaths when ignored.
- Deaths use real state population loss and the shared Deaths ledger.
- The Deaths breakdown includes `From famine`.
- Migration moves population between real states. Movement is not counted as death.
- Route deaths are tracked separately and only occur when a route is dangerous or people are trapped.
- An island under wartime blockade receives strong famine pressure only when isolation, port, convoy, and corridor evidence supports that result.
- Air Cleanliness affects food production, transport, recovery, and nuclear-winter risk.
- Occupation policy, camps, gulags, deportation, forced labor, genocide, bombing, nuclear attacks, outbreaks, natural disasters, sanctions, and relevant events all use shared adapters.
- Ideology affects flight and destination choice as one bounded factor. Direct persecution, atrocity, bombing, famine, and route safety can outweigh ideology.
- The famine and migration decision categories are separate and independently hidden until their own mechanic has a genuine problem. Register helpers record accounting/presentation context only; no incident event layer exists. Migration becomes available only after displacement becomes a sustained national issue.
- AI receives the same usable response paths as the player.
- The system uses event-driven and active-registry processing. It does not require a whole-world daily, weekly, or monthly scan.
- Event 149 `Immigrations` is absorbed or retired so the mod has one migration model.

## Reading proof and limitations

The input manifest records every supplied project file and every extracted subagent definition with size and SHA-256. All listed files were fully read before this package was written.

This environment did not expose the Windows Chaos Redux repository, the offline Paradox wiki snapshot, installed vanilla game files, the HOI4 MCP server, or a callable custom-subagent runtime. The package therefore contains repository-ready design, research, matrices, and context-complete subagent prompts. The coding prompt requires the implementation agent to perform the mandatory local source, wiki, vanilla, MCP, and probability passes before editing or claiming completion.
