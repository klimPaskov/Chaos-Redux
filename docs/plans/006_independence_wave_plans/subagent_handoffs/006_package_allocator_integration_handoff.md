# Event 006 package allocator integration handoff

## Outcome

The accepted 206-entry candidate registry now has a readiness-controlled, current-map allocator. It builds Event 006's full contribution inside the shared liberation transaction, freezes every country, state, host remnant, territory level, force level, and package metadata row, and makes no ownership change before the shared coordinator locks the complete incident.

This is an allocation tranche, not a playable-country completion claim. No country currently receives `independence_wave_package_content_ready`; therefore the live automatic pool remains closed until each package's identity, setup, forces, command roster, mechanics, AI, focus or overlay, localisation, and required assets are complete.

## Authoritative inputs

- Accepted registry: `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`
  - SHA-256: `B860C7DD9546B64BFA6A6D1E2575F8EB7BC728103BE0DF1ECF8D344606ADE8DC`
- Installed-map package bindings: `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`
  - SHA-256: `A7757E35B3FEF79D558CE62CB77C030A45C37D1E32CC2862AEED3D88614175C8`
- Reservation groups: `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv`
- State-collision audit: `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_state_collisions.csv`
- Runtime contract: `docs/plans/006_independence_wave_plans/package_bindings/006_runtime_package_registry_template.md`

No nearby, broad, generic, or fallback territory was substituted for an unbound package.

## Runtime coverage

| Contract | Count |
| --- | ---: |
| Accepted package rows | 206 |
| Current-map-bound packages | 149 |
| Deliberately unbound packages | 57 |
| Automatic or high-chaos package weights | 135 |
| Explicit route-only bindings | 9 |
| Explicit scenario-only bindings | 1 |
| Explicit community-only bindings | 4 |
| Fixed-anchor bindings | 145 |
| Ordered-choice anchors | 1 |
| Host-safe choice anchors | 2 |
| Host-branch choice anchors | 1 |
| Planning triggers | 149 |
| Metadata loaders | 149 |
| Exact reservation publishers | 149 |
| Automatic weight preparers | 135 |
| Automatic selector entries | 135 |

The 135 automatic entries are exactly 10 unconditional-ready bindings, 44 registered-tag-if-not-living bindings, 53 unique-state bindings, and 28 high-chaos bindings. The remaining 14 bound entries are callable only from their accepted route, scenario, or community system.

## Band and World Collapse behavior

`independence_wave_package_earliest_band` contains all 206 accepted earliest-band values:

| Accepted earliest band | Registry rows |
| --- | ---: |
| Calm | 35 |
| Gathering | 43 |
| Rising | 83 |
| Chaos | 36 |
| Totalen | 9 |

After current-map binding and accepted disposition restrictions, the static automatic pool can expose 30 packages at Calm, 68 by Gathering, 103 by Rising, 131 by Chaos, and all 135 by Totalen. Readiness, living-tag, origin, host-survival, ownership, control, reservation, and content gates reduce these numbers at runtime.

Automatic wave counts remain exactly 3, 4, 5, 7, and 10. World Collapse remains 10, requests extended territory and the high-chaos force package, opens the Totalen/Layer-E candidates, and multiplies their selection weight by `constant:independence_wave_allocation_factor.world_collapse_rarity` (`1.35`). The shared focus framework consumes `constant:independence_wave_allocation_factor.world_collapse_ambition` (`1.35`) for post-release ambition and revisionist pressure.

Explicit route, scenario, and community callers bypass automatic weight and earliest-band calculation. They must still call the package readiness trigger and exact reservation publisher, so tag, state, origin, host, and collision protections remain mandatory.

## Reservation invariants

- The target tag must be absent, content-ready, unreserved, and free of an active Event 5 or Event 6 origin.
- The anchor's current owner must exist and control the state.
- An anchor owned or controlled by a living Soviet Collapse origin is ineligible, including when Event 6 fires without a joint Event 5 transaction.
- The shared coordinator reserves one surviving state for every affected host before reserving candidate territory and prefers a valid current capital.
- The host loss ceiling is recalculated from current owned states. A candidate can never consume the final surviving state.
- Every package has exactly one committed anchor. Ordered, host-safe, and host-branch packages resolve one alternative and publish it through the saved anchor target.
- Extended states are optional and are attempted after compact states. Any unavailable optional state is recorded as a trim and cannot dislodge the anchor.
- A missing or unsafe anchor rejects the entire candidate and returns selection to the reroll loop.
- Reservation groups and the shared per-state reservation array prevent duplicate anchors and territory collisions. The Trabzon cross-group pair also has an explicit mutex; the Kashmir cross-group route remains protected by the readiness and per-state reservation checks.
- The committed 206-row force registry is probed before a country reservation is accepted. Missing force metadata rejects the package as unready.
- At most 206 distinct package attempts occur. A short viable pool invalidates Event 6's contribution instead of silently reducing the requested count.

## Metadata and execution contract

For every accepted candidate, the allocator records aligned arrays for package ID, country row, region, primary host, depth, archetype, disposition, registered-tag status, territory level, force level, state rows, state roles, state hosts, reservation groups, and protected host states. The package tag also receives plan-scoped pending metadata that is cleared on rollback.

The allocator never calls `release`, `transfer_state`, `set_state_owner`, or `set_state_controller`. Ownership execution remains a separate phase after the joint coordinator validates and locks the complete Event 5/Event 6 plan.

## Validation evidence

The final source-to-runtime audit used fixed-anchor semantics correctly: the first `anchor_state_ids` entry is the unique coordinator anchor, while later entries in the accepted compact set are compact territory. It found:

- 206 contiguous package IDs and 206 exact earliest-band entries;
- 149/149 exact can-plan, loader, and reservation definitions;
- 135/135 exact weight and selector memberships;
- zero runtime publishers for all 57 unbound rows;
- exact tag, reservation group, region, depth, disposition, registered-tag status, anchor, compact, and extended values for every bound row;
- exactly 28 high-chaos predicates and no high-chaos predicate on another automatic disposition;
- all 128 newly reserved Event 6 tags end in `X`;
- zero ownership-changing effects in allocator or regional package files;
- zero `independence_wave_package_content_ready` grants.

## Files in this integration tranche

- `common/script_constants/006_independence_wave_package_constants.txt`
- `common/scripted_triggers/006_independence_wave_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
- `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`
- `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt` through `006_independence_wave_packages_region_14_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt` through `006_independence_wave_packages_region_14_effects.txt`
- the five package-binding artifacts listed above
- the regional handoffs and this consolidated integration handoff

The 128 reserved X-tags and their identity shells were committed separately in `43f314747`. The exact 206-row force registry was committed separately in `fc785387e`.

## Remaining work and blockers

- Full researched playable packages are not complete, so no package is content-ready.
- Release execution must consume the frozen metadata, initialize the accepted country package, and preserve the separate origin contract.
- Route, scenario, formable, league, network, patron, host, focus, AI, asset, achievement, and presentation systems must finish their own wiring before any relevant content-ready flag is granted.
- The 57 unbound packages remain intentionally unavailable. Their missing exact geography or community distinction is an accepted readiness restriction, not a substitute implementation.

## Simplifications and fallbacks

No simplification or fallback was used in this allocator tranche. The unavailable rows remain unavailable, and the live pool remains closed rather than exposing shallow or incomplete country packages.
