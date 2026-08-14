# IW-050 Komi force-reinforcement contract repair — 2026-08-14

> Superseding correction (2026-08-14): the first version of this handoff attributed the Komi row to `p55`. Package keys are numeric package IDs, so IW-050 is `p50` and IW-055 is `p55`. The current source keeps the Komi five-pathway mask on `p50` and restores the Nenets `p55` row.

## Disposition

The package-local IW-050 force row is source-aligned after a narrow constants repair. Central adapter, content-attestation, normal/scenario preflight, and deterministic Join surfaces remain unchanged and fail-closed.

## Defect and repair

The accepted IW-050 mapping in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` requires five reinforcement pathways: integrate militias, regional guards, secure depots, terrain units, and professional officers. The Komi package setup and prepared trigger already use those five flags.

The accepted IW-050 mapping uses `p50 = 647`, which decodes to integrate militias, regional guards, secure depots, terrain units, and professional officers: `1 + 2 + 4 + 128 + 512`. The accepted IW-055 mapping uses `p55 = 403`, which decodes to integrate militias, regional guards, volunteer corridors, terrain units, and foreign arms. The current shared table preserves both rows according to their package mappings.

No package-local effect, trigger, decision, focus, localisation, central dispatcher, attestation, preflight, Join, formable, portrait, or flag wiring was widened by this repair.

## Evidence and validation

The source crosswalk and current package-core handoff identify IW-050 `p50` as profile `mountain_frontier`, tradition `55`, reinforcement mask `647`, and no navy or air inheritance. The current package setup at `common/scripted_effects/006_independence_wave_komi_package_effects.txt` and readiness trigger at `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt` agree with that package contract. The separate IW-055 `p55` row remains profile `4`, tradition `43`, reinforcement mask `403`, inheritance mask `0`, and research-sensitive flag `1` in the shared tables.

Static source checks should confirm balanced constants and package references. A fresh narrow Event 006 MCP inspection is required after this source change; the result must be treated as partial if the workspace helper/lifecycle projection remains deferred. No weighted surface was changed, so no probability claim is made from this repair.

The post-correction focused `hoi4.event_inspect` scans returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics for `common/script_constants/006_independence_wave_force_package_constants.txt` and `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt`. The linked artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aaab05df96fdef0afcc67c4ea318302f0fddfcc37d7e59507ba6c7da99b731e8/336f98b54e73acf5a1ad79602e7a7e6ed167e89e0e821c644789fab4e830aed5/event-scan-d21fdfa2723e.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8367776c5fe72939f5c641b8c7855255e909c1501c74b2e6dc838550e5e80539/05b9924594dbbc99e961b1518023debd6a4b0e5f2b913854c14e6197782b218a/event-scan-d21fdfa2723e.json`. The scans remain partial because the workspace-wide helper and lifecycle projection is deferred, but they found no blocking diagnostics.

## Remaining blockers

IW-050 remains package-local and unadmitted. Exact Pavel Murashev portrait identity/rights, neutral or route-specific flag provenance, typed mission fixtures, and central admission evidence remain unresolved. This constants repair does not authorize adding IW-050 to any central list.
