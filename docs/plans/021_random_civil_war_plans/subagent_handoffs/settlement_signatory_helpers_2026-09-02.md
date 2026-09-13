# Event 021 settlement-signatory helper handoff

Date: 2026-09-02.

Status: bounded helper tranche delivered; parent integration remains incomplete and the Event 021 goal is not complete.

This handoff records the new persistent treaty contract, exact parent obligations, validation evidence, and unresolved blockers.

No parent gameplay file was edited by this tranche.

No commit was created, and Hearts of Iron IV was not launched.

## Changed files

| File | Purpose |
| --- | --- |
| `common/scripted_effects/021_random_civil_war_treaty_effects.txt` | Seven bounded persistent agreement, signatory, proof, recurrence, and successor-rebinding effects. |
| `common/scripted_effects/021_random_civil_war_treaty_effects.md` | Helper documentation, registry schema, proof mapping, call order, scenarios, and risks. |
| `common/scripted_triggers/021_random_civil_war_treaty_triggers.txt` | Nine strict capture, contract, hold, breach, recurrence, and Terms Hold consumer triggers. |
| `docs/plans/021_random_civil_war_plans/subagent_handoffs/settlement_signatory_helpers_2026-09-02.md` | This parent integration handoff. |

The only source changes in this tranche are the two new helper source files listed above.

## Exact helper map

All effects receive inputs through the current scope, normal variables, flags, temporary variables, and the existing bounded arrays because Clausewitz scripted effects do not expose a formal parameter list.

### Effects

| Effect | Scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- |
| `event021_treaty_find_agreement_row` | Any | Temp `event021_treaty_lookup_id`. | Sets temp `event021_treaty_lookup_found` and `event021_treaty_lookup_index` while scanning only `global.event021_treaty_agreement_ids`. |
| `event021_treaty_snapshot_signatory_row` | Country | Temp agreement index, signatory index, snapshot agreement id, and temp `event021_treaty_snapshot_at_hold`. | Reads the current country’s own obligation and live public proof flags, freezes proof into aligned global rows, latches breach and recurrence, and marks invalid rows when obligation, front, or proof is missing. |
| `event021_treaty_capture_settlement` | Country settlement owner | `random_civil_war_crisis_id`, `random_civil_war_front_id`, settlement type, `event021_settlement_talks_open`, the owner’s active front-bound obligation, and the owner’s `random_civil_war_opposition_actors` array. | Appends one agreement row, one signatory row per exact participating country, and one front row per captured signatory/front binding; sets durable local agreement variables and helper receipt flags; rejects callers that fail the capture gate. |
| `event021_treaty_freeze_fulfilled_proof` | Any country carrying `event021_treaty_agreement_id` | The current country’s durable helper agreement id and current date. | Visits every aligned signatory row for that agreement through the persistent bounded registry and freezes live public proof before parent cleanup can clear it; missing or dead bindings fail closed. |
| `event021_treaty_review_agreement` | Country carrying `event021_treaty_agreement_id` | Durable agreement id and current date. | Calls the freeze effect, reviews every row for that agreement, requires positive members/fronts, requires every proof row valid after the shared hold date, latches breach/invalidity, and propagates aggregate receipts to still-bound signatories. |
| `event021_treaty_mark_recurrence` | One durable signatory country | Durable helper agreement id, current recurrence callback/flag, and the old live crisis identity before reset. | Latches recurrence-seen and during/after-hold history on the agreement and matching signatory row; in-period recurrence also latches agreement breach. The parent must call it once per durable signatory. |
| `event021_treaty_rebind_successor` | Predecessor country inside the exact `on_annex` transaction with successor in `ROOT` | Predecessor durable agreement/crisis identity and the existing successor proof contract. | Replaces matching signatory/front scope pointers with the successor and copies durable local receipts only when the successor is claimed, shares the crisis id, and points its host scope to the predecessor; conflicts and duplicates invalidate the agreement. |

### Triggers

