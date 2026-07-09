# 012 Africa spec part 28, diaspora and settlement closure

This file expands the Black Star Return and wider diaspora content into a complete planning layer. It keeps final player-facing text blocked for implementation, but it provides exact gameplay loops, mission families, failure states, and achievement hooks.

## Diaspora route identity

The diaspora route should not be a simple manpower button. It should be a port, convoy, reception, industry, culture, and diplomacy system. The player builds safe return corridors, receives skilled cadres, manages local reception, and turns the route into a continental legitimacy tool.

The route must include Afro-American return content because the event brief asks for it. It should also support Caribbean, Atlantic, European, Indian Ocean, and internal African diaspora directions where they fit the campaign.

## Core values

| Value | Meaning | Rises from | Falls from | Unlocks |
| --- | --- | --- | --- | --- |
| `returnee_capacity` | How many people and cadres can be absorbed safely | housing, ports, jobs, health systems, local support | shortages, unrest, blockade, failed settlement | settlement missions and industry projects |
| `lane_security` | Safety of sea and land routes | convoy escorts, port control, foreign access, League patrols | blockades, submarine pressure, hostile great powers | larger return waves and achievement hooks |
| `reception_confidence` | Trust between local communities and returnees | cultural diplomacy, land mediation, local jobs, route-specific fairness | coercive settlement, shortages, rival propaganda | durable settlement and lower resistance |
| `industrial_cadre_pool` | Skilled workers, engineers, teachers, doctors, dock workers, and organizers | successful lanes, foreign networks, education missions | failed convoys, disease, unemployment, foreign surveillance | factory, port, railway, and research projects |
| `diaspora_diplomacy` | International pressure and recognition from communities abroad | media missions, cultural delegations, anti-colonial lobbying | repression, route hypocrisy, coercion, failed promises | outside-power reaction softening or escalation |
| `settlement_backlash` | Local or foreign opposition to the return route | bad housing, land seizure, unemployment, surveillance, disease panic | fair mediation, jobs, local institutions, health missions | failure events, lane closures, achievement disqualifiers |

## Shipping lane families

| Lane | Origin direction | African gateway | Required conditions | Reward direction | Failure state |
| --- | --- | --- | --- | --- | --- |
| Afro-American Atlantic lane | United States communities and Black press networks | Liberia, Gold Coast, Senegal, Nigeria, or chosen West African port | safe Atlantic convoy, gateway port, reception capacity, no severe blockade | industry cadres, diplomacy, legitimacy, special settlement missions | foreign surveillance, dock strike, settlement backlash |
| Caribbean Atlantic lane | Caribbean islands and port cities | West African coast, Liberia, Ghana, Sierra Leone, Senegal | convoys, port access, diaspora diplomacy | dock workers, merchant cadres, cultural influence | convoy loss, foreign interference |
| Black Star Line memory lane | Garveyite symbolic route and shipping fantasy | Liberia and West African coast | researched route, Black Star focus, port project | strong legitimacy and achievement tracking | overpromise crisis and shipping debt |
| Brazilian and South Atlantic lane | Brazil and South Atlantic communities | Angola, Congo coast, Ghana, or Benin coast | foreign access, long convoy route, reception confidence | cultural diplomacy, industrial workers, port projects | customs seizure, foreign diplomatic pressure |
| European wartime diaspora lane | Black workers, students, sailors, and anti-colonial networks in Europe | North African or West African ports | war state or European access, intelligence risk | advisors, propaganda, research bonuses | surveillance and arrest abroad |
| Indian Ocean return lane | East African, island, and Indian Ocean networks | Zanzibar, Kilwa, Mombasa, Madagascar, Comoros | port control, Indian Ocean convoy security | maritime cadres, dockyard and port bonuses | blockade, port rival conflict |
| Internal African return lane | displaced Africans and colonial labor migrants inside Africa | nearest secure League region | rail safety, local support, housing | manpower, legitimacy, lower resistance if fair | overcrowding, local backlash |
| Scholar and technical cadre lane | students, doctors, teachers, engineers | capital, port, university, or industrial region | stable reception, no severe route repression | research, construction, medical, and education projects | brain drain accusation and unemployment |

## Settlement mission families

