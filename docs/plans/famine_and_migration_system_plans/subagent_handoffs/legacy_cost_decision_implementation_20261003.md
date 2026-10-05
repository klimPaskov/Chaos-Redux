# Legacy decision affordability and paid-work implementation, 2026-10-03

> **Current-status disposition (2026-10-06): superseded by** [takeover_status_2026-10-06.md](../takeover_status_2026-10-06.md) for current famine and migration status.
> This dated document remains historical evidence, with its original acceptance basis, source snapshot, audit outcome, and validation limits scoped to the work described below.
> This reconciliation grants no new design acceptance and upgrades no historical evidence to current or native validation.

Disposition: implemented in the assigned decision-owner source surfaces; parent integration, independent review, native decision parsing/callback evidence, and mandatory same-scenario probability comparison remain pending.
Acceptance basis: the parent accepted [the legacy-cost parity requirements](../legacy_cost_affordability_parent_acceptance_20261003.md), reviewed [the transaction architecture](legacy_cost_transaction_architecture_20261003.md), and assigned this bounded implementation to the decision owner.
This handoff covers the 25 existing custom-cost decisions that use the shared legacy-fee API; it does not claim completion of the wider famine/migration system.

## Changed files

- `common/decisions/famine_decisions.txt`
- `common/decisions/migration_decisions.txt`
- `common/scripted_triggers/famine_relief_triggers.txt`
- `common/scripted_triggers/famine_decision_owner_triggers.txt` and `common/scripted_triggers/famine_decision_owner_triggers.md`
- `common/scripted_triggers/migration_decision_owner_triggers.txt` and `common/scripted_triggers/migration_decision_owner_triggers.md`
- `common/scripted_effects/famine_decision_owner_effects.txt` and new `common/scripted_effects/famine_decision_owner_effects.md`
- `common/scripted_effects/migration_decision_owner_effects.txt` and `common/scripted_effects/migration_decision_owner_effects.md`
- Narrow stale-receipt cleanup calls in `common/scripted_effects/famine_core_effects.txt` and `common/scripted_effects/migration_core_effects.txt`.
- This handoff.

The two core-effect files also contain parent-owned quote-projection and mortality edits; those hunks were preserved. The parent remains responsible for source-wide API/quote integration, localisation, final review, and publication.

## Existing decisions and exact fee profiles

Every fee below is the same profile used by the matching `custom_cost_trigger`, its `available` cost gate, and the complete-action preflight. `PP` counts as a spendable type; no action exceeds four distinct spendable types.

