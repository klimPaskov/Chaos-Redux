# Decision and Mission Implementation Prompt: Event 039 Murder Mystery

Implement the complete Event 39 decision and mission system from Parts 2, 5, 7, 8, 10, 12, and 13 of the accepted specification package.

## Required reading

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, the Event 39 source package, existing Chaos Redux investigation, crisis, target-selector, scenario, and faction decision precedents, relevant offline Paradox wiki pages, vanilla decision files, and vanilla documentation.

Use `chaosx_decision_mission_auditor` after implementation and `chaosx_ai_probability_auditor` for every complex weight. The parent agent owns integration and review.

## Presentation contract

Use ordinary decision categories with category pictures and compact scripted status text. Do not build a separate scripted GUI.

Implement:

- Murder Mystery Investigation for the original host
- Foreign Cell Investigation for secondary countries
- Brotherhood Operations for the central Assassin State
- Cell Administration for foreign derivatives
- World Without Leaders after terminal readiness

Ordinary governments display Case Progress and Network Reach. Assassin actors display Network Reach and Brotherhood Cohesion. Do not add more persistent player-managed Event 39 values.

Each phase normally exposes three to five primary actions, with six as the hard maximum. Each country normally has one to three active missions. Obsolete or invalid actions disappear.

## Investigation loop

Implement succession security, evidence preservation, investigative method selection, office-group protection, intelligence or case-team commitment, route tracing, witness transfer, cell raids, target missions, and final capture plans.

Methods need distinct costs, adaptation, capabilities, and outcomes. Repeating one method becomes less effective in a visible way. Good preparation must matter. Do not use opaque random failure to erase a strong case.

The final capture routes are silent arrest, coordinated raids, baited target, and foreign interception. Each must require its public preparation state and have distinct success, partial success, escape, and failure outcomes.

## International network

Implement local Case Progress, evidence sharing, route interdiction, local target protection, cell dismantling, support to threatened countries, immunity, and bounded reseeding. Secondary investigations begin easier than the original case.

Stage 4 cells need visible counterinsurgency missions and map-based revolt preparation. A foreign revolt decision is unavailable until the dynamic state-cluster preflight, carrier capacity, movement support, and parent-remnant checks pass.

## Assassin decisions

Implement route-aware Cohesion actions, selected foreign-cell target management, supply, operations, territorial revolt preparation, elite-unit commitment, derivative reinforcement, subject handling, and unauthorized-cell discipline.

Supporting foreign cells must cost equipment, transport, intelligence capacity, units, production, or Cohesion consequences. Do not create free global cell growth.

## Terminal decisions

Implement terminal command settlement, activation confirmation, bounded campaign-sector selection, synchronized uprisings, command-spine operations, successor administration, and campaign-council renewal.

World of Anarchy activation must call the shared terminal transaction and cannot serve as a free rescue for a collapsing movement.

## Missions

Use real objectives such as named state control, supplied divisions, rail and port control, evidence transport, protection windows, agency operations, revolt prevention, capital survival, foreign-cell supply, or terminal sector mandates.

Normal investigation missions generally last 90 to 180 days. Revolt and counterinsurgency missions generally last 120 to 240 days. Terminal mandates can last 180 to 365 days. Adjust dynamically for distance, agency, war, supply, and scale.

Every mission needs success, partial success when appropriate, and failure. Failure creates pressure, not merely absence of reward.

## Costs

No action may use more than four spendable cost types. Use icon-first cost localisation. Separate nonconsumed requirements from costs.

Use civilian factories, equipment, trucks, trains, convoys, fuel, manpower commitment, command power within the project cap, service experience, operative or agency capacity, unit commitment, stability, war support, and political power only where the action fits.

Do not create a political-power shop or tiny modifier rewards. Important actions must alter public values, missions, map control, protection, cells, units, institutions, subjects, or route access.

## Target selection

Use the reusable selected-target pattern for countries, cells, subjects, office groups, and sectors. Human players see one selected target's decisions. AI evaluates all valid targets. Clear stored IDs, flags, event targets, and active decisions when the target becomes invalid.

## AI and probability

Gate invalid actions before weighting. AI must consider route, capability, cost, war, supply, mission load, agency, stockpile, target safety, derivative capacity, and expected result.

Run the named probability scenarios in Part 13. Use the mandatory MCP probability route and record inputs, result, expected ordering, anomalies, and changes.

## Integration and cleanup

Focuses must unlock, replace, or change decision families. Decisions must call shared Event 39 helpers for investigation, character safety, cells, country creation, units, subjects, Chaos, and terminal state.

All categories, missions, commitments, targets, costs, and flags must survive save and reload and clear on capture, local dismantling, host loss, country defeat, inheritance, scenario rollback, terminal victory, or terminal defeat.

## Validation

Audit objective quality, cost and texticon correctness, visible action count, duplicate missions, route integration, AI, exploit loops, target cleanup, phase replacement, localisation, and impact. Missing blocked text, generic state requirements, passive checklist missions, stale targets, and actions with no real consequence are blockers.
