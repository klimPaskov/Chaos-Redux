# Event 006 focus geometry closure — 2026-08-25

## Scope

This bounded tranche changes authored coordinates only in `common/national_focus/006_independence_wave_focus.txt`. Focus IDs, prerequisites, mutual exclusions, availability predicates, completion rewards, helper effects, AI blocks, icons, localisation keys, costs, and route gates are unchanged. No package admission, event, decision, mission, or probability surface is changed.

## Accepted coordinate layout

The reviewed coordinate-only reflow places the six-focus economy trunk at `x = 31`, with `independence_wave_create_independent_treasury` at `y = 7`, and retains the previously reviewed military/archetype lane and row-eight choice cohort alignment.

The five-focus military trunk remains at `x = 42` from `independence_wave_integrate_militia_commands` through `independence_wave_adopt_military_archetype_program`, on `y = 3..7`.

To preserve the clean connector graph without introducing the long edge produced by the trial military shift, the adjacent row-five lanes use `x = 44` for `independence_wave_declare_entrenched_neutrality`, `x = 46` for `independence_wave_balance_the_first_patrons`, and `x = 48` for `independence_wave_open_separation_talks`. The former-host settlement chain uses `x = 48` for `independence_wave_settle_property_and_citizenship` and `independence_wave_recognize_the_frontier`; the former-host root and regional convergence retain their reviewed coordinate-only reflow. These are coordinate-only changes; the branch logic is unchanged.

## MCP evidence

Fresh `hoi4.focus_inspect` on workspace `mod_chaos_redux_ea3b2d67c2c0` returned revision `44220c1ffcb7c1a24bbe122dd5c36c615d245d24915580572f985208e7ef3c2a` with 184 focuses and 195 connectors. Event 006 layout metrics are zero crossings, zero node intersections, zero long connectors, zero too-close same-row pairs, minimum same-row spacing 2, maximum horizontal span 8, and `diagnosticCount = 0`.

Fresh `hoi4.focus_render` returned `FOCUS_RENDERED` with layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, validation passed, and HTML/SVG/JSON/source-map/plan artifacts. The rendered dimensions are 21424x2440, so the separate raster route remains blocked by its 16384-pixel ceiling. The only remaining diagnostic is the unrelated vanilla `continuous_restrict_freedom_desc` localisation reference.

No live game, save/load, or player-owned runtime receipt is claimed.

## Boundary

This closes the current Event 006 focus geometry diagnostics but does not change the wider implementation disposition. Event 006 remains **HOLD / PARTIAL** at 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows. IW-050 remains queued and evidence-blocked; no central admission or fallback is introduced by this tranche.
