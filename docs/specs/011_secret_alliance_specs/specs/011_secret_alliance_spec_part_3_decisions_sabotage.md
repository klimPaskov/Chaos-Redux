# Event 011 Secret Alliance Spec Part 3: Decisions, Missions, And Sabotage

## Category Lifecycle

Working category id: `secret_alliance_countermeasures_category`

The category appears at Evolution II and remains through Evolution III, reveal war, and aftermath cleanup where relevant.

Before Evolution II:

- no broad decision category
- player sees reports and suspicion only
- hidden pact actions update state and future targets

Evolution II:

- category unlocks
- player sees exposure, pressure, readiness, industrial security, active operation cap, and known-member count
- known-member actions target only identified or exposed members
- broad domestic actions can run without naming every member

Evolution III:

- category shifts from investigation to public crisis management
- hidden suspect wording becomes public pact member wording
- pact cohesion becomes visible
- emergency diplomacy, readiness, and border-crisis decisions become stronger

War phase:

- remove peacetime negotiation that no longer makes sense
- keep industrial protection, propaganda, war readiness, and split-member wartime routes where valid
- prevent border-war decisions when formal war exists

Aftermath:

- hide the category when the pact ends or cleanup completes
- preserve achievement state and Event Log evidence

## Visible Values

The category header should show compact state, not raw scripting.

Required visible values:

- Exposure or Evidence
- Public Awareness or Proof
- Pact Pressure
- War Readiness
- Industrial Security
- Active Operations over cap
- Known Members count
- Border Risk when a known member borders the player
- Pact Cohesion after public reveal

Tooltips should explain current sources and consequences without exposing hidden future triggers.

## Active Mission Cap

Use an active operation cap so the category never becomes a resource-free checklist.

Design direction:

- Evolution II baseline cap is low
- major player countries can support one extra operation
- Evolution III or war can add one extra operation
- hard cap remains small enough to force tradeoffs
- AI gets stricter caps when low on equipment, stability, manpower, or trains

The cap should be recalculated by helper effect before mission activation.

## Target Selection

Human target selection should use a compact selected-target pattern:

- selector lists valid known members
- selecting a target stores a selected state and clears previous selection
- follow-up targeted decisions only appear for that selected target
- a close target decision clears the selection

AI should not use the human selector. AI evaluates valid targets through arrays and scripted effects with the same validity triggers.

Target rejects:

- target does not exist
- target is not a current pact member for member-only decisions
- target has capitulated
- target is in the player's faction
- target is a subject of the player
- target is already split from the pact
- target is already at war with the player for peacetime routes
- border pair is invalid for border routes

## Decision Family: Counterintelligence

Purpose:

- convert suspicion into evidence
- reveal members
- reduce sabotage pressure
- seed negotiation leverage

Working actions:

- `secret_alliance_expand_counterintelligence_desk`
- `secret_alliance_trace_courier_network`
- `secret_alliance_interrogate_captured_liaisons`
- `secret_alliance_turn_a_pact_contact`

Costs:

- command power or army XP for liaison work
- support equipment for field teams
- trucks or trains for courier tracing
- stability or war support risk for heavy domestic security work
- temporary civilian factory burden for nationwide investigations

Outcomes:

- success adds evidence, may reveal a member, lowers pressure, and can improve industrial security
- failure raises pact pressure, public anxiety, or triggers counter-propaganda
- partial success adds evidence but increases public awareness risk

## Decision Family: Preparation

Purpose:

- make the reveal war survivable without instantly starting it

Working actions:

- `secret_alliance_form_war_room`
- `secret_alliance_stockpile_border_railheads`
- `secret_alliance_disperse_aircraft_and_fuel`
- `secret_alliance_expand_emergency_reserves`
- `secret_alliance_prepare_allied_liaison_routes`

Costs:

- infantry equipment and support equipment
- trucks, trains, convoys, and fuel where the action uses supply routes
- army XP or command power
- war support or stability strain
- temporary civilian factory burden for logistics work

Outcomes:

- readiness rises
- first pact attack becomes less damaging
- defensive or logistics modifiers activate
- poor execution can consume equipment with reduced readiness gain

## Decision Family: Exposure

Purpose:

- turn evidence into public proof
- reveal or isolate members
- reduce cohesion
- force neutral governments to react

Working actions:

- `secret_alliance_prepare_public_dossier`
- `secret_alliance_invite_neutral_observers`
- `secret_alliance_expose_selected_member`
- `secret_alliance_expose_the_pact_network`

Costs:

- evidence thresholds
- convoys or trains for observers where distance matters
- civilian factory burden for press, legal, and diplomatic material
- small political power cost only for formal diplomacy
- higher cost against majors or high-pressure pact state

Outcomes:

- success reveals a member or all known members, lowers cohesion, and can improve neutral sympathy
- failure raises pact pressure and gives the target propaganda
- partial success raises public awareness and identifies a member with limited cohesion damage

Repeated exposure without evidence should raise war risk and cost more.

