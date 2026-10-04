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
