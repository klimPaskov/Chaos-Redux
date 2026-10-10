# Event 029 transport cost contract

Disposition: implemented helper module, with parent integration and native callback identity evidence unresolved.
The bounded transport-cost assignment dated 2026-10-07 authorizes the three cost families and these new files.
It does not authorize edits to the existing decisions, localisation, cost triggers, works effects, or shared helper documentation.

## Purpose and scopes

The module quotes, checks, debits, refunds, and closes three Event 029 transport purchases.
All public helpers execute in COUNTRY scope with THIS equal to ROOT, the original paying country.
FROM must be the exact mine STATE.
The source names are `riches_found_mine_sequence`, `riches_found_rail_route`, and `riches_found_port_route`.
The `rf_` helper names are lower case as requested.

The state sequence is a persistent positive integer.
Quotation rejects a missing, zero, negative, or fractional sequence without rounding it or imposing an invented maximum.
Country receipt fields use `_@var:rf_transport_cost_mine_seq` targeting, with a separate prefix for each family.
The same mine can therefore retain receipts for multiple families and multiple original payers without a controller overwriting another payer.

## Helper map

| Family | Public quote trigger | Inclusive preflight trigger | Debit effect | Exact refund effect | Success cleanup effect |
| --- | --- | --- | --- | --- | --- |
| Specialist labour | `rf_specialist_transport_quote` | `rf_specialist_transport_can_pay` | `rf_specialist_transport_debit` | `rf_specialist_transport_refund` | `rf_specialist_transport_clear_receipt` |
| Workforce replacement | `rf_workforce_transport_quote` | `rf_workforce_transport_can_pay` | `rf_workforce_transport_debit` | `rf_workforce_transport_refund` | `rf_workforce_transport_clear_receipt` |
| Evacuation | `rf_evacuation_transport_quote` | `rf_evacuation_transport_can_pay` | `rf_evacuation_transport_debit` | `rf_evacuation_transport_refund` | `rf_evacuation_transport_clear_receipt` |

Each family also exposes `rf_<family>_transport_has_receipt`.
It validates and loads that payer's exact stored receipt.
The generic `rf_transport_cost_*` definitions are implementation details.
Call public helpers with `= yes`, never named argument blocks.

## Constants and tuning

Prices remain in the existing `riches_found_decision_cost` category.
The new file declares only the unique `rf_transport_cost_model` category.
It provides none = 0, land = 1, sea = 2, family identifiers specialist = 1, workforce = 2, evacuation = 3, sign inversion, integer validation, and the manpower conversion divisor.
These route identifiers are enums, not boolean payment markers.

| Family | Civilian reservation | Political power | Manpower | Trucks | Land token and quantity | Sea token and quantity | Spendable types |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Specialist labour | civ_standard = 2 | pp_standard = 25 | 0 | 0 | train_equipment_1, train_light = 1 | convoy_1, convoy_light = 5 | 3 |
| Workforce replacement | civ_standard = 2 | 0 | manpower_emergency = 1000 | 0 | train_equipment_1, train_standard = 3 | convoy_1, convoy_standard = 15 | 3 |
| Evacuation | civ_standard = 2 | 0 | manpower_emergency = 1000 | motorized_standard = 75 | train_equipment_1, train_standard = 3 | convoy_1, convoy_heavy = 30 | 4 |

Only one transport column is paid.
Affordability reads the exact concrete token that payment removes.
Train or truck archetype totals and equipment in armies do not substitute for the selected concrete stockpile.
Manpower affordability uses `manpower_k`, with raw quoted manpower divided by 1000.
Every positive fee is checked inclusively.
A fee absent from the family creates no reserve requirement, so replacement and evacuation remain eligible at negative political power if their actual costs are affordable.

Civilian factories are reserved through the parent's decision-level `modifier = { civilian_factory_use = ... }` for the existing `days_remove`.
The helper records and checks this reservation amount but neither removes factories nor creates a second reservation.
The parent must attach the two-factory modifier to all three consumers and release it through native timer completion or the proven cancellation path.
A refund restores discrete payments and closes their receipt.
It must never add factories as a refund.
Native modifier application, release, and stale-click behavior remain parent integration evidence.
The module cannot prove that native timer reservation is skipped when a stale click reaches complete_effect but its fresh helper preflight rejects.
That atomicity remains a parent integration blocker rather than permission to introduce an alternative reservation mechanic.

## Inputs, outputs, defaults, and caller storage requirements

Before a quote, preflight, or debit, the caller sets temporary `rf_transport_cost_route_request` to the exact chosen route enum.
A land request requires both `riches_found_rail_route` and `riches_found_rail_route_valid` on FROM.
A sea request requires both `riches_found_port_route` and `riches_found_port_route_valid`.
The existing capability refresh owner must keep those validity flags current.
The helper does not infer a route from available stockpiles or silently switch an unaffordable route.

