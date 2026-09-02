# Event 006 DM-03 anchor and local-peace gate — 2026-09-03

## Scope and disposition

This bounded repair aligns the automatic Register the Population mission with the accepted Event 006 decision map. The mission now requires the released country to own and control its reserved anchor state while it is not at war, and it cancels when either condition is lost.

The repair is source-complete for this decision surface. It does not promote a country package, add a decision category, create a pre-event pressure surface, or claim live engine or save/load evidence.

## Files and identifiers changed

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`: added `is_independence_wave_register_population_anchor_secure`, a country-scope helper that checks `independence_wave_anchor_state`, exact ownership and control by `ROOT`, and `has_war = no`.
- `common/decisions/006_independence_wave_decisions.txt`: added the helper to `independence_wave_register_population` activation and replaced the unsafe `capital_scope` cancellation probe with the helper's negation.
- `localisation/english/006_independence_wave_decisions_l_english.yml`: describes the anchor-control and out-of-war requirements in player-facing terms.

## Evidence and validation

The accepted row `DM-03` in `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv` requires control of the anchor territory and local peace. The mission remains an automatic, non-selectable timed mission, matching the existing vanilla-style lifecycle.

Static source review confirms the helper is defined once, referenced by both DM-03 activation and cancellation, and no DM-03 `capital_scope` probe remains. The Event 006 allocator and scenario validators remain the relevant parent-owned checks; no live Hearts of Iron IV process was launched and no MCP event comparison was available for this narrow trigger change.

## Remaining limits

The implementation maps local peace to the country being out of war because HOI4 has no native per-state war trigger. A later owner-approved semantic change may narrow this to a specific host or anchor conflict, but no such alternate interpretation was invented here.

No simplification, fallback, new asset, or unrelated package admission was introduced.
