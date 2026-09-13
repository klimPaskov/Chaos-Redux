# Event 41: Disease in Divisions

## Catalog identity

- Event ID: `41`
- Event name: Disease in Divisions
- Event type: Minor Repeatable
- Minimum Chaos level: 1, Calm World
- Cluster: Diseases
- Cluster role: Low member
- Design status: Full rework specification

## Playable promise

Disease in Divisions creates a temporary military crisis inside an army that is already fighting. The disease begins among real frontline formations, grows through camps and supply relationships, removes soldiers from duty, and forces the country to choose between operational momentum and medical control.

The event should make the player look at the front differently. A strong army can lose tempo because its field hospitals are full, its rail network is carrying sick men instead of ammunition, and its best divisions cannot recover between battles. The player can preserve the offensive and accept rising illness, or pull formations back and give the enemy space. Good logistics and medical preparation create real protection. Poor supply and ruined infrastructure turn an ordinary outbreak into a front-wide emergency.

The baseline remains a low-severity disease event. It can hurt one country badly when ignored, yet it should usually stay inside that country's military system. International military spread belongs to Evolution I. Civilian spillover belongs to Evolution II.

## Public mechanic budget

The player tracks one persistent event-specific value:

### Army Infection Pressure

Army Infection Pressure measures the operational burden created by active military disease. It summarizes infected formations, camp crowding, spread risk, medical overload, supply failure, prolonged combat exposure, and the current ability to isolate and recover sick troops.

The value should be shown as a clear meter or staged bar in the temporary decision category. The category should also show a short trend indicator and a concise explanation of the largest current causes. Those causes remain qualitative or icon-based. They do not become separate persistent counters.

Examples of useful causes include:

- severe supply strain on affected fronts
- too many affected divisions sharing one logistics network
- prolonged offensive combat
- damaged railways and infrastructure
- inadequate field-hospital coverage
- transport shortage slowing evacuation
- active sanitation and isolation measures
- rested formations recovering away from combat

The player should always be able to answer five questions from the category header and short tooltips:

1. What is the current pressure stage?
2. Is pressure rising, stable, or falling?
3. What is driving the current trend?
4. Which response is most useful now?
5. What operational sacrifice will that response require?

No other persistent custom meter should be exposed. Counts such as affected formations, convalescent soldiers, deaths, and secondary countries may appear in concise status text where useful. They remain outputs and records, not values the player manages separately.

## Valid target countries

Each firing selects one ordinary country that satisfies all of the following:

- the country exists and controls territory
- the country is currently at war
- the country has a meaningful land army
- at least one land formation is committed to an active or recently active front
- the country is not classified as a special Chaos country
- the country does not already have an unresolved Event 41 outbreak
- the country is not inside the strongest recent-survivor resistance window
- enough valid frontline or front-adjacent formations exist to support a bounded opening outbreak

Player-controlled countries remain valid. A player-controlled minor can be selected when it meets the military conditions. Major status is not required.

The event should fail closed when it cannot prove a valid country, active front, or valid formation group. It should return to the event system without creating an empty incident.

### Target priority

Selection should remain random among valid countries, with dynamic weight shaped by the current military environment.

Higher target weight should come from:

- several divisions operating on the same active front
- prolonged fighting without rotation
- low supply or high attrition
- damaged infrastructure and railways
- harsh weather or disease-friendly terrain
- low field-hospital coverage
- large staging areas behind the front
- recent strategic bombing or disaster damage
- chemical or biological contamination near the front
- famine or refugee pressure in military transit states

Lower target weight should come from:

- strong field-hospital support
- high supply and infrastructure quality
- recent successful containment of Event 41
- a small dispersed army with little sustained combat
- a front that has been inactive long enough for units to rest

These factors shape selection odds. They should not become absolute immunity except where the event lacks a valid military target.

## Front and formation selection

The outbreak begins in a bounded frontline group. The group should represent formations sharing one operational environment, not a random sample from the whole army.

A valid seed group can be formed from one or more of these relationships:

- divisions fighting or entrenched in the same state group
- divisions assigned to the same active land front
- divisions drawing supply through the same hub or damaged transport corridor
- divisions occupying neighboring frontline states
- divisions concentrated in the same staging or reserve area
- divisions recently rotated through the same front or field-hospital network

The opening should prefer one coherent sector. It should not scatter isolated cases across every theater during the baseline.

### Opening footprint

Baseline opening size should scale with the army and the sector while staying bounded.

