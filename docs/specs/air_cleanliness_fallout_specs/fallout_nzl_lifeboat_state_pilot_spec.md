# New Zealand Lifeboat State pilot specification

Status: accepted for dormant additive implementation. The bounded pilot depth review is promoted for sea-road operations and Fallout-owned country-memory presentation. Activation remains subject to the live Fallout allocation ledger.

Every label in this file is a working design label unless it is a script identifier. Final player-facing wording is written during implementation.

## Playable promise

The New Zealand Lifeboat State is a small maritime survivor that turns the surviving ports, dairy stores, weather stations, and radio relays of New Zealand into one contested lifeboat. It begins with low manpower, damaged sea capacity, an improvised parliament, and a direct conflict over who receives the remaining berths.

The player manages four visible values through the decision category header:

| Value | Range | Strategic meaning | Main gains | Main losses |
| --- | ---: | --- | --- | --- |
| Harbor capacity | 0 to 100 | Working berths, repair crews, stores, and landing control | port repair, convoy investment, weather preparation | storms, refugee overload, battle damage |
| Food security | 0 to 100 | Dairy stores, fisheries, grain sheds, and ration reliability | dairy rail, fishing compacts, relief deliveries | failed ration choices, convoy loss, winter exposure |
| Parliament trust | 0 to 100 | Public acceptance of lifeboat law and the current route | published ledgers, fair admissions, successful missions | secret seizures, failed missions, broken promises |
| Sea-lane security | 0 to 100 | Patrol coverage, radio bearings, escort strength, and pirate suppression | patrols, radar, escorts, partner access | piracy, route overextension, lost patrols |

The four values are active mechanics. Focuses, decisions, missions, event choices, state control, war, and external partners change them. Thresholds unlock stronger decisions, route conclusions, and the Year 10 order. No value is a passive score used only for flavour.

Static presentation is preferred for this pilot. A scripted decision-category header can show all four values and their current bands without adding a separate window. Animated presentation would add asset and state complexity without making four slowly changing values easier to read.

## Identity and territory

| Field | Accepted dormant pilot value |
| --- | --- |
| Existing carrier tag | `NZL` |
| Country-memory id | `constant:fallout_country_memory.new_zealand_lifeboat_state` |
| Region | `constant:fallout_region.oceania_remote_islands` |
| Archetype | `constant:fallout_government_archetype.maritime_remnant` |
| Primary state package | `284`, `1079`, `723`, `1080`, `1081` |
| Ordered capital choices | `284`, then `1079` only after a current capital receipt proves the selected state |
| Base cosmetic identity | `NZL_FALLOUT_LIFEBOAT_STATE` |
| Humanitarian identity | `NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC` |
| Isolation identity | `NZL_FALLOUT_SOUTHERN_REFUGE` |

The reduced three-state package is not part of this design. If any of the five states fails the current grade, ownership, control, player-reservation, or event-reservation checks, the allocator skips this candidate.

State 726 requires an explicit Samoa disposition. It is owned by vanilla NZL, cored by SAM, used as SAM's capital, and reserved by the Independence Wave Samoa package. The allocator must prove that 726 is outside the NZL assignment and that the SAM reservation has a compatible resolution.

The Independence Wave Aotearoa candidate overlaps states 284 and 723. The allocator must prove that the overlapping identity is inactive, retired, or otherwise resolved before the NZL package can receive a current package receipt.

The package is additive. It does not replace vanilla NZL country history, state history, country tags, characters, focus files, decisions, ideas, AI plans, flags, or OOB files. Runtime activation removes obsolete vanilla NZL decisions and ideas, suppresses original-tag AI plans, and loads the Fallout tree only after every package surface and generation receipt is current.

## Government and characters

The opening government is the Lifeboat Parliament, represented by a fictional institutional council. Its internal factions are the Open Berth Caucus, the Port Wardens, the Dairy Relief Board, and the Radio Service. The public country remains a New Zealand successor rather than taking an agency name.

