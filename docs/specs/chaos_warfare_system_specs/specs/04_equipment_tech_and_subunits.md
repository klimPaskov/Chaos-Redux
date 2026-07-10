# Equipment, Technologies, and Subunits

## Equipment design principles

- Equipment represents production and logistics, not individual toxicology simulation.
- Similar agent variants share chassis and subunit definitions.
- Doctrine-only units require protective and specialist equipment, not every payload in the game.
- Offensive delivery consumes payload through operations, reinforcement, or ammunition lots.
- Defensive protection has ongoing filter and replacement costs.
- New equipment categories must be added to `common/script_enums.txt` in the implementation change.

## Protective equipment

### Gas Mask Equipment

Archetype: `gas_mask_equipment`

Models:

1. Basic Respirator Crate, 1918
2. Improved Service Mask Crate, 1936
3. Advanced CBRN Protective Set, 1940
4. Doctrine or special-project Sealed Protective Set, 1942

One equipment item is a standardized crate, not one literal mask. It supports civilian distribution, military issue, filters, fitting, training, and replacements.

Target production characteristics:

| Model | Relative IC | Reliability | Main improvement |
| --- | ---: | ---: | --- |
| Basic | 1.0 | 0.70 | Choking-agent respiratory protection. |
| Improved | 1.35 | 0.82 | Better fit, filters, warning kit, modest blister protection. |
| Advanced | 1.80 | 0.90 | Strong respiratory protection, protective clothing, nerve countermeasure compatibility. |
| Sealed set | 2.50 | 0.94 | Vehicle and assault-team use, highest military protection. |

The actual IC values must be tuned against infantry and support equipment after inspecting vanilla production.

### Decontamination Equipment

Archetype: `decontamination_equipment`

Represents pumps, sprayers, bleaching agents, absorbents, detection paper, wash equipment, sealed containers, and protective tools.

Models:

- field decontamination kit
- mobile decontamination plant
- advanced rapid decontamination set

Used by Hazard Pioneers, Mobile Decontamination Columns, civilian cleanup decisions, and biological containment.

### CBRN Instruments

Archetype: `cbrn_instrument_equipment`

Represents detection instruments, meteorological equipment, sampling kits, radios, mapping material, and laboratory field sets.

Used by headquarters weather cells, chemical reconnaissance, biosecurity sections, and evidence teams.

### Medical Countermeasure Stores

Prefer a scripted capacity backed by support equipment and medical decisions unless the engine and existing mod pattern support a clean equipment archetype. If implemented as equipment, use `cbrn_medical_equipment` and include antidote, respiratory, burn, and vaccination categories through technology profiles.

No local substitute should be implemented before checking the existing field-hospital and medical-equipment patterns.

## Offensive payload equipment

### Strategic Chemical Payload

The existing cylinder equipment can remain as the primary agent stockpile during migration.

Recommended consolidation:

- choking-agent payload
- blister-agent payload
- nerve-agent payload
- incapacitants and malodor payload

Individual historical agents can remain technologies and equipment variants when they produce meaningful differences. The system should not require a separate support-company definition for each variant.

### Chemical Shell Lots

Archetype: `chemical_artillery_ammunition`

Purpose:

- represents filled artillery shells and rocket or projector ammunition
- consumed by prepared fire plans
- created from strategic payload and artillery production capacity
- uses selected agent profile

The country chooses a filling program. Conversion decisions consume strategic payload and artillery stock or production burden. Shell lots are easier to use tactically but create storage and accident risk near the front.

### Armored Delivery Equipment

Archetype or module family: `armored_chemical_delivery_equipment`

Possible implementation:

- tank module that marks an eligible chassis as a chemical delivery vehicle
- dedicated support-equipment archetype paired with normal chassis
- role-based subunit that consumes a normal tank category and payload

The implementation agent must choose the pattern that best fits current 1.19 tank-designer and regimental-support behavior.

### Air Chemical Payload

Chemical aircraft modules remain design components. Their actual toxic payload is consumed through an operation budget or dedicated air payload stock.

Recommended equipment:

- chemical air payload lot by agent class

A mission or raid reserves payload before launch. Failed or intercepted raids consume part or all of it according to outcome.

## Biological payload equipment

Retain agent-specific payloads where spread profiles differ materially:

- anthrax payload
- plague payload
- tularemia payload
- smallpox payload
- weaponized-zombie payload, isolated from ordinary biological systems

