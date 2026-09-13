# Event 60 decision and mission implementation prompt

Implement the Research Reconstruction decision system from the full Event 60 specification pack.
Read `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, the current cost helpers, current decision precedents, and all Event 60 spec and matrix files before editing.
Use the least complex presentation accepted by the pack: one ordinary decision category with a static category picture and compact dynamic status text.
Do not create a dedicated scripted GUI.

## Public state

Show two persistent public values only:

- Scientific Capacity
- Archive Recovery

Also show operational research slots compared with the incident ceiling, current major project, current phase, and selected rediscovery domain as concise state labels.
Do not turn those labels into additional custom meters.
Every value tooltip must explain what changes it, the next relevant threshold, its consequence, and the available response in two to four short lines where possible.

## Phase structure

Implement four lifecycle phases:

1. Emergency triage
2. National reconstruction
3. Institutional settlement
4. Residual lost knowledge

A phase should normally expose three to five primary actions and one to three active missions.
Hide obsolete actions when the phase changes.
Keep AI visibility and action access valid without requiring a human target selector.

## Required action families

Implement the applicable actions from the decision map:

- secure surviving laboratories
- recover records and instruments
- protect and recall specialists
- establish emergency standards
- open a foreign archive channel
- reopen research institutes
- rebuild universities and technical schools
- restore the national standards network
- reconstruct the central archive
- recall the scientific diaspora
- train replacement cohorts
- prioritize a lost domain
- commission foreign reconstruction
- select or change a residual rediscovery priority under strict cooldown and cap rules

Implement the Stabilize the Scientific Network mission and the institute, university, standards, archive, and foreign commission project mission patterns.
Each mission needs success, partial success where useful, failure, cancellation, target invalidation, and cleanup.

## Institutional settlements

Implement the mutually exclusive International Recovery Consortium, Central Scientific Authority, and Independent Academy Compact when their requirements remain valid.
The Emergency Kruger Mandate uses its own Event 16-controlled settlement path and does not appear as a generic fourth choice.
Each settlement must alter later costs, foreign access, specialist behavior, archive quality, institutional resilience, AI, and at least one persistent idea lifecycle.

## Costs and objectives

Use dynamic costs based on country scale, severity, war, occupation, infrastructure damage, route, repeated use, and restored institutions.
An action may consume at most four distinct spendable cost types.
Use equipment, fuel, trains, convoys, civilian factory commitment, manpower, political power, command power, stability, war support, or intelligence exposure only where the action supports that cost.
Use the shared stockpile debit helpers where suitable.
Every displayed cost requires its matching texticon.

Projects must ask the country to commit resources or complete an objective over time.
Avoid passive checklist missions and tiny stat rewards.
Slot restoration must consume one exact owed-slot receipt.
Technology recovery actions may give bounded research support or close one explicitly authorized node, never a hidden full-tree refund.

## AI and probability

Implement AI-equivalent behavior for every usable action.
Use the named scenarios in the AI probability matrix as the balance contract.
Run the required baseline audit, owner patch, and `hoi4.probability_compare` cycle for every weighted action, route, mission, partner, incident, and domain choice.
AI must always retain at least one affordable useful recovery path and must not bankrupt itself during war.

## Handoff

Report categories, decisions, missions, scripted helpers, constants, localisation keys, cost formulas, AI surfaces, cleanup call sites, asset sprites, probability evidence, acceptance scenarios, and every blocked or simplified item.
