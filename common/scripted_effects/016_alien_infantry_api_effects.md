# Reusable Alien Infantry API

These public helpers run in `COUNTRY` scope and provide the shared contract for `alien_infantry`. Event 016, Event 019 provider 508, D’Rhondan sovereignty, Mengele, and future events must use these helpers instead of copying the unit template, production gate, or landing ledger.

## Contact receipts

Set `alien_infantry_contact_source_id` to one numeric source constant, then call `alien_infantry_grant_contact = yes` or `alien_infantry_revoke_contact = yes`. The API stores one receipt variable per source and derives the aggregate `alien_infantry_has_contact` state when any source receipt is positive. Revoking one source never removes another source’s entitlement.

The current source constants are `kruger_pact`, `mengele_expedition`, `event019_provider_508`, `dhrondan_sovereignty`, and `future`. A future event must add a source constant and receipt field before granting access; it must not reuse another event’s receipt.

Example:

```text
set_temp_variable = { alien_infantry_contact_source_id = constant:alien_infantry_contact_source.future }
alien_infantry_grant_contact = yes
```

Cleanup is idempotent, so a package teardown may revoke its own source unconditionally. It must never clear the aggregate flag or another source’s receipt directly.

## Landing eligibility and reservation

`alien_infantry_can_call_landing = yes` is a trigger-style helper for the normal decision path. It requires aggregate contact, a valid owned state target, at least 2,000 `alien_laser_weapon_equipment_1`, no pending landing, and no active landing cooldown. The decision reserves exactly 2,000 weapons immediately, saves `dhrondan_landing_state_id`, starts the seven-day landing mission, and sets the pending flag. If the selection becomes invalid before reservation, the API clears the saved state target and reservation metadata without debiting equipment. The normal landing completion calls `alien_infantry_spawn_landing_cohort = yes`.

`alien_infantry_spawn_landing_cohort = yes` creates exactly one locked `D’Rhondan Landing Cohort` and consumes exactly 2,000 laser weapons when the caller has not already reserved them. A successful ordinary landing records the state marker, persistent landing history, Alien Presence, Pact Strain, and the applicable cooldown, and inserts the state scope into the caller country’s sparse `alien_infantry_landing_state_registry` exactly once. The default cooldown is 30 days, reduced only by D’Rhondan landing-network upgrades. A failed or invalid state target clears the saved target and refunds the reservation; no stale state target may survive an invalid non-deferred call.

The D’Rhondan bootstrap may set temporary `alien_infantry_initial_force_mode = 1` together with batch mode and a positive sovereignty receipt. That branch still consumes one 2,000-weapon expedition store per cohort, suppresses ordinary pact-host telemetry, and does not start the normal cooldown.

## Event 019 provider transaction

Provider 508 remains the Event 019 family identifier. Its materializer sets `alien_infantry_event19_deferred_mode`, passes the engine deletion id and origin state, and calls the shared spawn helper. The materializer is guarded against re-entry while the deferred flag is set, so a repeated provider callback cannot create a second cohort. The shared helper debits the proven 2,000-weapon amount, records the persistent `alien_infantry_event19_deferred_debit_committed` receipt, and resets the country-scoped `alien_infantry_landing_spawn_succeeded` result. `chaos_unit_family_provider_508_event19_commit_landing = yes` uses the persistent receipt to apply the state history, presence, strain, cooldown, and landing callback after Event 019’s ledgers pass; it does not depend on a temporary value surviving a scripted-effect boundary. `chaos_unit_family_provider_508_event19_rollback_landing = yes` refunds only the proven debit after the engine cohort deletion is confirmed, then clears the deferred transaction state.

Event 019 cleanup calls `alien_infantry_revoke_contact = yes` with the provider 508 source id. This removes only provider 508’s receipt and is safe when the receipt is already zero.

## Country reconciliation

`alien_infantry_reconcile_country = yes` is the idempotent setup/reload helper. It recreates and relocks the landing template while any valid contact receipt remains, restores contact-gated laser production, and removes stale pending reservations and target metadata without changing unrelated contact receipts. It never grants human manpower, ordinary infantry equipment, or a free training path.

## Runtime invariants

- `alien_infantry` is inactive in the division designer and is never manually trainable or deployable.
- Every cohort uses only `alien_laser_weapon_equipment_1`; ordinary manpower and ordinary equipment are never consumed.
- One landing call creates one cohort, one state record, and one history increment after the owning transaction commits.
- State-targeted calls must use `dhrondan_landing_state_id`; callers must clear or let the API clear this target after completion, cancellation, expiry, or invalid ownership. The API owns the caller country’s sparse state-scope registry used by that country’s downstream consumers; callers must not maintain a second landing-state ledger. D’Rhondan reads only the current pact host’s country-scoped registry, so another provider’s landing cannot alter its revolt count, capital, transfer, or claims.
- Event 019 deferred mode is transactional. Do not call the provider materializer recursively or directly mutate the shared history ledger.
