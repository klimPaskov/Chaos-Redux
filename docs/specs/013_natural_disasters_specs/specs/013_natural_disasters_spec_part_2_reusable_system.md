# Event 013 Natural Disasters, Part 2, reusable dynamic disaster system

## The disaster season controller

The controller turns one Event 013 firing into a season. A season is a list of planned impacts with target, family, severity, delay, news behavior, report behavior, aftermath behavior, and chain behavior.

The controller should prepare the whole season before the first impact when possible. That lets the system avoid same-day hits, repeat targets, and news spam. It also lets the manual Disaster Barrage scenario show the player a coherent event rather than a random shower of unrelated popups.

### Season state

A season should store these ideas in variables, flags, arrays, or event targets according to implementation needs.

| State concept | Design role |
| --- | --- |
| Season id | Distinguishes one Event 013 sequence from another. |
| Caller type | Random, cluster, scenario, external event, scripted actor, or debug. |
| Anchor country | The country used for reports, log actor fallback, or scenario launch context. |
| Anchor region | Optional region around which family weights cluster. |
| Disaster queue | Ordered list of impact entries with family, target, delay, severity, and policy. |
| News throttle ledger | Prevents weak repeated news and keeps strong family news meaningful. |
| Report ledger | Ensures affected countries reliably receive delayed reports. |
| Aftermath ledger | Tracks active disaster cards, recovery work, failure risk, and cleanup progress. |
| Death ledger | Feeds civilian deaths into the shared Deaths system with family type and state. |
| Damage ledger | Records damaged building categories, transport disruption, and recovery needs. |
| Chain ledger | Stores delayed follow-up candidates such as aftershocks, famine, disease, and tsunamis. |

The system should avoid global permanent event targets unless the season must persist across unrelated event chains. When persistent references are needed, the cleanup design must clear them when the season ends.

## Family resolution order

An impact should resolve in this order.

1. Confirm the target is still valid.
2. Recalculate local vulnerability at impact time.
3. Run warning outcome if a warning was scheduled.
4. Apply family-specific impact damage.
5. Feed civilian deaths into the Deaths system.
6. Create or refresh state modifiers.
7. Schedule the affected-country report in 1 to 2 days.
8. Open or refresh aftermath category notification for the affected country.
9. Roll family-specific chains if severity and aftermath allow it.
10. Decide whether a news event is still meaningful after throttling.
11. Advance the queue and schedule the next delayed impact.

This order keeps the affected country report honest. It reports what happened after the damage is known, rather than announcing a planned disaster that later fails due to invalid target state.

## Warning model

Warnings are not a global agency. They are family-specific and local.

Examples of warning sources include seismographs, river gauges, coast observers, lighthouse reports, ship traffic, radio weather stations, railway engineers, port masters, forest patrols, mountain villages, local pilots, observatories, and military scouts. The text should not frame warnings as a single world disaster channel.

Warning success should reduce deaths, building loss, and aftermath difficulty, but it should not erase a serious disaster. A successful warning can turn a catastrophe into a hard recovery problem. A failed warning can make the same severity feel sudden and brutal.

Warning odds should vary by:

- country stability and war state
- infrastructure, radar, airfields, naval access, and railways
- relevant state terrain and ports
- disaster family
- chaos tier
- previous family memory
- completed preparation decisions
- active occupation, resistance, bombing, supply failure, and communication disruption

## Preparation decisions before impact

Warnings can open short-lived preparation decisions. These should use concrete costs and not become political power purchases.

