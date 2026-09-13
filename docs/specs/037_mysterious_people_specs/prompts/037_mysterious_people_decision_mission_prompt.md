# Prompt: Event 037 decisions and missions

Implement and audit the Event 037 decision and mission system from Part 4 of the specification.

Read the complete Event 037 pack, `AGENTS.md`, the event skill, decisions and missions skill, current Famine and Migration decisions, Camp and Repression decisions, current category and selected-target precedents, offline wiki, installed vanilla documentation, and local Chaos Redux examples.

Use an ordinary decision category with a static category picture. Do not create a dedicated scripted GUI.

## Public category

Show:

- current living mysterious population in the country
- one Overpopulation Pressure value and stage
- pressure trend and next threshold
- active policy
- concise highest-priority state status
- selected-state summary
- one to three active missions
- three to five primary actions for the current phase

Keep detailed calculation inputs internal. Use concise tooltips with clear blocked reasons.

## Policies

Implement:

- Open Integration
- Managed Settlement
- Restricted Registration

Each policy needs distinct effects, AI, availability, transition cost or cooldown, dynamic text, and cleanup. Restricted Registration can create undercounting and hidden population, but the player must receive public signs of the mismatch.

## Selected-state pattern

Use the established selected-target workflow:

- priority list of valid Event 037 states
- one selected state for human actions
- clear action to close selection
- state flag or equivalent selected proof
- stored target identity
- helper triggers and cleanup
- AI access to every valid target without using the human selector

Priority uses pressure, Famine, trapped people, housing, transport, capitals, industry, and project impact. Invalid targets clear immediately.

## Decision families

Implement the mapped phase actions:

Baseline:

- establish population office
- registration drive
- employ new workforce

Evolution I:

- emergency housing
- water and transport
- clinics and schools
- planned settlement
- agricultural support through Famine

Evolution II:

- emergency food channels through Famine
- military logistics
- foreign relief
- redistribution through Migration
- emergency property requisition

Evolution III constructive:

- new cities
- national food expansion through Famine
- international settlement compact through Migration

Evolution III extreme:

- closed settlement zones
- forced relocation through Migration
- forced labor through Camp and Repression
- systematic killing through the existing atrocity route

Do not duplicate shared Famine, Migration, Camp, or Condemnation actions. Event 037 can open, request, target, or summarize the shared action while the owner retains costs, transaction, mortality, evidence, and result.

## Missions

Implement:

- Absorb the Newcomers, about `120` to `180` days
- Prevent Demographic Emergency, about `180` days
- Keep the Corridor Open, about `90` to `150` days
- Complete the New Settlement, about `120` to `240` days

Missions require active work. Goal-style missions auto-complete when their conditions are met. Success, partial success, and failure use distinct effects. Maintain the visible mission budget.

## Costs

One action can use no more than four spendable cost types. Every visible cost uses the matching texticon.

Scale costs by population affected, state damage, distance, route, destination capacity, war, industry, prior failure, evolution, and pressure.

Use varied resource families appropriate to the action. Do not make every action a political-power purchase. Command-power costs remain conservative. New cities and national programs must have a scale matching their names.

## AI and probability

Before changing any AI weight, target score, mission score, random pool, or decision priority, run `chaosx_ai_probability_auditor` with the named scenarios in the probability matrix.

After the owner applies a patch, rerun the same scenarios with mandatory probability comparison.

AI must understand high-capacity integration, planned development, wartime logistics, relief dependence, restrictive rule, donor behavior, reception capacity, and rare atrocity conditions.

Support actions must dominate viable ordinary cases. Invalid targets have zero participation.

## Lifecycle and cleanup

Handle:

- state control and ownership changes
- annexation and civil war
- route and border closure
- destination disappearance
- cohort exhaustion
- pressure-stage change
- policy change
- Famine or Migration request completion
- country becoming nonhuman
- category closure
- save and reload
- selected-target cleanup
- duplicate project prevention

## Localisation and presentation

Write final policy, category, decision, mission, cost, requirement, result, and tooltip text. Use dynamic state, country, population, pressure, route, and resource values.

Do not expose raw triggers, internal variables, implementation history, or hidden future outcomes. Do not use fake table text, repeated separator characters, or debug-style telemetry.

## Audit and handoff

After implementation, use `chaosx_decision_mission_auditor`. It may make bounded local fixes and must write a handoff listing changed files, identifiers, before and after behavior, meaningful validation, skipped evidence, and remaining issues.

Do not claim completion until category clarity, selected-state validity, mission quality, costs, AI, shared-system ownership, cleanup, exploit checks, localisation, and probability comparisons all pass.
