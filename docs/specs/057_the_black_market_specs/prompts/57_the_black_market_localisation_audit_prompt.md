# Event 57 Localisation Audit Prompt

Audit Event 57 player-facing and scripted localisation as `chaosx_localisation_auditor`.

Read:

- `docs/specs/057_the_black_market_specs/08_event_chain_logs_localisation_and_catalog_alignment.md`
- all Event 57 event, decision, mission, achievement, Event Details, evolution, scripted-localisation, and workbook-facing text
- current repository localisation rules

## Required tone

Use period clandestine logistics and government language. Focus on restricted cargo, depots, neutral freight, false paperwork, corrupt officials, captured stock, intelligence contacts, route risk, customs searches, and political exposure.

Remove modern online-market language, dark-web language, gangster caricature, central-mastermind lore, generic dramatic filler, raw script terms, tuning history, and implementation notes.

## Secrecy

Check every line for unauthorized knowledge.

- Outsiders cannot see the member list.
- Members know only direct contacts, routes, and proven counterparties.
- Offer provenance must match the receipt.
- A seizure exposes only the proven route, cargo, intermediary, or participant.
- Evolution text must not reveal every hidden capability.

## Category clarity

The category must show Market Credit, Exposure, and Network Reach clearly without a debug-style telemetry row.

Each value needs a concise cause, consequence, next threshold, and response. Do not use divider characters to simulate columns.

Offer text must state cargo, amount, Market Credit price, other visible costs, route family, risk class, delivery-time band, and the main blocked reason.

## Dynamic text

Audit all branches for:

- selected offer
- quantity
- route
- risk
- delivery time
- posture
- Reach stage
- Exposure band
- known country or state
- evidence target
- transaction outcome

Every selector needs a neutral default that cannot leak another country or raw key.

## Event and log alignment

Check:

- Event 57 name
- founder invitation
- first member report
- transaction reports
- outsider reports
- three evolutions
- main History row
- History details
- Evolution history rows
- Event Details catalog previews
- achievement text

History remains sanitized and actorless. Event Details does not show active members, routes, balances, inventory, or readiness formulas.

## Workbook-facing wording

Compare final in-game Event Details and evolution descriptions with the catalog text that the spreadsheet worker will use. Flag any mismatch before workbook update.

## Patch authority

Patch bounded localisation defects directly. List every changed key in the handoff. Do not redesign the mechanic or reveal hidden content to make a tooltip easier.

Write the handoff under:

`docs/plans/057_the_black_market_plans/subagent_handoffs/`
