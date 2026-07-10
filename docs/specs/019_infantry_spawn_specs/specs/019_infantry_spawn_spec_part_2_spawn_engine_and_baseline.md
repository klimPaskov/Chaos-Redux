# Event 19 Infantry Spawn
## Part 2: Spawn engine, territorial scaling, and baseline play

## Spawn engine purpose

The spawn engine must satisfy three goals at the same time.

1. Every valid country receives a meaningful manifestation.
2. Countries with more territory receive more formations in absolute terms.
3. The share of territory used for spawning declines as controlled state count rises.

A flat one-division-per-state loop fails the second and third goals in practice because it gives continental empires an overwhelming free army and forces all states into the same template. The rework should use a diminishing coverage curve and formation lots.

## Eligible country scope

Every existing country capable of controlling land is evaluated, including:

- ordinary countries
- subjects
- countries at war or peace
- countries with one controlled state
- event-created countries
- special Chaos countries
- nonhuman countries

The system should not silently exclude a country merely because its military rules differ from ordinary countries. Instead, the compatibility layer chooses the appropriate pool:

- ordinary formation pool
- country-native registered pool
- mixed auxiliary pool
- anomalous registry pool at Evolution IV

Countries with no eligible controlled state receive no spawn and no false penalty.

## Eligible state rules

A state can be selected when it is controlled by the country, is not impassable, and can safely host a land unit.

Additional design rules:

- Occupied states can be selected, but their local legitimacy and resistance affect formation quality and loyalty.
- Core states receive higher coherent-formation weight.
- Colonial and non-core states receive more irregular, mounted, local auxiliary, or politically unreliable formations.
- Tiny island states should not receive formations that cannot move, supply, or operate there unless the absurdity is intentional at a later evolution.
- Front-line states receive higher readiness but higher risk of immediate disruption.
- States under active combat need a safe placement rule so units do not spawn in invalid or encircled positions without explanation.
- A state changing controller during the global effect must be evaluated once under the final valid scope used by the generation.

## Diminishing coverage curve

The following bands express the intended result. They are tuning anchors, not hard steps.

| Controlled eligible states | Typical selected share | Expected character |
| --- | ---: | --- |
| 1 to 5 | 90 to 100 percent | Almost every state produces a formation |
| 6 to 15 | 75 to 90 percent | Broad national manifestation |
| 16 to 35 | 55 to 75 percent | Strong regional spread with gaps |
| 36 to 70 | 40 to 60 percent | Major states and a sample of peripheral regions |
| 71 or more | 25 to 45 percent | Large absolute army with sharply diminishing coverage |

The implementation should use a smooth function or weighted ladder that avoids a sudden drop when a country gains one state. The number of selected states has no fixed cap.

A continental empire therefore gains more units than a small country, but each additional controlled state contributes less to the selection count.

## Minimum manifestation

A country with at least one eligible state should normally receive at least one selected state.

Exceptions are limited to:

- an explicit safe deferral during tag transition or annexation cleanup
- a local compatibility failure that is recorded for repair rather than silently ignored
- a scenario type that deliberately suppresses normal spawning in favor of immediate revolt setup

The minimum does not override impossible placement rules.

## State weighting

After calculating the target number of selected states, the system builds a weighted pool. State identity should influence both selection and the type of formation created there.

### Capital and administrative centers

Capital states and major administrative centers receive higher selection weight. They favor:

- coherent infantry
- reserve staff formations
- support-rich formations
- claimant headquarters at Evolution III

They also create high political risk if a claimant controls the local formations.

### Industrial states

Industrial states favor:

- artillery and support equipment
- motorized or mechanized lots at later evolutions
- factory guard or workshop formations
- golem sustainment hooks at Evolution IV where registered

The equipment burden should draw on local and national industrial capacity.

### Rail junctions and supply hubs

Rail and supply states favor larger or better supplied formations. They also become mission targets because congestion at these locations can damage the whole network.

### Ports and naval bases

Ports favor:

- marine or coastal defense elements where valid
- motor transport and support-heavy lots
- foreign-looking equipment through unexplained deliveries
- island-compatible formations

Port selection should consider convoy and naval access so a remote island does not receive an unusable armored army at baseline.

### Urban and high-population states

These states favor manpower-heavy infantry, militia, support, and political claimant networks. They can field more units but suffer greater local requisition and training-ground pressure.

### Mountain, desert, jungle, and steppe states

Terrain shifts family weights:

- mountains favor light infantry, pack artillery, cavalry, mountain-capable auxiliaries, and later strange terrain specialists
- deserts favor cavalry, camels where available, motorized patrols, and light formations
- jungle favors irregulars, light infantry, engineers, and supply-light lots
- steppe and broad plains favor cavalry, motorized, and armored families

The event should use existing valid unit definitions rather than inventing unavailable battalions.

### Occupied and resistant states

These states favor locally raised formations with uncertain loyalty. They can produce useful garrisons, partisan-like cadres, collaborator units, or claimant recruits. Integration should require legitimacy, suppression, or local administration work.

A country that raises too many units from hostile occupied territory risks mutiny, desertion, or defection rather than receiving free dependable manpower.

### Front proximity

States near an active land front gain readiness and heavier equipment weight because wartime networks are already active. They also gain higher immediate casualty and supply risk.

Rear areas produce less ready formations but provide more time for audit and retraining.

## Formation lots

A **formation lot** is the basic management unit.

One lot contains:

- one generated template family
- one readiness profile
- one equipment condition
- one origin region or state group
- one generation number
- zero or more divisions using that template
- one command ownership state
- one integration state
- optional claimant or anomalous family linkage

The number of lots should remain readable. Baseline and Evolution I should usually create a small number of lots per country even when many divisions appear. The divisions within a lot share a coherent identity.

At Evolution III, lot count can rise because template composition is random, but it should still be bounded by country size and UI capacity. The design target is two to eight generated lots for most countries, with larger countries able to exceed that only when the total formation count justifies it.

## Baseline units per state

The baseline normally creates one division in each selected state.

Variation can occur when:

- a state has very high population and military infrastructure
- the country is at war under severe front pressure
- a repeat firing hits a stacked muster state
- the selected state represents several remote territories through a safe placement abstraction

Baseline variation should remain modest. Multiple units per state are a central feature of Evolution II.

## Baseline template families

The following are working labels, not final localisation.

### Local Rifle Cadre

Purpose:

- basic infantry formation
- low to moderate equipment demand
- suitable for retraining or territorial defense

Composition direction:

- several infantry battalions
- zero or one basic support company
- no elite structure

Quality range:

- undertrained to serviceable

### Irregular Column

Purpose:

- weak but supply-light local force
- common in remote, occupied, or low-industry states

Composition direction:

- irregular infantry or the closest valid light infantry type
- limited support
- uneven equipment

Quality range:

- poor organization, variable local bonuses, weak standardization

### Mounted Patrol

Purpose:

- cavalry or camel-based local mobility
- common in steppe, desert, frontier, and low-motorization regions

Composition direction:

- cavalry or camel battalions where valid
- minimal support

Quality range:

- useful for security and low-supply movement, weak against heavy formations

### Light Gun Brigade

Purpose:

- infantry with a small artillery component
- higher supply and equipment burden

Composition direction:

- infantry core
- one or more artillery battalions or artillery support

Quality range:

- stronger combat potential, greater equipment debt

### Support-Rich Reserve

Purpose:

- smaller combat core with several support companies
- disproportionately valuable if the country can equip it

Composition direction:

- infantry core
- engineer, reconnaissance, artillery, anti-air, anti-tank, logistics, medical, or signal support drawn from valid technology and equipment context

Quality range:

- moderate training, high compatibility risk if the country lacks equipment

### Garrison Shell

Purpose:

- minimal formation suitable only for static defense or future retraining

Composition direction:

- one to several infantry battalions
- no expensive support by default

Quality range:

- very weak field performance

This family creates the baseline long tail of disappointing results without turning every poor roll into an unusable one-battalion joke.

