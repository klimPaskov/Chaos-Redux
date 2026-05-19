# Event 005 - Soviet Union Collapse

## Overview

Soviet Union Collapse is a one-per-campaign Liberations cluster event that turns the old stub release into an active union crisis. The entry event remains `chaosx.nr5.1`; it now routes to the visible Soviet event `chaosx.nr5.2`, which initializes the crisis, releases the first breakaway republics, grants them defensive support, and activates the opening Soviet objective board.

The baseline crisis stages are ordinary crisis progression, not evolution logs. Evolutions remain reserved for separate mutation tracks such as old movements, depot states, railway authorities, foreign liaison networks, and high-chaos splinters.

The Event Logs event-detail entry for Event 005 now uses scripted localisation to show the live broad crisis state, first-wave status, Free Republics' League status, Moscow Authority condition, Union Crisis Threat severity, foreign intervention level, and old-movement or high-chaos splinter pressure. The text stays in-world and reads the same crisis variables and flags that drive the gameplay board instead of using debug-style implementation notes.

## Current Implementation

The implemented opening slices cover the crisis scaffold and the first intervention layer:

- `common/script_constants/005_soviet_collapse_constants.txt` centralizes opening crisis values, breakaway support, future declaration support adjustments, objective requirements, objective pressure families, and first response costs.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt` adds active-crisis, breakaway, patron, cost, recovered-capital, second-wave quieting, provincial office, emergency procurator, capital district, western telegraph, grain-file, governors' oath, archive, negotiated-corridor, government-file, regional-command, inner-ring, loyal-rail, militia, amnesty, League-calendar, lost-depot, Soviet-identity, rump-preparation, victory-parade, shared-road, depot-retaking, volunteer-route, republic-army, defense-committee, next-declaration, League-front, printing-office, foreign-photo, commander-reassignment, moved-unit reward, rail-junction, signal-school, navy-oath, armored-train, officer-conference, guards-division, commissar-escort, war-room, Smolensk-ledger, Ukrainian-depot, Belarusian-rail, Baltic-port, Caucasus-oil, Ural-factory, Siberian-storehouse, fuel-relocation, ammunition-census, northern-port, unofficial-consulate, western-corridor, Finnish-border, Turkish-mission, Iranian-road, Japanese-liaison, sponsor-price, neutral-observation, radio-link, humanitarian-aid, peasant-anger, civil-war-file, Huliaipole quieting, village-League negotiation, religious-institution, Basmachi-chain, Volga-name, factory-committee, sailor-assembly, grave-register, western-gate, Baltic-legal, Caucasus-mountain, Tashkent-anchor, Dushanbe-pass, Ashgabat-border, Bishkek-signal, Kazakhstan-first-wave, Siberian-distance, Vladivostok-command, League-quorum, League-split, separate-exit, shared-defense-calendar, foreign-envoy, League-depot, loyalist-pocket, League-border-dispute, high-chaos report-classification, hospital-record containment, factory-whistle, star-iron rumor, funeral-train, crown-archive, resurrection-committee, northern-fleet, religious-war-room, living-grave-census, restored-budget, civilian-school, local-unit-demobilization, New Union budget, recognition-file, temporary-disorder narrative, rewritten-union, emergency-command retirement, recovered-depot inventory, and crisis-desk disbanding triggers.
- `common/scripted_effects/005_soviet_collapse_effects.txt` initializes the crisis meter, clamps and recalculates total threat, releases the opening breakaways, gives starting forces, applies recoverable republican startup disorder, runs progressive threat-based breakaway checks, and enforces the Soviet objective cap.
- `common/ideas/005_soviet_collapse_ideas.txt` adds country spirits for the union crisis, Moscow response routes, the restored union recovery, loyalist officers, captured depots, and breakaway defensive coordination.
- Soviet Collapse spirits use file-local tuning packages because idea modifier blocks do not parse shared script constants. The core spirits and special successor spirits are meant to change play through combined legitimacy, mobilization, command, supply, depot, defensive, manpower, production, and foreign-cohesion effects rather than isolated tiny percentages.
- `common/decisions/005_soviet_collapse_decisions.txt` adds four non-political-power Soviet response decisions, one hundred twenty-eight opening goal-style missions, four breakaway emergency actions, and thirteen targeted foreign patron decisions.
- `events/005_soviet_collapse.txt` replaces the old hidden release stub with a visible opening event and four posture choices.
- `events/005_soviet_collapse_factory_ancient.txt` adds the triggered notices for the first high-chaos factory and Volga successor states.

## Foreign Influence Tracking

Foreign patron decisions build permanent pressure on the target republic instead of only granting one-off aid. Each targeted intervention records both a category total and a sponsor total on the republic:

- category totals: recognition, arms, volunteers, industry, intelligence, ideology, logistics, and patronage risk
- sponsor totals: Germany, Britain, Japan, France, the United States, Turkey, Iran, Poland, Romania, Finland, Sweden, and Italy

The category totals mature into three parallel staged spirit tracks. Diplomatic backing grows from contacts to missions to treaty backing. Material backing grows from supply contacts to corridors to a full supply network. Patronage grows from contacts to liaison to a patronage network. These spirits can coexist because the republic may be recognized by one sponsor, supplied by another, and advised by a third.

The foreign patron category now covers the first full investment set: recognition, ideological liaison, equipment convoys, military advisers, intelligence channels, volunteer corps, trade missions, civilian construction, military construction, press and radio networks, aid corridors, republic conference sponsorship, and an anti-puppet clause. Civilian construction adds a civilian factory and infrastructure to the target republic while applying a temporary consumer-goods and output burden to the sponsor. Military construction adds military industry and anti-air. Aid corridors open a target-side flag for later route logic. Volunteer corps now spawns a republican field brigade in addition to the manpower and equipment package.

The anti-puppet clause is the first rival-contest decision. It raises `soviet_collapse_independence_resilience` and lowers `soviet_collapse_influence_patronage_risk`, giving puppet logic a resistance value that can come from balanced sponsorship instead of only raw strength.

## Reintegration And Dependency Pressure

Moscow now participates in the influence contest through two targeted Soviet decisions. `Offer a New Union Treaty` is available only while Union Crisis Threat is low or moderate, Moscow Authority is credible, the target is not at war with Moscow, and the target is not protected by a strong League or faction. The treaty spends political power, command power, fuel, and trains, then raises `soviet_collapse_influence_moscow`, lowers target patronage risk and independence resistance, and applies New Union Negotiations. `Offer a Federal Reintegration Compact` is the follow-up: it requires the treaty channel, dominant Moscow influence, lower threat, stronger Moscow Authority, a weak target, low patronage lock-in, and no League protection. It federates the target as a Soviet autonomous subject through `set_autonomy` instead of annexing it outright.

Foreign sponsors now use a three-step dependency chain rather than a simple puppet button. `Offer Protection Treaty` requires the sponsor to be the dominant influence holder on the target, the target to be weak, the target to have low independence resilience, and the target to lack strong League or faction protection. `Demand Adviser Privileges` requires the protection treaty and deepens volunteer influence and patronage risk. `Install Client Cabinet` requires adviser privileges and then sets the target as the sponsor's puppet. The chain is blocked while the republic is in a major war with Moscow, already a subject, or shielded by a strong League/faction, so a sponsor cannot bypass the independence-resilience and League-balancing systems.

Local leagues now operate as the regional layer below the Free Republics' League. The regional faction category exposes the Baltic Restoration Pact, Caucasus Defense Compact, and Central Asian League founding decisions to eligible breakaways before they already have a faction flag. Founders recruit aligned partners, apply regional commitments, pick shared goals, settle tension, and can call a high-threat defensive war that clears the progressive release cooldown and checks the MTTH release scheduler. Kazakhstan remains locked out of the Central Asian League and progressive Central Asian pressure until at least three smaller Central Asian republics are free. Full notes live in `docs/events/005_soviet_union_collapse_local_leagues.md`.

No new icons are required for this slice. The staged spirits and patron burden spirit reuse the existing `legal_restoration_claim`, `captured_soviet_depots`, and `foreign_volunteers` idea pictures already registered by `interface/005_soviet_collapse_icons.gfx`.

## Crisis Meter

The Soviet crisis category uses these variables:

- `soviet_collapse_total_collapse_threat`
- `soviet_collapse_moscow_authority`
- `soviet_collapse_republic_confidence`
- `soviet_collapse_military_obedience`
- `soviet_collapse_depot_vulnerability`
- `soviet_collapse_foreign_appetite`
- `soviet_collapse_league_cohesion`
- `soviet_collapse_evolution_weirdness`
- `soviet_collapse_breakaway_count`

In calm conditions, central authority still has room to answer the crisis. Opening values then change from chaos tier, Soviet stability, war support, active wars, and capital control. The total threat is recalculated from the component variables instead of being a fixed timer.

## Opening Breakaways

The normal opening wave is selected from structured pools instead of hard-coding Ukraine and Belarus. When the map supports it, the first wave chooses one western or eastern European actor, one Caucasus republic, and one Central Asian republic other than Kazakhstan, then adds extra ordinary republics as chaos, war, stability, and Soviet condition worsen. Kazakhstan is outside the normal opening pools and only enters early when southern pressure or severe crisis conditions justify a steppe rupture. Each appearing breakaway receives:

- `soviet_collapse_breakaway` country flag
- manpower and equipment from script constants
- `soviet_collapse_captured_soviet_depots`
- `soviet_collapse_defensive_coordination`
- an `Emergency Republican Guard` template and capital guard divisions from the base package
- an `Emergency Republican Field Brigade` template with artillery for larger or more chaotic releases
- extra manpower, rifles, support equipment, artillery, guard units, and field brigades from tag strength, chaos tier, Soviet war state, weak Moscow Authority, and high Union Crisis Threat

When Kazakhstan appears as an event-created opening breakaway, the southern cascade can also begin. Uzbekistan appears with Kazakhstan if still under Moscow control, Kyrgyzstan can appear at chaos tier 3 and above, Tajikistan can appear at chaos tier 4 and above, and Turkmenistan can appear at chaos tier 5. These southern republics receive the standard breakaway setup package and the shared Central Asian runtime focus tree.

Future breakaway setup also consumes one-use Soviet mission flags. `soviet_collapse_next_declaration_unarmed` reduces the next breakaway support package, while `soviet_collapse_next_declaration_armed` increases it; either flag clears after it is applied to one breakaway.

## Terminal Collapse

`Union Unmade` now resolves the crisis instead of only presenting the super-event. When `soviet_collapse_show_union_unmade_super_event` fires, `soviet_collapse_apply_terminal_collapse` runs before the presentation layer. The terminal pass releases every ordinary non-Russian Soviet republic that is still unreleased, has core territory owned and controlled by `SOV`, and is part of the supported republic set: Ukraine, Belarus, Moldova, the Baltic republics, the Caucasus republics, Uzbekistan, Kyrgyzstan, Tajikistan, Turkmenistan, and Kazakhstan. It also frees any already-existing supported republic that is still a Soviet subject. Each republic released or freed by this terminal pass receives `soviet_collapse_event_created_republic`, the normal breakaway setup package, its runtime focus tree, and an extra final-collapse military package from `constant:soviet_collapse_breakaway_support.terminal_*`.

High-chaos terminal collapse is additive. Chaos tier 4 and 5 attempt the implemented high-chaos successor spawns after ordinary republic release, so special actors can appear where their required territories remain under Soviet ownership and control. At chaos tier 5, the terminal pass treats the containment network as having broadly failed, unlocks the high-chaos successor gates used by the existing spawn helpers, and raises old-movement weirdness to the high-chaos gate if it has not already reached it. The existing tag checks, evolution-enable settings, mutually exclusive tag conflicts, and territory ownership/control requirements still decide which special actors are eligible.

The same terminal effect closes the pre-collapse crisis board. `soviet_collapse_cleanup_terminal_collapse_missions` clears the active Soviet Collapse and opening-wave flags, clears one-use next-declaration flags, clears transient loyal-unit and district war-room helper flags, removes any active Soviet crisis mission from mission 1 through mission 128 with `remove_mission`, and leaves `soviet_collapse_terminal_collapse` as the outcome memory. Because `is_soviet_collapse_active` now excludes the terminal flag, Soviet response, breakaway action, regional faction, special-actor, and foreign patron categories no longer remain visible after full collapse. The current foreign patron layer uses repeatable targeted decisions with `days_re_enable`, not active timed missions, so there is no separate foreign mission instance to remove in the terminal pass.

The local event catalog workbook row for Event 005 matches the current clean-spec implementation, and the current parser-oriented audit passes across the opening, republic, regional, custom successor, achievement, spreadsheet, and super-event surfaces.

## Republic Focus Trees

Event-created Ukraine, Belarus, Kazakhstan, southern cascade republics, prepared regional tags, and any remaining event-created breakaway without a bespoke tree receive runtime focus trees through `load_focus_tree` after the release effect finishes. The loading effect only applies to countries with `soviet_collapse_event_created_republic`, and it does not use `keep_completed`, so it is intended for freshly released tags rather than replacing progress on existing countries. The high-chaos `CFR`, `MFR`, `OGB`, `ICD`, `KRS`, `FTH`, `BBH`, `BSC`, `TNC`, `ALA`, `UDC`, `SDZ`, `RMC`, `RCD`, `ILU`, `PRA`, `TSC`, `BLT`, `NRF`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `TRS`, `NLC`, `SEP`, `DSC`, `COU`, `BEC`, `RLD`, `LID`, and `IRA` successors are loaded directly from their setup effects with `keep_completed = no`, because they are custom crisis countries rather than standard released republics.

The implemented trees are:

1. `soviet_collapse_ukraine_focus_tree` in `common/national_focus/005_soviet_collapse_republics.txt`: 97 focuses after the duplicate-pruning layout pass. The layout opens from the Emergency Rada into telegraph, grain, and depot side focuses, converges on the first republican line, then branches into six political route locks: Central Rada, socialist republic, military directory, Hetmanate file, Black Banner compact, and foreign provisional authority. The lower rows separate democratic legality, socialist sovereignty, military-directory rule, conservative restoration, army doctrine, industry mobilization, diplomacy, League preparation, foreign-aid, late expansion policy, and hidden high-chaos lanes.
2. `soviet_collapse_belarus_focus_tree`: 55 focuses after the duplicate-pruning layout pass. The layout opens through the Minsk emergency office, rail map, forest committees, corridor guard, evacuation choice, route locks for the National Council, socialist autonomy, military transit, and foreign corridor administration, then branches into rail sovereignty, forest defense, corridor diplomacy, League logistics, neutral-corridor survival, foreign-aid containment, high-chaos forest identity, late rail-state logistics, and final League, corridor-state, and no-foreign-timetable finishers. The tree uses existing branch sprites and shared Soviet Collapse focus reward helpers.
3. `soviet_collapse_kazakhstan_focus_tree`: 60 focuses after the duplicate-pruning layout pass. The layout opens from the Steppe Congress into rail, depot, and district-command branches, then separates Alash restoration, steppe socialist sovereignty, mobile military command, resource sovereignty, federal diplomacy, high-chaos myth, settlement, late defense, and final state-definition tracks with branch sprite reuse documented in the asset ledger.
4. `soviet_collapse_baltic_focus_tree`: 21 focuses after the duplicate-pruning layout pass. The layout opens from restoration of the state seal into archives, prewar deputies, and emergency border guards, then branches into legal continuity, military border government, Baltic League-first, and foreign-protection routes with port sovereignty, recognition, compact diplomacy, border defense, and high-chaos civic mobilization follow-ups.
5. `soviet_collapse_caucasus_focus_tree`: 20 focuses after the duplicate-pruning layout pass. The tree opens from mountain and city councils into pass defense, oil and port protection, and border faiths and nations, then branches into Mountain Federal Compact, Oil Emergency Directorate, National Restoration Councils, and Foreign Border Guarantees with compact, oil oversight, border treaty, Caspian watch, high-chaos ancient-claim, and survival finishers.
6. `soviet_collapse_central_asia_focus_tree`: 14 focuses after the duplicate-pruning layout pass. The tree opens from the Southern Emergency Majlis into oasis and pass guards, irrigation and bread councils, and border caravans, then branches into local republic, Turkestan federation, military border authority, and foreign border patronage routes with southern coordination, Basmachi, oasis arsenal, foreign-aid, pact/federation, cotton, high-chaos Khwarazm, and southern survival finishers.
7. `soviet_collapse_moldova_focus_tree`: 17 focuses for event-created Moldova after the duplicate-pruning layout pass. The tree opens from the Chisinau Emergency Council into Dniester crossing guards, Bessarabian legal files, and the Romanian question, then branches into an Independent Republic Council, Dniester Defense Directorate, Romanian Alignment Office, and Ukrainian Border Compact with river guard, Bessarabian negotiation, grain road, union-question, and small-state survival finishers.
8. `soviet_collapse_breakaway_focus_tree`: 27 focuses for remaining event-created breakaways without bespoke runtime trees. The fallback follows the clean-spec emergency replacement map: emergency government trunk, legal restoration, socialist sovereignty, military defense, foreign liaison, depot and garrison defense, League preparation, neutrality, high-chaos evolution hooks, capital-or-field committee governance, logistics identity, and late survival finishers. It reuses the already wired shared focus icons.
9. `CFR_soviet_collapse_focus_tree`: 45 focuses for the Civilian Factory of Russia high-chaos successor. The tree opens through crane, trust-office, ration-card, cement, and unfinished-city focuses, then splits into Worker Cooperative, Planner Directorate, Foreign Contract Board, and Concrete Committee governance routes. Its construction strategy fork covers Cities First, Rails First, Factories First, and Contracts First, while side branches cover construction battalions, foreign reconstruction contracts, the coercive City Without Citizens route, and late builder-state convergence.
10. `MFR_soviet_collapse_focus_tree`: 37 focuses for the Military Factory of Russia high-chaos successor. The tree opens through production-order, arsenal-board, machine-tool, factory-guard, and ration-law focuses, then branches into officer board, armorer delegate, ammunition merchant, and Eternal Arsenal routes. Its production lanes cover rifle, artillery, tank, aircraft, and unsafe shell output, with side paths for League weapons, unmarked exports, factory guards, armored trains, Civilian Factory rivalry, and late Arsenal State convergence.
11. `OGB_soviet_collapse_focus_tree`: 32 focuses for the Old Great Bulgaria high-chaos successor. The tree opens through the returned name, old crossings, Bolghar archive tables, ferry offices, and the question of who speaks for Bolghar, then branches into scholars, merchants, river captains, and high-chaos old-name routes. Its later rows cover market roads, ferry licenses, customs houses, steppe and southern trade, community compromise, river patrol doctrine, foreign correspondence, rival ancient claims, trade-peace, Volga-Caspian expansion, and Third Bulgar Realm finishers.
12. `ICD_soviet_collapse_focus_tree`: 21 focuses for the Iron Commissariat of the Dead, built around death-roll authority, foundry stores, death guards, cemetery logistics, and the Total Mobilization of the Dead capstone.
13. `KRS_soviet_collapse_focus_tree`: 20 focuses for the Kronstadt Free Soviet, built around sailor assemblies, fortress stores, naval militias, port councils, and the Every Port a Council capstone.
14. `FTH_soviet_collapse_focus_tree`: 21 focuses for the Free Territory of Huliaipole, built around free communes, depot-raiding guards, temporary League bargains, Black International channels, and the World Without Capitals capstone.
15. `BBH_soviet_collapse_focus_tree`: 21 focuses for the Black Banner Host, built around mobile columns, commune war councils, captured stores, anti-state campaigns, and the World Without Prisons capstone.
16. `BSC_soviet_collapse_focus_tree`: 21 focuses for the Basmachi Confederation, built around oasis confederation politics, pass guards, caravan stores, road control, and the Road Beyond the Steppe capstone.
17. `TNC_soviet_collapse_focus_tree`: 21 focuses for the Turkestan National Council, built around civic offices, railway guards, oasis bureaus, guarded routes, and the New Turkestan capstone.
18. `ALA_soviet_collapse_focus_tree`: 21 focuses for the Alash Restoration Authority, built around congress legitimacy, cavalry guards, schools, rail stations, and the National Modernization Mandate capstone.
19. `UDC_soviet_collapse_focus_tree`: 21 focuses for the Union Defense Committee, built around loyal districts, provisional command, signature forces, and the Provisional Soviet Command capstone.
20. `SDZ_soviet_collapse_focus_tree`: 21 focuses for the Security Directorate Zone, built around archives, directorate rule, signature forces, and the World in One Archive capstone.
21. `RMC_soviet_collapse_focus_tree`: 21 focuses for the Red Martyrs' Resurrection Cult, built around registers, funerary authority, signature forces, and the Every Grave a Barracks capstone.
22. `RCD_soviet_collapse_focus_tree`: 21 focuses for the Red Cosmist Directorate, built around common-task offices, resurrection logistics, signature forces, and the No Grave Outside the State capstone.
23. `ILU_soviet_collapse_focus_tree`: 21 focuses for the Iron Liturgy of the Urals, built around furnace councils, industrial discipline, signature forces, and the World as One Factory capstone.
24. `PRA_soviet_collapse_focus_tree`: 21 focuses for the Pale Railway Authority, built around timetable rule, rail logistics, signature forces, and the Every Junction Under Authority capstone.
25. `TSC_soviet_collapse_focus_tree`: 21 focuses for the Tunguska Star Committee, built around expeditionary command, star-iron rumor, signature forces, and the Bring the Fire West capstone.
26. `BLT_soviet_collapse_focus_tree`: 21 focuses for the Brotherhood of the Last Tsar, built around regency brotherhood authority, crown archives, signature forces, and the Universal Throne capstone.
27. `NRF_soviet_collapse_focus_tree`: 21 focuses for the Northern Revenant Fleet, built around icebound fleet command, northern ports, signature forces, and the Every Coast a Northern Port capstone.
28. `GAC_soviet_collapse_focus_tree`: 21 focuses for the Green Army Congress, built around village congresses, land-and-bread authority, signature forces, and the Land and Bread Against the World capstone.
29. `DHC_soviet_collapse_focus_tree`: 21 focuses for the Don Host Emergency Circle, built around host-circle consolidation, southern cavalry authority, signature forces, and the Southern Host Command capstone.
30. `KHC_soviet_collapse_focus_tree`: 21 focuses for the Kuban Host Provisional Council, built around crossing councils, Kuban line command, signature forces, and the Kuban Line Command capstone.
31. `FEV_soviet_collapse_focus_tree`: 21 focuses for the Far Eastern Republic Revival, built around buffer restoration, railway guards, foreign distance, and the Far Eastern Line Command capstone.
32. `SZA_soviet_collapse_focus_tree`: 21 focuses for the Siberian Zemstvo Authority, built around regional assembly rule, city guards, Siberian depth, and the Siberian Depth Command capstone.
33. `UWD_soviet_collapse_focus_tree`: 21 focuses for the Ural Workers' Directorate, built around factory committees, worker battalions, arsenal autonomy, and the Arsenal Autonomy capstone.
34. `MRC_soviet_collapse_focus_tree`: 21 focuses for the Mountain Republic of the Caucasus, built around elder councils, pass guards, mountain federal authority, and the Mountain Republic Mandate capstone.
35. `IUL_soviet_collapse_focus_tree`: 21 focuses for the Idel-Ural League, built around Volga-Ural federal offices, river guards, corridor authority, and the Federal Corridor Authority capstone.
36. `BAC_soviet_collapse_focus_tree`: 21 focuses for the Birobidzhan Autonomous Commune, built around settlement committees, militia mobilisation, autonomous offices, and the Autonomous Commune Mandate capstone.
37. `ARD_soviet_collapse_focus_tree`: 21 focuses for the Arctic Naval Directorate, built around port directorate rule, convoy officers, northern port logistics, and the Port Neutrality Mandate capstone.
38. `TRS_soviet_collapse_focus_tree`: 21 focuses for the Third Rome Emergency Synod, built around emergency synod authority, synod guards, Moscow sanctification, and the Fourth Testament of Moscow capstone.
39. `NLC_soviet_collapse_focus_tree`: 21 focuses for the Northern Lights Commune, built around polar survival committees, scientific refuge authority, northern survival logistics, and the World After Capitals capstone.
40. `SEP_soviet_collapse_focus_tree`: 21 focuses for the Sepulchre Soviet, built around burial committees, grave registries, cemetery administration, and the World Cemetery Mandate capstone.
41. `DSC_soviet_collapse_focus_tree`: 21 focuses for the Dead Soldiers' Congress, built around veterans' assemblies, dead-regiment myth, military memory, and the Army of the Fallen capstone.
42. `COU_soviet_collapse_focus_tree`: 21 focuses for the Commissariat of the Unburied, built around unburied claims, grave disputes, state custody of the dead, and the No Burial Without the State capstone.
43. `BEC_soviet_collapse_focus_tree`: 21 focuses for the Black Earth Resurrection Cult, built around black-earth rites, soil factions, harvest graves, and the Every Field a Grave capstone.
44. `RLD_soviet_collapse_focus_tree`: 21 focuses for the Red Lazarus Directorate, built around Lazarus laboratories, return committees, hospital guards, and the Return Is Mandatory capstone.
45. `LID_soviet_collapse_focus_tree`: 24 focuses for the Last International of the Dead, built around dead delegates, martyr rolls, battlefield congresses, and the All Dead Are Comrades capstone.
46. `IRA_soviet_collapse_focus_tree`: 24 focuses for the Iron Resurrection Army, built around foundry staffs, cemetery rails, repaired bodies, and the Army That Returns capstone.

Focus rewards call shared scripted effects for legal recognition, socialist sovereignty, military consolidation, depot control, League preparation, foreign channels, and high-chaos identity pressure. Those effects adjust local breakaway variables and feed the Soviet crisis meter through constants in `soviet_collapse_republic_focus`. Ukraine's replacement slice also documents each focus role in script comments, uses focus filters on every focus, keeps League escalation locked behind crisis pressure through `is_soviet_collapse_league_pressure_ready`, and keeps foreign provisional authority behind an actual liaison-office state and high foreign pressure.

Continuous focus windows for the Event 005 republic, factory successor, and custom splinter trees sit in a right-side panel outside each focus grid. The runtime layouts are generated from prerequisite depth, spread into branch lanes, and capped at ten visible focuses per row, leaving the opening trunks, route locks, side economies, diplomacy lanes, and high-chaos branches readable without coordinate collisions or shallow side focuses ending as isolated leaves.

The Ukraine middle-branch slices add the General Staff frontier choice, Republican Deep Battle, Militia Federalization, Black Sea port ledgers, grain and coal crosslinks, railway quartermasters, local factory guards, requisition crisis handling, the Industrial Mobilization Council, arms/export industry route locks, Economic Sovereignty, foreign liaison side branches, and League signal-code route locks. `soviet_collapse_form_free_republics_league_from_ukraine` creates the Free Republics' League only through the gated League Founding Charter focus and pulls eligible event-created breakaways into the faction. The late expansion slice adds the defensive-line gate, Black Sea rim, western and Romanian policy tracks, Balkan and Anatolian supply diplomacy, Carpathian security, protectorate debate, League security zones, direct national-claim policy, Black Sea hegemony, Breadbasket Empire, Granary of Free Republics, border-state coordination, No Foreign Master, and the Great Steppe and Sea Plan. The high-chaos slice follows the Part 3 row names for The Bread State Whispers, The Black Soil Oath, Harvest by Decree, Dead Fields Living Columns, Grain Census of Everyone, No One Leaves the Bread Line, The Last Harvest Plan, Black Banner Takes the Villages, Kyiv or Huliaipole, The Double Republic, The Commune War, and When the Fields Refuse the State. These focuses remain hidden behind high-chaos and old-movement pressure until the exact food-crisis and Free Territory evolution trigger pass is implemented. The democratic deep slice adds Coalition of Three Ministries, the Rural Deputy Bloc, Minority Autonomy Statutes, the Emergency Court of Kyiv, parliamentary front oversight, the governor/rada fork, Republic of Laws, and Civilian Command Over the Army. The socialist sovereignty slice adds the Workers' Congress in Kharkiv, Village Soviets Without Requisition, the party-card fork, Moscow loyalist purge or re-registration choices, armed factory soviets, the anti-landlord village line, left League diplomacy, the commune debate, and the red republic finisher. The military-directory slice adds Field Headquarters precedence, district mobilization, officer patronage lists, depot courts, the General Staff War College, the commander/cabinet fork, Army Supremacy, Mixed Emergency Cabinet, War Plans Beyond the Border, and the Directory State. The Hetmanate slice adds estate credit offices, the crown-without-a-crown fork, Symbolic and Executive Hetmanate choices, conservative officer circles, the church-and-grain settlement, foreign court recognition, and the Second Hetmanate finisher. The final foreign, League, and late-game slice adds sponsor-crate audits, the political-adviser fork, League arbitration, shared depot ledgers, Republics' Joint Staff, the border mandate vote, Black Sea customs policy, port soldiers, the western-question pressure focus, bread-line border escalation, and the two endgame settlement focuses. Achievement definitions for the implemented Event 005 routes are wired in `common/achievements/chaos_redux_achievements.txt`; future-only achievement entries stay tied to route or super-event flags reserved for later audit passes. Super-event escalation fires from the broad breakaway threshold and implemented route capstones for slots 15 through 27, with slot 16 backed by Iron Commissariat, Red Martyrs, Sepulchre Soviet, Dead Soldiers, Unburied Commissariat, Black Earth, Red Lazarus, Last International, and Iron Resurrection routes, and slot 18 backed by Kronstadt, Northern Revenant, and Arctic Naval Directorate routes.

## High-Chaos Tags

The first high-chaos successor tags are registered for spawn and mechanics work:

1. `CFR` - Civilian Factory of Russia, led by the Construction Board, with existing flag and leader assets.
2. `MFR` - Military Factory of Russia, led by the Arsenal Board, with existing flag and leader assets.
3. `OGB` - Old Great Bulgaria on the Volga, led by the Volga Restoration Council, with existing flag and leader assets.
4. `ICD` - Iron Commissariat of the Dead, led by the Iron Death Commissariat, with existing flag and leader assets.
5. `KRS` - Kronstadt Free Soviet, led by the Sailors' Assembly, with existing flag and leader assets.
6. `FTH` - Free Territory of Huliaipole, led by the Council of Free Soviets, with existing flag and leader assets.
7. `BBH` - Black Banner Host, led by the Black Banner War Council, with existing flag and leader assets.
8. `BSC` - Basmachi Confederation, led by the Oasis War Council, with existing flag and leader assets.
9. `TNC` - Turkestan National Council, led by the Turkestan Civic Council, with existing flag and leader assets.
10. `ALA` - Alash Restoration Authority, led by the Alash Restoration Council, with existing flag and leader assets.
11. `UDC` - Union Defense Committee, led by the Emergency Military Committee, with existing flag and leader assets.
12. `SDZ` - Security Directorate Zone, led by the Directorate Collegium, with existing flag and leader assets.
13. `RMC` - Red Martyrs' Resurrection Cult, led by the Funeral Commissar, with existing flag and leader assets.
14. `RCD` - Red Cosmist Directorate, led by the Common Task Directorate, with existing flag and leader assets.
15. `ILU` - Iron Liturgy of the Urals, led by the Foremen's Synod, with existing flag and leader assets.
16. `PRA` - Pale Railway Authority, led by the Central Timetable Board, with existing flag and leader assets.
17. `TSC` - Tunguska Star Committee, led by the Expeditionary Committee, with existing flag and leader assets.
18. `BLT` - Brotherhood of the Last Tsar, led by the Regency Brotherhood, with existing flag and leader assets.
19. `NRF` - Northern Revenant Fleet, led by the Icebound Admiralty, with existing flag and leader assets.
20. `GAC` - Green Army Congress, led by the Peasant Congress Council, with existing flag and leader assets.
21. `DHC` - Don Host Emergency Circle, led by the Host Emergency Circle, with existing flag and leader assets.
22. `KHC` - Kuban Host Provisional Council, led by the Kuban Provisional Council, with existing flag and leader assets.
23. `FEV` - Far Eastern Republic Revival, led by the Far Eastern Buffer Committee, with existing flag and leader assets.
24. `SZA` - Siberian Zemstvo Authority, led by the Siberian Regional Assembly, with existing flag and leader assets.
25. `UWD` - Ural Workers' Directorate, led by the Factory Directorate, with existing flag and leader assets.
26. `MRC` - Mountain Republic of the Caucasus, led by the Mountain Republic Council, with existing flag and leader assets.
27. `IUL` - Idel-Ural League, led by the Volga-Ural Federal Council, with existing flag and leader assets.
28. `BAC` - Birobidzhan Autonomous Commune, led by the Settlement Defense Council, with existing flag and leader assets.
29. `ARD` - Arctic Naval Directorate, led by the Northern Port Directorate, with existing flag and leader assets.
30. `TRS` - Third Rome Emergency Synod, led by the Emergency Holy Synod, with existing flag and leader assets.
31. `NLC` - Northern Lights Commune, led by the Aurora Survival Council, with existing flag and leader assets.
32. `SEP` - Sepulchre Soviet, led by the Central Sepulchre Soviet, with existing flag and leader assets.
33. `DSC` - Dead Soldiers' Congress, led by the Dead Soldiers' Congress, with existing flag and leader assets.
34. `COU` - Commissariat of the Unburied, led by the Unburied Claims Board, with existing flag and leader assets.
35. `BEC` - Black Earth Resurrection Cult, led by the Black Earth Synod, with existing flag and leader assets.
36. `RLD` - Red Lazarus Directorate, led by the Lazarus Directorate, with existing flag and leader assets.
37. `LID` - Last International of the Dead, led by the Last International Secretariat, with existing flag and leader assets.
38. `IRA` - Iron Resurrection Army, led by the Iron Resurrection Staff, with existing flag and leader assets.

These tags define country files, history files, politics, basic technologies, leader portraits, localisation, opening decision mechanics, event spawn effects, evolution-log entries, and runtime focus trees: `CFR` has its 45-focus Construction Directorate tree, `MFR` has its 37-focus Arsenal Board tree, `OGB` has its 32-focus Volga Bulgar Restoration tree, and `ICD`, `KRS`, `FTH`, `BBH`, `BSC`, `TNC`, `ALA`, `UDC`, `SDZ`, `RMC`, `RCD`, `ILU`, `PRA`, `TSC`, `BLT`, `NRF`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `TRS`, `NLC`, `SEP`, `DSC`, `COU`, `BEC`, `RLD`, `LID`, and `IRA` use 20- or 21-focus custom splinter trees after duplicate pruning.

At high chaos, the Soviet opening hook can create the implemented successor states without using any recurring on-action loop. Each spawn is gated by `is_soviet_collapse_high_chaos_successor_spawn_ready`, which requires the Soviet Collapse to be active for `SOV` and either chaos tier 4, chaos tier 5, or `soviet_collapse_evolution_weirdness` reaching `constant:soviet_collapse_high_chaos_event_log.spawn_weirdness_gate`. Each successor also respects the evolution disable UI by checking `is_current_evolution_enabled` for its own high-chaos stage before any state transfer happens.

The exact opening state packages are:

1. `CFR` receives Yaroslavl (`248`) and Ivanovo (`253`) if both are owned and controlled by `SOV`.
2. `MFR` receives Nizhny Novgorod (`252`) and Samara (`251`) if both are owned and controlled by `SOV`.
3. `OGB` receives Kazan (`249`) and Volga Germany (`829`) if both are owned and controlled by `SOV`.
4. `ICD` receives Northern Urals (`581`) and Southern Urals (`582`) if both are owned and controlled by `SOV` and the grave-census containment mission fails into a dead-state route.
5. `KRS` receives Leningrad Area (`195`) if it is owned and controlled by `SOV` and the sailor assembly or northern fleet signal route fails into a naval council route.
6. `FTH` receives Zaporozhe (`200`) and Dnipropetrovsk (`226`) if both are owned and controlled by `SOV`, Huliaipole containment fails, and old-movement pressure has not yet crossed the Black Banner threshold.
7. `BBH` receives Zaporozhe (`200`) and Dnipropetrovsk (`226`) if they are owned and controlled by `SOV`, Huliaipole containment fails, and old-movement pressure has reached the Black Banner threshold. Stalino (`227`) is added when the same ownership and control conditions hold there as well.
8. `BSC` receives Atyrau (`405`), Turkmenistan (`584`), and Stalinabad (`742`) if all three are owned and controlled by `SOV` and the Basmachi supply-chain mission fails.
9. `TNC` receives Uzbekistan (`585`) if it is owned and controlled by `SOV` and the Tashkent anchor mission fails. Kyrgyzstan (`586`) is added when the same ownership and control conditions hold there as well.
10. `ALA` receives Kazakhstan (`583`) and Western Kazakhstan (`587`) if both are owned and controlled by `SOV`, Kazakhstan has not already appeared, and the Kazakhstan-first-wave mission fails. Some Mountains (`588`) is added when the same ownership and control conditions hold there as well.
11. `UDC` receives Tula (`223`), Kursk Area (`220`), and Voronezh (`240`) if all three are owned and controlled by `SOV` and the loyal military districts mission fails.
12. `SDZ` receives Yaroslavl (`248`) and Vologda (`351`) if both are owned and controlled by `SOV` and the union archives mission fails.
13. `RMC` receives Stalingrad Area (`217`) and Borisoglbsk (`260`) if both are owned and controlled by `SOV` and the grave registers mission fails.
14. `RCD` receives Novosibirsk (`570`) and Krasnoyarsk (`568`) if both are owned and controlled by `SOV` and the wrong resurrection committee mission fails.
15. `ILU` receives Sverdlovsk (`653`) and Chelyabinsk (`572`) if both are owned and controlled by `SOV` and the Ural factory gates mission fails.
16. `PRA` receives Smolensk (`242`) and Pochep (`241`) if both are owned and controlled by `SOV` and the funeral train schedule mission fails.
17. `TSC` receives Irkutsk (`566`) and Omsk (`571`) if both are owned and controlled by `SOV` and the star-iron rumor mission fails.
18. `BLT` receives Vologda (`351`) and Kirov (`400`) if both are owned and controlled by `SOV` and the crown archive mission fails.
19. `NRF` receives Murmansk (`213`) and Arkhangelsk (`214`) if both are owned and controlled by `SOV` and the northern fleet signals mission fails.
20. `GAC` receives Orel (`222`) and Bryansk (`224`) if both are owned and controlled by `SOV` and the peasant-anger mission fails.
21. `DHC` receives Rostov Area (`218`) and Volgodonsk (`238`) if both are owned and controlled by `SOV` and the village-negotiation mission fails.
22. `KHC` receives Krasnodar (`234`) and Stavropol (`235`) if both are owned and controlled by `SOV` and the Caucasus mountain administration mission fails.
23. `FEV` receives Vladivostok (`408`) and Khabarovsk (`409`) if both are owned and controlled by `SOV` and the Vladivostok central-command mission fails.
24. `SZA` receives Tomsk (`578`) and Tobolsk (`580`) if both are owned and controlled by `SOV` and the Siberian distance command mission fails.
25. `UWD` receives Southern Urals (`582`) and Northern Urals (`581`) if both are owned and controlled by `SOV` and the Ural factory gates mission fails.
26. `MRC` receives Dagestan (`232`), Chechnya-Ingushetia (`821`), Kabardino-Balkaria (`827`), and North Ossetia (`828`) if all are owned and controlled by `SOV` and the Caucasus mountain administration mission fails.
27. `IUL` receives Ufa (`651`) and Ulyanovsk (`250`) if both are owned and controlled by `SOV` and the Volga names mission fails.
28. `BAC` receives Birobidzhan (`657`) and Amur (`561`) if both are owned and controlled by `SOV` and the Vladivostok central-command mission fails.
29. `ARD` receives Murmansk (`213`) and Arkhangelsk (`214`) if both are owned and controlled by `SOV` and the northern port directorate mission fails.
30. `TRS` receives Moscow Area (`219`) and Ryazan (`254`) if both are owned and controlled by `SOV` and the religious command war-room mission fails.
31. `NLC` receives Below Zero (`216`) and Nenetsia (`825`) if both are owned and controlled by `SOV` and the northern fleet signals mission fails.
32. `SEP` receives Borisoglbsk (`260`) and Saratov (`239`) if both are owned and controlled by `SOV` and the living grave census mission fails.
33. `DSC` receives Kursk Area (`220`) and Orel (`222`) if both are owned and controlled by `SOV` and the living grave census mission fails.
34. `COU` receives Pochep (`241`) and Bryansk (`224`) if both are owned and controlled by `SOV` and the funeral train schedule mission fails.
35. `BEC` receives Voronezh (`240`) and Tula (`223`) if both are owned and controlled by `SOV` and the grave registers mission fails.
36. `RLD` receives Ryazan (`254`) and Tula (`223`) if both are owned and controlled by `SOV` and the wrong resurrection committee mission fails.
37. `LID` receives Stalingrad Area (`217`) and Volgodonsk (`238`) if both are owned and controlled by `SOV` and the living grave census mission fails.
38. `IRA` receives Chelyabinsk (`572`) and Ts 15 (`573`) if both are owned and controlled by `SOV` and the Ural factory gates mission fails.

These are strict prerequisites, not contingency pools. If a required state has already left Soviet ownership or control, that successor is not created by the opening hook. A created high-chaos successor receives the normal breakaway support package, its tag-specific opening ideas, its tag-specific runtime focus tree with a clean focus state, and an event notice in `events/005_soviet_collapse_factory_ancient.txt` or `events/005_soviet_collapse_custom.txt`. The first eligible successor in each high-chaos tier records an actor-linked evolution-log entry under `Soviet Collapse: High-Chaos Aberrations`; later successor notices in the same tier remain normal reports so the crisis does not flood the evolution log.

Each tag also has an opening decision board:

1. `CFR` uses `The Reconstruction State` with `Construction Mandates`, `Survey the Unfinished Sites`, and `Issue Reconstruction Contracts`.
2. `MFR` uses `The Arsenal State` with `Arsenal Quotas`, `Audit Arsenal Orders`, and `Convert Depots to Arms Lines`.
3. `OGB` uses `The Volga Restoration` with `Volga Legitimacy`, `Claim the Volga Crossings`, and `Convene Bolghar Scholars`.
4. `ICD` uses `Iron Commissariat` with dead-roll consolidation, death-guard mobilisation, and the Iron Afterlife endgame.
5. `KRS` uses `Kronstadt Council` with council consolidation, sailor-guard mobilisation, and the Every Port a Council endgame.
6. `FTH` uses `Free Territory` with commune consolidation, free-soviet mobilisation, and the World Without Capitals endgame.
7. `BBH` uses `Black Banner Host` with war-council consolidation, black-column mobilisation, and the World Without Prisons endgame.
8. `BSC` uses `Basmachi Confederation` with oasis consolidation, pass-guard mobilisation, and the Road Beyond the Steppe endgame.
9. `TNC` uses `Turkestan National Council` with civic consolidation, railway-guard mobilisation, and the New Turkestan endgame.
10. `ALA` uses `Alash Restoration Authority` with congress consolidation, cavalry-guard mobilisation, and the National Modernization Mandate endgame.
11. `UDC` uses `Union Defense Committee` with command consolidation, signature-force mobilisation, and the Provisional Soviet Command endgame.
12. `SDZ` uses `Security Directorate Zone` with archive consolidation, signature-force mobilisation, and the World in One Archive endgame.
13. `RMC` uses `Red Martyrs' Resurrection Cult` with register consolidation, signature-force mobilisation, and the Every Grave a Barracks endgame.
14. `RCD` uses `Red Cosmist Directorate` with common-task consolidation, signature-force mobilisation, and the No Grave Outside the State endgame.
15. `ILU` uses `Iron Liturgy of the Urals` with furnace consolidation, signature-force mobilisation, and the World as One Factory endgame.
16. `PRA` uses `Pale Railway Authority` with timetable consolidation, signature-force mobilisation, and the Every Junction Under Authority endgame.
17. `TSC` uses `Tunguska Star Committee` with expedition consolidation, signature-force mobilisation, and the Bring the Fire West endgame.
18. `BLT` uses `Brotherhood of the Last Tsar` with brotherhood consolidation, signature-force mobilisation, and the Universal Throne endgame.
19. `NRF` uses `Northern Revenant Fleet` with fleet-watch consolidation, signature-force mobilisation, and the Every Coast a Northern Port endgame.
20. `GAC` uses `Green Army Congress` with village-congress consolidation, signature-force mobilisation, and the Land and Bread Against the World endgame.
21. `DHC` uses `Don Host Emergency Circle` with host-circle consolidation, signature-force mobilisation, and the Southern Host Command endgame.
22. `KHC` uses `Kuban Host Provisional Council` with crossing-council consolidation, signature-force mobilisation, and the Kuban Line Command endgame.
23. `FEV` uses `Far Eastern Republic Revival` with buffer-committee consolidation, railway-guard mobilisation, and the Far Eastern Line Command endgame.
24. `SZA` uses `Siberian Zemstvo Authority` with zemstvo consolidation, city-guard mobilisation, and the Siberian Depth Command endgame.
25. `UWD` uses `Ural Workers' Directorate` with factory-committee consolidation, worker-battalion mobilisation, and the Arsenal Autonomy endgame.
26. `MRC` uses `Mountain Republic of the Caucasus` with elder-council consolidation, pass-guard mobilisation, and the Mountain Republic Mandate endgame.
27. `IUL` uses `Idel-Ural League` with corridor-office consolidation, river-guard mobilisation, and the Federal Corridor Authority endgame.
28. `BAC` uses `Birobidzhan Autonomous Commune` with settlement-committee consolidation, militia mobilisation, and the Autonomous Commune Mandate endgame.
29. `ARD` uses `Arctic Naval Directorate` with port-directorate consolidation, naval-guard mobilisation, and the Port Neutrality Mandate endgame.
30. `TRS` uses `Third Rome Emergency Synod` with synod consolidation, guard mobilisation, and the Fourth Testament of Moscow endgame.
31. `NLC` uses `Northern Lights Commune` with polar-commune consolidation, survival-unit mobilisation, and the World After Capitals endgame.
32. `SEP` uses `Sepulchre Soviet` with burial-committee consolidation, cemetery-guard mobilisation, and the World Cemetery Mandate endgame.
33. `DSC` uses `Dead Soldiers' Congress` with veterans' congress consolidation, fallen-regiment mobilisation, and the Army of the Fallen endgame.
34. `COU` uses `Commissariat of the Unburied` with claim consolidation, signature-force mobilisation, and the No Burial Without the State endgame.
35. `BEC` uses `Black Earth Resurrection Cult` with claim consolidation, signature-force mobilisation, and the Every Field a Grave endgame.
36. `RLD` uses `Red Lazarus Directorate` with claim consolidation, signature-force mobilisation, and the Return Is Mandatory endgame.
37. `LID` uses `Last International of the Dead` with claim consolidation, signature-force mobilisation, and the All Dead Are Comrades endgame.
38. `IRA` uses `Iron Resurrection Army` with claim consolidation, signature-force mobilisation, and the Army That Returns endgame.