| Character role | Working identifier | Function | Route |
| --- | --- | --- | --- |
| Institutional leader | `NZL_fallout_lifeboat_parliament` | starting democratic council and national orientation actor | base |
| Relief speaker | `NZL_fallout_relief_speaker` | humanitarian route leader | humanitarian |
| Harbor constable | `NZL_fallout_harbor_constable` | isolation route leader | isolation |
| Dairy relief commissioner | `NZL_fallout_dairy_relief_commissioner` | food and logistics advisor | shared |
| Storm-port engineer | `NZL_fallout_storm_port_engineer` | construction and repair advisor | shared |
| Radio service coordinator | `NZL_fallout_radio_service_coordinator` | intelligence and sea-lane advisor | shared |

All six characters are fictional and require generated, identity-stable portraits. The institutional portrait should show a real group of people in a parliamentary or harbor meeting setting. It must not be a people-free emblem presented as a leader.

The base government is democratic with emergency elections suspended until the domestic chain resolves. The humanitarian route restores scheduled elections and installs the relief speaker. The isolation route retains an emergency assembly under the harbor constable, reduces political openness, and accepts a trust cost in exchange for security.

## Idea lifecycle

| Idea | Starting role | Mitigation | Route upgrade | Failure form | Final disposition |
| --- | --- | --- | --- | --- | --- |
| Empty Harbors | severe port, supply, convoy, and repair penalty | shared port and weather focuses | Storm Ports | Broken Breakwaters | absorbed by Lifeboat Navy or Two-Island Supply Ring, whichever converges first |
| Lifeboat Morality | refugee pressure and trust tension | opening and domestic chains | Open Berth Covenant or Last Berth Doctrine | Berth Riots | retained as one route-defining spirit |
| Dairy Rations | food security with industrial and convoy burden | dairy rail and fishery focuses | Dairy Relief Fleet | Spoiled Stores | absorbed by Two-Island Supply Ring at route maturity |
| Improvised Sea Guard | weak organization and strong home defense | military focuses and reinforcement decisions | Lifeboat Navy | Splintered Patrols | replaced by route naval doctrine |

Only three focus-created country spirits may remain active at once. Lifeboat Navy absorbs Storm Ports when naval convergence happens first. Storm Port Engineers does not recreate that intermediate spirit after Lifeboat Navy is active. Two-Island Supply Ring absorbs Storm Ports and the Dairy Relief Fleet once the food, rail, weather, and port branches converge. The final persistent set is one route spirit, Lifeboat Navy, and Two-Island Supply Ring. Most focuses modify a value, unlock a decision, change buildings, improve an existing spirit, grant equipment tied to a one-shot force action, or open diplomacy.

## Starting forces and growth

Package activation creates one weak one-shot force family only after ownership and control of the exact spawn states are current:

- Wellington Home Guard in province 1814
- Auckland Port Militia in province 4543
- Canterbury Convoy Volunteers in province 2197

The template is a small two-battalion infantry formation with limited starting manpower and equipment. These formations represent surviving local guards rather than a replacement national army. Activation records a one-shot force receipt before creating any unit.

Growth comes from distinct actions:

- Port Militia Drill consumes infantry equipment, manpower, and training time to improve the militia template.
- Convoy Volunteer Corps consumes support equipment and convoys to create one additional escort formation after a successful mission.
- Southern Cross Patrols spends navy experience and convoys to improve coastal defense and naval detection.
- Armed Rescue Cutters converts a limited convoy reserve into a naval patrol capacity benefit rather than spawning free ships.
- Home Guard Rolls uses state control, public trust, and equipment to unlock a defensive mobilization decision with a hard one-time state limit.

No repeatable action may create free divisions, equipment, factories, or convoys.

## Focus architecture

The tree uses `factor = 0`, `default = no`, and one package-active gate. The tree is never selected by tag alone.

### Opening trunk

