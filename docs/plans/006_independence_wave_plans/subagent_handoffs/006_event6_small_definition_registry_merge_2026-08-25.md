# Event 006 small definition-registry merge — 2026-08-25

## Scope

This source-layout pass removes three small Event 006 definition fragments whose top-level identifiers are disjoint from the existing shared registries. The two country-origin lifecycle effects now live in the main Event 006 scripted-effect registry. The seven evolution predicates and eight opening-force predicates now live in the main Event 006 scripted-trigger registry.

No event, decision, mission, on-action, package adapter, reservation gate, admission count, force profile, evolution flag, or localisation entry changed.

## Preservation evidence

The two former country-registry effect definitions, seven former evolution-trigger definitions, and eight former force-trigger definitions were compared against the receiver files after line-ending normalization. All seventeen identifiers and their executable bodies are preserved with no missing or changed definitions. The receiver registries have no duplicate top-level identifiers against the moved definitions.

## Changed paths

- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- removed `common/scripted_effects/006_independence_wave_country_registry_effects.txt`
- removed `common/scripted_triggers/006_independence_wave_evolution_triggers.txt`
- removed `common/scripted_triggers/006_independence_wave_force_triggers.txt`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`

## Validation boundary

This is a static source-layout consolidation only. The maintained Event 006 validators are the relevant source checks; no live game parser, event execution, save/load, package admission, or balance claim follows from this handoff.
