# Event 029 sealing receipt contract

Disposition: implemented bounded helper package and two native decision consumers, awaiting closure review and native execution evidence.
Acceptance basis: the parent's 2026-10-08 acceptance of direct inline native-boundary serialization under the original anti-cycling and exact-refund requirements.
The accepted scope covers the two sealing families, manual payment, controller epochs, and native-boundary receipt closure.
Native civilian-factory ordering and concurrent reservation remain unproven and outside this helper's payment proof.
Use the current implemented API below and the actual-helper source cases in the linked evidence record.
The earlier blocked review, proposed names, equal-input diagnostic, and the 2026-10-08 native-lifecycle follow-up are archived in [seal_receipt_evidence.md](../../plans/029_riches_found_plans/seal_receipt_evidence.md).

Parent integration is present in `decision_riches_found_gold_seal_depths` and `decision_riches_found_demons_permanent_seal`.
Their availability and custom-cost callers retain the full two-factory composite and add the manual receipt gate with caller-owned scratch storage.
Selection calls the matching `start` helper, removal calls `resolve` and permits the unchanged mine outcome only for `result_consumed`, and native cancellation calls `cancel` without a success outcome.
The old direct debits and fixed-price refunds are removed from these two consumers.
No new cancellation trigger or visibility cancellation is introduced; the receipt stays pending until its actual native boundary.
The registered-state `on_state_control_changed` branch calls the state epoch helper before existing reconciliation, without a new on-action or recurring scan.
The source wiring preserves partial-seal effects, entombment-before-cleanup, native modifiers/durations, and all original AI coefficients.
Post-integration closure and native execution evidence remain required.

## Current implemented API and parent callsite contract

All ten public family wrappers are COUNTRY scope, with THIS equal to ROOT, the original payer, and FROM the exact original mine STATE.
The family is selected by the wrapper, with Gold enum 1 and Demons enum 2.
No public helper takes a named argument block.

| Family | Pure quote trigger | Manual start trigger | Selection payment effect | Native removal effect | Native cancellation effect |
| --- | --- | --- | --- | --- | --- |
| Gold | `rf_gold_seal_quote` | `rf_gold_seal_can_start_manual` | `rf_gold_seal_start` | `rf_gold_seal_resolve` | `rf_gold_seal_cancel` |
| Demons | `rf_demons_seal_quote` | `rf_demons_seal_can_start_manual` | `rf_demons_seal_start` | `rf_demons_seal_resolve` | `rf_demons_seal_cancel` |

`rf_seal_note_control_change` is the eleventh public helper, STATE scope only inside the existing native control-change hook.
It requires THIS = native FROM.FROM, ROOT = new controller, and FROM = old controller.
Insert its call inside the existing registered-state FROM.FROM block immediately before `riches_found_handle_state_control_change`.
Do not call it after reconciliation, from another timer, or over a country/world iterator.
Same-controller notifications make no epoch or counter writes.

The manual start trigger checks current route, the absent exact actor/mine/family slot, epoch readiness, whole-number counter capacity, and inclusive manpower/support reserves.
The start effect runs that preflight afresh, stores the coherent positive quote and pending flag, increments the mine's pending count, then debits manpower and the actual shared support-equipment helper once.
Gold remains 300 manpower and 150 support equipment, while Demons remains 600 and 150.
Both record the existing two-factory commitment and 60/90-day duration as metadata.
The helpers never read free factories, grant/refund factories, attach modifiers, or invent a reservation receipt.
The parent retains the existing factory availability/custom-cost gates and the native modifier unchanged.
The start gate's name explicitly identifies its manual-payment scope.

Every outer caller initializes the following thirteen temporary slots in its own native block before calling a wrapper.
This applies to trigger, localisation, selection, removal, and cancellation callers that consume outputs.
An initializer scripted helper cannot create durable caller storage on behalf of the outer caller.
The three generic payment/resolution effects allocate their own nested-consumer storage directly in their own frames as well.

```txt
set_temp_variable = { rf_seal_family = 0 }
set_temp_variable = { rf_seal_result = 0 }
set_temp_variable = { rf_seal_mine_seq = 0 }
set_temp_variable = { rf_seal_payer = 0 }
set_temp_variable = { rf_seal_state = 0 }
set_temp_variable = { rf_seal_epoch = 0 }
set_temp_variable = { rf_seal_manpower = 0 }
set_temp_variable = { rf_seal_support = 0 }
set_temp_variable = { rf_seal_civilian = 0 }
set_temp_variable = { rf_seal_days = 0 }
set_temp_variable = { rf_seal_refund_manpower = 0 }
set_temp_variable = { rf_seal_refund_support = 0 }
set_temp_variable = { rf_seal_closed = 0 }
```

