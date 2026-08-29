# Decision and mission implementation prompt for Event 028: Asteroid Incoming

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, the Event 028 specification pack, the tuning matrix, and the current vanilla and Chaos Redux decision precedents. Implement one event-owned recovery category with phased visibility. Do not create a dedicated scripted GUI. Use the static category picture from the asset package.

## Visible category state

Show only:

- Current global dust stage
- Current national dust-protection state
- National recovery burden when local impact damage exists
- Controlled crater count when Extraordinary Minerals is active

Keep raw formulas and per-state ledgers internal or in concise tooltips. A phase should show three to five primary actions and one to three active missions. Six visible primary actions is the hard ceiling.

## Pre-impact response

Implement the target-country emergency event with three stances.

- Preserve command continuity
- Disperse transport and stockpiles
- Prepare hospitals and shelters

The stances may change command disruption, mobile reserve survival, opening recovery burden, and continuing rescue deaths. They must not change the required immediate center or ring population percentages.

## Emergency actions

Implement exact-state versions of:

- Deploy mobile hospitals
- Open an emergency rail corridor
- Clear unstable debris
- Distribute emergency water and filters

Use real costs such as support equipment, trucks, trains, fuel, manpower, and civilian-factory commitment. Each action has at most four spendable cost types. Show matching texticons, exact target state, route requirements, and blocked reason.

## Emergency missions

Implement:

- Keep the rescue route open
- Stabilize the damaged zone

Use 120 to 180 day timing based on objective difficulty. The missions should auto-complete from actual supply, route, infrastructure, and state conditions. Success and failure need distinct effects and Deaths-safe handling.

## Reconstruction actions and missions

Implement:

- Rebuild a supply spine
- Restore outer-ring industry
- Rehouse displaced workers
- Reconnect the national network
- Restore the outer ring
- Rebuild the regional economy for the original target

These actions must perform real state and network work. Main crater buildings remain permanently ineligible. Restore only capacity lost through the Event 028 incident, within current engine limits. Avoid free factory, railway, and infrastructure farming.

## Dust actions

Implement:

- Harden factories against dust
- Protect transport and reserves
- Join the atmospheric observation network

Use staged national protection that replaces earlier forms. Global mitigation has diminishing returns and a monthly cap. One country cannot remove global dust instantly. Dust actions hide at zero load.

## Crater actions

Under Extraordinary Minerals, implement:

- Secure the crater perimeter
- Survey extraordinary material
- Fortify access routes
- Bounded rival reconnaissance and disruption where the country borders or fights the controller

Security requires actual supplied divisions and equipment. Survey reveals persistent site flavor and may give a bounded research or intelligence benefit. It must not create another armour stack. Fortification builds or repairs access states, not the permanent main crater.

## AI

Create an AI path for every meaningful action. Use reserve floors and validity gates.

Priority order:

1. Prevent continuing deaths.
2. Restore capital and frontline supply.
3. Reconnect high-population states.
4. Protect national production from dust.
5. Restore surviving industry.
6. Secure and defend crater sites.
7. Contribute to global mitigation when resources allow.

AI must not spend its last trains, support equipment, fuel, manpower, or construction capacity during an active existential war.

Any probability-bearing AI change requires the audit, patch, and comparison cycle through `chaosx_ai_probability_auditor` and the named scenarios in `028_asteroid_incoming_ai_probability_prompt.md`.

## Cleanup and exploits

- Hide obsolete phases and invalid targets.
- Clear selected state records when control changes or the state becomes invalid.
- Cancel or fail missions cleanly when required routes are lost.
- Prevent repeat rewards on one state.
- Prevent rebuilding above incident loss or current valid levels.
- Prevent main-crater reconstruction.
- Preserve recovery burden through annexation.
- Prevent crater security and survey farming through rapid control changes.
- Keep global mitigation inside country and world caps.

## Presentation and audit

Use the static Event 028 category picture and separate 32x32 icons from the asset prompt. Do not paint controls or dynamic values into the picture.

After implementation, spawn `chaosx_decision_mission_auditor` with `fork_context=false`. Require a handoff listing every decision and mission ID, target model, cost types, dynamic cost source, AI behavior, success and failure, cleanup, exploit protection, localisation keys, and meaningful validation. Broad design changes return as a plan instead of an unreviewed patch.
