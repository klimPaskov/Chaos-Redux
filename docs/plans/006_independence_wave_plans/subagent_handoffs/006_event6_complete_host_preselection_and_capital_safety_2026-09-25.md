# Event 006 host-survival covenant implementation handoff

Disposition: **implemented for the bounded automatic allocator; probability and runtime outcomes remain unresolved**.
The user explicitly approved the accepted Event 006 Part 1 design and this continuation.
This handoff describes source behavior and its remaining engine uncertainty. It does not claim complete Event 006 readiness.

## Files changed in this continuation

- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
- `common/scripted_effects/chaosx_liberation_release_effects.txt`
- `common/scripted_triggers/chaosx_liberation_release_triggers.txt`
- This handoff.

The pre-existing uncommitted preselection work also touches `common/scripted_effects/006_independence_wave_effects.txt` and `common/scripted_triggers/006_independence_wave_package_triggers.txt`.
I preserved that work and did not edit those two files.
No decision, focus, GUI, map, asset, localisation, spreadsheet, or probability handoff file was edited.

## Helper map and call path

| Helper | Scope, inputs, outputs, and side effects | Call sites |
| --- | --- | --- |
| `independence_wave_collect_possible_state_host` | State scope. Reads the state's current owner. Adds an existing owner once to `global.independence_wave_preselection_hosts`. It changes no ownership, capital, plan row, or weight. | The optional-territory census below. |
| `independence_wave_collect_possible_extended_host` | State scope. Reads the frozen plan chaos band. Calls the owner collector only from `chaos_tier` onward, matching the current extended-territory ladder. | Extended state entries in the census. |
| `independence_wave_collect_possible_optional_hosts_for_candidate` | Country scope. Reads the positive-weight candidate's package ID and probes its exact compact and extended state IDs from the current package reservation registry. It does not reserve states. | `independence_wave_calculate_candidate_allocation_weight` while `independence_wave_host_preselection_collecting` is set. |
| `independence_wave_preselect_automatic_hosts` | Country scope. The existing first weight pass now inventories both primary anchor hosts and optional-state owners, then reserves each distinct possible host before the first candidate draw. It freezes `independence_wave_hosts_preselected` for the second weight pass and optional expansion. | `independence_wave_allocate_automatic_packages` in standalone and joint transactions. |
| `liberation_release_select_and_reserve_host_state` | Country scope. During Event 006 preselection it bypasses the Join conversion's anchor-as-protected-state branch, then chooses an existing current-plan reservation or the capital/fallback state. It returns the existing `liberation_candidate_reject_reason` and writes the existing aligned host row. | Existing Event 005 and Event 006 host reservations and the Event 006 preselection loop. |
| `liberation_release_prepare_host_capitals_for_execution` | Shared locked-plan scope. Relocates a host capital to its frozen protected state if the old capital is a release row, no longer owned, or no longer controlled. It checks the actual capital after `set_capital` and sets the existing relocation failure result on mismatch. | Existing execution preflight, before ownership mutation. |

The confirmed stale-target path is `005_006_liberations_collision_effects.txt` at the Event 005 joint candidate branch, which saves `soviet_collapse_joint_candidate_anchor` as `liberation_candidate_anchor`, followed by Event 006 allocation and preselection in the same effect chain.
There is no intervening clear of that regular event target.
The shared selector's Join branch could therefore choose that prior anchor during Event 006 preselection.
The `independence_wave_host_preselection_reserving` and `independence_wave_hosts_preselected` guards now keep the Join branch out of Event 006 automatic host selection and reservation while preserving its separate conversion path.
The shared state and country reservation predicates also disallow the Join exception from releasing an Event 006 protected state while preselection is frozen.

The existing `is_independence_wave_candidate_anchor_available` predicate requires a current host row after preselection and rejects a protected anchor.
The normal second weight pass therefore removes conflicting anchors without changing numeric package weights.
Compact and extended reservation helpers now trim an optional state whose owner has no preselected host row, so an optional state cannot create a late host reservation that displaces a selected anchor or another reservation.
The existing exact-count failure, candidate rollback, unused-host cleanup, frozen state ledger, and pre-execution compensation paths remain in place.

## Census coverage and implementation choice

The census mirrors all 66 compact and extended state declarations in the 41 package publishers that currently have optional territory among the 149 exact reservation publishers.
Only publishers whose readiness path yields a positive weight in the first pass invoke the census, and extended owners enter the list only at the frozen extended territory level.
No world or map iteration was added.
One-state hosts that cannot retain a safe owned remnant get no host row. Their optional state is trimmed, and their anchor package can remain eligible if its own host is protected.

