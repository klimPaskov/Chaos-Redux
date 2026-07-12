# Event 018 Tuning and Balance Framework

This file defines design ranges and relationships. It does not prescribe final Clausewitz syntax. Shared values should be centralized in script constants or documented tuning helpers during implementation.

## Fixed design rules

| Rule | Value |
| --- | --- |
| Baseline resource deposit | Centered on 100 units |
| Baseline practical random band | Roughly 80 to 120 before contextual scaling |
| Standard resource pool | Oil, aluminium, rubber, tungsten, steel, chromium |
| Cave starting army minimum direction | About 6 divisions |
| Cave starting army hard cap | 30 divisions |
| Captured-state capacity ratio | 1 division per 10 total strategic resources |
| Captured-state capacity cap | 10 divisions per state |
| Origin-state future capacity | 0, because the opening allocation already represents it |
| Anchor activation baseline | About 30 days of continuous control |
| World-end chaos gate | Above 1000 |
| Evolution stage count | Four stages, one per enabled evolution tier |

## Resource deposit packages

| Opening or result | Suggested number of rolls | Amount per roll | Special rule |
| --- | --- | --- | --- |
| Baseline first discovery | 1 | 80 to 120, target 100 | Completely random resource |
| Baseline repeat enrichment | 1 | 80 to 120 | Duplicate type stacks |
| Survey breakthrough | 0 or 1 | 40 to 100 | Can improve yield instead of adding a full roll |
| Evolution I pre-fire | 2 to 4 | 80 to 120 each | All rolls in same state |
| Evolution I active | 1 to 3 | 80 to 120 each | Scales with discovery history and depth |
| Evolution II pre-fire | 3 to 5 | 90 to 140 each | Accelerated incident clock begins after development |
| Evolution II active | 1 to 3 | 90 to 140 each | Higher depth and disturbance growth |
| Evolution III pre-fire | One deposit for every standard resource | Large amount per type, suggested 120 to 200 | Global trade-changing all-resource field |
| Evolution III active | Fill missing types plus large enrichment | 100 to 200 per affected type | Avoid exceeding safe engine display or balance limits |

The all-resource opening should be absurdly valuable. Balance comes from the public crisis, closure sacrifice, foreign pressure, and possible cave emergence rather than timid resource amounts.

## Field value scales

All visible values should display as integers. A 0 to 100 scale is recommended for player comprehension. Final thresholds can use other internal ranges if the UI stays clear.

### Developed Yield

| Band | Range direction | Gameplay meaning |
| --- | --- | --- |
| Dormant | 0 to 19 | Deposit exists, little usable infrastructure |
| Surveyed | 20 to 39 | Appraisal complete, limited extraction |
| Operating | 40 to 59 | Reliable field with core works |
| Industrial | 60 to 79 | Major processing and transport network |
| Maximum Extraction | 80 to 100 | Extreme output, highest strategic attention |

Typical changes:

- appraisal success: +5 to +12
- primary works: +15 to +25
- rail or processing project: +8 to +18
- heavy machinery: +8 to +15
- maximum shifts: temporary +10 to +20 effective yield
- suspension: effective yield falls to 0 to 20 without deleting reserve
- occupation or sabotage: -5 to -25 depending on damage

### Excavation Depth

| Band | Range direction | Gameplay meaning |
| --- | --- | --- |
| Surface Works | 0 to 19 | Shallow pits, wells, and access roads |
| Primary Shafts | 20 to 39 | Normal industrial depth |
| Deep Galleries | 40 to 59 | Large lower workings and strong Evolution II exposure |
| Lower Strata | 60 to 79 | Severe disturbance and closure difficulty |
| Extreme Depth | 80 to 100 | Maximum Evolution III and IV pressure |

Typical changes:

- deeper test: +8 to +15
- new deposit roll in same field: +3 to +10
- primary works: +5 to +10
- maximum shifts: +1 to +3 per monthly pulse
- heavy blasting or military survey: +5 to +15
- suspension: no growth and slow reduction
- seal one network: -5 to -15
- partial closure: -20 to -40
- full closure: ends field

### Workforce Safety

