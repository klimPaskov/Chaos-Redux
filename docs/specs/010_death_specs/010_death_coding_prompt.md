# Event 010 Death - Coding Prompt

## Goal

Implement Event 010 Death from `docs/specs/010_death_specs/`. Death replaces obsolete Event 010 `Spirit of War/Peace` completely while preserving ID `10` and root format `chaosx.nr10.1`.

## Required Pre-Implementation Reads

Before editing, read:

- AGENTS.md
- all core offline Paradox wiki pages required by AGENTS
- relevant vanilla docs in `~/projects/Hearts of Iron IV/documentation`
- vanilla and local examples for events, decisions, country creation, focus trees, dynamic modifiers, super-events, and state effects
- this entire spec package
- accepted addendum at `docs/plans/010_death_plans/010_death_deep_expansion_addendum.md`

Use the required skills:

- `chaos-redux-events`
- `chaos-redux-event-planning`
- `chaos-redux-event-assets`
- `chaos-redux-super-events`
- `chaos-redux-frame-animation` if animated assets are produced
- `hoi4-decisions-missions`
- `hoi4-focus-trees`
- `hoi4-mtth`
- `chaos-redux-subagents`
- `xlsx` when updating the spreadsheet after implementation facts are final

## Core Implementation Steps

1. Replace obsolete Event 010 War/Peace surfaces.
2. Add `DTH` Death country package, Zol, flags, country color, AI, and classifications.
3. Add `common/script_constants/010_death_constants.txt`.
4. Add `events/010_death.txt` with root `chaosx.nr10.1`.
5. Add `common/scripted_effects/010_death_effects.txt` and `common/scripted_triggers/010_death_triggers.txt`.
6. Add Death dynamic state modifiers.
7. Add Death focus tree and load it when Death spawns.
8. Add decisions/missions for Missing Islands, Black Shore Containment, Living Compact, Forbidden Files, and War Logistics.
9. Wire state withering, state consumption, civilian death accounting, industry deletion, Death coring, and recovery cleanup.
10. Wire ghost division stages and spawn caps.
11. Wire reveal, world threat, world-end, defeat, and world-consumed super-events.
12. Wire event log, event details, evolutions, triggerable scenario, achievements, and spreadsheet.
13. Register assets and placeholder sprites where final art is not ready.
14. Run focused audits and fix findings before completion.

## Touched Existing Surfaces

Update or remove references in:

- `events/010_war_or_peace_symbol.txt`
- `localisation/english/010_war_or_peace_symbol_l_english.yml`
- `events/_chaosx_news.txt`
- `common/ideas/chaosx_ideas.txt`
- `localisation/english/chaosx_ideas_l_english.yml`
- `interface/chaosx_pictures.gfx`
- `common/scripted_effects/chaosx_logic_effects.txt`
- `localisation/english/chaosx_event_names_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- event details/evolutions localisation and effects
- world-threat scripted effects/triggers
- special-country scripted triggers and docs
- super-event scripted GUI, scripted localisation, `.gfx`, music/audio docs
- custom achievements system
- triggerable scenarios system
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Do not delete `GFX_report_event_war_or_peace` while Event 004 still references it.

## Script Rules

- Tabs for Clausewitz script indentation.
- No `<=` or `>=`.
- Use script constants and MTTH variables for tuning.
- No whole-world daily/weekly on_actions without explicit approval.
- No silent substitute origin if no valid island exists.
- No hardcoded costs, durations, thresholds, weights, or unit counts.
- Use flags for booleans and variables for tunable quantities.
- Use scripted effects/triggers for repeated logic.
- Use existing dynamic helpers where they fit; document new dynamic helpers in `chaosx_dynamic_effects.md`.
- Do not use `modify_state_population_by_percent` for Death's main population deletion because its docs say it needs deaths-system integration.
- Register civilian deaths through Chaos Meter.
- If an effect field rejects constants, assign the constant to a variable first.

## Mandatory Subagent Audits Before Completion

Use:

- `chaosx_country_package_auditor`
- `chaosx_focus_tree_auditor`
- `chaosx_decision_mission_auditor`
- `chaosx_localisation_auditor`
- `chaosx_event_completion_auditor`

Use asset/audio/text subagents as needed for generated assets and super-event audio.

## Completion Standard

Do not claim Event 010 complete unless:

- all requested mechanics are implemented
- no old War/Peace content remains incorrectly wired to Event 010
- Death can spawn, remain hidden, spread, reveal, be contained, escalate, be defeated, trigger world-end, and consume the world through scripted paths
- localisation, tooltips, UI assets, decisions, focus tree, event log, super-events, achievements, docs, and spreadsheet are aligned
- no fallback or simplification was used without explicit approval
