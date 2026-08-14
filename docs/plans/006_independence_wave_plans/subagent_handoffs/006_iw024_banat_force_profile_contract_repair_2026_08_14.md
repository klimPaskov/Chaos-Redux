# IW-024 Banat force-profile contract repair

Date: 2026-08-14

## Disposition

The IW-024 package trigger now checks the accepted `industrial_security` force profile. No central adapter, attestation, Join order, or package admission surface was changed.

## Evidence

The accepted force mapping row in `006_force_package_mapping.csv` assigns IW-024 the `industrial_security` profile and military tradition 53. The shared profile table maps `industrial_security` to value 2, while the IW-024 force constants also use `p24 = 2`. The package trigger previously checked `mountain_frontier` (value 4), which could reject the otherwise correctly loaded IW-024 force package. The trigger now checks `constant:independence_wave_force_profile.industrial_security`.

The previously repaired IW-024 reinforcement mask remains aligned with the accepted five pathways: integrate militias, regional guards, secure depots, factory or rail guards, and capital-border defense.

## Changed files

- `common/scripted_triggers/006_independence_wave_banat_package_triggers.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw024_banat_force_profile_contract_repair_2026_08_14.md`

## Validation

Focused `hoi4.event_inspect` on the Banat package trigger returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics. The authoritative scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a1741caacd9cac1bd17dd468d852236b066006c350f75e84d8f166f54aa956d/eed8b5adb56a929b505251aa6a74d6a6a1812662caae68fa90ba15e67baf0c47/event-scan-d21fdfa2723e.json`. The partial status reflects deferred workspace-wide helper and lifecycle projection, not a package-local blocking diagnostic. Static allocator, SCN-008 matrix, flag-family, and protected-tag audits pass at the current 40-adapter, 32-attestation authority.

## Remaining limits

This repair proves source alignment only. The current MCP event scan is partial and no live-game execution or quantitative force-balance claim is made.
