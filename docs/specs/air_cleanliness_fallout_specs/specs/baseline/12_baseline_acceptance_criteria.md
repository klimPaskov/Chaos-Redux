# Air Cleanliness and Fallout World-End Source Spec, Part 12 Documentation, Catalog, and Acceptance Criteria

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

## Documentation surfaces

| Surface | Required update |
| --- | --- |
| Air Cleanliness mechanic doc | Replace simple threshold future plans with winter phase mapmode, state effects, treaty operations, and Fallout trigger rules. |
| Fallout world-end doc | New canonical source doc for black-screen transition and post-Fallout overhaul. |
| Triggerable scenarios doc | Add the manual Fallout scenario using the next free live id, with every-province thermonuclear launch and seven-day delay. |
| Chaos mechanics guide | Update Air Cleanliness, world-end rules, Deaths integration, and triggerable scenario list. |
| Event catalog spreadsheet | Add Fallout scenario row and align world-end notes for air contamination. |
| Asset manifests | Add mapmode, UI, icon, flag, portrait, report, news, and animated asset packages. |
| Music and super-event docs | Mark Fallout as not a normal super-event. If blackout audio is later added, document outside super-event pattern. |
| Subagent handoffs | Record every subagent patch or blocked report. |

## Spreadsheet direction

The spreadsheet should not become a mechanics dump. The Fallout scenario details should say that the scenario destroys the map with a global thermonuclear strike and then rewrites the campaign into a post-Fallout survival world after a short delay. It should not list hidden mutant branches or exact state classification formulas.

## Event details direction

Event Details should describe the premise, not raw effects. For Air Cleanliness, describe atmospheric contamination and visible winter spread. For Fallout, describe the world transition and survival premise. Do not expose secret route requirements.

## Catalog additions

| Catalog | Row direction |
| --- | --- |
| Scenario catalog | Add the manual Fallout scenario with the verified live id, type `World-End Scenario`, and evidence-based implementation status. |
| Event catalog | Fallout world-end note for Air Cleanliness and any event that can bridge to Fallout. |
| Cluster catalog | No cluster required unless later implementation creates a Fallout precursor cluster. |

## Implementation acceptance criteria

### Air Cleanliness

- New mapmode exists and is state-based.
- Winter phase appears on mapmode and in state tooltip.
- Winter phases create actual state effects.
- State population loss uses the Deaths system.
- Buildings and infrastructure can be damaged by severe phases.
- State categories can degrade after sustained severe phases.
- Treaty decisions interact with map states.
- AI uses air responses and does not ignore severe winter.
- Flavour events have real gameplay effects.

### Fallout transition

- Fallout can trigger above 100 percent contamination, from scripted terminal events, and from manual scenario.
- No 1000-percent contamination or 1000-Chaos requirement is used. Higher contamination may change urgency and severity.
- Fallout does not use normal super-event presentation.
- Black screen overlay blocks UI and shows timed text beats.
- Heavy world rewrite runs during blackout.
- Player continuation is handled when old tag dies or fragments.

### Manual scenario

- The manual Fallout scenario is registered with the next free live id and is directly launchable.
- Every valid province receives thermonuclear strike effects.
- There is a one-week delay before Fallout rewrite.
- If province-level strike is blocked, implementation reports blocker and does not silently downgrade.

### Post-Fallout overhaul

- State classes replace normal map identity.
- Old factions, normal trade, and incompatible events are disabled or transformed.
- Survival resources exist and are visible.
- Countries receive Fallout archetypes and non-generic focus content.
- Regional successors and mutant polities can appear with cosmetic identities.
- Decisions, missions, AI, assets, achievements, and docs are aligned.
- Gameplay remains interesting for ten more years.

## Required validation and audits

| Audit | Must check |
| --- | --- |
| Scripted system architect | Helpers, constants, state class assignment, cleanup, selected-state logic. |
| Decision mission auditor | Costs, tooltips, AI, clutter, exploit loops, cleanup. |
| Focus tree auditor | Route coverage, branch depth, icons, rewards, AI. |
| Country package auditor | Tags, cosmetics, leaders, flags, starting states, armies, AI, focus loading. |
| Localisation auditor | Missing keys, bad copied spec text, dynamic value formatting, blackout text quality. |
| Documentation curator | Source-of-truth map, stale plans, docs consistency. |
| Spreadsheet worker | Catalog rows after final localisation exists. |
| Completion auditor | Spec versus implementation and missing depth. |

## Known blockers that must not be hidden

- Local offline Paradox wiki and vanilla HOI4 docs were not present in this planning sandbox.
- Province-level thermonuclear sweep may require engine verification.
- Custom subagents were not spawnable here.
- This package is a planning source and does not implement game files.

## Final quality bar

The feature is incomplete if it only adds a mapmode, only adds a black screen, only damages states, or only creates a few generic countries. The requested design is a total overhaul. Completion requires every major system to reinforce the new world: air, map, population, buildings, state categories, governments, countries, focus trees, decisions, AI, assets, achievements, docs, and catalog rows.
