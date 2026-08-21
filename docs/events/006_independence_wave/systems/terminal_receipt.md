# Event 006 standalone transaction receipt

The standalone `chaosx.nr6.1` entry keeps one durable terminal receipt for the most recent Event 006 transaction.

The receipt is written after allocation, frozen execution, package setup, finalization, commitment, cancellation, or compensating rollback has reached its terminal branch.

It preserves the plan identifier, plan dates, terminal phase, last failure, finalization failure, rollback failure, chaos band, target and selected counts, sponsorship count, expected state count, and the prepared, activated, validated, initialized, instantiated, and transferred counts.

Outcome flags distinguish a committed incident, cancellation before mutation, failure after mutation, failure during finalization, compensating rollback, rollback completion, rollback failure, finalization failure, capital-restore failure, and optional-territory failure.

The receipt is diagnostic state only.

It does not open a decision category, mission, queue, pressure meter, cost, popup, report, or pre-event indication.

The previous receipt is cleared only when a new standalone root transaction begins, so a completed or failed transaction remains inspectable until the next manual entry.

No icons or sprites are required for this surface.

## Runtime ownership

`common/scripted_effects/006_independence_wave_execution_effects.txt` owns both the receipt reset and the terminal snapshot.

`events/006_independence_wave.txt` remains committed-only for the public `chaosx.nr6.2` report and does not display receipt fields.

The shared liberation coordinator continues to own plan lifecycle cleanup and ownership rollback.

## Future extension

If a dedicated diagnostic view is approved later, it should consume these durable receipt fields without changing the committed-only presentation gate or reintroducing a pre-event crisis surface.
