# Event 016 pending-opening duplicate guard

Date: 2026-08-03

## Scope

This follow-up closes the fire-once scheduler window exposed by the dormant-holder loader repair. It changes only the automatic availability trigger and does not alter appointment rewards, referral recipients, project history, models, or CBRN behavior.

## Finding

The shared dispatcher sets `brilliant_scientist_opening_chain_active` and `brilliant_scientist_prefire_opening_pending` before firing `chaosx.nr16.1`. The global `brilliant_scientist_event_resolved` flag is written only after the public or secret appointment commits. During a human referral, the dormant KRG holder is intentionally ignored, so an advancing scheduler could otherwise select another host while the recipient popup was still pending.

## Changes

- Added `brilliant_scientist_has_pending_opening_transaction` to `common/scripted_triggers/016_brilliant_scientist_triggers.txt`.
- The helper scans all countries for either dispatcher-owned pending flag.
- `brilliant_scientist_automatic_event_is_available` now rejects the fire-once selection while either flag exists.
- The existing appointment and forwarding effects remain responsible for clearing the flags after the current transaction commits or transfers.

## Validation evidence

- The Event 016 trigger file has balanced braces (`319/319`) and no unsupported `<=` or `>=` operators; the effects file remains balanced (`2485/2485`).
- The helper has one definition and one availability-gate reference. Direct source tracing confirms the dispatcher sets both flags before `.1`, appointment clears them after commit, and forwarding clears the old flags before setting them on the selected recipient.
- The focused read-only Event Inspector requests for `chaosx.nr16.1` and `.3` returned `status = ok`, no blockers, and zero blocking diagnostics, but both were workspace-partial and reused the analyzer's deferred helper/lifecycle inventory. They are recorded as tooling evidence only, not live acceptance.
- No HOI4 runtime was launched.

## Remaining boundaries

Non-KRG duplicate holders remain rejected by `brilliant_scientist_has_non_dormant_kruger_holder`, the dormant KRG history holder remains loader-safe, and the native CBRN callback, seven model packages, targeted transfer/cleanup scenarios, quantitative balance, and live campaign validation remain open.
