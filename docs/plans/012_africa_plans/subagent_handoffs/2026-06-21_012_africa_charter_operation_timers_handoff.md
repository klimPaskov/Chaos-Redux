# Event 012 Africa Charter Operation Timers Handoff

Date: 2026-06-21

Mode: parent-agent gameplay patch after the decision-surface audit.

## Scope

Closed the bounded decision-surface finding that `africa_influence_charter_member` and `africa_docket_authority_integration` were still too close to immediate exchange actions.

## Changed Files

- `common/decisions/012_africa_decisions.txt`
- `common/script_constants/012_africa_constants.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-21_012_africa_charter_operation_timers_handoff.md`

## Gameplay Changes

- `africa_influence_charter_member` now starts a timed liaison operation instead of immediately recording the influence package.
- The influence operation spends political power, command power, and support equipment at start, requires Regional Trust, marks the target with `africa_charter_member_influence_active`, and records `africa_charter_member_influence_recorded` only when the timer completes.
- The influence operation fails if the target leaves the Charter relationship, capitulates, goes to war with the Charter leader, or the Regional Trust gate collapses during the timer.
- `africa_docket_authority_integration` now starts a timed integration hearing instead of immediately docketing the authority.
- The integration hearing requires a successful regional-authority mandate, Authority, Regional Trust, political power, command power, support equipment, and manpower.
- The integration hearing marks `africa_authority_integration_docket_active` at start and records `africa_authority_integration_docketed` only when the timer completes.
- The integration hearing fails if the mandate/loyalty/capital/Authority/Regional Trust conditions collapse before completion.
- Runtime cleanup now clears the new active and failed flags alongside the existing Charter-member and authority-docket flags.
- Regional autonomy ratification and peaceful Charter exit now block while an integration hearing is active, while resistance-war preparation can explicitly react to either an active hearing or a completed docket.

## Validation Performed

- Consulted the offline decision-modding reference for `complete_effect`, `days_remove`, `remove_effect`, and `cancel_trigger` semantics.
- Mirrored the existing Event 012 timed-decision pattern used by liberation objectives and external proof audits.
- Reconciled custom-cost triggers, click-time start checks, delayed `remove_effect` success, cancel failure, cleanup flags, and localisation keys for both decisions.

## Remaining Blockers

- No live in-game proof was run. The broader Event 012 validation blockers remain open: scenario matrix proof, World Is One ordinary-route proof, GUI render proof, AI/balance/exploit checks, and achievement route proof.
- This patch does not implement full target-card GUI selection for Charter members or authority subjects; it only strengthens the decision-layer operations.
