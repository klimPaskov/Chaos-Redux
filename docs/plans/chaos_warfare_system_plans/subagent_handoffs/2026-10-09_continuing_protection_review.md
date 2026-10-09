# Continuing chemical protection repair

Disposition: implemented in the authorized source tranche.
Canonical documentation and parent source review are integrated; native execution remains unverified.
The parent accepted exact state-local interval-overlap accounting on 2026-10-09 under the existing hospital continuing-loss promise and same-mask 50% budget.
Subsequent parent instructions authorized future-date preservation, pre-hospital base extraction, centralized invalidation and state-local closure on every real control change, including suppressed Fallout rewrites.
No index change or commit was made.

## Requirement and frozen baseline

The specification is `docs/specs/chaos_warfare_system_specs/specs/07_gas_masks_civil_defence_and_population_protection.md:202–204`.
Protect Hospitals and Utilities consumes support equipment and masks and reduces medical saturation and continuing deaths.
Specification 13 supersedes conflicting older requirements, and the parent explicitly confirmed this hospital/medical behavior as accepted.
`corrections/2026-09-27_same_mask_hazard_budget.md` keeps actual issued masks foundational and caps combined additional chemical mitigation at 50% relative to the same-mask result.

The frozen baseline paid hospital response created a 14-day flag and local-supplies modifier.
The flag supplied authored +25 civilian medical protection and an initial medical-saturation multiplier of 0.85.
The continuing rate used contamination class, agent class and cached controller terminal doctrine.
The monthly event used that rate, density/infrastructure and the blister Burn Treatment factor.
The complete generic percentage-death, death-registration and population-handoff helpers had no hospital/current-mask consumer.
Hospital medical input did not indirectly lower contamination, whose protection multiplier uses decontamination.
The authored 14-day response and 30-day death period also meant a current-flag-only monthly check would miss the normal first response.

The baseline source is retained as exact `.before` files in `docs/testing/2026-10-09_continuing_protection/`.
Key original definitions were hospital payment/paid completion at `cbrn_immediate_response_cost_effects.txt:157–257`, rate/scheduler at `cbrn_chemical_state_effects.txt:243–325`, event `.4` at `cbrn_chemical_delivery_events.txt:154–215`, environment at `chaos_meter_effects.txt:3138–3219`, percentage loss at `3575–3707`, and death/population registration at `2774–2869`.

## Files and integration

| Source | Exact change |
| --- | --- |
| `common/scripted_effects/cbrn_continuing_protection_effects.txt` | New owner-specific STATE helper family below. |
| `common/scripted_effects/cbrn_chemical_state_effects.txt` | `cbrn_chemical_refresh_continuing_death_profile` retains authored scaled stage/class rate and defers terminal hazard to the current controller at the eligible tick. |
| `events/cbrn_chemical_delivery_events.txt` | `cbrn_delivery.4` uses the collector instead of direct Burn Treatment, consumes completed care, preserves future due dates and avoids extra duplicate receivers. Disabled/zero-rate due passes consume elapsed care without loss/RNG. `.1` and expired `.4` prune idle history. |
| `common/scripted_effects/cbrn_immediate_response_cost_effects.txt` | `cbrn_complete_paid_hospital_response` records an interval after the existing successfully paid outcome. The full payment/settlement order is unchanged. |
| `common/scripted_effects/cbrn_protection_effects.txt` | The hospital branch of `cbrn_clear_state_raid_dynamic_modifiers` invokes generic `cbrn_end_active_hospital_protection`, covering verified alert reset and existing centralized clears without recursion. |
| `common/on_actions/chaosx_on_actions.txt` | One call to that generic closure in the existing unconditional FROM.FROM block. Existing refunds, Fallout guard, mask transfer and kit callbacks remain unchanged. |

The six interval/lifecycle files above and three public-entry/quote files are edited; the payment effect also carries current ordinary prices into receipts.
The committed automatic-protection behavior and unrelated hunks are preserved.
Occupation/transaction owners, Fallout, Chaos Meter, global registries, initial exposure/consequence source, price constants, projects, weights and assets remain unchanged.

## Helper contracts

All helpers are STATE-scoped.

