# Event 34 Industrial Boom decision and mission implementation prompt

## Assignment

Implement the Event 34 decision and mission layer from the complete specification pack. The result must give the affected country a compact economic management loop built around one public value, `Overheating`, real material commitments, state projects, controlled landing, and AI-equivalent behavior.

Do not turn the category into a political power shop. Do not expose the hidden simulation as a wall of counters. Do not create a dedicated scripted GUI unless direct inspection proves that the normal decision category, category picture, progress display, scripted localisation, and state target flow cannot present the accepted mechanic clearly.

## Required reading and inspection

Read before editing:

- `AGENTS.md`
- every Event 34 specification part
- `034_industrial_boom_decision_map.md`
- `034_industrial_boom_ai_probability_matrix.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- the current Event 34 and Event 35 source when implementation has begun
- current Chaos Redux decision categories with dynamic values, state targeting, missions, and staged category lifecycle
- relevant offline Paradox wiki pages, installed vanilla documentation, and vanilla decision precedents

Use the HOI4 MCP decision, event, probability, and GUI routes that apply to the final implementation. A missing required route is a blocker for the affected validation claim.

## Public mechanic presentation

The category presents:

- current Overheating on a 0 to 100 scale
- broad trend state
- next meaningful threshold and consequence
- current boom phase
- reserve status as a compact qualitative state or icon
- selected Industrial Region when a state action needs a target

Overheating is the only persistent event-specific number the player actively manages. Reserve capacity, structural progress, exposure, project risk, labor strain, material pressure, speculative pressure, and state vulnerability remain hidden or qualitative unless a direct action needs a concise explanation.

Use one strong static category picture and a clear progress treatment. Keep the category header within one to three short lines. Tooltips for one value or action should normally fit within two to four short lines while still stating important thresholds, costs, and consequences.

## Visibility budget

A normal phase should expose three to five primary actions. Six is the hard maximum during an emergency. Active missions should normally stay between one and two, with three allowed only when each objective demands a distinct action.

Hide obsolete actions, invalid targets, completed projects, and evolution-specific actions outside their valid state. Replace basic actions with stronger later versions where appropriate instead of stacking every version in the category.

## Core decisions

### Run the Economy Hot

Role: deliberate short-term exploitation.

Visible result:

- stronger temporary industrial output and construction performance
- immediate and continuing Overheating pressure
- increased incident and shock exposure
- faster project progress when the country can actually supply the expansion

Requirements:

- active boom
- no cooling lock
- enough usable industrial capacity to benefit
- not already at a terminal safety block

Cost model:

- temporary output commitment or consumer burden as appropriate
- material or logistical pressure as a consequence
- no mandatory political power purchase

AI use: high during urgent war production or a short opportunity window, low when supply is broken, the country is close to capitulation, Overheating is dangerous, or the added output cannot be used.

### Stabilize Supply Chains

Role: repair the physical network supporting the boom.

Visible result:

- lower immediate Overheating
- reduced near-term drift
- protection against selected logistics shocks
- support for region project continuity

Dynamic costs may use no more than four spendable types and should select from trains, motorized equipment, convoys, fuel, support equipment, and civilian factory commitment according to the country's actual logistics profile. A landlocked country should not pay an irrelevant convoy cost. An import-dependent maritime country should not receive full protection without addressing ports and convoys.

AI use: high after rail, port, convoy, fuel, infrastructure, or supply disruption and when valuable regions are exposed.

### Build Industrial Reserves

Role: sacrifice immediate production to create spare capacity, inventories, and repair margin.

Visible result:

- build reserve status
- lower future Overheating shocks
- provide a buffer for accidents, blockade, disaster, or forced landing
- improve controlled-landing quality

Cost model:

- temporary factory output sacrifice
- civilian capacity commitment
- selected equipment or fuel only when the current reserve profile requires it

The action cannot be spammed for unlimited reserve credit. Reserve capacity has a cap, decay or consumption rules, and diminishing efficiency.

AI use: high before expected shocks, at medium Overheating, during peacetime consolidation, or when a valuable project is near completion.

### Cool the Expansion

Role: impose deliberate restraint.

Visible result:

- strong Overheating reduction over a timed period
- weaker temporary boom bonuses
- slower projects
- better landing eligibility

The decision starts a real cooling commitment. The player cannot immediately cancel it and run hot without paying the mapped reversal cost or consequence. Evolution I makes cooling more expensive and politically disruptive.

AI use: mandatory near terminal risk when the country can survive the output loss. A desperate wartime AI may delay cooling only under the bounded conditions in the AI matrix.

### Protect Key Industrial Regions

Role: harden a selected state network against disruption.

Target rules:

- state belongs to the target country or otherwise passes the exact project ownership contract
- state has a valid industrial role
- no duplicate protection receipt
- state selection uses the shared project registry, not a parallel hand-written list

Visible result:

- reduced shock from bombing, blockade, disaster, rail loss, port loss, shortages, or infrastructure damage
- improved project continuity
- possible achievement credit when a real incident is absorbed

Dynamic costs may use civilian factories, trains, support equipment, fuel, and construction time based on the selected state's needs. Protection does not prevent ordinary game damage. It reduces Event 34 pressure and project loss caused by that damage.

AI use: prioritize high-value, high-exposure, supply-critical, and nearly completed project states.

## State project actions

Implement a bounded state-target flow for Industrial Regions. The player should select one relevant region at a time, then see only actions valid for that state.

Expected action families include:

- survey regional capacity
- designate or confirm an Industrial Region
- expand rail and infrastructure links
- add reserve and repair capacity
- harden the region
- complete a structural conversion
- cancel a speculative or unsafe project
- restore a disrupted project

Every project needs a clear start, active state, completion receipt, interruption behavior, ownership or control transfer rule, landing conversion, depression inheritance, and cleanup condition. Project completion must not be inferred only from current building levels.

## Missions and timed objectives

### Controlled Landing

This is the central resolution objective. It should open once the boom has produced enough structural progress or lasted long enough to require normalization.

The objective evaluates:

- Overheating below the valid landing ceiling
- a sustained control period
- minimum structural progress
- reserve readiness
- no unresolved terminal shock
- retained control of the required project network

Success resolves the boom through the controlled-landing calculation. Failure may extend the dangerous phase, force a rough landing, or cause a crash according to current conditions. Do not use one final threshold reading as the whole outcome.

### Secure the Industrial Network

Use this objective when active disruptions threaten key regions. It should ask the player to repair or protect named current target states, restore transport access, or maintain control for a dynamic period. It must auto-complete when the objective is met.

### Evolution objectives

Evolutions may replace or expand the central objective:

- contain speculative exposure under Evolution I
- complete and stabilize Miracle Regions under Evolution II
- contain outward industrial spread and land a Runaway Industrialization economy under Evolution III

Do not show all evolution objectives at once.

## Cost and requirement rules

- One action may use at most four spendable cost types.
- Every displayed cost uses the correct texticon and dynamic amount.
- Non-consumed conditions are requirements, not hidden costs.
- Costs scale with economy size, boom intensity, project count, evolution, repeat memory, logistics profile, and current crisis state.
- Use concrete economic and logistical costs before political power or command power.
- Name dynamic state targets and relevant regions in tooltips.
- Long trigger blocks must be hidden behind concise custom tooltips.

## AI requirements

Every human action needs an AI-equivalent path. The AI must read:

- Overheating band and trend
- war urgency
- usable military and civilian production demand
- supply, fuel, train, motorized, convoy, and trade condition
- reserve status
- project value and exposure
- stability and capitulation risk
- current evolution
- repeat memory
- expected landing quality

Implement the profile and scenario ordering from `034_industrial_boom_ai_probability_matrix.md`. Route all complex weights through a baseline audit, owner patch, and mandatory `hoi4.probability_compare` pass with the same named scenarios.

## Cleanup and exploit controls

Test and handle:

- target annexation
- civil war and tag split
- state transfer and occupation change
- capital loss
- peace and war transitions
- Event 35 already active
- repeat firing after successful legacy
- invalid or empty region pool
- duplicate project starts
- decision cost refund after failed target resolution
- category cleanup after landing or crash
- stale target selection
- reserve farming
- project completion farming
- click spam and overlapping timed effects

## Assets and localisation

Use distinct decision icons, a distinct category icon, a static category picture family for major phases, project and state modifier icons, Overheating and trend indicators, reserve states, and landing states as mapped in the asset prompt. Do not resize one icon family to satisfy another.

Localisation must express public action, visible cost, immediate direction, and known risk. It must not reveal hidden rolls, future incidents, evolution surprises, or exact inheritance calculations.

## Required review and evidence

After implementation:

- Run `chaosx_decision_mission_auditor`.
- Run `chaosx_ai_probability_auditor` before and after every weighted patch.
- Run `chaosx_localisation_auditor` for the category, decisions, missions, costs, blocked states, and scripted localisation.
- Use `chaosx_event_ui_worker` only if the accepted presentation is formally changed to an event-owned scripted GUI.
- Run `chaosx_event_completion_auditor` before the event completion claim.

Return:

- decision and mission coverage table
- visible action counts by phase
- full cost matrix with scaling factors
- AI scenario results and probability comparison evidence
- cleanup and exploit scenario results
- asset and localisation coverage
- files and identifiers changed
- every simplification, merge, substitution, missing action, or blocker
