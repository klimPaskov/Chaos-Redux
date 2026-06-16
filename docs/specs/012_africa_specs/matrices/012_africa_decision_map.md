# Event 012 Africa — Decision and Mission Map

This decision map condenses the larger decision/UI spec into implementation-ready families. It should be used with `012_africa_decisions_missions_ui.md`.

## Value keys

| Value | Player-facing meaning | Main sources of change | Unlocks or blocks |
| --- | --- | --- | --- |
| Legitimacy | Whether the proclamation is accepted as African rather than merely ambitious | conferences, liberation success, diaspora programs, fair integration | federation route, voluntary accession, stable coring |
| Authority | Administrative and military ability to enforce continental policy | rail missions, command focuses, police/administration decisions | integration, war preparation, emergency commands |
| League Cohesion | Trust among Charter League members | aid, fair voting, victories, autonomy guarantees | joint wars, shared reserves, member integration |
| Liberation Momentum | Pace of anti-colonial wars and uprisings | victories, member rescue, volunteers, colonial defeats | anti-colonial war goals, scramble escalation |
| Regional Trust | Regional willingness to join the project | local missions, cultural autonomy, protection | regional authority integration and subject loyalty |
| Colonial Alarm | Outside panic and intervention pressure | cores, wars, ultimatums, unification progress | sanctions, scramble crisis, foreign intervention |
| Paper-Core Burden | Gap between claimed Africa and actually integrated Africa | gaining paper cores/claims without regional work | resistance, member refusal, overextension |
| Covenant Pressure | High-chaos mythic/nature pressure | Green Covenant decisions, disasters, supernatural pacts | high-chaos routes, nonhuman actors, natural disaster threats |

## Decision family overview