For a state carrying exactly one chosen route, the parent can set its matching request enum.
If both route flags exist, the parent must supply the feature's actual accepted route choice.
Neither route is chosen by this module when that choice is unclear.
A missing or invalid request produces route none and zero price outputs, returns false, and creates no receipt or debit.

Every outer caller initializes the following temporary storage before invoking a public wrapper.
This includes trigger callers, scripted localisation callers, and effect callers whose `if.limit` invokes preflight.
Initialize output storage once at the outer boundary and preserve intentional inputs.

```txt
set_temp_variable = { rf_transport_cost_family = 0 }
set_temp_variable = { rf_transport_cost_route = 0 }
set_temp_variable = { rf_transport_cost_civilian = 0 }
set_temp_variable = { rf_transport_cost_pp = 0 }
set_temp_variable = { rf_transport_cost_manpower = 0 }
set_temp_variable = { rf_transport_cost_motorized = 0 }
set_temp_variable = { rf_transport_cost_transport = 0 }
set_temp_variable = { rf_transport_cost_mine_seq = 0 }
set_temp_variable = { rf_transport_cost_receipt_payer = 0 }
set_temp_variable = { rf_transport_cost_receipt_state = 0 }
set_temp_variable = { rf_transport_cost_paid = 0 }
set_temp_variable = { rf_transport_cost_closed = 0 }
```

The zero literals above initialize storage and are not price tuning.
Quotation outputs the route enum, civilian reservation, pp, manpower, motorized, transport amount, and mine sequence.
Family wrappers assign `rf_transport_cost_family`.
Debit sets `rf_transport_cost_paid` to one only after its own fresh coherent preflight and discrete debit.
Refund and success cleanup set `rf_transport_cost_closed` to one only after validating and closing the selected receipt.
Temporary result booleans never act as persistent payment state.
The generic debit and refund also allocate the quote outputs in their own frames before nested trigger reads.

For receipt validation, refund, or success cleanup, the caller supplies the original paid mine sequence in `rf_transport_cost_mine_seq`.
Do not call a quote between loading that sequence and closing the receipt.
A native targeted callback may use FROM's sequence only when its immutability for that paid invocation has been established.
If the state was registered under a different sequence, recovery needs the exact old sequence from the original callback context.
The receipt's recorded state must match FROM and its recorded payer must match ROOT.
Current controller, current route flags, and current prices are deliberately irrelevant to refund and success cleanup.

Private scratch temps are `rf_transport_cost_identity`, `rf_transport_cost_fraction`, `rf_transport_cost_manpower_k`, and `rf_transport_cost_signed`.
They have no public output contract and must not govern later callbacks.

## Persistent outputs and side effects

For each family, the paying country stores eight normal variables:

```text
rf_<family>_transport_route_@var:rf_transport_cost_mine_seq
rf_<family>_transport_civilian_@var:rf_transport_cost_mine_seq
rf_<family>_transport_pp_@var:rf_transport_cost_mine_seq
rf_<family>_transport_manpower_@var:rf_transport_cost_mine_seq
rf_<family>_transport_motorized_@var:rf_transport_cost_mine_seq
rf_<family>_transport_transport_@var:rf_transport_cost_mine_seq
rf_<family>_transport_payer_@var:rf_transport_cost_mine_seq
rf_<family>_transport_state_@var:rf_transport_cost_mine_seq
```

The route field's presence identifies the paid enum.
The debit rejects any existing field for that payer, family, and mine, including an incomplete receipt.
This blocks overwriting an active or damaged record.
Zero price components are stored as amounts, not boolean flags.

The receipt is written once before native debit commands in a synchronous helper with no nested event dispatch.
The prices stored in the receipt remain positive.
Separate scratch storage supplies negative debit amounts.
Refund loads the retained amounts, validates whole nonnegative prices and land/sea identity, clears all eight receipt fields, and credits only the recorded concrete token and discrete amounts.
Success cleanup clears the same fields without crediting.
Repeated closure without a matching receipt performs no payment or refund.
A damaged receipt remains untouched and requires explicit owner recovery.

Receipts are country owned throughout control changes.
There are no state receipt mirrors, global pointers, event targets, actor gifts, world scans, or periodic hooks.
No event-target cleanup is needed.

## Individual action recipes and migration

| Existing parent-owned consumer | New family | Migration |
| --- | --- | --- |
| `decision_riches_found_specialist_labor` | specialist | Replace its old PP, manpower, support-equipment, and train payment/refund with the public specialist helpers and the native two-factory reservation. |
| `decision_riches_found_gold_replace_workforce` | workforce | Replace its old PP plus simultaneous train/convoy payment/refund with emergency manpower, the chosen transport, and the native two-factory reservation. |
| `decision_riches_found_demons_evacuate_district` | evacuation | Replace its old PP plus simultaneous train/convoy payment/refund with emergency manpower, trucks, the chosen transport, and the native two-factory reservation. |

The parent owns these call sites.
No existing decision, YML, cost trigger, or works file is changed by this module.

