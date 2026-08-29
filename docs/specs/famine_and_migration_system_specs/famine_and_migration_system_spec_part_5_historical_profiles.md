# Famine and Migration Mechanics

## Part 5: Historical profiles and regional logic

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

> **Superseded incident-layer and probability note (2026-08-25):** Any wording in this historical specification about incident events, event-option probability, `famine_incident.1`, `migration_incident.1`, `fm_*`, or combined `famine_migration_*` planning IDs is superseded. The register helpers are accounting/presentation seams only; the incident event files and constants were deliberately deleted.

## Historical-profile purpose

Historical research supplies cause patterns, regional memory, policy behavior, migration routes, and political consequences. It does not supply a fixed casualty script.

A historical profile can change:

- which pressure components activate first
- which states carry prior vulnerability or memory
- which government decisions become available
- which AI choices are more likely
- which foreign countries receive relief or refugee events
- how concealment, opposition, and evidence develop
- which migration routes have historical ties
- which event and system adapters receive extra weight

The actual outcome still depends on the campaign.

## Profile activation standard

A profile can activate through one of three modes.

### Historical memory

The famine or displacement predates the normal 1936 start. The campaign begins with memory, demographic damage, political mistrust, or administrative habits. No active mortality stage is imposed at game start.

### Historical-window crisis

The case falls inside the likely campaign period. The profile becomes eligible when its real structural conditions are reproduced. The date can raise weight, but the crisis should not fire when the campaign has removed the causes.

### Late-game or alternate-policy analogue

The historical case falls after the ordinary period or depends on a policy not present at game start. The profile becomes possible when a country adopts comparable policies and produces comparable pressure. It is not locked to one historical leader or ideology.

## Soviet famine, grain extraction, gulags, and movement restriction

### Historical role

The Soviet profile combines several mechanisms:

- forced grain procurement
- collectivization pressure
- confiscation of reserves
- punishment for alleged hoarding
- restricted movement from affected rural areas
- concealment and false reporting
- deportation and forced labor
- repression of national and rural opposition

The 1932 to 1933 Ukrainian famine and related famine across other Soviet regions predate a normal 1936 start. The active game profile should therefore begin as memory and vulnerability unless an earlier scenario exists.

### Starting memory

Relevant Ukrainian, Kazakh, North Caucasian, Volga, and other historically affected regions can receive hidden memory or a compact visible legacy modifier where the repository supports it.

Memory can affect:

- trust in requisition policy
- sensitivity to grain extraction
- support for local and national opposition
- willingness to report shortages honestly
- fear of movement restriction
- foreign propaganda and evidence
- response to gulag expansion

The memory should not impose a permanent generic penalty on every Soviet state.

### Dynamic reactivation

A renewed Soviet famine profile becomes possible when several conditions combine:

- heavy grain extraction or forced procurement
- low local production or disaster damage
- continued export or military priority
- movement restriction
- gulag or forced-labor expansion
- deportation of agricultural workers
- concealed reports
- low relief access

Event 5 Soviet Collapse should be a major adapter. Its grain extraction, forced-labor quotas, NKVD campaigns, deportation, gulag growth, and republic fear can increase state food pressure, displacement, and hidden evidence.

### Political outcomes

Possible outcomes include:

- peasant resistance
- Ukrainian, Kazakh, and other national opposition
- local party or administrative refusal
- military and police conflict over enforcement
- underground relief networks
- foreign exposure and condemnation
- stronger republic exit pressure during Soviet Collapse

The system should not force one modern legal interpretation into generic player-facing text. The research and internal design can recognize documented policy mechanisms, mass mortality, movement restriction, and contested legal classification.

## China profiles

China needs more than one famine profile because wartime Henan and the later Great Famine arose from different combinations of pressure.

### Henan wartime famine profile

This profile fits the normal campaign period.

Main pressure components:

- drought
- frost and hail
- locust damage
- wartime requisition
- military supply priority
- weak transport and relief
- refugees and prior war damage
- administrative delay or concealment

Activation should depend on actual conditions in Henan and nearby states. A peaceful China with functioning relief and no crop shock should not receive the crisis by date alone.

Possible responses:

- suspend requisition
- divert military grain
- request foreign relief
- organize rail evacuation
- distribute people into safer provinces
- enforce movement restrictions
- deny or conceal the crisis

Possible political consequences include rural opposition, local military defiance, communist or nationalist recruitment according to current control and credibility, and weakened legitimacy.

### Great Famine policy analogue

The Great Chinese Famine falls outside the core Second World War period. It should be a late-game or alternate-policy analogue.

The profile becomes possible when a government combines:

- radical collectivization or forced communal production
- unrealistic output targets
- falsified local reports
- over-procurement
- continued extraction from distressed states
- movement restriction
- punishment of local dissent
- weak correction after early mortality

