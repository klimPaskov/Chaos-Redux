# Event 010 — Death: Core Spec and Campaign Flow

## Replacement mandate

Event ID `10` is **Death**. It completely replaces the obsolete `Spirit of War/Peace` event.

The implementation must remove the old concept from every active surface: event script, event name mapping, debug mapping, event detail text, event catalog row, manual trigger labels, documentation, prompts, localisation, and any old decision or idea references. Nothing in the new event should mention, inherit, or imply the former `Spirit of War/Peace` design.

## Event identity

| Field | Required design |
| --- | --- |
| Event ID | `10` |
| Event name | `Death` |
| Event type | Minor Fire-Once |
| Cluster | No cluster |
| Primary country | `Death` |
| Proposed tag | `DTH`, subject to final conflict check |
| Leader | `Zol` |
| Map color | Complete black, not dark grey |
| First location | Random remote low-population ocean island state |
| First impression | Silent, inactive, peaceful, easy to ignore |
| Initial units | None |
| First public knowledge | Delayed missing-island reports, not a reveal of Death |
| True reveal | First consumed mainland state with more than 100,000 population |
| Terminal branch | Death consumes a full continent while Chaos is above 1000 |
| Final branch | Death consumes all eligible world states |

Death is not a normal country with ambitions, claims, ideology, industry, diplomacy, or politics. It is a black country on the map, ruled by Zol, that turns controlled states into empty territory. At first it should look like a strange quiet island tag that will probably never matter. The world should not receive a normal event announcement when Death appears.

## Player-facing promise

The event works because the player is allowed to miss it.

The first island does not open with a proclamation, super-event, global news item, world-threat flag, coalition decision, or obvious scripted GUI. The map has changed, but the event system does not tell the world what that means. Months later, small reports mention that nobody has heard from the island. The reports should sound like a bad telegraph line, a storm, a failed census, a quarantine rumour, or a shipping-office mistake. They should not say that a country called Death exists, that Zol rules it, or that the island has been consumed.

The danger becomes readable through repetition: more islands stop answering, state populations disappear, and the black country keeps acquiring useless territory. The true reveal happens only after the pattern reaches a mainland population centre large enough that governments cannot dismiss it.

## Baseline campaign stages

Baseline stages are the ordinary flow of the Death crisis. The First Silence and origin consumption are setup, not evolution entries. The event log records later milestone evolutions only after their required chaos tier and their actual in-world action have happened, so the event-log/evolution/detail window can explain a hidden crisis after the fact without pretending every baseline step is an evolution.

### Stage 0 — Hidden bootstrap

A hidden event creates or activates Death on one eligible remote island state. The old owner silently loses control of that state. Death owns and controls it, cores it, and the state becomes a Death wasteland immediately.

No popup fires. No super-event fires. No world threat flag is set. No coalition decisions appear. No public event log text should tell the player that Event 010 created a hostile crisis.

The first state consumption records the population loss internally and adds the lost population to the Death consumed-population variable. If the shared civilian deaths system is enabled, it also records civilian deaths through the shared death tracker. If that system is disabled, Death still tracks consumed population for its own spread scaling.

### Stage 1 — Quiet island origin

Death does almost nothing for a long time. It has no army and makes no declarations. It cannot attack by ordinary fronts. Its first spread pulses prefer tiny nearby island states with the lowest population and low strategic value.

A delayed report event may fire 90 to 180 days after the origin. It should not be global unless the player owns the island, controls it, owns nearby coasts, controls a nearby naval base, or has a relevant intelligence/observation hook. The report direction is:

- a radio silence;
- a mail ship returning with nobody at the pier;
- a colonial office missing a census return;
- fishing crews avoiding the place;
- rumours of a storm even though the weather records do not agree.

The report should offer small reactions such as sending a survey boat, waiting for the next mail ship, or filing it as a local matter. It must not reveal Death or Zol.

### Stage 2 — Island spread

Death consumes other islands. It still does not announce itself. It should continue selecting low-population island targets first. The player can miss the pattern unless they watch the map, own affected islands, or respond to delayed reports.

Repeated island reports become slightly more disturbing but still indirect. The strongest pre-reveal wording may say that several island offices have stopped answering and that maps no longer agree with shipping reports. It still should not say that Death is spreading.

Death remains militarily weak in this stage. It has no divisions and cannot be defeated through a conventional frontline unless a country discovers it, declares war, and occupies its tiles.

### Stage 3 — Mainland reveal

The reveal triggers when Death consumes a mainland state with more than 100,000 population. A nearby coastal state on a continent is the intended target. The threshold refers to the population of the state at the moment of consumption before it is set to zero.

