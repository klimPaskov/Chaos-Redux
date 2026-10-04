# Event 028 agent decisions, 2026-10-04

Disposition: accepted and implemented unless an entry says otherwise.
Acceptance basis: the user granted the implementing agent full design authority for Event 028 and asked for the recommended, spec-consistent option to be recorded here instead of asking for input.
Each entry names the spec basis and the commit or source surface that implements it.

## Crater actions

### Supplied crater garrison

Decision: a supplied garrison is at least one of the acting country's divisions in the crater state, or in an ordinary neighbouring state the actor controls that has a rail connection from the actor's current capital.
Basis: Part 6 asks for "supplied divisions in or adjacent to the crater".
The installed `triggers_documentation.md` has no trigger that reads a division's supply status, and neither COMBATANT nor state scopes expose one, so the capital rail link is the closest supported test.
The check follows `asteroid_incoming_state_has_capital_rail_route` and lives in `asteroid_incoming_crater_has_supplied_garrison` (`common/scripted_triggers/028_asteroid_incoming_crater_triggers.txt`).
The same garrison rule gates Secure the Crater Perimeter and Prepare a Crater Offensive.

### Perimeter ownership

Decision: a secured perimeter belongs to the country that secured it and lapses when another country takes control of the crater.
A new controller must secure the site again before it can survey it, while the survey record and its one-use research bonus stay on the state permanently, so changing controllers cannot farm the survey.
Basis: Part 6 exploit control "crater security actions cannot be farmed through rapid controller switching".

### Fortifying access states

Decision: Fortify Crater Access improves at most `asteroid_incoming_crater.access_state_limit` (two) neighbouring ordinary states the actor controls.
Each gains one infrastructure level when below the infrastructure cap and one fort level in every province whose fort is below the fort cap.
Each access state can be fortified once across all crater sites.
The old every-neighbour infrastructure loop is removed.
Basis: Part 6 "builds or repairs defenses and supply in neighboring normal states; the crater itself remains unusable".
Forts are province buildings, so the construction uses the province selector shown in the wiki `add_building_construction` row and vanilla focus precedents.

### Rival actions

Decision: reconnaissance grants army intelligence on the crater's controller, disruption applies a timed local-supply modifier to up to two hostile-held access states, and the offensive plan applies a timed attacker-only attack modifier to the actor's battles in the crater state.
Rival actions no longer require the actor to control the crater, which made them impossible before.
Basis: Part 6 "gather intelligence, affect local supply, or guide AI strategy; no free war goals or ownership transfers".

### Paid costs are shown as costs

Decision: command power for the security and survey actions and manpower for the fortification action appear in the cost text with the other paid costs, instead of as separate requirement lines.
Every crater action stays within four spendable cost types.
Basis: Part 6 "a requirement is not a hidden fifth cost" and "no action may have more than four spendable cost types".

### Crater competition alongside dust protection

Decision: crater actions open once the country's own emergency and reconstruction actions are closed, even while global dust remains.
Global dust can last for more than a year, and holding crater competition behind it hid the Extraordinary Minerals actions for most wars.
Basis: Part 6 Phase 4 is "visible only when Extraordinary Minerals is active and the country controls, borders, or is at war over a crater site" and does not wait for Phase 3 to end.
No `ai_will_do` block changed; only decision visibility widened.

## Recovery missions

### Missions run alongside projects

Decision: a pending paid project still blocks a second project in the same country, but an active mission no longer blocks projects.
Each mission keeps its own state pointers and hold date, and no more than `asteroid_incoming_recovery.active_mission_limit` (two) missions run at once.
Basis: Part 6 asks each phase to show three or four primary actions and no more than two active missions.
With one shared reservation, every project was followed by a mission of 120 to 365 days that froze the whole category, so a country with several ring states could not leave the emergency phase before the recovery deadline, and Restore the Outer Ring could never clear major-ring damage it was not allowed to work on.
No `ai_will_do` block changed.

### Missions are for player governments

Decision: completed projects start missions only for countries with `is_ai = no`.
AI countries keep every project effect but receive no mission contract.
Basis: mission success depends on ordinary construction of infrastructure, railway and factories in named states, which the AI cannot plan toward; AI countries would otherwise collect failure consequences they cannot avoid.
The network and outer-ring flags feed only a player achievement, so AI play loses nothing it could use.

### Hold period and grace window

Decision: each mission's objective can be met from `timeout - asteroid_incoming_recovery.mission_grace_days` (45 days), and the mission completes as soon as its conditions hold after that day.
Basis: the completion day and the native timeout used to fall on the same day, so success was unreachable.
45 days keeps at least one monthly recovery review inside the window for the regional economy measurement.

