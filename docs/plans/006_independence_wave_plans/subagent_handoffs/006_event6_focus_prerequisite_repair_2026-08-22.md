# Event 006 focus prerequisite repair — 2026-08-22

## Scope

Restored the visible military-archetype prerequisite for the two mutually exclusive Event 006 military choices while preserving the existing removal of impossible capstone prerequisites from the professional-defense focus.

## Source change

Changed `common/national_focus/006_independence_wave_focus.txt`:

- `independence_wave_standardize_with_league` now has `prerequisite = { focus = independence_wave_adopt_military_archetype_program }`.
- `independence_wave_preserve_independent_command` now has `prerequisite = { focus = independence_wave_adopt_military_archetype_program }`.
- Existing removals from `independence_wave_found_professional_defense_institution` were preserved; no capstone-specific prerequisites were reintroduced.

## Evidence

The mandatory HOI4 MCP national-tree inspection completed with `FOCUS_INSPECTED` at revision `f7beb4f84e132199362bbd60b00844fc82f8c85c2077f2198a030aef63535f11`. The Event 006 tree contains 184 focuses and 195 connectors with zero crossings and zero node intersections. The two previously isolated military choices now have explicit graph connectors from `independence_wave_adopt_military_archetype_program`.

The mandatory HOI4 MCP render completed with `FOCUS_RENDERED` and produced HTML, SVG, JSON, source-map, and plan artifacts under workspace `mod_chaos_redux_ea3b2d67c2c0`. Event-specific diagnostics now contain only the pre-existing layout warnings (seven linear-detour/long-connector warnings); the remaining 14 blocking diagnostics are generic vanilla continuous-focus icon references outside this Event 006 source file.

## Remaining risk

The two direct connectors are long because the authored focus coordinates are widely separated. The render is structurally valid; no automatic layout rewrite was applied because it would rewrite the accepted authored tree. Generic vanilla continuous-focus diagnostics remain outside this scoped repair.
