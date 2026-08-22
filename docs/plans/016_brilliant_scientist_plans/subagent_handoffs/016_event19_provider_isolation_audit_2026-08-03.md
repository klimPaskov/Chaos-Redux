# Event 016 Event 019 provider-isolation audit - 2026-08-03

> **Superseded provider-inventory notice (2026-08-09):** This static audit covers seven historical provider rows and 77 callback definitions. Provider 522 and the expanded 18-ID Event 19 census were added later, so the counts and coverage table below are archival evidence rather than the current inventory. Use `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`, `016_core_runtime_handoff_map.md`, and `.tmp/event19_docs_curator_current.md` for current facts and unresolved MCP or lifecycle evidence.

## Status

The static provider-isolation audit is complete for the Event 016 integration surface. This tranche is documentation-only: no gameplay files, assets, localisation, models, or Event 019 core files were changed. The audit does not replace live Anomalous Rising, management, defeat, or final-cleanup acceptance.

## Scope and contract

The audited provider surface is `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`.
The shared contract is documented in `docs/events/019_infantry_spawn/systems/triggerable_scenario.md` and `docs/events/019_infantry_spawn/overview.md`: a provider must register one complete row, preserve the frozen family/provider identity through setup and cleanup, publish a private derivative package, remove provider-owned public additions before cleanup proof, and fail closed when a proof is missing.

## Provider coverage

`brilliant_scientist_register_event19_project_force_providers` conditionally registers exactly seven Event 019 provider rows:

| Provider | Family | Gate | Event 016 source |
| --- | --- | --- | --- |
| 504 | clone | `brilliant_scientist_project_force_cloning_active` | `clone_infantry` |
| 505 | robot | `brilliant_scientist_project_force_robotics_active` | `kruger_robot_frame` |
| 506 | paleogenetic | `brilliant_scientist_project_force_paleogenetics_active` | `kruger_paleogenetic_beast` |
| 507 | xenobiological | `brilliant_scientist_project_force_xenobiological_synthesis_active` | `kruger_xenobiological_assault` |
| 508 | alien infantry | `brilliant_scientist_project_force_alien_arms_active` or provider-neutral operational technology | `alien_infantry` through the shared contact and landing API |
| 509 | portal | `brilliant_scientist_project_force_teleportation_active` | `kruger_portal_raider` |
| 510 | temporal | `brilliant_scientist_project_force_temporal_active` | `kruger_temporal_guard` |

The template callbacks select the corresponding generic Event 019 division name and map each provider to an existing Event 016 unit/equipment package.
Clones intentionally use vanilla `infantry_equipment`; all other rows use the Event 016 equipment definitions. No provider row contains an entity, `.mesh`, or `.anim` reference, so model work remains deferred as requested.

## Callback parity

All seven providers define each of the eleven required callback slots exactly once (77 callback definitions total):

1. `register`
2. `event19_evaluate_eligibility`
3. `event19_build_template`
4. `event19_spawn_unit`
5. `event19_reconcile_sustainment`
6. `event19_evaluate_management`
7. `event19_pay_management_action`
8. `event19_refund_management_action`
9. `event19_setup_derivative`
10. `event19_remove_public_additions`
11. `event19_cleanup_derivative`

The registration call is reached from `brilliant_scientist_rebuild_project_force_runtime_package`, after the history-derived package has been rebuilt. The ledger-change synchronizer also rebuilds the package for KRG or for an existing package state, so provider availability is not dependent on a one-time startup order.

## Parent-state isolation and cleanup

The shared setup path is guarded by the Event 019 parent-boundary trigger and the exact family/provider pair. It clears parent-isolation and public-package proofs before dispatch, then the provider helper sets the isolation proof only after the shared and Event 016 checks pass. Setup installs only the derivative's neutral leader, one provider-owned family idea, route state, and the one-time `chaosx.nr19.918` release report. The derivative is not allowed to inherit parent event flags, stages, progression markers, or parent-owned public additions.

Provider cleanup resolves the stored exact family/provider row rather than rechecking current provider availability. It removes the provider-owned leader, ideas, route state, and public-package marker first; defeat dispatches `chaosx.nr19.919` once, and the shared Event 019 phase then owns private-ledger, formation, and common derivative teardown. Final cleanup uses the same guarded path and marks cleanup only after provider-owned additions are absent.

## Static evidence

The bounded audit script checked:

- seven exact registrations (504-510), each with the required activation gate;
- eleven callback names for every provider, each defined exactly once;
- runtime rebuild registration and ledger-change synchronization call sites;
- every referenced Event 016 subunit and equipment definition;
- parent-isolation, public-package, report, defeat, and final-cleanup tokens;
- balanced Clausewitz braces; and
- absence of `entity =`, `.mesh`, and `.anim` references in the provider file.

The script returned `static provider-isolation audit: ok`. This is source-level evidence only. A direct Event Inspector scan of `chaosx.nr19.918` exceeded the available output context after starting, so it is not reported as a successful inspector pass. The requested completion-auditor subagent could not initialize because its required Meshy MCP server timed out during tool discovery; no subagent pass is claimed.

## Remaining acceptance

User-owned live validation is still required for Anomalous Rising, provider management payment/refund, parent-war defeat, final cleanup, and cross-save parent-state isolation. The seven Event 016 unit packages remain intentionally model-free and need the later 3D workflow before visual/entity wiring. The native CBRN callback boundary remains the blocker for biological stockpile and delivery outcomes; no fallback ledger or free payload was introduced.
