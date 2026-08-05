# Event 006 supported-effect correction

Date: 2026-08-05.

Scope: narrow source correction in the shared Independence Wave crisis and package-planner effects. This handoff uses current repository and vanilla documentation evidence only; obsolete pasted runtime logs were not used.

## Changes

- Replaced the unsupported `add_army_experience` form with the documented `army_experience` effect in `common/scripted_effects/006_independence_wave_crisis_effects.txt`.
- Replaced unsupported `clear_temp_variable` calls with documented `set_temp_variable = { ... = 0 }` assignments after event-log payload submission in the crisis history/resolution paths.
- Replaced the same unsupported temporary-variable clears in `common/scripted_effects/006_independence_wave_package_planner_effects.txt` after reservation and allocation-weight work.

The correction does not change the accepted crisis costs, allocation order, package admission gates, release ladder, or dynamic values. It only keeps the existing values from leaking into later scripted blocks while using documented effects.

## Evidence

- Vanilla `documentation/effects_documentation.md` documents `army_experience` and `set_temp_variable`.
- Event 006 allocator audit passes with 149 publishers, 16 attested packages, 15 compatible reservation groups, and the 6/8/10/14/20 ladder.
- Event 006 strict flag audit passes all 102 registered tag families.
- SCN-008 matrix audit passes all 32 mode/intensity cells and eight edge cases.

## Non-goals

No package was promoted, no portrait/flag/advisor asset was added, no formable was opened, no runtime log was consulted, and no whole-event completion claim is made.
