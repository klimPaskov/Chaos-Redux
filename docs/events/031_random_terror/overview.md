# Event 31 Random Terror

## Identity and pacing

Random Terror is Event `31`, enters through `chaosx.nr31.1`, remains a Minor Repeatable event at Chaos level `1`, and records one pacing event even though one bounded global wave can affect several eligible countries and exact states.

The hidden entry event calls `random_terror_run_global_wave`, refreshes the global ledgers, schedules eligible evolution or world-end work, and sends local report callbacks without allowing those callbacks to increment pacing again.

The accepted evolution names are Organized Cells, Transnational Terror Network, Territorial Insurgency, The Jihadist International, and The Final Jihad.

Each evolution has one presentation guarded by a one-time global flag (`random_terror_emit_evolution_report`): Evolution II sends report `chaosx.nr31.3` and news `chaosx.news.311`, Evolution III sends report `chaosx.nr31.4` once a territorial actor exists (deferred to the first actor otherwise), Evolution IV sends report `chaosx.nr31.5`, and Evolution V sends news `chaosx.news.313`.
The first territorial actor of the campaign sends news `chaosx.news.312` (`random_terror_emit_first_actor_news`), and a terminal defeat sends news `chaosx.news.314` beside report `chaosx.nr31.8` and the Broken Claim super-event.
Global Jihad setup holds all of these back while still setting their guards.

Global Jihad remains a scenario owned by Event 31, and The False Revelation remains the terminal world-end branch.

The accepted proposal for `SCN-014` collided with Fallout, and `SCN-015` is occupied by Missile Age.
Global Jihad uses triggerable-scenario slot `SCN-016` and its separate world-end registry uses slot 15.
Internal Fracture is not registered because its member package has not been accepted.

## State model

Every affected government maintains Terror Pressure, Response Legitimacy, incident count, response history, and mission locks.

Every affected state maintains activity, pressure, incident memory, exact civilian-loss accounting, cooldown state, territorial readiness, and action or mission commitments.

State activity uses the 0-100 stage ladder with Active above 20, Entrenched above 40, Armed Insurgency above 60 and Lost Local Control above 78 activity and pressure.
The first incident in a Clear or Dormant state opens it at Active (`state_activity_opening`), later incidents and setbacks add `state_activity_gain`, and routine response actions remove `state_activity_loss`, so a state normally advances one stage over a few incidents.

Each stage from Dormant to Lost Local Control carries its own dynamic state modifier in `common/dynamic_modifiers/031_random_terror_dynamic_modifiers.txt` (`random_terror_state_dormant`, `_active`, `_entrenched`, `_armed_insurgency`, `_lost_local_control`).
`random_terror_refresh_state_modifier` runs at the end of every stage update and in state cleanup, keeping exactly the modifier that matches `random_terror_state_stage` and none on a Clear state.
Impact grows by stage from slower construction at Dormant through output and resource losses at Active and Entrenched to recruitment and movement penalties at Armed Insurgency and Lost Local Control, with every value in the `random_terror_state_modifier` script constants.
The modifiers reuse the Event 31 idea sprites `GFX_idea_random_terror_distributed_command`, `_contested_legitimacy`, `_network_directorate`, `_unified_field_command` and `_failed_rule` from `interface/031_random_terror.gfx`, so no new art is required.

Active crises recur through event-owned pacing rather than a world scan.
Each affected government holds at most one pending hidden pulse (`chaosx.nr31.96`, guarded by the timed `random_terror_pulse_pending` flag).
`random_terror_schedule_country_pulse` reads `random_terror_incident_pulse_days` in the country's scope, which follows the Part 2 bands of its most severe owned state (about 60-90 days Active, 30-60 Entrenched, 15-35 Armed Insurgency or worse), is delayed by successful protection missions and accelerated by failed operations, high Terror Pressure and high Network Reach, then receives a random 0.8-1.2 spread and the band clamp.
The pulse applies one incident through `random_terror_apply_incident` to a valid active state that is off cooldown, postpones itself when no state is eligible, reschedules only while the crisis stays active, stops while Event 31 is disabled in the Event Logs settings, and never touches repeatable weight, minor-event pacing or the Event Logs history.

### Incident report and first emphasis

Every incident stores its state (`random_terror_last_report_state`), family (`random_terror_last_report_incident_type`) and measured civilian loss (`random_terror_last_report_loss`, the exact population loss applied by `random_terror_apply_exact_state_loss`) on the struck state's controller before the report `chaosx.nr31.2` fires.
The report title names the state, `GetRandomTerrorIncidentReportDesc` describes the family in the same nine groups and fallback as `GetRandomTerrorIncidentReportPicture`, so text and picture always agree (community rejection keeps the fallback picture with its own text), and `GetRandomTerrorIncidentReportLoss` adds the confirmed death toll only when one was measured.

The opening report of a crisis offers the four first emphases of Part 1 Assessment; later reports of the same crisis keep one acknowledgement, and `random_terror_emphasis_chosen` resets when the crisis closes.
Each emphasis lasts `random_terror_emphasis.days`, adds a timed country modifier from `031_random_terror_dynamic_modifiers.txt` with its decision family's icon, and sets a timed flag read by that family:

| Emphasis | Immediate | While it lasts |
| --- | --- | --- |
| Protective Cordons (`random_terror_emphasis_protection`) | local pressure in the reported state falls by `protected_pressure_reduction` | attacks on crowds, rail and ports anywhere in the country strike the guards at the transport-protection odds; war support up, conscription down |
| Intelligence Priority (`random_terror_emphasis_intelligence`) | none | Intelligence Sweep opens without a response cell, and the first Targeted Raid draws one outcome band higher (`random_terror_emphasis_first_raid`); civilian intelligence up, political power gain down |
| Relief First (`random_terror_emphasis_victims`) | Response Legitimacy rises by `response_legitimacy_gain` | Support Victims stays open beside a response cell and also removes `state_activity_loss` where it lands; stability up, construction speed down |
| Rapid Crackdown (`random_terror_emphasis_coercion`) | activity in the reported state falls by `state_activity_loss`, Response Legitimacy drops by `coercion_legitimacy_loss` | each Security Surge removes a further `state_activity_loss`; war support up, stability down |