| Band | Range direction | Gameplay meaning |
| --- | --- | --- |
| Catastrophic | 0 to 19 | Recurring deaths and failed control |
| Dangerous | 20 to 39 | Serious accident and sickness risk |
| Strained | 40 to 59 | Workable but vulnerable |
| Managed | 60 to 79 | Strong ordinary protection |
| Protected | 80 to 100 | Best available protection and early detection |

Typical changes:

- shaft reinforcement: +10 to +20
- hospital and inspection office: +8 to +15
- worker settlement: +5 to +10
- shorter shifts: +8 to +15 during effect
- maximum shifts: -5 to -15
- labor rush: -3 to -10
- sabotage or combat damage: -5 to -20
- concealment: no true safety gain and can apply hidden worsening

Safety should materially reduce deaths and slow evolution. It cannot guarantee that a site at extreme depth remains harmless.

### Foreign Pressure

| Band | Range direction | Gameplay meaning |
| --- | --- | --- |
| Curiosity | 0 to 19 | Flavor and normal trade interest |
| Commercial Interest | 20 to 39 | Buyers and investors become active |
| Strategic Competition | 40 to 59 | Rival bids, espionage, smuggling |
| Coercive Pressure | 60 to 79 | Guarantees, claims, nationalization disputes |
| Crisis | 80 to 100 | Commission, demilitarization, or border conflict |

Typical changes:

- large new deposit: +5 to +15
- each additional resource type: +3 to +8
- exclusive concession: +5 to +15 from rivals, lower from partner
- stable diversified contract: -5 to -10
- smuggling exposure: +5 to +12
- nationalization without settlement: +10 to +25
- fair compensation: -10 to -20
- functioning commission: gradual reduction toward managed band
- active border incident: +10 to +20
- public creature crisis: pressure can convert from resource competition to security concern

### Subsurface Disturbance

This value becomes visible in Evolution II.

| Band | Range direction | Gameplay meaning |
| --- | --- | --- |
| Trace | 0 to 19 | Rare anomalies, no confirmed pattern |
| Responsive | 20 to 39 | Repeated knocks, corrosion, animal behavior |
| Agitated | 40 to 59 | Missing workers and physical evidence |
| Hostile | 60 to 79 | Organized attacks inside workings |
| Violent | 80 to 100 | Evolution III exposure and open access routes |

Typical changes:

- deep-work monthly pulse: +1 to +4
- maximum extraction: additional +1 to +3
- new deposit roll: +3 to +10
- failed underground sweep: +5 to +15
- concealment with continued work: +3 to +8
- restricted workings: -1 to -3 per pulse
- suspension: -2 to -5 per pulse to a depth-dependent floor
- seal deep gallery: -8 to -20

### Breach Pressure

This value becomes visible in Evolution III.

| Band | Range direction | Gameplay meaning |
| --- | --- | --- |
| Contained | 0 to 19 | Surface exits controlled |
| Perimeter Strain | 20 to 39 | Packs testing guards and routes |
| Open Routes | 40 to 59 | Settlement and transport attacks |
| Urban Threat | 60 to 79 | City intrusion and mass evacuation |
| Final Breach | 80 to 100 | Evolution IV timing window |

Typical changes:

- active extraction pulse: +1 to +4
- surface attack success: +5 to +12
- failed hunt: +5 to +15
- transport collapse: +3 to +10
- public panic and abandoned perimeter: +3 to +8
- successful hunt: -5 to -15
- seal access network: -8 to -20
- evacuation: lowers death scaling more than pressure itself
- partial closure: -20 to -40
- full closure: ends field and blocks Evolution IV

## Evolution timing

| Evolution | Base active MTTH direction | Faster when | Slower when |
| --- | --- | --- | --- |
| Evolution I | 90 to 180 days after qualifying development | Repeat discoveries, high yield, high chaos | Suspension, low development |
| Evolution II | About 90 days after qualifying depth | Extreme depth, poor safety, maximum shifts | High safety, restricted work, inspection |
| Evolution III | About 90 days after hostile disturbance | Continued extraction, deaths, failed containment | Sealed galleries, suspension, successful sweeps |
| Evolution IV | 60 to 180 days after final-breach conditions, with protected public-crisis minimum | Critical breach, failed full seal, maximum exploitation | Active full seal, low breach, successful hunts |