The profile should not be exclusive to communist ideology. Any regime that creates the same policy structure can trigger a comparable crisis. Communist policy and historical leadership can raise AI weight where appropriate.

The crisis remains dynamic. A government that corrects reports, reduces procurement, opens movement, and accepts relief can prevent catastrophic mortality.

## Bengal 1943 profile

### Pressure composition

The Bengal profile should combine:

- loss or disruption of normal rice imports
- wartime shipping and transport priority
- local crop disease or cyclone damage when the natural-disaster system creates it
- inflation and unequal access represented through distribution failure without a literal price simulator
- administrative delay
- displacement and urban crowding
- military denial or coastal security policies where represented

The profile should avoid presenting one uncontested cause. The design treats it as a multi-causal wartime food-access collapse.

### Activation

Eligibility can rise when:

- Bengal is under British, Indian, Japanese, or successor control
- war disrupts Bay of Bengal and Burma routes
- convoys and ports are under pressure
- local crop or cyclone damage exists
- transport and storage are damaged
- relief is delayed or politically restricted

### Gameplay

The controller can:

- divert shipping and rail capacity
- accept military supply delays
- request imperial or international relief
- organize internal evacuation
- prioritize urban or rural distribution
- maintain denial policies
- conceal the severity

The profile should create tension between war logistics, colonial authority, and civilian survival.

## Vietnam and Java 1944 to 1945 profiles

These profiles combine harvest shortfall, wartime control, transport disruption, requisition, and government choices.

### Vietnam

Potential conditions:

- Japanese occupation or military dominance
- disrupted internal transport
- crop damage
- requisition
- Allied bombing of transport
- regional movement restrictions
- weak or politicized relief

Political consequences can strengthen anti-colonial or revolutionary movements when relief failure is visible.

### Java

Potential conditions:

- occupation and forced requisition
- transport breakdown
- harvest loss
- forced labor removal
- isolation from normal trade
- weak relief capacity

The profile should connect hunger with forced labor and movement without assuming the same political outcome as Vietnam.

## Occupied Greece 1941 to 1942 profile

### Pressure composition

The Greek profile combines:

- occupation requisition
- Allied blockade or maritime isolation
- fragmented occupation administration
- damaged shipping and internal transport
- urban dependence on imported food
- island vulnerability
- black-market diversion
- refugee movement toward Turkey and safer areas

### Island emphasis

Aegean islands and other isolated Greek states can receive strong blockade pressure when maritime proof exists. The profile should use the shared island-blockade contract, not a scripted Greek exception.

### Movement

Possible flows include:

- internal movement from cities to rural areas
- island flight toward Turkey
- organized relief shipping
- trapped populations when borders or sea routes close

### Politics

Relief, occupation responsibility, black markets, and resistance can affect legitimacy and movement growth. The profile should not reduce the crisis to one occupier flag or one fixed mortality event.

## Siege of Leningrad profile

### Pressure composition

The Leningrad profile uses:

- prolonged encirclement
- winter
- high urban population density
- rail and land-route loss
- limited lake or air access
- bombardment and bombing
- military ration priority
- evacuation difficulty

### Gameplay

The defender can:

- maintain a relief route
- allocate scarce transport between military supply and civilians
- organize evacuation
- improve ration distribution
- conceal or publicize conditions

The attacker can:

- permit or deny civilian corridors
- intensify blockade
- attack relief routes
- accept neutral relief arrangements

The profile should emerge only when the city is actually isolated. It should end or recover when access is restored.

## Dutch Hunger Winter profile

### Pressure composition

The Dutch profile uses:

- occupied western urban states
- transport stoppage
- rail and canal disruption
- German restrictions or retaliation
- fuel shortage
- severe winter
- separation from food-producing regions
- delayed negotiations and distribution disputes

### Gameplay

The crisis can be prevented or reduced by reopening transport, negotiating relief, ending punitive restrictions, using air drops or neutral aid, and protecting distribution.

The profile should be concentrated in the relevant urban states. It should not apply to all Dutch territory.

## Francoist Spain early 1940s profile

This profile can represent a combination of autarky, diplomatic isolation, import restriction, poor distribution, and postwar damage.

Eligibility rises through:

- pro-Axis alignment that provokes Allied economic pressure
- import dependence
- low domestic production
- transport weakness
- state extraction and ration inequality
- corruption and black markets

The profile should not treat blockade as the sole cause. Foreign policy, domestic administration, and agricultural conditions all matter.

## Ireland historical memory profile

The Great Irish Famine lies far before the campaign. It should inform memory, migration culture, and policy sensitivity. It should not create an automatic active famine.

Possible effects:

- stronger public sensitivity to crop failure and export policy
- earlier emigration options during severe shortage
- diaspora destination ties
- greater political consequences from relief failure
- migration routes to Britain, North America, or other established destinations when the campaign supports them

The memory can make organized emigration more feasible while also increasing opposition to coercive food policy.

## Brazil drought and retirante profile

### Regional focus

The profile applies to drought-prone northeastern states, especially Ceará and connected routes.

### Pressure composition

- prolonged drought
- crop and livestock loss
- water shortage
- rural labor collapse
- movement toward cities and coastal states
- government efforts to control or confine drought migrants
- relief works and labor camps
- disease and overcrowding

### Gameplay

The government can:

- fund water and transport projects
- distribute migrants among safer states
- create public works with fair rations
- confine migrants near cities
- block movement
- encourage permanent settlement elsewhere

Confinement can become camp-like when movement is coerced and living conditions are lethal. Death ownership depends on famine, outbreak, forced labor, or forced displacement.

## Congo profile

The Congo profile should avoid reducing complex colonial and conflict history to one famine event.

It models interacting mechanisms:

- forced labor
- violence and village destruction
- displacement
- disease
- transport failure
- resource extraction
- loss of agricultural labor
- conflict around mines, roads, and rivers
- weak or predatory administration

The profile can activate under colonial extraction, civil war, occupation, or severe state collapse.

Political consequences can include anti-colonial movements, local armed groups, separatism, labor resistance, and foreign humanitarian pressure.

Famine mortality should occur only when food access collapses. Forced-labor, repression, outbreak, and displacement deaths retain their own reasons.

## Ethiopia profile

The Ethiopian profile draws from later cases of famine concealment, politicized relief, forced resettlement, and regime legitimacy loss.

It should be used as a dynamic policy analogue. It should not become a date-locked historical event.

Pressure components can include:

- drought
- civil war
- weak transport
- government concealment
- taxation or extraction of relief
- forced resettlement
- denial of access to opposition areas
- refugee flight into neighboring countries

The profile can create a strong legitimacy crisis when the government suppresses evidence while mortality rises.

## South American and Andean extensions

The famine and migration mechanics can support additional owner-specific regional profiles when natural-disaster and political systems provide exact evidence.

Possible directions include:

- drought-driven rural exodus
- flood and landslide displacement
- plantation or mining labor coercion
- conflict-driven movement across mountain and jungle routes
- urban reception crises
- cross-border sanctuary and forced return

These should use researched regional institutions and routes during implementation. The package does not assign generic identical behavior to the whole continent.

## Colonial and occupied territories

Colonial and occupied famine profiles should account for divided responsibility.

Possible responsible actors include:

- colonial metropole
- local colonial administration
- military occupier
- puppet authority
- local collaborators
- blockade enforcer
- relief donor
- rebel or insurgent authority

The system should attribute pressure and evidence to the actor that controls the relevant policy. It should avoid assigning every death to the map owner.

## Historical AI profiles

Historical AI should reproduce tendencies, not guaranteed outcomes.

Examples:

- Stalinist Soviet AI can favor extraction, concealment, movement restriction, and gulag expansion when regime security is prioritized.
- Soviet AI can still choose relief when military collapse, republic exit risk, or foreign exposure becomes severe.
- Nationalist Chinese AI can maintain military requisition too long during major war, then seek relief when legitimacy falls.
- Japanese occupation AI can prioritize military supply and forced labor in occupied Asian states.
- British imperial AI can prioritize shipping and military logistics, with relief becoming more likely under public pressure, spare convoy capacity, and secure routes.
- German occupation AI can use harsher requisition and movement restrictions according to ideology, resistance, and war pressure.
- Democratic and neutral AI can still close borders when capacity is low or outbreak risk is proven.

AI profiles must remain sensitive to resources, war state, survival, condemnation, and available routes.

## Historical names and text direction

Historical profile text should name real regions, actors, and policies when the campaign reproduces them. It should avoid claiming that every alternate campaign outcome exactly repeats the real event.

Text direction should emphasize:

- food access and route failure
- requisition and policy responsibility
- civilian movement and border response
- concealment and relief
- local political consequences

Atrocity and mass-death text should remain serious. It can use official euphemism, propaganda, or bureaucratic cruelty when that exposes the speaker. It should not use cheap jokes.

## Historical-profile acceptance

A historical profile is ready only when:

- its cause pattern is supported by research
- its chronology is correct
- its states and routes are mapped from the installed game
- its activation depends on campaign conditions
- its AI behavior is conditional
- its deaths remain dynamic
- its migration flows use real origin and destination states
- its relationship with existing events and systems is documented
- legal or causal disputes are described carefully
- no profile turns a historical death estimate into a target the script must reach
