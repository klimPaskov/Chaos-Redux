# Event 012 Gods full grading helper API

Disposition: implemented bounded arithmetic repair on 2026-10-04; independent parent arithmetic re-review and combined integration remain pending.
Acceptance basis: the user's 2026-10-03 assignment implementing the accepted full grading/rewards design without simplifications.
Owner: chaosx_scripted_system_architect.
All effects and triggers have participant COUNTRY scope and are called with `= yes`.
Inputs are caller-set variables or retained normal ledger fields; there are no scripted arguments.
The public API is static and does not grant native goods.

## Helper map

| Helper | Inputs and defaults | Outputs and side effects | Parent call site |
| --- | --- | --- | --- |
| `gods_of_africa_initialize_grading_ledger` | Caller temp `gods_of_africa_grading_first_genuine_history = 1`; existing COUNTRY; ledger flag and issued field absent. Missing authorization performs no ledger initialization. | Consumes the caller authorization to zero; initializes the genuine actual ledger and new receipt/conduct storage; sets `gods_of_africa_grading_ledger_initialized`. Re-entry retains all normal history. | Only the first-genuine-history branch of `gods_of_africa_initialize_participant_history`. |
| `gods_of_africa_normalize_paid_quantity_milli` | Caller temps `gods_of_africa_normalize_paid_k`, `gods_of_africa_normalize_denominator`, `gods_of_africa_normalize_bound_milli`; accepted ten denominators and bound 16000. | Caller-owned temp `gods_of_africa_normalize_output_milli`; preinitialize to zero before call. Missing or nonpositive denominator/bound returns zero; arbitrary positive parameters are outside the certified domain. Internal scratch temps do not escape. | Freeze's explicit ten-kind calls for each of four quantity sets; optional parent arithmetic reuse. |
| `gods_of_africa_floor_temporary_value` | Caller temp `gods_of_africa_floor_input`. | Caller-owned temp `gods_of_africa_floor_output`; preinitialize to zero before call. Certified domain is 0-60000; missing input returns zero. Round then subtract one when rounding exceeded the input. | Entitlement's equipment and fuel arithmetic; reusable parent integer allocation arithmetic. |
| `gods_of_africa_freeze_final_grade_inputs` | Strict retained-history identity, initialized complete ledger, committed host endpoint, frozen host capability/doctrine, closed ordinary contract, and no participant outcome/freeze. | Durable snapshot, bounded derived milli-values, `gods_of_africa_grade_inputs_frozen`; invalid/inconsistent evidence sets `gods_of_africa_grading_unresolved` without outcome or entitlement. A successful snapshot is immutable on replay. | Participant final classifier after neutral closure/ordinary-demand clearing and the parent's conduct refresh, before any history cleanup. |
| `gods_of_africa_calculate_settlement_entitlement` | Valid frozen inputs and one existing four-standing enum in `gods_of_africa_final_settlement`; entitlement pair incomplete. | Only normal `gods_of_africa_reward_equipment_entitlement` and `gods_of_africa_reward_fuel_entitlement`. A completed pair remains unchanged; an incomplete pair is recomputed from the frozen inputs. No source, owed, delivery, reward, or outcome receipt is written. | Parent's obligation initializer after selecting the standing and before its source/owed commitment. |

| `gods_of_africa_required_fulfilled_count` | Caller temps `gods_of_africa_ratio_eligible` (nonnegative integral receipt count), `gods_of_africa_ratio_percent` (80, 90 or 50), and preinitialized `gods_of_africa_ratio_required_output`. Inputs are required; no default eligibility. | Caller output is exact `ceil(percent * N / 100)`; local floor/remainder scratch only. | Freeze computes four doctrine/standing requirements. |
| `gods_of_africa_floor_scaled_entitlement` | Caller temps `gods_of_africa_entitlement_contribution_milli`, `gods_of_africa_entitlement_coefficient`, `gods_of_africa_entitlement_denominator`, and preinitialized `gods_of_africa_scaled_entitlement_output`. Required domain is C_milli 0-16000, coefficient/denominator from the table below. | Caller output is exact integer floor of the rational reward; scratch only, no standing cap or durable write. | Entitlement computes equipment and fuel before publishing the completed pair. |

Temporary values are unscoped.
The immediate caller must own any temporary output it reads after helper return.
Both nested normalize and floor call sites already initialize their forwarded output storage.
An outer caller using either utility must follow the same rule.