| Script id | Role | Main visible result |
| --- | --- | --- |
| `fallout_nzl_count_the_living` | opening | initializes visible mechanic values and begins the opening chain |
| `fallout_nzl_seat_the_lifeboat_parliament` | government | recruits the institutional council and opens domestic decisions |
| `fallout_nzl_open_wellington_quays` | port | begins Wellington repair mission and improves harbor capacity |
| `fallout_nzl_relay_auckland_radio` | radio | opens weather and sea-lane actions |
| `fallout_nzl_measure_the_dairy_stores` | food | starts the dairy ration mission and improves food information |
| `fallout_nzl_bind_the_two_islands` | convergence | requires the opening systems and unlocks the route fork |

### Humanitarian route

| Script id | Role | Main visible result |
| --- | --- | --- |
| `fallout_nzl_keep_the_harbor_lights` | route lock | selects humanitarian admissions and opens rescue-passage decisions |
| `fallout_nzl_admit_the_first_rescue_fleet` | crisis | begins a timed refugee-fleet mission |
| `fallout_nzl_publish_the_berth_ledger` | legitimacy | improves trust and makes capacity losses public |
| `fallout_nzl_elect_the_relief_speaker` | politics | changes leader and restores elections |
| `fallout_nzl_guarantee_lifeboat_rights` | law | upgrades Lifeboat Morality into the Open Berth Covenant |
| `fallout_nzl_pacific_relief_republic` | identity | applies the humanitarian cosmetic identity and route AI |

### Isolation route

| Script id | Role | Main visible result |
| --- | --- | --- |
| `fallout_nzl_draw_the_southern_cordon` | route lock | selects controlled admissions and opens exclusion decisions |
| `fallout_nzl_close_unregistered_anchorages` | security | gains security with a trust and trade cost |
| `fallout_nzl_license_every_sea_road` | administration | opens generation-bound licensed fishery and patrol cycles |
| `fallout_nzl_appoint_the_harbor_constable` | politics | changes leader and retains emergency government |
| `fallout_nzl_reserve_the_last_berths` | law | upgrades Lifeboat Morality into the Last Berth Doctrine |
| `fallout_nzl_southern_refuge` | identity | applies the isolation cosmetic identity and route AI |

The numbered sea-road regime records a permanent current-generation licence receipt. It opens the existing Fishery Quota Compact even when the shared economy focus has not done so. A licensed fishery cycle spends five convoys, raises Food Security and Sea-Lane Security, and issues or renews one 90-day patrol window. The existing Quiet-Seas mission is the wartime surge. It spends ten convoys and navy experience, raises Sea-Lane Security by twelve, and renews the same window. Without a current licence receipt, both decisions retain their earlier fail-closed costs and results.

The patrol window records the current Fallout generation and increments one serial each time it is issued. While current, it improves naval detection and convoy escort efficiency. A maintained window adds four points to isolation-route external and Year 10 result scoring. A lapsed window subtracts four points. Opening and domestic scores do not read this route state. Package cleanup clears the active licence, generation receipt, timed window, and serial without a recurring on action.

### Economy and survival branch

| Script id | Main result |
| --- | --- |
| `fallout_nzl_dairy_relief_fleet` | unlocks dairy convoy actions and upgrades Dairy Rations |
| `fallout_nzl_repair_the_milk_rail` | repairs rail and infrastructure capacity between food regions and ports |
| `fallout_nzl_fishery_quota_compacts` | adds a food source with a manpower and patrol tradeoff |
| `fallout_nzl_weatherproof_the_grain_sheds` | reduces storm and winter food losses |
| `fallout_nzl_rebuild_devonport` | restores Auckland naval-base capacity and a dockyard only through the repair mission |
| `fallout_nzl_storm_port_engineers` | unlocks the engineer advisor and stronger port actions |
| `fallout_nzl_radio_weather_chain` | improves weather preparation, detection, and mission lead time |
| `fallout_nzl_two_island_supply_ring` | replaces Empty Harbors after both island logistics are proven |

