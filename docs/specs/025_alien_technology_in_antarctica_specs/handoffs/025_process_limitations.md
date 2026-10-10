# Process limitations

## Tool routes

- The HOI4 MCP event inspect, script validate, GUI render and probability routes did not return usable results during the October 2026 passes, so event flow, helper scripts and weighted logic were reviewed from source.
- Source tests under `.tools/test_event025_*.py` execute the production helpers with stubbed engine commands. They do not prove native scheduling, event delivery, rendering, multiplayer privacy or save and reload.
- The agent never launches Hearts of Iron IV. In-game validation belongs to the user.

## What was checked from source

- Every localisation key referenced by the Event 025 events, decisions and ideas resolves, and no report or news description carries colour codes.
- The seizure restitution layer, the shared rival-agent cooldown, the Forerunner Craft chain and the catalog row were reviewed after the move of the Alien Spacecraft recovery into this event.

## Open

- Live validation of the race, the five evolutions, custody transfer and seizure restitution.
- Probability comparison of the reward arbitration and the AI expedition weights once the analyzer routes respond.
