# South Africa purchase transactions

Disposition: implemented in source, with native payment, UI expansion, save/reload, and scenario-specific probability evidence pending.
The acceptance basis is the user's complete Event 26 universal-cost goal and Part 3's atomic component contract.
This integration covers the five existing paid actions in `common/decisions/012_africa_rsa_decisions.txt` and introduces no action, route, cooldown, reward, asset, or daily hook.
Event 26 remains default-disabled and this ledger does not establish universal coverage.

## Owner contract

The owner provides the existing `africa_rsa_cost` constants as current ordinary prices.
The same fresh quotation feeds availability, custom cost requirements, normal and blocked text, hover details, and payment.
Each positive component has a separate quote and exact concrete resource type.
Political Power is the primary achievement family for every action, including the citizenship milestone and the sovereignty guarantee.
Those actions do not hire an advisor or change an institutional law, so their flags do not establish an institutional purchase.
The stability quantum is the existing `universal_cost_fixed_point_quantum.stability = 0.01`, and all other registered components use one unit.

All components are checked before the first debit.
The payment path recomputes the shared effect quotation and rejects invalid or unequal display/payment quotations.
Each successful debit records an unsettled receipt row with its actual amount paid, ordinary counterfactual amount, concrete resource kind, and source ID.
The owner confirms after its outcome.
The regional-support purchase is the submission of a valid request, and its later response does not buy or refund a second action.
The request is queued only after successful settlement, and a rejected settlement refunds its fee without sending a request.
Its recipient has a persistent pending lock, so another purchase cannot queue a second request to that donor while the first is unanswered.
An accepted reply rechecks the original polity requirements, active civil war, live Coalition, and two-supporter cap before registration and the unchanged equipment reward.
Registration precedes shipment, and stale or duplicate replies send nothing.
Refusal consumes pending state once, and the original no-refund submission semantics remain unchanged.
The owner records pending donors in `africa_rsa_pending_support_requests`, and its existing host-transition, terminal, and crisis cleanup hooks clear only those donor flags.
No country-wide or periodic scan is introduced.
The sovereignty purchase confirms only when `FROM` is actually guaranteed by `ROOT`.
An unsuccessful native guarantee refunds the recorded amounts and never sets the completion flag.

A failed component payment refunds earlier recorded rows.
A failed receipt append immediately returns its unrecorded debit and then refunds earlier rows.
Rejected or unresolved refunds retain the payer's pending receipt pointer, and another purchase cannot overwrite it.
Repeated refunds are idempotent, and refund amounts are not recomputed when the sale expires.
The five pending fields are regular payer variables and the shared receipt arrays are persistent state.
The pending-donor array and recipient flags are also persistent state.
Every component record forwards its explicit Political Power logical family, component-basis contract, and PP-primary membership to the shared normal receipt metadata.
The public achievement entry checks that typed role and stored ordinary/paid amounts, rather than accepting the caller's family or payment claim alone.
The source model does not prove serialization or native engine execution.

## Exact cost-surface ledger

All rows use strategy B and status `blocked_pending_evidence` until the native, UI, probability, and save/reload evidence below is complete.
The owner file is `common/decisions/012_africa_rsa_decisions.txt`, the payer is the selecting country, the system is Chaos Redux decisions, and there is no additional DLC gate.
The logical transaction IDs are the existing decision IDs, with one player and AI candidate for each.
The normal, baseline sale, and Evolution I prices are shown in the last column.

| Surface ID | Logical transaction ID | Component ID | Resource and cost family | Ordinary source in `africa_rsa_cost` | Quantum | Normal / 50% / 75% |
| --- | --- | --- | --- | --- | --- | --- |
| BF-RSA-001 | `africa_rsa_protect_civilian_corridor` | 1 | Political Power, political power | `relief_pp` | 1 | 35 / 18 / 9 |
| BF-RSA-002 | `africa_rsa_protect_civilian_corridor` | 2 | Command Power, command power | `relief_cp` | 1 | 20 / 10 / 5 |
| BF-RSA-003 | `africa_rsa_protect_civilian_corridor` | 8 | `train_equipment_1`, trains | `relief_trains` | 1 | 5 / 3 / 2 |
| BF-RSA-004 | `africa_rsa_protect_civilian_corridor` | 6 | `support_equipment_1`, equipment | `relief_support_equipment` | 1 | 150 / 75 / 38 |
| BF-RSA-005 | `africa_rsa_seek_regional_support` | 1 | Political Power, political power | `regional_request_pp` | 1 | 15 / 8 / 4 |
| BF-RSA-006 | `africa_rsa_enact_citizenship_land_milestone` | 1 | Political Power, political power | `citizenship_pp` | 1 | 75 / 38 / 19 |
| BF-RSA-007 | `africa_rsa_enact_citizenship_land_milestone` | 15 | Stability, stability | `citizenship_stability` | 0.01 | 0.05 / 0.03 / 0.02 |
| BF-RSA-008 | `africa_rsa_guarantee_neighbor_sovereignty` | 1 | Political Power, political power | `sovereignty_guarantee_pp` | 1 | 40 / 20 / 10 |
| BF-RSA-009 | `africa_rsa_guarantee_neighbor_sovereignty` | 2 | Command Power, command power | `sovereignty_guarantee_cp` | 1 | 10 / 5 / 3 |
| BF-RSA-010 | `africa_rsa_reconstitute_exile_council` | 1 | Political Power, political power | `exile_recovery_pp` | 1 | 60 / 30 / 15 |
| BF-RSA-011 | `africa_rsa_reconstitute_exile_council` | 2 | Command Power, command power | `exile_recovery_cp` | 1 | 25 / 13 / 7 |

