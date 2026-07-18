# Event 15 Necessary Ground and Stewardship Architecture Review

> Current disposition, 2026-07-15: this is a historical architecture snapshot. The lifecycle defects and four open design questions were dispositioned during implementation. Temporary market access was omitted in favor of exact resource rights. Target disappearance now uses reverse founder records, a narrow annexation callback, successor adoption during active stewardship, explicit founder-extinction failure, pre-steward invalidation, enforcement-peace cleanup, and last-state transfer gates. Settlement, long-supply, association, and island-lease terms are centrally timed. Integrated-state ownership loss removes its flag, modifier, and array record. `decision_mission_completion_current_reaudit_2026_07_15.md` passes the current target lifecycle, founder attribution, auxiliary atomicity, and founder-local prefire state with no open P0 through P3 finding.

## Handoff metadata

- Role: `chaosx_scripted_system_architect`
- Review date: 2026-07-14
- Mode: read-only architecture audit
- Gameplay files edited by this review: none
- Parent ownership: final implementation, wiring, localisation alignment, validation, and commit
- Snapshot note: the parent was actively patching while this review ran. The three refusal and ultimatum sign errors were rechecked after the parent correction and are not listed as open defects.

## Executive verdict

The current implementation has a viable foundation. The prefire country scan is one-shot, the Necessary Ground target scan is one-shot, persistent decision target arrays are a reasonable fit, and the new dynamic state modifiers use clear state flags and self-removing `remove_trigger` blocks.

The Necessary Ground and stewardship systems are not completion-ready as a state machine. Several terminal paths leave missions, flags, diplomatic relations, or pointers alive. An ultimatum can currently unlock enforcement before the target answers. Generic `take_state` cleanup can delete an unrelated wargoal. Return logic always transfers ownership even for lease and joint administration. Revolt processing erases the scopes that its response event needs. The implementation also treats the six domestic deficit families as if they were the six accepted external case types from the specification.

The parent should patch the lifecycle kernel before adding more presentation or balance work.

## Sources consulted

The review followed `chaos-redux-events`, `hoi4-decisions-missions`, and `chaos-redux-subagents`.

The required offline wiki pages were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The vanilla documentation and examples consulted included:

- `documentation/script_concept_documentation.md`
- `documentation/script_collection_input.md`
- `documentation/script_collection_operator.md`
- `documentation/effects_documentation.md`
- `documentation/triggers_documentation.md`
- `common/script_constants/documentation.md`
- `common/on_actions/_documentation.md`
- `common/wargoals/00_invasion.txt`
- Vanilla on-action, decision, event, diplomatic relation, resource-rights, and state-transfer precedents

The accepted Event 15 specifications and matrices under `docs/specs/015_utopia_manifesto_specs/` were treated as the design authority.

## Required runtime invariants

These invariants should be represented by scripted triggers and enforced at every mutation boundary.

| State | Required invariant |
| --- | --- |
| No active case | No active case target or state array, no case response, no case expiry mission, no Event 15 wargoal, and no case-scoped variables |
| Claim drafted | Exactly one active target, matching `utopia_manifesto_case_target_id`, no state required yet, and stage equals claim |
| State assessed | Exactly one active target and one active state, both matching stored IDs, and the state owner matches the active target |
| Response pending | Exactly one current offer method, response flags cleared before dispatch, one targeted wait mission, and no settlement result flag |
| Ultimatum pending | Ultimatum method set, prior settlement refusal cleared, response active, and enforcement unavailable |
| Enforcement authorized | Exact Event 15 wargoal present against exact target, selected state retained, expiry lifecycle defined, and no duplicate grant possible |
| Enforcement war active | Case pointers retained, case expiry suspended or reconciled, and stewardship cannot start from occupation alone |
| Stewardship active | Exactly one target and one state, one settlement method, per-case stewardship progress reset, and no terminal status selected |
| Terminal return | Method-specific ownership or control restored, temporary modifiers removed, temporary diplomatic relations removed where supported, missions removed before flags clear, and all case pointers cleared |
| Terminal integration | Long integration proof completed, ROOT owns the state, persistent state marker has an ownership lifecycle, missions removed, and all case pointers cleared |
| Revolt pending | Dedicated revolt target and state pointers remain available until the response choice resolves them |

