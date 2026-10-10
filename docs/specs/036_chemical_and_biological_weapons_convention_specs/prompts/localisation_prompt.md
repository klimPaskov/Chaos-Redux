# Localisation prompt

Write the Event 036 localisation after gameplay identifiers exist, using the direction and coverage list in [11](../11_event_chain_reactions_and_localisation_direction.md) and the writing rules in [the events skill](../../../../.claude/skills/chaos-redux-events/SKILL.md#event-writing-and-player-facing-text).

Event-specific points to verify:

- option tooltips show visible consequences, including the Condemnation tier change from opening normalization, and never multipliers
- the header's permission line, Standing, ratification count, and project stage come from scripted localisation with a neutral fallback
- program completion says participants can begin the project, never that a weapon was delivered
- no text claims a source event happened, names an unselected project, or reveals another country's covert program
- Event Details and the workbook fields use the same premise and evolution wording

Run `chaosx_localisation_auditor` after the first complete pass and list every changed key in the handoff.