A small army should normally begin with two or three affected formations. A medium army should normally begin with three to six. A very large army should normally begin with four to eight. The opening should never infect most of the target's army at once.

The opening can be slightly larger when the selected sector has severe supply failure, intense combat, ruined infrastructure, or active contamination. Strong medical preparation can reduce the number of seeded formations or soften their opening penalties.

## Opening sequence

The first report should make the military problem visible without identifying a precise pathogen.

The sequence should show:

- growing sick-call numbers in one sector
- field hospitals reporting recurring fever, weakness, intestinal illness, respiratory illness, or other profile-specific signs
- formations losing available soldiers faster than replacements can restore readiness
- transport and medical units becoming crowded
- officers debating whether the sector can remain active

The opening creates the temporary decision category, selects the hidden disease profile, registers affected formations, records the episode, applies the first temporary penalties, and establishes the initial Army Infection Pressure.

The initial pressure should usually begin in the low or middle operational range. A well-protected army may start near the lower edge. A badly supplied army in sustained combat may start higher. The first firing must create a noticeable problem, yet it must leave enough time for the player to respond before the sector approaches collapse.

## Hidden disease profiles

Each episode selects one hidden profile from current conditions. The profile changes transmission logic, symptom direction, response efficiency, and environmental risk. It does not change the event identity and does not add another public meter.

### Camp-borne fever profile

This profile represents diseases that thrive in crowded camps, shared bedding and clothing, cold weather, lice, close quarters, and long periods in trenches or shelters.

It receives stronger spread pressure from:

- dense troop concentration
- cold or wet exposure
- shared camps and staging areas
- poor hygiene and laundry access
- long entrenchment without rotation
- overcrowded field hospitals

It responds especially well to:

- rotation and dispersal
- quarantine camps
- sanitation orders
- replacement of bedding and camp supplies
- reducing troop concentration

Its ordinary mortality should be lower than its readiness burden. It can remove many soldiers from duty without turning every case into a death.

### Enteric profile

This profile represents disease moving through unsafe water, food, damaged sanitation, contaminated supply, and crowded rear areas.

It receives stronger spread pressure from:

- low supply and damaged infrastructure
- destroyed water and transport systems
- hot weather
- ports, depots, and supply hubs under strain
- famine pressure
- bombardment and urban damage

It responds especially well to:

- emergency sanitation
- clean supply replacement
- infrastructure and route repair
- field-hospital expansion
- evacuation from contaminated rear areas

It should create strong organization, recovery, reinforcement, and attrition pressure. Mortality becomes significant when medical capacity and clean supply fail together.

### Tropical and vector-borne profile

This profile represents malaria-like, mosquito-borne, flea-borne, and other vector-heavy military disease environments.

It receives stronger spread pressure from:

- jungle, marsh, warm wet weather, and long tropical exposure
- poor camp discipline
- inadequate medicine or prophylaxis
- damaged supply routes
- long patrol and combat cycles
- troops operating without rest or replacement

It responds especially well to:

- medical supply distribution
- sanitation and vector control
- troop rotation
- evacuation and recovery time
- strong logistics and field hospitals

This profile should recover more slowly than the others. A country can suppress new cases while still carrying a large convalescent burden.

## Army Infection Pressure stages

The exact numbers should remain centrally tunable. The following five-stage model defines player-facing behavior and balance targets.

| Pressure band | Working stage label | Frontline meaning | Expected player experience |
| --- | --- | --- | --- |
| 0 to 19 | Controlled | Cases are isolated and medical capacity is recovering | Active penalties fade, new spread becomes uncommon, and resolution progress begins |
| 20 to 39 | Localized outbreak | Several formations are affected inside one sector | The player can contain the episode with moderate costs and one or two focused actions |
| 40 to 59 | Spreading field epidemic | The selected sector is losing readiness and medical capacity is strained | Rotation, evacuation, or offensive restraint becomes necessary |
| 60 to 79 | Operational epidemic | A substantial share of the sector is sick or recovering | The player must sacrifice tempo, transport, production, or front coverage to prevent a crisis |
| 80 to 100 | Army crisis | Medical services and reinforcement are failing across the affected front | Severe combat penalties, high deaths, broader spread, and long aftermath become likely |

Pressure should never jump from a manageable opening to the maximum through one ordinary weekly pulse. Large increases need a concrete cause such as a failed high-risk decision, a major offensive through infected terrain, a ruined evacuation route, a contamination event, or an evolution-enabled transmission milestone.

