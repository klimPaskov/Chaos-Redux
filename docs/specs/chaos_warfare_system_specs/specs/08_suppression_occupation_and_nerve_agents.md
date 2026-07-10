# Suppression, Occupation, and Nerve Agents

## Design boundary

Nerve-agent suppression belongs to military occupation and carries severe civilian consequences. Camp and genocide crisis systems retain separate ownership. The mechanic can create atrocity evidence and connect to discovered mass-death systems. It does not unlock extermination infrastructure or normalize historical genocide terminology as a doctrine reward.

## Nerve Agent Suppression Detachment

### Role

A regimental or garrison support detachment that uses controlled nerve-agent release, contaminated barriers, sealed teams, and terror to disrupt resistance networks.

### Unlocks

- Chaos Warfare armor mastery 3
- completed nerve-agent special project
- advanced protective equipment
- national policy permitting occupation use

### Equipment

- gas-mask equipment
- decontamination equipment
- CBRN instruments
- support equipment
- trucks
- nerve-agent payload

### Direct military profile

- high suppression contribution
- small garrison damage reduction while supplied
- low ordinary combat utility
- high supply and equipment burden
- strong effect scaling with payload and protective status

The detachment should not provide a large frontline soft-attack modifier.

## Occupation-use decision

The player does not gain passive nerve-agent effects merely by adding the detachment to a template. A targeted occupation decision authorizes use in a state.

Requirements:

- occupied non-core state with resistance above a threshold
- garrison template contains the detachment or a qualifying CBRN unit is present
- payload stockpile
- national policy permits use
- no active cooldown in the state

Costs:

- nerve-agent payload
- gas-mask and decontamination equipment
- command power or local security capacity
- political and diplomatic risk
- temporary local output loss

## Immediate effects

- large resistance reduction
- reduced resistance target for a short period
- lower immediate garrison damage
- local movement and organisation disruption for hostile units
- state contamination
- civilian and military deaths
- medical saturation
- evidence generation
- chemical Condemnation

## Delayed effects

- resistance radicalisation after the initial shock
- sabotage or partisan recruitment in neighboring states
- foreign intelligence and propaganda interest
- refugee or migration pressure if the relevant system exists
- coverup pressure if the user attempts concealment
- stronger discovery effect when an enemy later occupies or liberates the state

This prevents nerve suppression from becoming a permanent low-cost suppression exploit.

## Suppression balance

Suggested target bands for a fully supplied detachment:

- suppression equivalent: high enough to reduce garrison manpower need by roughly 15 to 30 percent in the targeted state
- garrison damage reduction: 10 to 25 percent during the immediate operation
- duration: 30 to 90 days
- state cooldown: 180 to 365 days
- national repeated-use pressure: escalates after every use within two years

The exact subunit suppression stat should remain moderate. The targeted decision creates the severe temporary effect. This keeps one detachment from providing limitless suppression in every occupied state without payload use.

## Death model

### Exposed population

Operation scale determines the exposed share. It should usually be 2 to 10 percent of the target state's population, rising for dense urban or catastrophic use.

### Immediate deaths

Before protection and medical reduction:

- controlled operation: 0.005 to 0.015 percent of exposed population
- severe operation: 0.015 to 0.05 percent
- catastrophic operation: 0.05 to 0.15 percent

The upper band is reserved for extreme routes and should create major evidence, resistance, and Condemnation.

### Continuing deaths

Short continuing deaths can occur for one to four weeks from contaminated sites, delayed treatment, and medical saturation. Nerve agents should not produce the same long persistence as blister agents unless a specific delivery profile justifies it.

## Protection

Occupying forces need advanced masks, sealed teams, antidotes, and decontamination. Low protection can kill or disable garrison forces and contaminate friendly supply routes.

Civilian masks reduce inhalation exposure but do not provide complete nerve protection. Medical countermeasures and rapid warning are important.

## Resistance response

### Immediate suppression

Resistance strength and activity fall sharply during the operation.

### Radicalisation memory

The state stores a bounded `nerve_suppression_trauma` or equivalent. It affects:

