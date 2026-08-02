# IW-030 Montenegro preflight hardening handoff

Date: 2026-08-02 (Europe/Kyiv).

Scope: bounded Event 006 IW-030 Montenegro (`MNT`) candidate and preflight trigger hardening. This patch does not promote IW-030 into the compile-time content-attestation set.

## Changed files

- `common/scripted_triggers/006_independence_wave_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt`
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`
- `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt`

## Changed identifiers and behavior

- Added `is_independence_wave_exact_package_iw_030_tag_available` in `006_independence_wave_package_triggers.txt`. The dormant candidate proof now requires the exact `MNT` original tag, capital state `105`, a currently available state-105 anchor, a living non-MNT owner/host, and the shared origin-safety exclusions. The wrapper remains candidate-safe and does not require active-country setup receipts that cannot exist before release.
- Replaced the IW-030 planner's legacy `MNT = { is_independence_wave_candidate_tag_available = yes }` gate with the exact wrapper in `can_plan_independence_wave_package_iw_030`.
- Added `is_independence_wave_exact_package_iw_030_runtime_ready` in the Montenegro package trigger file. The post-release proof requires the active MNT/package-id contract, complete IW-030 setup, current-generation force receipt, state-105 ownership/control and capital, the stored former-host protected-state contract, and a non-ended origin lifecycle. The existing `independence_wave_cleanup_iw_030_montenegro` effect remains the cleanup owner; the `origin_ended` exclusion prevents a cleaned origin from satisfying runtime readiness.
- Added the exact IW-030 candidate wrapper branch to `is_independence_wave_runtime_package_preflight_ready` and `is_independence_wave_scenario_package_preflight_ready`.
- `has_independence_wave_runtime_package_content_attestation_for_execution_id` remains unchanged and still omits `iw_030`; normal execution and SCN-008 therefore remain fail-closed for this package until a separate admission decision closes the portrait, focus, and content-audit gates.

## Before and after

Before, IW-030 used the dormant legacy candidate-content flag path, had no exact package wrapper, and had no normal or SCN-008 exact MNT identity branch. After, candidate planning uses a static exact MNT/anchor/host wrapper, dispatch uses exact IW-030 identity branches, and a separate runtime trigger records the setup, force-generation, lifecycle, and cleanup boundary without making the absent-tag planner require active-country state.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, and the unchanged 14-package attestation set.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all SCN-008 cells and eight edge-case receipts.
- Targeted trigger assertions found the IW-030 wrapper, planner replacement, normal branch, scenario branch, runtime setup and force receipts, and lifecycle cleanup exclusion; they also confirmed no `iw_030` content-attestation branch was added.
- Targeted brace-count checks passed for all four gameplay trigger files, and `git diff --check` reported no whitespace errors.
- Required offline Paradox wiki pages and the relevant vanilla HOI4 trigger/effect/script documentation were consulted before editing.

## Skipped checks and remaining risks

- No in-game launch or live save validation was performed; live consumer validation belongs to the parent/user boundary.
- No map write or map rewrite was attempted. State 105 remains the vanilla MNT/YUG anchor and its map safety is outside this narrow trigger patch.
- The installed MCP exposes no Technology Tree Viewer, so no technology render was available.
- IW-030 remains outside content attestation and cannot execute through normal release or SCN-008 until the parent closes the existing grounded portrait, shared focus geometry, and broader package admission gates.
