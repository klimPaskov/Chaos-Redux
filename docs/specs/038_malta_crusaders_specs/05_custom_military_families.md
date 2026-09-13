# Custom medieval military families

## Non-negotiable implementation rule

The Event 38 military cannot be represented by ordinary infantry divisions with medieval names. Every named family must have an explicit gameplay disposition, concrete equipment relationship, provider registration, presentation, AI use, reinforcement path, counter art, sound roles, and model decision.

The owner is Event 38 and its Malta Crusader country package. Shared consumers can request these families only through owner-side provider callbacks.

## Family inventory

| Family | Disposition | Primary role | Main weakness |
| --- | --- | --- | --- |
| Armored Knights | Standalone line battalion | armoured defence and breakthrough | speed, supply, hard-attack exposure |
| Mounted Knights | Standalone line battalion | mobile breakthrough and exploitation | armour and anti-tank vulnerability |
| Archers | Standalone line battalion | low-fuel soft attack and defence | poor hard attack and penetration |
| Crossbows | Standalone line battalion | stronger piercing and defensive fire | slower training and equipment burden |
| Siege Formations | Standalone line or specialized battalion | fort attack and heavy soft attack | low organization, very slow, high logistics cost |
| Crusader Engineers | Support attachment | forts, crossings, sieges, construction | support equipment and specialist cost |
| Hospitaller Companies | Support attachment | HP, recovery, casualty care | command and equipment cost |
| Anti-Tank Lancers | Support or specialist battalion | short-range anti-armour ambush | fragile against infantry and air attack |
| Mechanized Knight Carriers | Standalone line battalion | late-game mobile armour | fuel, vehicles, industry |
| Blessed Crusader Guard | Elite variant package | organization, recovery, morale | strict cap and legitimacy dependency |
| Supreme Papal Knights | Terminal-only provider family | terminal heavy breakthrough | terminal route only |
| Atlantean Supreme Tanks | Hidden German provider family | exceptional armoured spearhead | initial units hard to replace |

## Owner-side provider contract

Each standalone family needs idempotent callbacks for:

- registration and eligibility
- concrete equipment token publication
- template construction
- spawn construction
- sustainment and reinforcement
- AI template use
- presentation and localisation
- derivative setup
- public-package removal
- cleanup and invalid actor handling
- CXT test-country setup

Support attachments remain inside the parent provider transaction and do not register as independent spawnable families unless a shared consumer genuinely needs them.

The provider must fail closed when equipment, country origin, technology, or actor proof is missing. It must not substitute generic infantry.

## Armored Knights

### Combat identity

Armored Knights are small elite formations built around heavy personal armour, shields, close combat, hardened commanderies, and twentieth-century support elements. Their battlefield role is to hold exposed positions, absorb soft attack, and force local breakthroughs.

### Strengths

- very high HP for an elite battalion
- strong armour relative to ordinary infantry
- strong defence
- strong breakthrough at close range
- high organization when properly led
- good fort and urban combat through route upgrades

### Weaknesses

- very low strategic and tactical speed
- high supply consumption
- expensive heavy armour equipment
- vulnerable to dedicated anti-tank weapons, artillery concentration, and air attack
- poor pursuit capability
- severe terrain penalties in marsh, mountain, and deep desert without support

### Equipment

A concrete **knight armour equipment** family should represent plate, shields, reinforced weapons, radios, protective gear, and the industrial support needed to keep the formation viable. Later marks add modern alloys, shock protection, anti-fragmentation layers, and integrated firearms.

The equipment is not literal medieval plate alone. The visual identity remains medieval while the production cost reflects modern battlefield survival.

### Template limits

The AI and player should not fill entire armies with Armored Knights. A country-level cap should depend on:

- heavy armour production
- order headquarters
- Crusade Authority
- relevant technology
- active principalities
- evolution stage

## Mounted Knights

### Combat identity

