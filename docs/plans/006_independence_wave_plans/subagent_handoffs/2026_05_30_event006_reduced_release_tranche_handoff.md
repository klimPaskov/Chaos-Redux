# Event 006 Reduced Release Resolver Tranche Handoff

Scope: Event 006 Independence Wave release resolver only.

## Changed Files

- `events/006_independence_wave.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md`

## Resolver Behavior

- The release loop now saves the current host as `independence_wave_current_host` before each release attempt.
- `independence_wave_prepare_reduced_release_footprint` picks a host-owned, host-controlled, candidate-cored anchor state that is not marked `independence_wave_host_survival_reserved`.
- Before `release = PREV`, the helper temporarily removes the candidate core from the candidate's other host-owned cores and marks those states with `independence_wave_reduced_release_core_masked`.
- After the release setup runs, `independence_wave_restore_reduced_release_cores` restores the masked cores to the Event 006 candidate so they remain later claim and package-proof targets instead of being free starting territory.
- Countries that used masked cores receive `independence_wave_reduced_territory_start` and `constant:independence_wave_startup.reduced_start_claim_ambition_gain`.
- Temporary global event targets are cleared by the restore helper and by `independence_wave_clear_pending_candidate_state`.

## Safety Notes

- The protected host state remains mandatory. The tranche does not release a candidate unless the existing host-survival target is present.
- The host survival state is excluded from anchor selection and masking.
- The host safety trigger now checks the looped candidate with `PREV` inside the host selector, matching the `for_each_scope_loop` and `random_country` scope stack.
- `independence_wave_host_survival_reserved` is intentionally persistent and is not cleared by per-candidate cleanup.
- Event 005 files and Event 005 origin flags were not touched.
- No flag image files, flag asset definitions, country flag graphics, or `.gfx` flag surfaces were touched.

## Validation

- Brace balance passed for:
  - `events/006_independence_wave.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/script_constants/006_independence_wave_constants.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
- Pattern scan found no `<=`, `>=`, direct constant-backed duration fields, or unary negative variable-token assignments in the touched Event 006 script files.
- `git diff --check` passed for the touched tranche files.
- Leading-space indentation scan found no space-indented lines in the touched Event 006 script files.

## Remaining Risks

- This is a generic reduced-start resolver. Package-specific anchor preferences and balance scenarios are still required for major packages.
- No live in-game scenario validation was run in this tranche.
- Scripted-system subagent audit completed in `2026_05_30_100749_event006_reduced_release_resolver_audit.md`. The parent accepted its `PREV` trigger fix, kept its reduced-anchor cleanup review, and reverted only the suggested cleanup of `independence_wave_host_survival_reserved` because that protected-state flag must persist.
