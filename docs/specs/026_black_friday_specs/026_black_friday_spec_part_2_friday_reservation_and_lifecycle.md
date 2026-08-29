# Friday reservation and lifecycle

## Lifecycle state machine

Event 26 uses one global state machine.

| State | Meaning | Pool status | History status |
| --- | --- | --- | --- |
| Unavailable | Chaos is below 200, the event is disabled, or it has already fired | No live weight | No new entry |
| Eligible | Chaos is at least 200 and the event is enabled and unfired | Normal fire-once weight | No entry |
| Reserved | The random picker selected Event 26 and the popup is waiting for Friday | Removed from selection | No entry |
| Active | Friday activation occurred and the discount snapshot is live | Removed from selection | One Event 26 history entry |
| Expired | The next daily tick removed the sale | Permanently fired | Existing history remains |
| Canceled | A pending reservation was canceled by an explicit event disable or terminal shutdown | Disabled or unavailable according to cause | No history entry |

Working identifiers may use names such as `black_friday_reserved`, `black_friday_active`, `black_friday_fired`, `black_friday_discount_basis_points`, and `black_friday_reservation_owner`. Final identifiers should follow the event-owned naming pattern selected during implementation.

## Eligibility before selection

The live-weight trigger requires all of the following:

- Event 26 is enabled.
- Event 26 has not fired.
- Event 26 is not already reserved.
- The global chaos value is at least 200.
- The shared event system is active.
- No terminal state has frozen ordinary event firing.

If the chaos value is below 200, Event 26 is unavailable and the Events list should show `N/A` in place of a misleading zero weight.

## Reservation transaction

Selection performs one atomic reservation transaction:

1. Confirm Event 26 is still eligible.
2. Set the global reserved state.
3. Remove Event 26 from live selection without setting its permanent fired state.
4. Preserve enough context to cancel or activate safely after save and reload.
5. Complete the current random-selection transaction.
6. Roll or continue the next event timer through the normal event-system path.

The reservation must be idempotent. Two player timers, two manual clicks, or two selection callbacks during the same date cannot create two reservations.

The reservation is not an event-history entry. It does not show the sale popup. It does not set the Event 26 fired count. It does not log Evolution I. It does not apply the discount.

## Event-system pacing

Event 26 creates two distinct moments, selection and activation. The implementation must avoid counting either moment twice.

### At reservation

- The random picker has consumed one selection result.
- The selecting timer is resolved through the normal timer path.
- The event does not increment `total_events_fired`.
- The event does not increment the fire-once fired count.
- The event does not add minor-event pressure.
- The event does not add dynamic major-event weight.

### At Friday activation

- Event 26 records one normal fire-once event.
- The fired count, history row, minor-event pressure, and dynamic major-event gain are applied once.
- Activation does not reset or overwrite a timer that is already counting down from the earlier reservation transaction.
- Activation does not create a second random selection.

If the current event-system helpers cannot separate timer completion from fired-event accounting, implementation must add a narrow pending-event adapter. It must not approximate the behavior by treating reservation and activation as two events.

## Daily Friday check

The pending check belongs in the existing bounded global event-system pulse. It must not introduce a new daily whole-world country iteration.

The check runs once per in-game date and performs these steps:

1. Exit when Event 26 is not reserved.
2. Exit when the current weekday is not Friday.
3. Exit while chaos is below 200.
4. Exit when the event has been disabled after reservation, after applying the cancellation contract.
5. Exit when a terminal state has stopped normal events, after applying terminal cleanup.
6. Activate Event 26 once.

The direct selection path performs the same Friday and chaos check. This permits same-day activation when Event 26 is selected on Friday after the daily pending check has already run.

The implementation must verify the installed engine weekday trigger or weekday index against the offline wiki, Vanilla documentation, and a Vanilla precedent. The final code and documentation must use one shared Friday helper.

