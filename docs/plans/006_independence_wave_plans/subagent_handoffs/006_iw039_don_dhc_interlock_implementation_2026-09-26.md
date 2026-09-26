# IW-039/DON and Event 005 DHC interlock

**Disposition:** implemented at source/static-witness level; both-order runtime behavior remains unverified, and IW-039 stays unadmitted.

## Acceptance basis

The user explicitly accepted state 245/Millerovo as the required Event 006 anchor and capital, state 238/Volgodonsk as optional compact territory, vanilla state 218 outside IW-039, and mutual exclusion between Event 005 DHC and Event 006 IW-039 in both event orders. The decision and capacity-one `RG-DON-KUBAN` rule are recorded in Part 5; see commit `5cccc8b4e`.

## Source changes

`common/scripted_triggers/005_006_liberations_collision_triggers.txt` now defines three context-specific guards. `is_don_dhc_cross_event_collision_clear` protects Event 006 candidate weighting against the DHC successor receipt, DHC ownership/control, active Event 005 ownership/control, and Event 005-owned current-plan reservations of states 218/238. It also rejects reserved/pending/prepared/active DON markers. `is_soviet_collapse_dhc_creation_clear` protects Event 005 DHC creation against an existing DHC receipt and pending/reserved/prepared/active IW-039, without rejecting ordinary Event 005 merely because SOV is its active host. `is_iw039_dhc_runtime_preflight_clear` checks DHC receipt and state ownership/control before final package preflight; state 218 rejects Event 005 reservations and any IW-039 reservation, while state 238 rejects Event 005 reservations and permits the IW-039 compact reservation. A competing non-Event-005 state-238 reservation passes this DHC-specific preflight and remains subject to the ordinary compact-trim and plan-collision checks. The active-origin predicate treats an ended Event 006 origin as inactive; the guards do not latch on the historical `independence_wave_origin_committed` receipt.

`common/scripted_triggers/005_soviet_collapse_triggers.txt:8194-8208` calls `is_soviet_collapse_dhc_creation_clear` from normal `can_soviet_collapse_spawn_dhc`, before the existing 218/238 Soviet ownership and control tests.

`common/scripted_effects/005_soviet_collapse_effects.txt:23503-23531` applies `is_soviet_collapse_dhc_creation_clear` to the force-all DHC branch before the state-transfer effects. The ordinary branch remains gated by `can_soviet_collapse_spawn_dhc`; the guard therefore applies before either path transfers states 218 or 238 and runs `soviet_collapse_setup_dhc_successor`.

