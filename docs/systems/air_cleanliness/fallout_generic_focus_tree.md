# Fallout generic survivor focus tree

The Fallout rewrite grants one shared focus tree to every country after the map-return phase. The tree is deliberately loaded after survivor and fracture assignment, so every retained tag and every dynamic Independence Wave template receives the same playable decision surface without loading an Independence Wave tree.

## Runtime contract

The transition success branch in `common/scripted_effects/fallout_consolidated_effects.txt` sets `fallout_active`, iterates every country once, and calls `fallout_generic_focus_activate`. The effect is idempotent for the current `global.fallout_transition_generation`. It loads `fallout_generic_focus_tree` with `keep_completed = no`, marks the layout dirty, sets `fallout_generic_focus_tree_loaded`, and initializes the country values.

The tree is in `common/national_focus/fallout_consolidated_focus.txt`. Its country weight is zero because it is a runtime tree. The activation effect is the only active loader. The retained NZL and USA package tree definitions are legacy dormant content with no active loader and are not used as the universal Fallout tree.

## Player-facing routes

The opening counts survivors, maps usable frontier, and secures the capital. Four mutually exclusive government routes then shape the campaign:

- Civic Compact restores elections and builds cohesion through councils.
- Ration Congress centralizes food and workshop capacity.
- Command Directorate turns the frontier into a military chain of orders.
- Shelter Council protects sealed stores before it permits elections.

After the route split, every country can reopen power, repair rails, reclaim workshops, raise and train a survivor guard, arm a cordon, open a radio net, found the Frontier Pact, claim adjacent states, issue a state-targeted annexation ultimatum, and settle the resulting border. The Pact is a real faction and its invitation focus records an opinion invitation for eligible Fallout countries.

The regional branch uses the assigned `fallout_region_id` and exposes one of nine concrete lanes. North America receives relay work, Europe receives water councils, the Eurasian interior receives inland roads, East Asia receives seed banks, South Asia receives delta routes, the Middle East and North Africa receive quarantine roads, sub-Saharan Africa receives river wards, Latin America and the Caribbean receive water charters, and Oceania receives remote stations. The late branch federates survivor leagues, reclaims the heartland, and records the Year Ten order.

## Dynamic state values

`fallout_generic_authority`, `fallout_generic_cohesion`, `fallout_generic_frontier_pressure`, `fallout_generic_regional_influence`, and `fallout_generic_memory` are country values initialized from `fallout_generic_focus` constants and clamped to zero through one hundred. Route identity is recorded in `fallout_generic_route_id`. Frontier focuses add claims to adjacent owned-state neighbours with a valid owner. The ultimatum helper selects one adjacent owner at completion and creates an `annex_everything` wargoal with the shared expiry constant.

## Asset and localisation contract

Every focus title and description is in `localisation/english/fallout_consolidated_l_english.yml`. The tree uses confirmed vanilla goal sprites only. No Fallout-specific focus sprite, folder, or asset is required. The reused icon names are `GFX_goal_generic_national_unity`, `GFX_goal_generic_more_territorial_claims`, `GFX_goal_generic_defence`, `GFX_goal_generic_production`, `GFX_goal_generic_major_war`, `GFX_goal_generic_alliance`, `GFX_goal_generic_scientific_exchange`, `GFX_goal_generic_construct_infrastructure`, `GFX_goal_generic_construct_mil_factory`, `GFX_goal_generic_allies_build_infantry`, `GFX_goal_generic_army_motorized`, `GFX_goal_generic_radar`, `GFX_goal_generic_major_alliance`, `GFX_goal_generic_territory_or_war`, `GFX_goal_generic_demand_territory`, and `GFX_goal_generic_build_navy`.

## Review evidence

Static review found thirty-two focus nodes plus the tree id, unique Fallout focus ids, balanced source braces, a cost, icon, AI weight, and localisation title and description for every focus. The nine regional branches all use `allow_branch` against the assigned region enum. Vanilla evidence for `load_focus_tree` and `mark_focus_tree_layout_dirty` is recorded in the accepted engine-reference notes and the official effects documentation.

The installed focus MCP was attempted against the consolidated source, but its workspace scan returned `SCAN_BYTE_LIMIT` before reading any file. No live Hearts of Iron IV execution was performed, as live validation belongs to the user.

## Future extension

Country-memory overlays can later be layered on this tree through additional reviewed focus branches or decisions. That is intentionally outside this tranche. The generic tree already supplies government, regional, pact, war, border, industry, military, and late-order mechanics for every Fallout country.
