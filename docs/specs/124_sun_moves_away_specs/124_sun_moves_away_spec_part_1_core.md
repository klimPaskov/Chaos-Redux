# Event 124: Sun Moves Away

## The experience

The Sun recedes and the familiar distinction between a safe working day and a dangerous night disappears.
The map visibly darkens across the whole world, armies fight under the normal rules of night at every hour, and every state enters an unnatural winter.
Governments must keep homes warm, move food through failing transport networks, maintain exhausted industries and protect communities whose roads become increasingly unsafe.
The crisis has no fixed expiry date.
Return of the Sun is its resolution, and the world remains continuously dark until that resolution takes effect.

The player should feel an immediate change to the campaign and then make difficult choices about the distribution of scarce capacity.
A large army can secure a corridor while consuming the fuel needed by nearby shelters.
A prosperous city can keep its factories and hospitals operating while the settlements supplying it become isolated.
A small country can protect a few communities effectively through local labor, careful routing and outside assistance, even when it cannot sustain a large refuge network.
Success means preserving people and functioning services through an uncertain crisis, followed by repair of the real damage that remains.

All new labels in this package are working design labels and text direction.
The supplied event and evolution names are retained from the brief.
Final player-facing wording belongs to the later localisation and source-research passes.
Numeric balance anchors in these specifications are proposed tuning unless expressly identified as a requirement from the brief or a documented system constraint.
The gameplay design in this part is an unresolved proposal and nothing in it is accepted, implemented or validated.
The two central engine mechanisms, reversible whole-map daytime darkness and normal native night combat at every hour, remain unproven.

## Identity and campaign position

| Field | Proposed design |
| --- | --- |
| Event | 124, Sun Moves Away (catalog identity) |
| Former catalog ID | 136, retained as migration history |
| Classification | Major, fire once in an ordinary campaign |
| Initial availability | Proposed minimum Chaos tier 2 |
| Cluster relationship | Proposed High member of Natural Disasters, cluster 5 |
| Ordinary outcome | Return of the Sun, followed by recovery of actual harm |
| Evolution thresholds | Deep Freeze at 400+, Things in the Darkness at 600+, The Endless Night at 800+ |

The Major uses the existing adaptive Major selection and buildup system.
Its severity does not turn it into a repeatable minor disaster.
A cluster activation counts once for shared pacing while each actual member retains its own consequences and history.
Core entry, responses, evolutions, AI, manual setup, Return and recovery operate with the base game, without a required DLC.
Event 124 is the catalog identity of Sun Moves Away, with former catalog ID 136; the previous catalog Event 124, Demilitarization, moved to 114, so 124 is free for this event.
The identity history is recorded in the [research record](124_sun_moves_away_research_and_sources.md).
Super-event presentation slots, playback audio IDs and scenario IDs are separate namespaces, so any such number this package proposes must still be checked against the shared identifier registry.

## Three simultaneous world changes

### Persistent map darkness

The ordinary world map becomes visibly darker at all locations, including locations where the normal clock indicates daytime.
Darkness must remain apparent in the ordinary strategic and political views used to conduct a campaign.
It persists through opening and closing windows, camera movement, zoom changes, saves, reloads, evolution transitions, newly released countries and changes of player country.
Normal time continues to advance.

The change must preserve usable province selection, frontlines, orders, labels, ports and unit counters.
Interface text and important symbols need sufficient contrast, and selections require shape or outline cues as well as color.
An accessibility adjustment may improve contrast without restoring normal daylight to the world.
Every client in a multiplayer campaign receives the same authoritative crisis state.

The production mechanism must establish a reversible world presentation change tied to this episode.
The inspected sources have not established that mechanism.
A popup, a selected thematic map mode, a full-screen opaque panel or a permanent campaign-wide asset edit cannot stand in for this requirement.

### Night rules at every hour

