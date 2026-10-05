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
Superseded in part: unit damage in the footprint is now owned by "Units in the footprint take location-based damage" (round 3 lead items); the visual's own province damage still applies on top.
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

## Takeover round 2 (2026-10-05)

### Achievement tracking runs without the Chaos Meter

Decision: `asteroid_incoming_update_achievements` is called from the first global-host `on_monthly` block in `common/on_actions/chaosx_on_actions_chaos_meter.txt`, next to `asteroid_incoming_monthly_dust_update`, and no longer from the Chaos Meter decay block.
Inside the updater, the original-target annexation check still runs whenever the target pointer exists, while hold tracking moves into `asteroid_incoming_update_player_achievement_progress`, which runs only when `asteroid_incoming_impact_recorded` is set without `asteroid_incoming_miss_recorded` and visits only existing human-controlled countries.
AI fragment counts stay current through `asteroid_incoming_refresh_mineral_control`, which every crater control change already calls.
Basis: Part 10 makes three achievements depend on this updater, and nothing else sets their flags, so the Chaos Meter setting must not decide whether they are attainable; a campaign without an impact should not carry Event 028 variables on every country.

### Collector of Fallen Stars and subjects

Decision: the Collector check no longer requires the player to be independent, and its tooltip says sites held by your subjects do not count.
Basis: Part 10 says only that subject control does not count; `any_controlled_state` and `asteroid_incoming_count_controlled_mineral_fragments` already count direct control only.

### The trajectory-locked notice names the target and date

Decision: at the lock, `global.asteroid_incoming_expected_impact_date` is the current date plus `asteroid_incoming_runtime.lock_duration_days`, converted with `chaosx_convert_days_to_date_offset`, and the `chaosx.nr28.4` resolver delay is injected from the same constant through `meta_effect` with an integer literal instead of a written `days = 2`.
`chaosx.news.30.d` names the original target state, its country, its continent and that date in plain text, and says nothing about fragments.
The date is cleared by `asteroid_incoming_resolve_miss`, `asteroid_incoming_fail_closed_transaction` and `asteroid_incoming_cleanup_finished_transaction`.
The preparedness event `chaosx.nr28.3` keeps its existing text, because a popup left open past the impact would read the cleared date.
Basis: Part 8 (Observer trajectory notice) and Part 7 (Observer information) require the notice to name the intended target and impact date, and a single constant keeps the announced day and the real delay equal.

### Crater AI strategy and peace value

Decision: crater AI uses two documented vanilla mechanisms instead of new script.
`asteroid_incoming_crater_fronts` (`common/ai_strategy/028_asteroid_incoming_ai_strategy.txt`) runs while Extraordinary Minerals is active, the country is at war and its surrender progress is at most 0.25, with `abort_when_not_enabled = yes`, and adds `front_unit_request` weight to fronts crossing the main crater (60) or a fragment site (25).
It adds no `front_control` order, so the normal attack and defence logic still decides whether an offensive happens, and the surrender guard keeps a collapsing country from pulling divisions toward a distant site.
`common/peace_conference/ai_peace/028_asteroid_incoming_ai_peace.txt` adds `take_states` desire when the negotiator bids for itself: 75 for the main crater and 30 for each fragment site, both below the vanilla `take_our_cores` desire of 100 and far below the -1000 influence cutoffs.
Values are file-scoped `@` constants because no script reads them.
`put_unit_buffers` was not used because it takes literal state ids and crater states are chosen at runtime.
Basis: Part 7 (Crater control and Peace behavior) and the acceptance line "Crater AI values sites without abandoning normal survival logic"; vanilla `CHI_bog_them_down_and_war_zones_concentrations` (CHI.txt:705-728) and the installed `common/peace_conference/ai_peace/_documentation.md` scope list.
Probability evidence: `hoi4_probability_inspect` with `adapter = ai_strategy_factor` returned INTERNAL_ERROR for a single-file source selector and rejected a one-name `candidatePool` as invalid arguments, so no baseline or `probability_compare` could be produced; the route has no adapter for `peace_ai_desires`. This is a recorded route gap; the review is source-only. The values are needs-live-game tuning checks.

### Recovery category header

