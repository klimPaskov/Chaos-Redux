# Fallout Callback Cleanup Order Proof

## Status

Static reconciliation complete for the dormant Last Inventory, River Intake at Dawn, and Rail Crew Twenty-Seven callback pilots on 2026-07-22. The chains remain dormant and add no release-floor blocks. Hearts of Iron IV was not launched.

## Ownership contract

The generic delayed-row reconciler now recognizes a resolved row as callback-held only when its cleanup token is the exact Last Inventory, River Intake, or Rail Crew cleanup token and the matching country-owned callback flag is present. A cancelled row is never held by this rule. Unrelated delayed rows continue to enter ordinary cleanup preparation.

The Last Inventory, River Intake, and Rail Crew result resolvers no longer mark the result row cleanup-pending before they schedule the callback. A callback scheduling failure marks the result row cleanup-pending immediately. A successful callback keeps the result row resolved while the callback row is pending.

The callback cleanup event first authenticates and removes its own delayed row. After that receipt succeeds, it prepares the exact stored result cleanup ticket and clears the callback hold only when that preparation succeeds. The result cleanup event then removes the result row. Final chain cleanup requires both release receipts, while the no-callback scheduling failure path still permits one result release.

## Static evidence

- `fallout_event_delayed_cleanup_is_deferred` checks the resolved status, the selected row cleanup token, and the matching callback flag for all three pilots.
- Last Inventory, River Intake, and Rail Crew result resolvers contain no pre-callback `fallout_event_prepare_delayed_cleanup` call.
- All three callback cleanup effects call `fallout_event_release_issued_delayed_cleanup` before preparing their exact result cleanup ticket.
- All three callback cleanup effects clear their callback hold only after the result cleanup preparation returns an accepted transaction.
- All five touched script files have balanced braces.
- The corrected River Intake signs remain pump authority `-0.06`, compact `-0.05`, and epidemic aftershock `0.10` for `supply_consumption_factor`.
- No activation setter, ordinary scheduler caller, zombie reference, em dash, or semicolon was added.

## Remaining runtime gates

Static source cannot prove save and reload retention, exact engine event ordering, multiplayer ownership, callback due-day delivery, dynamic modifier placement, Deaths accounting, event-log presentation, or scheduler performance. The pilots must remain dormant until those runtime surfaces and the full bilateral branches are reviewed.
