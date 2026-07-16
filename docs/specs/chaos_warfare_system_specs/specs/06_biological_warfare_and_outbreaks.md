# Biological Warfare and Outbreaks

## Design role

Biological warfare is a slow, uncertain, and potentially self-propagating weapon system. It is not chemical warfare with a longer state modifier. Its central mechanics are incubation, detection, spread, outbreak intensity, containment, attribution, mutation risk, and public-health capacity.

Conventional biological warfare and weaponized zombies remain separate. Zombie systems can use the shared outbreak and contamination tools, but ordinary anthrax, plague, tularemia, and smallpox programs must not automatically enter zombie content.

## Biological program values

| Value | Meaning |
| --- | --- |
| Biosecurity | Laboratory and stockpile safety. |
| Surveillance | Detection speed and hidden-outbreak visibility. |
| Containment capacity | Ability to isolate states and reduce spread. |
| Medical response | Vaccination, antibiotics, field hospitals, and treatment. |
| Weaponization quality | Reliability of delivery and intended agent behavior. |
| Attribution control | Ability to avoid direct evidence. |
| Mutation pressure | Risk of unintended behavior, intensified by high chaos and poor safety. |

## Agent profiles

### Anthrax

Role: persistent local contamination and high local lethality with limited person-to-person spread.

Gameplay profile:

- high mortality when untreated
- low natural cross-state spread
- persistent contaminated-site burden
- strong effect on livestock, local supply, and medical capacity if represented
- high forensic evidence after samples are recovered

Best use:

- airfield, depot, port, industrial, or laboratory target
- sabotage and strategic raid

Counterplay:

- antibiotics
- decontamination
- rapid detection
- sealed handling

### Plague

Role: high-spread outbreak weapon.

Gameplay profile:

- moderate to high mortality
- strong neighbor-state spread
- urban and low-healthcare amplification
- border closure and quarantine are important
- severe international reaction

Best use:

- dense transport corridors and cities
- covert introduction

Counterplay:

- surveillance
- quarantine
- antibiotics
- movement control
- vector-control abstraction

### Tularemia

Role: military incapacitation and regional disruption.

Gameplay profile:

- lower death rate than plague or smallpox
- high organisation, recovery, and supply impact
- useful against concentrated armies
- moderate spread
- difficult diagnosis before surveillance improves

Best use:

- frontline air or covert operation
- depot and troop-concentration target

Counterplay:

- rapid detection
- antibiotics
- field epidemiology

### Smallpox

Role: long-incubation mass civilian and military outbreak.

Gameplay profile:

- high spread
- long duration
- high civilian death potential
- vaccination is the main strategic counter
- extreme Condemnation

Best use:

- strategic escalation or doomsday route

Counterplay:

- vaccination reserve
- surveillance
- strict quarantine
- international medical aid

### Weaponized zombie pathogen

Role: separate high-chaos system.

Rules:

- uses its existing custom decisions, state decay, weaponized-zombie creation, and cure systems
- does not share ordinary vaccination or antibiotic outcomes unless the zombie design explicitly calls them
- cannot be selected as a normal biological payload profile
- requires its own project, flags, AI, and world-threat handling

## Development and special projects

Every offensive agent requires a completed special project. Research after the project handles delivery, containment, and countermeasures.

Project choices should create real tradeoffs:

- cautious development: slower breakthrough, higher Biosecurity
- military acceleration: faster progress, higher accident risk
- dispersed facilities: harder to destroy, more evidence and local risk
- centralized facility: faster and safer at high investment, catastrophic if compromised
- human experimentation route: faster weaponization, atrocity evidence, deaths, coverup, and extreme Condemnation after discovery

The last route belongs to the atrocity and evidence system. It is never a free research bonus.

## Stockpile production

Biological payload is produced after project completion. Production increases accident risk according to:

- stockpile size
- agent danger
- facility safety
- Biosecurity
- war damage
- sabotage
- doctrine and designer traits
- recent handling operations

The player sees a stockpile-risk band:

- controlled
- strained
- dangerous
- critical

Exact hidden accident chance can remain undisclosed, but the contributing factors must be readable.

## Delivery methods

### Strategic biological raid

Reliable state-targeted operation.

Inputs:

- eligible aircraft
- agent payload
- intelligence
- weather and target conditions
- Biosecurity and weaponization quality

Outcomes:

- failed delivery
- partial contamination
- hidden contamination
- detected outbreak seed
- successful outbreak seed
- attacker accident

A successful delivery does not guarantee an outbreak. It creates contamination and an incubation timer.

### Operative outbreak operation

Uses the existing intelligence-operation concept.

Stages:

1. acquire sample and transport chain
2. infiltrate target
3. establish release condition
4. release or abort
5. attribution and containment resolution

Costs:

- operatives and network strength
- biological payload
- equipment
- time
- exposure risk

Captured operatives can create immediate confirmed attribution and coverup Condemnation.

### Battlefield biological dissemination

Allowed only for selected agents and high readiness.

It targets concentrated armies and supply areas. It has lower strategic spread than a city attack but high risk of affecting friendly troops and occupied territory.

