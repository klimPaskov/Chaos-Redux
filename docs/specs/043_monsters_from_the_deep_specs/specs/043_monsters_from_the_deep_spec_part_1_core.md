# Event 043: Monsters from the Deep

## Part 1: Core event design

## Catalog entry

- Event ID: `43`
- Event name: Monsters from the Deep
- Replaces: Massive Flood
- Type: Major
- Status: To Be Reworked
- Chaos level: `3`
- Cluster: none
- Severity field: not applicable outside a cluster
- Evolution I working label: The Rising Tide
- Evolution II working label: Every Sea Opens
- Public world-end working label: Cthulhu's Dominion
- Triggerable scenario proposal: `SCN-015`

Working labels in this specification describe roles and routes. They are not final localisation.

## Event promise

Several mythic sea monsters emerge in distant oceans during one coordinated incident. Each creature establishes a country around one coastal foothold. The creature rules that country, appears as its leader, and exists on the map as one unique apex division. Its country expands through ports, islands, river mouths, coastal capitals, and shallow hinterlands.

The event creates a world war made from several separate predators. The opening should feel global without instantly covering every coastline. Human countries face local survival problems. Monster countries face Hunger, coastal access, rival apexes, and a hard inland limit. The campaign can remain a scattered war of littoral empires, become an abyssal pact system, or end in Cthulhu's Dominion after World Collapse.

The event succeeds when each monster produces a recognisable campaign, defenders can understand how to kill it, and the world map keeps meaningful safe and threatened regions during baseline play.

## What the player should experience

### As a threatened ordinary country

The player first sees a named creature seize a nearby coastal state. Ports close, coastal populations flee, a new hostile flag appears, and one unusually strong enemy division anchors the invasion. The player has a clear strategic question. Preserve the coastline, evacuate it, or draw the apex inland and cut its Sea Bond.

The threat should be severe at once. It should not erase the country before the player can react when another valid opening exists. A one-state country may still be destroyed when every viable anchor would produce that result, but the selector must not choose that outcome casually.

The defending player can fight the invasion conventionally, starve its reinforcement loop, destroy its support formations, deny feeding, break its coastal network, or concentrate enough force to kill the apex. Killing the apex before terminal unification collapses its full country.

### As a monster country

A monster player begins with one apex division, a limited supporting force, one lair state, and a short survival window. The apex is much stronger than ordinary divisions, yet it cannot be replaced. The player must secure a second port, manage Hunger, protect Sea Bond, choose an inland adaptation, and decide whether rival monsters are prey, temporary partners, or future components of a terminal union.

The campaign must not become ordinary HOI4 under a monster flag. The country receives no normal recruit-and-deploy loop, no ordinary manpower economy, no equipment production plan, and no human cabinet. Its force growth comes from named objectives and destructive choices.

### As a distant major power

The event should become globally visible even when no monster appears nearby. Distant majors can fund ocean watch, send specialist forces, support threatened allies, secure naval routes, or exploit human weakness. They should not receive a full wall of local decisions for every invasion. The response category projects only the most urgent valid objectives.

### In multiplayer

Each human player receives accurate local information and can use the shared response system. A human-controlled monster receives its own mechanics and remains exempt from human civilian systems. The event must not duplicate global opening effects for every player. The opening, emergence ledger, terminal state, and Chaos changes are global transactions.

## Design pillars

### One creature, one life

Every named monster has exactly one apex division. No route creates a duplicate. No replacement appears after death. Cthulhu can unite living apexes but cannot restore a dead one.

### Coastal empires

Ordinary monster countries should form irregular maritime realms. They can dominate islands, ports, coastal capitals, and nearby hinterlands. They should stop before crossing a continent until a route explicitly extends their range.

### Distinct predators

The sixteen countries share lifecycle rules, civilian exclusions, force-generation principles, and terminal integration. Their apex roles, support mixtures, focus mechanics, pact preferences, geography, visual identity, and campaign plans differ.

### Defensible rules

The player must be able to learn why a monster is strong, where it weakens, how it gains reinforcements, and what happens when its apex dies. Mystery belongs in the event fiction. Core combat and objective rules need readable tooltips.

### Sparse runtime

The event processes registered monster countries and active threatened states. It must not add an unrestricted daily, weekly, or monthly scan over every country or every state.

### Earned escalation

Evolution changes the active package after a paced milestone. It does not add Chaos by itself. Cthulhu requires World Collapse and one of several proven campaign states.

