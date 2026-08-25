# Event 006 Evolution localisation merge — 2026-08-25

## Scope

This source-layout pass folds the Evolution stage strings and the five rotating Evolution incident strings into `localisation/english/006_independence_wave_evolution_l_english.yml`.

The receiver keeps one `l_english` root and separates the stage and incident sections with comments. Package-local, super-event, and scenario localisation remain separate because their ownership and loading boundaries differ.

## Preservation evidence

The receiver retains all 44 disjoint key/value pairs from the two source files, including `independence_wave.evolution.type`, the five stage title/body pairs, `independence_wave.evolution.summary`, the incident category keys, the five incident decision labels/descriptions, and the fifteen `chaosx.nr6.360` through `chaosx.nr6.364` event strings. A key/value comparison found no missing or changed entries.

The receiver retains the UTF-8 BOM (`EF BB BF`) and a single `l_english:` root. No event ID, decision ID, category ID, scripted-localisation name, or player-facing wording changed.

## Boundary

This is a source-layout consolidation only. It does not change Evolution timing, incident visibility, decision costs, event reachability, or the Event 006 32/29/40/161 boundary. It does not claim live localisation rendering or in-game acceptance evidence.

## Changed paths

- `localisation/english/006_independence_wave_evolution_l_english.yml`
- removed `localisation/english/006_independence_wave_evolution_incidents_l_english.yml`
- removed `localisation/english/006_independence_wave_evolutions_l_english.yml`
