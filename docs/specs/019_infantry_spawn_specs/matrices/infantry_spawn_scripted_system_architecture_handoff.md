# Infantry Spawn scripted system architecture handoff

This file is a design handoff for `chaosx_scripted_system_architect`. It does not contain final code.

## Helper families needed

| Helper family | Purpose | Inputs | Outputs or side effects |
| --- | --- | --- | --- |
| country eligibility | decide which countries can receive the event | country scope, event state, special chaos classification | valid or invalid result |
| state eligibility | find safe controlled states | country scope, state filters, special exclusions | state candidate list or selected state |
| density calculation | lower per-state spawn density for large countries without a hard cap | controlled state count, war state, fatigue, supply, stability | per-state chance or density band |
| spawn budget | decide how many units and how strong | density band, evolution, war state, chaos, country strength | unit budget and quality band |
| template family selection | choose baseline, organized, arsenal, random, or chaos profile | evolution, state class, country values | template family id |
| random battalion builder | assemble Evolution III divisions | absurdity, coherence, support pool, battalion pool | created division or selected fixed template |
| strain application | apply supply, command, depot, and training effects | spawned unit count, quality, heavy unit count | country variables and temporary ideas |
| management values | raise and lower seven core values | decisions, missions, events, repeats | visible country variables |
| possessed general selector | create or assign a scary general | country scope, portrait pool, name pool | character, commander, demand seed |
| revolt builder | build human or chaos breakaway | parent, target states, linked units, profile | tag setup, units, war, cleanup flags |
| chaos unit registry | future-proof chaos unit availability | unit profile registry | spawn, train, splinter, exclusion rules |
| scenario launcher | launch selected type and intensity | scenario UI variables | setup flags, spawns, immediate revolts, cleanup |
| cleanup | remove stale flags and targets | country, tag, scenario, mission state | no stale decisions or leaked targets |

## Constants and tuning groups

Recommended constants should be grouped by purpose:

- density bands by controlled state count
- baseline and evolution quality weights
- war and peace modifiers
- heavy unit weights
- random battalion count bands
- support company count bands
- on-demand cooldown and escalating cost multipliers
- command coherence, supply strain, absurdity, appetite, and leakage thresholds
- general demand MTTH or weighted roll factors
- revolt strength bands
- chaos unit registry weights
- scenario intensity values
- AI willingness thresholds

Durations that reject global script constants should use file-scoped constants or meta effects according to repository rules.

## Event targets and cleanup

Likely event targets:

- selected_muster_state
- selected_depot_state
- selected_general_character
- selected_splinter_country
- selected_parent_country
- selected_scenario_country

Global event targets should be avoided unless persistence is truly needed. If used, they must be cleared through cleanup helpers.

## Documentation requirement

Any new reusable dynamic helper should be documented in the matching markdown file beside the scripted effect or trigger file. The docs should state purpose, scope, inputs, outputs, side effects, defaults, and an example call site.
