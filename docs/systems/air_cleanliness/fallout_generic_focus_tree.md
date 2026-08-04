# Fallout generic survivor focus tree

The Fallout rewrite grants one shared focus tree and decision category to every surviving country after map return. Original countries and new fracture countries receive the same package. Independence Wave trees are never loaded by this system.

## Runtime contract

`fallout_apply_transition_phase_map_return` calls `fallout_generic_focus_clear_state_runtime` once, then calls `fallout_generic_focus_activate` for every country carrying `fallout_country_survives`. Activation is idempotent for `global.fallout_transition_generation`, loads `fallout_generic_focus_tree` with `keep_completed = no`, marks the layout dirty, initializes the country values, and opens the generation-bound decision category.

The tree is defined in `common/national_focus/fallout_consolidated_focus.txt`. Its country weight is zero because only the Fallout transition loads it. Retained bespoke pilot tree definitions have no active loader and are not part of the universal package.

## Player routes

The opening counts survivors, maps usable land, and secures the capital. Four mutually exclusive government routes represent civic councils, ration administration, military command, and shelter rule. All twelve Fallout government archetypes map to one of those routes through explicit AI weights.

The recovery and military layers reopen one power loop, repair one rail spine, reclaim workshops, equip a survivor guard, train frontier columns, and fortify one controlled frontier state. The diplomacy layer opens radio links, permits an independent country outside every faction to found the Frontier Pact, and allows its leader to invite neighbouring survivor governments.

The expansion layer claims eligible adjacent ash zones and dead cities. Issuing an ultimatum records the exact target country, target state, and Fallout generation. Border settlement remains unavailable until the acting country owns and controls that recorded state. The separate heartland campaign records its own target and generation. The Year Ten capstone requires either the survivor federation or ownership and control of the recorded heartland target, a completed regional programme, the configured memory and regional influence floors, and exactly ten years of elapsed availability.

The regional ledger exposes one of nine authored lanes through `fallout_region_id`: North America relays, European water councils, Eurasian inland roads, East Asian seed banks, South Asian delta routes, Middle East and North African quarantine roads, sub-Saharan river wards, Latin American water charters, and Oceanian remote stations.

## Decision layer

`fallout_generic_survivor_mandate_category` displays authority, cohesion, frontier pressure, regional influence, and memory. Its actions survey adjacent claims, consolidate the chosen government, repair one selected corridor, integrate a controlled state, pressure a selected neighbour, negotiate a Frontier Pact membership, and extend the assigned regional network.

The Frontier Pact mission debits support equipment when negotiations start. It refunds the same receipt on cancellation and consumes one payment on success. Border pressure refunds its pressure payment if the mission cancels. Tree reset refunds every unresolved Pact payment before removing the old decisions.

## State helper contracts

The following subsystem-private effects are defined in `common/scripted_effects/fallout_consolidated_effects.txt`.

### `fallout_generic_focus_improve_one_service_state`

Purpose: add one infrastructure level to one random owned and controlled state below the wasteland grade.

Scope: country.

Inputs and defaults: no temporary input is required. If no valid service state exists, the effect does nothing.

Side effects: at most one state receives immediate infrastructure construction. No target or receipt is retained.

Usage: `fallout_generic_focus_improve_one_service_state = yes`.

### `fallout_generic_focus_improve_one_border_state`

Purpose: add one infrastructure level to one owned and controlled state adjacent to foreign land.

Scope: country.

Inputs and defaults: no temporary input is required. The controlled capital is the fallback when no foreign frontier exists.

Side effects: at most one state receives immediate infrastructure construction. No target or receipt is retained.

Usage: `fallout_generic_focus_improve_one_border_state = yes`.

### `fallout_generic_focus_fortify_one_frontier_state`

Purpose: add the centralized bunker level to one owned and controlled state adjacent to foreign land.

Scope: country.

Inputs and defaults: no temporary input is required. The controlled capital is the fallback when no foreign frontier exists.

Side effects: at most one state receives immediate bunker construction. No target or receipt is retained.

Usage: `fallout_generic_focus_fortify_one_frontier_state = yes`.

## Values and cleanup

Authority, cohesion, frontier pressure, regional influence, and memory are initialized from shared constants and clamped from zero through one hundred. Government route, regional lane, and campaign targets are generation-bound. Tree reset removes late ideas, clears pending targets and state flags, refunds unresolved Pact payments, and removes stale decisions. The map-return state cleanup scans the state collection once per Fallout generation so flags cannot survive an ownership change.

## Assets and localisation

Every focus, decision, tooltip, cost, and late idea has English localisation in `localisation/english/fallout_consolidated_l_english.yml`. The package uses installed vanilla goal, decision, and idea sprites. It adds no Fallout-specific focus artwork.

## Review evidence

The installed focus renderer found thirty-three nodes, no node intersections, six connector crossings, twelve long connectors, and a maximum vertical connector span of five rows. Every focus has a title, description, icon, cost, and AI surface. All sixteen referenced goal sprites are present in installed vanilla `interface/goals.gfx`.

The current tree consumes all twelve government archetypes and all nine regions. State rewards are bounded to one state per helper call. Border and heartland progress use exact state-result receipts rather than treating an issued wargoal as a completed expansion.

## Future extension

Bespoke country trees remain outside this package. Country-memory overlays and later authored event content can deepen individual identities without replacing the universal campaign surface.