| Helper | Inputs/outputs | Defaults and side effects | Consumers |
| --- | --- | --- | --- |
| `cbrn_prepare_hospital_history_cutoff` | Caller-owned temporary cutoff output, current day and optional due date. | Keeps one authored idle period or older time still owed by a pending callback. Temporary arithmetic. | Registration, invalidation, idle prune. |
| `cbrn_prune_hospital_protection_history` | Cutoff, truncate proof, optional end limit and aligned normal start/end arrays. | Mismatched lengths retain evidence. Rebuilds retained rows after traversal, with private reset break/index names. | Registration, invalidation and cleanup wrappers. |
| `cbrn_record_paid_hospital_protection_interval` | Existing response duration and current day. | Positive successfully paid time is appended/merged chronologically without stacking. No payment. | Successful paid hospital completion. |
| `cbrn_end_active_hospital_protection` | Exact native/reset current day. | Ends future care, preserves elapsed owed care, clears hospital flag/modifier idempotently. No country stock/aggregates. | Real control callback and central response clear. |
| `cbrn_prune_idle_hospital_protection_history` | Current day and optional due date. | Drops unusably old time and retains recent/future valid care for later overlap. | Terminal contamination/expired callback cleanup. |
| `cbrn_measure_hospital_protection_overlap` | Scheduled period start/end and caller-owned fraction output. | Starts at zero. Union-intersects chronological equal-length rows and clamps fraction to 0–1. | Continuing collector. |
| `cbrn_calculate_continuing_civilian_protection` | Stored class, current real mask/fitting/filter/kit snapshot, pre-hospital medical base and caller-owned mask/without/with outputs. | Calls unchanged pure calculator twice, preserving inherited enum, six inputs, outputs and medical scratch. No attacker/raid/target context. | Continuing collector. |
| `cbrn_apply_continuing_civilian_protection` | Caller-owned scaled percentage and environment scalar, rate/class/due, paid intervals and current valid controller. | Defaults to unprotected factors if input cannot resolve. Applies authored current protection and Burn Treatment once under same-mask floor, with terminal percent quantization once. | Eligible `cbrn_delivery.4` branch. |
| `cbrn_finish_continuing_hospital_protection_window` | Execution day. | Consumes completed portions and retains future care, including disabled/zero-rate passes. | Legitimate due callback. |

Persistent data is limited to STATE `cbrn_hospital_protection_start_days` and `cbrn_hospital_protection_end_days`.
No target namespace, new flag, tuning category, global registry or periodic hook was added.
All constants, thresholds, durations and coefficients remain authored in existing CBRN files.

### Calculation and timing

The loss window is `[due_day - period_days, due_day]`.
Paid fraction f is union-covered days divided by the authored 30-day period.
Both medical passes sample the same current discrete issued models, fitting, filter condition, current military-priority kit coverage and controller values.
This accepted model does not reconstruct a historical equipment/medical-capacity timeline.

The existing shared snapshot's `cbrn_state_controller_medical_capacity` temporary is caller-declared before its call and captured afterward.
The without-hospital pass uses that base.
The with-hospital pass adds authored 25 and clamps to the existing limits.
No 25 is subtracted from an already clamped combined snapshot, preserving bases 0/50/90/100 correctly.

The pure calculator returns same-mask M, P_without and P_with.
The period protection is `P_without * (1 - f) + P_with * f`.
The existing Burn Treatment helper supplies B once.
Combined protection is clamped at `M * constant:cbrn_hazard_budget.residual_floor`, whose authored value is 0.50.
There is no new hospital death coefficient and no conversion of initial saturation's 0.85 into a death bonus.

Current terminal hazard's authored 1.10 multiplies caller-owned scaled percentage once before population/divisor arithmetic.
Stored stage/class rate stays raw.
This preserves original five-decimal quantization, including local blister `.00125 * 1.10 → .00137`, and prevents stale former-controller doctrine.
Terminal hazard is common to full and same-mask outcomes, outside the additional-support budget.

Authored plateaus remain.
Full sealed/full-kit medical 50 yields M and P_without .12/.42/.32/.20 for choking/blister/nerve/incapacitating.
Authored +25 reaches medical 75 and yields P_with .06/.21/.16/.10.
Zero/partial/basic issue, exhausted filters, inadequate fitting or missing kits can remain on a plateau.
Medical bases 90/100 remain exact, with the hospital pass capped at 100.
The 50% bound is a factor floor before existing RNG, rounding and episode caps, without a claim about engine-measured integer death ratios.

### Lifecycle

Only the existing successful paid outcome records care.
Timed flags alone do not create intervals.
Repeated/overlapping 14-day responses merge actual paid windows and retain future portions across periods.
Expired flags can still represent paid service earlier in the measured period, but no later period receives credit without overlap.
Early/stale callbacks preserve a future due date and do not enqueue another receiver.
Late legitimate callbacks measure the originally scheduled 30-day window, then rearm from execution day as before.
Callback count never stands in for elapsed service.
Disabled/zero-rate due passes consume elapsed care without loss or RNG, preventing later phantom credit.

