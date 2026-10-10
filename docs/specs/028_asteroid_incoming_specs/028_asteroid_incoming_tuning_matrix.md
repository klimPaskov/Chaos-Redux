# Asteroid Incoming: Tuning Matrix

The constants file `common/script_constants/028_asteroid_incoming_constants.txt` owns every value; idea modifiers mirror theirs as `@` constants in `common/ideas/028_asteroid_incoming_ideas.txt` because idea fields reject script constants.
This matrix records the implemented value beside the design range it must stay within.
If this file and the constants disagree, the constants are current and this file is stale.

## Change control

These values are explicit user requirements and change only with user approval:

- main centre 100 percent, Ring 1 about 50, Ring 2 about 25, Ring 3 about 5 percent civilian loss;
- fragment centre about 50 percent population and building loss, fragment rings about 25 and 5 percent;
- plus 100 percent main-crater armour, plus 20 percent per fragment site, uncapped stacking;
- 600 and 800 Chaos evolution thresholds.

Every other value can move inside its design range after probability, modifier and scenario review.

## Damage

| Profile | Civilian loss | Industry / logistics / strategic building loss | Range | Local modifier days | Range |
| --- | ---: | --- | --- | ---: | --- |
| Main centre | 100% | 100 / 100 / 100% | Fixed | Permanent | Fixed |
| Ring 1 | 50% | 70 / 80 / 75% | 60-80 / 70-90 / 65-85 | 720 | 540-900 |
| Ring 2 | 25% | 45 / 55 / 50% | 35-55 / 45-65 / 40-60 | 405 | 270-540 |
| Ring 3 | 5% | 15 / 22.5 / 22.5% | 10-20 / 15-30 / 15-30 | 180 | 90-270 |
| Fragment centre | 50% | 50 / 62.5 / 60% | about 50 / 55-70 / 50-70 | Crater persistent, recovery 540 | 360-720 |
| Fragment ring 1 | 25% | 32.5 / 42.5 / 40% | 25-40 / 35-50 / 30-50 | 270 | 180-360 |
| Fragment ring 2 | 5% | 10 / 15 / 15% | 5-15 / 10-20 / 10-20 | 120 | 60-180 |

Building shares round per province for ordinary provincial buildings (Part 3).

## Continuing rescue deaths

| Profile | Monthly share of survivors | Months | Range |
| --- | ---: | ---: | --- |
| Ring 1 | 0.04% | 6 | 0.03-0.05%, up to 6 |
| Ring 2 | 0.02% | 4 | 0.01-0.03%, up to 4 |
| Fragment centre | 0.03% | 6 | 0.02-0.04%, up to 6 |
| Fragment ring 1 | 0.015% | 3 | 0.01-0.02%, up to 3 |

The medical stance multiplies these by 0.5; each month is capped at 25,000 people and never takes a state below 1,000.

## Unit damage

| Profile | Strength / organisation | Ships struck |
| --- | --- | --- |
| Main centre | 75 / 95% | Yes |
| Ring 1 | 45 / 75% | Yes |
| Ring 2 | 25 / 50% | No |
| Ring 3 | 8 / 25% | No |
| Fragment centre | 35 / 65% | No |
| Fragment ring 1 | 20 / 40% | No |
| Fragment ring 2 | 5 / 20% | No |

Each value must fall ring by ring, each fragment profile must stay lighter than its main counterpart, and none may delete a unit.

## Fragments

| Chaos | Planned centres |
| --- | ---: |
| 600-699 | 3 |
| 700-799 | 4 |
| 800-899 | 5 |
| 900+ | 6 |

At least two applied centres are needed for the evolution to apply; the planner reduces the count cleanly when the world lacks separated centres.

## Dust Load

| Contributor | Implemented | Cap |
| --- | --- | ---: |
| Main crater base | 25 | 25 |
| Civilian deaths | 1 per 500,000 | 25 |
| Industry levels destroyed | 1 per 4 | 20 |
| Logistics and strategic levels destroyed | 1 per 6 | 15 |
| Footprint states | 2 / 1.5 / 1 / 0.5 per main profile, 1.5 / 1 / 0.5 per fragment profile | 10 |
| Fragment centres | 3 each, plus their destruction above | 20 |
| Accepted Event 013 secondaries | 2 each, at most 4 | 10 |

The visible load is clamped to 1-100 for a strike and 0 for a near miss.

## Dust stages

