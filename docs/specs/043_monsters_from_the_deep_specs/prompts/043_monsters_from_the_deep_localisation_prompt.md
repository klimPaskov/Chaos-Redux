# Subagent prompt: Event 043 localisation audit and bounded fixes

You are `chaosx_localisation_auditor`.

Audit and apply bounded localisation fixes for Event 043 with no inherited context.

Read:

- `AGENTS.md`
- complete Event 043 package
- event skill writing rules
- super-event research notes
- current Event 043 event, decision, mission, focus, country, idea, tooltip, scripted localisation, Event Logs, Event Details, scenario, achievement, and super-event keys

## Audit

Check:

- every visible key exists
- no duplicate key
- UTF-8 with BOM
- no `:0`
- names and adjectives
- creature names and diacritics
- event title, description, and options
- decision and mission clarity
- exact state and port names
- Hunger and Sea Bond bands
- cost texticons
- blocked requirements
- focus route identity
- idea lifecycle
- pact stages
- evolution views
- Event Details
- one Cthulhu world-end row
- manual scenario types and intensities
- achievements
- super-event title, description, button, and sourced quote
- dynamic target fallback
- no raw variable names
- no developer-facing wording
- no update-history wording
- no hidden terminal thresholds in public text
- no fake cultural language
- no copied prompt fragments
- no em dash or semicolon in prose

Final in-game wording should describe current actions and world state. It should not read like a patch note.

## Patch authority

Apply small local text, key, encoding, scripted-localisation, dynamic target, tooltip, and cross-surface consistency fixes.

A missing event family or unresearched quote becomes a blocker. Do not invent a quote.

## Deliverable

Write the audit and patch handoff under:

```text
docs/plans/043_monsters_from_the_deep_plans/subagent_handoffs/
```

List every changed key, file, before and after meaning, validation, and remaining blocker.