No emphasis closes any response, so the choice steers the opening without locking a doctrine.
The AI weighs protection up for a capital or disrupted transport state, intelligence up after Evolution II or with high legitimacy, relief up after measured deaths or with middling legitimacy, and coercion up at war or under high pressure and down for democracies.

Later evolutions add Network Reach, International Unity, territorial-control values, actor authority, external supply, strategic victories, and hidden apocalyptic readiness without changing the identity-neutral baseline targeting rules.

Religion, ethnicity, nationality, refugee status, and ordinary ideology never increase baseline target or recruitment weight.

Evolution IV alone opens the wholly fictional jihadist branch, and its content includes opposition from Muslim governments, communities, clerics, soldiers, civic organizations, and fictional religious authorities.

The final entity is presented as an unexplained presence whose followers make a divine claim.
The game never confirms that it is Allah or any divine being.

## Outcomes and containment

The accepted baseline covers containment, continued spread, coups, civil war, state partition, territorial takeover, negotiated surrender, territorial actor formation, and defeat.
The current source contains those outcome families, with the unresolved unit, mission and transaction findings listed below.

Disabled evolutions leave the ordinary incident, containment, state-response, surrender, and defeat paths available.

### Recovery and closure

A state that falls from Active or worse back to Dormant or Clear becomes recovering (`random_terror_state_recovery`, set in `random_terror_update_state_stage`), and the marker clears when the state reaches Clear or when Restore Civil Authority succeeds there.
A government enters the recovery phase (`random_terror_government_phase_recovery`) once none of its states is Active or worse, no core is held at Armed Insurgency or Lost Local Control, and no Event 31 command is at war with it; no actor defeat is needed.
The recovery phase shows Support Victims and Restore Services on the priority recovering state, Publish a Public Accounting after recent attacks, civilian losses, an exposed sponsor or a failed raid, and Reform the Security Services after any response action, accounting or defeated command.
Public Accounting and Security Reform are once per crisis: Public Accounting raises Response Legitimacy and lowers Terror Pressure by `random_terror_recovery.accounting_pressure_reduction`, and Security Reform raises legitimacy and lengthens the post-crisis rest.

Every affected government keeps one hidden recovery check (`chaosx.nr31.97`, guarded by the timed `random_terror_recovery_check_pending` flag) every `random_terror_recovery.check_days` while its crisis is open.
In the recovery phase each check lowers Terror Pressure by `pressure_decay` and the activity of every recovering state by `activity_decay`, then calls `random_terror_close_country_recovery`, which the recovery decisions and every mission end also call.
The crisis closes when `random_terror_country_recovery_complete` holds: no recovering state, no running mission and zero Terror Pressure.
Closure finalizes the player's achievement checks, sends the short recovery report `chaosx.nr31.9` once, gives the country a `random_terror_recovery_cooldown` rest from ordinary waves (`cooldown_days`, or `reformed_cooldown_days` after Security Reform), and runs `random_terror_reset_crisis_cycle`, which clears the affected marker, Terror Pressure, Response Legitimacy, response capacity, the per-crisis decision markers, the coup and civil-war gates, the failed-raid and sponsor-exposure records and every mission outcome flag.
A later crisis in the same country can therefore run every response decision again, while a deliberate Global Jihad scenario may still re-enter a resting country.

The terminal transaction requires the normal Chaos and territorial-readiness gates even when Maximum Global Jihad activates The Final Jihad.

The actual terminal role requires the final profile, a country final-actor receipt and the active terminal transaction.
Ordinary JMX is a human Final Jihad command with ordinary ideas and three research slots.
Its symbolic Final Command Council precedes the entity, which is recruited without a leadership role and promoted only through the gated transaction.
The terminal marker supplies five slots and records the host's prior count for exact cleanup restoration.
The counteroffensive commits denial from its three-contribution quorum and terminal losses, allowing the objective to be established before the final-defeat predicate requires it.
Member consent, merger accounting, faction handling and the full aftermath retain open validation and implementation findings.

## Decisions, missions, and exact states

The system uses the compact government-response, actor-command, and False Revelation decision categories defined in `common/decisions/categories/031_random_terror_categories.txt`.

Government and actor actions use standard state-targeted decision presentation, concrete variable-backed costs, exact state flags, target locks, outcome helpers, AI weights, and cleanup hooks.

No Event 31-specific scripted GUI exists.

Each government keeps a priority crisis state, its most severe crisis among the states it controls and its own cores held by others (higher stage first, then higher activity), refreshed after each incident, on every stage change and when a state is lost (`random_terror_refresh_priority_state`, state flag `random_terror_priority_state_<tag>`).
With no active crisis left, a recovering state it controls (`random_terror_state_recovery`, most residual activity first) becomes the priority state, so Support Victims keeps one row through the recovery phase.
Decisions with a generic crisis target (response cell, transport, victim support, intelligence sweep, security surge, raid, allied intelligence, movement restrictions, reinforcement and the territorial actions) accept only that state, the government's hostage or uprising subject, or the subject of the containment, corridor or civil-authority mission they advance (`random_terror_state_is_response_target`), so each shows one row in normal play.
Decisions keyed to a recorded marker (corridor, sponsor evidence, defection, community rejection, recovery or capital infiltration) keep that marker as their target.

Event 31 repeats, so no response or actor decision uses `fire_only_once`; each carries the guard its matrix cleanup asks for.
Establish a Response Cell runs once per crisis through `random_terror_response_cell_active`, which the crisis closure resets.
Expose the Sponsor and Pressure the Sponsor in Private are alternatives on one evidence package: either consumes the state's `random_terror_sponsor_evidence_recorded` marker, and the public case condemns each sponsoring country only once.
Negotiate an Enclave Surrender is one settlement per armed command (`random_terror_negotiated_surrender` on the command).
Absorb a Rival Actor allows one pending offer per target and never asks again a command that refused (`random_terror_absorption_refused_by_<tag>`), Contest the Network Leader challenges each leader once (`random_terror_leader_contested_<tag>`), and Join the Jihadist International allows one petition at a time, none while a member and none to a leader that rejected the command (`random_terror_jihad_refused_by_<tag>`).
Actor retirement clears these per-target records in both directions, so a reused carrier starts clean.
Recruit Foreign Fighters closes for `foreign_fighters_cooldown_days` after each intake through its timed flag.

