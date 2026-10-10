# Asteroid Incoming, Part 5: Evolutions

Status: implemented, except the fragment-marker cleanup marked as proposed.
The evolution thresholds and armour values are explicit user requirements ([README](028_asteroid_incoming_spec_index.md#explicit-user-requirements)).

## Structure

Event 028 has two sequential evolutions that change the strike; neither creates a separate event.

| Evolution | Shared toggle id | Tier | Threshold | Requires |
| --- | --- | --- | --- | --- |
| Global Fragmentation | event 28, type 2801, stage 1 | Chaos Tier | 600 Chaos | A strike |
| Extraordinary Minerals | event 28, type 2802, stage 1 | Totalen Chaos | 800 Chaos | Global Fragmentation applied in the same strike |

Accepted decision F04 (basis: user-granted design authority): the Chaos thresholds are read once in the opening snapshot, because they are part of what the board announced, while the Events Log toggles are read again at impact.
Disabling Global Fragmentation after the opening gives a clean main-only strike; disabling Extraordinary Minerals keeps the fragments without armour bonuses.
The snapshot records Extraordinary Minerals as eligible only when Global Fragmentation was eligible in the same snapshot, so the board never announces minerals without fragmentation.

An evolution is logged only when it actually applies.
The near miss records no evolution.

## Global Fragmentation

### Role

The altered course destabilizes the asteroid.
The main body still strikes the chosen state while smaller fragments strike unrelated states worldwide, including possibly the chooser's own territory.
The chooser controls the main target and accepts uncertainty for the rest of the planet.

### Fragment count

The planned count rises with Chaos: 3 at 600, 4 at 700, 5 at 800 and 6 at 900.
The actual count can be lower when the world lacks separated valid centres, and fewer than two applied centres means the evolution does not apply for that strike (the main impact still resolves).
Reports and the history row state the actual count.

### Centre selection

A fragment centre is a valid populated land state outside the main footprint and outside other fragments' first rings, never an existing crater or wasteland, and never an actually nonhuman or system country's state.
The planner prefers several continents, one centre per country and centres with a land neighbour, includes majors and minors alike, and can strike the chooser.
All centres lock before any damage, so the selection cannot change mid-transaction.
Locations are never shown before impact.

### Fragment damage

Each fragment uses the centre and two-ring profiles in Part 3 (50, 25 and 5 percent civilian loss).
The centre becomes a persistent fragment crater and, under Extraordinary Minerals, a mineral site.

### Resolution order

1. Lock every fragment centre.
2. Build every footprint and merge overlaps by strongest profile.
3. Apply each state once, main and fragment alike.
4. Register craters, assign material profiles and record each struck continent once.
5. Add fragment destruction to the Dust Load.
6. Aggregate country reports.
7. Present the main strike, then the fragment visuals one at a time, four hours apart.

### Reports and log

Countries hit only by fragments receive the same single consolidated report.
The impact bulletin and super-event state the fragment count and name each struck continent once.
The evolution writes one global log row (type fragmentation, stage 1, Chaos Tier, no actor).

## Extraordinary Minerals

### Role

Crater material with unusual structural properties strengthens the armour of whoever controls the site.
The disaster leaves permanent military objectives that change front lines and peace terms.
Public text keeps the science uncertain: dense meteoric alloys, fused impact material, unfamiliar crystals.

### Armour benefits

- The current controller of the main crater gains plus 100 percent land-division armour (`armor_factor`) through the main-crater material idea.
- Each directly controlled fragment site adds plus 20 percent through one country dynamic modifier whose value is rebuilt from the controlled-site count.
- Bonuses stack without a cap.

`armor_factor` multiplies existing armour, so divisions with zero armour gain nothing, and piercing, hardness, naval and air values are unchanged.
Ownership, cores, compliance and ideology do not matter; only current control does.

### Transfer and refresh

Every crater control change, annexation, civil-war control change, peace transfer, release and controller disappearance refreshes the affected countries.
The refresh rebuilds each country's main-crater flag and fragment count from the registered site array and replaces stale modifiers instead of stacking copies.
A site with no valid controller grants nothing.

### Strategic objectives

Crater states are objectives through existing mechanisms, not free claims or war goals.

- Crater actions for controllers and rivals (Part 6).
- A war-time AI front strategy and peace desire (Part 7).
- Event Details names the current main-crater controller and each fragment site's controller.

The original design also asked for intelligence reports to countries at war with a crater controller explaining the armour advantage; that is removed as redundant, because the modifier tooltip, Event Details and the reconnaissance action already carry the information.

### Material profiles

Each crater site rolls one persistent material profile when it is registered: dense metallic material, fused silicate composite, or shock-formed crystal and glass, with equal weights.
A stored profile never re-rolls.
Surveying a site reveals it through a named state marker with its own icon and description, and gives a one-use research bonus in a matching field (industry, synthetic resources or electronics).
Once any country has surveyed a site, reconnaissance of that site names its material.
Profiles never change armour or any AI weight; they add a small, replayable research choice without creating separate balance tracks.

### Fragment marker cleanup (proposed)

Status: proposed by the 2026-10-10 audit, not implemented.

A fragment controller currently sees two national surfaces for one bonus: a modifier-free "fragment material" idea and the dynamic modifier that carries the armour.
The idea exists only as a marker for older AI reads, and five further numbered identities are kept only to be removed.
The dynamic modifier should be the single visible fragment surface; AI checks should read the controlled-fragment count or the modifier, and the marker ideas should be retired.
This changes no armour value.

### Log

The evolution writes one global log row (type extraordinary minerals, stage 1, Totalen Chaos, no actor).

## Disable behaviour

- Disabling Global Fragmentation removes fragments from a future strike and makes Extraordinary Minerals unavailable.
- Disabling Extraordinary Minerals keeps fragment damage and dust but grants no armour or mineral-site actions.
- Rebuilding Event Details preserves both toggles.
- Disabling an evolution after it applied follows the shared evolution-toggle policy and does not silently erase a campaign outcome.

## Balance review

The armour values are deliberately large and can only change with user approval.
Review their campaign consequences in these cases:

- one country holds only the main crater;
- one country holds one fragment site;
- one country holds the main crater and three fragment sites;
- one country holds every site at 900 Chaos (plus 220 percent);
- several rivals hold one or two sites each;
- infantry-only armies with zero base armour;
- armoured armies near common piercing thresholds.

A balance concern is evidence for the user, not permission to change the values.
