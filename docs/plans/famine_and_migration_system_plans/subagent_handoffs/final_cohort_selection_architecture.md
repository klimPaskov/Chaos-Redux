# Famine and migration multi-cohort selection architecture handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Handoff status

This is a read-only architecture audit for the shared famine and migration cohort ledger.

Only this Markdown handoff is added by this subagent; no gameplay, localisation, map, decision, mission, scripted effect, scripted trigger, on-action, or spreadsheet file was edited.

The current design is not safe for multiple live cohorts in one host state.

The recommended repair is a bounded per-action row selector backed by exact state/host reconciliation, while retaining the existing single-ID state and country variables only as derived legacy/display caches.

The selector must not silently replace cause, custody, original-owner, or physical-host identity with a different row merely because the state-level cache is ambiguous.

## Evidence and required references read

The audit read the current repository `AGENTS.md`, the complete `chaos-redux-state-ledgers` skill, the current `chaos-redux-subagents` skill, the famine and migration specifications, prompts, closure review, implementation map, resume packet, source-of-truth map, completion report, map validation, and existing subagent handoffs.

The relevant offline wiki pages read were `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`.

The relevant vanilla references read were `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, and `common/script_constants/documentation.md`.

The vanilla references confirm that event targets are single-scope pointers, regular targets are chain-local, global targets require explicit cleanup, aligned arrays are index-based, and `for_each_loop` or bounded `while_loop_effect` can inspect an existing registry without creating a world scan.

The vanilla documentation does not provide a cohort-specific multi-row selector precedent.

The Chaos Redux sparse aligned registry and exact transfer contract therefore remain the governing implementation pattern.

## Current ledger and pointer census

The live registry in `common/scripted_effects/chaosx_famine_migration_effects.txt` has eight aligned arrays.

| Row field | Current array | Meaning and identity rule |
| --- | --- | --- |
| Monotonic identity | `global.famine_migration_cohort_ids` | Stable cohort identity; array index is not identity. |
| Original state | `global.famine_migration_cohort_origins` | Historical origin and return target; it must not be used as the physical debit state. |
| Current host | `global.famine_migration_cohort_hosts` | The only state that may perform a later physical debit for this row. |
| Destination | `global.famine_migration_cohort_destinations` | Bound destination; the origin placeholder is valid only while status is `active`. |
| Persisted owner | `global.famine_migration_cohort_owners` | Original initiating owner/custody identity; it must not be overwritten by current host owner. |
| Survivor amount | `global.famine_migration_cohort_amounts` | Actual live survivor amount after the last accepted transfer. |
| Cause/source | `global.famine_migration_cohort_sources` | Durable cause identity used by reports, policy, and outcome logic. |
| Lifecycle status | `global.famine_migration_cohort_statuses` | Current lifecycle, currently `active`, `destination_bound`, `destination_bound_unsafe`, `completed`, `invalid`, or `none`. |

The aligned history ledger in `common/scripted_effects/famine_migration_cohort_history_effects.txt` has `global.famine_migration_cohort_history_ids` and `global.famine_migration_cohort_history_states`.

The history ledger records visits and cycle checks, but it does not replace the live row’s current-host proof.

The live-array alignment trigger is `famine_migration_cohort_history_live_ledger_arrays_are_aligned` in `common/scripted_triggers/famine_migration_cohort_history_triggers.txt`.

The global count is `global.famine_migration_cohort_count`, and the monotonic allocator is `global.famine_migration_next_cohort_id`.

The state-level cache is `famine_migration_current_cohort_id` with `famine_migration_cohort_selection_ambiguous`.

The country-level cache is `famine_migration_current_country_cohort_id` with `famine_migration_country_cohort_selection_ambiguous`.

Neither cache can represent more than one live row.

The country reconciler at `famine_migration_reconcile_country_cohort_selection` currently counts persisted-owner matches but does not fully filter status, positive amount, valid origin, valid host, or stale ownership.

## Append, bind, transfer, rebind, and cleanup paths

`famine_migration_initialize_runtime` currently clears the eight live arrays when the runtime flag is absent.

That behavior is unsafe for an old save that contains ledger rows without the current initialization marker and requires the migration behavior described below.

`famine_migration_record_displaced_cohort` appends one value to all eight arrays, records history, and sets the state and country single-row caches.

When the state already has a different cache id, the function clears `famine_migration_current_cohort_id` and sets `famine_migration_cohort_selection_ambiguous`.

This is the direct trigger for the reported second-live-cohort failure.

`famine_migration_bind_cohort_destination` updates destination, host, and status for one exact id from the actual destination state scope and records history.

It repeats the same single-pointer conflict behavior, but it does not reconcile or clear the old origin state’s cache.

`famine_migration_bind_cohort_destination_forced` has the same old-origin selector gap while changing the status to `destination_bound_unsafe`.

`famine_migration_rebind_cohort_destination_safe` updates only destination and host for a nonterminal row and preserves origin, owner, amount, source, and history.

It clears the old host cache only when that cache equals the row id, but it does not perform an exact old-host reconciliation when the old host contains another row or when the stale pointer came from the historical origin.

`famine_migration_resolve_cohort_origin` selects a requested id, or falls back to the state cache and then the country cache when no id was supplied.

Its explicit-id path currently returns origin, host, owner, amount, source, status, and destination targets without proving that the current state performing a physical debit equals the row’s persisted host.

`famine_migration_transfer_civilians_exact` correctly owns the single physical population debit, measures actual debit and actual destination credit, treats route deaths as a debit slice, and records conservation residuals.

It currently validates route proof and destination scope but does not itself require `FROM` to equal the persisted current host for an existing cohort id.

`famine_migration_update_cohort_host_after_transfer` updates host and survivor amount at the destination after a successful exact transfer.

It clears the row when survivor credit is not positive, but it also clears only the destination state’s cache and does not reconcile the pre-transfer state that may still contain the old id.

`famine_migration_cleanup_cohort_record` removes all eight aligned live arrays and the matching history rows for one exact id.

It does not repair every affected state and country pointer after removal.

`famine_migration_cleanup_cohort_records_for_state` removes rows whose origin, host, or destination matches the state and then unconditionally clears the state cache and ambiguity flag.

That broad cleanup must distinguish historical origin from current host so that an origin state recovering or changing control does not erase a still-live row hosted elsewhere.

The forced movement cleanup and decision terminal blocks also clear the current state cache directly instead of asking a surviving-row reconciler to select the remaining host row.

## Critical cross-transaction duplication finding

The physical debit owner is correct, but the current row identity contract is not sufficient to prevent a duplicate debit across transactions.

The failure sequence is:

1. A cohort is recorded in state A, so `famine_migration_current_cohort_id` is set on A.
2. A successful bind or spontaneous movement transfers survivors to state B and updates the row’s persisted host to B.
3. The old state A still retains the row id in its state cache because bind did not reconcile the historical origin selector.
4. A later state-targeted movement or return decision can select that stale id from A.
5. `famine_migration_resolve_cohort_origin` returns the row’s historical origin and amount, but the exact transfer effect does not prove that the physical debit scope is the persisted host.
6. A can therefore be debited again even though the live survivors are in B, after which the row can be rebound again and the physical population ledger is duplicated.

This is not only a UI ambiguity defect.

It is a conservation and custody defect.

Every existing-cohort debit must prove all of the following immediately before `famine_migration_transfer_civilians_exact` mutates population:

- the request contains one exact monotonic cohort id;
- the live arrays are aligned and contain exactly one occurrence of that id;
- the row status is live and the amount is positive;
- the row’s current host is valid;
- the physical `FROM` state is exactly the row’s current host;
- persisted owner identity is valid and policy ownership proof is still satisfied;
- the selected row’s origin is used only as a historical return destination;
- the route destination is valid and distinct from the physical debit state;
- request amount does not exceed the row’s actual survivor amount unless the action explicitly clamps it through the accepted transfer contract.

If the physical host proof fails, the transaction must return an invalid or stale-host result without changing population, Deaths, reception load, pressure, cohort amount, history, or route projections.

After every accepted bind, transfer, rebind, zero-survivor cleanup, or terminal cleanup, reconcile both the old host and new host state caches and the persisted-owner country cache.

The negative conservation scenario must explicitly attempt the stale-origin debit above and prove that actual origin debit, route deaths, survivor credit, reception delta, and cohort amount all remain unchanged.

## Recommended bounded architecture

Use the live row as the source of truth and treat state and country pointers as derived caches.

Do not expand the single state pointer into a second parallel pointer or choose a “current” row by overwriting cause or custody metadata.

Add a narrow selection layer beside the existing cohort helpers, preferably in the existing famine/migration scripted-effect and trigger files unless the owning implementer finds a clearly bounded existing selection file.

### Proposed helper map

The following names are proposed contracts for the parent implementation.

| Helper | Scope | Inputs | Outputs | Side effects | Required call sites |
| --- | --- | --- | --- | --- | --- |
| `famine_migration_cohort_registry_is_aligned` | Global/any trigger context | Eight live arrays, count, and optionally history alignment | Boolean only | None; alignment failure must fail closed | Every selector, resolver, transfer, bind, rebind, and cleanup entry point. Reuse the existing live-array alignment contract rather than creating a second registry. |
| `famine_migration_select_cohort_for_action` | State scope for state-targeted actions; country scope only for country phase or owner summaries | Action token, optional explicit id, current state or persisted owner, action proof, and current host requirement | Temporary result, selected id, selected array index, candidate count, ambiguity/stale/host-mismatch/alignment result | No population, reception, pressure, history, or row mutation; chain-local event targets may be prepared only after selection succeeds | The nine decisions listed below, corridor preparation, camp/custody adapters, decision phase, and any future row-specific caller. |
| `famine_migration_resolve_selected_cohort` | Physical host state or owner country before a route is prepared | Exact selected id, expected physical host state, optional owner/policy proof | Temporary amount, source, status, origin/host/destination event targets, persisted owner target, and exact row index | No mutation; regular event targets are cleared by the chain and must not be treated as durable identity | Replace direct current-pointer calls to `famine_migration_resolve_cohort_origin` in movement, return, resettlement, integration, and custody paths. |
| `famine_migration_selected_cohort_host_is_current_state` | State trigger | Exact id and live row index or resolved host target | Boolean | None | Mandatory guard inside `famine_migration_transfer_civilians_exact` and each physical movement adapter. |
| `famine_migration_reconcile_state_cohort_selection` | State scope | Current state and registry alignment result | State live-row count, optional derived cache id, and cache status | Sets or clears the state cache only as a projection; sets ambiguity only for the legacy/display cache; never deletes or mutates a row. | Record, bind, forced bind, transfer-host update, safe rebind, exact cleanup, invalidation callback, and old-save migration. |
| `famine_migration_reconcile_country_cohort_selection` | Country scope | Current country and registry alignment result | Valid owner-row count, optional derived country cache id, and cache status | Sets or clears the country cache only as a projection; filters stale/dead rows. | Existing registered-country processor, old-save migration, terminal cleanup, and owner identity changes. |
| `famine_migration_reconcile_cohort_selectors_after_mutation` | Any transaction owner with saved old/new state and owner targets | Old host, new host, original state if valid, destination if valid, persisted owner, removed-row id, and mutation result | None | Calls state reconciliation for every affected valid state and country reconciliation for the owner; never scans all world states. | Bind, transfer, rebind, zero-survivor cleanup, terminal cleanup, and control/annexation callbacks. |

The existing `famine_migration_resolve_cohort_origin` may remain as a compatibility wrapper only after it delegates to exact-id resolution and requires a valid selected row.

No caller may use a state or country pointer as a durable cohort identity.

### Selection inputs and result semantics

An explicit id is always preferred.

An explicit id that is missing, duplicated, stale, dead, misaligned, owned by the wrong actor, or hosted outside the physical action state returns `invalid`, `stale`, `duplicate`, or `host_mismatch` and does not fall back to another row.

Without an explicit id, the selector scans only the bounded global registry and filters rows by current host, positive amount, live status, valid origin/host/destination scopes, persisted-owner validity, and the action-specific proof.

The selector must count exact matching rows rather than breaking on the first matching array index.

Array compaction cannot change a row’s identity because the monotonic id, not the index, is retained in every contract and mission variable.

### Deterministic priority and ambiguity

Use the following semantic priority in order:

1. Explicit requested id.
2. Exact current-host match to the action’s state scope.
3. Action-specific lifecycle status preference.
4. Action-specific route, reception, custody, owner, and policy proof.
5. Positive survivor amount, with the larger amount preferred only where the action is amount-insensitive and the player-facing surface explains the choice.
6. Lowest monotonic cohort id as the deterministic display or state-projection primary row.

The final id tie-break is allowed for a map/report primary projection and for state-wide actions that do not mutate a specific row.

It is not sufficient authority for a population-changing or outcome-changing action.

For a row-specific mutation, a unique top semantic candidate is required.

If multiple candidates remain at the top semantic rank, return `ambiguous_action` with the valid candidate count and no selected mutation id.

Ambiguity is action-local, not a permanent state-wide disable.

The state-level legacy flag may remain set when more than one live host row exists so old un-migrated callers fail closed, but migrated callers must invoke the action selector and receive an honest row-specific result.

If the current decision surface cannot present an explicit row choice, it must show a truthful multiple-cohort tooltip or leave the row-specific action unavailable for that transaction; it must not route the lowest id silently when causes or custody differ.

State-wide border policy can remain available when at least one eligible live host row exists because the policy changes the state, not a particular cohort.

### Action-specific eligibility

| Consumer | Required selected-row condition |
| --- | --- |
| `fm_close_border` | State-wide action may use a valid positive host-row count and need not mutate one row. If a later closure outcome records a cohort, capture one exact id at that later transaction boundary. |
| `fm_negotiate_corridor` | One exact row hosted in the targeted state, positive amount, live status, valid controller/owner/corridor proof, and trapped/flight pressure relevant to the contract. Save the id into the corridor contract before any offer or mission. |
| `fm_distribute_arrivals` | One exact row hosted in the targeted state, normally `destination_bound` or `destination_bound_unsafe`, positive amount, valid reception state and owner ledger, and the distribution policy proof. |
| `fm_transit_only` | One exact row whose current host is the physical `FROM` state, positive amount, live status, valid foreign transit destination, and route proof. The exact transfer must run in the persisted host scope, never in the historical origin merely because the old origin cache still contains the id. |
| `fm_enforce_closure` | One exact positive live row hosted in the targeted state with closure and forced-return policy proof. The historical origin may be the return destination but can never be the debit scope unless it is also the current host. |
| `fm_local_integration` | One exact `destination_bound` row hosted in the targeted state, valid owner/custody identity, integration capacity and policy proof, and a terminal outcome that does not create population. |
| `fm_third_country_resettlement` | One exact `destination_bound` row hosted in the targeted state, valid safe neighbor/reception capacity, route and actor proof, and a rebind that changes only destination and host metadata. |
| `fm_voluntary_return` | One exact live bound row hosted in the targeted state, valid safe original state and return route, and host/owner policy proof. The transfer debit must prove physical `FROM` equals current host. |
| `fm_forced_repatriation` | One exact live row hosted in the targeted state, valid unsafe-host and policy proof, valid original state target, and explicit route-death slice. Deaths remain a slice of one measured debit. |

The `famine_migration_decision_phase_effects` country phase should count valid live rows and remain active when multiple owner rows exist.

It must not treat the current country pointer as the only row that can drive phase state.

The `famine_migration_adapter_effects` custody helper and generic camp decisions must use the same exact-id and current-host proof.

## Host, destination, origin, and ownership rules

`origin` is historical provenance and the default return target.

`host` is the physical state holding the current survivor amount and is the only allowed debit scope.

`destination` is the state bound by the last accepted destination or resettlement contract.

`owner` is the persisted initiating owner/custody identity and must remain unchanged across movement, bind, rebind, integration, resettlement, and return until the row reaches its terminal outcome.

The current owner of the host state may be consulted for reception capacity, controller, border, and policy proof, but must not overwrite `global.famine_migration_cohort_owners`.

Every physical transfer must carry a regular event target for the destination and a chain-local target or exact id for origin/host/owner.

The transfer helper must reject an invalid event target rather than applying a fallback state.

No global event target is necessary for this selector.

If a future mission genuinely outlives one effect chain, store its exact monotonic id and subject state in durable normal variables and clear them on mission success, expiry, invalidation, control loss, or owner removal.

## Reconciliation and cleanup contract

`famine_migration_reconcile_state_cohort_selection` should count only rows whose current host equals the state, whose status is live, whose amount is positive, and whose host and persisted owner are valid.

An active row whose destination field equals the origin placeholder must not be counted as destination-bound, but it may be counted as a live host row for an origin-state action.

When the count is zero, clear the state cache and ambiguity flag.

When the count is one, set the state cache to that exact id and clear ambiguity.

When the count is greater than one, clear the legacy cache and set the ambiguity flag while writing a state-local live-row count and selector status for map/report consumers.

The state reconciler must never remove a live row.

Country reconciliation should apply the same live-row filters, then count persisted-owner matches for country-phase summaries.

It may set a country display primary id only when exactly one valid owner row exists.

When more than one valid owner row exists, clear the country cache and set country ambiguity for legacy callers while leaving the country phase and action-local selectors operational.

On a successful bind from old host A to destination B, save and reconcile A before or immediately after the row update, then reconcile B and the persisted-owner country.

On a successful transfer from old host A to destination B, update the row only after actual survivor credit is measured, then reconcile A and B and the owner.

On safe rebind from A to B, reconcile A and B even though population does not change.

On zero survivor credit, capture origin, old host, destination, and owner targets before removing the row, remove all eight aligned arrays and the matching history rows, then reconcile each still-valid affected state and country.

On exact terminal integration, returned, resettled, completed, or invalid cleanup, clear the row only through the explicit terminal transaction and reconcile surviving rows instead of unconditionally clearing the state.

`famine_migration_cleanup_cohort_records_for_state` should not erase a live row merely because the historical origin matches the cleaned state.

If the current host state becomes invalid and there is no approved rebind path, the owning invalidation transaction may retire that row, but it must first preserve the row’s id, cause/source, original owner, host, amount, and cleanup reason in the existing terminal or outcome ledger.

If only the original state recovers, is annexed, or changes controller while the host remains valid, preserve the live row and mark only return eligibility as invalid when the return target is no longer valid.

## Corridors, missions, reports, and map context

`famine_migration_prepare_corridor_contract` currently falls back to `famine_migration_current_cohort_id` when no explicit corridor id is supplied.

That fallback must be replaced with a successful action-local selection before contract preparation.

The exact selected id must be copied into `famine_migration_corridor_cohort_id`, the offer mirror, and `famine_migration_mission_corridor_cohort_id`.

Corridor acceptance, route binding, evacuation, reception credit, and mission completion must revalidate that exact id and current host rather than selecting a replacement row from the state.

If the selected row dies, is terminally resolved, or becomes invalid before the mission completes, close that mission as an invalidated obligation and do not silently substitute another cohort.

The six current mission families in `famine_migration_decisions.txt` and the corridor mission state must carry the exact row id when the objective is row-specific.

Mission subject state and mission flags alone are not sufficient identity when multiple rows share a host.

Report and event-detail state should snapshot the exact id, source, origin, host, destination, owner, and outcome at the transaction boundary.

The shared report header may show a state-level multiple-cohort status without exposing private ids to unauthorized viewers.

The existing map localisation at `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt:742-743` currently emits exact versus ambiguous from the single pointer.

It should consume transaction-time state projections such as a valid live-row count and selector status rather than scanning the global arrays from map refresh.

The primary map projection may use the lowest id as a deterministic display row, but the tooltip must say when multiple live cohorts share the host and must not imply that the primary row is the only row.

Exact amounts, causes, owner identity, and outcome totals remain restricted to the existing owner/controller or authorized report context.

The successful read-only map inspection produced this artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d5440b986381907e75c247a65a40c9a1405bf6f44f2329d29e562caed2bf9df/00e1977afa42c7cffa91e1189152fc1f525852e70ce87d1900e518fd40f693f1/map-inspect.cda612cbd4957210.json`

