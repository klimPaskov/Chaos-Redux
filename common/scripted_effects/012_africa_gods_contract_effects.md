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

The twelve-factor final grader consumes this exact denominator and recovery streak, together with measured paid quantities and the frozen material obligation.
The accepted implementation and native acceptance limits are recorded in `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_full_grading_rewards_design_2026-10-03.md`.
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

## Owned agreements and treaty breaches

A treaty breach is recorded only when an owned agreement is broken.
The agreement kinds are `gods_of_africa_agreement` in `012_africa_gods_contract_constants.txt`: `tribute_terms = 1`, `protection_compact = 2`, `reconciliation = 3`, and `victor_renewal = 4`.

| Helper | Scope and inputs | Behaviour |
| --- | --- | --- |
| `gods_of_africa_mark_contract_agreed` | Participant with an open contract ledger | Sets `gods_of_africa_contract_agreed` and binds `gods_of_africa_contract_agreed_id` to the ledger ID. Called when a partial payment succeeds, when an extension is granted, and when Africa accepts a substitute. |
| `gods_of_africa_clear_contract_agreement` | Participant | Clears the agreed-terms receipt; called when a contract ledger opens, in `gods_of_africa_clear_demand`, and in participant cancellation after terminal retirement. |
| `gods_of_africa_record_treaty_breach` | Participant; temporary `gods_of_africa_treaty_breach_kind` (agreement kind) and `gods_of_africa_treaty_breach_war` (one when war broke it) | Increments `gods_of_africa_treaty_break_count` once, sets `gods_of_africa_unresolved_treaty_break`, `gods_of_africa_prior_treaty_break`, and the `gods_of_africa_broken_treaty` floor cause, stores `gods_of_africa_last_treaty_breach_kind` and `_day`, ends the broken agreement (a war ends all of them), writes one `treaty_break` history row, and applies `gods_of_africa_wrath.treaty_breach_magnitude`. Both temporary inputs are reset to zero. |
| `gods_of_africa_observe_agreement_war` | Participant, from `gods_of_africa_refresh_participant_floors` | Clears the per-war dedupe flag at peace; at war with Africa with a live compact, reconciliation, or renewal and no Wrath gain yet recorded for this war, records one war breach when the participant attacked (`gods_of_africa_participant_is_aggressor_against_host`), otherwise ends the agreements through `gods_of_africa_end_agreements_for_host_war`, and fires `chaosx.nr12.616` (host variant when Africa attacked). |
| `gods_of_africa_select_live_agreement_kind` | Participant | Sets temporary `gods_of_africa_live_agreement_kind` to the live compact, reconciliation or renewal (that priority), or zero. |
| `gods_of_africa_end_agreements_for_host_war` | Participant; caller sets temporary `gods_of_africa_ended_agreement_kind` | Africa attacked: withdraws protection, ends the reconciliation and renewal without a breach, clears agreed contract terms, sets the per-war dedupe flag, records `agreement_ended_by_host` history and `gods_of_africa_last_ended_agreement_kind`. |

Triggers in `012_africa_gods_contract_triggers.txt`: `gods_of_africa_contract_is_agreed`, `gods_of_africa_victor_renewal_agreement_is_live`, `gods_of_africa_participant_has_live_agreement`, and `gods_of_africa_participant_needs_reconciliation` (defiance or an unresolved breach).

## Cancellation of temporary terms

`gods_of_africa_cancel_participant` executes on the cancelled participant through the historical-receipt wrapper during host loss or residual original-host recovery cleanup.
Participant archival and participant capitulation have separate cleanup owners; this helper is not their entry point.
It first retires the interrupted contract and releases its frozen original-host slot through their one-use receipts.
It then calls the existing agreement, diplomatic-term and instalment-term cleanup helpers.
This removes the signed instalment schedule and amount, named-state demand array, named enemy and support-kind flags, and agreed-terms marker without changing contribution totals or historical contract outcomes.
Private ease/burden flags, armour quotes, payment credit and affordability requirements are cleared with the cancelled demand.
The native demand mission is removed when `has_active_mission` confirms it exists, even if its private active flag is already absent; installed `remove_mission` does not run completion or timeout effects.
Cancellation schedules no next-demand cooldown and never transfers material or applies punishment.
The recovery wrapper retains its existing historical settlement and victor receipts independently of these temporary terms.
Calling cleanup again cannot close another contract or debit another host slot.

No new inputs, defaults, constants, icons, localisation or public fields are introduced.
Usage remains `gods_of_africa_cancel_participant = yes` in the existing bounded owner cleanup; do not call the normal demand cooldown owner to cancel authority.

The refusal, failure, wartime-cancellation, and defiance owners read `gods_of_africa_contract_is_agreed` before closing the ledger, then call the breach recorder instead of applying their ordinary Wrath gain.
`gods_of_africa_mark_offender` keeps its offense and punishment-priority behaviour and never sets `gods_of_africa_broken_treaty`.
`gods_of_africa_complete_reconciliation` clears only `gods_of_africa_unresolved_treaty_break` and `gods_of_africa_broken_treaty`, keeps the count and the prior-breach flag, and sets `gods_of_africa_reconciliation_agreement_live`.
Example:

```
set_temp_variable = { gods_of_africa_treaty_breach_kind = constant:gods_of_africa_agreement.tribute_terms }
set_temp_variable = { gods_of_africa_treaty_breach_war = constant:gods_of_africa_value.zero }
gods_of_africa_record_treaty_breach = yes
```