## Initial actual ledger

The ten kinds are `infantry`, `support`, `trucks`, `artillery`, `armor`, `aircraft`, `fuel`, `convoys`, `trains`, `manpower`.
Each kind has exactly four normal thousands fields: `gods_of_africa_paid_<kind>_k`, `gods_of_africa_voluntary_paid_<kind>_k`, `gods_of_africa_emergency_paid_<kind>_k`, and `gods_of_africa_campaign_paid_<kind>_k`.
All forty start at zero only under first-genuine-history authorization.
Emergency political power is the separate raw-PP field `gods_of_africa_emergency_paid_pp`.
No coarse history, quote, promise, procedural click, host gift, or protection receipt is converted to quantity.

The initialized count and cache fields are:

- `gods_of_africa_demands_issued`
- `gods_of_africa_demands_retired`
- `gods_of_africa_demands_fulfilled`
- `gods_of_africa_demands_full_original`
- `gods_of_africa_demands_honored_substitute`
- `gods_of_africa_demands_failed`
- `gods_of_africa_demands_refused`
- `gods_of_africa_demands_broken_by_war`
- `gods_of_africa_compliance_streak`
- `gods_of_africa_longest_compliance_streak`
- `gods_of_africa_post_reconciliation_fulfilled`
- `gods_of_africa_post_reconciliation_failures`
- `gods_of_africa_post_reconciliation_refusals`
- `gods_of_africa_war_count`
- `gods_of_africa_treaty_break_count`
- `gods_of_africa_reconciliation_count`
- `gods_of_africa_observed_host_core_count`
- `gods_of_africa_owned_host_core_count`
- `gods_of_africa_emergency_paid_pp`

The initializer also starts live and last-closed contract identities, material transfer sequence/consumption/receipt fields, and `gods_of_africa_reconciliation_fulfilled_baseline` at zero.
It empties only the new `gods_of_africa_occupied_core_state_ids` and `gods_of_africa_returned_core_state_ids` arrays.
It clears only the new prior-conduct, observation, actual outstanding-offense, ledger, and material-receipt flags.
It does not clear existing live defiance, permanent opt-out, coarse history, or participant membership.

The initializer is not a migration.
The parent must never supply its first-history authorization for an existing coarse-history participant, even when the old history count is zero.
A missing genuine actual ledger makes final evidence unresolved.
Migration without actual receipts is unsupported.

## Freeze contract and actual field names

Retained-history proof delegates current-or-one-inherited-generation selection to `gods_of_africa_participant_has_settlement_history`, then additionally requires existing exact `gods_of_africa_history_owner_id = THIS.id` and `gods_of_africa_history_origin_host_id = event_target:africa_host.africa_origin_host_id`.
The participant must exist and cannot be the host under that parent's existing history trigger.
The host must have `gods_of_africa_final_settlement_committed`, `gods_of_africa_settlement_final_strength`, and `gods_of_africa_settlement_final_doctrine`.
Doctrine must be one of 0, reciprocal, exaction, or ambiguity.
Both `gods_of_africa_contract_ledger_open` and `gods_of_africa_demand_active` must be clear.

Every actual ledger scalar must exist and be nonnegative.
All eighteen count/cache fields must also be integral actual receipts.
Their validation scratch uses modulo one and must have remainder zero, so no assumed numeric maximum limits grading eligibility.
That upper value is the largest positive integer representable under the conservative storage contract, not a gameplay/history cap.
Emergency PP remains fractional and is excluded from this integer test.
Each voluntary/emergency/campaign kind subset must not exceed its actual total kind.
The freeze requires `issued - retired = fulfilled + failed + refused + broken_by_war`, a nonnegative denominator, and `fulfilled = full_original + honored_substitute`.
Validation starts from N, then subtracts each terminal count only when the residual is at least that count.
A failed comparison blocks every later residual subtraction.
Full-original plus honored-substitute is checked as `F - full_original = honored_substitute` after proving `F >= full_original`, without summing them.
An invariant failure leaves the inputs unfrozen, sets unresolved, and creates no standing.
Zero denominator sets `gods_of_africa_grade_no_contract_history`; the better-standing ratio checks require a positive denominator.