The map inspection validated state membership, adjacency, supply, and railway data but reported a failed map-position/port-locator check with `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics for existing `mod:map/buildings.txt` entries.

Those diagnostics are outside this cohort-selection architecture and were not edited or treated as selector evidence.

## Old-save migration and initialization

`famine_migration_initialize_runtime` must stop clearing non-empty live arrays merely because `famine_migration_runtime_initialized` is absent.

The proposed load-time path is:

1. If all eight arrays are absent, initialize empty arrays, count zero, and the next id constant.
2. If any live array exists, verify all eight lengths equal the id-array length and the stored count equals that length.
3. Verify ids are positive and unique, statuses are known, amounts are positive for live rows, and origin/host/destination values are valid for their status.
4. If the arrays are aligned and valid, preserve every row and set the next id above the maximum persisted id.
5. If arrays are partially missing, misaligned, contain duplicate ids, or contain an unknown live status, set a registry-migration-blocked result and fail closed for movement and outcome actions.
6. Do not infer a destination from an invalid target and do not convert a stale host to the origin automatically.
7. Reconcile each row’s host state and persisted-owner country by iterating the existing registry rows only; this is bounded by ledger size and is not an `every_state`, `every_country`, or world scan.
8. Validate old state and country cache ids against one exact live row and matching host or persisted owner; clear stale pointers, repair a unique row, and preserve ambiguity when more than one valid row remains.
9. Preserve the history arrays only when their two arrays and count are aligned; otherwise block cycle-sensitive actions and retain the live row identity for review.

No old-save path may silently debit, credit, move, kill, duplicate, or remove a row while rebuilding selectors.

## Constants and tuning-table plan

Do not add balance weights to this repair.

The existing `common/script_constants/famine_migration_constants.txt` is the appropriate shared location for selector result/status codes if the implementation needs them.

Add only semantic constants such as selector results `none`, `unique`, `ambiguous`, `stale`, `duplicate`, `host_mismatch`, and `alignment_broken`, plus action/status rank identifiers if the engine requires numeric comparisons.

Reuse the existing `famine_migration_runtime` zero/one/index constants and `famine_migration_cohort_status` values rather than introducing magic numbers.

Do not use the existing destination-selection weights for cohort-row selection.

The destination state selector is a separate weighted neighbor-state system in `famine_migration_destination_selection_effects.txt` and must remain responsible only for choosing a legal destination state.

The probability source inspection for that file succeeded with source hash `4d7797526b0f9379745510b08265308d96b2582ccb7f2c33bde973efe56b697e` and artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00d74be1796afeddb3d3ba649c56107b17c1f3b756c649d2de62cbdc85ba4dbb/a4e9eb119d98642893df2d77bc6c0cf13b0d19407154e33983ddb7b0869db211/probability-inspect-4d7797526b0f.json`

