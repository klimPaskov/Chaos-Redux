# Event 011 Secret Alliance Scripted Runtime Handoff

Subagent: `chaosx_scripted_system_architect`
Date: 2026-07-01

## Scope

Audited and narrowly patched the scripted runtime for Event 011 Secret Alliance:

- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/script_constants/011_secret_alliance_constants.txt`
- Event 011 integration references in `common/on_actions/chaosx_on_actions.txt`, `common/scripted_effects/chaosx_settings_effects.txt`, `common/scripted_effects/chaosx_logic_effects.txt`, and `common/scripted_effects/chaosx_events_log_effects.txt`

Required references consulted before and during audit: `AGENTS.md`, `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-subagents`, Event 011 specs under `docs/specs/011_secret_alliance_specs/`, offline wiki pages for data structures/triggers/effects/scopes/on actions/events/decisions/localisation/ideas/AI/modifiers, and vanilla documentation for effects, triggers, script concepts, and script constants.

## Files Changed

- `common/scripted_effects/011_secret_alliance_effects.txt`

No commit was created, per parent instruction.

## Patches Made

### Evolved Opening Minimum

`secret_alliance_select_opening_profile` now uses the existing `constant:secret_alliance_opening.major_patron_minimum_members` fallback for tier II and tier III pre-fire openings when a valid major patron exists but only two valid minor members are available. This aligns the runtime with the spec's major founder plus two-to-four minor opening shape.

`secret_alliance_select_opening_core_members` now handles `major_patron_minimum_members` by selecting two opening core members instead of falling through to the baseline three-member branch.

### Experience Cost Effects

Replaced invalid/non-vanilla effect names:

- `add_army_experience` -> `army_experience`
- `add_air_experience` -> `air_experience`

Affected helpers:

- `secret_alliance_pay_cipher_cost`
- `secret_alliance_pay_contingency_plan_cost`

Vanilla precedent checked in current HOI4 event files uses `army_experience`, `air_experience`, and `navy_experience`.

## Audit Findings

### Hidden Baseline Formation

Pass. `secret_alliance_possible_target_candidate` requires at least `constant:secret_alliance_opening.baseline_core_members` valid opening core candidates, and the constant is 3. `secret_alliance_opening_core_candidate` excludes subjects, faction members, capitulated countries, the target itself, and countries already at war with the target. `secret_alliance_start_hidden_pact` does not create a public faction at start.

### Core Member War With Target

Pass. `secret_alliance_opening_core_candidate` prevents core members from being selected if already at war with the target. `secret_alliance_on_war_relation_added` is wired from `on_war_relation_added` and reveals immediately when either side of the new war relation is the target and the other side is a valid core member.

`secret_alliance_reveal_compact` exposes members, creates or joins a public faction/coalition when possible, and declares war for all valid core members not already at war with the target.

### Evolution I/II/III Runtime

Pass with patch. Active-event evolution changes call the expected evolution effects and event-log recorders. Pre-fire openings now support:

- Evolution I: wider minor compact through four or five minors.
- Evolution II/III: major patron opening with three minors, falling back to the documented two-minor minimum when needed.
- Evolution III: public crisis path through `secret_alliance_force_public_crisis`.

### Global Event Targets And Cleanup

Pass with residual risk below. Global event targets are justified because Event 011 state persists across scheduled operation pulses, delayed reports, reveal events, and on-action callbacks:

- `secret_alliance_target`
- `secret_alliance_major_patron`
- `secret_alliance_second_major`
- `secret_alliance_public_leader`
- `secret_alliance_pending_target`

They are cleared by `secret_alliance_clear_runtime_state` and `secret_alliance_finish_runtime_cleanup`. Paper dissolution schedules `chaosx.nr11.31`, whose immediate block calls `secret_alliance_finish_runtime_cleanup`.

### On-Action Polling

Pass for Event 011. Event 011 uses targeted hooks for faction joins, war relation additions, peace, and capitulation. It does not add Event 011 logic to whole-world daily, weekly, or monthly polling.

### Unsupported Operators And Scoped Temp Variables

Pass for audited Event 011 runtime files. No `<=` or `>=` were found in:

- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/script_constants/011_secret_alliance_constants.txt`

No scoped temporary variable assumptions were found in Event 011 runtime helpers.

## Constants And Tuning Table Plan

No new constants were added. The patch used the existing tuning constant:

- `constant:secret_alliance_opening.major_patron_minimum_members`

This keeps the pre-fire evolved opening size controlled from `common/script_constants/011_secret_alliance_constants.txt`.

## Helper Documentation

No new scripted effects/triggers or dynamic helpers were introduced, so no helper markdown update was needed.

## Call Sites Changed

Changed direct call behavior in:

- `secret_alliance_select_opening_profile`
- `secret_alliance_select_opening_core_members`
- `secret_alliance_pay_cipher_cost`
- `secret_alliance_pay_contingency_plan_cost`

No integration call sites were changed.

## Cleanup Logic

No new cleanup helper was added. Existing cleanup remains centralized in:

- `secret_alliance_clear_runtime_state`
- `secret_alliance_finish_runtime_cleanup`

The audit confirmed those helpers clear Event 011 global event targets, arrays, country flags, and ideas.

## Validation

Meaningful checks run:

- Searched Event 011 runtime files for invalid experience effect names after patch: no `add_army_experience`, `add_air_experience`, or `add_navy_experience` remain.
- Searched audited Event 011 runtime files for unsupported `<=`/`>=`: no matches.
- Checked Event 011 on-action wiring: only `secret_alliance_on_join_faction`, `secret_alliance_on_war_relation_added`, `secret_alliance_on_peace`, and `secret_alliance_on_capitulation` are wired.
- Checked vanilla precedent for experience effects: vanilla uses `army_experience`, `air_experience`, and `navy_experience`.
- Checked vanilla and Chaos Redux precedents for dynamic `country_event` `days = variable/constant`; existing vanilla and Chaos Redux files use this pattern.

Skipped validation:

- No HOI4 executable parse/load test was run from this subagent session.
- No in-game validation was requested or performed.

## Residual Risks

- `secret_alliance_recalculate_member_counts` removes invalid countries from `global.secret_alliance_core_members` while iterating that same array. This is a narrow residual risk if the engine skips adjacent invalid entries after mutation. It was not patched because a safer two-pass cleanup helper would be a broader runtime refactor than this audit required.
- If all valid core members join third-party factions before reveal and none is a faction leader, `secret_alliance_choose_public_leader` can fall back to a member that cannot form or lead a faction. The reveal still declares wars for valid core members, but public coalition joining may be limited in that edge case.
- Paper-collapse cleanup is finalized through the delayed `chaosx.nr11.31` event. The event has no trigger and calls `secret_alliance_finish_runtime_cleanup` in `immediate`, but state persists until that event fires.

## Completion Status

Audit complete with narrow runtime patch applied. No fallbacks or simplifications were introduced.