### Repair targets from the pre-impact snapshot

Decision: mission repair targets are `asteroid_incoming_recovery.mission_repair_share` (60 percent) of each state's pre-impact infrastructure, railway, supply hubs, civilian factories and military factories, rounded to whole levels.
The fixed floors (infrastructure above 3, railway above 1, a supply node, one factory) are removed from the missions.
Basis: a fixed floor asked states that never had that level or building to exceed it, so many missions were impossible, and Part 6 asks for named states and exact public thresholds tied to the damage.
The AI preparedness and target weights still read `mission_railway_floor` and `mission_supply_node_floor`, which keep their values.

### Rail links that existed before the impact

Decision: rail objectives ask only for links that existed before the impact, recorded per footprint state from its controller's capital before any damage or capital move.
Basis: an island state or a state without a railway can never reach the capital by rail, and "reconnect" means restoring links that were cut.

### Stabilize the Damaged Zone

Decision: the mission captures, at activation, the two damaged states the country holds that still miss their targets, ranked by impact profile first and then by the infrastructure and railway gap.
A country with only one such state gets a one-state mission.
Success closes both local emergencies so reconstruction can begin there.
Basis: Part 6 "repair named infrastructure, railway, or supply thresholds in its two worst affected states" and "success should move the country into reconstruction earlier".
The old requirement that catastrophic and heavy-fragment damage be absent is removed, because those modifiers last 270 to 720 days and could not be cleared while the mission ran.

### Reconnect the National Network

Decision: every damaged state the country holds that was linked before the impact must be linked to the current capital, every damaged state must meet its infrastructure target, and the largest industrial state that is or was on the network (captured at activation) must be linked to the capital.
Success closes the emergency work in every damaged state the country holds.
Basis: Part 6 "restore defined infrastructure and railway links between the capital, major industry, and damaged states" and "closes obsolete emergency decisions".

### Restore the Outer Ring

Decision: no held affected state may keep the Outer Shock Zone or Light Fragment Damage, and the Ring 2 burden is defined per state: every held state of the major impact ring must meet its infrastructure and both factory targets.
Basis: Part 6 "remove all timed Ring 3 and light fragment modifiers and reduce Ring 2 burden below a defined threshold".
A count of states still carrying the 405-day major-impact modifier could not be reduced by construction during the mission; repair targets can.

### Rebuild the Regional Economy

Decision: the monthly recovery review sums current factories, infrastructure and railway across the surviving damaged states the country holds and compares each total with the same pre-impact total; each must reach `asteroid_incoming_recovery.regional_capacity_share` (75 percent).
Basis: Part 6 "restore a meaningful share of surviving pre-impact industrial and logistical capacity outside the permanent crater".

### Cancellation carries no penalty

Decision: a mission whose named state leaves the country's control ends without any outcome.
Only an expired mission applies failure consequences.
Basis: Part 6 "missions cancel or transfer cleanly when the country ceases to control the required route".

## Local emergencies and mission failure

### Natural emergency closure

Decision: emergency projects require a live local emergency (a rescue burden or the catastrophic, major, fragment-centre or heavy-fragment modifier).
States with only outer-shock or light-fragment damage start with their emergency resolved, and the monthly recovery pass closes every other listed emergency once its burdens have ended.
Basis: Part 6 phases urgent work before reconstruction; reconstruction actions required the resolved flag, which only a project could set, so states whose damage expired naturally never reached reconstruction.

### Failure consequences