Combat uses the normal nighttime rules throughout the crisis, including hours that the ordinary calendar would classify as daylight.
This covers each combat domain to which the installed game normally applies night penalties.
Existing technology, doctrine, equipment and trait interactions with nighttime must retain their normal meaning.
An army that has invested in night fighting therefore gains a real relative advantage.

The event applies the effective night condition once.
Actual nighttime must not add a second copy, and ordinary daytime must not receive an unrelated penalty whose interaction with night mitigation differs.
Relief spending, factory lighting and refuge construction do not switch this global condition off locally.
The normal day and night cycle resumes immediately on Return.

The inspected modifier references show modifiers that affect existing night conditions, which does not establish a supported way to make daytime count as night.
The coding handoff must resolve this capability before claiming an implemented event.
The design requirement remains intact while that mechanism is unresolved.

### Winter in every state

All states experience the environmental crisis, including tropical, desert, unowned and nonhuman-controlled states.
The event does not require every place to have identical snowfall or identical mortality.
It requires cold-related disruption across the world, with consequences scaled by climate preparedness, terrain, transport, exposed population and functioning relief.
States that already experience winter remain affected by the additional anomaly.

The table defines intended net Sun-owned contributions in a substantially unprotected, ordinary affected state.
The implementation must choose supported fields and avoid charging the same simulated weather loss twice.

| Consequence | Baseline target | With Deep Freeze active | Design meaning |
| --- | ---: | ---: | --- |
| Land movement | About -15% | About -30% | Cold, poor visibility and route servicing slow movement |
| Delivered supply capacity | About -15% | About -30% | Routes and handling facilities operate below normal capacity |
| Construction and repairs | About -10% | About -20% | Cold and lighting requirements occupy workers and machinery |
| Cold-related equipment burden | About +10% relative attrition pressure | About +20% | Maintenance and equipment losses become material concerns |
| Agricultural production exposure | About 25% of normal affected production at risk | About 50% at risk | Famine receives proven affected-population pressure through its owner |

These targets describe a balance outcome, not five asserted native modifiers or an instruction to create a new food-stock currency.
Agricultural exposure does not immediately erase stored food, and different crops, imports and reserves produce different outcomes.
Loss of delivery and loss of production are distinct receipts so the same shortage is not counted twice.

Prepared cold-weather services can reduce the avoidable part of environmental disruption by up to 40% before additional paid local work.
Relief can reduce the service failures that cause deprivation, famine and direct exposure deaths.
It cannot erase the world condition or grant every state full protection through a national click.
Any existing weather contribution used to deliver these targets must be measured against a matching ordinary-weather baseline.
Independent environmental damage from another owner remains independent.

## Sunlight Deprivation

Sunlight Deprivation combines disrupted routines, exhaustion, reduced morale and impaired work over a prolonged period of darkness.
The player first encounters coordination and sleep problems, then the burden of maintaining workers, soldiers and families without ordinary daylight.
Nutritional problems can deepen during a long crisis, especially where food access is poor.
Ordinary electric light is useful for work and movement but does not provide food or establish vitamin D production.
The contextual evidence and its limits are recorded in the [research record](124_sun_moves_away_research_and_sources.md).

| Exposure band | Proposed unprotected national contribution | Responses that matter |
| --- | --- | --- |
| Initial disruption, approximately the first 15 days | Organization recovery -5%, factory output -5%, stability -5 percentage points | Clear schedules, functioning services and reliable public information |
| Established exhaustion, approximately 15 to 60 days | Organization recovery -15%, factory output -10%, stability -5 points | Rest rotations, clinics, food distribution and secure travel |
| Prolonged exposure, beyond approximately 60 days | Organization recovery -25%, factory output -20%, stability -10 points | Sustained essential services and targeted nutrition through actual food access |

The dates are exposure tuning bands, with service history affecting the transition and strength.
They are not medical claims or universal deadlines for illness.
The computation uses actual time exposed and actual intervals of service.
Changing policy or briefly crossing a border does not reset exposure.
Existing exhausted states can remain vulnerable while their governments reorganize.

