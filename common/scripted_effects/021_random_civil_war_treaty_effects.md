# Event 021 treaty and settlement-signatory helpers

Status: bounded helper tranche and parent call-site integration delivered on 2026-09-02; engine-backed consumer validation remains outstanding.

## Overview

This file documents `common/scripted_effects/021_random_civil_war_treaty_effects.txt` and its persistent contract for the Event 021 settlement-signatory achievement path.

The contract is keyed by the Event 021 crisis id and stores append-only agreement, signatory, and front rows in bounded global arrays.

The capture pool is the current settlement owner plus that owner's recorded `random_civil_war_opposition_actors` array, filtered by the exact current crisis id, the opposition-actor role, the absence of the sponsor-side role, and `NOT = { is_actual_nonhuman_country = yes }`.

Every captured country must carry its own non-`none` settlement obligation, the parent active-obligation receipt, a current front id, and a matching `random_civil_war_settlement_obligation_front_id`.

The helper never copies the host's obligation to another country, never scans the world, never awards the achievement, and never treats an empty member or front set as success.

AI signatories use the same country-row and public-proof contract as human signatories.

The same-tag internal route contributes its one real country scope and its real front; it does not create or infer a fake country.

## Helper map

All inputs below are convention variables and flags on the documented scope because Clausewitz scripted effects do not expose a formal argument list.

| Helper | Scope | Inputs | Outputs | Persistent side effects |
| --- | --- | --- | --- | --- |
| `event021_treaty_find_agreement_row` | Any | Temp `event021_treaty_lookup_id` | Temp `event021_treaty_lookup_found`, `event021_treaty_lookup_index` | None; scans only `global.event021_treaty_agreement_ids`. |
| `event021_treaty_snapshot_signatory_row` | Country | Temp agreement index, signatory index, snapshot agreement id, and `event021_treaty_snapshot_at_hold` | Aligned proof, breach, and recurrence row values plus local receipt flags | Freezes the country’s actual public obligation proof, latches live breach inputs, and marks the agreement invalid when the row has no real obligation/front or misses proof by the hold date. |
| `event021_treaty_prepare_signatory_obligations` | Country settlement owner | Current crisis/front identity, settlement type, open talks, owner obligation, and recorded opposition actors | Prepared/rejected binding receipt plus actor-local recognition or disarmament obligations | Preflights every intended human actor, marks prior durable agreements for recurrence, and binds each actor to its own exact front and shared hold date before closure. |
| `event021_treaty_capture_settlement` | Country settlement owner | `random_civil_war_crisis_id`, `random_civil_war_front_id`, negotiated settlement type, `event021_settlement_talks_open`, current owner obligation, and current owner opposition-actor array | Durable local agreement id, shared hold date, settlement type, member/front counts, signatory flags, and capture committed/rejected flags | Appends one agreement row, aligned signatory rows, and aligned front rows when the id is new; filters stale crisis rows and sponsors; records invalidity rather than allowing an incomplete contract to pass. |
| `event021_treaty_mark_settlement_outcome_proof` | Country signatory | Durable agreement id and public settlement outcome | Frozen signatory proof row | Records ordinary actor disarmament from the actual cleanup path and freezes all still-bound rows before live flags disappear; it never fabricates Event 006 recognition. |
| `event021_treaty_freeze_fulfilled_proof` | Any country carrying a durable helper agreement id | Local `event021_treaty_agreement_id` | Frozen proof rows and agreement-level invalid/breach latches | Re-reads every still-bound signatory before cleanup and freezes each actual public proof before live proof flags can be cleared. |
| `event021_treaty_review_agreement` | Country carrying a durable helper agreement id | Local durable agreement id and current date | Agreement terms-held receipt, fulfilled-signatory count, aggregate review flags propagated to live signatories | Calls the freeze helper, reviews every row for the agreement, requires a nonempty member/front set and shared hold date, and latches any breach or missing/invalid proof. |
| `event021_treaty_mark_recurrence` | One durable signatory country | Local durable agreement id, current recurrence callback/flag, and current crisis identity | Agreement/signatory recurrence-seen and during/after-hold history | Latches recurrence for this country’s row before parent reset overwrites crisis identity; the parent must invoke it for every durable signatory. |
| `event021_treaty_mark_agreement_recurrence` | Country settlement owner | Local durable agreement id | Agreement and every aligned signatory recurrence history row | Covers all durable rows through the bounded persistent registry before a new opening resets live identities, including signatories no longer present in the actor array. |
| `event021_treaty_rebind_successor` | Predecessor country in the exact `on_annex` transaction with successor in `ROOT` | Predecessor durable agreement/crisis ids and the lifecycle successor proof | Rebound signatory/front scope pointers and successor local receipts | Rebinds only a claimed successor with the same crisis id and a host pointer to the predecessor; preserves all history and invalidates conflicts or duplicates. |