That inspection reported `poolComplete = false`, zero discovered candidates, and no available custom weighted-pool adapter inputs for a scenario evaluation.

No probability balance target was changed, so no baseline/post probability comparison is claimed for this architecture-only handoff.

## Migration from duplicated pointer logic

1. Add the alignment and exact-row trigger contract before changing callers.
2. Add state reconciliation and call it from record, safe bind, forced bind, transfer-host update, rebind, exact cleanup, state invalidation, and old-save migration.
3. Update country reconciliation to filter valid live rows and preserve persisted-owner identity.
4. Add action-local selector outputs and migrate the nine state-target consumers listed above.
5. Replace direct `current_cohort_id` gates in row-specific visibility/availability with a valid host-row or selector contract, while retaining the state-wide border action when it is not row-specific.
6. Replace corridor fallback selection with an exact id captured in the corridor contract and mission state.
7. Replace custody and generic camp adapter pointer checks with exact-id and current-host proof.
8. Require the physical-host guard inside the exact transfer owner, not only in decision callers, so a future caller cannot recreate the stale-origin duplication.
9. Replace unconditional terminal pointer clearing with affected-state and owner reconciliation.
10. Add old-save validation and migration-blocked behavior before enabling movement from legacy rows.
11. Update map/report localisation only after state projection fields are written at validated mutation boundaries.