The reveal fires a super-event. The world now recognizes that this is not an ordinary insurgency, secession, colony, epidemic, or diplomatic accident. The country name `Death` and leader `Zol` can be stated openly after this point.

After reveal:

- Death becomes a world threat source.
- Death automatically declares war on any country that controls a neighboring state.
- Countries can use public containment decisions.
- Death can wither neighboring states if it controls at least one mainland state.
- The defender can block withering by keeping non-Death divisions present in the target state.
- Death can attempt a coastal jump if pushed back from the mainland, subject to cooldown and target rules.
- Ghost divisions can appear later through evolution stages, but the reveal itself should not instantly spawn an army unless the campaign is already at a high chaos evolved opening.

The reveal should feel like the moment the world finally gives the black shape on the map a name.

### Stage 4 — Continental threat and world-end opening

The terminal branch begins only when both conditions are true:

1. Death has consumed every eligible inhabited state on one continent; and
2. Chaos is above 1000.

If Death consumes a continent before Chaos passes 1000, the crisis enters a severe non-terminal `Black Continent` state and waits. If Chaos passes 1000 before a continent is fully consumed, the event remains a major world threat but does not start its world-end branch yet.

When both conditions are true, Death becomes a world-end scenario:

- automatic random event firing should be frozen or gated as required by the world-end system;
- a world-end super-event fires;
- a random coastal foothold is created on every remaining continent that does not already contain Death;
- Death spawns ghost divisions in those footholds;
- Death shifts from passive border pressure to aggressive expansion;
- withering intensifies and no longer waits as long between pulses;
- all containment decisions move into emergency mode.

The world-end state is not just a stronger evolution. It is a terminal campaign branch.

### Stage 5 — World consumed

When Death controls or has consumed every eligible world state, a final super-event fires and the Death completion tracking can resolve for the relevant player state.

The final stage should not be written as a normal victory parade. There is no audience. The tone is silence, record failure, and the absence of witnesses. If a human player reaches this as a Herald of Zol or through a Death-controlled scenario, the achievement can still record it, but the final event text should emphasize that survival through allegiance is not normal survival.

## Eligibility and starting-location rules

The origin target should be selected from ordered island eligibility tiers. The event should show `N/A` in event detail/manual availability if no valid island state exists at all.

### Preferred origin tier

A valid preferred origin state:

- is an island state with no land adjacency to another state;
- is coastal;
- has low population, normally below 75,000;
- is not a national capital;
- is not owned by a major;
- is not the player capital;
- has little or no industry;
- is not already a wasteland, outbreak core, terminal scenario state, or other special chaos-country seat;
- is not currently occupied by a non-owner army;
- is not a scripted state that another active event requires.

### Secondary origin tier

If the preferred tier has no candidates, the secondary tier may allow remote island states below 250,000 population, still excluding capitals, majors, player capitals, occupied states, and critical event states. The secondary tier must remain island-only. Do not silently switch to a mainland origin.

### Target bias

Within the valid origin pool, bias toward:

- lower population;
- lower industrial value;
- farther distance from major capitals;
- island states with few ports and low supply;
- states in the middle of oceans rather than dense archipelagos beside major home islands.

The event should not always choose the same famous island. The point is that a place nobody is watching stops answering.

## Public event chain direction

### Hidden creation event

`chaosx.nr10.1` is the canonical entry event. It may be hidden and should create Death without opening a popup. It initializes variables, consumes the origin, registers the event, schedules delayed reports, and marks the old Spirit event as superseded in documentation.

### Delayed report events before reveal

Pre-reveal reports should be small report events or local news events, not global super-events. Countries far away from the islands shouldn't even get notified. The events should appear after a long delay, because news move from remote places very slowly.

Suggested titles:

- `The Mail Boat Waited Until Dusk`
- `No Answer from the Island Office`
- `The Lighthouse Kept Burning`

Suggested option tone:

- dry official uncertainty;
- mild annoyance;
- uneasy maritime superstition;
- colonial bureaucracy pretending nothing serious happened;
- no direct apocalyptic language.

Example option directions:

- `The mail will arrive tomorrow.`
- `Blame the weather and file another copy.`

### Mainland reveal super-event

The reveal super-event should be blunt and memorable. It should use the name `Death` only after the trigger has happened.

Do not prewrite the title, button text, cultural remark, or quote in this spec. Those fields must be researched through the super-event text workflow, with documented candidates, source links, attribution confidence, and copyright notes. The implementation agent must treat any unresearched text as blocked, not as final localisation.

Title research direction: find a short reveal title that names or exposes the crisis without making the moment sound like the final apocalypse.

Description direction: a mainland coastal state has emptied; the black country on the map is no longer a remote anomaly; governments now understand that ordinary quarantine, diplomacy, and colonial inquiry cannot explain the silence.

