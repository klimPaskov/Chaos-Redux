# Decision and Mission Prompt: Event 064 Border Fortifications

Implement the complete Event 064 response-posture, decision, and mission system defined under `docs/specs/064_border_fortifications_specs/`.

Read the full package, especially:

- `specs/064_border_fortifications_spec_part_3_responses_decisions_and_ai.md`
- `matrices/decision_mission_matrix.md`
- `matrices/ai_probability_scenario_matrix.md`
- `matrices/tuning_and_balance_framework.md`
- `matrices/acceptance_criteria.md`
- `prompts/064_border_fortifications_asset_prompt.md`

Follow `AGENTS.md`, `chaos-redux-decisions-missions`, current repository decision patterns, current AI conventions, the localisation handoff rules, and the event log conventions. Use `fork_context=false` for spawned specialists.

All names below are working labels, not final localisation. Write final player-facing text during implementation.

## Core contract

The Event 064 global construction wave completes before any country response option is selected. Report options choose a temporary posture. They never own, repeat, delay, or cancel the automatic fort grant.

A country can have:

- one current Event 064 posture
- one Event 064 response window
- one active Event 064 sector project
- one target per project

Older posture modifiers must be removed before a new posture applies. Active project state must survive save and reload and must not duplicate after completion.

## Surface design

Use a normal decision category with a static category picture as the complete player surface for posture, deadline, project, and target state.

The category should show:

- current posture
- response time remaining
- active project and target
- highest concrete local evolution package
- clear invalidation reason when no target is available

Use targeted decisions or the current clean map-target pattern. Do not create a long duplicated decision list for every state.

Show the category only while posture, response window, active project, or a linked visible achievement mission requires it. Hide it cleanly afterward.

## Report posture options

Implement three mutually exclusive response postures when valid.

### Integrate the Line

Purpose: improve use, coordination, entrenchment, or repair of local fortifications through valid current modifiers.

Access: local direct frontier, depth position, Fortress State package, or internal redoubt exists.

Main project: Reinforce a Priority Sector.

AI preference: defensive war, capital threat, weaker than enemy, adequate supply and garrison resources.

### Keep the Roads Open

Purpose: improve transport, supply, infrastructure or railway repair, and sustained use of fortified sectors through valid current modifiers.

Access: local affected state has a meaningful network or supply role.

Main project: Connect the New Line.

AI preference: long frontier, poor or damaged network, supply strain, several sectors, adequate train and truck reserves.

### Study the Breach

Purpose: improve attacks against real fort lines through fort-attack, planning, engineer, or target-bound preparation effects supported by the current engine.

Access: a meaningful fortified foreign target exists.

Main project: Conduct Breach Exercises.

AI preference: current or planned offensive, high enemy forts, available Army Experience, support equipment, and fuel.

### Observation-only route

Use a concise acknowledgement and no persistent category when the country has no local result, no redoubt, and no meaningful fortified foreign target.

## Posture duration and replacement

Starting duration: about 180 days.

- show expiry or remaining time
- remove older Event 064 posture first
- never stack posture modifiers
- let a valid active project finish after the response window ends
- prevent new project starts after expiry
- a later wave can replace posture while preserving one still-valid active project

## Project 1: Reinforce a Priority Sector

### Access

- Integrate posture
- open response window
- no active Event 064 project
- controlled affected border state below cap

### Target

One border state with valid direct frontier or anchor positions below the active strategic cap.

### Costs

Use up to four types:

- temporary civilian factory commitment
- infantry equipment
- support equipment
- manpower

Scale with target size, fort gap, industry, stockpiles, war state, and infrastructure. Preserve reserve floors and prevent negative values.

### Duration

Starting range: 45 to 75 days.

### Result

Add one bounded fort package to qualifying direct frontier or anchor positions in the selected state. Respect all Event 064 caps, dedupe rules, and one-package-per-target-state-per-wave limits. Do not fortify every land province in the state.

