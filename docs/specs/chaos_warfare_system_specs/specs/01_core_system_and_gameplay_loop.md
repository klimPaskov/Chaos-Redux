# Chaos Warfare Core System and Gameplay Loop

## Design promise

Chaos Warfare is the doctrine for a state that intends to plan, supply, deliver, survive, exploit, and politically absorb unconventional warfare at theater scale.

A country that adopts it gains tools that ordinary doctrine users cannot reproduce through one research node or one support company. It can prepare an Army Headquarters for a contaminated offensive, choose an agent class, equip divisions for protection, deliver agents through artillery, armor, aircraft, raids, or covert operations, isolate affected terrain, and exploit the disruption before the battlefield recovers.

The power is conditional. A country that lacks protective equipment, payloads, decontamination capacity, medical preparation, or political tolerance can cripple its own army and economy. A country that uses weapons repeatedly can cause real civilian and military deaths, persistent contamination, outbreaks, evidence, Condemnation, sanctions, coalition responses, and retaliation.

## Player loop

### 1. Establish a national program

The player chooses a policy posture before normal use becomes practical:

- defensive preparedness
- retaliatory reserve
- limited battlefield authorization
- unrestricted theater use
- covert biological capability
- civil-defence priority

The posture controls AI willingness, decision visibility, public doctrine, treaty response, and the rate at which evidence becomes politically damaging.

### 2. Build protective capacity

The player researches protective equipment, produces gas-mask crates, assigns military protection companies, creates civilian reserves, builds decontamination equipment, and develops medical countermeasures.

Protection is never a free passive percentage. It is supplied through equipment and support formations. When masks or filters run out, protection falls.

### 3. Build a delivery system

The player chooses which delivery roles to support:

- projector and mortar batteries
- chemical artillery ammunition
- armored delivery vehicles
- chemical aircraft
- strategic raids
- clandestine outbreak operations
- doctrine-only assault formations

The player does not need every agent or every delivery method. Specialisation is cheaper and more reliable than trying to maintain a universal arsenal.

### 4. Prepare an operation through Army Headquarters

The strongest battlefield effects require an Army Headquarters company and a commander ability. The headquarters selects an order, verifies stockpile and protective coverage, calculates weather and intelligence quality, spends command power and payloads, then applies an order-scoped preparation state.

The player sees:

- divisions covered by the headquarters
- current protective coverage
- payload requirement
- forecast confidence
- expected contamination class
- friendly-exposure risk
- likely evidence and Condemnation band
- operation duration and cooldown

### 5. Deliver and exploit

Delivery creates an exposure event. Exposure affects units, state population, supply, movement, organisation, entrenchment, reinforcement, and medical burden according to agent class, dose, weather, terrain, and protection.

The immediate combat bonus is smaller than the current broad doctrine modifiers. The decisive power comes from temporary enemy disruption and the ability to coordinate protected assault units into the affected area.

### 6. Contain the aftermath

The user can:

- withdraw before friendly exposure worsens
- establish a decontamination corridor
- distribute replacement filters
- open field hospitals
- isolate contaminated supply hubs
- clean priority states
- deny responsibility
- admit use and accept inspection
- destroy part of the arsenal
- continue escalating

The victim can protect troops, distribute civilian masks, close movement corridors, quarantine outbreaks, request foreign aid, expose evidence, retaliate, or seek sanctions.

## Core mechanic values

### National values

| Value | Range | Meaning |
| --- | ---: | --- |
| Chemical readiness | 0 to 100 | Ability to plan and sustain chemical operations. |
| Protective reserve | Equipment-derived | Available gas masks, filters, suits, and issue material. |
| Decontamination capacity | 0 to 100 | Ability to clear units, routes, and states. |
| Medical countermeasure capacity | 0 to 100 | Antidotes, burn treatment, respiratory care, vaccination, and surge hospitals. |
| Biological security | 0 to 100 | Laboratory safety, surveillance, sample control, and outbreak response. |
| Delivery capacity | Profile by role | Artillery, armor, air, raid, and covert delivery readiness. |
| Attribution control | 0 to 100 | Ability to avoid accidental evidence and maintain operational secrecy. |
| CBRN command integration | 0 to 100 | Headquarters competence, forecast use, signal discipline, and protected routing. |

