# Event 112 shared helper integration review

## Evidence boundary

All nine files in repository_evidence.json were fully semantically read at commit `a3ef485c5da7e2337122eca04ac65c175050f251`.
The checked line ranges below identify the particular bodies used for each conclusion.
They are line numbers in the normalized local reference copies, with original Git blob identities preserved in the ledger.
The October 10 supplied owner contracts remain the newer authority.
No installed-game scenario, log inspection, MCP validation suite, or live trace was run.
These are source and contract findings, with arithmetic implications identified as inferences where engine semantics remain unverified.

## Exact shared contracts that the design needs

| Owner interface | Contract used by Event 112 | Evidence and disposition |
|---|---|---|
| `damage_state_building_dynamic` | Damage one deliberately selected native building in the explicit state scope | Present at lines 49 to 60 of the pinned dynamic effects file, while exact fractional damage and selected-state behavior still require an installed scenario |
| `apply_state_population_loss_without_recruitable_manpower_gain` | A physical state population debit must not create recruitable manpower as a side effect | Present at lines 539 to 626, optional civilian relocation requires the newer complete transaction contract |
| `apply_exact_state_civilian_population_loss` | Validate floor, perform one physical loss, observe actual loss, then register exactly that loss without a second debit | Pinned lines 628 to 716 differ from the newer owner contract |
| `union_compatible_researched_technologies_from_donor` | Full admitted sovereign continuity only, never a generic reward for one tradition or state | Present at lines 482 to 528 and deliberately excluded from ordinary Event 112 actions |
| `universal_cost_quote_integer` | Owner computes ordinary current price, helper composes eligible sources, one quantized final quote drives display and payment | Present at lines 420 to 598, composition and quantization must be reconciled with the newer documented algorithm |
| `universal_cost_check_quote_affordable` | Native resource availability is checked against the exact final quote | Lines 675 to 687 call the shared trigger, inclusive boundary required |
| `universal_cost_pay_component` | Pay one supported resource kind after the complete action preflight | Lines 698 to 997 issue native effects, owner must still prove actual debit |
| `universal_cost_record_transaction` | Unique positive transaction and component IDs, ordinary and quoted amounts, actual amount equal to quote, payer-owned ledger | Lines 1222 to 1456 reject a quote versus actual mismatch and duplicate components |
| `universal_cost_refund_transaction` | Refund stored actual paid amounts once while the transaction remains refundable | Lines 1543 to the file end, owner must verify any native capped credit before acknowledging completion |
| `universal_cost_mark_component_refunded` | An unsupported owner adapter acknowledges only a component it already credited exactly | Lines 1488 to 1536, never a substitute for the physical credit |
| `universal_cost_settle_transaction` | Mark the accepted completed transaction nonrefundable and preserve its proof | Lines 1460 to 1482 |

Dynamic effects are inspected in the [pinned shared file](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_dynamic_effects.txt).
Universal interfaces are inspected in the [pinned implementation](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_universal_cost_effects.txt), its [API documentation](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_universal_cost_effects.md), the [system contract](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/systems/universal_cost_modifier.md), the [constant definitions](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/script_constants/chaosx_universal_cost_constants.txt), and the [affordability triggers](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_triggers/chaosx_universal_cost_triggers.txt).

### Universal quote input and output names

The quotation inputs are `universal_cost_quote_ordinary_cost`, `universal_cost_quote_family_mask`, and `universal_cost_quote_rounding_quantum`.
The outputs are `universal_cost_quote_final_cost`, `universal_cost_quote_displayed_cost`, `universal_cost_quote_saved_cost`, `universal_cost_quote_composed_ratio`, `universal_cost_quote_source_count`, `universal_cost_quote_primary_source_id`, and `universal_cost_quote_valid`.
The ratio basis is 10000.
For a positive ordinary price and eligible sources, the desired mathematical result is `ceil(ordinary × composed_ratio / 10000 / quantum) × quantum`.
A zero cost stays zero and a reward is not discounted as if it were a spend.
An owner supplies coherent quantization when no eligible source exists, without rounding a discounted component twice.