## Findings by priority

### P0. Reset response state before every offer and ultimatum

Current identifiers:

- `decision_utopia_offer_purchase_or_supply`
- `decision_utopia_offer_long_supply_contract`
- `decision_utopia_request_lease`
- `decision_utopia_propose_joint_administration`
- `decision_utopia_offer_association`
- `decision_utopia_issue_need_ultimatum`
- `mission_utopia_wait_for_need_answer`
- `utopia_manifesto_refuse_case_settlement`
- `chaosx.nr15.200` through `chaosx.nr15.205`

The founder-side result flags persist across negotiation rounds. In particular, `utopia_manifesto_case_settlement_refused` remains set when `decision_utopia_issue_need_ultimatum` activates a new wait mission. The mission can therefore complete immediately, clear `utopia_manifesto_case_response_active`, and expose `decision_utopia_enforce_need_case` before `chaosx.nr15.204` is answered.

Required fix:

1. Add `utopia_manifesto_clear_case_response_state`.
2. Remove an existing targeted wait mission from the exact active target.
3. Clear target-side `utopia_manifesto_case_response_accept`, `utopia_manifesto_case_response_counter`, and `utopia_manifesto_case_response_refuse`.
4. Clear founder-side accepted, countered, refused, and all `utopia_manifesto_case_offer_*` flags.
5. Add a distinct `utopia_manifesto_case_ultimatum_refused` flag.
6. Add `utopia_manifesto_begin_case_response`, which calls the clear helper, records exactly one method and offer, sets response active, activates one targeted mission, then fires the target event.
7. Require `utopia_manifesto_case_ultimatum_refused` for enforcement. Do not use the generic settlement refusal flag.

The response bridge `chaosx.nr15.205` also calls `utopia_manifesto_record_case_offer` on acceptance even though the sending decision already records the offer. Remove that second call so offer count and local support are not doubled.

Every target response option should require a live exact case and no war with the founder. The bridge should revalidate the target ID, state ID, method, response-active flag, and peace state before applying settlement. This prevents a delayed human event from accepting terms after war or invalidation.

### P0. Stewardship terminal helpers must remove missions before clearing flags

Current identifier: `utopia_manifesto_clear_stewardship_runtime`.

It clears only the active, proven, and charter-recorded flags plus three counters. It does not remove:

- `mission_utopia_emergency_provision`
- `mission_utopia_restore_stewardship_route`
- `mission_utopia_hold_charter_period`
- `mission_utopia_long_integration`

It also leaves their activation and progress flags. A return or integration while one of those missions is active causes the mission to cancel on the next evaluation. Its cancel effect can then fail the already-closed stewardship or fire a revolt.

Required fix:

1. Add `utopia_manifesto_remove_active_stewardship_missions`.
2. Remove each of the four missions if active.
3. Clear `utopia_manifesto_stewardship_provision_active`, `utopia_manifesto_stewardship_route_active`, `utopia_manifesto_stewardship_charter_period_active`, and `utopia_manifesto_stewardship_integration_active`.
4. Call this helper as the first operation in every stewardship terminal helper.
5. Do not rely on `utopia_manifesto_remove_all_active_missions`, which is a full Event 15 shutdown helper rather than a case terminal helper.

### P0. Do not let target clearing strand an active case

Current identifier: `decision_utopia_clear_necessary_ground_target`.

The decision is available whenever no response is active. It does not exclude `utopia_manifesto_need_case_active`. Clearing `utopia_manifesto_selected_country_targets` during an active case makes all targeted settlement, conversion, ultimatum, and enforcement decisions lose their target while the active case remains.

Required fix:

- Add `NOT = { has_country_flag = utopia_manifesto_need_case_active }` to visibility and availability.
- If the design wants an active-case clear action, route it through a complete renunciation or invalidation helper instead of clearing only the selected pointer.

### P0. Give enforcement its own wargoal identity and war lifecycle

Current identifiers:

- `utopia_manifesto_enforce_active_need_case`
- `utopia_manifesto_remove_active_case_wargoal`
- `decision_utopia_enforce_need_case`
- `on_state_control_changed`

