# Event 021 agent decisions, 2026-10-04

Disposition: accepted agent decisions under the user's full-authority takeover grant, recorded by the Claude implementing engineer for Event 021.
Acceptance basis: the user granted the takeover engineer authority to choose the recommended, spec-consistent option and record it here; the lead's round-1 assignment for Event 021 lists the same choices.
Each entry states the decision, its basis, and where it is implemented.

## D1. Adopt the stopped thread's uncommitted tranche

Decision: adopt, review, and commit the stopped Codex thread's uncommitted Event 021 work instead of discarding or rewriting it.
Basis: every called scripted effect and trigger, every `constant:` reference, and every localisation key resolved in the working tree; the ledger tranche had an independent re-review; the external-war fallback carries the user's explicit approval in `docs/specs/021_random_civil_war_specs/021_random_civil_war_external_war_successor_addendum.md`; the mission rework closes the 2026-09-26 audit findings and holds the routed `exists` fixes 1(a) and 1(b).

Focused review of the parent-effects diff before commit found no country-only trigger in state scope, no scope-prefixed temporary variable, no timed flag fed `days = constant:`, no date arithmetic outside `event021_days_to_date_offset`, and correct `on_state_control_changed` scoping (ROOT new controller, FROM old controller, FROM.FROM the state).
The new mission hook fails a hold for FROM, the country that lost control, which is the intended holder.

The commit split follows the code rather than the six suggested groups, because the parent-effects file interleaves the ledger, scenario cap, provenance and external-queue hooks hunk by hunk.
Splitting those hunks across commits would have produced intermediate trees calling undefined helpers.
Every commit below was built in an isolated index and checked for definition, constant and brace closure against its own tree.

| Commit | Content |
| --- | --- |
| `de3f7de71` | External-war successor prompt: new effects, triggers, event and localisation, its annex and on-action wiring, and the external-queue gates in target triggers. |
| `4c041ead2` | Dynamic front ledger, candidate traversal, crisis-scoped secondary review, successor roster rebuild, MTTH actor predicates, Maximum scenario front envelope, opening provenance, and the ledger contract test. |
| `00fe90801` | Mission continuity and sponsor gating, including the routed fixes 1(a) and 1(b), and the decision text rewording. |
| `628a50c32` | KUB Ivanis placeholder portrait and deletion of the fifteen orphaned achievement DDS files. |

The documentation commit that carries this file records the plans, specs, handoffs and probability snapshots of the same tranche, plus only the Event 021 hunk of `.gitattributes`.

## D2. Selectable missions resolve on selection, not at the timer

Finding: HOI4 runs `complete_effect` when a selectable mission is selected and then removes the mission, while `timeout_effect` runs only when the timer expires unselected.
Vanilla precedents `AST.txt` (Canberra cabinet mission) and `CHI_warlord_decisions.txt` (`TSR_pay_for_support_from_warlord_PP`) treat the two blocks as alternative terminal outcomes.
The adopted Event 021 missions used `complete_effect` to start a hold and `timeout_effect` to judge it, so a selected hold never resolved and an unselected one did nothing.
Decision: repair this in a dedicated commit after the tranche commits (see D3).

## D3. Mission repair shape

Decision: keep each selectable mission as the player's commitment, and on selection start a non-selectable hold mission through `activate_mission`.
The hold mission shows the native countdown, cannot complete early, judges the objective in its `timeout_effect`, and is cancelled when the hold breaks or the crisis ends.
The existing `on_state_control_changed` hook still fails a capital or rail hold the moment control of the bound state changes.
Basis: the mission spec (`021_random_civil_war_spec_part_3_decisions_missions_and_outcomes.md`, Mission families) requires timed holds with success and failure; vanilla `ETH_time_based_war_escalation_mission` uses a non-selectable mission with `available` never true to run a visible timer.
No cost, AI weight or reward changes.

## D4. Switched-off evolution stages are independent

Decision: follow the Event 004 precedent of independent stages.
`event021_parent_process_evolution_schedule` builds each stage's Events Log context and checks `is_current_evolution_enabled` before it samples a due date or fires the hidden callback.
A stage switched off in the settings is never sampled, fired, activated, or recorded, and a stale due date is cleared.
Evolution II needs Evolution I recorded or switched off; Evolution III needs both earlier stages recorded or switched off, which keeps enabled stages in order without letting a switched-off stage block a later one.
`event021_apply_evolution_ii` and `event021_apply_evolution_iii` no longer call the earlier core effects, and the parent wrappers accept a switched-off earlier stage, so a later stage never switches on a disabled stage's mechanics.
Re-enabling a stage returns it to normal scheduling through its own wrapper.
Basis: the lead's round-1 assignment, the audit finding EV21-DISABLED-01 in `subagent_handoffs/event021_date_units_probability_audit_2026-10-03.md`, and `common/scripted_effects/004_random_war_effects.txt`, which checks `is_current_evolution_enabled` per stage.
Contract: `common/scripted_effects/021_random_civil_war_parent_effects.md` (scheduler section).

## D5. Evolution I reviews wars that were already running

Decision: take the accepted addendum's recommended options.
The first recorded Evolution I queues one review on the canonical government of every live crisis whose recorded opening stage is baseline; a crisis without that record fails closed.
The existing daily global-host pulse dispatches a bounded, rotating slice of the theater registry to hidden callback `chaosx.nr21.20`, so ROOT is the reviewed government.
Each live side of the crisis is reviewed once by front ID: the government and its ordinary claimants may give up a connected region from their own held states with their own route evidence, and the government may release a complete Event 006 package from its own territory.
The donor keeps its capital, a connected remnant at or above `minimum_remnant_states` (checked by a flood fill from the capital), and its reserved share of divisions; spare divisions are split across kept rows by region weight with whole divisions and no borrowing.
Rows live in the government's own `random_civil_war_active_front_*` arrays with their own validator, and commit synchronously through the existing ordinary and Event 006 secondary adapters under a commit lock; the loader, receipt validator, span copy, opening-receipt copy, and row binding gained active branches, and the borrowed transaction globals are saved and restored.
New sides inherit the crisis ID and the donor's generation, so no descendant crisis is created, and they are marked reviewed so they cannot split again in the same epoch.
Temporary blockers (no spare front, another serial transaction or scenario, settlement talks, successor grace, a side near defeat) defer the review on `retry_days`; an idle finished opening template is offered to its owner's release check first.
Event 006 carriers are no-side sources, because their package identity cannot be proven to survive a further split; this is a fail-closed reading of the addendum rather than a new rule.
The region-growth and package loops were extracted from the opening collector into shared helpers; the opening path runs them with the active mode off and its rows are unchanged.
Basis: master spec Evolution I section, `021_random_civil_war_spec_part_4_evolution_i.md` "Active-war transition", and the parent acceptance at the top of `event021_active_war_evolution_i_repair_addendum_2026-10-03.md`.
Contract: `common/scripted_effects/021_random_civil_war_active_evolution_effects.md`; accepted behavior merged into the spec section "Accepted active-war review".

## D6. Evolution I management phase for wars without a new side

Decision: queueing a crisis for its Evolution I review also gives its government and every live registered side `random_civil_war_evolution_i_management_ready`, with no actor and no multi-front flag.
While Evolution I is active and switched on, that receipt moves the side out of the opening phase into the front-management phase: Review Command Loyalty, Integrate Loyal Formations, and Set the Priority Front, plus Protect State Communications while the capital is controlled and keeps a supply node, replacing the opening arsenal, capital, and depot actions; Offer Emergency Settlement stays the government's conditional fifth action.
Settlement removes the receipt from every side of the crisis, crisis cleanup removes it per country, and any new crisis role starts without it.
No AI weight, cost, or mission changed; the hold-capital mission keeps its existing activation.
Basis: the spec's no-side outcome and the addendum's management section; granting at queueing instead of after a no-side verdict keeps the phase available while a review waits on a temporary blocker.