### Military branch

| Script id | Main result |
| --- | --- |
| `fallout_nzl_home_guard_rolls` | unlocks one-shot state defensive mobilization |
| `fallout_nzl_port_militia_drill` | upgrades the militia template and consumes equipment |
| `fallout_nzl_convoy_volunteer_corps` | opens the escort-formation mission |
| `fallout_nzl_southern_cross_patrols` | improves sea-lane security and coastal detection |
| `fallout_nzl_pirate_bearing_rooms` | unlocks anti-piracy target actions against proven hostile coastal actors |
| `fallout_nzl_armed_rescue_cutters` | converts convoys and navy experience into patrol capacity |
| `fallout_nzl_coastal_denial_batteries` | builds limited coastal forts and anti-air at exact controlled ports |
| `fallout_nzl_lifeboat_navy` | replaces Improvised Sea Guard with the final route doctrine |

### External and late branch

| Script id | Route | Main result |
| --- | --- | --- |
| `fallout_nzl_call_the_island_radios` | shared | opens the bilateral external chain with one proven coastal successor |
| `fallout_nzl_offer_rescue_passages` | humanitarian | offers convoy and refugee access to a valid partner |
| `fallout_nzl_pacific_rescue_mandate` | humanitarian | opens a relief league only after two current partners accept |
| `fallout_nzl_relief_ports_without_annexation` | humanitarian | opens postwar relief and guarantee decisions without core or claim grants |
| `fallout_nzl_demand_quiet_seas` | isolation | pressures hostile coastal actors through access and patrol decisions |
| `fallout_nzl_punitive_anti_piracy_patrols` | isolation | grants a 180-day war goal only against the exact hostile partner that rejected passage and only while neither settlement nor defeat has been recorded |
| `fallout_nzl_southern_sea_exclusion_zone` | isolation | establishes the final closed-seas doctrine after a recorded aggressor is settled, after New Zealand records defeat with reduced rewards, or directly when no aggressor was ever proven |
| `fallout_nzl_year_ten_order` | shared convergence | resolves the late identity chain and records the final campaign order after 3,650 elapsed days |

## Decisions and missions

The category shows early actions first, then route and external actions after their focuses. At most one major repair mission and one external mission may be active.

| Working decision family | Cost or risk | Success | Failure or tradeoff |
| --- | --- | --- | --- |
| Wellington breakwater works | convoys, trucks, repair time | port and harbor recovery | port damage and lost trust |
| Auckland storm-port works | support equipment, manpower, civilian repair capacity | naval-base and supply recovery | delayed repairs and equipment loss |
| Milk rail assignments | trucks, trains, and uninterrupted control of Canterbury | food recovery | spoiled stores and lost equipment |
| Fishery quota compact | manpower, political power, and five convoys under current licensing | food gain and a 90-day licensed patrol window | security falls without licensing, while the licensed cycle raises it |
| Weather station chain | command power and radio equipment | longer mission warning and lower storm loss | no refund if a station is lost |
| Port militia drill | infantry equipment, manpower, and army experience | training experience and sea-lane security | committed resources are lost if the package ends |
| Convoy volunteer corps | support equipment, convoys, manpower | one bounded escort formation | loss of committed resources if mission fails |
| Armed rescue cutters | convoys and navy experience | patrol capacity and security | reduced harbor capacity during conversion |
| Refugee fleet admission | harbor capacity, food security, and political power | a bounded population transfer and trust recovery | overload costs are paid when the mission begins |
| Last-berth closure | trust and trade access | security and food protection | diplomatic isolation and reduced partner pool |
| Offer rescue passage | convoys, food, and target eligibility | bilateral access and relief partner | rejection and sunk cost |
| Anti-piracy bearing | exact aggressor receipt, 65 percent enemy surrender progress, and command power | verified white peace and a generation-bound settlement receipt | unavailable against any substitute target |
| Mobilize a Home Guard state | infantry equipment, manpower, army experience, and public trust | one bunker and a generation-bound state receipt | one active mobilization at a time, with a trust loss if control breaks |
| Dispatch a dairy relief convoy | convoys, trucks, factory time, and harbor capacity | one bounded food and trust recovery | one sailing only, with no transport refund |
| Rebuild a partner relief port | convoys, support equipment, factory time, and an exact current partner | one naval-base level in the partner's stored coastal capital | cancels if that exact state or partner becomes invalid |
| Guarantee a relief partner | convoys, command power, and public trust | one exact current guarantee with reciprocal memory | only one guarantee may be held by this package |
| Revoke raider access | command power, public trust, and an exact aggressor receipt | removes military access and docking rights in both directions | sacrifices trust and cannot substitute another target |
| Quiet-Seas patrol | ten convoys under current licensing, navy experience, and factory time | a larger bounded security gain and one renewed 90-day window during the exact pirate war | one patrol only, with a trust loss if the operation is cancelled |

