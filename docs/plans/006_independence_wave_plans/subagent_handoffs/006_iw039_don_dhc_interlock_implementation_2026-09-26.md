# IW-039/DON and Event 005 DHC interlock

**Disposition:** implemented at source/static-witness level; both-order runtime behavior remains unverified, and IW-039 stays unadmitted.

## Acceptance basis

The user explicitly accepted state 245/Millerovo as the required Event 006 anchor and capital, state 238/Volgodonsk as optional compact territory, vanilla state 218 outside IW-039, and mutual exclusion between Event 005 DHC and Event 006 IW-039 in both event orders. The decision and capacity-one `RG-DON-KUBAN` rule are recorded in Part 5; see commit `5cccc8b4e`.

## Source changes

`common/scripted_triggers/005_006_liberations_collision_triggers.txt:34-45` adds `is_don_dhc_cross_event_collision_clear`. In country scope it rejects an existing DHC, a DON carrier marked reserved/pending/prepared or active for Event 006, and current-plan reservations of states 218 or 238. It relies on `is_independence_wave_active_country`, which treats an ended Event 006 origin as inactive; it deliberately does not latch on the historical `independence_wave_origin_committed` receipt, so ordinary DHC behavior can resume after Event 006 cleanup.

`common/scripted_triggers/005_soviet_collapse_triggers.txt:8194-8208` calls the shared guard from normal `can_soviet_collapse_spawn_dhc`, before the existing 218/238 Soviet ownership and control tests.

`common/scripted_effects/005_soviet_collapse_effects.txt:23503-23531` applies the same guard to the force-all DHC branch before the state-transfer effects. The ordinary branch remains gated by `can_soviet_collapse_spawn_dhc`; the guard therefore applies before either path transfers states 218 or 238 and runs `soviet_collapse_setup_dhc_successor`.

`common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:345-352` calls the shared guard before IW-039 enters the Region-04 candidate pool. IW-039 therefore cannot receive a candidate weight when DHC is live, DON is already pending or active under Event 006, or either conflict state is reserved by the current liberation plan.

The static SCN-008 edge matrix `EDGE-SCN-005` now names the two-order DON/DHC case and the force-all branch. `.tools/audit_event6_scenario_matrix.py` reads that current matrix and checks the DHC helper, both Event 006/005 trigger gates, the force-all gate, states 218/238, and the pending/active DON markers.

## Source-level scenario coverage and validation

The accepted design's source-level cases are:

- Existing DHC: the shared guard fails and IW-039 receives no candidate weight.
- Event 005 has current-plan reservations on state 218 or 238 but has not yet created DHC: the shared guard fails and IW-039 receives no candidate weight.
- Event 006 has reserved or marked DON pending/prepared/committed/active while Event 005 reaches DHC creation: the shared guard fails before Event 005 transfers either state.
- None of those DHC/DON markers or state reservations is present: the interlock passes, leaving the existing package, ownership, host-survival, origin, and attestation gates to decide eligibility.
- Event 006 has ended and its current release reservations are cleared: the active-origin predicate is false, so the Event 005 DHC path is not permanently suppressed by a historical commit receipt.

These are source-condition witnesses; they do not execute the scenarios in Clausewitz or prove event-order behavior in a running campaign. `python .tools/audit_event6_scenario_matrix.py` passed with 32 unique mode/intensity cells, eight edge IDs, and the expected success-only publication census. Its SCN-008 edge witness is static and does not execute any of the cases above.

Read-only `hoi4.event_inspect` lint calls for `chaosx.nr5_custom.14` and `chaosx.nr6.1`, with matching `hoi4.event_render` calls, returned `EVENT_INSPECTED_PARTIAL`/`EVENT_RENDERED_PARTIAL` at focused revision `02aadd003a66d42965ee451ee17108816105638af9ec6f0a31e9ffaa4138eafb`. They reported zero blocking diagnostics and zero skipped sources but selected only 3/4 event nodes, omitted approximately 42,860 workspace nodes, and projected zero helpers. The focused route reads event/on-action sources and does not expose the modified shared scripted trigger/effect, so it is not interlock evidence.

A bounded `hoi4.event_inspect(mode=state_flow)` request returned `EVENT_INSPECTED` in full analysis mode at revision `841eb72eda640af041a50082160622dd4ad69d28cd8f94b22b862520a9d80cda`, with 3,911 blocking diagnostics, 29,419 unresolved nodes, 19,711 helpers, and zero skipped sources. Artifact: [full state-flow report](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/815b5042500d753e87f6ba6898c9fa88a7efc746370be71372d7b0ea7ad4d8a9/ac1d4d5d1216c6a28f7594b0876e3db96cd916ff514e560c9f5cd7b145d3857c/event-state_flow-841eb72eda64.json). This workspace-wide report is partial; it does not isolate successful DON/DHC order cases.

`hoi4.event_compare` between the focused pre-edit graph revision `02aadd003a66d42965ee451ee17108816105638af9ec6f0a31e9ffaa4138eafb` and the full post-edit state-flow revision returned `EVENT_REVISION_NOT_CACHED` with no artifact. No semantic event comparison is claimed. The parent has not launched HOI4 or performed live-game validation.

## Remaining boundaries

The interlock does not add IW-039 to either the runtime adapter or content-attestation registry, create a DON setup/final-validation/cleanup dispatcher, change the one-package-per-wave limit, or implement the proposed Millerovo charter, OOB, decisions, focus group, AI, FORM-11, or package assets. The separate DON package addendum remains `unresolved`; imported root-level focus layout remains blocked by the user's selected architecture. No new on-action iteration or global world scan was added. Event 006 remains **HOLD / PARTIAL**.