| Trigger | Scope and exact requirement |
| --- | --- |
| `event021_treaty_capture_ready` | Settlement owner has current crisis/front/type identity, open settlement talks, no harsh settlement, no sponsor-side role, and an allowed negotiated type or explicit `event021_treaty_armistice_contract`. |
| `event021_treaty_current_agreement_known` | Local durable agreement id is present in the persistent agreement-id registry. |
| `event021_treaty_nonempty_agreement` | Local agreement receipt has a positive signatory count and a positive participating-front count. |
| `event021_treaty_signatory_contract_valid` | One signatory is bound to a non-`none` obligation, has frozen valid proof, and has no invalid, breach, or in-period recurrence latch. |
| `event021_treaty_shared_hold_period_complete` | Current date is at or beyond the one agreement-level shared hold-until date. |
| `event021_treaty_terms_hold_valid` | Achievement is eligible and not disqualified, the country is a signatory, the aggregate terms-held/all-reviewed/all-obligations flags are present, no breach or in-period recurrence is latched, the agreement is nonempty, and the shared hold period is complete. This trigger awards nothing. |
| `event021_treaty_review_due` | Durable agreement is at or beyond its shared hold date and has not received terms-held. |
| `event021_treaty_agreement_breached` | Durable agreement has a latched breach from any signatory or agreement-level recurrence. |
| `event021_treaty_recurrence_after_hold_recorded` | Durable agreement has recorded recurrence after the shared hold date. |

## Persistent contract and row alignment

Agreement rows are keyed by Event 021 `random_civil_war_crisis_id` and use aligned arrays for settlement type, start date, one shared hold-until date, front count, signatory count, fulfilled-signatory count, breach, recurrence history, terms-held, invalidity, and explicit armistice state.

Signatory rows use aligned arrays for agreement id, country scope, exact front id, obligation id, obligation-present state, proof-observed state, proof-frozen state, proof-valid state, proof snapshot date, breach, and recurrence history.

Front rows use aligned arrays for agreement id, exact front id, signatory country scope, and settlement-owner scope.

The capture pool is bounded to the current owner plus the owner’s recorded `random_civil_war_opposition_actors` array.

Actor rows must match the owner’s current crisis id and carry the opposition-actor role.

Sponsor-side rows are explicitly excluded.

The helper does not scan all countries, all fronts, or all world actors.

Same-tag internal settlement has one real country scope and one real front binding and does not create a fake country.

An empty signatory/front set is invalid and cannot pass any Terms Hold trigger.

Rows remain persistent across the parent’s narrow reset, settlement cleanup, later recurrences, and valid annex/succession rebinding.

## Actual public-obligation proof mapping

The helper freezes only these existing public proof flags.

| Existing obligation | Required proof flag |
| --- | --- |
| `constant:event021_settlement_obligation.recognition` | `random_civil_war_event6_recognized_independence` |
| `constant:event021_settlement_obligation.disarmament` | `random_civil_war_disarmament_complete` |
| `constant:event021_settlement_obligation.rail_security` | `event021_rail_spine_secured` |
| `constant:event021_settlement_obligation.sponsor_repayment` | `random_civil_war_sponsor_repaid` |
| `constant:event021_settlement_obligation.coalition_governance` | `random_civil_war_coalition_governance_complete` |

Each signatory must have its own non-`none` obligation, the parent active-obligation receipt, an exact front binding, and the matching public proof.

The host proof cannot satisfy an actor row.

The helper never reads the old caller-only `random_civil_war_settlement_signatory` flag as sufficient proof.

## Parent integration obligations

The parent owns all existing-file integration and must add the following calls in the existing lifecycle.

### Settlement capture call order

1. In `event021_parent_apply_settlement`, after `event021_parent_select_settlement_terms` and after every intended signatory has its own active front-bound obligation, call `event021_treaty_capture_settlement = yes` while `event021_settlement_talks_open` is still set.

2. The capture call must precede `event021_parent_end_event6_war`, `event021_parent_promote_ordinary_successor`, `event021_parent_close_ordinary_opposition`, secondary-front closure, `event021_apply_settlement`, and any cleanup or annex that can remove a signatory scope.

3. The current parent sequence at `event021_parent_apply_settlement` selects the caller’s obligation, then begins closure logic, then sets the caller’s live settlement-obligation state, then clears talks, so the helper must be inserted at the earliest safe post-selection point and the parent must bind actor obligations before that call.

4. The parent must also wire the same capture sequence into the same-tag settlement route without creating a country scope.

5. The parent keeps its existing settlement application, logs, event details, localisation, and award ownership after capture.

### Freeze before cleanup

1. Before `event021_cleanup_decision_state` or any actor cleanup clears `random_civil_war_disarmament_complete`, `random_civil_war_sponsor_repaid`, `random_civil_war_coalition_governance_complete`, or `event021_rail_spine_secured`, call `event021_treaty_freeze_fulfilled_proof = yes` from a country carrying the durable helper agreement id.

2. The freeze call must happen while every intended signatory scope is still alive and still carries the same helper agreement id.

3. The parent must not expect the helper to reconstruct a proof after cleanup has cleared the live flag.

