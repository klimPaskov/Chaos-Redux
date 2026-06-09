# Decision and Mission Prompt for Event 007 Fury

Implement the Event 007 Fury decision and mission layer according to:

- docs/specs/007_fury_specs/007_fury_decisions_missions_spec.md
- docs/specs/007_fury_specs/007_fury_spec.md
- AGENTS.md
- hoi4-decisions-missions
- chaos-redux-events

Non-negotiables:

- no player country can receive Fury decisions
- no player country can be selected as scripted Fury target
- decision category must clean up after Fury ends
- costs must use concrete resources where the action demands it, not only political power or command power
- active coring or integration decisions must be capped and target valid states only
- missions must be real objectives, not passive checklists
- AI must understand when to expand, integrate, slow down, or coordinate

Build these families:

1. Prepare the Next Border War.
2. Seize Border Depots.
3. Captured Depot Mobilization.
4. Install Provisional Administration.
5. Proclaim Frontier Core.
6. Coordinate the Next War from Evolution II onward.
7. Emergency War Tables for General Staff or Evolution III.
8. Convene the March Council for administration or no-neighbor play.
9. Open the Continental Mandate for world-end preparation.

Build these mission families:

- Hold the First Capital.
- Guard the Captured Border.
- Keep the March Supplied.

Required validation:

- duplicate mission check
- invalid target cleanup
- AI target safety
- player exclusion
- coring exploit check
- repeatable unit farming check
- stale decision visibility check

Report every decision id, mission id, localisation key, changed file, and skipped or simplified item.
