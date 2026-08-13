# Decision and mission prompt for Event 013 Natural Disasters

> Implementation disposition: executed for staged warnings, rescue, stabilization, reconstruction, chain prevention, foreign relief, caps, partial outcomes, AI, and cleanup. Future changes must start from the live decision file and its audit handoff.

Use `chaos-redux-decisions-missions` and the Event 013 spec package. Design and implement decisions as family-specific recovery work, not political power stores.

## Main category

Create or plan a Natural Disaster Aftermath category that appears reliably after serious impacts. It must show active disaster cards and notify affected countries when opened or refreshed.

## Decision families

Implement preparation and recovery decisions for search and rescue, evacuation, rail clearance, port closure, medical corridor, food corridor, firebreaks, ash cleanup, winter fuel line, water trains, observatory watch, and reconstruction.

Use concrete costs such as manpower, support equipment, trucks, trains, convoys, fuel, army XP, navy XP, air XP, civilian capacity, and stability strain. Political power should only appear where it fits public administration.

## Mission families

Timed missions should cover relief railheads, port status, evacuation corridors, valley roads, water distribution, damaged airfields, and structure inspection. Missions should have success, failure, and partial success where useful.

## UI and localisation

Long requirements need custom tooltips and dynamic named places. Cost text should be icon-first and readable. Event Details and decision category text should not expose hidden formulas.

## AI

AI must take preparation and recovery actions when they matter. It should prioritize capital states, dense states, supply hubs, ports, airfields, and war fronts. It should avoid invalid or impossible actions.

## Cleanup

Clear stale cards, decisions, missions, flags, variables, and event targets after recovery, country invalidation, tag switch, annexation, or season cleanup.
