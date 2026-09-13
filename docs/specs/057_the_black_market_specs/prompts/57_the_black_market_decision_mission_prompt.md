# Event 57 Decision and Mission Implementation Prompt

Implement the member and outsider decision systems from:

- `docs/specs/057_the_black_market_specs/02_membership_secrecy_and_government_postures.md`
- `docs/specs/057_the_black_market_specs/03_smuggling_routes_and_network_growth.md`
- `docs/specs/057_the_black_market_specs/05_decisions_missions_and_player_loop.md`
- `docs/specs/057_the_black_market_specs/07_ai_probability_balance_and_edge_cases.md`

Follow the current repository versions of `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, and the current vanilla decision documentation and precedents.


Spawn every project subagent with a complete self-contained prompt and `fork_context=false`.

## Presentation

Use one hidden member-only decision category with an evolution-dependent static category picture.

Show exactly three persistent custom values:

- Market Credit
- Exposure
- Network Reach

Show current posture and route status as qualitative state, not additional meters.

A normal phase exposes three to five primary actions. Six is the hard maximum. Keep visible active missions between one and three.

Use a selected-offer show and hide flow when the inventory cannot fit the action budget. AI must evaluate all valid offers without using the player selector.

Outsiders receive a separate temporary targeted counter-smuggling category only after a valid evidence receipt. Do not reveal a global membership list.

## Member action families

Implement the complete accepted families:

- acquire current lot
- list verified surplus
- commission a broad offer class after Evolution I
- open, repair, shift, or burn a route
- choose or change government posture
- underwrite limited Market Credit
- compartmentalize contacts and manage Exposure
- contribute or buy intelligence packages
- Grand Auction bidding after Evolution III
- dormant, suspended, withdrawal, expulsion, and reconnection actions

Use working labels only as design identifiers. Write final player-facing text during implementation.

## Missions

Implement route and delivery objectives that use real state, port, railway, convoy, fuel, airbase, unit-presence, and intelligence conditions where applicable.

Every dispatched purchase starts one visible delivery mission. It auto-completes when the transaction settles. A delayed delivery can create one bounded crisis mission, then must resolve.

Route-opening and repair objectives need enough time for the player and AI to act. Use the dynamic bands in the source specs. Avoid passive stockpile-check missions and second confirmation clicks after the objective is already complete.

## Costs

Use concrete costs that match the action:

- Market Credit
- convoys
- trains
- trucks
- fuel
- equipment
- civilian factory burden
- relevant XP
- conservative command power
- political power only for genuine government or diplomatic action

A single action may use no more than four spendable cost types. Every visible cost needs the matching texticon. Exposure is a consequence, not a spendable cost.

## Transaction safety

Every decision must call the Event 57 validation and receipt helpers. Do not place source debit, buyer grant, credit movement, route selection, and settlement as unrelated inline effects.

Prevent:

- double clicks
- stale selected offers
- duplicate source debit
- duplicate delivery
- repeated founding credit
- recent-import resale
- self-purchase
- route reward farming
- offer reroll by reopening the category
- auction bid duplication

## Postures

Implement:

- Compartmentalized Tolerance
- State Patronage
- Counterintelligence Penetration
- Suppression Campaign

Posture changes need a cooldown, valid political or security basis, and full category replacement. Switching posture cannot reset Exposure or grant another access package.

## Outsider counterplay

Implement evidence-gated actions for:

- inspect suspicious cargo
- watch a route or depot
- pressure a proven intermediary
- turn a broker
- coordinate a seizure
- dismantle a local cell

Each action targets one proven route, intermediary, delivery, or member. Failure can expose the investigation or close the case. Regional success must not destroy unrelated cells.

## AI

Every action needs AI validity and strategic weighting. Use BM-P01 through BM-P10. A patch to any weight requires the audit, patch, and compare cycle with `chaosx_ai_probability_auditor`.

## Cleanup

Remove or replace actions when:

- offers expire or settle
- selected targets become invalid
- routes change
- membership state changes
- posture changes
- deliveries settle
- investigations close
- countries disappear
- the network becomes dormant or dismantled

## Audit

After implementation, route the complete category to `chaosx_decision_mission_auditor`. It may patch bounded local issues and must write a handoff under `docs/plans/057_the_black_market_plans/subagent_handoffs/`.

Do not claim the decision layer complete while it exceeds the action budget, uses placeholder text, lacks AI, exposes raw triggers, leaves stale targets, or permits a repeatable reward loop.
