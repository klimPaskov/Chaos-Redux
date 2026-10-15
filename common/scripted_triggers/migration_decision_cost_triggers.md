# Humanitarian decision fee bundles

These COUNTRY predicates combine the existing inclusive equipment components with the same physical selected-state transport profile used by payment and display.
They never debit resources or publish persistent gameplay state.

Every scope-sensitive `<action>_cost_is_affordable` helper has a single `<action>_cost_is_affordable_in_context` implementation.
It reads the mandatory unscoped temporary COUNTRY pointer `humanitarian_action_actor` and STATE pointer `humanitarian_action_target`.
The original native helper initializes those values from ROOT and FROM before its bare `= yes` call.
The shared panel action gate initializes them from the actor country and exact selected target.
The helpers initialize unscoped transport quote and receipt inputs from subsystem constants and reject an already paid action/state receipt.
They return a Boolean and temporary scratch values only, with no implicit target fallback and no named-argument API.

The public action inventory, scopes, state and actor binding, payment ownership, timing, cleanup, and validation limits are documented in [humanitarian_gui_action_effects.md](../scripted_effects/humanitarian_gui_action_effects.md).
The transport receipt and saved actual-quantity refund API remains in [migration_transport_cost_effects.md](../scripted_effects/migration_transport_cost_effects.md).

Example from an actor country with the exact state pointer:

```text
set_temp_variable = { humanitarian_action_actor = ROOT }
set_temp_variable = { humanitarian_action_target = my_selected_state }
famine_release_reserves_cost_is_affordable_in_context = yes
```
