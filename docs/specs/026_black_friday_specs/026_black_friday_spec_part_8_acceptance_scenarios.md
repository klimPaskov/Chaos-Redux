# Acceptance scenarios

## Evidence standard

Source review, MCP inspection, scripted validation, and live testing serve different purposes. Event-chain and weighted-logic surfaces require the current HOI4 MCP workflow during implementation. Live testing remains necessary for Friday timing, displayed prices, actual payments, save persistence, and multiplayer behavior.

A forced launch cannot prove natural selection or weekday gating.

## Reservation and timing scenarios

| ID | Setup | Action | Expected result |
| --- | --- | --- | --- |
| `BF-T01` | Chaos 199, Event 26 enabled and unfired | Inspect event list and allow timer selection | Event 26 shows `N/A` and cannot be selected |
| `BF-T02` | Chaos 200 on Monday | Automatic picker selects Event 26 | One global reservation is created, no popup appears, and the next timer continues |
| `BF-T03` | Reserved on Monday, chaos stays at least 200 | Advance to Friday | One activation occurs on Friday |
| `BF-T04` | Event 26 selected on Friday at 200 chaos | Resolve selection | Event activates the same day through the direct path |
| `BF-T05` | Reserved at 250 chaos | Drop chaos to 199 before Friday | Friday is skipped and reservation remains |
| `BF-T06` | Continue `BF-T05` | Raise chaos to 200 before a later Friday | Event activates on that later Friday |
| `BF-T07` | Reserved at 700 chaos | Reach Friday at 599 chaos | Baseline 50 percent discount activates |
| `BF-T08` | Reserved at 250 chaos | Reach Friday at 600 chaos | Evolution I activates at 75 percent |
| `BF-T09` | Active at 50 percent | Raise chaos above 600 during the day | Discount remains 50 percent |
| `BF-T10` | Active at 75 percent | Lower chaos below 600 during the day | Discount remains 75 percent |
| `BF-T11` | Reserved | Disable Event 26 | Reservation clears, event remains unfired, and no history entry appears |
| `BF-T12` | Continue `BF-T11` | Re-enable at 200 chaos | Event returns to the eligible pool without restoring the old reservation |
| `BF-T13` | Active sale | Disable Event 26 | Current sale finishes normally and cannot duplicate |
| `BF-T14` | Reserved | Begin terminal event freeze | Reservation clears through terminal cleanup |
| `BF-T15` | Active sale | Begin terminal state | Sale follows the documented terminal cleanup policy and cannot remain permanent |
| `BF-T16` | Reserved below 200 on Friday after the normal daily check | Raise chaos to 200 later that Friday | The central chaos-change hook activates the sale that Friday |
| `BF-T17` | Reserved while the ordinary event system is paused | Reach an eligible Friday, then resume that Friday | Reservation survives the pause and activates once on resume |
| `BF-T18` | Reserved, then selecting country is annexed or switched | Reach an eligible Friday | The actorless reservation remains valid and activates once |
| `BF-T19` | Active baseline or evolved sale | Toggle Evolution I | The snapshot and logged activation remain unchanged |

## Event-system pacing scenarios

| ID | Setup | Expected result |
| --- | --- |
| `BF-P01` | Automatic reservation | Random selection resolves one timer transaction without adding fired count or minor pressure |
| `BF-P02` | Friday activation | Fired count, minor pressure, dynamic major gain, and history increment once |
| `BF-P03` | Friday activation while another timer is running | Current countdown is not reset or replaced |
| `BF-P04` | Two player timers select during the same date | One reservation survives and the second selection path rejects Event 26 |
| `BF-P05` | Same-day Friday selection | Reservation and activation still count as one Event 26 fire |
| `BF-P06` | Save and reload reserved state | No duplicate reservation or timer reset occurs |

## Discount and rounding scenarios

| ID | Ordinary current cost | Active sale | Expected payable amount |
| --- | --- | --- | --- |
| `BF-R01` | 0 integer units | 50 percent | 0 |
| `BF-R02` | 1 integer unit | 50 percent | 1 |
| `BF-R03` | 1 integer unit | 75 percent | 1 |
| `BF-R04` | 2 integer units | 50 percent | 1 |
| `BF-R05` | 3 integer units | 50 percent | 2 |
| `BF-R06` | 3 integer units | 75 percent | 1 |
| `BF-R07` | 5 integer units | 50 percent | 3 |
| `BF-R08` | 5 integer units | 75 percent | 2 |
| `BF-R09` | 101 integer units | 50 percent | 51 |
| `BF-R10` | 101 integer units | 75 percent | 26 |
| `BF-R11` | One factory commitment | Either sale | One factory remains committed |
| `BF-R12` | Five factory commitment | 50 percent | Three factories remain committed |
| `BF-R13` | Five factory commitment | 75 percent | Two factories remain committed |

## Composition scenarios

| ID | Ordinary modifiers | Expected result |
| --- | --- | --- |
| `BF-C01` | Base 100 with an ordinary 20 percent discount | Baseline Black Friday charges 40 |
| `BF-C02` | Base 100 with an ordinary 25 percent surcharge | Baseline Black Friday charges 63 after upward integer rounding |
| `BF-C03` | A second universal payment-ratio source is active | Sources multiply in deterministic order and quantize once |
| `BF-C04` | The second source expires first | Black Friday remains active without restoring a stale value |
| `BF-C05` | Black Friday expires first | The second source remains active |
| `BF-C06` | A family has a documented source exclusion | Other sources remain and the tooltip follows the registry disposition |

## Transaction integrity scenarios

