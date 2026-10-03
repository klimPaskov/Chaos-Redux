# Gods equipment tribute helpers

These Event 012 owner helpers measure and transfer installed vanilla tank chassis.
The mobile API below measures and transfers trucks or towed artillery as separate subtypes.
They do not add equipment definitions, grant technology, manufacture variants, or create a new country-wide clock.

## Capacity

`gods_of_africa_measure_armor_archetype = yes` is a COUNTRY-scope scripted trigger reading the caller-set temporary `gods_of_africa_armor_archetype` enum.
Native `meta_trigger` injects its validated `GetGodsOfAfricaArmorEquipmentToken` localisation token into the three installed equipment reads.
It reads stockpile, army equipment target, and fielded equipment through the installed dynamic variables.
The target and fielded values use their thousand-unit forms and are converted back to equipment units.
The protected reserve is the larger of the chassis floor and reinforcement shortfall plus a fraction of the army target.
Only whole units above that reserve count as spare.
It always returns true after measurement and adds to temporary `gods_of_africa_armor_stock`, `gods_of_africa_armor_deficit`, and `gods_of_africa_armor_spare` accumulators.
Initialize all outputs needed outside a helper in the caller before calling it, because temporary variables created only in nested helpers may not survive the return.
It modifies no normal variables, flags, stockpiles, or countries.

Set temporary `gods_of_africa_armor_required_amount` before calling `gods_of_africa_armor_capacity_is_sufficient = yes`.
The trigger initializes the three totals, measures light, medium, heavy, modern, super-heavy, and amphibious tank chassis, and compares spare units inclusively with that caller input.
There is no default amount.
Callers must supply an amount; transaction callers separately require it to be positive.
The final comparison supplies a meaningful capacity tooltip.
Both the base game and the tank designer use the installed chassis archetypes.
The bound is six chassis, independent of world country count.

## Quote

Set temporary `gods_of_africa_equipment_amount` before calling `gods_of_africa_floor_equipment_amount = yes`.
The helper rounds that temporary amount down by subtracting its remainder modulo one, and the caller copies the output to its normal amount field.
It has no default, pays nothing, and modifies only the temporary input/output and its remainder.
This uses the documented `modulo_temp_variable` operation instead of an unsupported floor effect token.

`gods_of_africa_quote_armored_tribute = yes` runs in participant COUNTRY scope.
It initializes both normal output variables to zero, then quotes only if the minimum shipment is transferable.
Its base amount combines a fraction of live spare stock with a fraction of actual cumulative `total_equipment_produced_armor`.
The production input is recorded production, not an inferred factory count or a forecast from current production lines.
The ceiling limits a quote to a fraction of spare stock and the configured maximum shipment, allowing the minimum shipment when the sender can spare exactly that minimum.
All quotes are whole equipment units.
Outputs are `gods_of_africa_armor_quote_amount` and `gods_of_africa_armor_quote_ceiling`; no payment occurs.
The parent demand calculation applies existing doctrine, Strength, Wrath, Chaos, capacity, conduct, and repetition adjustments and then respects the armour ceiling.
Demand preparation clears both quote outputs after creation or rejection, and demand cleanup clears them defensively.

## Transfer

`gods_of_africa_send_armored_tribute = yes` runs in the sender's COUNTRY scope after a current-contract, positive-payment, valid-host, and live-capacity preflight.
Required normal input is `gods_of_africa_payment_amount`; required receiver is `event_target:africa_host`.
No default receiver or payment is selected.
It initializes its temporary shipment balance and type outputs before invoking its six bounded slices.
Each `gods_of_africa_send_armored_archetype = yes` reads the caller-set temporary chassis enum, recomputes its protected spare amount, and sends only the smaller of that amount and the remaining payment.
Native `meta_effect` injects the validated bare equipment token into `send_equipment`.
`send_equipment = { equipment = chassis amount = shipment_slice target = event_target:africa_host }` performs the native debit and delivery.
The helper adds no replacement stockpile or technology grant.
Shipment order is light, medium, heavy, modern, super-heavy, then amphibious chassis.
All slices count toward one armoured resource payment, and each chassis retains its own reserve.
The helper leaves the temporary remaining balance at zero under the live preflight and the native effect's documented semantics.
Full compliance, partial compliance, and accepted substitutes retain their existing receipt and contract guards.
Odd armoured contracts round the partial shipment down to whole tanks, leaving the exact residual balance due.

Example in participant scope after the existing contract preflight:

```text
set_variable = { gods_of_africa_payment_family = constant:gods_of_africa_demand_family.armor }
set_variable = { gods_of_africa_payment_amount = gods_of_africa_demand_remaining }
gods_of_africa_transfer_payment = yes
```

## References and validation boundary

Installed `documentation/effects_documentation.md:6550-6557`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, defines native transfer.
Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:2254,2285-2293`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, describes removal from the sender and uses `equipment` in its example, despite the table labelling the argument `type`.
The direct vanilla precedent `events/AAT_Finland.txt:3722-3735` also uses `equipment`.
Installed dynamic-variable documentation `:557-565,687-691,870-871`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, covers stock, army targets, fielded stocks, and actual production.
Offline Data structures `:440-441` covers temporary trigger arithmetic and caller initialization.
Installed effects `:4986-5011` and offline Data structures `:572-575` define modulo and clamping, including the fractional remainder used to keep shipments integral.
The existing mod chassis-transfer surface is `common/scripted_effects/077_send_eq_effects.txt:50-80`.
The package handoff records MCP results and the source scenarios; it does not claim observed stock movement or DLC execution.

The tank text icon reuses `GFX_medium_tank_chassis_texticon` from vanilla `interface/texticons.gfx:2167-2172` through the `gods_of_africa_icon_armor` localisation leaf.
No new bitmap or sprite alias is required.
Future accepted work may add specific-role or quality demands with frozen compatibility receipts and matching capacity proof.
Such a proposal must preserve actual equipment transfer and cannot replace this family with motorized equipment.

## Mobile API and ownership

The family-2 API uses static `motorized_equipment` and `artillery_equipment` branches and caller-owned temporary inputs.
Every scripted helper is invoked with `= yes`.
Named argument blocks and dollar-delimited substitutions are unsupported for these helpers.
The three measurement/quote/transfer effects live in `common\scripted_effects\012_africa_gods_equipment_effects.txt` and the two mobile triggers live in `common\scripted_triggers\012_africa_gods_equipment_triggers.txt`.
The parent-owned binding and quote-cleanup effects live in `common\scripted_effects\012_africa_gods_mobile_contract_effects.txt` and are documented below.
The accepted bounded assignment supersedes parameter-shaped examples in `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_mobile_artillery_design_2026-10-03.md`.
No additional measurement, payment-binding, or cleanup helper is introduced in this lane.

| Helper | Scope and inputs | Outputs | Side effects and intended owner call sites |
| --- | --- | --- | --- |
| `gods_of_africa_mobile_type_is_valid` | COUNTRY with temporary `gods_of_africa_mobile_type` | Boolean accepting only trucks or artillery | No mutation, intended typed contract/payment/offer gates |
| `gods_of_africa_mobile_capacity_is_sufficient` | COUNTRY with temporary type and `gods_of_africa_mobile_required_amount` | Boolean and optional temporary matching stock, target, fielded, deficit, reserve, spare measurements | Temporary arithmetic only, invoked by quote and intended full/partial/substitute/live-transfer gates |
| `gods_of_africa_build_mobile_need_profile` | Authoritative host COUNTRY, native stock/army measures and its two existing route flags | Normal host `gods_of_africa_truck_need_amount` and `gods_of_africa_artillery_need_amount` | Overwrites both quantities and scratch temps, intended existing `gods_of_africa_build_need_profile` call site |
| `gods_of_africa_quote_mobile_tribute` | Participant COUNTRY, existing `africa_host` and refreshed host need quantities | Normal participant `gods_of_africa_mobile_quote_type`, `gods_of_africa_mobile_quote_amount`, `gods_of_africa_mobile_quote_ceiling`, failed quote has no type and zero amount/ceiling | Clears and overwrites quote outputs and scratch temps, intended existing demand family selector and authorized future typed offer producers |
| `gods_of_africa_send_mobile_tribute` | Participant COUNTRY, normal `gods_of_africa_payment_mobile_type`, `gods_of_africa_payment_amount`, explicit `africa_host` | Native equipment transfer only | One matching native debit/delivery branch, intended family-2 `gods_of_africa_transfer_payment` branch after parent preflight |

These owner call sites and their validation are parent-owned.
Installed internal calls are capacity to type validation, quote to capacity, and host need/quote to the existing integer floor helper.
The helper implementation handoff records source acceptance and its validation boundary.

## Mobile capacity and caller initialization

There is no inferred type or required amount.
Boolean-only callers initialize exactly the following two temporary inputs in their enclosing effect or trigger before invoking capacity:

```text
set_temp_variable = { gods_of_africa_mobile_type = gods_of_africa_payment_mobile_type }
set_temp_variable = { gods_of_africa_mobile_required_amount = gods_of_africa_payment_amount }
gods_of_africa_mobile_capacity_is_sufficient = yes
```

Use the immutable demand subtype and partial requirement for partial gates, and the submitted offer's own subtype and requirement for substitute gates.
The capacity trigger accepts a nonnegative integral requirement and rejects negative or fractional values.
A zero requirement explicitly permits measurement, including a valid zero-spare result.
Transaction callers still require a positive payment and validate field presence, frozen identity, amount no greater than remaining, host generation/existence, deadlines, war state, and duplicate settlement upstream.
Uninitialized input is a caller error and must not be used as an implicit measurement request.

For literal archetype stock `S`, army target `T` and fielded equipment `F`, convert the installed target/fielded `_k` measures to units and compute:

```text
deficit = max(0, T - F)
reserve = max(subtype_reserve_floor, operating_reserve_fraction * T + deficit)
spare = floor(max(0, S - reserve))
capacity = spare >= required_amount
```

The two subtype stocks never add together.
Each valid call overwrites its matching measurements rather than accumulating another subtype's spare.
Optional measurement outputs are temporary `gods_of_africa_mobile_stock`, `gods_of_africa_mobile_target`, `gods_of_africa_mobile_fielded`, `gods_of_africa_mobile_deficit`, `gods_of_africa_mobile_reserve`, and `gods_of_africa_mobile_spare`.
Any caller reading them after this nested trigger must initialize those outputs in its enclosing block first:

```text
set_temp_variable = { gods_of_africa_mobile_stock = constant:gods_of_africa_value.zero }
set_temp_variable = { gods_of_africa_mobile_target = constant:gods_of_africa_value.zero }
set_temp_variable = { gods_of_africa_mobile_fielded = constant:gods_of_africa_value.zero }
set_temp_variable = { gods_of_africa_mobile_deficit = constant:gods_of_africa_value.zero }
set_temp_variable = { gods_of_africa_mobile_reserve = constant:gods_of_africa_value.zero }
set_temp_variable = { gods_of_africa_mobile_spare = constant:gods_of_africa_value.zero }
set_temp_variable = { gods_of_africa_mobile_type = constant:gods_of_africa_mobile_type.trucks }
set_temp_variable = { gods_of_africa_mobile_required_amount = constant:gods_of_africa_value.zero }
gods_of_africa_mobile_capacity_is_sufficient = yes
```

Capacity initializes stock, target, fielded and reserve-floor temps in its outer trigger frame before either conditional measurement branch, so those branch writes remain visible to its later arithmetic.
Measurement outputs are usable only after a successful call.
Rejected type/amount input does not promise a complete refreshed measurement.
`gods_of_africa_mobile_required_remainder`, `gods_of_africa_mobile_reserve_floor`, and `gods_of_africa_mobile_fractional_spare` are private scratch temps.
Temporary variables have no country scope prefix.
The final inclusive comparison uses the matching `gods_of_africa_mobile_truck_capacity_tt` or `gods_of_africa_mobile_artillery_capacity_tt` custom trigger tooltip.
The parent owns those localisation keys and surrounding hidden requirement wrappers.

## Host mobile need

`gods_of_africa_build_mobile_need_profile = yes` executes directly in the authoritative host COUNTRY scope.
It independently reads literal truck and artillery stock, army target and fielded equipment.
For each subtype, desired stock starts at `max(0, target - fielded)`.
`gods_of_africa_focus_logistics_support_unlocked` raises only the truck desired stock to at least the truck route floor.
`gods_of_africa_focus_arsenal_support_unlocked` raises only the artillery desired stock to at least the artillery route floor.
Need is `floor(max(0, desired_stock - stock))`.
The route floor uses a maximum with reinforcement shortfall and is never added to that shortfall.
Both normal need outputs are overwritten on every invocation, including zero values.
There is no default route flag and no arbitrary floor when its matching route is locked.
The helper initializes `gods_of_africa_equipment_amount` before the nested integer helper.
It also overwrites mobile stock/target/fielded/desired-stock scratch temps and pays nothing.
It does not read or credit `africa_common_defence_stockpile`.

Example in a host preparation block:

```text
event_target:africa_host = {
	gods_of_africa_build_mobile_need_profile = yes
}
```

This API measures army reinforcement shortfall and an existing route stock objective.
Exact native supply-network truck shortage is not an input or a supported claim here.

## Mobile quote

`gods_of_africa_quote_mobile_tribute = yes` needs no subtype input.
It clears normal quote type and resets normal amount and ceiling to zero before testing the receiver or either subtype.
It requires an existing living `event_target:africa_host` and reads that target's corresponding refreshed integral need quantity explicitly.
It tries artillery first when artillery need is positive and the participant can spare the minimum shipment.
Only when that attempt fails does it try trucks against independently positive truck need and matching truck spare.
It produces one type and one quote, or leaves type absent and amount/ceiling zero.
Missing, dead, or unneeded host yields a zero quote without a subtype identity.
No implicit ROOT receiver, stock conversion, cumulative production term, or random tie-break is used.

For matching spare `P`, host need `N`, and absolute subtype shipment maximum `M`:

```text
ceiling = floor(min(P, N, M, max(minimum_shipment, maximum_spare_fraction * P)))
amount = floor(clamp(spare_quote_fraction * P, minimum_shipment, ceiling))
```

The accepted `minimum_shipment` is one.
Host need is generated as whole units by the need helper and must be refreshed before participant quoting.
The quote effect preinitializes all six measurement outputs before its nested capacity call so spare remains available for the shared amount calculation.
It also owns type/required-amount, host-need, maximum-shipment, and integer-amount scratch temps before use.
Those temps may overwrite earlier mobile scratch state in the same outer block.
Callers must bind contract/payment type again from normal frozen fields before later capacity checks.
Normal quote outputs survive the helper return and belong to the participant even when the outer ROOT belongs to the host.
The parent applies existing demand scaling, clamps and floors the scaled amount to this ceiling, freezes the selected subtype, and clears preparation outputs on every exit.

Example inside participant scope after host need refresh:

```text
gods_of_africa_quote_mobile_tribute = yes
# Read participant normal quote_type, quote_amount and quote_ceiling here.
```

## Mobile transfer and cleanup

`gods_of_africa_send_mobile_tribute = yes` reads the participant's normal payment type and amount.
The truck branch sends `motorized_equipment` and the exclusive artillery branch sends `artillery_equipment` to explicit `event_target:africa_host`.
Missing or invalid subtype invokes neither branch.
No defaults are selected and no stock is synthesized.
The parent must establish a positive integral payment, matching frozen subtype, live capacity, valid receiver/contract identity, and remaining balance before invoking it.
This helper does not repeat preflight or write success flags, counters, histories, remaining balance, receipts, or an infantry-only host stockpile ledger.
The native effect has no documented transfer receipt returned to this helper.
Success accounting therefore remains part of the parent's guarded synchronous transaction rather than a claim of observed receipt here.

Example after the parent's full or partial preflight in participant scope:

```text
gods_of_africa_send_mobile_tribute = yes
```

No event target is created, rebound or cleared by these helpers.
The Charter layer continues to own `africa_host` and its generation/loss cleanup.
The parent clears both host need outputs on unifier loss/system cleanup and clears participant quote outputs after preparation and ordinary demand cleanup.
Frozen demand/payment/offer/slot/rollback subtype lifecycle and the response-receipt subtype belong to parent integration.
Keep latest-response subtype receipts out of ordinary demand cleanup and clear them with the existing report-receipt reset.
Temporary scratch outputs naturally end with their enclosing chain and need no persistent cleanup helper.

## Parent-owned mobile contract helpers

`gods_of_africa_bind_payment_mobile_type = yes` runs in participant COUNTRY scope after the caller binds normal `gods_of_africa_payment_family`.
Its normal inputs are `gods_of_africa_payment_family`, `gods_of_africa_demand_family`, and the optional frozen `gods_of_africa_demand_mobile_type` on that same country.
It first clears normal `gods_of_africa_payment_mobile_type`.
It copies the frozen demand subtype into that normal output only when both families equal `constant:gods_of_africa_demand_family.mobile_artillery` and the demand subtype field exists.
Otherwise the payment subtype remains absent.
There is no default subtype, quote-based inference, temporary input or receiver selection.
The output remains country-owned normal transaction work until the next binding or owner cleanup.
Presence permits copying, while the separate typed validator and parent transaction preflight reject unsupported numeric subtypes.
The helper leaves payment family, amount, capacity requirement, remaining balance and demand identity unchanged.
It charges nothing and writes no success, history, receipt, counter, flag or event target.
The parent uses it when binding full or partial payments and when restoring payment work after negotiation, rollback or residual-balance changes.

Example in participant scope before the parent's capacity and transaction checks:

```text
set_variable = { gods_of_africa_payment_family = gods_of_africa_demand_family }
gods_of_africa_bind_payment_mobile_type = yes
```

The caller binds the payment amount and requirement separately and then initializes the capacity trigger's two temporary inputs from that normal work record.

`gods_of_africa_clear_mobile_quote = yes` runs in COUNTRY scope on the country whose preparation quote is being discarded.
It takes no inputs and clears exactly normal `gods_of_africa_mobile_quote_type`, `gods_of_africa_mobile_quote_amount`, and `gods_of_africa_mobile_quote_ceiling`.
All three outputs become absent, including when they previously held zero.
There is no default, refund, debit, authority change, contract cancellation or response-receipt mutation.
It leaves host needs, frozen demand/payment/substitute identity, remaining balances, success accounting, flags, event targets and temporary scratch variables unchanged.
The parent uses it after preparation succeeds or fails and at the existing demand/participant cleanup boundaries.
Repeated invocation safely leaves the same three fields absent.

Example at a participant preparation exit:

```text
gods_of_africa_clear_mobile_quote = yes
```

Both helpers are parent-owned source and lifecycle wiring.
This documentation update adds no UI action or AI weight.

## Accepted arithmetic sanity results

These are the previously computed Decimal source-model results using the accepted tuning constants.
They are not observed engine delivery, campaign balance or live temporary-lifetime evidence.
The sender and host triplets below are native stock, army target and fielded equipment expressed in units.

| Case | Sender | Host | Result |
| --- | --- | --- | --- |
| Artillery | 275 / 100 / 50 | 40 / 200 / 100 | Sender deficit 50, reserve 60, spare 215, host need 60, quote 21, ceiling 53 |
| Trucks | 1000 / 100 / 100 | 30 / 200 / 100 | Sender deficit 0, reserve 100, spare 900, host need 70, quote 70, ceiling 70 |
| Odd artillery contract | 135 / 0 / 0 | 0 / 40 / 0 | Sender reserve 25, spare 110, host need 40, quote 11, ceiling 27 |

For the odd 11-unit contract, the accepted shared half-payment floor yields 5 paid and exactly 6 remaining.
That partial split belongs to the parent contract resolver and does not add accounting to the native sender.

## Mobile constants and reference boundary

The parent adds these categories in `common\script_constants\012_africa_gods_constants.txt`.
The helper lane only consumes them and adds no tuning definition.

| Category | Keys and accepted values |
| --- | --- |
| `gods_of_africa_mobile_type` | `trucks = 1`, `artillery = 2` |
| `gods_of_africa_mobile` | `units_per_thousand = 1000`, `operating_reserve_fraction = 0.10`, `truck_reserve_floor = 100`, `artillery_reserve_floor = 25`, `truck_route_stock_floor = 100`, `artillery_route_stock_floor = 25`, `minimum_shipment = 1`, `spare_quote_fraction = 0.10`, `maximum_spare_fraction = 0.25`, `maximum_truck_shipment = 500`, `maximum_artillery_shipment = 300` |
| Existing `gods_of_africa_value` | `zero` and `one` for nonnegative bounds and modulo granularity |

Mobile measurements use installed `documentation\dynamic_variables_documentation.md:557-565,687-691`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`.
Installed `documentation\triggers_documentation.md:2110-2134,2145-2152,5166-5174,6442-6452,7482-7500`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, covers inclusive comparisons, trigger arithmetic, conditional triggers and modulo.
Offline `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md:339-345,386-403`, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, supplies short-circuit AND/OR and exclusive conditional-branch structure.
Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:435-442,449,557-574`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, covers caller-owned unscoped temp lifetime, explicit target-variable reads and arithmetic.
The installed constants references are `documentation\script_concept_documentation.md:216-243`, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, and `common\script_constants\documentation.md:1-32`, revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
Native transfer uses the installed send reference and offline Effects example cited above, with direct vanilla artillery precedent `events\AAT_Finland.txt:3722-3735`, revision `363c53751ed2fbe113fbed5635940f4494b5c67f3bfa0a3787aa327f6cdfda13`.
Exact native variant aggregation and selection order, stock movement, temporary-variable survival in the installed engine, and campaign balance remain unobserved.
The handoff records MCP blockers separately from the local source/arithmetic acceptance checks.

No asset is created in this helper lane.
Parent presentation reuses existing motorized and vanilla `GFX_artillery_texticon` wiring.
Any future exact-model, quality, or weighted acceptance policy needs separate accepted design and evidence.