## D7. Set the Priority Front resolves its own target

Finding: `event021_set_priority_front` acted only on the chain-local `random_civil_war_anchor_state` target, which exists only inside opening chains, so the decision charged command power and did nothing; calling it also cleared the row-bound receipt.
Decision: when that target is absent, the setter resolves the taker's own front state from durable receipts in a fixed order (its own anchor, the shared opening anchor, its capital, then the first held state of its current front), each owned and controlled by the taker and inside its current front membership.
The decision's `available` and the setter share `event021_priority_front_target_valid`, and the decision tooltip names the chosen state with the same order.
`event021_bind_front_plan_row` now replaces the bound receipt only when a plan is published.
Opening chains keep their exact behavior because they always pass the anchor target.
Basis: the lead's round-1 assignment and the 2026-09-26 decision audit finding.

## D8. Dynamic civil-war tag capacity is guarded, not extended

Decision: Event 021 counts the declared dynamic pool (D01 to D75 in vanilla `common/country_tags/zz_dynamic_countries.txt`) with a bounded `meta_trigger` loop over `country_exists`, keeps a centralized reserve free for other events, and plans no more new ordinary claimants than remain.
It does not rely on `is_dynamic_country`, whose installed documentation says D01 to D50, and it does not extend the shared vanilla pool, which every event uses.
A shortfall rejects an opening, trims optional rows, skips a frozen Fracture Cascade plan, or defers an Evolution I review source, always with the existing `cap_reached` reason; no plan is converted into a same-tag contest, which the user ruled out.
Fracture Cascade holds tags per frozen country so a Maximum batch cannot overcommit, and releases each hold right after that country's commit.
Basis: the lead's round-1 assignment, the offline Country creation warning about running out of dynamic countries, and the 2026-10-03 tag-capacity audit that left this blocked.
Contract: `common/scripted_effects/021_random_civil_war_dynamic_tag_effects.md`.

## D9. Decision text tidy

Decision: Offer Emergency Terms shows political power, command power, and rifles inline, and its cost tooltip names the manpower the talks also commit; every gate and payment is unchanged.
Support the Government and Support the Opposition state that the sponsor ships 150 rifles and 100 arrive after transport and handling losses, using the existing gate and transfer constants, without changing either amount.
Their descriptions, and Monitor the Border's, name the live target through `event021_GetSupportGovernmentTarget`, `event021_GetSupportOppositionTarget`, and `event021_GetExposureSourceName`, with neutral fallbacks when no target is recorded.
Basis: the 2026-09-26 decision and localisation audit findings and the decisions skill's three-inline-value limit.

## D10. The private date converter wraps the shared helper

Decision: keep `event021_days_to_date_offset` and its 41 call sites, but make it a thin wrapper that hands the days to the shared `chaosx_convert_days_to_date_offset` and copies the result back, creating the shared output before the call so it survives the return.
The duplicate `event021_calendar` constants and their file `common/script_constants/021_random_civil_war_date_constants.txt` are removed because nothing else uses them.
`.tools/test_event021_date_units.py` now runs the wrapper through the shared helper and the shared `chaosx_date_units` constants and still passes.
The shared registry row in `chaosx_dynamic_effects.md` was updated with a single-row edit.
Basis: the harness rule that day and date arithmetic uses the shared converter, and the lead's round-1 assignment.

## D11. Event detail and catalog wording

Decision: `event021_event_log_detail` gains two sentences describing the Evolution I review of running wars and the successor's choice of a new war for its own core or claimed territory, and `event021_evolution_i_body` and `event021_evolution_i_log` describe the stage as it now plays.
The matching catalog Details and Evo I wording is queued in `catalog_changes_pending.md` with Status kept at Needs Testing; no spreadsheet or CSV was edited.
Basis: the lead's round-1 assignment and the rule that catalog fields match in-game localisation.

## D12. Tag-capacity accounting in the opening validator

Finding from the takeover's post-round review: a same-tag plan that fails its remnant check falls into the ordinary branch of `event021_parent_validate_opening_plan`, where the tag guard could label it `cap_reached`, and a reserved cluster target rejected for tags was also counted as a failed state reservation.
Decision: the tag guard skips same-tag plans as well as Event 006 plans, and the cluster opening caller creates `event021_dynamic_tag_short` before the call and records `state_reservation_failed` only when no tag shortfall was already recorded.
No gate, cost, weight, or plan outcome changes; only the skip reason and skip count become accurate.
Basis: decision D8 and the acceptance that same-tag rows never use dynamic-tag capacity.
Contract: `common/scripted_effects/021_random_civil_war_dynamic_tag_effects.md` (Callers).

## R1. Round 1 review: each side keeps its own priority front

Finding from the round 1 skeptical review: `event021_set_priority_front` wrote `random_civil_war_priority_front_state` and its id to the chain ROOT instead of the country being set up.
Every opening chain initializes the government and each claimant under one ROOT, so the government's receipt ended as the last claimant's anchor and no claimant ever received its own.
The Evolution I review (D5) runs under the reviewed government as ROOT, so each side it opened overwrote that government's priority front with a state the new side now holds.
Because Seize an Opposition Depot requires the taker's own priority-front state, the opposition could never take it during the opening phase.
Decision: the setter writes the receipt to the calling country (`PREV` inside the anchor scope); the decision path is unchanged because its taker is both ROOT and the caller.
No cost, gate, AI weight, or global target changes; the Seize an Opposition Depot decision becomes reachable for opposition sides as its existing AI weights already intend, which remains `needs_live_game`.
Contract: `common/scripted_effects/021_random_civil_war_effects.md` (priority front paragraph).

## R2. Round 1 review: successor review carry-over comment

`event021_prepare_successor_roster_adoption` said the review retry date carries over to the successor, but the code copies only the queue receipt, crisis ID, epoch, reviewed front IDs, and management access.
The comment now matches the code; the successor's grace already defers the review, so no behavior changes.

## R3. Round 1 review: Defend the Capital stays reachable while Hold the Capital is on offer

Finding: Hold the Capital is offered in the opening phase and in the front-management phase, and it can only be selected while `event021_capital_defense_active` is set, which only Defend the Capital sets.
Defend the Capital was visible only in the opening phase, so a side that entered the Evolution I management phase (D6) or a real multi-front war before using it saw a Hold the Capital card it could never select.
Decision: Defend the Capital is also visible in the front-management phase until it is used or the capital hold has succeeded or failed.
The arsenal and depot actions stay excluded from that phase, as the addendum's management section requires; it names only those two opening actions as excluded and keeps the capital hold as the immediate mission.
Cost, effect, and AI weights are unchanged; AI sides in the front-management phase can now take the action under its existing weights, which remains `needs_live_game`.
Contract: `docs/events/021_random_civil_war/decision_action_family_crosswalk.md` and the accepted active-war review section of `021_random_civil_war_spec_part_4_evolution_i.md`.

## R4. Round 1 review: hold mission outcomes are explained, not printed raw

Finding: the three non-selectable hold missions added in D3 ran their resolvers directly in `timeout_effect` and `cancel_effect`, so the mission tooltip printed raw conditional effects and internal state instead of the outcome, unlike the selectable cards, which already wrap their commitment in a tooltip.
Decision: each hold mission's timeout shows one outcome tooltip (`event021_holding_the_capital_outcome_tt`, `event021_securing_the_rail_spine_outcome_tt`, `event021_upholding_the_settlement_outcome_tt`) and runs its resolver hidden; cancellation runs hidden because it has no player-facing result.
The capital hold names its bound state through `event021_GetHoldCapitalTargetName`, and the three selectable cards describe themselves as commitments, because selecting one starts the hold rather than finishing it.
No gate, timer, cost, reward, or AI weight changes.

## R5. Round 1 review: helper results that callers read survive the helper return