## Consumer trigger map

| Trigger | Scope and contract |
| --- | --- |
| `event021_treaty_binding_owner_ready` | Country settlement owner with crisis/front/type identity, open talks, no harsh settlement or sponsor role, an allowed negotiated type or explicit `event021_treaty_armistice_contract`, and a current owner obligation bound to the current front. |
| `event021_treaty_capture_ready` | Country settlement owner passing `event021_treaty_binding_owner_ready` with `event021_treaty_bindings_prepared` and no binding rejection. |
| `event021_treaty_current_agreement_known` | Country with a durable local agreement id that is present in the global agreement-id registry. |
| `event021_treaty_nonempty_agreement` | Durable local receipt with a positive member count and positive participating-front count. |
| `event021_treaty_signatory_contract_valid` | One signatory whose obligation is non-`none`, proof is frozen and valid, and no invalid, breach, or in-period recurrence latch exists. |
| `event021_treaty_shared_hold_period_complete` | Durable local agreement whose one shared hold-until date has elapsed. |
| `event021_treaty_agreement_terms_hold_valid` | The agreement-level Terms Hold receipt for AI or human country rows; it requires every-signatory review, every-signatory proof, no breach, no in-period recurrence, a nonempty contract, and the shared hold period. |
| `event021_treaty_terms_hold_valid` | The authoritative Terms Hold achievement consumer trigger; it adds achievement eligibility to `event021_treaty_agreement_terms_hold_valid` and awards nothing itself. |
| `event021_treaty_review_due` | Durable agreement at or beyond its shared hold date without a terms-held receipt. |
| `event021_treaty_agreement_breached` | Durable agreement with a latched breach, including a breach originating in any signatory row. |
| `event021_treaty_recurrence_after_hold_recorded` | Durable agreement with historical recurrence after the shared hold period. |

## Persistent registry schema

The following arrays are append-only and aligned by their row index until a future owner explicitly supplies a safe compaction design.

Agreement rows use `global.event021_treaty_agreement_ids`, `event021_treaty_agreement_settlement_types`, `event021_treaty_agreement_start_dates`, `event021_treaty_agreement_hold_until_dates`, `event021_treaty_agreement_front_counts`, `event021_treaty_agreement_signatory_counts`, and `event021_treaty_agreement_fulfilled_signatory_counts`.

Agreement history uses `event021_treaty_agreement_breach_latched_entries`, `event021_treaty_agreement_recurrence_seen_entries`, `event021_treaty_agreement_recurrence_during_hold_entries`, `event021_treaty_agreement_recurrence_after_hold_entries`, `event021_treaty_agreement_terms_held_entries`, `event021_treaty_agreement_contract_invalid_entries`, and `event021_treaty_agreement_armistice_entries`.

Signatory rows use `event021_treaty_signatory_agreement_ids`, `event021_treaty_signatory_country_scopes`, `event021_treaty_signatory_front_ids`, `event021_treaty_signatory_obligation_ids`, and `event021_treaty_signatory_obligation_present_entries`.

Signatory proof history uses `event021_treaty_signatory_proof_observed_entries`, `event021_treaty_signatory_proof_frozen_entries`, `event021_treaty_signatory_proof_valid_entries`, and `event021_treaty_signatory_proof_snapshot_dates`.

Signatory breach and recurrence history uses `event021_treaty_signatory_breach_latched_entries`, `event021_treaty_signatory_recurrence_seen_entries`, `event021_treaty_signatory_recurrence_during_hold_entries`, and `event021_treaty_signatory_recurrence_after_hold_entries`.

Front rows use `event021_treaty_front_agreement_ids`, `event021_treaty_front_ids`, `event021_treaty_front_signatory_countries`, and `event021_treaty_front_host_countries`.