A qualifying chaos change that occurs later on a Friday must call the same narrow activation helper. A reservation that crosses from below 200 to 200 or higher after the normal daily check should activate that Friday, provided the event system is running. This hook belongs in the central chaos-change or tier-refresh path and must not add another recurring scan.

## Chaos changes while reserved

Reservation does not lock the chaos tier.

- If chaos falls below 200 before Friday, the event stays reserved.
- Every Friday below 200 is skipped.
- The event activates on the first later Friday at 200 chaos or higher.
- The 50 percent or 75 percent discount is chosen from chaos at activation.

A reservation created at 700 chaos can therefore activate at 50 percent if the world falls below 600 before the eligible Friday. A reservation created at 250 chaos can activate at 75 percent if chaos reaches 600 before Friday.

## Same-day Friday selection

When Event 26 is selected on Friday at 200 chaos or higher, it may activate during the same selection transaction. The sequence remains atomic:

1. Reserve the event.
2. Snapshot the current discount tier.
3. Mark the event fired through the delayed-event accounting adapter.
4. Broadcast the popup to human players.
5. Activate the shared cost source.
6. Start the one-day expiry.

The direct path must set the same flags, history data, evolution data, and expiry data as the pending Friday path.

## Disable and re-enable behavior

### Disabled before selection

The event has no live weight.

### Disabled while reserved

The reservation is canceled. The event remains unfired. No popup, history entry, pacing change, or discount occurs.

Re-enabling the event later returns it to the eligible fire-once pool when chaos is at least 200. The earlier reservation does not return automatically.

### Global event-system pause

A temporary pause of ordinary random-event processing preserves a valid reservation but blocks activation. Resuming the system on an eligible Friday calls the same activation helper immediately. Resuming on another weekday leaves the reservation pending. A terminal freeze is different and follows the cancellation contract.

Changing or disabling the selecting country's personal timer after reservation does not cancel the actorless global reservation. Annexation or tag change of that country also does not cancel it.

### Disabled while active

The active sale is allowed to finish its current one-day window. Disabling prevents future selection, which is already irrelevant for a fire-once event. It must not tear down a transaction in progress or create partial restoration.

## Manual trigger behavior

The ordinary manual trigger uses the same reservation and Friday rules as random selection.

Force Trigger Mode is a testing path. It may bypass the 200 chaos gate and Friday requirement, but it must still use the same activation, discount snapshot, coverage, expiry, log, and cleanup paths. A force-triggered run is flagged so it cannot satisfy the Event 26 achievement.

Force Trigger Mode cannot be used as proof that natural eligibility, random selection, Friday waiting, or chaos-tier selection works.

## Save and reload

The following state must survive save and reload:

- reserved or active state
- permanent fired state
- discount snapshot
- activation date and expiry date or timed-source state
- force-trigger disqualification
- achievement transaction-family progress during the active day
- any source-specific transaction ledger needed for refunds

A save loaded while reserved must continue waiting for an eligible Friday. A save loaded while active must retain the same snapshot and expire on the same next daily tick. Loading must not re-broadcast the popup or create another history row.

## Multiplayer synchronization

Event 26 has one global reservation and one global active state.

- A selection from any player timer can reserve the event.
- Other player timers continue normally.
- Another player cannot reserve Event 26 again.
- Friday activation broadcasts one synchronized informational popup to every current human-controlled country.
- AI countries receive the cost effect without a popup.
- The event history contains one actorless global row.
- A player who changes country during the active day receives the active status through the normal tag-switch refresh path.

The effect must remain deterministic for all clients. Cost quotations and payments must read synchronized global state and deterministic rounding.

## Terminal cleanup

If a terminal world state freezes ordinary events while Event 26 is reserved, clear the reservation without recording a fire. The normal event pool no longer matters after that freeze.

If the terminal state begins while the sale is active, remove the sale through the normal terminal cleanup or allow the timed source to expire immediately according to the shared terminal policy. The implementation must choose one consistent project-wide rule and record it. It must not leave a permanent discount in the terminal save.