A second verified alert follows its existing reset policy and truncates future care centrally.
Unverified alerts leave care intact.
Central closure works even when the modifier is absent, and transfer plus central duplicates are idempotent.
Every real native control change closes future care at its exact day, including zero-mask states and suppressed Fallout rewrites.
The existing Fallout guard still suppresses all ordinary mask/kit callbacks.

The parent accepted independent hospital closure after inspecting `fallout_restore_state_controllers_to_owners:46208–46213`, map return `46091–46146`, and generic state cleanup `46168+`.
Those final paths have no CBRN care disposition.
No Fallout edit or guessed later-snapshot cutoff was used.

## Public entry and quote integration

The existing hospital decision, `cbrn_state_has_hospital_response_need` and the payment gate share exact-alert-or-current-contamination relevance, current control and the active-response exclusion.
`common/decisions/cbrn_protection_decisions.txt`, `common/scripted_triggers/cbrn_protection_triggers.txt` and `common/scripted_triggers/cbrn_immediate_response_cost_triggers.txt` provide that public path.
The existing quote uses current FROM STATE population with unchanged ratios, bounds and rounding; its two ordinary outputs are declared by the order before preflight and supply all receipt and purchase-basis inputs.
All three cost getters, both decision affordability gates and the order consume the same quote without any alert-time cache prerequisite.
The former alert-only action is unavailable for contamination-only states in the frozen public baseline; the current action is usable with actual contamination and sufficient supplies.
No active source caller supplies the exact-alert adapter, and this repair neither fabricates alerts nor broadens other pre-raid actions.

The 32 added cases cover public before/after relevance, real getter/preflight agreement below/exactly at/above each payment, current population bounds and rounding, ignored stale caches, all five mask models, duplicate orders, controller loss, ordinary and two discounted receipt fixtures, rejected settlement/refund without care, and paid care expiring before the loss tick.
Native component-price services, stock commands, receipts and the final purchase observer remain modeled boundaries.
The population formula, five-model allocation, public decision predicates, live preflight, ordinary receipt inputs and order/service logic execute actual source ASTs.
The rejected-refund fixture verifies retained recovery status and absence of care; it does not claim a successful native refund.
The parent corrected one test expectation to the existing VM's `@1` targeted-key spelling; production code was unchanged.

## Meaningful validation

Run `node docs/testing/2026-10-09_continuing_protection/continuing_protection_source_tests.js`.
The final parent run passed 157 cases with zero failures, plus four ROOT-binding probes.
It reuses the existing parser and unchanged conservative VM.run cleanup, plus the earlier scope/stock adapter prelude without changing or running that earlier suite.
Frozen before ASTs exclude every new helper definition.
After cases execute actual production interval, snapshot/kit/protection, hospital order/gate/payment, rate, event and control bodies.

The parent-reviewed ROOT fidelity correction binds continuing state events and scalar/state-only helpers to STATE ROOT throughout nested controller scopes.
Paid outcomes/orders retain payer COUNTRY ROOT, and native control callbacks retain new-controller COUNTRY ROOT.
ROOT values, scoped normal/native reads and ROOT scope entry all resolve that binding independently of current scope, while scoped reads cannot resolve an unscoped temporary.
Country-only and state-only native flag/stock/technology commands assert their required current scope.
The original 125 cases and four binding probes remain in the final suite alongside 32 public-entry, quote, cost, receipt and lifecycle cases.
The final result records the exact state-event, state-helper, paid-outcome, public-order and control-callback binding counts.
No production dependency on country ROOT was exposed in the state-event correction; the public-entry extension additionally reads FROM native inputs independently of normal and temporary variables.
The final test harness SHA-256 is `70348df169504a0d0537e17d3e5a6c0c5c18bc071944cd135686d8762dbc522c`.
BaseVM.run and its conservative temporary cleanup were not changed.

The hospital-order AST matches its frozen original after exactly two caller-owned ordinary-price declarations and four authorized cached-price-to-current-output substitutions in receipt and achievement fields.
Removing the one new control call makes the entire shared on_actions AST match its frozen original.
Initial exposure/consequence and shared percentage/RNG/cap/population source remain untouched.

Cases cover all four classes and zero/partial/basic/sealed real issue, the first 14-day response expiring before day 30, pre-exposure/cross-period/repeated/overlapping windows, military-priority missing/partial kits, filters/fitting, medical 0/50/90/100, the hospital threshold, combined MIO/terminal floor, current-controller changes, below/exact/above real mask stock in before/after ordinary payment orders, verified/unverified resets, missing modifiers, ordinary/suppressed zero/positive-mask transfers and repeated closure.
They also cover 32 matched all-class/all-stage unprotected loss/RNG/due cases, early/stale/duplicate/late callbacks, disabled/zero-rate/zero-population no-loss passes, private cursor/break isolation, over 1,000 pruning rows, mismatched paired lengths retaining evidence and a bare timed flag creating no credit.