Each signatory row binds one actual country scope to one actual front id and one obligation id, while front rows preserve the exact agreement, front, signatory, and settlement-owner relationship.

Agreement and signatory rows are never cleared by `begin_achievement_history`, `event021_cleanup_decision_state`, `event021_parent_cleanup_crisis`, or the narrow reset described by the parent.

## Public-obligation proof mapping

The snapshot helper maps only the following real public flags to proof.

| Obligation enum | Required country flag |
| --- | --- |
| `constant:event021_settlement_obligation.recognition` | `random_civil_war_event6_recognized_independence` |
| `constant:event021_settlement_obligation.disarmament` | `random_civil_war_disarmament_complete` |
| `constant:event021_settlement_obligation.rail_security` | `event021_rail_spine_secured` |
| `constant:event021_settlement_obligation.sponsor_repayment` | `random_civil_war_sponsor_repaid` |
| `constant:event021_settlement_obligation.coalition_governance` | `random_civil_war_coalition_governance_complete` |

An obligation id of `constant:event021_settlement_obligation.none`, an absent active-obligation receipt, an absent front binding, or a missing matching proof is not a harmless empty value and makes the agreement ineligible.

The proof is frozen into the aligned global row and local helper receipts before parent cleanup clears the live flags.

## Parent call order

### Settlement capture

1. The parent binds the current crisis and front targets and selects the negotiated settlement type.

2. The parent selects the owner obligation, then calls `event021_treaty_prepare_signatory_obligations = yes` to clear any stale local signatory receipt and bind every intended human actor to its own real obligation, exact front, and shared hold date while each country still has its live settlement state.

3. The parent calls `event021_treaty_capture_settlement = yes` immediately after obligation binding and while `event021_settlement_talks_open` remains set.

4. The capture call must precede `event021_parent_end_event6_war`, actor promotion or closure, `event021_apply_settlement`, and any cleanup that can remove an actor or a live obligation proof.

5. The parent then performs its existing settlement transaction and keeps the durable helper agreement variables and rows intact.

6. Before `event021_cleanup_decision_state` or actor cleanup clears `random_civil_war_disarmament_complete`, `random_civil_war_sponsor_repaid`, `random_civil_war_coalition_governance_complete`, or `event021_rail_spine_secured`, the parent calls `event021_treaty_freeze_fulfilled_proof = yes` from a country carrying the durable agreement id.

7. At the bounded reconstruction/review point, after the shared hold date, the parent calls `event021_treaty_review_agreement = yes` and lets the achievement consumer use `event021_treaty_terms_hold_valid = yes` rather than a single caller flag.

### Recurrence

The parent calls `event021_treaty_mark_agreement_recurrence = yes` before `event021_parent_commit_generation_history`, `event021_prepare_*`, or any reset that clears or overwrites the live crisis identity. This helper records every aligned signatory row through the bounded persistent registry, including rows no longer present in the live actor array.

The callback must happen before the signatory's `random_civil_war_crisis_id` is replaced, because recurrence history is keyed to the old agreement id and old hold date.

If a signatory has already completed a live proof, the parent freezes that proof before cleanup and then records recurrence; the historical row is not reset by the new crisis.

The capture helper contains a bounded owner-only protection for a missed callback when an old local helper id differs from the new crisis id, but this is not a substitute for the explicit agreement recurrence call.

### Annex and succession

Inside the same exact `on_annex` transaction used by `event021_handle_annexed_country`, the predecessor calls `event021_treaty_rebind_successor = yes` with the successor in `ROOT` before the predecessor scope disappears.

The successor must have `random_civil_war_successor_claimed`, the same `random_civil_war_crisis_id`, and `random_civil_war_host_country_scope` pointing to the predecessor.

The helper changes only the aligned country-scope pointers and copies durable local receipts; it does not erase agreement history, create a fake country, or transfer an unrelated annexer into the contract.

Any missing proof of succession, an existing successor row for the same agreement, or a successor agreement conflict latches the agreement invalid.

### Cleanup

Freeze is the required boundary before `event021_cleanup_decision_state` because that helper clears the actual obligation proof flags.

The parent must not use those live flags as the Terms Hold source after cleanup.

