# Event 013 — Decision and Mission Map

## Decision category concept

Working category label: **Disaster Response Office** — implementation can finalise localisation. The category appears for a country only when it has active disaster warnings, active aftermath, regional relief obligations, or the manual scenario is running. It should not be a permanent wall of dormant buttons.

The category header should use scripted localisation to show:

- current active disaster count;
- worst active severity;
- most urgent affected area;
- available relief capacity;
- warning status, if any;
- active regional chain, if any.

The category should be curated by phase:

1. **Warning phase:** preparation decisions only for current warned areas.
2. **Impact phase:** immediate relief and evacuation.
3. **Recovery phase:** infrastructure, population, industry, supply, and port recovery.
4. **Regional chain phase:** cross-border aid, refugee handling, famine prevention, tsunami follow-up, or ash cleanup.
5. **Scenario phase:** compressed response options for manual disaster barrage.

## Cost palette

Disaster response should use varied costs that tell a story. Avoid political power as the default.

| Resource or requirement | Use cases |
| --- | --- |
| Support equipment | engineers, medical tents, emergency shelters, ash cleanup |
| Trucks | evacuation, food transport, firefighting, road repair |
| Trains | relief trains, moving grain, evacuating workers, restoring rail corridors |
| Convoys | island/coastal relief, port recovery, famine imports |
| Fuel | evacuation, firefighting, generator support, transport |
| Infantry equipment | guards for depots, emergency police, flood barrier labour security |
| Manpower | rescue workers, engineers, labour battalions, medical staff |
| Civilian factory burden | rebuilding, public works, flood barriers, dam inspection |
| Military factory disruption | emergency conversion of factories to relief gear |
| Stability | forced evacuation, rationing, public panic, harsh requisitioning |
| War support | disaster fatigue, front deprioritisation, visible state weakness |
| Command power | military engineers and emergency logistics under army control |
| Army XP | engineering doctrine, military bridge teams, disaster logistics |
| Supply state | target must be connected or the mission cannot progress |
| Unit presence | hold/guard rail hubs, dams, ports, or evacuation routes |

## Warning decisions

| Decision | Visible meaning | Requirements and costs | Result direction | AI use |
| --- | --- | --- | --- | --- |
| Pre-Position Relief Trains | Move engineers, food, and medical supplies toward the warned area. | trains, support equipment, fuel, state supply access | reduces population loss and shortens recovery if disaster hits | high if target state has factories, capital, or supply hub |
| Evacuate Industrial Districts | Temporarily move workers and machinery away from danger. | trucks/trains, stability or production disruption | reduces population/factory damage, temporary output penalty | high for rich factory states; low if at war and low trucks |
| Reinforce Flood Barriers | Sandbags, pumps, bridge inspections, dam watches. | support equipment, manpower, civilian factory burden | reduces flood/dam/storm-surge severity | high if flood warning and state has port/rail/factories |
| Close Vulnerable Ports | Stop shipping and prepare port facilities. | convoy/fuel opportunity cost, temporary port/naval disruption | reduces storm/tsunami port damage; hurts short-term logistics | cautious; avoids if country depends on port supply |
| Move Air Wings Inland | Remove aircraft from an airbase in the danger zone. | requires airbase/air wings; possible air mission disruption | reduces airbase and aircraft losses | only for high airbase value states |
| Grain and Water Rationing | Prepare for drought or ash-crop failure. | stability cost, trains/convoys if importing | reduces famine chain chance | high if drought warning and low food/security variables |
| Inspect Dams and Tunnels | Engineers check high-risk infrastructure. | support equipment, army XP or civilian factories | reduces dam failure, landslide, rail collapse risk | high for mountain/river/supply hub states |
| Observatory Alert | Prepare for meteor or volcanic abnormal warnings. | civilian factories/research-like admin cost; may require high chaos | reduces meteor/eruption casualties, unlocks evacuation choices | high for player/majors; cautious for minors |

## Impact response decisions

| Decision | Trigger | Cost | Success | Failure or downside |
| --- | --- | --- | --- | --- |
| Dispatch Emergency Engineers | local building or infrastructure damage | support equipment, manpower, civilian factory burden | reduces state modifier duration and repair damage | if under-supplied, only partial relief |
| Send Medical Columns | civilian casualty/displacement pressure | support equipment, trucks, manpower | reduces additional population loss and stability pressure | may consume scarce manpower/equipment during war |
| Open Relief Convoys | coastal/island/overseas disaster | convoys, fuel, naval access, port control | reduces famine/refugee pressure and port recovery time | convoy exposure or disruption if at war |
| Emergency Railway Repair | rail/supply disruption | trains, support equipment, army XP or civilian factory burden | restores supply and shortens rail penalties | failure extends supply penalties |
| Temporary Shelter Program | displacement/refugee aftermath | civilian factories, support equipment, stability | reduces refugee pressure | too many shelters increase consumer goods burden temporarily |
| Firebreak Mobilisation | wildfire/firestorm | trucks, manpower, fuel, infantry equipment for order | reduces spread and factory damage | harsh mobilisation can reduce stability |
| Ash Clearance Crews | volcanic/meteor ash | support equipment, trucks, airbase/rail access | reduces airbase/supply penalty | if ignored, air and crop penalties linger |
| Shoreline Rescue | tsunami/storm surge | convoys, trucks, support equipment, port access | reduces population loss and port closure | unavailable if enemy controls sea/port route |
| Controlled Factory Shutdown | industrial firestorm/earthquake | temporary production loss | reduces factory destruction and population deaths | slows military production during emergency |

