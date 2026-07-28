# Event 006 pre-wave crisis requester-loss repair - 2026-07-29

## Scope

This bounded repair covers only the Event 006 host-facing crisis queue. It does
not alter Random Events Mod, CBB/CBD/etc., or Soviet Collapse release content.

## Source change

`common/on_actions/006_independence_wave_crisis_on_actions.txt` calls the new
`independence_wave_recover_crisis_requester_loss` effect from `on_annex`. The
effect checks the annexed `FROM` country for the queued crisis requester flag
before the victim scope disappears. It clears the global queue, records a
requester-loss resolution and date, preserves the former host id, writes the
dedicated Event 006 history payload, and leaves state ownership unchanged.

The crisis constants now define `requester_lost` history payload `6006` and
central resolution values for queued, blocked, cancelled, requester-lost, and
committed outcomes. Successful execution sets the committed receipt; blocked,
cancelled, and requester-loss paths set the failure receipt. A new crisis clears
the prior outcome flags before opening another queue.

## Localisation and Event Details

`common/scripted_localisation/006_independence_wave_crisis_localisation.txt`
resolves the requester-loss cause, and the Event Details crisis selector accepts
the new payload. The player-facing cause states that the requesting host was
annexed before the synchronized release could be built and that ownership was
not changed.

## Validation boundary

The touched Clausewitz files are brace-balanced and use the existing Event 006
event-log helpers and vanilla `on_annex` scope convention (`ROOT` is the winner,
`FROM` is the annexed country). No game launch was performed. Live annexation,
queue recovery, and save/load evidence remain required before whole-event
completion.

## Remaining risk

If the requester is removed by a non-annexation engine path, the transaction
callback is not exercised; that edge remains a runtime evidence item rather
than a new periodic world scan.
