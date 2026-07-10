# UI, Localisation, Assets, and Achievements

## CBRN Operations interface

The main player-facing surface is a CBRN Operations category or custom window opened from decisions. It complements the Chaos Meter tabs rather than replacing them.

## Tabs

### Arsenal

Shows:

- chemical payload by class and agent
- chemical shell lots
- chemical air payload
- biological payload
- stockpile risk
- current production
- conversion and disposal actions

### Protection

Shows:

- gas-mask stockpile
- military reserved crates
- civilian distributed crates
- national military coverage
- selected state civilian coverage
- filter replacement demand
- decontamination and medical capacity

### Operations

Shows:

- active CBRN headquarters
- selected army order
- available commander abilities
- prepared raids
- payload ratio
- forecast confidence
- friendly-exposure risk
- operation cooldowns

### Contamination

Shows:

- contaminated and infected states
- severity class
- continuing deaths
- medical saturation
- cleanup progress
- spread risk
- active quarantine or decontamination actions

### International Response

Shows:

- public Condemnation
- source breakdown
- evidence and attribution state
- current tier
- sanctions and participants
- inspections, compliance, denial, and retaliation options

The existing Chaos Meter Condemnation, Deaths, and Air Cleanliness tabs remain authoritative global summaries. The CBRN window provides operational detail.

## Interface states

- no program
- defensive preparation
- offensive program available
- operation preparing
- operation active
- protection shortage
- contamination emergency
- outbreak emergency
- sanctions escalation
- doomsday authorization

The UI should hide irrelevant actions by state, policy, doctrine, and target rather than listing every possible operation.

## Dynamic values and tooltips

Every visible value needs:

- current value
- short description
- main sources of gain and loss
- next threshold
- current penalties or unlocks
- selected target or order context

Use integer formatting for coverage, readiness, contamination, and evidence unless fractional precision changes a decision.

## Decision categories

### CBRN Program Management

Long-term policy, production, stockpile, disposal, inspection, and designer actions.

### Civil Defence and Protective Distribution

State-targeted masks, shelters, hospitals, filters, and emergency response.

### Chemical Operations

Prepared artillery, armored, air, and headquarters-linked operations.

### Biological Operations and Containment

Special-project strikes, covert operations, quarantine, surveillance, and countermeasures.

### Occupation CBRN Measures

Nerve suppression and protected occupation, visible only when relevant.

Categories should use phase and target filters. They must not become flat stores.

## Localisation direction

This package does not provide final player-facing copy.

### Doctrine text

Direction:

- military planning and institution language
- concrete references to masks, shell filling, protected routes, headquarters, and contamination
- avoid generic apocalyptic wording
- avoid glorifying mass civilian harm
- distinguish professional command routes from reckless terminal routes

### Chemical attack text

Direction:

- describe visible exposure, evacuation, medical burden, battlefield confusion, and contaminated terrain
- do not present use as a simple stat bonus
- options can range from controlled military language to self-condemning extremist policy

### Biological text

Direction:

- describe symptoms, isolation, movement control, laboratory and medical response
- preserve uncertainty before attribution and outbreak confirmation
- do not announce hidden incubation values

### Civil defence text

Direction:

- practical distribution, fitting, warning, shelter, hospital, and replacement language
- show equipment and population cost clearly

### Condemnation text

Direction:

- name the public evidence, deaths, contamination, inspections, and sanctions
- do not imply doctrine makes confirmed responsibility disappear

### Tooltips

Requirements should be icon-first and concise. Long dynamic requirements belong in a breakdown tooltip.

## Asset plan

All visible assets require source PNG, processed PNG, final DDS, manifest entry, and GFX handoff through the asset skill.

### Doctrine icons

- Chaos Warfare grand doctrine
- four track adoption icons
- twenty mastery reward icons
- four milestone icons

The current icons can be audited for reuse. New concepts need new final art.

### Technology icons

- four gas-mask models
- decontamination equipment line
- CBRN instruments
- chemical shell filling
- armored delivery
- sealed tank crews
- chemical air interdiction
- theater CBRN headquarters
- Chaos Assault Battalion
- Hazard Pioneer
- Nerve Suppression Detachment
- Biological Security Assault Detachment
- medical countermeasure technologies

### Unit and support icons

- six Army HQ support companies
- ten regimental support companies
- Chaos Assault Battalion
- optional Hazard Pioneer Battalion

Each support type needs its own icon composition. Do not resize one focus icon to serve as an idea, decision, and unit icon.

### Equipment art

- gas-mask crate models
- decontamination equipment models
- CBRN instruments
- chemical shell lots
- armored delivery equipment
- chemical air payload
- biological payload variants

### Decision icons

- establish reserve
- civilian distribution
- emergency distribution
- filter replacement
- protective posture
- prepared chemical offensive
- decontamination corridor
- chemical artillery fire plan
- chemical air raid
- biological raid
- outbreak operation
- quarantine
- vaccination
- antibiotics
- inspection
- stockpile destruction
- retaliation policy
- nerve suppression
- protected occupation

### Category and UI assets

- CBRN program category icon
- civil defence category icon
- chemical operations category icon
- biological operations category icon
- occupation CBRN category icon
- window background and header
- readiness meter
- protection meter
- contamination severity frames
- evidence and attribution icons
- operation status seals
- warning overlays
- target-state cards

### State modifier icons

