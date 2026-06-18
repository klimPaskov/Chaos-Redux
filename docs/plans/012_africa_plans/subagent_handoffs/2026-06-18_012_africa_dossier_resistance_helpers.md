# Event 012 Africa Dossier Resistance Helper Architecture Handoff

Date: 2026-06-18

Scope: scripted-system architecture review for profile-aware intervention decisions and consequences for active historical Authority Atlas dossier resistance watches. No gameplay files were edited.

## Files Inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Required offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding
- Vanilla docs: `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`
- Existing dynamic helper docs: `common/scripted_effects/chaosx_dynamic_effects.txt`, `common/scripted_effects/chaosx_dynamic_effects.md`
- Requested Event 012 files:
  - `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
  - `docs/plans/012_africa_plans/2026-06-16_foundation_gap_improvement_addendum.md`
  - `common/script_constants/012_africa_constants.txt`
  - `common/scripted_effects/012_africa_effects.txt`
  - `common/scripted_triggers/012_africa_triggers.txt`
  - `common/scripted_localisation/012_africa_scripted_localisation.txt`
  - `events/012_african_union.txt`
- One directly relevant call-site file: `common/decisions/012_africa_decisions.txt`

## Current Helper State

The resistance-watch layer should use the existing selected dossier state only at watch creation time. The settlement helpers already copy:

- `africa_selected_dossier_id` to `africa_archive_resistance_dossier_id`
- `africa_selected_dossier_seat_state` to `africa_archive_resistance_seat_state`
- selected settlement mode into `africa_dossier_resistance_watch_observer` or `africa_dossier_resistance_watch_direct_archive`

After that copy, new intervention decisions should read `africa_archive_resistance_*`, not `africa_selected_*`. The selected dossier can legitimately advance to another file while the old resistance watch is still active.

There is already useful parent-side scaffolding in the current worktree:

- `can_africa_mediate_dossier_resistance_watch`
- `can_africa_enforce_dossier_resistance_watch`
- `is_africa_archive_resistance_profile_*` profile triggers
- constants for intervention PP cost, enforcement command power, mediation/enforcement equipment and manpower, and `africa_decision_days.dossier_resistance_intervention`

## Recommended Helper Map

### `africa_apply_dossier_resistance_mediation_cost`

- Scope: Africa unifier country.
- Inputs: active observer-mode resistance context.
- Outputs: spends PP, support equipment, and manpower from existing constants.
- Side effects: none beyond costs.
- Call sites: observer-mode intervention decision complete effect.
- Notes: use `dossier_resistance_intervention_cost_spend`, `dossier_resistance_mediation_support_equipment` negated through a temp variable, and `dossier_resistance_mediation_manpower_spend`.

### `africa_apply_dossier_resistance_enforcement_cost`

- Scope: Africa unifier country.
- Inputs: active direct-archive-mode resistance context.
- Outputs: spends PP, command power, infantry equipment, support equipment, and manpower.
- Side effects: none beyond costs.
- Call sites: direct-archive intervention decision complete effect.
- Notes: avoid unary negative equipment variables; set positive temp, multiply by `-1`, then spend.

### `africa_record_dossier_resistance_mediation_used`

- Scope: Africa unifier country.
- Inputs: `africa_archive_resistance_dossier_id`.
- Outputs: `africa_dossier_[DOSSIER_ID]_resistance_mediated`.
- Side effects: can set a generic `africa_dossier_resistance_intervention_used` flag if decisions should be one-shot for the active watch.
- Call sites: mediation decision complete effect.
- Meta safety: safe if gated by `has_africa_dossier_resistance_watch_context = yes`.

### `africa_record_dossier_resistance_enforcement_used`

- Scope: Africa unifier country.
- Inputs: `africa_archive_resistance_dossier_id`.
- Outputs: `africa_dossier_[DOSSIER_ID]_resistance_enforced`.
- Side effects: can set `africa_dossier_resistance_intervention_used`.
- Call sites: enforcement decision complete effect.

### `has_africa_dossier_resistance_intervention_used`

- Type: scripted trigger.
- Scope: Africa unifier country.
- Inputs: `africa_archive_resistance_dossier_id`.
- Output: true if either route-specific intervention flag exists for the active watch.
- Call sites: add to `can_africa_mediate_dossier_resistance_watch` and `can_africa_enforce_dossier_resistance_watch` if the parent wants one intervention per watch.
- Recommendation: use this to prevent farming unless the parent explicitly wants repeatable interventions with cooldown.

### `africa_apply_dossier_resistance_mediation_profile_effects`

- Scope: Africa unifier country.
- Inputs: `africa_archive_resistance_dossier_id` and the archive-resistance profile triggers.
- Outputs: profile-aware value movement.
- Suggested logic: observer mediation should mostly improve `africa_regional_trust`, `africa_league_cohesion`, `africa_local_sovereignty`, or reduce `africa_restoration_debt` depending on profile. Reuse existing `dossier_profile_secondary`, `dossier_profile_pressure`, and `dossier_profile_relief` constants unless a stronger balance distinction is required.
- Side effects: clamp core values.
- Call sites: mediation decision complete effect.

### `africa_apply_dossier_resistance_enforcement_profile_effects`

- Scope: Africa unifier country.
- Inputs: `africa_archive_resistance_dossier_id` and archive-resistance profile triggers.
- Outputs: profile-aware direct-archive value movement.
- Suggested logic: enforcement should usually improve `africa_authority` or reduce `africa_paper_core_burden`, while adding `africa_local_sovereignty`, `africa_restoration_debt`, or `africa_colonial_alarm` for coercive profiles. Reuse existing profile/resistance constants where possible.
- Side effects: clamp core values.
- Call sites: enforcement decision complete effect.

## Constants and Tuning Plan

Use the constants already present in the current worktree for costs and duration:

- `africa_decision.dossier_resistance_intervention_cost`
- `africa_decision.dossier_resistance_intervention_cost_spend`
- `africa_decision.dossier_resistance_enforcement_command_power_gate`
- `africa_decision.dossier_resistance_enforcement_command_power_spend`
- `africa_decision_days.dossier_resistance_intervention`
- `africa_force.dossier_resistance_mediation_support_equipment`
- `africa_force.dossier_resistance_mediation_manpower_gate`
- `africa_force.dossier_resistance_mediation_manpower_spend`
- `africa_force.dossier_resistance_enforcement_infantry_equipment`
- `africa_force.dossier_resistance_enforcement_support_equipment`
- `africa_force.dossier_resistance_enforcement_manpower_gate`
- `africa_force.dossier_resistance_enforcement_manpower_spend`

Additional constants are only needed if the parent wants intervention outcomes to differ numerically from existing profile/resistance deltas. If so, add a compact set rather than one constant per profile:

- `dossier_resistance_mediation_primary`
- `dossier_resistance_mediation_secondary`
- `dossier_resistance_mediation_debt_relief`
- `dossier_resistance_enforcement_authority`
- `dossier_resistance_enforcement_burden_relief`
- `dossier_resistance_enforcement_sovereignty_pressure`
- `dossier_resistance_enforcement_debt_pressure`

Do not add duration `@` constants for the new intervention decisions if they use `days_remove`; existing decisions successfully use `constant:africa_decision_days.*` there. Keep file-scoped `@..._mission_days` only for mission timeout fields that the repo already treats as constant-sensitive.

## Meta Effect and Meta Trigger Safety

The existing dynamic flag pattern is safe for this feature when it is guarded:

- Good: `has_variable = africa_archive_resistance_dossier_id` before meta injection.
- Good: `has_africa_dossier_resistance_watch_context = yes` before dynamic checks and effects.
- Good: `DOSSIER_ID = "[?africa_archive_resistance_dossier_id|.0]"` for numeric dossier IDs.

Use meta effects/triggers only for dynamic flag names such as `africa_dossier_[DOSSIER_ID]_resistance_mediated`. Do not use meta effects for normal value changes, costs, or profile branches; those can use normal triggers and script constants.

## Event Target and Cleanup Plan

No new global event target is needed for resistance watches. The current country variables are enough:

- `africa_archive_resistance_dossier_id`
- `africa_archive_resistance_seat_state`

The seat variable already supports state scoping with `var:africa_archive_resistance_seat_state` and localisation with `[?africa_archive_resistance_seat_state.GetName]`.

Cleanup must be delayed until player-facing text has consumed the context. `chaosx.nr12.49` and `chaosx.nr12.50` read:

- `[GetAfricaArchiveResistanceDossierName]`
- `[GetAfricaArchiveResistanceSeatName]`
- `[GetAfricaDossierResistanceSettlementMode]`

Current flow is correct: `africa_complete_dossier_resistance_watch` and `africa_fail_dossier_resistance_watch` fire the event while leaving `africa_archive_resistance_*` and mode flags alive; the event option then calls `africa_clear_dossier_resistance_watch_context`. The parent should not move cleanup into the complete/fail helpers before the popup fires.

If intervention decisions fire their own report popups, use the same pattern: preserve resistance context through the popup, then clear only short-lived intervention state from the option. Do not clear `africa_archive_resistance_*` unless the whole watch is ending.

## Migration Plan

1. Keep watch creation in `africa_start_dossier_resistance_watch_for_selected_observer_settlement` and `africa_start_dossier_resistance_watch_for_selected_direct_archive_settlement`.
2. Add mediation/enforcement decisions in `africa_authority_atlas_category`, visible only while `africa_dossier_resistance_watch_active` is set.
3. Use `can_africa_mediate_dossier_resistance_watch` and `can_africa_enforce_dossier_resistance_watch` for availability and cost trigger clarity.
4. Call the matching cost helper, record helper, and profile-effect helper from the decision complete effects.
5. If one intervention per watch is desired, add the intervention-used trigger to both availability helpers and clear the generic intervention-used flag only in `africa_clear_dossier_resistance_watch_context`.
6. Leave `africa_complete_dossier_resistance_watch` and `africa_fail_dossier_resistance_watch` as the only helpers that end the watch and fire `chaosx.nr12.49/50`.

## Risks and Validation Notes

- Existing uncommitted parent changes are present in `common/script_constants/012_africa_constants.txt` and `common/scripted_triggers/012_africa_triggers.txt`. I did not edit or revert them.
- The line between repeatable intervention and exploit loop needs a parent decision. My recommendation is one intervention per active watch by dynamic flag.
- The active mission uses `@africa_dossier_resistance_watch_days = 150` while `africa_decision_days.dossier_resistance_watch = 85`; this mismatch predates this review path or comes from current parent work. Do not “fix” it blindly. If the mission should be 85 days, change both deliberately; if 150 is intended for true timed watches, keep the file-scoped `@` and document the reason.
- No task-specific gameplay validation was run because this was a design-only handoff. I validated by tracing the watch context from settlement helpers through mission complete/timeout and the `chaosx.nr12.49/50` event text cleanup path.

## Patch Made

Added this handoff only:

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_dossier_resistance_helpers.md`