## Decision Family: Negotiation And Splitting

Purpose:

- split, delay, or neutralize members without making negotiation a flat peace button

Working actions:

- `secret_alliance_open_backchannel_to_selected_member`
- `secret_alliance_offer_verification_terms`
- `secret_alliance_guarantee_a_pact_exit`
- `secret_alliance_buy_out_pact_contracts`
- `secret_alliance_host_security_conference`

Costs:

- negotiation leverage
- civilian factory burden or equipment concessions
- convoys, trains, or fuel for support packages
- war support loss risk if concessions look weak

Rules:

- target must not be at war with the player
- target must be valid and known or correctly suspected
- organizer and major sponsor are much harder to split
- reluctant members are the best targets

Outcomes:

- success splits or delays a member and lowers cohesion
- failure loses leverage and hardens the target
- partial success delays participation or reveals another member

## Decision Family: Industrial Protection

Purpose:

- protect factories, depots, railways, ports, and supply lines from pact sabotage

Working actions:

- `secret_alliance_harden_military_factories`
- `secret_alliance_guard_rail_and_train_yards`
- `secret_alliance_secure_depot_belt`
- `secret_alliance_screen_war_contracts`

Costs:

- support equipment
- trucks
- trains
- temporary civilian factory burden
- local state control for targeted protection

Outcomes:

- industrial security rises
- sabotage severity decreases
- target states gain protection
- failure can create output, rail, or supply penalties

## Decision Family: Propaganda And Diplomacy

Purpose:

- manage public morale, build external support, and deny pact narratives

Working actions:

- `secret_alliance_sponsor_independent_press`
- `secret_alliance_rally_allied_observers`
- `secret_alliance_warn_threatened_neighbors`
- `secret_alliance_publicize_pact_defections`

Costs:

- civilian factory burden
- convoys for foreign observers
- small political power where the action is formal diplomacy
- stability or war support risk if inflammatory

Outcomes:

- controlled public awareness
- negotiation leverage
- lower chance of neutral recruits
- allied willingness to help

Failure should raise anxiety faster than evidence.

## Decision Family: Border Incidents And Border Wars

Purpose:

- give the player an active military response against neighboring pact members without creating free war-goal spam or state farming

Working actions:

- `secret_alliance_probe_selected_border_member`
- `secret_alliance_secure_border_corridor`
- `secret_alliance_start_limited_border_operation`
- `secret_alliance_border_clash_time_until_cancelled`
- `secret_alliance_escalate_border_clash`

Availability:

- Evolution II or later
- selected target is a known pact member
- target borders the player through a valid land border
- neither side is already at war with the other
- no active border war or active state-pair flag exists
- player has enough divisions and supply in the attacker region
- target has a controlled neighboring state that is not impassable

Handling:

- use the vanilla WTT paired-state pattern
- store attacker and defender states
- set flags on both states
- start border war with `change_state_after_war = no`
- activate timeout or escalation missions
- clear flags, selected targets, and active missions on win, loss, cancel, timeout, or formal war

Outcomes:

- player win raises readiness, lowers member commitment, and may reveal that member
- player loss raises pact cohesion, pressure, and reveal chance
- cancel reduces immediate risk but can raise heat

## Sabotage Packets

Sabotage should be concrete, paced, and tied to member roles.

Baseline:

- mostly reports and minor pressure
- no major building damage

Evolution I:

- press, courier, arms shipment, and border rumour reports
- small readiness or industrial security pressure

Evolution II:

- factory, railway, port, airfield, supply node, and arsenal incidents
- rare abstract assassination or disappearance events only when safe surfaces exist
- sabotage severity reduced by industrial security and preparation decisions

Evolution III:

- sabotage becomes public coercion, open mobilization, sanctions, threats, and border crisis

Implementation should use existing reusable building-damage helper patterns where they fit. Repeated sabotage against the same state or building family needs cooldowns.

## Timed Mission Families

Missions should be activated by decisions or event effects, not dumped passively.

Core missions:

- trace couriers: evidence and member reveal
- guard border corridors: readiness and border risk
- secure depot belt: industrial security and sabotage reduction
- neutral observer tour: public proof and exposure
- split selected member: negotiation and delayed participation
- war room readiness: national readiness and first-strike mitigation
- counter-sabotage surge: reactive recovery after sabotage
- border clash timer: stale border-war cleanup or escalation
- contain leak panic: recovery after failed public exposure

Each mission needs:

- owner
- target or region
- concrete resource cost
- active operation cap check
- success
- failure
- partial success where useful
- cleanup
- AI validity rules

## Cleanup

Use a central cleanup effect for decisions and missions.

Cleanup must:

- remove active Event 011 missions
- remove active targeted decisions
- clear selected target variables and target flags
- clear border state flags and paired-state variables
- clear temporary global event targets if used
- preserve Event Log and achievement history
- remove peacetime decisions when reveal war begins
- hide the category when the event ends or pact collapses