I reviewed collection-mode dispatch through the existing reservation publishers, as suggested by the parent.
All 149 publishers contain only a loader, begin helper, anchor and optional helpers, and finish helper, but the begin and finish helpers currently own plan-row mutation, rejection recording, sponsorship metadata, and rollback cleanup.
Intercepting those helpers would require a second execution mode across the shared transaction and more temporary-frame and rollback changes.
The explicit bounded census keeps this patch narrower.
Its maintenance risk is that a future optional state declaration must also update the mirrored census. The source parity check below makes this concrete for parent review.

## Capital choice and tuning

The current owned and controlled capital retains first priority unless it is already reserved for release.
The fallback order is controlled owned core, remaining eligible owned core, controlled owned non-core state, then any owned state.
This follows Part 1's requirement to protect an eligible owned core whenever one exists. Current control ranks safety within the core tier, and a non-core remnant is used only when no eligible core exists.
Every fallback requires `impassable = no`, the documented state predicate used here as the available script-level capital-location gate.
The installed `set_capital` documentation describes a state target but exposes no separate predicate proving that every candidate has a valid capital province. The post-effect capital check remains the final fail-closed guard before ownership changes.
Vanilla `events/MTG_Britain.txt` uses a state-scoped `PREV` as a `set_capital` target, and the existing shared release coordinator already uses an event target plus `remember_old_capital = no` and restoration from the frozen original-capital ledger.
No victory-point, supply, port, adjacency, or numeric safety score was added.
There is no new constant or tuning table. The existing chaos-band territory ladder, package weights, and exact automatic count ladder are unchanged.

## Targets, cleanup, and migration

No new event target or persistent country/state variable was introduced.
The census reads the existing short-lived package target and uses the existing `global.independence_wave_preselection_hosts` array.
That array and the collecting/reserving/frozen flags are cleared at contribution start, contribution cleanup, and shared plan cleanup.
The existing host, protected-state, original-capital, snapshot, country, and state arrays remain aligned and use their prior cleanup and rollback paths.
Before plan lock, the pre-existing optional-expansion cleanup clears the freeze and removes unused host rows.
No migration of stored game state is needed for this transient transaction logic.

## Evidence and limits

Source review confirmed the Event 005 joint anchor alias at `005_006_liberations_collision_effects.txt:277`, the Event 006 preselection call before the first draw, the frozen-flag lifetime through optional expansion, and relocation before ownership mutation.
An exact source comparison found 66 optional declarations in the package reservation registry and 66 matching census entries, with no missing or extra `(package, state, compact/extended)` tuple.
The parent independently cross-checked all current `independence_wave_reserve_package_iw_*` publishers and found the same 41 packages and 66 compact/extended rows on both sides, with zero missing or extra rows and matching territory-level gates. I rechecked this against the final gameplay diff before handoff.
`git diff --check` passed for the three gameplay files touched in this continuation.
No tests, HOI4 process, logs, or live game were used, as requested.