Production must require completed special projects. Storage increases accident risk unless containment safety and Biological Security are adequate.

## Technology architecture

### Protective branch

1. Basic Gas Masks, 1918
2. Improved Service Masks, 1936
3. Advanced Protective Clothing, 1940
4. Sealed Assault Protection, doctrine-only or special project, 1942
5. Military Filter Standardization
6. Civil Defence Fitting and Registration
7. Rapid Filter Replacement
8. Vehicle Overpressure and Sealed Compartments

### Detection and forecast branch

1. Portable Anemometers
2. Meteorological Stations
3. Upper-Air Soundings
4. Chemical Detection Paper
5. Mobile Sampling Laboratories
6. Theater Forecast Fusion, doctrine-only
7. Remote Contamination Reconnaissance

### Decontamination branch

1. Field Decontamination Kits
2. Mobile Wash Columns
3. Route Decontamination Planning
4. Rapid Vehicle Decontamination
5. Persistent Agent Neutralization
6. Biological Site Sterilization

### Chemical delivery branch

1. Projector Equipment
2. Improved Projectors
3. Advanced Projectors
4. Chemical Artillery Shells, doctrine-only
5. Persistent Agent Shell Filling, doctrine-only
6. Armored Agent Delivery, doctrine-only
7. Chemical Air Payload Modules
8. Chemical Air Interdiction, doctrine-only

### Medical branch

1. Respiratory Casualty Treatment
2. Burn and Blister Treatment
3. Dimercaprol Countermeasure
4. Nerve-Agent Antidote Kits
5. Mass Casualty Sorting
6. Mobile CBRN Hospitals
7. Vaccination Production
8. Antibiotic Distribution

### Biological security branch

1. Pathogen Handling Protocols
2. Sealed Containment Laboratories
3. Fail-Safe Containment Facilities
4. Biological Surveillance Networks
5. Rapid Outbreak Response
6. Integrated Epidemic Control
7. Field Epidemiology Teams
8. Biological Security Assault Detachment, doctrine-only

## Doctrine-only technology details

### Chaos Assault Battalion

Unlock condition: Infantry mastery 3.

Enables a line special-forces battalion with protected assault role.

Target profile:

- combat width comparable to ordinary specialist infantry, not 2-width stat compression
- manpower around a reinforced battalion
- organisation below ordinary infantry but high enough to function
- high supply and support-equipment burden
- urban, fort, forest, jungle, and marsh utility
- open-terrain and prolonged defensive weakness
- special-forces cap use

Essential equipment:

- infantry equipment
- support equipment
- gas-mask equipment
- decontamination equipment
- CBRN instruments

No biological bomb requirement.

### Improved Chaos Assault Equipment

Unlock condition: Chaos Assault Battalion and Infantry mastery 5.

Adds:

- better breakthrough
- organisation retention under exposure
- reduced friendly-exposure deaths
- improved contaminated-route movement

It should not add another 30 percent universal soft attack.

### Hazard Pioneer Formation

Unlock condition: Infantry mastery 2.

Enables Hazard Pioneer regimental support and possibly a small line pioneer battalion if vanilla structure supports a useful role.

### Chemical Artillery Shells

Unlock condition: Combat Support mastery 3.

Enables shell-lot production, ammunition-train support, and prepared fire plans.

### Persistent Agent Shell Filling

Unlock condition: Combat Support mastery 4 and blister-agent technology.

Increases persistence and route denial while increasing cleanup cost, delayed deaths, and evidence.

### Armored Agent Delivery

Unlock condition: Armor mastery 2.

Enables role-based armored delivery subunits or modules.

### Sealed Tank Crews

Unlock condition: Armor mastery 1 and advanced protective technology.

Reduces crew exposure and vehicle contamination effects at increased production and maintenance cost.

### Nerve Suppression Detachment

Unlock condition: Armor mastery 3 and nerve-agent special project.

Enables garrison-oriented suppression support with severe consequences.

### Mobile Decontamination Columns

Unlock condition: Operations mastery 3.

Enables HQ support and route cleanup ability.

### Chemical Air Interdiction

Unlock condition: Operations mastery 4 and chemical air modules.

Enables reliable operation or raid integration, payload reservation, and ground-exploitation coordination.

### Theater CBRN Headquarters

Unlock condition: doctrine milestone 4.

Improves headquarters ability capacity, operation information, and simultaneous protection and cleanup. It should require advanced radios, CBRN instruments, masks, decontamination equipment, trucks, and medical preparation.