4. The current narrow reset at `event021_begin_achievement_history` may continue clearing command/UI flags, but it must leave the helper agreement id, hold date, signatory history, breach history, recurrence history, and frozen proof rows intact.

5. The current `event021_cleanup_decision_state` proof-flag clearing is compatible only when freeze is called before it.

### Review and achievement consumer

1. At the existing bounded reconstruction completion/review point, call `event021_treaty_review_agreement = yes` after the shared hold date is reached.

2. Replace the old caller-only Terms Hold readiness use with `event021_treaty_terms_hold_valid = yes` in the parent-owned achievement consumer path.

3. The parent may retain separate eligibility, presentation, event-details, and award effects, but no one-country settlement flag may bypass this trigger.

4. Review must happen after all signatory proofs have been frozen and must not clear any persistent helper row.

### Recurrence and reset

1. Before `event021_parent_commit_generation_history`, `event021_prepare_*`, or any reset that overwrites the live `random_civil_war_crisis_id`, call `event021_treaty_mark_recurrence = yes` once for every durable signatory.

2. The callback must run before the old signatory’s crisis identity is replaced.

3. An in-period recurrence from any one signatory latches both that signatory row and the agreement row as breached.

4. A recurrence after the shared hold date is preserved in historical after-hold rows and is not silently converted into an in-period breach.

5. The capture effect contains only bounded owner-side protection for a missed callback when an old helper agreement id differs from the new crisis id; this does not replace the required per-signatory callback.

6. The parent must preserve agreement/signatory history across later recurrence cycles and must not clear the new helper arrays during the existing narrow reset.

### Annex and succession

1. Inside the same `on_annex` transaction used by `event021_handle_annexed_country`, invoke `event021_treaty_rebind_successor = yes` from the predecessor with the successor in `ROOT` before the predecessor disappears.

2. The successor must satisfy the existing proof of `random_civil_war_successor_claimed`, matching `random_civil_war_crisis_id`, and `random_civil_war_host_country_scope` pointing to the predecessor.

3. The helper must be called only in that exact predecessor/`ROOT` arrangement or the parent must provide an explicitly equivalent, source-backed scope contract.

4. A missing successor proof, duplicate successor row, or agreement conflict intentionally invalidates the persistent agreement instead of guessing a replacement.

5. Rebinding changes scope pointers and durable local receipts only and does not clear agreement history.

### Cleanup boundary

The parent may continue clearing transient command/UI, settlement-phase, reconstruction-phase, decision, event-target, and temporary actor state according to its existing cleanup contract.

The parent must not clear `event021_treaty_agreement_*`, `event021_treaty_signatory_*`, or `event021_treaty_front_*` persistent rows, nor the durable country helper variables and history flags, until a separately designed migration/compaction contract exists.

## Source-backed scenarios

### Scenario A: one host and one actor

The parent binds the owner and actor to the same crisis id with distinct exact front ids and active non-`none` obligations.

Each country’s matching public proof is frozen before cleanup, no breach or in-period recurrence is recorded, and one shared hold date elapses.

`event021_treaty_review_agreement` counts both rows and Terms Hold can pass only when both proof rows are valid.

This closes the current gap where `event021_parent_record_achievement_receipts` and the old readiness trigger rely on the caller’s flags.

### Scenario B: one actor missing its real obligation

If an actor has no obligation, a `none` obligation, no active-obligation receipt, or a mismatched `random_civil_war_settlement_obligation_front_id`, capture records the row as structurally invalid.

The owner’s valid proof cannot make the agreement pass.

### Scenario C: sponsor and unrelated-front exclusion

A sponsor-side country in the owner’s actor array is excluded by the sponsor-side filter.

An actor from another crisis id is excluded by the exact crisis-id filter.

The caller’s actor array remains the bounded participant source, so no all-world participant search is introduced.

### Scenario D: same-tag internal agreement

The owner is the single real country and its current front id is the only front binding.

The helper does not release, duplicate, or invent a country for the internal opposing side.

The real owner obligation and proof remain mandatory.

### Scenario E: AI signatory

An AI signatory is captured and reviewed through the same country-row, active-obligation, public-proof, breach, recurrence, and shared-hold checks.

There is no player-only bypass in the helper contract.

### Scenario F: one signatory breach or recurrence

A breach flag or in-period recurrence on any one signatory is copied to its row and the agreement row before cleanup.

Review and Terms Hold remain false for the agreement even if every other signatory is valid.

### Scenario G: proof cleared before freeze

If cleanup clears a live proof flag before `event021_treaty_freeze_fulfilled_proof`, the helper cannot infer the old proof from a caller flag and intentionally fails the row.