All nineteen count/cache/PP fields and all forty actual quantity fields are copied using the exact same suffix under `gods_of_africa_grade_`.
Examples are `gods_of_africa_grade_demands_issued`, `gods_of_africa_grade_emergency_paid_pp`, and `gods_of_africa_grade_voluntary_paid_infantry_k`.
Additional normal frozen fields are `gods_of_africa_grade_eligible_demands`, `gods_of_africa_grade_returned_core_state_count`, `gods_of_africa_grade_occupied_core_state_count`, `gods_of_africa_grade_wrath`, `gods_of_africa_grade_history_owner_id`, and `gods_of_africa_grade_history_origin_host_id`.
Existing participant snapshot names are preserved: `gods_of_africa_settlement_strength`, `gods_of_africa_settlement_doctrine`, `gods_of_africa_settlement_generation`, `gods_of_africa_settlement_origin_host_id`, and `gods_of_africa_settlement_history_generation`.
They use the host's frozen capability, not live capability.
The parent must not overwrite them with live host values in its old classifier.

Frozen boolean flags are:

- `gods_of_africa_grade_prior_defiance`
- `gods_of_africa_grade_prior_war`
- `gods_of_africa_grade_prior_occupation`
- `gods_of_africa_grade_prior_treaty_break`
- `gods_of_africa_grade_current_war`
- `gods_of_africa_grade_unresolved_treaty_break`
- `gods_of_africa_grade_unresolved_major_offense`
- `gods_of_africa_grade_permanent_opt_out`
- `gods_of_africa_grade_defiant`
- `gods_of_africa_grade_reconciliation_accepted`
- `gods_of_africa_grade_no_contract_history`

Current war is checked directly against the proven host.
Other conduct is read from the parent's actual flags and current core caches.
The actual outstanding major-offense input is `gods_of_africa_unresolved_major_offense`; generic offender-selection flags alone are not treaty proof.
Reconciliation acceptance is `gods_of_africa_reconciliation_count > 0`.
The parent must refresh conduct caches before freeze, retain prior flags on acceptance, reset post-acceptance counters at actual acceptance, and update them through unique terminal closures.

Derived normal fields are `gods_of_africa_grade_material_milli`, `gods_of_africa_grade_voluntary_milli`, `gods_of_africa_grade_emergency_milli`, `gods_of_africa_grade_campaign_milli`, `gods_of_africa_grade_exceptional_sum_milli`, `gods_of_africa_grade_effective_failures`, and `gods_of_africa_grade_effective_refusals`.
Ratio proof compares the actual frozen `gods_of_africa_grade_demands_fulfilled` with `gods_of_africa_grade_ratio_<reciprocal|exaction|ambiguity|respected>_required_fulfilled`.
These four private normal fields replace the previous percent cross-products; all four predicate consumers were changed together.
They mean required fulfilled contracts, never percentages or denominators.
Post-reconciliation effective adverse counts replace the applicable lifetime comparison record while all lifetime fields remain frozen.

## Standing trigger map

Parent binds its existing final classifier aliases to:

- `gods_of_africa_full_grade_enemy_is_valid`: enum 4.
- `gods_of_africa_full_grade_favored_is_valid`: enum 1.
- `gods_of_africa_full_grade_respected_is_valid`: enum 2.
- `gods_of_africa_full_grade_distrusted_is_valid`: enum 3.

Check `gods_of_africa_full_grade_inputs_are_valid` before selecting or committing any standing.
All four public standing checks reject an unresolved or absent freeze.
The checks are mutually exclusive in Enemy, Favored, Respected, Distrusted order.
The parent's old unconditional Distrusted fallback must not run when freeze failed.

Supporting triggers are `gods_of_africa_full_grade_history_is_valid`, `gods_of_africa_full_grade_ledger_is_present`, `gods_of_africa_full_grade_freeze_is_authorized`, `gods_of_africa_full_grade_has_prior_hostility`, `gods_of_africa_full_grade_favored_recovery_is_valid`, `gods_of_africa_full_grade_respected_recovery_is_valid`, `gods_of_africa_full_grade_single_exceptional_is_valid`, `gods_of_africa_full_grade_favored_doctrine_is_valid`, and `gods_of_africa_full_grade_respected_adverse_record_is_valid`.

The doctrine matrix, strict Wrath bands, Enemy causes, ratio gates, streaks, aid/return alternatives, and post-reconciliation recovery are the accepted design.
No chosen doctrine shares ambiguity's Favored gate; only actual strategic ambiguity gets the relaxed Respected failure/refusal ceilings.
Current hostility wins over any contribution or repaired prior history.

