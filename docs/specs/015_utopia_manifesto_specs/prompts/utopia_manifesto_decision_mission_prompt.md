# Decision and mission implementation prompt for Event 015, `utopia_manifesto`

Use with `hoi4-decisions-missions`, `chaos-redux-events`, `hoi4-focus-trees`, `chaos-redux-subagents`, and the event specs.

## Primary files to read first

- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_1_core.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_2_focus_tree.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_3_decisions_mechanics.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_4_ai_assets_acceptance.md`

## Required decision families

Implement the Utopian Ledger category and staged decision families:

- household census and public reading
- common stores and audits
- vocation petitions, apprenticeships, urgent service, and second trade
- rural rotation and harvest missions
- just-war review and defensive household guard
- needful land arbitration and settlement charters
- occupation and integration projects
- friends, neighbors, aid, and magistrates
- Utopian League actions
- Marked Bounds crisis actions and reform exit

## Core mechanic values

The category must show and update:

- Need
- Consent
- Surplus
- Overreach
- Vocation Balance
- Foreign Suspicion

Use script constants for thresholds, duration bands, AI weights, caps, costs, and route modifiers. Use scripted localisation for values and status bands. Values should affect focus availability, decision visibility, integration, claims, AI, and late routes.

## Cost model

Do not make the system a political power store. Use concrete costs and requirements:

- civilian factory burden
- support equipment
- infantry equipment
- trains
- trucks
- convoys
- manpower
- army XP
- stability
- war support
- local support or compliance
- resistance thresholds
- supply route, port, rail, or state control
- divisions placed in named states for missions
- Surplus, Consent, Need, and Overreach values

Command power must stay conservative and never exceed 60 for a decision.

## Mission design

Timed missions need real objectives and varied durations:

- Harvest Rotation: 90 to 140 days
- Storehouse Build: 120 to 180 days
- Household Guard or shore defense: 90 to 180 days
- Boundary Arbitration: 120 to 180 days
- Local Households integration: 150 to 220 days
- League Aid Corridor: 120 to 180 days
- Renunciation Vote: 120 days

Use success, failure, and partial success. Failure must do something visible.

## Target and clutter control

Humans should not see every possible country or state target at once. Use selected-target flow or staged visibility. AI may evaluate all valid targets through AI-only decisions or helper effects.

Clean up stale targets when:

- target country dies
- target state is lost
- war ends
- route changes
- target joins League
- country is annexed or puppet state changes

## AI behavior

AI must use the decisions without the scripted GUI. Respect target safety:

- no ordinary claims against majors
- no claims against much stronger countries
- no dead countries
- no invalid states
- no League actions with invalid members
- no repeated forced settlement when Overreach is already catastrophic unless hardline route is active

## Localisation

Use clear custom trigger tooltips. Do not expose raw trigger blocks. Cost text should be icon-first where possible. Use dynamic placeholders for target state, country, Need band, route, and missing resources.

## Audit requirement

After implementation, spawn or run `chaosx_decision_mission_auditor` for this event. It should audit objective quality, costs, tooltips, AI validity, cleanup, route integration, exploit risk, and localisation.

