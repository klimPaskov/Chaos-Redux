# Event 006 pre-event overlay gate and capital-scope repair — 2026-08-28

## Scope

This bounded repair removes the remaining pre-event visibility path for the living vanilla-route overlays and prevents dormant Banat, Epirus, and Thrace shells from evaluating an invalid current-capital scope. It does not widen Event 006 admission, create a crisis category, expose a mission or cost before the event, alter package weights, or change fixed-anchor and supply semantics.

## Files changed

- `events/006_independence_wave.txt` sets the persistent `independence_wave_event6_runtime_unlocked` global marker only from the committed joint or standalone branch of `chaosx.nr6.1` immediately before the public report is delivered.
- `common/scripted_triggers/006_independence_wave_minor_overlay_triggers_registry.txt` adds `is_independence_wave_overlay_runtime_unlocked` and requires it in all thirteen living overlay route-active predicates: IW-005, IW-022, IW-025, IW-035, IW-059, IW-085, IW-101, IW-102, IW-105, IW-156, IW-196, IW-197, and IW-204.
- `common/decisions/006_independence_wave_balkan_decisions.txt` replaces AXX/Banat, BBX/Epirus, and BAX/Thrace current-capital control checks with `has_independence_wave_current_capital_controlled_by_root`; the unrelated BOS foundation check and all fixed-anchor checks remain unchanged.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` record the new authority and no-pre-event boundary.

## Behavior and evidence

Before Event 006 commits a joint or standalone result, every overlay route-active predicate fails at the shared global gate, so daily refreshes cannot initialize overlay values, ideas, missions, decisions, or categories. A failed or cancelled standalone attempt never sets the marker. After a committed result, existing route identity and local overlay flags continue to control activation and cleanup; the marker is intentionally historical and is not cleared by overlay suspension.

The owned-state helper checks for a controlled owned capital and therefore fails closed for an absent or dormant shell with no capital. It is used only for current-capital control semantics; fixed-anchor and supply-node checks were not substituted.

Focused static checks passed after the edit: allocator strict, country API strict, country-flag strict, FORM-16, and SCN-008 scenario matrix. Custom source assertions found no raw `capital_scope` in the AXX block, exactly thirteen overlay gate insertions, all thirteen overlay category keys still present, and marker writes only in the two committed root-event branches.

Fresh Event 006 MCP event inspect/render was attempted after the edit but remains blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with `artifactCount: 0` because the workspace artifact provenance manifest does not match its immutable address. No engine, save/load, GUI, probability, or live-runtime result is claimed.

## Simplifications, omissions, and blockers

None introduced by this repair. Event 006 remains HOLD / PARTIAL at the existing admission boundary; unresolved package, asset, rights, typed-probability, and MCP-artifact gaps remain outside this bounded patch.
