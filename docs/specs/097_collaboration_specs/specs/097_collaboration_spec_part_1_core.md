# Event 097 Collaboration: Part 1, Core Event

## Event identity

Collaboration is a Minor Repeatable event available from Chaos level 1. It belongs to the Intelligence cluster as a Medium-severity member. The existing `chaosx.nr97` namespace and the entry event `chaosx.nr97.1` stay stable.

The event has one sentence at its center: everyone has collaborators everywhere.

When it fires, every valid country gains a prepared network of collaborators inside every other valid country. The networks use the native Hearts of Iron IV collaboration value and nothing else as their store of power. There is no Collaboration currency, no new meter, and no management screen. The event changes the world by making the existing collaboration rules matter in every war at once.

## Event promise

The player should finish the first firing understanding three things.

1. Every government now has people abroad who will cooperate with it once its armies arrive, and every foreign government has the same inside this country.
2. Wars will end sooner and occupied land will be easier to hold, for the player and for everyone fighting the player.
3. Each later firing makes the same networks deeper, and higher Chaos lets them grow into organized administrations, an internal fifth column, and finally governments ready to replace defeated ones.

The event should feel quiet, ugly, and global, with no explosion at its center. Officials, clerks, policemen, factory managers, party secretaries, and junior officers in every capital quietly start to keep two sets of loyalties. The danger appears later, when the first state falls and its administration turns up for work under the new flag the next morning.

## What collaboration does in the engine

The design builds on the native collaboration value between two countries, stored on a scale from 0 to 100 percent. Engine rules that already exist, and that the design relies on, are recorded in `research/097_collaboration_research_notes.md`. In short:

- Collaboration lowers the host's surrender limit against the beneficiary, so a host with deep foreign networks capitulates earlier to that enemy.
- At capitulation, each percent of collaboration becomes one point of starting compliance in the territory the beneficiary occupies.
- Countries with collaboration receive a bonus when the engine decides which enemy receives a capitulation.
- High compliance reduces resistance targets, garrison needs, and peace-conference costs, and the vanilla collaboration-government route opens at high average compliance.

The baseline event touches only this native value. Every stronger behavior belongs to an evolution and is described in Part 2 and Part 3.

## Participants

A country participates in a firing when it exists, owns at least one state, and uses ordinary human civilian systems.

The shared classifiers decide the human boundary. Actual nonhuman countries never participate in either direction, because they have no population that could collaborate and no human society that would collaborate with them. Special Chaos countries managed by other events also stay outside the event in both directions. Their identities, governments, and lifecycles are owned by scripted logic that a native collaboration government or a seated foreign administration would break. Examples include Death's realm, rat realms, outbreak actors, and Fury hosts.

Everything else participates without exception:

- democracies, fascist states, communist states, monarchies, and non-aligned regimes
- allies, faction partners, subjects, overlords, neutrals, rivals, and enemies
- collaboration governments created earlier by this event or by vanilla
- event-created ordinary countries such as Independence Wave states, once they own territory

A government in exile that owns no state does not receive new networks as a host because there is no territory left for collaborators to deliver. It still receives networks abroad as a beneficiary, because its own exiles and sympathizers remain in other countries. Collaboration it held before exile stays in place.

A country created after a firing joins at the next firing. It does not receive a back-payment for earlier firings.

If fewer than two countries can participate, Event 097 is unavailable and shows `N/A` in the event list.

## The layer

Each firing adds one layer of collaboration to every ordered pair of participants. A pair is ordered because the network of France inside Germany is a different network from that of Germany inside France. Both receive a layer from the same firing.

### Base layer size

| World state at the moment of application | Base layer |
| --- | --- |
| Deep Networks not active | 15 percentage points |
| Deep Networks active (Evolution I) | 25 percentage points |

These are tuning anchors kept in one script constant group. The values were chosen so that one firing is noticeable at capitulation, where 15 points of collaboration become 15 points of starting compliance and lower every host's surrender limit against every enemy, while the vanilla 80 percent collaboration-government threshold stays out of reach until the event has fired several times or Evolution IV opens its own route.

### Stance multipliers

The base layer is the same for every pair. The only pair-level differences come from the choice each government makes in the opening report (see below). Each country chooses one stance for the current firing. The stance changes two multipliers:

- the outgoing multiplier, applied to the networks this country gains abroad
- the incoming multiplier, applied to the networks every foreign country gains inside this country

The layer for beneficiary B inside host H equals the base layer times B's outgoing multiplier times H's incoming multiplier.

| Stance | Outgoing multiplier | Incoming multiplier | Cost |
| --- | --- | --- | --- |
| Accept the situation | 1.0 | 1.0 | none |
| Cultivate the networks | 1.5 | 1.25 | the country's own services become more porous |
| Screen the state apparatus | 0.75 | 0.5 | a timed vetting campaign (see below) |

The table describes design intent. The final values are tuning anchors in the same constant group and must pass the probability and balance checks in `matrices/097_collaboration_ai_probability_scenarios.md`.

Stances apply to the current firing only. The next firing asks again.

### Why the base layer stays uniform

The brief is explicit that the event ignores ideology, alliances, relations, and plausibility, and that it is global and symmetrical. A uniform base layer is what keeps the event readable: the player can always say that every foreign government holds at least the same network inside this country as this country holds inside them. Dynamic behavior lives in the places where it matters and where the player can act on it:

- the size of the layer changes with the evolution state
- each country chooses how open or closed it is for each firing
- engine collaboration stops at 100 percent, so repeated layers naturally lose value near the cap
- Fifth Column strength scales with the host's military situation and the strongest enemy network (Part 3)
- prepared administrations scale with the network of the specific occupier (Part 3)
- cluster combinations with Events 039 and 052 add bounded extra depth to one host (Part 5)

### Engine cap and repeated firings

Collaboration cannot exceed 100 percent. A pair that already sits at the cap gains nothing from a later layer. The design adds no separate ceiling. The brief asks for stacking only as far as the native system meaningfully allows, and the native cap provides that limit.

Two Accept countries reach the vanilla 80 percent collaboration-government level after four firings when at least two of them use the Deep Networks layer, or after six base firings. Whether that happens early or late depends on how often the event fires, described below. Reaching it in mid-campaign is accepted, because the brief asks for stronger foundations for collaboration governments. Evolution IV adds its own lower installation route and the Installed Administration package at high Chaos.

### Expected number of natural firings

The shared Repeatable rules halve the event's weight cap after each firing and recover a small amount of weight after each pacing update, major or minor. Every repeatable event shares those rules, so the halving evens out firing counts across the pool instead of limiting Event 097 on its own. The number of natural firings depends mainly on how many events are enabled, the Chaos path, and the player's event settings.

A planning estimate from the probability review, not yet confirmed with the HOI4 probability tools, gives these ranges over ten years:

- with a small enabled pool like today's default list, about six to eleven firings, with the fourth firing around the fifth to seventh year
- with every event enabled, about one to three firings

The design is built to work across that whole range. The native 100 percent cap stops depth growth in long campaigns with many firings, the stance choice lets each country slow its own exposure, and the evolutions give a campaign with few firings its deeper behavior.

Network depth does not depend on firings alone. The Deep Networks tranche adds one extra layer to every pair without a firing, and later evolutions turn the existing depth into stronger behavior instead of requiring more firings. The table below states the depth a pair of two Accept countries reaches.

| Firings | Without Deep Networks | Deep Networks from the third firing, with its tranche |
| --- | --- | --- |
| 1 | 15 | 15 |
| 2 | 30 | 30 |
| 3 | 45 | 40 tranche, then 65 |
| 4 | 60 | 90 |
| 5 | 75 | 100 |
| 6 | 90 | 100 |
| 7 | 100 | 100 |

From the seventh firing, every Accept pair is at the native cap in both columns. These figures are the reference for the balance scenarios in Part 6. Two countries that both choose Cultivate in every firing reach the Strong band after two firings and the Total band after three. Two countries that both choose Screen gain about 5.6 points per base firing in each direction, stay in the Thin band for two firings, and reach the Ordinary band on the third. Band names are defined in Part 3.

### Collaboration from other sources

Event 097 adds to the native value and never overwrites it, so collaboration earned through vanilla intelligence operations or other events stays in place. The few reductions in this specification subtract a fixed number of points from the current value, whatever produced it, and stop at zero.

## The opening report

### Flow