Effective protection can mitigate up to 60% of this event's deprivation contribution.
That limit leaves a meaningful cost of living through the anomaly even in a well-run country.
Industry-specific relief reduces only the industrial contribution it actually supports.
The same reduction cannot be applied again through a second national carrier.

Return removes these temporary Sunlight Deprivation effects immediately, as required by the brief.
Actual injuries, deaths and food-system damage already recorded remain with their owners.

## Two public national values

### Civilian Protection

Civilian Protection ranges from 0 to 100 and describes the population-weighted share of eligible human residents whose essential services are functioning.
For a locality, protected capacity is limited by its weakest essential service among shelter and warmth, delivered food access, local safety, and a workable rest and basic care routine.
Installing lights without fuel, food, staff or safe access cannot produce a fully protected settlement.

The national value weights actual residents currently under the country's responsibility.
Occupied residents are included when the applicable civilian-system owner accepts the owner and controller relationship.
Exact population eligibility remains with that owner.
The environmental crisis continues in states that do not qualify for a human relief adapter.

Food access reads the shared famine system's supported state projection.
It is not a new inventory of food, and the event does not copy the Famine panel's values into its own persistent dashboard.
Warmth and protection depend on operating services and receipts for the population those services can reach.
Evacuating residents moves their protection needs to the actual destination and cannot create coverage at both ends.

A high value limits avoidable civilian harm and reduces the appropriate deprivation contribution.
A low value makes untreated exposure, interrupted work, flight and vulnerability to incidents more likely.
The proposed meaningful national bands are below 35, 35 to 59, 60 to 79, and 80 or above.
Their final wording should communicate failing, strained, functioning and resilient services without exposing a hidden medical score.

### Establishing ordinary service capacity

Entry assesses the services that existed before the crisis and then applies the new environmental burden.
It does not start every resident at zero protection or give every country a completed relief program.
Shelter and staffing derive from documented state settlement and infrastructure data, adjusted for actual damage and access.
Warmth preparedness derives from the state's climate exposure and usable service capacity, with its initial burden changed by the active opening and manual intensity where applicable.
Food access comes from the valid famine owner, safety from actual access and living threats, and routines from functioning local services and exposure history.
The initial model must be deterministic and use the same capacity bounds as later paid work.

The first balance pass should place severely unprepared or disconnected states below 35 protection, strained but functioning communities around 40 to 60, and well-prepared supplied communities around 65 to 75.
These are calibration targets for the documented service assessment, not assigned national constants or a historical claim about named countries.
An already well-protected population can begin above those ranges when the underlying service proof supports it.
Missing owner data displays an unverified condition and must be resolved through the supported initialization contract, without fabricating food, heat or delivery.
The corresponding scarce-country, prepared-country and existing-famine fixtures verify that the initial assessment remains meaningful.

### Lifeline Reliability

Lifeline Reliability also ranges from 0 to 100.
It weights the actual delivery of essential services by the demand assigned to critical domestic and overseas corridors.
An established route contributes while delivery works, even if the player did not purchase a special event project for it.
A newly protected corridor contributes only as it supports actual service.

Road distance, rail or port damage, weather disruption, combat, convoy availability, custody and receiving capacity can limit delivery.
Putting soldiers in a state is not sufficient evidence that an overseas shipment arrived.
The relevant owner must establish route and delivery facts.
An inland country is not penalized for lacking an ocean route it does not need.
An island is not assigned famine merely because it is an island.

The same qualitative bands as Civilian Protection make the value readable, although its effects differ.
Improving reliability prevents supply interruptions and makes existing food, heat and equipment usable at their destination.
It does not manufacture those supplies.

### Display discipline

These are the only two persistent public mechanic values created by this event.
The panel may show actual costs, current equipment balances, dates, required service conditions and native mission progress where an action needs them.
State condition appears qualitatively, with a concrete explanation of the failed service and an available response.
There is no extra public meter for terror, darkness, research, predators, health or time until sunrise.
Shared Famine and Migration retain their own authoritative interfaces.

