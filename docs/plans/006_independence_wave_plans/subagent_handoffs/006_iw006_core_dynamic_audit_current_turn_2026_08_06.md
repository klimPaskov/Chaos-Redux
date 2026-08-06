# Event 006 core dynamic allocator/API audit — current turn

Date: 2026-08-06

Scope: allocator preflight and plan locking, protected host-state survival, reroll and collision handling, origin and ownership provenance, reusable `chaosx_country` collections, crisis queue and synchronised release, dynamic ledgers, and formable or league handoff.

## Verdict

Source review is PASS for the requested core surfaces. The shared planner and liberation-release API preserve transaction order, reserve one remnant state for the former host, reject collisions before lock, and keep origin metadata through execution. Static country collections and their Event 006 projections agree with the registry constants, and the ledger, formable, and league adapters use the same frozen plan rather than rebuilding ownership from presentation data.

One narrow lifecycle defect was found and repaired: a newly queued crisis could inherit the requester country's terminal `independence_wave_crisis_blocked` or `independence_wave_crisis_abandoned` flag from an earlier request. `independence_wave_queue_crisis_release` now clears both flags when it starts a new queue transaction.

## Helper map

| Helper | Scope and inputs | Outputs and side effects | Main call sites |
|---|---|---|---|
| `independence_wave_allocate_automatic_packages` | Country scope; frozen Event 006 count, chaos tier, eligible region/package pool, and allocation seed state | Builds aligned selected-region, selected-package, and package metadata arrays; rejects invalid or colliding candidates without consuming the draw count | `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`, standalone Event 006 preparation in `events/006_independence_wave.txt` |
| `independence_wave_begin_package_reservation` / `independence_wave_finish_package_reservation` | Country scope; one candidate, attestation, chaos band, host, anchor, optional territory, and sponsorship inputs | Reserves host/country/state rows atomically, trims unavailable optional states, records rejection or locked metadata, and keeps ownership unchanged until lock | `common/scripted_effects/006_independence_wave_package_planner_effects.txt` |
| `liberation_release_select_and_reserve_host_state` | Country scope; target package and protected former-host constraints | Chooses a valid owned and controlled host state by priority, snapshots protected/remnant state, and records planned host loss capacity | `common/scripted_effects/chaosx_liberation_release_effects.txt`, Event 006 planner |
| `liberation_release_add_country_reservation` | Global plan scope; target tag, host tag, anchor state, and reservation-group id | Adds a unique country row, rejects invalid anchors or duplicate reservations except the documented Rhine/Saar pair, and increments host planned losses | Shared liberation-release callers, Event 006 planner |
| `liberation_release_add_state_reservation` | Global plan scope; target tag, state id, and host | Appends aligned country/state/host arrays only when the state remains available and owned by the reserved host | Shared liberation-release callers, Event 006 planner |
| `liberation_release_validate_plan` / `liberation_release_lock_plan` | Global plan scope and frozen metadata | Rechecks row, set, host, and state invariants; changes allocation to locked only on a valid complete plan | `common/scripted_effects/chaosx_liberation_release_effects.txt`, Event 006 execution |
| `independence_wave_execute_standalone_frozen_plan` | Country scope; locked arrays and origin metadata | Instantiates and releases countries, transfers only frozen states, restores planned cores, commits origin and history ledgers, then cleans plan state | `common/scripted_effects/006_independence_wave_execution_effects.txt` |
| Crisis queue/resolver helpers (`independence_wave_queue_crisis_release`, `independence_wave_resolve_crisis_release`, recovery callback) | Requester country plus global queue, retry, receipt, and annexation state | Queues one requester, bounds retries, resolves through the same planner, records receipts, and recovers if the requester is annexed | `common/scripted_effects/006_independence_wave_crisis_effects.txt`, `events/006_independence_wave.txt`, `common/on_actions/006_independence_wave_crisis_on_actions.txt` |
| Origin wrappers and country collections | Country scope; registry tag and active-origin state | Set or clear Event 006 origin provenance and expose static fail-closed selectable/registered/owned carrier projections | `common/scripted_effects/006_independence_wave_country_registry_effects.txt`, `common/collections/chaosx_country_collections.txt`, `common/collections/006_independence_wave_country_collections.txt` |