## Baseline family weights

Weights should react to state and country context.

Examples:

- high industry increases Light Gun Brigade and Support-Rich Reserve weight
- low infrastructure increases Irregular Column and Mounted Patrol weight
- high population increases Local Rifle Cadre and Garrison Shell count
- war increases readiness and combat-oriented families
- peace increases reserve and retraining-oriented families
- low equipment stockpile shifts arrivals from equipped strength toward equipment debt
- high prior Muster Control increases coherent family weight
- stacked muster increases Garrison Shell and Irregular Column weight

The player should learn broad patterns but never predict the exact template.

## Readiness profile

Each lot receives a readiness profile built from four components.

### Training state

Possible states:

- improvised
- minimally drilled
- partially trained
- serviceable

Baseline should rarely create fully trained formations.

### Organization state

Organization measures whether the lot has a usable command structure, communications, and deployment order.

A well-equipped formation can still have poor organization.

### Equipment state

Equipment state records how much of the template’s initial equipment exists and how compatible it is with national stockpiles.

Possible states:

- skeletal
- understrength
- mixed issue
- substantially equipped

### Supply burden

Supply burden records whether the lot’s size and composition fit the local network.

Possible states:

- light
- ordinary
- heavy
- locally impossible

A locally impossible lot should be rare at baseline and should trigger an immediate relocation or demobilization choice.

## Equipment and manpower accounting

The event must not create unrestricted free stockpiles.

### Initial equipment principle

A spawned division may arrive with equipment, but the value must be accounted for through one or more of these sources:

- national stockpile requisition
- temporary muster debt
- reduced future production or reinforcement priority
- captured or unidentified equipment that cannot replenish normally
- local industrial requisition burden
- scenario-specific grant with an explicit balance cost

The exact script representation can differ by equipment type, but the design result must be visible. A country receiving many equipped formations owes something to the military economy.

### Manpower principle

The event can create formations whose personnel appear without ordinary recruitment, but their existence should still affect manpower, population, local labor, or a dedicated muster liability.

The baseline should not kill population merely because units spawn. It should create a labor and mobilization burden. Later combat casualties flow through ordinary military and shared death systems.

### Unsupported equipment

At baseline, unsupported equipment types should be rare. When they appear, the player can:

- cannibalize the lot
- accept poor reinforcement
- convert the lot through retraining
- preserve it as a limited special formation

The event should not silently unlock the associated technology.

## Event-owned template safeguards

The implementation needs an event-owned template and division lifecycle that prevents exploitation.

During the audit period:

- event divisions cannot be freely switched into a cheaper template to extract equipment
- event divisions cannot be instantly disbanded for full equipment and manpower return
- the generated result cannot be rerolled by cancelling and reopening a decision
- event-owned templates are marked by generation and lot
- deleting a template does not orphan divisions or bypass accounting

After disposition:

- integrated formations can become ordinary divisions after their equipment debt and command status are resolved
- demobilized formations return only a controlled share of salvage after time and cost
- consolidated lots can merge into a national standard through a mission or decision
- anomalous spawn-only units remain governed by registry rules

These restrictions should be explained through clear tooltips. They are not permanent arbitrary locks.

## Baseline decisions

The baseline decision category should be compact. It should not expose the later crisis interface prematurely.

### Audit the New Formations

Working role:

- starts or accelerates registration
- reveals lot quality and burden
- costs administrative or military resources that scale with size

Possible cost palette:

- army experience
- command power at a conservative level
- temporary officer or training burden
- trains or support equipment for a large country

### Assign Territorial Roles

Working role:

- converts suitable lots into garrison or local defense duty
- lowers congestion
- limits offensive value

Requirements:

- suitable template families
- controlled states needing defense

### Begin Standardization Cycle

Working role:

- starts a timed mission to consolidate compatible lots
- consumes equipment, training capacity, and time
- raises Muster Control on success

### Supervised Demobilization

Working role:

- removes unwanted weak lots safely
- returns partial salvage after delay
- lowers congestion
- may reduce war support or anger local communities if used during war

