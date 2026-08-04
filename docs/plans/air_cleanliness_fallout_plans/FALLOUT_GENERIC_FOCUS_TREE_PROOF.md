# Fallout generic focus tree proof

Date: 2026-08-04

## Outcome

`common/national_focus/fallout_consolidated_focus.txt` defines one runtime tree named `fallout_generic_focus_tree` with thirty-three manually reviewed focuses. Every surviving original tag and every completed fracture output receives the tree after map return. No Independence Wave focus package is loaded.

## Loader and reset proof

`fallout_apply_transition_phase_map_return` calls the global state-flag cleanup once, then activates the generic tree for every country carrying `fallout_country_survives`. `fallout_generic_focus_activate` is generation-bound and idempotent. It loads the tree with `keep_completed = no`, calls `mark_focus_tree_layout_dirty`, sets its load receipt, and initializes all universal values.

Reset refunds unresolved Frontier Pact equipment payments, removes old decisions and late ideas, clears route and campaign variables, and clears stale state receipts before a generation can load again.

## Route coverage

| Layer | Implemented surface |
| --- | --- |
| Opening | Survivor count, ruin survey, capital security |
| Government | Civic Compact, Ration Congress, Command Directorate, Shelter Council |
| Recovery | One power loop, one rail spine, bounded service-state and workshop recovery |
| Military | Survivor Guard, Frontier Columns, one-state cordon fortification |
| Diplomacy | Radio net, Frontier Pact creation, neighbour invitation |
| Border pressure | Adjacent claims, exact target-state ultimatum receipt, ownership-and-control settlement gate |
| Regions | Regional ledger and nine `fallout_region_id` lanes |
| Decisions | Claims, route consolidation, corridor repair, integration, frontier pressure, Pact recruitment, regional extension |
| Late order | Survivor federation, exact heartland target receipt, ten-year capstone |

## Result receipts

The border ultimatum stores `fallout_generic_border_target_country`, `fallout_generic_border_target_state`, and the current transition generation. `fallout_generic_border_campaign_resolved` requires the same generation plus ownership and control of that exact state. `fallout_generic_settle_the_new_border` cannot begin without that proof.

The heartland route uses separate `fallout_generic_heartland_*` variables, flag, and state marker. The Year Ten focus accepts the federation route or a resolved heartland campaign. It also requires the regional programme, configured memory and influence thresholds, and the day stored as Fallout map return plus 3,650 days.

## AI and region proof

All twelve government archetypes appear exactly once in the four route weight families. Every regional focus has a matching region-id AI modifier. Diplomacy and expansion keep their own validity gates, so an AI cannot complete them against a stale faction or state target.

## Localisation and assets

All focus titles, descriptions, requirement tooltips, decision text, custom costs, and late ideas resolve in the UTF-8 BOM English localisation file. The package uses sixteen confirmed vanilla focus sprites and existing vanilla decision and idea sprites. No new focus artwork is required.

## Renderer proof

The latest installed renderer pass found thirty-three nodes, thirty-six connectors, no node intersections, six connector crossings, twelve long connectors, and a maximum vertical span of five. The HTML artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/022e833f45abc67b804ea0ade2edf9557a4f82ff39fde46e75c3123b81117eaa/9f5d6e0123117cbae7d5a49704c9e8f76ce3d56de75cf966847deb4e43e04184/fallout_generic_focus_tree.focus.html` and the SVG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e378fa977ef9c393eda4fe44d05e48bd6f16b9ee28361ab880370281df106a8/ad9b0c25128f71d77cb729b1228afa469e54527f637400341b1ce1a2afa833d7/fallout_generic_focus_tree.focus.svg`.

The renderer reports missing generic icons because its mod-only scan does not index installed vanilla GFX. Direct installed-game inspection found every referenced goal sprite in `interface/goals.gfx`.

## Scope boundary

Live HOI4 testing and bespoke country trees are explicitly outside this goal. The universal tree is the complete focus surface required for the core Fallout consequence package.
