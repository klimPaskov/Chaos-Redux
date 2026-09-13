# Event 067 Generalissimo Decision and Mission Prompt

Implement and audit the complete Event `067` decision and mission system.

## Required sources

Read:

- `docs/specs/067_generalissimo_specs/specs/067_generalissimo_spec_part_2_character_and_influence.md`
- `docs/specs/067_generalissimo_specs/specs/067_generalissimo_spec_part_3_decisions_and_removal.md`
- `docs/specs/067_generalissimo_specs/specs/067_generalissimo_spec_part_4_revolt_and_country_package.md`
- `docs/specs/067_generalissimo_specs/specs/067_generalissimo_spec_part_6_scenario_and_world_end.md`
- `docs/specs/067_generalissimo_specs/handoffs/067_generalissimo_probability_scenario_matrix.md`
- `AGENTS.md`
- `chaos-redux-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-subagents`

Use `chaosx_decision_mission_auditor` after the main implementation. Route every weighted AI or chance surface through `chaosx_ai_probability_auditor` before and after patches.

## Category structure

Create an Event 067 crisis category for the active host.

The category must:

- expose Generalissimo Influence through the event-owned attached display
- show current command authority
- show no more than six primary actions
- normally show three to five actions
- show no more than three active missions
- hide before the event
- hide after removal or takeover
- replace obsolete decisions by phase
- close invalid targets and missions

Do not turn the category into a store of minor bonuses.

Create separate event-owned categories or phased decision families for:

- junta consolidation and force growth
- postwar integration
- world-end military governments
- world-end civilian governments

Use the fewest categories that keep the current state clear.

## Costs

Every action uses at most four spendable cost types.

Use action-appropriate costs from:

- command power, never above 60
- army experience
- political power for constitutional or administrative acts
- infantry equipment
- support equipment
- motorized equipment
- trains
- fuel
- manpower
- stability
- war support
- civilian or military factory commitment
- tied-down divisions through mission requirements

Player-facing cost strings use amount and texticon only. Requirements remain separate.

Scale important costs by army size, industry, war state, Influence, and prior use. Centralize tuning in script constants.

## Command decisions

Implement:

- expand to National Field Command
- grant Supreme Command
- return to Advisory Reserve

Each changes command authority, military effects, Influence, and future decision state. Add cooldowns and memory so authority cannot be cycled for bonuses.

## Concessions

Implement the full concession pool:

- public promotion
- authority over appointments
- military budget expansion
- protection for loyal officers
- operational planning authority
- transfer of armament boards
- internal security under army command
- emergency powers
- foreign-policy veto
- loyal officers in government

Each concession needs:

- valid target and institution checks
- real immediate benefit
- Influence and hidden-network consequence
- one-time or cooldown control
- AI logic
- final localisation direction from the spec

Demand selection shows one active demand at a time.

## Counterweights

Implement:

- rotate regional commands
- establish civilian military oversight
- remove loyal appointees
- create loyal reserve command
- disperse guard formations
- move the arsenals
- separate military intelligence

Every counterweight reduces a real coup component and imposes a real military, political, industrial, or logistics cost.

The loyal reserve and arsenal actions must use real equipment and manpower. Do not create free forces or duplicate stockpiles.

## Crisis missions

Implement:

- Hold the Command Centers
- Win the Campaign
- Secure the Civilian Chain of Command
- Build the Loyal Reserve

The final names are localisation work. The mechanics must follow the spec.

Mission rules:

- select named dynamic states or enemies
- avoid conditions already satisfied at launch
- use 120 to 270 day durations according to difficulty
- require unit placement, state control, equipment, war outcome, or active command action
- auto-complete when the objective is met
- use distinct success and failure effects
- update Influence, counterweights, prestige, or force shares
- clean up selected targets

## Removal decisions

Implement separate methods:

- negotiate retirement
- dismiss from command
- arrest at headquarters
- capture during inspection or transit
- assassination
- final removal during the ultimatum

Required behavior:

- retirement is safe only at low Influence
- ordinary dismissal failure before Evolution III does not revolt
- failed arrest causes immediate revolt
- failed capture causes immediate revolt
- failed assassination causes immediate revolt
- failed final removal causes immediate revolt
- successful removal ends the crisis permanently
- player sees failure consequence before confirmation
- exact chance or an honest bounded band is shown
- strongest positive and negative factors are explained
- one coercive attempt per crisis
- no save-state or cooldown path permits repeated chance farming

Use the chance model and scenario IDs in the probability matrix.

## Junta decisions

Implement resource-backed force and state actions:

- Officer Class Mobilization
- Requisition the Arsenals
- Regional Command Levies
- Integrate Defecting Formations
- Foreign Officer Missions
- Generalissimo Guard
- secure capital command
- officer reconciliation
- selective retirement
- broad purge
- restore supply command
- subject settlement
- faction settlement

These decisions must use the host's equipment, manpower, templates, territory, and command state. No custom unit family is required.

## Postwar integration

Phase the category so the player sees current reconstruction tasks.

Required families:

- reunify armed forces
- repair rail and supply networks
- reopen armament plants
- settle officers
- integrate government-held regions
- resolve subject loyalty
- resolve faction status
- proclaim permanent government

Successful integration removes temporary civil-war state. It does not grant instant full stability.

## World-end military decisions

Implement:

- support an officer coup
- send a general staff mission
- guarantee a military government
- coordinate military production
- pressure a neutral junta
- remove a rival military leader through a valid owner path
- establish a client junta

Require target validity, distance, access, resources, cooldown, failure, and AI logic.

## World-end civilian decisions

Implement:

- secure capital command
- recall arsenals
- form loyal officer council
- support legal government
- coordinate anti-coup intelligence
- restore civilian authority

These decisions consume equipment, command resources, intelligence, political authority, or unit commitments. They cannot be free anti-coup buttons.

## Clutter control

- No more than six primary actions per phase.
- Replace early actions with stronger later forms.
- Hide invalid targets.
- Use selected-target flow for foreign coup and support actions when many targets exist.
- AI can evaluate all valid targets without requiring the player selector.
- Remove decisions after target death, annexation, government change, war resolution, or world-end role change.

## AI

AI must consider:

- war state and direction
- Influence
- command authority
- displayed removal chance
- loyal reserve
- equipment
- capital security
- faction support
- government type
- Generalissimo military value
- Cohesion after takeover
- route and world-end role

Do not let AI choose an action it cannot pay for or an operation with an invalid target.

## Probability evidence

Audit:

- demand weights
- AI concessions
- AI counterweights
- removal chances
- final ultimatum choices
- foreign coup targets
- bloc support targets

Use the exact scenario IDs from the matrix. Apply no weighted patch without a post-change `hoi4.probability_compare` result.

## Completion handoff

The decision auditor must write a handoff under:

```text
docs/plans/067_generalissimo_plans/subagent_handoffs/
```

Include:

- files changed
- category and decision IDs
- missions
- cost models
- AI surfaces
- probability evidence
- cleanup
- exploit checks
- unresolved design gaps

Do not claim completion while any mapped decision or mission is missing, passive, duplicated, unlocalized, unaudited, or unsupported by AI.
