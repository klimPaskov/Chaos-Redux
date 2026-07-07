# Event 013 Natural Disasters, Part 10, recovery decision and mission map

This file deepens the aftermath decision and mission system. It is direction-only design. Working decision and mission keys are not final localisation.

The recovery system should feel like a country dealing with a specific physical disaster in named places. It should not feel like a political power store. Costs should use manpower, equipment, trucks, trains, convoys, fuel, XP, construction capacity, temporary output loss, stability strain, local support, and time pressure when those fit the action.

## Category lifecycle

| Phase | Opens when | Player problem | Typical cap | Closes when |
| --- | --- | --- | --- | --- |
| `early_rescue` | serious impact lands or warning converts to impact | Keep people alive, keep one route open, stop the worst chain. | 3 active rescue missions, adjusted down for weak states and up for major countries. | Rescue score reaches threshold or late rescue date passes. |
| `middle_stabilization` | first report delivered or rescue mission completes | Restore supply, water, shelter, port, rail, and public stability. | 2 active stabilization missions plus 1 chain prevention mission. | Stabilization score reaches threshold and no immediate chain is pending. |
| `late_reconstruction` | disruption remains after stabilization or building damage is high | Rebuild stronger, remove lingering modifiers, reduce future recurrence. | 2 active reconstruction projects, with more only for Disaster Barrage or regional Evolution II seasons. | All required modifiers are removed or converted to long-term resilience. |
| `foreign_relief` | affected country asks for or receives external help | Decide whether relief is accepted, routed, delayed, politicized, or refused. | 1 inbound relief mission and 1 outbound donor action per donor country by default. | Relief arrives, fails, is refused, or converts into debt or influence risk. |

Caps are design anchors. Implementation should centralize them as tuning values and adjust by country size, war state, number of active cards, chaos tier, and scenario intensity.

## Early rescue decision families

| Working key | Family fit | Cost palette | Success direction | Partial success direction | Failure direction | AI priority |
| --- | --- | --- | --- | --- | --- | --- |
| `013_rescue_search_teams` | earthquake, meteor, tornado, wildfire, lahar | manpower, trucks, support equipment, command direction | Lowers immediate death continuation and improves rescue score. | Reduces deaths but leaves shelter shortage. | Adds missing survivor pressure and worsens stability. | Highest in dense states and capitals. |
| `013_rescue_open_shelters` | heat, cold, blizzard, flood, storm surge, tsunami | support equipment, civilian capacity, stability strain | Reduces deaths and refugee pressure. | Shelters open but disease risk rises if water is not secured. | Death ticks continue and refugees move. | Highest when population density is high. |
| `013_rescue_clear_one_route` | earthquake, flood, blizzard, landslide, lahar, storm corridor | trains, trucks, fuel, manpower | Opens a route for supply and relief. | Route opens but factory or port repair is delayed. | Supply collapse risk increases. | Highest at war or island dependency. |
| `013_rescue_emergency_evacuation` | tsunami, wildfire, cyclone, meteor, volcano, storm corridor | trucks, fuel, manpower, stability strain | Reduces death driver and moves card toward stabilization. | Saves people but increases refugee pressure in adjacent states. | Death spike and panic modifier worsen. | Highest for coastal and fire path states. |
| `013_rescue_medical_triage` | flood disease risk, heat, cold, ash, meteor, fire | manpower, support equipment, trucks | Reduces ongoing deaths and disease chain chance. | Deaths drop but recovery remains slow. | Disease, shelter, or exposure chain becomes more likely. | High after flood, heat, ash, and dense impacts. |
| `013_rescue_port_lifeline` | cyclone, tsunami, storm surge, island flood, volcanic island | convoys, fuel, naval access, civilian capacity | Keeps a port route open or reopens a minimal route. | Relief arrives slowly with supply penalty. | Island or port supply collapse risk. | Very high for islands and naval powers. |

## Middle stabilization decision families