- Trace contamination
- Local contamination
- Serious contamination
- Severe contamination
- Catastrophic contamination
- medical saturation
- active quarantine
- decontamination corridor
- civilian mask coverage
- outbreak intensity bands

### Designer icons

- Protective Equipment Consortium
- Chemical Munitions Combine
- Mobile Decontamination Works
- Aerosol and Air Delivery Bureau
- Biological Security Directorate
- Medical Countermeasure Directorate

Country-specific final assets can use existing company logos where source and style support it.

## Animation planning pass

A major mechanic window benefits from restrained state animation.

### Animated CBRN readiness seal

Use:

- slow four-to-eight frame pulse when an operation is ready
- warning variation when payload or protection is insufficient
- critical variation during contamination emergency

Requirements:

- real per-frame source art
- static fallback
- horizontal frame sheet
- GIF preview only for review
- verified current GUI wiring

### Contamination warning border

A subtle state-driven frame for Severe or Catastrophic contamination. It should not pulse continuously at lower levels.

### Operation preparation indicator

A small progress animation for headquarters operation preparation.

Static presentation remains better for stockpile values, death totals, and long lists.

## Report and news images

Normal tactical use does not need a popup image for every operation. Major public thresholds can use report or news images:

- first confirmed chemical use
- first strategic chemical air raid
- first confirmed biological attack
- catastrophic civilian protection failure
- international inspection of stockpiles
- mass decontamination effort
- CBRN doomsday release

Historical real scenes use sourced archival material. Alternate or fictional operations can use generated period-documentary art. Follow the asset skill source rules.

## Achievement set

Working labels are not final localisation.

### The Air Is Still Breathable

Requirement direction:

- survive a major war after confirmed enemy chemical use
- maintain high military protection
- keep national Air Cleanliness contribution below a strict limit
- no offensive chemical first use

Difficulty: hard.

### Masks Before Guns

Requirement direction:

- reach high civilian coverage in every core state before any chemical attack lands
- maintain a minimum military reserve

Difficulty: hard for a large country.

### The Prepared Army

Requirement direction:

- field several fully equipped protected armies with CBRN headquarters
- repel a chemical offensive with low military deaths

### A Poisoned Victory

Requirement direction:

- win a major war through Chaos Warfare operations
- end above a high Condemnation tier
- suffer meaningful contamination or sanctions

This is an intentionally costly victory achievement.

### Clean Hands, Dirty Work

Requirement direction:

- conduct covert chemical or biological operations without public confirmation for a long period
- disqualify on discovered coverup before the end condition

Hidden achievement.

### The Evidence Survives

Requirement direction:

- capture an enemy CBRN facility with a Biological Security Assault Detachment
- preserve evidence
- trigger international action against the responsible country

### No Wind Is Friendly

Requirement direction:

- suffer forecast failure during a prepared chemical offensive
- recover the army and win the affected battle or campaign without another chemical use

### The Antidote Arrived

Requirement direction:

- contain a severe nerve-agent attack with advanced masks, medical countermeasures, and decontamination
- keep deaths below a strict threshold

### Quarantine Without Collapse

Requirement direction:

- contain a catastrophic biological outbreak before it spreads outside the original country
- maintain stability and supply thresholds

### The Arsenal Dismantled

Requirement direction:

- reach a high Condemnation tier
- accept inspection
- destroy offensive stockpiles
- return to a low tier without regime change or defeat

### Terminal Contagion

Requirement direction:

- complete all four Chaos Warfare tracks
- field doctrine-only formations
- execute a capstone operation
- survive the resulting sanctions and contamination

### A Mask for Every Door

Requirement direction:

- as Britain or another mass civil-defence profile, reach near-total civilian coverage and aid several allies before first confirmed chemical use

### The Weapon Turns Home

Requirement direction:

- suffer a major domestic accident from an offensive stockpile
- contain it
- later dismantle or reform the program

### Unbroken Supply Corridor

Requirement direction:

- maintain a decontamination corridor through several contaminated states for a sustained offensive
- keep assigned army supply above a threshold

### The First User Pays

Requirement direction:

- as a retaliation-policy country, defeat the first confirmed chemical user without conducting a strategic civilian chemical or biological attack

## Achievement tracking

Achievements require:

- start-country or route eligibility
- use-policy memory
- first-use and retaliation flags
- coverage records
- death thresholds
- contamination records
- operation completion
- Condemnation peaks
- disqualifiers for doomsday or prohibited actions

Do not make achievements unlock merely because a technology or doctrine was selected.

## Documentation

Update:

- core mechanics guide
- chemical warfare documentation
- biological warfare documentation
- Condemnation impact spec references
- Deaths and Air Cleanliness docs
- Army HQ and support-company docs
- equipment and technology docs
- AI program docs
- asset manifest
- achievement docs

The event catalog spreadsheet does not require a new event row unless the implementation creates actual event chains. Relevant existing event rows must be updated if their behavior changes.

## Accessibility and clarity

- use distinct icons and text, not color alone
- show agent class and severity with words
- avoid rapid full-screen flashing
- keep animations subtle
- show death and Condemnation warnings before irreversible actions
- provide static fallback for every animation

## Acceptance criteria

- the player can understand stockpile, protection, operation, contamination, and consequence from the UI
- categories hide irrelevant actions
- every visible new concept has an asset entry
- animation clarifies state rather than decorating every icon
- achievements cover defense, offense, cleanup, diplomacy, and rare failures
- final localisation is written in-world during implementation