The parent should not create a generic central MCP router or wrapper skill for this change.

## Validation scenarios

The following scenarios are required before claiming the repair complete.

### Multiple live rows and deterministic selection

- Record two cohorts into one state with different causes and the same persisted owner.
- Confirm both rows exist with all eight arrays aligned, two positive amounts, and distinct monotonic ids.
- Confirm the state cache is ambiguous only as a legacy projection and the state live-row count is two.
- Confirm `fm_close_border` remains state-wide available when its state proofs pass.
- Confirm corridor, transit, integration, resettlement, voluntary return, forced return, and custody actions require an exact action-local id.
- Confirm a unique top semantic candidate selects deterministically and equal semantic candidates return `ambiguous_action` without mutation.
- Confirm selection is unchanged after removing an unrelated lower array index because id, not index, is identity.

### Stale and dead identity

- Supply an id absent from the live ledger, an id duplicated in the id array, a terminal status, a zero amount, an invalid host, and a wrong persisted owner in separate cases.
- Confirm each case fails closed without selecting another row, changing state population, writing Deaths, changing reception, changing pressure, or clearing the other live row.

### Cross-transaction stale-origin debit prevention

- Record a row in A, transfer survivors to B, and verify the row’s persisted host is B.
- Verify A’s state cache is reconciled and no longer exposes the row as a current host.
- Attempt `fm_transit_only`, `fm_enforce_closure`, voluntary return, or forced return from A using the stale id.
- Confirm the physical-host guard rejects the transaction before the population-loss helper runs.
- Confirm A population, B population, route deaths, reception deltas, row amount, history, and conservation totals are unchanged.
- Attempt the same action from B with a valid route and confirm exactly one debit, one measured credit, one reception delta, and one host update.

