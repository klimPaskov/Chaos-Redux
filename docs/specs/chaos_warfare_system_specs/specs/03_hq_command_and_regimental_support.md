# Army Headquarters and Regimental Support Integration

## Design rule

Army Headquarters owns theater preparation. Regimental support owns division-level execution and protection. A normal support company can still represent a specialist detachment, but the strongest order-wide effects require an HQ company and a commander ability.

## Army Headquarters support companies

The exact 1.19 schema and slot rules must be verified against the installed game. The following entries define gameplay roles and target balance.

### CBRN Operations Section

Role: basic headquarters integration and prerequisite for most chemical commander abilities.

Essential equipment:

- support equipment
- radios or signal equipment through vanilla categories
- gas-mask equipment
- CBRN instruments

Baseline effects:

- small planning-speed bonus for assigned orders
- reduced operation preparation time
- operation tooltips reveal payload ratio and friendly-exposure risk
- unlocks Prepare Chemical Offensive

Equipment shortage behavior:

- ability cannot activate below the essential-equipment floor
- planning and exposure-control benefits scale down with equipment status

### Chemical Intelligence and Weather Cell

Role: forecast, target protection estimate, wind confidence, and evidence analysis.

Essential equipment:

- support equipment
- trucks for mobile stations
- meteorological instruments
- radios

Effects:

- higher forecast confidence
- lower chance that a favorable forecast becomes unfavorable
- better estimate of enemy protective coverage
- increased evidence quality when defending against enemy chemical use
- unlocks Seal Operational Area or an equivalent intelligence preparation ability

Tradeoff:

- minimal direct combat stats
- requires a headquarters slot that could hold ordinary reconnaissance or signal staff

### Protective Logistics Section

Role: distribution of masks, filters, suits, antidotes, and warning equipment.

Essential equipment:

- gas-mask equipment
- support equipment
- trucks
- medical supplies abstraction

Effects:

- increases effective military protective coverage for assigned divisions
- reduces mask and filter consumption
- reduces organisation loss from exposure
- unlocks Issue Theater Protective Posture

The company does not protect an order with no mask stockpile.

### Mobile Decontamination Column

Role: clean routes, vehicles, equipment, and concentration points.

Essential equipment:

- decontamination equipment
- trucks
- fuel
- support equipment
- protective equipment

Effects:

- reduces contaminated-state attrition and movement penalties
- accelerates local cleanup in states occupied by the order
- reduces persistent blister-agent effects on assigned divisions
- unlocks Establish Decontamination Corridor

Tradeoff:

- high supply and fuel burden
- loses most effect when the army is encircled or out of supply

### Medical Countermeasure Directorate

Role: antidotes, respiratory care, burn care, casualty sorting, vaccination coordination.

Essential equipment:

- support equipment
- field-hospital equipment or vanilla medical category
- gas-mask equipment
- trucks

Effects:

- reduces military death multiplier after exposure
- improves casualty trickleback for protected units
- reduces medical saturation caused by assigned divisions
- unlocks Mass Antidote and Casualty Response

It cannot prevent casualties from catastrophic unprotected nerve-agent exposure.

### Biological Security Section

Role: surveillance, sample control, quarantine planning, and outbreak containment.

Essential equipment:

- support equipment
- trucks
- medical supplies
- decontamination equipment
- radios

Effects:

- reduces deliberate biological attack success against assigned order areas
- lowers accidental spread after capturing infected territory
- increases outbreak detection speed
- unlocks Seal Infection Corridor

This company is defensive by default. Offensive biological operations require national special projects and policy permission.

## Commander abilities

All Army HQ abilities use the current 1.19 order-scoped unit-modifier system. Exact script keys require local verification.

### Prepare Chemical Offensive

Requirements:

- CBRN Operations Section
- researched agent and delivery method
- minimum Chemical Readiness
- sufficient payload ratio
- assigned order with active divisions
- national policy permits use

Costs:

- command power scaled by battalions affected
- payload stock scaled by divisions and frontage
- gas-mask and filter reserve
- preparation time
- temporary supply burden

Duration:

- preparation phase of 7 to 21 days
- active phase of 3 to 14 days depending on delivery type
- cooldown of 30 to 120 days by severity

Effects:

- enables chosen chemical delivery profile for the order
- grants protected assault and organisation-retention modifiers
- creates enemy exposure when combats meet delivery conditions
- can contaminate friendly territory after forecast failure or retreat

### Issue Theater Protective Posture

Requirements:

- Protective Logistics Section
- minimum gas-mask stockpile

Costs:

- command power
- gas-mask crates and filters
- supply consumption during active alert

Effects:

- faster warning response
- higher respiratory protection
- reduced first-use surprise
- lower movement and attack efficiency because troops operate in masks and suits

The player can activate it preemptively. Long use consumes stock and reduces offensive tempo.

### Establish Decontamination Corridor

Requirements:

- Mobile Decontamination Column
- controlled route through contaminated states
- trucks, fuel, and decontamination equipment

Costs:

- command power
- fuel
- equipment attrition
- temporary movement restrictions around cleanup points

Effects:

- marks a route or state group for priority cleanup
- reduces supply and movement penalties for the assigned order
- accelerates state decontamination
- lowers continuing military deaths

### Seal Operational Area

Requirements:

- Chemical Intelligence and Weather Cell or Biological Security Section
- controlled target area or occupied state

Costs:

- command power
- political and local stability burden
- tied-down units or garrison pressure

Effects:

- reduces civilian movement out of contaminated or infected states
- reduces spread to adjacent states
- increases local economic and resistance pressure
- can improve evidence preservation when used defensively
- can increase Condemnation if used to conceal offensive use or trap civilians

### Mass Antidote and Casualty Response

Requirements:

- Medical Countermeasure Directorate
- medical stock or capacity

Costs:

- command power
- medical capacity
- support equipment and protective stores

Effects:

- reduces nerve-agent military deaths
- reduces organisation loss after exposure
- increases short-term supply consumption
- creates a cooldown before the same headquarters can repeat it

### Seal Infection Corridor

Requirements:

- Biological Security Section
- detected biological contamination or outbreak

Costs:

- command power
- equipment and manpower
- local industry penalty

Effects:

- reduces spread and cross-border movement
- improves surveillance and outbreak response
- increases local resistance and civilian hardship if maintained too long

## HQ statistic philosophy

HQ companies should not add large flat soft attack. Target values are narrow:

- planning speed: 3 to 8 percent
- coordination: 2 to 5 percent
- recon or intel factor: 5 to 15 percent
- contaminated-state attrition reduction: 10 to 30 percent
- exposure mortality reduction: 10 to 30 percent depending on equipment
- friendly-exposure risk reduction: 10 to 35 percent
- operation preparation reduction: 10 to 25 percent

The strongest effects appear only while an ability is active and properly supplied.

## Regimental support companies

### Gas Mask and Decontamination Detachment

Role: general military protection.

Requirements:

- basic gas-mask technology
- gas-mask crates
- support equipment

Effects:

- respiratory protection against choking agents
- modest skin and nerve protection at improved technology levels
- reduced organisation and recovery loss under chemical exposure
- lower military death multiplier
- slight attack, movement, and supply penalty while full protective posture is active

This company is the default defensive choice.

### Chemical Reconnaissance Detachment

Role: detect chemical preparation, mark contaminated routes, sample agents.

Requirements:

- CBRN instruments
- support equipment
- protective equipment

Effects:

- reduces first-use surprise
- identifies agent class more quickly
- improves target and evidence information
- small recon contribution
- helps headquarters select a decontamination route

### Hazard Pioneer Detachment

Role: protected engineers for forts, urban areas, river crossings, and contaminated obstacles.

Requirements:

- engineer equipment
- decontamination equipment
- masks
- support equipment

Effects:

- urban and fort assault utility
- reduced contaminated terrain movement penalty
- local cleanup after combat
- stronger effect when paired with an engineer company

### Chemical Projector Battery

Role: consolidated successor to one support company per Livens agent.

Requirements:

- projector equipment
- selected payload class
- protective equipment
- chemical-ammunition train or prepared headquarters operation for sustained use

