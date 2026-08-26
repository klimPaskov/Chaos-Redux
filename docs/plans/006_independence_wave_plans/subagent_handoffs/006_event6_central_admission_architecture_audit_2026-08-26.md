# Event 006 central admission architecture audit

Date: 2026-08-26.

Owner: `chaosx_scripted_system_architect`.

Status: source audit complete; no gameplay source patch applied; no staging, commit, or live-game claim.

## Verdict

The central Event 006 source path is internally wired for the current bounded admission set, and no missing scripted effect or trigger was proven in the local source.

The current boundary is 40 runtime adapters, 32 content-attested selectable packages, 29 compatible reservation groups, 149 package publishers, and 161 unattested selectable rows.

The eight adapter-only rows remain intentionally fail-closed and must not be promoted by this audit: IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179.

The safe recommendation is no central gameplay patch and no attestation widening.

## Full traced path

The canonical root is hidden trigger-only `chaosx.nr6.1` in `events/006_independence_wave.txt:11-63`; its direct callers are numeric event dispatchers rather than literal `country_event = { id = chaosx.nr6.1 }` calls.

The automatic queue stores Event 006 as numeric id `constant:independence_wave_event.id`, whose value is `6` in `common/script_constants/006_independence_wave_constants_registry.txt:583-591`.

`fire_event_by_temp_id_no_cluster` in `common/scripted_effects/chaosx_settings_effects.txt:4526-4780` uses a meta effect to build `country_event = { id = chaosx.nr[EVENT_ID].1 }`, so Event 006 reaches `chaosx.nr6.1` after the Event Cluster path has either completed or deliberately declined the cluster.

The Liberation cluster registers member id `6` in `common/scripted_effects/chaosx_event_cluster_effects.txt:434-452`, and `event_cluster_member_check_availability` injects the Event 006 capacity context before the shared candidate evaluator at `common/scripted_effects/chaosx_event_cluster_effects.txt:557-596`.

On the root, an eligible joint presentation consumes the already executed joint plan and opens the public report; otherwise the root calls `independence_wave_prepare_and_execute_standalone_incident` and only reports after a committed standalone result.

Standalone preparation in `common/scripted_effects/006_independence_wave_execution_effects.txt:957-1050` clears stale receipt state and failure state, captures the current chaos tuning, opens a shared Event 006 plan, calls `independence_wave_allocate_automatic_packages`, expands optional territory, and executes only when the contribution is ready and no optional expansion failed.

Allocation in `common/scripted_effects/006_independence_wave_effects.txt:3255-3405` recomputes all fourteen regional totals before every draw, selects a region and then a package with dynamic `random_list` weights, rerolls rejected candidates without reducing the accepted count, and preserves exact-count fail-closed behavior for joint plans.

The standalone-only recovery exception rewrites the target to a non-empty aligned selected count when the admitted pool is exhausted; an empty pool and every joint shortfall still fail closed with `insufficient_pool` or `aligned_array_failure`.

