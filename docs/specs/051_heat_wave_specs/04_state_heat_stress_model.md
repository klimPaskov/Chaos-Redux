# State Heat Stress Model

## Purpose

Local Heat Stress converts global intensity into a state-specific condition. It is the main bridge between the worldwide episode and actual gameplay.

A state can be hot because the climate is exposed, because the population and industry retain heat, because war has destroyed water and transport, because an army is consuming local supply, or because mitigation failed. A state can be safer because it is cool, elevated, well supplied, lightly populated, prepared, or actively protected.

## Public bands

Working bands:

| Internal score | Working band | Typical behavior |
| --- | --- | --- |
| 0 to 19 | Manageable | Minor disruption and local flavour |
| 20 to 39 | Strained | Noticeable water, work, supply, and training pressure |
| 40 to 59 | Dangerous | Strong sector penalties and urgent mitigation targets |
| 60 to 79 | Extreme | Infrastructure failure, harvest loss, army exhaustion, and Evolution I death risk |
| 80 to 100 | Scorched | Severe collapse and Evolution III near-uninhabitable behavior |

The final interface can show an icon, color, band name, and trend without exposing the exact number. Debug and map inspection tools may show exact points.

## Calculation structure

Local Heat Stress should be derived from five internal groups.

### 1. Environmental exposure

- Global Heat Wave Intensity
- regional amplification
- maintained climate and aridity classification
- latitude or climate band
- desert-state registry where applicable
- terrain family
- elevation proxy through mountain or hill terrain
- coastal or inland exposure when supported
- active drought pressure
- prior permanent degradation
- nighttime retention or urban heat condition

### 2. Human and economic load

- state population
- urbanization proxy
- factory and dockyard concentration
- resource extraction concentration
- active construction load
- local military unit and supply load
- refugee or displaced population pressure published by Migration
- trapped population demand published through the humanitarian adapters

### 3. System weakness

- infrastructure damage
- railway and supply disruption
- low local supply
- damaged water or power proxies
- occupation damage and resistance pressure where relevant
- strategic bombing damage
- recent wildfire or other natural disaster damage
- weak controller capacity
- active Famine stage or food insecurity fact

### 4. Mitigation

- national protection priority
- completed local water action
- cooling-center coverage
- army heat protocols
- harvest protection
- railway and power maintenance
- local mission success
- strong infrastructure and supply
- temporary night-shift or shutdown policy
- relief access

### 5. Exposure memory

- consecutive days in Dangerous or higher
- consecutive days in Extreme or higher
- cumulative Extreme exposure for environmental degradation
- recent peak
- recent failed mitigation
- recovery lag

## Baseline score model

A planning formula can use weighted sub-scores:

`stress target = global pressure + environmental exposure + load + weakness - resilience - mitigation`

The live script should not recalculate every component from scratch every day. Stable components such as climate, terrain, and long-term vulnerability can be cached at episode start and refreshed only when a relevant state fact changes.

Dynamic components such as global intensity, regional amplification, supply, military load, Famine stage, and local mitigation should update through bounded pulses.

## Suggested weighting direction

The final weights require live probability and scenario review, but the following ordering should hold.

### Strong positive drivers

- high global intensity
- desert or already degraded terrain
- severe regional amplification
- dense urban or industrial concentration
- damaged infrastructure and low supply
- large army load in a low-capacity state
- active water or food failure
- long uninterrupted exposure

### Moderate positive drivers

- ordinary plains and hills under a severe episode
- high construction and factory load
- port and dockyard concentration
- refugee reception beyond capacity
- recent natural disaster damage
- occupation and disrupted governance

### Strong negative drivers

- mountain or cold-climate protection
- effective local water mission
- successful national priority aligned with the state's dominant risk
- high infrastructure and supply capacity
- early shutdown or night-shift conversion
- successful army rotation
- sustained global decline

### Limited negative drivers

- small population alone
- northern latitude alone
- coastal location alone

No single geographic factor should make a state immune. Evolution III can push normally cool regions into real stress.

## Climate and terrain treatment

### Desert

High base exposure, high water demand, poor recovery, severe military sustainment risk. Desert regions may have existing adaptation, so infrastructure and local preparation should matter more than a simple automatic maximum.

### Plains and farmland

Moderate base exposure with high agricultural sensitivity. Long extreme exposure should damage crops before it converts terrain.

### Forest

Lower initial daytime exposure than open dry land, but drought and wildfire risk can rise sharply. Burned or degraded forest loses protection.

### Jungle

High humidity can increase human heat stress while vegetation retains a different environmental profile. Jungle should not be treated as desert. Supply, disease, and labor consequences can be severe even before drying.