### Emergency Field Integration

Working role:

- immediately makes selected lots field-ready
- useful during war
- creates larger supply strain and lower long-term control

The baseline should not yet offer an unrestricted random unit request. That becomes a defining Evolution II feature.

## Baseline missions

### Formation Roll Call

A timed audit mission checks whether the country resolves registration before the deadline.

Success direction:

- raises Muster Control
- reduces hidden failure risk
- unlocks more precise disposition

Failure direction:

- raises congestion
- leaves some lots under informal command
- can produce a follow-up local incident

Duration should scale by country size and current war pressure. A larger country gets more absolute time but less time per formation.

### Clear the Rail Sidings

This mission appears only when selected states or lots create meaningful rail congestion.

Objective direction:

- maintain sufficient trains or repair named rail links
- avoid overloading selected supply corridors
- possibly move lots away from critical hubs

Success improves supply handling. Failure creates real front-line or reinforcement disruption.

### Find the Officers

This mission appears when the country lacks command capacity for the new formations.

Objective direction:

- spend army experience
- complete an officer assignment decision
- keep claimant influence absent at baseline

Failure keeps formations less organized and worsens the next generation.

## Baseline flavor incident families

Flavor events need real effects. They should be selected from current lot and state data rather than fire as disconnected prose.

### Barracks Without Records

Direction:

A unit occupies a training site but no ministry recognizes its officer list. The choice decides whether local authorities, the regular army, or a provisional committee controls it.

Effects can change Muster Control, local readiness, and later claimant susceptibility.

### The Wrong Ammunition Train

Direction:

A formation has weapons that do not match the ammunition delivered to it. The country can divert production, cannibalize the formation, or accept a delayed deployment.

Effects must alter equipment debt or readiness.

### Horses in the Motor Pool

Direction:

A mounted formation appears in a mechanized district or a motorized lot appears where fuel and roads are poor. The response changes its role and supply burden.

### The Village Regiment

Direction:

A local formation refuses distant deployment because its members believe they were raised to defend their own state. The country can accept territorial service, enforce transfer, or bargain for better supply.

Effects alter local loyalty, organization, and congestion.

### Officers Who Arrived First

Direction:

An unknown officer cadre already controls the new formations. At baseline this remains an administrative anomaly, not yet a possessed claimant. The response creates a hidden susceptibility record that can matter at Evolution III.

## Baseline AI behavior

AI countries choose among four broad responses.

### Integrator

Prefers audit, standardization, and normal field incorporation.

Favored by:

- high industry
- adequate stockpiles
- stable government
- professional military context

### Territorialist

Prefers garrison, border, and local defense roles.

Favored by:

- long borders
- low supply
- defensive wars
- occupied territory

### Emergency User

Rushes field integration.

Favored by:

- active war
- enemy superiority
- capital threat
- low division count

### Demobilizer

Removes weak lots and limits burden.

Favored by:

- peace
- low manpower or equipment
- high congestion
- no immediate threat

AI should never treat every division as automatically valuable. It must compare projected combat value against supply, equipment, and command burden.

## Baseline closeout outcomes

At closeout, the country receives one generation record.

Possible record classes:

- integrated
- territorialized
- standardized
- demobilized
- neglected
- stacked
- collapsed

The record affects future generation weights. It should not create a permanent national spirit for every firing. Use persistent variables, a compact staged idea, or scripted values where appropriate.

## Baseline acceptance criteria

The baseline design is satisfied when:

- every valid country is evaluated
- larger countries receive more formations but lower proportional state coverage
- selected state context changes template families
- at least six baseline family identities are represented
- war and peace produce different benefits and burdens
- event equipment and manpower are accounted for
- the player can integrate, territorialize, standardize, or demobilize lots
- the AI can make equivalent choices
- free equipment extraction is blocked
- repeated unresolved generations create stacked muster
- ordinary lifecycle is not logged as an evolution
- no later claimant, random-draw, or anomalous interface is shown before it becomes relevant