Decision: the Asteroid Recovery category header keeps its dust and protection values and names the recovery burden the country carries now, in this order: burden extended after a failed mission (while `asteroid_incoming_recovery_failure_pressure` runs), recovery complete (after the closeout report), recovery burden (`asteroid_incoming_recovery_burden` idea), recovery legacy (the legacy idea or flag), active recovery (an affected country before the first monthly assessment), or no national recovery required.
While Extraordinary Minerals is active, a crater clause names whether the country directly controls the main crater (`any_controlled_state` with `asteroid_incoming_main_crater`) and its `asteroid_incoming_country_controlled_fragment_count` fragment sites, with singular and plural wording; the clause is empty otherwise.
Colour codes follow the header's existing label and yellow value pattern only.
Basis: Part 6 (Presentation choice) lists the national recovery burden for damaged countries and the controlled crater-site count under Extraordinary Minerals as header values.

## Takeover round 3 (2026-10-05)

### Achievement list names and descriptions

Decision: the five Event 028 achievements gain the native `<id>_NAME` and `<id>_DESC` keys, and both the description and the `<id>_tooltip` read the Chaos threshold, the Government Beyond the Crater deadline, the Collector site minimum and hold, and the Piercing hold from `asteroid_incoming_runtime` through `[?constant:...|0]`.
The tooltips no longer describe the hold as an "accepted control period".
Basis: the wiki Achievement modding Localization section (`paradox_wiki/Achievement modding - Hearts of Iron 4 Wiki.md`, lines 96-103) and the convention used by 400 of the 410 mod achievements.
Commit: 08cb48523.

### One target per state recovery action

Decision: each of the seven state-targeted recovery decisions lists only the highest-ranked state its country controls that is open for that action now.
The ranking is evaluated live in `target_trigger`, not refreshed on a schedule, so an action can never disappear while a valid state remains, and a used, resolved or lost state hands over to the next one on the following daily check.
Emergency ranking: active rescue burden, then the strongest `asteroid_incoming_state_profile`, then the larger current `state_population_k`.
Reconstruction ranking: the strongest profile, then the larger infrastructure plus railway gap against the pre-impact snapshot.
Ties fall back to the lower state id, so the choice is deterministic.
Each comparison reads and writes its own unscoped temporaries inside one scripted trigger, because the wiki Data structures page warns that temporaries set inside a scripted trigger may not survive outside it.
`visible`, `available`, costs, crater and dust decisions and every `ai_will_do` are unchanged.
Basis: Part 6 caps the visible actions (three or four in Phase 1, three in Phase 2), the acceptance line "Decision phases expose no more than the planned visible action cap", and "Prioritize the state with the largest expected preventable loss" for mobile hospitals; reconstruction mirrors the accepted Stabilize ranking.
Engine references: the wiki Decision modding section (target_trigger is checked daily with ROOT as the country and FROM as the target, lines 527-535; `any_controlled_state` checks every controlled state, lines 578-581), the wiki Triggers table (NOT is a NOR, line 341), and vanilla `common/decisions/AST.txt:149` for `FROM.state_population_k` in a state-targeted decision.
Probability evidence: one `hoi4_probability_inspect` call with `adapter = decision_ai_will_do`, the seven decision names as `candidatePool` and a single-file source selector returned "Invalid tool arguments"; no further attempt was made. The candidate pool shrinks from every valid state to one state per action and no weight changed, so this is a recorded route gap and the review is source-only. The live ranking display is a needs-live-game check.

### The Regional Economy legacy is lasting

Decision: a country with `asteroid_incoming_regional_economy_complete` keeps `asteroid_incoming_recovery_legacy` after its last local burden ends: the monthly `asteroid_incoming_refresh_national_recovery` re-adds it in the no-burden branch, and `chaosx.nr28.6` removes only the burden for that country while still removing the legacy for everyone else.
The closeout tooltip adds a clause that the legacy stays in force, and the category header shows "Lasting recovery legacy" before closeout and "Recovery complete, lasting legacy kept" after it.
The other four missions keep the temporary burden-to-legacy swap, and a failure window still removes the legacy until it ends, after which the monthly pass restores it.
`on_annex` clears the completion flag on the annexed country, so a later release does not bring the legacy back; idea removal before each re-add prevents duplicates.
Basis: Part 6 says Regional Economy success "grants a lasting but measured recovery legacy", and the shipped success tooltip promises "a lasting recovery legacy replaces the national burden"; Part 6 describes the other successes as replacing the national recovery idea with a lighter form.

### An impact resolves without its chooser