| Stage | Load | Factory output | Construction | Efficiency growth | Supply consumption | Air missions | Air weather penalty | Opening Air Cleanliness | Monthly reservoir |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Residual Haze | 1-24 | -3% | -2% | 0% | +2% | -1% | 0 | +50 bp | +1 bp |
| Global Dust Veil | 25-49 | -7% | -5% | -3% | +5% | -3% | 3% | +100 bp | +2 bp |
| Impact Winter | 50-74 | -12% | -10% | -8% | +10% | -5% | 5% | +200 bp | +4 bp |
| Severe Impact Winter | 75-100 | -20% | -15% | -12% | +15% | -10% | 10% | +350 bp | +6 bp |

## Dust decay

- Opening hold: 30 days.
- Monthly decay: 6 (severe), 5 (impact winter), 4 (veil), 3 (residual) points.
- Global mitigation: at most 3 extra points per month (Part 4 proposes earning it only through the Observation Network, half a point per member).
- A severe opening should clear in roughly 16 to 24 months without mitigation; a residual opening within a few months.

## National protection

| Tier | Share of the stage penalty offset | Source |
| --- | ---: | --- |
| Unprepared | 0% | |
| Basic | 15% | Emergency filters |
| Organized | 30% | Transport protection |
| Hardened | 45% | Factory hardening |
| Observation Network | +15% to air and weather only | Joining the network |

The combined offset never exceeds 100 percent of the stage penalty, so protection can never become a bonus.

## Target score

The board's state score uses fixed points (`target_score_*`): base 100, capital 40, victory point 25, large population 30, medium population 15, industry 15, supply 15, railway 10, infrastructure 10, air base 12, naval base 12, per direct land neighbour 10, per reachable state 8, frontline penalty -30, and a 0.6 multiplier below six reachable states.
Design intent: footprint size, population and industry should together outweigh national prestige, and an island should win only when nothing better exists.

## Preparedness

| Stance | Implemented |
| --- | --- |
| Command continuity | Dislocation 100 days instead of 180 after a capital strike, 50 instead of 90 otherwise, with milder penalties |
| Transport dispersal | Keeps 60% of the transport loss (2% of trains, trucks and fuel per main-footprint state held, at most 20%); the first transport response restores 30% |
| Medical command | Local burden durations times 0.75, rescue deaths times 0.5, first mobile hospitals restore 30% |

## Recovery

| Item | Value |
| --- | --- |
| Restore shares | Emergency 20%, reconstruction 35%, industry 25%, network 40%, rehousing 15% |
| Mission durations | Rescue route 150, stabilize 120, network 180, outer ring 270, regional economy 365 days |
| Mission grace window | 45 days |
| Mission repair targets | 60% of pre-impact levels |
| Regional economy target | 75% of pre-impact totals |
| Active mission limit | 2 |
| Failure rescue deaths | 1% (2% in Ring 1 or a fragment centre), at most 25,000 |
| Failure windows | Returned damage 90 days, national burden 90 days, repair surcharge 25% for 180 days |

## Prices

- State quote multiplier: 1.00 plus 0.01 per profile point plus 0.0005 per thousand people lost (at most 0.50), times 1.25 under a surcharge, clamped to 1.00-2.50.
- Dust project multiplier by stage: 1.00, 1.25, 1.50, 1.75.
- Reserve floors: 1,000 manpower, 100 support equipment, 100 trucks, 2 trains, 500 fuel, 20 convoys, 10 command power.

## Crater actions

| Item | Value |
| --- | --- |
| Perimeter security | +10% defence, -10% attrition at the site |
| Survey | One research bonus of 20% in the profile's field |
| Access fortification | Up to 2 states, +1 infrastructure (cap 5) and +1 fort per province (cap 10) |
| Reconnaissance | +5 army intelligence |
| Route disruption | -20% local supplies for the enemy controller, 90 days |
| Offensive plan | +10% attack into the crater state, 90 days |

## Mineral stacking

| Controlled sites | Armour factor |
| --- | ---: |
| One fragment | +20% |
| Three fragments | +60% |
| Main crater | +100% |
| Main plus three fragments | +160% |
| Main plus six fragments | +220% |

## Opening AI headline weights

Near miss base 1,000 (+500 democratic, +250 at peace, +250 stable, +400 fragmentation, +300 crater holder; ×0.35 desperate, ×0.65 fascist at war, ×0.75 high Chaos).
Strike base 1 (+400 enemy, +150 major, +200 faction leader, +200 capital, +75 logistics; ×2 fascist, ×3 desperate, ×1.25 high Chaos, ×0.25 democratic, ×0.75 fragmentation, ×0.5 crater holder, ×0.25 target near capitulation, ×0.25 friendly ground, ×0 protected).
The full set is in `asteroid_incoming_ai`; any change needs the probability comparison in the AI prompt.
