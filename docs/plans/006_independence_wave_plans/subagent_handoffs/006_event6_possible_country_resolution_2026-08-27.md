# Event 006 possible-country resolution handoff — 2026-08-27

## Scope

This tranche hardens the Event 006 allocator's country-scope resolution for carriers that are absent at game start or exist only as empty startup shells. It does not admit any new package, change the automatic count ladder, restore a pre-event crisis surface, or alter ownership outside the existing frozen-plan executor.

## Changes

- `common/scripted_effects/006_independence_wave_package_planner_effects.txt` now builds `global.independence_wave_plan_possible_countries` with `every_possible_country` before package weights and clears it with the plan contribution.
- `common/scripted_triggers/006_independence_wave_triggers.txt` now evaluates all 32 automatic package readiness wrappers through that registry, retaining each exact package identity, content-attestation, dormant-carrier, and anchor check.
- `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt` now routes all 32 admitted automatic `can_plan_independence_wave_package_iw_*` predicates through their matching runtime readiness wrappers. The remaining direct carrier checks were removed from IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-033, IW-038, IW-040, IW-041, IW-044, IW-045, IW-070, IW-071, IW-072, IW-173, and IW-184; adapter-only and route-only predicates remain unchanged.
- `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` now resolves each of its 138 registered carrier targets with an `every_possible_country` tag match before saving `liberation_candidate_country`.

## Rationale and references

The offline Scopes reference permits `every_possible_country` to reach absent country carriers and documents arrays as valid scope collections for `any_of_scopes`. Vanilla `effects_documentation.md` likewise defines `every_possible_country` as including countries that are not present. Event 005's terminal release code uses the same pattern to collect absent candidates before release. The change keeps Event 006's dormant-tag and exact-package predicates as the admission authority while removing direct static-tag resolution from the allocation and publisher paths.

## Validation and remaining risk

The source-level pass confirms all 32 admitted automatic `can_plan` predicates and all 32 readiness wrappers use the same absent-country-safe contract, and no direct one-line `save_event_target_as = liberation_candidate_country` publishers remain in the merged registry. The allocator, country API, strict flag-family, FORM-16, and SCN-008 scenario-matrix validators all pass after the patch. A post-patch `hoi4.event_inspect` trace for `chaosx.nr6.1` timed out after 180 seconds, matching the earlier state-flow and lint refresh timeouts; this is an MCP transport limitation, not a runtime receipt. HOI4 live execution and save/load behavior are not claimed here; the allocator still remains HOLD/PARTIAL until runtime receipts prove a committed non-empty plan.