### Movement conservation and no duplicate deaths

- Exercise no-death movement, route-death movement, protected-floor clamping, blocked route, partial destination credit, and failed destination credit.
- Confirm route deaths never trigger a second physical debit and the conservation residual is zero only for an accepted transaction.
- Confirm a nonzero residual invalidates the transaction and leaves the row and physical ledgers in the documented recovery state.

### Bind, rebind, and cleanup

- Bind one row from A to B while another row remains hosted in A.
- Confirm A reconciles to the surviving row, B reconciles to the bound row, and the owner country cache counts both valid rows.
- Rebind one row from B to C and confirm B’s other row is not selected, removed, or marked ambiguous globally.
- Terminally remove one row and confirm the remaining row’s state and country pointers are repaired rather than cleared.
- Run state cleanup with a row whose origin matches the cleaned state but whose host is elsewhere and confirm the live row is preserved.
- Run explicit host invalidation and confirm terminal evidence preserves id, cause, owner, host, amount, and cleanup reason before row removal.

### Integration, resettlement, return, and missions

- Integrate exactly one bound row and verify no population is created and the other row remains live.
- Resettle exactly one bound row and verify only destination/host metadata changes, with origin, source, owner, and amount preserved.
- Return exactly one row and verify the physical debit is performed from its current host, not from its historical origin unless those states are equal.
- Arm and complete a corridor mission with a stored exact id and verify no later state refresh substitutes another row.
- Resolve the selected row before mission completion and verify the mission closes as invalidated rather than operating on a different row.

