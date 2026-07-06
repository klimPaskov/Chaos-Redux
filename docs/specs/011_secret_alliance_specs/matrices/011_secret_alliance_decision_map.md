# Event 011 Decision And Mission Map

This file is a compact implementation matrix. It does not provide final localisation.

## Category

Working id: `secret_alliance_countermeasures_category`

Visibility:

- hidden before Evolution II
- visible at Evolution II
- shifts to public crisis state at Evolution III
- shifts to war state after reveal
- cleans up after pact collapse or war resolution

Header values:

- exposure
- public awareness or proof
- pact pressure
- war readiness
- industrial security
- active operations
- known members
- border risk
- pact cohesion after public reveal

## Decisions

| Family | Working ids | Cost direction | Success | Failure or risk |
| --- | --- | --- | --- | --- |
| Counterintelligence | `expand_counterintelligence_desk`, `trace_courier_network`, `interrogate_captured_liaisons`, `turn_a_pact_contact` | command power, army XP, support equipment, trucks, trains, stability risk | evidence, member reveal, pressure drop | public anxiety, pact pressure, counter-propaganda |
| Preparation | `form_war_room`, `stockpile_border_railheads`, `disperse_aircraft_and_fuel`, `expand_emergency_reserves`, `prepare_allied_liaison_routes` | equipment, support equipment, trains, trucks, fuel, convoys, XP, command power | readiness, defense, first-strike mitigation | reduced gain, resource loss, industrial security strain |
| Exposure | `prepare_public_dossier`, `invite_neutral_observers`, `expose_selected_member`, `expose_the_pact_network` | evidence, convoys, trains, civilian factory burden, small political power | proof, cohesion damage, member reveal | pressure, propaganda, awareness without proof |
| Negotiation | `open_backchannel_to_selected_member`, `offer_verification_terms`, `guarantee_a_pact_exit`, `buy_out_pact_contracts`, `host_security_conference` | leverage, concessions, equipment, civilian factory burden, war support risk | split, delay, lower cohesion | harden target, lose leverage, raise heat |
| Industrial protection | `harden_military_factories`, `guard_rail_and_train_yards`, `secure_depot_belt`, `screen_war_contracts` | support equipment, trucks, trains, factory burden | industrial security and sabotage reduction | state penalties, pressure increase |
| Propaganda and diplomacy | `sponsor_independent_press`, `rally_allied_observers`, `warn_threatened_neighbors`, `publicize_pact_defections` | factory burden, convoys, small political power, stability risk | controlled awareness, leverage, fewer recruits | anxiety, counter-propaganda |
| Border incidents | `probe_selected_border_member`, `secure_border_corridor`, `start_limited_border_operation`, `border_clash_time_until_cancelled`, `escalate_border_clash` | command power, army XP, infantry equipment, support equipment, fuel | readiness, commitment drop, member reveal | cohesion, pressure, formal-war risk |

## Timed Missions

| Mission | Owner | Target or region | Success | Failure |
| --- | --- | --- | --- | --- |
| `secret_alliance_mission_trace_couriers` | player | domestic rail and border routes | evidence and member reveal chance | pressure and public anxiety |
| `secret_alliance_mission_guard_border_corridors` | player | border states adjacent to known members | readiness and border risk drop | target confidence and pressure |
| `secret_alliance_mission_secure_depot_belt` | player | industrial or supply states | industrial security and sabotage reduction | state damage or output penalty |
| `secret_alliance_mission_neutral_observer_tour` | player | selected member or domestic proof route | awareness becomes proof | awareness rises without proof |
| `secret_alliance_mission_split_selected_member` | player | selected known member | split or delay member | leverage loss and target cooldown |
| `secret_alliance_mission_war_room_readiness` | player | national | readiness and first-strike mitigation | reduced readiness gain |
| `secret_alliance_mission_counter_sabotage_surge` | player | industrial states after sabotage | security recovery and evidence | further sabotage or security loss |
| `secret_alliance_mission_border_clash_timer` | player and target if playable | paired border states | cleanup or result record | escalation or pressure |
| `secret_alliance_mission_contain_leak_panic` | player | national | stabilize awareness | stability or war support loss |

## Border War Rules

Use WTT-style border conflict structure:

- select valid paired states
- set state flags
- activate warning and timeout missions
- use no state transfer by default
- clear all state and target flags on outcome

No border decision should run if:

- target is already at war with player
- target is not a live pact member
- either side lacks a valid controlled adjacent state
- target has a cooldown
- state pair is already in a border incident
- player lacks required supplied divisions or resources

## AI Requirements

Every AI action must:

- use the same validity triggers as human decisions
- check active operation cap
- check dynamic costs
- avoid human selected-target state
- avoid dead, capitulated, subject, player-faction, or already split targets