These decision boards are deliberately small foundations. They provide the variables, costs, blocked-cost localisation, ideas, and first rewards for tag-specific focus trees and event spawn effects.

## Intervention Decisions

Breakaway republics have a small playable emergency board:

1. `soviet_collapse_request_foreign_recognition`
2. `soviet_collapse_mobilize_defense_units`
3. `soviet_collapse_seize_depots`
4. `soviet_collapse_coordinate_fronts`

These actions use stability, army experience, fuel, and support equipment instead of a generic political-power default. They build recognition progress, depot control, defensive ideas, emergency units, republican recovery progress, and Soviet crisis pressure. A newly released republic starts with `soviet_collapse_republican_startup_disorder`; repeated decisions and focuses remove it and add `soviet_collapse_emergency_administration_stabilized`.

Major foreign patron candidates that are hostile to Moscow can target entries from `global.soviet_collapse_breakaway_countries` with:

1. `soviet_collapse_recognize_breakaway_government`
2. `soviet_collapse_fund_ideological_liaison_offices`
3. `soviet_collapse_ship_border_armaments`
4. `soviet_collapse_dispatch_military_advisers`
5. `soviet_collapse_open_republican_intelligence_channel`
6. `soviet_collapse_sponsor_volunteer_corps`
7. `soviet_collapse_negotiate_republican_trade_mission`

