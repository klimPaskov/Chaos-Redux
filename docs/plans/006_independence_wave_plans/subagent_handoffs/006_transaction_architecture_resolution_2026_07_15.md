# Event 006 Transaction Architecture Resolution

Date: 2026-07-15

Status: shared transaction correction implemented and source-audited. This resolves the ownership-transaction blockers in `006_transaction_architecture_audit_2026_07_15.md`; it does not attest any country package or open the fail-closed runtime pool.

## Result

The Event 005/Event 006 Liberations coordinator now has an explicit reversible execution interval and an explicit point of no return.

Before finalization, the only permitted mutations are fixed-tag release, target-core preparation, exact state owner/controller transfer, and host-capital relocation. Every affected state carries its original owner, original controller, original-owner core fact, and target core fact. Every host carries its original capital and protected remnant. A failed execution restores those facts, removes only transaction-created state-less countries, verifies the complete frozen ledger, and clears it only after exact compensation succeeds.

Package setup is outside that interval. Event 006 politics, technology inheritance, forces, stockpiles, air/naval inheritance, live registries, origin history, and Event 005 breakaway setup begin only after the exact ownership footprint crosses `liberation_release_begin_finalization`. A terminal package-count failure enters `finalization_failed`, retains the ledger, cannot be reset or routed through compensating rollback, and queues no successful presentation.

## Files changed

- `common/script_constants/chaosx_liberation_release_constants.txt`
- `common/scripted_triggers/chaosx_liberation_release_triggers.txt`
- `common/scripted_effects/chaosx_liberation_release_effects.txt`
- `common/scripted_effects/005_006_liberations_collision_effects.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/006_independence_wave_execution_effects.txt`
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
- `common/scripted_effects/006_independence_wave_evolution_effects.txt`
- `common/scripted_effects/006_independence_wave_scenario_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `docs/systems/liberation_release_coordinator.md`
- `docs/events/006_independence_wave.md`

## Implemented contracts

1. `rolling_back`, `rollback_failed`, `finalizing`, and `finalization_failed` are non-resettable active phases.
2. Lock validation requires aligned arrays and a complete owner/controller/core/capital recovery ledger.
3. Host protection reuses an existing valid row, otherwise prefers an owned and controlled capital, then controlled core, controlled state, uncontrolled core, and any owned state. The current mandatory anchor is never eligible as the protected remnant.
4. Event 005 selects its anchor before host protection. Event 006 and Event 005 therefore reserve anchors before optional territory without allowing protection to consume the anchor.
5. The complete live state footprint must match the frozen target owner and controller before finalization.
6. Compensating rollback restores target and original-owner core facts, original owners and controllers, transaction-created country absence, and every original host capital. A mismatch preserves the ledger in `rollback_failed` for an idempotent retry.
7. Event 006 performs no package or force setup before finalization, so pre-finalizer rollback does not pretend to reverse host aircraft, ships, technology, politics, stockpiles, or spawned forces.
8. Joint finalization proves the Event 005 terminal setup count before any Event 006 package setup begins.
9. Event 006 validates every prepared package and active registry before durable origin history. Shared commit requires the final validation flag of every included event.
10. Joint success-presentation flags are written only after the shared plan reaches `committed`. An unexpected shared-commit failure becomes terminal finalization failure.
11. SCN-008 distinguishes pre-execution cleanup, compensating rollback, and terminal finalization failure. An aborted lock attempt clears Event 006 pending package metadata before a later plan can reset the shared country array.
12. Event 006 generation reset clears force-package mapping state before provenance keys disappear.

## Review evidence

The final independent reread found no remaining P0, P1, P2, or P3 defect in the reviewed transaction scope. It traced standalone Event 006, joint Event 005/Event 006, and SCN-008 through allocation, lock, capital preparation, execution, rollback, finalization, commit, and failure dispatch.

The reviewed call graph has balanced script blocks, no unsupported textual comparison operator, and no direct loop-level `limit` inside `for_each_scope_loop`. Targeted diff hygiene is clean. The Event 005 terminal proof was checked against every joint opening-republic setup invariant rather than treating an effect call as success.

## Failure-path matrix

| Injection point | Required outcome | Source result |
| --- | --- | --- |
| Exact count cannot be filled | No ownership mutation; restore any prepared host capital; clear pending Event 006 rows | Wired |
| Living/invalid tag or duplicate anchor | Reject and reroll while preserving exact target count | Wired in allocator |
| Optional state collides or consumes the host remnant | Record trim and keep the anchored package | Wired in compact/extended passes |
| Failure after the first release | Restore exact cores, owners, controllers, transient-country absence, and capitals | Wired through compensating rollback |
| Failure after all transfers but before finalization | Same exact compensation; no package/force mutation exists | Wired |
| Rollback assertion mismatch | Retain arrays and scope marks in `rollback_failed`; refuse a new plan | Wired |
| Event 005 terminal setup count mismatch | Stop before Event 006 setup and retain `finalization_failed` evidence | Wired |
| Event 006 package validation mismatch | Retain `finalization_failed`; no durable Event 006 origin commit or successful presentation | Wired |
| Event 006 durable-origin count mismatch | Retain `finalization_failed`; no shared commit or successful presentation | Wired |
| Shared commit unexpectedly fails | Convert to `finalization_failed`; joint presentation flags remain unset | Wired |
| SCN-008 lock abort | Freeze failure summary, restore capitals, clear pending package metadata | Wired |
| SCN-008 post-transfer failure | Run the same exact compensating rollback | Wired |

## Remaining scope outside this resolution

Runtime and scenario content-attestation gates are still fail-closed. Current automatic, joint, and SCN-008 success paths therefore stop before ownership mutation. The transaction is source-audited against its failure paths, but no claim is made that the package pool is playable or that these paths were exercised in a live engine session.

Ordinary Liberations-cluster availability and package readiness are separate implementation tranches. This transaction correction does not weaken either gate, reduce the exact wave count, or substitute shallow packages.

No fallback or simplification was accepted in this transaction correction.