## Core terms

| Term | Meaning |
| --- | --- |
| Apex | The one unique named monster division owned by a full monster country |
| Full monster country | A living event country whose apex survives and whose unique focus tree remains active |
| Support monster | A generic event-owned formation from one of six shared unit families |
| Lair | A registered controlled coastal state that anchors Sea Bond and selected decisions |
| Inland depth | A map-derived number counting state layers from the nearest valid saltwater coast |
| Operational range | The deepest inland layer that a monster route may target, core, and plan through |
| Hunger | A public country value from `0` to `100` that represents pressure to feed |
| Sea Bond | A public country value from `0` to `100` that represents coastal access and physical coherence |
| Emergence | Creation of one full monster country, apex, lair, supporting force, and first war package |
| Abyssal Remnant | A surviving tag whose apex died before Cthulhu unification |
| Pact | A staged monster-to-monster relationship that can end hostilities and unlock cooperation |
| Terminal readiness | Hidden proof that one of the Cthulhu paths is complete |
| Cthulhu's Dominion | The single public Event 043 world-end country and terminal campaign state |

## Event lifecycle

The normal lifecycle is:

1. Event 043 becomes eligible at Chaos level 3.
2. The Major-event picker selects Event 043.
3. The entry event resolves the active evolution package.
4. The opening selector chooses valid geographically separated monster identities and landing states.
5. Each selected monster receives a bounded emergence transaction.
6. Opening presentation and one global event-log entry occur.
7. Full monster countries run their event-owned campaign loops.
8. Evolution I or II can add later emergence waves when enabled and eligible.
9. Apex deaths collapse individual countries into defeat or remnant state.
10. At World Collapse, Evolution II may open one or more Cthulhu readiness paths.
11. A valid path can unite surviving full monster countries under Cthulhu.
12. Human victory comes from normal capitulation or destruction of every surviving apex.
13. A sufficiently long and destructive global campaign may open a defeat aftermath.

The event is fire-once as a Major. Later waves belong to its active lifecycle. They do not refire Event 043 through the random-event picker.

## Major-event classification

Event 043 must move out of the repeatable-event registry and into the Major-event registry. Its event weight starts and grows under the shared Major-event rules. When it fires, it resets the ordinary Major-event competition and the dynamic timer acceleration according to the current system.

The old flood script, old flood localisation, old event-name mapping, and old direct callers are replacement targets. Renaming the file while leaving Event 043 in the repeatable registry would break the design.

## Cluster decision

Event 043 belongs to no cluster.

The event already creates a coordinated multi-country global incident. Cluster wrapping would add another chance layer, create unclear pacing ownership, and make member-event logging hard to interpret. The `Alien Invasions` label from the early catalog block is not used because no matching cluster exists in the supplied cluster catalog and the brief later excludes this event from every cluster.

Implementation must leave the cluster ID and member severity fields empty.

## Country identity model

Every monster country is:

- a special Chaos country
- an actual nonhuman country
- exempt from normal civilian systems
- governed by one unique nonhuman leader
- assigned one unique focus tree
- assigned one unique apex unit
- unable to use ordinary recruitment
- unable to recreate its apex
- hostile to ordinary reachable neighbours
- hostile to other full monster countries unless a pact changes that relationship
- eligible for terminal integration while its apex lives

One stable marker should identify the Event 043 family. A second stable marker should prove active full-monster status. Creature-specific markers identify the apex package. Remnant and terminal markers replace the full-monster marker when those transitions occur.

The shared `is_special_chaos_country` and `is_actual_nonhuman_country` classifiers must recognise active full monsters, Cthulhu's Dominion, and Abyssal Remnants. The event owner sets stable markers. The shared classifier only answers the cross-system routing question.

## Event-owned world threat

At least one living full monster country activates an Event 043 world-threat source.

Recommended source identity:

```text
world_threat_source_monsters_from_deep
```

The Event 043 owner sets or clears this source, then calls the shared threat refresh. The source remains active during Cthulhu's Dominion and while meaningful Abyssal Remnants continue the war. It clears only when the event threat has ended.

This source must be added to the registered world-threat aggregate. A local duplicate `world_in_threat` flag is forbidden.

## Global event memory

The system must remember:

- Event 043 fired
- opening evolution package
- registered monster identities
- selected landing states
- every emergence date
- active full monsters
- dead apex identities
- remnant identities
- pact stages and betrayal memory
- regional coverage
- weighted coastal control
- terminal readiness path receipts
- Cthulhu unification status
- all-apex defeat status
- manual scenario launch state
- opening and later Chaos receipts
- global aftermath eligibility

Dead apex memory is permanent for the campaign. Tag retirement or terminal integration must not erase it.

## Opening event-log behavior

The opening records one Event 043 history row, not one random-event row for every monster. The detail view can list the opening roster and number of emerged countries through dynamic content.

Later emergences belong to the active Event 043 system. They can create report events and evolution-linked records without pretending Event 043 fired again.

Actual evolution milestones use the shared evolution logger. Normal focus progress, Hunger stages, pact proposals, territorial growth, and apex battles are not evolutions.

## Public information and uncertainty

The opening should make these facts clear:

- several named creatures appeared at once
- each seized a coastal foothold
- each leads a new hostile country
- the apex creature is physically present as one division
- the new countries attack reachable ordinary neighbours
- the invasions weaken inland
- more creatures may appear at higher Chaos

The opening should not state:

- the exact terminal thresholds
- which pact will succeed
- which readiness path is closest
- whether Cthulhu will awaken
- hidden reinforcement scores
- hidden AI target weights
- future surprise reports

The player can see public Hunger and Sea Bond for a selected monster through clear tooltips or visible ideas. A human monster player sees exact values and next thresholds. An ordinary enemy sees qualitative bands unless the implementation proves that exposing the exact number improves counterplay without creating clutter.

## Baseline campaign boundaries

At baseline:

- four monster countries normally emerge
- opening selection favours separate macroregions
- each receives one coastal lair state
- each receives one apex division
- each receives a bounded support package
- each begins wars against valid ordinary neighbours
- monsters remain hostile to one another
- normal operational range stops at shallow inland depth
- pact routes exist but develop slowly
- Cthulhu paths remain locked
- the rest of the roster remains dormant

The selector may create fewer than four when map validity, tag readiness, protected terminal state, or spacing rules prevent a safe fourth emergence. It may not fill the quota by forcing two apex capitals into the same crowded coast.

## Natural escalation boundaries

Evolution I increases roster size, support pressure, pact activity, and inland ambition. Evolution II opens all remaining valid regions and terminal readiness.

The event does not repeat from the Major pool. A direct call to the entry event after opening must reject or route to a deliberate debug or scenario path. Legacy event calls from unrelated systems must be removed or redirected to an event-owned, idempotent helper with a documented reason.

## Victory and failure in ordinary invasion play

A full monster country loses its unique campaign when its apex dies. It immediately surrenders to its current enemies. Its unique focus tree and terminal eligibility end.

A monster player can also lose through conventional capitulation while the apex survives. The apex and remaining formations follow the normal capitulation settlement defined by implementation. They must not remain under a dead or invalid country scope. The post-capitulation path needs explicit test coverage.

Human defenders can fail locally through loss of all coastal access, destruction of a capital, or expansion of a monster pact. Local failure does not automatically trigger a world end.

## Design limit on custom values

The complete Event 043 system exposes two persistent monster values. It does not add a third pact meter, fourth lair meter, fifth reinforcement currency, or global invasion score for ordinary play.

Pact stage is a named state. Inland depth is a state property. Regional coverage and terminal readiness are hidden proofs. Human response uses missions, map objectives, and ordinary resources.

## Design limit on interfaces

Event 043 does not receive a full custom scripted GUI in this specification.

The intended presentation uses:

- one evolving monster decision category
- one human-response decision category
- strong static or animated category pictures with static fallbacks
- compact status text
- map highlights
- state and national-spirit tooltips
- existing Event Details and Event Logs surfaces
- normal focus-tree presentation and Focus Navigation

A full custom window would have to justify another persistent interface beside sixteen focus trees and two decision categories. The current design does not require it. Implementation should not add one without a separate accepted addendum.

## Relationship with the old flood event

The old Event 043 applies global coastal damage through broad loops. None of that behavior survives as an Event 043 baseline effect.

Useful flood behavior can remain under Event 013 Natural Disasters. Event 043 must not call the old flood effects as an emergence shortcut. Jiaolong and selected monster routes may cause local flood damage through Event 043-owned, bounded state effects or the documented Natural Disasters gateway when that integration is justified.

## End of Part 1

Part 2 defines landing regions, opening selection, map safety, first wars, inland depth, and operational range.