## Constants and arithmetic

The grading file owns exactly four categories: integer `gods_of_africa_grading`, `gods_of_africa_contribution_units`, `gods_of_africa_reward_units`, and fixed-point `gods_of_africa_reward_scale`.
The sole `gods_of_africa_contract_close` owner is `012_africa_gods_contract_constants.txt`, with `war_breach = 5`; that file is outside this repair ownership.
Each schema is the first entry.
The additional `gods_of_africa_grading.ratio_percent_scale = 100` keeps compliance comparison independent from the Strength divisor.
The exact accepted close enum is full_original 1, honored_substitute 2, failure 3, refusal 4, war_breach 5, retired 6.
The parent owns contribution-kind enums in its contribution owner.

Normalization first prepares the exact scale `1000 * 1000 / native_denominator`, then the cap `16000 / scale`, bounds the actual quantity in temporary storage, and multiplies once.
The parent already corrected this order; this repair retains it.
Only the ten listed denominators and bound 16000 are certified here; an arbitrary positive denominator/bound is not a generic range-safe API.
The denominators are `infantry = 1000`, `support = 500`, `trucks = 100`, `artillery = 50`, `armor = 25`, `aircraft = 50`, `fuel = 1000`, `convoys = 20`, `trains = 20`, `manpower = 10000`.
A one-man payment is 0.001k and gives 0.1 milli-package.
500 actual qualified emergency PP gives 1000 emergency milli-packages and zero material milli-packages.
The bounded derived aggregates saturate at 16000 milli-packages; each input is capped before multiplication, each aggregate after addition.
This retains every grading threshold and the reward contribution ceiling while every actual snapshot remains uncapped.
Emergency PP first computes scale `1000 / 500 = 2`, then cap `16000 / 2 = 8000`, bounds a temporary copy of actual paid PP, and multiplies by 2 once.
Its largest converted term is 16000, and it never enters material, voluntary, or campaign aggregates.

For integral N, ratios split `N = 100q + r`, `q = floor(N / 100)`, `r = N - 100q`.
Each exact required F is `percent*q + ceil(percent*r/100)` for 80/90/50.
The largest q*percent is 1932660, r*percent at most 8910, and final required count at most 1932735.
No historical count is reduced or capped.
Rewards use `C = min(16, M + 0.5V + 0.5L)`, `S = clamp(frozen_strength, 0, 100) / 100`, Favored `B = (1 + 2S) * (1.25 if reciprocal else 1)`, and Respected `B = 0.25 + 0.75S`.
Integer entitlements are equipment `floor(min(ceiling, 1000CB))` and raw fuel `floor(min(ceiling, 500CB))`.
Favored ceilings are 50000/25000; Respected ceilings are 10000/5000; Distrusted/Enemy use zero.
There is no base gift, PP fallback, payment effect, or native stock assumption.

Arithmetic uses these direct raw-Strength coefficients instead of storing S or prematurely rounded B:

| Standing/doctrine | Coefficient | Equipment D | Fuel D |
| --- | --- | ---: | ---: |
| Favored, other/default | 50 + Strength | 50 | 100 |
| Favored, reciprocal | (50 + Strength) * 5 | 200 | 400 |
| Respected | 100 + 3*Strength | 400 | 800 |
| Distrusted / Enemy | 0 | 50 | 100 |

All integral-count checks use documented modulo-one scratch validation; the former assumed-maximum constant has been removed.
New fixed-point reward-scale keys are `arithmetic_split_base = 100`, `favored_coefficient_base = 50`, `favored_denominator = 50`, `reciprocal_coefficient_multiplier = 5`, `reciprocal_denominator = 200`, `respected_coefficient_base = 100`, `respected_coefficient_strength_multiplier = 3`, `respected_denominator = 400`, and `fuel_denominator_multiplier = 2`.
These rational coefficients are authoritative for calculation; retained older S/B constants describe the accepted formula and are not evaluated by this helper.
A tuning change must keep the rational table algebraically equivalent to the accepted formula rather than independently moving the old descriptive anchors.

