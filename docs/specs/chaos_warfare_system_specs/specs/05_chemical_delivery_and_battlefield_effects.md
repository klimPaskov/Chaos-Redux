# Chemical Delivery and Battlefield Effects

## Shared chemical-use pipeline

Every chemical action calls one shared exposure model. Delivery systems provide inputs. The shared model calculates effects and sends results to units, states, Deaths, Air Cleanliness, evidence, and Condemnation.

### Required inputs

- attacker country
- victim country when known
- target state
- target order or combat when known
- agent class and agent variant
- delivery method
- nominal dose
- payload ratio
- weather profile
- terrain profile
- target military protective coverage
- target civilian protective coverage
- medical capacity
- decontamination capacity
- attacker Chemical Readiness
- attacker headquarters integration
- attacker attribution control
- public visibility state
- repeat-use pressure

### Required outputs

- military organisation loss
- military recovery and reinforcement penalty
- temporary attack, defence, movement, or entrenchment changes
- military deaths
- civilian deaths
- state contamination change
- medical saturation change
- mask and filter consumption
- friendly blowback
- evidence quality
- chemical Condemnation gain
- activity log entry

No delivery system should implement its own isolated death or Condemnation formula.

## Delivery-method identities

### General cylinder ability

Role: immediate local release for an assigned army.

Strength:

- fast activation
- flexible
- lower infrastructure requirement

Weakness:

- high wind sensitivity
- high friendly-exposure risk
- limited dose
- weaker state persistence

Rework:

- move from a general-wide free buff to an Army HQ ability or a legacy compatibility ability
- require CBRN Operations Section and payload
- affect only the selected order
- show forecast and protection information
- retain agent-specific profile selection

### Chemical projector battery

Role: short-range fortified-position and urban-area delivery.

Strength:

- high local dose
- effective in forts, urban terrain, forest, and enclosed terrain
- relatively cheap equipment

Weakness:

- vulnerable to counterbattery fire
- poor mobile use
- high friendly blowback in changing fronts
- requires close supply

### Chemical artillery shells

Role: prepared battlefield fire plan.

Strength:

- longer range
- target concentration and counterbattery options
- scales with artillery density
- can choose choking, blister, or nerve profile

Weakness:

- expensive shell-lot production
- supply burden
- visible evidence and predictable launch area
- long cooldown for large operations

### Armored delivery

Role: protected close delivery during breakthrough and occupation.

Strength:

- mobile
- strong urban and fort utility
- lower crew exposure with sealed systems
- can exploit immediately

Weakness:

- expensive vehicles
- maintenance and fuel burden
- limited affected area
- severe risk to accompanying unprotected infantry

### Chemical air interdiction

Role: battlefield and operational-area contamination through chemical aircraft.

Strength:

- reaches behind the front
- affects supply routes, reserves, and airfields
- can combine with ground exploitation

Weakness:

- requires air superiority or survivable strike aircraft
- payload reservation and loss
- weather and mission reliability
- strong evidence and Condemnation
- continuous mission detection may be engine-limited

### Strategic chemical raid

Role: reliable state-targeted operation with explicit completion outcome.

Strength:

- exact target and payload
- clear success, partial success, interception, and failure outcomes
- ideal for cities, ports, depots, capitals, and fortified zones

Weakness:

- long preparation
- high aircraft and payload requirement
- high civilian deaths
- major evidence and sanction risk

### Covert chemical operation

Role: sabotage or clandestine release.

Strength:

- uncertain attribution
- lower direct military footprint

Weakness:

- intelligence cost
- limited scale
- risk of captured operatives and extreme evidence
- not a substitute for battlefield delivery

## Chemical air bombs

## Aircraft design layer

Chemical air modules should remain available for CAS and tactical bombers, with possible strategic-bomber use only after local air-designer validation.

Module effects:

- increased production cost
- increased weight
- reduced agility or range according to payload installation
- modest ordinary ground-attack value
- marks aircraft as eligible for chemical operation contribution

The ordinary ground-attack stat is not the main chemical effect.

## Reliable operation path

The primary functional path is an explicit chemical air operation or raid:

1. player selects a target state or strategic region
2. system verifies eligible aircraft design and deployed aircraft
3. system reserves chemical air payload
4. operation runs for a fixed preparation and execution period
5. interception, weather, target air defence, intelligence, and readiness determine outcome
6. completion applies exact exposure to selected states
7. payload is consumed
8. deaths, contamination, evidence, and Condemnation are recorded

Outcome bands:

| Outcome | Payload consumed | Exposure |
| --- | ---: | ---: |
| Aborted | 10 to 25 percent | none or trace friendly accident risk |
| Failed | 40 to 80 percent | no target exposure, possible crash evidence |
| Partial | 70 to 100 percent | 35 to 65 percent intended dose |
| Successful | 100 percent | full intended dose |
| Catastrophic success | 100 percent | 110 to 140 percent dose with extreme civilian exposure and evidence |

Catastrophic success is a moral and political disaster, not a free critical hit.

## Continuous mission path