Decision: an expired mission, once per named state and day, records a rescue-failure Deaths entry (1 percent of the state's population, 2 percent in the catastrophic ring or at a fragment centre, at most 25,000 people), brings back the state's ended impact-zone damage for 90 days, and applies the existing failure-pressure modifier and national recovery burden.
Damage still running keeps its own timer, because the remaining days of a dynamic modifier cannot be read and re-adding it could shorten it.
Emergency-class damage reopens the local emergency, so "failure keeps the emergency phase open" (Part 6).
The temporary repair-cost increase is applied through the recovery cost quote.
Basis: Part 6 failure lists "extend the state recovery modifier", "a bounded rescue-period death entry", and "raises future repair costs for a limited period".

## Evolutions at impact

### Thresholds from the opening, toggles at impact (F04)

Decision: Global Fragmentation applies at impact only when the opening snapshot recorded its Chaos threshold and `has_disabled_current_evolution` is false for event 28, type 2801, stage 1.
Extraordinary Minerals activates only when its opening snapshot exists, type 2802 stage 1 is not disabled, and at least one fragment applied.
The Chaos threshold is not re-checked live at impact; the fragment-site count still follows the current Chaos value.
Basis: Part 5 and the event skill's rule that an evolution's enable state is read where it applies; the threshold is part of what the opening announced.
No AI weight changed.

### Near-miss eligibility (F14)

Decision: "eligible" for the near-miss achievement means the Chaos threshold is met and both evolution toggles are enabled; there is no geographic check that two separated fragment centres would exist.
The existing award logic stands, so no probability surface changes.
Basis: Part 10 Achievement 1 lists only the threshold, the enabled and eligible evolutions, and the miss.

## Nuclear separation (F18)

Decision: `launch_nuke` stays the accepted impact map visual, and its native unit and building effects are part of the impact.
Before each call the struck state receives the timed flag `asteroid_incoming_visual_strike_state` for `asteroid_incoming_runtime.visual_strike_marker_days` (seven days), and the global `asteroid_incoming_visual_strike_active` flag is kept around the call.
Every mod `on_nuke_drop` consumer that reacts to a nuclear strike skips a state carrying the marker: the Chaos Meter nuclear-use entry, the humanitarian corridor, migration evacuation reports and famine and migration pressure, the Event 016 Kruger achievement, and Event 023's delivery confirmation.
Basis: Part 3 makes the map visual the only nuclear-adjacent surface; a state-scoped marker still works when the callback does not fire synchronously inside `launch_nuke`.
Native `on_nuke_drop` timing and the vanilla consequences of the visual remain a live-game check.
The untracked Event 042 on_nuke_drop hook (`common/on_actions/042_equipment_from_heavens_on_actions.txt`) belongs to another in-progress package and needs the same one-line marker check from its owner.

## Late capital loss (F02)

Decision: the impact always proceeds at its locked coordinates and is never redirected or cancelled because of the capital.
When the existing settled, fully controlled backup selection finds nothing, the relocation tries, in order, any owned state the country controls, any owned state even if occupied, then any state it controls, keeping the best backup score within each tier and then the lowest state id.
If no state qualifies, or the engine refuses the move, the capital stays at the crater, the country receives the full Government Dislocation for the capital duration whatever its preparation, and Government Beyond the Crater stays closed because it requires a relocation.
The failure flags are consumed after the preparedness aftermath, and the impact report and Event Details state the outcome.
Basis: Part 2 fixes the coordinates and says peace, annexation and civil war never move the impact; this closes the resume packet's open capital question.
The proposed `.4` rollback journal and publication-order changes are rejected as unneeded machinery: validity is checked before the physical phase, and the reentry guards already stop a duplicate resolution.

## Main crater clearance

Decision: after the measured building receipt, the main centre alone zeroes every province naval base, land fort and coastal fort with `set_building_level` over all provinces, and wrecks its remaining supply hubs and railways with `damage_building` and a full negative repair-speed modifier, mirroring `death_strip_current_state_buildings` in Event 010.
Only levels that actually disappear are added once to the logistics (naval bases, supply hubs, railways) or strategic (forts) receipts.
Ring and fragment profiles keep their fractional state-aggregate removal.
New and queued construction in the crater stops through the existing wasteland category and the `asteroid_incoming_main_crater` modifier (no building slots and minus 100 percent construction speed), so no separate construction purge is added.
Whether province buildings, wrecked railways and queued projects behave this way in the running game remains a live check.

## Recovery prices and transport dispersal (F08)

### One stored quote per affected state

Decision: each affected non-crater state stores one price quote, and the cost text, `custom_cost_trigger`, reserve check and payment all read it.
The multiplier is one plus 0.01 per impact-profile point plus 0.0005 per thousand people the state lost (at most 0.50), times 1.25 while the controller carries a mission-failure surcharge, bounded between 1.00 and 2.50.
Quotes are written at impact, refreshed monthly and refreshed at once when a country takes the surcharge, so a controller change or an expired surcharge reaches the price within a month while the displayed price always equals the debit.
The cost checks compare the engine's `manpower_k`, `fuel_k` and `num_equipment@` values with the stored quote through `check_variable`, so no `meta_trigger` is needed.
Basis: Part 6 asks for costs that scale with affected population and damage, with no more than four spendable cost types and the reserve floors kept.

### Dust-protection prices

Decision: the three dust-protection projects read one global quote scaled by the dust stage (1.00 residual haze, 1.25 global veil, 1.50 impact winter, 1.75 severe impact winter).
Basis: Part 6 lists the dust stage as a cost input for national protection.

### Mission-failure surcharge

Decision: an expired mission raises the failing country's repair prices by 25 percent for 180 days through a timed country flag that the quote reads; the cost text marks raised prices.
Basis: Part 6 "raises future repair costs for a limited period".

### Transport dispersal

Decision: at impact the original target loses 2 percent of its trains, trucks and fuel per main-footprint state it controls, up to 20 percent; Disperse Transport keeps 60 percent of that loss, and the impact report lists both amounts.
The fixed equipment grant is removed.
Basis: Part 2 and Part 6 describe dispersal as preserving reserves that the impact would otherwise destroy; a grant with nothing at risk preserved nothing.
No `ai_will_do` or `ai_chance` value changed, so no probability comparison is required; affordability gates now follow the scaled prices.

## Default queue

Decision: Event 028 joins `event_log_event_is_reworked_default_enabled`, so new campaigns include it in the normal event queue.
Basis: the user wants every event from 1 to 40 playable, and every priority-1 and priority-2 source item from the 2026-10-04 remaining-work list is committed; what remains is live-game verification.

## Review round 1 corrections

### Crater access disruption penalises the enemy

Decision: Disrupt Extraction Routes applies `local_supplies_for_controller` at `asteroid_incoming_crater.access_supply_disruption` (minus 20 percent), scoped to the hostile controller of each disrupted access state.
Basis: vanilla uses a positive `local_supply_impact_factor` as a penalty (`dam_blown_modifier`, `yellow_river_blown`) and a negative `local_supplies_for_controller` as a penalty (`ITA_mafia_on_the_rise`), so the earlier negative supply-impact value eased the enemy's supply instead of disrupting it.
Part 6 asks rival actions to "affect local supply" against the crater holder.

### Stabilize ranks by impact profile first

Decision: the Stabilize the Damaged Zone severity multiplies the impact profile by `asteroid_incoming_recovery.stabilize_profile_rank_weight` (100) before adding the infrastructure and railway gap.
Basis: profiles step by 10 while the combined gap can reach 10 or more, so the plain sum could rank a lighter ring above a heavier one, contrary to the recorded "impact profile first" rule.

## Review round 2 corrections

### One stored result for the target board

Decision: the opening board (`chaosx.nr28.1`) and the reopened board (`chaosx.nr28.8`) read one global flag, `asteroid_incoming_board_ready`, for both their description and their options.
The dispatcher sets it when its board validates, `chaosx.nr28.1` rebuilds its still-unseen board once in `immediate` when nothing is locked and the pairs are missing or invalid, and `chaosx.nr28.8` re-validates the saved pairs without rerolling through `asteroid_incoming_refresh_board_ready`.
The single description key resolves through `GetAsteroidIncomingOpeningDesc` at display time, options a to d require the flag and the N/A option requires its absence.
The target-pool reset, the lock, the miss, the fail-closed close and both cleanup helpers clear it, and the N/A close leaves a locked trajectory untouched so a duplicate opening popup cannot end it early.
`chaosx.nr28.2` keeps its live pair re-check and its path for a coordinate that is no longer valid.
Basis: Part 2 fail-closed target rules and the routed live defect in which the board described no trajectory while offering three; description and option triggers are evaluated at different moments, including when a pending popup is restored from a save, so they cannot each test the live pairs.
No `ai_chance` value changed.
Restoring a pending board from a save is a needs-live-game check.

### A failed mission keeps its full burden for the stated window

Decision: an expired mission removes the recovery legacy and the normal burden, applies the full `asteroid_incoming_recovery_burden` for `asteroid_incoming_recovery.mission_failure_pressure_days` (90) and sets the timed country flag `asteroid_incoming_recovery_failure_pressure` for the same days, both read from a temporary variable.
While the flag runs, the monthly national recovery pass leaves the idea alone and queues no closeout report, and a mission success in that window records the legacy without swapping the idea; the normal legacy, burden or closeout logic resumes on the first monthly pass after the window.
A second failure inside the window restarts both timers.
The failure tooltip says the full burden returns for that many days and sets aside any recovery legacy until then.
The never-read state counter `asteroid_incoming_recovery_actions_completed` is removed.
Basis: Part 6 failure consequences ask for a real temporary escalation, and the tooltip already promised the window; the monthly pass used to replace the burden with the legacy or an untimed burden within a month.
No `ai_will_do` or `ai_chance` value changed.

### Minerals eligibility follows the fragmentation snapshot

Decision: the opening snapshot sets `asteroid_incoming_evolution_ii_eligible` only when `asteroid_incoming_evolution_i_eligible` was set in the same snapshot, so the board, the confirmation and the near-miss check never announce Extraordinary Minerals while Global Fragmentation is disabled or below its threshold.
Basis: the catalog evolution text says Extraordinary Minerals requires Global Fragmentation, and the impact already needs an applied fragment before minerals can activate.
The AI factors `strike_mineral_holder_factor` and `miss_mineral_holder_add` read the chooser's existing crater holdings, not this flag, so no weight changes.

### Named AI stability threshold

Decision: the Command Continuity weight on `chaosx.nr28.3` reads `asteroid_incoming_ai.preparedness_unstable_stability_threshold` (0.45) instead of a literal.
Basis: the repository rule that tuning thresholds live in constants; the value is unchanged, so no probability comparison is needed.

## Open acceptance points closed in round 2

### Historical target identity (F06)

Decision: Event Details and the history rows keep naming the target through the persistent `asteroid_incoming_original_target_country` and `asteroid_incoming_original_target_state` pointers, the impact news and super-event read the `asteroid_incoming_super_event_target_*` pointers saved from the locked pair, and no separate name or flag snapshot is stored.
`GetName` and `GetFlag` still resolve for a tag that no longer exists, so a target annexed inside the two-day window is shown as the former country.
A cosmetic rename inside the two-day window shows the current name, which is accepted.
Basis: Part 2 freezes the target country and state, and no engine-supported effect stores a name or flag string; annexation is the realistic change within two days.
The display of an annexed target's name and flag is a needs-live-game check.

### Rail objectives across the main crater

Decision: rail objectives keep the links recorded before the impact, and a main crater that sat on a state's only rail route to the capital is accepted.
The crater's railways are wrecked beyond repair, and players can build detours through ordinary neighbouring states to restore the link.
Basis: Part 6 asks missions to restore links that the impact cut, and Part 3 keeps the crater itself unusable.
Whether a detour is buildable for a specific map position is a needs-live-game check.

### Secondary-disaster order

Decision: secondary-disaster slots keep filling in state-id order, because `asteroid_incoming_process_footprint` applies profiles through `every_state` and only catastrophic-ring states and fragment centres in a disaster-prone zone can call one, up to `asteroid_incoming_runtime.secondary_disaster_maximum`.
Basis: the spec sets a slot limit but no ring priority, so any stable order meets it, and the state-id order is deterministic across saves.

### Event 042 nuclear-drop hook

Decision: the missing `asteroid_incoming_visual_strike_state` guard in `common/on_actions/042_equipment_from_heavens_on_actions.txt` is a cross-owner dependency on the Event 042 package, not Event 028 work.
That file is untracked and belongs to another in-progress owner; Event 028 keeps the state marker and global flag that the guard needs.
Basis: the shared-tree ownership rule and the nuclear-separation decision above.

## Review round 3 corrections

### Timed flags take literal days

Decision: every Event 028 timed flag is built inside a `meta_effect` whose text receives integer literals from `[?temp|.0]`: the impact super-event flag (`super_event_visible`, days from `asteroid_incoming_runtime.super_event_visible_days` and value from `asteroid_incoming_event.super_event_id`), the struck-state map-visual marker (`asteroid_incoming_mark_visual_strike_state`, from `asteroid_incoming_runtime.visual_strike_marker_days`), the mission-failure repair surcharge (`asteroid_incoming_repair_costs_raised`, from `asteroid_incoming_cost.failure_surcharge_days`) and the national failure window (`asteroid_incoming_recovery_failure_pressure`, from `asteroid_incoming_recovery.mission_failure_pressure_days`).
The state failure-pressure modifier reads its duration from a temporary variable instead of a `constant:` token.
Basis: installed `common/scripted_effects/SOV_scripted_effects.txt` notes that a timed flag's days do not read variables, and Event 5 and Event 23 use the same literal-injection pattern; a flag that ignored its duration could leave repair prices raised and the national recovery idea frozen for the rest of the campaign, or keep a struck state out of later nuclear consequences.
Values are unchanged; flag expiry is a needs-live-game check.

### The crater perimeter lapses with control

Decision: the perimeter modifier's `enable` and `remove_trigger` name the crater state through `ROOT`, as the vanilla scoped state modifiers `CHI_bog_defensive_modifier` and `CZE_sudetenland_paramilitaries_modifier` do, because the modifier is added with `scope` set to the securing country.
`asteroid_incoming_on_state_control_changed` clears the perimeter flag and holder id once another country controls the site, so a former holder that retakes it must secure it again and regains the modifier, as the perimeter-ownership decision above states.
The survey record and its one-use research bonus stay on the state.
Basis: the perimeter-ownership decision; before this, a former holder that retook the site kept a held perimeter without its modifier and could not secure it again.

### Dust-protection modifier name

Decision: `asteroid_incoming_national_dust_protection` has a display name, so modifier breakdowns no longer show its raw key.