| Decision | Shared profile helper | Spendable types | Payment and delayed receipt |
|---|---|---:|---|
| `famine_release_reserves` | `humanitarian_cost_pp20_support50_fuel500_is_affordable` | 3 | Upfront once; `famine_release_reserves_cost_paid` plus state-scoped payer. |
| `famine_emergency_imports` | `humanitarian_cost_pp20_convoy10_fuel500_is_affordable` | 3 | Upfront after exact route-contract setup and a fresh full-bundle check; paid flag, payer, contract generation, and donor state. |
| `famine_repair_relief_route` | `humanitarian_cost_pp10_train5_fuel1000_is_affordable` | 3 | Upfront once; paid flag and payer. |
| `famine_escorted_relief_convoy` | `humanitarian_cost_pp20_convoy10_support50_fuel1000_is_affordable` | 4 | Upfront after exact route-contract setup and a fresh full-bundle check; paid flag, payer, contract generation, and donor state. |
| `famine_emergency_airlift` | `humanitarian_cost_pp20_planes5_fuel1000_airxp10_is_affordable` | 4 | Upfront after exact route-contract setup and a fresh full-bundle check; paid flag, payer, contract generation, and donor state. |
| `famine_invite_relief` | `humanitarian_cost_pp20_convoy5_fuel500_is_affordable` | 3 | Upfront after exact land-contract setup and a fresh full-bundle check; paid flag, payer, contract generation, and donor state. |
| `famine_evacuation` | `humanitarian_cost_pp20_train10_fuel1000_is_affordable` | 3 | Upfront once; paid flag and payer; original measured-zero-origin refund retained. |
| `famine_requisition_safer_state` | `humanitarian_cost_pp20_train5_fuel500_is_affordable` | 3 | Upfront once; paid flag and payer. |
| `famine_conceal_crisis` | `humanitarian_cost_pp10_infantry100_fuel500_is_affordable` | 3 | Upfront once; paid flag and payer. |
| `famine_maintain_extraction` | `humanitarian_cost_pp10_train5_fuel500_is_affordable` | 3 | Upfront once; paid flag and payer. |
| `migration_prepare_evacuation` | `humanitarian_cost_pp10_train5_fuel500_is_affordable` | 3 | Upfront once; `migration_prepare_evacuation_cost_paid` plus state-scoped payer. |
| `migration_open_departure_routes` | `humanitarian_cost_pp10_train5_fuel500_is_affordable` | 3 | One guarded complete-body debit; no delayed receipt. |
| `migration_restrict_departure` | `humanitarian_cost_pp10_infantry100_fuel500_is_affordable` | 3 | One guarded complete-body debit; no delayed receipt. |
| `migration_close_border` | `humanitarian_cost_pp20_infantry250_fuel1000_is_affordable` | 3 | Upfront once; paid flag and payer. |
| `migration_evacuate_vulnerable` | `humanitarian_cost_pp20_train5_fuel500_is_affordable` | 3 | Upfront once; paid flag and payer; original measured-zero-origin refund retained. |
| `migration_evacuate_workers` | `humanitarian_cost_pp20_train10_fuel500_is_affordable` | 3 | Upfront once; paid flag and payer; original measured-zero-origin refund retained. |
| `migration_negotiate_corridor` | `humanitarian_cost_pp35_infantry100_fuel500_is_affordable` | 3 | Deferred: complete records only `migration_negotiate_corridor_cost_pending` plus payer; charge once after a valid newly submitted offer and a fresh full-bundle recheck. |
| `migration_controlled_medical_reception` | `humanitarian_cost_pp20_support100_infantry100_is_affordable` | 3 | One guarded complete-body debit; no delayed receipt. |
| `migration_distribute_arrivals` | `humanitarian_cost_pp10_train5_fuel500_is_affordable` | 3 | Upfront once; paid flag and payer. |
| `migration_transit_only` | `humanitarian_cost_pp10_convoy5_fuel500_is_affordable` | 3 | Upfront once; paid flag and payer. |
| `migration_enforce_closure` | `humanitarian_cost_pp20_infantry250_fuel1000_is_affordable` | 3 | Upfront once; paid flag and payer. |
| `migration_local_integration` | `humanitarian_cost_pp20_support100_fuel500_is_affordable` | 3 | One guarded complete-body debit; no delayed receipt. |
| `migration_third_country_resettlement` | `humanitarian_cost_pp35_train5_convoy5_fuel500_is_affordable` | 4 | Upfront once; paid flag and payer. |
| `migration_voluntary_return` | `humanitarian_cost_pp20_train5_fuel500_is_affordable` | 3 | Upfront once; paid flag and payer; original measured-zero-origin refund retained. |
| `migration_forced_repatriation` | `humanitarian_cost_pp35_train10_fuel1000_is_affordable` | 3 | Upfront once; paid flag and payer; original measured-zero-origin refund retained. |

The separate fixed-fee `migration_open_reception` custom-cost action is unchanged and excluded from this 25-consumer pass. Its preparation fee remains owned by its existing preparation-cost API.

## Payment, receipt, refund, and cleanup behavior

All 25 listed actions call the same inclusive component/profile predicates for player affordability and native custom-cost selection. Actual debits use the paired `constant:humanitarian_legacy_cost.<key>_debit` values; positive refunds use the matching positive `constant:humanitarian_legacy_cost.<key>` entries. The local `@..._NEG` macros remain only as unused legacy definitions and do not issue these 25 payments.

Each of the 20 upfront delayed actions writes one state-local paid flag and the actual payer only after its full current bundle has passed. Those callbacks consume their own receipt before entering the original removal body and do not check already-spent stock again; the four Famine relief receipts additionally carry exact route generation and donor-state metadata until their separate work guard has been evaluated.

The Famine relief receipt guard is intentionally payer-and-selected-state only. The four `*_cost_contract_is_current` work guards separately check actor, mode, saved contract generation, and exact donor identity before delivery or invitation reward. Each matching payer/state callback consumes and clears only its own paid metadata even when the contract is expired, replaced, or mismatched; no delivery, stability reward, or generic relief-contract cleanup runs on that failed work guard, and a different live contract is untouched.

The five accepted measured-zero-origin refunds remain exactly inside their original actual-origin-debit-zero branches: `famine_evacuation`, `migration_evacuate_vulnerable`, `migration_evacuate_workers`, `migration_voluntary_return`, and `migration_forced_repatriation`. Their new outer guard proves only the current payer and selected state, so a later route/cohort failure does not suppress an original refund. No blanket late-failure refund or cancellation refund was added.

Every delayed action cancellation clears only that action's paid flag and payer when the recorded payer equals callback `ROOT`, then preserves its existing cancellation work. Corridor negotiation has a separate cancellation of its unpaid pending flag/payer. The existing bounded `*_cleanup_state_registration` and `*_handle_state_control_change` owners call the action-specific stale cleanup effects; those effects clear only missing/invalid payers or payer/control mismatches and preserve valid funded work after phase recovery.

