# Liberations Release Coordinator

## Purpose

The Liberations release coordinator is the shared transaction boundary for Event 005 Soviet Collapse and Event 006 Independence Wave. It lets both systems publish exact provisional country and state footprints, protects one surviving state for every affected host, freezes the combined allocation, revalidates it against the live map, and permits ownership changes only after the whole plan passes.

The coordinator does not decide which Independence Wave package is eligible and does not apply either event's country content. Event-specific selectors, setup effects, focus composition, decisions, ideas, AI, and origin state remain in their owning event files.

## Files

- `common/script_constants/chaosx_liberation_release_constants.txt` defines shared phase, mode, owner, origin, rejection, territory, force, state-role, and end-reason enums.
- `common/scripted_triggers/chaosx_liberation_release_triggers.txt` exposes plan-state, origin, reservation, and aligned-array contracts.
- `common/scripted_effects/chaosx_liberation_release_effects.txt` owns lifecycle, reservation, validation, commit, abort, and cleanup effects.
- `common/script_constants/006_independence_wave_constants.txt` owns Event 006 counts and Event 006-specific tuning.

## Plan lifecycle

1. The caller supplies the plan mode, expected country count, and owner enum.
2. `liberation_release_begin_plan` allocates a monotonically increasing plan ID, clears stale transient marks, and starts the `collecting` phase.
3. A joint Liberations incident marks both Event 005 and Event 006 as participants. Event 005 publishes its exact provisional footprint first.
4. `liberation_release_enter_allocation_phase` opens state and package allocation.
5. Each affected host reserves one protected state. Multiple packages drawing from the same host must reuse that exact protection row.
6. Country rows and exact state rows enter aligned global arrays. A publisher may add rows only for an event declared as a plan participant. Each state records its package, owning event, target country, original host and controller, and territory role.
7. Rejected candidates enter aligned package and reason ledgers for deterministic reroll and later diagnostic reporting.
8. `liberation_release_lock_plan` validates the complete array set, exact count, unique reservation state, living-tag exclusion, anchor ownership, and host survival before changing the phase to `locked`.
9. `liberation_release_begin_execution` repeats the live validation immediately before mutation. A stale plan aborts before the first release.
10. The owning event effects execute every locked release in one synchronous incident and call `liberation_release_commit_plan` only after all setup work finishes.

## Host-survival contract

Every distinct host has one row in `global.liberation_plan_hosts`, an owned-state snapshot, one protected-state row, and a computed planned-loss count. A plan is valid only when both the snapshot and the live owned-state count are greater than the number of unique planned losses. The protected state must remain owned by its host and cannot appear in the release-state array.

The shared host-reservation effect applies this deterministic protection order:

1. Owned and controlled capital.
2. Another owned core suitable for the capital.
3. Another owned state paired with an explicit capital relocation plan.

A one-state host cannot provide its only state. Optional territory is removed before the package itself is rejected.

Candidate construction is transactional. The planner records the current state-row tail before it begins a package. If an optional or compact claim fails, it removes the failed tail and retries with a smaller footprint. If no valid anchor remains, it removes the complete candidate country row, clears its scope marks, decrements every affected host loss count, and removes any host-protection row that no accepted candidate still uses.

## Exact fixed-tag instantiation

The locked release executor uses the documented fixed-tag path:

1. Identify target cores owned by the host but excluded from the locked footprint.
2. Temporarily remove only those unplanned cores.
3. Confirm the locked anchor is a target core.
4. Release the fixed target tag from the host.
5. Set it to `autonomy_free` and apply the accepted faction relationship.
6. Restore every temporarily masked core.
7. Transfer any additional locked states and apply the event-specific country package.

The mask set is part of pre-execution validation. `transfer_state_to` is not used as an undocumented absent-country creator.

## Origin separation

Creator origin is immutable historical data. Event 005 and Event 006 reserve the same tag and state namespace but maintain separate active-origin flags, generation IDs, mechanics, trees, decisions, AI, and formable rights. A living tag is never adopted as a new release candidate. Ending an origin through annexation, voluntary reunion, consensual formable absorption, or explicit dissolution records an end reason; later resurrection creates a new generation.

## Performance

The system runs only when Event 005, Event 006, or the Liberations cluster invokes it. Its loops are bounded to the frozen country, state, host, rejection, package, network, or league arrays. It introduces no world-scanning daily, weekly, or monthly on action.

## Validation scenarios

- Event 005 and Event 006 selected in one Liberations incident in either presentation order.
- An Event 006-origin country already lives when a progressive or terminal Event 005 release is evaluated.
- Same-tag and different-tag/same-anchor collisions.
- Multiple packages drawing from one host while sharing one protected state.
- A one-state host and a host that loses an unplanned state between lock and execution.
- Every Flag after Soviet Collapse and Soviet Collapse after Every Flag.

## Icons and interface assets

The coordinator itself is headless and requires no sprite. Event 006 decisions, focuses, ideas, reports, scenario controls, and super-events register their own icons and image assets in the Event 006 asset manifest and `.gfx` files.

## Future extensions

- Expose the rejection ledger in a developer-only diagnostic view without changing release eligibility.
- Reuse the transaction contract for a future liberation event only after assigning a distinct owner and origin enum and proving compatibility with the existing host-survival rules.
