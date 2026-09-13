# Event 021 GLB parent deterministic review

Date: 2026-09-01.

Owner: parent implementation pass.

Status: current-source deterministic evidence, not an independent probability-auditor certificate and not a live scheduler sequence.

## Findings and patches

Each due-country review snapshots eligibility before advancing the review date and performs exactly one opening dispatch from that frozen marker. The redundant post-review due check was removed because a failed first dispatch could otherwise be attempted a second time in the same bounded review.

The Critical queue primitive was designed to retain a valid country while theater capacity was full, but `event021_global_review_current_country` required free capacity before calling the queue primitive. This prevented GLB-04 from entering the persistent queue. The parent admission check no longer requires current capacity; `event021_launch_critical_country` still requires theater capacity, so the cap remains authoritative at launch.

The bounded registered-country review now also dequeues a country whose target or actor proof expires. This prevents a stale but still-existing country from remaining in the Critical array indefinitely.

Automatic and scenario target predicates now reject `random_civil_war_successor_grace`. A human Event 006 country becomes eligible again after grace expires when it has controlled territory and another valid opposition route; actual nonhuman countries remain excluded through `is_actual_nonhuman_country`.

## Named matrix disposition

| Scenario | Current deterministic disposition |
| --- | --- |
| GLB-01 | A Critical country with a valid route passes `random_civil_war_critical_queue_entry_valid`, enters the persistent array once, and uses the fifteen-day Critical review interval. Majors remain subject to their stricter route and targeting gates. |
| GLB-02 | `random_civil_war_critical_queue_entry_valid` delegates to `random_civil_war_country_can_be_target`, which requires a valid opposition route. A Fractured or Critical country without an actor cannot enter the launch queue. |
| GLB-03 | Stable countries receive a 120-day review interval and do not satisfy the Critical admission branch. |
| GLB-04 | A valid Critical country is admitted even while the theater cap is full. Launch remains blocked by `random_civil_war_theater_capacity_available`, leaving the Critical band and queue receipt intact for a later bounded pulse. |
| GLB-05 | `event021_handle_annexed_country` dequeues the disappearing country, removes it from the registered array, releases live front/theater membership, and repairs both cursors. |
| GLB-06 | Successor grace is an exact target exclusion. After the finite grace flag clears, a normal-human Event 006 country with territory and a valid route can pass the same target and queue contract as another human country. |
| GLB-07 | `random_civil_war_is_normal_human_country` rejects `is_actual_nonhuman_country`, and that predicate is inherited by registry, target, queue, recurrence, and scenario paths. |

## Boundedness

Evolution III alone enables broad registration. One existing global-host pulse samples at most four unregistered countries, scans at most twelve registered rows and eight Critical rows, admits at most three Critical rows through the review budget, and advances persistent cursors. No unrestricted daily, weekly, or monthly all-country on-action exists.

## MCP and local evidence

The focused four-file helper manifest refreshed under revision `b8b928ac6119099215dd486990704d24c5ac36e2b4a305713954081663d1884d` with graph hash `4de181295a914d2f86f42d604a900365f19e2e39651179608128d3cca756127e`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbffd24b9ac0d94d73c532f972b9b82eca76eb0ff93928da0c8ed3256f23b02d/c936b257b477ca816390357a9b935c995254abdcca20817ed4775800a8a19940/event-lint-b8b928ac6119.json`.

The report remains partial because the installed event analyzer defers workspace-wide helper projection. Source braces are balanced and no unsupported comparison operators were introduced.

## Release boundary

The runtime initializer deliberately clears `random_civil_war_rework_ready`, so Global Fracture remains unavailable until all release blockers are resolved. This review proves the dormant current-source control flow; it does not authorize opening the gate.