This is the direct integration reason the parent must place freeze before `event021_cleanup_decision_state`.

### Scenario H: succession

A successor passing the existing lifecycle proof inherits the exact persistent row pointer and durable receipts.

A successor lacking that proof or conflicting with another agreement invalidates the contract rather than being silently attached.

### Scenario I: after-hold recurrence

A recurrence recorded after the shared hold date remains historical after-hold memory.

It does not retroactively become an in-period breach, while any breach already latched remains permanent.

## Validation performed

The two new script files were checked with a focused structural pass.

`common/scripted_effects/021_random_civil_war_treaty_effects.txt` has balanced Clausewitz block braces.

`common/scripted_triggers/021_random_civil_war_treaty_triggers.txt` has balanced Clausewitz block braces.

`git diff --check` returned no output for the new helper source files.

The helper source contains no `<=` or `>=` operators; date comparisons use supported `check_variable` comparison names.

The helper source contains no all-world loops; loops are limited to the current owner’s actor array, temporary pools, and persistent agreement/signatory/front arrays.

The required read-only Event 021 MCP target render completed with status `ok` and code `EVENT_RENDERED_PARTIAL` at revision `65f53c2f4a099c16d11d6ab9960f409df2c881e6ad4b02f663cc098b6d5137bd`.

The render artifact references are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf66fbd1b94be7fcf0b0074292736546ceb25e7b2cb6ce286fb52d3d4492c9a6/ce098dfa50044a91e8dfe5b06ece1762b2fea83bf7369e906ef779cd6f058218/event-targets-65f53c2f4a09-manifest.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/645920be1416796da2f5aae2ff126f2eacedb004495069b85108c4878c677466/c4bfb8ceacde59649a5eea511a03c9afffa2a014415cf9ae74da2d7d53770096/event-targets-65f53c2f4a09.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/44f5f7597fdc9ae388cdb4743107190d7a36cc91a7028ca2279f8ccdea76518a/9c3cc1c3b35ba1c95a0679492a1189d5cf81f005b927cb17c93ee24126d6ebb9/event-targets-65f53c2f4a09.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8074287045bd40fa41f0c0a51eba48b6848fe554ca4320270790956520858738/1413a7691d43c6420bad4dc71727c1e6cf3b87a58215eaae3301f687578f235c/event-targets-65f53c2f4a09.png`.

The focused MCP lint completed with status `ok` and code `EVENT_INSPECTED_PARTIAL` at the same revision.

The lint artifact reference is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7de4c27245310f27bebdbaa0c44becda60fbdd239c33d94bcaef2c4630d764a3/7f39034a752ed84c93cd9b809d15936fcff22fcf77b9cd58a72bd5058c0a320d/event-lint-65f53c2f4a09.json`.

The MCP render and lint were partial focused analyses with inline inventory truncated to 64 of 368 paths and deferred workspace-wide helper/lifecycle passes, so they are not clean proof that the new unintegrated helper files work in the engine.

The expanded Event 021 state-flow and trace inspections attempted earlier timed out after 180 seconds and were not treated as evidence.

No `event_compare` pass was run because no existing Event 021 source file was changed and the new helpers are not yet wired into a parent call site.

No probability inspection or AI probability audit was run because this tranche adds no weighted or probability-bearing helper and the parent owns existing weights.

No engine launch or live-save validation was performed.

## Blockers and follow-up

The parent’s current settlement selector initializes the obligation on the caller, while this contract requires an active, real, front-matching obligation for every signatory.

Until the parent binds every intended actor before capture, multi-signatory agreements fail closed as invalid.

The parent must freeze all live public proof before `event021_cleanup_decision_state`; there is no safe source-backed reconstruction after those flags are cleared.

The parent must confirm that the caller’s `random_civil_war_opposition_actors` array is complete for every settlement branch that should share one agreement, including the intended secondary-front behavior.

The parent must wire the helper into both normal and same-tag settlement paths and preserve the helper rows through narrow reset and cleanup.

The parent must call recurrence per durable signatory before identity reset and call successor rebinding from the exact existing annex scope.

The parent still owns final achievement call-site integration, existing gameplay files, weights, localisation, event details, and live consumer validation.

No silent fallback was added for missing armistice enum support, missing participant containers, missing proof flags, missing successor proof, or incomplete MCP evidence.

## Completion statement

This is a usable helper and documentation tranche, not a completed Event 021 implementation.

The parent goal remains incomplete until the integration obligations above are wired and validated by the parent in the existing gameplay surfaces.