### Failure

Fail or cancel on target loss, frontier invalidation, annexation, or complete loss of valid building targets. Do not fully refund meaningful elapsed work.

## Project 2: Connect the New Line

### Access

- Keep the Roads Open posture
- open response window
- no active Event 064 project
- affected border or redoubt state with a real network gap

### Costs

Use up to four types:

- temporary civilian factory commitment
- trains
- trucks
- support equipment

Preserve current army supply and transport reserves.

### Duration

Starting range: 60 to 100 days.

### Result priority

1. repair or improve existing damaged infrastructure or rail support
2. add one bounded infrastructure level below cap
3. improve one verified railway connection
4. use a bounded local supply alternative only when a physical network change cannot be represented safely

Do not create a normal free supply hub. Any exceptional hub route needs separate target, cost, and balance proof.

### Failure

Fail on target loss, invalid route, annexation, or loss of every meaningful network result. Remove all target markers and active state.

## Project 3: Conduct Breach Exercises

### Access

- Study the Breach posture
- open response window
- no active Event 064 project
- valid fortified foreign target

### Target

Store one target country and one objective frontier or route context. Exclude allies, invalid tags, targets with no meaningful forts, and targets with no plausible land-war route.

A land-borderless country can qualify through a real invasion or continental-war plan.

### Costs

Use up to four types:

- Army Experience
- support equipment
- fuel
- Command Power

Use a smaller valid bundle for minor countries. Preserve operational reserves.

### Duration

Starting range: 45 to 75 days.

### Reward

Grant a target-bound or tightly fort-scoped preparation for about 90 to 150 days. Use current valid modifiers for fort attack, planning, engineer support, or another accepted equivalent. Do not create a broad permanent attack bonus.

A new completed Event 064 breach preparation replaces the previous one. Copies do not stack.

### Failure

Clean up when the target disappears, becomes an invalid ally, or loses the accepted war route. Do not refund consumed Army Experience after meaningful progress.

## Project 4: Harden the Air and Coastal Flank

### Access

- Evolution II has concretely materialized locally
- selected valid Fortress State exists
- open response window
- no active Event 064 project

Available under any posture. Posture can alter cost, duration, or AI preference without changing target validity.

### Air branch

Target needs an industrial, airbase, supply, capital, missile, nuclear, radar, or enemy-air-threat role.

Use up to four costs:

- temporary civilian factory commitment
- valid air-defense equipment
- Air Experience
- support equipment

Result adds up to two justified improvements under cap, such as state anti-air and radar, with an optional temporary coordination effect.

### Coastal branch

Target needs both a valid foreign land frontier and a coast, port, naval base, supply role, or landing threat.

Use up to four costs:

- temporary civilian factory commitment
- convoys
- Navy Experience
- support equipment

Result adds up to two justified improvements under cap, such as one port or landing-approach coastal fort and radar or state anti-air.

Never charge Air Experience and Navy Experience in the same project bundle.

### Duration

Starting range: 60 to 100 days.

### Limits

- one package per target state per wave
- no full coastline fortification
- no invalid inland coastal branch
- no result when all relevant buildings are capped

## Project 5: Prepare a National Redoubt

### Access

- Evolution III has concretely materialized locally
- valid internal redoubt target exists
- open response window
- no active Event 064 project
- no prior National Redoubt project completed this wave

### Target

Capital, capital approach, major victory point, supply hub, industrial center, major port, or other accepted strategic site.

Default to the capital or capital approach. Allow another valid target through the map interface when the tradeoff is clear.

### Costs

Use up to four types:

- temporary civilian factory commitment
- trains or infantry equipment according to target role
- support equipment
- manpower

### Duration

Starting range: 90 to 140 days.

### Result

Add one land-fort level to the bounded redoubt target below cap. Add at most one support improvement when the target role clearly justifies it. Do not create a full ring around the capital.