Affordability adds `universal_cost_quote_resource_kind` and returns `universal_cost_quote_affordable`.
Payment uses `universal_cost_payment_resource_kind` and `universal_cost_payment_amount`, with `universal_cost_payment_result` as its reported result.
That result is not a substitute for measured before and after inventory values where native effects can clamp or select different models.

The receipt fields are `universal_cost_transaction_id`, `universal_cost_transaction_component_id`, `universal_cost_transaction_resource_kind`, optional `universal_cost_transaction_resource_id`, `universal_cost_transaction_ordinary_cost`, `universal_cost_transaction_quoted_cost`, `universal_cost_transaction_actual_paid_cost`, optional `universal_cost_transaction_source_id`, and `universal_cost_transaction_primary_component`.
The API returns `universal_cost_record_transaction_result` and `universal_cost_recorded_component_index`.
Refund and settlement use the original transaction ID.
All temporary inputs and outputs are initialized explicitly at the correct scope because a similarly named temporary in another nested scope is not an isolated variable.

### Relevant price families and native resource kinds

| Resource | Family mask | Native kind | Event 112 handling |
|---|---:|---:|---|
| Political Power | 1 | 1 | Quote the actual ordinary political cost |
| Command Power | 2 | 2 | At most 60 CP per authored action, engine-owned raid allocation is separately classified |
| Manpower | 4 | 3 | Real pool payment and observed debit |
| Fuel | 8 | 4 | Native capacity, route, and measured amount |
| Infantry equipment | 16 | 5 | Exact compatible model required for a physical transfer |
| Support equipment | 32 | 6 or exact-model kind 11 | Do not claim an archetype query proves a model-specific debit |
| Motorized equipment | 64 | 7 | Pinned kind 7 names `motorized_equipment_1`, so old-model handling needs a different verified adapter |
| Train equipment | 128 | 8 or exact-model kind 12 | Exact donor and receiver model continuity |
| Convoys | 256 | 9 | Actual route capacity and exact native model |
| Army Experience | 32768 | 10 | Ordinary spend, not a new tradition currency |
| Stability | 67108864 | 15 | Native fraction and 0.01 quantum if a route explicitly spends it |
| War support | 134217728 | 16 | Native fraction and 0.01 quantum if a route explicitly spends it |
| Unsupported owner adapter | Declared matching family | 199 | Owner pays and refunds actual values, generic framework records proof |

The common equipment family mask is 112 for infantry, support, and motorized families together.
Navy Experience has family 16777216 and kind 13, and Air Experience has family 33554432 and kind 14.
These are inspected definitions, not a request to use every possible resource in this event.

## Source and contract mismatches requiring an integration disposition

| Checked body | Expected contract | Observed pinned algorithm | Disposition and required boundary scenarios |
|---|---|---|---|
| `universal_cost_source_matches_quote_family`, lines 287 to 358 | Membership by `mask mod (2 × bit) >= bit`, tested on both masks | Divides by each bit, applies modulo 2, then accepts any positive remainder | Algorithm differs from the documented modulo-span route. If fractional division survives, disjoint masks such as 1 and 2 can both appear positive at bit 2. This is a conditional arithmetic inference, not proven live behavior. Check disjoint, overlapping, zero, all, and high-bit masks |
| `universal_cost_round_up_to_quantum`, lines 364 to 414 | Exact upward quantum with current Euclidean-remainder rule and positive minimum | Rounds raw units, compares with the unrounded value, and adds one when below | Might agree under some native rounding semantics. Verify exact quantum, just below and above a quantum, tiny positive prices, negative rewards, and 0.01 fraction costs |
| `universal_cost_quote_integer`, lines 420 to 598 | One final price for display, availability, payment, AI, and refunds | Starts from ordinary cost and quantizes in the active-source path | Define the ordinary no-source quantum before integration without introducing a second ceiling when sources apply |
| `universal_cost_pay_component`, lines 698 to 997 | Actual debit equals quoted component and exact equipment model | Checks affordability, invokes a native effect, then reports success without a complete observed-debit receipt | Require owner measurement and fault receipt on partial payment, stock-model selection mismatch, or native clamp |
| `universal_cost_credit_component`, lines 1001 to 1127, and refund from 1543 | Only actual credited value becomes refunded | Reports successful native credit after the native effect without measuring resource-cap truncation | Test CP and XP near cap, changed caps, partial native credit, and a second refund call. Preserve uncredited remainder |
| Receipt lookup, lines 1135 to 1210, and refund iteration from 1543 | Correct lookup and settlement for all retained records | Payer arrays grow and while loops traverse records | Current owner notes a 1000-iteration engine guard. Check record 1000 and 1001 and define archive or bounded index strategy before exceeding it |
| `apply_exact_state_civilian_population_loss`, lines 628 to 716 | Upward floor, one physical debit, measured actual loss, Deaths does not debit population a second time, state ledger recorded | Rounds the floor, computes requested clamped loss before mutation, reports success, and uses `chaos_deaths_apply_state_pop = 1` in the logged route | This differs from the newer supplied owner contract. Do not install Event 112 civilian relocation against this older route. Check fractional floor, actual short debit, Deaths disabled, state and country reception symmetry, and no recruitable windfall |

