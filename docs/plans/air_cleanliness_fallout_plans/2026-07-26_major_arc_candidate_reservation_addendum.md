# Fallout major-arc candidate reservation addendum

Date: 2026-07-26

Status: accepted for dormant reservation-substrate implementation with a Year Zero stage-consumer pilot. This addendum does not authorize scheduler activation, a new event range, or release-floor credit.

## Scope

The reviewed candidate producer carries four major-arc rows, but the selector previously rejected the entire class. This tranche routes a proven top-level candidate into the existing capped major-arc ledger and wires the existing Year Zero chain as the first dormant stage consumer. Orchard Flowers, Skilled List, and False Spring Losses remain reservation-only. No new event ids are created.

## Contract

The candidate id is the immutable arc identity and cleanup token. A row must be a top-level major arc with no parent arc ticket, a current candidate row, a valid actor shape, and a current target when an actor or target is authored. The selected control mode and visible-budget cost remain frozen in the arc ledger. The existing `fallout_event_reserve_major_arc` API remains the only writer and retains exact retries, three-slot capacity, actor uniqueness, identity uniqueness, current owner checks, and rollback on structural mismatch.

The major-arc row begins at the existing `opening` stage. The Year Zero consumer uses the separate `major_arc_stage` dispatch source, authenticates human token `401` or hidden-AI token `402`, advances conflict, choice, delayed result, consequence, callback, and cleanup stages, and releases the same arc identity after delayed cleanup. It does not create an ordinary receipt. The dedicated proof is `FALLOUT_YEAR_ZERO_MAJOR_ARC_STAGE_PILOT_PROOF.md`. The other three rows still require authored stage consumers.

## Selection integration

`fallout_event_candidate_row_is_eligible` admits a major row only through the top-level payload proof. `fallout_event_commit_selected_candidate` routes major rows to the major-arc wrapper, keeps the ordinary cooldown and selection memory, and skips ordinary receipt reconciliation and ordinary dispatch for the accepted arc reservation. Relationship rows continue through their separate bilateral path.

All four major rows remain dormant behind the unset activation flags. The Year Zero path reuses its existing event ids, transaction key, route, Event Log history, and cleanup assets. No new event id, transaction key, route, Event Log history, or activation setter is added. The reviewed count remains 460 defined blocks and 0 of 660 countable blocks.

## Validation evidence

Static review must confirm balanced Clausewitz blocks, no new ids, no ordinary wrapper call on the major branch, exact identity and actor fields, the existing three-slot cap, major-stage token matching, Year Zero stage progression, and no scheduler activation setter. This addendum does not claim runtime save, multiplayer, host-authority, or live scheduler presentation proof.