## Timed missions

Timed missions should be objective-based when possible. A mission should auto-complete if the country satisfies the visible objective.

| Mission | Duration band | Objective | Success | Failure |
| --- | --- | --- | --- | --- |
| Restore the Main Line | 90–150 days | Keep the affected state controlled and connected to supply; repair/maintain infrastructure/rail threshold. | removes or reduces transport aftermath | state keeps supply penalty and may trigger refugee pressure |
| Hold the Dam Watch | 90–120 days | Keep divisions or security presence in dam/river states and pay support equipment. | blocks dam-failure follow-up | flood chain fires with secondary damage |
| Keep the Port Open | 90–150 days | Control the port state, maintain convoy/fuel availability, avoid enemy blockade if possible. | removes storm/tsunami port closure faster | longer port/naval base penalty |
| Feed the Dry Belt | 120–180 days | Provide trains/convoys and avoid losing supply access in drought states. | prevents famine chain | famine/refugee pressure event fires |
| Clear the Ash Fields | 120–180 days | Maintain support equipment/trucks and recover airbase/infrastructure. | removes ashfall penalties and crop pressure | crop failure or air disruption persists |
| Rehouse the Displaced | 150–240 days | Spend factories/support equipment and keep stability above a threshold. | reduces refugee pressure and population loss | stability hit, migration pressure, longer recovery |
| Guard the Mountain Passes | 90–150 days | Place supplied divisions in key mountain/rail states. | prevents pass collapse and supply penalty | landslide/avalanche follow-up damages rail/supply |
| Survey the Crater Belt | 120–180 days | Engineers and military units inspect meteor states. | reduces meteor scars and panic | high-chaos panic or firestorm follow-up |

## Regional and cross-border decisions

Regional disasters can affect multiple countries. Affected countries should receive local response decisions, while major powers and neighbours can receive selective aid decisions when connected by faction, border, subject relationship, guarantee, or good relations.

| Decision | Owner | Meaning | Costs | Consequence |
| --- | --- | --- | --- | --- |
| Offer Relief Mission | neighbour, faction leader, major power | send aid to affected country | convoys/trains/support equipment/fuel | improves relations, reduces target recovery pressure |
| Seal the Border Camps | neighbour | refuse refugees and militarise crossing | infantry equipment, stability/war support tradeoff | lowers refugee intake, worsens relations and target pressure |
| Accept Disaster Refugees | neighbour/ally | receive displaced civilians | stability and consumer goods burden | target pressure lowers; receiver gets temporary burden and later workforce benefit |
| Joint River Commission | countries sharing basin | coordinate flood control | political/diplomatic cost, factories, support equipment | reduces future flood severity in shared basin |
| International Ash Warning | majors/air powers | share observation data | air XP/intel/admin cost | reduces volcanic/meteor warning failure chance |
| Military Bridge Teams | faction leader or strong neighbour | army engineers restore corridor | army XP, support equipment, trains | target state supply penalty shortens |

## Recovery outcome levels

Recovery should allow partial outcomes.

| Outcome | Meaning | Follow-up |
| --- | --- | --- |
| Full success | damage controlled, aftermath ends early | small positive recovery memory or reduced future vulnerability |
| Partial success | core damage repaired but population/refugee pressure remains | lighter modifier or one smaller follow-up |
| Harsh success | order restored through coercive means | reduced damage but stability/war-support/local resistance pressure |
| Failure | recovery missed or resources absent | longer modifier, refugee/famine/panic follow-up, possible extra chaos |
| Exploited disaster | country uses disaster to seize power or propaganda | political gain and humanitarian penalty; optional future branch only if implemented deliberately |

## Decision category clutter control

Only show decisions for:

- active warning target;
- active aftermath states owned/controlled by the country;
- active regional chain affecting the country;
- aid-eligible neighbours/allies;
- manual scenario emergency response.

Use a selected-target pattern if there are many affected states. The player should choose an affected area to inspect rather than seeing twenty duplicate “repair” decisions at once.

## Localisation requirements

Each decision needs:

- title;
- short description that names the affected area;
- icon-first cost text;
- blocked text for missing trains, convoys, support equipment, fuel, supply access, or unit presence;
- result tooltip that describes visible outcome without revealing hidden future chains;
- AI-use note for implementation review.

## Scripted GUI recommendation

A custom scripted GUI is useful but not mandatory for the first implementation pass. The spec recommends a compact **Disaster Ledger** window if implementation time allows. It should be opened from the decision category and show:

- a list of active affected states/regions;
- disaster family icon;
- severity band;
- warning/impact/recovery/chain phase;
- remaining recovery time;
- top three available response buttons;
- a warning pulse if a follow-up chain is near.

Animated UI is useful for warning pulses, selected state cards, and high-chaos meteor/volcano state. Static fallback sprites are required for every animated element.
