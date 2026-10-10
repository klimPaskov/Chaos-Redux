# Event 037: Mysterious People

## Part 3: Overpopulation Pressure and evolutions

## Overpopulation Pressure

Overpopulation Pressure is the one national value the player manages.
It measures how many newcomers are still unsettled compared with the country's population, worsened where people are already hungry.
The scale runs from `0` to `100`.

| Range | Stage | What it means for the player |
| --- | --- | --- |
| `0` to below `20` | Absorbing | Settled newcomers give the full workforce bonus. |
| `20` to below `40` | Strained | The workforce bonus is halved. Housing and roads pay off here. |
| `40` to below `60` | Overcrowded | No workforce bonus, and stability starts to fall. |
| `60` to below `80` | Emergency | Stability and construction suffer, and crowded hotspots press on Famine. |
| `80` to `100` | Breakdown | The worst hotspots also send people into flight through Migration. |

### State pressure

```text
state pressure = clamp(100 x unsettled newcomers / (state population x 0.25), 0, 100)
                 + famine stage addition, clamped to 100
```

The famine stage addition is `+10` at acute shortage, `+20` at famine, and `+30` at catastrophic famine, read from the Famine owner's committed stage.
The `0.25` scale means a backlog equal to a quarter of the population is full Breakdown.

### National pressure

```text
national base = clamp(100 x country unsettled newcomers / (country population x 0.25), 0, 100)
national pressure = national base + 0.25 x (worst hotspot pressure - national base), when that gap is positive
```

The national base is a population-weighted average, so one tiny state in Breakdown cannot drive a large country to Breakdown alone.
The worst-hotspot term keeps a crowded capital or industrial heartland visible.

All scales, additions, and weights are planning anchors in `common/script_constants/`.
The [balance matrix](../quality/037_mysterious_people_balance_matrix.md) shows the stages each manifestation produces.

## What the player sees

The decision category header shows three things: the newcomers living in the country, Overpopulation Pressure with its stage, and the current stance.
The pressure tooltip adds the unsettled newcomers and the single largest hotspot.

A hotspot's tooltip shows its newcomers, its unsettled newcomers, its pressure stage, and the main thing slowing settlement there (occupation, hunger, or poor infrastructure).

Everything else stays internal: settlement rates, fixed-point shares, the hotspot ranking, adapter receipts, and milestone flags.
When pressure falls because people died or fled rather than settled, the hotspot tooltip names hunger or flight as the cause, so a death toll never reads as a project success.

## Consequences

One country dynamic modifier, **Newcomers**, carries every national effect.
Its values come from variables, so it never stacks per firing or per stage.

| Effect | Rule (planning anchors) |
| --- | --- |
| Workforce bonus | Construction speed `+0.4 x settled share` up to `+10%`, factory output `+0.2 x settled share` up to `+5%`. Full at Absorbing, half at Strained, none from Overcrowded. |
| Unrest | Stability `-0.25%` per pressure point above `40`, up to `-15%`. Restricted Registration halves it. |
| Overloaded building trades | Construction speed `-0.5%` per pressure point above `60`, up to `-20%`. |

"Settled share" is settled newcomers divided by country population.
Recruits need no modifier because the newcomers are real population and become recruitable through the engine (Part 2).

### Famine connection

From the monthly pulse, each hotspot at state pressure `60` or more submits one food-need component to Famine through `famine_apply_pressure_request`.
The component equals state pressure minus `40`, so it runs from `20` to `60`, and it is refreshed or dropped each pulse.
Famine decides whether that need, together with its own war, stores, blockade, and relief inputs, produces a stage.
On its own an Emergency hotspot adds between `8` and `24` food-security points, below the supply-strain threshold of `25`, so crowding alone strains food only together with another cause.

The request uses a dedicated pressure source constant (planned `population_surge` in `humanitarian_pressure_source`) so the Famine report can name crowding as a cause.
Event 037 never creates a food value, a famine decision, or a famine death.

### Migration connection

From the monthly pulse, each hotspot at state pressure `80` or more requests flight pressure through `migration_request_flight_pressure` for `2%` of its unsettled newcomers.
Migration decides whether people actually leave, where they go, and whether the border traps them.
When the civilian transfer primitive applies a departure, its Event 037 hook removes the measured departures from the origin's unsettled backlog and blends the destination's newcomer share (Part 2).
Arrivals become the destination's Migration reception load, not Event 037 pressure.

Breakdown therefore relieves itself through flight, at the cost of neighbours and Migration load.
The player can keep people at home with Migration's own departure and border controls, which leaves the pressure in place.

## Evolutions

Event 037 has three evolutions.
Each one raises the grant scale of every later manifestation (Part 2), which pushes countries into the next pressure band unless they have built settlement capacity.

Activation follows the shared evolution system: eligibility from Chaos and event history, paced timing, logging in the shared evolution log, zero Chaos, and disabled stages that never record or unlock anything.
A higher enabled evolution includes the grant scale and unlocks it needs when a lower stage is disabled.

| Evolution | Eligibility | Base timing | What changes for the player |
| --- | --- | --- | --- |
| I: Population Surge | Chaos `200+`, at least one firing | about `90` days | Grants of `6%` reach Strained and make housing and roads worth building. |
| II: Overpopulation Crisis | Chaos `400+`, at least one firing | about `120` days | Grants of `12%` reach Overcrowded and push hotspots into Emergency and the Famine connection. |
| III: Humanity Multiplies | Chaos `600+`, at least one firing | about `150` days | Grants of `25%` reach Breakdown, Build a New City unlocks, and origin politics appear (Part 5). |

Timing uses the MTTH workflow.
Each eligible evolution is faster (`x 0.75`) when any country is at Emergency or worse, and again (`x 0.75`) when living newcomers exceed `5%` of world population for Evolution II or `10%` for Evolution III.
It is slower (`x 1.5`) when no country is above Strained.

Each activation sends one short report to human players (`chaosx.nr37.3` to `chaosx.nr37.5`) describing the next manifestation's scale through people and places, without tier language.

### First firing after evolution thresholds

If Event 037 first fires when Chaos already exceeds an evolution threshold, the first manifestation uses the highest enabled eligible stage.
Enabled stages record in order immediately before the manifestation, disabled stages stay unrecorded, and activation still adds no Chaos.

## Recovery

Evolutions never reverse.
Pressure recovers fully as newcomers settle, and a country can move from Breakdown to Absorbing through projects, stance, and time.
Completed projects keep their settlement bonus and their buildings.
The settled newcomers stay, and so does the workforce bonus once pressure is low again.

## Evolution acceptance statement

Each evolution must change future manifestations and the player's choices.
Evolution I makes building pay, Evolution II connects crowding to hunger, and Evolution III makes national collapse possible while offering new cities as the constructive answer.
Flags, logs, and thresholds alone do not satisfy the design.
