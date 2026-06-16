# Event 013 — Natural Disasters: Full Source Specification, Part 1

## Event identity

**Event ID:** `13`  
**Event name:** Natural Disasters  
**Event type:** Minor Repeatable  
**Cluster:** Natural Disasters  
**Cluster member severity:** Low  
**Core promise:** a natural disaster strikes a clearly named place, damages industry and local population, leaves a visible recovery problem, and returns later in more varied forms as chaos rises.

Natural Disasters should feel like the world itself has become unreliable, but it should not become a silent global debuff. The event is a repeatable incident system with a public bulletin, a named disaster family, a named affected area, immediate state damage, casualty and displacement recording, local recovery decisions, occasional warning notices, and chaos-tier evolutions that change how many disasters can happen at once and how far their aftermath reaches.

This event must not become a one-click punishment where a random state silently loses factories. The player should read where the disaster happened, understand why the place was vulnerable, see what was damaged, and receive a credible recovery or mitigation route. The baseline hit remains noticeable but not campaign-ending. Higher evolutions make disasters more varied, regional, chained, and eventually abnormal.

## Player-facing premise

Reports arrive from a state, region, country, sea lane, river basin, mountain belt, volcanic zone, or coast. The first accounts are confused: a factory district has collapsed, rail yards are flooded, a town has disappeared under ash, reservoirs have failed, or the sky has burned with impossible fragments. Local officials ask for engineers, trains, medical workers, fuel, convoys, and temporary factory capacity. The event identifies the affected area clearly and records the incident in the event log.

The disaster itself applies the unavoidable immediate blow. The response layer determines whether the aftermath becomes a short recovery story or a second problem. Countries that invest in preparation, protect critical infrastructure, and respond with suitable resources reduce later damage and casualties. Countries at war, out of equipment, low on stability, cut off from supply, or suffering other Chaos Redux crises struggle to recover.

## Baseline firing model

The baseline event chooses one valid disaster target and one suitable disaster family. It fires as a minor repeatable event and counts as one event-system pacing incident. It should be able to repeat without stacking the same state indefinitely.

A baseline firing has four parts:

1. **Warning roll** — sometimes a warning report appears before the main disaster, especially for storms, floods, droughts, volcanic unrest, and high-chaos meteor activity. Warnings do not guarantee safety; they give a short mitigation window.
2. **Impact report** — the main event identifies the affected area and disaster family. It applies hidden immediate effects and shows one or two player-facing options with tone appropriate to the disaster and the country.
3. **Aftermath marker** — the affected state receives a disaster aftermath state modifier or a country receives a short national recovery pressure if the disaster is not state-bound.
4. **Recovery opportunity** — the affected controller receives one or more decisions or timed missions. Recovery is not mandatory for every tiny hit, but larger or evolved incidents should leave a playable cleanup choice.

### Baseline target size

The baseline should usually affect one state. It may affect one small area represented by a state group only when the disaster family makes a single state feel wrong, for example a river flood crossing two neighboring states, a coastal surge hitting a few ports, or a drought belt hitting several rural states. In calm and early chaos tiers the default is still one main state plus at most one nearby “spillover” state.

### Baseline impact strength

The baseline is repeatable. It must hurt, but the player should not lose a campaign because one minor repeatable disaster rolled early. A good baseline impact is:

- visible damage to one or several local buildings or infrastructure values;
- a small but real local population loss;
- a temporary local modifier that makes fighting, supply, production, construction, or recovery harder;
- a short event-log entry with the affected area and disaster family;
- a recovery decision that costs something concrete.

The damage should scale with state vulnerability and country resilience rather than use one flat value everywhere. Dense urban states, ports, lowlands, drylands, mountains, volcanic regions, and poorly supplied front states should feel different.

## Target selection principles

The implementation should use a reusable target-scoring helper instead of hand-picking global lists in every event option. State selection should prefer valid owned or controlled states with enough population or infrastructure to make the incident meaningful, but it should not always hit the same capitals.

### Valid target gates

A state can be a valid disaster target when:

- it is controlled by an existing country that can receive events;
- it has population, buildings, supply relevance, industry, a port, a railway, terrain vulnerability, or strategic importance;
- it is not already under a fresh identical disaster cooldown;
- it is not an uninhabited or irrelevant placeholder state unless the disaster is specifically wilderness/volcanic/meteor related;
- it can be named clearly in localisation.