### Control changes and old saves

- Change controller or owner of a host state while multiple rows are live and confirm persisted owner is not overwritten and action policy proof is re-evaluated.
- Annex or invalidate the original state while the host remains valid and confirm the row remains live but return eligibility fails closed.
- Load an old save with arrays but no initialization flag and confirm rows survive, next id is monotonic, and caches are rebuilt.
- Load an old save with a stale pointer, ambiguous flag, misaligned arrays, duplicate id, or unknown status and confirm stale pointers clear and unsafe movement is blocked without population mutation.

### Bounded performance

- Verify every reconciliation loop iterates only the existing global registry arrays and touched state/country targets.
- Verify no new `on_daily`, `on_weekly`, `every_state`, `every_country`, or map-refresh global array scan is introduced.
- Verify map/report consumers read transaction-time projections rather than scanning the live registry.

## MCP evidence, unsupported analysis, and blockers

The matching read-only `hoi4.map_inspect` route was available and succeeded, producing the artifact recorded above.

The map route reports existing map locator errors, but no map rewrite is requested by this handoff and no map source was changed.

The matching weighted route was started with `hoi4.probability_inspect` for `famine_migration_destination_selection_effects.txt` and produced the source artifact recorded above.

The weighted source is a destination-state neighbor selector, not the proposed deterministic cohort-row selector.

