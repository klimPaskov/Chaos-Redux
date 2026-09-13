# Event 050 localisation audit prompt

Audit and patch Event 50 localisation after gameplay behavior is final.

Read `AGENTS.md`, `chaos-redux-events`, the Event 50 presentation spec, every implemented event, decision, mission, idea, scripted localisation, Event Details entry, history entry, evolution entry, achievement, and asset consumer.

## Required coverage

Check:

- event name and debug mapping
- target opening report
- core participant choices
- neutral and intermediary events
- threshold and review reports
- resolution reports
- decision category
- Embargo Pressure stage, trend, threshold, and cause text
- all responses and missions
- custom trigger tooltips
- dynamic countries, states, resources, routes, and coalition actors
- national spirit or modifier text
- Event Details and evolution previews
- Event Logs history and evolution surfaces
- achievement titles and descriptions
- asset and icon tooltips where visible
- documentation and workbook mirror wording

## Writing requirements

Write in-world text grounded in halted shipments, shortages, ports, factories, rationing, routes, commercial interests, and political choices.

Do not expose raw variables, unsupported bilateral trade percentages, hidden dependence scores, future evolution conditions, implementation history, process notes, achievement solutions, or secret accusations as fact.

Keep one consistent name and colour treatment for Embargo Pressure. Explain what changes it, what the next threshold means, and which action responds.

Use concise custom tooltips for long triggers. Name actual states, regions, ports, resources, and countries where the player must act.

Avoid em dashes, semicolons in sentences, dialectical contrast formulas, staccato filler, generic crisis slogans, fake administrative mystery, and reward-list prose.

Humor can target coalition hypocrisy, secret trade, and commercial evasions. It must not mock civilian deprivation or famine.

## Technical checks

- English localisation uses UTF-8 with BOM.
- Keys use the current project format without `:0`.
- Scripted localisation has neutral fallback branches.
- No country inherits another country's wording.
- Dynamic values have correct formatting and no unwanted decimals.
- Costs use matching texticons and remain within the four-cost cap.
- Event Details wording matches the workbook fields after export.

## Handoff

List every changed key, file, dynamic selector, fallback, and player-facing mismatch corrected. Report any behavior that cannot be described accurately because implementation remains incomplete.