### Limits

- one National Redoubt project per country per wave
- target remains controlled and valid
- completion applies once

## Dynamic cost implementation

Centralize tunable values. Use shared dynamic helpers where they already fit. Add an Event 064 helper only when the rule is event-specific.

Cost factors:

- target scope
- relevant building gap
- civilian factory count
- total industry
- manpower
- equipment, train, truck, convoy, and fuel reserves
- relevant experience pool
- war state
- infrastructure and damage
- current Chaos tier
- repeated project use in the state
- exact cluster benefit

Rules:

- no more than four spendable types per action
- no hidden cost
- no negative stockpile
- no cost type the actor does not use
- small-country floor and large-country cap
- longer duration can preserve affordability
- political power is not the default universal price

Use the starting bands in the tuning matrix, then test against current economy values.

## Failure, cancellation, and refund model

Use one simple documented refund model.

- involuntary immediate invalidation can return a high partial share
- early failure can return a moderate unconsumed share
- middle or late failure returns little or nothing
- player cancellation returns less than involuntary failure at equal progress
- annexation returns nothing to a dead country
- state-transfer exploit returns nothing
- refund never exceeds paid cost

Do not expose a long component ledger. Tooltips should state the accepted public rule.

## AI implementation

Implement full posture, project-start, and target-selection logic from the scenario matrix.

Dominant cases need strong floors:

- capital emergency favors Integrate
- severe supply crisis favors Keep the Roads Open
- real high-fort offensive favors Study the Breach

Invalid choices need exact zero probability.

AI can skip a project when:

- no valid target
- no physical or target-bound result
- reserve floor fails
- civilian commitment is unsafe
- target likely falls before completion
- an Event 064 project is already active
- another critical system owns the same scarce resources
- owner contract does not support the action

Target priority begins with capital survival, active hostile front, major supply route, major victory point or industry, important port or air defense, and real fortified offensive target.

## Mandatory decision audit

Spawn `chaosx_decision_mission_auditor` with `fork_context=false` after the system is substantially implemented. Pass all Event 064 decision, mission, modifier, localisation, AI, and cleanup files. Resolve its findings before completion.

The audit must inspect:

- choice quality
- public clarity
- cost meaning
- action count
- mission duration
- target selection
- AI use
- cleanup
- save-load
- exploits
- asset coverage

## Mandatory probability audit

Spawn `chaosx_ai_probability_auditor` with `fork_context=false` and use every scenario in `matrices/ai_probability_scenario_matrix.md`.

Use configured probability inspection, evaluation, sweep, comparison, rendering, simulation, and sequence tools when available. Save normalized posture probabilities, project start results, target pool evidence, and cluster arbitration evidence.

Source inspection alone does not close the probability requirement.

## Localisation and assets

Write final category, posture, decision, mission, target, completion, failure, cancellation, and invalidation text from the spec directions.

Wire:

- category picture
- category icon
- three posture icons
- five decision icons

Do not use generic placeholder icons as final completion.

## Required tests

Prove at minimum:

- each posture appears only when valid
- old posture is removed
- active project cap
- every project starts, persists, completes once, fails, cancels, and cleans up
- save and reload during each project
- target control change during each project
- annexation cleanup
- response expiry before and during active project
- new Event 064 wave during active project
- tiny-country cost floor
- major-country cost cap
- train, truck, convoy, fuel, equipment, and manpower reserve floors
- AI emergency defense
- AI supply crisis
- AI high-fort offensive
- island behavior
- subject and civil-war behavior
- special actor behavior
- cluster cost benefit
- invalid target exact zero probability

## Completion rule

Do not claim the Event 064 response system complete until every mapped posture, decision, mission, target, cost, AI route, probability scenario, localisation key, icon, save-load case, cleanup path, and exploit control is implemented and evidenced. Report every simplification, fallback, unavailable hook, skipped tool, and blocker directly.
