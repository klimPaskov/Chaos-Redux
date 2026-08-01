# Event 020 runtime surface handoff

Date: 2026-08-01

## Implemented tranche

The shared Emergency Countermeasure Drive now takes its civilian-factory reservation from `constant:black_plague_shared_cost.emergency_countermeasure_civilian_factories` and displays that same value in both available and blocked cost text. The mission continues to consume the shared support-equipment, motorized-equipment, and fuel bundle and retains its explicit cancellation cleanup.

SCN-012 setup-failure branches now clear the temporary port, selected-rat, internal-brood, and King-expansion event targets. They also clear the temporary scheduler-anchor target after a downstream postcondition failure, preventing a retry from inheriting an event target left by the failed transaction. Reservation flags and scenario arrays continue to be cleared by the existing failure cleanup.

## Validation evidence

- `hoi4.event_inspect` focused lint for `events/020_black_death.txt` returned `status: ok`, `blockers: []`, and zero blocking diagnostics. The tool deferred workspace-wide helper/lifecycle passes as an analysis limitation.
- Touched Clausewitz files have balanced braces and no unsupported `<=` or `>=` operators.
- `localisation/english/020_black_plague_response_l_english.yml` retains a UTF-8 BOM.
- Only the two live rat tags remain registered: `RTA` and `RTX`.

## Remaining limitation

The launch still does not have a full inverse transaction for disease state changes, territory transfers, evolution flags, or country activation if a postcondition fails after mutation. The UI now keeps that failure retryable and reports it explicitly; this handoff does not claim atomic rollback or live in-game validation.
