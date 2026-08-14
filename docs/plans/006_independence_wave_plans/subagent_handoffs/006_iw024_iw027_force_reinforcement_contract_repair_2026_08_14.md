# IW-024 and IW-027 force-reinforcement contract repair — 2026-08-14

## Disposition

The admitted IW-024 AXX and IW-027 BAX packages now match their accepted force mappings. The repair is limited to the package setup and readiness triggers; central adapter, attestation, preflight, and Join surfaces are unchanged.

## Defect and repair

The accepted AXX mapping requires integrate militias, regional guards, secure depots, factory or railway guards, and capital-border defense. Its p24 mask is `1095`, which decodes to `1 + 2 + 4 + 64 + 1024`. The AXX setup and trigger now use those five flags and exclude terrain units and professional officers.

The accepted BAX mapping requires regional guards, secure depots, terrain or frontier units, volunteer corridors, and capital-border defense. Its p27 mask is `1174`, which decodes to `2 + 4 + 16 + 128 + 1024`. The BAX setup and trigger now use those five flags and exclude militias, professional officers, and the other non-row pathways.

## Validation boundary

The package mask audit now checks all eleven package-local setup files and reports zero mismatches. Focus, decision, localisation, assets, central dispatcher, content-attestation, normal/scenario preflight, and deterministic Join surfaces were not changed by this repair. Focused Event MCP scans remain `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics because workspace helper/lifecycle projection is deferred. No weighted surface changed, so no probability claim is made from this repair.

## Remaining risks

The current Event 006 boundary, package admission receipts, and formable/portrait/flag gates remain unchanged. This source alignment does not authorize any additional package admission.