Finding: the Evolution I review's Event 006 commit (D5) saves and restores the government's Event 006 receipt through `event021_parent_save_event6_host_identity` and `event021_parent_restore_event6_host_identity`, which kept the copy in temporaries first created inside the save helper.
The repository's helper-output rule (`chaos-redux-events`, Helper output lifetime) treats such temporaries as lost after return, in which case the restore would erase the host's Event 006 receipt instead of restoring it; the opening path's two existing callers share the helper.
Decision: the saved copy lives in normal `random_civil_war_event6_saved_*` variables and flags on the host, the restore runs only when this country holds a saved copy, and it clears the copy afterwards.
The shared candidate collector now creates `event021_parent_event6_package_found` before it calls the Event 006 package finder, and the secondary initializer creates `event021_planned_state_span_found` before the span copy, so both results the callers read survive the call.
No gate, cost, weight, or plan outcome changes; a restore without a saved copy now leaves the host unchanged instead of clearing it.

## D13. Settled crises keep ticking until the obligation and cleanup resolve

Finding from the round 2 review: reconstruction ends after `reconstruction_days` (120) while the settlement terms hold for `settlement_terms_hold_days` (180), but the global review called `event021_parent_reconstruction_tick` only while `random_civil_war_reconstruction_active` was set.
Once reconstruction completed, the obligation was never judged, `chaosx.nr21.10` never fired, and every settled crisis kept its theater registered and `random_civil_war_active` set, so the baseline cap of two active theaters stopped new civil wars after the first settlements.
Decision: the global review calls the tick whenever `event021_parent_reconstruction_due` holds, and that trigger gains a third case: reconstruction complete, settlement recorded, obligation no longer open, and `random_civil_war_reconstruction_resolved` not yet set.
The existing hold-date case now also reaches a crisis whose reconstruction already finished, because the caller no longer requires the active flag.
The tick's final block (administration restored, recurrence prepared, reconstruction record, `chaosx.nr21.10`) requires `random_civil_war_reconstruction_resolved` to be absent, so it runs once per crisis generation and an Event 006 actor that host cleanup already finalized is only judged on its obligation.
At the hold date, a terms mission that confirmed the objective (`random_civil_war_settlement_obligation_objective_met`) now counts as met in the missed-objective branch too, matching the fulfilled branch and the mission's "success confirms the settlement" text.
Trace with the shipped constants: the first review at or after day 120 completes reconstruction while the obligation stays open, the first review at or after day 180 judges it held or breached, and the same tick records the reconstruction, prepares recurrence, and fires `chaosx.nr21.10`, whose cleanup unregisters the theater and clears `random_civil_war_active`.
An obligation breached early, such as a failed terms mission, resolves inside that mission and the crisis closes on the first review after reconstruction completes.
No periodic hook or world iteration is added, and all date offsets still pass through `event021_days_to_date_offset` and the shared converter.
Basis: the lead's round 2 assignment and the spec's requirement that settlements create obligations that must resolve before the category closes.
Contract: `common/scripted_effects/021_random_civil_war_parent_effects.md` (reconstruction tick paragraph).

## D14. The settlement phase lasts for the whole obligation period

Finding: `chaosx.nr21.9` fires as soon as terms are applied, and its option cleared `random_civil_war_settlement_phase`, which turned `event021_country_can_manage_settlement` false.
Complete Disarmament, Complete Coalition Governance, and End Sponsor Commitment disappeared, Hold the Settlement Terms stopped activating, and Upholding the Settlement was cancelled, so those obligations could only end in breach, and AI governments, which answer the event at once, essentially always breached.
Decision: Event 9 keeps firing when a settlement is applied, but its option no longer clears the phase; it shows one outcome tooltip (`chaosx.nr21.9.a.tt`) and runs the reconstruction flag and first tick hidden.
`event021_parent_review_settlement_obligation` clears the settlement phase once the obligation is fulfilled or breached, so the phase lasts from settlement until the obligation resolves whether or not the event was answered.
Event 9's title and description now describe the settlement just reached and the obligation ahead (`event021_GetSettlementObligationName`), and the settlement summary line says the fighting has stopped.
During the overlap the visible set is Reconstruct Administration, at most one obligation action, Protect State Communications, Review Regional Administration, Secure the Rail Spine, and Hold the Settlement Terms, which stays within the six-action ceiling.
Opening, front, multi-front, Evolution I prevention, and exposure gates already exclude the settlement and reconstruction phases (`event021_country_can_manage_opening`, `event021_country_can_manage_fronts`, `event021_country_can_manage_multifront`, `event021_country_can_use_evolution_i_prevention`, and `event021_country_can_manage_exposure`), and settlement application sets both phases, so none of them reopens.
No AI weight, cost, timer, or MTTH constant changed. The Evolution I and II MTTH `settlement_progress_factor` keys on `random_civil_war_settlement_phase`, so for a sampled settled theater it now applies for the whole obligation period instead of until Event 9 was answered, which is the period the factor describes.
Basis: the spec and decision prompt require settlement obligations to resolve before the category closes, and the crosswalk maps the amnesty, coalition, and guarantee families to these obligation actions.
Contract: `docs/events/021_random_civil_war/overview.md` (Settlement, reconstruction, and recurrence).

## D15. Signing the terms settles the war at once

Finding: the `chaosx.nr21.5` option set `random_civil_war_settlement_signed` and cleared `event021_settlement_pending` before calling `event021_parent_apply_settlement`, which checks `event021_settlement_signed` and the pending marker, so signing did nothing while the war was still running.
The government paid political power, command power, rifles, manpower, and authority, then sat with talks open: its opening actions were hidden, its Evolution I review was deferred, no settlement actions appeared, and `event021_settlement_deadline` and `event021_settlement_obligation_active` were written but never read. Failing AI governments, whose weights favour the offer, fell into the same state.
Decision: signing applies the negotiated settlement immediately, rather than keeping talks open until the war ends.
The option keeps the pending marker set, shows one outcome tooltip (`chaosx.nr21.5.a.tt`), and runs the apply hidden; a same-tag loyalty contest goes through `event021_parent_resolve_same_tag_takeover`, which also retires the contest route.
With talks open, the selector never chooses a government military victory: at or above `strong_settlement_threshold` a lone regional or legal front is reintegrated by merger, a regional route receives autonomy, and anything else becomes a coalition; below it the result is partition when the partition topology is ready and coalition otherwise.
Keeping merger in the strong branch is this decision's reading of the lead's "autonomy or coalition" rule: merger is the spec's negotiated reintegration, its topology already requires open talks, and it has no other route, so dropping it would delete a settlement family. The natural-path merger branch, which could never be reached without talks, is removed.
After signing, no internal war of the crisis stays active: ordinary claimants rejoin the state through `event021_parent_close_ordinary_opposition` or survive as partition successors, which now also make peace with the claimant they split from, and an Event 006 host war ends through the independence branch, after which the host's ordinary claimants rejoin the state through the same close path.
Offer Emergency Terms is unavailable, with the requirement line `event021_offer_emergency_settlement_sides_tt`, while `random_civil_war_event6_secondary_front_active` is set or any live opposing side is player-controlled (`event021_settlement_offer_blocked`), because the close paths cannot settle a package-owned secondary front and nothing should annex or partition a player without consent.
The unused `event021_settlement_deadline` and `event021_settlement_obligation_active` writes and their dead `settlement_obligation_days` constant are removed; the obligation and its hold date come from `event021_parent_select_settlement_obligation` as for every settlement.
No cost, AI weight, or MTTH value changed, so no probability compare is required; AI governments that take the offer now leave the war with a partition or coalition instead of stalling. Event 021 status stays Needs Testing, and the runtime outcome of each branch is `needs_live_game`.
Basis: the option already calls `event021_parent_apply_settlement`, which accepts the pending marker as a reason to settle now (the same-tag path uses it that way); the event text "A settlement can stop the guns" and "Sign the terms"; the decision text "Offer a ceasefire ... before the remaining fronts become permanent"; the crosswalk row for settlement talks; and the probability matrix intents SET-01, SET-03, and SET-05.
Accepted design merged into `021_random_civil_war_spec_part_3_decisions_missions_and_outcomes.md` ("Accepted signed-terms settlement") with its manifest hash refreshed. Contract: `common/scripted_effects/021_random_civil_war_parent_effects.md`. Crosswalk and `catalog_changes_pending.md` updated; no catalog field changes.