| Mission family | Player action | Cost palette | Success | Failure |
| --- | --- | --- | --- | --- |
| Build reception districts | Create housing, clinics, schools, and local offices | civilian factories, support equipment, stability, time | raises capacity and confidence | raises backlash and stalls lane |
| Secure returnee work | Match cadres to factories, ports, rail, and farms | factories, trains, convoys, local support | industrial cadre pool becomes visible benefits | unemployment backlash |
| Mediate land access | Prevent land seizure and local resentment | political attention, local support, time, route concessions | lowers resistance and backlash | local conflict and member confidence loss |
| Protect convoy routes | Escort ships and keep ports open | convoys, fuel, naval access, port control | raises lane security | convoy loss and foreign pressure |
| Cultural diplomacy tour | Use returnee networks for recognition | political effort, stability, local support | diaspora diplomacy rises | rival propaganda |
| Health and quarantine support | Keep movement safe without turning it into fear propaganda | medical projects, support equipment, time | lowers disease and panic risk | reception confidence falls |
| Port apprenticeship program | Use returnee dock and merchant skills | dockyard, convoys, industrial cadre pool | dockyard or convoy benefits | port strike or smuggling risk |
| Teacher and print network | Build cultural and education link | industrial cadre pool, paper or civilian project | legitimacy and ideology route benefits | propaganda backlash |
| Veteran and officer cadre | Integrate returnees with military experience | army XP, infantry equipment, command capacity | special training decisions | officer resentment |
| Local member exchange | Send returnee cadres to League members | member confidence, convoys, local support | boosts League cohesion | member backlash if capacity is low |

## Settlement outcomes

| Outcome | Conditions | Effect direction |
| --- | --- | --- |
| Durable settlement | high reception confidence, low backlash, enough capacity | staged manpower and industrial rewards, lower resistance, achievement progress |
| Cadre network without mass settlement | high industrial pool, low capacity | advisors, research, factories, and ports without large manpower |
| Cultural diplomacy success | high diaspora diplomacy and stable League | outside power pressure reduced or exposed |
| Backlash containment | backlash rises but missions succeed | route remains available, but rewards slow down |
| Settlement failure | high backlash, low capacity, convoy losses | lane closes temporarily, confidence and stability fall |
| Exploit prevention | repeated settlement without jobs or housing | rising backlash and no further manpower |
| High-chaos corruption | Deep Green or disease pressure contaminates route | route locks mass movement until safety projects succeed |

## Focus integration

Black Star Return should connect to these focus groups.

| Focus group | Unlocks |
| --- | --- |
| `black_star_line_memory` | lane setup and Garveyite source research direction |
| `returnee_port_authorities` | port and convoy missions |
| `settlement_without_seizure` | land mediation and reception confidence |
| `diaspora_industrial_cadres` | industrial cadre pool and factory projects |
| `atlantic_radio_networks` | diplomacy and cultural missions |
| `returnee_defense_volunteers` | veteran and officer cadre decisions |
| `black_star_world_links` | diaspora diplomacy in outside-power reaction tree |
| `returnee_commonwealth` | post-unification route and achievement hooks |

## AI behavior

AI should not use the diaspora route if it lacks ports, convoys, stability, or reception capacity. Stable federal and Black Star route AI can use it. Command route AI should use it mainly for veteran cadres and port labor, with higher backlash. Revolutionary route AI can use media and anti-colonial networks, but it should risk foreign surveillance. Deep Green AI should not use mass return lanes unless disaster and disease pressure are under strict control.

## Achievement hooks

| Working id | Route condition |
| --- | --- |
| `012_africa_black_star_safe_harbor` | complete three return lanes without settlement failure |
| `012_africa_no_seized_land` | achieve major settlement with low backlash and no coercive land decisions |
| `012_africa_dockworkers_of_two_oceans` | operate Atlantic and Indian Ocean lanes together |
| `012_africa_returnee_arsenal` | use industrial cadres to complete major factory and railway projects |
| `012_africa_letters_home` | use cultural diplomacy to soften a Scramble reaction without war |
| `012_africa_line_did_not_break` | keep a lane open during major war or blockade pressure |

## Asset needs

The route needs its own visual family.

| Asset | Type | Size | Source mode | Motif |
| --- | --- | --- | --- | --- |
| Black Star route focus icons | focus | 94x86 | generated | star, ship, dock crane, newspaper, workshop |
| Returnee settlement idea icons | idea | 64x64 | generated | house, toolkit, school, port ledger without readable text |
| Shipping lane decision icons | decision | 32x32 | generated | convoy, anchor, dock, passport-like symbol without text |
| Diaspora super-event image if used | super-event | 457x328 | generated or sourced depending on route | port crowd, ship, flags, period documentary style |
| Garvey or UNIA source materials if used | historical reference only unless implementation needs real portrait | source research | source mode required | must be sourced, not generated |

## Localisation direction

Final localisation should describe ships, ports, jobs, families, workshops, churches, newspapers, labor halls, returnee committees, and local mediation. It should not present the route as free population transfer. It should not use achievement language in ordinary event or focus text. It should use researched references only after the localisation workflow verifies them.
