# Manual Improvement-Loop Review

## Review method

The supplied improvement-loop and event-planning standards were applied manually because the custom planner could not be spawned.

The review asked whether the package has a playable promise, pressure, choices, failure, AI, visual feedback, consequences, country identity, and a stopping point.

## Gaps found and resolved during the pass

### Gas masks risked becoming only a new stockpile

Resolution:

- added military and civilian allocation
- added filter exhaustion
- added protective posture penalties
- added state distribution and replacement
- added historical starting profiles
- added humanitarian export and occupied-population choices

### Army HQ integration risked being cosmetic

Resolution:

- assigned unique abilities to companies
- added order scope, command-power scaling, equipment requirements, preparation, active duration, and cooldown
- moved the strongest effects out of doctrine passives

### Agent variety risked creating duplicated units

Resolution:

- introduced role-based delivery units and payload profiles
- kept individual agents only where toxic profile, project, countermeasure, or national identity differs

### Chemical air bombs risked preserving an unreliable approximation

Resolution:

- explicit reliable operation and raid path is mandatory
- continuous mission estimation is conditional and requires approval if no verified hook exists

### Nerve suppression risked becoming a free garrison bonus

Resolution:

- made it a targeted operation
- added payload, deaths, contamination, trauma, evidence, Condemnation, and cooldown
- kept genocide systems separate

### Biological warfare risked becoming a copy of chemical contamination

Resolution:

- added incubation, hidden contamination, agent profiles, detection, spread, containment, accidents, facilities, and attribution

### Consequence systems risked double counting

Resolution:

- one action record owns deaths, contamination, evidence, and base Condemnation
- Air Cleanliness updates by state class changes
- atrocity and coverup buckets add context rather than a second full score

### Country differentiation risked relying on invented history

Resolution:

- used gameplay program profiles
- required source verification for final historical names and firms
- marked stockpile values as gameplay bands with confidence

### Implementation framing risked becoming mechanic simplification

Resolution:

- kept the original specific chemical and biological wording across every numbered spec and matrix
- added a narrow fictional-game scope file for the implementation agent
- allowed direct public-facing terms when they improve clarity
- prohibited real-world procedural guidance without changing game mechanics
- made subject-based omission, merging, weakening, or generic replacement a completion defect

## Anti-bloat decision

Further broad expansion is not recommended before implementation. The package already contains:

- four doctrine tracks
- four milestones
- twelve doctrine-only and supporting technologies
- six HQ companies
- seven major HQ abilities including a capstone
- ten regimental support roles
- two possible line battalions
- chemical and biological delivery families
- civilian protection
- suppression
- diplomacy
- designers
- AI
- assets
- achievements

Adding more agents, more duplicate support companies, a second global meter, or a separate event chain for every operation would add maintenance burden without improving the core loop.

## Recommended remaining design decisions

The implementation environment must decide:

1. Whether current 1.19 exposes reliable chemical-module mission activity.
2. Whether Hazard Pioneers need a line battalion or remain regimental support only.
3. Whether medical countermeasures use a new equipment archetype or existing support and hospital capacity.
4. Whether tabun is a complete field agent or a precursor technology.
5. Whether the CBRN interface is a custom scripted GUI or a rich decision-category header.
6. Which existing country MIOs and designers can be reused.

These are engine and source decisions, not missing gameplay design.

## Closure recommendation

The planning loop can close after the six implementation decisions above are recorded. Broad expansion should stop. The next work is implementation, source verification, asset production, and balance testing.
