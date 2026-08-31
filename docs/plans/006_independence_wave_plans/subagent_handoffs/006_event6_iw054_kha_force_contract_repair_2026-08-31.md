# Event 006 IW-054 KHA force-contract repair handoff

Date: 2026-08-31

Status: COMPLETE for a package-local source repair; KHA remains FAIL-CLOSED for central Event 006 admission.

## Scope

The repair was limited to the IW-054 Khakassia package loader, its generation-bound force receipt, and the current authority prose that described that contract. No central adapter, attestation, reservation, planner weight, scenario preflight, deterministic Join, identity receipt, rights decision, portrait, flag, map binding, or pre-event surface was changed.

## Evidence and correction

The accepted IW-054 row in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` specifies the `mounted_mobile` force profile with military tradition score `55`.

The shared package tables are keyed by the numeric package id: `independence_wave_force_package_profile.p54` resolves to `mounted_mobile` (profile value `6`) and `independence_wave_force_package_military_tradition.p54` resolves to `55`. The adjacent `p55` row is the IW-055 Nenets contract (`mountain_frontier`, tradition `43`), so using p55 for KHA was an off-by-one cross-package reference.

The IW-054 setup and prepared triggers already require the package archetype `mountain_or_frontier`; the loader had incorrectly published `nomadic_or_dispersed`, which made its own setup gate impossible even before identity and roster gates were considered. The loader now publishes `mountain_or_frontier`.

The KHA prepared-setup trigger now checks the correct p54 tradition row while retaining the `mounted_mobile` profile check and package-id receipt. Its generation-rollover comment now names p54.

## Files changed

- `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`: IW-054 candidate archetype corrected to `mountain_or_frontier`.
- `common/scripted_triggers/006_independence_wave_siberian_package_triggers.txt`: IW-054 tradition receipt corrected from p55 to p54 and comment aligned.
- `docs/events/006_independence_wave/khakassia_package.md`: package contract records p54 `mounted_mobile` with tradition 55.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`: current KHA authority records the p54 contract.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`: current KHA authority records the p54 contract.
- `docs/specs/006_independence_wave_specs/quality/package_manifest.md`: KHA package manifest records the p54 contract.
- `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md`: KHA package boundary records the p54 contract.

## Validation

The focused allocator, country API, and flag validators remain green after the source correction: 149 publishers, 126 automatic/high-chaos selectable candidates, 138 SCN-008-ranked candidates, 40 runtime adapters, 32 attested packages, 29 compatible groups, 102 complete flags, and zero missing or duplicate country API rows. The exact automatic ladder remains 3/4/5/7/10 with World Collapse at 10.

No live or save-load claim is made. The available Event 006 MCP route remains partial and the typed probability compare route remains unavailable, so KHA is not promoted into central admission.

## Remaining KHA gates

KHA still lacks parent-owned identity and leadership provenance, a rights-cleared portrait, accepted neutral or route-specific flag provenance, Event 005 collision and host-remnant proof, typed probability evidence, central content attestation, deterministic Join, and live engine release evidence.