Decision: at the lock, the hidden resolver `chaosx.nr28.4` is queued on both the chooser and the locked target country with the same constant-driven delay.
Whichever fires first resolves the impact; the existing `impact_resolution_started`, `impact_recorded`, `transaction_resolved`, `miss_recorded` and `fail_closed_recorded` guards make the second a no-op, and no resolution helper reads ROOT (the history follow-up only uses ROOT as a scope for a temporary).
If both callbacks are lost, the monthly `asteroid_incoming_resolve_orphaned_transaction` watchdog, called from the ungated `asteroid_incoming_update_achievements`, sees a lock past `global.asteroid_incoming_lock_expires_day` with no resolution started, sets `asteroid_incoming_lock_overdue` and fires the resolver on the global host; `asteroid_incoming_locked_transaction_is_valid` accepts an overdue lock, and `asteroid_incoming_cleanup_finished_transaction` clears the flag.
The late strike happens on the watchdog's date rather than failing closed, because the trajectory was announced and Part 2 freezes it.
A board or confirmation whose chooser is annexed closes at once from `on_annex`, and the watchdog closes any other board whose chooser no longer exists; both use the existing `asteroid_incoming_close_unavailable_board`, which writes the fail-closed history outcome and picks no new chooser or coordinate.
Basis: Part 2 freezes the locked coordinates, Part 10 requires the impact to resolve two days after the lock, and the spec allows no reroll.
Needs live game: that a queued country event is dropped for an annexed country, and the watchdog path.

### Part 8 fields in Event Details, the history row and the preparedness event

Decision: the lock saves the chooser as the global event target `asteroid_incoming_impact_chooser`, which no cleanup path clears, and the impact Event Details view adds "Trajectory chosen by", the original target state's continent, and the current dust stage next to the current score.
The impact history row adds the fragment-site count and the opening dust stage; `global.asteroid_incoming_fragment_site_count` is the applied count, because the fragment planner resets it to zero when fewer than the minimum centres apply.
`chaosx.nr28.3.d` says whether the locked state is the target country's current capital, reading the country's `capital` against the locked state, and says nothing once the lock pointers are cleared.
The miss and fail-closed views are unchanged, and the preparedness clause carries no colour codes.
Basis: Part 8 lists the chooser, locked state and region, current Dust Load and stage for the impact Details view, the actual fragment count and opening dust stage for the history row, and the capital status for the target emergency.

### The observation network helps its own country

Decision: while dust is active, a country with `asteroid_incoming_observation_network` adds `asteroid_incoming_dust_protection.observation_sky_fraction` (0.15) to the share of the current stage's air-mission and weather penalties that the hidden `asteroid_incoming_national_dust_protection` modifier offsets, with or without a protection tier.
The combined share is clamped to `maximum_fraction` (1.00), and the modifier is removed at zero dust as before, so it can never become a bonus; at Residual Haze the weather penalty is zero, so only air missions gain.
Joining the network refreshes the modifier at once; the decision tooltip states the value; `ai_will_do` is unchanged.
Basis: Part 6 says the observation network "improves weather warning, contributes a bounded amount to global dust decay, and reduces the country's warning delay for linked disasters"; the air-weather share is the supported national form of the weather-warning benefit.
The linked-disaster warning clause has nothing to act on: Event 028 calls its Event 013 secondary disasters only inside the impact transaction (`asteroid_incoming_apply_state_profile`), before any country can join the network, so no later linked disaster exists whose warning could be improved.

### Rival crater actions target the crater-site array

Decision: Reconnoitre a Crater Site, Disrupt Extraction Routes and Prepare a Crater Offensive use `state_target = yes` with `target_array = global.asteroid_incoming_mineral_site_states` instead of `state_target = any`.
That existing global array already is the persistent crater-site array: the impact transaction adds the main crater when it registers it, the fragment planner adds every applied fragment centre, and neither `asteroid_incoming_initialize_transaction`, `asteroid_incoming_cleanup_transaction`, `asteroid_incoming_fail_closed_transaction` nor `asteroid_incoming_cleanup_finished_transaction` clears it, so it survives save and load like any global array; a comment in the cleanup now records that contract.
A second array with the same members was not added.
`visible` and `target_trigger` are unchanged.
Basis: the wiki Decision modding section (`state_target = any` checks every state in the game daily, and explicit targets need `state_target = yes` or `any`, lines 578-584) and the vanilla precedent `common/decisions/AUS.txt:942-944` (`state_target = yes` with a state `target_array`) and `CHI_decisions.txt:7929` (a `global.` target array).

