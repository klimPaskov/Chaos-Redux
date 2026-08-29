# Host resolution phase owner handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: bounded implementation complete in the owned phase helper and matching documentation; no commit was created.

## Owned surface

The only gameplay file changed is `common/scripted_effects/famine_migration_decision_phase_effects.txt`.

The matching helper contract is documented in `common/scripted_effects/famine_migration_decision_phase_effects.md`.

This handoff is the only plan surface changed, at `docs/plans/famine_and_migration_system_plans/subagent_handoffs/host_resolution_phase_owner.md`.

No decision file, achievement or corridor file, cohort core, localisation, mapmode, unrelated helper, constant file, or call-site file was edited.

## Helper and call-site map

The existing helper is `famine_migration_refresh_decision_phase_from_country` in `common/scripted_effects/famine_migration_decision_phase_effects.txt`.

Its existing call site remains `famine_migration_process_registered_displacement_country` in `common/scripted_effects/chaosx_famine_migration_effects.txt`, after cohort selection, displacement-load refresh, achievement reconciliation, and the sparse corridor pulse.

No new scripted effect or scripted trigger was introduced because the defect is local to the existing country phase projection.

The helper remains COUNTRY scope, receives no explicit arguments, writes only the existing phase flags, and uses the existing regular event target `famine_migration_decision_phase_country` for the invoking country during the bounded effect chain.

## Defect and implementation

Before this patch, the reverse `global.famine_migration_cohort_ids` loop required each row id to equal `famine_migration_current_country_cohort_id` and then accepted only a persisted-owner match.

That owner-only selection excluded a foreign receiving country because destination binding intentionally preserves the original cohort owner while updating the aligned current-host and destination state fields.

The helper now uses the existing global `famine_migration_forced_transfer_live_ledger_arrays_are_aligned` predicate before examining every registry row, so any mismatch among the eight aligned array/count values fails closed without a country/world scan.

The legacy `famine_migration_country_cohort_selection_ambiguous` flag is no longer an outer phase gate because multiple valid live rows can legitimately make owner-side selection ambiguous.

1. The row status must be `active`, `destination_bound`, or `destination_bound_unsafe`.
2. The row amount must be greater than `constant:famine_migration_population.zero`.
3. The origin and authoritative `global.famine_migration_cohort_hosts` state scopes must pass `famine_migration_state_is_valid`.
4. A destination-bound row must also have a valid exact `global.famine_migration_cohort_destinations` state scope, so a missing or stale old-save destination cannot create a host match.
5. The persisted `global.famine_migration_cohort_owners` country is one match path.
6. The current `OWNER` of the authoritative current-host state is the second match path.
7. The helper sets one `famine_migration_decision_phase_row_country_match` boolean from the two paths and promotes one `famine_migration_decision_phase_live_cohort` boolean before breaking the same loop, so domestic owner-plus-host matches cannot double count.

The host identity is evaluated from the current state `OWNER` at refresh time, while `famine_migration_state_is_valid` still requires a valid current controller as part of stale-state safety.

The active status intentionally does not require the destination slot to be valid because the record contract uses the origin as an unbound destination placeholder until a real destination scope is entered.

## Constants, weights, and cleanup

No constants or tuning tables were added or changed.

The helper reuses `famine_migration_runtime.zero`, `famine_migration_runtime.one`, `famine_migration_runtime.array_index_increment`, `famine_migration_population.zero`, and the existing cohort-status constants.

No decision density, phase threshold, mission score, AI weight, random weight, or probability-bearing value was changed.

No event target lifecycle change is needed because `famine_migration_decision_phase_country` is a regular target saved and consumed within the existing effect chain.

No cleanup effect, flag, variable, array entry, or global target was added.

## Acceptance evidence

Foreign host scenario: a positive `destination_bound` row keeps an origin country in the persisted owner array, has valid origin, host, and destination states, and has a host state whose current `OWNER` is the receiving country; the host path sets the single row-match boolean, and positive reception load with clear crises permits active-to-resolution.

Unrelated-country scenario: a country that is neither the persisted owner nor the current `OWNER` of the authoritative host state leaves the single row-match boolean at zero, so the row cannot provide live evidence for resolution.

Domestic scenario: when the persisted owner and current host owner are the same country, both identity paths can match but only one row-match boolean and one phase-live promotion are used before the loop breaks.

Stale-destination scenario: a row with a destination-bound status and missing or invalid destination state fails the destination validity gate even if the persisted owner or host field is present.

Old-save active scenario: an `active` row may retain the origin placeholder in its destination slot, but it still requires valid origin and host state scopes and a positive amount before it can match.

Two-live-hosted-row scenario: two positive destination-bound rows with different persisted owners but valid aligned fields and the same receiving country as current host `OWNER` pass the alignment gate even when owner-side selection is ambiguous, and the first qualifying row supplies the one live-row proof needed for resolution.

The existing post-phase dormant guard remains safe for foreign hosts because it checks positive reception load before retiring a country that lacks a persisted owner row; that call site was inspected but intentionally left outside this bounded ownership surface.

## Validation and blockers

Source inspection confirmed that destination binding updates `global.famine_migration_cohort_destinations` and `global.famine_migration_cohort_hosts` together while preserving `global.famine_migration_cohort_owners`, and that the existing displacement-load helper already uses current host `OWNER` matching as the local precedent.

The touched scripted effect was structurally inspected after the patch, including the aligned-ledger predicate, reverse registry loop, status and positive-amount gate, origin/host/destination validity gates, current `OWNER` comparison, one row-match boolean, and single break path.

The matching markdown records the scope, inputs, outputs, side effects, no-icon requirement, stale-target behavior, current-owner semantics, and foreign-host/unrelated-country proof obligations.

The required supported probability inspection was attempted once with `mcp__hoi4_agent_tools__hoi4_probability_inspect`, adapter `decision_ai_will_do`, source `common/decisions/famine_migration_decisions.txt`, `refresh = true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`. The call produced no artifact and aborted after repeated approximately 30-second waits, so no probability or engine decision evidence is claimed and no further retry was made per the parent instruction.

No callable `chaosx_ai_probability_auditor` route or dedicated decision-inspection route was available in this runtime, so the required auditor evidence and probability comparison remain blocked by tool availability and timeout rather than substituted with source-only claims.

No Hearts of Iron IV process was launched; live runtime acceptance remains parent/user-owned.

## Risks and follow-up

The phase helper trusts the existing ledger contract that `cohort_hosts` is the authoritative current-host field and that destination binding/rebinding keeps it synchronized with the destination array; the destination validity gate protects missing or invalid stale rows but does not add a second world or state scan.

The country reconciliation helper remains owner-only for other country-level consumers by design, while this phase projection independently recognizes current foreign hosts and does not suppress valid multi-row ledgers because of that selector state.

Parent review should confirm the foreign-host and two-live-hosted-row scenarios in the live consumer; broader ledger repair remains outside this bounded patch.

Owned phase helper files are released for parent integration review.