Every row's affordability source is its matching `africa_rsa_can_pay_*_purchase` wrapper and `universal_cost_component_is_affordable`.
Payment is `africa_rsa_pay_selected_purchase` through `universal_cost_pay_component`, and rollback is `africa_rsa_refund_pending_purchase` through `universal_cost_refund_transaction`.
Display is the corresponding `GetAfricaRsa*Cost`, `CostBlocked`, and `CostDetails` getters in `common/scripted_localisation/012_africa_rsa_purchase_localisation.txt`, selecting real keys in `localisation/english/012_africa_rsa_l_english.yml`.
Their normal, blocked, and detail text triggers initialize all quote storage before calling nested helpers.
Only valid, nonpending quotes select numeric prices.
Invalid quotes select the real `Price unavailable` keys, and pending receipts select `Order pending` with an explanatory hover.
Neither status adds a sale-source clause.
Only an unaffordable component is red.
The relief inline price contains three components and its hover text contains all four.
Active source text uses `black_friday.cost_source.line`, and ordinary prices have no sale-source clause.

The AI consumer remains each existing `ai_will_do` block and target pool.
Literal `ai_hint_pp_cost` values mirror ordinary Political Power prices, because the native hint cannot evaluate the dynamic custom quote.
These conservative hints are not a claim of discounted AI scoring or completed probability validation.
Baseline and Evolution I source scenarios cover every row and its component affordability boundary.
Native engine, live display/payment agreement, and save/reload scenarios remain unresolved for every row.
The authoritative full-registry commit freeze remains pending.

## Helper API

All helpers use country scope and have no periodic side effects.
The `africa_rsa_purchase_action` temporary selector is defined in `common/script_constants/012_africa_rsa_purchase_constants.txt` as relief, regional request, citizenship, sovereignty, and exile recovery.
An invalid selector produces an invalid quotation and cannot pay.

| Helper | Inputs | Outputs and side effects |
| --- | --- | --- |
| `africa_rsa_prepare_purchase_costs` | Action selector | Resets all five ordinary fields and validity, then reads the selected existing ordinary constants |
| `africa_rsa_quote_purchase_component` | Component ordinary cost and family | Component quote, and invalid logical-quote state if the active source cannot quote |
| `africa_rsa_quote_selected_purchase` | Action selector | All ordinary and quoted fields, refreshed independently on each call |
| `africa_rsa_can_pay_selected_purchase` | Action selector, native payer resources and pending state | True only for a valid quote, no pending receipt, and every inclusive component affordability check |
| Five `africa_rsa_quote_*_purchase` wrappers | Existing action identity | Select and quote the action, with caller-preinitialized output storage |
| Five `africa_rsa_can_pay_*_purchase` wrappers | Existing action identity | Select and check the action, without changing eligibility or resources |
| `africa_rsa_append_purchase_component` | Component ID, resource kind, family, ordinary amount, quote | Appends only a positive component to five aligned temporary arrays |
| `africa_rsa_prepare_purchase_bundle` | Fresh ordinary and quote fields | Builds the aligned bundle, preserving concrete train and support model types |
| `africa_rsa_pay_selected_purchase` | Action selector and owner eligibility | Payment result, persistent unsettled receipt pointer and snapshots, native debits or rollback |
| `africa_rsa_confirm_pending_purchase` | Persistent pending fields and receipt | Settles once, reports qualifying natural-sale achievement proof, clears pending fields after successful settlement |
| `africa_rsa_refund_pending_purchase` | Persistent receipt pointer | Returns recorded actual-paid amounts, preserving unresolved refund state |
| `africa_rsa_clear_pending_purchase` | Proven settled/refunded/no-receipt outcome | Clears the five pending fields only |
| Five `africa_rsa_purchase_*` entry effects | Existing owner route and target state | Revalidate non-cost gates, pay one bundle, apply original outcome, confirm or refund |
| `africa_rsa_queue_paid_regional_support_request` | Successfully settled request and eligible `FROM` | Records the donor pointer, sets its pending flag, and queues the existing reply event once |
| `africa_rsa_accept_pending_support_request` | Pending donor, original polity requirements, live Coalition and support capacity | Registers one supporter before the unchanged equipment shipment, then consumes pending state |
| `africa_rsa_refuse_pending_support_request` | Pending donor | Records one refusal and consumes pending state without refunding the submission fee |
| `africa_rsa_release_pending_support_request` | Recipient and stored Coalition target | Clears the pending flag and corresponding owner array pointer |
| `africa_rsa_clear_pending_support_requests` | Existing host transition/terminal/crisis cleanup | Clears only the recorded pending recipients and their pointer array |

