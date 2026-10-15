# Migration action bridge

The public helpers, stable enum, scope contract, inputs, outputs, side effects, defaults, cleanup, call sites, and all action callbacks are documented in [humanitarian_gui_action_effects.md](humanitarian_gui_action_effects.md).

Example in the actor country:

```text
set_temp_variable = { migration_gui_action = constant:migration_gui_action.prepare_evacuation }
migration_gui_start_action = yes
```

Set the exact `migration_panel_selected_state` pointer before this call.
There is no implicit fallback to another state.

`migration_gui_publish_transfer_participants` runs at the end of transfer-backed action resolvers, after receipt/refund cleanup and action-owned preparation, trapped-state, mission, reception, and return projections. It publishes only valid finalized endpoint states to their current owners and distinct controllers.
