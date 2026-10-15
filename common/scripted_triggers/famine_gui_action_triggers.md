# Famine panel action predicates

`famine_gui_can_start_<suffix>` and `famine_gui_can_show_<suffix>` run in actor COUNTRY scope with the exact selected state.
They expose no persistent gameplay mutation.
The action-specific internal predicate shares the native decision requirements and live quote, with current-generation and cooldown guards.
See [the action contract and inventory](../scripted_effects/humanitarian_gui_action_effects.md).
