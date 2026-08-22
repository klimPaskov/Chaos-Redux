# Event 019 provider 508 shared alien-infantry API handoff

Date: 2026-08-21
Owner: alien_api_runtime_recovery
Scope: Event 019 unit-family provider/family 508 only, plus the narrow DHR sovereignty bootstrap input required by the shared API.

## Accepted runtime contract

Provider and family ID 508 remain 508. Event 019 setup grants only `constant:alien_infantry_contact_source.event019_provider_508` through `alien_infantry_grant_contact`; the source receipt is 3. Provider 508 is spawn-only and uses the API-owned locked ten-battalion `D’Rhondan Landing Cohort`.

Each ordinary request validates the selected state and reserves/debits exactly 2,000 `alien_laser_weapon_equipment_1`, then materializes through `alien_infantry_spawn_landing_cohort`. Provider 508 does not charge human manpower, Infantry Equipment, Support Equipment, political power, command power, a training path, or a separate cohort sustainment ledger. The Event 019 administrative transaction remains provider-neutral overhead only.

Cancellation or failure refunds exactly one 2,000-laser reservation only when the API did not materialize a cohort. The API reservation cancellation path is idempotent, and the direct debit path refunds once after a failed materialization. Provider 508 has no three-battalion template and no manually deployable/editable formation.

## Changed runtime surfaces

- `common/scripted_effects/016_alien_infantry_api_effects.txt`: fixed cohort template, source-specific contact grant/revoke, eligibility, reservation/debit, materialization proof, exact refund, and the gated DHR initial-force branch. Ordinary success owns DHR telemetry and callback; bootstrap success does not.
- `common/script_constants/016_alien_infantry_api_constants.txt`: exact reserve/debit and reservation constants plus DHR cooldown tiers 30/24/18/12 days and AI factors 1.25/1.50/1.25/1.50.
- `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`: provider 508 registration, derivative setup/cleanup, spawn-only management, payment/refund transaction no-ops, and sustainment no-op. The runtime clear/rebuild path revokes source 3 without touching receipts 1/2/4/5.
- `common/scripted_effects/016_brilliant_scientist_aftermath_effects.txt`: removed the stale retired alien-interface formation deletion reference.
- `common/scripted_effects/019_infantry_spawn_generation_effects.txt`: provider 508 verifies the API-owned template, limits each Event 019 request to one API cohort, and routes materialization to the selected state through the shared API.
- `common/scripted_effects/019_infantry_spawn_ledger_effects.txt`: provider 508 resource obligation manifests are prevented from becoming Event 019 resource rows; the provider no-op clears the manifest. Component metadata remains descriptive only.
- `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt`: corrected the existing alien-infantry family alias.
- `localisation/english/019_infrantry_spawn_l_english.yml`: request/sustainment text reflects the shared 2,000-laser landing API and no separate cohort sustainment charge.
- `common/scripted_effects/016_dhrondan_focus_effects.txt`: removed the dead `dhrondan_paid_landing_request_ready` flag.
- `localisation/english/016_dhrondan_focus_l_english.yml`: documents ordinary DHR landing recovery tiers of 24/18/12 days.
- `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`: records provider 508 receipt, fixed cohort, exact cost, and removed legacy ledgers.
- `docs/events/016_brilliant_scientist/systems/alien_infantry.md` and `docs/events/016_brilliant_scientist/systems/016_dhrondan_focus_tree.md`: document receipt ownership, bootstrap behavior, cooldown tiers, and AI modifiers.

## Receipt lifecycle

The registration-country grant is retained because the registering country is the provider owner and must possess source 3 for provider unlock and shared API eligibility. Derivative setup is a separate country scope, so it grants the same source receipt to that derivative. Runtime package clear/rebuild revokes source 3 from the registering owner when that owner received it; derivative cleanup revokes source 3 from the derivative. All revocations use `alien_infantry_revoke_contact` with the source-3 token and leave sources 1/2/4/5 intact. No broad contact wipe is used.

## DHR sovereignty bootstrap contract

`alien_infantry_spawn_landing_cohort` honors temporary `alien_infantry_initial_force_mode = 1` only when `alien_infantry_landing_batch_mode = 1` and `alien_infantry_contact_receipt_dhrondan_sovereignty > 0`. In that exact branch it retains state validation, the canonical 2,000-laser debit, cohort creation, and success output, but skips `dhrondan_arrival_count`, `dhrondan_alien_presence`, `dhrondan_pact_strain`, `dhrondan_landing_history_count`, and `dhrondan_record_successful_landing`. Batch bootstrap also skips ordinary landing cooldown selection and does not consume the DHR cooldown flags. Paid ordinary landings remain unchanged.

## DHR cooldown and AI tuning

Ordinary DHR landings use the shared default cooldown of 30 days, reduced by active focus flags to 24 days for the landing network, 18 days for guarded descent windows, or 12 days for near-space secured; the last active tier wins. Every tier still uses the exact 2,000-laser cost and 7-day arrival reservation. The shared landing decision AI applies the documented network, reserve-priority, guarded-descent, and near-space factors (1.25, 1.50, 1.25, and 1.50 respectively). The one-time sovereignty batch does not set or consume these flags.

## Validation and MCP evidence

- Scoped search across owned runtime/docs/localisation surfaces found no dead landing-request flag, pre-migration provider token, retired formation label, or retired equipment identifier.
- Provider 508 wrapper inspection shows `can_train = 0`, `can_sustain = 0`, and no resource charge; `can_spawn` is enabled only through shared API eligibility/contact and a valid state.
- Source-3 call-site inspection found only the registration grant, derivative setup grant, runtime-owner clear revoke, and derivative cleanup revoke, all using `event019_provider_508`.
- Constants inspection confirms reserve/debit 2,000, reservation 7 days, and cooldown tiers 30/24/18/12.
- Touched English localisation files retain UTF-8 BOM.
- `git diff --check` completed without patch errors; its only output was Git's existing LF-to-CRLF warning for an unrelated skill file.
- `hoi4.event_inspect` was attempted for `chaosx.nr19.1`; it returned `EVENT_INSPECTED_PARTIAL` in workspace `mod_chaos_redux_ea3b2d67c2c0`, with inventory/full-report resources but no complete engine verdict in this bounded pass.
- `hoi4.probability_inspect` was attempted first with no arguments and then against `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:160`, candidate provider 508. It returned `PROBABILITY_SOURCE_INSPECTED` with zero resolved and one unresolved candidate. This is recorded as source/MCP evidence, not a false pass.
- `chaosx_ai_probability_auditor` was not callable in this runtime. The required probability evidence pass and any final MCP event/probability compare remain a parent/central-runtime blocker.

## Superseding transaction review

The final Event 016 completion audit supersedes the original deletion-identity concern. Provider 508 now copies the exact Event 019 deletion ID into a persistent country receipt, constrains automatic and scenario materialization to one cohort, suppresses inner commit while an outer same-tag transaction owns the package, defers history/cooldown/callback state until commit, and retains debit/deletion receipts across asynchronous rollback retries. A refund occurs only after Event 019 proves the exact package objects are absent.

The behavioral migration is accepted at source level. The remaining architectural limitation is that materialize/commit/rollback are private provider-508 branches rather than published generic registry callbacks; a future provider needing the same deferred external-resource transaction must extend the registry contract instead of copying those branches. Complete engine render/compare and live acceptance remain blocked separately.

No commit was made by the original provider worker.
