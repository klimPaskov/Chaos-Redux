# Decision and mission implementation prompt for Event 013 Natural Disasters

Use `hoi4-decisions-missions`, `chaos-redux-events`, and the Event 13 spec. After implementation, use `chaosx_decision_mission_auditor` for a focused audit and local patches.

## Core correction

Do not implement Natural Disasters as one generic recovery category. The generic Natural Disaster Recovery overview is a small local incident hub. Every big disaster that directly hits a country must open a family specific decision category with its own values, decisions, missions, AI, costs, tooltips, icons, and cleanup.

Follow:

- `specs/013_natural_disasters_big_disaster_decision_categories.md`
- `specs/013_natural_disasters_individual_disaster_playbooks.md`
- `matrices/013_natural_disasters_big_disaster_category_matrix.md`

## Required family categories

Implement these working category surfaces or equivalent final ids that preserve the design.

- Flood Relief Authority
- Cyclone Emergency Command
- Severe Storm Response Board
- Hail Damage Board when regional hail damage matters
- Wind Damage Control when extreme wind is serious
- Storm Corridor Command
- Seismic Emergency Authority
- Great Rupture Command
- Tsunami Coastal Command
- Volcanic Crisis Board
- Massive Eruption Command
- Firefront Command
- Drought and Famine Board
- Heat Emergency Board
- Winter Emergency Directorate
- Dust Emergency Board
- Landslide Rescue Board
- Slope Collapse Response
- Skyfall Emergency Bureau
- Meteor Storm Command
- Famine and Displacement Commission

## Required behavior

- Show warning decisions only during warning windows.
- Show impact decisions only for active ledgers.
- Show recovery missions only for unresolved aftermaths.
- Show only the family actions relevant to the active disaster.
- Use phase filters and active caps so categories are not debug menus.
- Use family specific costs and requirements.
- Use infantry equipment, support equipment, trucks, trains, convoys, fuel, manpower, army XP, navy XP, air XP, conservative command power, stability, war support, supply, state control, route access, local objectives, and time pressure as appropriate.
- Political power can support administrative or diplomatic actions, but it must not be the default cost.
- Every decision and mission needs readable blocked requirement text.
- Every mission needs success, failure, partial success where useful, and cleanup.
- AI needs an equivalent route for every important action.
- Serious categories must include at least one real objective. Do not use passive stockpile checks as the main mission.

## Death related decision rule

Decisions may reduce or increase a dynamic loss rate, but they must not add or subtract fixed death numbers. For example, evacuation lowers the final per state loss rate. It does not save a fixed number of people. Failed recovery raises follow up loss rates. It does not add a fixed death total.

## Audit expectations

The decision auditor should check:

- category lifecycle and cleanup,
- family specific category coverage,
- active caps and target filtering,
- non political cost coverage,
- duplicate missions,
- missing AI use,
- invalid target cleanup,
- raw trigger exposure,
- exploit risks,
- missing localisation keys,
- missing state or region names in requirement text,
- no fixed casualty amounts hidden in decisions or mission failure effects.
