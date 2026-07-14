# Event 006 Scripted-System Architecture Handoff

## Architectural decision

Independence Wave is a transaction-style release coordinator. It must never select a tag and mutate ownership immediately. Planning is mutation-free, the complete allocation is locked and revalidated, and all releases execute synchronously behind one commit barrier.

## Shared coordinator ownership

Create shared Liberations files for plan lifecycle, Event 005/Event 006 reservation ownership, origin enums, historical generation IDs, commit state, rejection reasons, and cross-event collision checks. Event 006 retains ownership of its 206-package registry and its country mechanics.

Plan phases are `idle`, `collecting`, `allocating`, `locked`, `executing`, `committed`, and `aborted`. Modes are `automatic`, `cluster_joint`, and `triggerable_scenario`. Boolean state uses flags; variables are reserved for IDs, enums, counts, scales, and generation numbers.

## Persistent state

The joint plan must persist across the existing cluster presentation delay, so it uses global arrays, global variables, state variables, and country scope variables—not regular event targets.

Required parallel plan data includes:

- Candidate/package IDs and target country scopes.
- Exact planned states and roles.
- Original host and controller scopes.
- Reservation groups and protected host-survival states.
- Rejected package IDs and machine-readable rejection reasons.
- Event ownership of each reservation.

Every Event 006 country stores immutable origin generation, package, region, overlay, AI profile, territory and force levels, former hosts, wave sequence, and the five visible country values.

## Allocation contract

1. Begin a new plan ID and clear stale transient marks.
2. Capture mode, intensity, scenario type, chaos band, and exact target count.
3. If Event 005 participates, collect its exact provisional tag/state reservations first.
4. Compile the Event 006 pool from implementation-ready, mode-eligible, nonexistent tags.
5. Snapshot every prospective host and reserve one surviving state, prioritising its owned and controlled capital.
6. Draw from aligned weighted arrays without replacement.
7. Attempt extended, compact, then anchor-only territory; trim optional states before rejecting the package.
8. Reject state, reservation-group, Event 005, living-tag, readiness, or host-survival collisions and reroll.
9. Continue to the exact automatic count or, for Every Flag, until all viable scenario candidates are allocated.
10. Validate all aligned arrays and invariants, then lock.
11. Revalidate immediately before mutation; rebuild the whole plan if stale.
12. Execute all releases synchronously and clear transient state only after the commit.

Automatic counts remain exactly `3`, `4`, `5`, `7`, and `10`; World Collapse stays at `10`. Scenario intensity never changes candidate count.

## Host survival

For every host in the combined plan:

`owned states at snapshot - unique planned losses >= 1`

Protection priority is current owned/controlled capital, then another owned core suitable for a capital, then any owned state with explicit capital relocation. A one-state host invalidates every package that consumes its only state. The invariant is checked both at lock and at the mutation barrier.

## Fixed-tag exact-state release

The installed effects documentation states that `release` creates the specified country as a puppet from the releasing country’s owned core states. `transfer_state_to` documents ownership transfer but does not document absent fixed-tag creation. Vanilla repeatedly uses `release`, then `set_autonomy = { autonomy_state = autonomy_free }`, to create independent countries.

The production method therefore uses the documented path:

1. Snapshot which planned target cores are owned by the host but not in the locked footprint.
2. Temporarily remove only those target cores.
3. Ensure the locked anchor is a target core.
4. Call `release = TARGET` from the host.
5. Set the released subject to `autonomy_free` and remove inherited faction membership when the accepted route does not retain it.
6. Restore every temporarily masked core.
7. Transfer any additional locked states explicitly.

This is the primary exact-state instantiation method, not a dynamic-tag or generic-country fallback. No mutation begins until the mask set and full release footprint validate.

## Provenance

Creator provenance is immutable historical data keyed by a monotonically increasing generation ID. Active origin ends through one effect called from annexation, voluntary reunion, consensual formable absorption, or explicit dissolution. Resurrection creates a new generation and never rewrites prior history.

Network and patron links pair a country scope with its generation ID so a later resurrection cannot reactivate an old relationship accidentally.

## Focus composition

HOI4 cannot overlay two unrelated trees by loading two focus trees. Event 006 base lanes, 14 regional overlays, government routes, and signature modules must be composed as shared-focus components into audited trees. Existing meaningful trees keep their tree and receive the safe additive Event 006 decision/mechanic overlay. A generic tree is never an implementation-ready fallback for a package that requires a distinct composition.

## Country and league state

The five country values are updated only by concrete focuses, decisions, missions, events, wars, territory changes, patrons, hosts, and league actions. Fixed staged ideas represent lifecycle thresholds; bounded event-driven refreshes avoid world-periodic scans.

The informal network is not a faction. It uses active-country and relationship arrays keyed by generation. The charter league uses a faction template/manifest/goals, leader-held Cohesion/Common Cause/Patron Capture/Shared Reserve, and member-held Confidence, refreshed only on relevant actions.

## Formables and scenario

The 48 formable families use generic staged APIs with family-specific dispatch, consent methods, claims/integration rights before cores, and no transformation of unrelated living countries.

Every Flag calls the same planner in scenario mode. All intensities attempt every viable scenario-enabled package; intensity changes territory, forces, starting values, and route emphasis. Scenario type applies the accepted congress, host-war, belligerence, patron, or partition setup by iterating only frozen participant/host arrays.

## Performance constraints

- No daily, weekly, or monthly whole-world iteration.
- Planner work occurs only when Event 006, Every Flag, or the Liberations cluster invokes it.
- All iterations are bounded to package, participant, state, host, sponsor, network, or league arrays.
- Aligned arrays are length-checked before indexed access.
- Scope variables, not scoped temporary variables, persist country/state references.

## Risks carried forward

- Every package must pass the compiled readiness contract before entering the pool.
- Current-map state bindings must be semantically resolved, not only numerically valid.
- Event 005 must be refactored to publish exact provisional footprints before truthful joint allocation is possible.
- Runtime plan validation can prevent partial mutation; Clausewitz cannot provide a genuine rollback after the first ownership transfer, so execution must remain one synchronous chain.

## Simplifications

None. This architecture preserves every accepted invariant and explicitly rejects dynamic-tag, generic-package, and broad-release substitutes.