The zero literals allocate storage and are not cost tuning.
Quote/preflight outputs are valid only when the trigger returns true.
Payment and resolution callers consume `rf_seal_result`, whose values come from the unique `rf_seal_protocol` int-schema constant category:

| Value | Name | Meaning |
| --- | --- | --- |
| 0 | `result_none` | No pending receipt exists, with no outcome or credit |
| 1 | `result_paid` | This invocation published and charged one receipt |
| 2 | `result_consumed` | This native boundary consumed its receipt for the existing success outcome |
| 3 | `result_refunded` | This native boundary closed and credited the saved discrete quote |
| 4 | `result_rejected` | Selection entry failed fresh manual preflight, with no custom debit |
| 5 | `result_invalid` | Context, receipt, or counter is malformed, with no closure, outcome, or credit |

`rf_seal_refund_manpower` and `rf_seal_refund_support` are fresh nonzero refund amounts only with result 3.
`rf_seal_closed` is an immediate fresh temporary result used internally, never a persistent boolean.
All persistent boolean receipt/exhaustion state uses flags.
Other outputs expose the family, mine sequence, exact payer/state pointers, captured epoch, saved or quoted manpower/support, and native civilian/duration metadata.
Private scratch slots are `rf_seal_fraction`, `rf_seal_manpower_k`, `rf_seal_signed`, the shared debit input `equipment_stockpile_removal_amount`, and the control hook's changed-state/old-controller/new-controller pointers.
They are not return storage or asynchronous identity.

For parent integration, add the family manual gate alongside the existing selection gates rather than replacing the two-factory composite with a narrower gate.
Wrap its implementation receipt/counter checks in `hidden_trigger` inside player-visible requirements so the internal pending/exhaustion flag names never become raw localisation keys.
The parent retains existing visible costs/requirements and owns any additional blocked-reason wording required by final integration.
In `complete_effect`, replace the two direct manpower/support debit instructions with the matching `start` helper.
Do not also retain those old debit instructions.
Only result 1 authorizes any existing project-start publication.
At the exact original native `remove_effect` boundary, initialize the slots and invoke the matching `resolve` helper once.
Only result 2 authorizes the existing success body.
Gold keeps its two seal flags, partial-seal guard, pressure effects, and existing reconciliation/refresh calls.
Demons keeps its seal flag and entombment harm before `riches_found_permanently_seal_mine`, followed by the existing reconciliation/refresh calls.
Replace the old fixed-quote failure refund branch rather than adding the resolver before it.
Result 3 has already refunded, and results 0/5 authorize no success, additional refund, or unrelated cleanup.
If the parent integrates native cancellation, use the family `cancel` helper in `cancel_effect` at that actual boundary, never on transfer or an independent timeout.
Cancellation always refunds its saved quote and never publishes a finish result.
There is no independent public raw finish/refund/consume API.
All generic `rf_seal_*` definitions other than the control hook are private implementation details.

Each COUNTRY tuple stores seven normal fields `rf_seal_{payer,state,epoch,manpower,support,civilian,days}_<family>_@var:rf_seal_mine_seq` and one literal pending flag `rf_seal_pending_<family>_<sequence>`.
Native integer variable targeting supplies the variable key, while documented meta token replacement constructs the flag and the static family portion.
The actor's country scope supplies actor identity, and both saved pointers are checked against the live original ROOT/FROM objects.
STATE storage is `rf_seal_control_epoch`, `rf_seal_pending_count`, and `rf_seal_epoch_exhausted`.
For two families at one actor/mine this is fourteen normal COUNTRY fields and two COUNTRY flags, plus the mine's two counters and exhaustion flag.
There are no global event targets, shared country slot, or periodic scans.
The count is incremented once per publication and decremented once per native closure.
Transfers and generic mine closure must preserve it and all other pending tuples.

The protocol's central `max_integer = 2147483647` is the documented normal whole-number limit.
The helper checks epoch/count integerness and bounds before any increment.
A real control change below the epoch limit increments once.
A real change at the limit marks the mine exhausted, making all existing receipts invalid for success and blocking starts.
The exhausted epoch resets to zero only when its module-owned pending count is zero.
With pending receipts, reset waits for every actual native boundary to refund or consume its own tuple.
With no pending receipts, the same real-change hook can mark and immediately reset without overflow.
The final native closure also resets an exhausted epoch after decrementing to zero.
This is counter-based rollover, with no virtual timeout or actor scan.
No refund rereads current price tuning or requires current control, route, or nonterminal status.

The count's coherence assumes these helpers exclusively own their new receipt fields and counters.
A damaged loaded receipt, impossible counter, or dead payer returns invalid and is retained for parent-owned recovery rather than silently erasing its contribution or guessing another payer.
The original mine sequence must remain immutable as in its existing one-time binding owner.
External replacement of that sequence can make its old tuple inaccessible and return none instead of invalid, with the old fields/count retained for owner recovery and no outcome or credit.
Quantity refunds do not reconstruct equipment manufacturer/variant provenance or reverse elapsed factory opportunity time.
The native callback serialization acceptance covers inline native boundaries only, with no scheduled receipt events or external raw resolver calls.