A country can be a valid disaster owner when:

- it exists;
- it controls at least one valid state;
- it is not a nonhuman or incompatible special chaos actor unless the disaster family is designed to affect such actors;
- it is not excluded by a terminal world-end state.

### Target weighting factors

Use a weighted score. The score should not be visible to the player, but the resulting incident should feel plausible.

| Factor | Increases likelihood for | Design reason |
| --- | --- | --- |
| High population | earthquake, flood, storm, heat, wildfire, meteor fragments | more people and structures exposed |
| High civilian or military factories | earthquake, storm, meteor, fire, flood | industrial damage is part of the event promise |
| Coastal state and port | storm surge, tsunami, cyclone, flood | coastlines are physically relevant |
| Mountain/hills | earthquake, landslide, avalanche, volcanic adjacency | slope and fault vulnerability |
| Desert/arid terrain | drought, sandstorm, heat wave, dust storm | climate fit |
| Jungle/forest | wildfire after drought, flood, storm | vegetation and rainfall fit |
| High infrastructure and rail | earthquake, flood, storm, landslide | critical network disruption |
| Low infrastructure/supply | flood, drought, famine aftermath | recovery vulnerability |
| War zone/frontline | flood, earthquake, storm, refugee aftermath | relief harder under combat |
| Prior disaster memory nearby | aftershock, flood follow-up, famine, refugee pressure | supports chaining without daily polling |
| Chaos tier | all higher-intensity variants | world instability changes severity and pattern |

### Anti-repeat protection

The same state should not be hit by the same family again too quickly unless it is an aftershock or chain branch. The same country can receive multiple disasters in a campaign, but there should be a soft spread rule so the repeatable event does not feel like it is bullying one player for no reason. High chaos can loosen this protection, but not remove it completely.

## Disaster families

The event should begin with a curated set of disaster families that can be reused by evolutions. Each family needs a warning style, impact style, aftermath style, AI response, and asset direction.

### Earthquake

**Baseline use:** one state, especially urban, mountainous, or high-infrastructure states.  
**Primary damage:** buildings, infrastructure, railways, supply hubs, forts, and population.  
**Warning chance:** low at baseline; higher only as abnormal seismograph reports appear in evolutions.  
**Aftermath:** aftershocks, ground failure, damaged factories, rescue work, broken rail arteries.  
**Option tone:** official shock, engineers called in, denial by authoritarian regimes, terrified public reports.

Earthquakes are the most direct industrial-damage disaster. They should use a different local modifier from storms or floods: high construction repair pressure, supply disruption, and factory output reduction rather than a generic “bad state” modifier.

### Flood and river failure

**Baseline use:** river basins, lowlands, states with infrastructure, agriculture, or ports.  
**Primary damage:** infrastructure, railways, civilian industry, population, supply, temporary movement penalties.  
**Warning chance:** medium; warnings can trigger flood-barrier or evacuation decisions.  
**Aftermath:** waterborne disease pressure, damaged bridges, displaced civilians, food disruption.  
**Option tone:** warnings ignored, sandbags, railway embankments, evacuation trains.

Floods should support small multi-state variants earlier than other families because river systems often cross borders. This does not make the baseline global; it creates a named basin incident.

### Storm, cyclone, blizzard, and coastal surge

**Baseline use:** coastal states, islands, ports, plains, severe winter or monsoon-like regions.  
**Primary damage:** ports, naval bases, airfields, infrastructure, dockyards, supply, population.  
**Warning chance:** high; the warning event should name the coastline or region.  
**Aftermath:** blocked ports, wrecked convoys, refugee pressure, supply delay.  
**Option tone:** harbours closed, fishermen lost, weather offices blamed, armies stuck in mud or snow.

Storm variants should distinguish ordinary storm, coastal surge, severe winter storm, and high-chaos hyperstorm. The player should not read “storm” for every weather disaster.

### Drought and crop failure

**Baseline use:** arid, steppe, desert, plains, or vulnerable agricultural states.  
**Primary damage:** population loss is slower; direct building damage is lighter; local supply, recruitable population growth, resistance/compliance, and stability pressure matter more.  
**Warning chance:** high but slower; drought is one of the best families for warning and mitigation events.  
**Aftermath:** famine risk, refugee movement, livestock collapse, water rationing, industry slowdown where water matters.  
**Option tone:** crop reports, grain offices, ration cards, propaganda about rain.

