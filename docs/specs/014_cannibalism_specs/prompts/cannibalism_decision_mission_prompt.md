# Event 014 Cannibalism Decision and Mission Implementation Prompt

Read:

- `AGENTS.md`
- `chaos-redux-decisions-missions`
- `chaos-redux-events`
- Event 14 Parts 1, 2, 3, 6, 7, 8, and 9
- `matrices/decision_mission_matrix.md`

Implement the complete phased decision system.

## Ordinary-country phases

1. Field breakdown with Field Hunger and Command Integrity.
2. Ritual cells with Cult Cohesion.
3. Organized network with Network Reach and node targeting.
4. Military counterwar against communes and warlords.
5. Revealed counterwar against Hannibal and the Wendigo transformation.

The category must evolve rather than show every action at once. Use active mission caps, selected targets, route locks, emergency visibility, and cleanup.

## Required ordinary families

- supply restoration
- overseas convoy and evacuation
- formation rotation and screening
- officer replacement
- burial and medical protection
- forensic investigation
- witness protection
- tribunals, amnesty, and disbandment
- cell infiltration and ritual-economy disruption
- prisoner and port protection
- island reconnaissance and blockade
- joint multi-country suppression
- commune and feeding-state liberation
- convergence disruption
- Hannibal network counterwar
- Wendigo anchor assault and countdown delay
- state recovery and burial

## Exploitation route

Implement terror battalions, prisoner feeding, compromised-unit deployment, concealed losses, and occupation terror as powerful short-term actions with severe long-term Cult Cohesion, Command Integrity, condemnation, network, warlord, and achievement consequences. AI may use the route only under explicit desperation and ideological conditions.

## Cannibal-country families

- controlled-state consumption
- Larder transfer and protection
- Scavenger Warband, Feast Cohort, Bone Guard, origin specialist, and Network Cadre recruitment
- depot, prison, convoy, relief-route, and battlefield raids
- hunting-ground, feeding-state, and Silent Larder progression
- foreign formation seeding
- courier and synchronized-offensive actions
- warlord tribute, submission, manipulation, challenge, and betrayal

## Hannibal families

- absorb, appoint, chain, or purge warlords
- centralize Larder
- create legions
- launch continental campaigns
- seed major enemy forces
- designate feeding capitals
- destroy coalition hubs
- begin ordinary terminal mobilization

## Wendigo families

- preserve and train existing Wendigo units
- train new transformed units
- strengthen anchors
- accelerate transformation
- freeze enemy supply routes
- consume anchor population
- launch terminal progression

## Mission quality

Every timed mission needs:

- owner
- target country or state
- named objective
- duration based on difficulty
- success
- failure
- partial success where useful
- duplicate-risk review
- AI behavior
- cleanup

Do not use passive stockpile checklists. Missions should require route control, supplied units, convoy access, state capture, prison protection, or simultaneous node destruction.

## Costs

Use equipment, manpower, army experience, trains, trucks, convoys, fuel, civilian factories, tied divisions, supply, intelligence exposure, local support, Larder, population, state control, and time. Political or command power can support a cost, but cannot be the default complete cost.

## GUI

Wire the attached category header, Evolution II network window, cannibal command window, revealed Hannibal window, and Wendigo transformation window. Every button must call the same validated scripted effect and cost logic as the decision system. Provide AI equivalents.

## Cleanup and validation

- remove dead and annexed targets
- cancel obsolete missions
- clear temporary flags, variables, and global targets
- prevent consumption and recruitment duplication
- prevent free-unit and Larder farming loops
- close categories after local or global victory
- remove pre-reveal uncertainty UI after reveal
- block terminal actions below chaos 1000

Spawn `chaosx_decision_mission_auditor` with `fork_context=false` after implementation. Resolve every task-specific finding before completion.