| Family | Category | Phase | Main targets | Costs/requirements | Success | Failure or risk | AI equivalent |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Convene the Proclamation Congress | Continental Congress | Opening | Unifier capital/selected symbolic city | legitimacy need, stability, political preparation | creates Charter League framework | low turnout increases Colonial Alarm | AI uses early unless at war collapse |
| Seat Regional Delegates | Continental Congress | Early-mid | regional authority slots | convoys/trains/PP/equipment depending region | raises Regional Trust and Cohesion | visible regional grievance if neglected | AI prioritises nearby regions |
| Draft the Charter Articles | Continental Congress | Early | whole League | legitimacy, time, no immediate collapse | unlocks voluntary accession | factions may object | AI chooses according route |
| Emergency War Council | Continental Congress | War/emergency | League members | command power, army XP, equipment, active threat | shared reserves and coordination | lower legitimacy if overused | military AI uses more often |
| Recognise a Provisional African Authority | Charter League Diplomacy | Early-mid | African country at war/threatened | relations, convoys, equipment, access | target can join League | patronage risk and Colonial Alarm | AI targets threatened countries |
| Send Officer Cadres | Charter League Diplomacy | Mid | League member or liberation target | army XP, support equipment, command power | improves target army and influence | dependence pressure | AI uses on weak members |
| Open a Relief/Aid Corridor | Charter League Diplomacy | Early-mid | land/sea corridor | convoys/trains/fuel/port or rail access | raises trust and survival | convoy loss, supply strain | AI checks route availability |
| Demand Anti-Puppet Clauses | Charter League Diplomacy | Mid | member/subject/future protectorate | legitimacy and diplomatic leverage | reduces outside influence | strong countries resist | AI uses before integration |
| Prepare Liberation Front | Liberation War Office | Early-mid | coloniser-held region | equipment, manpower, local support | unlocks war prep mission | discovery raises alarm | AI uses where colonial hold exists |
| Raise Border Liberation Columns | Liberation War Office | War | border states | infantry equipment, manpower, supplied divisions | spawns regional units | free-unit loop risk; use caps | AI uses if equipment surplus |
| Secure the Rail Belt | Liberation War Office | Mission | rail hubs | place supplied divisions/control states | improves authority and supply | failure raises authority loss | AI uses for adjacent fronts |
| Protect an African Ally | Liberation War Office | War mission | ally/member capital | divisions in target or aid shipments | keeps ally in League | failure lowers cohesion | AI prioritises capitals |
| Begin Regional Integration Talks | Regional Integration | Mid | one region/member | Regional Trust, Legitimacy, no active betrayal | opens integration meter | member suspicion | AI uses only after aid/victory |
| Establish a Charter Administration | Regional Integration | Mid-late | controlled region | equipment, trains, admin burden, low resistance | claims become administrative control | Paper-Core Burden if rushed | AI uses region by region |
| Hold the Integration Referendum | Regional Integration | Mid-late | member/protectorate | high trust, stability, mission success | voluntary annex/coring progress | refusal, exit, war risk | AI avoids if target strong/unhappy |
| Convert Paper Cores to Living Cores | Regional Integration | Late | integrated states | time, local support, rail/admin requirements | staged cores | resistance if instant/cheap | AI uses only with stable state |
| Invite Return Cadres | Diaspora Return Offices | Early-mid | unifier/ports/industry centres | convoys, civ burden, stability | advisors, industry, legitimacy | backlash, espionage attention | AI uses federal/socialist routes |
| Build the Return Settlements | Diaspora Return Offices | Mid | chosen states | civilian factories, rail/port access | local building/skills | local tension | AI limited by economy |
| Form Diaspora Officer Schools | Diaspora Return Offices | Mid | army branch | army XP, support equipment | commanders/templates | dependency or faction tension | AI uses with low officer quality |
| Read the River and Sky Reports | Green Covenant | High chaos | affected regions | Covenant Pressure, route flag | warnings/disaster prediction | public fear and instability | AI high-chaos only |
| Bargain with the Forest Courts | Green Covenant | High chaos | Congo/forest regions | high pressure, forest route, legitimacy | nonhuman pact/forest defence | nonhuman actor spawn if mishandled | AI only route-locked |
| Call the Tides | Green Covenant | High chaos | ports/coastal regions | convoys, sea-spirit pact, high chaos | port defence or storm pressure | trade/convoy losses | AI coastal route only |
| Threaten the Scramble | Post-Unification | Late | colonial powers | Africa mostly unified, high momentum | ultimata/withdrawal | starts Scramble crisis | AI only with strength |
| Sponsor Another Continent | Post-Unification | Evolution III+ | continent unifier candidates | convoys, equipment, legitimacy, world state | creates/sponsors unifier | proxy blowback | AI late and strong only |
| Proclaim a Cross-Continental Union | Post-Unification | Evolution IV+ | completed continent unifier | both continents secured, focus path done | dynamic union name/annex/federation | rivalry or collapse if forced | AI only when safe/eligible |
| Pursue The World Is One | World-end | Terminal | all continent unifiers | extreme chaos, all paths complete | world-end scenario | cannot trigger if prerequisites absent | AI only if terminal conditions true |

## Mission families

| Mission | Owner | Region | Duration band | Objective | Success | Failure |
| --- | --- | --- | --- | --- | --- | --- |
| Guard the Capital of a Member | Unifier or member | target capital | 90–150 days | keep target capital controlled/supplied | cohesion, member survival, integration trust | member panic, exit chance, colonial momentum |
| Secure the Coastal Corridor | Unifier | selected coastal state group | 120–180 days | hold port and convoy route | aid decisions cheaper, port trust | convoy losses, alarm |
| Hold the Rail Spine | Unifier | selected rail belt | 120–180 days | control named rail hubs | authority, supply, integration | authority loss, supply penalty |
| Keep the Congress Together | Unifier | all League | 120 days | keep cohesion above threshold | unlock next charter step | route crisis, member refusals |
| Win the Liberation Campaign | Unifier + member | coloniser-held region | 180–365 days | take regional capital/ports | liberation momentum, new authority | truce pressure, loss of legitimacy |
| Integrate Without Rebellion | Unifier | one regional authority | 180 days | trust/stability/resistance thresholds | staged cores | authority split, rebel member or exit |
| Calm the Covenant | Green route | high-chaos region | 120–240 days | reduce Covenant Pressure or complete bargain | safe pact | nonhuman actor/ disaster event |
| Defeat the Allied Continuity Government | RSA branch | South Africa | civil-war duration | continental side wins | Allied peace, special unifier package | event ends or RSA remains ordinary |