### Fragment visuals follow the main strike in sequence

Decision: the main centre's `launch_nuke` visual stays inside the impact transaction, while each applied fragment centre is added to the persistent `global.asteroid_incoming_fragment_visual_queue` during its profile application.
Right after `asteroid_incoming_process_footprint`, the resolver queues the hidden presentation event `chaosx.nr28.9` `asteroid_incoming_runtime.fragment_visual_interval_hours` (4) hours later; each callback takes the first state off the queue, marks it with `asteroid_incoming_mark_visual_strike_state`, plays its `nuclear_bomb` visual from the current controller under `asteroid_incoming_visual_strike_active`, and queues the next callback while entries remain.
The hour delay is injected as an integer through `meta_effect`, as the resolver delay is.
Damage, dust, deaths and reports are untouched by the callbacks; removing the state before the visual and queuing the next in the same `immediate` means a save between visuals neither repeats nor loses one.
Basis: Part 9 asks to "resolve the visuals in a short sequence after the main effect so the player can understand that several sites were struck"; `effects_documentation.md` documents `hours` on `country_event` and the `launch_nuke` fields.
Needs live game: the visual spacing on the map, and whether a late `on_nuke_drop` consumer still sees each marker (the marker lasts `visual_strike_marker_days` from each launch).

### Round 3 review (2026-10-05)

A skeptical review of commits 08cb48523, f83b2e4ed, c05bec3a5, 2aa5bc6d2, 57dab97f3, 9161231c7, 431b48dfb, 37fdab5cf and 9b376d0f9 found no gameplay defect.
Checked in source: FROM stays the decision target inside `any_controlled_state` (vanilla `common/decisions/CHI_decisions.txt:591-592` uses `state = FROM` there in a state-targeted decision), so the ranking triggers compare each candidate with the real target, and the target never outranks itself; the duplicate resolver is a no-op because `asteroid_incoming_impact_recorded`, `impact_resolution_started`, `miss_recorded` and `fail_closed_recorded` are never cleared; the watchdog cannot fire before the queued resolver, because it needs `lock_expires_day` below the current day; `asteroid_incoming_locked_target_pair_is_valid` needs only a live owner and controller, so an overdue strike still lands after both callers are annexed; `tag = event_target:...`, `country_event` `hours`, `GetContinent` and `state_target = yes` with a global `target_array` are documented or have vanilla precedents.
Cleanup: the unread temporary `asteroid_incoming_force_remove_mineral_modifier` was removed from `asteroid_incoming_cleanup_transaction`, and the overview now says the national dust modifier is removed only when the country has neither a protection tier nor observation-network membership.
Cross-owner gap, not edited: the untracked Event 042 file `common/on_actions/042_equipment_from_heavens_on_actions.txt` adds an `on_nuke_drop` consumer that does not skip `asteroid_incoming_visual_strike_state`, so an asteroid visual launched by a human controller holding `efh_ach_nuclear_active` would be treated as that country's nuclear strike. That file belongs to unfinished Event 042 work and needs the same `FROM = { NOT = { has_state_flag = asteroid_incoming_visual_strike_state } }` guard when its owner finishes it.
MCP: `hoi4_event_inspect` returned "Invalid tool arguments" for `lint` with a string selector and for `trace` with an object selector; review is source-only.

## Round 3 lead items (2026-10-05)

### Plain transport-loss lines on the impact report

Decision: the two transport-loss keys returned by `GetAsteroidIncomingTransportLossClause` lose their `§Y` codes, so the original target's parchment impact report carries no coloured numbers.
Basis: the routed parchment defect and the chaos-redux-events rule that parchment descriptions use plain text, including text returned by scripted localisation.
Commit: 3e21eec34.

### The impact and fragment reports are short dynamic prose

