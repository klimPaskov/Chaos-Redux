---
name: chaos-redux-events
description: Use when implementing or updating Chaos Redux events.
---

# Chaos Redux Events

Use this skill for any Chaos Redux event work, including:

- adding or updating `chaosx.nr<ID>.*` event chains
- wiring event log, event details, evolutions, and world-end branches
- maintaining `docs/events/` event documentation
- updating spreadsheet or event presentation decks

## Event implementation workflow

### 1. Pick and classify the event

- Entry events keep the format `chaosx.nr<ID>.1`.
- Keep related subevents in the same namespace.
- Confirm whether the event belongs in:
  - `global.major_events`
  - `global.repeatable_events`
  - `global.fire_once_events`

### 2. Wire the gameplay files

Main files to check:

- `events/chaosx_events.txt`
- `common/on_actions/chaosx_on_actions_system.txt`
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/chaosx_event_names_l_english.yml`

Minimum integration:

1. Add or update the event script in `events/chaosx_events.txt`.
2. Register the event in `initialize_event_categories`.
3. Wire automatic firing if it is an auto event.
4. Add event-name localisation.
5. Update the scripted localisation name mappings.
6. Update actor mapping if the event log row should show a flag.
7. Update the event details window content if the event appears in the Events Log.

If you have to add new plumbing to make those steps possible, stop and check whether that plumbing can be generic for future events as well.

### 3. Evolutions

If the event has stages, mutations, branches, or escalation milestones:

- log them through `record_events_log_evolution_entry`
- set the evolution temp variables before logging
- set an actor event target if the evolution is tied to a specific country
- update evolution localisation in the event-log localisation files
- if the user-facing event details window should preview all stages, keep the preview list aligned too

### 4. Handle world-end branches cleanly

If the event can end the campaign or trigger a super event:

- guard it with `NOT = { has_global_flag = world_end }`
- set `world_end`
- set the specific scenario flag
- set the matching `super_event_visible` slot
- update super-event scripted localisation and image mapping
- update event localisation in the same change

### 5. Keep special countries excluded

Chaos Redux has non-standard system countries such as zombies and aliens.

- Do not let civilian, ideology, migration, panic, or similar normal-country logic hit them unless that is explicitly intended.
- Re-check scripted triggers and shared effects when the event touches broad systems.

## Documentation rules

Event-specific documentation belongs in `docs/events/`.

Write for maintainers, but keep the structure practical:

1. What the event is.
2. Entry event and subevents.
3. Trigger flow.
4. Main gameplay effects.
5. AI behavior if relevant.
6. Evolutions and escalation flow if relevant.
7. World-end and super-event integration if relevant.
9. Asset wiring and sprite expectations if relevant.
10. Open tuning notes or future extension ideas.

### Docs and gameplay must stay aligned

When mechanics change, update the matching event doc in the same change.

Do not leave the doc describing old triggers, old stages, old cooldowns, or removed mechanics.

## Event presentation workflow

Use this workflow when the user asks for event slides, a showcase deck, or an event presentation.

### Required tools and order

1. Use `pptx` for the deck.
2. Use `theme-factory` for the theme.
3. Use `canvas-design` for custom art and slide visuals.
4. If the deck includes formulas, ratios, or gameplay calculations that should be shown clearly, use the LaTeX MCP server to render them beautifully.

### Presentation standard

The event deck is not allowed to look generic.

The visual standard should feel close to Chaos Redux thumbnail art:

- inspect `thumbnail.png`
- inspect `thumbnail_2.png`
- inspect `thumbnail_3.png`

Target look:

- minimalistic
- stark
- propaganda-poster energy
- 1984-inspired restraint
- strong contrast
- deliberate negative space
- bold composition
- no generic corporate deck styling

### Slide structure

Each event needs at least one slide.

Add more slides when the event has:

- evolutions
- world-end branches
- special subevents
- mechanics that would overcrowd one slide

### Visual quality rules

This matters a lot.

- Every slide must have an original visual built for that event.
- Do not reuse one generic illustration across the deck.
- The visual should look like real effort went into it.
- Each slide should feel distinct, not like a repeated template with swapped text.
- If the event has evolutions, the visual language should evolve with it.
- If the event has a world-end branch, that branch should get its own heavier, more terminal visual treatment.

### Recommended deck layout

If the user does not provide a path, prefer:

- `docs/presentations/chaos_redux_events.pptx`

Store generated art near the deck, for example:

- `docs/presentations/assets/`

## Event catalog spreadsheet

Maintain the gameplay-facing event table in:

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Audience:

- people who do not know the script
- people who want to understand what an event does in play

Write casually and focus on gameplay, not implementation details.

## Final event checklist

Before closing the task, verify:

1. Event script is updated.
2. Category registration is updated.
3. Auto-firing is updated if needed.
4. Localisation and scripted localisation mappings are updated.
5. Event details window content is updated.
6. Evolution logging is updated if relevant.
7. World-end and super-event wiring is updated if relevant.
8. `docs/events/` is updated.
9. The event spreadsheet is updated.
10. The presentation material is updated.