### Hills and mountains

Reduced heat pressure through elevation and cooler conditions. Low infrastructure, isolated water systems, and displaced arrivals can still create local crisis. Mountains should become important cooler destinations without becoming unlimited safe zones.

### Marsh

Humidity and sanitation can worsen human stress. Long drying can transform hydrology, but the state should not jump directly to desert.

### Urban

Urban concentration raises nighttime retention, water demand, hospital load, and power demand. Strong utilities and cooling measures can offset part of this vulnerability.

### Wasteland

Already hostile terrain receives severe logistical and civilian penalties but should not accumulate another identical degradation stage.

## Controller and owner logic

Temporary state effects follow the current controller where they represent operations, water distribution, supply, or emergency management. Permanent population and terrain transactions must use the correct owner and controller rules of the owning system.

When control changes:

- recalculate current mitigation authority
- preserve environmental exposure and permanent degradation
- preserve local physical damage
- retire invalid controller-owned missions
- offer new valid controller actions after a short handover delay
- prevent duplicate action rewards from the old and new controller

## Sparse processing

The event should avoid a whole-world daily scan.

Preferred pattern:

1. Register valid states at setup through a bounded transaction.
2. Split them into stable processing cohorts.
3. Process one cohort per event-owned pulse.
4. Promote urgent states into a small high-frequency queue when they cross Extreme or receive an active mission.
5. Remove states from urgent processing after confirmation of recovery.
6. Rebuild hotspot rankings only after material changes.

The implementation must use an existing repository-approved sparse pattern if one exists.

## Hotspot selection

Each normal country should have up to three player-facing hotspots at once.

Priority score should consider:

- current Heat Stress band
- upward trend
- population exposure
- capital or major city status
- front-line military load
- agricultural importance
- rail, port, resource, or industrial importance
- active Famine or Migration demand
- absence of mitigation

Hotspots should be diverse when possible. A country with one burning capital and two similar neighboring factory states should not necessarily hide a collapsing grain belt.

## State trend

Trend should compare the current score with a smoothed recent score. It should display as rising, stable, or easing.

A state should not show a changing trend because of tiny point noise. Suggested material change threshold: 4 to 6 points or a public band transition.

## Temporary modifiers

State modifiers should be banded and replace one another. Avoid stacking many separate heat penalties.

Each band can combine:

- local supply consumption or throughput
- infrastructure and railway efficiency
- construction speed
- factory and dockyard output
- resource extraction
- population and migration pressure hooks
- military environmental effects through supported unit or terrain paths

Sector-specific local protection can subtract or override selected penalties without creating a second full modifier stack.

## Accumulated exposure

From the beginning of every episode, states should record:

- days at Dangerous or higher
- days at Extreme or higher
- days at Scorched
- longest uninterrupted extreme run
- mitigation-adjusted extreme exposure points

This ledger is hidden. It supports:

- Evolution I death timing
- infrastructure damage timing
- Famine and Migration proof
- Evolution II environmental degradation
- Evolution III wasteland eligibility
- achievements
- recovery burden

Exposure should persist through a short lull within the same episode but decay slowly when the state genuinely cools. It should not reset because the score crossed a threshold for one pulse.

## Failure and recovery hysteresis

Use different thresholds for worsening and recovery. A state should require confirmed improvement before losing a severe band.

Example:

- enter Extreme at 60
- leave Extreme only after falling below 54 for two completed checks

This prevents rapid modifier replacement and unstable decision visibility.

## Special-country routing

Ordinary civilian reports and decisions require `uses_normal_civilian_systems = yes`.

Special but human countries can remain eligible when the shared classifier says they use ordinary civilian systems. Actual nonhuman countries should not receive ordinary civilian water, health, school, livestock, or migration text.

The state stress calculation may still run where needed for map, supply, terrain, and combat consistency. The presentation and response route should follow the country classifier.

## Acceptance examples

### Prepared desert state

High environmental exposure, strong infrastructure, low population, active water protection, and acclimatized army. Expected result: Dangerous during a severe global phase, possibly Extreme during a surge.

### Bombed temperate capital

Moderate climate exposure, high population, damaged infrastructure, weak water service, and high nighttime retention. Expected result: Extreme before the prepared desert state.

### Northern mountain state

Low environmental exposure, small population, functioning supply. Expected result: Manageable or Strained during baseline, Dangerous during Evolution III peaks.

### Jungle front

Moderate environmental score, high humidity, low supply, large army, weak infrastructure. Expected result: high military and health stress without using desert logic.

### Empty remote state

High climate exposure, little population, no industry, and no army. Expected result: environmental stress can be high, but civilian reports and country burdens remain limited.