Every costed decision has one inclusive affordability trigger, `random_terror_can_afford_<decision>` in `031_random_terror_triggers.txt`, used by its `custom_cost_trigger` and mirrored in `available` through `hidden_trigger`, so an exact balance pays and each line matches one debit in the decision's `complete_effect`.
Every `custom_cost_text` key has `_blocked` (red values) and `_tooltip` companions, and cost rows put each texticon before its value.
Temporary Movement Restrictions is the one escalating price: each use adds to `random_terror_movement_restrictions_uses`, and `random_terror_update_movement_restrictions_cost` raises the Stability and support equipment price by one repeat step per earlier use, up to `movement_repeat_max_steps`; its only state flag is the timed `random_terror_movement_restrictions_active`, and every use after the first draws public condemnation.

Every mission is started by a `random_terror_begin_<family>_mission` helper in the receiving country's scope and ended by the matching `random_terror_finish_<family>_mission`, which clears only that receiver's receipt.
The begin helper keys the subject flag and the stored baseline to the receiver (`random_terror_<family>_goal_@<receiver>` and similar state variables), so each objective compares the state's live values with its own start.
Country counters `random_terror_hotspot_count` (owned states that newly became an active crisis) and `random_terror_states_lost_count` (states lost to an actor), and state counters `random_terror_state_incident_count` and `random_terror_state_disruption_count`, measure spread, losses and attacks.

| Mission | Type | Success | Partial | Failure |
| --- | --- | --- | --- | --- |
| Contain the Attack Wave | achieve | subject activity down by 15 or no longer an active crisis, with no new hotspot | deadline without spread or stage advance | deadline after a new hotspot or a stage advance |
| Protect the Transport Network | hold (`is_good`) | deadline with no new transport attack | deadline after one attack | two attacks, loss of control or Lost Local Control ends it early |
| Break the Cross-Border Corridor | achieve | corridor marker absent and activity a further 10 below the post-strike value | deadline with the route closed and no new hotspot | deadline with the route reopened or a new hotspot |
| Prevent the Capital's Seizure | hold (`is_good`) | deadline with no new capital attack and no state lost | deadline after a capital attack or a lost state | loss of control or Lost Local Control ends it early and triggers the coup branch |
| Retake the Lost State | achieve | military control of the subject | deadline with the subject held by a non-actor | deadline with the actor still holding it |
| Restore Civil Authority | achieve | activity down by 10 and no higher than 20 under control | deadline with some activity reduction | deadline without progress |
| The Hostage Deadline | achieve | captives freed by a surge or a clean or costly raid | deadline after a surge on an armed cell or a partial raid freed some captives | deadline with captives held, with mass casualties |
| Stop the Coordinated Uprising | achieve | subject held and broken by a surge or raid, or activity down by 15 | deadline with the subject still held | deadline after control is lost |

Resolved missions move national Terror Pressure (success lowers it by 12, partial by 6, failure raises it by 8), and every state-targeted response lowers it by 3, so a country can bring pressure back down.
Security Surge and Targeted Raid stay usable on the receiver's hostage or uprising subject in any phase before the terminal war, even while that emergency holds its mission slot.
Missions cancel only through `random_terror_can_hold_response_mission`, so the action lock applied by each response decision never cancels the mission it started.
A protected transport state turns half of the route attacks against it into attacks on its guards.

Global Jihad is registered in the shared `chaosx_scenarios_window` list with all five deployment types, all four intensities, dynamic descriptions and impact warnings, fail-closed launch status, and the Event 31 preflight transaction. Maximum enables The Final Jihad but only schedules The False Revelation through the ordinary `1000+` Chaos, readiness, unity, territorial-control, crisis-state, strategic-victory, and viable-actor gates.

`random_terror_resolve_scenario_profile` writes only the scenario targets and the evolution stage the launch will open (`global.random_terror_scenario_target_stage`).
The preflight counts only free carriers whose spawner gate that stage unlocks, so JMX counts only at Maximum, and Maximum clamps its actor target to the free carriers and valid states with at least one actor in all.
Evolution flags and the stage are applied by `random_terror_apply_scenario_evolutions` only after the preflight passes, and a blocked launch clears the profile it wrote, so it leaves no evolution, flag or actor behind.
From Medium upward, when at least two actors exist, `random_terror_scenario_form_coordination` lets the strongest actor found the Jihadist International and brings the others in, while High and Maximum keep one rival command independent (`random_terror_independent_command`).
Setup records its evolutions in the Event Logs but holds back their report popups; seeded governments receive the launch report `chaosx.nr31.90`, every other player receives `chaosx.nr31.6`, and the world receives `chaosx.news.310`.

## Territorial actors

Eight predeclared carrier tags provide bounded territorial-country capacity without dynamic tags, custom units, Event 19 providers, 3D models, custom unit sounds, or bespoke counters.

The carrier framework declares capitals, fictional leaders and councils, existing infantry templates, basic technology, manpower and equipment setup, focus loading and diplomatic or cleanup helpers.
The complete accepted country package requires dynamic safe capitals, resource-grounded forces, compatible donor research, functional economy, reinforcement, diplomacy, AI and playable cleanup.
The current capacity/force audit identifies gaps in those requirements and does not approve the eight declarations as complete packages.

