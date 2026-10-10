# Event 037: Mysterious People

## Part 4: Decisions, mission, and AI

## Purpose

The decision category answers three questions quickly: how bad is pressure, which states are worst, and what will settle people fastest.
Every action changes the settlement of real people.
Food, movement, borders, camps, and relief stay in the Famine, Migration, and camp categories, and Event 037 adds no copy of them.

## Category

One ordinary decision category with a static picture, a category icon, and the three-value header from [Part 3](037_mysterious_people_spec_part_3_pressure_and_evolutions.md#what-the-player-sees).
It does not use a dedicated scripted GUI.

The category appears after the first manifestation for every country with newcomers and hides when the country has no unsettled newcomers, no running project, and no active mission.

State actions target the country's hotspots through the established selected-state pattern: the category lists up to `8` hotspots, the player selects one, its actions appear, and a clear action returns to the national view.
AI evaluates every hotspot directly without the selector.
Projects require the state to be owned and controlled by the country.

## Stance

Each country chooses one stance once newcomers arrive.
Choosing costs `50` political power, and the stance is locked for `180` days.
Until a stance is chosen, settlement runs at the plain rate.

| Stance | Settlement | Other effect | Why choose it |
| --- | --- | --- | --- |
| Open Integration | `x 1.25` | Full stability penalty from pressure | Pressure falls fastest and the workforce bonus returns sooner. |
| Restricted Registration | `x 0.75` | Stability penalty from pressure halved | Calm now, at the cost of a longer crisis. Adopting the origin register in Part 5 also switches a country to it. |

## Actions

| Action | Target and availability | Cost (planning anchors) | Result |
| --- | --- | --- | --- |
| Registration Drive | National, pressure Strained or higher, `180`-day cooldown | Political power `30` to `90`, scaled by unsettled newcomers | Settlement `x 1.5` in every state for `60` days |
| Requisition Empty Property | Hotspot, state pressure Overcrowded or higher, once per state per year | Stability `-2%` for `90` days | Settles `20%` of the state's unsettled newcomers at once |
| Build Emergency Housing | Hotspot, state pressure Strained or higher, once per state | `2` to `6` civilian factories for `90` days and `25` political power | Settles `30%` of the state's unsettled newcomers on completion and adds the housing bonus |
| Extend Roads and Water | Hotspot, state pressure Strained or higher, once per state | `3` to `8` civilian factories for `150` days and `25` political power | `+1` infrastructure and the roads bonus on completion |
| Build a New City | Hotspot with at least `1,000,000` people, Evolution III, once per state | `8` to `15` civilian factories for `300` days and `100` political power | Settles `50%` of the state's unsettled newcomers, adds the city bonus, `+1` infrastructure, `+1` civilian factory, and `+1` shared building slot |

Civilian-factory commitment uses the vanilla timed-decision `civilian_factory_use` modifier, scaled by the state's unsettled newcomers between the listed bounds.
Each action uses at most two spendable cost types, and every displayed cost has its texticon.
A country can run at most `3` state projects at once, and a state runs one project at a time.
Settlement bonuses are defined in [Part 2](037_mysterious_people_spec_part_2_population_and_ledger.md#settlement).

A project fails closed when its state changes owner or controller before completion: the factories are released, the political power is not refunded, and nobody is settled or removed.

Housing and roads are the core choice.
Housing settles people now, roads settle them faster forever and leave a building behind.
Requisition is the cheap emergency lever with a political price, and the drive is the option for a country without spare factories.

## Mission: Absorb the Newcomers

The only Event 037 mission.
It starts after a manifestation that leaves national pressure at Strained or higher, and at most one runs at a time.

- Duration: `180` days.
- Goal: bring national pressure below the lower bound of the stage it started in.
- It completes as soon as the goal is met.
- Success doubles the workforce bonus for `180` days, applied after the stage rule, and counts toward Three Censuses (Part 7).
- Failure costs `5%` stability for `90` days.

## Visibility budget

At any time the category shows the header, the stance choice while unlocked, at most one national action, the hotspot list, at most four actions for the selected hotspot, and at most one mission.
Completed, invalid, and locked actions hide instead of listing blocked rows.

## AI

All AI uses the same availability and cost gates as the player.

### Stance

- Democracies, and countries with stability above `60%`, prefer Open Integration.
- Fascist governments, and countries with stability below `40%` while at Overcrowded or worse, prefer Restricted Registration.
- Other countries weigh the two by stability, with Open Integration ahead at equal conditions.

### Actions

- Projects are weighted by the target hotspot's pressure and population, so a crowded capital or industrial state comes first.
- Roads and Water leads when the hotspot's infrastructure is below `5`, and Emergency Housing leads otherwise.
- A country at war with fewer than `10` free civilian factories delays projects and uses the Registration Drive and Requisition instead.
- Build a New City is chosen only by countries with at least `25` civilian factories.
- Requisition is avoided above `50%` stability and favoured at Emergency or worse.

Weighted AI follows the named scenarios in the [probability scenarios](../quality/037_mysterious_people_probability_scenarios.md).

## Cleanup

Selections clear when the hotspot leaves the list, projects fail closed on owner or controller change, the mission ends when the country has no unsettled newcomers, and the stance persists with the country.
A country that stops using normal civilian systems loses the category, its running projects fail closed, and its states keep their ledger values.