## National allocation choices

Countries choose one continuing priority at entry and can later change it through a paid reorganization.
The choice directs scarce capacity and changes the efficiency of eligible work.
It does not grant completed buildings, stocks, divisions or perfect coverage.

| Priority | Main advantage | Continuing tradeoff | Best circumstances |
| --- | --- | --- | --- |
| Distributed civilian relief | More affordable dispersed warmth, kitchens, clinics and road servicing | Greater labor and transport burden, slower discretionary construction | Large rural populations, accessible local routes, governments able to sustain broad services |
| Strategic continuity | Better protection of selected industry, hospitals and high-demand supply corridors | Rural protection grows more slowly and protected corridors consume real equipment and fuel | Major wars, industry concentrated along a few vital routes, threatened transport nodes |
| Concentrated refuge support | More efficient service for residents who can reach a functioning supplied settlement | Reception pressure, evacuation costs and greater danger in abandoned hinterlands | Damaged rural regions, constrained logistics, later sustained refuge networks |

Every priority retains basic warmth, food, security and evacuation responses.
The player can make exceptions when local conditions justify them.
Switching has a political and administrative cost and a short reorganization period, while existing supply debts, paid commitments and damage persist.
Repeated switches cannot refill services, reset deadlines, erase exposure or produce repeated Chaos reductions.

The event uses at most three national spirit slots for a country.
They communicate the environmental crisis, Sunlight Deprivation or the eligible purely nocturnal counterpart, and the selected allocation commitment.
State and family-specific effects carry their own exact scope and do not become a stack of additional national spirits.
The visual design is specified in [part 7](124_sun_moves_away_spec_part_7_presentation.md).

## The ordinary lifecycle

| Stage | What happens | Player responsibility |
| --- | --- | --- |
| Manifestation | Commit one global episode, darkness, night rules and winter exposure, then notify countries | Choose an allocation priority and identify the most exposed places |
| Adaptation | Routes, homes and workplaces reveal the gaps in existing preparedness | Establish affordable services and protect critical deliveries |
| Sustained crisis | Exposure, agricultural losses and incidents continue through owner-controlled cadence | Keep commitments supplied, change priorities and respond to new needs |
| Return of the Sun | Resolve the episode once and remove all temporary Sun effects immediately | Assess the actual damage and continue necessary relief |
| Recovery | Famine, displacement and damaged infrastructure continue under their owners | Reopen routes, restore services and support durable resettlement or return |

The first three stages do not automatically unlock evolutions.
An ordinary country can survive a long baseline episode, and a high-Chaos opening can begin with an enabled evolved behavior set.
The exact evolution and Return rules are in [part 2](124_sun_moves_away_spec_part_2_evolutions_and_return.md).

All countries receive the world condition through the single global episode.
Local acknowledgements do not replay global effects.
The initial policy has a conservative default when a country has no responding player.
New and released countries inherit only current environmental obligations and valid local physical assets, with their own lawful payment and registration identity.
Country removal, annexation and civil war cannot leave an old payer receiving a benefit without a valid holder.

## What makes a good run

A strong response is a functioning pattern of services that survives shortages and attacks.
It protects people at real opportunity cost, uses the current food and migration systems honestly, and remains affordable after the first payment.
The action and mission map in [part 4](124_sun_moves_away_spec_part_4_decisions_missions.md) makes those commitments concrete.
The country and incident design in [part 3](124_sun_moves_away_spec_part_3_incidents_and_countries.md) ensures that different situations create different choices.
The AI and balance framework in [part 5](124_sun_moves_away_spec_part_5_ai_balance.md) applies the same rules to computer-controlled countries.

The event is complete as an implementation only when its map, combat, civilian, creature, lifecycle and presentation requirements work together.
Source correctness alone does not establish the two unresolved engine mechanisms.
Their evidence requirements remain explicit in the [acceptance matrix](124_sun_moves_away_acceptance_matrix.md).
