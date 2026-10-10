# Asset prompt

Produce the Event 036 visual package listed in [14](../14_asset_requirements.md), following [the event-assets skill](../../../../.claude/skills/chaos-redux-event-assets/SKILL.md) and the image-generation route in `CLAUDE.md`.

Routing:

- `chaosx_generated_event_art` for the report image and the category picture
- `chaosx_icon_artist` for the category icon, the twelve decision and mission icons, the four idea icons, and the seven achievement families

Each subagent receives a self-contained prompt with the inventory rows it owns, the visual direction and palette from [14](../14_asset_requirements.md), the inspected consumer dimensions, and the output and handoff paths.

Before production, confirm that each row still has a live consumer in the implemented decisions, missions, and ideas, and drop any row that does not.
The parent wires every asset and clears the temporary workspace under the skill's rules.
