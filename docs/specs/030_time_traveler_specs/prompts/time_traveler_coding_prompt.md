# Event 030 Implementation Prompt

Implement Event 030, Time Traveler, from `docs/specs/030_time_traveler_specs/` as a complete Chaos Redux major event.

## Before editing

- Confirm that the parent or user has accepted the design, or the part being implemented, as the package [README](../README.md#status-and-acceptance) requires.
- Read the package README, the twelve specification parts, and the matrices for the surfaces in scope.
- Read `CLAUDE.md` and the skills it routes for events, decisions, focus trees, super-events, assets, portraits, 3D models, the improvement loop, and subagents under `.claude/skills/`.
- Read the current runtime: `events/030_time_traveler.txt`, `common/ideas/030_time_traveler_ideas.txt`, `common/scripted_effects/030_time_traveler_effects.txt`, the Event 016 bridge helpers, and the individual-crisis provider.
- Read the relevant offline wiki and installed vanilla documentation sections and one vanilla or Chaos Redux precedent per touched surface.

## Contract

The specification parts are the single source of requirements.
[Part 12](../specs/030_time_traveler_spec_part_12_acceptance_criteria.md) owns completion criteria and the legacy migration checklist.
Do not restate or reinterpret them here.

The design boundaries that most often go wrong are:

- three public values with three bands each, and Temporal Stability only as the Evolution V display of Divergence
- no fourth meter, no full Event 030 window, no cluster, no dinosaur country, and no unrestricted future technology
- one original traveler, one consultation mission at a time, and at most six visible actions per phase
- owner APIs for Deaths, migration, famine, camps, biological outbreaks, missiles, nuclear use, doctrine, technology, condemnation, Air Cleanliness, world threat, and individual-crisis targeting
- no recurring whole-world iteration without explicit user permission
- tuning values in script constants, one-shot Chaos milestones, and no double counting of generic sources

## Delivery

Route portraits, icons, art, flags, super-event text and audio, the drone model, and its sound through the project subagents listed in the [orchestration plan](subagent_orchestration_plan.md), each with a self-contained prompt.
Update registration, default enable state, runtime hooks, decisions, ideas, characters, AI, scripted effects and triggers, classifications, CXT registration for the drone family and the Closed Future package, event logs, evolutions, Event Details, the world-end and scenario registries, super-events, assets, localisation, docs, achievements, and the authoritative catalog XLSX.
Run `python .tools/export_event_catalog_csv.py` after the workbook update.

After each major tranche, run the improvement loop.
Before completion, run the audits listed in Part 12 and report every simplification and blocker.