The extracted `africa_rsa_apply_*` helpers in `common/scripted_effects/012_africa_rsa_effects.txt` apply the original four immediate outcomes without charging again.
The old public full-price effects retain their original payment contracts for direct callers.
No original outcome, proof consumption, cooldown, target pool, fire-once state, or AI weight is discounted.
The old relief gate accepted aggregate equipment stock below its exact model-specific debit, and several old resource gates used decimal tolerance.
The adapter checks the actual payable amounts and types inclusively, preventing a selection that cannot pay its stated price.
No additional reserve floor is imposed.

Usage example for the existing citizenship owner entry:

```text
africa_rsa_purchase_citizenship = yes
```

A caller needing quotation outputs must initialize the ordinary fields, quote fields, component quote, and validity before calling a quote wrapper.
The actual text consumers and payment entry already do this.
Temporary output variables and arrays created only inside a helper are not relied upon after return.

## Evidence and limits

Run `node docs/plans/026_black_friday_plans/verification/rsa_purchase_source_tests.mjs` from the mod root.
The source interpreter executes the actual owner adapter blocks with conservative helper temporary lifetime and an independent BigInt quotation oracle.
Its 295 checks include all five actions at three prices, each below-payable component, every payment and receipt failure position, repeated refunds, failed guarantees after sale expiry, invalid active quotes, route rejection, pending-receipt exclusion, rejected refund retention and later retry, quote disagreement, manual/forced achievement exclusion, 45 fresh text-trigger contexts, 75 invalid/pending fallback contexts, request settlement failure, and pending-donor exclusion.
The source comparison checks unchanged visibility, activation, target pools, target predicates, cooldowns, mission duration, fire-once state, and `ai_will_do` against `docs/testing/2026-10-03_event26_rsa_before/012_africa_rsa_decisions.txt`.
Native resource operations, shared receipt APIs, external route helpers, and achievement proof are explicitly mocked contracts.
The test does not establish engine rendering, exact native resource mutation, guarantee behavior, save/reload, multiplayer, or AI candidate selection.
Run `node docs/plans/026_black_friday_plans/verification/rsa_support_request_source_tests.mjs` for the bundle tests and 30 additional request-scope checks.
Those checks execute the actual pending-request and registration helpers under explicit country fixtures, with native dispatch, equipment transfer, and unchanged polity eligibility mocked.
They cover duplicate queue/reply, supporter-cap overflow, refusal, ended crisis, changed donor eligibility, cleanup, unchanged original target requirements, and unchanged reply AI expressions.
The archived decision's physical and raw committed bytes match SHA-256 `40283784e0d0ea091bd96c96c46f0155ec01e911091b2b20a0389ac5e1d696cc` after baseline repair commit `f9f057581c080784b92ed14fd0a736f6f9708958`.
No Hearts of Iron IV process was launched.

Reference evidence uses the offline wiki's Data structures lines 425-490, including helper temporary lifetime at line 440, and Localisation lines 680 and 729-791 for real localisation keys and temporary values.
Installed `documentation/triggers_documentation.md` covers temporary assignment at 7482-7502 and inclusive variable comparisons at 2110-2136.
Installed `documentation/effects_documentation.md` documents concrete equipment debit at 1252-1265, Command Power at 901, Political Power at 1854, Stability at 2173, and guarantees at 4565.
Installed decision documentation lines 1-46 and offline Decision modding lines 284-336 describe custom cost payment and literal AI hints.
The installed `WUW_GER_scripted_loc.txt` lines 689-697 and its `oppositional_monroe_list` localisation key provide the real-key temporary-text precedent.
The exact reference identities are retained in the universal-cost and numeric-binding handoffs rather than inferred from engine behavior.

## Assets and future work

This integration uses the existing RSA decision icons and introduces no visual asset or sprite.
Required decision, localisation, and probability review handoffs are under `docs/plans/026_black_friday_plans/subagent_handoffs/` with the `2026-10-03_rsa_*` prefix.
Native execution and final registry reconciliation remain completion gates.
Future refundable owner actions can reuse this bundle contract if their actual completion and cancellation callbacks are registered explicitly.
No such action is added here.

## Remaining owner findings

The decision audit's repeat-shipment finding is repaired by the pending-target and response guards above.
The native host and exile availability predicates retain their exact requirements and have concise player-facing summaries.
The post-war category can expose more than six native target clones in the audit's bounded scenario.
Restructuring or suppressing those target choices would exceed this cost integration's preserved-route contract, so the finding is unresolved Event 12 owner work rather than an implemented reduction.
The other four immediate actions retain their persistent receipt pointer if abnormal settlement fails after their outcome.
Their recovery behavior and the complete shared receipt implementation need the architect's actual-source receipt audit, and are not established by the bundle's mocked API.
Probability normalization also requires the category's unpaid lease action and expanded target instances, not only the five purchased decision IDs.
These limitations prevent a full Event 12 or Event 26 completion claim.
