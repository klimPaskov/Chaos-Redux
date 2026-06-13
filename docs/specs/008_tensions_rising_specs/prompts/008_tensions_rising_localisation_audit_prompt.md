# Localisation Audit Prompt: Event 008 Tensions Rising

Audit or patch localisation for Event 008 `Tensions Rising` after implementation.

Read:

- `AGENTS.md`
- `chaos-redux-events`
- Event 008 specs under `docs/specs/008_tensions_rising_specs/`
- `specs/008_tensions_rising_event_log_and_localisation.md`
- implemented event, scripted localisation, event log, super-event, and GUI files relevant to Event 8

Audit for:

- missing event title/description/option keys
- missing event-name mapping
- missing debug-name mapping
- missing event-detail and evolution-detail keys
- delayed follow-up keys
- timed opinion modifier localisation
- Stage IV super-event keys if implemented
- raw trigger text or hidden mechanics exposed too directly
- spreadsheet-facing wording drift
- UTF-8 BOM and duplicate-key issues if editing localisation files

Text rules:

- The event should sound like diplomacy, pressure, rumours, offices, cables, markets, and staff rooms.
- Do not write player-facing text as update history.
- Do not reveal hidden exact pair-selection math or timer-pulse values in ordinary popups.
- Make the final-stage super-event non-terminal in wording.

Output required:

- missing key list
- duplicate key list
- scripted localisation issue list
- cross-surface mismatch notes
- changed keys if patched
- handoff under `docs/plans/008_tensions_rising_plans/subagent_handoffs/` if files are edited
