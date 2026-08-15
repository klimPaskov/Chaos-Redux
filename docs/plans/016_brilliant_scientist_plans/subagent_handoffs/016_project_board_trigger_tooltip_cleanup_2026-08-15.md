# Event 016 project-board trigger tooltip cleanup handoff

## Scope

This presentation-only patch condenses the raw trigger expansions shown by Event 016 Directorate project decisions. It covers the full `common/decisions/016_brilliant_scientist_directorate_project_board.txt` surface rather than only the photographed computation-theory order.

## Files changed

- `common/decisions/016_brilliant_scientist_directorate_project_board.txt`.
- `localisation/english/016_brilliant_scientist_projects_l_english.yml`.
- This handoff.

## Implementation

Existing authoritative availability and cancellation trigger bodies remain in place inside `hidden_trigger` blocks. Where a payment trigger was previously evaluated once as a raw line and again inside its existing cost tooltip, the redundant raw copy was removed while the same authoritative payment trigger remains in the cost tooltip; the eligibility condition is unchanged. Concise `custom_trigger_tooltip` wrappers now present one player-facing requirement or cancellation summary for:

- board selection and replication actions;
- all fifteen project families and their theory, deployment, and weaponization stages;
- prototype construction;
- control and singularity audit/construction orders;
- incident response and cancellation surfaces.

Existing cost tooltips remain separate and unchanged, so equipment, fuel, manpower, factory, political-power, and duration information still appears where it is useful. Visibility rules remain hidden presentation gates. No cost, duration, project prerequisite, completion effect, cancellation effect, AI weight, or project state transition was changed.

## Localisation keys

The patch adds eleven concise English keys under `localisation/english/016_brilliant_scientist_projects_l_english.yml`, including `brilliant_scientist_project_stage_requirements_tt`, `brilliant_scientist_project_stage_cancel_tt`, project-board action/replication summaries, prototype/control/singularity summaries, and incident summaries.

## Review

All 147 added tooltip bindings were reformatted as normal multiline Clausewitz blocks after the first mechanical pass produced collapsed single-line blocks. The photographed `brilliant_scientist_advance_computation_theory` decision now shows a concise eligibility summary and its existing detailed cost line, while the long host/facility/state/capacity tree and inverse cancellation tree remain hidden engine logic.

No fallback or gameplay simplification was used. Live tooltip rendering remains user-owned.
