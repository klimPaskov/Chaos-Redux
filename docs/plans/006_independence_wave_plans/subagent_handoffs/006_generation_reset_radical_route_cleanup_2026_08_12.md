# Event 006 generation-reset radical-route cleanup

> Superseded by `006_generation_reset_route_exclusion_cleanup_2026_08_12.md`, which extends the same central fallback to all shared route-exclusion markers. This dated note remains as the original narrow finding.

## Scope

The shared Event 006 generation reset and active-origin termination paths now clear `independence_wave_radical_sovereignty_route_excluded`.

This marker is installed by package setup when a route matrix excludes the high-chaos radical lane, so it is generation-local state and must not survive a reused origin.

## Changed file

- `common/scripted_effects/006_independence_wave_effects.txt`

The marker is cleared in both `independence_wave_reset_current_generation` and `independence_wave_end_active_origin` as a defensive fallback after package dispatch cleanup.

## Validation

- At the pre-IW-044 snapshot, `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 30 attested packages, and 27 compatible reservation groups.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and 8 edge cases.
- `python -B .tools/audit_event6_flags.py --strict` passed all 102 registered flag families.
- `python -B .tools/audit_event6_gui_matrix.py` passed the five-tab semantic matrix and cleanup contract.
- `python -B .tools/audit_chaosx_country_tags.py` passed with 136 protected tags and zero external collisions.
- The touched effect file has balanced braces, and the central reset contains two explicit clears for the marker.

Fresh HOI4 MCP event evidence remains unavailable because the workspace returns `ARTIFACT_MANIFEST_INVALID` before source scanning.

## Boundary

This is a cleanup hardening patch only; it does not widen package attestation, change Join ordering, alter route eligibility, or promote any fail-closed country package.