| Preparation action | Suitable costs | Families |
| --- | --- | --- |
| Evacuate exposed districts | trains, trucks, fuel, manpower, stability risk | flood, tsunami, cyclone, volcano, wildfire, meteor warning |
| Close ports and move ships | navy XP, fuel, convoys, dockyard disruption | cyclone, tsunami, storm surge, volcanic ash, wind |
| Disperse aircraft and crews | air XP, fuel, support equipment, temporary mission penalty | hail, cyclone, ash, meteor, thunderstorm |
| Reinforce rail embankments | trains, support equipment, civilian capacity | flood, earthquake, landslide, blizzard |
| Open shelters and field kitchens | infantry equipment, support equipment, manpower | heat, cold, blizzard, wildfire, dust, flood |
| Pre-position medical teams | support equipment, manpower, stability or war support burden | all high-casualty families |
| Firebreak and reservoir work | trucks, fuel, local support, civilian capacity | wildfire, drought, heat |
| Observatory watch | air XP, radar presence, command attention | volcano, meteor, cyclone, tsunami |

A warning window can be too short for all actions. The player should choose what kind of loss to reduce. AI countries should pick actions based on family, capacity, and war state.

## Impact scoring

Impact scoring should not be one flat random roll. Each family should build an impact profile.

| Profile component | Meaning |
| --- | --- |
| Direct death | Immediate population loss from collapse, drowning, heat, cold, fire, ash, blast, or debris. |
| Secondary death | Delayed losses from famine, disease, exposure, refugees, blocked medicine, or failed recovery. |
| Industrial damage | Factory, dockyard, resource, and building loss or repair burden. |
| Transport damage | Infrastructure, rail, port, supply hub, and convoy disruption. |
| Military disruption | Temporary supply, organization, movement, airbase, naval base, or attrition effects. |
| Social disruption | Stability, war support, local order, refugee pressure, and resistance effects. |
| Chain pressure | Chance to create follow-up aftershocks, floods, fires, famine, disease, or displacement. |

Each disaster family should weight these components differently. This is what makes a blizzard feel different from a tsunami and a wildfire different from an earthquake.

## Death scaling bands

The implementation can tune exact numbers, but the design bands should remain strong.

| Band | Intended use | Population loss direction |
| --- | --- | --- |
| Local hard hit | Baseline serious disaster in one state | Enough to matter in Deaths UI, often thousands to tens of thousands |
| Severe local hit | Dense state or failed warning | Tens of thousands to low hundreds of thousands |
| Regional system | Evolution II spread over nearby states | Large aggregate deaths, with vulnerable regions crossing hundreds of thousands |
| Catastrophic chain | Evolution II follow-up famine, disease, tsunami, major flood, or regional quake | Deaths continue across weeks or months if recovery fails |
| Abnormal disaster | Evolution III meteor, rupture wave, massive eruption, storm corridor, or global tsunami chain | Major death spikes, potentially multi-million aggregate losses |

Dense states should naturally produce larger absolute deaths. A sparse desert state can be badly damaged without producing the same death total as a dense coastal city state.

## Building damage scaling bands

| Band | Direction |
| --- | --- |
| Local hard damage | Several meaningful building levels damaged or destroyed, plus repair delay. |
| Severe local damage | Multiple building categories hit, infrastructure and supply made visibly worse. |
| Regional system damage | Anchor state hit hard, neighboring states receive family-specific falloff. |
| Catastrophic damage | Industry, infrastructure, and supply are damaged enough to change fronts and production. |
| Abnormal damage | Regions can be devastated, with several systems damaged at once and lingering recovery work. |

The player should feel a baseline serious hit in production, supply, or local manpower. Evolution III should be able to devastate regions when family and target match.

## Aftermath ledger

Every serious disaster should create an aftermath card. A card is a player-readable record in the aftermath category or scripted GUI.

A card should show:

- disaster family
- affected state or states
- severity band
- known deaths or death direction if the exact value is hidden
- damaged systems such as transport, industry, ports, housing, crops, supply, or medical access
- active state modifiers
- open recovery actions
- warning result if it matters
- chain risk such as aftershock, disease, famine, fire, refugee, or tsunami
- cleanup progress
- failure date if a timed mission is active

The card should close when recovery is complete, the target is no longer valid, or the disaster is superseded by a larger unresolved regional aftermath.

## Recovery category families

Recovery should use family-specific objectives. Do not make every aftermath the same button.

