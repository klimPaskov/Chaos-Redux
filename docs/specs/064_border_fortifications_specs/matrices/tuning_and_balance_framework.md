# Event 064 Tuning and Balance Framework

This file collects starting anchors in one place. Final values should live in centralized script constants or another documented tuning surface. Do not scatter magic numbers across events, decisions, AI blocks, achievements, and cluster code.

All numbers are starting values for implementation testing.

## Fort-level framework

| Active package | Ordinary direct frontier cap | Strategic or selected-sector cap | Depth cap | Internal redoubt cap | Maximum land-fort gain in one wave |
| --- | ---: | ---: | ---: | ---: | ---: |
| Baseline only | 3 | not used | not used | not used | 1 |
| Defense in Depth | 4 | 5 | 2 | not used | 2 on direct anchor, 1 elsewhere |
| Fortress States | 6 | 7 | 3 | not used | 2 on resolved direct strategic role, 1 elsewhere |
| Fortress World | 7 | 8 | 4 | 3 | 2 on resolved direct strategic role, 1 elsewhere |

Rules:

- Existing levels above a cap remain unchanged.
- The event adds levels up to a cap. It never sets every candidate to the cap in one wave.
- One direct frontier province receives one baseline level and at most one evolved bonus in a wave.
- One depth or internal redoubt position receives at most one land-fort level in a wave.
- A player project can add one further bounded package after the automatic wave, under project and wave-use limits.
- Level ten remains outside automatic Event 064 design.

## Support-building framework

| Building or network | Automatic Evolution II cap | Evolution III cap where relevant | Automatic gain per selected state per wave | Player-project allowance |
| --- | ---: | ---: | ---: | --- |
| State anti-air | 3 | 3 | 1 when role score qualifies | 1 through air-defense project below cap |
| Radar | 2 | 3 | 1 when warning role qualifies | 1 through air or coastal project below cap |
| Coastal fort | 3 | 3 | 1 at selected port or bounded approach | 1 through coastal project below cap |
| Infrastructure | current engine maximum, project should usually stop below full saturation | same | 1 or repair equivalent | 1 or repair equivalent through logistics project |
| Railway | verified current network cap | same | one bounded verified improvement | one bounded verified improvement through logistics project |
| Supply hub | exceptional only | exceptional only | normally 0 | only after separate targeting and balance proof |

Automatic package rule:

- one supply-related automatic change per selected Fortress State per wave
- normally two or three package components per selected state
- one component is acceptable when the state has few valid slots
- no state receives every support building only because it was selected

## Candidate quota framework

| Candidate family | Formula anchor | Minimum | Hard cap | Diversity rule |
| --- | --- | ---: | ---: | --- |
| Frontier anchors | about one per six direct frontier provinces | 1 | 12 | distinct border states and regions before repetition |
| Depth positions | about one per eight direct frontier provinces | 1 | 10 | no random interior filler, distinct approaches preferred |
| Fortress States | about 30 percent of border states | 1 | 6 | current hostile and strategic fronts first, geographic spread required |
| Coastal defense states | up to half of selected coastal Fortress States | 1 when valid threatened coast exists | 3 | important ports and landing approaches first |
| Internal redoubts | size bands plus one for a major | 1 when valid | 6 | capital first, then supply, VP, industry, port, strategic site, regional spread |

### Internal redoubt size bands

| Controlled state count | Base redoubt quota |
| ---: | ---: |
| 1 to 5 | 1 |
| 6 to 15 | 2 |
| 16 to 30 | 3 |
| 31 or more | 4 |
| Major status | add 1 |
| Final hard cap | 6 |

A country receives fewer positions when valid candidates do not exist.

## Strategic score framework

Use score bands with clear dominance rules. Avoid one giant additive list.

### Dominant factors

These should normally place a candidate in the top band:

- capital under direct land threat
- active enemy frontier leading to capital
- major supply hub supporting an active front
- narrow corridor whose loss divides controlled territory
- major strategic site under real hostile pressure

### Strong factors

- major victory point
- high-value industrial border state
- mountain or hill pass
- major river crossing approach
- important port on a coastal border
- severe enemy air pressure on a strategic state
- new frontier created since the last wave

### Supporting factors

- moderate industry
- airbase
- railway junction
- allied or neutral frontier with high geographic value
- missing anti-air or radar coverage
- current cluster context

### Penalties

- already at cap
- selected in the immediately prior wave when equivalent untouched choices exist
- overconcentration in one state or region
- no meaningful objective or route
- likely imminent loss without a capital-survival reason
- invalid map slot

Dominant conditions need floors so small random variation cannot demote them below trivial candidates.

## Wave frequency framework

| Timing item | Starting anchor | Purpose |
| --- | ---: | --- |
| Natural Event 064 cooldown | about 365 days | prevent rapid global scans and early cap saturation |
| Exact duplicate or active-incident guard | at least 30 days plus active token | block same cluster or manual incident duplication |
| Response posture duration | 180 days | keep one meaningful post-wave policy window |
| Direct repeat Chaos cooldown | about 365 days | prevent farming from repeat waves |
| Last-wave state memory | one Event 064 wave | encourage new strategic targets without permanent bookkeeping |

Tune the natural cooldown with the shared repeatable weight lifecycle. The cooldown must not make repeatability meaningless.

## Automatic wave scale examples

| Country example | Direct frontier provinces | Border states | Anchor quota | Depth quota | Fortress State quota | Redoubt quota at Evolution III |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| one-state minor | 1 to 4 | 1 | 1 | 1 when valid | 1 | 1 |
| small regional country | 5 to 12 | 2 to 4 | 1 to 2 | 1 to 2 | 1 | 1 to 2 |
| medium continental country | 13 to 30 | 5 to 10 | 3 to 5 | 2 to 4 | 2 to 3 | 2 to 3 |
| large continental major | 31 to 70 | 11 to 20 | 6 to 10 | 4 to 8 | 4 to 6 | 4 to 5 |
| very large empire | more than 70 | more than 20 | capped at 12 | capped at 10 | capped at 6 | capped at 6 |

These examples illustrate bounded sublinear growth. They are not guaranteed output counts when candidates are capped or invalid.

## Response timing framework

| Project | Base duration | Short end conditions | Long end conditions |
| --- | ---: | --- | --- |
| Reinforce a Priority Sector | 45 to 75 days | compact state, strong industry, high infrastructure, urgent defense with higher material cost | long frontier, low infrastructure, damage, weak industry |
| Connect the New Line | 60 to 100 days | existing developed network, strong transport reserve | poor network, long distance, damage, weak industry |
| Conduct Breach Exercises | 45 to 75 days | relevant doctrine, engineers, experience, recent fort combat | high target forts, missing engineers, low planning capacity |
| Harden the Air and Coastal Flank | 60 to 100 days | existing supporting network and clear single role | combined role, weak industry, low infrastructure |
| Prepare a National Redoubt | 90 to 140 days | strong industry, existing strategic site and network | weak industry, poor access, broader support work |

Project reward duration for breach preparation: `90` to `150` days.

## Material cost framework

### Reinforce a Priority Sector

| Cost | Small-country anchor | Large-country anchor | Reserve rule |
| --- | ---: | ---: | --- |
| Infantry equipment | 250 to 500 | 750 to 1,500 | preserve active army reinforcement floor |
| Support equipment | 40 to 100 | 150 to 300 | preserve division and support-company floor |
| Civilian factories | 1 to 2 | 3 to 5 | temporary commitment, never exceed bounded share of usable civilian industry |
| Manpower | 1,000 to 4,000 | 8,000 to 20,000 | preserve minimum free manpower and never create negative pool |

### Connect the New Line