Drought should not feel like an earthquake with a different icon. It should lean on timed missions: protect granaries, keep rail routes open, import food, spend convoys/trains, or accept stability/war-support pressure.

### Wildfire and industrial firestorm

**Baseline use:** forest, dryland, high-factory, high-chaos states.  
**Primary damage:** infrastructure, civilian factories, military factories, population, temporary local construction and supply penalties.  
**Warning chance:** medium; can follow drought.  
**Aftermath:** smoke, evacuation, damaged forests, rail closure, factory fire investigations.  
**Option tone:** ash on the windows, volunteer fire brigades, factory sirens.

Wildfire should connect to drought memory and high-heat events. If Event 51 Heat Wave exists separately, Natural Disasters should not replace it. Instead, it can read heat-wave or drought flags when present and make fires more likely.

### Landslide, avalanche, and dam failure

**Baseline use:** mountainous states, high-infrastructure states, river states, states with rail/supply importance.  
**Primary damage:** infrastructure, supply hubs, railways, population, temporary movement penalty.  
**Warning chance:** low for landslide, medium for dam strain.  
**Aftermath:** blocked passes, unstable slopes, downstream flood risk.  
**Option tone:** mountain roads gone, railway tunnels buried, dams groaning.

This family is valuable because it gives small countries and mountain regions disaster identity without always using earthquake.

### Volcanic unrest and eruption

**Baseline use:** only where volcanic-region selection can be built reliably. If exact volcanic state mapping is not available, start with a curated scripted state group and document it.  
**Primary damage:** infrastructure, airbases, supply, population, factories near eruption, temporary air/visibility penalties through state modifiers.  
**Warning chance:** high for unrest, low for sudden high-chaos eruption.  
**Aftermath:** ashfall, lahars, port disruption, airbase closure, crop damage.  
**Option tone:** mountain smoke, evacuation bells, ash on factory floors.

Volcanoes should become more important in Evolution IV, where massive eruptions can become world-affecting without creating a world-end scenario.

### Tsunami

**Baseline use:** normally a follow-up to earthquake or volcanic/meteor ocean impact; rare as a direct family.  
**Primary damage:** coastal infrastructure, ports, naval bases, dockyards, civilian factories, population.  
**Warning chance:** high only when chained from a detected offshore earthquake or volcanic collapse; otherwise low.  
**Aftermath:** refugee pressure, contaminated water, port closure, coastal reconstruction.  
**Option tone:** sea withdrawals, sirens, ships on streets, broken harbours.

Tsunami should not fire randomly in landlocked places. It is a chain family.

### Meteor fragments and abnormal skyfall

**Baseline use:** not at baseline except extremely rare flavour warning.  
**Primary damage:** state buildings, population, supply, airbases, sometimes naval or coastal if offshore.  
**Warning chance:** low early, stronger in Evolution IV with observatory warnings.  
**Aftermath:** crater fields, fires, panic, possible tsunami if ocean impact, high-chaos lingering “skyfall scars.”  
**Option tone:** astronomers uncertain, ministries denying the sky has artillery, fragments through roofs.

This family defines Evolution IV and the manual disaster barrage scenario. It must not turn Event 13 into the separate Event 28 Asteroid Incoming. Asteroid Incoming remains a distinct large-object calculation story; Natural Disasters handles smaller meteor showers and regional impact swarms.

## Warning events

Old notes specifically asked for more warning events and clearer affected countries/regions. The warning layer should be a first-class part of this rework.

Warning events should be short, uncertain, and actionable. They should never read like debug alerts. A warning can be wrong, late, or only partly useful. It should name the area and offer one or two temporary preparations:

- evacuate industrial districts;
- pre-position relief trains;
- close ports or move convoy routes;
- reinforce flood barriers;
- inspect dams and rail bridges;
- move air wings from a vulnerable airbase;
- stockpile grain or water;
- call up engineers;
- warn neighboring states if the family can spill over.

Preparations should cost concrete resources. Good costs include trains, trucks, convoys, fuel, infantry equipment for guards, support equipment for engineers, civilian factory days, command power for military engineers, and stability/war-support tradeoffs. Political power can appear for public administration but should not be the default.

Warning success should reduce or redirect damage, not cancel the disaster entirely in most cases. Canceling should be rare and tied to smaller storms, dam failures, or wildfire containment.

## Recovery system

