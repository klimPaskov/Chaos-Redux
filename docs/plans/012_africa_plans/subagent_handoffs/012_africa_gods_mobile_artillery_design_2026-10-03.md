# Event 012 family-2 trucks and artillery implementation advice — 2026-10-03

## Decision, acceptance, and ownership

Disposition: **implemented in source within the delegated implementation-choice scope**, with native acceptance still unconfirmed.
Acceptance basis: this assignment identifies the accepted `mobile_artillery` family, proposes freezing truck OR artillery subtype, and explicitly authorizes recommended implementation choices within the accepted goal without a new approval round.
The accepted source design is `docs\specs\012_africa_is_one_gods_of_africa_specs\specs\012_gods_of_africa_full_spec.md:424-438`, especially transferable compatible equipment, protected army/reinforcement reserves, and current host deficit or route reason.
The recommendation below completes that existing family rather than introducing another family, currency, player counter, world iteration, clock, or DLC requirement.
The parent implementation is recorded in `012_africa_gods_mobile_tribute_2026-10-03.md`, with separate helper, text, and integration audit handoffs.
The parameter-shaped examples below are historical design advice; current scripted helpers use caller-set variables and `= yes`, as documented in the implemented helper contract.
Numeric anchors below are authorized recommended implementation choices, not a claim of completed balance or engine validation.
Only this handoff was written; source, localisation, parent docs, Git, and the previous armour audit were not edited.
Skills applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`; none created or updated.

**Implement one family-2 contract with one immutable subtype: trucks (`motorized_equipment`) OR towed artillery (`artillery_equipment`).**
Select that subtype only from a current corresponding African need and compatible sender spare stock.
Never aggregate trucks with artillery, never switch subtype at payment, and never fulfil an artillery requirement with trucks.
Accept all installed versions within the selected archetype through native transfer; freeze the archetype/subtype rather than inventing an exact technology-level requirement.
Do not describe this as self-propelled artillery or a combined trucks-plus-guns bundle.

The spec permits obsolete/current compatibility rules and possible high-Wrath rejection (`:437-438`); it does not specify an obligatory probability table or exact quality threshold in the assigned passage.
This advice proposes no weighted quality rule, random selection, or AI weight change, and does not claim those optional policies have been implemented.
Any later weighted compatibility/quality or AI adjustment requires `hoi4.probability_inspect`, a read-only `chaosx_ai_probability_auditor` baseline, owner patch, and matching named-scenario comparison before acceptance.

## Initial implementation evidence

- `common\script_constants\012_africa_gods_constants.txt:135-138` preserves `mobile_artillery = 2`; `:301` defines the flat `mobile_amount = 100`.
- Main effects `gods_of_africa_build_need_profile` (`:833`) has no truck/artillery need measurement, and `gods_of_africa_select_demand_family` (`:971`) has neither a family-2 priority gate nor a normal family-2 candidate branch.
- `gods_of_africa_set_priority` (`:2486-2500`) also omits family 2 from its accepted requests.
- `gods_of_africa_calculate_demand_amount:1163` uses the flat mobile amount; the candidate quote has no subtype field.
- Main triggers `:304-307`, `:423-426`, and `:951-954` check trucks for family-2 full, substitute, and partial affordability respectively.
- Main effects `:1741-1746` remove motorized stock through a helper and add replacement motorized stock to Africa; no actual artillery branch exists.
- `gods_of_africa_build_substitute_set:1428-1473` offers only infantry, fuel, manpower, or support equipment, never family 2.
- `gods_of_africa_grant_leniency:2544-2574` changes offender state, Wrath, and history; it does not reduce or retype the frozen demand.
- Current display resolvers name the generic mobile/artillery family and always use the truck icon for family 2.

The armour context is the published commit `46ea619977e21c1e210ea6ebd487a534ec45af23`.
Its helper source hashes match the audited package, and its modulo floor helper is reusable without changing armour behavior.
All line references here identify the inspected shared-workspace snapshot; the parent is concurrently changing visible localisation, so follow the named functions if lines move.

## Receipt-tranche update and snapshot boundary

This section incorporates the parent's subsequent receipt and shared-rounding tranche; it supersedes the earlier suggestion to add a new itemized response receipt or extend an armour-only partial gate.
The updated source was read directly, and only this design handoff was edited.
Parent source continues to move, so the following are inspected snapshots rather than a frozen final commit or a whole-tranche completion audit:

| Parent file re-read for this update | Inspected content and lines | SHA-256 |
| --- | --- | --- |
| `common\scripted_effects\012_africa_gods_report_effects.txt` | `gods_of_africa_capture_response_report:5-13`; `gods_of_africa_clear_report_receipts:15-24` | `0f3a23e4ae4e9fd8f2ef5dabcb6d02c0eea158695054eb21a52f30347a87dcb5` |
| `common\scripted_effects\012_africa_gods_report_effects.md` | Receipt lifetime/capture contract `:7-29`; shared classifier `:44-49` | `398c6292055043c4db2dc19f45de2840b30b7b056481bf396e3c27b1aae416bd` |
| `common\scripted_effects\012_africa_gods_effects.txt` | Full quote floor `:1278-1288`; partial floor `:1652-1660`; success captures `:1871-1884`; partial capture `:1915-1919`; refusal/expiry captures `:2640-2644,2691-2695` | `ed5855eafccb6655a54b8acecb56049a6182ec1ed1e824a75d6c62599c1b97a5` |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | `gods_of_africa_family_is_equipment:268-277` already includes family 2 and five other equipment families | `b70b438cf6ad01e34690ad67f97ad3630940bee650d5962a1f84244796e747ed` |
| `common\scripted_localisation\012_africa_gods_scripted_localisation.txt` | Existing `GetGodsOfAfricaResponseFamilyName:96-113`, currently with generic family-2 leaf | `a4e7172cb1b0cc87c62dbb3f2ef3d9c234f5c416a9de3853bdaebc8f2cc8d4b7` |

The shared classifier takes `FAMILY` as the literal variable name and covers infantry, mobile/artillery, armour, aircraft, transport, and support equipment.
Its full/partial quote call sites already normalize family 2; retain that shared coverage rather than add a parallel armour-or-mobile classifier or duplicate its six-family list.
The parent example is now the arithmetic regression contract: 55 aircraft produces a 27-unit partial and 28-unit residual.
Family-2 amount/ceiling quoting still requires its own subtype-specific bounds and flooring after a cap/fallback changes the value.
The earlier source line references and hashes below remain historical evidence for the initial design; this update's function names and snapshot table govern receipt/rounding integration.
For this follow-up, bounded live source lookup of `gods_of_africa_capture_response_report` and event trace of `chaosx.nr12.604` were attempted, but neither returned evidence before the orchestration cell was terminated at the update boundary.
Unlike the earlier confirmed 600-second failures, these follow-up requests establish only a no-result bounded cancellation, not a new server timeout or health diagnosis.
The receipt/rounding advice is based on the exact local source snapshots above and the previously cited arithmetic/lifetime references; mandatory engine/MCP coverage remains unresolved.

## Exact state contract

Add integer constants category `gods_of_africa_mobile_type` with `trucks = 1` and `artillery = 2`.
Do not assign either meaning to zero and do not default a missing type to trucks.
These normal country variables carry multi-valued identity rather than Boolean state:

| Owner/lifetime | Exact identifiers | Contract |
| --- | --- | --- |
| Host, refreshed need quantities | `gods_of_africa_truck_need_amount`, `gods_of_africa_artillery_need_amount` | Actual nonnegative missing-unit amounts; zero means healthy; no separate numeric 0/1 needs |
| Participant, preparation only | `gods_of_africa_mobile_quote_type`, `gods_of_africa_mobile_quote_amount`, `gods_of_africa_mobile_quote_ceiling` | Quote outputs, cleared before attempting a quote and after preparation succeeds or fails |
| Host, preparation only | `gods_of_africa_selected_mobile_type` | Copied from the successful participant quote; cleared at selector/preparation entry, failure, and after creation |
| Participant, active contract | `gods_of_africa_demand_mobile_type` | Present and valid exactly when demand family is 2; immutable until contract closes or an accepted substitute temporarily swaps the transaction identity |
| Participant, transaction work | `gods_of_africa_payment_mobile_type` | Bound to the exact payment family and amount; cleared when work family is not 2 and after successful transfer |
| Participant, submitted substitute | `gods_of_africa_substitute_mobile_type` | Required for family-2 offer; absent for other families |
| Participant, frozen offer slots | `gods_of_africa_substitute_slot_1_mobile_type`, `gods_of_africa_substitute_slot_2_mobile_type`, `gods_of_africa_substitute_slot_3_mobile_type` | Type belongs to each slot's own family and amount, never inherited from the original demand |
| Participant, acceptance rollback | `gods_of_africa_substitute_original_mobile_type` | Backup alongside existing original-family/original-remaining fields; preserve absence for an original non-family-2 contract |
| Participant, latest response receipt | `gods_of_africa_last_response_mobile_type` | Frozen with `last_response_family` before demand cleanup; present only for a typed family-2 response; survives ordinary demand cleanup and is cleared with existing report receipts |

Reuse existing demand ID, generation, deadline, status, remaining balance, success variable, cooldown, and kind/day history receipts.
No additional demand sequence, payment counter, timer, array, global pointer, or player currency is needed.
The authoritative receiver remains `event_target:africa_host`; entering nested countries does not make ROOT the intended recipient.

## Measurement, need, and tuning

Append feature-local helpers to the existing `012_africa_gods_equipment_triggers.txt` and `012_africa_gods_equipment_effects.txt`, with matching contracts/examples in `012_africa_gods_equipment_effects.md`.
Do not replace or broaden the six-chassis armour helper.

For a selected literal archetype `E`, read stock `S = num_equipment@E`, army target `T = 1000 * num_target_equipment_in_armies_k@E`, and fielded amount `F = 1000 * num_equipment_in_armies_k@E`.
Compute `D = max(0, T - F)`, sender reserve `R = max(subtype_reserve_floor, 0.10 * T + D)`, and sender spare `P = floor(max(0, S - R))`.
Use modulo-one subtraction for temporary integer outputs and reuse `gods_of_africa_floor_equipment_amount` for normal amounts.
No unsupported floor token and no fractional equipment payment are needed.

For host need, measure the same literal archetype in the authoritative host scope.
The default desired host stock is its reinforcement shortfall `D_host`; need is `floor(max(0, D_host - S_host))`.
Only when the existing logistics-support route flag is set may truck desired stock be raised to the route truck stock floor; only when the existing arsenal-support route flag is set may artillery desired stock be raised to the route artillery stock floor.
Specifically use `max(D_host, route_floor)` in that route case, not `D_host + route_floor`, then subtract current native stock.
The exact existing flags are `gods_of_africa_focus_logistics_support_unlocked` and `gods_of_africa_focus_arsenal_support_unlocked`.
This is the spec's explicit route-reason path, not a fabricated claim that a native supply-network truck deficit was measured.
Without shortfall or an unlocked route reason, a zero-stock host with no army requirement does not generate an arbitrary demand.
Do not use the infantry-only `africa_common_defence_stockpile` ledger as artillery/truck stock or increment it after these shipments.

Add fixed-point constants category `gods_of_africa_mobile` in the existing constants file:

| Key | Recommended value | Purpose |
| --- | --- | --- |
| `units_per_thousand` | 1000 | Installed `_k` unit conversion |
| `operating_reserve_fraction` | 0.10 | Sender army reserve above reinforcement shortfall |
| `truck_reserve_floor` | 100 | Protected trucks |
| `artillery_reserve_floor` | 25 | Protected artillery |
| `truck_route_stock_floor` | 100 | Existing logistics route's host stock objective |
| `artillery_route_stock_floor` | 25 | Existing arsenal route's host stock objective |
| `minimum_shipment` | 1 | Whole-unit granularity; small genuine residual need can be fulfilled |
| `spare_quote_fraction` | 0.10 | Base stock quote |
| `maximum_spare_fraction` | 0.25 | Quote safety ceiling |
| `maximum_truck_shipment` | 500 | Absolute truck ceiling |
| `maximum_artillery_shipment` | 300 | Absolute artillery ceiling |

For the chosen subtype, let `N` be the current integer host need and `M` its absolute shipment ceiling.
Only quote when `P > 0` and `N > 0`.
Set `C = floor(min(P, N, M, max(1, 0.25 * P)))`, then `Q = floor(clamp(0.10 * P, 1, C))`.
Thus production without stock cannot create capacity, healthy hosts cannot create a quote, and a one-unit real shortage can be met without rounding it up to five or ten.
Take existing demand scaling from `Q` and clamp/floor the scaled amount to `1..C`, including after any existing scaled-to-base fallback.
The existing global amount limits still apply, but the subtype ceiling is authoritative for this equipment lane.
Do not use `gods_of_africa_transaction.mobile_amount` as the family-2 base after this migration.
Leave that constant if another verified consumer still needs it; otherwise remove its unused definition in the owner's change.

**No cumulative production term is recommended for this lane.**
Installed production counters are equipment `type` categories, not counters for the exact requested archetype.
Installed artillery definitions also include rocket artillery and other separate archetypes, so adding `total_equipment_produced_artillery` would admit production outside the towed-artillery payment token.
Likewise, do not add motorized and artillery production totals together or reuse the armour production term.
The assigned land-equipment passage requires compatible transferable stock and protected reserves, not a cumulative production contribution; the explicit production/stock scaling requirement at `:446` applies to armour and remains implemented there.
Future exact-archetype production tracking is a separate proposal requiring actual source/engine evidence and no broad-category double counting.

## Proposed helper map

| Identifier | Scope/inputs/defaults | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `gods_of_africa_mobile_type_is_valid` | COUNTRY; required `TYPE` variable/token value | True only for the two declared IDs; no economic effect | Quote, family validators, demand/full/partial/substitute preflight |
| `gods_of_africa_measure_mobile_equipment` | COUNTRY; literal `EQUIPMENT` and required `RESERVE_FLOOR` | Temporary `gods_of_africa_mobile_stock`, `_target`, `_fielded`, `_deficit`, `_reserve`, `_spare`; true after measurement | Host need, typed capacity, typed quote |
| `gods_of_africa_mobile_capacity_is_sufficient` | Participant COUNTRY; required `TYPE`, `AMOUNT`; no type default | Static type branch measures only its matching archetype; inclusive spare check; typed custom tooltip | Full, partial, substitute and transfer gates |
| `gods_of_africa_build_mobile_need_profile` | Authoritative host COUNTRY | Resets and writes the two normal need quantities from native stock/shortfall and existing route flags | Existing `gods_of_africa_build_need_profile` |
| `gods_of_africa_quote_mobile_tribute` | Participant COUNTRY; required `TYPE`; valid host | Initializes normal quote outputs, measures spare, uses corresponding host need, writes Q/C/type or leaves quote invalid; no payment | Selector's two subtype attempts |
| `gods_of_africa_bind_demand_payment` | Participant COUNTRY; required `AMOUNT` expression/variable | Sets payment family/amount from current demand, clears stale payment type, copies demand type for family 2, rebuilds capacity requirement | Full and partial resolvers, remaining-balance restoration, rejection, rollback, return from negotiation |
| `gods_of_africa_send_mobile_tribute` | Sender COUNTRY; valid typed payment/current contract | Exactly one static native transfer to `africa_host`; no removal helper or replacement stock grant | Family-2 branch of existing transfer function |
| `gods_of_africa_clear_mobile_contract_fields` | Participant COUNTRY | Clears demand type, payment type, mobile quote outputs and rollback type; no counters or receiver changes | Existing demand/participant cleanup entry points |
| Existing `gods_of_africa_capture_response_report` — extend, do not duplicate | Participant COUNTRY; existing required `KIND`, `AMOUNT`, `BALANCE`, current demand family/type | Existing four fields plus frozen `gods_of_africa_last_response_mobile_type`; no payment, counter, timer, or new callback | Existing successful full/partial/substitute, refusal, and expiry captures |
| Existing `gods_of_africa_family_is_equipment` — reuse unchanged | COUNTRY; required literal variable-name `FAMILY` | Six-family classification; family 2 already included | Shared full and partial normalization; do not add another family list |

For parameter implementation, materialize `TYPE` into a caller-owned temporary before comparing it if the caller may pass a `constant:` value rather than a literal variable name.
Do not use `has_variable = constant:...` to validate a numeric enum value.
Validate field presence separately at the demand/offer wrappers, then validate its numeric value through the typed helper.
Preinitialize every temporary measurement output used after a nested scripted trigger in the enclosing quote/need effect before the helper call, exactly as in the armour package.
All temp outputs remain unscoped; normal type/quote variables belong to the participant or host indicated above.
The measurement helper should overwrite its outputs rather than add unrelated archetypes to an aggregate.
The typed capacity helper must not borrow or overwrite armour output names.

## Owner implementation sequence and exact call sites

1. **Make need and selection reachable.**
Call the new host need helper from `gods_of_africa_build_need_profile` and include either positive need quantity in the existing preparation and demand-scale need OR blocks.
Add family 2 to the existing priority validity/selection path when either typed host need is positive and that same subtype passes participant capacity for at least one unit.
Use that matching need-plus-capacity eligibility in the normal candidate gate too; host need alone must not select an unquotable lane ahead of other legitimate families.
If an already authorized callback sends priority request 2, allow it in `gods_of_africa_set_priority`; no new player priority decision is necessary for normal reachability.
Add the normal family-2 candidate branch immediately after fuel and armour, before manpower, without changing other families' internal rewards or weights.
For a family-2 attempt, try artillery first when its host need is positive and the participant can quote it; if that fails, try trucks only when truck host need is independently positive.
When both succeed, keep artillery as the deterministic tie-breaker and produce one quote, not two contracts.
An artillery-only host need with a truck-only sender must fail that lane rather than relabel trucks as artillery; the existing dispatcher may continue its legitimate other-family behavior.
Copy successful quote type to the host selected type and participant payment work type before `gods_of_africa_build_capacity_profile` runs.
Copy the selected type into `gods_of_africa_demand_mobile_type` during `gods_of_africa_create_demand_contract`; clear that field when creating any other family.
Guard final creation with existing live participant eligibility/current host checks and typed live capacity, then clear scratch quote/selected type outputs on both success and failure.

2. **Use one exact typed capacity rule everywhere.**
In `gods_of_africa_compute_capacity_requirement`, family 2 joins armour's amount-only special case; remove it from the generic extra-500 equipment-floor path.
Its full trigger passes `payment_mobile_type` and current payment requirement; its partial trigger passes immutable `demand_mobile_type` and partial requirement; its substitute trigger passes the offer's own type and substitute requirement.
Family-2 branches of `gods_of_africa_demand_family_is_valid` and `gods_of_africa_payment_family_is_valid` must additionally validate their corresponding type when those validators are used on an actual contract/payment record.
The generic enum alone must not classify an untyped truck/artillery payment as valid.
At actual transfer, require a valid type equal to the active demand's frozen type, a positive integral payment no greater than remaining, and existing ID/generation/host/deadline/war guards.
An accepted substitute temporarily installs its own family/type into the resolver's demand work record before this same equality check, so it still uses the sole debit path.
Capacity checks must recalculate matching native stock and reserves at click/submission/acceptance time; stored quotes are not permission to bypass lost stock.

3. **Send real equipment once.**
Replace only the family-2 branch in `gods_of_africa_transfer_payment` with the new sender helper.
For truck type use `send_equipment = { equipment = motorized_equipment amount = gods_of_africa_payment_amount target = event_target:africa_host }`.
For artillery type use the identical native structure with `equipment = artillery_equipment`.
These are two exclusive static branches; no meta effect or dynamic equipment-type token is required.
Remove the old family-2 `remove_motorized_equipment_from_stockpile` and `add_equipment_to_stockpile` credit from that branch.
Keep success/history/remaining accounting in the existing transaction and resolvers; do not add a second success or counter write in the native sender helper.
Clear payment type alongside the existing success-path payment-family/amount/credit cleanup.

4. **Preserve exact integer partial and leniency semantics.**
Keep the parent's shared `gods_of_africa_family_is_equipment = { FAMILY = gods_of_africa_demand_family }` gate and floor operation in `gods_of_africa_create_demand_contract` before partial capacity is computed; family 2 is already covered.
Keep its shared full-quote gate using `FAMILY = gods_of_africa_selected_family`, and still normalize family-2 amounts after its typed ceiling or existing base fallback is applied.
Reuse the existing half ratio, modulo floor helper, minimum-one work amount and strict `partial_amount < remaining` gate.
A one-unit demand has no legal partial payment; an 11-unit demand has a frozen five-unit partial and six-unit residual.
`gods_of_africa_resolve_partial_compliance` binds payment type from demand before transfer, subtracts exactly the same integral paid amount once, and restores payment work fields from the residual demand afterward.
`gods_of_africa_grant_leniency` keeps the frozen type, amount, remaining balance, and partial amount unchanged because the inspected existing mechanic only alters conduct/Wrath.
Do not re-run subtype selection when Wrath changes, an extension is granted, or the sender's inventory mix changes.

5. **Carry type through every substitute and restoration boundary.**
No existing frozen slot chooses family 2, so do not invent a new slot family or silently turn one current slot into a truck offer.
Nevertheless extend `gods_of_africa_freeze_substitute_offers`, all three `gods_of_africa_substitute_demand_slot_*` wrappers, and `gods_of_africa_submit_substitute` to carry each slot's own optional type with its family/amount.
Clear canonical type before copying a slot so selecting a non-family-2 offer cannot inherit the previous family-2 type.
A future callback supplying family 2 without a valid type must fail closed before submission; never infer its type from sender stock or original demand.
Any future producer of a family-2 substitute slot must call the typed quote helper against the refreshed corresponding host need and freeze its result, rather than insert the old flat mobile amount.
When the original demand and offered substitute both have family 2, require their types to match; reject a truck-type offer against an artillery-type contract instead of treating the umbrella family as compatibility.
This narrow rule does not remove the existing explicitly negotiated fuel, manpower, infantry, or support-equipment alternatives allowed by the spec.
`gods_of_africa_resolve_substitute` backs up original type/presence, temporarily copies offer type with substituted family, and restores original type plus ordinary payment work fields if live transfer fails.
When switching to a non-family-2 substitute, clear the demand/payment mobile types during that temporary work state; restore their original presence on rollback.
Rejecting an offer or returning from negotiation restores original demand-bound payment type; returning from negotiation must also restore family/amount/requirement rather than leaving the submitted offer's work fields behind.
The ordinary comply decision is hidden during negotiation (`decisions:124-129`), but its resumed price and icon still must describe the original frozen demand.
Clear slot types in `gods_of_africa_clear_substitute_slots` and canonical/rollback type in its existing submit/reject/cleanup lifecycle.

6. **Cleanup without changing receipts or host ownership.**
Call the narrow mobile cleanup helper from `gods_of_africa_clear_demand`, `gods_of_africa_archive_invalid_participant`, `gods_of_africa_clean_participant`, `gods_of_africa_finalize_participant`, and `gods_of_africa_cancel_participant` wherever they clear demand-family/payment fields directly.
Reset its fields when `gods_of_africa_register_participant` establishes a new participant generation.
Existing war cancellation, refusal, timeout, defiance, full settlement, and accepted substitute flows already reach those cleanup entry points; retain their once-only active-demand/count guards.
Do not clear subtype during successful partial payment or ordinary leniency.
Clear host need quantities and selected type in `gods_of_africa_cancel_on_unifier_loss` and `gods_of_africa_clean_system`; normal preparation refreshes them without a new recurring hook.
No global event target is added; `africa_host` remains owned by the existing Charter layer.
No extra type-history array or payment counter is required, but the parent's latest-response receipt now requires a frozen subtype field.
Extend `gods_of_africa_capture_response_report` in `012_africa_gods_report_effects.txt` to snapshot `gods_of_africa_demand_mobile_type` into `gods_of_africa_last_response_mobile_type` beside its existing family/amount/balance writes, while the demand family still exists.
At each actual capture, clear the receipt subtype before conditionally copying a valid family-2 demand subtype; a subsequent infantry, fuel, or other response must not retain an earlier truck/artillery identity.
Do this inside the helper's existing `has_variable = gods_of_africa_demand_family` guard so a no-family no-op leaves the entire previous receipt intact rather than clearing only its subtype.
Read the demand subtype, not the payment-work subtype: the transfer success path has already cleared payment work fields before the full/partial resolver captures its report.
Full and accepted-substitute captures retain the family/type actually resolved with zero balance; partial captures happen after exact balance reduction; refusal and expiry snapshot the demanded type with zero paid amount and the unpaid balance.
The substitute resolver must install its frozen offer type together with the temporary substituted demand family before calling full compliance, so that a successful receipt records the accepted resource rather than the original resource.
Failed acceptance restores original family/type and must not write a new successful response receipt.
Keep `gods_of_africa_last_response_mobile_type` out of `gods_of_africa_clear_mobile_contract_fields` and ordinary `gods_of_africa_clear_demand`; otherwise the queued `.604` report loses its subtype before rendering.
Add the receipt subtype to the existing `gods_of_africa_clear_report_receipts` reset helper, following that helper's enrollment/archive/cancellation lifecycle rather than inventing a new acknowledgement timer or clearing policy.
Preserve the parent's latest-response contract and its documented multiple-queued-instance limit; this recommendation does not introduce a per-event-instance receipt archive.

## Concrete family/icon and documentation wiring

Keep `gods_of_africa_family_mobile_artillery` for the umbrella/category description.
Add player-facing leaves `gods_of_africa_family_trucks: "trucks"`, `gods_of_africa_family_artillery: "artillery"`, and `gods_of_africa_icon_artillery: "£artillery_texticon"`.
Reuse existing `gods_of_africa_icon_motorized` for truck subtype.
Vanilla `interface\texticons.gfx:2131-2135` registers `GFX_artillery_texticon`; no new asset, DDS, sprite alias, or DLC asset assumption is needed.
Branch `GetGodsOfAfricaDemandFamilyName`/`GetGodsOfAfricaDemandIcon` on demand type, `GetGodsOfAfricaPaymentIcon` on payment type, and `GetGodsOfAfricaSubstituteIcon` on canonical offer type.
Branch the existing `GetGodsOfAfricaResponseFamilyName` on `gods_of_africa_last_response_family = mobile_artillery` AND the matching `gods_of_africa_last_response_mobile_type`, returning the same concrete trucks/artillery leaves.
Its response branch must use only receipt fields after cleanup, never `gods_of_africa_demand_mobile_type`, payment type, or current stock.
Replace the generic family-2 response leaf with the two typed leaves; a malformed or absent receipt subtype uses the existing localized unknown family leaf rather than silently reporting trucks.
Branch each `GetGodsOfAfricaSubstituteSlot[1-3]Name`/`Icon` on that slot's own type.
Add `gods_of_africa_mobile_truck_capacity_tt` and `gods_of_africa_mobile_artillery_capacity_tt` to explain the real subtype and protected army/reinforcement reserve.
Missing/invalid family-2 types should show a localized unavailable requirement and fail the control gate, not fall through to truck/political-power icons.
Parent visible-flag localisation work is separate; this report does not take ownership of its edits.
Update matching helper docs, `docs\events\012_africa\gods_of_africa.md`, and any source spec implementation evidence/contract field description in the owner's change.
Also update parent `012_africa_gods_report_effects.md` to document the additional receipt subtype, its capture/clear lifecycle, and concrete response-family resolver.
No GUI layout rewrite or new window is required.

## Required boundary scenarios and validation contract

These are implementation acceptance scenarios, not claims that the proposed code was executed.
A Decimal arithmetic model checked the stock-only formula and integral quote/ceiling/partial invariants for six cases.

| Scenario | Expected behavior/evidence |
| --- | --- |
| Zero sender stock | Either subtype has zero spare; no family-2 quote or payment, regardless of historical production |
| Artillery deficit, truck-only sender | Host has artillery need and zero truck need; trucks cannot quote or satisfy that artillery contract |
| Valid artillery full stock | Sender stock/target/fielded 275/100/50 gives reserve 60 and spare 215; host 200/100/40 gives need 60; ceiling 53 and base quote 21; exactly 21 artillery transfers |
| Valid truck full stock | Sender 1000/100/100 gives reserve 100 and spare 900; host 200/100/30 gives need 70; quote/ceiling 70; exactly 70 trucks transfer |
| Mixed capacity and both host needs | Deterministic artillery attempt succeeds first; one artillery contract; truck stock never pads artillery affordability; try truck type only if its independent need is positive and artillery cannot quote |
| Healthy host stock | Host 200 target, 100 fielded, 100 stock covers shortfall; no deficit quote; route floor must also already be covered to remain healthy |
| Route-only need | With no army deficit, unlocked logistics floor can request only missing trucks; unlocked arsenal floor can request only missing artillery; without the corresponding route flag no arbitrary floor demand |
| Odd partial | Sender artillery stock 135/target 0/fielded 0 gives spare 110; host need 40 gives base quote 11; partial sends 5 artillery, leaves 6; repeated cooldown partial cannot overdraw the residual |
| Shared classifier regression | Retain all six physical equipment families, including aircraft 55 -> partial 27/residual 28 and family-2 11 -> partial 5/residual 6; no mobile-only fork of the parent's normalization |
| Response after cleanup | Successful artillery full response still names artillery after live demand/payment type fields are cleared; successful truck response names trucks |
| Partial/refusal/expiry receipt | Partial artillery receipt stores amount 5/balance 6/type artillery; refusal/expiry preserve the demanded subtype with amount 0 and unpaid balance |
| Accepted/failed substitute receipt | Successful typed family-2 offer records its accepted subtype; non-family-2 offer clears any old response subtype; failed transfer leaves the previous completed-response receipt unchanged and restores original live type |
| Sequential and reset receipts | Artillery response followed by fuel response has no leftover mobile receipt subtype; enrollment/archive/cancellation report reset clears the subtype alongside the four existing fields |
| Fractional reserve | Sender 500/257/257 yields reserve 25.7, spare 474, ceiling 118, base quote 47; partial 23 leaves 24 |
| Lost stock after quote | Full/partial/substitute callback recomputes matching spare; no truck substitution, no success/history/balance credit for a failed artillery preflight |
| Leniency and extension | Existing conduct/deadline result occurs; type and frozen payment amounts do not reroll or change |
| Malformed/future family-2 offer | Missing/unknown type rejects; valid typed offer uses its own slot type; failed acceptance restores original family/type/remaining and work price |
| Stale/dead/replaced host | Generation/existence/war/deadline guards reject native transfer; cancellation clears mobile fields through existing lifecycle paths without altering a successor's host target |
| Duplicate full resolution | First success clears active contract; second attempt cannot transfer or credit again |
| Native variant/source identity | Sender stock decrease and receiver stock increase match exact integer amount in the frozen archetype; neither replacement grants nor truck-for-artillery conversion occur |

Before owner completion, inspect source and MCP evidence for those same named cases and both subtype paths, including real callback scopes and cleanup closures.
Existing decision AI weights should remain unchanged in this lane patch; changed eligibility may alter observed AI choices, so the parent should include truck/artillery eligibility cases in its required read-only AI/probability audit before making AI behavior claims.
This handoff proposes no weighted patch and chooses no probability/balance target on the auditor's behalf.

## Reference routes, local citations, and unresolved facts

Current connected metadata exposes `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, and event inspection routes.
Live context for native equipment/reserve contracts, installed-doc-only `send_equipment` search with limit 1, and bounded `event_inspect` for `selector: { kind: "event", eventId: "chaosx.nr12.603" }` each returned the exact error **`timed out awaiting tools/call after 600s`**.
The audit used that time for source tracing and arithmetic rather than blocking on transport.
A narrower installed-doc-only `num_target_equipment_in_armies_k` search with limit 1 and bounded source lookup for `gods_of_africa_transfer_payment` were attempted separately and each subsequently returned the same 600-second timeout.
After the confirmed timeout, an exact installed-doc-only `modulo_temp_variable` search with limit 1 was retried.
That final retry returned no result before its orchestration cell was terminated at the bounded handoff boundary rather than waiting through another transport timeout.
No reference IDs, artifact URIs, or scenario/graph coverage were returned, so revision-bound `reference_read` could not be populated from a discovered ID and the exact local sections below were read directly.
No helper-expansion route, service-health claim, GUI render, or current-to-itself comparison is substituted for missing MCP evidence.
The parent must retain or obtain its owning event/helper inspection and scenario evidence before treating the implementation as complete.