Button or cultural remark research direction: find a short researched line or allusion that reacts to diplomatic helplessness, official disbelief, counting the living, or the failure of ordinary treaty language. Do not use an invented sample line.

Quote research direction: verify a quote about death, silence, discovery, fear, naming, or the inevitable. Prefer public-domain literature, scripture, philosophy, speeches, or historical sources.

### Continental world-end super-event

Do not prewrite the title, button text, cultural remark, or quote in this spec. The super-event text researcher must select them from sourced candidates.

Title research direction: find a short terminal title tied to coasts, final borders, silence, or the spread of Death across continents.

Description direction: one continent has become a black absence, Chaos has passed the world-end threshold, and new black footholds are appearing on every continent. The event should tell the player this is a terminal scenario without writing a mechanical checklist inside the super-event text.

Button or cultural remark research direction: find a short researched line or allusion about every shore becoming exposed, the sea carrying disaster, or the last safe border failing. Do not use an invented sample line.

Quote research direction: verify a quote about finality, judgment, silence, shores, collapse, or the end of order.

### Defeat aftermath super-event

If Death is defeated after reveal and after consuming a large population threshold, a defeat aftermath super-event should fire. The threshold should be high enough that the world suffered a real crisis, for example more than 10 million consumed population, a mainland foothold, or a world-end attempt.

Do not prewrite the title, button text, cultural remark, or quote in this spec. The text package must be researched and documented before implementation.

Title research direction: find a short aftermath title about survival, empty land, memory, or victory that cannot restore the dead.

Description direction: Death is gone from the map, but the states it consumed remain empty. The victory is real, but it does not restore the people, ports, factories, or towns that vanished.

Button or cultural remark research direction: find a researched line or allusion about grief, memorial records, the limits of victory, or the names of the dead. Do not use an invented sample line.

Quote research direction: verify a quote about memory, survival, grief, vigilance, or rebuilding after loss.

### Whole-world consumed super-event

Do not prewrite the title, button text, cultural remark, or quote in this spec. This final package must be researched, sourced, and documented.

Title research direction: find a short final title about witness, silence, last records, or the end of human observation.

Description direction: the last records stop. The last radio claims to hear nothing. The last map contains one country and no population to read it.

Button or cultural remark research direction: find a researched line or allusion about silence without witnesses, the end of record keeping, or the absence of an audience. Do not use an invented sample line.

Quote research direction: verify a quote about silence, oblivion, lastness, witness, or the failure of records.

## Event details window wording

The Event Details window should describe the premise, not the mechanics. It should not list attrition, speed penalties, population deletion values, or spawn formulas. A suitable direction:

> A quiet black country appears on a remote island and does not announce itself. Months later, nearby records stop matching reality. Islands fall silent, ports empty, and the name Death remains more rumour than diplomacy until the first mainland state vanishes.

The details field should mention that the event replaces `Spirit of War/Peace` only in developer documentation, not in player-facing text.

## Event log and evolution log role

Event log history should record the fire-once event as Death once it is known. Before reveal, reports can be logged under ambiguous labels if the event log supports hidden-stage text. After reveal, all logs should use `Death`.

Evolution logs should record Death's milestone mutations as descriptive crisis history. The Island Pattern, mainland reveal, Last Shores, and whole-world consumption are evolution/detail entries only after the required chaos tier has been reached and the corresponding spread, consumption, or world-end action has happened. The quiet origin, delayed local reports, and `The First Silence` remain baseline setup and should not be logged as evolutions.

## Cluster role

Death has no event cluster. It is a solitary fire-once incident with its own internal escalation. It should not be added to Wars, Natural Disasters, Various Anomalies, or any other cluster unless a future accepted spec explicitly creates a Death-related cluster.

## Non-negotiables

- Event ID 10 is `Death`
- Death starts on a remote island and is not globally announced.
- The hidden island stage spreads slowly, prioritizes nearby sub-100,000-population islands, and falls back to distant eligible islands only when no nearby target exists.
- The mainland reveal path cannot open before the Island Pattern evolution has happened through delayed evolution pacing, the required chaos tier has been reached, and enough hidden island pressure exists.
- Death has no starting units.
- Every consumed state becomes a wasteland and its population is deleted.
- Death must be defeated by occupying all of its tiles, not by ordinary surrender shortcuts.
- The first true reveal is mainland consumption over 100,000 population.
- Death states must be strategically useless, hostile to divisions, and visually dark/foggy if the engine and assets allow it.
- Death's spread accelerates with consumed population.
- Ghost divisions appear only around the 600-tier evolution and strengthen at later stages.
- The world-end branch requires both continent consumption and Chaos above 1000.
- The final whole-world consumed branch has a super-event and achievement.