Mounted Knights are heavy cavalry and mobile order columns. Early variants use horses, motorcycles, trucks, and light support according to technology. Later variants can transition into mechanized carriers while preserving their order identity.

### Strengths

- high movement for the event's early special forces
- strong breakthrough
- good organization
- rapid exploitation after a siege
- low fuel use in horse-heavy early variants
- strong desert and open-terrain potential with route support

### Weaknesses

- less armour than Armored Knights
- vulnerable to anti-tank and machine-gun fire
- remount and training burden
- weak in fortified urban assaults without support
- supply and horse-loss pressure in famine or disease

### Equipment

Early Mounted Knights use standard infantry weapons plus a concrete **crusader remount and cavalry kit** equipment family only when the engine and provider design justify a separate token. If a separate token would create needless clutter, the family can consume infantry equipment, support equipment, and a provider-owned remount capacity ledger.

Later Mechanized Knight Carriers require a concrete vehicle equipment family.

## Archers

### Combat identity

Archers are manpower-heavy ranged formations used for defensive saturation, low-fuel operations, and soft-target pressure. They are intentionally strange but cannot outperform modern artillery in every role.

### Strengths

- low fuel requirement
- strong soft attack against poorly protected infantry
- useful defence and suppression
- relatively low heavy-industry requirement
- good operations in low-infrastructure areas when supplied locally

### Weaknesses

- poor hard attack
- poor piercing
- vulnerable to armour and air attack
- high manpower use
- limited range compared with artillery
- lower breakthrough

### Equipment

A concrete **war bow equipment** family is appropriate if it includes bows, arrows, protective gear, sights, maintenance, and standardized ammunition. Production costs must prevent limitless free battalions.

Modern upgrades can add incendiary, explosive, smoke, illumination, and signal arrows. Explosive or chemical ammunition requires the relevant technology, treaty, condemnation, and CBRN integration. It is not part of the normal baseline.

## Crossbows

### Combat identity

Crossbows are slower, more equipment-intensive ranged formations with better penetration and defensive fire than Archers.

### Strengths

- higher piercing than Archers
- strong defence
- good ambush and urban utility
- route access to anti-equipment bolts

### Weaknesses

- slower training
- lower organization if massed badly
- more industrial cost
- still poor against modern armour without upgrades

### Equipment

A **crossbow equipment** family can share an archetype with war bows only if technology, production, bonuses, and localisation remain distinct. Do not create two identical equipment tokens merely for names.

## Siege Formations

### Combat identity

Siege Formations use catapults, trebuchets, heavy engineering, demolition, captured artillery integration, and later explosive or incendiary projectiles. They are specialized fortress breakers.

### Strengths

- high fort attack
- strong soft attack against entrenched positions
- building and infrastructure damage in explicit siege actions
- support for river crossing and urban assault through engineers
- high psychological and flavour impact

### Weaknesses

- very slow movement
- low organization
- high transport and supply cost
- vulnerable to counterbattery fire, aircraft, and mobile attack
- poor performance in fast-moving fronts

### Equipment

A concrete **siege engine equipment** family is required. It should represent frames, counterweights, heavy timber, metal fittings, ammunition, tractors or transport, tools, and crews.

Later marks can combine siege identity with conventional artillery or rockets. They do not receive unrestricted artillery stats merely because the visual is a trebuchet.

### State damage

Any building damage from siege actions must use explicit decisions, raids, battle outcomes, or controlled effects. The battalion itself should not silently destroy civilian infrastructure every combat tick.

## Crusader Engineers

### Combat identity

Crusader Engineers are a support company for forts, crossings, coastal landings, siege works, rail repair, and battlefield construction.

### Strengths

- fort attack and defence
- river crossing
- naval invasion support
- entrenchment
- repair and construction mission bonuses
- siege decision efficiency

### Costs

- support equipment
- specialist manpower
- engineer training
- possible trucks and trains for major projects

