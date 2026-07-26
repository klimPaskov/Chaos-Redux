# Fallout major-arc candidate reservation addendum

Date: 2026-07-26

Status: accepted for dormant reservation-substrate implementation. This addendum does not authorize scheduler activation, a new event range, or release-floor credit.

## Scope

The reviewed candidate producer carries four major-arc rows, but the selector currently rejects the entire class. This tranche routes a proven top-level candidate into the existing capped major-arc ledger. It does not create an arc event consumer, stage event mapping, or new event ids.

## Contract

The candidate id is the immutable arc identity and cleanup token. A row must be a top-level major arc with no parent arc ticket, a current candidate row, a valid actor shape, and a current target when an actor or target is authored. The selected control mode and visible-budget cost remain frozen in the arc ledger. The existing `fallout_event_reserve_major_arc` API remains the only writer and retains exact retries, three-slot capacity, actor uniqueness, identity uniqueness, current owner checks, and rollback on structural mismatch.

The major-arc row begins at the existing `opening` stage. This tranche does not issue an ordinary dispatch envelope. A later authored arc consumer must map the identity and stage to its human or hidden-AI event token, advance the exact ticket, and terminalize cleanup through the existing arc wrappers.

## Selection integration

`fallout_event_candidate_row_is_eligible` admits a major row only through the top-level payload proof. `fallout_event_commit_selected_candidate` routes major rows to the major-arc wrapper, keeps the ordinary cooldown and selection memory, and skips ordinary receipt reconciliation and ordinary dispatch for the accepted arc reservation. Relationship rows continue through their separate bilateral path.

The current four major rows remain dormant behind the unset activation flags. No new event id, transaction key, route, Event Log history, or activation setter is added. The reviewed count remains 460 defined blocks and 0 of 660 countable blocks.

## Validation evidence

Static review must confirm balanced Clausewitz blocks, no new ids, no ordinary wrapper call on the major branch, exact identity and actor fields, the existing three-slot cap, and no scheduler activation setter. This addendum does not claim runtime save, multiplayer, host-authority, or authored arc-consumer proof.
