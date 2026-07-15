# Liberations Release Coordinator

## Purpose

The Liberations release coordinator is the shared transaction boundary for Event 005 Soviet Collapse and Event 006 Independence Wave. It lets both systems publish exact provisional country and state footprints, protects one surviving state for every affected host, freezes the combined allocation, revalidates it against the live map, and permits ownership changes only after the whole plan passes.

The coordinator does not decide which Independence Wave package is eligible and does not apply either event's country content. Event-specific selectors, setup effects, focus composition, decisions, ideas, AI, and origin state remain in their owning event files.

## Files

- `common/script_constants/chaosx_liberation_release_constants.txt` defines shared phase, mode, owner, origin, rejection, territory, force, state-role, and end-reason enums.
- `common/scripted_triggers/chaosx_liberation_release_triggers.txt` exposes plan-state, origin, reservation, and aligned-array contracts.
- `common/scripted_effects/chaosx_liberation_release_effects.txt` owns lifecycle, reservation, validation, commit, abort, and cleanup effects.
- `common/script_constants/006_independence_wave_constants.txt` owns Event 006 counts and wave tuning; `006_independence_wave_package_constants.txt` owns package-planner phases and allocation tuning.

## Plan lifecycle

1. The caller supplies the plan mode, expected country count, and owner enum.
2. `liberation_release_begin_plan` allocates a monotonically increasing plan ID, clears stale transient marks, and starts the `collecting` phase.
3. A joint Liberations incident marks both Event 005 and Event 006 as participants. Event 005 freezes its selected tags and one unique anchor per republic first; Event 006 then rerolls its tags and anchors against that footprint.
4. `liberation_release_enter_allocation_phase` opens state and package allocation.
5. Each affected host reserves one protected state and snapshots its original capital. Multiple packages drawing from the same host must reuse that exact protection row.
6. Country and anchor rows enter aligned global arrays before optional territory. A publisher may add rows only for an event declared as a plan participant. Each state records its package, owning event, target country, original host and controller, and territory role.
7. Once every selected anchor is frozen, Event 005 attempts its compact republic cores, then Event 006 runs one compact pass across every selected package and one extended pass across every selected package. A collision or host-survival limit trims that optional state; it cannot displace an anchor or invalidate an otherwise viable country.
8. Rejected candidates enter aligned package and reason ledgers for deterministic reroll and later diagnostic reporting.
9. `liberation_release_lock_plan` validates the complete array set, exact count, unique reservation state, living-tag exclusion, anchor ownership, and host survival before changing the phase to `locked`.
10. `liberation_release_begin_execution` repeats the live validation immediately before mutation. A stale plan aborts before the first release.
11. The owning event effects execute every locked release in one synchronous incident. Each transferred state must prove both target ownership and target control before it is counted; a failed proof prevents country initialization and plan commit.
12. `liberation_release_commit_plan` runs only after release, verified transfer, package initialization, and origin-history work all succeed.

## Host-survival contract

Every distinct host has one row in `global.liberation_plan_hosts`, an owned-state snapshot, one protected-state row, one original-capital row, and a computed planned-loss count. These four host arrays must remain aligned. A plan is valid only when both the snapshot and the live owned-state count are greater than the number of unique planned losses. The protected state must remain owned by its host and cannot appear in the release-state array.

The shared host-reservation effect applies this deterministic protection order:

1. Owned and controlled capital.
2. First owned, controlled core in the engine's stable owned-state iteration.
3. First owned core in that iteration.
4. First owned and controlled state in that iteration.
5. First owned state in that iteration, paired with an explicit capital relocation plan.

A one-state host cannot provide its only state. Optional territory is removed before the package itself is rejected.

Capital preparation remains inside the pre-ownership transaction boundary. If a relocation fails, final live validation rejects the plan, or another pre-execution condition cancels the incident, `liberation_release_restore_host_capitals_before_execution` restores every host from the original-capital ledger before reservation cleanup. A restoration failure raises `liberation_release_capital_restore_failed` rather than silently claiming a clean rollback.

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
- Every Flag after Soviet Collapse and Soviet Collapse after Every Flag.

## Icons and interface assets

The coordinator itself is headless and requires no sprite. Event 006 decisions, focuses, ideas, reports, scenario controls, and super-events register their own icons and image assets in the Event 006 asset manifest and `.gfx` files.

## Future extensions

- Expose the rejection ledger in a developer-only diagnostic view without changing release eligibility.
- Reuse the transaction contract for a future liberation event only after assigning a distinct owner and origin enum and proving compatibility with the existing host-survival rules.
