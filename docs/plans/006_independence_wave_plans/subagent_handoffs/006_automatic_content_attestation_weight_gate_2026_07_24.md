# Event 006 automatic content-attestation weight gate

Date: `2026-07-24`

## Finding

The automatic allocator's execution preflight correctly rejected packages outside the exact compile-time runtime-content attestation set.
However, `independence_wave_calculate_candidate_allocation_weight` could still assign positive weight to an unadmitted package when its map, tag, chaos-band, and package-planning trigger passed.
The confirmed adapter-backed contamination paths included IW-018 at Gathering Storm and IW-043 and IW-058 at Rising Chaos.
IW-173, IW-179, and IW-184 already had package-local attestation checks in their regional preparation effects and are not examples of the defect.
If a weighted draw froze one of those IDs, the later execution attestation rejected the synchronized transaction, so the four- and five-country automatic bands were safe but not reliable.

## Resolution

`common/scripted_effects/006_independence_wave_package_planner_effects.txt` now bridges the loaded candidate package ID into temporary `independence_wave_execution_package_id` before calculating weight.
The same canonical `has_independence_wave_runtime_package_content_attestation_for_execution_id` trigger used by execution and scenario preflight is required before base weight or any bonus can be assigned.
The scratch execution ID is cleared at the end of every calculation.
This keeps one compile-time attestation authority and avoids a second duplicated admitted-ID list.

An unadmitted candidate now remains at the centralized zero constant even when all of its earlier map and chaos-band checks pass.
It may remain registered, loadable for audit, or available to another origin system without entering an Event 006 automatic draw.
Admitting a package through the existing exact trigger automatically makes it eligible for normal weight calculation without editing fourteen regional random lists.

`independence_wave_begin_package_reservation` applies the same canonical trigger again during the anchor phase.
An unadmitted direct or stale reservation dispatch receives `package_unready` before the planner increments its attempt counter or reserves a host, country, or state.
This second check keeps reservation fail-closed even if a future caller bypasses the weighted regional list.
Optional-territory publication remains tied to the already frozen and aligned package row, while execution performs its existing final attestation recheck.

## Static coverage evidence

- All `144` current calls to `independence_wave_calculate_candidate_allocation_weight` originate in the fourteen regional package-effect files and therefore pass through the centralized weight gate.
- All `126` unique package IDs published by the fourteen regional `random_list` surfaces map to preparation effects that call that centralized calculator; zero random-list IDs bypass it.
- All `149` current calls to `independence_wave_begin_package_reservation` originate in those same fourteen files and therefore pass through the centralized anchor-phase reservation gate.
- The fourteen regional effect files still expose fourteen `random_list` surfaces.
- The HOI4 probability inspector reports Region 1's representative `random_list` pool as complete with nine resolved candidates and zero unresolved entries after the central change.
- The exact attestation trigger still contains only IW-001, IW-004, IW-007, IW-008, IW-017, and IW-019.
- Ordering checks confirm the weight attestation occurs before base weight and the reservation attestation occurs before `liberation_release_select_and_reserve_host_state`.
- The planner file retains balanced braces and both scratch uses clear `independence_wave_execution_package_id` before returning.
- The HOI4 event inspector could not produce a file-scoped lint artifact because its repository-wide issue count exceeds the tool's fixed `20,000` ceiling; this is a tool-limit disclosure, not a substitute for the targeted checks above.

## Exact-count consequence

The current attested set is IW-001, IW-004, IW-007, IW-008, IW-017, and IW-019.
The conservative automatic-capacity witness already uses the same execution preflight, so the three-, four-, and five-country bands may plan only from those six exact IDs and will not be poisoned by a later visually unadmitted selection.
The seven- and ten-country bands still fail closed because six admitted packages cannot satisfy their exact count.
This repair does not claim those higher bands are implemented; they remain blocked on additional complete country admissions.

## Preserved boundaries

- The allocator still freezes the package list before release.
- Host survival, capital preference, unique-anchor, reservation-group, optional-territory trim, living-tag, Event 5 collision, force-package, chaos-band, and final transaction checks remain mandatory.
- Event 5 and Event 6 keep separate origin/content systems.
- No package was admitted, no fallback was introduced, and no world-iteration on action was added.
- No count, force, territory, World Collapse, scenario, focus, decision, localisation, asset, advisor, or tag rule changed.