The support company must use a concrete unlock and CXT setup. It cannot be a renamed vanilla engineer company with no route-specific effects.

## Hospitaller Companies

Hospitaller Companies are support attachments that improve HP, trickleback, recovery, outbreak response, and casualty care. They interact with famine, migration, contamination, and camp discovery only through validated shared adapters.

They should gain unique value in contaminated or diseased regions without making disease irrelevant.

## Anti-Tank Lancers

Anti-Tank Lancers are a later absurd-modern support family. Their equipment combines shaped-charge or explosive lance systems, short-range anti-armour tactics, and mobile assault teams.

They provide meaningful piercing and hard attack in specific conditions but have severe vulnerability, training cost, and reliability risk. They cannot replace ordinary anti-tank production cheaply.

## Mechanized Knight Carriers

This late family carries knight units in armored or half-tracked vehicles with medieval visual motifs. It requires:

- motorization technology
- a dedicated vehicle equipment family
- fuel
- modern workshops
- the relevant focus route
- strong supply

It provides speed, armour, breakthrough, and better combined-arms performance. It is not an early unit.

## Blessed formations

Blessed formations are elite variants created by high Sacred Legitimacy, Evolution III, the Papal route, or the Holy World terminal.

Their effects represent morale, command cohesion, recruitment prestige, recovery, and concentrated equipment. They do not prove supernatural protection.

Rules:

- strict country-level cap
- full manpower and equipment cost
- no free monthly spawning
- losses remain permanent unless replaced
- disbanding does not refund more equipment than remains
- access can be lost when legitimacy collapses, but existing units are not deleted instantly

## Terminal Papal families

The Holy World can unlock:

- Supreme Papal Knights
- Blessed Heavy Cavalry
- Holy Siege Hosts
- Papal Armored Divisions
- multinational Believer armies

Terminal bonuses can be deliberately extreme. The units still require valid templates, equipment, manpower, supply, and a reinforcement route appropriate to the terminal state.

## Atlantean Supreme tanks

The hidden Atlantis package starts with 20 fully equipped formations. The formations use a unique equipment family and an exact one-time transaction.

Rules:

- the first 20 formations are exceptionally strong
- the initial equipment stock is hard to replace
- no repeatable decision can recreate the initial package for trivial cost
- later production requires route technology, dedicated factories, resources, and time
- templates and stockpiles are removed or transferred safely if Atlantis is defeated
- model, counter, sound, and equipment art are unique

## Technology structure

Suggested technology or special-project groups:

1. Order Arms Standardization
2. Modern Plate and Shock Protection
3. Remount and Cavalry Logistics
4. War Bow Production
5. Crossbow Metallurgy
6. Siege Engine Standardization
7. Explosive Siege Ammunition
8. Incendiary Siege Ammunition
9. Anti-Tank Lance Systems
10. Mechanized Knight Carriers
11. Extreme Holy Armour
12. Blessed Command Doctrine
13. Papal Terminal Armaments
14. Atlantean Supreme Armour

The final graph must avoid isolated one-off technologies. Placement, prerequisites, exclusivity, unlocks, bonuses, and icons need MCP technology evidence.

## Production and sustainment

### Cost principles

- special units should be powerful in their intended role
- their production cost must be visible in equipment, manpower, fuel, supply, training, or cap pressure
- low-tech visuals do not justify low industrial cost when the unit survives modern weapons
- no family can bypass resource scarcity without a route tradeoff

### Stockpile helpers

Dynamic stockpile debits should use existing shared removal helpers where supported. New equipment types need owner-side debit helpers only when shared consumers require them.

### Capture and conversion

Captured infantry equipment, artillery, trucks, and armour can be converted into crusader equipment through explicit workshops. Conversion rates depend on technology, industry, order route, and equipment category. The player should see the resource sacrifice before committing.

### Foreign donations

Foreign support sends traceable equipment packages. Donations raise sponsor influence or Sacred Legitimacy and can create political obligations. They are not unlimited free stockpile events.