Effects:

- short-range chemical delivery in forts and urban combat
- dose and persistence depend on selected payload profile
- vulnerable to counterbattery and poor wind

The player chooses payload through a division profile or operation rather than changing to a different subunit for every agent.

### Chemical Ammunition Train

Role: carry, seal, and distribute chemical artillery ammunition.

Requirements:

- trucks or trains through the appropriate category
- support equipment
- protective equipment
- chemical shell lots

Effects:

- enables chemical artillery fire plans for divisions with line or support artillery
- increases supply use and explosion risk
- loses most effect if essential equipment is disabled or depleted

### Armored Chemical Delivery Detachment

Role: close armored delivery and protected breakthrough.

Requirements:

- selected tank chassis role
- armored delivery equipment
- payload
- masks and decontamination material

Effects:

- rapid delivery in urban and fort combat
- modest battalion adjuster to protected infantry breakthrough
- high maintenance and supply burden
- no parachute eligibility

### Nerve Agent Suppression Detachment

Role: occupation and garrison terror with advanced nerve agents.

Requirements:

- nerve-agent special project
- advanced protection
- national policy permits occupation use
- agent payload

Effects:

- very high suppression
- reduced immediate garrison damage
- state civilian and military deaths
- contamination and medical saturation
- evidence and Condemnation
- delayed resistance radicalisation

It should be blocked from ordinary frontline templates if the engine supports role restrictions. Otherwise, visibility and AI must keep it in garrison-oriented designs.

### Field Epidemiology and Quarantine Detachment

Role: defensive biological surveillance and containment.

Requirements:

- surveillance technology
- support equipment
- trucks
- medical supplies

Effects:

- reduces outbreak spread from the division's state
- improves detection
- helps occupation of infected territory
- modest supply and movement cost

### Medical Countermeasure Detachment

Role: division-level antidotes, respiratory support, burn care, and vaccination.

Requirements:

- field hospital or compatible medical tech
- support equipment
- protective equipment

Effects:

- lower military death multiplier
- improved recovery after exposure
- higher effect against nerve agents with researched antidotes
- complements but does not replace gas masks

### Biological Security Assault Detachment

Role: doctrine-only unit for seizing laboratories, infected facilities, and contaminated urban sites.

Requirements:

- Operations mastery 4
- Biological Security Section at the assigned HQ
- advanced protective equipment
- decontamination equipment

Effects:

- reduced outbreak acquisition after capturing infected states
- evidence preservation
- lower accidental release risk
- modest urban assault utility

## Support grouping and compatibility

Suggested mutual-exclusion groups:

- one offensive chemical delivery detachment per division
- one primary protective detachment per division
- one medical or biosecurity detachment per division unless doctrine mastery expands capacity
- gas-mask protection can coexist with ordinary engineer, recon, signal, logistics, or field-hospital support
- armored chemical delivery can coexist with vanilla flame support only if local balance confirms the combination is not abusive

## Template AI

AI templates use role packages:

- protected line infantry
- protected assault infantry
- chemical artillery formation
- armored chemical breakthrough
- CBRN garrison
- biosecurity occupation force

AI does not add offensive chemical support without:

- payload production
- gas-mask reserve
- national use policy
- doctrine or special project
- a target and operation plan

## Equipment status scaling

Every support company with an adjuster or scripted protection effect needs an essential-equipment floor. Suggested bands:

| Equipment status | Special effect |
| ---: | ---: |
| Below 25 percent | 0 percent and ability blocked |
| 25 to 49 percent | 25 percent effect |
| 50 to 74 percent | 55 percent effect |
| 75 to 89 percent | 80 percent effect |
| 90 percent or higher | 100 percent effect |

The same scale applies to payload, masks, decontamination equipment, and headquarters instruments independently where practical.

## Acceptance criteria

- Every HQ ability names its required HQ company.
- Every ability scales command-power cost by forces affected.
- Every company has essential equipment and shortage behavior.
- Regimental support companies compete with vanilla choices.
- Protection works against all chemical pipelines through one shared helper.
- No company grants broad army-wide attack while unequipped.
- AI can create and supply viable templates.
