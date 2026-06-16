# Decision and Mission Implementation Prompt — Event 013 Natural Disasters

Use `hoi4-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`. Implement the Disaster Response decision category and mission families according to the source spec and the decision matrix.

## Source files

- `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_spec_part_1.md`
- `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_evolutions_and_variants.md`
- `docs/specs/013_natural_disasters_specs/matrices/013_natural_disasters_decision_mission_map.md`
- `docs/specs/013_natural_disasters_specs/matrices/013_natural_disasters_ai_balance_and_validation.md`

## Must implement

1. Disaster Response Office decision category visible only when a country has active warning, impact, recovery, regional aid, or scenario context.
2. Warning decisions for relief trains, evacuation, flood barriers, port closure, air wing relocation, rationing, dam/tunnel inspection, and observatory alerts where supported by implemented families.
3. Impact/recovery decisions for engineers, medical columns, convoys, railway repair, shelters, firebreaks, ash cleanup, shoreline rescue, factory shutdown, and crater survey.
4. Timed missions for rail restoration, dam watch, port recovery, drought food relief, ash cleanup, rehousing displaced people, mountain pass guard, and crater survey.
5. Cross-border aid decisions for regional disasters, with clear AI validity checks.
6. Dynamic, icon-first costs using equipment, trucks, trains, convoys, fuel, manpower, factories, stability, war support, command power, army XP, supply, or unit presence where appropriate.
7. Custom trigger tooltips and dynamic localisation naming the affected area and missing resources.
8. AI `ai_will_do` that considers disaster family, severity, country size, war state, stability, available resources, capital/factory/port/supply value, and relation/faction context.
9. Cleanup for obsolete decisions and missions when aftermath ends, state changes owner, target country disappears, scenario ends, or world-end freezes normal events.

## Must not do

- Do not create a political-power store.
- Do not show every possible disaster response at once.
- Do not expose raw triggers or state id lists.
- Do not give net-positive farmable rewards for recovery.
- Do not require chaos tier or prior event history for the manual scenario.

## Audit requirement

After implementation, run `chaosx_decision_mission_auditor` for the category. The auditor should inspect objective quality, costs, duplicate missions, AI validity, tooltip clarity, cleanup, and exploit risk. Any patch must produce a handoff under `docs/plans/013_natural_disasters_plans/subagent_handoffs/`.