No AI weight, MTTH value, decision score, mission score, random-list weight, or custom weighted pool is changed by this architecture.

Therefore no probability baseline/post comparison or `chaosx_ai_probability_auditor` balance claim is made.

The MCP server exposes event inspection and map inspection but no dedicated decision/mission inspection route in the discovered tool set.

Source-level decision and mission census is therefore recorded here, and source-only analysis is not presented as engine decision evidence.

The existing completion report records earlier event-inspect timeout and GUI/mapmode route limitations; those routes are not required for this cohort ledger handoff and were not substituted with an unsupported wrapper.

## Risks and parent-owned follow-up

The largest risk is implementing a deterministic lowest-id fallback for row-specific decisions without an explicit user-facing row choice.

That would remove the visible deadlock but could route the wrong cause, custody owner, destination, or return policy.

Keep lowest-id selection for state-wide projections only, and require a unique semantic candidate or explicit id for physical and outcome mutations.

The second risk is placing the host guard only in decision visibility.

The guard must live inside the exact transfer owner so every caller, including future adapters and scripted GUI buttons, receives the same no-duplicate guarantee.

The third risk is broad state cleanup deleting rows whose historical origin matches a state while their current host is elsewhere.

Cleanup must be reason-coded and must reconcile affected states after removal.

The parent owns gameplay implementation, call-site migration, localisation/tooltips, any new projection fields, final decision/mission audit, final probability audit if weights are changed later, and live consumer validation.

No simplification or fallback was applied in this handoff.