| Recovery family | What the player does |
| --- | --- |
| Search and rescue | Spend manpower, support equipment, fuel, and command attention to reduce delayed deaths. |
| Transport clearing | Repair rails, infrastructure, ports, supply hubs, and key roads. |
| Shelter and rationing | Use trucks, trains, convoys, support equipment, and manpower to reduce exposure and famine. |
| Medical corridor | Spend support equipment and manpower, reduce disease chain risk, especially after floods and heat. |
| Fire containment | Spend fuel, trucks, manpower, and stability risk to stop wildfire spread. |
| Coastal evacuation | Use convoys, trains, fuel, and navy coordination before storm surge or tsunami follow-up. |
| Ash cleanup | Ground aircraft temporarily, clear airfields, protect crops, and reduce respiratory deaths. |
| Winter relief | Move fuel, equipment, and supplies into cold-hit states before exposure rises. |
| Drought relief | Manage water, livestock, food, rail shipments, and crop failure risk. |
| Reconstruction | Expensive longer task that restores buildings and closes the aftermath card. |

AI should not ignore recovery. Strong AI should protect dense states, capitals, ports, rail hubs, and major industry first. Weak AI should still attempt at least the cheapest useful relief actions.

## Chain model

A chain is not a second event log row. It is a delayed continuation inside the same Event 013 season or aftermath.

| Chain | Trigger direction | Prevention direction |
| --- | --- | --- |
| Aftershock | Earthquake, rupture wave, volcanic quake | Reinforce search zones, inspect rail and buildings, keep rescue teams in place. |
| Tsunami follow-up | Offshore earthquake, volcanic collapse, meteor ocean impact | Coastal evacuation and port closure before the wave. |
| Famine | Drought, flood, ashfall, winter blockade, refugee pressure | Food rail, convoy corridor, rationing, crop protection, foreign relief. |
| Disease | Flood, heat, refugee camps, poor infrastructure, unresolved bodies | Medical corridor, clean water, shelter, support equipment. |
| Wildfire spread | Drought, heat, wind, thunderstorm | Firebreaks, fuel and truck use, local evacuation. |
| Refugee pressure | Dense disaster, war-torn state, destroyed transport | Shelter, train movement, border coordination, camp hardening. |
| Supply collapse | Any severe transport hit | Rail repair, supply hub repair, temporary convoy route. |
| Political shock | High deaths or failed recovery | Stability and war support pressure, local unrest, leader criticism. |

Chains should be visible in the aftermath card. A player should be able to see that an unresolved flood can turn into disease pressure, or an offshore quake can create a delayed tsunami risk.

## News throttle policy

Early Natural Disasters should feel newsworthy because the world has not adapted to repeated incidents. Later evolutions should avoid noise.

News policy should consider:

- first time a family appears in a campaign
- unusually high deaths or damage
- capital or major port hit
- multiple neighboring states hit
- strange or abnormal behavior
- disaster chain crossing borders
- global or continental scope
- super-event eligibility
- active player country affected

Minor repeated hits in Evolution II should usually not create global news. They should still create local reports and aftermath cards.

## External caller examples

| External caller | Call pattern |
| --- | --- |
| Nature god punishes enemy | Specific family group, enemy country target, severity from divine pressure, news meaningful only, full aftermath. |
| African god targets colonizer | Chosen country or region, drought, flood, plague of locust bridge only if accepted, recovery hard in occupied states, local resistance effect. |
| Mysterious Man offers disaster | Random valid family, chosen player country, caller report enabled, warning odds reduced. |
| Disaster Barrage scenario | Scenario type sets family pool, intensity sets sequence size and abnormal access, direct manual launch actor. |
| Sandstorm placeholder bridge | Event 099 calls dust or sandstorm family and then stops, no separate sandstorm logic. |
| Earth Earthquake placeholder | Event 046 does not call anything automatically unless a manual debug path is accepted. Evolution III rupture wave owns the concept. |