## Decision category clutter controls

- Only one selected integration target should expose detailed integration decisions at a time.
- Liberation targets should be grouped by region; only active/prioritised targets are visible.
- Green Covenant decisions should be hidden unless the route, evolution, or high-chaos event reveals them.
- Diaspora decisions should appear in tiers: invitation, settlement, officer schools, post-unification return congress.
- Post-unification continent sponsor decisions should hide until Africa is unified and Evolution III is unlocked.
- World-end decisions should hide until all continent unifiers exist and have completed their own post-unification paths.

## Exploit prevention notes

- Unit decisions require equipment/manpower, regional caps, cooldowns, and mission context.
- Paper cores should not become full cores without integration missions.
- Integration decisions should have target flags to prevent repeated annex/coring loops.
- War goals should be target-limited and expire or be replaced after settlement.
- Member aid should not farm influence infinitely; influence gain should taper and risk dependency/backlash.
- Sponsoring other continent unifiers should be expensive and limited by convoys, equipment, legitimacy, and global chaos state.

## Restoration Dossiers decision family

| Decision family | Unlock | Player action | Main values changed | Required non-PP costs/objectives | Cleanup / exploit control |
| --- | --- | --- | --- | --- | --- |
| Open Regional Archive | Archive opener focus. | Select a macro-region and reveal eligible dossiers. | +archive mandate, reveal regional pool. | Controlled/protected region, civilian factory burden, trains/convoys where relevant. | Region selector hides irrelevant targets; cap active pools. |
| Survey Old Seat | Regional pool visible. | Investigate one dossier and decide whether to charter it. | +old-seat legitimacy or forgery risk. | Divisions/escort equipment, access to state/ally, support equipment. | One survey per dossier; failed survey creates cooldown. |
| Charter Local Office | Successful survey. | Create office/observer/subject path. | +local sovereignty, +restoration debt, +regional trust. | Local support, construction, state/port/rail control. | Dossier flag prevents duplicate office. |
| Raise Local Guard | Chartered office. | Raise route-specific guards. | +military readiness, +restoration debt if overused. | Manpower, rifles, support equipment, army XP, local trust. | Escalating costs and one-time templates. |
| Protect Monument / Regalia | Dossier has site/symbol. | Guard/repair old seat. | +old-seat legitimacy, -colonial alarm if public. | Unit presence in named states, construction capacity, trains. | Mission success/failure unique per site. |
| Negotiate Settlement | Mature dossier. | Choose autonomy/protectorate/integration/direct rule. | Local sovereignty, League cohesion, paper-core burden. | Stability, war support, local trust, time, mission objectives. | Removes obsolete decisions after settlement. |
| Manage Forgery Crisis | Counterfeit route or exposure. | Admit, suppress, double down, or redirect scandal. | Legitimacy, mythic pressure, restoration debt. | Intelligence exposure, stability, court trust. | Exposure flag gates follow-up events; no infinite concealment. |
| Bestiary Clause | Evolution III+ and focus unlock. | Grant/deny nonhuman observer seats. | Mythic pressure, nonhuman sovereignty, bestiary alarm. | Habitat/river/forest control, local trust, cooldown. | Nonhuman packages limited by separate cap. |
| Supernatural Sanction | Evolution IV and Green Covenant route. | Ask courts/river/masks/nature for intervention. | Covenant pressure, mythic pressure, colonial alarm. | Stability, disaster risk, autonomy concessions, cooldown. | Long cooldown, high failure consequence, AI restrictions. |