All eighteen actions have explicit visible and availability conditions, AI weights, cancellation conditions, cleanup, and nonstandard-cost tooltips. Obsolete actions disappear when their route, mission, target, or idea stage ends.

## Country-memory event chains

All events remain in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`. Suffixes 127 through 152 are reserved for this pilot. They do not use the living-world reservation range 100 through 126.

| Suffixes | Chain | Block roles | Durable memory |
| --- | --- | --- | --- |
| 127 to 132 | Harbor Law opening | human root, hidden AI root, human result, delayed hidden resolver, human closure, hidden cleanup | `new_zealand_lifeboat_state_opening_route` |
| 133 to 138 | Lifeboat Morality and Dairy Rations | human root, hidden AI root, human result, delayed hidden resolver, human closure, hidden cleanup | `new_zealand_lifeboat_state_domestic_route` |
| 139 to 146 | Pacific bilateral contact | human owner root, hidden AI owner root, human partner response, delayed hidden resolver, human owner result, hidden cleanup | `new_zealand_lifeboat_state_external_partner`, `new_zealand_lifeboat_state_external_result` |
| 147 to 152 | Year 10 identity | human root, hidden AI root, human result, delayed hidden resolver, human closure, hidden cleanup | `new_zealand_lifeboat_state_late_identity` |

Each chain presents a concrete conflict with three choices. Choice costs are applied before the delayed result. A deterministic score uses the relevant mechanic values, state control, route memory, current war pressure, and prior chain results. Failure and success thresholds are inclusive, while values between them produce partial success. Human and hidden AI routes use the same costs, scoring, effects, memory, and cleanup. Every delayed callback is hidden and always reaches an NZL cleanup path. It shows the human result only after the package, generation, chain, and result receipts pass again.

The external chain saves one exact partner and records reciprocal memory. It refuses to begin without a current Fallout successor row, a coastal state, valid diplomacy, and no existing NZL external transaction. A missing or stale partner cancels through the cleanup block without selecting a substitute. A hostile rejection records that exact partner as the only valid pirate aggressor. The result event can grant that partner military access and docking rights in return for patrol cover. This is a real foreign-basing concession and permanently disqualifies the closed-seas achievement.

The humanitarian rescue-passage focus starts a second deterministic transaction after the first chain closes. The selector excludes every country that already holds a current-generation New Zealand relief-partner receipt, then retains the valid country with the lowest country id. The mission writes its reciprocal receipt only on successful completion. Pacific Rescue Mandate and the open-harbors achievement count at least two living, independent partner countries directly. The numeric count remains presentation memory and cannot satisfy either gate by itself.

### Fallout-owned country-memory presentation

Each resolved chain commits one Fallout country-memory record rather than one record per script block. Opening, domestic, and Year 10 commit at most once per transition generation. Their durable generation receipts survive package runtime reset, so same-generation reactivation cannot duplicate them. Each valid external transaction may commit one record because the humanitarian route can contact more than one exact partner.

Every record stores the Fallout transition generation, country-memory id, chain type, result band, selected policy token, completion date, NZL as primary actor, an optional exact external partner, route token, and snapshots of Harbor Capacity, Food Security, Parliament Trust, and Sea-Lane Security. Stale callbacks may clean their chain state but cannot commit or duplicate history. Package cleanup may remove pending selection state but does not rewrite committed snapshots.

The Event Log exposes these records through a Fallout country-memory subsection, newest first, without placing them in the ordinary Events list. Each compact History row shows its result band. A partnered external row also shows the exact partner name and a second clickable flag. A selected record opens its stored choice, result, date, route, actor, partner, and four value readings. Domestic details also preserve the preceding Harbour Law result. A future post-consequence package view may summarize the exact five-state identity, both routes, the four chain outcomes, valid partner or aggressor memory, and Year 10 order for every human viewer. It must not be attached to a Fallout consequence details card because Fallout has no public Event Details surface.

The presentation is not an evolution row, an ordinary Chaos event, a super-event, or a living-world ledger entry. Event 2 remains Zombie-only. The 26 NZL blocks remain outside the 660 release floor. No ordinary Fallout workbook row and no SCN-014 row may be created by this pilot presentation.

## AI behavior

The package AI plan is active only while the package flag and current transition generation are both valid. It aborts when the package is lost or the generation changes.

The AI first protects food and harbor capacity from critical bands. It then repairs the port network, builds patrol capacity, and resolves the domestic route. It chooses the humanitarian route when food and harbor capacity can support admissions, valid partners exist, and the country is not under severe war pressure. It chooses isolation when sea-lane security is low, hostile coastal actors exist, or the country is fighting for survival.

The humanitarian AI funds rescue passages only when it can pay the convoy and food cost without crossing a critical band. The isolation AI does not create anti-piracy pressure without a proven hostile target. It will not spend the last five convoys on a licensed fishery cycle. With at least ten convoys, it prioritizes a licensed cycle when the patrol window has lapsed and other action gates pass. Both routes prioritize the Year 10 order only after their late route conditions and all four mechanic values meet the required bands. Package activation writes a 3,650-day timed country flag. The Year 10 readiness trigger requires that flag to expire, so focus availability survives saves without a recurring on-action poll.

The package activation effect removes the two obsolete vanilla NZL infrastructure decisions and sets an explicit Fallout AI override flag. Fallout AI plans require this flag. Vanilla original-tag plans must include an abort condition through an additive compatibility surface before activation can be approved.

## Achievements

Three difficult custom achievements belong to the pilot:

- Complete the humanitarian route, keep at least two independent relief partners alive, finish Year 10 with all four mechanic values at 70 or more, and never close the last berths.
- Complete the isolation route, settle every proven pirate aggressor, finish Year 10 with full five-state control, and never accept foreign basing rights. A campaign in which no partner was ever proven hostile can complete the no-aggressor route without creating a substitute enemy.
- Complete the shared economic and naval branches, suffer no failed major mission, keep both Wellington and Auckland ports operational, and finish Year 10 without creating more than one extra escort formation.

The separate achievement handoff defines exact script keys, disqualifiers, and art.

## Activation boundary

The dormant implementation may define package content, receipt validators, assets, and event blocks. It must not set the package-active flag at startup, call the tree by tag, call an event from an on action, change NZL ownership, or set the global successor-allocation completion flag.

Activation requires all of these facts in one current transition generation:

- the live conflict ledger resolves NZL and the five states without player or event-package conflict
- Samoa state 726 has an explicit compatible disposition
- the Aotearoa overlap is resolved
- one approved capital row proves owner, controller, hostability, and assigned-capital membership
- all five package flags and package generations are written by the allocator after their surfaces pass
- the package's focus, decision, character, idea, force, AI, localisation, asset, event, event-log, Event Details, spreadsheet, and audit surfaces are complete
- map return accepts the country package receipt

The package helper never finalizes the global allocation transaction.
