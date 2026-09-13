# Localisation implementation prompt

Write and audit the full player-facing localisation for Event 036 after gameplay identifiers and final mechanics exist.

Read `AGENTS.md`, `chaos-redux-events`, `11_event_chain_reactions_and_localisation_direction.md`, every implemented event, decision, mission, idea, scripted localisation selector, Event Details row, evolution row, project provider display token, achievement, and workbook-facing field.

Use `chaosx_localisation_auditor` after the first complete pass.

## Coverage

Write final text for:

- canonical event and national opening responses
- news and report events
- all five postures
- Convention Standing
- every agenda and treaty
- reservations and first-use policies
- doctrine integration states
- decisions, missions, costs, requirements, success, and failure
- inspections, guarantees, exposure, accession, withdrawal, and collapse
- project selection, milestones, pause, dormancy, completion, and cancellation
- Event History, Event Details, and evolution selectors
- achievements
- asset-facing labels where required

## Writing rules

Write in-world text from the viewpoint of governments, diplomats, military planners, scientists, doctors, inspectors, victims, and opponents.

Use concrete weapons, facilities, obligations, evidence, countries, sponsors, and deadlines when the game state supports them.

Keep uncertainty where evidence is hidden or incomplete.

Do not expose raw multipliers, AI weights, candidate pools, internal project points, provider contracts, source-event bypass rules, hidden foreign programs, or future outcomes.

Do not use developer wording, update history, rework history, debug language, em dashes, semicolons, staccato fragments, generic crisis filler, or copied prompt instructions.

Options should express the government’s stance and tone.

They should not read like reward lists.

## Dynamic text

Use scripted localisation for current country, sponsor, victim, agenda, posture, standing, treaty, reservation, selected project, contribution status, and deadlines.

Provide a neutral fallback for every selector.

No country-specific branch may leak another country’s wording.

## Consistency

Event Details and workbook fields must match the final in-game premise and evolution wording.

Decision cost text must match actual costs.

Blocked tooltips must name exact missing requirements.

Project completion text must say that the research route or prerequisite is open, not that the completed weapon was granted.

Run duplicate-key, missing-key, dynamic-selector, encoding, raw-key, tone, and cross-surface consistency audits.

List every changed key in the handoff.
