# Liberations Release Coordinator

## Purpose

The Liberations release coordinator is the shared transaction boundary for Event 005 Soviet Collapse and Event 006 Independence Wave. It lets both systems publish exact provisional country and state footprints, protects one surviving state for every affected host, freezes the combined allocation, revalidates it against the live map, and permits ownership changes only after the whole plan passes.

The coordinator does not decide which Independence Wave package is eligible and does not apply either event's country content. Event-specific selectors, setup effects, focus composition, decisions, ideas, AI, and origin state remain in their owning event files.

## Files

- `common/script_constants/chaosx_liberation_release_constants.txt` defines shared phase, mode, owner, origin, rejection, territory, force, state-role, rollback-failure, finalization-failure, and end-reason enums.
- `common/scripted_triggers/chaosx_liberation_release_triggers.txt` exposes plan-state, origin, reservation, recovery-snapshot, ownership-proof, rollback-proof, and aligned-array contracts.
- `common/scripted_effects/chaosx_liberation_release_effects.txt` owns lifecycle, reservation, validation, execution, finalization, compensation, commit, abort, and cleanup effects.
- `common/scripted_effects/005_006_liberations_collision_effects.txt` owns the synchronous joint dispatcher and Event 005 contribution adapter.
- `common/scripted_effects/006_independence_wave_execution_effects.txt` owns Event 006 fixed-tag instantiation, transfer, finalizer, and rollback acknowledgement.
- `common/script_constants/006_independence_wave_constants.txt` owns Event 006 counts and wave tuning; `006_independence_wave_package_constants.txt` owns package-planner phases and allocation tuning.

## Plan lifecycle

1. The caller supplies the plan mode, expected country count, and owner enum.
2. `liberation_release_begin_plan` allocates a monotonically increasing plan ID, clears stale transient marks, and starts the `collecting` phase.
3. A joint Liberations incident marks both Event 005 and Event 006 as participants. Event 005 freezes its selected tags and one unique anchor per republic first; Event 006 then rerolls its tags and anchors against that footprint.
4. `liberation_release_enter_allocation_phase` opens state and package allocation.
5. Each affected host reserves one protected state and snapshots its original capital. Multiple packages drawing from the same host must reuse that exact protection row.
6. Country and anchor rows enter aligned global arrays before optional territory. A publisher may add rows only for an event declared as a plan participant. Each state records its package, owning event, target country, original owner, original controller, territory role, and the original owner/target core facts required for compensation.
7. Once every selected anchor is frozen, Event 005 attempts its compact republic cores, then Event 006 runs one compact pass across every selected package and one extended pass across every selected package. A collision or host-survival limit trims that optional state; it cannot displace an anchor or invalidate an otherwise viable country.
8. Rejected candidates enter aligned package and reason ledgers for deterministic reroll and later diagnostic reporting.
9. `liberation_release_lock_plan` validates the complete array set, exact count, unique reservation state, living-tag exclusion, anchor ownership, host survival, original capitals, and every recovery snapshot before changing the phase to `locked`.
10. `liberation_release_begin_execution` repeats the live validation immediately before mutation. A stale plan aborts before the first release.
11. The owning event effects instantiate every frozen tag and transfer every frozen state in one synchronous incident. Each state must prove both target ownership and target control, every host must still own its protected state, and the complete live footprint must equal the frozen ownership ledger.
12. A failure while the plan remains in `executing` runs `liberation_release_execute_compensating_rollback`. Event-specific pre-finalizer acknowledgements run first, followed by exact core, owner, controller, transient-country, and capital restoration. Reservation marks and arrays are cleared only after the restored world matches the frozen recovery ledger.
13. `liberation_release_begin_finalization` is the point of no return. Event 006 package setup, politics, technology inheritance, units, stockpiles, host air/naval transfers, active registries, and Event 005 country setup do not begin before this phase.
14. Event 005 counts only countries that pass `has_completed_soviet_collapse_breakaway_setup`. Event 006 first proves every prepared package and live registry, then writes durable origin history and counts only countries that set `independence_wave_origin_committed`.
15. `liberation_release_commit_plan` requires the terminal validation flag of every participating event. If an unexpected deterministic finalizer assertion fails, the plan enters `finalization_failed`, preserves the complete ledger and scope marks, queues no successful presentation, and is never sent through compensating rollback. This state is terminal diagnostic evidence because finalizer force and host-asset mutations are not exactly reversible.

## Host-survival contract

Every distinct host has one row in `global.liberation_plan_hosts`, an owned-state snapshot, one protected-state row, one original-capital row, and a computed planned-loss count. These four host arrays must remain aligned. A plan is valid only when both the snapshot and the live owned-state count are greater than the number of unique planned losses. The protected state must remain owned by its host and cannot appear in the release-state array.

The shared host-reservation effect applies this deterministic protection order:

