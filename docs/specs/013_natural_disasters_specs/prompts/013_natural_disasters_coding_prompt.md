# Coding prompt for Event 013 Natural Disasters

Implement Event 13 Natural Disasters according to the source spec package under `docs/specs/013_natural_disasters_specs/`.

Read and follow `AGENTS.md`, `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-subagents`, and the relevant offline HOI4 wiki and vanilla documentation before editing.

## Source files to follow

- `specs/013_natural_disasters_spec.md`
- `specs/013_natural_disasters_external_event_boundary.md`
- `specs/013_natural_disasters_individual_disaster_playbooks.md`
- `specs/013_natural_disasters_big_disaster_decision_categories.md`
- `specs/013_natural_disasters_evolutions_cluster_scenario.md`
- `specs/013_natural_disasters_recovery_gui_spec.md`
- `matrices/013_natural_disasters_big_disaster_category_matrix.md`
- `matrices/013_natural_disasters_disaster_family_matrix.md`
- `matrices/013_natural_disasters_ai_matrix.md`
- `matrices/013_natural_disasters_effects_tuning_matrix.md`
- `matrices/013_natural_disasters_validation_matrix.md`
- all prompt files in `prompts/`

## Non negotiables

- Event 13 remains Minor Repeatable.
- One Event 13 sequence creates one random event log row. Subevents inside that sequence must not spam random event history.
- Disasters are delayed from one another. Baseline sequences should not feel same day stacked.
- Building damage, population loss rates, civilian deaths, supply penalties, aftermath modifiers, decisions, missions, AI priorities, and assets must be family specific.
- Population loss feeds the shared deaths system through per state dynamic percentages. Do not use fixed casualty amounts, fixed per state death totals, or absolute death caps. Compute `current_state_population * final_dynamic_loss_rate` for each affected state, then log civilian deaths and reduce real population.
- Severe disasters must be able to kill millions when the computed percentage hits dense states or dense regional chains. Dense Chinese, Indian, Javanese, Japanese, European, and other high population states must naturally suffer larger absolute deaths than sparse states under the same loss rate.
- Natural disasters must not add condemnation.
- No Event 13 world end branch exists.
- Event 51 Heat Wave, Event 99 Sandstorm, Event 28 Asteroid Incoming, Event 43 Massive Flood, Event 46 Unknown Placeholder, Event 47 BOOM, and any separate Meteor Shower placeholder are not logic sources. Do not copy, call, adapt, or tune around their old code.
- Sandstorm active gameplay routes through Event 13. Event 99 is a placeholder or wrapper only.
- Event 46 stays inactive and unknown. Event 13 owns seismic content.
- Event 13 heat content must not stack with active Event 51 heat effects. Convert to drought, wildfire, water emergency, or unique heat aftermath when needed.
- Event 13 meteor showers must not reuse Event 28 Asteroid Incoming. Asteroid Incoming is a single object future rework. Meteor showers are multi impact disaster sequences.
- Evolution I adds varied local disaster families.
- Evolution II adds regional disaster systems, neighboring state damage, family categories, supply penalties, and chained aftermath.
- Evolution III adds meteor showers, massive rupture wave, massive volcano, delayed tsunami, and moving storm corridor variants without world end behavior.

## Big disaster category requirement

Do not implement one generic recovery list for every major disaster. The generic Natural Disaster Recovery overview is the small incident hub. Every serious, regional, catastrophic, and abnormal disaster that directly hits a country opens its family category from `013_natural_disasters_big_disaster_decision_categories.md`.

Required family categories include Flood Relief Authority, Cyclone Emergency Command, Severe Storm Response Board, Storm Corridor Command, Seismic Emergency Authority, Great Rupture Command, Tsunami Coastal Command, Volcanic Crisis Board, Massive Eruption Command, Firefront Command, Drought and Famine Board, Heat Emergency Board, Winter Emergency Directorate, Dust Emergency Board, Landslide Rescue Board, Slope Collapse Response, Skyfall Emergency Bureau, Meteor Storm Command, and Famine and Displacement Commission.

Each category needs visible values, decision families, missions, non political costs, AI use, localisation, icons, cleanup, and category hiding when the disaster ends. Categories must be curated, with active caps and phase filters.

## Cluster and scenario

Implement the Natural Disasters cluster with multiple conceptual Event 13 member slots and delayed member sequences. Implement Disaster Barrage as the next free triggerable scenario, using type and intensity controls, direct launch, and no ordinary chaos or evolution prerequisites.

## GUI and assets

The scripted GUI or decision category presentation must show active warnings, impacts, aftermaths, active family category, recovery state, and selected state where relevant. Evolution III moving disasters need map tracking or an equivalent readable presentation. Animated assets require real frame source packages and static fallbacks. Do not use transform only animation as final art.

## Subagent routing

Use `chaosx_scripted_system_architect` before duplicating disaster family, target selection, damage, recovery, scheduling, category, or percentage death logic. Use `chaosx_decision_mission_auditor` after the categories and missions are implemented. Use `chaosx_localisation_auditor` after broad text is written. Use asset subagents for icons, report images, news images, GUI assets, and animated sprites. Use `chaosx_event_completion_auditor` before claiming completion. Use `chaosx_spreadsheet_doc_worker` only after in game wording exists.

## Completion report requirements

Report changed files, event ids, decision ids, category ids, mission ids, helper names, scripted GUI ids, localisation keys, cluster ids, scenario ids, asset sprite names, docs changed, meaningful validation, remaining blockers, and any simplification. If no simplifications remain, say so with evidence. Do not claim completion until the implementation satisfies the full spec package.