## Constants and tuning

The planner uses the shared script-constant tables rather than new magic numbers. Automatic package counts are 6, 8, 10, 14, and 20 for the ordinary chaos bands, with World Collapse capped at 20. The planner's bounded candidate-attempt ceiling is 206. Reservation proceeds in host, country, anchor, optional compact/extended, attestation, and lock phases. Host capacity preserves one protected remnant state. Crisis timing and retry values remain the existing shared tuning: 120-day cooldown, 365-day queue window, one requester transaction, and a 14-attempt retry ceiling.

## Event targets, flags, variables, and cleanup

Short-lived candidate and setup targets (`liberation_candidate_*` and `independence_wave_setup_*`) are cleared by the planner rollback/finalization paths. The global plan arrays and row flags are created during contribution, validated before lock, and cleared after execution or rejection. Host, country, and state reservation flags are removed by the shared liberation-release cleanup helpers, including unused host rows with zero planned loss. Crisis queue state clears active runtime, receipts, requester state, cooldown markers, and stale terminal flags before a fresh queue is accepted. Global origin targets are cleared by the Event 006 origin-clear wrapper after the lifecycle ends.

## Findings and migration notes

- Region/package omissions checked in the automatic pool are intentional overlay-only, scenario-only, formable-only, or route-only rows (`always = no`, `scenario_variant_only`, or equivalent attestation), not allocator defects.
- The former-host unique-target and reserve-one-remnant behavior is already implemented in the shared API and should not be reopened.
- No source defect was found in ownership provenance, collision rerolls, dynamic visible ledgers, formable handoff, or league integration.
- Duplicated region dispatchers already feed the shared planner; package adapters feed shared setup and final validation; public `chaosx_country_*` collections remain static fail-closed arrays with runtime origin gates. No broad migration is required this turn.

## Files changed

- `common/scripted_effects/006_independence_wave_crisis_effects.txt`: clear stale blocked/abandoned country flags at the start of a new crisis queue transaction.
- This handoff document.

## Validation and evidence

Task-specific local audits passed:

- `.tools/audit_event6_allocator.py`: publishers 149; automatic/high-chaos selectable packages 126; SCN-008 selectable packages 138; attested packages 23; compatible reservation groups 22; static standalone witness 20; protected former-host capacity and Rhine/Saar pair checks passed; automatic counts and crisis/order checks passed.
- `.tools/audit_event6_country_api.py`: 242 broad rows, 191 unique carriers, Soviet 34, Africa 45, missing 0, duplicates 0.
- `.tools/audit_event6_flags.py`: 102 registered Event 006 tags, 102 complete flag families, 0 incomplete.

Read-only `hoi4.event_inspect` scans for `chaosx.nr6.1` and `events/006_independence_wave.txt` returned `EVENT_INSPECTED_PARTIAL` with `MCP_INLINE_FILES_TRUNCATED`; the workspace graph was valid but large helper projections were deferred. Artifact URIs are retained in the parent tool transcript. A probability inspection was attempted for the custom weighted pool, but its response was truncated and is not used as balance evidence; the required scenario-specific `chaosx_ai_probability_auditor` pass remains parent-owned.

## Limitations and follow-up

No game launch, save/load, live ownership scenario, Event Log render, or mission-timer playback was performed because those checks belong to the parent/user boundary. The requested `docs/systems/006_independence_wave_country_registry.md` path is absent; the existing authoritative registry docs are under `docs/events/006_independence_wave/systems/country_registry.md` and `docs/events/006_independence_wave/country_api.md`. Existing terminal crisis flags currently have no consumers elsewhere, so the patch is forward-safe lifecycle hygiene rather than a presently visible UI fix. No gameplay simplification was introduced, and no other safe source patch was identified.

Parent owns final review and commit for this shared worktree.