| Cost | Small-country anchor | Large-country anchor | Reserve rule |
| --- | ---: | ---: | --- |
| Trains | 10 to 20 | 30 to 70 | preserve active supply reserve |
| Trucks | 100 to 300 | 500 to 1,200 | preserve motorization and reinforcement reserve |
| Support equipment | 40 to 100 | 150 to 300 | preserve normal military floor |
| Civilian factories | 1 to 2 | 3 to 6 | temporary commitment with country-size cap |

### Conduct Breach Exercises

| Cost | Small-country anchor | Large-country anchor | Reserve rule |
| --- | ---: | ---: | --- |
| Army Experience | 10 to 20 | 20 to 40 | do not consume below a small planning reserve when AI uses it |
| Support equipment | 40 to 100 | 100 to 250 | preserve reinforcement floor |
| Fuel | bounded target and army scaled commitment | larger bounded commitment | preserve operational reserve based on active army and air needs |
| Command Power | 10 to 25 | 20 to 40 | never make the decision unavailable solely because base regeneration is low when a three-cost variant fits better |

### Harden the Air and Coastal Flank

Air branch uses civilian factories, air-defense equipment, Air Experience, and support equipment.

Coastal branch uses civilian factories, convoys, Navy Experience, and support equipment.

Suggested anchors:

- 1 to 2 civilian factories for small countries
- 3 to 6 civilian factories for large countries
- 5 to 15 relevant experience for small countries
- 15 to 30 relevant experience for large countries
- 30 to 80 support equipment for small countries
- 100 to 250 support equipment for large countries
- equipment or convoy bundle scaled to the exact physical result

### Prepare a National Redoubt

| Cost | Small-country anchor | Large-country anchor | Reserve rule |
| --- | ---: | ---: | --- |
| Civilian factories | 2 to 3 | 4 to 8 | temporary commitment, longer duration can replace impossible cost |
| Trains or infantry equipment | 10 to 25 trains or equivalent | 30 to 80 trains or equivalent | choose the bundle that fits target role and preserve reserves |
| Support equipment | 50 to 150 | 200 to 500 | preserve army floor |
| Manpower | 2,000 to 6,000 | 10,000 to 30,000 | preserve minimum free pool |

## Posture effect framework

Exact modifiers require current game and mod validation.

| Posture | Primary effect range | Secondary effect range | Scope limit | Prohibited design |
| --- | --- | --- | --- | --- |
| Integrate the Line | modest fort-defense or prepared-ground combat improvement | entrenchment or fort-repair improvement | temporary, focused on defensive use | broad permanent army attack or defense bonus everywhere |
| Keep the Roads Open | modest supply-consumption or transport-repair improvement | lower fortified-sector attrition or network repair support | temporary, logistics focused | free factory or full network construction bonus unrelated to line use |
| Study the Breach | meaningful fort-attack improvement | planning speed, engineer, or target-bound adaptation | temporary and fort or target focused | broad general attack bonus against every enemy |

Starting magnitude target:

- posture should change a real decision
- posture alone should not decide a war
- posture plus its completed project should be stronger than posture alone
- offensive posture should offset a meaningful share of one or two fort levels, not erase a level eight anchor

## Chaos tuning framework

| Source | Starting target | Allowed band | Scaling ceiling | Guard |
| --- | ---: | ---: | ---: | --- |
| First natural global wave | +8 | +5 to +12 | no more than +12 | one-time, natural, material footprint |
| Meaningful repeat wave | +2 | +1 to +3 | no more than +3 | 365-day family cooldown, minimum footprint |
| First Defense in Depth materialization | +5 | +3 to +7 | no more than +7 | one-time concrete stage result |
| First Fortress States materialization | +10 | +6 to +14 | no more than +14 | one-time concrete stage result |
| First Fortress World materialization | +15 | +10 to +20 | no more than +20 | one-time concrete stage result |
| Distinct cluster convergence | +3 | +2 to +4 | no more than +4 | once per cluster incident, requires another real military-abundance result |
| No-op, debug, eligibility, posture choice | 0 | 0 | 0 | automatic |

