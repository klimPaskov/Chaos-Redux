# Event 006 Reduced Release Resolver Audit Handoff

Date: 2026-05-30 10:07 UTC

## Scope

Audited the Event 006 Independence Wave reduced-territory release resolver tranche.

Files inspected:
- `events/006_independence_wave.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- Offline Paradox wiki core pages required by `AGENTS.md`
- Vanilla HOI4 documentation in `~/projects/Hearts of Iron IV/documentation`
- Vanilla precedents for `release = event_target:*`, `add_core_of = event_target:*`, `add_core_of = PREV`, and `remove_core_of = PREV`

## Files Changed

- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_100749_event006_reduced_release_resolver_audit.md`

No flag image files, flag asset definitions, country flag graphics, or Event 005 files were touched.

## Helper Names and Call Sites

- `can_independence_wave_host_release_current_candidate_safely`
  - Call site: `events/006_independence_wave.txt` inside the `random_country` host selector for each `global.independence_wave_candidate_pool` entry.
  - Patch: changed candidate-core references from `PREV.PREV` to `PREV`.

- `independence_wave_clear_pending_candidate_state`
  - Call site: `events/006_independence_wave.txt` after each attempted release branch.
  - Patch: clears `independence_wave_host_survival_reserved` on `event_target:independence_wave_protected_host_state` and `independence_wave_reduced_release_anchor` on `event_target:independence_wave_reduced_release_anchor_state` before clearing temporary global event targets.

## Findings

1. `event_target:independence_wave_current_candidate` as the core target is acceptable for the current local pattern.
   - Vanilla docs list core effects as state-scoped and vanilla uses `add_core_of = event_target:west_britain_company`.
   - The offline wiki says event targets can be used as scopes and targets in most effect blocks.
   - `remove_core_of` has the same target class as `add_core_of`; no safer local rewrite was needed.

2. The new reduced-footprint helpers use host, candidate, and state scopes correctly.
   - `independence_wave_prepare_reduced_release_footprint` is called from candidate scope through `PREV = { ... }`.
   - It scopes into `event_target:independence_wave_current_host`, then into host-owned states.
   - In those state scopes, `PREV` is the host, and `event_target:independence_wave_current_candidate` remains the candidate.
   - `independence_wave_restore_reduced_release_cores` runs from the released candidate scope and restores masked candidate cores through the saved host event target.

3. The host-selection trigger had an unsafe scope mismatch.
   - Inside the `for_each_scope_loop` candidate entry and nested `random_country`, the selected candidate is `PREV`.
   - The trigger was checking candidate core tests against `PREV.PREV`, which points back past the candidate.
   - The patch makes the host safety trigger test `is_core_of = PREV` consistently.

4. Cleanup was missing temporary state-flag clearing.
   - `independence_wave_restore_reduced_release_cores` already clears reduced core mask flags and the reduced anchor flag on normal restoration.
   - `independence_wave_clear_pending_candidate_state` now also clears the protected host survival flag and reduced anchor flag before dropping global event targets.

5. The reduced-territory resolver tranche preserves host survival and does not add Event 005 coupling.
   - The resolver keeps a non-candidate host-owned state protected before release.
   - The reduced anchor avoids the protected flag.
   - This audit did not add Event 005 calls, Event 005 flags, or Event 005 file edits.
   - Existing Event 006 Soviet Collapse/Event 005-named exclusion and achievement markers outside the reduced-territory resolver were observed but left untouched as out of this narrow tranche.

## Constants and Tuning

No constants were added or changed.

Existing constants used by the tranche:
- `constant:independence_wave_resolver.host_survival_state_floor`
- `constant:independence_wave_resolver.host_stability_weakness_gate`
- `constant:independence_wave_resolver.host_war_support_weakness_gate`
- `constant:independence_wave_resolver.host_surrender_weakness_gate`
- `constant:independence_wave_resolver.protected_state_building_floor`
- `constant:independence_wave_resolver.protected_state_infrastructure_gate`
- `constant:independence_wave_startup.reduced_start_claim_ambition_gain`

## Event Targets and Cleanup

Temporary global event targets in the tranche:
- `independence_wave_current_host`
- `independence_wave_protected_host_state`
- `independence_wave_reduced_release_anchor_state`

Cleanup status:
- `independence_wave_current_host`: cleared by `independence_wave_clear_pending_candidate_state`.
- `independence_wave_protected_host_state`: state flag cleared, then target cleared by `independence_wave_clear_pending_candidate_state`.
- `independence_wave_reduced_release_anchor_state`: anchor flag cleared in restore and cleanup, then target cleared.
- `independence_wave_current_candidate`: regular event target, auto-clears with the effect chain.

## Validation

Run:
- Brace balance on scoped files: passed.
- `rg` scan for `<=` and `>=` in scoped files: passed, no matches.
- `rg -P` scan for direct `days = constant:` or `days = @` in scoped files: passed, no matches.
- `rg` scan for unary negative variable-token assignments in scoped files: passed, no matches.
- `git diff --check -- events/006_independence_wave.txt common/scripted_effects/006_independence_wave_effects.txt common/script_constants/006_independence_wave_constants.txt common/scripted_triggers/006_independence_wave_triggers.txt`: passed.
- Final `git diff --check` including this handoff file: passed.

## Skipped Validation

- No live in-game validation was run; this subagent cannot verify runtime release behavior in a loaded HOI4 session.
- No broad Event 006 completion audit was run; this was limited to the reduced-territory release resolver tranche.

## Remaining Risks and Follow-Up

- `remove_core_of = event_target:independence_wave_current_candidate` is supported by the same target pattern as `add_core_of = event_target:*`, but I did not find a vanilla `remove_core_of = event_target:*` precedent. If the engine rejects that target form despite accepting `add_core_of`, the parent should replace both core operations with a tested meta-effect or country-tag-alias pattern rather than using a fallback release path.
- Existing Event 006 references to Soviet Collapse/Event 005-named flags remain outside this tranche. They were not introduced or modified here.

## Parent Review Correction

The parent kept the trigger correction from this audit, but reverted the cleanup of `independence_wave_host_survival_reserved`. That state flag is not temporary: it must persist after a successful release so later Event 006 releases and Border Commission claims cannot consume the protected host state. Only the reduced-release anchor flag is cleared by `independence_wave_clear_pending_candidate_state`.