A carrier is free only when its tag does not exist and its `random_terror_slot_<tag>_used` flag is clear (`random_terror_carrier_is_free`).
The spawner, the Global Jihad availability trigger and the scenario preflight share that predicate, and `random_terror_release_dead_carriers` clears a reservation only after the tag has stopped existing, so a retained or occupied carrier never receives a second package.
A carrier that died in a peace deal without an Event 31 cleanup pass has its previous lifetime cleared before its next package.
When an AI actor is retired, `random_terror_return_actor_states` hands its states to its living parent; without one, each state goes to a living government outside the crisis that holds its core, otherwise to the actor's strongest enemy by division count.
An AI actor left holding a state that nobody could take keeps its Event 31 flags, units and carrier reservation, so the crisis can still defeat or absorb it, and a human actor is always retired in place.

An ordinary spawn (`random_terror_state_can_spawn_actor`) never takes the parent's capital and requires the parent to keep its own controlled capital.
When a capital reaches Lost Local Control and cannot secede, its government faces a coup attempt, and the ordinary civil-war check carries any other blocked state.
Every new actor, ordinary or created by Global Jihad, declares war on its parent through `random_terror_actor_declare_parent_war` when the game allows it, which opens the retake, isolation and offensive actions.

Actor actions perform their matrix operations with existing units and buildings.
`random_terror_actor_raise_formation` raises one formation of the carriers' shared `Infantry Division` template through `create_unit`, using the start factors and ids in the `random_terror_unit` constants, and the formation actions stay below `actor_division_cap` divisions.
Raise Local Militia forms an under-strength militia keyed to its state and marks the state for conversion, Integrate Defectors forms one seasoned formation, Convert the Militia retires that state's militia by id and trains one regular formation in its place, and Recruit Foreign Fighters gives a net manpower and equipment intake with one experienced volunteer formation.
Begin Ideological Mobilization turns its manpower price into one disciplined formation in the target state (`cadre_id`), a second one after Codify the Doctrine, and gives the command `random_terror_mobilized_cadres` (more recruitable population, less stability) for `mobilization_days`; its timed `random_terror_ideological_mobilization_active` flag keeps the decision closed until the mobilization ends, after which it can be called again in any active or entrenched state the command holds, including the same one, and the permanent `random_terror_ideological_mobilization_recorded` flag keeps the Jihadist International entry open.
Repair a Captured Depot rebuilds the depot as an arms factory, or as infrastructure when no factory slot is free, and Build a Civil Administration rebuilds infrastructure while raising Territorial Control and Network Authority.
Relocate the Network moves a cell out of a crisis state its government has swept (`random_terror_cell_relocated`), so the next government raid there can at best be a partial success.
Military Reinforcement keeps the government's state from falling into Lost Local Control for `reinforcement_days` (`random_terror_state_reinforced`).
When focuses reuse these helpers without a target state, the formation forms in the actor's own provinces and the building work goes to a damaged depot or the capital.
A focus reward sets the temp variable `random_terror_focus_context` before it reuses a helper, so `random_terror_actor_action_common` skips the decision cooldown and completing a focus never locks the actor's decisions.
The retirement cleanup also removes International Mandate and the Local Revolt, Mass Defection and Failed Rule spirits, so a reused carrier starts without them.

Each one-person carrier history recruits its leader and a small roleless candidate pool from `common/characters/031_random_terror_characters.txt`: JLX the jihadist pool, JNX the clandestine and three criminal candidates, JOX the military and three criminal candidates, and JPX the revolutionary and millenarian pools.
A fresh actor package (`random_terror_select_actor_leader`) promotes one random candidate or the history leader, never the outgoing one, and removes the leader role of the pooled leader it replaces, with `random_terror_leader_slot` recording the current candidate.
The Shadow Council and the War Directorate alternate with the Civic Coordination Council and the Regional Continuity Council when their carrier is reused, while the Ideological Secretariat, the Final Command Council and The Unanswered Presence keep their identities, so all 45 portraits have a consumer.

The three starting spirits are replaced by the route focuses through three idea slots (`031_random_terror_focus_effects.txt`, ids in the `random_terror_idea_form` constants).
Each focus that grants a stable form calls `random_terror_set_command_form`, `random_terror_set_economy_form` or `random_terror_set_legitimacy_form`, which removes every other stable form of that slot, so an actor holds at most one command, one economy and one legitimacy spirit from the tree:

| Slot | Start | Stable forms and the focuses that grant them |
| --- | --- | --- |
| Command | Improvised Command | Distributed Command (Shadow Network Directorate), Unified Field Command (Field Command Board), Cadre Authority (Convene the Cadre), Network Directorate (Intelligence by Whisper), Directorate General Staff (Directorate General Staff), Ideological State (Enthrone the Ideological State) |
| Economy | Captured Economy | External Supply System (Smuggling and External Supply), Looting Spiral (Coerced Extraction), Directed War Economy (Directed War Economy), Civil Administration (Civil Administration), Patron Development Mission (Foreign Sponsorship), Sponsor Dependency (Sponsor Dependency) |
| Legitimacy | Contested Legitimacy | Security State (Fortify the Headquarters, Harden the Defensive Line, Establish Forced Rule), Claimed Authority (Stabilize the Capital, Protect the Council, Authority through Service, Consolidate Captured Territory, Return from the Crisis), Recognized Enclave (Build the Regional State, Secure Recognition, Negotiated Enclave), International Mandate (Form the Confederation, Accept the International Claim) |

