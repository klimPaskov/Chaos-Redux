# Event 037 balance matrix

## Purpose

This file shows what the planning anchors in Parts 2 to 4 produce, so implementation can check its constants against the intended feel.
Every value here is a planning anchor held in `common/script_constants/` and tuned against the installed state-population distribution.

The intended feel is a useful baseline, an Evolution I that makes building pay, an Evolution II that strains food in crowded states, and an Evolution III that can break unprepared countries while prepared ones grow stronger.

## Grant examples

The formula and stage table are owned by [Part 2](../specs/037_mysterious_people_spec_part_2_population_and_ledger.md#grant-model).

| Pre-fire population | Baseline | Evolution I | Evolution II | Evolution III |
| ---: | ---: | ---: | ---: | ---: |
| `5,000` | `250` | `500` | `1,000` | `2,000` |
| `20,000` | `1,000` | `2,000` | `4,000` | `8,000` |
| `100,000` | `2,500` | `6,000` | `12,000` | `25,000` |
| `1,000,000` | `25,000` | `60,000` | `120,000` | `250,000` |
| `5,000,000` | `125,000` | `300,000` | `600,000` | `1,250,000` |
| `20,000,000` | `500,000` | `1,200,000` | `2,400,000` | `5,000,000` |
| `60,000,000` | `1,500,000` | `3,000,000` | `7,200,000` | `15,000,000` |
| `100,000,000` | `1,500,000` | `3,000,000` | `7,500,000` | `20,000,000` |

The small-state ceiling keeps the floor from doubling a tiny state, and the cap keeps the largest states from absorbing a disproportionate share.

## Pressure after one firing

For a country whose states are below the cap, start with no backlog, and have average infrastructure:

| Stage | Grant share | National pressure | Stage reached | Months to settle at the plain rate |
| --- | ---: | ---: | --- | ---: |
| Baseline | `2.5%` | `10` | Absorbing | `2.5` |
| Evolution I | `6%` | `24` | Strained | `6` |
| Evolution II | `12%` | `48` | Overcrowded | `12` |
| Evolution III | `25%` | `100` | Breakdown | `25` |

National pressure is `100 x backlog / (population x 0.25)` before the worst-hotspot term (Part 3).
A second firing before the first wave settles stacks on the remaining backlog.

## Settlement speed

| Setup | Monthly settlement (share of state population) |
| --- | ---: |
| Plain rate, infrastructure `5` | `1.0%` |
| Infrastructure `1` | `0.68%` |
| Infrastructure `8` | `1.24%` |
| Open Integration | `1.25%` |
| Open Integration, housing and roads built | `1.875%` |
| The same during a Registration Drive | `2.8%` |
| Restricted Registration, occupied | `0.375%` |

An Evolution III wave in a state with housing, roads, and Open Integration settles in about `13` months instead of `25`.
Emergency Housing settles `30%` of the backlog at once, and a New City settles `50%`.

## Consequence scale

| National pressure | Stability | Construction speed | Workforce bonus |
| ---: | ---: | ---: | --- |
| `10` | `0` | `0` | full |
| `30` | `0` | `0` | half |
| `50` | `-2.5%` | `0` | none |
| `70` | `-7.5%` | `-5%` | none |
| `100` | `-15%` | `-20%` | none |

Restricted Registration halves the stability column.
The workforce bonus reaches its `+10%` construction and `+5%` factory output ceiling when settled newcomers are `25%` of the country.

## Famine and Migration reach

- A hotspot at state pressure `60` submits a food-need component of `20`, worth `8` food-security points, and at `100` it submits `60`, worth `24`.
  Supply strain starts at `25`, so crowding needs another cause, such as war in the state, a blockade, or low stores, to start a famine stage.
- A hotspot at state pressure `80` or more requests flight for `2%` of its backlog each month, so a Breakdown state sheds roughly `0.5%` of its population a month while Migration allows it.
- Famine stages feed back by adding `+10` to `+30` to state pressure and halving settlement, which is the spiral the player prevents with housing, roads, and Famine's own relief.

## Repeat compounding

For an uncapped state with no deaths or movement:

| Stage | After one firing | After two | After three |
| --- | ---: | ---: | ---: |
| Baseline `2.5%` | `102.5%` | `105.1%` | `107.7%` |
| Evolution I `6%` | `106%` | `112.4%` | `119.1%` |
| Evolution II `12%` | `112%` | `125.4%` | `140.5%` |
| Evolution III `25%` | `125%` | `156.3%` | `195.3%` |

The shared repeatable weight controls frequency.
There is no hidden reduction of later grants.

## Exploit controls

- One grant per state per firing, keyed to one firing identity that survives reload.
- The instant recruitable gain is removed, so a firing never hands an army millions of soldiers on the same day.
- Projects are once per state, settle a fraction of the backlog, and fail closed without refunds when the state changes hands.
- The mission rewards one success per manifestation, and Three Censuses counts a success once.
- Pressure that falls through deaths or flight earns no reward, since the mission and achievements require low pressure over time and Room for Everyone forbids famine stages.

## Required balance cases

1. Stable industrial major after a baseline firing.
2. Small island after a baseline firing.
3. Poor agrarian country after an Evolution I firing, with and without housing.
4. Blockaded island hotspot at Evolution II.
5. Major at war during Evolution II, with too few free factories for projects.
6. Prepared Evolution III country with Open Integration, housing, roads, and a New City.
7. Unprepared Evolution III country at Breakdown.
8. Three firings without intervention and three with strong intervention.
9. Ownership transfer of a hotspot with a running project.
10. Newcomer-majority state hit by famine, bombing, and flight.

## Balance acceptance

Baseline gives a clear benefit, Evolution I makes building pay, Evolution II strains food in crowded states, Evolution III can break unprepared countries while rewarding preparation, no transaction duplicates population, and the shared repeatable frequency stays authoritative.