## D16. The crisis record shows only its own opening status

Finding: `event021_parent_record_system_log` read the country variable `random_civil_war_cluster_skip_reason`, which nothing writes, and fell back to the persistent `global.random_civil_war_cluster_skip_reason`, so after any skip anywhere every later record, including successful openings and settlements, showed that stale reason under Opening status.
Decision: a record carries a skip reason only when its payload is `failed_opening` and the global skip receipt was written in the same transaction (its date equals `global.date`); every other record shows None. The dead country-variable branch is removed.
The package-incomplete failed opening still shows its reason because it records the skip immediately before its log entry, and a validator tag shortfall still shows `cap_reached` on its failed opening.
The optional narrowing of the validator's tag-shortfall receipt to cluster and scenario launches is not taken: the global receipt is read only by this log snapshot, so recording the shortfall for ordinary openings keeps their failed-opening record explained.
No gate, weight, or launch behavior changes, and the shared Events Log files are untouched.
Contract: `common/scripted_effects/021_random_civil_war_parent_effects.md` (`event021_parent_record_system_log` paragraph).

## D17. Mission availability shows plain requirements only

Finding: the available blocks of Secure the Rail Spine and Hold the Settlement Terms showed `event021_secure_rail_mission_target_valid` (a raw `has_variable` and `is_in_array` check), a raw NOT/AND over the rail state's flags, `has_variable = random_civil_war_settlement_terms_hold_until`, and the obligation-failed flag as script text beside their own requirement lines.
Decision: the rail card states its requirement through `event021_secure_rail_requirement_tt`, which names the bound state through `event021_GetRailMissionStateName` and now wraps `event021_secure_rail_mission_target_valid`; the lost and already-repaired checks, which activation and cancellation also enforce, sit in `hidden_trigger`.
The settlement card states "The settlement's obligation, [obligation], is still in force and has not been broken" through `event021_settlement_terms_requirement_tt`, which wraps the active and not-failed obligation checks, and the hold-date variable check is hidden.
Every gate is logically unchanged. A scripted pass over every available block in `common/decisions/021_random_civil_war_decisions.txt` finds no visible trigger at all outside `hidden_trigger` or `custom_trigger_tooltip` (the same pass on the previous file listed the seven raw checks above).

## D18. Unselected mission cards lapse instead of re-offering at once

Finding: Hold the Capital, Secure the Rail Spine, and Hold the Settlement Terms are selectable missions with `fire_only_once = no` and no `timeout_effect`, so a card whose selection timer ran out unselected did nothing and reactivated at once with a fresh full timer, indefinitely.
Decision: each card gains a `timeout_effect` that shows `event021_mission_offer_lapsed_tt` ("The moment passes. The commitment can be offered again in N days.") and sets a timed lapse flag (`event021_hold_capital_offer_lapsed`, `event021_secure_rail_offer_lapsed`, `event021_settlement_terms_offer_lapsed`) that the card's activation excludes.
The duration is `constant:event021_action_tuning.action_cooldown_days`, copied into the temporary `event021_decision_flag_days` first because timed flags cannot take `days = constant:`.
There is no penalty and no change to costs, rewards, timers, or AI weights. `event021_clear_mission_offer_lapses` clears the three flags; `event021_cleanup_decision_state` and both new-role helpers (`event021_commit_opening_evolution_provenance` and `event021_inherit_crisis_opening_evolution_provenance`) call it.
Basis: the lead's round 2 assignment and the D2 finding that `timeout_effect` runs only for an unselected selectable card.

## D19. Requirement-flag text describes the world

The six origin and package flags that Event 006 package requirement blocks can display (`independence_wave_event021_adapter_setup_proven`, `independence_wave_event6_adapter_package_ready`, `random_civil_war_event6_adapter_complete`, `random_civil_war_event6_adapter_preparing`, `random_civil_war_event6_origin_recorded`, `random_civil_war_origin_adapter_complete`) described records and systems.
Each now states the world fact the flag stands for, matched to when it is set (all at package setup during an Event 021 opening): the movement is ready to take up arms, is taking up arms, entered the war as an independence front, or the country rose from the civil war.
Key names are unchanged, the file stays UTF-8 with BOM, and no Event 006 file is edited.

## D20. Target tickets keep the major reduction at low scores

Finding: `event021_parent_add_target_to_selection_pool` divided the 0-1000 target weight by 100, rounded it, and clamped it to 1-10, so a major's reduced weight (`major_target_factor` 0.35) and a minor's full weight both became one ticket for every raw score below 150, which erased the spec's lower major likelihood for weakly eligible targets.
Decision: `target_pool_weight_scale` becomes 25 and `target_pool_weight_cap` 40, keeping their product at the 1000-point score ceiling, so a major draws fewer tickets than a minor with the same raw score from a raw score of 38 upward, which covers every candidate without the recent-war memory penalty.
The helper also creates the shared curve's output before calling it. The pool stays bounded at 960 entries and 160 iterations per country.
The before and after ticket table and the named TGT scenario shares are in `target_ticket_resolution_2026-10-05.md`. TGT-02, TGT-03, and TGT-05 keep their intents, and TGT-04 now follows the score ratio (2:1) instead of a rounding artifact (3:1).
The MCP baseline was attempted once and returned `INTERNAL_ERROR`, so no compare exists. This is recorded as a blocker and was not retried.
This closes the "Target ticket conversion" tuning group in `subagent_handoffs/script_constant_completion_2026-09-02.md`. Live selection shares remain `needs_live_game`.

## D21. Offer Emergency Terms waits for the war to run, and the AI offers terms only when the war turns

Finding from the round 2 lead review: since D15 made signing settle the war at once, Offer Emergency Terms was available from the first day of every war, and its AI weight was base 1 for every government (x1.5 negotiator or Failing authority, x0.75 hardliner, never 0).
AI governments therefore signed within days and ended almost every AI civil war by negotiation, contradicting SET-01 (dominant government: military or firm settlement) and SET-04 (hardliner: repression), and a player government could end its own war on day one.
Decision: the decision needs `event021_settlement_offer_ready`, shown through the requirement line `event021_offer_emergency_settlement_ready_tt` ("The war has been fought for at least 90 days, which it reaches on [date]."), with every implementation check hidden.
The ready date is the crisis start (`random_civil_war_crisis_start_date`) plus `constant:event021_settlement_offer.minimum_war_days` (90).
A decision trigger cannot call an effect, so `event021_record_settlement_offer_baseline` computes the date once through `event021_days_to_date_offset`, which wraps the shared `chaosx_convert_days_to_date_offset`, when the opening commits. The trigger then compares `global.date` with it.
A successor government copies the war's start date from its predecessor during roster preparation and records its own baseline when it adopts the government role, so the duration still counts from the original opening. A missing start date falls back to the current date rather than blocking the offer forever.
The AI weight (base `event021_ai.base_action`) now reads the war:

| Government | Factor | Weight |
| --- | --- | --- |
| Cohesive authority, not losing ground (SET-01) | 0 | 0 |
| Contested, holding its ground | `ai_holding_ground` 0.25 | 0.25 (negotiator 0.375) |
| Hardliner above Failing (SET-04) | `ai_hardliner_holdout` 0.05, x0.25 holding or x2 lost states | 0.0125 to 0.1 |
| Failing authority | `ai_failing_authority` 3 | 3 (negotiator 4.5) |
| Collapse authority | `ai_collapsed_authority` 5 | 5 |
| Fewer of its own states than after the opening | `ai_lost_ground` 2 | multiplies the above |
| Surrender above `near_defeat_threshold` (0.70) | `ai_near_defeat` 3 | multiplies the above |

"Losing ground" (`event021_government_losing_ground`) is either of the last two rows.
The opening baseline for lost states is `random_civil_war_opening_held_state_count` (`num_owned_controlled_states`), recorded at the commit and again on both host opening paths after `event021_parent_activate_planned_optional_front_rows`, because the Event 006 package and optional fronts take their states after the commit.
The old hardliner x0.75 and failing x1.5 modifiers are replaced. The negotiator x1.5 stays.
Costs, the settlement selector, and the player-side protection in `event021_settlement_offer_blocked` are unchanged.
MCP: one narrow `hoi4.probability_inspect` baseline for this decision returned `INTERNAL_ERROR`, and the single same-scenario `hoi4.probability_compare` was rejected with "Invalid tool arguments". Neither was retried, so the table above is a source trace, not engine evidence.
Basis: the lead's round 2 assignment and the probability matrix rows SET-01, SET-03, SET-04, and SET-05.
The war duration and the AI timing of offers remain `needs_live_game`.

## D22. Prevention actions run on their own cooldown and never consume crisis actions

Finding: in Global Fracture prevention (`event021_country_can_prevent_fracture`, no live crisis) Review Command Loyalty and Protect State Communications wrote the crisis one-shot flags `event021_loyalty_action_used` and `event021_prevention_communications_used`, which only crisis cleanup cleared.
A country that used either action while Stable or Exposed never saw it in its own later civil war, and each prevention action was usable once per game. `random_civil_war_prevention_action_taken` was written and never read.
Decision: both effects branch on `event021_country_can_prevent_fracture` before any other change. Prevention use sets the timed flags `event021_prevention_loyalty_recent` and `event021_prevention_communications_recent` for `constant:event021_action_tuning.prevention_cooldown_days` (180), copied into the temporary `event021_decision_flag_days` first because timed flags cannot take `days = constant:`. Crisis use keeps the once-per-crisis flags.
Visibility and availability read `event021_review_loyalty_offered` and `event021_protect_communications_offered` (parent triggers), which pair each phase with its own flag, so the prevention surface still shows at most these two actions, each returning after its cooldown while the band conditions hold.
`event021_clear_crisis_action_receipts` clears every once-per-crisis action flag. Crisis cleanup, `event021_commit_opening_evolution_provenance`, and `event021_inherit_crisis_opening_evolution_provenance` call it, so a new crisis role starts with all of its actions. The timed prevention cooldowns are not crisis receipts and are left to expire.
The dead `random_civil_war_prevention_action_taken` flag is removed. Costs, effects, and AI weights are unchanged; Review Regional Administration stays out of prevention as `b9dbb2039` decided.
Basis: the lead's round 2 assignment and the crosswalk's two-action prevention surface.

## D23. Hold the Settlement Terms ends on the obligation's hold date and rewards success