For every action, use its public `can_pay` trigger in both `available` and `custom_cost_trigger`.
Initialize the documented temporary storage in each native caller before consuming helper outputs.
Use the same explicit route request and public quote for cost display and colours.
Remove old duplicate fees and refunds.
Retain the existing duration, requirements, outcomes, and AI ownership.

In `complete_effect`, initialize caller storage and set the actual route request before debit:

```txt
# COUNTRY THIS = ROOT, FROM is the mine. Caller storage initialized above.
set_temp_variable = { rf_transport_cost_route_request = constant:rf_transport_cost_model.land }
rf_specialist_transport_debit = yes
if = {
	limit = { check_variable = { rf_transport_cost_paid = constant:rf_transport_cost_model.one } }
	# Apply only the parent's existing start/authorization effects.
}
```

Use `rf_workforce_transport_debit` or `rf_evacuation_transport_debit` for the other two actions.
The shown land request is illustrative.
It is valid only when the actual chosen state route is land and its required flags are present.

In the original payer's delayed callback, initialize storage, load the original mine sequence, and validate the corresponding receipt before any gameplay outcome.
Use a family `has_receipt` trigger to distinguish a paid invocation from a stale click.
On accepted success, execute the existing outcome once and call the matching `clear_receipt`.
On rejection, call the matching `refund`.
Gate any further parent cleanup or publication on `rf_transport_cost_closed = one`.
A missing receipt must not trigger an outcome, refund, or cleanup belonging to another invocation.

## Identity blocker and unsupported analysis

Installed decision documentation and offline wiki establish actor COUNTRY and target FROM STATE for targeted decision evaluation.
The wiki distinguishes immediate `complete_effect` from delayed `remove_effect`.
They do not provide an invocation nonce or a demonstrated payload API that binds a delayed callback to a specific generation of the same payer/family/mine receipt.

The module therefore cannot distinguish an old callback from a later paid invocation with exactly the same payer, family, and mine sequence.
It blocks a second debit while the first receipt remains open, and repeated closure before re-payment is safe.
After a receipt is closed and another invocation is paid, a delayed duplicate callback could address the later receipt unless the parent proves native timer exclusivity and original callback identity.
No invented actor nonce, state mirror, placeholder ledger, or undocumented callback payload is supplied.
That integration proof remains blocked.
The parent must not claim callback-generation replay protection from this module.

A callback whose ROOT is another country cannot be repaired by merely entering the original payer's scope because that does not rebind ROOT.
Do not redirect refunds to FROM's current controller.
Do not guess an original payer or mine sequence when native context is absent.

Concrete-token quantity refund does not reconstruct producer, variant, equipment wear, native PP cap overflow, or recruitment-law effects.
Installed effects documentation establishes quantity mutation, not restoration of an equipment item's provenance.
Native reservation timing and actual map connectivity remain outside this helper's source model.

## Validation and references

The dated handoff records live MCP results, exact reference revisions, source-model scenarios, and unresolved fields.
Source inspection and bounded source execution are not native engine execution.
The parent's separate probability auditor owns the unchanged decision AI surfaces and the frozen physical-cost snapshot.

Required reference sections read for this module:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`: 263-327 event targets, 425-454 normal variables and temporary lifetime, 546-553 integer targeting.
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`: 339-354 timer and modifier lifetime, 513-536 ROOT/FROM targeting, 579-588 FROM state targeting.
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`: 75-82 variable-valued effects, 700-743 variable operations, 1068-1075 PP/manpower, 2253 equipment mutation.
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`: 571-605 variable comparisons and scopes.
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`: 283-329 ROOT/PREV/FROM examples and invalid-target limits.
- Installed `documentation/script_concept_documentation.md`: 184-215 arithmetic limits and 216-245 script constants.
- Installed `common/script_constants/documentation.md`: complete schema and examples.
- Installed `documentation/effects_documentation.md`: 1252-1268 equipment mutation, 1468-1477 manpower scope, 1854-1863 PP scope, 2773-2783 clearing, 7888-7909 variable assignment.
- Installed `documentation/triggers_documentation.md`: 2110-2136 inclusive comparisons and 6442-6454 modulo scratch validation.
- Installed `documentation/dynamic_variables_documentation.md`: 469-472 manpower in thousands, 557-559 equipment reader, 592-594 civilian-factory reader.
- Installed `common/decisions/_documentation.md`: 12-44 actor/target scopes.
- Vanilla `common/decisions/INS.txt`: 2809-2837 delayed effect and concrete train token precedent.
- Existing `common/scripted_effects/chaosx_dynamic_effects.txt`: 748-816 stockpile helpers, and corresponding `.md`: 304-350 inputs, defaults, side effects, and exact-model limitations.
- Current Event 029 Part 3: 173-178 specialist labour, 546-551 workforce replacement, 576-584 evacuation.

No GUI, icons, visual assets, units, equipment definitions, or 3D models are introduced.
Future work is limited to parent integration and the missing callback evidence.
Broader reuse would require a separately accepted caller and identity contract.
