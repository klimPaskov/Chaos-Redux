# Event 021 disabled-stage scheduler resolution

Disposition: implemented in source on 2026-10-04; live confirmation pending.
This note resolves the disabled-evolution finding EV21-DISABLED-01 in `event021_date_units_probability_audit_2026-10-03.md`.

`event021_parent_process_evolution_schedule` now checks `is_current_evolution_enabled` for each stage before sampling or dispatch, clears a stale due date for a switched-off stage, and lets later stages proceed when an earlier stage is recorded or switched off.
The core and parent apply effects no longer switch on a disabled earlier stage.
The policy and its basis are recorded as D4 in `../agent_decisions_2026-10-04.md`.
No MTTH value, weight, or timing constant changed, so the audit's numeric baseline is unaffected; the disabled case is now a skip rather than a repeated resample.