`common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:345-352` calls `is_don_dhc_cross_event_collision_clear` before IW-039 enters the Region-04 candidate pool. The final release gate in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:207-220` calls `is_iw039_dhc_runtime_preflight_clear` only for IW-039, after the country reservation is expected to exist. A conflicting Event 005 state reservation still fails there; an optional 238 reservation by another Event 006 package is left to the ordinary compact trim.

The static SCN-008 edge matrix `EDGE-SCN-005` now names the two-order DON/DHC case and the force-all branch. `.tools/audit_event6_scenario_matrix.py` reads that current matrix and checks the DHC helper, both Event 006/005 trigger gates, the force-all gate, states 218/238, and the pending/active DON markers.

## Source-level scenario coverage and validation

The accepted design's source-level cases are:

- Existing DHC: the shared guard fails and IW-039 receives no candidate weight.
- Event 005 owns/controls or has a current plan reservation for state 218 or 238 but has not yet created DHC: the candidate guard fails and IW-039 receives no candidate weight; final preflight rechecks the Event 005 reservation after IW-039's own reservation is present.
- Event 006 has reserved or marked DON pending/prepared/active while Event 005 reaches DHC creation: the Event 005 creation guard fails before either state transfer.
- DHC successor receipt or DHC/active-Event-005 ownership/control of 218/238 remains when Event 006 reaches its final preflight: the package-specific final guard fails. An Event-005-owned state-238 reservation fails; the IW-039 optional reservation passes, and a competing non-Event-005 reservation remains for the ordinary compact-trim and plan-collision checks.
- None of those DHC/DON markers or state reservations is present: the interlock passes, leaving the existing package, ownership, host-survival, origin, and attestation gates to decide eligibility.
- Event 006 has ended and its current release reservations are cleared: the active-origin predicate is false, so the Event 005 DHC path is not permanently suppressed by a historical commit receipt.

These are source-condition witnesses; they do not execute the scenarios in Clausewitz or prove event-order behavior in a running campaign. `python .tools/audit_event6_scenario_matrix.py` passed with 32 unique mode/intensity cells, eight edge IDs, and the expected success-only publication census. Its SCN-008 edge witness is static and does not execute any of the cases above.

The final post-edit read-only `hoi4.event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` at revision `02aadd003a66d42965ee451ee17108816105638af9ec6f0a31e9ffaa4138eafb` and graph hash `65d862ddd1a7893bfede856be54280246099dc7c95c67203da75673e889a9695`. It reported zero blocking diagnostics, zero skipped sources, zero projected helpers, and 8,910 unresolved nodes. Artifact: [current focused lint](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8bdb20a9476ad2606e66063ed0ebbcdcdfb85375910bede37ba65550c9eb79e/97a9cd89823913d964160f649f1550fea3c6b1d3171e5723ff960adc16768471/event-lint-02aadd003a66.json).

The matching final `hoi4.event_render(view=overview)` returned `EVENT_RENDERED_PARTIAL` at the same revision and graph hash, with layout hash `340071ffd5797720635ee88ef724d794ec40a8b419d505221944ec59b8ab1bb8`, five selected nodes, 42,859 omitted nodes, zero projected helpers, 2,193 diagnostics, zero blocking diagnostics, and zero skipped sources. Artifact: [current Event 006 overview render](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4846e4676b85e24d1a34f6b8470cbd59af980235e9cb934ced1438add38e4a75/8002ced7f8b836ac9dc2393f4242391f918a76c1144e3a69dfe485a8a6cca260/event-overview-02aadd003a66.png). The focused routes read event and on-action sources but do not expose the changed shared triggers/effects, so their unchanged graph revision is not interlock evidence.

A bounded `hoi4.event_inspect(mode=state_flow)` request returned `EVENT_INSPECTED` in full analysis mode at revision `841eb72eda640af041a50082160622dd4ad69d28cd8f94b22b862520a9d80cda`, with 3,911 blocking diagnostics, 29,419 unresolved nodes, 19,711 helpers, and zero skipped sources. Artifact: [full state-flow report](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/815b5042500d753e87f6ba6898c9fa88a7efc746370be71372d7b0ea7ad4d8a9/ac1d4d5d1216c6a28f7594b0876e3db96cd916ff514e560c9f5cd7b145d3857c/event-state_flow-841eb72eda64.json). This workspace-wide report predates the final package-preflight guard and is partial; it does not isolate successful DON/DHC order cases.

`hoi4.event_compare` between the focused pre-edit graph revision `02aadd003a66d42965ee451ee17108816105638af9ec6f0a31e9ffaa4138eafb` and the full post-edit state-flow revision returned `EVENT_REVISION_NOT_CACHED` with no artifact. A final same-revision comparison attempt timed out after 180 seconds and returned no artifact. No semantic event comparison is claimed. The parent has not launched HOI4 or performed live-game validation.

## Remaining boundaries

The interlock does not add IW-039 to either the runtime adapter or content-attestation registry, create a DON setup/final-validation/cleanup dispatcher, change the one-package-per-wave limit, or implement the proposed Millerovo charter, OOB, decisions, focus group, AI, FORM-11, or package assets. The separate DON package addendum remains `unresolved`; imported root-level focus layout remains blocked by the user's selected architecture. No new on-action iteration or global world scan was added. Event 006 remains **HOLD / PARTIAL**.