Corridor negotiation does not charge at action completion. It requires a valid selected-state pending receipt and current start/cost conditions before preparation, rechecks the complete tuple immediately before the only successful-offer debit, and clears only the exact just-submitted new offer through the existing corridor cleanup if that final fee recheck fails. Invalid or rejected setup has no charge or surviving unpaid offer; no event or extra automatic action was added.

The direct airlift debit is still exactly 10 air XP, and its unchanged strict 50-XP modifier remains AI-only. The workers decision retains strict `support_equipment > 50` as a non-spend requirement, outside its paid PP/train/fuel profile. The three existing four-type fee rows remain intact: escorted relief convoy, airlift, and third-country resettlement.

No fee amount/type, duration, cooldown, numeric AI factor, country category, decision family, metric, GUI, population operation, discount, generic transaction registry, replay UID, or native service grant was added or retuned.

## Source changes and review notes

The two decision files now use one exact profile for `available`, `custom_cost_trigger`, and the matching whole-body `*_can_start` guard. Famine route-candidate stock gates and the vulnerable/worker evacuation train checks use the corresponding inclusive shared component reader instead of masking an exactly affordable bundle with a strict duplicate threshold.

The 15 Migration start predicates and 10 Famine start predicates repeat the current owner, selected state/control, original start/target requirements, and full cost profile before any setup/payment/policy/service/phase/report work. A delayed upfront-paid lane also rejects a pre-existing receipt for its own action; immediate lanes use their existing non-reentrancy requirements, and corridor negotiation separately rejects an existing pending receipt in availability and completion. The four full-body immediate Migration actions are `migration_open_departure_routes`, `migration_restrict_departure`, `migration_controlled_medical_reception`, and `migration_local_integration`; they write no delayed paid receipt.

`migration_evacuate_workers` still requires strict support-equipment50 independently from its actual inclusive profile PP20/train10/fuel500. The airlift spends PP20/planes5/fuel1000/airXP10 in one profile; the cost gate, availability profile, and one debit share that exact tuple.

The migration owner helper documentation records the exact start and receipt identifiers. The Famine owner-trigger documentation now distinguishes ownership receipt validity from exact relief-contract work validity. The new Famine owner-effect documentation defines stale receipt cleanup scope and the action-local receipt/contract boundary.

## Validation and remaining evidence

Source inventory found 10 Famine custom-cost decision families, 15 Migration families in this shared profile API, and the unchanged 16th fixed-fee `migration_open_reception`. All 25 authorized consumers map to one of the architect's 18 exact inclusive profiles.

The two decision files were checked with a bounded source brace-stack parser after the action wrappers and receipt/cancellation edits; neither has an unmatched block. A source scan confirmed that the five refund paths use paired positive central constants and that no actual decision charge/refund call in these files still uses a legacy `@..._NEG` macro. This source scan is not Clausewitz or engine validation.

The architect's [production-source boundary report](legacy_cost_core_implementation_20261003.md) covers the exact central profile API with 60 component cases, 204 profile boundary/short/poisoned-quote cases, 36 tuned-constant cases, and quote isolation/repeat/stale repair. Those tests do not exercise any decision remove/cancel callback or native debit; the decision transaction/callback boundary remains independently untested here.

An independent source review also found an unrelated, pre-existing local-integration terminalization defect that remains outside this accepted cost patch. `migration_integrate_displaced_cohort` in `common/scripted_effects/migration_core_effects.txt:1201` increments `migration_integrated_population` and sets `migration_cohort_integrated`, but the local-integration caller does not transition its positive cohort row to a completed status and zero amount before calling `migration_cleanup_cohort_record` in `common/decisions/migration_decisions.txt:2159-2183`. The cleanup adapter at `common/scripted_effects/migration_core_effects.txt:292-340` requires a completed/invalid status and zero row amount, so the positive integrated cohort can remain nonterminal and available for replay/receipt divergence. This implementation deliberately preserves the body and only guards its existing cost; the parent has queued a separate exact terminal-settlement design and owner patch. The bounded cost handoff is not a completion claim for local integration or the wider system.

`hoi4.script_validate` is not exposed in the connected tool list. The decision inspect route is exposed, but the prior narrow inspect returned partial/unbound evidence and the parent recorded 600-second inspect/compare timeouts; no duplicate long job was started in this bounded patch. No post-patch decision-inspect artifact, native parser result, native callback result, or user-game result is claimed.

The mandatory same-scenario before/after probability comparison remains unresolved even though no numeric AI factor changed, because action eligibility/applicability changed. The parent or `chaosx_ai_probability_auditor` must complete the same-named comparison on the accepted baseline and fixed scenarios before claiming validated AI parity. The parent owns the independent completion audit and any required source/cost/localisation follow-up.

No localisations, YML values, quote call sites, phase providers, selectors, source indices, icons, assets, workbook rows, GUI files, archive data, or AI weights were edited by this decision-owner patch. No commit or staging action was performed.
