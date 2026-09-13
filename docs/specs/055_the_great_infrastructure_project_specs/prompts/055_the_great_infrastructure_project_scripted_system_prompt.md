# Scripted System Architecture Prompt for Event 55

Design and implement the reusable Event 55 project runtime without moving event-owned lifecycle logic into shared registries.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, the dynamic effect and trigger registries, the Event 55 specs, and the relevant offline wiki and vanilla documentation.

Use `chaosx_scripted_system_architect` for the bounded event-owned architecture and small implementation. The parent remains responsible for full event wiring and completion.

## Event-owned state

Provide stable persistent records for:

- first-time recipient and opening-grant proof
- recent target cooldown
- proposal generation and stored proposal slots
- active project generation
- primary family and secondary components
- origin, destination, route states, and critical nodes
- crossing token when relevant
- partner roles, invitations, receipts, contribution shares, and agreement state
- construction method
- stage and active mission
- full or reduced scope
- operational status
- completion, damage, repair, reroute, transfer, and abandonment history
- achievement facts
- one-time cooperation Chaos guard

Long-lived records must not rely only on temporary event targets.

## Required event-owned APIs

Plan concise event-owned scripted triggers and effects for:

- target validity
- proposal family validity
- route and node validity
- crossing registry validity
- National Works Capacity calculation
- proposal generation and replacement
- project authorization
- stage transition
- partner invitation and receipt handling
- construction progress adjustment
- project completion
- status refresh
- repair, reroute, renegotiation, transfer, and abandonment
- idempotent cleanup
- save reload category rebuild
- Event 18 resource adapter
- Famine and Migration route publication
- Embargo and disaster fact consumption

Use generation identities and fail-closed proof for every cross-country or delayed response.

## Performance

Use a sparse Event 55 recipient registry and bounded project critical-node lists.

Do not add a whole-world daily, weekly, or monthly scan.

Prefer monthly processing only for registered recipients, event-driven updates for project stage and partner responses, and targeted refresh after state control, disaster, embargo, or annexation changes.

## Shared registry boundary

Use the shared `uses_normal_civilian_systems` and nonhuman classifiers for broad routing.

Do not add Event 55 stage, evolution, project, or category rules to the shared classifier registry.

Use existing neutral stockpile debit helpers where possible.

Add a new shared dynamic helper only if its contract is neutral and needed across unrelated systems. If one is added, document purpose, scope, inputs, outputs, defaults, side effects, and example in the same change.

## Tuning

Centralize thresholds, duration bands, slot rules, cooldowns, capacity contributions, costs, incident limits, AI weights, and status thresholds in Event 55 script constants or a clearly owned tuning file.

Do not scatter magic numbers.

## Safety

- Cleanup is idempotent.
- Late partner receipts cannot mutate a newer project.
- Transfer cannot duplicate benefits.
- Rerouting preserves identity and does not count as a new achievement project.
- Repeat firing cannot apply the opening grant twice.
- Invalid crossing entries fail closed.
- Shared system adapters do not read or write another system's primary ledger.

Write a handoff listing helpers, call sites, persistent variables or arrays, generation rules, cleanup paths, and unresolved engine constraints.
