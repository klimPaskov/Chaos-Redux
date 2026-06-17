# Event 012 Authority Atlas Cleanup Parent Follow-Up

## Scope

Reviewed the stale decision-audit finding that dynamic per-dossier and high-chaos package flags were not visibly cleared by a reset loop.

## Findings

- `africa_register_authority_atlas_catalog` registers the dossier and high-chaos package arrays before setup progress is selected.
- `africa_clear_authority_atlas_progress_flags` loops over `global.africa_authority_atlas_dossier_ids` and clears generated dossier flags for opened, surveyed, survey-active, survey-failed, local-office, guarded, and settled states.
- The same helper loops over `global.africa_authority_atlas_high_chaos_package_ids` and clears generated high-chaos package unlocked flags.
- `africa_establish_union_start` calls `africa_clear_authority_atlas_progress_flags` immediately after catalog registration and before selecting the first dossier and high-chaos package.

## Patch

- Cleaned indentation in `common/scripted_effects/012_africa_effects.txt` around `africa_clear_bestiary_actor_action_flags` and `africa_clear_authority_atlas_progress_flags`.
- Updated `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_decision_mission_audit_handoff.md` to mark the dynamic cleanup finding as superseded.

## Remaining Risk

This resolves the reset-coverage documentation issue only. It does not finish the broader Authority Atlas depth gap: dossier-specific missions, settlement forks, resistance events, and richer selected-target presentation remain incomplete.