The implementation creates and removes the generic `take_state` wargoal. `remove_wargoal` identifies a wargoal by type and target, not by the state generator. Cleanup can therefore remove an unrelated player-created `take_state` wargoal against the same country.

The reusable effect also depends on `FROM` inside a state loop. It is safe only when called from the current targeted decision scope. Event or on-action reuse can bind a different `FROM`.

The vanilla `take_state` type has its own expiry. The case mission has different route-dependent expiry values. The current implementation does not define how those clocks reconcile. It also does not prevent a duplicate grant.

Required fix:

1. Add a dedicated wargoal type such as `utopia_manifesto_necessary_ground_take_state` in an Event 15 wargoal file.
2. Make it unavailable to normal justification and generation paths.
3. Use only that exact type in `create_wargoal`, `has_wargoal_against`, and `remove_wargoal`.
4. Save the one active target as a regular event target before entering the state loop. Use `event_target:utopia_manifesto_case_wargoal_target` as the wargoal target.
5. Gate the grant against an existing exact Event 15 wargoal.
6. Define expiry ownership. A safe design is for the dedicated type to have the maximum lawful prewar expiry while the case mission performs earlier explicit removal for limited cases.
7. On an exact `on_war_relation_added`, set `utopia_manifesto_case_enforcement_war_active` and remove or suspend the case expiry mission.
8. On peace, resolve the exact case once. Start stewardship only if ROOT owns the selected state. Otherwise run an enforcement-failure cleanup that does not count as voluntary renunciation.

`on_state_control_changed` currently starts stewardship when ROOT becomes controller of the marked state. Wartime occupation is enough to satisfy that branch. Require ROOT ownership and a matching enforcement resolution. Control alone must not convert an occupation into settlement.

### P0. Terminal helpers must own pointer cleanup and method-specific restoration

Current identifiers:

- `utopia_manifesto_return_stewardship`
- `utopia_manifesto_integrate_stewardship`
- `utopia_manifesto_restore_active_case_state_to_target`
- `utopia_manifesto_fail_invalid_stewardship_case`
- `utopia_manifesto_expire_active_need_case`

The return and integration helpers do not clear `utopia_manifesto_selected_country_targets` or `utopia_manifesto_selected_country_id`. Some decisions clear them afterward, but event paths do not. The helper itself must own complete terminal cleanup.

`utopia_manifesto_restore_active_case_state_to_target` always transfers state ownership to the original target. That is wrong for lease and joint administration, where the target remains owner and only control should be restored. It can also steal a state from a third party if ownership changed during the case.

Required fix:

- Add method-specific settlement exit helpers.
- Purchase, accepted ultimatum, and completed enforcement may return ownership only if ROOT still owns the state.
- Lease and joint administration restore control to the owner and do not transfer ownership.
- If a third party owns the state, do not transfer it silently. Invalidate or reconcile according to an explicit design decision.
- Remove temporary military access and guarantees with documented `diplomatic_relation = { country = X relation = military_access active = no }` and guarantee equivalents when the agreement ends.
- Do not assume a reversible market-access effect. No supported market-access removal was confirmed in the reviewed vanilla documentation or examples. Either make that grant intentionally durable and document it, or omit the temporary grant until a supported reversal is verified.
- Clear `utopia_manifesto_purchase_settlement_state` in every terminal and invalidation path.
- Call `utopia_manifesto_clear_selected_country_target` from return, integration, revolt resolution, expiry, invalidation, and enforcement failure.

### P1. Split header validity from assessed-case validity

Current identifier: `utopia_manifesto_active_need_case_is_valid`.

It always requires `utopia_manifesto_case_state_id` and a live active state. A newly drafted claim intentionally has no state until assessment. `on_state_control_changed` validates any active case when the founder gains control of any state, so an unrelated state-control change can invalidate a legitimate claim-stage case.

Required fix:

- Add `utopia_manifesto_active_need_case_header_is_valid` for the target, target ID, stage, method, and core variables.
- Add `utopia_manifesto_assessed_need_case_is_valid` for the exact one-state invariant and state ID.
- Make `utopia_manifesto_active_need_case_is_valid` stage-aware.
- In `on_state_control_changed`, validate only if the changed state is the exact active state or an active state ID is already stored.

### P1. Enforce exact array cardinality and ID equality

Current one-item arrays:

- `utopia_manifesto_selected_country_targets`
- `utopia_manifesto_active_case_targets`
- `utopia_manifesto_active_case_states`

The validity triggers use `any_of_scopes`, which accepts a valid member even if a stale second member exists. Add exact cardinality and ID checks:

- `utopia_manifesto_selected_country_targets^num = 1`
- `utopia_manifesto_active_case_targets^num = 1`
- `utopia_manifesto_active_case_states^num = 1`
- The country scope ID equals `utopia_manifesto_selected_country_id` or `utopia_manifesto_case_target_id`.
- The state scope ID equals `utopia_manifesto_case_state_id`.

Keep the case candidate array persistent because targeted decisions need it. Continue to clear candidate flags before rebuilding it.

### P1. Predeclare the weighted candidate temp variable at the caller boundary

Current identifiers:

- `utopia_manifesto_prepare_candidate_weight`
- `utopia_manifesto_add_current_country_to_candidate_pool`

The helper creates `utopia_manifesto_candidate_weight` as a temporary variable, then its caller uses the variable as the loop end. The offline Data structures reference warns that a temporary variable first created inside a nested scripted effect may not survive back to the caller. A temp variable that is predeclared by the caller can be modified safely by the nested effect.

Required fix:

```txt
utopia_manifesto_add_current_country_to_candidate_pool = {
	set_temp_variable = { utopia_manifesto_candidate_weight = constant:utopia_manifesto_candidate_limits.ticket_minimum }
	utopia_manifesto_prepare_candidate_weight = yes
	# existing ticket loop
}
```

The three weighted prefire arrays are otherwise correctly one-shot and are cleared before and after selection.

### P1. Separate calling deficit family from accepted external case type

Current identifiers:

- `utopia_manifesto_case_family`
- `utopia_manifesto_case_family_context`
- `utopia_manifesto_state_is_relevant_to_case_context`
- `utopia_manifesto_case_candidate_is_valid`
- `utopia_manifesto_from_state_is_valid_case_state`

The code maps the six domestic calling families directly onto external territory. The accepted specification defines different external case types:

- port access
- defensive corridor
- essential resource
- settlement and housing
- island or capital refuge
- reconstruction zone

The current relevance trigger is broad enough that ordinary populated or developed states qualify for several families. It proves that a state has population, infrastructure, or a building, not that the state addresses the deficit or that taking it is proportionate.

Required architecture:

1. Keep `utopia_manifesto_case_family` as the domestic deficit that relief will modify.
2. Add a `utopia_manifesto_case_type` script constant enum and stored country variable.
3. Branch state relevance on case type, not directly on calling family.
4. Add `utopia_manifesto_case_state_is_relevant` and method-eligibility triggers.
5. A candidate country may qualify if one owned and controlled state supports one eligible case type.
6. State selection locks the exact state and case type.
7. Relevance, proportionality, alternatives review, and local support should all be evaluated against that exact type and state.

### P1. Make domestic alternatives a family-bound survey result

Current identifiers:

- `utopia_manifesto_prepare_case_integrity`
- `utopia_manifesto_resolve_domestic_alternatives`
- `utopia_manifesto_domestic_alternatives_reviewed`
- `utopia_manifesto_case_domestic_alternatives`
- `utopia_manifesto_case_has_domestic_alternative`

`utopia_manifesto_prepare_case_integrity` currently sets the domestic-alternative variable merely because the founder controls more than one state. All three survey outcomes also set the same required numeric value, including the outcome named `utopia_manifesto_no_domestic_alternative_found`. The global reviewed flag then remains valid for later deficit families.

The survey changes aggregate Need but does not relieve the calling-family severity, so a successful domestic solution cannot actually close the calling deficit.

Required fix:

- Remove the controlled-state shortcut.
- Use a flag for the reviewed true or false state and a variable only for the prepared family enum.
- Store `utopia_manifesto_domestic_review_family` when the survey starts.
- Require it to match `utopia_manifesto_prepared_case_family` when drafting.
- Distinguish found, partial, and none. Do not encode all three as the same passing value.
- When a domestic solution is found, call a family-specific relief helper before refreshing the calling state.
- Clear or supersede the review proof when the dominant family changes.

### P1. Enforce the peaceful escalation ladder