1. The hidden entry event confirms that at least two countries can participate, freezes the participant list for this firing, records the firing, and decides whether the layer uses the base or Deep Networks size.
2. Every participant receives the opening report.
3. Each government chooses a stance. AI countries choose immediately. Human players can take the time the event allows.
4. After a response window, the layers are applied in a hidden application pass. The pass reads every participant's chosen stance and applies each ordered pair exactly once.
5. When the pass is complete, the event records its own Chaos change (see `matrices/097_collaboration_chaos_impact_map.md`) and runs any evolution follow-up that depends on the new layer.

The response window is a tuning anchor with an ordinary value of about two weeks. It exists so that human stance choices count. A player who never answers receives the first option, which is Accept.

### Application performance

The application pass touches every ordered pair of participants. With N participants it makes N times N minus 1 collaboration changes, which is close to ten thousand for a world of one hundred countries. The pass must be spread across several days by processing a bounded batch of beneficiaries per day from the frozen participant list. Each beneficiary is processed once, and a country that stops being valid before its batch runs is skipped.

The pass belongs to the event itself: each step processes one batch and schedules the next step a day later until the list is finished. It adds no periodic hook and does not ride on any shared daily pulse. It runs once per firing and ends.

### What the player sees

The report goes to every participant from its own point of view. The government learns that foreign sympathizers have appeared inside its own ministries, police, factories, and political organizations, and that its own sympathizers have appeared abroad in the same numbers.

The player learns nothing exact. They do not learn names, numbers, or which foreign power is most active. They learn that the same thing is happening everywhere and that no country appears to be an exception.

The option tooltips show the visible consequence of each stance in plain terms: our networks abroad grow faster or slower, and foreign networks among us grow faster or slower. Exact multipliers can appear in the tooltip as percentages because they describe a direct, visible consequence of the choice.

### Stance details

#### Accept the situation

The government notes the reports and does nothing unusual. It is the default and has no cost.

Option direction: resigned bureaucratic shrug, or the cynical observation that a country cannot arrest its whole civil service. It should read as realism that is slightly too comfortable.

#### Cultivate the networks

The government decides that the foreign friends of today are the administrators of tomorrow and tells its embassies, trade missions, émigré offices, and party contacts to keep every useful name warm. The price is that the same openness lets foreign services find more willing contacts at home.

Option direction: cold opportunism. The speaker plans ahead for conquests and treats foreign officials as future employees. Ideology changes the register. A fascist government talks about friends of the new order abroad. A communist government talks about fraternal parties and class allies. A democracy talks about consular contacts and commercial goodwill, which should read as self-serving euphemism. A non-aligned government talks about keeping every door open.

#### Screen the state apparatus

The government opens a vetting campaign across ministries, police, the officer corps, and major enterprises. Foreign networks among its people grow at half the normal rate in this firing, and its own networks abroad also shrink because émigré contacts and friendly foreign officials stop trusting a government that is arresting its own.

The cost is a timed national spirit, working label Vetting Campaign, that lowers stability and raises consumer goods demand while the campaign runs. Its duration is dynamic. It runs longer for a country at war or under Fifth Column pressure, because vetting in wartime disrupts more of the state, and shorter for a country at peace. The ordinary anchors are 120 days at peace and 180 days at war, with stability and consumer goods values large enough to matter, such as 10 percent each. A country already running a Vetting Campaign from an earlier firing can choose Screen again, and the new campaign replaces the old one with the new duration instead of stacking.

Screen also has a requirement: the country must not be in open civil war, and its stability must be at least 30 percent, a tuning anchor that keeps the vetting campaign from pushing a fragile state toward collapse. The blocked tooltip names the exact requirement. The option is still visible when blocked, and the event always keeps Accept as a valid choice.

Option direction: suspicion that turns on the speaker. The irony is that the vetting committee itself may contain the people it is looking for, and the report should let the player suspect this without stating it. Grim irony fits. Comedy at the expense of victims of purges does not.

### Text tone for the opening report

Viewpoint: the receiving government, written as an in-world account of what its services are noticing. Visible information: sympathizers in many institutions, the same pattern abroad, no evidence of a single organizer. Uncertain information: who started it, how deep it goes, and which foreign power gains the most.

The text must not explain the mechanic, must not mention surrender limits or compliance, and must not announce that conquest has become easier. It should show behavior instead: clerks who copy lists for strangers, a police inspector who knows a foreign language he never studied, a factory director who has already chosen which flag to fly, and a provincial prefect who asks which office he will report to after the war.