Decision: `chaosx.nr28.5.d` and `chaosx.nr28.7.d` are rewritten from pipe-separated stat sheets into a few plain sentences built by scripted getters.
The opening names the worst-hit state and describes it by the country's strongest damage profile, one sentence per profile (main centre, three main rings, fragment centre, two fragment rings) and a generic sentence when no state is bound.
The second sentence gives the civilian deaths and the number of damaged states, with separate wording for no confirmed deaths and for a single damaged state, so no zero count prints.
Destroyed roads, railways, ports and supply hubs and destroyed factories, dockyards and refineries follow only when their level counts are above zero; strategic levels are left out to keep the report short.
The main-impact report adds the capital sentence only when the government moved (naming the new capital from the existing `asteroid_incoming_relocated_capital_state` target) or could not move, and the transport sentence only for the original target and only when something was lost or saved.
Both reports end with the current recovery phase and the most useful Asteroid Recovery order open now. The getter uses the decisions' own surface triggers (`asteroid_incoming_country_has_emergency_recovery_surface`, `..._reconstruction_...`, `..._dust_...`, `..._crater_...`) and the per-action `asteroid_incoming_state_is_open_for_*` triggers, so it never names an order the country cannot see. Emergency work prefers Deploy Mobile Hospitals where a rescue burden is active, then Open an Emergency Rail Corridor when transport levels were lost, then Clear Unstable Debris; a pending project, an occupied damaged state and an empty phase each get their own sentence. Decision names are pulled in with `$key$` references so they cannot drift from the decision titles.
The "state-months" rescue-burden figure, raw level counts, the zero capital-relocation line, the dust and protection labels and the pipes are gone; dust and protection remain in the Asteroid Recovery header.
The unused getters `GetAsteroidIncomingReportWorstState`, `GetAsteroidIncomingWorstDamageProfile` and `GetAsteroidIncomingCapitalRelocationClause` and their keys were removed.
Basis: Part 8 Country reports (specific and restrained, state names, rail loss, hospital pressure and displaced people; avoid one generic paragraph, map-table framing and raw hidden variables) and the Affected-country report role (worst state, total deaths, damaged states, capital relocation when relevant, the opening recovery problem).

### Each struck continent is named once

Decision: right after `asteroid_incoming_choose_fragment_sites`, the resolver calls `asteroid_incoming_record_fragment_continents`, which walks the applied fragment slots in strike order and saves the first centre on each continent as the global event target `asteroid_incoming_fragment_continent_<n>_state`, counting them in `global.asteroid_incoming_fragment_continent_count`.
The comparison uses `is_on_same_continent_as = event_target:...` in state scope, the form the fragment planner already uses for its second site.
`GetAsteroidIncomingFragmentContinents` lists the saved continents, and the impact news and the super-event fragment clause each became one key that prints the fragment count and that list, instead of five keys that repeated one continent per fragment.
Basis: Part 8 Fragment summary ("actual fragment count and broad regions") and the super-event direction ("mention fragments when active without listing every site"); `triggers_documentation.md` documents `is_on_same_continent_as` for state scope with any target.

### Units in the footprint take location-based damage

Decision: this replaces the unit half of the F18 decision. `launch_nuke` stays the map visual, but its native damage reaches only one province of the main centre and of each fragment centre, which left armies in the rest of the crater state and in every ring untouched.
`asteroid_incoming_apply_state_profile` now calls `asteroid_incoming_damage_units_in_state` once per processed state, after the profile's modifiers and before the rescue burden, local emergency, prices, country aggregation and reports. It applies one `damage_units` call with `state = THIS`, `ratio = yes`, `army = yes`, and `navy = yes` only for the main centre and the catastrophic ring, and no country limit, so every army standing in the state is struck whoever owns it.
Strength and organisation shares come from the new `asteroid_incoming_unit_damage` constants category: main centre 0.75/0.95, catastrophic ring 0.45/0.75, major ring 0.25/0.50, outer ring 0.08/0.25, fragment centre 0.35/0.65, heavy fragment ring 0.20/0.40, light fragment ring 0.05/0.20. Each value falls ring by ring, each fragment profile is lighter than the main profile it resembles, and none removes a unit outright, so an army caught in the crater survives broken and disorganised rather than deleted.
The damage fields take temporary variables set from those constants, the form `cbrn_consequence_effects.txt` already uses in its own `damage_units` calls, so no `meta_effect` is needed.
The step runs only inside the impact branch of `chaosx.nr28.4` (through `asteroid_incoming_process_footprint`), behind `asteroid_incoming_state_is_resolvable_transaction`, so a miss or a fail-closed trajectory never reaches it and no state is struck twice.
Basis: Part 3 Units in affected states (units suffer through supported location-based mechanics; the main crater must not leave units operating normally; no deletion of all units regardless of location) and the `damage_units` section of `effects_documentation.md` (location fields `province`, `state`, `region`, optional `limit`, `org_damage`, `str_damage`, `ratio`, `army`, `navy`).
Needs live game: the visible strength and organisation loss of armies and fleets in each ring.

