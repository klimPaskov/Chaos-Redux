# Event 012 unique tribute contract ledger

Purpose: record genuine contract issuance and exactly one terminal result without treating partial payments, extensions, rejected substitutes, report acknowledgements, or reconciliation expiry as completed tribute.
Scope: all helpers execute on the participant country.
No helper creates a public meter, price, timer, world scan, or live membership.

`gods_of_africa_initialize_contract_history` is called before the history marker and counter in the first-genuine-history branch of `gods_of_africa_initialize_participant_history`.
It initializes the unique issued/retired/fulfilled/full-original/honored-substitute/failed/refused/war-broken counts, current and longest streak, accepted reconciliation count, and three post-reconciliation counts.
Existing history without these receipts is not backfilled, even when its coarse history count is zero.
Re-entry and cleanup retain these fields.

`gods_of_africa_open_contract_ledger` requires initialized contract history and the fully committed live demand.
It requires a future current demand on the active host, copies origin, host generation, demand ID, and original family, and increments issuance once.
A matching last-closed tuple cannot be reopened.
Substitute review changes the payment family but leaves this original-family receipt intact.

`gods_of_africa_close_contract_ledger` requires an open, unconsumed receipt, matching native demand ID and generation, the durable history origin, and an explicit caller-set temporary `gods_of_africa_contract_close_kind`.
Valid values live in `constant:gods_of_africa_contract_close`.
Fulfillment additionally requires the one-use authorization written only by a successful full-payment resolver or the zero-balance partial resolver; a stale partial success alone cannot close a remaining balance.
The helper consumes permission and freezes the terminal tuple/day/kind before updating exactly one outcome count.
Full-original and honored-substitute outcomes both increase fulfillment and streak; adverse failure/refusal/war outcomes reset the current streak; neutral retirement removes the contract from the denominator without resetting either streak or manufacturing a payment.
Longest streak is retained through the documented variable clamp.
Neutral retirement deliberately does not require a current active host because loss, archival, and final cleanup operate after authority has ended.

`gods_of_africa_retire_open_contract` supplies the neutral-retirement enum for an existing open receipt.
Real payment/refusal/expiry/war/defiance owners close first, so their subsequent ordinary cleanup cannot relabel the outcome as retired.
Archival and unifier-loss cleanup retire before clearing native demand fields.
The one-use final classifier retires an open contract before its classification snapshot; final cleanup repeats retirement only inside its committed-outcome guard, where the consumed receipt makes it inert.
A last-unit partial payment that leaves no balance also closes once and clears its native mission.

`gods_of_africa_record_accepted_reconciliation` is called while the existing paid offer and host consent are still valid.
It increments the actual accepted-reconciliation count, resets the current recovery streak and post-reconciliation counters, and preserves lifetime outcomes and longest streak.
The actual paid-offer owner advances a durable per-participant sequence, and the acceptance helper consumes that sequence before incrementing counts.
The existing bilateral effect consumes the paid-offer flags immediately afterward; replaying the helper for the same offer cannot count acceptance twice.
Report presentation, rejected offers, expired offers, and personal victor authority renewal do not invoke this helper.

Usage from the ordinary participant response surface:

```text
gods_of_africa_resolve_full_compliance = yes
```

That canonical resolver validates identity, executes the actual payment owner, and supplies the one-use fulfillment authorization before terminal closure and cleanup.

The native mission failure owners require a present current deadline that has actually elapsed before they modify Wrath, history, or contract state.
An old timeout cannot consume a replacement contract's future deadline.

References: installed `documentation/effects_documentation.md:2695?2712` explains variable clamp order and dynamic bounds (revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`); the offline Data structures page documents ordinary country variables and temporary variables, and the existing Event 012 lifecycle and demand owners supply the integration precedent.
Source cases and independent review belong to `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_contract_audit_2026-10-03.md`.
Native execution and full grading/material payout remain separate acceptance work.

Future work: consume this exact denominator and recovery streak in the accepted twelve-factor final grader, and combine genuine paid-quantity receipts with the frozen material obligation.
No additional icons or visual assets are required by these private records.

## Audit corrections and slot ownership

Opening and accepted reconciliation additionally validate immutable history owner/origin; accepted reconciliation requires a positive issued offer sequence.
Economic response owners validate the ledger before transferring, and terminal owners consume their receipt before Wrath, history, opinion, or report writes.
The partial affordability gate permits its positive payment to equal the final remaining unit, making terminal partial closure reachable.
Native victor capture closes an existing wartime contract before applying permanent exemption.
Archival and host-loss cleanup give a provable current war against the frozen original demand host priority over neutral retirement, without applying punishment after authority ends.

Each genuine native contract captures `gods_of_africa_demand_host`, its ID, and origin alongside its generation, independently of report presentation.
`gods_of_africa_release_demand_slot` consumes a one-use release flag and debits only that stored country object when its identity and generation still match.
A replacement global host cannot lose one of its unrelated active slots, and repeated cleanup cannot debit twice.
All live host pointers are cleared with native demand fields; immutable terminal receipts and lifetime counts remain.
The contract closure enum has one owner, `012_africa_gods_contract_constants.txt`, with `.war_breach = 5`.

The native participant capitulation/annexation cleanup owner also performs interrupted retirement and frozen slot release before clearing its contract.
Interrupted war classification proves the stored host object's ID, origin, and generation before using war against that object as adverse evidence.
Ordinary reconciliation completion requires a present positive offer sequence at least as recent as its consumed acceptance; this permits the genuine recorder-first/completion-second case and rejects missing, zero, or older envelopes before pardon.