The tone is quiet and corrosive, as fits a minor event, and a sharp line is welcome when it exposes cynicism. The writing must avoid bureaucratic document motifs as the main source of mystery, staged contrast between unofficial fear and official denial, labels such as warning or threat, and real collaborator names. The final wording belongs to the implementation agent and follows the localisation direction in `handoffs/097_collaboration_localisation_direction.md`.

## Hidden records

The event owns a small set of hidden records. None of them is a new public meter.

### Global records

- number of times Event 097 has applied layers in this campaign
- size of the last applied base layer
- current evolution states and their activation dates
- the frozen participant list and batch cursor of the active application pass
- milestone markers used by the Chaos impact map and achievements
- the registry of collaboration governments installed through the Event 097 route (Part 3 and Part 5)

### Country records

- incoming network depth: the total collaboration that Event 097 has added inside this country, after incoming multipliers, capped at 100
- outgoing network depth: the total collaboration that Event 097 has added for this country abroad before host multipliers, capped at 100
- the stance chosen in each firing, kept for achievements
- Fifth Column state, active responses, and cooldowns (Part 3 and Part 4)

The two depth records mirror what Event 097 has added. They do not try to read the native per-pair value, which the engine exposes reliably only in occupation contexts. They exist so the player and AI can understand the event's own contribution without a per-pair ledger of thousands of entries.

## Public presentation

The event keeps the public-facing value budget at the minimum the mechanic allows. The single public value is the native collaboration itself. The event presents it through two qualitative readings derived from the hidden depth records:

| Reading | Source | Bands |
| --- | --- | --- |
| Foreign networks among us | incoming network depth | Scattered below 20, Established from 20, Deep from 40, Pervasive from 70 |
| Our networks abroad | outgoing network depth | same bands |

The readings appear in the opening-report option tooltips, in the Loyalties decision category header when that category is visible (Part 4), and in the reports of later evolutions. They use words, not numbers, and each band has a short tooltip that explains what it means in play. For example, Deep tells the player that enemy armies will find administrations ready to serve them and that capitulation will come sooner.

The readings share one colour identity in dark tooltip and decision surfaces. Reports drawn on parchment use plain text for these words, without colour formatting.

## Selection and weight

Event 097 uses the shared Repeatable rules for weight recovery and cap reduction. Its normal eligibility needs at least two valid participants and no application pass in progress. Both conditions are reported through the shared unavailability path, so the event list shows `N/A` with a reason instead of a silent zero weight.

The event uses the ordinary shared weight. The shared selection system has no event-owned weight factor, and adding one would change event selection for every event. A war-weighted factor for Event 097 is recorded as an unresolved proposal in the package README and is not part of this specification.

The event has no actor. It records one history row per firing with no country flag.

## Event Details premise

The Event Details text describes the premise and nothing else. It says that sympathizers prepared to serve foreign governments have appeared in every country at once, that each government has the same abroad, and that the networks grow deeper as the world grows more unstable. It does not list effects, numbers, stances, or evolution rules.

One qualitative current-state line is allowed, in the same style as other Chaos Redux events that show a current reading: how deep the networks have grown in this campaign, using words such as first contacts, spreading, or entrenched, derived from the firing count and evolution state.

## Cleanup and persistence

Collaboration added by Event 097 is permanent native state. It does not decay through event logic and it is not removed when the event ends, because the event has no end. Reductions happen only through the responses and connections described in this specification.

Temporary state clears on schedule:

- stance markers clear after the application pass completes
- the Vetting Campaign spirit expires on its own timer
- Fifth Column modifiers and decisions clear at peace, capitulation, or annexation (Part 3)
- registry rows for installed governments clear when the government stops existing or stops being a subject of its installer (Part 3)

The Fallout transition resets diplomatic memory, including collaboration, through its own system. It records every collaboration pair, sets every pair to zero, and then fails its clean-world proof if any pair still holds collaboration. Event 097 must not reapply or restore collaboration during or after that reset. When the Fallout transition has begun, Event 097 becomes unavailable for selection, its pending application pass stops at the next step without applying another batch, and its evolution behaviors stop creating new consequences. Every Event 097 write to native collaboration, including the shared write surface in Part 5, checks the Fallout gate first.
