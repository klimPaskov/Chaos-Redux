# Decision and Mission Prompt: Separate Famine and Migration Mechanics

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, separate `famine_decision_category` and `migration_decision_category`, and separate `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

Use `chaos-redux-decisions-missions` to implement and audit the famine response, evacuation, border, reception, integration, resettlement, and return decision families.

These are separate mechanics with no event IDs, event objects, event-pool entries, or event-pacing surfaces.

## Source design

Read:

- all eight system specification parts
- `famine_and_migration_system_decision_map.csv`
- `famine_and_migration_system_probability_scenarios.csv`
- `famine_and_migration_system_asset_matrix.csv`
- `famine_and_migration_system_coding_prompt.md`

## Category lifecycle

Use the separate runtime categories `famine_decision_category` and `migration_decision_category`; the umbrella project filename is documentation-only and is not a runtime identifier.

Each category is hidden until its own mechanic has a genuine starting problem or reaches its own evidence threshold.

`famine_register_initial_incident` and `migration_register_initial_incident` are accounting and presentation seams only. They do not create event objects, event IDs, event-pool entries, event-log rows, random events, or pacing pulses; the deleted incident event files and constants are deliberate.

Unlock each category only after a meaningful mechanic-specific issue, such as famine supply strain for famine or a large/repeated/sustained displacement, trapped population, corridor, or reception problem for migration.

Close the category when all active flows, trapped populations, reception obligations, return work, and recent issue memory are resolved. Preserve policy memory so it can reopen later.

## Presentation budget

The category should show:

- one primary value, Displacement Load
- one support value, Reception Capacity
- one policy state, Border Policy
- one to three active missions
- three to five primary actions in normal phases
- no more than six primary actions in any phase

Use an ordinary category with a static category picture, concise dynamic header, state targeting, and map highlights.

Do not create a shared full scripted GUI.

## Decision families

Implement every accepted row in `famine_and_migration_system_decision_map.csv` that is supported by the final repository and engine review.

Required families include:

- rationing and reserve release
- emergency imports
- relief-route repair
- escorted relief convoy
- emergency airlift
- foreign relief and observers
- famine evacuation
- requisition from safer states
- concealment and continued extraction
- evacuation preparation
- vulnerable-civilian evacuation
- skilled-worker evacuation
- departure-route opening or restriction
- humanitarian corridors
- emergency reception
- controlled medical reception
- distribution among safe states
- transit
- border closure and enforcement
- local integration
- third-country resettlement
- voluntary return
- forced repatriation

## Cost standard

Use no more than four spendable cost types for any one decision or gameplay-changing action.

Prefer concrete costs:

- trains
- convoys
- trucks
- support equipment
- fuel
- civilian factory burden
- food reserves
- reception capacity
- manpower for relief administration
- stability or war support where policy creates a real domestic sacrifice
- limited XP or command power only for specialized military operations

Political power can support diplomatic or political decisions. It must not be the only cost for logistical relief or movement.

Use compact icon-first cost localisation and valid texticons.

## Missions

Missions must require actual action.

Required objective families include:

- keep a named corridor open
- repair or hold a named rail, port, hub, or border route
- protect evacuation transport
- deliver relief before reserves fail
- prevent reception collapse
- prepare a safe return route

Do not use passive stockpile or stability checklists as the whole objective.

Use enough time for the player and AI to act. Scale duration with route length, damage, severity, and military pressure.

## Target selection and clutter control

Do not expose one permanent decision per affected state.

Use the existing selected-target pattern, priority pools, urgent-state caps, regional grouping, or dynamic activation.

The same eligibility helper must control:

- visible state selection
- decision availability
- map highlight
- tooltip status
- effect target

Clear stale targets after annexation, control change, route loss, peace, recovery, and country transformation.

## AI

Give AI countries the same usable action paths.

Route every complex weight through `chaosx_ai_probability_auditor` before and after any patch.

Use the named scenarios in the probability matrix.

AI must not:

- choose invalid routes
- send civilians to famine, camps, fallout, or active fronts
- admit arrivals with no destination state
- delete a cohort through closure or forced return
- repeat completed integration
- spend all critical military transport without survival logic
- force return to a known lethal origin unless regime policy supports the consequences

## Tooltips and text

Write final player-facing localisation from the tone direction in Part 6.

Every action must explain:

- current target
- public requirement
- costs
- visible result
- visible risk or tradeoff

Do not expose hidden weights, secret outcomes, future evidence paths, or raw variables.

Do not describe refugees as inherently diseased. Controlled medical reception requires proven outbreak exposure.

## Audit and handoff

After implementation, spawn `chaosx_decision_mission_auditor` with `fork_context=false`.

The auditor should inspect and patch only bounded issues, then return:

- category lifecycle coverage
- decision-row coverage
- mission quality
- cost compliance
- state-target cleanup
- AI and probability evidence
- exploit findings
- localisation keys
- assets used
- remaining blockers

Do not claim the decision system complete while any accepted row is missing, simplified, or replaced without explicit approval.