Installed paths below are under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.

| Source and relevant section | SHA-256 revision |
| --- | --- |
| `documentation\effects_documentation.md:6550-6557` native send; `:4986-5011` modulo | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `documentation\triggers_documentation.md:6442-6452` temporary modulo | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `documentation\dynamic_variables_documentation.md:557-565,687-691` stock/army measures; `:873-875,927-929` broad production types | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| `documentation\script_concept_documentation.md:216-243` constants; `common\script_constants\documentation.md:1-32` schema | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`; `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:435-442,570-574` temp lifetime and arithmetic | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:2254,2285-2293` removal/partial delivery and `equipment` example | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Vanilla `events\AAT_Finland.txt:3722-3735` direct native transfers, including artillery | `363c53751ed2fbe113fbed5635940f4494b5c67f3bfa0a3787aa327f6cdfda13` |
| Vanilla `common\units\equipment\motorized.txt:3-40` motorized archetype, supply-truck identity, installed concrete model | `b25c3797280f471b89a43da5b02e135091cf205acdf37c09d547a88df52d5128` |
| Vanilla `common\units\equipment\artillery.txt:3-13` artillery archetype/type and separate later artillery archetypes | `24b4f418a5bf55dd3428cdc0171009ba35188aa1f97baae93e576e316d7463e1` |
| Vanilla `interface\texticons.gfx:2131-2135` artillery icon | `e0349b22f05affe550e755fc2e1f3a2ad3749fb016b5c9031b3672d9656304b5` |