## Narrow control hook

The current hook is `common/on_actions/029_riches_found_on_actions.txt:23-33`.
Native context is new controller ROOT COUNTRY, old controller FROM COUNTRY, and changed state FROM.FROM STATE.
The existing hook saves the three regular event targets and then enters FROM.FROM for `riches_found_handle_state_control_change`.
The parent insertion point is inside that same registered-state branch, in FROM.FROM STATE, immediately before the existing reconciliation helper.
The proposed epoch helper must compare the actual old and new country pointers before mutation and require the state's actual controller to match ROOT.
A spurious same-controller callback must perform zero epoch writes, even if the old and new regular aliases both exist.
The current reconciliation helper updates `riches_found_recorded_controller`, so an epoch helper after reconciliation would lose that pre-change comparison if it used the recorded pointer.
Using the native FROM/ROOT pair avoids relying on a mutable alias and entering the state does not rebind ROOT.
The state registration flag and sequence validate the state object.
Country pointers require COUNTRY `exists = yes` when entered, never `scope_exists` on a variable pointer.

This is a documented scope contract and source insertion point.
No epoch helper was implemented, so spurious-callback suppression is a required source case, not a passing implementation test.
No whole-world scan or additional recurring hook is needed.

## Proposed helper map

Each family has separate public names and separate payer-country fields keyed by the exact mine sequence.
No country-wide single-project slot is permitted.
Call syntax would be `= yes`, with inputs in documented temporary storage, never named argument blocks.

| Proposed name | Scope | Inputs | Outputs | Side effects | Parent consumer |
| --- | --- | --- | --- | --- | --- |
| `rf_gold_seal_quote`, `rf_demons_seal_quote` | COUNTRY THIS = ROOT, FROM STATE | Exact family through wrapper and native target | Sequence and coherent manpower/support/civilian/duration quote | Temporary output writes only | Existing cost display and start gates |
| `rf_gold_seal_can_start`, `rf_demons_seal_can_start` | Same COUNTRY context | Current route and quote | Eligibility | Read-only persistent state | `available`, `custom_cost_trigger` |
| `rf_gold_seal_start`, `rf_demons_seal_start` | Same COUNTRY context | Native reserved entry context, full current route | Fresh paid result | Publish pending receipt, then debit discrete costs once | `complete_effect` |
| `rf_gold_seal_finish_valid`, `rf_demons_seal_finish_valid` | Same COUNTRY context | Original native invocation identity, exact receipt | Current paid/epoch/finish validity | Temporary output writes only | `remove_effect` |
| `rf_gold_seal_consume`, `rf_demons_seal_consume` | Same COUNTRY context | Exact validated invocation | Fresh consumed result | Close receipt once without currency credit | Successful `remove_effect`, before mine mutation |
| `rf_gold_seal_refund`, `rf_demons_seal_refund` | Original payer COUNTRY | Exact original invocation and target | Fresh refunded result and recorded refund amounts | Close once and credit saved manpower/support quantities | Failed native callback, including native cancellation if integrated |
| `rf_seal_note_control_change` | FROM.FROM STATE in native hook | Native old/new controller pointers | None | Advance state epoch on a real change only | Existing control-change hook before reconciliation |

The original invocation identity input is unresolved and cannot be replaced by reading the latest receipt generation.
Without the missing native guarantee, the resolver, consume, and refund APIs cannot honestly authorize reuse.

## Receipt storage, outputs, and exact counts

Proposed storage is seven COUNTRY normal variables plus one COUNTRY pending flag for each actor/mine/family tuple.
The seven fields are payer pointer, state pointer, captured control epoch, actual paid manpower, actual paid support equipment, native civilian commitment, and native duration.
The immutable sequence is the key rather than a redundant eighth field.
Two simultaneous families for one payer/mine therefore need fourteen variables and two flags.
Two payers for that same mine need independently owned tuples.
Different mines allocate independent keys, so one pending mine cannot block another mine.
One state epoch variable is additional STATE storage, independent of payer slots.
The existing `riches_found_event.registry_cap` is 64, so the proposed layout can represent 128 simultaneous mine/family tuples for a country participating at every registered mine, with 896 COUNTRY variables and 128 pending flags if all such tuples exist.
That is a derived storage count under the existing registry cap, not an additional project cap or a proven native reservation capacity.
No fields or flags are created by this blocked sidecar.

Variable `_@var:sequence` targeting is documented for integer values.
That variable rule must not be extended to flags by assumption.
Sequence-bearing flag names require separately verified native targeting or a literal name built through documented meta syntax, with the sequence validated before string construction.
A proposed flag name is `rf_gold_seal_pending_<sequence>` or `rf_demons_seal_pending_<sequence>`.
Persistent booleans use flags, not numeric 0/1 saved variables.