- future resistance growth
- foreign support acceptance
- compliance gain
- liberation reactions
- discovery evidence

Trauma decays slowly or is addressed through compensation, medical relief, inspections, or regime change.

### Neighbor spillover

High-severity use can raise resistance or foreign pressure in neighboring occupied states. This should be event-driven and capped.

## Occupation laws

The redesign should not add a generic law named after concentration systems.

Possible military occupation law or policy, working label only:

### CBRN Coercive Security

Effects while active:

- permits nerve suppression decisions
- modest suppression bonus
- higher garrison supply and protective-equipment use
- reduced compliance growth
- higher resistance radicalisation after use
- higher evidence and Condemnation exposure

The law is visible only after the doctrine unlock and should be AI-gated.

A defensive occupation policy can also exist:

### Protected Occupation Administration

- equips garrisons and civilians for contaminated territory
- improves compliance and lowers deaths
- increases mask and decontamination cost
- blocks offensive nerve suppression

## Agent handling and storage

Occupation units draw payload from a theater reserve. Large reserve near occupied populations increases accident and capture risk.

Possible incidents:

- leaking depot
- stolen cylinders
- partisan attack on storage
- captured records
- accidental friendly exposure
- black-market diversion

Biosecurity and Chemical Readiness reduce risk.

## Evidence and discovery

Evidence quality rises through:

- recovered agent samples
- mass casualties
- hospital records
- captured orders
- storage sites
- foreign observers
- liberated contaminated facilities
- coverup attempts

The responsible country is stored on the state at use time. Later occupation or liberation can attribute the act correctly even if control changes.

## Coverup decisions

### Seal the state

Reduces short-term evidence spread. Increases local output loss, resistance, and coverup pressure.

### Destroy contaminated records

Can lower immediate evidence. Later discovery adds coverup Condemnation and stronger atrocity response.

### Admit accidental release

Creates immediate chemical Condemnation but lowers coverup pressure and can unlock medical aid.

### Permit inspection

Consumes political control and can expose stockpiles. Reduces long-term suspicion if the inspection is credible.

## Condemnation

Nerve suppression contributes to:

- chemical source bucket
- atrocity source bucket when civilian mass death or deliberate population targeting is confirmed
- coverup bucket when concealment is discovered

The system should avoid double counting the same deaths at full value in every bucket. Chemical source records the weapon use. Atrocity and coverup add smaller contextual components.

## AI behavior

AI uses nerve suppression only when:

- doctrine and special project are complete
- resistance is high and strategically important
- ordinary garrison methods are failing
- it has advanced protection and payload
- country profile accepts the political risk
- sanction vulnerability is tolerable
- use does not threaten allied or core populations

AI refusal conditions:

- democratic or defensive posture without an extreme route
- active compliance or inspection agreement
- low payload or mask reserve
- high current Condemnation and fragile trade dependence
- likely liberation or loss of the state
- insufficient garrison protection

High-chaos, radical, or near-collapse AI can ignore some refusal conditions. It should still calculate self-harm.

## Counterplay

Victim and foreign countries can:

- supply protective equipment to occupied populations
- support resistance and evidence recovery
- infiltrate storage depots
- expose medical records
- demand inspections
- sanction the responsible country
- target chemical units and supply nodes
- prepare decontamination and medical relief for liberation

## Connections to camp and genocide systems

Connections occur through:

- shared Deaths tracker
- state responsible-country pointer
- evidence quality
- atrocity and coverup Condemnation
- discovery on liberation
- restricted chemical-site exposure

The doctrine does not create camps, extermination buildings, or experiment sites. Those remain owned by their existing crisis systems.

## Acceptance criteria

- nerve suppression has strong short-term suppression value
- it consumes payload and protection
- it causes state deaths and contamination
- it creates resistance trauma and delayed backlash
- it can create chemical, atrocity, and coverup consequences without full double counting
- it remains separate from genocide infrastructure
- AI does not use it casually
- player tooltips make deaths and diplomatic risk explicit