No entry above establishes a live-game bug by source reading alone.
Do not silently edit the shared files as an Event 112 private implementation.
The parent must assign accepted neutral fixes or adapters to their owners, with before and after evidence.

The two current-owner referenced paths `common/scripted_triggers/chaosx_universal_cost_exact_triggers.md` and `common/scripted_triggers/chaosx_universal_cost_exact_triggers.txt` returned 404 at the pinned commit.
The fully read pinned dynamic effects file does not define `cbrn_debit_motorized_stockpile_oldest_first`, `chaosx_convert_days_to_date_offset`, or `chaosx_convert_date_offset_to_days`.
This establishes absence from that declared shared file, not an exhaustive claim about every unexamined repository or installed file.
Retrieve the accepted newer implementation or assign the dependency before an action relies on it.

## Native raid boundary

The repository's [native raid documentation copy](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/raids/_documentation.md) and [Event 016 precedent](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/raids/016_brilliant_scientist_portal_raids.txt) were both read in full.
The former documents both actor and victim outcome effects in RAID_INSTANCE scope, with explicit actor_country, victim_country, target_state, and target_province references.
Entering a country does not change ROOT into that country.
The newer owner requires an immediate hidden country receiver for a country-ROOT-only helper, regular saved references across that boundary, and disjoint exact-one pending slots.
No temporary value is assumed to survive an event boundary.

Native Command Power allocation and essential-equipment collection are engine-owned parts of raid preparation.
Do not pay an extra scripted copy of those same costs, claim universal discounts affect an unverified native field, or invent a cancellation refund.
The Event 016 precedent demonstrates bounded types, preparation, mission costs, target-specific effects, and both state and special-facility targets.
It does not prove that a cavalry Event 112 raid, arbitrary frontier origin, current DLC combination, or the proposed land route works in the installed game.
The exact success, critical-success, limited-success, and disaster interpretation also needs the current native scenario.

## CXT integration

The [CXT testing document](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/testing/chaosx_test_country.md) was read in full.
Daily registration is inert and bounded to the relevant tag or pending registration scope.
Initial application and manual player debug invocation are distinct from registration.
Event 112's package fixture records schema and component readiness only unless a user explicitly invokes a concrete test fixture.
It never fires the actual rise, transfers a live state, creates a host army, grants models, or reruns the founding every day.
Native combat-family templates do not become new Event 19 archetype registrations merely because their visuals differ.
Actual new entity, template fixture, or shared content owners require explicit disposition under the current integration contracts.

The destructive CXT console command was not invoked.
No registered-system application or debug-country mutation occurred during this planning task.

## Event 112 trade design review closed

The parent accepted and part 03 now defines actual-paid PP escrow for arms deliveries.
Supplier PP is credited only against observed equipment delivery, cumulative proportional compensation rounds down at the PP quantum, and full delivery pays the exact remainder.
Undelivered cancellation refunds unearned escrow only.
Completed trades need a separate actual equipment return and actual supplier PP debit before any reversal credit.
For 37 PP and 300 rifles with 100 delivered, supplier compensation is 12 PP and refundable undelivered escrow is 25 PP.
A native credit cap leaves earned but uncredited PP payable and does not convert it into an unearned buyer refund.
This closes the specification-level duplication concern.
Implementation and installed native payment tests remain pending.
