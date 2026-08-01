# Event 016 external-incident bridge handoff

Date: 2026-08-01

Scope: bounded content tranche for the accepted Event 023, Event 027, and Event 028 world-reaction links.

## Implemented

- `chaosx.nr23.2` records the Soviet nuclear milestone only when SOV is the active Kruger host.
- `chaosx.nr27.2` records one external military-research posture after any of its four doctrine choices for an active Kruger host.
- `chaosx.nr28.2` records one exposure and capacity shock after either the predicted or unpredicted asteroid outcome for an active Kruger host.
- Each bridge uses a country receipt and a fixed `KRG_warren_kruger` character receipt, so ordinary transfer and fixed-tag Kruger State formation cannot replay the consequence.
- Meter deltas are centralized in `brilliant_scientist_external_incident` and only call the existing Directorate value helpers.
- Source events retain their normal nuclear, doctrine, damage, prediction, news, construction, and state outcomes.
- No project stage, free unit, evolution, Event Log row, asset, or model dependency was added.

## Changed files

- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`
- `common/scripted_effects/016_brilliant_scientist_context_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt`
- `events/023_soviet_nukes.txt`
- `events/027_doctrine_research.txt`
- `events/028_asteroid_impact.txt`
- `localisation/english/016_brilliant_scientist_l_english.yml`
- `docs/events/016_brilliant_scientist/overview.md`
- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_7_world_reactions_and_ai.md`

## Validation evidence

- Braces balance and unsupported-operator scans returned clean results for all seven gameplay files.
- Event 023, Event 027, and Event 028 focused `hoi4.event_inspect` lint returned `status = ok`, `EVENT_INSPECTED_PARTIAL`, and zero blocking diagnostics; the MCP deferred workspace-wide helper projections.
- The Event 016 localisation file retains a UTF-8 BOM and all three new tooltip keys resolve in source.
- The seven country and character receipt identifiers are present in the source, transfer helper, formation helper, and localisation/docs surfaces where applicable.

## Remaining risks and follow-up

- Live event ordering, transfer during an external event, and UI presentation remain user-owned validation because the agent must not launch Hearts of Iron IV.
- The seven bespoke Event 016 project-force 3D packages remain deferred by user instruction; current unit consumers keep their documented temporary presentation boundary.
- Event 137 and Event 151 are described in the accepted specification but have no source events in this repository, so no unwired bridge was invented for them.