The targeted decision scope follows the vanilla `target_array` pattern: the patron remains `ROOT`, and the chosen breakaway is `FROM`. The aid costs use stability, war support, equipment, army experience, manpower, trains, convoys, and higher fuel thresholds. Effects raise breakaway recognition or military capacity while feeding Soviet `Foreign Penetration`, `Depot Vulnerability`, `League Cohesion`, `Moscow Authority`, or `Armed Breakaway Momentum` as appropriate.

## Soviet Objective Board

The Soviet category currently activates these opening goal-style missions:

1. `soviet_collapse_soviet_mission_001_confirm_the_emergency_chain_of_command`
2. `soviet_collapse_soviet_mission_002_seal_the_first_circular`
3. `soviet_collapse_soviet_mission_003_guard_the_peoples_commissariats`
4. `soviet_collapse_soviet_mission_004_establish_the_crisis_desk`
5. `soviet_collapse_soviet_mission_005_count_the_missing_trains`
6. `soviet_collapse_soviet_mission_006_freeze_unapproved_transfers`
7. `soviet_collapse_soviet_mission_007_order_the_border_posts_to_report_twice`
8. `soviet_collapse_soviet_mission_008_audit_the_republic_radios`
9. `soviet_collapse_soviet_mission_009_open_the_loyalist_courier_line`
10. `soviet_collapse_soviet_mission_010_protect_the_first_reclamation_staging_area`
11. `soviet_collapse_soviet_mission_011_announce_the_legal_continuity_decree`
12. `soviet_collapse_soviet_mission_012_convene_loyal_republican_deputies`
13. `soviet_collapse_soviet_mission_013_publish_the_union_guarantee`
14. `soviet_collapse_soviet_mission_014_register_emergency_autonomy_charters`
15. `soviet_collapse_soviet_mission_015_use_the_supreme_soviet_as_a_shield`
16. `soviet_collapse_soviet_mission_016_certify_loyal_military_districts`
17. `soviet_collapse_soviet_mission_017_restore_the_central_supply_seal`
18. `soviet_collapse_soviet_mission_018_send_the_quiet_governors`
19. `soviet_collapse_soviet_mission_019_prepare_the_reduced_union_formula`
20. `soviet_collapse_soviet_mission_020_declare_the_union_treaty_valid_until_rewritten`
21. `soviet_collapse_soviet_mission_021_prove_one_republic_can_be_recovered`
22. `soviet_collapse_soviet_mission_022_keep_the_second_republic_quiet`
23. `soviet_collapse_soviet_mission_023_rebuild_a_provincial_party_office`
24. `soviet_collapse_soviet_mission_024_assign_the_emergency_procurators`
25. `soviet_collapse_soviet_mission_025_hold_the_capital_district_parade`
26. `soviet_collapse_soviet_mission_026_repair_the_western_telegraph_offices`
27. `soviet_collapse_soviet_mission_027_secure_the_grain_accounting_files`
28. `soviet_collapse_soviet_mission_028_demand_the_governors_oaths`
29. `soviet_collapse_soviet_mission_029_guard_the_union_archives`
30. `soviet_collapse_soviet_mission_030_stabilize_the_first_negotiated_corridor`
31. `soviet_collapse_soviet_mission_031_move_the_government_files_east`
32. `soviet_collapse_soviet_mission_032_declare_emergency_regional_commands`
33. `soviet_collapse_soviet_mission_033_hold_the_inner_ring`
34. `soviet_collapse_soviet_mission_034_secure_the_last_loyal_rail_spine`
35. `soviet_collapse_soviet_mission_035_buy_time_with_local_militias`
36. `soviet_collapse_soviet_mission_036_offer_amnesty_to_the_second_line`
37. `soviet_collapse_soviet_mission_037_break_the_leagues_first_calendar`
38. `soviet_collapse_soviet_mission_038_publicly_recover_a_lost_depot`
39. `soviet_collapse_soviet_mission_039_keep_the_officers_from_choosing_russia_alone`
40. `soviet_collapse_soviet_mission_040_prepare_the_rump_state_without_admitting_it`
41. `soviet_collapse_soviet_mission_041_deny_the_first_victory_parade`
42. `soviet_collapse_soviet_mission_042_cut_the_republics_shared_road`
43. `soviet_collapse_soviet_mission_043_prove_the_depots_can_be_retaken`
44. `soviet_collapse_soviet_mission_044_stop_the_volunteer_review`
45. `soviet_collapse_soviet_mission_045_discredit_the_first_republic_army`
46. `soviet_collapse_soviet_mission_046_break_the_defense_committees_supply`
47. `soviet_collapse_soviet_mission_047_keep_the_next_declaration_unarmed`
48. `soviet_collapse_soviet_mission_048_force_the_league_to_choose_a_front`
49. `soviet_collapse_soviet_mission_049_capture_the_emergency_printing_office`
50. `soviet_collapse_soviet_mission_050_deny_the_first_foreign_mission_photo`
51. `soviet_collapse_soviet_mission_051_reassign_the_local_born_commanders`
52. `soviet_collapse_soviet_mission_052_reward_the_units_that_moved`
53. `soviet_collapse_soviet_mission_053_send_political_officers_to_the_rail_junctions`
54. `soviet_collapse_soviet_mission_054_secure_the_signal_school`
55. `soviet_collapse_soviet_mission_055_audit_the_navys_oath`
56. `soviet_collapse_soviet_mission_056_gather_the_armored_train_crews`
57. `soviet_collapse_soviet_mission_057_stop_the_officers_private_conference`
58. `soviet_collapse_soviet_mission_058_keep_the_guards_divisions_apolitical`
59. `soviet_collapse_soviet_mission_059_escort_the_commissars_safely`
60. `soviet_collapse_soviet_mission_060_reopen_the_district_war_rooms`
61. `soviet_collapse_soviet_mission_061_seal_the_smolensk_ledger`
62. `soviet_collapse_soviet_mission_062_recount_the_ukrainian_depots`
63. `soviet_collapse_soviet_mission_063_guard_the_belarusian_rail_net`
64. `soviet_collapse_soviet_mission_064_prevent_baltic_port_transfers`
65. `soviet_collapse_soviet_mission_065_secure_caucasus_oil_accounting`
66. `soviet_collapse_soviet_mission_066_lock_the_ural_factory_gates`
67. `soviet_collapse_soviet_mission_067_inspect_the_siberian_storehouses`
68. `soviet_collapse_soviet_mission_068_move_the_fuel_before_the_flags_change`
69. `soviet_collapse_soviet_mission_069_guard_the_ammunition_census`
70. `soviet_collapse_soviet_mission_070_reopen_the_northern_port_books`
71. `soviet_collapse_soviet_mission_071_close_the_unofficial_consulates`
72. `soviet_collapse_soviet_mission_072_guard_the_polish_and_romanian_corridors`
73. `soviet_collapse_soviet_mission_073_watch_the_finnish_border_roads`
74. `soviet_collapse_soviet_mission_074_shadow_the_turkish_mission`
75. `soviet_collapse_soviet_mission_075_seal_the_iranian_road`
76. `soviet_collapse_soviet_mission_076_track_the_japanese_liaison_train`
77. `soviet_collapse_soviet_mission_077_expose_the_sponsors_price`
78. `soviet_collapse_soviet_mission_078_offer_safe_neutral_observation`
79. `soviet_collapse_soviet_mission_079_cut_the_radio_link_abroad`
80. `soviet_collapse_soviet_mission_080_keep_humanitarian_aid_from_becoming_arms`
81. `soviet_collapse_soviet_mission_081_separate_peasant_anger_from_separatism`
82. `soviet_collapse_soviet_mission_082_reopen_the_civil_war_files`
83. `soviet_collapse_soviet_mission_083_keep_huliaipole_quiet`
84. `soviet_collapse_soviet_mission_084_negotiate_with_the_villages_before_the_league_does`
85. `soviet_collapse_soviet_mission_085_guard_the_monasteries_and_mosques_from_politics`
86. `soviet_collapse_soviet_mission_086_break_the_basmachi_supply_chain`
87. `soviet_collapse_soviet_mission_087_quiet_the_volga_names`
88. `soviet_collapse_soviet_mission_088_prevent_the_factory_committees_from_writing_law`
89. `soviet_collapse_soviet_mission_089_stop_the_sailor_assembly_before_it_votes`
90. `soviet_collapse_soviet_mission_090_contain_the_grave_registers`
91. `soviet_collapse_soviet_mission_091_western_gate_discipline`
92. `soviet_collapse_soviet_mission_092_baltic_legal_counterclaim`
93. `soviet_collapse_soviet_mission_093_caucasus_mountain_administration`
94. `soviet_collapse_soviet_mission_094_the_tashkent_anchor`
95. `soviet_collapse_soviet_mission_095_dushanbe_pass_watch`
96. `soviet_collapse_soviet_mission_096_ashgabat_border_screen`
97. `soviet_collapse_soviet_mission_097_bishkek_and_the_mountain_signals`
98. `soviet_collapse_soviet_mission_098_kazakhstan_must_not_be_first`
99. `soviet_collapse_soviet_mission_099_siberian_distance_command`
100. `soviet_collapse_soviet_mission_100_vladivostok_does_not_negotiate_alone`
101. `soviet_collapse_soviet_mission_101_deny_the_league_founding_quorum`
102. `soviet_collapse_soviet_mission_102_split_the_league_between_west_and_south`
103. `soviet_collapse_soviet_mission_103_offer_one_republic_a_separate_exit`
104. `soviet_collapse_soviet_mission_104_break_the_shared_defense_calendar`
105. `soviet_collapse_soviet_mission_105_discredit_the_leagues_foreign_envoys`
106. `soviet_collapse_soviet_mission_106_prove_the_league_cannot_protect_depots`
107. `soviet_collapse_soviet_mission_107_keep_loyalists_alive_behind_the_league`
108. `soviet_collapse_soviet_mission_108_force_a_league_border_dispute`
109. `soviet_collapse_soviet_mission_109_classify_the_impossible_reports`
110. `soviet_collapse_soviet_mission_110_guard_the_hospitals_from_politics`
111. `soviet_collapse_soviet_mission_111_keep_the_factory_whistles_ordinary`
112. `soviet_collapse_soviet_mission_112_deny_the_star_iron_rumor`
113. `soviet_collapse_soviet_mission_113_break_the_funeral_train_schedule`
114. `soviet_collapse_soviet_mission_114_prevent_the_crown_from_leaving_the_archive`
115. `soviet_collapse_soviet_mission_115_silence_the_wrong_resurrection_committee`
116. `soviet_collapse_soviet_mission_116_seal_the_northern_fleet_signals`
117. `soviet_collapse_soviet_mission_117_keep_the_priests_out_of_the_war_room`
118. `soviet_collapse_soviet_mission_118_order_the_graves_counted_by_the_living`
119. `soviet_collapse_soviet_mission_119_publish_the_first_restored_budget`
120. `soviet_collapse_soviet_mission_120_reopen_the_schools_without_soldiers`
121. `soviet_collapse_soviet_mission_121_return_the_local_units_to_barracks`
122. `soviet_collapse_soviet_mission_122_confirm_the_new_union_budget`
123. `soviet_collapse_soviet_mission_123_seal_the_last_recognition_file`
124. `soviet_collapse_soviet_mission_124_record_the_crisis_as_temporary_disorder`
125. `soviet_collapse_soviet_mission_125_admit_the_union_was_rewritten`
126. `soviet_collapse_soviet_mission_126_retire_the_emergency_commands`
127. `soviet_collapse_soviet_mission_127_inventory_the_recovered_depots`
128. `soviet_collapse_soviet_mission_128_disband_the_crisis_desk`

