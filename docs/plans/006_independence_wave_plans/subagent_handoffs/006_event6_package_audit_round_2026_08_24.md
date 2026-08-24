# Event 006 country-package audit round — 2026-08-24

## Disposition

This is an audit-only handoff. No gameplay, admission, package, map, identity, force, AI, or cleanup file was changed by this round, and no package was promoted. The Event 006 source-of-truth boundary remains HOLD/PARTIAL at 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, 161 unattested selectable rows out of 193 non-overlay rows, and eight adapter-only fail-closed IDs.

The requested `docs/specs/006_independence_wave_specs/005_package_contracts.md` path is absent in the repository. The audit therefore used the current design authority `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md` and the implementation authority `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`.

## Country-package coverage checklist

- Central runtime adapter registry is present in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63`.
- Central content-attestation registry is present in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-202` and contains the current 32 IDs only.
- Exact preflight requires dormant carrier, adapter, content attestation, origin safety, and package/tag identity in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:207-260`.
- Package planning rechecks content attestation before reservation and weighting in `common/scripted_effects/006_independence_wave_package_planner_effects.txt:95-150`, `:484-702`.
- Frozen setup requires origin preparation and package setup completion before the selected row counts as prepared in `common/scripted_effects/006_independence_wave_execution_effects.txt:563-595`.
- Final validation dispatches package-local validation and the shared generic focus/AI contract in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:45-91` and `common/scripted_effects/006_independence_wave_execution_effects.txt:604-631`.
- Cleanup dispatch remains centralized across the package groups in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:93-119`.
- Static allocator, country API, flag, scenario, FORM-16, and Statehood Ledger audits passed during this round; these are source/static checks and are not live proof.

## Package and file-surface checklist

The current attested package IDs are IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-033, IW-038, IW-040, IW-041, IW-044, IW-045, IW-070, IW-071, IW-072, IW-173, and IW-184.

The runtime adapter-only IDs remain IW-013/NAV, IW-015/GLC, IW-043/CHU, IW-058/ASY, IW-093/DOX, IW-098/SOK, IW-177/FIJ, and IW-179/FSM. They appear in the adapter OR-list but not the attestation OR-list, so the exact preflight remains fail-closed; adapter presence is not package admission evidence.

The current attested anchor bindings are IW-001/SCO/121, IW-002/WLS/122, IW-004/BRI/14, IW-006/AFX/34, IW-007/AGX/36, IW-008/RHI/51, IW-009/BAY/52, IW-010/AJX/42, IW-012/ICE/100, IW-014/CAT/165, IW-017/COR/1, IW-018/ARX/114, IW-019/ASX/115, IW-023/TRA/84, IW-024/AXX/82, IW-026/MAC/106, IW-027/BAX/184, IW-028/BBX/185, IW-029/BOS/104, IW-030/MNT/105, IW-031/KOS/802, IW-033/KAR/146, IW-038/RUT/73, IW-040/KUB/234, IW-041/CRI/137, IW-044/TAT/249, IW-045/BSK/651, IW-070/ARM/230, IW-071/GEO/231, IW-072/AZR/229, IW-173/HAW/629, and IW-184/HBX/378.

No missing or stale package identifier was found in the central adapter-versus-attestation comparison. No adapter-only ID was promoted, and no new package-local file was created.

## Missing or stale package surfaces

No bounded admission bug was identified. The source-of-truth map explicitly directs the parent to preserve 32/29/161/40 and not widen admission from adapters alone.

The eight adapter-only rows remain incomplete on one or more identity, flag, portrait/source, force, typed-probability, host, collision, or cleanup gates. The current registry gap map `docs/plans/006_independence_wave_plans/subagent_handoffs/006_current_registry_gap_map_2026_08_15.md` also keeps IW-046, IW-049, IW-051, IW-052, IW-054, IW-055, IW-057, and IW-060 outside central admission; this audit found no evidence to change that boundary.

## Map and state setup

The package binding CSV `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` remains the authority for the 32 anchor states listed above. No map write was performed.

Read-only `hoi4.map_inspect` for state 121 succeeded with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9cabee3f387f75ad1f5aacfcbd54a8cc9a7bd7b2547213e421e2eac22f37c76/2245480169550d17ad146b083d718882127a2846bf95fd85d21a166035d4e067/map-inspect.3695c5c5e7223ef1.json`; the narrow result had no unknown/missing geometry IDs and passed state-region membership and network checks. The 32-state batch timed out after 180 seconds, so no whole-anchor map acceptance is claimed.