Finding: selecting the card started Upholding the Settlement with a fixed 180-day timer, while the obligation is judged at `random_civil_war_settlement_terms_hold_until` (settlement date plus `settlement_terms_hold_days`, 180).
Any selection after the settlement day ran past the hold date, so the parent review judged the obligation first, cleared `random_civil_war_settlement_obligation_active`, and the cancel trigger removed the hold before it could resolve. Even a resolved hold gave no reward.
Decision: `event021_mission_start_settlement_terms_hold` converts the time left (`hold_until - global.date`) to whole days with the shared `chaosx_convert_date_offset_to_days` (output created before the call, rounded up, clamped to at least `settlement_terms_minimum_remaining_days`) into the normal variable `event021_settlement_terms_hold_days`, which the hold mission reads through `days_mission_timeout = var:event021_settlement_terms_hold_days` at activation (vanilla `EST.txt` and `CHI_decisions.txt`, and this repository's `012_africa_decisions.txt`, use the same variable timer).
The card is offered, and stays open, only while `event021_settlement_terms_offer_open` holds: `global.date` is at or before `event021_settlement_terms_last_offer_date`, the hold date less one day through `event021_days_to_date_offset`, recorded by `event021_record_settlement_terms_offer_limit` at every writer of the hold date (obligation selection, the signed-terms branch of the settlement, and the treaty copy to signatories).
`event021_parent_review_settlement_obligation` skips both hold-date branches while `event021_settlement_terms_mission_active` is set. Early breaches still resolve at once and cancel the hold quietly.
Success adds the distinct reward `event021_mission_reward_settlement_terms_upheld`: State Authority +8 (`settlement_terms_authority_gain`), pressure -8 (`settlement_terms_pressure_relief`), and `random_civil_war_settlement_terms_upheld`, which lowers the recurrence score by 15 (`terms_upheld_recurrence_relief`) when reconstruction ends. The flag is generation-local and cleared when the next crisis begins. Failure breaches the obligation as before.
The outcome tooltip names the review date and both outcomes in one line. The card description and commit tooltip name the review date instead of a fixed duration.
Source trace, 180-day obligation selected on day 30: the hold date is day 180 and the last offer date day 179. At selection the offset is 150 days, the converter returns 150, and the hold starts with a 150-day timer ending on day 180. Reconstruction completes at the first review after day 120. Reviews on or after day 180 defer while the hold runs. On day 180 the hold resolves: with the objective met it sets `objective_met`, pays the reward, and the review it calls marks the terms held (reconstruction is complete and the hold date has passed). Without it, the obligation is breached. The next review runs the final block, whose recurrence score includes the relief, and fires `chaosx.nr21.10`.
Basis: the lead's round 2 assignment and the mission families of `021_random_civil_war_spec_part_3_decisions_missions_and_outcomes.md`.
The timer read at activation and the resolution day remain `needs_live_game`.

## D24. Evolution II strange incidents become a visible, counterable report

Finding: `event021_parent_roll_strange_incident` only took 3 State Authority and added 4 pressure on its 8% roll. No event fired, nothing appeared on screen, the side gained nothing, and no countermeasure existed, so the feature required by spec parts 5 and 10 was invisible.
Decision: the 8%/92% roll, its outer gates, and the recent-incident cooldown are unchanged, and the roll is also refused while `event021_strange_incident_active` holds, so a side never runs two incidents.
A success keeps the authority and pressure cost and calls `event021_parent_start_strange_incident`. It names the region (the side's anchor state while it controls it, otherwise its capital), picks one of five practices with equal weights from `event021_strange_incident.variant_weight`, adds the practice as a 90-day timed idea, adds Unease in the Ranks (`event021_strange_incident_strain`: attrition +5%, stability -3%, command power gain -10%) for 120 days, and fires `chaosx.nr21.21`.
The practices follow the spec's directions: Night Assemblies (organization +8%, max planning +10%), Oath Circles (defense +10%, morale +8%), Signal Fires (planning speed +15%, division speed +5%), The Sleepless Column for the endurance rumours (morale +10%, attack +5%), and Relic Procession (recruitable population factor +10%, war support +5%).
The report text describes what witnesses see in the named region and never confirms a cause. Its three options are the countermeasures: leave the practice alone (both ideas run their course and `random_civil_war_strange_incident_tolerated` adds `tolerate_recurrence_pressure` 8 to the recurrence score when reconstruction ends), investigate the organizers (25 political power, the practice ends, the strain stays, State Authority +6), and rotate the affected units (15 army experience, both ideas end). The paid options are hidden when the side cannot afford them.
AI chance by role: leave alone 20 (x3 opposition side, x0.5 hardliner), investigate 30 (x3 hardliner, x0.5 opposition side), rotate 30 (x3 negotiator or consolidator).
A switched-off Evolution II already suppresses the roll. Crisis cleanup calls `event021_cleanup_strange_incident`, which removes both ideas and the report receipts. The tolerated memory stays for the recurrence review and is cleared when the next crisis begins.
Assets: the report reuses `GFX_report_event_021_random_civil_war_opening`, which spec part 9 allows because one image covers the incidents and only one incident event exists. The five practice ideas reuse `idea_021_fractured_command` and the strain reuses `idea_021_war_torn_administration`, following part 9's rule against near-identical new icons.
`event021_evolution_ii_body` gains one sentence on the unexplained practices, as part 9's Evolution II direction asks, and the catalog change is queued in `catalog_changes_pending.md`.
The roll's probability weights are unchanged, so no probability compare is required. The report, its AI answers, and the idea magnitudes in play remain `needs_live_game`.
Basis: the lead's round 2 assignment and spec parts 5, 9, and 10.

## D25. Every settlement changes the aftermath, and a battlefield victory chooses its postwar direction

Finding: spec part 3 has the player choose a postwar direction after a government military victory and lists Unsettled Settlement variants, and part 10 requires every settlement type to change the aftermath, with no recorded exception.
The Fighting Stops had one option, the hardliner profile silently decided harsh classification, and `event021_unsettled_settlement` was the only aftermath idea, added only to negotiated settlements, so autonomy, coalition, and merger played out alike apart from the obligation.
Decision: `event021_parent_apply_settlement` sets `random_civil_war_postwar_direction_pending` for a government victory without signed terms, and The Fighting Stops then offers four directions in place of its single option: amnesty and reintegration (State Authority +4, pressure -8, Amnesty Commissions), trials and institutional reform (30 political power, State Authority +8, Reform Tribunals), a harsh security settlement (State Authority +10, pressure -4, Security Regime), and continued emergency rule (State Authority +6, Continued Emergency Rule).
Only the last two set `random_civil_war_harsh_settlement` and `random_civil_war_failed_settlement`. The old automatic hardliner classification is moved into this choice, and partition stays a harsh settlement as before.
The spec's other two directions, regional autonomy and negotiated local administration, are not victory options because the autonomy compact and coalition settlements already cover them through signed terms. Offering them after a total victory would duplicate those families without a front to negotiate with.
AI governments choose by profile with zeroed alternatives (hardliner security settlement, consolidator reform, negotiator amnesty, no profile an even pick among those three), and AI never chooses emergency rule. `event021_resolve_pending_postwar_direction` applies the same default if the event is still unanswered when reconstruction ends.
While a direction is pending, the settlement defers `event021_parent_record_achievement_receipts` (clearing the opening-states receipt) until the direction is chosen, so a later harsh choice is known before No State Left Behind is judged. The achievement predicates are unchanged.
`event021_apply_settlement_aftermath` gives every other family its own idea in the obligation selector's order: Recognized Border for independence or a recognition obligation, Foreign Patronage for a sponsor-repayment obligation, Autonomy Compact, Power-Sharing Council for coalition or merger, and Armistice Line for partition. An opposition victory or a negotiated multi-front settlement keeps Unsettled Settlement.
`event021_clear_settlement_aftermath` removes every aftermath idea when the obligation is fulfilled or breached (`event021_parent_review_settlement_obligation`) and at crisis cleanup.
Assets: all nine aftermath ideas reuse `idea_021_unsettled_settlement`, following part 9's rule against near-identical new icons.
Signed terms keep their single option. The settlement selector, the obligation selector, and the achievement predicates are unchanged. Accepted design merged into spec part 3 ("Accepted postwar direction and settlement aftermath") with its manifest hash refreshed. No catalog field changes.
The direction choice, AI defaults, and idea magnitudes in play remain `needs_live_game`.
Basis: the lead's round 2 assignment and spec parts 3 and 10.

## D26. The category shows phase, pressure, and the Global Fracture band

Finding: spec part 3 asks the category to show the current stage, one objective, and one summary of the strongest visible pressure, and part 6 asks Stable countries to see their band and Critical countries a visible emergency. The category text showed only State Authority, its band, guidance, and the current focus, `event021_GetCrisisPhase` and `event021_GetCrisisSummary` had no consumer, and a prevention country read "State Authority: N/A (N/A)".
Decision: `event021_civil_war_crisis_category_desc` is `[event021_GetCategoryStatus]`, which picks one of three lines. A crisis, settlement, or reconstruction side reads its phase, State Authority with band and guidance (the objective), one pressure summary, and its current focus. An exposed neighbour reads its phase, the exposure summary, and the source war. A prevention country reads its band from `event021_GetFractureBand` (the `random_civil_war_pressure_is_*` triggers, Stable without a pressure record) and one resilience or emergency line from `event021_GetFractureBandSummary`.
The phase getter now names Settlement before Reconstruction while the obligation is open and uses the opening phase for the opening scramble. The summary getter is ordered by severity: settlement, reconstruction, exposure, lost or threatened capital, lost supply, Failing or Collapse authority, command or political claimants, and an active-war fallback.
No raw pressure value or implementation term is shown, and the localisation file stays UTF-8 with BOM. Rendering in the decision panel remains a live or MCP GUI check (`needs_live_game`).
Basis: the lead's round 2 assignment and spec parts 3 and 6.

## D27. The end of a crisis is reported, and a breached obligation counts against the peace

Finding: the final reconstruction block fired only the hidden cleanup `chaosx.nr21.10`, whose unused text keys claimed every obligation had been met. The player never learned whether the settlement obligation held, although it decides recurrence and The Terms Hold, and a breach had no effect on the recurrence score.
Decision: the final block fires the visible report `chaosx.nr21.22` (The Peace Is Judged) immediately before `chaosx.nr21.10`, whose content and timing are unchanged. The report names the obligation through `event021_GetSettlementObligationName`, picks its description from `random_civil_war_settlement_obligation_breached`, and states the consequence through `event021_GetSettlementVerdictConsequence`. Its AI chance is 100.
It reads only the obligation variable and flags, which crisis cleanup leaves in place until the next settlement or crisis, so the report is correct even if the cleanup event is processed first.
To make the stated consequence true, `event021_prepare_recurrence` adds `breached_obligation_pressure` (15) to the recurrence score for a breached obligation, as the recurrence matrix row REC-05 (broken guarantee, strong increase) expects. The orphaned `chaosx.nr21.10.t/.d/.a` keys are replaced by the `chaosx.nr21.22` keys.
The recurrence change and the report timing remain `needs_live_game`, and no MCP probability compare was run because the probability routes failed earlier in this round.
Basis: the lead's round 2 assignment and the probability matrix row REC-05.

## D28. Fractured Command changes from the opening actions are explicit

Finding: every side starts with a permanent `event021_fractured_command`, and Defend the Capital (30 days) and Review Command Loyalty (45 days) called `add_timed_idea` on it while it was present. The installed `add_timed_idea` documentation and the wiki Effects page do not define that case, so the penalty could be ignored, turned into a short timer stronger than Secure the Arsenals' conversion, or reset, and no tooltip mentioned it.
Decision: no action calls `add_timed_idea` on a present idea. The helpers `event021_fractured_command_set_timed`, `_extend`, `_shorten`, and `_end` remove before adding, use the documented `modify_timed_idea` with positive or negative days, and record the end date in `event021_fractured_command_until` through the shared date converter, so `event021_fractured_command_is_timed` and `event021_fractured_command_is_permanent` (parent triggers) can tell the two apart.
Secure the Arsenals gives a permanent penalty a 45-day end date and leaves a timed or absent one alone. Integrate Loyal Formations ends it. Defend the Capital no longer touches it. Review Command Loyalty, careful branch: a permanent penalty gets a 45-day end date and a timed one ends 15 days sooner (`loyalty_shorten_days`), ending at once when no more than 15 whole days remain, which the converter measures. Hardliner branch: a timed penalty lasts 30 days longer (`loyalty_extend_days`), an ended one returns for 45 days, and a permanent one stays.
The unused `capital_idea_days` constant is removed. `event021_clear_crisis_action_receipts` clears the timer record, so a new crisis starts from a permanent penalty.
The Secure the Arsenals, Review Command Loyalty, and Integrate Loyal Formations tooltips state the change. Review Command Loyalty picks its profile branch through `event021_GetLoyaltyReviewOutcome`. Costs and AI weights are unchanged.
Basis: the lead's round 2 assignment, `effects_documentation.md` (`add_timed_idea`, `modify_timed_idea`), and the wiki Effects page.

## D29. Neighbour mediation opens settlement talks in the mediated war

Finding: spec part 5 says Mediate a Local Ceasefire can open settlement talks, but `event021_decision_offer_mediation` changed only the mediator's own authority, pressure, exposure, and flags, and `event021_mediation_until` had no consumer.
Decision: mediation calls `event021_record_mediation_receipt`, which follows the mediator's `random_civil_war_exposure_source_country_scope` to the government of that war (the source itself, or a claimant's host government) and gives it `random_civil_war_mediator_scope` and `random_civil_war_mediation_until`, the current date plus the existing `mediation_days` (90) through `event021_days_to_date_offset`. The mediator-side `event021_mediation_until` write is replaced by this receipt.
`event021_settlement_mediation_live` (the receipt has not expired and the mediator exists) lets `event021_settlement_offer_ready` pass before the minimum war duration from D21. Offer Emergency Terms' requirement line comes from `event021_GetSettlementOfferReadyLine` and names the mediator and the receipt's end date, and the mediation tooltip names the mediated government and what the talks allow.
Terms signed while the receipt is live count as negotiated even for a partition, so `random_civil_war_settlement_negotiated` follows the mediated agreement. The partition's harsh classification and every settlement gate are unchanged.
The government's Offer Emergency Terms AI weight gains `ai_mediated` (x2) while the receipt is live, so AI governments answer mediation, still never from a Cohesive position held without losses. Mediator AI weights are unchanged.
The receipt expires on its date and `event021_clear_crisis_action_receipts` clears it at crisis cleanup and at any new crisis role.
Basis: the lead's round 2 assignment, spec part 5 (Mediate a Local Ceasefire), and decision D21. The mediated offer remains `needs_live_game`.

## D30. A government chooses its opening posture

Finding: spec part 9 asks important government options to express a posture (firm command, constitutional response, or cautious containment) with a stated public response and visible consequence, but the opening reports `chaosx.nr21.2` and `chaosx.nr21.3` had one option, and `event021_parent_assign_government_profile` picked the hardliner, negotiator, or consolidator profile from authority and pressure without the player's input, although that profile decides the loyalty-review branch and the government AI's terms and postwar choices.
Decision: both government opening reports offer three postures while `event021_opening_posture_available` holds (a government side that is human, or an AI with an assigned profile). Holding firm sets the hardliner profile and raises State Authority by 6, appealing to the constitution sets the negotiator profile and lowers pressure by 6, and containing the rising sets the consolidator profile and grants 15 command power. Each tooltip states that consequence and the loyalty-review branch the profile takes, and the values live in `event021_opening_posture`.
Each posture option has AI chance 100 for its own profile and 0 otherwise, so an AI government keeps the profile it was assigned. An AI government without a profile, such as a same-tag government, and every non-government recipient keep the plain report option.
The profile helper `event021_clear_government_profile` is shared with `event021_parent_assign_government_profile`. Claimant (`chaosx.nr21.7`) and Event 006 (`chaosx.nr21.8`) reports and the AI strategy files are unchanged.
Basis: the lead's round 2 assignment and spec part 9. The posture choice in play remains `needs_live_game`.

## Round 2 tool evidence (D21 to D30)

`hoi4.probability_inspect` for `event021_offer_emergency_settlement` returned `INTERNAL_ERROR`, and `hoi4.probability_compare` rejected its arguments. Neither was retried (D21).
One narrow `hoi4.event_inspect` lint with selector `{ kind: event, eventId: chaosx.nr21.21 }`, depth 1 and 20 nodes, returned `EVENT_INSPECTED_PARTIAL` at revision `8153b19347fc69b5430657d9f6e7272ecde8e9e62df61e88eaa690972433d344` with zero blocking diagnostics. The server deferred whole-workspace helper projections, so it lists every Event 021 scripted helper, old and new, as an unresolved helper. That is a coverage limit of the run, not a finding, and the lint is not engine evidence for the new helpers.
Source checks run on every touched script file: braces balance with comments removed, every `constant:` token resolves to a category with a schema block, every called `event021_*` effect or trigger is defined, every localisation key and `event021_Get*` scripted localisation referenced from the Event 021 event, decision, idea, and scripted localisation files exists, and the localisation file keeps its UTF-8 BOM.
No decision or GUI render was attempted. The category text (D26), the new reports (D24, D25, D27, D30), and every timing claim remain `needs_live_game`.

## D31. Round 2 review: two text corrections

A source review of the round 2 commits (`c25f7139a` to `a06a553c9`) found two player-facing lines that could state something false.
Review Command Loyalty's careful branch always described a Fractured Command change, but a country in Global Fracture prevention, or a crisis side whose Fractured Command was already ended by Integrate Loyal Formations, has none to change. `event021_GetLoyaltyReviewOutcome` now picks `event021_review_loyalty_outcome_steady`, which omits that sentence, for a non-hardliner without the idea. The hardliner line is unchanged because an ended penalty does return for that profile.
The breached description of The Peace Is Judged (`chaosx.nr21.22.d_breached`) opened with "The date set by the settlement has passed", but an obligation breached early reaches the final reconstruction block on the first review after reconstruction completes, before the hold date. It now opens with "Reconstruction is over", which is true on both paths. The held description keeps its wording because a held obligation is only judged at or after the hold date.
No gameplay, cost, constant, or AI weight changed. Both lines remain `needs_live_game` for rendering.
Basis: the lead's round 2 assignment (D24 to D30 acceptance asks for plain, accurate tooltips and report text).

## D32. Round 2 skeptical review: verdict and integration text

A second source review of every round 2 commit (`c25f7139a` to `539b55887`) found no engine, scope, constant, key, or brace defect, and two more player-facing lines that claimed more than the script does.
The Peace Is Judged stated for every held obligation that renewed civil war becomes less likely, but `event021_prepare_recurrence` lowers the score for a held settlement only when Hold the Settlement Terms upheld it (`random_civil_war_settlement_terms_upheld`, `terms_upheld_recurrence_relief`). `event021_GetSettlementVerdictConsequence` now picks `event021_settlement_verdict_upheld` for that case, and the plain held line says only that no broken terms add to the risk. The breached line no longer promises that former opponents distrust new terms, which no script models; it keeps the true recurrence increase (`breached_obligation_pressure`).
Integrate Loyal Formations lowers pressure (`integration_pressure_cost`, -6) but its tooltip omitted it, so `event021_integrate_formations_tt` now says it eases internal division.
No gameplay, cost, constant, or AI weight changed. A narrow `hoi4.event_inspect` lint of `chaosx.nr21.22` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics (revision `7bfe6f10fabba881405c51fc8bc2b3ee154c825436f2aa99428725b935b994d8`), and `hoi4.probability_inspect` for the Offer Emergency Terms AI weight rejected its arguments again, so the D21 table stays a source trace. Both lines remain `needs_live_game` for rendering.
Basis: the lead's round 2 assignment (plain, accurate tooltips and report text).

## D33. State Authority conditions change it once, on the transition

Finding from the round 3 lead review: `event021_add_authority` re-added every standing condition flag on every call. `random_civil_war_capital_lost` and `random_civil_war_admin_restored` were never cleared, and `random_civil_war_capital_secured` was cleared only by the next achievement receipt pass. After a settlement the amnesty (+4 in its tooltip) gave +12, every Reconstruct the Administration or reconstruction tick gained an extra +8, and a later crisis shifted every change by -6 or +14, turning losses such as the strange-incident cost into gains.
Decision: `event021_add_authority` applies exactly `random_civil_war_pending_authority_delta` (nothing when it is absent), clamps, and refreshes the band. The default delta and the then-unused `admin_restored` constant are removed.
Conditions change State Authority once, through transition helpers: `event021_authority_capital_lost` and `_regained` own `random_civil_war_capital_lost` (`capital_lost` -12 on the loss, `capital_secured` +8 on the recovery), and `event021_authority_supply_state_lost` and `_regained` own the bound supply-state flags (`rail_or_depot_lost` -5 and `supply_secured` +5, with `random_civil_war_supply_lost` set while any bound state is lost). D34 wires them to the war.
`event021_clear_authority_conditions` removes every condition flag, the contested-state count, and the recorded crisis capital. Crisis cleanup, the annexation teardown, and both new-role helpers call it.
The settlement no longer sets a capital flag from the opening's remnant proof, and the final reconstruction block no longer sets `random_civil_war_admin_restored`.
`random_civil_war_capital_secured` is now only the Hold the Center receipt: the achievement receipt pass still clears and writes it, and `event021_begin_achievement_history` clears it when a new crisis begins, so an earlier war's receipt cannot satisfy the achievement. While a postwar direction is pending, the receipt is absent until the direction is chosen and the deferred receipt pass runs.
Source trace (government at 60, no conditions): settlement +10 to 70; The Fighting Stops amnesty +4 to 74; Reconstruct the Administration +8 to 82; reconstruction tick +5 to 87; the final block changes nothing; cleanup clears the conditions; in a second crisis Secure the Arsenals adds exactly +5. Each change equals its tooltip constant. The capital summary line now appears only while `random_civil_war_capital_lost` is set in the current crisis.
Basis: the lead's round 3 assignment and spec part 2 ("It changes through" its listed sources).

## D34. State Authority follows the war

Finding from the round 3 lead review: spec part 2 says State Authority changes through capital, rail and depot control, key territory, victory, negotiations, repression, and foreign intervention, and the overview and the category summary promise it, but every side started at the default 70 and only actions moved it, almost always upward. `rail_or_depot_lost`, `victory`, and `defeat` were unused, and ten condition flags plus `random_civil_war_contested_state_count` were read but never set, so Failing and Collapse were practically unreachable and the D21 terms weights, the Failing and Collapse summary, the faster Evolution I timing at low authority, and Hold the Center's Collapse clause never came into play.
Decision, with the constants in `random_civil_war_authority`:
- Opening. `event021_apply_government_opening_authority` runs in `event021_random_civil_war_commit_opening` after the achievement history starts. It caps State Authority at the default 70 and applies a one-time loss by severity: Limited -8 (62, Contested), Serious -20 (50, Contested), Severe -32 (38, Failing), Critical -42 (28, Failing). The region was already sized from the pre-opening value. Claimants start at `claimant_opening` 50 and Event 006 fronts at `independence_front_opening` 60 through `event021_apply_claimant_opening_authority`, which every claimant initializer calls. Each side records its crisis capital.
- Control changes. The existing `on_state_control_changed` hook (ROOT new controller, FROM old controller, FROM.FROM state; vanilla `common/on_actions/00_on_actions.txt` line 5075 and the wiki On actions page line 450) calls `event021_authority_review_lost_state` on FROM and `event021_authority_review_gained_state` on ROOT, only while `event021_authority_follows_control` holds (a live crisis side outside its settlement and reconstruction phases). The crisis capital applies `capital_lost` -12 and `capital_secured` +8, and a bound rail or priority-front depot state `rail_or_depot_lost` -5 and `supply_secured` +5, once per transition. No world iteration or periodic hook is added.
- Territory. `event021_review_held_territory` compares owned-and-controlled states with `random_civil_war_opening_held_state_count` (D21), stores the shortfall in `random_civil_war_contested_state_count`, and applies `territory_state_lost` -2 for each state of change, so every lost state costs its share once and a recovered state returns it. It sets `random_civil_war_contested_territory` from one lost state and `random_civil_war_key_state_lost` from `key_territory_states` 2, which feed Fracture Pressure, and `random_civil_war_capital_supply_risk` for a capital without a supply node or bordering a state held by an enemy, which feeds the capital summary and Protect State Communications' AI. Re-recording the baseline when the opening's own fronts have formed returns any charge for states they took. The bounded country review (`event021_review_crisis_conditions`) re-measures, records a missing claimant baseline, and ends a lapsed intervention.
- Settlement. `event021_apply_settlement_outcome_authority` adds `victory` +15 for the side whose war aims prevailed (government victory, claimant victory, independence or partition successor) and `defeat` -15 for a government that lost the war or territory to it; autonomy, coalition, merger, and negotiated multi-front settlements add neither. The territory and capital-risk conditions end with the war.
- Former dead inputs. `random_civil_war_negotiation_active`: a neighbour's mediation first reaching the government gives `negotiation` +4 once per crisis role, stated in the mediation tooltip. `random_civil_war_foreign_intervention_active`: a sponsor arming the government's opponents costs it `foreign_intervention` -6 once while an intervention is live, recorded with the sponsor in `random_civil_war_foreign_sponsor_scope` and stated in the Support the Opposition tooltip; it ends when the sponsor's commitment lapses. Repression: a hardliner's loyalty purge now uses `repression` -4, and the duplicate `hardliner_authority_cost` and the never-set `random_civil_war_repression_active` are removed. `random_civil_war_supply_secured` and the `supply_lost` constant are removed, and `random_civil_war_supply_lost` marks a lost bound supply state. The political summary line reads a government whose primary claimant took the ideological route (`random_civil_war_ideological_route_reserved`) in place of the never-set `random_civil_war_ideological_claimant`. `random_civil_war_humanitarian_pressure` belongs to the Evolution II exposure work and is settled with it below.
- Presentation. The opening reports (`chaosx.nr21.2`, `.3`, `.7`, `.8`) and both The Fighting Stops descriptions end with `event021_authority_report_line`, which states the current value and band.
Source trace, Serious minor opening (pre-crisis 70, Cohesive): the opening takes it to 50 (Contested). Losing the capital applies -12 and -2 for the lost state, 36 (Failing). Retaking it returns +8 and +2, 46 (Contested). Losing two core states applies -4, 42 (Contested), and sets contested and key territory for Fracture Pressure. A government victory adds the settlement +10 and victory +15, 67 (Contested). The band moves Cohesive, Contested, Failing, Contested.
D21 reacts: while Failing the government's Offer Emergency Terms weight takes `ai_failing_authority` x3 and, with states lost, `ai_lost_ground` x2; a Contested government holding its ground keeps `ai_holding_ground` x0.25 instead of the Cohesive zero, so a contested government can occasionally seek terms. The strong-settlement threshold 75 is now earned by actions (posture, arsenals, capital defense, loyalty, integration, held missions) rather than met by default, so signed terms from a weakened government lean to partition or coalition.
Hold the Center: the opening always lowers the government's authority, so its minimum tracks a war that actually tested it, and the Collapse clause can now fail.
The probability compare for the Offer Emergency Terms weight shift is recorded as blocked: the probability routes returned `INTERNAL_ERROR` or rejected their arguments in rounds 1 and 2, and the lead's round 3 instruction is not to retry them. Runtime feel and the hook's behaviour during engine state transfers are `needs_live_game`.
Basis: the lead's round 3 assignment, spec part 2 ("Opening State Authority"), and overview line 47.
