# Event 014 Player-Safe Host Selection Fix Handoff

Date: 2026-07-15

Agent: `/root/portrait_regen_a`

Mode: patch-capable, bounded to deterministic ordinary and Wendigo host selection.

## Changed files

- `common/scripted_effects/014_cannibalism_unification_effects.txt`
- `common/scripted_effects/014_cannibalism_wendigo_effects.txt`
- `docs/plans/014_cannibalism_plans/audits/event014_country_package_reaudit_2026-07-15.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_player_safe_host_selection_fix_2026-07-15.md`

The two gameplay files already contained unrelated concurrent edits. This task owns only the new candidate helpers and the two selector-body rewrites described below. Those neighboring edits were preserved.

## Identifiers implemented

### Ordinary CBL selection

- Added `cannibalism_consider_current_unification_host_candidate`.
  - Calls the existing `cannibalism_calculate_current_unification_host_score`.
  - Replaces the selected target only for a higher score, or for an equal score with a lower numeric `THIS.id`.
  - Persists `cannibalism_unification_host` and its actor generation together.
- Reworked `cannibalism_select_unification_host`.
  - First pass accepts only viable warlords with `is_ai = no`.
  - `cannibalism_human_unification_host_found` prevents the AI pass whenever an eligible human exists.
  - Second pass accepts only viable warlords with `is_ai = yes`.
  - The existing score remains the ordering rule inside the selected human or AI class.

### Original-ZZZ Wendigo selection

- Added `cannibalism_consider_current_wendigo_merge_host_candidate`.
  - Calls the existing `cannibalism_calculate_current_wendigo_merge_host_score`.
  - Replaces the selected target only for a higher score, or for an equal score with a lower numeric `THIS.id`.
- Reworked `cannibalism_select_wendigo_merge_host`.
  - First pass accepts only valid human-controlled original-ZZZ Wendigo survivors.
  - `cannibalism_human_wendigo_merge_host_found` prevents the AI pass whenever an eligible human survivor exists.
  - Second pass accepts only valid AI original-ZZZ Wendigo survivors.

## Preserved downstream behavior

- `cannibalism_try_execute_wendigo_unification` still runs the Wendigo selector and the ordinary constituent selector before the merge transaction.
- `cannibalism_prepare_wendigo_merge_identity` still transforms the selected original-ZZZ country in place through its cosmetic and Event 014 state mutations. No replacement country is created or released.
- `cannibalism_create_wendigo_unification_from_selected_hosts` still:
  - leaves a human warlord donor unabsorbed when both the donor and Wendigo host are human;
  - transfers a human donor player to an AI Wendigo host before donor annexation;
  - retains a selected human Wendigo host on the same country scope.
- Ordinary CBL creation and later voluntary absorption still use `change_tag_from` before annexing a human-controlled warlord.

## Before and after

Before, each selector used one combined-score pass. Human control was only a score bonus, so a stronger AI or a capped score tie could defeat the player-first contract.

After, human eligibility is a distinct first selection class. AI candidates are not scored unless that class is empty. Strength still orders candidates within the active class, and equal scores use lower country ID instead of loop order.

## Validation

- Reconsulted the offline Effects, Triggers, Scopes, and Data Structures wiki references and the installed vanilla effects and triggers documentation. The country-ID tie uses the documented `THIS.id` variable form.
- Confirmed balanced effect-block structure in both edited gameplay files.
- Confirmed both selectors contain a human-only first pass, a no-human guard, and an AI-only second pass.
- Confirmed both helpers contain the higher-score comparison and explicit equal-score/lower-country-ID tie comparison.
- Confirmed ordinary selection still stores `cannibalism_actor_generation`, and the selected-host trigger still requires it for stale-target validation.
- Confirmed the selected original-ZZZ scope still receives `set_cosmetic_tag = ZZZ_CANNIBALISM_HANNIBAL` in place.
- Confirmed the dual-human donor protection and human-donor `change_tag_from` branch remain reachable after the selector calls.
- Exercised the selector matrix for weak human versus stronger AI, stronger human among humans, equal-score lower-ID tie, strongest AI with no human, and human original-ZZZ versus stronger AI survivor. All expected winners were selected.
- The optional Event Chain Viewer lint could not retain an artifact because the shared artifact store had reached its retention limit. It made no source changes and was not required for the source-path validation above.

## Remaining risk and ownership

- The country-package reaudit now records P0 0, P1 0, P2 0, and P3 1.
- P3-01, the non-atomic manual scenario failure path, remains in the report pending the separately owned scenario remediation by `/root/portrait_regen_b`.
- No scenario, trigger, script-constant, localisation, interface, asset, manifest, or spreadsheet file was edited by this task.
- No fallback or simplification was introduced.
- No commit was created by this subagent.

## Skills used

- `chaos-redux-events`