Natural Disasters needs a visible recovery layer so the player does not only watch damage happen. Recovery should be optional for small baseline events and important for evolved or high-severity incidents.

### State aftermath modifiers

Use family-specific modifiers instead of one universal disaster modifier.

| Modifier family | Use | Gameplay feel |
| --- | --- | --- |
| `recent_earthquake_damage` | earthquakes and aftershocks | repair, supply, production disruption |
| `flooded_transport_belt` | floods, storm surge, tsunami | movement, supply, port and rail problems |
| `crop_failure_pressure` | drought and famine chains | food, stability, manpower, refugee pressure |
| `storm_wreckage` | storm and blizzard | ports, airfields, supply, infrastructure repair |
| `burned_districts` | wildfire and firestorm | construction repair, factory output, local population |
| `unstable_mountain_passes` | landslide/avalanche | movement, supply, rail chokepoints |
| `volcanic_ashfall` | volcanoes | airbases, supply, crop and industry disruption |
| `tsunami_scoured_coast` | tsunami | ports, dockyards, population, water safety |
| `meteor_scars` | meteor showers | mixed heavy local damage, panic, abnormal high-chaos effect |

The modifiers should have durations scaled by disaster severity and recovery choices. Strong recovery should shorten or replace them with a lighter `rebuilding_underway` style modifier.

### Country recovery pressure

A country with multiple active disaster states should receive a national recovery pressure idea or scripted-localisation summary. It should show current active disaster count, worst disaster family, displaced population pressure, and relief capacity. This can be shown in the Disaster Response decision category rather than as a permanent idea stack.

### Recovery decisions and missions

Recovery should not be a store. The player should be asked to commit actual resources to the affected state or region. Details are mapped in the decision/mission prompt, but the core loop is:

1. A disaster creates an aftermath marker and a relief need.
2. The decision category shows only relevant current actions.
3. The player chooses between fast emergency aid, slower infrastructure recovery, population relief, and industry repair.
4. Missions can auto-complete when the player keeps supply connected, controls the state, repairs infrastructure, or keeps convoys/trains available.
5. Failure leaves a weaker but real follow-up problem: extra displacement, longer modifier, stability pressure, or delayed industrial recovery.

## Event options and tone

Event options should have character without turning mass death into a joke. Minor local incidents can use irony; severe disasters should use grim official language, bitter understatement, or self-condemning propaganda.

Examples of option tone directions:

- Democratic or reformist state: “Send the engineers before the speeches.”
- Authoritarian state: “The province will be grateful when it stops trembling.”
- Communist state: “The workers will rebuild the district from the rubble.”
- Fascist state: “The earth has no permission to interrupt production.”
- High-chaos meteor report: “The sky has filed its own declaration.”
- Drought report: “The grain ledgers are thinner than the fields.”
- Volcanic ash report: “The mountain has entered the war.”

Implementation may write final event option text from these tone directions. Event Details text must describe the situation and premise, not list mechanical effects.

## Event log and details window

Every firing should record:

- event ID 13;
- disaster family;
- affected state, region, or country;
- severity band;
- whether it had a warning;
- whether it produced a chain or aftermath;
- whether it was a baseline firing, evolved burst, regional disaster, high-chaos abnormal variant, or manual scenario member.

The Events tab detail window should explain Natural Disasters as a repeatable world condition with local, regional, chained, and abnormal variants. It should not list exact modifiers. The History detail should show the specific fired disaster and affected area. The Evolution tab should show the evolution stage as a mutation track, not every ordinary disaster stage.

## Cluster role

Natural Disasters belongs to the **Natural Disasters** cluster as its only current member. Do not add Event 43 Massive Flood, Event 51 Heat Wave, Event 99 Sandstorm, or any other similar event to this cluster during this rework. The cluster exists so later disaster-related events can be attached deliberately, not as a dumping ground.

Since the cluster currently has only Event 13, automatic cluster firing should behave almost exactly like the event firing, while the cluster catalogue can show “Natural Disasters” as a future-ready category. The cluster member severity for Event 13 should remain **Low** at baseline because individual repeatable disasters are meant to be manageable. Evolved bursts and manual scenarios may show stronger incident severity inside the event detail, but the cluster membership itself remains low until more event members are added.

## No world-end scenario

There is no automatic world-end scenario for Natural Disasters. Even massive eruptions, meteor showers, regional tsunamis, and continent-wide storm paths remain high-chaos disaster evolutions, not a terminal campaign ending.

