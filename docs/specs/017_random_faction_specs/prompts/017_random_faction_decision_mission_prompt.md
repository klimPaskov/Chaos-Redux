# Decision and mission prompt for Event 17: Random faction

Use `hoi4-decisions-missions`, `chaos-redux-events`, and the Event 17 spec files. Implement the Bloc Pressure decision category and mission families from `matrices/017_random_faction_decision_map.md`.

Core requirements:

- decisions must represent real action, not a political power store
- use concrete costs such as support equipment, infantry equipment, command power, army XP, stability, war support, divisions in states, convoys, trains, trucks, or supply access where appropriate
- use timed missions for border posts and corridor proof
- use custom tooltips and scripted localisation for requirements
- hide obsolete decisions when pressure ends
- faction leader decisions must target valid pressured or aligned minors
- AI must have equivalents for human-facing actions
- cleanup must remove missions, target flags, variables, and category visibility when the country joins a faction, becomes invalid, or the source faction disappears

Audit after implementation with `chaosx_decision_mission_auditor`.
