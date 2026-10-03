# Event 012 typed truck and artillery tribute — 2026-10-03

Disposition: implemented source design from `012_africa_gods_mobile_artillery_design_2026-10-03.md` within the active user's complete Gods-of-Africa goal and instruction to choose recommended bounded implementation options.
The acceptance basis is the full spec's compatible mobile/artillery family at `docs/specs/012_africa_is_one_gods_of_africa_specs/specs/012_gods_of_africa_full_spec.md:424–438` and the parent-accepted implementation advice.
No substitute for artillery, new family, player currency, extra clock, world scan, or additional player action was introduced.

## Implemented contract

Family 2 freezes either `motorized_equipment` or `artillery_equipment` using subtype constants 1 and 2.
There is no zero/default truck type.
The host separately measures native army target minus fielded equipment and subtracts available native stock; existing logistics and arsenal focus receipts can establish their matching stock objective.
The sender retains the greater of its subtype reserve floor and ten percent of its army requirement plus reinforcement shortfall.
Only positive compatible spare stock and positive corresponding host need can quote a shipment.
The whole-unit quote uses ten percent of spare stock; its ceiling is bounded by spare stock, host need, subtype shipment maximum, and the greater of one unit or one quarter of spare stock.
Existing scaling and the shared six-equipment-family floor remain authoritative, with a final typed ceiling.

Selection tries artillery before independently needed trucks.
The ordinary ladder adds the mobile lane after armour and before manpower.
The existing priority helper accepts family 2 when a valid quote exists, without creating another decision row.
Demand creation rechecks the live participant, matching selected family/amount/type, protected capacity, and host budget before assigning its immutable fields.

Full, partial, and substitute capacity use the same typed native measurement.
A debit additionally requires a positive whole-unit quantity no greater than remaining and a payment type matching the temporary or original frozen demand type.
Native `send_equipment` has two exclusive static archetype branches and sends to the explicit host.
Truck and artillery stock are never pooled, nor credited to the infantry-only common-defence ledger.

Slot freeze and submission copy only each slot's own optional type; current producers still offer their existing infantry/fuel/manpower/support alternatives.
An untyped family-2 callback fails closed, and opposite truck/artillery substitutions fail their compatibility check.
Host acceptance recomputes live offer capacity before installing temporary transaction fields.
Failed transfer restores original family, type presence, remaining balance, and ordinary payment work fields.
Rejection and return from negotiation restore ordinary payment fields, including the fixed type.
Archive, cleanup, cancellation, finalization, and family cleanup clear their optional live types and preparation quotes.

Response capture snapshots the subtype before demand cleanup and clears a prior optional receipt on each capture.
The response resolver reads receipt fields only.
Missing or invalid types use the localized unavailable leaf, and all eleven demand/payment/offer/receipt resolvers match their own type field.

## Review and balance scenarios

The helper handoff `012_africa_gods_mobile_helpers_2026-10-03.md` owns native arithmetic and API evidence.
The text handoff `012_africa_gods_mobile_text_2026-10-03.md` records 770 resolver cases and exact leaf wiring.
The independent integration audit belongs in `012_africa_gods_mobile_integration_audit_2026-10-03.md`.
That audit found missing mobile quantities in the shared need-scaling test and incomplete host/demand cleanup.
The owner added both need quantities to that existing scaler, cleared them and selected subtype on host loss, cleared needs on system closure, and called quotation cleanup on ordinary demand closure; the auditor's narrow follow-up records the final disposition.
Parent byte review also caught and corrected the artillery icon's initial question-mark character to the native U+00A3 marker.

Source checks cover zero stock, healthy host stock, artillery-only need with truck-only capacity, mixed compatible capacities, route-only need, fractional spare flooring, a one-unit residual, capacity lost after submission, malformed subtype, and receipt survival after cleanup.
The hand-calculated artillery case uses sender stock 275, target 100, fielded 50: reserve 60, spare 215; host target 200, fielded 100, stock 40: need 60; quote 21 and ceiling 53.
The truck case uses sender stock 1000, target/fielded 100: reserve 100, spare 900; host need 70: quote and ceiling 70.
An eleven-artillery quote pays five on a partial action and leaves six; a one-unit remaining amount cannot enter the strict smaller-partial gate.
These checks establish arithmetic and source wiring, not engine execution.
No AI weights changed; the separate named-scenario probability audit remains required before full Gods completion.

## Source and asset evidence

Changed systems: Gods constants, core effects/triggers, equipment effects/triggers and contracts, mobile contract helpers, report capture and contracts, scripted localisation and English leaves, and the Gods guide.
All reusable helpers use caller-set variables and boolean invocation.
The shared dynamic-effects owner index points at the equipment and report contracts; its other owners' edits are excluded from this commit.
No art was generated.
Truck display reuses its current native text icon, and artillery uses `GFX_artillery_texticon` from installed `interface/texticons.gfx:2131–2135`, texture `gfx/interface/equipmentdesigner/tanks/role_icons/role_icon_2.dds`.

Installed `documentation/dynamic_variables_documentation.md:557–564,687–691` defines stock and thousand-unit army quantities, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`.
Installed `documentation/effects_documentation.md:6550–6557` defines native transfers, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Installed `documentation/triggers_documentation.md:5166–5174` documents conditional trigger branches, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
Vanilla `common/scripted_effects/USA_scripted_effects.txt:402–418` and `events/AAT_Finland.txt:3722–3735` use the exact `equipment/amount/target` transfer structure and archetypes.
Their source revisions are respectively `9da33cb6e469906d7c8353b88d3957945f35ae12d81e1134d294b78b14f76f75` and `363c53751ed2fbe113fbed5635940f4494b5c67f3bfa0a3787aa327f6cdfda13`.
Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:1614–1619` documents the stock and army quantities, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.

## Remaining acceptance limits

The first narrow lifecycle `.606` inspect returned a confirmed 600-second timeout; a one-node retry and render were started.
Reference context and mission-removal search succeeded, but omitted source headers do not establish detailed coverage.
Native stock movement, live tooltips, error.log cleanliness, and full owner-loop behavior remain unconfirmed.
The broader accepted goal still has outstanding lifecycle settlement/restoration and weighted validation work.
This source tranche uses no simplification, but it is not full Event 012 completion.
