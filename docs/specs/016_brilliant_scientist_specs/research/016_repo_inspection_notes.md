# Event 016 repository inspection notes

## Reverification, 2026-07-14

The Event 016 gameplay footprint remains the same placeholder baseline described below. The repository contains no implemented Directorate, persistent Warren Kruger character, staged project portfolio, temporal-debt system, Kruger State country package, Event 016 focus tree, Event 016 achievements, or wired Event 016 asset and super-event packages. The reconciled design must therefore be described as planned, never implemented.

## Current event script

The live event is currently a two-step placeholder.

- `chaosx.nr16.1` is hidden and triggered only.
- It chooses a random country from a pool restricted to majors or human-controlled countries.
- It fires `chaosx.nr16.2` after one day.
- The visible event has one option.
- That option adds the `brilliant_scientist` idea and fires a news event.

This structure does not support refusal, transfer, a persistent scientist character, special-project scientist use, a project portfolio, security, foreign reactions, evolutions, removal, rebellion, a new country, a focus tree, super-events, or a world-end branch.

## Current national spirit

`common/ideas/016_brilliant_scientist_ideas.txt` currently defines a country idea called `brilliant_scientist` with `research_speed_factor = 0.5`.

The rework must deliberately raise the opening anchor to the requested `+100%` research speed. The final system can stage, specialize, suppress, transfer, or transform the bonus after major events, but the initial accepted appointment must feel unmistakably stronger than the placeholder.

The idea should become part of a lifecycle rather than a permanent isolated modifier. Suggested lifecycle roles are:

1. Kruger's Appointment.
2. The Kruger Method.
3. National Scientific Dependence.
4. Controlled Directorate or Public Science Compact.
5. Sovereign Laboratory Network.
6. Former Host Scientific Vacuum after defection or rebellion.

These are working labels and are not final localisation.

## Current localisation

The existing text states an alien explanation too directly and uses generic wording. The rework should preserve uncertainty at first. Early observers can see knowledge, methods, equipment, or biological details that do not fit ordinary explanation, while the alien question stays unresolved until later evidence or a rare route.

Doctor Warren Kruger should be named consistently. The character voice should be precise, impatient, dry, and increasingly possessive. He should not read as a generic laughing mad scientist.

## Event registration

Event 16 is already registered in the fire-once event array. That classification is correct and should remain stable.

The repository's rework queue disables unfinished events by default. Event 16 should remain disabled in that queue until the complete rework, all player-facing surfaces, AI, assets, documentation, event-log integration, and catalog updates are ready.

## Scientist and special-project precedent

The repository already contains character definitions with `scientist` blocks, scientist traits, and field specializations. It also contains custom special-project specializations and project families for biowarfare, chemical warfare, cloning, and weaponized zombie work.

This makes a shared Doctor Warren Kruger scientist package plausible, but implementation must verify how one character can be exposed across every special-project field. The preferred player-facing result is one persistent character identity. If the engine requires field-specific entries, the implementation should create linked field instances that share Kruger's name, portrait stage, status, loyalty state, and removal lifecycle.

## Existing package precedent

The `007_fury_specs` package demonstrates the project's expected planning shape. It separates core event design, evolutions, focus-tree architecture, decisions, country packages, AI and balance matrices, prompts, research, and acceptance criteria. Event 16 follows that pattern while expanding the asset and animation handoffs because Kruger's portrait evolution is central to the user brief.

## Adjacent catalog concepts

The current event catalog contains several ideas that should connect to or be reconciled with Event 16.

| Catalog concept | Event 16 relationship |
| --- | --- |
| Soviet Nuclear Bombs | Kruger can accelerate, steal, counter, or corrupt nuclear research. |
| Alien technology in Antarctica | Exotic materials or alien-origin evidence can become project prerequisites or reveal hooks. |
| Doctrine research | Kruger can create unusual doctrine research incidents, but should not replace the separate event. |
| Asteroid incoming | Kruger can propose interception, mining, diversion, or exploitation projects. |
| Time Traveler | Temporal project results can create cross-event recognition, paradox, or rivalry. |
| Missiles | Guidance and exotic propulsion projects can strengthen missile systems. |
| Space race | Kruger can accelerate launch systems and later threaten orbital weaponization. |
| Mass Panic | Public exposure, cloning evidence, or monster escape can increase panic. |
| Gift from scientists | A research gift can be influenced by Kruger's reputation or assistants. |
| Research Failure | Kruger can prevent, exploit, or deliberately cause failures. |
| Tech sharing | Kruger can create a private network, reject participation, or dominate the group. |
| Research Investment | National investment can increase Kruger's capacity and dependence. |
| Teleportation Experiment | The event should become a direct cross-event hook rather than duplicating teleportation in isolation. |
| Army of Clones scenario | Clone research can seed or modify this triggerable scenario. |
| Crazy Scientist, unnumbered catalog idea | This substantially duplicates the final Event 16 fantasy and should be absorbed or marked superseded. |
| Super Soldiers, Bioweapon Race, Facilities, Special Project | These can become later connections, project branches, or supporting events without replacing the core Event 16 loop. |

## Non-negotiable implementation implication

The event is too broad for an event-file-only rework. A complete implementation will touch event registration state, event-log details and evolutions, characters, ideas, decisions, scripted effects, scripted triggers, constants, special projects, country setup, focus trees, AI, localisation, GUI, GFX, assets, super-events, achievements, event docs, and the event catalog workbook.
