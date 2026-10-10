# Event 035 Public Works escrow sidecar

Status: implemented isolated receipt/arithmetic and opt-in native-return helpers under the parent's accepted U1 full-unused policy.
The payment, project failure and completion, transfer, pulse and cleanup call sites are wired in `035_great_depression_decision_effects.txt`, `035_great_depression_public_works_effects.txt`, `035_great_depression_effects.txt` and `events/035_great_depression.txt`.
The player sees one line on the program tooltip that unused materials return to the stockpile and no running balance.
The physical legacy of Convert Works into Lasting Capacity remains pending.
Acceptance basis: the parent explicitly requested these three new helper files and a handoff for Part 3 regional-work interruption and Part 4 cleanup.
The parent owns all shared action, project, selector, presentation, and cleanup call sites.
No helper debits payment, grants a factory, changes a national modifier, scans the world, or substitutes money/equipment for another resource.

## Public helper map

All effects run in STATE under a COUNTRY ROOT caller.
Invoke with `= yes`.
There is no named-parameter API or file-scoped macro dependency.

| Helper | Inputs / gate | Outputs and side effects |
| --- | --- | --- |
| `great_depression_works_escrow_prepare` | Existing prepared PW need, current actor/site/episode/open slot, four current integer quotes | Immutable `prepared_*` normal state fields and `prepared` flag, no debit |
| `great_depression_works_escrow_bind` | Fresh paid current PW plan, matching quotes, exact payer/site/episode/action count/day, newer authorization, coherent work duration | Immutable funding identity, gross quotes, required work, zero initial used work, `open` flag, clears preparation and stale policy permission |
| `great_depression_works_escrow_adopt_live_context` | Actual matching existing adoption receipt, prior live episode, exact paid PW payer/auth/action/site/duration | Updates only the live owner/episode mirror, no refund, debit, CIV migration or funding reset |
| `great_depression_works_escrow_authorize_full_unused_return` | Accepted U1 policy, exact funded request, matching current paid PW payer/action witness | Enables full-unused returns only for this matched open funding row |
| `great_depression_works_escrow_measure_unused` | Exact request and current project type/auth/required-work identity | Monotone bounded used work, integer `used_*` / `unused_*`, `remaining_work`, fresh `quote_ready` output, no native refund |
| `great_depression_works_escrow_settle` | Fresh exact funding request, authenticated parent retirement intent, measured quote, eligible original payer and explicit return policy for nonzero returns | Consumes exactly this open funding once, frozen `settlement_*` snapshot, `settled` / `fresh_settlement`, optionally emits native original-payer credit commands |
| `great_depression_works_escrow_discard_preparation` | Same unpaid preparation payer/site, no open funding, action count has not reached its expected payment witness | Clears only unpaid preparation, never settled history or material funding |
| `great_depression_works_escrow_can_prepare`, `great_depression_works_escrow_can_bind` | Pure preflight predicates | Boolean eligibility, no persistent write |
| `great_depression_works_escrow_funding_is_coherent`, `great_depression_works_escrow_request_matches_funding`, `great_depression_works_escrow_project_matches_funding` | Exact receipt and work contract | Boolean identity and authority proof |
| `great_depression_works_escrow_payer_can_receive` | Stored original country exists and uses normal civilian systems, excludes special/nonhuman classes | Boolean recipient eligibility, does not require that country to remain in an active depression |
| `great_depression_works_escrow_integer_input_is_whole`, `great_depression_works_escrow_quote_is_nonnegative_whole`, `great_depression_works_escrow_no_material_return_due` | Explicit numeric storage | Internal pure validation |

Public outputs use normal STATE storage.
Temporary variables only support internal integer predicates and are not public outputs.
Callers therefore need no surviving temporary output frame.
Every effect and nested country credit reads frozen normal state data.
ROOT is not rebound by entering the original payer.
Inside that payer scope, PREV is the escrow state, and native credits read `PREV.great_depression_works_escrow_settlement_unused_*`.

## Preparation and real payment binding

The current parent payment family is Public Works.
Its actual native debit is COUNTRY `add_manpower` with the negative manpower quote, `add_fuel` with the negative fuel quote, and `add_equipment_to_stockpile` with negative `train_equipment` quantity.
CIV is a committed capacity term, not a returned stockpile.
The shared `great_depression_committed_civilian` field is overwritten by other action families and is not an escrow source of truth.

Prepare freezes ROOT's `great_depression_cost_manpower`, `great_depression_cost_fuel`, `great_depression_cost_trains`, and `great_depression_cost_civilian` before that real debit.
It also freezes site, original payer, original episode, preparation day, next expected paid-action count, and the pre-authorization serial from the existing PW preparation.
Duplicate preparation cannot overwrite an outstanding preparation or open funding.
The first trusted valid actor may have no successful-action counter yet.
Preparation treats only that absence as zero, without writing a country counter, and predicts the first actual count of one.
Binding still requires the existing real paid path's fresh positive counter.

