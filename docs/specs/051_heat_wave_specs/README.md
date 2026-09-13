# Event 051 Heat Wave Specification Package

## Status

This package is the source design for the rework of Event 051, Heat Wave.

It expands the attached rough brief into a full implementation specification. It is planning material, not a claim that the event has been implemented in the repository.

## Catalog identity

| Field | Accepted design |
| --- | --- |
| Event ID | `051` |
| Event name | Heat Wave |
| Type | Minor Repeatable |
| Chaos level | 1, Calm World |
| Cluster | Natural Disasters |
| Member severity | High |
| Current design status | To Be Reworked |

The supplied event catalog CSV still identifies Event 51 as Minor Fire-Once. The attached rough brief is newer and more detailed, so this package treats Minor Repeatable as the accepted type. The authoritative workbook must be corrected during implementation and the CSV exports must then be regenerated.

## Design summary

Event 051 creates a persistent global heat crisis whose intensity changes over time. Every valid state receives a dynamic Heat Stress state derived from climate, terrain, population, infrastructure, water access, supply, active war conditions, prior devastation, and mitigation. The event can ease, surge, and return before entering a gradual recovery.

The player tracks only two event-specific values:

1. **Global Heat Wave Intensity**, a worldwide 0 to 100 value with a named stage and visible trend.
2. **Local Heat Stress**, a qualitative state condition with a visible trend and hotspot presentation.

Water pressure, agricultural pressure, industrial cooling load, military exposure, accumulated environmental exposure, and mitigation strength remain internal. They appear as causes, warnings, target priorities, and consequences instead of becoming additional meters.

The baseline event disrupts armies, water, agriculture, industry, transport, and daily life. Evolution I makes heat systematically lethal. Evolution II permits gradual permanent environmental degradation. Evolution III can make large areas temporarily close to uninhabitable and permits rare final degradation into wasteland.

## File index

### Event design

- [00 Catalog and core contract](00_catalog_and_core_contract.md)
- [01 Player experience and design pillars](01_player_experience_and_design_pillars.md)
- [02 Lifecycle and episode state machine](02_lifecycle_and_episode_state_machine.md)
- [03 Global Heat Wave Intensity](03_global_heat_wave_intensity.md)
- [04 State Heat Stress model](04_state_heat_stress_model.md)
- [05 Military operations under extreme heat](05_military_operations.md)
- [06 Civilian water, health, and daily life](06_civilian_water_health_and_daily_life.md)
- [07 Agriculture, famine, and migration](07_agriculture_famine_and_migration.md)
- [08 Industry, power, transport, and infrastructure](08_industry_power_transport_and_infrastructure.md)
- [09 Decisions and missions](09_decisions_and_missions.md)
- [10 Flavour and report event families](10_flavour_and_report_event_families.md)
- [11 Evolutions](11_evolutions.md)
- [12 Environmental degradation and terrain](12_environmental_degradation_and_terrain.md)
- [13 Shared-system and event connections](13_shared_system_and_event_connections.md)
- [14 AI strategy and probability scenarios](14_ai_strategy_and_probability_scenarios.md)
- [15 Chaos, event logs, cluster behavior, and repeatability](15_chaos_logs_cluster_and_repeatability.md)
- [16 Presentation and writing direction](16_presentation_and_writing_direction.md)
- [17 Asset and animation specification](17_asset_and_animation_specification.md)
- [18 Evolution III super-event](18_evolution_iii_super_event.md)
- [19 Achievements](19_achievements.md)
- [20 Balance, exploits, performance, and multiplayer](20_balance_exploits_performance_and_multiplayer.md)
- [21 Implementation architecture and file map](21_implementation_architecture_and_file_map.md)
- [22 Validation and acceptance scenarios](22_validation_and_acceptance_scenarios.md)
- [23 Catalog and documentation alignment](23_catalog_and_documentation_alignment.md)
- [24 Scope closure and anti-bloat ruling](24_scope_closure_and_anti_bloat_ruling.md)

### Implementation prompts

- [Master implementation prompt](prompts/implementation_master_prompt.md)
- [Scripted-system architect prompt](prompts/scripted_system_architect_prompt.md)
- [Decision and mission audit prompt](prompts/decision_mission_audit_prompt.md)
- [Asset production prompt](prompts/asset_production_prompt.md)
- [Super-event research prompt](prompts/super_event_research_prompt.md)
- [AI probability audit prompt](prompts/ai_probability_audit_prompt.md)
- [Completion audit prompt](prompts/completion_audit_prompt.md)
- [Catalog workbook update prompt](prompts/catalog_workbook_update_prompt.md)
- [Compact goal prompt](prompts/goal_prompt.txt)

### Quality and evidence

- [Source reading ledger](quality/source_reading_ledger.md)
- [Research evidence and design implications](quality/research_evidence.md)
- [Subagent role synthesis](quality/subagent_role_synthesis.md)
- [Specification coverage matrix](quality/specification_coverage_matrix.md)
- [Simplifications, omissions, and blockers](quality/simplifications_omissions_and_blockers.md)
- [Package validation](quality/package_validation.md)
- [Package manifest](PACKAGE_MANIFEST.md)

## Implementation order

The safest implementation order is:

1. Reconcile the event type and cluster data in the authoritative workbook only after the gameplay design is accepted.
2. Inspect the live Event 051 namespace, Event 013 disaster gateway, Deaths API, Famine adapter, Migration adapter, event-log registry, Natural Disasters cluster registry, state map-mode framework, and current supported terrain tooling.
3. Build the event-owned data model and lifecycle helpers.
4. Build bounded state registration and Heat Stress processing.
5. Add temporary state, country, unit, economy, and supply consequences.
6. Add decisions and missions with AI-equivalent paths.
7. Add the three evolution tracks and their log behavior.
8. Add Deaths, Famine, Migration, wildfire, and Air Cleanliness adapters.
9. Add environmental degradation only after map tooling proves the intended terrain path is safe.
10. Add presentation, assets, super-event research, achievements, and catalog wording.
11. Run event-chain, probability, map, decision, localisation, completion, and live user validation passes required by the repository rules.

## Reading limitation

All supplied project files, all three supplied CSV exports, and every TOML definition inside the supplied subagent archive were read in full. The live Windows repository, offline Paradox wiki snapshot, installed vanilla Hearts of Iron IV files, approved reference mods, and HOI4 MCP server were not mounted in this environment. This package therefore specifies the required inspections and evidence gates but does not pretend those repository and engine checks occurred.