The parent must leave all `event021_treaty_*` agreement/signatory/front arrays and the durable country agreement id, hold date, and history flags intact across settlement cleanup and later recurrence/succession.

## Constants and tuning

No new tuning constant or weighted/probability surface is introduced by this tranche.

The fallback shared hold date uses the existing `constant:event021_parent_tuning.settlement_terms_hold_days` value when the parent has not already supplied `random_civil_war_settlement_terms_hold_until`.

Settlement types and obligation ids use the existing Event 021 script constants, and zero/one values use the existing `constant:random_civil_war_value.zero` and `constant:random_civil_war_value.one` constants.

The current settlement enum has no armistice value, so an armistice contract is accepted only when the caller explicitly sets `event021_treaty_armistice_contract`; no silent enum or type fallback is invented.

## Migration plan

The parent calls binding and capture at the post-obligation, pre-closure point in `event021_parent_apply_settlement`, which also covers the same-tag settlement path without creating a country scope.

The parent binds active, front-matching obligations for every intended human actor through `event021_treaty_prepare_signatory_obligations`; a malformed actor row still fails closed as an invalid contract.

The parent calls outcome proof before ordinary actor cleanup and after Event 006 recognition, then calls freeze before each cleanup boundary and review from the existing reconstruction completion path.

The parent replaces the old single-caller Terms Hold readiness condition with `event021_treaty_terms_hold_valid = yes` while retaining parent-owned eligibility, presentation, and award effects around it.

The parent invokes the bounded agreement recurrence callback in the generation-reset path and invokes successor rebinding from the existing lifecycle annex proof.

Parent, achievement, trigger, and on-action integration now calls the helper tranche; no decision, localisation, or weighted surface was changed by the treaty integration.

## Meaningful scenarios

An owner and one actor with distinct real front-bound obligations, frozen valid proofs, no breach, and the same hold-until date can satisfy Terms Hold only after the shared date.

A missing actor obligation, inactive obligation receipt, `none` obligation, or mismatched obligation front makes the agreement invalid even if the owner has a valid proof.

A sponsor present in the owner's actor array is excluded by the capture filter, while an unrelated actor from another crisis id is excluded.

A same-tag internal agreement uses the current real country and current real front only and cannot pass through a fabricated country scope.

An AI actor follows the same obligation, proof, breach, recurrence, and hold checks as a human actor.

A breach or in-period recurrence on any one signatory latches the aligned signatory and agreement rows and prevents Terms Hold.

A recurrence after the shared hold date is preserved as history and does not silently mutate into an in-period breach.

A successor that satisfies the exact lifecycle proof inherits the durable row binding without clearing historical proof or recurrence state.

An empty signatory or front array fails the nonempty trigger and cannot pass vacuously.

## Risks and unsupported evidence

The parent currently selects an obligation on the caller and may not yet bind active, front-matching obligations for every actor; until that integration exists, multi-signatory contracts will fail closed as invalid.

If a signatory is cleaned up before `event021_treaty_freeze_fulfilled_proof`, its live proof cannot be reconstructed from the cleared flags and the agreement is intentionally invalid.

The helper depends on the parent owner's recorded opposition-actor array being the authoritative bounded participant source for the settlement call; if a future route uses another participant container, the parent must explicitly supply that binding rather than widening this helper to a world scan.

Successor rebinding depends on the existing `on_annex` scope arrangement and its exact predecessor/`ROOT` proof; no alternative successor inference is implemented.

The required read-only Event 021 MCP render and lint were available, but the expanded `event_inspect` state-flow and trace requests timed out after 180 seconds and the returned graph reported 3,950 blocking diagnostics with inline source truncation, so this helper has no clean engine-trace proof yet.

No engine launch, live save validation, or probability audit was performed because this tranche adds no weighted logic and the project rules reserve engine validation for the parent/user.

## Assets and localisation

This helper tranche adds no player-facing text, scripted localisation, GUI, icon, or other visual asset, so no asset or localisation wiring is required here.

## Future plans

The parent may later add aggregate Event Details or achievement receipts that read the durable agreement row, but those consumers should remain read-only and continue to use the shared signatory proof contract.

A future bounded registry-compaction design could reclaim obsolete rows, but no compaction is safe until the parent defines how agreement history survives recurrences, succession, and old-save migration.