The parent must call the existing real launch/debit/authorization/bind chain.
After it produces its actual paid PW plan, call escrow bind.
The escrow does not create, emulate, or debit a payment.
Binding verifies the existing positive PW paid-action count, its expected fresh serial/count/day, exact original payer/site/episode, current registration, unspent authorization, and all four unchanged quote values.
The frozen required work must match the already coherent shared project duration.

Binding clears `great_depression_works_escrow_full_unused_return_authorized` so policy permission from an old receipt cannot enable a later one.
Funding's original payer, original funded episode, authorization, paid-action count, type, and site remain immutable during transfer.
They are distinct from the parent's live successor plan episode and live owner.
The escrow also stores `live_owner` and `live_episode`, initially the funding payer/episode.
After the parent actually adopts the project, `great_depression_works_escrow_adopt_live_context` accepts only the matching native adoption receipt and prior live episode, then updates those two mirror fields.
That prevents a later unrelated same-serial project from being mistaken for the funded project, while retaining original material provenance through real adoption.

## Exact request fields

Before measuring or settling, the authorized parent sets these normal variables on the exact escrow state:

- `great_depression_works_escrow_request_site`
- `great_depression_works_escrow_request_payer`
- `great_depression_works_escrow_request_episode`
- `great_depression_works_escrow_request_auth`
- `great_depression_works_escrow_request_action_count`

They must match the full frozen funding identity.
A site pointer alone does not authorize settlement.
ROOT must be the original payer, or the existing PW plan's actual current live owner that owns the state.
An arbitrary foreign ROOT or stale receipt cannot settle another transaction.
A successor supplies the original funded episode, not its own current national episode.
Existing project authorization, Public Works type, required work, and actual controlled-work count must still exist and match before cleanup clears them.
A project-type near miss, changed required work, fractional count, negative quote, wrong payer/site/episode/auth/action count, or occupied funding slot fails closed.

## Consumption arithmetic and capacity

For gross integer quantity G, immutable required work R, and bounded monotone actual controlled work W:

`remaining = R - min(R, max(previous_used_work, actual_project_work))`

`unused = floor(G * remaining / R)`

`used = G - unused`

This defines the parent's accepted U1 full-unused quantity in conservative whole native units.
It is a material-progress budget abstraction tied to measured accepted work, not native evidence that particular people, fuel batches, or train versions remained physically reserved.
The used portion is never returned, work zero returns the entire proved unused material budget, and completed work returns zero.
Manpower is people, fuel is the same units as the current debit quote, trains are whole units, and CIV is the frozen number of committed civilian factories.
Fractional input quotes and work/receipt counters reject rather than being rounded into proof.

The implementation uses quotient/remainder:

`r = G mod R`

`base = ((G - r) / R) * remaining`

`tail_numerator = r * remaining`

`tail = (tail_numerator - (tail_numerator mod R)) / R`

`unused = base + tail`

It never forms G times work.
The base and final result are bounded by G.
The tail product is below R squared.
The existing accepted duration maximum is 245 days, so that product is below 60,025.
No artificial material/receipt numeric maximum is introduced.
All divisions have mathematically integral quotients, and trains cannot be rounded upward from fractions.
Normal-variable/native modulo precision still requires native evidence.
Installed math-expression fixed point and the offline normal-variable precision description are different representations and do not establish a universal maximum.
Tests must enforce native-sized intermediate arithmetic instead of relying solely on unbounded Python integers.

Measure only uses the shared actual controlled-work counter, never calendar time or callback count.
The parent's process integration must call it after accepted work advances and before project identity/work is cleared.
At failure, pause, transfer or recovery, the last authenticated counter plus the escrow high-water count supplies consumption.
Dropping the counter or changing the type before settlement rejects safely and leaves the receipt outstanding.

## Settlement and accepted opt-in policy boundary

`great_depression_works_escrow_full_unused_return_authorized` is a required explicit state permission for any nonzero material return.
It is absent by default and cleared on new funding.
After successful funding capture and setting the exact request fields, the parent calls `great_depression_works_escrow_authorize_full_unused_return` once.
That helper checks the matching funded PW payer/action witness before enabling the flag.
The acceptance basis is the parent's explicit U1 instruction approving exact unused budget by monotone accepted work, with conservative whole units.
The permission applies only to the matched PW escrow, never a generic project, sunk-cost shop, arbitrary salvage fraction, or mobilization anchor.

Funding policy alone does not authorize a mid-project return.
`great_depression_works_escrow_can_settle` also requires `great_depression_works_escrow_retirement_requested` from the parent's exact authorized terminal/cancellation/recovery callback.
An old completed/failed authorization serial alone is deliberately not accepted because serials can restart in later episodes.
That private retirement flag is cleared on new funding and never set by this sidecar.
It grants no new gameplay outcome and does not itself stop the shared project.
The parent must retire that exact paid authorization and close its slot as part of the same terminal transaction so refunded work cannot continue to award map output.
Without material-return permission, `measure_unused` provides exact quantities and an authorized retirement settlement leaves an open `pending_return` receipt.
An ineligible, dead, or vanished original payer likewise leaves nonzero liability pending.
The successor never receives the refund instead.
No cash, replacement equipment family, compensation, or silent forfeiture occurs.
The parent must preserve a bounded pending-state list before deleting actor or center arrays.

