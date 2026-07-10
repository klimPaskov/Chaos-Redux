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

Spread is event-driven or uses an approved targeted pulse. Do not create an unapproved all-state daily loop.

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