The same map receipt reported global unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics from `mod:map/buildings.txt`; these are not evidence of a package-local anchor defect. `hoi4.map_render` produced a validated offline state-layer artifact at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c8a38f2a0c09e2af8e7995c5a27803696c79c642b4d19a9fb7e001d8d2e9ae9/fc654777d43e626e50e5e3d5e8bb3820a3dd2705d754538af09605764b5722cb/map-state.png`.

## Politics, leaders, portraits, flags, advisors, and parties

No package identity or political surface was changed. The current package contracts and source-of-truth map remain the evidence for party, government, leader, portrait, flag, advisor, and host-survival gates.

The static flag audit reports 102 registered Event 006 tags, 102 complete flag families, and zero incomplete families. This does not replace source/rights evidence for grounded portraits or live visual review.

No Event 006 advisor icon is required or authorized by the current authority. Portrait-worker provenance and user-supplied grounded finals remain separate package gates; no placeholder was promoted by this round.

## Focus, decision, idea, and asset surfaces

The shared Event 006 focus surface remains HOLD. The current authority records 184 focuses, 195 connectors after prerequisite repair, zero crossings, zero node intersections, seven authored Event 006 layout warnings, and fourteen unrelated vanilla continuous-focus icon diagnostics. No focus route or icon was changed.

The read-only focus inspect and render calls for `common/national_focus/006_independence_wave_focus.txt` / `independence_wave_focus_tree` each exceeded the installed MCP 180-second timeout during this round. The prior source-linked focus artifacts remain usable evidence, but no fresh clean focus acceptance is claimed.

The decision and idea surfaces were source-audited through the package dispatch and existing static audits. No package-specific decision, idea, cost, or localisation patch is justified by this round.

## Starting military, technology, industry, supply, and production

No package starting setup or force mapping was changed. The runtime preflight still requires the package-local force mapping probe and the final package validation still requires the shared force contract; these gates are visible in `common/scripted_effects/006_independence_wave_execution_effects.txt:205-260` and `:604-631`.

The installed MCP package exposes no Technology Tree Viewer. No technology-tree evidence was substituted or claimed; technology inheritance remains a documented unresolved limitation where package-specific proof is required.

## AI and playability

The allocator static witness reports 20 admissible standalone packages and the automatic target ladder 3/4/5/7/10, with World Collapse targeting 10. This is source/static capacity evidence only and is not live transaction or playability proof.

The required named `chaosx_ai_probability_auditor` route was unavailable in the installed callable tools. Direct `hoi4.probability_inspect` for `common/ai_strategy/006_independence_wave_banat.txt` with the `ai_strategy_factor` adapter also exceeded the 180-second timeout. Therefore no same-scenario probability comparison or quantitative package AI-balance claim is made.

The package planner requires exact content attestation before positive allocation weight in `common/scripted_effects/006_independence_wave_package_planner_effects.txt:484-702`, so no AI or adapter observation justifies admission widening.

## Manual Event 006 no-country finding

`events/006_independence_wave.txt:11-61` defines `chaosx.nr6.1` as a hidden, triggered-only orchestrator. Its standalone branch calls `independence_wave_prepare_and_execute_standalone_incident` and opens `chaosx.nr6.2` only when `independence_wave_standalone_incident_committed` is set. `chaosx.nr6.2` itself requires a positive frozen presentation count at `events/006_independence_wave.txt:68-76`.

The standalone effect clears terminal receipts, initializes the automatic Event 006 plan, allocates only after collecting/allocating phase checks, executes the frozen package plan, and sets the committed receipt only when the global plan phase is committed at `common/scripted_effects/006_independence_wave_execution_effects.txt:899-946`. Otherwise it marks finalization failure, rollback, or pre-mutation cancellation and suppresses the report at `:947-980`.

Therefore “manual Event 006 has no countries” means only that no committed standalone plan was available to present; it does not identify a single live rejection cause. Likely source-level branches include no valid liberation-release call, an exhausted pool after exact attestation/anchor/host/force gates, or setup/finalization rollback. A runtime receipt or live save observation is required to distinguish them, and none is claimed here.

## Six package strategic-cost trigger files

This round did not change any of the six files. Their pre-existing working-tree diffs remove only the `war_support_minor` condition from local strategic-cost helpers:

- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:51-56`, helper `can_pay_independence_wave_komi_strategic_cost`.
- `common/scripted_triggers/006_independence_wave_kosovo_package_triggers.txt:41-46`, helper `can_pay_independence_wave_kos_strategic_cost`.
- `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt:43-48`, helper `can_pay_independence_wave_kub_strategic_cost`.
- `common/scripted_triggers/006_independence_wave_ruthenia_package_triggers.txt:43-48`, helper `can_pay_independence_wave_rut_strategic_cost`.
- `common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt:43-48`, helper `can_pay_independence_wave_tat_strategic_cost`.
- `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:50-55`, helper `can_pay_independence_wave_udm_strategic_cost`.

Those six local decision-cost edits do not appear in `events/006_independence_wave.txt`, the central planner, the package allocator, or the central adapter/attestation OR-lists, so they cannot explain the absence of countries from a manual Event 006 allocation. They are outside this audit’s ownership and must not be reverted or folded into an admission patch without the owning agent’s direction.

## Validation and limitations

The following task-specific static checks passed: `.tools/audit_event6_allocator.py`, `.tools/audit_event6_country_api.py`, `.tools/audit_event6_flags.py`, `.tools/audit_event6_scenario_matrix.py`, `.tools/audit_event6_form16.py`, and `.tools/audit_event6_gui_matrix.py`.

Read-only MCP evidence succeeded for a narrow map inspect, full offline map render, status-window GUI inspect/render, and source-linked Event 006 event inspect/render. Event inspect/render returned partial validation because large-workspace helper/lifecycle projections were deferred. GUI inspect reported global graph diagnostics and visible-overlap fidelity issues without proving an Event 006 package defect.

Meaningful validation skipped: no live HOI4 run, no save/load observation, no live event receipt, no full 32-state map inspect, no fresh focus inspect/render acceptance due to 180-second timeout, no package-level typed probability comparison because the named auditor route was unavailable and direct probability inspect timed out, and no Technology Tree Viewer evidence because the installed package exposes none. No live proof is claimed.

## Parent handoff and remaining gates

Preserve fail-closed central admission at 32/29/161/40 and retain the eight adapter-only IDs outside content attestation. Do not use the six strategic-cost trigger diffs as evidence for package admission or manual Event 006 country selection. For a concrete zero-country runtime diagnosis, capture the standalone terminal receipt or equivalent parent-owned runtime evidence and map it to the branches at `common/scripted_effects/006_independence_wave_execution_effects.txt:943-980`.

Remaining gates are the whole-event focus HOLD, package-specific identity/source/portrait and host/collision evidence where documented, package force/technology inheritance proof, required named probability-auditor scenario/comparison, full map-anchor inspection, and live transaction/save-load evidence. This round found no small safe package patch.