With that exact authorization and an eligible original payer, settlement freezes quantities and identity before entering that country's scope, consumes only this validated open receipt, and emits at most one native credit per positive material quantity.
Zero-unused settlement needs no return permission and can close fully consumed work without entering a nonexistent payer.
Repeated, stale or mismatched requests cannot refund twice, clear another durable settlement, or restore an already consumed receipt.
`fresh_settlement` is cleared at every attempt and set only after this invocation consumed the matching open row.
The durable `settled` flag and `settlement_*` snapshot survive later attempts.
Parent cleanup must distinguish that fresh result from an already-used receipt.

The snapshot records quantities offered to the native refund commands.
It does not prove actual engine receipt, fuel-cap overflow behavior, train variant/producer preservation, or manpower mobilization accounting.
The current debit records only a train-archetype quote, not the concrete train versions removed.
Those native semantics remain explicitly unproven even though the quantity-level U1 policy is accepted.
They require parent/native evidence and are not filled with a substitute or silently treated as exact native receipt.
In particular, no automatic population/mobilization compensation is implemented.

## CIV row and transfer proposal, pending parent integration

Each funded state retains `great_depression_works_escrow_gross_civilian`, the full quote and required/used work, independently of the global last-action quote.
The parent should maintain a bounded country-owned list of funded state pointers and aggregate only exact live obligation rows.
Validate state identity, live CIV obligor, funding nonce, active/suspended disposition, and receiver eligibility per row.
Do not sum the shared last quote or scan all states/countries.

Materials stay owned by the original payer after transfer.
Migration of the ongoing CIV obligation to ROOT's successor requires a separate exact acceptance/availability gate and one acknowledged old-row removal plus new-row insertion.
The gate must check free usable CIV after other obligations, avoid double-counting the same row, and handle old/new obligor equality.
The parent owns that policy, slot cap, paused-project obligation handling, modifier application, and availability wiring.
This sidecar never changes shared CIV fields or modifiers.
There is no new tuning constant needed for the material arithmetic.
Any future CIV cap, refund fraction, anchor, or transfer cost must be declared and accepted by the parent rather than inferred here.

## Required integration order and cleanup

1. Existing need preparation, then escrow prepare and its positive prepared flag, before any payment.
2. Authoritative existing affordability/debit/authorization/PW binding, then exact escrow bind, frozen request fields, and the matched U1 return-authorization helper.
3. Accepted project work processing, then escrow measure on the same state.
After an actual transfer adoption, rebind only the escrow live context through its guarded adoption helper before measuring or settling as the successor.
4. On terminal success/failure/cancellation/recovery, set exact request fields and the parent-authorized retirement intent, then settle before changing type, authorization, required work, actual work, or paid-plan identity.
The parent owns stopping the paid project's future progression and exact slot retirement.
5. Consume the fresh settlement or matching durable settlement acknowledgment, then clear project/selection/temporary treatment data through the parent's existing helpers.
6. Preserve escrow funding/settlement history and pending rows.
The existing PW paid receipt and payer/site/auth/action witness must remain intact until settlement consumes the funding.
Do not call unpaid discard on a payment that may have occurred.
A failed post-debit bind needs exact pending-preparation recovery and cannot be replaced by a generic cost refund.

There are intentionally no new shared call-site edits in this delegated scaffold.
The parent explicitly requested review before wiring.
The pending lasting-capacity prerequisite/closing transaction is separate and is not implemented by this sidecar.

## References and validation limits

Primary sections read through the confirmed MCP reference routes: installed effects add_manpower 1468-1476, add_fuel 1388-1396, add_equipment_to_stockpile 1252-1266, modulo_variable 4999-5011, divide_variable 3609-3615, round_variable 6486-6495.
Installed effects revision: `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Offline Effects 1075 and 1718 use revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
Offline Data structures variable operations/types use revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Script Constants concept/schema were read with revisions `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` and `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
The payer scope contract follows offline Scopes PREV usage and the installed decision ROOT/FROM contract.
Exact source lookup of `great_depression_pay_action_cost` returned helper revision `20b47f810126de7f8e98485f9827744778755b10b50c7f6039d79c095a8ad9ef`.
Native GRE scripted effects 193-198 supplies an explicit divide-variable precedent.
The targeted reference read outside the selected one-line modulo section was rejected and corrected using its actual section line.
The initial context omitted Localisation, which remains presentation-owner coverage outside these non-visible helpers.
The parent has accepted the quantity-level material-return policy within U1.
Native docs and offline wiki do not establish a manpower mobilization anchor, fuel-cap delivery proof, or concrete train version/producer provenance for this existing debit.

Production source tests and native partial checker results are recorded in the assigned handoff.
No helper is replaced by a no-op fixture.
No HOI4 execution, live refund outcome, save/reload behavior, AI probability audit, CIV integration or whole Event 35 completion is claimed.
No new icons, localisation keys or visual assets are introduced.