1. Owned and controlled capital.
2. First owned, controlled core in the engine's stable owned-state iteration.
3. First owned and controlled state in that iteration.
4. First owned core in that iteration.
5. First owned state in that iteration, paired with an explicit capital relocation plan.

A one-state host cannot provide its only state. Optional territory is removed before the package itself is rejected.

Capital preparation remains inside the pre-ownership transaction boundary. If a relocation fails, final live validation rejects the plan, or another pre-execution condition cancels the incident, `liberation_release_restore_host_capitals_before_execution` restores every host from the original-capital ledger before reservation cleanup. A restoration failure raises `liberation_release_capital_restore_failed`, moves the plan to `rollback_failed`, and retains the ledger rather than silently claiming a clean abort.

Candidate construction is transactional and phase-separated. The anchor pass records only a country row and its required anchor. Invalid, living, collided, or unready candidates roll back that provisional tail and reroll. The later compact and extended passes rehydrate the frozen country, anchor, host, owner, and package row before publishing optional states. A failed optional claim is recorded as a trim and processing continues; only aligned-array corruption aborts the contribution. Host-protection rows with no accepted country or planned loss are removed after each pass.

## Exact fixed-tag instantiation

The locked release executor uses the documented fixed-tag path:

1. Identify target cores owned by the host but excluded from the locked footprint.
2. Temporarily remove only those unplanned cores.
3. Confirm the locked anchor is a target core.
4. Release the fixed target tag from the host.
5. Set it to `autonomy_free` and apply the accepted faction relationship.
6. Restore every temporarily masked core.
7. Transfer any additional locked states and apply the event-specific country package.

The mask set is part of pre-execution validation. `transfer_state_to` is not used as an undocumented absent-country creator. Additional frozen states use documented owner/controller effects and are verified in their state scopes immediately afterward; successful-effect calls are never treated as proof by themselves.

Before finalization, an execution failure restores the two snapshotted core facts on every reserved state, restores each original owner and controller separately, deinstantiates only the now-state-less tags proven absent before lock, and restores every original host capital. The country release core loop filters inside the loop body; it cannot add one package's cores to another package's states. Event 006 package and force setup is deliberately absent from this reversible interval, so compensation never has to destroy inherited host aircraft or ships.

## Origin separation

Creator origin is immutable historical data. Event 005 and Event 006 reserve the same tag and state namespace but maintain separate active-origin flags, generation IDs, mechanics, trees, decisions, AI, and formable rights. A living tag is never adopted as a new release candidate. Ending an origin through annexation, voluntary reunion, consensual formable absorption, or explicit dissolution records an end reason; later resurrection creates a new generation.

## Performance

The system runs only when Event 005, Event 006, or the Liberations cluster invokes it. Its loops are bounded to the frozen country, state, host, rejection, package, network, or league arrays. It introduces no world-scanning daily, weekly, or monthly on action.

## Validation scenarios

- Event 005 and Event 006 selected in one Liberations incident in either presentation order.
- An Event 006-origin country already lives when a progressive or terminal Event 005 release is evaluated.
- Same-tag and different-tag/same-anchor collisions.
- Multiple packages drawing from one host while sharing one protected state.
- A package's compact or extended claim is another selected package's anchor.
- Event 005 optional republic cores intersect Event 006 anchors in the same joint incident.
- A one-state host and a host that loses an unplanned state between lock and execution.
- Failure after the first tag is instantiated but before all frozen states transfer: exact owner, controller, core, country-existence, and capital restoration.
- Failure after Event 006 execution metadata validation but before finalization: no Event 006 active, network, league, former-host, technology, force, stockpile, or host-asset mutation exists to clean.
- A compensating rollback retry after an owner, controller, core, country-deinstantiation, or capital assertion fails; the ledger remains intact until exact verification succeeds.
- Event 006 package setup count mismatch, Event 006 durable-origin count mismatch, and Event 005 terminal setup count mismatch: `finalization_failed`, no shared commit, no successful presentation, no compensating rollback, and preserved diagnostic ledger.
- Event 006 navy/air inheritance at finalization: no host asset transfer occurs on any rollback-eligible path.
- Direct loop-filter checks for package cores, unique-anchor counts, per-host loss counts, Event 006 pending metadata cleanup, and evolution actor selection.
- Every Flag after Soviet Collapse and Soviet Collapse after Every Flag.

## Icons and interface assets

The coordinator itself is headless and requires no sprite. Event 006 decisions, focuses, ideas, reports, scenario controls, and super-events register their own icons and image assets in the Event 006 asset manifest and `.gfx` files.

## Future extensions

- Expose the rejection ledger in a developer-only diagnostic view without changing release eligibility.
- Reuse the transaction contract for a future liberation event only after assigning a distinct owner and origin enum and proving compatibility with the existing host-survival rules.