The specifications require attempts and escalation history, but all peaceful settlement methods can currently be selected as the first offer once the survey proof exists. Association can be the first proposal.

Add a per-case progression enum or flags such as:

- `utopia_manifesto_case_trade_attempted`
- `utopia_manifesto_case_lease_attempted`
- `utopia_manifesto_case_settlement_attempted`
- `utopia_manifesto_case_joint_attempted`

Gate each method by its accepted predecessor or by a route-specific lawful exception. A coercive route that skips the peaceful ladder should record the skip as conduct and pay its intended integrity and Concord cost.

### P1. Route-specific agreements need real terms and cleanup

| Method | Current result | Required architecture |
| --- | --- | --- |
| Purchase | Ownership transfers to ROOT and stewardship begins | Pay target-side compensation or another explicit consideration. Record purchase as a territorial compact, not automatically as associate recognition. |
| Long supply contract | Resource rights and market access are granted, then the case closes immediately | Persist exact target and state, contract term, expiry or renewal, and resource-rights removal. Do not treat it as permanent associate status. |
| Lease | Target stays owner, ROOT controls the state, with access and guarantee | Add fixed term, termination, method-specific control restoration, and supported diplomatic cleanup. |
| Joint administration | Same owner and controller split with a state modifier and access | Add shared-governance status, term or review, and an actual joint terminal choice. |
| Association | Access and guarantee are granted, then the target enters the generic recognized partner array | Add an associate status flag or enum, duties, withdrawal or review path, and subject-autonomy reconciliation. Separate associates from other compacts. |
| Accepted ultimatum | Purchase-style transfer and stewardship | Use distinct ultimatum response state. Keep coercion conduct and target consent history separate. |
| Enforcement | Generic `take_state` wargoal | Use dedicated wargoal identity, exact war hooks, exact postwar ownership check, and failure cleanup. |

`utopia_manifesto_record_external_case_completion` currently labels purchase, contract, lease, joint administration, and association as the first associate and adds all targets to `utopia_manifesto_recognized_external_partners`. Split at least `recognized_compacts` from `recognized_associates`.

`chaosx.nr15.200` serves both purchase and long supply while its terms are written as one offer. Split it or make every title, description, and option dynamic from the locked method.

### P1. Reset all per-case stewardship progress

Current case-scoped flags can leak into a later case:

- `utopia_manifesto_stewardship_obligation_confirmed`
- `utopia_manifesto_stewardship_provision_complete`
- `utopia_manifesto_stewardship_route_restored`
- `utopia_manifesto_stewardship_charter_convened`
- `utopia_manifesto_stewardship_charter_period_complete`
- `utopia_manifesto_stewardship_status_vote_held`
- `utopia_manifesto_assigned_colony_active`
- `utopia_manifesto_stewardship_integration_authorized`
- `utopia_manifesto_stewardship_long_integration_complete`
- `utopia_manifesto_stewardship_associate_partnership`
- `utopia_manifesto_stewardship_autonomy_selected`
- `utopia_manifesto_stewardship_return_selected`
- Founder-side target accepted, countered, and refused flags

Add `utopia_manifesto_reset_current_stewardship_progress`. Call it before starting a new stewardship and from all terminal helpers. Preserve only permanent unlocks, doctrine, conduct history, and achievement evidence.

Do not clear an unresolved global failure when starting another case. `utopia_manifesto_start_stewardship_from_active_case` currently clears `utopia_manifesto_stewardship_failed`. Split current-case failure from a durable `utopia_manifesto_unresolved_stewardship_failure` that formation logic can inspect.

### P1. Bind the status vote to one real terminal path

Current identifiers:

- `chaosx.nr15.63`
- `decision_utopia_begin_long_integration`
- `utopia_manifesto_integrate_stewardship`
- `utopia_manifesto_complete_long_integration`

Event option 63.a calls `utopia_manifesto_integrate_stewardship` immediately, bypassing the long integration mission. Options 63.b and 63.c set flags but leave stewardship active, after which integration remains selectable. The choice is therefore not binding.

Required fix:

- Add a mutually exclusive `utopia_manifesto_stewardship_status` enum with integration, association, autonomy, and return values.
- Option 63.a authorizes integration only. `mission_utopia_long_integration` must be the sole final integration path.
- Options 63.b, 63.c, and 63.d should execute or schedule their real terminal outcomes.
- Gate every later stewardship decision against the locked status.
- In `utopia_manifesto_complete_long_integration`, set completion proof before calling the guarded integration helper.

### P1. Preserve revolt scopes until the revolt response resolves

Current identifiers:

- `utopia_manifesto_trigger_stewardship_revolt`
- `chaosx.nr15.64`
- `decision_utopia_clean_up_stewardship_revolt`

The revolt helper flags the target, restores the state, clears stewardship, and clears the active case arrays before event 64 is handled. Event 64 then calls helpers that require active stewardship and mostly no-op. The cleanup decision targets `neighbors`, so a former target that is not a neighbor cannot be selected.

Required fix:

1. Add persistent `utopia_manifesto_stewardship_revolt_targets` and `utopia_manifesto_stewardship_revolt_states` arrays.
2. Copy the exact active target and state into them before case cleanup.
3. Set a `utopia_manifesto_stewardship_revolt_pending` flag.
4. Let event 64 own one of four real resolutions: return or independence, association, suppression with assigned administration, or mediation.
5. Clear the dedicated arrays only after the chosen resolution applies.
6. Use the dedicated target array in the cleanup decision, not `neighbors`.

### P1. Invalidity must not count as voluntary renunciation

Current identifier: `utopia_manifesto_validate_active_need_case`.

Pre-stewardship invalidity currently calls `utopia_manifesto_renounce_active_need_case`. That sets voluntary renunciation evidence, including `utopia_manifesto_case_renounced`, `utopia_manifesto_false_cases_resolved`, and the first renunciation method. Target annexation, disappearance, or state loss is not a voluntary renunciation.

Add `utopia_manifesto_invalidate_active_need_case`. It should cancel the response, remove only the Event 15 wargoal, clean pointers and temporary markers, and record an invalidation reason without granting renunciation or peaceful-completion evidence.

`utopia_manifesto_fail_invalid_stewardship_case` also assigns colonial administration after losing the authoritative target or state relationship. If the original target is live and the state can lawfully be returned, use method-specific restoration. If the target disappeared, the recipient or successor policy is a design blocker and must not default to silent integration or colonial administration.

### P1. Expand one-shot on-action reconciliation

The current one-shot hooks are preferable to periodic world iteration, but their coverage is incomplete.

Required additions or changes:

- `on_state_control_changed`: operate only on the exact active state. Require ownership before stewardship begins.
- `on_war_relation_added`: identify an exact enforcement war, suspend case expiry, and set war-active state.
- `on_peaceconference_ended`: reconcile both ROOT and FROM when either is an accepted Event 15 actor. Resolve enforcement only after ownership is settled.
- `on_annex`: while the annexed target scope still exists, invalidate the founder's exact case and clean arrays. A bounded one-shot scan is acceptable if the founder cannot otherwise be recovered.
- `on_subject_free` and `on_subject_autonomy_level_change`: reconcile association and partner status.
- State ownership loss after integration: remove the integrated marker from the former actor array or explicitly transfer the status if that is intended.

No daily, weekly, or monthly world scan is required for this architecture.

### P2. Make local support state-specific

`utopia_manifesto_case_local_support` is currently a founder country variable initialized to a fixed value and adjusted by offer, refusal, ultimatum, and provision effects. It does not inspect the selected state's resistance, compliance, damage, target opinion, or other local conditions.

Add `utopia_manifesto_refresh_case_local_support` and derive the value from the exact target and state before charter, status vote, return, and integration checks. The final formula should remain constant-driven, but the state and target must supply the facts.

### P2. Persistent integrated state modifiers need ownership cleanup

The state modifier definitions are structurally sound. Each temporary modifier is enabled by a state flag and removes itself when the flag is cleared. `utopia_manifesto_clear_temporary_stewardship_state_modifiers` also clears its variables.

The persistent `utopia_manifesto_integrated_commonwealth_state` modifier is different. Its removal depends only on its state flag. If the state later leaves ROOT, the flag, modifier, and founder-side array membership can remain indefinitely and benefit the new owner.

