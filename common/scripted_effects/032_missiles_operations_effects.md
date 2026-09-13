# Missile operations lifecycle contracts

`032_missiles_operations_effects.txt` owns missile operation calculations, damage receipts, capture/inheritance transactions, and warning closure.

Scratch temporaries are unscoped and live for the enclosing effect evaluation.
The reach stage, reserve-after-operation and AI reserve floor, four guidance components, population cap, disaster reserve loss calculation, ally half threshold, warning schedule days, inherited/captured reserve amount, civil-war site pool and child reserve, and annex site receipt are initialized before their reads on each applicable execution path.
Their consumers copy durable results into country/state variables before return; they are not presence sentinels.
Training contribution is read only inside its initializing training branch.
Capture amount is initialized in `missiles_transfer_captured_reserve` before the caller caps, debits, and credits it; the helper output must remain alive throughout that caller.
Warning scheduling consumes its temporary duration when queuing `chaosx.nr32.82`; the delayed event uses stored warning dates and recomputes the duration on a later scheduling call.
Nested helpers do not read any of these names after their terminal use without a fresh initializer; loop iterations recompute their scratch values.
No manual temporary-clear effect exists.

`missiles_initialize_scenario_package` consumes country-scoped `missiles_scenario_package_stage`, `reserve`, `readiness`, `control`, and `site_capacity` inputs from `missiles_scenario_apply_country_package`.
Missing inputs retain the helper's existing defaults; a supplied zero readiness or control remains distinct from an absent input.
State iteration deliberately reads `PREV.missiles_scenario_package_site_capacity` from the country owning the transaction.
The scenario adapter clears all nine package input variables at country completion and again in bounded transaction cleanup.

`missiles_close_root_incident` tests the global warning root with `has_event_target` and clears that global target through `clear_global_event_target` after closure.
`missiles_register_conventional_military_losses` uses file-local `@missiles_division_presence_floor = 0` because the `divisions_in_state.size` parser does not support a script-constant token.
The strict greater-than condition and impact-state reference remain intact.
The incident inspection threshold uses existing `missiles_attribution.unknown = 4`; comparison and assigned highly-likely value are unchanged.

These repairs add no helper or call site and change no weighted pool, weight, random draw, duration formula, reserve allocation formula, asset, or localisation.
See `docs/testing/live_qa/20260913_main_menu_startup/script_missile_handoff.md` and its exact-token reference companion for repair evidence and validation limits.