The current repository estimates chemical air activity from deployed CAS and tactical bombers, frontline density, and war activity because exact module mission use is not reliably exposed.

The rework must not call the approximation fully reliable. Use one of these outcomes after local engine research:

### Preferred

A current 1.19 hook identifies mission activity by design or module. Use it to calculate weekly payload and contamination.

### Acceptable only with explicit approval

Keep a conservative estimator that requires:

- a country flag that the player enabled continuous chemical sorties
- eligible chemical aircraft share above a threshold
- actual air mission activity in the region
- active ground operations or selected target region
- a weekly payload budget reserved by decision

The estimator must never infer use merely because chemical-capable aircraft are deployed.

### Blocked

If no reliable mission activity hook exists and the user does not approve the estimator, continuous contamination remains unavailable. Explicit raids and operations still function.

## Air contamination targeting

A successful operation does not contaminate every state in a strategic region equally.

Target score considers:

- selected primary state
- airbase, supply hub, port, capital, victory point, or industrial target
- enemy unit density
- wind direction
- weather
- target air defence
- operation size

The primary state receives full dose. One to three adjacent or operationally linked states can receive partial dose at high operation intensity.

## Chemical artillery

### Shell-lot preparation

The player converts payload and production capacity into chemical shell lots. A filling program chooses one agent class. Changing filling profile has a delay and wastage cost.

### Fire-plan types

#### Choking barrage

- high immediate organisation loss
- low persistence
- strong wind dependence
- moderate deaths when unprotected
- low utility against advanced masks

#### Persistent blister barrage

- moderate immediate combat effect
- high state contamination
- delayed deaths and medical saturation
- supply-route denial
- requires decontamination before friendly occupation

#### Nerve shock barrage

- very high immediate disruption and death ceiling
- shorter persistence than blister agents
- advanced-project gate
- extreme evidence and Condemnation
- strong counter from advanced masks, antidotes, and sealed positions

#### Incapacitating barrage

- temporary organisation, movement, and attack penalties
- low death ceiling
- lower but nonzero Condemnation
- useful for capture or withdrawal operations

### Artillery scaling

Effective dose scales with:

- number of artillery battalions and support batteries in the assigned order
- Chemical Ammunition Train coverage
- shell-lot ratio
- headquarters planning
- enemy dispersion
- weather and terrain

The effect must scale down with damaged or unequipped artillery. It cannot be gained from one token support battery applied to a huge army.

## Chemical tank and armored shells

The current agent-by-agent tank support list should be consolidated.

### Roles

- light delivery vehicle: reconnaissance, rapid local release, river and rough-terrain access
- medium delivery vehicle: standard breakthrough support
- heavy delivery vehicle: fortified and urban assault

The chassis role determines survivability, fuel, speed, and number of vehicles. The selected payload profile determines chemical effect.

### Chemical shells and spray systems

Armored delivery can use:

- close-range chemical shells
- projector or spray equipment
- sealed transport for chemical mortar teams

The operation should create local combat exposure rather than region-wide contamination. Persistent agents can leave state contamination after repeated or prepared use.

### Protection interaction

Sealed crews protect the vehicle crew. They do not protect nearby infantry. Combined-arms formations need Gas Mask and Decontamination Detachments or a Protective Logistics HQ.

## First-use surprise

The current flat thirty-day attacker buff is replaced by defender adaptation.

### Surprise state

A country that has not experienced recent chemical use can suffer First Chemical Shock when attacked.

Shock severity depends on:

- military mask coverage
- chemical reconnaissance
- intelligence warning
- prior global chemical use
- treaty and civil-defence preparation
- agent visibility

Effects:

- delayed mask response
- higher organisation loss
- higher initial deaths
- temporary planning and reinforcement penalty

### Adaptation

After exposure:

- target gains chemical awareness
- surprise penalty falls for future attacks
- gas-mask research and production AI priority rises
- allies can share warning and protection experience
- evidence and international reaction increase

The attacker does not receive a universal attack buff against every country for a fixed period.

## Weather and terrain

### Wind

Wind has direction, strength, and forecast confidence. The player sees a forecast band, not exact hidden rolls.

- favorable wind increases target dose and lowers friendly exposure
- neutral wind leaves dose near baseline
- unfavorable wind lowers target dose and raises friendly exposure
- strong or unstable wind can disperse choking agents

### Temperature

- cold can increase persistence for some agents and slow decontamination
- heat can increase evaporation, equipment burden, and mask fatigue
- extreme heat reduces long choking persistence but can worsen protective-posture penalties

### Rain

- reduces some airborne agent effectiveness
- can spread or retain persistent contamination in local terrain
- improves some cleanup while complicating routes

### Terrain

- urban, forest, jungle, marsh, and forts retain agents and complicate evacuation
- plains and desert disperse choking agents more easily
- mountains and strong elevation changes reduce predictable delivery
- river and amphibious operations increase friendly-exposure and logistics risk

These are gameplay profiles, not claims of exact toxicological behavior.

## Military effects

Chemical exposure should use temporary unit modifiers and casualty helpers.

Possible effects:

- organisation damage
- reduced recovery
- reduced reinforcement
- movement penalty
- planning loss
- entrenchment disruption
- attack and defence penalty
- increased equipment attrition
- increased supply consumption
- reduced command ability duration

Protection reduces these effects. Full protective posture creates its own modest movement, attack, and supply penalties.

## Death model

Deaths must be strong enough to matter while avoiding uncontrolled repeated ticks.

### Immediate civilian death bands

Share of exposed state population, before protection and medical reduction:

| Agent and operation | Low | Typical | Catastrophic |
| --- | ---: | ---: | ---: |
| Choking tactical use | 0.001% | 0.004% | 0.015% |
| Choking strategic raid | 0.003% | 0.012% | 0.040% |
| Blister tactical use | 0.0005% | 0.003% | 0.010% |
| Blister strategic raid | 0.002% | 0.008% | 0.025% |
| Nerve tactical use | 0.003% | 0.015% | 0.050% |
| Nerve strategic raid | 0.010% | 0.040% | 0.120% |
| Incapacitating use | 0.00005% | 0.0003% | 0.0015% |

These are exposed-population rates, not total state-population guarantees. The model first calculates an exposed share from operation scale, target type, shelters, weather, and urban density.

### Continuing deaths

Persistent contamination can create weekly deaths for 2 to 16 weeks. The weekly value falls as decontamination progresses and is capped by remaining exposed population. A state cannot receive multiple full continuing-death ticks from overlapping operations. The system stores the highest active severity and refreshes or adds bounded duration.

### Military deaths

Military deaths scale from divisions, manpower, exposure, and protection. Use the shared Deaths military category. Do not attempt to create all battle casualties through direct state population loss.

## Protection multipliers

Suggested first-pass multipliers to exposure effect:

| Protection | Choking | Blister | Nerve |
| --- | ---: | ---: | ---: |
| No protection | 1.00 | 1.00 | 1.00 |
| Partial basic masks | 0.75 | 0.90 | 0.85 |
| Full basic masks | 0.45 | 0.75 | 0.65 |
| Improved masks and decon | 0.25 | 0.45 | 0.40 |
| Advanced set and medical support | 0.12 | 0.25 | 0.20 |
| Sealed crew or shelter | 0.06 | 0.15 | 0.10 |

Blister and nerve protection require more than a mask. The system should calculate component coverage when practical.

## Contamination values by delivery

| Delivery | Trace to local | Serious | Severe to catastrophic |
| --- | ---: | ---: | ---: |
| Cylinder ability | 1 to 5 | 6 to 12 | not normally available |
| Projector combat use | 2 to 8 | 9 to 18 | 19 to 30 with persistent profile |
| Prepared artillery | 4 to 12 | 13 to 30 | 31 to 55 |
| Armored delivery | 1 to 6 | 7 to 15 | 16 to 25 after repeated use |
| Continuous air week | 1 to 5 | 6 to 12 | capped at 20 per week per state |
| Strategic air raid | 10 to 25 | 26 to 50 | 51 to 80 |
| Doomsday release | 40 to 70 | 71 to 100 | multiple states at catastrophic class |

## Evidence and attribution

Evidence sources:

- captured shells or cylinders
- aircraft wreckage
- weather and strike pattern
- laboratory samples
- prisoner testimony
- reconnaissance and intelligence
- public casualties
- persistent contamination
- repeated use

Public attribution bands:

- hidden
- suspected
- probable
- confirmed

Doctrine and intelligence can reduce evidence generation. Deaths and persistent contamination create a minimum evidence floor. A confirmed strategic raid cannot be converted back to hidden through a generic doctrine modifier.

## Condemnation scaling

Chemical gain considers:

- use severity
- civilian deaths
- military deaths
- persistent contamination
- use against neutral, allied, subject, occupied, or non-core populations
- first use or retaliation
- repeated use window
- attribution confidence
- public policy and treaty status

Suggested attribution multiplier:

| Attribution | Multiplier |
| --- | ---: |
| Hidden | 0.10, stored as latent exposure |
| Suspected | 0.25 |
| Probable | 0.60 |
| Confirmed | 1.00 |

When later evidence confirms a hidden act, the stored latent value is released with a coverup component.

## AI use

AI prepares chemical operations only when:

- target value is high enough
- it has protection and payload
- weather and forecast are acceptable
- expected military benefit exceeds supply and sanction cost
- national policy permits use
- target is not already collapsing so quickly that use is wasteful

AI should favor:

- choking agents early against unprotected fronts
- blister agents for fortified routes and supply denial
- nerve agents only under advanced, radical, retaliatory, or desperate profiles
- explicit raids against key logistics or fortified targets

## Acceptance criteria

- Chemical air raids reliably contaminate selected states.
- Continuous chemical air contamination is either based on a verified hook or clearly blocked.
- Artillery and armored delivery consume payload.
- Agent classes create distinct effects.
- First-use surprise belongs to defender adaptation.
- Protection modifies all delivery systems.
- Deaths and contamination are bounded and nonduplicative.
- Confirmed use creates meaningful Condemnation.