### Footprint factors

- countries changed
- direct frontier provinces changed
- states and regions represented
- share of all valid remaining frontiers
- first-time versus repeat result
- concrete evolution package diversity
- time since prior direct Event 064 gain

Do not multiply gains aggressively by current Chaos.

## Cluster tuning framework

Numeric cluster IDs, unlock tiers, roll chances, participation chances, order scores, and cooldowns belong to the authoritative cluster registry. Event 064 does not assign them locally.

Event-specific requirements:

| Item | Requirement |
| --- | --- |
| Sudden Abundance membership | Medium |
| Military Preparation membership | Medium |
| Automatic cluster contexts per Event 064 selection | maximum one |
| Event 064 executions per cluster incident | maximum one |
| Cluster cost benefit | one bounded relevant cost element per incident |
| Cluster convergence Chaos | only when another participating member produces a concrete military-material gain |
| Cluster effect on fort levels | none by default |
| Cluster effect on strategic scoring | permitted for exact relevant context |

## Achievement tuning framework

| Achievement | Main threshold anchors | Tuning risk |
| --- | --- | --- |
| Continent of Concrete | 5 land neighbors, 8 core border states, 12 frontier provinces, 80 percent at level 5 or higher, 4 border states with AA or radar, 2 simultaneous neighboring enemies, 180-day hold | impossible geography for most countries, expensive recurring check, state-release exploit |
| The Line Held | non-major, attacker at least twice accepted strength, factionless and independent, 365-day survival or favorable peace, no loss of capital or marked core border state | strength metric instability, third-party war resolution, faction loophole |
| Breach the Unbreachable | target line level 5 or higher, at least 3 relevant states or equivalent, stored land route, capital within 180 days | fort-average definition, paratroop detection, target deletion, third-party capture |
| Last Redoubt | 600 Chaos, 10 owned core states, below 40 percent core VP control, hold capital and supply redoubt 180 days, recover to 80 percent | VP calculation cost, moved capital exploit, small-country exploit |

Adjust thresholds only after testing. Preserve each achievement's core challenge.

## Performance budget

| Operation | Budget rule |
| --- | --- |
| Global country pass | once per Event 064 incident |
| Country controlled-state pass | once for frontier and strategic preparation where possible |
| Province application | bounded to direct frontier and selected candidate sets |
| Strategic scoring | temporary per-country candidates, cleared immediately after local finalization |
| Achievement checks | player-country and stored challenge targets only at meaningful checkpoints |
| Decision target checks | country-local and category-active only |
| Recurring world scan | forbidden |
| New border detection | next Event 064 wave, or bounded compatibility hook explicitly owned by another event |

## Balance questions for final tuning

1. How many early wars become static after one baseline wave?
2. How often do repeated waves reach the baseline cap before engineers and air support become common?
3. Does Study the Breach let a prepared attacker cross level three to five lines without making level seven to eight anchors irrelevant?
4. Does AI select supply work when supply is the actual problem?
5. Can a small country afford one meaningful project without emptying its stockpiles?
6. Can a major buy every project with no real tradeoff?
7. Do Fortress States remain selected and visible without covering every border state?
8. Are new supply hubs rare enough to preserve normal logistics gameplay?
9. Do island countries receive a useful high-tier result without receiving fake land-border packages?
10. Does Event 064 direct Chaos remain meaningful without overtaking shared war and casualty sources?
11. Can either cluster membership occur in practice?
12. Does one cluster incident ever execute Event 064 twice?
13. Does the world transaction finish cleanly on a heavily fragmented late-game map?
14. Do reports remain concise when global counts are large?
15. Are achievement checks difficult, scriptable, and resistant to transfers and tag changes?