| ID | Setup and action | Expected result |
| --- | --- | --- |
| `BF-X01` | Open a decision before activation, click during sale | Payment uses the sale price |
| `BF-X02` | Open a decision during sale, click after expiry | Payment uses the ordinary current price |
| `BF-X03` | Open a confirmation window during sale, confirm after expiry | Confirmation recalculates the price |
| `BF-X04` | Pay upfront during sale for a delayed project | The committed payment keeps the sale price |
| `BF-X05` | A delayed installment becomes due after expiry | That installment uses the post-sale price |
| `BF-X06` | A paid action fails and refunds | Refund equals the amount actually paid |
| `BF-X07` | Attempt a second refund | No second refund occurs |
| `BF-X08` | Ordinary cost is negative or a reward | No discount multiplier is applied |
| `BF-X09` | A static action has three source records | Only the correct normal, 50 percent, or 75 percent record is visible and valid |
| `BF-X10` | Save and reload during a refundable paid action | Paid amount and refund state persist |
| `BF-X11` | One action pays political power, equipment, and fuel | Each component is discounted and rounded separately, and the action commits once |
| `BF-X12` | The multi-resource action in `BF-X11` is refunded | Each paid component returns once and no ordinary amount is refunded |
| `BF-X13` | A multi-resource action completes during achievement tracking | It credits only its registry-defined primary family |
| `BF-X14` | Two players quote country-specific costs at the same time | Neither quote overwrites the other payer's amount or display |

## Cost family coverage scenarios

For each completed registry row, create one baseline and one Evolution I test where the surface is available. The minimum family checks are:

| ID | Family | Required proof |
| --- | --- | --- |
| `BF-F01` | Political power | Displayed and paid value match |
| `BF-F02` | Law | Real law-change cost is reduced and eligibility remains |
| `BF-F03` | Advisor or personnel | Hiring cost is reduced and slot rules remain |
| `BF-F04` | Command power | Ability cost is reduced and cooldown remains |
| `BF-F05` | Army experience | Payment and display match |
| `BF-F06` | Navy experience | Payment and display match |
| `BF-F07` | Air experience | Payment and display match |
| `BF-F08` | Equipment | Correct equipment type and amount are debited |
| `BF-F09` | Convoys | Exact discounted amount is removed |
| `BF-F10` | Trains | Exact discounted amount is removed |
| `BF-F11` | Fuel | Exact discounted amount is removed |
| `BF-F12` | Manpower | Exact voluntary discounted amount is removed |
| `BF-F13` | Stability or war support | Correct precision and floor apply |
| `BF-F14` | Civilian factory commitment | Factory count, duration, and restoration are correct |
| `BF-F15` | Military factory or dockyard commitment | Commitment count and duration are correct |
| `BF-F16` | Intelligence | Cost falls without changing network, operative, target, or duration rules |
| `BF-F17` | MIO or equivalent organization | Real cost and displayed cost match |
| `BF-F18` | Special project | Registered payment falls and project prerequisites remain |
| `BF-F19` | Custom mechanic currency | Exact currency quantum and floor apply |
| `BF-F20` | Scripted GUI action | Button text, affordability, payment, and AI equivalent agree |

Every additional registry family receives its own test ID.

## AI scenarios

Run the named AI probability scenarios from Part 5. Where weights change, perform baseline inspection, owner patch, and probability comparison with the same scenario inputs.

Live time progression should confirm that AI countries can use valid cheaper actions without purchase spam, invalid targets, duplicate static variants, or reserve collapse.

## Multiplayer scenarios

| ID | Setup | Expected result |
| --- | --- | --- |
| `BF-M01` | Two human players, one reservation | Both receive one Friday popup and use the same ratio |
| `BF-M02` | Two timers reach Event 26 | One reservation and one history row |
| `BF-M03` | One player tag switches during sale | New human country sees active status and the same price |
| `BF-M04` | A player joins during sale | Joined player reads current global snapshot and expiry |
| `BF-M05` | Simultaneous clicks on independent country actions | Each country pays its own correctly rounded price |
| `BF-M06` | Save and reload multiplayer session | Reservation, snapshot, and expiry remain synchronized |

## Event Logs and presentation scenarios

| ID | Check | Expected result |
| --- | --- | --- |
| `BF-U01` | Event list below 200 chaos | `N/A`, not zero |
| `BF-U02` | Event list while reserved | Truthful reserved status |
| `BF-U03` | History after activation | One actorless Event 26 row on Friday |
| `BF-U04` | Evolution at 600 chaos | One Evolution I row with correct tier and stage |
| `BF-U05` | Evolution disabled at 600 chaos | Baseline sale, no evolution row |
| `BF-U06` | Event Details while active | Correct percentage and next-tick expiry |
| `BF-U07` | Cost tooltip during sale | Final paid cost and source text agree |
| `BF-U08` | Cost tooltip after expiry | Black Friday source disappears and current ordinary cost returns |
| `BF-U09` | Report image and status icon | Correct assets appear with no missing texture |
| `BF-U10` | Localisation | No raw keys, stale desert wording, clipped text, or contradictory percentages |

## Save and reload checkpoints

Create dedicated checkpoints for:

- eligible and unfired
- reserved before Friday
- reserved after a skipped low-chaos Friday
- active baseline sale
- active Evolution I sale
- one refundable transaction paid during sale
- achievement progress before the fifth family
- expired sale

Each checkpoint must preserve the expected state and must not replay a popup, history entry, or payment.

## Catalog and documentation acceptance

The implementation is not ready for completion audit until:

- the authoritative XLSX row for ID 26 describes Black Friday
- the duplicate no-ID Black Friday backlog row is resolved
- CSV exports are regenerated from the workbook
- the old desert-industry script, localisation, news references, event name mappings, and docs are removed or replaced
- Event Details and spreadsheet mirror fields agree
- the cost coverage registry is complete for the implementation commit
