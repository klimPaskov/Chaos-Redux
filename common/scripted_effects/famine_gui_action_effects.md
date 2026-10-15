# Famine action bridge

The public helpers, stable enum, scope contract, inputs, outputs, side effects, defaults, cleanup, call sites, and all action callbacks are documented in [humanitarian_gui_action_effects.md](humanitarian_gui_action_effects.md).

Example in the actor country:

```text
set_temp_variable = { famine_gui_action = constant:famine_gui_action.release_reserves }
famine_gui_start_action = yes
```

Set the exact `famine_panel_selected_state` pointer before this call.
There is no implicit fallback to another state.

Reserve-capacity refreshes used while forming relief contracts publish the target state after contract/payment preparation settles. Reserve consumption, requisition and delivery retain their exact core ledger receipts, and Famine action resolvers publish again after their mission, concealment, extraction, and evacuation tails finish.