### Each crater has a persistent profile that the survey reveals

Decision: the main crater (in the `main_center` branch of `asteroid_incoming_apply_state_profile`) and each applied fragment centre (in the commit loop of `asteroid_incoming_choose_fragment_sites`) call `asteroid_incoming_assign_crater_site_profile`, which rolls one `random_list` only when the state has no `asteroid_incoming_crater_site_profile` variable yet and stores id 1 (dense metallic material), 2 (fused silicate composite) or 3 (shock-formed crystal and glass). The ids and equal weights live in the new `asteroid_incoming_site_profile` constants category; the weights enter `random_list` as temporary variables, the form the zombie outbreak roll already uses and `effects_documentation.md` allows ("The weight can be a variable valid in the current scope"). A stored state variable survives save and reload, and the guard means a second call never re-rolls it.
Survey Extraordinary Material replaces the single generic `asteroid_incoming_crater_surveyed_material` marker with one of three named state markers, each with its own in-world description and no modifier values, so armour is untouched.
Its one-use research bonus keeps `asteroid_incoming_crater.survey_research_bonus` and `survey_research_uses` but takes its category from the profile: dense metallic material gives industry (metallurgy and production), fused silicate composite gives synthetic resources (materials made in furnaces), and shock-formed crystal and glass gives electronics (optics and radio crystals). The category is a literal in each branch, because `add_tech_bonus` takes a category token.
The survey tooltip names the profile as the first samples' finding and the research field it feeds, so the controller sees what the survey will record before paying; the profile becomes public on the map through the state marker once surveyed. Reconnoitre a Crater Site adds a sentence naming the material only after some country has surveyed the site.
`ai_will_do` is unchanged for every crater decision.
Basis: Part 5 Site flavor profiles (one persistent scientific profile per crater for reports and icons, no armour change, assigned once) and Part 6 Survey extraordinary material (reveals the profile, improves the modifier tooltip, grants a bounded material-science research benefit, no armour stack).
Remaining asset work: the three markers reuse `GFX_idea_asteroid_incoming_fragment_crater`, the icon the generic survey marker used; three profile-specific state-modifier icons are an open asset request for the Event 028 asset owner.

### Co-belligerents and friendly ground in the strike weights