A first firing at Evolution III or IV should use a compressed chain, but still preserve at least several incidents and a real closure window.

## Accident and death scaling

Death results should use the shared Deaths system and real state population.

A conceptual death-pressure model should combine:

- exposed workforce band
- Workforce Safety inverse
- Disturbance or Breach Pressure
- active extraction mode
- incident severity
- evacuation status
- state population floor and cap

Design direction:

- ordinary baseline accidents are painful but limited
- Evolution II recurring losses become noticeable over months
- Evolution III public attacks can cause severe state population loss
- a failed city evacuation can produce a major single spike
- careful safety and evacuation must visibly reduce deaths
- no event should remove more population than the state can safely support under the shared system

## Project cost bands

Costs should scale by country size and field value. These are composition directions, not fixed universal prices.

| Project class | Typical commitment |
| --- | --- |
| Small inspection | 1 to 2 civilian factories or equivalent burden, small equipment, 30 to 90 days |
| Medium field project | 2 to 5 civilian factories, trucks or support equipment, 90 to 180 days |
| Major transport or processing project | 4 to 10 civilian factories, trains, trucks, fuel, 180 to 360 days |
| Compound-field corridor | 6 to 15 civilian factories, rail and equipment, 240 to 480 days |
| Partial closure | 4 to 10 civilian factories, engineers, evacuation, 180 to 300 days |
| Full Evolution III sealing | 8 to 20 civilian factories where available, major equipment and transport, 240 to 540 days |
| Emergency seal | Large immediate equipment and organization sacrifice, 45 to 90 days |

Small countries need scaled alternatives through longer duration, foreign aid, or phased construction. The system should not make full closure impossible solely because a country lacks major-power industry.

## Starting cave-army model

The implemented score is centralized in `resources_found_strength` and `resources_found_strength_factor`, with calculation owned by `resources_found_calculate_cave_starting_strength`.

The score is clamped to `0..120`. Starting divisions are `6 + floor(score / 5)`, hard-capped at 30. The unavoidable direct Evolution III package is normalized by subtracting its 720-resource floor before resource tonnage is scored.

### Positive score contributors

| Contributor | Implemented score |
| --- | ---: |
| Event 018 resource tonnage above the 720-resource package floor | `(resources - 720) / 100 * 0.50` |
| Each distinct standard resource | `0.25` |
| Each discovery after the first | `2.50` |
| Maximum Developed Yield reached | `yield * 0.25` |
| Maximum Excavation Depth reached | `depth * 0.25` |
| Each recorded 30-day maximum-extraction month, capped at 18 months | `1.25` |
| Event 018 field deaths | `deaths / 10000 * 2.00` |
| Failed full seal | `12.00` |
| Military exploitation during Evolution III | `14.00` |
| Unsealed surface nest at breach | `5.00` |

### Negative score contributors

| Contributor | Implemented reduction |
| --- | ---: |
| Workforce Safety above 40 | `(safety - 40) * 0.20` |
| Successful evacuation | `8.00` |
| Sealed access network | `7.00` |
| Each 90 days of completed or live suspension, capped at three periods | `4.00` |
| Each successful hunt, capped at four | `2.50` |

Maximum-extraction and suspension durations include completed intervals plus a still-live interval at breach. Starting strength is calculated once, persisted on the origin and DHO, and never recalculated from later captured states.

### Mapping score to divisions

| Score | Opening divisions | Exploitation profile |
| --- | ---: | --- |
| `0` to below `25` | 6 to 10 | Minimal qualifying breach |
| `25` to below `65` | 11 to 18 | Developed or dangerous field |
| `65` to below `95` | 19 to 24 | Heavily exploited field |
| `95` to below `120` | 25 to 29 | Extreme, repeated, or military exploitation |
| `120` after the clamp | 30 | Capped extreme |

The deterministic regression fixture is: direct package low/high `8/8`, protected breach `6`, developed `15`, dangerous developed `18`, heavy `20`, rich unmitigated `21`, failed-seal heavy `23`, mitigated rich history `13`, extreme military `26`, extreme repeated `28`, and capped extreme `30`.