Every consuming outer caller would allocate these thirteen temporary outputs before the first nested helper call: `rf_seal_family`, `rf_seal_mine_seq`, `rf_seal_paid`, `rf_seal_valid`, `rf_seal_consumed`, `rf_seal_refunded`, `rf_seal_manpower`, `rf_seal_support`, `rf_seal_civilian`, `rf_seal_days`, `rf_seal_payer`, `rf_seal_state`, and `rf_seal_epoch`.
Initialize new storage to zero and do not reset intentional identity inputs between validation and closure.
Each nested caller also preallocates the outputs it consumes or forwards.
Temporary result booleans are immediate outputs, not durable project state.
No helper-created temporary slot may be treated as surviving return without caller allocation.
The parent's cited Gold Disease caller fix `9751194` is a parent-supplied precedent, not a commit examined by this sidecar.

Normal variables and exact whole-number identity/count fields must be validated without rounding, using scratch modulo by one where supported.
The existing registry assigns `riches_found_mine_sequence` once and the source search found its assignment in `riches_found_bind_history_sequence` only.
Terminal cleanup currently preserves that sequence, but cannot stand in for an immutable native invocation identity.

## Constants and tuning

| Family | Existing manpower source | Existing support source | Native factories | Existing days source |
| --- | --- | --- | --- | --- |
| Gold | `riches_found_decision_cost.manpower_standard` = 300 | `riches_found_decision_cost.support_heavy` = 150 | `civ_standard` = 2 | `riches_found_decision_duration.project` = 60 |
| Demons | `riches_found_decision_cost.manpower_heavy` = 600 | Same support source = 150 | Same factories = 2 | `riches_found_decision_duration.long_project` = 90 |

Do not redeclare these categories in the new constants file.
Only a unique protocol category for family enums, zero/one, sign inversion, and manpower conversion would be needed.
No new AI weights, price table, spend type, or duration band is proposed.
Refunds must load the saved positive paid quantities and never reread current tuning.
Factory commitment remains the existing static native modifier and is not a debit or refundable building.

Numeric rollover remains unresolved.
The offline variable page describes a larger normal-variable range and five fractional places, while installed math-expression documentation establishes fixed-point arithmetic without proving that the same range governs ordinary variable storage.
An arbitrary 2.1-million epoch cap, a wrap to zero/one, or a modulo epoch would create unsupported restrictions or identity reuse.
No such cap or rollover code is installed.
A production epoch implementation needs an authoritative normal-variable exact-integer bound and a collision-free rollover contract that preserves all outstanding old receipts, or another proven non-reused identity representation.
Counts in the source diagnostic in the linked evidence record are small exact integers and prove no general engine arithmetic bound.

## Parent migration and cleanup contract

1. Preserve both existing decision IDs, all route predicates, current icons/localisation, native factory modifier, durations, and AI source.
2. Share the coherent start quote and pending-slot gate between availability and custom-cost selection.
3. At native `complete_effect` entry, recheck the route, registration, nonterminal status, pending slot, and manpower/support reserves immediately before publication and debit.
4. Count two factories at selection, but do not count the project's own reservation twice at entry.
5. Publish the actor/mine/family receipt before debit and gate every start publication on the fresh paid result.
6. In the documented state hook, record a real control change before existing reconciliation and never refund or clear actor pending receipts there.
7. Native `remove_effect` must resolve the exact paid invocation, require unchanged epoch and current finish requirements, and consume it once before applying the existing successful mine outcome.
8. Gold retains the localized restricted route, partial-seal guard, and current pressure effects.
9. Demons retains evacuation or military-purge eligibility and calls entombment harm before permanent-seal terminal cleanup.
10. Failure closes and refunds the exact saved discrete amounts to the original payer once, regardless of current controller or current prices.
11. Generic transfer, temporary closure, permanent closure, and terminal cleanup must leave every other pending payer tuple intact until its own native callback resolves.
12. Do not use the availability purchase gate again at expiry, current selected-mine UI state as original identity, or a virtual deadline as proof that the native callback has closed.

The original native callback proof in step 7 is the blocking dependency.
The factory reservation-before-entry ordering and atomicity in step 4 remain separate gaps.
No documented inspection establishes whether a rejected stale click still incurs its native reservation or cooldown.
No factory grant, ledger currency, or compensating modifier is proposed.

Existing regular targets in the control hook are short-lived scope aliases and require no manual clearing.
No new regular or global event targets are needed for the proposed payer tuples.
A global shared payer/mine target would break parallel projects.
Package documentation would remain here, with the parent updating any shared documentation after integration review.
No icons, GUI, registry, catalog, art, event route, mission, or asset change is required.
