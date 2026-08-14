# IW-002 and IW-050 force-tradition contract repair

Date: 2026-08-14

## Disposition

Two source-level military-tradition references were aligned with the accepted force mapping. No central adapter, attestation, preflight, Join order, or package admission surface was changed.

## Repairs

- The shared `independence_wave_force_package_military_tradition` table now assigns `p2 = 58`, matching the accepted IW-002 mapping row and its package trigger.
- The IW-050 Komi package trigger now checks `p50`, its own package entry, instead of `p55`.

## Evidence

The mapping table requires IW-002 tradition 58 and IW-050 tradition 55. Before this repair, the shared table held `p2 = 60`, and the IW-050 trigger referenced `p55`, whose table value is 43. The corrected references resolve to 58 and 55 respectively.

The full 206-row force-profile table comparison reports zero mismatches. The full 206-row military-tradition table comparison reports zero mismatches. The package-trigger sweep reports 38 profile checks and 35 tradition checks with zero mismatches.

## Changed files

- `common/script_constants/006_independence_wave_force_package_constants.txt`
- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw002_iw050_force_tradition_contract_repair_2026_08_14.md`

## MCP evidence

Focused `hoi4.event_inspect` on the shared force constants returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d986eefa28c04997dd1eb5894de77c70db3c27fe67dab4b6d5a12d11aa444a45/f8b164c126b83dbc364dd6a3f4db25678e3f6fdb000953ad3e99e23bd0d91020/event-scan-d21fdfa2723e.json`.

Focused `hoi4.event_inspect` on the Komi package trigger returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5d8e6068eb72be205775efb41b32c0f564a3c7785eb35cb87395c1bd0239577/23961465f85b7c8bdd561a3a4330eb0f5c41546ea158609feb3160abde35bab5/event-scan-d21fdfa2723e.json`.

The partial status reflects deferred workspace-wide helper and lifecycle projection. It is not a package-local blocking diagnostic.

## Remaining limits

These repairs establish source-table and trigger parity only. They do not provide live-game execution or quantitative force-balance evidence.
