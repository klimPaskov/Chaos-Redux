# Migration panel action predicates

`migration_gui_can_start_<suffix>` and `migration_gui_can_show_<suffix>` run in actor COUNTRY scope with the exact selected state.
They expose no persistent gameplay mutation.
Each state flag read through the `humanitarian_action_target` pointer, such as the `<action>_cost_paid` receipt guard and the prepared-evacuation guard, runs inside an `if` whose limit is `humanitarian_state_is_valid`, so a native decision evaluated without a selected state returns false instead of reading state flags in country scope.
The action-specific internal predicate shares the native decision requirements and live quote, with current-generation and cooldown guards.
See [the action contract and inventory](../scripted_effects/humanitarian_gui_action_effects.md).
