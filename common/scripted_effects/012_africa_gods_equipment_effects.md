# Gods armoured tribute helpers

These Event 012 owner helpers measure and transfer installed vanilla tank chassis.
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