### Sabotage of food, water, or medical systems

Covert decision family. It creates lower initial dose, high attribution uncertainty, and severe political consequence after discovery.

## Chaos Warfare doctrine interaction

Chaos Warfare doctrine is an escalation path. It may raise seed potency, outbreak growth, spread, deaths, duration, medical saturation, preparation speed, and aggressive AI willingness. It may also ease deployment through bounded preparation savings or a bounded Command Power refund after an operation has resolved.

Condemnation is the only consequence record doctrine may reduce. Doctrine may not reduce physical payload debit, evidence, attribution, deaths or death history, contamination or contamination history, medical saturation or medical history, confirmed-use history, domestic war-support penalties, biological-use counters, accident records, resistance trauma, or public-harm floors.

Doctrine cannot create, reveal, authorize, or unlock camps, extermination sites, experiment sites, restricted chemical sites, or generic concentration laws. Any separately authorized interaction with an existing camp system is limited to increasing its already resolved killing efficiency. It cannot change that system's evidence, discovery, responsibility, resistance, trauma, Condemnation, or historical records.

## Current implementation boundary

The strategic biological raid tranche uses the native selected state, exact agent payload reservation and debit, six biological outcomes, and state-owned incubation and lifecycle ticks. It does not seed contamination from continuous air activity or infer a launch state.

The ordinary operative-release tranche implements four separate native intelligence operations for Anthrax, Plague, Tularemia, and Smallpox. Each operation uses its native selected state, agent-specific state profile, native non-refunded agent equipment, distinct preparation time and equipment bill, and abort, partial-release, or full-release resolution. Partial and full release enter the same state-owned lifecycle as the strategic raid with the operative-release route profile; an abort records an attempt but does not create confirmed biological-use history. The operation engine does not expose the runtime amount charged by its equipment block, so the native cost and `return_on_complete = no` are authoritative and no numeric payload proof or lifecycle amount is fabricated for this route.

The current-version `on_operative_captured` hook reads the captured character's exact operation token, assigned country, and positive assigned state. Every actual capture callback is evaluated immediately. A capture matching a live seeded episode creates confirmed attribution and a one-shot outbreak coverup consequence; otherwise it creates attempt and coverup consequences without falsely recording completed weapon use. The engine exposes no unique operation-instance identifier, so actual captured operatives cannot be deduplicated by operation without inventing identity. Missing or mismatched context fails closed, with no inferred country, inferred state, periodic search, proxy, estimator, or fallback.

Theater Contamination and Terminal Hazard doctrine increase operation success and refund bounded Command Power after resolution while leaving the native equipment cost intact. Operation AI uses defensive-profile suppression and agent-specific target-country evidence. The native API cannot rank the eventual selected state, and current-version triggers expose no exact state-scope frontline predicate; Tularemia therefore uses only verified troop-presence and supply-node evidence rather than unrelated buildings or an estimator.

The ordinary lifecycle reads `smallpox_vaccination_program_idea` directly for agent-specific growth, spread, and death multipliers. Recovery calls `bio_lifecycle_cleanup_state_response_if_no_ordinary_episode` for the exact state. This removes field hospitals, quarantine, stale legacy protection state, and the quarantine modifier only after no ordinary episode remains.

The current implementation has no `common/on_actions/chaosx_on_actions_biowarfare.txt` file and no startup or weekly calls to `initialize_smallpox_vaccination_protection`, `progress_smallpox_vaccination`, or `check_all_states_for_contamination_cleanup`. Ordinary biological progression and cleanup do not use a global daily, weekly, or monthly country pulse.

`GFX_decision_bio_designate_strategic_raid_staging_state` is registered in `interface/biological_warfare.gfx`. Strategic raids reuse the byte-preserved Chaos Redux raid icons under `gfx/interface/military_raids/`.

The operative operations reuse the existing `GFX_operations_plant_bioweapon`, `GFX_operations_plant_bioweapon_map`, and operation phase sprites. Weaponized-zombie operations remain separate and retain their existing project, operation, effects, and player-facing outcome text.

These implemented surfaces do not close Stage 7. Battlefield dissemination, food/water/medical sabotage, laboratory accidents, captured-facility release, doomsday release, the complete countermeasure and treatment package, remaining required assets and localisation, package scenarios, and the mapped audits remain accepted wherever the Stage 7 plan has not established completion evidence.

## Incubation and detection

A seeded state receives hidden biological contamination. Detection time depends on:

- surveillance
- target medical infrastructure
- operation quality
- agent profile
- chaos tier
- population density
- active war damage
- attacker concealment

The target receives ambiguous local pressure before confirmation:

- rising medical saturation
- reduced local output
- unusual military sickness
- supply disruption

Final player-facing text must describe observable conditions without announcing hidden mechanics.

## Outbreak intensity

| Intensity | Meaning |
| ---: | --- |
| 1 to 19 | isolated cases or failed seed |
| 20 to 39 | local outbreak |
| 40 to 59 | serious regional outbreak |
| 60 to 79 | severe multi-state crisis |
| 80 to 100 | catastrophic epidemic |

Intensity rises through:

- population density
- low surveillance
- low containment
- movement and trade routes
- adjacent outbreaks
- war damage
- refugee pressure
- repeated biological attacks
- high Air Cleanliness contamination thresholds where existing design calls for it

Intensity falls through:

- quarantine
- hospitals
- antibiotics
- vaccination
- border closure
- medical aid
- successful containment missions
- seasonal or agent-specific decay

## Spread model

Spread is driven by the active agent's state-owned lifecycle event and schedules only the exact newly exposed state. It does not use a global daily, weekly, or monthly country pulse or an all-state scan.

A state can spread to:

- adjacent controlled states
- connected supply or port corridors
- occupied neighboring states
- foreign states through active border or transport links

Spread chance considers movement-control severity, outbreak intensity, surveillance, medical capacity, and agent profile.

## Countermeasure decisions

### Activate surveillance network

Requires instruments, political support, and medical capacity. Reveals contamination earlier and improves evidence.

### Quarantine affected state

Consumes equipment, manpower, local economy, and stability. Reduces spread but increases resistance and civilian hardship.

### Deploy field hospitals

Consumes support equipment, trucks, and medical capacity. Reduces deaths and saturation.

### Antibiotic campaign

Effective against relevant bacterial profiles. Consumes industrial or medical stores and can create diminishing efficiency after repeated emergency use.

### Vaccination campaign

Requires agent-specific preparation or broad vaccination technology. Slow to establish, strong for smallpox and selected agents, less useful after widespread outbreak without supply.

### Close borders and transport corridors

Uses the existing border-closure foundation. It reduces spread and trade while disrupting supply and diplomacy.

### Request international medical mission

Available when diplomatic relations and Condemnation politics permit. It increases containment and evidence transparency. A suspected aggressor that accepts outside inspection gains credibility but risks exposure of its own program.

## Deaths

Biological deaths occur over time. Each agent has a base fatality profile and treatment sensitivity.

Suggested weekly exposed-population death bands before countermeasures:

| Agent | Low intensity | Serious | Catastrophic |
| --- | ---: | ---: | ---: |
| Anthrax | 0.0005% | 0.004% | 0.015% |
| Plague | 0.0003% | 0.006% | 0.025% |
| Tularemia | 0.00005% | 0.0008% | 0.004% |
| Smallpox | 0.0002% | 0.005% | 0.020% |

The exposed share is calculated separately. Continuing deaths are capped, use the shared Deaths tracker, and stop when the outbreak ends.

Medical capacity and countermeasures can reduce these rates greatly. War damage and medical saturation can raise them.

## Military effects

- organisation and recovery loss
- reinforcement delay
- manpower availability pressure
- supply consumption
- training and mobilisation disruption
- infected-unit movement restrictions
- increased attrition
- temporary commander ability penalties

A well-protected and medically prepared army should resist military disruption even while the state civilian population suffers.

## Attribution and evidence

Evidence sources:

- recovered delivery device
- captured operative
- distinctive laboratory strain
- compromised facility records
- whistleblower or scientist defection
- repeated agent match
- foreign intelligence
- discovered experiment site

Attribution states:

- unknown natural outbreak
- suspicious
- probable deliberate outbreak
- confirmed biological attack

A deliberate outbreak can remain uncertain at first. Later confirmation releases latent biological Condemnation and coverup pressure.

## Biosecurity accidents

Accident chance increases with stockpile and facility strain. Outcomes:

- contained incident
- laboratory contamination
- local outbreak
- major domestic outbreak
- international exposure of the program

Containment safety technologies reduce chance and severity. The highest safety tier can prevent ordinary stockpile accidents, but sabotage, bombing, and doomsday release remain possible.

## Captured facilities

When an enemy captures a biological facility:

- it can secure or destroy the stockpile
- it can preserve evidence
- it risks accidental release
- a Biological Security Assault Detachment reduces the risk
- discovered experimentation or coverup can create atrocity and coverup Condemnation

## Doomsday release

The existing last-resort biological release remains, but it requires:

- explicit national route or extreme policy
- near capitulation or world-end condition
- existing stockpile
- warning tooltip that lists domestic states at risk

It consumes the arsenal, seeds controlled territory and nearby fronts, creates severe deaths and outbreaks, sets maximum evidence, and causes extreme Condemnation. It can damage allies and the releasing country.

## AI behavior

AI evaluates:

- target value and population
- war state
- retaliation status
- Biosecurity
- expected spread into own territory
- border and occupation position
- medical readiness
- sanction vulnerability
- ideology and country program
- chaos tier

Ordinary AI avoids strategic biological first use. High-chaos, radical, retaliatory, or desperate AI can use it. Japan-specific historical routes can have stronger China-theater willingness, but they remain gated by route, war, evidence, and program state.

## Acceptance criteria

- Biological use creates incubation and outbreak rather than instant chemical-style penalties.
- Agent profiles differ meaningfully.
- Countermeasures can prevent or contain spread.
- Accidents scale with stockpile and safety.
- Captured facilities create evidence and release risk.
- Conventional biological warfare remains separate from zombies.
- Deaths, Air Cleanliness, Condemnation, and outbreaks stay synchronized.
