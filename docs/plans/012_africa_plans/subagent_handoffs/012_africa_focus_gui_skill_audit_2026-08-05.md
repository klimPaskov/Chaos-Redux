# Event 012 Africa focus and Charter GUI skill audit - 2026-08-05

## Scope

This audit applies `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, and `chaos-redux-events` to the Event 012 external focus packages and the Charter League scripted GUI.

It uses the HOI4 MCP focus and GUI inspection/render routes and does not launch Hearts of Iron IV.

The branch-conditioned continental overlay coordinates in `common/national_focus/012_africa_continental_focus_tree.txt` remain unchanged because the static inspector cannot select a host and overlay branch.

## Focus-tree changes

The six external package files contain 121 focuses with unique IDs and coordinates.

Every external focus has a meaningful `search_filters` field, a completion reward, and an inline AI weight.

The filters distinguish political, stability, industry, military, air, and naval route institutions instead of leaving constitutional and post-route nodes invisible to focus search.

The shared constitutional lanes previously required every route-specific institution in the same prerequisite block even though the route focuses are mutually exclusive.

Those convergence gates now use an `OR` prerequisite so one selected constitution can reach its shared lane while the existing route-aware completion effects continue to apply.

The Middle East command, Red Sea and Nile treaty, and withdrawal law use common visible preparation prerequisites with route-specific `available` OR gates so their hard conditions remain playable without long or crossing connectors.

Where a secondary prerequisite would create a long connector or cross an unrelated lane, it remains an exact `has_completed_focus` condition in `available` rather than a visible line.

The Europe post-colonial treaty keeps its colonial-reckoning requirement in `available` for the same layout reason.

The external tree IDs, focus references, rewards, route flags, and shared-lane effect calls remain unchanged apart from the reachability correction above.

## MCP focus evidence

`hoi4_focus_inspect` returned `FOCUS_INSPECTED` for Asia, Europe, Middle East, North America, Oceania, and South America with zero Event 012 diagnostics.

`hoi4_focus_render` returned `FOCUS_RENDERED` for all six external trees at horizontal spacing 120, vertical spacing 100, and padding 40.

All six rendered trees report zero authored layout warnings after the compact source edits.

The workspace validation still reports 14 unrelated missing continuous-focus sprites in vanilla `common/continuous_focus/generic.txt`.

The main branch-conditioned tree still produces branch-unaware static overlap diagnostics; moving those authored descendants would damage runtime overlay placement.

The MCP compact-layout rewrite returned `FOCUS_COMPACT_QUALITY_BLOCKED` on the four trees that needed the most manual compaction, so the source layouts were patched directly and then rerendered successfully.

## Charter GUI changes

The header now has non-overlapping value columns with authority as the primary signal and reach, integration burden, and colonial pressure as the supporting values.

The authority ring occupies the clear right header slot, and the regional metrics/state-candidate boundary has an explicit gap.

All five state rows remain inside the 1000 by 680 window with distinct click regions.

State controls mirror the decision gate by requiring a live quote, a state or region target mode, an available candidate, unused regional capacity, and a candidate that is not already selected.

Family tabs disable the currently selected family, and the high-chaos tab also requires `africa_evolution_iii_logged`.

Overlay and diaspora selectors remain cursor-only inputs and use scaled button text so direct public names fit their fixed click regions.

## MCP GUI evidence

`hoi4_gui_inspect` returned `GUI_INSPECTED` for `africa_charter_window` with no Event 012 diagnostics.

`hoi4_gui_render` returned `GUI_RENDERED` with 24 artifacts across 1920 by 1080, 1366 by 768, and 2560 by 1440 resolutions in normal, disabled, warning, and long-text states.

A source geometry audit found 35 button controls and zero overlapping click regions.

## Remaining audit notes

The member roster cursor still uses bounded roster-array indices in the GUI, while execution-side action validation remains authoritative.

Advanced action families remain available through the decision ledger rather than adding more simultaneous Charter buttons.

No 3D models or new visual assets were created in this tranche.

Live HOI4 runtime testing remains user-owned.

The overall Event 012 Africa goal remains blocked because the broader country, asset, audio, achievement, event, and world-order surfaces are outside this focus and GUI audit tranche.