The activation effect counts active missions before activating the next one and stops at `constant:soviet_collapse_soviet_objective.active_cap`, currently 10. Mission deadlines vary by objective family: local administrative goals use 95 to 110 days, short operational goals use 120 days, regional and rail goals use 150 to 165 days, republic-legitimacy and foreign-pressure goals use 180 to 210 days, League and high-chaos containment goals use 240 to 270 days, and terminal containment goals use 365 days. This keeps early failures from cascading during the first month while giving large rail, League, foreign, and high-chaos objectives the longer operational windows required by the correction spec. The missions use equipment, manpower, fuel, trains, stability, war support, army experience, and command power as requirements or costs; political power is not the default cost. Successful troop-placement missions can set `soviet_collapse_loyal_units_moved`, which mission 52 consumes and clears. Mission 60 can set `soviet_collapse_district_war_rooms_reopened` for later reclamation logic.

Mission outcomes use family-specific crisis pressure helpers tuned through `constant:soviet_collapse_objective_pressure`. Authority, legal, command, rail, depot, old-movement, foreign, cleanup, and settlement objectives no longer share the same flat success and failure effects; each family adjusts the relevant Union Crisis Threat components and then recalculates the total threat. A SOV-only delayed check now uses `mtth:soviet_collapse_progressive_release_weight` and `mtth:soviet_collapse_progressive_release_miss_weight` from `common/mtth/005_soviet_collapse_mtth.txt` to decide whether a new eligible republic breaks away. The MTTH variables respond to Union Collapse Threat, Moscow Authority, Command Obedience, active breakaway count, regional cascade signals, depot vulnerability, foreign penetration, League cohesion, old-movement resurgence, failed Soviet mission flags, war pressure, and chaos tier. If a release fires, the visible cause event is selected from ministry refusal, rail-office seal change, border-guard defection, local party sovereignty, foreign liaison acceleration, depot commander oath, old-movement pressure, or League envoy coordination. At 100 threat, Union Unmade fires immediately, releasing every ordinary republic still under Moscow control and all eligible terminal special successors.