For each component, split `C_milli = 100q + r` and set `denomA = D / 100` (exactly 0.5, 1, 2, 4 or 8).
Calculate `numeratorA = q*coefficient`, `floorA = floor(numeratorA/denomA)`, `remainderA = numeratorA - floorA*denomA`, `numeratorB = remainderA*100 + r*coefficient`, and result `floorA + floor(numeratorB/D)`.
Then apply the standing ceiling to the completed integer.
Native material thousands fields on the conservative 0.001 grid normalize to multiples of 0.1 milli, so half-subset premiums and C_milli remain exact multiples of 0.05.
Raw frozen Strength on the 0.001 grid produces an exactly representable coefficient.
q is integral, so numeratorA is exact on that grid; floorA*denomA and remainderA*100 are exact too.
Only the positive r*coefficient product may truncate below 0.001.
Every integer-floor threshold is an integer multiple of D, and the other summand is on the 0.001 grid.
A downward error smaller than 0.001 cannot cross such a threshold: at equality the product must itself have a representable fractional part, and above it the truncated result stays on or above the grid threshold.
Truncating a positive quotient to 0.001 also preserves its integer floor.
Thus no residual precision gap remains within the declared input domain and conservative truncation model.

q is at most 160, coefficient at most 750, numeratorA at most 120000, floorA at most 60000, and floorA*denomA at most numeratorA.
remainderA is below denomA (at most 8), so its scaled term is below 800; r*coefficient is below 75000; numeratorB is below 75800.
The uncapped integer reward maxima are 60000 equipment / 30000 fuel.
All intermediate magnitudes fit the assumed 2147483.647 positive bound.
No source flag, outcome, native grant, owed field, or delivery receipt is written here.
Only after both temporary component results are complete does the helper publish the durable pair; replay with both fields present preserves it, and a partially present pair can be recalculated.

These are conservative source arithmetic proofs and bounded source-model cases.
Installed documentation confirms the variable operators and fixed-point math but does not fully specify engine width or precision.
The offline five-decimal/wider-whole-number claim is not used as a primary engine guarantee.
No native engine verification is claimed.
The three-decimal, 2147483.647 model is a conservative audit contract; modifier precision and deprecated plain manpower getter limits do not establish ordinary variable storage width.
Actual ordinary-variable width and precision remain a documentation gap.


## Parent migration and cleanup

1. Initialize only new genuine history with the explicit caller authorization.
2. Install actual receipt and unique closure owners; keep all live and retained history fields unchanged on re-entry.
3. Freeze common host Strength/doctrine once before the retained candidate census.
4. Neutral-retire and clear an ordinary open demand, refresh actual conduct, then call freeze before cleanup.
5. Guard the four-way classifier with valid frozen inputs, bind existing core aliases, and select one enum.
6. Calculate entitlement once, then let the parent create the immutable source/receiver obligation and standing diplomacy.
7. Let the parent deliver native source-funded goods and update owed/delivered/complete receipts.
8. Retain all actual ledger, frozen inputs, entitlements, prior flags, and unique state arrays through ordinary cleanup, archival, acknowledgement, and deferred delivery.

There are no new event targets.
Existing `event_target:africa_host` is read only during identity validation and freeze; frozen grading and entitlement do not follow a replacement host pointer.
The parent's regular report-chain target and durable source identity remain its owners.
No new world observer, periodic hook, CXT package, asset, icon, or GUI is introduced.
Presentation reuses the accepted existing settlement assets through parent wiring.
Future extensions should retain these explicit receipt and frozen-input contracts; no additional mechanic is proposed.

See [current arithmetic repair handoff](../../docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_grading_arithmetic_repair_2026-10-04.md) for current bounded cases, source hashes, mathematical proof, MCP route limits, and pending independent review.
The [original helper handoff](../../docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_grading_helpers_2026-10-03.md) retains historical five-decimal fixture provenance; it does not certify current arithmetic.


## Parent correction of count eligibility

The independent review identified the scratch maximum as an actual grading eligibility restriction, not merely an unchanged historical field.
The parent removes `maximum_integral_count` and replaces all eighteen clamp/round integer checks with remainder modulo one on caller-owned scratch, requiring remainder zero.
The installed trigger documentation explicitly supports `modulo_temp_variable` at `documentation/triggers_documentation.md:6442?6454`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`; the effect counterpart is `effects_documentation.md:4986?4998`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
This validates integral receipt counters without imposing an assumed numeric maximum or rounding a near-maximum field upward.
Actual history remains untouched, and the residual accounting and exact ratio decomposition remain unchanged.
The earlier bounded maximum description records the pre-correction source; independent same-case review is required for this replacement.
