# Decision and Mission Prompt: Event 021 Random Civil War

Implement the Event 021 decision and mission system from:

- `021_random_civil_war_spec_part_3_decisions_missions_and_outcomes.md`
- `021_random_civil_war_spec_part_4_evolution_i.md`
- `021_random_civil_war_spec_part_5_evolution_ii.md`
- `021_random_civil_war_spec_part_6_evolution_iii.md`
- `021_random_civil_war_spec_part_8_cluster_scenario_ai_balance.md`

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and current Chaos Redux decision precedents.

Use `chaosx_decision_mission_auditor` after implementation. Spawn it with `fork_context=false`.

## Presentation

Use a normal decision category.

The category contains:

- one static category picture
- one category icon
- concise dynamic text
- one visible State Authority value
- current phase
- current main pressure
- current selected or priority front when several fronts exist
- one to three active missions
- three to five primary actions in a normal phase
- no more than six primary actions in an emergency phase

Do not create:

- custom scripted GUI
- selected-front window
- animated seal
- animated category art
- plain ledger of several visible values
- fake buttons or meters painted into the category picture

Hidden Fracture Pressure remains implementation logic.

## State Authority

State Authority is the one main visible crisis value.

Working stages:

- Cohesive, 70 to 100
- Contested, 40 to 69
- Failing, 15 to 39
- Collapse, 0 to 14

Final thresholds belong in centralized tuning after probability and balance review.

The player must understand:

- why authority changed
- the next meaningful threshold
- what public action can change it
- which front or condition is causing the strongest pressure

## Cost rules

Every action represents a real public act.

Use concrete costs that fit the action:

- infantry or support equipment
- artillery
- trucks
- trains
- convoys
- fuel
- manpower
- army, navy, or air experience
- command power within the project cap
- stability
- war support
- civilian-factory commitment
- tied-down units
- local support
- diplomatic access
- intelligence exposure
- time

An action can have at most four spendable cost types.

Requirements do not count as costs.

Cost localisation must be icon-first and compact. Every displayed resource needs the correct texticon.

Avoid political power or command power as the only cost unless the action is truly political or command administrative work.

## Government action families

Implement the valid subset of:

- secure arsenals
- establish capital defense
- restore the rail spine
- conduct bounded loyalty review
- integrate loyal formations
- negotiate regional guarantee
- offer limited amnesty
- call emergency coalition
- emergency requisition
- prepare against a likely independence front
- negotiate autonomy
- rotate suspect commands
- restore local administration

Actions change authority, front strength, supply, command loyalty, settlement options, and later recurrence. They do not exist only to give small modifiers.

## Opposition action families

Implement the valid subset of:

- seize local depot
- organize regional recruitment
- integrate defecting officers
- establish field administration
- open foreign liaison
- request recognition
- coordinate with another opposition
- reject a rival claim
- secure a capital
- protect a port or corridor
- prepare a separate settlement

Event 006 actors keep their package decisions. Event 021 adds only civil-war emergency actions that do not erase package identity.

## Mission families

Use goal-style or timed missions for actions the player must perform on the map.

Expected families:

- hold capital
- secure rail junctions
- defend depot belt
- keep supply corridor open
- place supplied divisions in named states
- complete local mobilization
- deny enemy recognition
- fulfill ceasefire obligations
- disarm formations
- restore administration
- protect the settlement

Missions need varied durations, clear locations, success, failure, partial success when useful, AI, cleanup, and no second payment click after the objective is fulfilled.

## Evolution I

Support several registered fronts without showing every possible action at once.

Use:

- priority-front selection through ordinary decisions and dynamic text
- one category per playable country
- front-specific missions
- independent settlement
- separate cleanup
- rival-front cooperation or conflict

Defeating one side does not close the category while another Event 021 front remains.

## Evolution II

Neighbors receive a compact category only while an active or decaying reason exists.

Separate:

- civilian relief
- border control
- armed-network suppression
- government support
- opposition support
- mediation
- recognition
- foreign-intervention exposure

Displaced civilians are never treated as an armed enemy.

Military aid and relief use separate costs, consequences, and text.

Strange-incident countermeasures remain rare and appear only when an incident is active.

## Evolution III

Stable countries see a short status and at most one or two relevant prevention actions.

Exposed countries see actions tied to their strongest risk source.

Fractured countries receive the full prewar category.

Critical countries receive emergency missions while waiting for the bounded launch queue.

Do not turn Evolution III into permanent monthly busywork.

## Settlement and reconstruction

Implement:

- military government victory
- opposition victory
- recognized independence
- negotiated autonomy
- coalition settlement
- armistice
- temporary partition
- merger
- reconstruction
- renewed conflict

Settlements create obligations. The category changes phase after the war and closes only after obligations, reconstruction, recurrence memory, and all front records are resolved.

## AI and cleanup

Every meaningful human action needs an AI route.

AI evaluates:

- State Authority
- front strength
- capital and supply
- equipment and manpower
- ideology
- settlement quality
- sponsor dependence
- current wars
- route validity
- expected survival

Invalid actions receive zero weight.

Clean:

- active decisions
- missions
- selected fronts
- event targets
- sponsor routes
- aid corridors
- temporary modifiers
- actor references
- settlement obligations
- scenario bypass
- invalid country records

The decision system is incomplete while stale decisions, duplicate missions, free-unit loops, political-power stores, or hidden fifth costs remain.