## Pressure movement

Pressure rises from the current burden and the environment. Pressure falls from effective medical action and time away from exposure.

### Major rising factors

- the share of registered affected formations
- new formations exposed within the same front or logistics network
- active combat involving affected formations
- offensive operations sustained through the outbreak
- low supply and high attrition
- damaged infrastructure, railways, hubs, and ports
- severe weather and profile-friendly terrain
- field hospitals below the required coverage
- transport shortage blocking evacuation
- overcrowded staging areas and rear hospitals
- failed quarantine or sanitation measures
- chemical contamination, biological exposure, famine, displacement, and heavy bombardment

### Major falling factors

- removing the worst-hit formations from combat
- keeping affected formations in a supplied rear area long enough to recover
- expanding field-hospital capacity
- establishing quarantine and clean camps
- assigning trains and trucks to medical evacuation
- replacing contaminated camp and supply stocks
- repairing the relevant supply route
- reducing offensive operations
- dispersing crowded formations
- sustained weeks without new transmission

A response should not give the same pressure change in every country. Its effect should scale with the size of the affected sector, current profile, available medical support, transport, supply, and whether the player fulfills the operational requirement behind the action.

## Military effects

Affected formations should show a clear temporary disease state. The penalty package should scale by local severity and national pressure.

The core effects are:

- reduced available military manpower or effective strength
- lower organization
- slower organization recovery
- lower reinforcement and recovery rate
- reduced attack and defense when the formation remains in combat
- higher ordinary attrition when the environment remains severe
- slower movement during quarantine or evacuation
- reduced planning and offensive tempo at high pressure

The event should not use equipment destruction as a substitute for sick soldiers. Rifles, artillery, vehicles, and support equipment do not vanish because personnel are ill. Equipment can still be lost through normal combat, attrition, bombing, and logistics. Event 41 itself should not debit division equipment as a disease effect.

### Worst-case baseline target

A badly managed baseline episode can reduce the effective strength of the worst-hit front toward roughly half of normal strength. This is an operational ceiling for sustained failure. It should emerge from several weeks of spread, unavailable sick personnel, poor reinforcement, organization loss, and medical collapse.

The baseline should not remove half of the country's entire army. The extreme effect belongs to the infected sector. Other fronts remain capable unless transmission reaches them through normal baseline military connections or later evolutions.

## Sick, recovering, and dead soldiers

The military manpower model separates three outcomes.

### Active sick

These soldiers are temporarily unavailable. They reduce effective formation strength and increase pressure. They are not deaths.

### Convalescent

These soldiers have left active infection but have not returned to duty. They form a temporary recovery pool. They return gradually through reinforcement or a direct recovery transaction after the required recovery delay.

### Fatal cases

These soldiers are permanently removed and registered once as military casualties in the shared Deaths system. Fatality should be a minority of total cases under ordinary medical conditions. High pressure, failed evacuation, poor hospitals, contamination, and prolonged exposure raise the fatal share.

The implementation must prevent the same soldier from being counted once as temporarily sick and again as a death without reconciliation. It must also prevent recovered soldiers from generating deaths or permanent manpower loss.

## Baseline lifecycle

The ordinary episode moves through five broad stages. These are event stages, not evolutions.

1. **Detection** begins when one sector receives the opening cases and the temporary category appears.
2. **Field response** begins as the country chooses rotation, sanitation, quarantine, hospitals, evacuation, supply replacement, or continued offensive operations.
3. **Containment or expansion** is determined by pressure trend, affected formations, and the operational environment.
4. **Recovery threshold** begins after pressure remains low, new spread stops, and the infected share falls below a meaningful level.
5. **Aftermath** returns convalescent soldiers over time and applies a temporary preparedness benefit or medical exhaustion penalty.

A baseline episode can resolve without reaching the operational epidemic stage. It can also worsen into a front-wide crisis without any evolution activating.

## Core design boundaries

The event must preserve these rules through every implementation choice:

- one public custom value governs the player-facing crisis
- the baseline begins in a bounded frontline sector
- equipment is not deleted to represent sickness
- recoverable illness and fatal military casualties are separate
- real military deaths enter the shared Deaths system once
- ordinary stage progression is not logged as evolution
- special Chaos countries are excluded through the shared classifier
- the baseline can be contained in one country
- the event remains dangerous but manageable at every evolution
- the event uses sparse registered processing and never depends on a daily scan of every country or division
