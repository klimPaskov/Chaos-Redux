# Event 006 shared-focus presentation and AI compensation handoff

Date: 2026-08-02

## Scope

This parent-owned patch closes the presentation and implicit-AI weighting gap created by the Event 006 shared-tree geometry reflow. The reflow removed 37 direct prerequisite edges from 33 focus blocks so the tree could render without crossings, intersections, long connectors, or cramped same-row pairs. The source still keeps the exact gating in `available` blocks.

Six high-value edges are restored as visible prerequisite lines:

- `independence_wave_grant_military_autonomy` and `independence_wave_standardize_with_league` to `independence_wave_found_professional_defense_institution`.
- `independence_wave_complete_founding_settlement` to `independence_wave_prepare_traditional_confirmation`.
- `independence_wave_complete_founding_settlement` to `independence_wave_establish_emergency_command`.
- `independence_wave_complete_founding_settlement` to `independence_wave_open_guarantor_talks`.
- `independence_wave_bay_reconcile_landesbank_accounts_focus` to `independence_wave_bay_entrust_mountain_guardians_focus`.

The remaining 31 hidden prerequisite edges remain exact `available` gates. Each affected focus now has an explicit AI modifier using `constant:independence_wave_focus_ai.prerequisite_boost = 1.5`, matching vanilla's implicit AI nudge for a just-completed declared prerequisite. Multi-parent hidden gates use an `OR` modifier so the boost follows the same branch semantics as the source gate.

## Source changes

- `common/national_focus/006_independence_wave_focus.txt`
  - Restores the six visible edges above.
  - Removes redundant `has_completed_focus` availability checks for the restored single-parent edges.
  - Keeps the capstone's `available` OR groups intact, but removes the restored parents from its explicit compensation modifier.
  - Applies the compensation modifier to the remaining 31 hidden edges only.
- `common/script_constants/006_independence_wave_focus_constants.txt`
  - Adds the centralized `prerequisite_boost` tuning value.

## Validation evidence

Static source comparison against the pre-reflow tree reports 184 focus IDs in both versions, 31 remaining removed prerequisite edges, 31 matching compensation references, and no extra compensation references.

The latest deterministic focus render returned `FOCUS_RENDERED` with layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`, SVG hash `4045ca444e340509e31445db1c27a4d63fa678abc2d6ec3d800594827590f6b3`, HTML hash `83bab5b3527cb77b1661ec9694c41707e0438e50b82e7cf142fd0fc85ec7d6d8`, and JSON hash `5ca461ac81d6b56fa4adf3ab065da1aba5fc8e2b3b0838d8b827a24cca855426`. The render reports no Event 006 layout diagnostics. One intentional `FOCUS_ISOLATED` warning remains for `independence_wave_preserve_independent_command`; vanilla continuous-focus missing-sprite and localisation diagnostics are outside this Event 006 tree.

This handoff does not claim live-game testing. The broader Event 006 completion gate remains open for package attestation/capacity, formable readiness, super-event 6001 rights/audio/runtime dispatch, source/asset proof, catalog promotion, and final AI/balance sweeps.