Native scope/stock, dates/expiry, ordinary quote outputs and native receipt settlement are explicit fixture models.
The actual percentage/RNG/cap body runs with identical declared severity/cap draws on both sides.
Its register-deaths boundary observes calculated loss without executing unrelated global history/UI.
Initializers and unrelated achievement refreshes are initialized/no-op model boundaries.
Callbacks do not mutate country stock or PP in the cases.
This is source execution under declared native dependencies, with no engine-emulator or in-game claim.

Exact before/after bytes, attributes, hashes and diffs are in `source_metadata.json` and `.before/.after/.diff` files.
Snapshots use scoped -text attributes.
The nine gameplay hashes match current source, frozen after files and `source_test_results.json`.
Dependency hashes and individual results are retained.
Writes used guarded same-directory staging and os.replace, preserving unrelated changes.

### MCP/reference limits

Narrow before/final `cbrn_delivery.4` traces use downstream depth 2, max 12 nodes/20 edges and requested helper expansion.
Before revision: `283a550085362183c930b3e9508acd4051d381fab0d6edd4f1b8afac59de6889`.
Final revision: `55ea5af07a5d87470ed643708cef316ac4112d82a4dc54bf7c1b56a28c7598d9`.
Both are focused partial results with zero helper projections and deferred lifecycle analysis.
Exact artifact URIs, hashes and byte counts are retained in `event_baseline.json` and `event_frozen.json`.
The large trace bodies were not recovered or promoted to complete helper evidence.
No broad scan, helper-expansion job or unnegotiated task was repeated.

Explicit STATE snippet checks are retained for pruning, registration, calculator, collector, invalidation and the event.
Final packets report SCRIPT_CHECK_PARTIAL, valid=null, no reported syntax/kind/scope error, and unresolved helper/native argument semantics with bounded omitted findings.
Earlier packet stages remain distinguishable.
The generic native-random probability inspection reported no_weighted_surfaces despite visible set_temp_variable_to_random commands.
This is an adapter coverage gap, not a deterministic-loss or complete-probability claim.
Original random/cap inputs are preserved and covered by the 32 matched unprotected cases.
Parent event/probability review remains separate.

| Reference | Read lines | Revision |
| --- | --- | --- |
| Offline Data structures | 425–443 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline Event modding | 212–226 | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |
| Offline Effects | 824–857 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline On actions | 450 | `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a` |
| Installed effects_documentation | 2278–2292, 2681–2694, 4279–4295, 8096–8128 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed script_concept_documentation | 184–222 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed on_actions/_documentation | 68–70 | `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4` |

Offline sources resolve under repository paradox_wiki, installed sources under the vanilla HOI4 directory.
Vanilla `common/on_actions/00_on_actions.txt:5076–5097` supplies the direct FROM.FROM precedent.
The existing vanilla clamp precedent is operation_strat_effects.txt.
Reference-context omissions and domain coverage gaps were not substituted with source-equivalent engine claims.

## Parent integration and limitations

No gameplay simplification was made.
The accepted discrete-tick interpretation, plateaus and current hazard quantization are explicit.
No numerical hospital coefficient, new price/duration/decision/project gate, world iteration, native debit receipt or attacker context was introduced.
The parent owns canonical helper documentation, specification/ledger/system alignment, final audits and commit.
Add the helper contracts, returned medical base, raw rate/current terminal percent point, interval semantics, disabled-loss pruning and unconditional invalidation to cbrn_scripted_effects.md and matching owner docs.
No new icon or localisation key is required.

Native timers/callback ordering, inventory/receipt behavior, random distributions and full population/history execution remain unproved.
Mismatched paired history is retained and cannot grant hospital time, with no automatic corruption recovery.
Valid registration creates chronological merged rows, while externally malformed unsorted dates are outside the accepted contract.
HOI4 was not launched, and no log or live-game action was requested.
Skills used: chaos-redux-events, chaos-redux-decisions-missions and chaos-redux-subagents.

The parent ran the same 157 cases and four ROOT-binding probes from an isolated proposed commit tree; scenario results matched the working run.
The receipt is `docs/testing/2026-10-09_continuing_protection/parent_isolated_source_review.json`, which distinguishes unchanged raw baseline snapshots, normal Git line-ending conversion and two unrelated shared-tree constant-file differences.
Those unrelated files are excluded from this commit, and matching fixture results do not establish their equivalence outside the tested cases.