These are not all independent player-facing meters. Chemical readiness is the main visible national value. The others appear as named components in the CBRN interface, decision tooltips, headquarters tooltips, and national-spirit breakdowns.

### State values

| Value | Range | Meaning |
| --- | ---: | --- |
| Chemical contamination | 0 to 100 | Persistent chemical burden in the state. |
| Biological contamination | 0 to 100 | Pathogen burden before or during outbreak. |
| Civilian protective coverage | 0 to 100 | Share of population with usable protection and training. |
| Local decontamination progress | 0 to 100 | State cleanup progress. |
| Medical saturation | 0 to 100 | Pressure on local medical capacity. |
| Evidence quality | 0 to 100 | Publicly usable evidence of responsibility. |
| Movement-control severity | 0 to 100 | Quarantine, route closure, and access restrictions. |

State values should be stored only where needed and cleaned after recovery. The design must not create a permanent variable set on every state at game start.

### Army and order values

| Value | Meaning |
| --- | --- |
| Order protective coverage | Weighted coverage across assigned divisions. |
| Operation payload ratio | Available payload divided by required payload. |
| Forecast confidence | Weather prediction quality for chemical delivery. |
| Friendly exposure risk | Chance and severity of self-inflicted effects. |
| Decontamination routing | Ability to move through contaminated states. |
| Medical readiness | Ability to reduce military deaths and organisation loss. |

## Readiness bands

| Readiness | Gameplay state |
| ---: | --- |
| 0 to 19 | Program exists on paper. Offensive actions are hidden or blocked. |
| 20 to 39 | Limited local use. High accident and friendly-exposure risk. |
| 40 to 59 | Operational use. Basic headquarters abilities and raids are reliable. |
| 60 to 79 | Integrated theater use. Combined delivery and cleanup become practical. |
| 80 to 100 | Full Chaos Warfare posture. Doctrine capstones and extreme operations are available. |

Readiness rises through doctrine mastery, exercises, specialist equipment, trained headquarters, successful controlled operations, special projects, and established production. It falls through stockpile exhaustion, accidents, failed operations, headquarters losses, sanctions, destroyed facilities, and prolonged inactivity without maintenance.

## Agent classes

The system uses classes for gameplay logic. Individual historical agents remain research and equipment identities when useful.

### Choking agents

Examples: chlorine and phosgene.

Role: early battlefield denial, organisation damage, respiratory casualties, high weather sensitivity.

Strengths:

- cheap production
- useful against unprotected troops
- high immediate panic
- early availability

Weaknesses:

- poor persistence
- strong mask counterplay
- high friendly-exposure risk under bad wind
- visible clouds and clear attribution

### Blister agents

Examples: mustard gas and lewisite.

Role: persistent terrain denial, medical overload, equipment contamination, delayed deaths.

Strengths:

- long state persistence
- strong effect on supply routes and prepared positions
- mask-only protection is incomplete
- creates continuing medical burden

Weaknesses:

- slower tactical effect
- harms attackers entering the area
- expensive decontamination
- strong long-term evidence

### Nerve agents

Examples: tabun, sarin, and soman.

Role: severe short-duration disruption, high immediate lethality, suppression, strategic raids.

Strengths:

- powerful against poorly protected forces and populations
- lower visible warning before exposure
- useful for rapid breakthrough or occupation terror

Weaknesses:

- requires special projects and advanced handling
- severe stockpile accident risk
- extreme Condemnation and retaliation risk
- antidotes, sealed crews, and advanced protection greatly reduce effect
- high evidence value after samples are recovered

### Incapacitating and malodor agents

Role: disruption, morale damage, evacuation, nonlethal area denial, covert embarrassment.

Strengths:

- lower direct deaths
- useful for temporary disruption
- lower initial Condemnation when no fatalities occur

Weaknesses:

- unreliable against trained troops
- resistance and propaganda backlash
- can still become a condemned chemical attack

### Biological agents

Biological agents use separate profiles because spread, incubation, containment, and attribution matter more than battlefield wind.

## Exposure resolution

Every deliberate use calculates five outputs:

1. military disruption
2. military deaths
3. civilian deaths
4. contamination or outbreak pressure
5. evidence and Condemnation

### Inputs

- agent class
- delivery method
- delivered dose
- payload ratio
- target population
- target unit density
- target protective coverage
- weather and terrain
- medical readiness
- decontamination capacity
- attacker command integration
- attacker attribution control
- whether the target is enemy, neutral, allied, occupied, core, or non-core
- recent repeated use

### Protection layers

Protection is split into:

- respiratory protection
- skin protection
- antidote readiness
- decontamination
- medical treatment
- training and warning

A gas-mask company provides strong respiratory protection but weaker blister and nerve protection unless paired with decontamination and medical countermeasure support.

## State contamination classes

| Class | Chemical value | General effect |
| --- | ---: | --- |
| Trace | 1 to 9 | Short local disruption. No persistent state modifier after cleanup. |
| Local | 10 to 24 | Noticeable attrition, movement, and recovery penalties in affected combat areas. |
| Serious | 25 to 49 | State modifier, civilian deaths, supply and construction disruption. |
| Severe | 50 to 74 | Heavy medical saturation, prolonged deaths, major supply degradation. |
| Catastrophic | 75 to 100 | State crisis, mass evacuation pressure, extreme evidence, long cleanup. |

The existing Air Cleanliness system should receive a bounded contribution when a state enters a new contamination class, not every time one internal contamination point changes. This prevents repeated tactical use from creating runaway global pollution through tiny ticks.

## Operational permissions

A country can set one national use policy:

| Policy | Use permissions | Political effect |
| --- | --- | --- |
| Defensive preparation | Protection and cleanup only. | Low international concern. |
| Retaliation authority | Offensive use after confirmed enemy chemical or biological use. | Easier allied support and lower first-use blame. |
| Limited battlefield authority | Army HQ can use approved battlefield operations. | Monitoring and treaty tension. |
| Strategic release authority | Raids and air operations allowed. | High evidence, sanctions risk, domestic strain. |
| Unrestricted Chaos Warfare | All doctrine actions allowed, including extreme operations. | Severe internal and external consequences. |

Policy changes require political, command, institutional, and stockpile conditions. They are not cheap political-power toggles.

## Counterplay

Every offensive tool has at least three counters:

- pre-war protection and stockpile preparation
- tactical or headquarters response during exposure
- cleanup, medical, diplomatic, or intelligence response after exposure

The defender should be able to turn an attacker’s chemical offensive into a supply disaster if the defender has strong protection, decontamination corridors, medical capacity, and air or artillery interdiction.

## Failure states

### Friendly blowback

Bad forecast, low readiness, damaged headquarters, low payload discipline, or use in rapidly moving fronts can contaminate friendly states and divisions.

### Stockpile accident

Large advanced-agent stockpiles without safety technology can cause a domestic contamination or outbreak event.

### Medical collapse

Repeated exposure can push medical saturation above capacity, increasing deaths and slowing reinforcement even after contamination falls.

### Political rupture

Allies can refuse support, leave sanction shields, demand inspections, or split over continued use.

### Doctrine lock-in

A country that invests deeply in Chaos Warfare becomes dependent on specialist equipment and headquarters. Switching doctrine should create a long conversion period and retire doctrine-only abilities rather than instantly refunding the system.

## Multiplayer behavior

- All random or hidden attribution rolls must be deterministic and synchronized.
- The UI must show the same public evidence and Condemnation to all players.
- Secret attacker information can remain hidden only through established country-scoped data and scripted localisation.
- Operations must use fixed target scopes and cleanup to avoid stale selected-state or selected-army references.
- No broad all-country daily loop is introduced.

## Acceptance criteria

The system succeeds when:

- a protected army can survive chemical use noticeably better than an unprotected army
- gas masks and decontamination are real production choices
- an Army HQ changes the value and safety of chemical operations
- agent classes play differently
- aircraft, artillery, tanks, raids, and covert delivery use one shared exposure model
- deaths, contamination, Air Cleanliness, and Condemnation agree
- AI can use and counter the system
- offensive power is strong enough to matter without coming from permanent universal attack stacking
- repeated use creates an aftermath the player must manage