| Working key | Family fit | Cost palette | Success direction | Partial success direction | Failure direction | AI priority |
| --- | --- | --- | --- | --- | --- | --- |
| `013_stabilize_clean_water` | flood, storm surge, tsunami, heat, ash, lahar | trucks, support equipment, convoys or trains | Removes water contamination and lowers disease risk. | Disease risk drops but ration pressure remains. | Disease chain can fire. | High when risk badge includes disease. |
| `013_stabilize_restore_rail` | earthquake, flood, blizzard, landslide, storm corridor | trains, steel or support equipment direction, civilian capacity | Removes rail disruption and improves supply. | Rail works at reduced throughput. | Supply collapse or delayed recovery. | Highest when state feeds front or capital. |
| `013_stabilize_reopen_port` | cyclone, tsunami, surge, volcanic coast | convoys, fuel, civilian capacity, dockyard burden | Restores port throughput and relief access. | Port reopens with temporary throughput cap. | Port closure persists and relief can fail. | High for island or port-dependent countries. |
| `013_stabilize_secure_food` | drought, hail, flood, ash, wildfire | trains, convoys, civilian capacity, stability strain | Reduces famine and ration pressure. | Food arrives but foreign relief dependency can rise. | Famine or unrest chain can fire. | High when several agricultural or dense states are hit. |
| `013_stabilize_factory_inspection` | earthquake, wind, meteor, ash, fire | civilian capacity, support equipment, temporary factory output loss | Prevents secondary factory damage and improves reconstruction speed. | Some output saved, repair remains slower. | Industrial accident or longer output penalty. | High in high industry states after rescue. |
| `013_stabilize_chain_prevention` | all families with risk badges | family-specific cost package | Cancels or weakens one chain risk. | Chain fires at reduced strength. | Chain fires normally or stronger if overdue. | AI should pick the highest expected loss chain. |

## Late reconstruction decision families

| Working key | Family fit | Cost palette | Success direction | Partial success direction | Failure direction | AI priority |
| --- | --- | --- | --- | --- | --- | --- |
| `013_reconstruct_resilient_rails` | earthquake, flood, blizzard, landslide, rupture | civilian capacity, trains, support equipment | Removes lingering rail modifier and lowers future rail damage. | Modifier becomes weaker but remains. | Future same-family hit receives vulnerability bonus. | High for major supply corridors. |
| `013_reconstruct_seismic_retrofit` | earthquake, rupture, meteor blast-adjacent rebuild | civilian capacity, steel direction, stability strain | Lowers future seismic building damage. | Only priority districts protected. | Future aftershock and quake damage remains high. | High in capitals and dense urban states. |
| `013_reconstruct_coastal_barriers` | flood, storm surge, tsunami, cyclone | civilian capacity, convoys, manpower | Lowers future water and port damage. | Port protected but civilian districts remain exposed. | Repeat coastal disaster worsens. | High for island, port, and coastal capital states. |
| `013_reconstruct_firebreak_network` | wildfire, drought, heat, wind | manpower, infantry equipment, support equipment | Reduces future wildfire spread and smoke damage. | Reduces spread only in selected states. | Fire recurrence risk remains. | High in forest and dry industrial states. |
| `013_reconstruct_volcanic_exclusion_routes` | volcano, lahar, ash, massive eruption | trucks, civilian capacity, stability strain | Reduces lahar and vent deaths, improves evacuation. | Main route works, secondary valley remains exposed. | Lahar or ash recovery remains fragile. | High around active volcanic cards. |
| `013_reconstruct_water_security` | drought, heat, flood contamination | civilian capacity, trains, convoys | Lowers future drought and heat deaths, removes ration pressure. | Urban water secured, countryside pressure remains. | Drought recurrence can escalate. | High for repeated heat or drought regions. |
| `013_reconstruct_crater_or_exclusion_cordon` | meteor impact, skyfire, abnormal rupture scar | manpower, support equipment, civilian capacity | Removes crater or exclusion modifier and closes card. | Some areas remain closed with lower output. | Persistent exclusion and panic remain. | High for capital or industry states. |

## Chain prevention missions

Chain prevention should be presented as timed objectives, not extra flavor popups. The player should understand what chain can happen and which visible action reduces it.

| Chain mission | Opens from | Objective direction | Duration band | Success | Partial success | Failure |
| --- | --- | --- | --- | --- | --- | --- |
| `013_chain_prevent_tsunami` | offshore quake, ocean meteor, volcanic collapse | Evacuate coast and close quays before arrival. | hours to 4 days by origin distance | Tsunami deaths and port damage reduced. | Deaths reduced, port damage remains high. | Tsunami hits at full or increased panic strength. |
| `013_chain_prevent_disease` | flood, tsunami, surge, lahar, shelter crowding | Secure clean water and medical route. | 30 to 90 days | Disease chain blocked. | Disease appears as smaller modifier. | Disease death tick and stability strain. |
| `013_chain_prevent_famine` | drought, ash, hail, flood, coastal closure | Bring food corridors online. | 60 to 180 days | Famine pressure lowered or blocked. | Famine pressure delayed with foreign aid risk. | Famine event chain and deaths. |
| `013_chain_prevent_wildfire_spread` | heat, drought, wind, thunderstorm, meteor | Build firebreaks and patrol lines. | 20 to 70 days | Spread blocked. | Spread limited to one neighbor. | Fire spreads to adjacent state. |
| `013_chain_prevent_supply_collapse` | blizzard, flood, landslide, rupture, port damage | Hold at least one rail, port, or road route. | 30 to 120 days | Supply modifier removed. | Reduced supply remains. | Local supply collapse and military penalties. |
| `013_chain_prevent_lahar` | volcanic eruption, ashfall, massive eruption | Clear channels and evacuate valleys. | 10 to 60 days | Lahar blocked or weakened. | Lahar damages infrastructure but deaths reduced. | Full lahar impact. |
| `013_chain_prevent_aftershock` | earthquake, rupture | Inspect priority buildings and bridges. | 15 to 45 days | Aftershock damage reduced. | Aftershock still damages rail or factories. | Aftershock hits at dangerous strength. |

