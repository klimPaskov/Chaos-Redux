# Event 005 - Soviet Union Collapse

## Overview

Soviet Union Collapse is a one-per-campaign Liberations cluster event that turns the old stub release into an active union crisis. The entry event remains `chaosx.nr5.1`; it now routes to the visible Soviet event `chaosx.nr5.2`, which initializes the crisis, releases the first breakaway republics, grants them defensive support, and activates the opening Soviet objective board.

The baseline crisis stages are ordinary crisis progression, not evolution logs. Evolutions remain reserved for separate mutation tracks such as old movements, depot states, railway authorities, foreign liaison networks, and high-chaos splinters.

The Event Logs event-detail entry for Event 005 now uses scripted localisation to show the live broad crisis state, first-wave status, Free Republics' League status, Moscow Authority condition, Union Crisis Threat severity, foreign intervention level, and old-movement or high-chaos splinter pressure. The text stays in-world and reads the same crisis variables and flags that drive the gameplay board instead of using debug-style implementation notes.

## Current Implementation

The implemented opening slices cover the crisis scaffold and the first intervention layer:

- `common/script_constants/005_soviet_collapse_constants.txt` centralizes opening crisis values, breakaway support, future declaration support adjustments, objective requirements, objective pressure families, and first response costs.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt` adds the active-crisis, breakaway, patron, cost, republic-release, local-league, objective-requirement, terminal-cleanup, and event-created country triggers used by the current Event 005 script surface.
- `common/scripted_effects/005_soviet_collapse_effects.txt` initializes the crisis meter, clamps and recalculates total threat, releases the opening breakaways, gives starting forces, applies recoverable republican startup disorder, runs progressive threat-based breakaway checks, and enforces the Soviet objective cap.
- `common/ideas/005_soviet_collapse_ideas.txt` adds country spirits for the union crisis, Moscow response routes, the restored union recovery, loyalist officers, recoverable republican disorder, and consolidated staged republic support.
- Soviet Collapse spirits use file-local tuning packages because idea modifier blocks do not parse shared script constants. The core spirits are meant to change play through combined legitimacy, mobilization, command, supply, depot, defensive, manpower, production, and foreign-cohesion effects rather than isolated tiny percentages.
- `common/decisions/005_soviet_collapse_decisions.txt` adds four non-political-power Soviet response decisions, one hundred twenty-eight opening goal-style missions, four breakaway emergency actions, and seventeen targeted foreign patron decisions.
- `events/005_soviet_collapse.txt` replaces the old hidden release stub with a visible opening event and four posture choices.
- `events/005_soviet_collapse_factory_ancient.txt` adds the triggered notices for the first high-chaos factory and Volga successor states.

## Foreign Influence Tracking

Foreign patron decisions build permanent pressure on the target republic instead of only granting one-off aid. Each targeted intervention records both a category total and a sponsor total on the republic:

- category totals: recognition, arms, volunteers, advisers, industry, intelligence, ideology, logistics, and patronage risk
- sponsor totals: Germany, Britain, Japan, France, the United States, Turkey, Iran, Poland, Romania, Finland, Sweden, and Italy

Foreign influence now feeds one consolidated staged `External Support` republic spirit rather than a stack of separate diplomatic, volunteer, adviser, and reconstruction spirits. Category totals and sponsor totals still drive acceptance, dependency, sponsor balance, and pressure effects, but the visible republic idea surface stays compact: outside support grows stronger as total influence rises and active sponsor count is weighted heavily enough for broad backing to matter. Balanced support still improves independence resilience and reduces patronage risk, while one-sided dominance still increases dependency pressure.

The foreign patron category covers the first full investment set: recognition, ideological liaison, equipment convoys, military advisers, intelligence channels, volunteer corps, trade missions, civilian construction, military construction, press and radio networks, aid corridors, republic conference sponsorship, League-mediated logistics aid, and an anti-puppet clause. Civilian construction adds a civilian factory and infrastructure to the target republic while applying a temporary consumer-goods and output burden to the sponsor. Military construction adds military industry and anti-air. Aid corridors open a target-side route flag for later support. Targeted aid and dependency steps require a real access route: war against Moscow, faction contact, a shared land border, a coastal convoy route, an opened aid corridor, or League conference access for a League member. They also pass a target-side acceptance gate: wartime pressure, weak stability or war support, rifle shortage, prior recognition, a trusted aid corridor, balanced sponsorship, low patronage risk, relief sponsorship, or League conference sponsorship can open the republic to aid, while a dominant sponsor lock, high patronage risk, direct client pressure, or strong League/faction protection can restrict direct patron missions. League-mediated logistics aid can target a Free Republics' League member through an existing route or a League aid channel, costs more negotiation and transport, improves League cohesion and independence resilience, and lowers patronage risk compared with direct patron corridors. Volunteer corps sponsorship requires a target-tier fielded army floor, transfers a sponsor field formation fraction to the republic, and spawns a republican field brigade in addition to the manpower and equipment package. Expanded patron action costs scale by target tier: regional republics and major republics require higher political, command, equipment, fuel, train, convoy, or stability commitments than ordinary breakaways, fuel-heavy target-tier costs make logistics, construction, intelligence, protection, and reintegration expensive enough to compete with other crisis spending, dependency-chain actions use the same target-tier scripted localisation as direct aid, and the decision cost text displays only the active icon-value costs for the selected target.

Foreign patron AI uses sponsor-style triggers instead of treating all patrons as interchangeable. Germany, Japan, Italy, Poland, Romania, and Finland bias toward arms, volunteers, officers, intelligence, and client pressure. Britain, the United States, France, and Sweden bias toward recognition, relief, reconstruction, conferences, and anti-puppet guarantees. Poland, Romania, Finland, Turkey, Iran, and Japan bias toward border corridors, while Turkey and Iran receive extra weight around Caucasus and Central Asian targets.

The anti-puppet clause is the first rival-contest decision. It raises `soviet_collapse_independence_resilience` and lowers `soviet_collapse_influence_patronage_risk`, giving puppet logic a resistance value that can come from balanced sponsorship instead of only raw strength.

Every foreign influence update now recalculates the target republic's active sponsor count, top sponsor, second sponsor, and sponsor gap. Two or three meaningful sponsors add one-time independence resilience and reduce patronage risk, while a large one-sponsor lead adds one-time patronage risk and lowers resilience. This lets broad sponsorship strengthen a republic without handing it to one patron, while a dominant sponsor makes the dependency chain easier only when the influence gap is truly one-sided.

## Reintegration And Dependency Pressure

Moscow now participates in the influence contest through two targeted Soviet decisions. `Offer a New Union Treaty` is available only while Union Crisis Threat is low or moderate, Moscow Authority is credible, the target is not at war with Moscow, and the target is not protected by a strong League or faction. The treaty spends political power, command power, fuel, and trains, then raises `soviet_collapse_influence_moscow`, lowers target patronage risk and independence resistance, and applies New Union Negotiations. `Offer a Federal Reintegration Compact` is the follow-up: it requires the treaty channel, dominant Moscow influence, lower threat, stronger Moscow Authority, a weak target, low patronage lock-in, and no League protection. It federates the target as a Soviet autonomous subject through `set_autonomy` instead of annexing it outright.

Foreign sponsors now use a three-step dependency chain rather than a simple puppet button. `Offer Protection Treaty` requires the sponsor to be the dominant influence holder on the target, the target to be weak, the target to have low independence resilience, and the target to lack strong League or faction protection. `Demand Adviser Privileges` requires the protection treaty and deepens volunteer influence and patronage risk. `Install Client Cabinet` requires adviser privileges and then sets the target as the sponsor's puppet. The chain is blocked while the republic is in a major war with Moscow, already a subject, or shielded by a strong League/faction, so a sponsor cannot bypass the independence-resilience and League-balancing systems.

Local leagues now operate as the regional layer below the Free Republics' League. The regional faction category exposes the Baltic League, Caucasus League, and Central Asian League founding decisions to eligible breakaways before they already have a faction flag. Founders recruit aligned partners, apply regional commitments, pick shared goals, settle tension, and can call a high-threat defensive war that clears the progressive release cooldown and checks the MTTH release scheduler. Kazakhstan remains locked out of the Central Asian League and progressive Central Asian pressure until at least three smaller Central Asian republics are free. Full notes live in `docs/events/005_soviet_union_collapse_local_leagues.md`.

No new icons are required for this slice. The consolidated staged republic spirits reuse existing idea pictures already registered by `interface/005_soviet_collapse_icons.gfx`: `emergency_union_authority`, `defensive_coordination`, `legal_restoration_claim`, and `old_underground_networks`.

## Crisis Meter

The Soviet crisis category uses these variables:

- `soviet_collapse_total_collapse_threat`
- `soviet_collapse_moscow_authority`
- `soviet_collapse_republic_confidence`
- `soviet_collapse_military_obedience`
- `soviet_collapse_depot_vulnerability`
- `soviet_collapse_foreign_appetite`
- `soviet_collapse_league_cohesion`
- `soviet_collapse_old_movement_pressure`
- `soviet_collapse_breakaway_count`

In calm conditions, central authority still has room to answer the crisis. Opening values then change from chaos tier, Soviet stability, war support, active wars, capital control, already fired major-event pressure, and the shared `world_in_threat` source count. The prior-crisis layer only reads generic event-system and world-threat signals; it does not key off individual crisis names. The total threat is recalculated from the component variables instead of being a fixed timer.

The 30-day crisis pulse records successful and failed Soviet objectives before checking progressive releases. If a calm or moderate month has stabilizing objective successes, no failed objectives, no active Soviet war, and no above-baseline foreign or League pressure, `soviet_collapse_apply_monthly_threat_guard` limits the monthly threat increase to the tuned calm or moderate cap before it snapshots the next month. This keeps a quiet month with real Soviet successes from producing a runaway threat jump while still allowing visible failures, foreign penetration, League coordination, war pressure, and high crisis levels to drive escalation. Ordinary poor-play failures are paced separately from severe-overlap failures: authority, legal, command, rail, depot, and cleanup failures each move the total threat by at most three points after the formula multiplier, so a calm baseline does not reach 80 threat inside two years from ordinary monthly failure pressure alone.

## Opening Breakaways

The normal opening wave is selected from structured pools instead of hard-coding Ukraine and Belarus. When the map supports it, the first wave chooses one western or eastern European actor, one Caucasus republic, and one Central Asian republic other than Kazakhstan, then adds extra ordinary republics as chaos, war, stability, and Soviet condition worsen. First-wave size feeds the threat formula through per-breakaway, major-republic, and regional-republic pressure constants; the completion verifier measures an ordinary three-republic wave and a larger six-republic tier-2 wave directly so the opening stays below terminal levels while still rising with scale. Kazakhstan is outside the normal opening pools and only enters early when southern pressure or severe crisis conditions justify a steppe rupture. Each appearing breakaway receives:

- `soviet_collapse_breakaway` country flag
- manpower and equipment from script constants
- `soviet_collapse_republican_startup_disorder`
- local republic variables for institutions, League support, foreign support, and local authority pressure
- an `Emergency Republican Guard` template and capital guard divisions from the base package
- an `Emergency Republican Field Brigade` template with artillery for larger or more chaotic releases
- extra manpower, rifles, support equipment, artillery, guard units, and field brigades from tag strength, chaos tier, Soviet war state, weak Moscow Authority, and high Union Crisis Threat

When Kazakhstan appears as an event-created opening breakaway, the southern cascade can also begin. Uzbekistan appears with Kazakhstan if still under Moscow control, Kyrgyzstan can appear at chaos tier 3 and above, Tajikistan can appear at chaos tier 4 and above, and Turkmenistan can appear at chaos tier 5. These southern republics receive the standard breakaway setup package and the shared Central Asian runtime focus tree.

Future breakaway setup also consumes one-use Soviet mission flags. `soviet_collapse_next_declaration_unarmed` reduces the next breakaway support package, while `soviet_collapse_next_declaration_armed` increases it; either flag clears after it is applied to one breakaway.

## Terminal Collapse

`Union Unmade` now resolves the crisis instead of only presenting the super-event. When `soviet_collapse_show_union_unmade_super_event` fires, `soviet_collapse_apply_terminal_collapse` runs before the presentation layer. The terminal pass releases every ordinary non-Russian Soviet republic that is still unreleased, has core territory owned and controlled by `SOV`, and is part of the supported republic set: Ukraine, Belarus, Moldova, the Baltic republics, the Caucasus republics, Uzbekistan, Kyrgyzstan, Tajikistan, Turkmenistan, and Kazakhstan. It also frees any already-existing supported republic that is still a Soviet subject. Each republic released or freed by this terminal pass receives `soviet_collapse_event_created_republic`, the normal breakaway setup package, its runtime focus tree, and an extra final-collapse military package from `constant:soviet_collapse_breakaway_support.terminal_*`.

Terminal collapse no longer appends fixed custom successor tags. Chaos tier and old-movement pressure still affect ordinary release pacing and crisis pressure, but the terminal pass itself stays with supported Soviet republics instead of spawning hardcoded special actors.

The same terminal effect closes the pre-collapse crisis board. `soviet_collapse_cleanup_terminal_collapse_missions` clears the active Soviet Collapse and opening-wave flags, clears one-use next-declaration flags, clears transient loyal-unit and district war-room helper flags, removes every defined active Soviet crisis mission with `remove_mission`, and leaves `soviet_collapse_terminal_collapse` as the outcome memory. Because `is_soviet_collapse_active` now excludes the terminal flag, Soviet response, breakaway action, regional faction, and foreign patron categories no longer remain visible after full collapse. The current foreign patron layer uses repeatable targeted decisions with `days_re_enable`, not active timed missions, so there is no separate foreign mission instance to remove in the terminal pass.

The local event catalog workbook row for Event 005 matches the current clean-spec implementation, and the current parser-oriented audit passes across the opening, republic, regional, achievement, spreadsheet, and super-event surfaces.

## Republic Focus Trees

Event-created Ukraine, Belarus, Kazakhstan, southern cascade republics, prepared regional tags, and any remaining event-created breakaway without a bespoke tree receive runtime focus trees through `load_focus_tree` after the release effect finishes. The loading effect only applies to countries with `soviet_collapse_event_created_republic`, and it does not use `keep_completed`, so it is intended for freshly released tags rather than replacing progress on existing countries. Fixed custom successor trees are not loaded from Event 005 release, mission, regional-faction, terminal-collapse, or spawn-dispatch script.

The implemented trees are:

1. `soviet_collapse_ukraine_focus_tree`: 81 focuses for Ukraine emergency republic tree with political route locks, depot and grain branches, League preparation, and late settlement tracks.
2. `soviet_collapse_belarus_focus_tree`: 53 focuses for Belarus rail, forest, military-transit, corridor, League logistics, and state-definition routes.
3. `soviet_collapse_kazakhstan_focus_tree`: 92 focuses for Kazakhstan steppe-congress tree with rail, depot, Alash legal institutions, socialist planning, military district mobility, resource sovereignty, foreign mediation, federal, and southern-defense branches.
4. `soviet_collapse_baltic_focus_tree`: 42 focuses for Baltic restoration, legal continuity, archive protection, border government, Baltic League, port/customs sovereignty, coastal and forest defense, foreign-protection, tag-specific Estonia/Latvia/Lithuania routes, and recognition settlement routes.
5. `soviet_collapse_caucasus_focus_tree`: 40 focuses for Caucasus mountain compact, oil emergency directorate, national restoration, pass defense, Georgian Tbilisi/Black Sea observer route, Armenian Yerevan relief and border-fortress route, Azerbaijani Baku oilfield and Caspian oil diplomacy route, sponsor-consulate, border treaty, compact, and high-chaos crown routes.
6. `soviet_collapse_central_asia_focus_tree`: 45 focuses for Central Asian local republic, Turkestan federation, military border authority, Uzbek Tashkent/Samarkand-Bukhara/cotton-rail congress, Tajik Dushanbe/Pamir mountain sovereignty, Kyrgyz Bishkek/Tian Shan pass authority, foreign patronage, Turkmen Ashgabat/desert/Caspian authority, cotton/water logistics, Basmachi pressure, Khwarazm high-chaos, southern pact, and federation routes.
7. `soviet_collapse_moldova_focus_tree`: 23 focuses for Moldova Dniester, Bessarabian, Romanian-alignment, union-debate, Ukrainian grain-road, Eastern Buffer, river-state, and small-state survival routes.
8. `soviet_collapse_internal_republic_focus_tree`: 62 focuses for Karelia, Komi, Crimea, Tatarstan, Bashkiria, Far East, Yakutia, Buryatia, and Tuva with regional survival, deeper Komi Syktyvkar/Pechora/mine-and-timber/exile-camp/northern-accord content, Bashkir Ufa/oilfield/mobile-defense/Volga-Ural compact content, Crimean Ukraine-settlement/Turkish-mediation/peninsula-fortress/Black Sea compact content, Yakut Aldan and Arctic resource routes, Far Eastern Pacific harbor and Amur customs routes, Buryat Baikal pass and Ulan-Ude relay routes, Tuvan border-road and steppe compact routes, industry, defense, tag-specific border/resource/port/military branches, foreign-channel, high-chaos, and common-front routes.
9. `soviet_collapse_breakaway_focus_tree`: 36 focuses for the shared fallback tree for remaining event-created breakaways with emergency governance, legal records, local courts and militia rolls, depot repair, home industry, border militia, foreign liaison, many-patron accounting, League observer access, road-and-rail repair, and survival lanes.
10. `CFR_soviet_collapse_focus_tree`: 45 focuses for Civilian Factory of Russia construction-board tree with cooperative, planner, contract-board, concrete-committee, and builder-state routes.
11. `MFR_soviet_collapse_focus_tree`: 37 focuses for Military Factory of Russia arsenal-board tree with officer, worker, merchant, unsafe-output, export, and arsenal-state routes.
12. `KRS_soviet_collapse_focus_tree`: 27 focuses for Kronstadt Free Soviet sailor-assembly, fortress-store, naval-militia, Gulf battery posts, fortress signal rooms, free-port conference, port-council, and port-sovereignty routes.
13. `FTH_soviet_collapse_focus_tree`: 27 focuses for Free Territory of Huliaipole commune, depot-raiding, League bargain, tachanka front, free rail communes, roaming embassies, Black International, and anti-capital routes.
14. `BBH_soviet_collapse_focus_tree`: 27 focuses for Black Banner Host mobile-column, commune-war, captured-store, anti-state, column schools, temporary anti-protectorate diplomacy, non-domination pacts, and anti-prison endgame routes.
15. `BSC_soviet_collapse_focus_tree`: 27 focuses for Basmachi Confederation oasis, pass-guard, caravan-store, road-control, caravan officer school, road-and-water guarantees, recognition, and Steppe Federation news routes.
16. `TNC_soviet_collapse_focus_tree`: 27 focuses for Turkestan National Council civic-office, railway-guard, oasis-bureau, guarded-route, railway officer school, autonomy guarantees, recognition, and New Turkestan routes.
17. `ALA_soviet_collapse_focus_tree`: 27 focuses for Alash Restoration Authority congress, cavalry-guard, Alash officer schools, rail-station, campaign planning, aksakal mediation, minority steppe guarantees, recognition, and modernization/endgame routes.
18. `UDC_soviet_collapse_focus_tree`: 27 focuses for Union Defense Committee loyal-district, provisional-command, signature-force, staff-recognition, emergency staff college, operational war plan, command mediation, loyalist statute, and emergency command routes.
19. `SDZ_soviet_collapse_focus_tree`: 27 focuses for Security Directorate Zone archive, directorate, signature-force, custody-recognition, internal troop school, archive war plan, custody review, chain-of-custody statute, and security-state routes.
20. `GAC_soviet_collapse_focus_tree`: 27 focuses for Green Army Congress village, land-and-bread, peasant guard, forest-column, food-recognition, field-road, village mediation, harvest-truce, and rural federation routes.
21. `DHC_soviet_collapse_focus_tree`: 27 focuses for Don Host Emergency Circle host-circle, cavalry, southern defense, passage-recognition, river patrol school, river-road war planning, stanitsa mediation, convoy-autonomy guarantees, and host-between-capitals routes.
22. `KHC_soviet_collapse_focus_tree`: 27 focuses for Kuban Host Provisional Council crossing-council, Kuban line, cavalry, Ukrainian diplomacy, crossing patrol school, steppe-river war planning, stanitsa mediation, grain passage guarantees, and between-steppe-and-mountains endgame routes.
23. `FEV_soviet_collapse_focus_tree`: 27 focuses for Far Eastern Republic Revival buffer, railway guard, foreign-distance, Pacific line routes, port-rail war planning, Vladivostok harbor board logistics, Amur buffer posts, Pacific observer missions, and Far Eastern survival capstone routes.
24. `SZA_soviet_collapse_focus_tree`: 27 focuses for Siberian Zemstvo Authority regional assembly, city guard, Trans-Siberian depot control, depth defense planning, Tomsk-Omsk switchyards, Irkutsk depth stores, Yenisei city federation, and Siberian survival routes.
25. `UWD_soviet_collapse_focus_tree`: 27 focuses for Ural Workers Directorate factory committee, worker battalion, arsenal autonomy, labor-defense, factory security school, rail-belt campaign, shift council mediation, output guarantees, and arsenal autonomy mandate routes.
26. `MRC_soviet_collapse_focus_tree`: 27 focuses for Mountain Republic of the Caucasus elder council, pass closure, lowland depot raids, village autonomy, Caucasus negotiation, anti-border-troop, mountain federal authority, and mandate routes.
27. `IUL_soviet_collapse_focus_tree`: 27 focuses for Idel-Ural League Volga-Ural office, river guard, corridor authority, Volga-line war planning, Kazan-Ufa workshop cordons, Orenburg approach posts, federal congress missions, and federal corridor mandate routes.
28. `BAC_soviet_collapse_focus_tree`: 27 focuses for Birobidzhan Autonomous Commune settlement, militia, autonomous office, river-settlement defense planning, Birobidzhan archive workshops, Amur relief posts, observer relief conferences, and autonomous commune mandate routes.
29. `ARD_soviet_collapse_focus_tree`: 27 focuses for Arctic Naval Directorate port directorate, convoy officer, northern logistics, northern sea denial, Murmansk dockyard sheds, Kola denial posts, White Sea observer boards, and port-neutrality mandate routes.
30. `NLC_soviet_collapse_focus_tree`: 27 focuses for Northern Lights Commune polar survival, Ice Watch, scientific refuge, northern recognition, Ice Watch school, icebound war planning, station mediation, winter guarantees, and post-capital routes.

Focus rewards call shared scripted effects for legal recognition, socialist sovereignty, military consolidation, depot control, League preparation, foreign channels, and high-chaos identity pressure. Those effects adjust local breakaway variables, update the consolidated staged republic spirits, add practical construction rewards where appropriate, and feed the Soviet crisis meter through constants in `soviet_collapse_republic_focus`. Military and League preparation focuses add defensive works; depot and supply focuses add civilian or military factories. Foreign-channel focuses do not grant foreign support spirits by themselves; those come from external support decisions. Ukraine's replacement slice also documents each focus role in script comments, uses focus filters on every focus, keeps League escalation locked behind crisis pressure through `is_soviet_collapse_league_pressure_ready`, and keeps foreign provisional authority behind an actual liaison-office state and high foreign pressure.

Continuous focus windows for the Event 005 republic, factory successor, and custom splinter trees sit in a right-side panel outside each focus grid. The runtime layouts are generated from prerequisite depth, spread into branch lanes, and checked for zero coordinate collisions, zero crossing hard prerequisite lines, zero visually detached long prerequisite jumps, no isolated focus components, no shallow side-focus leaves, a fourteen-row depth ceiling, and at least seven grid units between mutually exclusive choices. Republic-tree convergence focuses use separate prerequisite blocks for each required parent; limited same-block alternative prerequisites are reserved for route outcomes that intentionally feed one visible finisher or for opening fork nodes whose hidden two-of-three gates should still be visibly connected to their branch parents.

The Ukraine middle-branch slices add the General Staff frontier choice, Republican Deep Battle, Militia Federalization, Black Sea port ledgers, grain and coal crosslinks, railway quartermasters, local factory guards, requisition crisis handling, the Industrial Mobilization Council, arms/export industry route locks, Economic Sovereignty, foreign liaison side branches, and League signal-code route locks. `soviet_collapse_form_free_republics_league_from_ukraine` creates the Free Republics' League only through the gated League Founding Charter focus and pulls eligible event-created breakaways into the faction. The late expansion slice adds the defensive-line gate, Black Sea rim, western and Romanian policy tracks, Balkan and Anatolian supply diplomacy, Carpathian security, protectorate debate, League security zones, direct national-claim policy, Black Sea hegemony, Breadbasket Empire, Granary of Free Republics, border-state coordination, No Foreign Master, and the Great Steppe and Sea Plan. The high-chaos slice follows the Part 3 row names for The Bread State Whispers, The Black Soil Oath, Harvest by Decree, Dead Fields Living Columns, Grain Census of Everyone, No One Leaves the Bread Line, The Last Harvest Plan, Black Banner Takes the Villages, Kyiv or Huliaipole, The Double Republic, The Commune War, and When the Fields Refuse the State. These focuses remain hidden behind high-chaos and old-movement pressure until the exact food-crisis and Free Territory evolution trigger pass is implemented. The democratic deep slice adds Coalition of Three Ministries, the Rural Deputy Bloc, Minority Autonomy Statutes, the Emergency Court of Kyiv, parliamentary front oversight, the governor/rada fork, Republic of Laws, and Civilian Command Over the Army. The socialist sovereignty slice adds the Workers' Congress in Kharkiv, Village Soviets Without Requisition, the party-card fork, Moscow loyalist purge or re-registration choices, armed factory soviets, the anti-landlord village line, left League diplomacy, the commune debate, and the red republic finisher. The military-directory slice adds Field Headquarters precedence, district mobilization, officer patronage lists, depot courts, the General Staff War College, the commander/cabinet fork, Army Supremacy, Mixed Emergency Cabinet, War Plans Beyond the Border, and the Directory State. The Hetmanate slice adds estate credit offices, the crown-without-a-crown fork, Symbolic and Executive Hetmanate choices, conservative officer circles, the church-and-grain settlement, foreign court recognition, and the Second Hetmanate finisher. The final foreign, League, and late-game slice adds sponsor-crate audits, the political-adviser fork, League arbitration, shared depot ledgers, Republics' Joint Staff, the border mandate vote, Black Sea customs policy, port soldiers, the western-question pressure focus, bread-line border escalation, and the two endgame settlement focuses. Achievement definitions for the implemented Event 005 routes are wired in `common/achievements/chaos_redux_achievements.txt`; future-only achievement entries stay tied to route or super-event flags reserved for later audit passes. Super-event escalation fires from the broad breakaway threshold and implemented route capstones for the active grounded routes; disabled hardcoded packages do not contribute route calls.

## Dormant Custom Tag Packages

Event 005 no longer activates fixed high-chaos successor tags from mission failures, opening releases, terminal collapse, or regional-league recruitment. The ordinary collapse path releases supported Soviet republics, uses the progressive release system, and ends at terminal collapse by freeing all supported ordinary republics still under Moscow control. The legacy custom-tag package files remain outside the active Event 005 runtime path until a grounded design pass replaces the hardcoded special-successor layer.

The verifier checks this boundary through `hardcoded_high_chaos_successor_activation_removed`, which requires zero active calls to `soviet_collapse_maybe_spawn_high_chaos_successors`, zero terminal calls to fixed successor activation, zero dispatches inside that helper, and zero regional-faction invite clauses for `soviet_collapse_high_chaos_successor`.

## Intervention Decisions

Breakaway republics have a small playable emergency board:

1. `soviet_collapse_request_foreign_recognition`
2. `soviet_collapse_mobilize_defense_units`
3. `soviet_collapse_seize_depots`
4. `soviet_collapse_coordinate_fronts`

These actions use explicit icon-value costs instead of generic political-power defaults. Mobilizing defense units spends political power and command power, depot seizure spends army experience, and front coordination spends fuel and support equipment. They build recognition progress, depot control, League support strength, emergency units, republican recovery progress, and Soviet crisis pressure. A newly released republic starts with `soviet_collapse_republican_startup_disorder`; repeated decisions and focuses remove it and add `soviet_collapse_emergency_administration_stabilized`. The visible republic support surface is capped to consolidated staged spirit families: Republican Institutions, League Coordination, External Support, and Local Authority Pressure.

Major foreign patron candidates that are hostile to Moscow can target entries from `global.soviet_collapse_breakaway_countries` with:

1. `soviet_collapse_recognize_breakaway_government`
2. `soviet_collapse_fund_ideological_liaison_offices`
3. `soviet_collapse_ship_border_armaments`
4. `soviet_collapse_dispatch_military_advisers`
5. `soviet_collapse_open_republican_intelligence_channel`
6. `soviet_collapse_sponsor_volunteer_corps`
7. `soviet_collapse_negotiate_republican_trade_mission`
8. `soviet_collapse_fund_civilian_construction_mission`
9. `soviet_collapse_fund_military_construction_mission`
10. `soviet_collapse_sponsor_press_and_radio_network`
11. `soviet_collapse_secure_republican_aid_corridor`
12. `soviet_collapse_build_republics_league_conference`
13. `soviet_collapse_demand_anti_puppet_clause`
14. `soviet_collapse_offer_protection_treaty`
15. `soviet_collapse_demand_adviser_privileges`
16. `soviet_collapse_install_client_cabinet`

The targeted decision scope follows the vanilla `target_array` pattern: the patron remains `ROOT`, and the chosen breakaway is `FROM`. The aid costs use stability, war support, equipment, army experience, manpower, trains, convoys, and higher fuel thresholds. Stronger target republics expose higher cost text and require larger payments before the action can fire. Effects raise breakaway recognition or military capacity while feeding Soviet `Foreign Penetration`, `Depot Vulnerability`, `League Cohesion`, `Moscow Authority`, or `Armed Breakaway Momentum` as appropriate.

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
111. `soviet_collapse_soviet_mission_111_keep_the_factory_whistles_ordinary`
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

Mission outcomes use family-specific crisis pressure helpers tuned through `constant:soviet_collapse_objective_pressure`. Authority, legal, command, rail, depot, old-movement, foreign, cleanup, settlement, and League objectives no longer share the same flat success and failure effects; each family adjusts the relevant Union Crisis Threat components, records whether the month saw a success or failure, and then recalculates the total threat. The verifier resolves every successful objective helper against the threat formula, requiring all success helpers to be net non-increasing and to avoid destabilizing component changes. A SOV-only delayed check now uses `mtth:soviet_collapse_progressive_release_weight` and `mtth:soviet_collapse_progressive_release_miss_weight` from `common/mtth/005_soviet_collapse_mtth.txt` to decide whether a new eligible republic breaks away. The MTTH variables respond to Union Collapse Threat, Moscow Authority, Command Obedience, active breakaway count, regional cascade signals, depot vulnerability, foreign penetration, League cohesion, old-movement resurgence, failed Soviet mission flags, war pressure, and chaos tier. If a release fires, the visible cause event is selected from ministry refusal, rail-office seal change, border-guard defection, local party sovereignty, foreign liaison acceleration, depot commander oath, old-movement pressure, or League envoy coordination. At 100 threat, Union Unmade fires immediately, releasing every ordinary republic still under Moscow control.

Failed Soviet objective families also trigger short report events in `events/005_soviet_collapse.txt`: authority (`chaosx.nr5.10`), command (`chaosx.nr5.11`), rail (`chaosx.nr5.12`), depot (`chaosx.nr5.13`), foreign exposure (`chaosx.nr5.14`), cleanup/backlog (`chaosx.nr5.15`), and settlement (`chaosx.nr5.16`). These are normal crisis reports, not evolution logs.

The main crisis decision AI weights react to the same crisis state. Soviet responses prefer authority restoration, loyalist officers, supply-route action, or reserve mobilization based on Moscow Authority, Military Obedience, Depot Vulnerability, Foreign Penetration, League coordination, active war, and Union Crisis Threat. Breakaway actions prefer recognition, mobilization, depot seizure, or front coordination based on Soviet weakness, war with Moscow, faction membership, League coordination, and chaos tier. Foreign patron actions prefer recognition, liaison, arms, advisers, intelligence, volunteers, or trade based on Soviet authority, foreign penetration, military obedience, depot vulnerability, war with Moscow, total threat, and League coordination.

The full Soviet objective mission audit lives in `docs/events/005_soviet_union_collapse_mission_audit.md`. It records all 118 active missions against owner, purpose, requirement summary, success helper, failure helper, and duplicate-risk evidence, and links the table to `soviet_objective_board_surface`, `mission_quality_surface`, `mission_requirement_surface`, `localisation_surface`, and `terminal_mission_cleanup`.

## Icon Wiring

This slice reuses existing wired sprites. No new art was generated.

- Ideas use `GFX_idea_union_crisis`, `GFX_idea_emergency_union_authority`, `GFX_idea_new_union_negotiations`, `GFX_idea_union_restored`, `GFX_idea_loyalist_officer_corps`, `GFX_idea_captured_soviet_depots`, `GFX_idea_defensive_coordination`, `GFX_idea_legal_restoration_claim`, and `GFX_idea_old_underground_networks` from `interface/005_soviet_collapse_icons.gfx`.
- Decision categories use `GFX_decision_category_soviet_collapse_soviet`, `GFX_decision_category_soviet_collapse_breakaway`, `GFX_decision_category_soviet_collapse_foreign_patron`, and `GFX_decision_category_soviet_collapse_regional_faction`.
- Soviet responses use `GFX_decision_restore_party_control`, `GFX_decision_send_loyalist_officers`, `GFX_decision_cut_rebel_supply_routes`, and `GFX_decision_emergency_mobilization`.
- Breakaway actions use `GFX_decision_request_foreign_recognition`, `GFX_decision_mobilize_defense_units`, `GFX_decision_seize_depots`, and `GFX_decision_coordinate_fronts`.
- Foreign patron actions use `GFX_decision_soviet_collapse_foreign_recognition`, `GFX_decision_soviet_collapse_foreign_armaments`, `GFX_decision_soviet_collapse_foreign_advisers`, `GFX_decision_soviet_collapse_foreign_intelligence`, `GFX_decision_soviet_collapse_foreign_volunteers`, and `GFX_decision_soviet_collapse_foreign_trade`.
- The consolidated republic spirit families use `GFX_idea_emergency_union_authority`, `GFX_idea_defensive_coordination`, `GFX_idea_legal_restoration_claim`, and `GFX_idea_old_underground_networks`.
- Soviet objectives use the shared goal sprites in `interface/005_soviet_collapse_icons.gfx`, including `GFX_decision_soviet_collapse_authority_goal`, `GFX_decision_soviet_collapse_command_goal`, `GFX_decision_soviet_collapse_rail_goal`, `GFX_decision_soviet_collapse_depot_goal`, `GFX_decision_soviet_collapse_old_movement_goal`, `GFX_decision_soviet_collapse_border_goal`, `GFX_decision_soviet_collapse_foreign_goal`, and `GFX_decision_soviet_collapse_cleanup_goal`.
- The visible opening event uses `GFX_report_union_crisis`; the news event uses `GFX_news_soviet_union_collapse`.
- Progressive MTTH release events `chaosx.nr5.130` through `chaosx.nr5.137` reuse `GFX_report_union_crisis`; no new report art is required.
- Republic focus trees use existing sprites from `interface/005_soviet_collapse_icons.gfx`, `interface/005_soviet_collapse_ukraine_icons.gfx`, `interface/005_soviet_collapse_blr_icons.gfx`, `interface/005_soviet_collapse_kaz_icons.gfx`, and `interface/005_soviet_collapse_regional_icons.gfx`. No additional focus sprite filenames are required for this slice.
- `CFR_soviet_collapse_focus_tree` reuses the existing 33 Civilian Factory focus sprites in `interface/005_soviet_collapse_factory_ancient_icons.gfx` across 58 focuses. No new CFR focus art is required for this slice.
- `MFR_soviet_collapse_focus_tree` reuses the existing Military Factory focus sprites in `interface/005_soviet_collapse_factory_ancient_icons.gfx` across 37 focuses. No new MFR focus art is required for this slice.
- `KRS`, `FTH`, `BBH`, `BSC`, `TNC`, `ALA`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, and `NLC` custom-splinter focus trees reuse the existing per-tag `GFX_focus_TAG_*` sprites in `interface/005_soviet_collapse_custom_icons.gfx`. No new custom-splinter focus art is required for this slice.
- High-chaos tag foundations use flag assets under `gfx/flags/`, leader portraits under `gfx/leaders/005_soviet_collapse/`, and portrait sprite keys in `interface/005_soviet_collapse_factory_ancient_icons.gfx` or `interface/005_soviet_collapse_custom_icons.gfx`. The high-chaos notice events currently reuse `GFX_report_union_crisis`, so no new report sprite is required for this slice.
- Custom Event 005 country flags were audited for the 21 custom tags across base, communism, democratic, fascism, and neutrality variants in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`. All 315 audited TGA files exist, all use top-origin TGA headers after the vertical asset correction, and every medium or small variant matches its large source orientation more closely than a vertically flipped source. No historical or existing custom flags were regenerated during this audit.
- Event 005 achievements use `common/achievements/chaos_redux_achievements.txt`, localisation in `localisation/english/chaosx_achievements_l_english.yml`, sprites in `interface/chaosx_achievements.gfx`, and the icon ledger in `docs/assets/005_soviet_union_collapse/achievement_icon_manifest.md`.

## Future Plans

- Expand the Soviet objective board beyond the first one hundred twenty-eight missions while preserving the ten-active cap.
- Expand breakaway missions, foreign intervention missions, regional faction categories, and action-based foreign aid routes beyond the first playable board.
- Continue deepening longer event chains and route-specific follow-up content for implemented custom countries where the clean specification calls for more than the current foundational country, decision, spawn, and focus package.
- Extend remaining route-specific super-event triggers, future-only achievement completion flags, and evolution logs only where the clean specification allows them.
- Audit existing Soviet Collapse evolution localisation so ordinary crisis stages are not presented as evolutions.