The installed stock description alone does not fully specify variant aggregation or native variant-choice order; do not claim oldest-first/current-first delivery without separate evidence.
The inspected dynamic-variable documentation exposes army target/fielded counts but no documented native supply-network truck target counter.
Army reinforcement need and an explicit existing-route stock objective are supported design inputs; exact native supply-network shortfall remains an unresolved engine fact if the parent wants to add that as an additional input.
Weighted quality/obsolete rejection is not designed or validated here and must not be advertised as implemented by this lane patch.
The absolute ceilings/reserve anchors have bounded arithmetic evidence, not campaign balance observations.
Native stock movement, all version aggregation, temporary-variable persistence, and DLC execution were not observed in game; no game was launched and no logs were requested.

## Initial design snapshot identities and delivery limit

| Inspected source | SHA-256 |
| --- | --- |
| Main effects | `949dd25f64e48de3ad5a602147dbff3d59f3ea445c40704e544afea95b82b6aa` |
| Main triggers | `1e4e99a517bef1dd546ae0223142010b9e54e942972642073c6024a28d3e8297` |
| Constants | `dea075a53455cbcb894e33a8e5e8bf15dd1a5c2969edcec63ea70a96d18dbeea` |
| Equipment effects | `61c7189bdee1ec84f5c5315b4d5d18f0f97c978cd6f53387d3016e1c1b06b1ba` |
| Equipment triggers | `8113c7f41e3fe55be1bf191de7108fa6698cb7cecee8bd737f4d5691f85eb3ae` |
| Accepted full spec | `2ccb9fbdedb7f7715187397b6bdc31610dc0fdd7cf4e2b1388f16d7490066798` |
| Preserved previous armour architecture audit | `90478d30d4bc238ef2fc3afa71482742e938f94658fe18946fd26418b80fccbe` |

No simplification of the bounded trucks-AND-artillery coverage goal is recommended: both concrete subtype paths, native transfers, dynamic reserves/quotes, all payment gates, exact partials, subtype display, and cleanup are mapped above.
Implementation remains with the parent, and mandatory MCP evidence remains blocked by the recorded transport failures.
This handoff is implementation advice with exact touchpoints, not a gameplay completion claim or promotion of an unvalidated balance result into the accepted spec.