Read-only `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` for `chaosx.nr6.1` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/433de52f26ba1ab961863abe2f95b97b23d3438be4aaddec908830ec5290766f/3ca3a404d794d22454641dd6f8ba4a15b0a6d2c67b978ab8e7459157191a1c31/event-trace-289c3d1a9560.json`.
This is chain evidence, not execution proof for the allocator.
Read-only `hoi4.map_inspect` returned revision `1f528671b86e406914cbb4d9b463af263281646ca5ded7074ffc39ab480a5fbe` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/426284450ec80568826572c45b3670286b41ea600ddeb94948984a9eb9602c7e/6a3339dbdcc27c48b34c4d37a4724181e06ff506879d326f41412b8cb78aee02/map-inspect.1f528671b86e4069.json`.
That query matched no specific capital state and reported map position/port diagnostics, so it does not prove capital location validity.
The first `hoi4.probability_inspect` source probe returned `identifier_not_found` for `independence_wave_region_pool`; the read-only `chaosx_ai_probability_auditor` was launched for the exact weighted pool and its scenario evidence but had not returned at handoff time.
A subsequent source-path `hoi4.probability_inspect` on `common/scripted_effects/006_independence_wave_effects.txt` returned `PROBABILITY_SOURCE_INSPECTED`, source revision `88b7fe4136b16049e13a73db3bf4b259e8878c6b8746fa095cbe1bb478adafa8`, source hash `800416aa4370f500c2799e3cf8abb3cb310da3127c80e4ad01bad8e8f533c4b9`, zero constructed candidates, and `poolComplete=false`. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7732a80d4764df50806a2701f092024b1c7f6de768f8ff8974267c0285a23fd0/84d925f51e4b2fb553fa2e1322c8281bd0e67c5b18cd3abc9e2bc6b234c9f0eb/probability-inspect-800416aa4370.json`.
That source hash matches the prior handoff's outer-pool source hash because this continuation changed host eligibility outside the outer weight file. The inspector result is not a scenario comparison.

Engine execution of optional owner census, nested temporary-variable propagation, selection after a protected-anchor conflict, emergency capital relocation, rollback after a failed `set_capital`, and actual exact-count outcome remain unobserved.
The parent owns post-patch MCP inspection and probability comparison, integration review, and the path-limited commit.
The user owns live game validation.

## Parent integration review — 2026-09-25

The parent kept the Event 005-only fallback order intact by gating the new controlled non-core and `impassable = no` rules to Event 006 host preselection; an Event 006 plan relocates a capital that is already unowned or uncontrolled before release, while Event 005-only plans retain the previous condition.

The parent review found that `liberation_candidate_anchor` holds only the latest scope visited during the first weight pass. The collector now records every positive-weight anchor in `global.independence_wave_preselection_anchors` and clears that array after host reservation and on every contribution/shared-plan cleanup path.

Preselection preserves an eligible owned and controlled capital even when it is an anchor, matching Part 1's host-first covenant. Fallback ordering is controlled non-anchor cores, other non-anchor cores, controlled anchor cores, other anchor cores, controlled non-anchor states, other non-anchor states, controlled non-core anchor states, then any remaining owned anchor state. An anchor selected as the protected seat is rejected by the normal second weight pass; the planner still requires the exact frozen candidate count or aborts before ownership mutation.

The anchor-array correction and capital exception were reviewed against the accepted host-survival covenant in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md:109-120` and the offline Data Structures page's single-scope event-target behavior. The independent architect review confirmed the one-target overwrite and the capital-priority conflict before the final source edit.

The parent reran the compact/extended registry parity cross-check: 41 package publishers and 66 optional state rows match the bounded census, with no missing or extra `(package, state, compact/extended)` entries. No global map or world iteration was added, and no numeric package weight or exact-count value changed.

Final read-only `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL`, revision `0106e3d60ec54fc3aee99358e16e371c895ba21d24260b46ba2318536924e62f`, graph hash `f696533757b4b98de6690330c948484bd5446ce56c83a45d7833c25a90e9f8e5`, 38,545 edges, 8,900 unresolved nodes, 2,194 diagnostics, and zero blocking diagnostics. Its trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e129ac4c626f6c47eefa4fd40e38bb1fe1c965db3f6911b50dbabf073648e426/4f1648479154704072f64d0f4086f1e57ac336211a427a866ae4867340609b89/event-trace-0106e3d60ec5.json`.

Final `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` at the same revision and graph hash, with a bounded overview of five selected nodes and 42,848 omitted nodes. The manifest and source-linked diagram are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/357f227e652d9def481a2a56510883c4e4bc587f8da5a29a1f9b114190c59b84/be56cfdbd738b444116f8f105aa4581ccef7e14334e56d276f5605f6d0de263c/event-overview-0106e3d60ec5-manifest.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b006f5c09a025ce3fa4ba755165efc6674611c0b8d593d55c2d2c0538c3ccd51/944d78d93c32f3a2fc21c023655faebeac77d5e1a63adec588d612770ca9f79e/event-overview-0106e3d60ec5.svg`.

`hoi4.event_compare` was attempted on the immediately preceding and final inspect revisions and returned `EVENT_REVISION_NOT_CACHED`; an earlier artifact-backed attempt returned `ARTIFACT_NOT_FOUND` because the old trace's provenance manifest was unavailable. No event-comparison artifact exists.

The weighted-source audit is recorded in `006_event6_preselection_probability_baseline_2026-09-25.md`. It inspected the immutable Git baseline and the current weighted sources, but `hoi4.probability_compare` returned `PROBABILITY_SURFACE_EMPTY` for the sole diagnostic scenario `E006_OUTER_REGION_TOTALS_UNBOUND`. The baseline defines no complete count-band or collision scenario fixtures, and the adapter cannot bind the required host, map, and candidate-array state. Numeric odds and the host-preselection probability delta remain unresolved; no fixture was invented.

The parent `git diff --check` review produced no findings for the five allocator gameplay files. This is source-level hygiene only. No automated test, HOI4 process, save/load run, or live campaign execution was performed.

This allocator tranche has no simplification or fallback implementation. Its unresolved items are the MCP event-graph compare, weighted scenario comparison, engine execution of the array and nested scope behavior, capital relocation/rollback behavior, and final exact-count outcomes. Event 006 as a whole remains `HOLD/PARTIAL` under the current source-of-truth map.
