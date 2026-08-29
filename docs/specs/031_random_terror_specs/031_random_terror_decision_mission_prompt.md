# Event 31 Random Terror decision and mission implementation prompt

## Task

Implement the complete Event 31 government-response and territorial-actor decision systems.

The source specification is:

`docs/specs/031_random_terror_specs/`

Required source files:

- `031_random_terror_spec_part_1_event_identity_and_player_loop.md`
- `031_random_terror_spec_part_2_targeting_and_incident_engine.md`
- `031_random_terror_spec_part_3_government_response_decisions_and_missions.md`
- `031_random_terror_spec_part_4_evolutions_and_escalation.md`
- `031_random_terror_spec_part_5_territorial_insurgency_and_country_packages.md`
- `031_random_terror_spec_part_7_global_jihad_scenario.md`
- `031_random_terror_spec_part_8_false_revelation_world_end.md`
- `031_random_terror_spec_part_9_ai_balance_probability.md`
- `031_random_terror_decision_mission_matrix.md`
- `031_random_terror_ai_scenario_matrix.md`

Follow:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-subagents`
- `chaos-redux-event-assets` for the category pictures and icons

Read the required offline wiki decision, trigger, effect, localisation, modifier, scope, and data-structure pages.

Read current vanilla decision documentation and relevant vanilla decision and mission examples.

Inspect existing Chaos Redux categories that use targeted states, active mission caps, dynamic category text, map modes, selected targets, and concrete equipment costs.

## Accepted presentation

Do not create a permanent dedicated scripted GUI.

The accepted government presentation is:

- one ordinary decision category
- one static government-response category picture
- concise dynamic category text
- Terror Pressure as the primary value
- Response Legitimacy as the supporting value
- exact active-state list
- one next important threshold or mission
- three to five visible primary actions
- six as the hard maximum
- no more than three active missions
- an event-owned state map mode or state highlight

The accepted territorial-actor presentation is:

- one ordinary actor decision category
- one static actor-command category picture
- Territorial Control
- Network Authority
- External Supply
- phase and route filtered actions
- no more than six visible primary actions
- no more than three active missions

The final-state category uses the accepted terminal category picture and the same clarity limits.

Do not replace this design with a full window, tabbed panel, large value board, or fake category picture containing controls.

## Values

Implement visible bounded values with centralized tuning.

### Government

- Terror Pressure, `0` to `100`
- Response Legitimacy, `0` to `100`

### State

- activity stage `0` Clear
- stage `1` Dormant
- stage `2` Active
- stage `3` Entrenched
- stage `4` Armed Insurgency
- stage `5` Lost Local Control

### Later global values

- Network Reach after Evolution II
- International Unity after Evolution IV

### Territorial actor

- Territorial Control
- Network Authority
- External Supply

### Hidden

- Apocalyptic Readiness

Show only values that matter to the current player and stage.

Do not expose internal scoring components or hidden world-end readiness.

Each visible value needs a concise tooltip that states what it means, what changes it, why the current stage matters, and which action can respond.

## Category phases

Implement four government phases.

1. Immediate shock
2. Active network
3. Territorial challenge
4. Recovery

Visible actions should be replaced by phase.

Do not leave early and late variants visible together.

Targeted decision families should use one selected state, corridor, sponsor, or actor at a time where this keeps the category compact.

AI must still evaluate every valid target without using the human selector flow.

## Government decisions

Implement every accepted matrix row or document any necessary merge before coding.

Core families:

- Establish Joint Response Cell
- Protect Critical Transport
- Support Victims and Restore Services
- Targeted Intelligence Sweep
- Immediate Security Surge
- Conduct Targeted Raid
- Disrupt Finance and Smuggling
- Request Allied Intelligence
- Offer Defection and Amnesty Channel
- Temporary Movement Restrictions
- Protect Community and Religious Sites
- Expose the Sponsor
- Quiet Sponsor Leverage
- Military Reinforcement
- Emergency Capital Security
- Isolate the Enclave
- Secure Relief Corridor
- Prepare and conduct a state-retaking operation
- Negotiate Local Surrender
- Request Foreign Intervention
- Restore Services
- Public Accounting
- Security Reform

Each action needs:

- phase
- visibility
- availability
- exact target
- cost
- blocked tooltip
- public result
- failure or tradeoff
- AI
- cooldown or one-shot state
- cancellation behavior
- invalid-target cleanup
- event and value hooks
- asset and localisation key

## Territorial-actor decisions

Implement every accepted actor matrix row needed by the final focus and country package.

Core families:

- Raise Local Militia
- Integrate Defectors
- Repair Captured Depot
- Open External Corridor
- Seek Sponsor
- Support Foreign Cell
- Relocate Network
- Convert Militia
- Ideological Mobilization
- Absorb Actor
- Contest Network Leader
- Prepare State Offensive
- Build Civil Administration
- Force Extraction
- Recruit Foreign Fighters
- Join or contest the Jihadist International
- Call Coordinated Uprising
- Accelerate the Revelation without bypassing hard gates

These decisions must use actual actor resources, population, equipment, territory, route, evolution, sponsor, and target state.

Do not create free units, equipment, corridors, cells, or uprisings.

## Missions

Implement the accepted mission families.

- Contain the Attack Wave
- Protect the Transport Network
- Break the Cross-Border Corridor
- Prevent Capital Seizure
- Retake the Lost State
- Restore Civil Authority
- Hostage Deadline when the incident appears
- Stop Coordinated Uprising after Evolution V

Missions should auto-complete when their real objective is satisfied.

Do not require a second paid click after the player performs the work.

Use the duration bands from the specification.

Short emergency timers are reserved for capital or hostage crises.

Every mission needs distinct success, partial success where accepted, and failure logic.

A mission failure should change the relevant pressure, state, actor, or world condition.

It cannot be a small generic stability loss.

## Costs

A gameplay-changing action may have at most four spendable cost types.

Use concrete action-appropriate costs.

Potential costs include:

- army experience
- conservative command power
- support equipment
- infantry equipment
- trucks
- trains
- convoys
- fuel
- manpower
- temporary civilian-factory burden
- temporary military-factory burden
- tied-down divisions
- stability or war support as an accepted consequence
- Response Legitimacy risk
- intelligence exposure
- sponsor dependency

Political power is allowed only where the action is genuinely political or administrative.

Do not use political power or command power as the generic payment for every action.

Cost localisation is icon-first and compact.

Every spendable value needs a valid texticon.

Do not hide a fifth cost in an effect or tooltip.

Requirements do not count as costs when they are not consumed.

## Dynamic cost and outcome model

Costs, durations, risks, aid, mission difficulty, and AI willingness should respond to:

- country size
- active-state count
- industry
- manpower
- equipment reserves
- fuel
- trains and convoys
- current war and fronts
- capital and supply risk
- state geography
- Terror Pressure
- Response Legitimacy
- state activity
- Network Reach
- External Supply
- actor force and territory
- previous failures and successes
- current evolution

Centralize shared tuning in script constants or a documented event-owned tuning file.

Use existing dynamic effects and stockpile-debit helpers where their contract fits.

Use `chaosx_scripted_system_architect` with `fork_context=false` when repeated logic needs reusable effects, triggers, targets, constants, or selected-target helpers.

Keep event-private helpers with Event 31.

Do not add them to the public dynamic registry unless they have demonstrated cross-system use.

## Operation outcomes

Implement five outcome classes for raids and comparable operations.

- clean success
- costly success
- partial success
- failure
- abusive failure

Outcome factors include:

- intelligence quality
- Response Legitimacy
- state activity
- organization supply
- force preparation
- local support
- terrain when the exact route can prove it
- current protection
- previous action history

The player sees a broad risk band and main contributing public factors.

The hidden random roll remains hidden.

Government-caused civilian harm uses its own Deaths reason and can reduce legitimacy or add Condemnation.

## State map mode and targets

Create an Event 31 state map presentation for:

- Dormant
- Active
- Entrenched
- Armed Insurgency
- Lost Local Control
- Recovery
- selected operation target
- corridor or safe haven where the implementation can show it accurately

Use exact state targets.

Do not use a capital proxy for an operation in another state.

The map and category must agree with the same state activity data.

The tooltip should name the organization, stage, current mission, broad next risk, and selected state action.

The map must use non-color cues.

If the required map-mode MCP route is unavailable, record the exact blocker. Do not treat source-only review as equivalent.

## Religion and community safeguards

Religion, ethnicity, nationality, refugee status, and ordinary ideology do not enter ordinary vulnerability, recruitment, or target weights.

After Evolution IV, an event-local Muslim-majority registry can control only:

- actor-specific jihadist enemy priority
- government reaction content
- fictional religious and community opposition
- protection of threatened worship and community sites

It cannot change baseline target or recruitment chance.

Protect Community and Religious Sites is available whenever the current network threatens relevant institutions. It adapts to the country's actual threatened civic and religious context.

Do not use sacred text as decision flavor.

## Foreign cooperation

A partner spends nothing before accepting a request.

Joint actions need valid actors, access, relations, threat, and target.

The design supports intelligence, border, relief, aid, volunteers, blockade, air support, and intervention according to real capacity.

No decision can commit another player's units or stockpile without consent.

Foreign aid creates influence, dependency, exposure, or postwar obligations where specified.

## AI

Implement AI for every action and mission.

Use the priority and validity rules from Part 9.

AI must:

- protect capital and critical supply first
- preserve resource reserve floors
- avoid duplicate missions
- target the actual support profile
- use victim support after major civilian losses
- avoid endless restrictions
- avoid raids with no intelligence unless an emergency justifies the risk
- intervene abroad only with access and domestic capacity
- keep actor capitals and supply viable
- avoid unsupported distant offensives

Every complex or balance-sensitive AI weight requires the full probability-audit cycle.

Spawn `chaosx_ai_probability_auditor` before a weighted patch and again after the owning patch.

Use the same named scenarios from `031_random_terror_ai_scenario_matrix.md` and require `hoi4.probability_compare` for the final pass.

## Cleanup

Every action and mission needs cleanup for:

- state cleared
- state lost to another actor
- country annexed
- actor defeated
- actor merged
- actor split
- sponsor dead or hostile
- corridor closed
- war ended
- route changed
- evolution disabled
- scenario ended
- world-end transition
- save and reload

Release tied divisions, factory burdens, targets, temporary modifiers, and scheduled jobs.

Do not refund consumed equipment or fuel.

Refund only resources that were reserved but genuinely unused under the accepted cancellation contract.

No stale selected target, duplicate mission, invalid corridor, or active decision may remain.

## Exploit checks

Test:

- repeated victim-support rewards
- free equipment capture
- sponsor-aid loops
- restriction stacking
- raid cancellation
- repeated surrender rewards
- duplicate capital security
- retake mission against restored state
- tag-switch persistence
- actor merger duplication
- scenario setup duplication
- uprising from stale pressure
- AI reserve exhaustion

## Assets and localisation

Use the final Event 31 category pictures, decision icons, mission icons, state-modifier icons, and map-mode sprites from the asset handoff.

Do not create primitive placeholders.

Write final localisation from the specification's direction.

Do not paste working labels, prompt language, hidden formulas, or implementation notes into player-facing text.

Name exact states, corridors, actors, sponsors, values, and requirements through scripted localisation.

Run `chaosx_localisation_auditor` after the full visible system exists.

## Required subagent and audit handoffs

Use:

- `chaosx_scripted_system_architect` for shared Event 31 helper design and bounded implementation
- `chaosx_ai_probability_auditor` for weighted surfaces
- `chaosx_decision_mission_auditor` after implementation for costs, mission quality, AI, cleanup, exploits, and clarity
- `chaosx_localisation_auditor` for visible text
- `chaosx_event_completion_auditor` during final event completion

Every patch-capable subagent must use `fork_context=false` and write a handoff under:

`docs/plans/031_random_terror_plans/subagent_handoffs/`

The parent owns final integration and completion.

## Validation cases

At minimum validate:

1. stable baseline containment
2. failed raid and adjacent-state relocation
3. capital-seizure mission
4. cross-border corridor with two consenting countries
5. territorial actor retake and civil restoration
6. negotiated surrender and hardliner split
7. sponsor death and cleanup
8. AI reserve floors during war
9. identity-neutral paired target cases
10. Evolution IV community opposition
11. Final Jihad coordinated uprising from real pressure
12. save and reload during every phase

## Completion gate

Do not claim the decision and mission system complete until every accepted matrix row is implemented or explicitly dispositioned, the visible action and mission budgets hold, costs and tooltips are correct, AI and probability evidence exist, cleanup passes, assets and localisation are final, and no custom GUI or unapproved fallback replaced the accepted design.