Founding Crisis adds a starting spirit only when the actor setup has not already given it (`random_terror_focus_ensure_starting_forms`), and the opening keeps the three starting problems: Captured Economy waits for the economy route choice, Improvised Command for the leadership route choice, and Contested Legitimacy for the first legitimacy focus.
Looting Spiral and Sponsor Dependency are also failure overlays; a slot change removes them only when the overlay does not own them, and a focus that chooses one takes it over from the overlay.
Focuses whose only reward would repeat a spirit the actor already holds carry their own rewards: Hold the Enclave raises a militia, Restore Supply repairs a depot, Secure the Command Center adds anti-air and radios, Restore the Workshops builds a military factory, Seal the Inner Circle ends Compromised Network and hides threatened cells, Layered Safehouses builds bunkers outside the seat, Protect the Route opens a corridor with roads and convoys, Appoint the Directorate raises a guard formation, Field Radio Discipline gives radios and `random_terror_field_radio_discipline`, Unify the Brigades raises two formations, Claim Revolutionary Authority gives political power, Purge the Hardliners ends Doctrinal Schism and Rival Warlords at a stability cost, Align with the Patron gives an infantry-weapons research bonus, Patron Development builds a civilian factory, Reconcile the Factions ends Rival Warlords and Doctrinal Schism, the Compliant Religious Councils give political power, and Reconcile the Jihadists makes a white peace with every AI-run International command it is fighting.
Actor decisions run `random_terror_refresh_actor_lifecycles`, which owns only a failure overlay of at most one command failure and one economy failure, chosen by route as in the Part 6 lifecycle table.
Territorial Control or Network Authority below the low band shows Compromised Network for the Shadow Council, Rival Warlords for the War Directorate and Doctrinal Schism otherwise (the route chosen in the tree first, then the starting profile's); External Supply below the low band shows Looting Spiral on the coerced economy, Sponsor Dependency under foreign sponsorship and Famine otherwise.
The overlay adds a failure spirit only when it is absent and marks it with a `random_terror_lifecycle_owns_<idea>` flag; recovery or a route change removes only those owned spirits, so focus rewards are never stripped.
The crisis focuses choose failure forms through the same slots.
Leadership Split (Rival Warlords), Compromised Network and Doctrinal Schism call `random_terror_set_command_failure_form`, which replaces any other command failure and takes the chosen one over from the overlay, and the overlay adds a command failure only while the actor shows none (`random_terror_has_command_failure_form`).
Local Revolt and Mass Defection call `random_terror_add_legitimacy_failure`: the first legitimacy failure shows as itself, and a second, different one merges both into Failed Rule.
Negotiated Enclave ends the command failures, Local Revolt and Failed Rule the actor holds, and Return from the Crisis ends every failure form it holds, including the overlay's economy failures (`random_terror_focus_end_failure_forms`).
The terminal transition (`random_terror_mark_final_actor`) removes every slot and failure form, International Mandate included, before the three terminal spirits.
Ambiguous Light adds only the terminal spirits the final command does not hold yet and raises one final formation (`random_terror_focus_reward_ambiguous_light`).

`common/ai_strategy/031_random_terror_ai_strategy.txt` steers live actors only.
At war, an actor weights units and force concentration toward its own parent, which carries `random_terror_parent_of_<actor tag>` from the moment the actor forms until its runtime is cleared, and pulls units away from fronts against non-neighbouring enemies.
Each carrier befriends and supports the other carriers while it is a live actor, unless Global Jihad setup kept it independent or it is in a leadership contest.

The actor focus tree is `random_terror_actor_focus_tree` in `common/national_focus/031_random_terror_focus.txt`.

Its 114 focuses cover opening survival, Shadow Council, War Directorate, Ideological Secretariat, captured economy, armed movement, network and diplomacy, expansion, crisis, Jihadist International, Final Jihad, and False Revelation routes.

Actor decisions are gated by route flags (`random_terror_route_<route>`): the starting profile sets one, and the route-choice focuses (Shadow Network Directorate, Field Command Board, Convene the Cadre, Accept the International Claim) add their own, so choosing a route in the tree opens that route's decision family alongside the profile's.
The header route line shows the route chosen in the tree before the starting profile.

Focuses whose reward changes the map, units, factions or decisions run one `random_terror_focus_reward_<name>` effect (in `031_random_terror_effects.txt` or `031_random_terror_focus_effects.txt`) hidden behind a plain custom tooltip, with amounts in the `random_terror_focus_reward` and `random_terror_unit` constants.
Every formation a focus or actor action raises goes through `random_terror_focus_raise_formation`, which gives the formation's rifles instead once the actor reaches `actor_division_cap`, and a militia marks its state for conversion only when it actually forms:

| Focus | Route | Reward |
| --- | --- | --- |
| Define Leadership | Opening | Political power and army experience; opens the three leadership routes. |
| Secure Forward Depots | Opening | Roads and, with a free slot, a fuel silo in a state facing the enemy or on the border, plus `forward_depot_fuel` fuel. |
| Relocate the Command | Opening | A fallback seat: bunkers on the key towns and anti-air in another held state, or anti-air over the seat. |
| Distribute the Cells | Shadow Council | Up to `cell_select_count` foreign cells, bordering ones first, are linked to the network and gain `cell_seed_activity` (`random_terror_focus_reach_foreign_cells`). |
| Foreign Cell Channels | Shadow Council | Links up to `cell_select_count` foreign cells and brings convoys. |
| Foreign Cell Support | Shadow Council | Up to `cell_select_count` already linked foreign cells gain `cell_support_activity`. |
| Command the Front | War Directorate | `random_terror_synchronized_offensive` for `synchronized_offensive_days`. |
| Prepare the Parent Offensive | War Directorate | Claims, links and `parent_offensive_activity` on every populated state of the parent or another enemy bordering the command. |
| Command the Armed Movement | War Directorate | One territorial brigade (`brigade_id`). |
| Open the Border Corridor | Smuggling | The external corridor, roads in a border state and `forward_depot_fuel` fuel. |
| Salvage the Rail Spur | Smuggling | A railway from the seat to a border state (`build_railway` through the command's own or allied land) and roads there. |
| Control the Market | Coerced Extraction | `market_infantry_equipment` rifles and `market_fuel` fuel, with the extraction's condemnation. |
| Secure the Fuel Stores | Coerced Extraction | `fuel_stores_fuel` fuel and, with a free slot, a fuel silo in the seat. |
| Identify the Sponsor | Foreign Sponsorship | A sponsor request (`chaosx.nr31.42`) to a country at peace that could back the command, a neighbour first (`random_terror_focus_request_sponsor`). |
| Map the Network | Network and Diplomacy | Military access to every live command at peace with the actor; AI commands open theirs in return. |
| Protect Safe Havens | Network and Diplomacy | Support equipment, and up to `protected_cell_count` threatened cells abroad go to ground. |
| Bargain with Rivals | Network and Diplomacy | Non-aggression pacts with every AI command at peace and outside the faction. |
| Merge the Enclaves | Network and Diplomacy | A merger offer (`chaosx.nr31.43`) to a weaker command at peace, a neighbour first (`random_terror_focus_offer_merger`); the other command decides. |
| A Common Front | Network and Diplomacy | Guarantees for every AI command at peace that is not independent. |
| Form the Confederation | Network and Diplomacy | A leading command also brings in every AI command at peace, outside any faction, not independent and not serving the Jihadist International. |
| Absorb a Compatible Enclave | Network and Diplomacy | A merger offer to a weaker command, a faction partner first. |
| Claim the Transport Hub | Expansion | A claim on a neighbouring state above `hub_infrastructure`, else any neighbour, and roads in the facing state. |
| Seize the Urban District | Expansion | A claim on a neighbouring enemy-held city above `urban_population_k`, else any enemy-held or foreign neighbour, pressed by `urban_seizure_activity`. |
| Prepare the State Offensive | Expansion | `random_terror_commit_state_offensive` on one neighbouring enemy-held state, and army experience. |
| Break the Parent Government | Expansion | The parent loses stability and war support, gains Terror Pressure, and its crisis states gain `parent_cell_activity`. |
| Join the Jihadist International | Jihadist International | A membership request (`chaosx.nr31.44`) to the jihadist command that leads the International, which decides; with no other leader the command founds the International or leads it in its own faction (`random_terror_focus_request_membership`). |
| Unify the Jihadist Cells | Jihadist International | Up to `cell_select_count` foreign cells are linked and gain `cell_seed_activity`. |
| Command the International | Jihadist International | One International column (`column_id`). |
| Prepare the Global Uprising | Jihadist International | Up to `cell_select_count` linked foreign cells gain `cell_support_activity`, and each government holding one gains `uprising_pressure_gain` Terror Pressure. |
| Open the Worldwide Uprising | Jihadist International | After Evolution V, one linked cell whose government meets the uprising pressure rises through `random_terror_launch_coordinated_uprising`, shared with Call a Coordinated Uprising; before that it prepares cells as above. |
| Lead the Final Jihad | Final Jihad | Takes the free network leadership and raises one final formation (`final_id`). |
| Contest the Final Claim | Final Jihad | Runs `random_terror_resolve_network_leadership_contest` against the jihadist leader, or takes a free leadership. |
| Deny the False Revelation | Final Jihad | Ends The Presence of the Entity and restores `revelation_denial_stability`. |
| Continuity Protocol | Shadow Council | Bunkers on the victory-point provinces of the seat; Relocate the Network stops costing Territorial Control. |
| Establish Political Offices | Ideological Secretariat | The seat becomes a core state; Build a Civil Administration opens to the command (`random_terror_focus_political_offices`). |
| Trace the Border Corridors | Expansion | Claims on every bordering crisis state the command does not own. |
| Open the Next Front | Expansion | One regular formation (`front_id`) in an owned state facing a claimed state, or its rifles at the division limit; the cells in that claimed state gain `next_front_activity`. |
| Break the Last Corridor | Expansion capstone | Every claimed state the command holds, except a national capital, transfers to it. |
| Forge the Seal | Jihadist International | Every state the command owns and holds becomes a core state. |
| Lead the Coordination Structure | Jihadist International | A free or leading command founds or keeps the Jihadist International, takes the free network leadership and brings in every free AI-run International command at peace with it except an independent command; a command serving elsewhere gets courier support equipment and convoys. |
| Challenge Rival Governments | Jihadist International | Every bordering crisis state of another government gains `rival_pressure_activity`, and the command gets one `topple_government` war goal against a neighbour it is not fighting, preferring one facing Armed Insurgency or Lost Local Control. |
| Synchronize the Columns | Jihadist International | The command and every actor fighting in its faction gain `random_terror_synchronized_offensive` (division attack and speed) for `synchronized_offensive_days`. |
| Secure the Capital Approach | Final Jihad | Claims on the capital state of every neighbouring enemy and one level of infrastructure in an owned state facing the enemy. |
| Fracture the Sky | Final Jihad | Every neighbouring enemy suffers `random_terror_sky_fracture_shock` (war support and stability) for `sky_fracture_days`. |

The two bunker focuses build on the victory-point provinces of their state (Fortify the Headquarters) or on its border provinces (Harden the Defensive Line), since bunkers are province buildings.

## Visual assets and wiring

The authoritative visual audit is `docs/plans/031_random_terror_plans/031_random_terror_visual_asset_audit.md`.

Base sprites are registered in `interface/031_random_terror.gfx` and the 114 focus shine sprites are registered in `interface/031_random_terror_shine.gfx`.

Focus icons live under `gfx/interface/goals/031_random_terror/` and use `GFX_goal_random_terror_*` plus exact `_shine` counterparts.

Idea icons live under `gfx/interface/ideas/031_random_terror/` and use `GFX_idea_random_terror_*`.

Decision and mission icons and the three category pictures live under `gfx/interface/decisions/031_random_terror/` and use `GFX_decision_random_terror_*`, `GFX_decision_mission_random_terror_*`, and the three consumed `GFX_decision_category_031_random_terror_*` sprites.

Six news pictures and sixteen accepted report pictures live under `gfx/event_pictures/031_random_terror/`.

`GetRandomTerrorIncidentReportPicture` selects baseline report art from the incident type preserved by the global wave, while evolution, diplomacy, terminal, and defeat events use fixed report consumers.

Portraits live under `gfx/leaders/031_random_terror/`.

The ten-frame entity sheet lives at `gfx/interface/animated/031_random_terror/false_revelation_entity_sheet.dds`, is registered as `GFX_Portrait_Random_Terror_Entity_Animated`, and is consumed by Evolution V in the shared Event Details portrait selector.

The explicit static fallback is `GFX_Portrait_Random_Terror_Entity_Static_Fallback`, consumed by the final actor character.

Four large two-frame faction emblems and four miniature emblems live under `gfx/interface/emblems/031_random_terror/` and are consumed by the regional coordination, network confederation, Jihadist International, and Final Command faction transactions.

Thirty-seven fictional cosmetic identities provide 111 normal, medium, and small TGA files under the standard `gfx/flags/` roots, alongside 24 base flag files for the eight carrier tags.

Deterministic ordinary, transnational, and jihadist cycles expose all active identities over carrier generations, while cleanup assigns all eight dormant identities and the terminal actor uses the unique final identity.

Achievement states live directly under the engine-facing `gfx/achievements/` root as twelve colored, twelve grey, and twelve not-eligible DDS files whose basenames match their achievement IDs.

The Terror Activity map mode (`random_terror_state_map_mode` in `common/map_modes/031_random_terror_map_mode.txt`) colours each state by its activity stage, thickens its border with each stage, pulses the viewer's priority crisis state and mission or emergency subjects, and shows a delayed tooltip with the stage, the viewer's mission there and the broad next risk through `GetRandomTerrorStateMapModeDetail`; it never shows hidden readiness.
Its buttons `GFX_mapmode_buttons_selected_small_random_terror_state_map_mode` and `GFX_mapmode_buttons_deselected_small_random_terror_state_map_mode` are registered in `interface/031_random_terror.gfx` and point at `gfx/interface/mapmode/custom/random_terror_state_map_mode_selected.dds` and `_deselected.dds`, 20x18 one-level BGRA files matching the custom map mode button family (cream subject inside the family's shared one-pixel frame when selected, grey subject without frame when deselected).
The subject is a lit round bomb generated with native alpha through the ChatGPT image tool (prompt: a single interface icon on a fully transparent background, a classic round black-powder bomb with a short curved fuse and a small spark, bold flat silhouette in pale parchment cream with darker tan shading and a thin dark outline, no text, frame, border or background), then cropped to its alpha bounds, resized with premultiplied Lanczos to 15x16, mapped onto the family's cream and grey ramps and given the frame copied from the existing famine button.
The native-alpha source, processed PNGs and native and family contact sheet are kept under `docs/plans/031_random_terror_plans/evidence/map_mode_buttons_20261004/`; both DDS files decode back to their processed PNGs exactly.

## Achievement coverage

The single root registry in `common/achievements/chaos_redux_achievements.txt` exposes the twelve accepted Event 031 IDs below.

| Achievement ID | Persistent proof flag | Visibility | Runtime icon aliases |
| --- | --- | --- | --- |
| `031_no_second_blast` | `random_terror_achievement_no_second_blast` | Visible | `GFX_achievement_031_no_second_blast[_grey|_not_eligible]` |
| `031_the_long_watch` | `random_terror_achievement_the_long_watch` | Visible | `GFX_achievement_031_the_long_watch[_grey|_not_eligible]` |
| `031_the_city_still_stands` | `random_terror_achievement_the_city_still_stands` | Visible | `GFX_achievement_031_the_city_still_stands[_grey|_not_eligible]` |
| `031_cut_every_route` | `random_terror_achievement_cut_every_route` | Visible | `GFX_achievement_031_cut_every_route[_grey|_not_eligible]` |
| `031_the_false_claim_rejected` | `random_terror_achievement_false_claim_rejected` | Visible | `GFX_achievement_031_the_false_claim_rejected[_grey|_not_eligible]` |
| `031_no_collective_punishment` | `random_terror_achievement_no_collective_punishment` | Visible | `GFX_achievement_031_no_collective_punishment[_grey|_not_eligible]` |
| `031_enemy_of_my_enemy` | `random_terror_achievement_enemy_of_my_enemy` | Visible | `GFX_achievement_031_enemy_of_my_enemy[_grey|_not_eligible]` |
| `031_fracture_from_within` | `random_terror_achievement_fracture_from_within` | Hidden | `GFX_achievement_031_fracture_from_within[_grey|_not_eligible]` |
| `031_maximum_survivor` | `random_terror_achievement_maximum_survivor` | Visible | `GFX_achievement_031_maximum_survivor[_grey|_not_eligible]` |
| `031_false_revelation_denied` | `random_terror_achievement_false_revelation_denied` | Hidden | `GFX_achievement_031_false_revelation_denied[_grey|_not_eligible]` |
| `031_victims_before_victory` | `random_terror_achievement_victims_before_victory` | Visible | `GFX_achievement_031_victims_before_victory[_grey|_not_eligible]` |
| `031_war_without_a_capital` | `random_terror_achievement_war_without_a_capital` | Hidden | `GFX_achievement_031_war_without_a_capital[_grey|_not_eligible]` |

Completion predicates live in `common/scripted_triggers/031_random_terror_triggers.txt` and read proof flags produced by `common/scripted_effects/031_random_terror_achievement_effects.txt`.

The existing `on_daily` country pass calls `random_terror_achievement_daily_tick` only for Event 031 affected countries, actors, or initialized ledgers, so historical counters survive ordinary save and reload without adding a second world iteration.

Event 031 thresholds use the existing `random_terror_tuning` script constants, including the 180-day crisis window, pressure gates, legitimacy gates, corridor count, route stage size, movement duration, capital recovery window, and major-loss threshold.

The Network Authority text icon lives under `gfx/texticons/031_random_terror/`.

Two super-event pictures live under `gfx/super_events/031_random_terror/`, are registered in `interface/chaosx_super_events.gfx`, and use a public-domain or licensed WAV package played through the shared settings-aware super-event audio helper.

## Validation surfaces

The current visual inventory contains 444 runtime files and is recorded row by row in `docs/plans/031_random_terror_plans/031_random_terror_visual_asset_inventory.md`.

The complete event remains incomplete.

Nine portrait identities have history recruitment and reachable role consumers, including the gated entity and human Final Command Council.
Thirty-six additional identities have roleless definitions and a durable source archive, with recruitment, selection and recycling still open.
Original per-image prompt records and two current source-to-DDS equality records remain missing.
The capital-defense mission icon uses the reviewed native-alpha edit, with its inherited background-removal procedural gap resolved.
The full achievement audit retains player-identity observation limits, and numerical probability comparison and final subsystem audits remain unresolved.

The bounded multi-country wave repair is implemented in commit `b10e6a30292a51d09104aa1c120ab9843be6db25`, with source and acceptance evidence in `docs/plans/031_random_terror_plans/subagent_handoffs/031_multi_country_wave_scope_repair_20261003.md`.
Candidate-state controller checks use the candidate's PREV scope, owned-and-controlled draws use intrinsic state eligibility, and action targets retain their explicit ROOT contract.
The mapped callers initialize temporary outputs and pool storage, and automatic reservations follow successful incident application.
The one-firing pacing path, raw ticket curve, provider definitions, cap, attempt counts and two-day reservation remain unchanged.
The named wave baseline and comparison handoffs preserve the unchanged 17-case fixture, with 600-second failures and no numerical artifact.
The narrower shared-curve comparison is still unreturned in the handoff, so normalized probabilities, complete provider pools and native execution remain unresolved.
The newer mission audit in `docs/plans/031_random_terror_plans/subagent_handoffs/031_mission_owner_and_progress_contract_20261003.md` identifies cross-country consumption and cleanup of all eight generic mission subjects, owner-local recovery performing global cleanup, and shared-slot activation of the wrong mission family.
Five success predicates lack an independently reachable progress producer, while the hostage slot blocks its only current progress action and its accepted partial outcome is missing.
Mission receiver isolation is implemented in `38fd9b9da337f647f91a804628a24d3216075cb6`, with receiver-keyed subjects, family locks, guarded callbacks and exact-state descriptions.
Restoration reserves its slot before invoking its helper, recovery waits for active missions to resolve, and only successful timed restoration records completed civil authority for the achievement check.
The independent source review found no receiver-isolation defect, while the same-fixture numerical comparison remains blocked by archived-source recognition.
Mission progress and outcome implementation remains incomplete.
Foreign-owned controlled targets, external retake targets and controller-owned hostage/uprising missions remain part of the accepted design.
The decision audit also retains split actor-control values, incomplete click-time affordability and exact-balance handling, missing cost companions, excessive target-row fan-out and actor operations that record receipts without performing the promised unit changes.
The carrier audit identifies undeployed-carrier false-negative gates, occupied-tag reuse, stage-blind capacity counting, Maximum/map preflight gaps, weak geography constraints and unresolved force/research sources.
The mapped accepted contracts remain implementation work under the user's instruction to complete the accepted specs and visual audit.
Audit suggestions and proposed regression fixtures remain recommendations until the parent reviews them, and no gameplay simplification is approved.
Carrier, force, technology, economy, exact-cost, AI and full terminal-atomicity coverage remain open.

Detected daily control changes disqualify only the changed country, preserving unrelated player countries' eligibility.

Same-day round trips and swaps between already-human countries remain unresolved because the daily country marker does not identify individual clients.

The Event 31 CXT daily hook registers newly discovered content and marks it pending for manual application.

The compact scenario-list label is `#016`, while the stable Global Jihad catalog identifier is SCN-016.
The existing adjacent `#018` scenario label and SCN-018 identifier are preserved.

Capital-dependent achievement tracking stores each government's exact original state and separately records the capital at Maximum scenario confirmation.

Retaking and restoration proof requires a matching country-owned identity, current control is checked at completion, and repeated loss cannot extend the recovery deadline.

The source repair and validation limits are recorded in `docs/plans/031_random_terror_plans/subagent_handoffs/031_achievement_capital_identity_repair_20261003.md`.

The workbook mirrors Event 31 localisation and contains Global Jihad as SCN-016, with Event 31 classified as `To Be Reworked` and Global Jihad as `Needs Testing`.

No Internal Fracture cluster is registered by this implementation.

The achievement active-state count credits the government owning the counted states, including when the global wave's event root is a different country.

The exact repair and its validation limits are recorded in `docs/plans/031_random_terror_plans/subagent_handoffs/031_achievement_count_scope_repair_20261003.md`.

Measured casualty receipts are implemented in commit `bbb2ba6f90ec75462cb94f7274122c52df4abcb3` under the accepted civilian-loss and achievement contracts.
`random_terror_apply_exact_state_loss` initializes both helper outputs, reads measured applied loss for the major-loss receipt and records that same measured amount rather than the requested loss.
The strict major-loss threshold remains greater than 400 people, with the 0/300/400/450 boundary model and full validation limits recorded in `docs/plans/031_random_terror_plans/subagent_handoffs/031_measured_casualty_receipt_repair_20261003.md`.
The current checkpoint lists eleven bounded repair commits and keeps full Event 31 validation open.

The historical HOI4 focus route resolves one 114-focus tree with 114 titles, zero connector crossings and zero same-row spacing violations.
Its structural render is 8,752 by 3,136.
The post-fix decoded-icon raster route timed out after 180 seconds, so the earlier decoded raster remains icon evidence and does not prove post-fix topology.

The event inspector accepts the Event 31 root and returns a partial artifact without an Event 31-specific blocker.

The installed event renderer accepted an exact namespace selector but expanded into a full-workspace render and did not complete after more than six minutes, so namespace-scoped renderer evidence remains an exact tool-route blocker rather than being replaced by source-only proof.

The historical mandatory GUI inspector and renderer completed for `chaosx_scenarios_window` with Event 31 selected, Random Pattern and Maximum at 1920x1080 and UI scale 1.
The inspector reported no missing fields.
Shared-window overlap and alignment findings remain open.
Current narrowed event/reference requests and terminal-role probability comparisons timed out after 600 seconds, with exact limitations in the MCP ledger and specialist handoffs.

## Future extensions

Optional future work can add more fictional incident compositions or additional non-weighted cosmetic identities only when they receive exact consumers, complete source and rights evidence, and the same native-scale audit.

Optional work must not add real extremist identities or symbols, sacred hostile branding, a dedicated Event 31 GUI, a custom unit, an Event 19 provider, a 3D model, a custom unit sound, or a bespoke counter.
