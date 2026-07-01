# Event 015 scripted system architect handoff

## Files changed

- `common/script_constants/015_utopia_manifesto_constants.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_scripted_system_architect.md`

No events, registry files, decisions, focus trees, localisation, interface, assets, achievements, spreadsheets, or dynamic helper docs were edited.

## Helper map

Target helpers:

- `utopia_manifesto_has_valid_target_available`, trigger, any scope. Returns true when any eligible player or automatic AI target exists.
- `is_valid_utopia_manifesto_target`, country trigger. Hard gates majors, strong industry, strong armies, terminal world states, nonhuman/special actors, current Utopia state, and known event-created replacement tree actors.
- `is_valid_utopia_manifesto_player_target`, country trigger. Human target using the same hard gates.
- `is_valid_utopia_manifesto_automatic_target`, country trigger. AI target using the same hard gates plus dead-on-arrival checks and subject stability checks.
- `utopia_manifesto_select_target`, effect, any scope. Builds a weighted temporary country pool, prefers eligible player countries and small minors, saves `event_target:utopia_manifesto_target`, and sets temp `utopia_manifesto_target_selected`.
- `utopia_manifesto_prepare_random_event_fire`, effect, dispatcher scope. Calls selection, fires `chaosx.nr15.1` on `event_target:utopia_manifesto_target`, sets `event_single_fire_allowed = 0`, and sets temp `event_fire_dispatched = 1`. If no target exists, it only sets `event_single_fire_allowed = 0`.

Acceptance and route helpers:

- `utopia_manifesto_accept_manifesto`, country effect. Sets accepted and ledger flags, initializes ledger, refreshes geography, and loads `utopia_manifesto_tree` when `utopia_manifesto_can_load_tree` passes.
- `utopia_manifesto_reject_manifesto`, country effect. Sets rejected flag, clears accepted ledger state and variables, and applies only a small public-calm stability effect.
- Route setters: `utopia_manifesto_set_living_humanism_route`, `utopia_manifesto_set_common_store_state_route`, `utopia_manifesto_set_island_discipline_route`, `utopia_manifesto_set_guild_commonwealth_route`, `utopia_manifesto_set_marked_bounds_route`, `utopia_manifesto_set_new_utopia_route`.
- Route triggers: `utopia_manifesto_has_open_route`, `utopia_manifesto_has_unresolved_route`, `utopia_manifesto_is_living_humanism`, `utopia_manifesto_is_common_store_state`, `utopia_manifesto_is_island_discipline`, `utopia_manifesto_is_guild_commonwealth`, `utopia_manifesto_is_marked_bounds`, `utopia_manifesto_is_new_utopia`.

Ledger helpers:

- `utopia_manifesto_initialize_ledger`, country effect. Sets Need, Consent, Surplus, Overreach, Vocation Balance, Foreign Suspicion, and five vocation share variables from constants, then applies initial war, subject, stability, geography, and factory adjustments.
- `utopia_manifesto_refresh_ledger`, country effect. Clamps values, refreshes display variables, and refreshes ledger status flags.
- `utopia_manifesto_clamp_ledger`, country effect. Clamps six primary ledger values and five vocation shares to constants.
- `utopia_manifesto_add_need`, `utopia_manifesto_add_consent`, `utopia_manifesto_add_surplus`, `utopia_manifesto_add_overreach`, `utopia_manifesto_add_vocation_balance`, `utopia_manifesto_add_foreign_suspicion`, country effects. Input is temp variable `utopia_manifesto_ledger_delta`. Each adds the delta to its value, then clamps and refreshes.
- Ledger triggers: `utopia_manifesto_has_ledger`, `utopia_manifesto_need_high`, `utopia_manifesto_need_crisis`, `utopia_manifesto_consent_low`, `utopia_manifesto_consent_stable`, `utopia_manifesto_surplus_low`, `utopia_manifesto_surplus_stable`, `utopia_manifesto_overreach_high`, `utopia_manifesto_overreach_safe`, `utopia_manifesto_vocation_balance_low`, `utopia_manifesto_foreign_suspicion_high`.

Geography and project helpers:

- `utopia_manifesto_refresh_geography_mode`, country effect. Sets `utopia_manifesto_geography_mode` and geography flags for subject, island, coastal, or landlocked state.
- `utopia_manifesto_country_has_coast`, `utopia_manifesto_country_island_capital`, `utopia_manifesto_country_landlocked`, `utopia_manifesto_subject_route_available`, triggers.
- `utopia_manifesto_start_storehouse_project`, state effect. Sets active storehouse state flag, increments ROOT active project count, and raises Need slightly until completion.
- `utopia_manifesto_complete_storehouse_project`, state effect. Marks local storehouse, decrements project count, raises Surplus, and lowers Need.
- `utopia_manifesto_start_integration_project`, state effect. Marks active integration and common administration, increments ROOT active integration count.
- `utopia_manifesto_complete_integration_project`, state effect. Marks integration complete, decrements count, improves Consent, lowers Overreach, and grants a core only when compliance, Consent, and Overreach gates pass.
- `utopia_manifesto_cleanup_project_state`, state effect. Clears active project flags.

Needful Land and relationship helpers:

- `utopia_manifesto_can_open_needful_land`, country trigger. Requires ledger and Need or Marked Bounds access, blocks worst low-Consent high-Overreach combination.
- `utopia_manifesto_needful_land_target_safe`, country trigger with PREV as Utopian country. Blocks majors, special actors, war/faction targets, and countries stronger than PREV by factories or divisions.
- `utopia_manifesto_needful_land_claim_safe`, state trigger with ROOT as Utopian country. Requires controlled non-core state and Needful Land access.
- `utopia_manifesto_can_integrate_state`, state trigger with ROOT as Utopian country. Requires controlled non-core state, administration or claim context, project availability, and peaceful or Marked Bounds integration gates.
- Relationship effects expect current scope to be the target country and PREV to be the Utopian country: `utopia_manifesto_set_relationship_observed_from_prev`, `utopia_manifesto_set_relationship_neighbor_from_prev`, `utopia_manifesto_set_relationship_friend_from_prev`, `utopia_manifesto_set_relationship_league_member_from_prev`, and `utopia_manifesto_clear_relationship_status_from_prev`.
- Relationship triggers mirror the same PREV-targeted flags.

AI and unit helpers:

- `utopia_manifesto_prepare_ai_route_weights`, country effect. Sets temp route weights for focus or decision AI from ideology, subject status, Need, chaos tier, and low Consent.
- `utopia_manifesto_spawn_household_guard`, country effect. Creates the Household Guard template if needed and spawns a capped number of batches in a random controlled state.
- `utopia_manifesto_spawn_storehouse_engineers`, country effect. Creates the Storehouse Engineers template if needed and spawns a capped number of batches in a random controlled state.

## Constants and tuning table plan

Added constant categories:

- `utopia_manifesto_event_log`
- `utopia_manifesto_target_gate`
- `utopia_manifesto_target_weight`
- `utopia_manifesto_ledger_bounds`
- `utopia_manifesto_ledger_default`
- `utopia_manifesto_ledger_delta`
- `utopia_manifesto_route`
- `utopia_manifesto_geography`
- `utopia_manifesto_decision_cost`
- `utopia_manifesto_duration`
- `utopia_manifesto_integration`
- `utopia_manifesto_ai_route_weight`
- `utopia_manifesto_relationship_status`
- `utopia_manifesto_unit`

The cost and duration constants are intentionally broader than the scaffold call sites so decision and focus integrators can use one shared tuning source.

## Event target and cleanup plan

- `utopia_manifesto_select_target` uses regular `save_event_target_as = utopia_manifesto_target`. It is short-lived and should carry into `chaosx.nr15.1` when the event is fired from the same effect chain.
- No global event target was added. If the parent needs persistent selected-target UI state later, add a global target plus explicit cleanup in the decision or GUI system.
- State project cleanup exists as `utopia_manifesto_cleanup_project_state`, but no broad all-country or all-state cleanup loop was added.
- Relationship status uses targeted country flags with `@PREV`. Parent decision/GUI call sites should clear or overwrite status through the provided relationship helpers when target country state changes.

## Migration plan for parent integration

1. Register Event 015 as Minor Fire-Once in the event registry and call `utopia_manifesto_prepare_random_event_fire` from the special dispatch branch for event id 15.
2. In `chaosx.nr15.1`, call `utopia_manifesto_accept_manifesto = yes` from the accept option and `utopia_manifesto_reject_manifesto = yes` from the reject option.
3. Add `utopia_manifesto_has_valid_target_available` to event-list availability or N/A display logic.
4. Wire decision and focus effects to set temp `utopia_manifesto_ledger_delta` before calling the exact ledger add helpers.
5. Use `utopia_manifesto_can_open_needful_land`, `utopia_manifesto_needful_land_target_safe`, `utopia_manifesto_needful_land_claim_safe`, and `utopia_manifesto_can_integrate_state` for Needful Land and integration decisions.
6. Use `utopia_manifesto_prepare_ai_route_weights` for focus or decision AI route selection variables.
7. Gate unit-spawn decisions with the cost constants before calling `utopia_manifesto_spawn_household_guard` or `utopia_manifesto_spawn_storehouse_engineers`.

## Validation performed

- Consulted required offline wiki pages and vanilla documentation for script constants, triggers, effects, event targets, random country scopes, decisions, events, ideas, AI, and unit creation.
- Inspected Event 007 and Event 010 helper patterns before creating the Event 015 scaffold.
- Verified the existing dispatcher uses `event_single_fire_allowed` and that Event 015 needs special handling because the generic dispatcher fires in the current scope.

## Risks and required parent decisions

- `utopia_manifesto_prepare_random_event_fire` self-dispatches to the selected target and marks the generic single-fire path closed for that attempt. Parent should ensure event-history logging still happens once, either by special-casing Event 015 in the dispatcher after self-dispatch or by recording history from the event chain.
- `utopia_manifesto_accept_manifesto` references `utopia_manifesto_tree`, which is not in this sidecar scope. Parent must add the focus tree before calling this helper in-game.
- Unit spawn helpers are capped and executable, but they do not pay costs themselves. Parent decisions or focus rewards must apply equipment, manpower, XP, and cooldown gates before calling them.
- Integration helpers grant a core only after compliance, Consent, and Overreach gates pass. If the final design needs multi-stage progress variables per state, add that in the decision implementation rather than replacing this safety gate with instant coring.
- Known mutually exclusive focus-tree blockers are represented by current project flags that were visible in the inspected code. Parent may need to add more event-created tree exclusion flags as other Event 015 integration work reveals them.