Failed Soviet objective families also trigger short report events in `events/005_soviet_collapse.txt`: authority (`chaosx.nr5.10`), command (`chaosx.nr5.11`), rail (`chaosx.nr5.12`), depot (`chaosx.nr5.13`), foreign exposure (`chaosx.nr5.14`), cleanup/backlog (`chaosx.nr5.15`), and settlement (`chaosx.nr5.16`). These are normal crisis reports, not evolution logs.

The main crisis decision AI weights react to the same crisis state. Soviet responses prefer authority restoration, loyalist officers, supply-route action, or reserve mobilization based on Moscow Authority, Military Obedience, Depot Vulnerability, Foreign Penetration, League coordination, active war, and Union Crisis Threat. Breakaway actions prefer recognition, mobilization, depot seizure, or front coordination based on Soviet weakness, war with Moscow, faction membership, League coordination, and chaos tier. Foreign patron actions prefer recognition, liaison, arms, advisers, intelligence, volunteers, or trade based on Soviet authority, foreign penetration, military obedience, depot vulnerability, war with Moscow, total threat, and League coordination.

## Icon Wiring

This slice reuses existing wired sprites. No new art was generated.

- Ideas use `GFX_idea_union_crisis`, `GFX_idea_emergency_union_authority`, `GFX_idea_new_union_negotiations`, `GFX_idea_union_restored`, `GFX_idea_loyalist_officer_corps`, `GFX_idea_captured_soviet_depots`, and `GFX_idea_defensive_coordination` from `interface/005_soviet_collapse_icons.gfx`.
- Decision categories use `GFX_decision_category_soviet_collapse_soviet`, `GFX_decision_category_soviet_collapse_breakaway`, `GFX_decision_category_soviet_collapse_foreign_patron`, and `GFX_decision_category_soviet_collapse_regional_faction`.
- Soviet responses use `GFX_decision_restore_party_control`, `GFX_decision_send_loyalist_officers`, `GFX_decision_cut_rebel_supply_routes`, and `GFX_decision_emergency_mobilization`.
- Breakaway actions use `GFX_decision_request_foreign_recognition`, `GFX_decision_mobilize_defense_units`, `GFX_decision_seize_depots`, and `GFX_decision_coordinate_fronts`.
- Foreign patron actions use `GFX_decision_soviet_collapse_foreign_recognition`, `GFX_decision_soviet_collapse_foreign_armaments`, `GFX_decision_soviet_collapse_foreign_advisers`, `GFX_decision_soviet_collapse_foreign_intelligence`, `GFX_decision_soviet_collapse_foreign_volunteers`, and `GFX_decision_soviet_collapse_foreign_trade`.
- The intervention and focus country spirits use `GFX_idea_popular_defense_committees`, `GFX_idea_foreign_volunteers`, `GFX_idea_legal_restoration_claim`, `GFX_idea_socialist_sovereignty`, `GFX_idea_military_defense_council`, and `GFX_idea_old_underground_networks`.
- Soviet objectives use the shared goal sprites in `interface/005_soviet_collapse_icons.gfx`, including `GFX_decision_soviet_collapse_authority_goal`, `GFX_decision_soviet_collapse_command_goal`, `GFX_decision_soviet_collapse_rail_goal`, `GFX_decision_soviet_collapse_depot_goal`, `GFX_decision_soviet_collapse_old_movement_goal`, `GFX_decision_soviet_collapse_border_goal`, `GFX_decision_soviet_collapse_foreign_goal`, and `GFX_decision_soviet_collapse_cleanup_goal`.
- The visible opening event uses `GFX_report_union_crisis`; the news event uses `GFX_news_soviet_union_collapse`.
- Progressive MTTH release events `chaosx.nr5.130` through `chaosx.nr5.137` reuse `GFX_report_union_crisis`; no new report art is required.
- Republic focus trees use existing sprites from `interface/005_soviet_collapse_icons.gfx`, `interface/005_soviet_collapse_ukraine_icons.gfx`, `interface/005_soviet_collapse_blr_icons.gfx`, `interface/005_soviet_collapse_kaz_icons.gfx`, and `interface/005_soviet_collapse_regional_icons.gfx`. No additional focus sprite filenames are required for this slice.
- `CFR_soviet_collapse_focus_tree` reuses the existing 33 Civilian Factory focus sprites in `interface/005_soviet_collapse_factory_ancient_icons.gfx` across 58 focuses. No new CFR focus art is required for this slice.
- `MFR_soviet_collapse_focus_tree` reuses the existing 46 Military Factory focus sprites in `interface/005_soviet_collapse_factory_ancient_icons.gfx` across 46 focuses. No new MFR focus art is required for this slice.
- `OGB_soviet_collapse_focus_tree` reuses the existing 54 Old Great Bulgaria focus sprites in `interface/005_soviet_collapse_factory_ancient_icons.gfx` across 54 focuses. No new OGB focus art is required for this slice.
- `ICD`, `KRS`, `FTH`, `BBH`, `BSC`, `TNC`, `ALA`, `UDC`, `SDZ`, `RMC`, `RCD`, `ILU`, `PRA`, `TSC`, `BLT`, `NRF`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `TRS`, `NLC`, `SEP`, `DSC`, `COU`, `BEC`, `RLD`, `LID`, and `IRA` custom-splinter focus trees reuse the 24 existing per-tag `GFX_focus_TAG_*` sprites in `interface/005_soviet_collapse_custom_icons.gfx`. No new custom-splinter focus art is required for this slice.
- High-chaos tag foundations use flag assets under `gfx/flags/`, leader portraits under `gfx/leaders/005_soviet_collapse/`, and portrait sprite keys in `interface/005_soviet_collapse_factory_ancient_icons.gfx` or `interface/005_soviet_collapse_custom_icons.gfx`. The high-chaos notice events currently reuse `GFX_report_union_crisis`, so no new report sprite is required for this slice.
- Event 005 custom country flags were audited for the 38 custom tags across base, communism, democratic, fascism, and neutrality variants in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`. All 570 TGA files exist, all use top-origin TGA headers after the vertical asset correction, and every medium or small variant matches its large source orientation more closely than a vertically flipped source. No historical or existing custom flags were regenerated during this audit.
- Event 005 achievements use `common/achievements/chaos_redux_achievements.txt`, localisation in `localisation/english/chaosx_achievements_l_english.yml`, sprites in `interface/chaosx_achievements.gfx`, and the icon ledger in `docs/assets/005_soviet_union_collapse/achievement_icon_manifest.md`.

## Future Plans

- Expand the Soviet objective board beyond the first one hundred twenty-eight missions while preserving the ten-active cap.
- Expand breakaway missions, foreign intervention missions, regional faction categories, and action-based foreign aid routes beyond the first playable board.
- Continue deepening longer event chains and route-specific follow-up content for implemented custom countries where the clean specification calls for more than the current foundational country, decision, spawn, and focus package.
- Extend remaining route-specific super-event triggers, future-only achievement completion flags, and evolution logs only where the clean specification allows them.
- Audit existing Soviet Collapse evolution localisation so ordinary crisis stages are not presented as evolutions.