### Biological Security Assault Detachment

Unlock condition: Operations mastery 4 and biological security technology.

Defensive capture and containment role. It does not automatically enable offensive bioweapon use.

## Subunit architecture

### Line battalions

- Chaos Assault Battalion
- optional Hazard Pioneer Battalion after local validation

The doctrine should not add a separate line battalion for every agent.

### Regimental support

- Gas Mask and Decontamination Detachment
- Chemical Reconnaissance Detachment
- Hazard Pioneer Detachment
- Chemical Projector Battery
- Chemical Ammunition Train
- Armored Chemical Delivery Detachment
- Nerve Agent Suppression Detachment
- Field Epidemiology and Quarantine Detachment
- Medical Countermeasure Detachment
- Biological Security Assault Detachment

### Army Headquarters support

- CBRN Operations Section
- Chemical Intelligence and Weather Cell
- Protective Logistics Section
- Mobile Decontamination Column
- Medical Countermeasure Directorate
- Biological Security Section

## Equipment needs and scale

Recommended first-pass division requirements:

| Unit | Masks | Decon | Instruments | Support equipment | Vehicles | Payload |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Gas Mask Detachment | 80 to 120 crates | 5 to 15 | 0 to 5 | 20 to 40 | 0 to 10 trucks | none |
| Chemical Recon | 15 to 30 | 5 to 10 | 20 to 40 | 30 to 50 | 5 to 15 trucks | none |
| Hazard Pioneer | 40 to 70 | 30 to 60 | 5 to 15 | 40 to 70 | 10 to 25 trucks | optional operation use |
| Projector Battery | 20 to 40 | 10 to 20 | 5 to 10 | 20 to 40 | 0 to 15 | 40 to 100 lots |
| Ammunition Train | 20 to 40 | 15 to 30 | 5 to 10 | 30 to 60 | 30 to 80 trucks or train burden | 80 to 200 shell lots |
| Armored Delivery | 15 to 30 | 10 to 20 | 5 to 10 | 20 to 40 | 12 to 20 eligible tanks | 40 to 120 lots |
| Nerve Suppression | 30 to 50 | 20 to 40 | 10 to 20 | 30 to 50 | 10 to 25 trucks | 20 to 60 nerve lots |
| Chaos Battalion | 80 to 120 | 40 to 80 | 10 to 20 | 60 to 100 | 20 to 40 trucks | supplied through attached delivery or operation |

These are planning bands. Exact values must be normalized against vanilla regimental support and division equipment totals.

## Payload profile selection

The selected profile can be represented by country flags, division profile, operation state, or a scripted equipment family. The implementation must avoid requiring the player to rebuild a template every time the agent changes.

Suggested profiles:

- choking
- blister
- nerve
- incapacitants
- no offensive payload

The UI shows which profile a prepared order will use.

## Equipment consumption

### Standing issue

Masks, decontamination equipment, and instruments reinforce units like ordinary equipment.

### Operational expenditure

Payloads and chemical shell lots are reserved and consumed by decisions or commander abilities. Additional loss occurs from:

- enemy air or artillery interdiction
- forecast failure
- overrun supply depots
- contaminated storage accidents
- retreat

### Filter consumption

Active protective posture consumes a small recurring fraction of mask crates. Actual enemy exposure increases consumption. Tropical, desert, and contaminated conditions increase replacement demand.

## Conversion and legacy cleanup

- Legacy agent-specific Livens support companies become hidden compatibility units.
- Legacy agent-specific chemical tank companies become hidden compatibility units.
- A one-time migration effect can replace them in AI and starting templates with consolidated roles.
- Legacy payload cylinders convert to class stockpiles or remain valid inputs for the selected profile.
- The current Chaos Battalion is replaced or migrated through a hidden technology and template conversion.
- Existing technology identifiers can remain aliases when removing them would break saves or focuses.

## Designer integration

Equipment uses MIO or designer families described in the country and designer spec. Protective equipment, decontamination vehicles, chemical munitions, air dispersal, and biological security need separate trait identities.

## Acceptance criteria

- Gas masks exist as equipment with a visible stockpile.
- Military protection falls when equipment falls.
- Civilian distribution consumes the same stock family.
- Chemical aircraft and artillery consume payloads through operations.
- Unit definitions are role-based, not agent-by-agent duplication.
- Chaos Battalion no longer requires every chemical and biological payload.
- All new equipment categories are registered and localized.
- AI production plans cover protection before offensive delivery.
