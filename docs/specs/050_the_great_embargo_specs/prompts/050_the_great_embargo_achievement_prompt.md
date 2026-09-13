# Event 050 achievement prompt

Implement and audit the five Event 50 achievements defined in the achievement matrix and Part 8 of the source spec.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, current achievement precedents, and every Event 50 crisis and cleanup contract.

The listed achievement names are working labels. Write final titles and descriptions during localisation work without revealing hidden evolution behavior in ordinary event text.

## Required achievements

- break a severe coalition as an initially import-dependent target without major concessions or Resource Seizure
- cause three important participants to leave without war against them
- remain at Pressure 80 or higher for 365 days and survive through domestic adaptation
- cooperate with two other targets under Evolution II and resolve all connected crises
- act as a neutral intermediary under Evolution I, resist secondary sanctions, and remain outside the coalition

## Tracking quality

Use crisis sequence identity for all crisis-scoped counters. Do not accumulate severe days, member exits, routes, or disqualifiers across unrelated repeat firings.

Count practical core or high-value participants where the design requires them. Do not count minor background members, duplicate exits, or countries removed through annexation.

Track every disqualifier explicitly. Cleanup must commit the final achievement result before clearing transient crisis values.

## Full surface

Implement:

- achievement registry entries
- tracking flags and variables
- unlock triggers
- disqualifiers
- event and decision hooks
- documentation
- final localisation
- one unique completed `64x64` icon per achievement
- grey and not-eligible variants

Do not grant an achievement for selection, passive waiting without its required proof, force-trigger setup, or flavor-only cooperation.

## Audit output

List achievement IDs, tracking state, source hooks, cleanup order, disqualifiers, icon paths, localisation keys, and task-specific validation. Flag any cross-crisis leakage, duplicate counting, hidden automatic unlock, or missing asset.
