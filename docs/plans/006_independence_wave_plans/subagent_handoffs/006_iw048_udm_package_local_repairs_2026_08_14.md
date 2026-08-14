# IW-048 UDM package-local repairs

Date: 2026-08-14

This handoff records three narrow source repairs applied to the package-local UDM implementation. Central adapter, attestation, normal/scenario preflight, deterministic Join, map, portrait, flag, and workbook surfaces remain untouched.

## Repairs

- `common/scripted_effects/006_independence_wave_udm_package_effects.txt` now loads `independence_wave_add_reinforce_factory_rail_guards` for the fifth IW-048 reinforcement pathway, matching the accepted IW-048 force row in `006_force_package_mapping.csv`.
- `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt` now requires `independence_wave_reinforce_factory_rail_guards` and rejects `independence_wave_reinforce_terrain_units`, so the prepared-package predicate matches the source mapping rather than accepting a terrain-unit substitute.
- Setup snapshots `independence_wave_generation_id` into `independence_wave_udm_package_generation_id`, and `independence_wave_cleanup_iw_048_udm` now requires that snapshot to equal the live generation plus `has_independence_wave_force_package_for_current_generation = yes`. The shared reset order runs package cleanup before the shared force-generation variable is cleared, preventing a stale cleanup call from mutating a later generation.
- UDM cleanup now restores the installed vanilla UDM popularity split: democratic 60, communism 10, neutrality 10, fascism 20.

## Current disposition

IW-048 UDM remains package-local and fail-closed. These repairs close the source-level force-path and cleanup-generation defects identified by the current audit, but they do not prove identity/portrait acceptance, neutral flag provenance, usable probability scenarios, or central admission. The package remains absent from central attestation, runtime preflight, scenario registration, and deterministic Join until the owning admission review supplies those gates.

The remaining package-local review item is the deliberate provisional politics choice in `independence_wave_initialize_udm_politics`; it sets a democratic provisional government and elections before a route government is chosen. This is retained as a design review item rather than silently changing the package contract.

## Validation evidence

The edited source blocks remain balanced and retain the existing tab-indented Clausewitz structure. Static source review confirms the UDM setup and prepared trigger now use the same five mapping pathways, and the cleanup guard compares the package-local setup snapshot with the shared current-generation helper already used by UDM readiness. No probability or balance claim is made because the current UDM mission pool still has no available scenario candidates and the AI-strategy adapter exposes no weighted surface.

The current mandatory probability inspection remains `PROBABILITY_SOURCE_INSPECTED` for `mission_ai_will_do`, with 11 candidates, zero available candidates, 15 required inputs, and `poolComplete = false`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5bde7918af716c7d91ce1b2bf3d04be7c0edbdb111bd674dee501bf52df13f39/2e20ab7c018ff65e2e2bce040a6982b9546754190048fe6ef15aebb597e46955/probability-inspect-cae802712e77.json`. The current focused Event 006 scan for `chaosx.nr6.350` is `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics and deferred workspace-wide helper/lifecycle analysis; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1eb9393def226e92453a0fca619a772a3f01c9187385858b183cd41c74e21a7c/e4791cb4b6d2ae70f89971c6350fca57baf6392cbe6d75b8ececafd768352a41/event-scan-741883f50501.json`.