Add an ownership reconciliation helper called by state transfer and peace hooks. Clear the flag, dynamic modifier, state variables, and array entry when ROOT no longer owns the state, unless the specification explicitly makes the status portable across owners.

## State modifier review

Reviewed file: `common/dynamic_modifiers/015_utopia_manifesto_state_modifiers.txt`.

Structurally sound definitions:

- `utopia_manifesto_stewardship_obligation_state`
- `utopia_manifesto_lease_administration_state`
- `utopia_manifesto_joint_administration_state`
- `utopia_manifesto_provisioned_stewardship_state`
- `utopia_manifesto_restored_stewardship_route_state`
- `utopia_manifesto_local_charter_state`
- `utopia_manifesto_assigned_colony_state`
- `utopia_manifesto_integrated_commonwealth_state`

The temporary modifiers have correct flag-driven removal design. The main risk is not the modifier schema. It is whether every terminal path clears the owning flag and whether the persistent integrated marker follows state ownership.

## Recommended implementation order

1. Add exact array and stage-aware validity triggers.
2. Add response reset and begin-response helpers, plus distinct ultimatum refusal.
3. Replace generic wargoal identity and wire war and peace reconciliation.
4. Add stewardship mission removal and per-case progress reset.
5. Make return, integration, expiry, invalidation, and revolt helpers fully terminal and idempotent.
6. Add method-specific restoration and diplomatic cleanup.
7. Split calling family from external case type and tighten state relevance.
8. Make domestic review family-bound and enforce the peaceful ladder.
9. Add persistent contract, lease, joint, and associate lifecycle data.
10. Bind the status vote to one terminal status and make long integration authoritative.
11. Add revolt arrays and resolve event 64 against retained scopes.
12. Add ownership cleanup for integrated states and complete on-action coverage.
13. Update localisation, event text, docs, event details, and matrices after identifiers and terms stabilize.

## Validation scenarios for the parent

These are architecture scenarios, not generic syntax checks.

1. Draft a claim, do not select a state, then gain control of an unrelated state. The claim remains valid.
2. Refuse a purchase, issue an ultimatum, and leave target event 204 unanswered. Enforcement remains unavailable.
3. Send a revised offer after refusal. The new wait mission does not complete from the prior response.
4. Let a target response event remain open, then start a war. Acceptance cannot transfer territory or grant a compact.
5. Grant an enforcement wargoal while another generic `take_state` wargoal exists against the same target. Event 15 cleanup removes only its own wargoal.
6. Occupy the selected state during the enforcement war. Stewardship does not begin until ROOT owns it after peace.
7. End the enforcement war without receiving the selected state. The case resolves as enforcement failure without voluntary renunciation evidence.
8. Return stewardship while each stewardship mission is active. No later mission cancel effect fires a revolt or failure.
9. Complete a lease return. Ownership never transfers because the target already owns the state.
10. Complete a purchase return while a third party owns the state. Event 15 does not steal the state.
11. Complete stewardship, then draft a second case. No obligation, provision, route, charter, vote, colony, integration, or response flag is inherited.
12. Choose association or autonomy in event 63. Long integration is no longer selectable.
13. Trigger event 64. Every option operates on the retained exact target and state and then clears revolt pointers.
14. Lose an integrated state in a later peace conference. The persistent modifier and founder array entry reconcile correctly.
15. Change the dominant deficit family after a domestic review. The old review cannot authorize a case for the new family.

## Design blockers requiring an explicit parent or user decision

1. Market access cleanup was not verified as a supported reversible effect. Temporary market-access grants should not be implemented on an assumed removal syntax.
2. A stewardship target that disappears needs an explicit successor or disposition policy. Silent integration, colonial administration, or transfer to an arbitrary country would be an unapproved fallback.
3. Contract, lease, and joint-administration terms need accepted durations and renewal or exit rules if the specification does not already lock them numerically.
4. Integrated-state status after a later owner change needs an explicit policy. The recommended default is to remove Event 15 integration benefits when ROOT loses ownership.

## Handoff result

- Changed file: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/scripted_system_architect_case_review.md`
- Gameplay edits: none
- Simplifications: none in the audit. Unverified engine behavior is identified as a blocker rather than replaced with a fallback.
- Skills used: `chaos-redux-events`, `hoi4-decisions-missions`, and `chaos-redux-subagents`
