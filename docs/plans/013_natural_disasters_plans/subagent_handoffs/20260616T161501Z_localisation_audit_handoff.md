# Event 013 Localisation Audit Handoff

Audit surface:
- `localisation/english/013_natural_disasters_l_english.yml`
- `localisation/english/013_natural_disasters_event_names_l_english.yml`
- `localisation/english/013_natural_disasters_event_details_l_english.yml`
- shared scenario, achievement, super-event, Event 046, and GUI localisation surfaces touched by Event 013

Result:
- The localisation audit found missing or stale keys during the implementation pass and confirmed that the Event 013 English localisation file retained its UTF-8 BOM after edits.
- The main implementation added missing decision, mission, warning, event-log, achievement, scenario, Event 046 placeholder, and super-event localisation.
- After the first completion audit, the main implementation also updated the delayed-aftermath tooltip and added localisation for `natural_disaster_seal_border_camps_against_FROM` plus its concrete cost strings.

Follow-up status:
- Event 013 player-facing strings describe the live world state rather than update history.
- Static foreign-relief cost strings intentionally match the fixed Event 013 foreign-relief constants.
- A final localisation audit should re-check duplicate keys, BOM, and decision/event key coverage before completion.