## Cave division balance

The base division should be a major threat to ordinary infantry.

### Intended strengths

- armor high enough that unprepared infantry usually cannot pierce
- hardness high enough to reduce soft-attack effectiveness
- strong defense
- useful breakthrough
- no manpower or equipment reinforcement burden
- good recovery in active anchors

### Intended weaknesses

- severe speed penalty
- poor strategic redeployment
- weak recovery away from anchors
- vulnerable to high hard attack and piercing
- vulnerable to encirclement and resource denial
- no air force and limited anti-air until adaptation
- no navy before world end
- spawn pacing limits replacement

### Practical validation

Test against:

- 1936 infantry with no anti-tank
- infantry with support anti-tank
- dedicated anti-tank divisions
- medium armor with high piercing
- heavy armor or tank destroyers
- air-supported defense
- low-supply fronts
- mountain and urban terrain

The cave units should crush unprepared infantry, fight prepared combined arms seriously, and lose when isolated and pierced by concentrated hard attack.

## Captured capacity validation

| State total resources | Capacity result |
| --- | --- |
| 0 | 0 |
| 9 | 0 |
| 10 | 1 |
| 19 | 1 |
| 20 | 2 |
| 48 | 4 |
| 99 | 9 |
| 100 | 10 |
| 150 | 10 |
| Origin state at any value | 0 future capacity |

## Spawn pacing

Suggested ordinary cadence:

- one division every 20 to 45 days depending on focus, active anchors, and world state
- minimum interval to prevent instant army creation
- replacement divisions use the same queue
- several active anchors can shorten interval but not below the minimum
- world-end transformation can use a faster 10 to 25 day band

The queue should show current capacity, active divisions, protected origin allocation, excess, and next spawn.

## Capacity loss timing

Suggested sequence:

1. State lost or anchor disrupted.
2. A grace period of 15 to 30 days begins.
3. If not recaptured, capacity is removed.
4. Excess divisions receive Unfed Broods.
5. Penalties worsen over 30 to 90 days if no capacity returns.
6. Destroyed or consolidated excess formations reduce the mismatch.

This avoids disappearing units and prevents permanent full strength without anchors.

## Border-crisis tuning

Border war should require several independent conditions.

Recommended minimum design gates:

- valid claim or dispute
- Foreign Pressure at Coercive or Crisis band
- field value above ordinary baseline importance
- failed or rejected negotiation stage
- military strength ratio within a viable range
- local supply and adjacency
- no functioning commission

A claimant more than roughly three times weaker should normally avoid escalation without a strong guarantor or desperate route. Exact ratios should be dynamic and tested.

## World-end verification

| Condition | Design value |
| --- | --- |
| Chaos | Greater than 1000 |
| Continent control | All eligible states owned and controlled |
| Verification period | 30 to 90 days depending on front activity |
| World-end flag | Must be absent before trigger |
| Cave country | Must exist and remain valid |
| Final footholds | At least one valid resource-rich state per selected new continent |

## Cross-continent foothold tuning

| Factor | Effect |
| --- | --- |
| Number of remaining inhabited continents | Increases foothold count |
| Very large continent | Can receive more than one foothold |
| High resource total | Raises state selection weight and opening strength |
| High chaos above 1000 | Increases strength within cap |
| Cave hierarchy and doctrine completion | Changes template mix and coordination |
| Remaining world strength | Can increase or reduce opening strength to preserve a serious end-state campaign |

The world-end route is allowed to be deliberately overpowered. It should still avoid deleting entire countries without a playable response.

## Anti-exploit invariants

- Event-owned resource amounts never become negative.
- Closure subtracts no more than the field ledger records.
- A state can have only one active Event 018 field record.
- A field can have only one exclusive concession partner.
- Repeat enrichment increments the same field rather than duplicating initialization.
- The origin state never enters future capacity.
- State capacity never exceeds 10.
- Capacity requires continuous control.
- One destroyed cave division frees only one capacity slot.
- World end fires once.
- Permanently closed fields never re-enter selection.
- Successful Evolution III full closure always prevents Evolution IV for that field.