## Foreign relief variants

Foreign relief should add useful help without becoming free recovery. It should create route access, delay, influence, and dependency choices.

| Variant | Who can offer | Aid shape | Cost to donor | Risk to affected country | AI use |
| --- | --- | --- | --- | --- | --- |
| `relief_neighbor_convoy` | neighbors, faction members, nearby majors | trucks, support equipment, convoys, food direction | equipment, convoys, temporary consumer goods or stability strain | dependency pressure or political influence | Common for allies and friendly neighbors. |
| `relief_port_lifeline` | naval powers, faction leaders, trade partners | port supply, medical aid, evacuation ships | convoys, fuel, naval access | port route can be delayed by blockade or damaged port | High for island disasters and tsunami. |
| `relief_engineer_mission` | industrial majors or faction leaders | rail, bridge, port, factory repair help | civilian capacity, support equipment | foreign influence and possible intelligence exposure | Used when state has high infrastructure value. |
| `relief_medical_mission` | majors, neighbors, humanitarian-aligned countries by ideology direction | disease, heat, cold, ash medical relief | support equipment and manpower direction | lower disease risk but possible legitimacy comparison | Used for high death and disease threats. |
| `relief_political_refusal` | affected country can refuse | no aid accepted | none | slower recovery, possible prestige or independence gain | AI refuses when hostile donor or puppet risk is high. |
| `relief_misdirected` | failed or overloaded relief route | aid arrives late or to wrong card | donor still pays partial cost | recovery score lower, unrest can rise | Occurs under bad ports, war, low stability, or many cards. |

## Active mission cap model

| Cap input | Direction |
| --- | --- |
| Base active rescue cap | Low, readable cap with enough room for urgent actions. |
| Country size factor | Larger countries can manage more active missions. Small countries get fewer but cheaper actions. |
| War factor | War can reduce civilian recovery capacity, but raises priority for route and supply missions. |
| Disaster count factor | Disaster Barrage and Evolution II seasons add limited extra capacity so the category does not choke. |
| State severity factor | Abnormal or severe cards can reserve one mission slot. |
| Foreign relief factor | Relief can add an extra temporary mission slot if it arrives, or occupy a slot while delayed. |

## Partial success rule

| Outcome | What it means | Design use |
| --- | --- | --- |
| Full success | The country met the objective before the deadline and paid the required cost. | Remove or sharply reduce the related modifier, lower deaths, and close or downgrade one risk badge. |
| Partial success | The country achieved the core rescue or route goal but missed a secondary requirement or deadline. | Reduce deaths or damage but leave a weaker modifier, dependency risk, refugee pressure, or delayed repair. |
| Failure | The country did not meet requirements in time or cancelled the mission under pressure. | Fire or strengthen the follow-up chain, extend state modifier, raise recovery cost, or create additional report. |

Partial success is important because disaster recovery should not be binary. A country can save people while losing a port. It can open a rail route while leaving disease risk. It can accept foreign food while creating dependency risk.

## Category cleanup

| Cleanup condition | Required behavior |
| --- | --- |
| Affected country no longer exists | Cancel visible missions, clear country card variables, and keep history only in Event 013 season record. |
| State changes controller during active card | Transfer recovery responsibility only if the new controller owns or controls the state and is valid. Otherwise hold the card as unresolved territory. |
| Disaster card closes | Remove card-specific decisions, clear temporary targets, keep history entry available. |
| Evolution changes | Existing cards continue with old family logic, new cards use evolved rules. |
| Disaster Barrage ends | Close scenario-only launch flags and leave ordinary Event 013 system clean. |
| Event 051 Heat Wave becomes active | Event 013 heat cards stop creating new heat modifiers and either resolve or convert to non-stacking local relief. |