Decision: `asteroid_incoming_ai_target_is_protected` adds `has_war_together_with = ROOT`, so a country fighting on the chooser's side is protected even outside its faction.
A new state trigger, `asteroid_incoming_ai_strike_would_hit_friendly_ground`, is true when the target state, a neighbour, or a neighbour's neighbour (two nested `any_neighbor_state` steps) is controlled by the chooser, a faction partner not at war with it, or a co-belligerent. Each strike option of `chaosx.nr28.1` and `chaosx.nr28.8` multiplies by the new `asteroid_incoming_ai.strike_friendly_ground_factor` (0.25) when it holds. Two steps match the catastrophic (50 percent civilian loss) and major (25 percent) rings; the outer ring was left out because its 5 percent loss is not the devastation Part 7 describes and three nested scans would cost more on every board.
The protected-target factor moved from the first to the last modifier of each strike option. HOI4 applies MTTH modifiers in written order (wiki AI modding, MTTH blocks), so a first-place factor of zero could be followed by an `add`; as the last modifier it keeps every protected target at exactly zero.
Both boards still carry byte-identical `ai_chance` blocks (checked by comparing the four weighted option blocks of each event).
Hand review, because the probability route failed: in AST_AI_06 (fascist chooser at war; subject, faction ally and enemy targets) the subject and ally now end at 0 whatever adds apply, and the enemy keeps (1 + 400) x 2 = 802 against a miss of about 812 unless its state lies within two steps of the chooser's front, where it falls to about 200 (about 20 percent). In the self-harm case (a neutral or enemy target state bordering the chooser's own state) the strike weight is a quarter of its previous value, and a target the chooser itself occupies is treated the same way. AST_AI_03's enemy faction leader keeps its rank unless the chooser already holds ground within two steps of the locked state, where Part 7 asks the score to fall.
Probability evidence: one `hoi4_probability_inspect` call with `adapter = event_option_ai_chance` and `candidatePool = ["chaosx.nr28.1"]` returned "Invalid tool arguments"; no further attempt was made, so the compare pass is a recorded route gap and the review above is source-only.
Basis: Part 7 Protected targets ("active allies in the same war") and Hostile target value (the score falls when the rings would devastate friendly or allied neighbouring states or the chooser's own states).

### Dust projects lapse once the sky has cleared

Decision: `asteroid_incoming_harden_factories_against_dust`, `asteroid_incoming_protect_transport_reserves`, `asteroid_incoming_join_observation_network` and `asteroid_incoming_distribute_emergency_filters` apply their protection idea, completion flag and mitigation only while `global.asteroid_incoming_dust_score` is above `asteroid_incoming_dust.minimum`; otherwise they do nothing.
These outcomes run a `decision_civilian_factory_days` work period after payment (the three national projects in their decision `remove_effect`, the filters through `asteroid_incoming_finish_recovery_project`). If dust reached zero in between, the zero-dust pass had already removed every protection idea, and the monthly update stops at zero dust with no local recovery, so an idea added afterwards stayed for the rest of the campaign with no effect.
The paid cost is not refunded: the four tooltips say that the project lapses if the sky has cleared when the work is done. Distribute Emergency Filters also gains the active-dust condition in `visible` and in `asteroid_incoming_state_is_open_for_emergency_filters`, as the three national projects already had, so it is not offered when it could only lapse. The project slot is still released by the finish callback either way.
Projects finishing during active dust behave as before. A World Reconnected candidate whose project lapses does not get the matching flag, which matches the achievement's own requirement that the protection be in place while dust remains.
Basis: the stale-idea defect in the round 3 lead list; Part 4 ties national protection to active dust stages.

### Second review of the round 3 takeover (2026-10-05)

A second skeptical review re-read commits 08cb48523, f83b2e4ed, c05bec3a5, 2aa5bc6d2, 57dab97f3, 9161231c7, 431b48dfb, 37fdab5cf and 9b376d0f9 against the current tree, including the later Event 028 commits that build on them.
Confirmed in source: the five `_NAME` and `_DESC` keys match the award conditions (near miss at `minerals_chaos_threshold` with both evolutions enabled; capital relocation only when the locked state was the capital; collector and capture holds; the World Reconnected opening stage, non-target and Hardened checks); the ranking triggers use only documented temporary-variable triggers and `building_level@` with the profile ids ordered so a larger id is a stronger profile; `country_event` accepts `hours`; vanilla compares a variable with an event target in `check_variable` (`common/scripted_effects/AST_scripted_effects.txt:1724`); `GetContinent` is a documented state property; `state_target = any_controlled_state` and a `global.` `target_array` have vanilla precedents (`AFG.txt:1844`, `CHI_decisions.txt:7929`); every new constant is defined under a schema of the right type.

Decision: the four Event Logs history rows for Event 028 use the two-line form every other row uses.
The history entry is 41 pixels high and its text box stops at 38 pixels (`interface/chaosx_events_log_popup.gui`, `events_log_history_entry_country`), which holds two lines of `hoi_16mbs`, while the Event 028 rows had four or five lines (Actor, Target country, Outcome, and the fragment and opening-dust line added in 57dab97f3), so only the header and the actor line could show.
The row's flags already show the chooser and, after an impact, the target country, so the second line now carries the outcome: the offered board, "Impact on <state>: <deaths> dead, <n> fragments" (the fragment clause comes from `GetAsteroidIncomingHistoryFragmentClause` and is empty when no fragment struck), the near-miss date, or the closed trajectory.
Deaths use the compact `|*1` form so the line stays inside the 350-pixel text box. The opening dust stage, the impact date and the rest of the Part 8 history fields stay in the Event Details view the row opens, which already lists them.
Basis: Part 8 Event History lists the fields of the history record, and the shared row convention (`chaosx.events_log.window.history.dynamic_entry.event`, `black_friday.history.50`) is a header plus one summary line.

Decision: `on_annex` also removes `asteroid_incoming_recovery_legacy` from the annexed country when it clears `asteroid_incoming_regional_economy_complete`.
The monthly pass that would otherwise remove the idea stops once dust and local recovery end, so clearing only the flag could let a released country return with the lasting legacy, which the c05bec3a5 decision rules out.

MCP: `hoi4_gui_render` for `events_log_history_entry_country` returned "Invalid tool arguments"; the row fit was checked from the `.gui` source only.
Needs live game: that each Event 028 history row shows both lines unclipped, including a long state name on the impact row, and that `[?constant:...]` resolves in the achievement list's `_DESC` text.
