# Half gone

## Catalog entry

- Event ID: `094`
- Event name: Half gone
- Type: Minor Repeatable
- Status: To Be Reworked
- Chaos level: 1
- Cluster: Various Anomalies
- Cluster role: Medium member

## Core idea

> Half of something a country owns suddenly disappears.

Each firing affects one random valid major country or player-controlled country.

At baseline, the affected country loses **50% of every eligible equipment stockpile** it currently possesses.

Because the event is repeatable, later firings always halve what exists at that moment.

The event never explains where the missing things went.

## Baseline

The target loses half of all compatible stored military equipment.

This should cover the country's actual current stockpiles dynamically, including ordinary, DLC, country-specific, captured, outdated, and Chaos Redux equipment where applicable.

The event does not use fixed quantities.

Equipment already fielded with active formations is not part of the baseline disappearance. The baseline is about what is sitting in reserve.

## The mystery

Warehouses can remain locked.

Guards can report nothing unusual.

Records can still claim that the missing equipment should be there.

The event should never settle on one explanation such as theft, sabotage, corruption, or supernatural intervention.

The recurring pattern is simply that **half is gone**.

# Evolutions

The evolutions expand what can disappear.

The basic rule stays the same. A selected category loses roughly half of what the country currently has.

## Evolution I: Half the Reserves

- Chaos requirement: `200+`.

In addition to the normal equipment loss, another national reserve can be halved.

Possible categories include:

- fuel
- Political Power
- Command Power
- Army Experience
- Navy Experience
- Air Experience
- convoys
- trains
- other compatible accumulated national resources

The additional category is selected dynamically from values the country actually possesses.

## Evolution II: Half the Nation

- Chaos requirement: `400+`.

The event can begin halving broader national values.

Possible categories include:

- stability
- war support
- available manpower
- research progress
- intelligence-related resources where applicable
- other suitable country-level values

The loss is always proportional to the current value.

If the country has 80% stability and stability is selected, roughly half of that current stability disappears.

## Evolution III: Half the People

- Chaos requirement: `600+`.

People themselves can disappear.

Possible categories include:

- civilian population
- generals
- field marshals
- admirals
- operatives
- advisors
- scientists
- other important character groups

If population is selected, roughly half of the country's current population disappears across its populated territory.

If a character group is selected, roughly half of the valid characters in that group disappear.

Unique Chaos Redux characters such as Doctor Wu or the Brilliant Scientist can receive special connected outcomes in the full planning pass instead of being treated exactly like generic characters.

## Evolution IV: Half of Everything

- Chaos requirement: `800+`.

A single firing can strike several different categories at once.

Equipment still loses its normal half, while additional categories are selected dynamically from everything unlocked by the earlier evolutions.

A severe firing could therefore remove half of the equipment stockpile and also halve several things such as fuel, experience, stability, manpower, population, or commanders.

The exact combination changes from country to country and from firing to firing.

## Repeat behavior

Every firing reads current values.

If a country rebuilds what it lost, a later firing can halve the rebuilt amount again.

If it never recovers, another firing halves the smaller remaining amount.

The event should never remember an old original value and subtract from that.

## Connections

**Abundance** can become especially valuable when it affects something that Half gone previously reduced.

**Doctor Wu** and **Brilliant Scientist** can receive special consequences if their characters are caught by the later disappearance evolutions.

**Deal with the Devil** can use a severe Half gone crisis as a reason to offer an extremely tempting replacement or restoration deal.

## Your Task

Create the full specs and expand the idea thoroughly using the full planning skill, all the other skills, and provided subagents. Before writing the specs, fully and thoroughly read and process all required project source files and must-read skill files. If you are unable to fully read every file, then say so directly and be honest in your final output. If you simplified or truncated things for a quicker output then also be honest about it.