Each package publisher in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` loads immutable package metadata, invokes `independence_wave_begin_package_reservation`, reserves one fixed anchor, attempts only its declared compact or extended optional states, and finishes through `independence_wave_finish_package_reservation`.

`independence_wave_dispatch_current_package_reservation` in `common/scripted_effects/006_independence_wave_package_planner_effects.txt:397-430` uses the supported numeric meta-effect formatting branches (`iw_00`, `iw_0`, and `iw_`) to call the exact publisher selected by the frozen package id.

Host survival is enforced before candidate acceptance by `liberation_release_select_and_reserve_host_state` and `liberation_release_reserve_host_state` in `common/scripted_effects/chaosx_liberation_release_effects.txt:247-457`; the normal path prioritizes capital, controlled core, owned core, and emergency owned states while retaining one protected host state.

Country and state reservation use `liberation_release_add_country_reservation` and `liberation_release_add_state_reservation` at `common/scripted_effects/chaosx_liberation_release_effects.txt:458-660`, which reject occupied tags, duplicate packages, duplicate reservation groups, anchor conflicts, owner mismatch, plan mismatch, and host-loss overflow before any ownership mutation.

The planner trims optional states when necessary, compacts aligned rows, and leaves the frozen package, country, anchor, former-host, region, depth, territory, force, sponsorship, and generation arrays aligned before contribution readiness.

Execution locks and validates the frozen transaction in `common/scripted_effects/006_independence_wave_execution_effects.txt:259-390`, instantiates countries, transfers all reserved states, assigns exact capitals, and only then calls the package setup dispatcher.

The synchronized package passes are `independence_wave_prepare_frozen_country_packages`, `independence_wave_activate_frozen_country_origins`, `independence_wave_validate_frozen_country_packages`, and `independence_wave_commit_frozen_country_origins` in `common/scripted_effects/006_independence_wave_execution_effects.txt:620-760`.

The consolidated central dispatcher in `common/scripted_effects/006_independence_wave_effects.txt:3416-3530` calls all regional setup, final-validation, and cleanup families; every current attested id has a package-local setup and final-validation adapter, and duplicate scripted-effect definition count is zero.

The final central barrier also requires `has_independence_wave_generic_focus_contract = yes` and `independence_wave_generic_ai_profile` before a package can validate.

Terminal receipt staging and snapshot are implemented in `common/scripted_effects/006_independence_wave_execution_effects.txt:57-140` and are invoked before contribution cleanup on cancellation or compensating rollback; the receipt stage survives coordinator reset and is then cleared after snapshot.

The root clears stale standalone receipt and failure state before opening the next plan and clears the temporary stage a second time after reset, closing the previously observed stale-count and stale-failure lifecycle hazards.

The Join path is bounded and country-scoped: `independence_wave_join_offer_if_eligible` at `common/scripted_effects/006_independence_wave_join_effects.txt:278-355` checks identity, peace, Event 005/Event 006 exclusion, peak-loss threshold, and coordinator availability; `independence_wave_join_probe_attested_package` at `:213-276` probes the same 32 attested ids in deterministic order.

An accepted Join offer reserves the exact remaining footprint, enables the explicit zero-host conversion context, locks and executes the frozen one-package plan, records receipt, clears the plan, and changes the source tag only after setup, validation, transfer, and commit in `common/scripted_effects/006_independence_wave_join_effects.txt:356-470`.

## Helper map

| Helper | Scope and inputs | Output and side effects | Call sites |
| --- | --- | --- | --- |
| `independence_wave_prepare_and_execute_standalone_incident` | Country root; current chaos band and standalone mode. | Opens, allocates, expands, executes, records commit/failure receipt, and resets transient state. | `events/006_independence_wave.txt:49`; standalone/manual Event 006 callers. |
| `independence_wave_allocate_automatic_packages` | Shared plan in allocating phase; Event 006 participant flag. | Frozen selected package and aligned metadata arrays, or fail-closed reason. | Standalone execution and joint Event 005/Event 006 coordinator paths. |
| `independence_wave_begin_package_reservation` / `independence_wave_finish_package_reservation` | Candidate package metadata plus setup event targets. | One candidate transaction, anchor/optional reservations, selected arrays, or candidate rollback. | All package publishers in the package-region registry. |
| `liberation_release_select_and_reserve_host_state` / `liberation_release_add_state_reservation` | Candidate anchor, former host, protected-state ledger, and plan id. | Host row and state rows with planned-loss accounting; no ownership mutation. | Planner anchor and optional-state reservation helpers. |
| `independence_wave_dispatch_package_setup` / `independence_wave_dispatch_package_final_validation` | Frozen `independence_wave_setup_*` values in the released country scope. | One-result setup/final-validation contract across all regional adapters. | Execution preparation and validation passes. |
| `independence_wave_stage_standalone_terminal_receipt` / `independence_wave_snapshot_standalone_terminal_receipt` | Frozen execution counters and terminal status. | Durable receipt that remains after coordinator reset. | Cancellation, rollback, commit, and standalone wrapper. |
| `independence_wave_join_probe_attested_package` / `independence_wave_join_accept_and_execute` | Country-scoped remaining footprint and pending offer identity. | Exact one-package Join reservation and post-commit source-tag conversion. | Join offer event and acceptance option. |

## Constants and tuning plan

No new constants are required for this audit.

The existing authoritative tuning surface is `common/script_constants/006_independence_wave_constants_registry.txt`, including Event 006 id `6`, registry package count `206`, reservation-group count `111`, scenario bound count `138`, active count ladder `3/4/5/7/10`, retry duration, planner attempt limits, reservation-group ids, territory/force bands, and receipt sentinels.

The package table and research count constants intentionally describe the full researched registry, not the current admitted runtime subset; changing `package_count` or adding attestations would widen a contract this audit did not authorize.

Weighted surfaces were reviewed with the required probability-inspection start, but no quantitative balance claim is made because the installed probability route exposed no available adapter and the planner source scan timed out.

## Event-target and cleanup plan

Short-lived candidate pointers use regular event targets such as `liberation_candidate_anchor`, `liberation_candidate_primary_host`, `independence_wave_setup_anchor_state`, and `independence_wave_setup_former_host` so they carry through the immediate execution chain.

Persistent host and Join coordination pointers use global markers and are cleared by the corresponding plan reset, Join runtime clear, or explicit stale-plan cleanup; cleanup is guarded by plan identity to avoid deleting a later operation.

The shared release rollback path preserves the frozen ledger until compensating rollback completes, then clears plan contribution arrays and host/state reservation marks.

The standalone receipt stage is explicitly cleared before and after coordinator reset, and final receipt snapshot clears the stage after copying values.

No event-target leak or cleanup bypass was found in the traced path.

## Concrete blocking contract and exact owner patch

The one concrete broken contract found is the engine-evidence adapter contract, not a local gameplay helper: the required HOI4 MCP Event 006 trace returned `EVENT_INSPECTED_PARTIAL` with 8,314 unresolved nodes and 14 blocking diagnostics after the 2026-08-25 registry consolidation, while source-only inspection confirms the reported IW-043/IW-058 clamp helpers exist.

The required probability route likewise reported no available adapters, and a targeted custom weighted-pool scan of `common/scripted_effects/006_independence_wave_package_planner_effects.txt` timed out after 180 seconds.

This blocks accepted runtime/probability evidence, not the local engine source path; it must not be “fixed” by admitting the eight adapter-only rows or by duplicating the consolidated dispatch file.

Exact owner patch: refresh or reindex the `hoi4_agent_tools` Event 006 source catalog against the current consolidated files, restore a working custom weighted-pool source adapter, and rerun the Event 006 root trace plus the named probability scenarios and compare pass.

Until that owner patch is complete, the parent should report the package boundary as HOLD/PARTIAL and retain the current 32/40 admission split.

## Migration plan

No gameplay migration is needed because the former allocator and dispatch files were consolidated on 2026-08-25 into `006_independence_wave_effects.txt` and the current source markers preserve ownership and call-site identity.

Historical handoffs that mention `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` should be read as pre-consolidation provenance; path-addressed tooling must resolve the current consolidated file.

No helper extraction, source repair, attestation change, or call-site migration is safe within this audit.

## Validation and limitations

The task-specific static validators passed: `.tools/audit_event6_allocator.py`, `.tools/audit_event6_scenario_matrix.py`, `.tools/audit_event6_flags.py --strict`, `.tools/audit_event6_country_api.py`, `.tools/audit_event6_form16.py`, and `.tools/audit_event6_gui_matrix.py`.

The helper call/definition scan found 5,133 definitions and 2,905 calls with no missing scripted helper, and the duplicate scripted-effect definition scan found zero duplicates.

The source checks do not prove parser acceptance, live save/load survival, in-game ownership transfer, or AI probability balance.

No GUI or map redesign was in scope, so no GUI/map rewrite was attempted.

No live Hearts of Iron IV process was launched, and no live-game claim is made.