The event can have super-event-level presentation for the first abnormal Evolution IV disaster burst or for a manual maximum-intensity disaster barrage, but that presentation must not set the `world_end` flag. If a disaster branch becomes truly terminal during implementation, it belongs in a different future event or a separate accepted spec.

## Manual triggerable scenario

Natural Disasters should have a manual triggerable scenario for sandbox testing and challenge campaigns. Working scenario label: **Global Disaster Barrage** — role label, not final localisation.

The scenario launches a compressed sequence of selected disaster families in a short period. It must be directly fireable from the scenario UI unless a terminal world-end state blocks all scenarios. It should not require chaos level, prior Natural Disasters evolutions, date gates, or previous disaster history.

### Scenario intensity

| Intensity | Intended behavior |
| --- | --- |
| Low | 3–5 local disasters over several weeks, mostly baseline families. |
| Medium | 6–9 disasters, mixed local and small regional events, limited chains. |
| High | 10–14 disasters, several regional incidents, stronger aftermath, one abnormal variant possible. |
| Maximum | 16–24 disasters in a compressed disaster week, many regions affected, Evolution IV variants allowed, high chance of meteor shower and massive volcanic or tsunami chains. |

### Scenario type options

| Type | Meaning |
| --- | --- |
| Random Barrage | weighted mix of all eligible families. |
| Geological Crisis | earthquakes, volcanoes, landslides, tsunamis, aftershocks. |
| Weather Crisis | storms, floods, droughts, wildfires, blizzards, sand/dust storms. |
| Skyfall Crisis | meteor fragments, impact fires, possible coastal tsunami chains. |
| Full Catalogue | attempts to fire at least one incident from every implemented family, then fills remaining slots by intensity. |

The scenario should use the same helpers as normal Event 13 where possible, but it should record that the incidents came from the manual scenario so balance and event log review are clear.

## Relationship to Event 46 “Earth Earthquake”

Event 46 currently exists as **Earth Earthquake**, described as applying slight global building damage. This rework absorbs that idea into Natural Disasters Evolution IV. The old Event 46 should be stripped of gameplay content, kept only as a placeholder, renamed or marked as unknown according to project convention, and removed from normal random-event selection if the system supports placeholder disabling.

The absorbed concept becomes a high-chaos disaster variant inside Event 13:

- not a normal repeatable event;
- not a full world-end scenario;
- a rare abnormal global/semi-global earthquake wave;
- triggered by Evolution IV or the maximum manual scenario;
- implemented through Event 13 disaster-barrage helpers so it records affected regions and can apply aftermath instead of silently damaging all buildings everywhere.

## Connections with other Chaos Redux systems

### Chaos Meter

Natural disasters should usually add modest chaos through death, displacement, and infrastructure shock. The event should not flood the Chaos Meter by itself at baseline. Higher evolutions can add more chaos, especially when multiple countries are hit, critical infrastructure collapses, or disasters chain into famine/refugee pressure.

### Deaths system

Population loss from disasters should feed the shared deaths tracker where available. The baseline should record civilian deaths as disaster-related rather than military deaths. Combat losses caused indirectly by supply penalties should remain normal military losses.

### Air cleanliness and contamination

Most natural disasters should not affect air cleanliness. Volcanic ash, wildfire smoke, high-chaos acid-rain-like storms, and meteor dust can add small temporary contamination or air-cleanliness pressure if the existing air system supports it. These effects should remain much smaller than chemical, biological, nuclear, or thermonuclear sources.

### Condemnation

Natural disasters are not a condemnation source unless a country deliberately uses the disaster for atrocities, blocks aid, weaponizes relief, or lies about foreign aid in a later future branch. This rework does not add a condemnation route by default.

### Chemical and biological warfare

Floods, droughts, refugee camps, and damaged water systems can make biological outbreaks or contamination cleanup harder if those systems are active. The link should be event-driven and state-based, not a new global daily loop. Natural disasters should not become a biowarfare event.

### Other disaster-like events

Do not delete or absorb every disaster-like event in the catalog. Event 43 Massive Flood, Event 51 Heat Wave, Event 99 Sandstorm, Event 28 Asteroid Incoming, and similar future events may remain separate concepts. Event 13 can read their flags or share helpers later, but this rework only explicitly absorbs Event 46 Earth Earthquake because the user requested that integration.
