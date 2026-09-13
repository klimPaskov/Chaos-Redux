# Event 050 decision and mission prompt

Audit and implement the decision surface for Event 050, The Great Embargo.

Read the complete Event 50 source package, `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, current vanilla decision documentation, the offline wiki pages required by the decision skill, and existing Chaos Redux selected-target precedents.

## Accepted presentation

Use one ordinary decision category with a static category picture. Do not create a dedicated scripted GUI.

Show Embargo Pressure, its stage, trend, and one urgent exposure summary. Keep all other calculations hidden or qualitative.

Expose three to five primary actions per phase and no more than one active timed objective. Replace obsolete or weaker actions as the crisis changes. Use a selected-target pattern for coalition members and neutral intermediaries so the human player does not see every possible country row.

## Required response families

Implement and audit:

- Self-Sufficiency
- Smuggling Networks
- Neutral Intermediaries
- Diplomatic Concessions
- Defy the World
- Resource Seizure
- Secure Replacement Supply mission

These are working design labels. Final localisation must follow the text-direction file.

## Action quality

Every action must have a concrete purpose, target, cost, timing, risk, success state, partial success where relevant, failure state, AI use, and cleanup.

No action may use more than four spendable cost types. Use political power only for genuinely political or administrative work. Prefer construction capacity, civilian burden, equipment, trains, trucks, convoys, fuel, stability, war support, access, concessions, and unit commitments where they fit.

Use exact named regions, resources, ports, routes, and staging states in requirements. Hide raw triggers behind concise custom tooltips.

## Mission quality

The replacement-supply mission must auto-complete from real response proof. Give enough time for the target to act, normally around 150 days with dynamic adjustment. Implement distinct full success, partial success, and failure.

Resource Seizure uses a separate 120 to 180 day preparation mission. Require real force, fuel, supply, equipment, and geographic preparation. It cannot give free cores or a war against an invalid or suicidal target.

## Clutter and lifecycle

- Opening actions hide after their setup is complete.
- Failed or invalid intermediary targets disappear.
- Completed projects become status or upgrade actions.
- Resolution hides ordinary responses.
- Every selected target, active decision, mission, cooldown, and temporary cost state clears.
- A later firing starts fresh decision state.
- Evolution II keeps each target category and selected-country state isolated.

## AI and probability

Do not patch weighted AI logic without the required baseline probability audit. After the owner patch, require comparison against the same named scenarios.

AI must preserve minimum survival stockpiles, refuse invalid routes, and select responses according to dependence, Pressure, military strength, ideology, stability, war state, route capacity, and settlement cost.

## Audit output

List affected category IDs, decisions, missions, selected-target helpers, scripted localisation, AI weights, and cleanup hooks. Identify any passive objective, repeated reward, tiny effect, fifth hidden cost, invalid target, stale decision, or exploit. Patch only bounded local issues. Broad design changes return as a plan for parent review.
