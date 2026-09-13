# Localisation audit prompt for Event 58 Random Buildings

Use this prompt with `chaosx_localisation_auditor` after implementation text exists. Spawn with `fork_context=false`.

Read `AGENTS.md`, `chaos-redux-events`, the complete Event 58 specs, the Event 58 localisation and scripted-localisation files, Event Logs and Event Details source paths, achievement localisation, the authoritative in-game wording handed to the spreadsheet worker, and the relevant MCP event and GUI artifacts.

## Audit scope

Audit and patch only Event 58 text:

- root report title, description, and acknowledgement
- dynamic player-country result summary
- exhausted-state explanation
- Event Logs name and history detail
- Event Details premise
- Evolution I, II, and III names and preview text
- evolution history titles and bodies
- Chaos History source names
- achievement titles, descriptions, and requirements
- debug names and provider display-family labels that are player-facing
- Positive Economy cluster wording changed for member `58`

## Writing direction

Use concrete construction imagery and simple language. Describe what appeared and where. Keep the cause unknown without staged contrasts between witnesses and authorities.

The root option can use dry bewilderment, restrained sarcasm, or administrative resignation. Keep it short.

Do not expose:

- raw risk bands
- provider IDs
- random weights
- callback states
- debug skip reasons
- future unregistered buildings
- implementation history
- the stale `The Industrial Complex` concept

Dynamic summaries should show useful counts and a few notable states without becoming telemetry rows or a complete state list.

Follow the project prohibition on em dashes, semicolons in sentences, staccato fragments, dialectical hedging, staged contrast formulas, and generic dramatic filler.

## Technical checks

- verify all keys exist once
- preserve UTF-8 with BOM
- verify scripted localisation resolves the correct player, state, layer, and display family
- prevent raw keys or wrong-country summaries
- check report, Event Details, Event Logs, achievement, and workbook wording for contradictions
- use custom tooltips and hide raw long triggers
- inspect GUI render evidence for clipping, wrapping, and text crossing the report background
- preserve dynamic tokens and formatting codes

Return changed files and keys, prose issues fixed, dynamic text changes, MCP evidence, remaining blockers, and any source wording that the spreadsheet must mirror exactly.
