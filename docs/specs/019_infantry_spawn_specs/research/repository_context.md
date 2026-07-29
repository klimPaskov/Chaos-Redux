# Event 19 Repository Context

## Inspection date

July 10, 2026.

> **Historical inspection snapshot:** The implementation descriptions below
> record the pre-rework public repository and are not live status. Use the
> package `README.md` source-of-truth map, `docs/events/019_infantry_spawn/overview.md`,
> and `review/blockers_and_uncertainty.md` for current implementation and
> closure state.

## Current public Event 19 implementation

The current public repository file is:

- [events/019_infrantry_spawn.txt](https://github.com/klimPaskov/Chaos-Redux/blob/master/events/019_infrantry_spawn.txt)

The filename currently uses `infrantry` rather than `infantry`. The existing script is a small hidden global event followed by one report event. It creates one fixed template containing eight infantry battalions, loops through countries and fully controlled non-impassable states, and creates one unit in each valid state. It does not contain the decision, evolution, claimant, AI, derivative-country, or documentation layers planned in this package.

The stable event ID and namespace should be preserved. A filename correction or migration should be decided during implementation after checking all current references.

## Event documentation

The public `docs/events/` tree did not show a canonical Event 19 document during inspection:

- [docs/events](https://github.com/klimPaskov/Chaos-Redux/tree/master/docs/events)

Implementation should create `docs/events/019_infantry_spawn/overview.md` and keep it aligned with final behavior.

## Shared special-country classification

The public shared trigger file includes central classification for special Chaos countries and actually nonhuman countries:

- [common/scripted_triggers/chaosx_dynamic_triggers.txt](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/scripted_triggers/chaosx_dynamic_triggers.txt)

Event 19 derivative countries should use those shared classifications rather than create duplicate event-local classifiers.

## Zombie parent isolation

The public zombie trigger package uses parent identity and dynamic-country logic that must be audited before derivative zombie states are implemented:

- [common/scripted_triggers/002_zombie_outbreak_triggers.txt](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/scripted_triggers/002_zombie_outbreak_triggers.txt)

Public inspection showed parent zombie identification patterns that include the parent tag, original-tag checks, and zombie outbreak flags. Event 19 derivative countries therefore need distinct origin handling and explicit exclusion from parent counts, leagues, progression, and super-events.

## Death parent isolation

The public Death trigger package contains extensive actor, wasteland, state-consumption, and progression logic:

- [common/scripted_triggers/010_death_triggers.txt](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/scripted_triggers/010_death_triggers.txt)

Event 19 ghost derivatives must not use the Death tag, original-tag identity, or parent country flag. Their slow population and wasteland effects need separate Event 19 origin checks and must not enter parent consumed-state or soul-style counts.

## Likely implementation surfaces

The full local repository must determine exact final paths. The likely surfaces are:

- Event 19 event file and follow-up event family
- Event 19 scripted effects and scripted triggers
- event-specific script constants
- event-owned decisions and category
- event-owned scripted GUI and interface files
- event-owned ideas and dynamic modifiers
- character or leader creation helpers
- dynamic country and cosmetic identity helpers
- shared special and nonhuman classifiers
- parent zombie, Death, and golem exclusion checks
- Event Log effects, scripted localisation, and GUI selectors
- triggerable scenario registry, effects, triggers, GUI, and localisation
- AI strategy and decision behavior
- achievements
- GFX and asset manifests
- event and system docs
- event catalog workbook

## Required local verification before implementation

This planning environment did not include the full local Chaos Redux repository, offline Paradox wiki snapshot, or installed vanilla documentation. The implementation agent must inspect:

- `AGENTS.md`
- all relevant repo skills
- local current Event 19 references
- local dynamic unit and country helpers
- offline wiki pages for data structures, effects, triggers, scopes, events, decisions, AI, countries, divisions, equipment, localisation, GUI, scripted GUI, and graphical assets
- vanilla documentation and at least one relevant vanilla precedent for each engine surface
- actual zombie, ghost, golem, helicopter, flamethrower, camel, bicycle, amphibious, and support-company identifiers
- current dynamic civil-war and dynamic-country patterns
- existing Event Log and triggerable scenario helpers

No exact script identifier in the planning package should override verified local evidence.