## Template design

Templates should have distinct roles and combined-arms logic. Examples:

### Armored Knight Banner

- Armored Knights as the core
- Crusader Engineers
- Hospitaller Company
- limited conventional artillery or support weapons

### Mounted Crusader Column

- Mounted Knights
- reconnaissance
- logistics
- optional Anti-Tank Lancers

### Crossbow Levy

- Crossbows or Archers
- ordinary infantry or militia where appropriate
- engineers or field hospitals

### Siege Host

- Siege Formations
- ordinary guard infantry
- engineers
- logistics
- anti-air support when available

### Mechanized Order Column

- Mechanized Knight Carriers
- Armored Knights or motorized support
- logistics
- anti-air and anti-tank

The player can create custom divisions, but AI templates must remain sane and affordable.

## Balance direction

The special families should win through asymmetry:

- Armored Knights punish low-piercing infantry but lose to prepared anti-tank forces.
- Mounted Knights exploit open fronts but struggle in forts and dense urban combat.
- Archers and Crossbows conserve fuel but cannot solve modern armour alone.
- Siege Hosts break forts but are easy to encircle.
- Engineers make campaigns possible but consume scarce support equipment.
- Blessed units create elite concentration, not army-wide invulnerability.

No family should dominate all terrain, all targets, and all resource situations.

## 3D model requirements

Each visually distinct runtime unit needs a model review.

Likely model packages:

- Armored Knight infantry model
- Mounted Knight cavalry model
- Archer or Crossbow model, possibly one family with equipment variants if visually legible
- Siege engine model
- Crusader Engineer model if separate presentation is justified
- Mechanized Knight Carrier vehicle
- Blessed Papal variant where a texture and effect variant is insufficient
- Atlantean Supreme tank

The 3D worker must use Meshy 7, one approved model-ready image, local vanilla scale calibration, PDX material mapping, required skeletal actions, sourced Internet audio, bespoke counters, export, and reimport evidence. Provider success alone is not completion.

## Animation roles

Humanoid units need role-appropriate actions such as:

- idle
- walk
- run where used
- attack or fire
- charge where used
- hit or impact where supported
- death
- special action only when consumed

Mounted, siege, and vehicle models need domain-specific actions. No role can be satisfied by renaming another clip. Attack actions need visible aim or preparation, discharge or strike, recoil or impact, and recovery where applicable.

## Sound roles

Every custom unit needs legally usable Internet-sourced audio with provenance. Required roles include:

- selection
- acknowledgement
- movement
- idle or machinery loop where applicable
- attack
- impact
- special action
- death or destruction

Generated, synthesized, recorded, placeholder, and unlicensed audio are forbidden.

## Counter requirements

Every custom unit must have bespoke counter art for every counter surface it uses. Counter production must inspect the exact installed-vanilla definition and DDS, the matching skill-local reference family, canvas, frame count, alpha treatment, border, silhouette, and sampled vanilla green palette.

Reused or renamed counters do not satisfy the requirement.

## CXT coverage

Each new land sub-unit and concrete equipment token needs:

- a modifier-free hidden-idea carrier
- an idempotent `_apply` setup effect
- bounded startup registration
- tag-scoped daily repair for existing saves
- weekly maintenance only when genuinely required
- documentation in the CXT test-country contract

The final inventory audit must cover every Event 38 sub-unit, support company, archetype, concrete equipment token, provider callback, presentation token, and CXT registration.

## Completion evidence

The military package is incomplete until all of these exist:

- concrete sub-unit definitions
- equipment definitions and script enums where required
- technologies and doctrines
- owner provider registrations
- templates and AI use
- production and sustainment
- decisions and focus unlocks
- localisation and icons
- counters
- 3D models and animations
- sourced audio
- CXT setup
- exact equipment debit and spawn safety
- removal and cleanup
- MCP technology evidence
- live runtime consumers ready for user validation
