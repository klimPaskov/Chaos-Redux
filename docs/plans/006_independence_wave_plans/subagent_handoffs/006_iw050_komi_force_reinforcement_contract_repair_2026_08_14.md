# IW-050 Komi force-reinforcement contract repair — 2026-08-14

## Disposition

The package-local IW-050 force row is source-aligned after a narrow constants repair. Central adapter, content-attestation, normal/scenario preflight, and deterministic Join surfaces remain unchanged and fail-closed.

## Defect and repair

The accepted IW-050 mapping in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` requires five reinforcement pathways: integrate militias, regional guards, secure depots, terrain units, and professional officers. The Komi package setup and prepared trigger already use those five flags.

The shared reinforcement mask for `p55` was `403`, which decodes to integrate militias, regional guards, volunteer corridors, terrain units, and foreign arms. That value contradicted both the accepted mapping and the package-local setup/trigger contract. `common/script_constants/006_independence_wave_force_package_constants.txt` now sets `p55 = 647`, which decodes to the five intended pathways: `1 + 2 + 4 + 128 + 512`.

No package-local effect, trigger, decision, focus, localisation, central dispatcher, attestation, preflight, Join, formable, portrait, or flag wiring was widened by this repair.

## Evidence and validation

The source crosswalk and package-core handoffs already identify `p55` as profile `mountain_frontier`, tradition `55`, reinforcement mask `647`, and no navy or air inheritance. The current package setup at `common/scripted_effects/006_independence_wave_komi_package_effects.txt` and readiness trigger at `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt` now agree with that mask. The other p55 rows remain profile `4`, tradition `43`, and inheritance `1` in their respective shared tables.

Static source checks should confirm balanced constants and package references. A fresh narrow Event 006 MCP inspection is required after this source change; the result must be treated as partial if the workspace helper/lifecycle projection remains deferred. No weighted surface was changed, so no probability claim is made from this repair.

## Remaining blockers

IW-050 remains package-local and unadmitted. Exact Pavel Murashev portrait identity/rights, neutral or route-specific flag provenance, typed mission fixtures, and central admission evidence remain unresolved. This constants repair does not authorize adding IW-050 to any central list.
