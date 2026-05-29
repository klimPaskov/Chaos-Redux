# Soviet Collapse Focus Full Rework Audit Handoff

Date: 2026-05-29
Scope: Event 005 Soviet Collapse focus-tree current-state audit.
Mode: Audit only. No gameplay patch was made.

## Required references used

- Repo instructions: `AGENTS.md`
- Skills: `hoi4-focus-trees`, `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`
- Offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`
- Vanilla precedents inspected: `common/national_focus/generic.txt`, `common/national_focus/soviet.txt`
- Event specs/docs inspected:
  - `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_3_decisions_missions_influence.md`
  - `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_4_releases_leagues_union_unmade.md`
  - `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`
  - `docs/events/005_soviet_collapse.md`

## Executive finding

The four Soviet Collapse focus files contain 41 focus trees and 1,698 focuses. They are technically wired better than a pure draft: every focus has an icon, `ai_will_do`, and `search_filters`; no duplicate focus ids were found; focus localisation and icon sprite definitions are present. The problem is content architecture, not missing syntax.

The current trees remain too linear, visually noisy, and reward-thin for the requested end state. A large share of focuses are still variable or helper-updater nodes that repeatedly call consolidated idea helpers, set route flags, or grant small generic modifiers. Many country identities are represented by similar 47-focus shells instead of distinct mechanics. The layout scan also found many pathline-crossing risks in the large republic trees and several mutual-exclusive clusters placed far enough apart that symbols and lines are likely to cut across focus panels.

No small safe patch was made because the dominant issues are structural: route design, layout reflow, mechanic integration, and reward replacement. Moving one or two focuses or deleting one helper call would not materially improve the requested rework and would risk conflicting with the larger redesign.

## Focus tree count table

| File | Tree | Start line | Focuses | Tiny/generic reward candidates | Strong visible reward candidates | Idea/helper reward focus count |
|---|---:|---:|---:|---:|---:|---:|
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_ukraine_focus_tree` | 17 | 83 | 65 | 11 | 17 |
| same | `soviet_collapse_breakaway_focus_tree` | 2355 | 36 | 27 | 7 | 0 |
| same | `soviet_collapse_internal_republic_focus_tree` | 3152 | 62 | 33 | 29 | 4 |
| same | `soviet_collapse_baltic_focus_tree` | 4656 | 42 | 31 | 11 | 2 |
| same | `soviet_collapse_caucasus_focus_tree` | 5620 | 40 | 31 | 8 | 4 |
| same | `soviet_collapse_central_asia_focus_tree` | 6549 | 45 | 23 | 18 | 9 |
| same | `soviet_collapse_moldova_focus_tree` | 7698 | 48 | 29 | 13 | 8 |
| same | `soviet_collapse_belarus_focus_tree` | 8866 | 53 | 41 | 6 | 10 |
| same | `soviet_collapse_kazakhstan_focus_tree` | 10198 | 92 | 68 | 18 | 12 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | `FTH` | 14 | 47 | 20 | 12 | 24 |
| same | `PRA` | 1218 | 22 | 6 | 10 | 5 |
| same | `TSC` | 1790 | 18 | 6 | 6 | 6 |
| same | `RMC` | 2267 | 18 | 6 | 5 | 5 |
| same | `DSC` | 2751 | 18 | 3 | 6 | 7 |
| same | `NRF` | 3313 | 18 | 3 | 7 | 6 |
| same | `ICD` | 3816 | 18 | 6 | 5 | 5 |
| same | `BSC` | 4290 | 47 | 23 | 13 | 24 |
| same | `TNC` | 5420 | 47 | 22 | 14 | 24 |
| same | `ALA` | 6558 | 47 | 25 | 10 | 25 |
| same | `BBH` | 7678 | 47 | 25 | 10 | 24 |
| same | `KRS` | 8882 | 47 | 19 | 16 | 21 |
| same | `UDC` | 10124 | 47 | 27 | 7 | 26 |
| same | `SDZ` | 11325 | 47 | 27 | 8 | 26 |
| same | `GAC` | 12570 | 47 | 27 | 10 | 25 |
| same | `DHC` | 13753 | 47 | 28 | 16 | 26 |
| same | `KHC` | 14959 | 47 | 26 | 13 | 26 |
| same | `FEV` | 16158 | 47 | 25 | 14 | 24 |
| same | `SZA` | 17333 | 47 | 25 | 15 | 26 |
| same | `UWD` | 18513 | 47 | 22 | 20 | 24 |
| same | `MRC` | 19718 | 47 | 24 | 17 | 23 |
| same | `IUL` | 20894 | 47 | 24 | 13 | 23 |
| same | `BAC` | 22051 | 47 | 26 | 13 | 22 |
| same | `ARD` | 23197 | 47 | 23 | 17 | 23 |
| same | `NLC` | 24395 | 47 | 23 | 14 | 28 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | `CFR` | 15 | 47 | 37 | 9 | 0 |
| same | `OGB` | 1135 | 23 | 12 | 6 | 4 |
| same | `MFR` | 1712 | 58 | 50 | 6 | 2 |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | `KZR` | 12 | 16 | 8 | 6 | 3 |
| same | `SOG` | 384 | 16 | 8 | 6 | 3 |
| same | `KHW` | 757 | 16 | 8 | 7 | 3 |
| same | `ALN` | 1133 | 16 | 8 | 7 | 2 |

Notes:
- "Tiny/generic reward candidates" are mechanically detected focuses where the completion reward did not visibly contain a map, unit, decision, war, faction, building, tech, template, or similar concrete payoff. Some helpers may have deeper effects, but the focus reward surface still reads as indirect or small.
- "Strong visible reward candidates" are focuses whose completion reward directly contains decisions, missions, buildings, offsite buildings, cores, claims, war goals, units, templates, factions, tech, or similar concrete effects.

## Repeated idea and helper usage

Direct idea calls in the focus files are limited, but helper-driven idea churn is widespread.

Direct `remove_ideas` occurrences:

| File line | Focus area | Idea |
|---:|---|---|
| `005_soviet_collapse_custom_splinters.txt:1375` | `PRA` | `pra_dispatcher_court_tensions` |
| `005_soviet_collapse_custom_splinters.txt:1950` | `TSC` | `tsc_field_station_rivalries` |
| `005_soviet_collapse_custom_splinters.txt:2385` | `RMC` | `rmc_credal_cell_rivalries` |
| `005_soviet_collapse_custom_splinters.txt:2871` | `DSC` | `dsc_grave_regiment_rivalries` |
| `005_soviet_collapse_custom_splinters.txt:3427` | `NRF` | `nrf_drowned_crew_disputes` |
| `005_soviet_collapse_custom_splinters.txt:3932` | `ICD` | `icd_grave_commissar_rivalries` |
| `005_soviet_collapse_custom_splinters.txt:20112` | `MRC` | `mrc_pass_confederation_rivalries` |
| `005_soviet_collapse_factory_successors.txt:1199` | `OGB` | `ogb_disputed_restored_name` |

Direct `add_ideas` and `swap_ideas` calls in the focus files: none found.

Major helper/updater use:

| Helper | Definition/reference | Count in focus rewards | Audit note |
|---|---:|---:|---|
| `soviet_collapse_update_consolidated_republic_ideas` | `common/scripted_effects/005_soviet_collapse_effects.txt:5459` | 111 direct focus calls | Centralized updater is useful, but repeated focus use makes many rewards feel like idea maintenance rather than route payoffs. |
| `soviet_collapse_apply_focus_high_chaos_identity` | `005_soviet_collapse_effects.txt:9288` | 96 | High-chaos identity is too often a generic route wrapper instead of a country-specific mechanic branch. |
| `soviet_collapse_apply_custom_splinter_economy_identity` | `005_soviet_collapse_effects.txt:11838` | 18-19 per repeated template family | Often resolves to small per-tag rewards and ends in consolidated idea updating. |
| `soviet_collapse_apply_custom_splinter_doctrine_identity` | `005_soviet_collapse_effects.txt:13194` | 18-19 per repeated template family | Supports specialization, but repeated use across many countries makes route reward rhythm similar. |
| Other `soviet_collapse_apply_custom_splinter_*_identity` helpers | `005_soviet_collapse_effects.txt` | 473 total identity/helper reward focuses including high-chaos helper calls | This is the main reward-spam source for the custom splinter layer. |

## Route coverage table

| Country/tree group | Current implemented route surface | Required proper route families | Status | First implementation tranche |
|---|---|---|---|---|
| Ukraine, `005_soviet_collapse_republics.txt:17` | Large 83-focus tree with democratic, socialist, directory, league, expansion, black banner, industry, and high-chaos labels. | Emergency Kyiv institutions; Rada legalism; sovereign socialist commune; military directory; grain/Black Soil economy; Dnieper-Donbas arsenal; Black Sea/navy; foreign patronage; Free Republics League leadership; expansion/integration; Black Banner/Bread State. | Partial. Route labels exist, but 65/83 focuses are tiny/generic candidates and layout is the worst crossing cluster. | Rebuild opener and political route-lock grid, then attach visible decision phases, unit/building payoffs, and route AI to each lane. Reflow into compact parallel columns. |
| Belarus, `005_soviet_collapse_republics.txt:8866` | National council, socialist, rail/transit, foreign corridor, forest themes. | Minsk emergency state; legal restoration; rail sovereignty; forest defense; foreign corridor diplomacy; League logistics command; Pale Railway/high-chaos. | Partial. Only 6/53 strong visible reward candidates; rail identity is not mechanically dominant enough. | Build a rails/supply branch with railways, supply hubs, trains, armored train/rail guard units, and rail missions. |
| Kazakhstan, `005_soviet_collapse_republics.txt:10198` | 92-focus large tree with Alash, socialist, resource, steppe, foreign technical, and high-chaos labels. | Alma-Ata emergency; Alash; socialist steppe; military district; resource/rail economy; southern cascade; Central Asian League; foreign mediation; Basmachi/high-chaos. | Partial. Good route naming but 68/92 focuses are tiny/generic candidates. | Build resource + rail + steppe-defense mechanics first: mines/oil guards, rail hubs, state-targeted supply, Central Asian league decisions. |
| Baltic shared tree, `005_soviet_collapse_republics.txt:4656` | Shared regional restoration/defense/recognition lanes. | Legal restoration; coastal defense; forest defense; recognition race; Baltic League; exile/underground; anti-puppet intervention. | Partial. Too shared and too indirect for Estonia/Latvia/Lithuania identities. | Split the key payoff nodes by per-tag state targets: ports, forests, capitals, recognition, Baltic League founder/member behavior. |
| Caucasus shared tree, `005_soviet_collapse_republics.txt:5620` | Shared defense/compact/institution content. | National councils; mountain/pass defense; oil/infrastructure; Turkey/Iran mediation; Caucasus League; loyalist garrison; ancient/restoration pressure. | Partial. 31/40 tiny/generic candidates and weak country-specific map payoffs. | Add pass/oil/port nodes and mediation decisions keyed to each Caucasus tag. |
| Central Asia shared tree, `005_soviet_collapse_republics.txt:6549` | Shared steppe/rail/irrigation/league content. | Council authority; southern defense; old movement/Basmachi; foreign mediation; cotton/water/rail/pass economy; Central Asian League; high-chaos/ancient pressure. | Better than several shared trees, but still not distinct enough per tag. | Split legal councils, military border, foreign patronage, and old movement settlement/war into visible decision unlocks. |
| Moldova, `005_soviet_collapse_republics.txt:7698` | Dniester, Romanian, Ukrainian corridor, and observer/compact themes. | Chisinau council; Dniester defense; Romanian diplomacy; Ukrainian settlement; river/agrarian economy; observer/League; Dniester high-chaos. | Partial and visually risky. 91 crossing risks in the mechanical layout scan. | Build Dniester/Prut/Odessa corridor decision family with forts, bridges, river missions, and branch reflow. |
| Internal republic shared tree, `005_soviet_collapse_republics.txt:3152` | Generic internal republic package with defense/economy/compact/payoff. | Crisis government; local defense; economy/logistics; regional compact; late settlement; high-chaos. Needs regional overlays for Karelia/Komi/Volga-Ural/Crimea/Siberia/Far East/Yakutia/Buryatia/Tuva. | Functional but generic. | Convert to regional branch packs or overlay payoffs so internal republics do not all play the same. |
| CFR Construction Directorate, `005_soviet_collapse_factory_successors.txt:15` | 47-focus governance/building theme with many mutual-exclusive clusters. | State-building mandate; civilian factory surge; infrastructure and construction offices; foreign contracts; forced housing; builder army; cores/integration by construction. | Not overpowered enough. 37/47 tiny/generic candidates; current construction identity should be much more direct. | Replace early/mid small rewards with visible civs, infrastructure, building slots, supply hubs, construction-speed ideas, and repeatable construction-program decisions. |
| MFR arsenal/factory successor, `005_soviet_collapse_factory_successors.txt:1712` | 58-focus arsenal/factory tree. | Arsenal quotas; factory guards; arms export/client market; armored train/artillery/tank lines; war-market expansion; production AI. | Very shallow in reward surface: 50/58 tiny/generic candidates. | Build production line and unit/equipment branch first, including production strategy AI and repeatable arms-client decisions. |
| OGB, `005_soviet_collapse_factory_successors.txt:1135` | 23-focus restored-name/special compact tree. | Name legitimacy; archive/administration control; integration/settlement; regional military or industrial identity. | Compact and incomplete for full rework goals. | Decide whether OGB is a side tree or full successor; if full, expand to 4 route families before reward pass. |
| PRA Railway, `005_soviet_collapse_custom_splinters.txt:1218` | 22-focus rail country with dispatcher/court tension and some payoff nodes. | Timetable state; rail/supply hubs; armored trains; rail tolls; moving capital/rail sovereignty; rail-locked expansion. | Better than most small chaos trees but not extreme enough. | Add state-targeted railway/supply hub construction, train equipment, armored trains, rail guard units, and logistics AI. |
| DSC Dead Soldiers' Congress, `005_soviet_collapse_custom_splinters.txt:2751` | 18-focus dead-soldier package. `DSC_revenant_staff_line` around line 2858 adds aggressive AI pressure, but the tree is still compact. | Roll-call legitimacy; revenant mobilization; immediate cores on controlled land; many war goals; dead army units; no-demobilization economy; zombie-style conquest. | Underbuilt for requested identity. | Add an early war-machine branch with immediate coring helper, neighbor war goals, special undead units, and aggressive route AI. |
| NRF naval revenant, `005_soviet_collapse_custom_splinters.txt:3313` | 18-focus naval/dead crew compact tree. | Ports; dockyards; convoys; ships; naval invasions; White Sea lanes; fleet that does not dock. | Underbuilt for naval identity. | Add dockyards, convoys, ship spawns/build speed, naval invasion preparation, naval AI. |
| TSC science/anomaly, `005_soviet_collapse_custom_splinters.txt:1790` | 18-focus field station package. | Radar/airbases; anomaly expeditions; decryption; special projects; observatory vs signs route choice. | Too compact and helper-driven. | Make the anomaly mechanic visible through decisions, radar, air/special tech, and scouting missions. |
| RMC/ICD death/commissar trees, `005_soviet_collapse_custom_splinters.txt:2267` and `3816` | 18-focus compact identity packages. | Cult/commissariat rule; undead manpower; martyr/roll-call expansion; archive coring; forced mobilization. | Too small for full identity-driven play. | Add coring/war/mobilization branch and unique internal pressure mechanic. |
| FTH/BBH/KRS/BSC/TNC/ALA and other 47-focus high-chaos trees | Mostly 47-focus repeated template using custom splinter identity helpers. | Each needs a country-specific military, economy, diplomacy/special, and expansion route built around its lore. | Broadly shallow. Repeated 47-focus shell is the main "same tree with different names" risk. | Pick one country at a time and replace helper-template middle lanes with visible state, unit, decision, and war mechanics. |
| Ancient restorations KZR/SOG/KHW/ALN, `005_soviet_collapse_ancient_restorations.txt` | Four 16-focus compact packages. | Ancient legitimacy; modern survival; trade/water/pass/oasis economy; symbolic restoration vs modern administration; expansion; League bargain. | Too compact for requested "all trees" rework unless they are explicitly side trees. | Add 4 compact but distinct route lanes per tree, with actual formation/integration/claim decisions. |

## Mechanics disconnect list

The focus files reference existing Soviet Collapse systems, but many references are shallow or indirect. The main disconnect is that the focus reward layer often updates variables and ideas without unlocking or advancing the mechanics the player expects to use.

High-priority disconnects:

1. Release pressure and terminal collapse mechanics are not consistently turned into focus-route decisions. Focuses should unlock or accelerate regional release pressure, anti-SOV missions, crisis escalation, or terminal collapse choices. Current focus surface mostly grants variables or flags.
2. Free Republics League coordination exists in helper logic, including hardcoded member handling in `common/scripted_effects/005_soviet_collapse_effects.txt:9022` through `9034`, but many league focuses do not create differentiated league diplomacy, joint missions, or member-specific obligations.
3. Influence/patronage is represented by flags and variables, but foreign-aligned routes need visible decisions: missions, advisors, lend-lease hooks, guarantees, or dependency tradeoffs.
4. War declaration, coring, and integration are too sparse. Expansion identities like DSC, Black Banner/Bread State, Basmachi, ancient restorations, and construction/rail integration should grant visible war goals, claims, cores, compliance/resistance tools, or immediate coring when appropriate.
5. Unit templates and special forces are not a strong enough part of country identity. Dead soldiers, rail guards, construction battalions, naval revenants, arsenal guards, steppe cavalry, mountain pass troops, and forest partisans need recurring unit/template payoffs rather than mostly support equipment or variables.
6. Regional factions and diplomatic compacts exist but do not dominate route gameplay. Baltic, Caucasus, Central Asian, and League routes should have clear founder/member branches and AI preferences.
7. Country identity is too often abstracted into repeated `soviet_collapse_apply_custom_splinter_*_identity` helpers. The helper approach is maintainable, but it makes many focus rewards read as the same idea-update pulse instead of a distinct overpowered country fantasy.

## Layout and pathline risk audit

The scan approximated focus lines as straight prerequisite segments between focus coordinates. It is not a pixel-perfect HOI4 UI renderer, but it reliably flags dense layouts and likely pathline problems.

Highest-risk groups:

| Tree | Crossing risks | Line-through-focus risks | Mutual-exclusive placement risks | Notes |
|---|---:|---:|---:|---|
| Ukraine | 153 | 4 | 16 | Worst offender. Example cluster: `ukr_soviet_collapse_guard_the_telegraph_house`, `ukr_soviet_collapse_question_of_statehood`, `ukr_soviet_collapse_seal_the_grain_ledgers`, `ukr_soviet_collapse_village_granary_guards`, and `ukr_soviet_collapse_direct_national_claims` around `005_soviet_collapse_republics.txt:138`, `267`, `1747`. |
| Moldova | 91 | 4 | 0 | Large crisscrossing branch risk despite a smaller tree. |
| Kazakhstan | 120 | 13 | 2 | Too wide/deep for the current coordinate structure. |
| BAC | 44 | 0 | 0 | 47-focus custom tree still produces many crossing risks. |
| UWD | 35 | 2 | 0 | Custom template has through-focus risk. |
| SZA | 29 | 0 | 0 | Custom template line density risk. |
| FEV | 18 | 0 | 0 | Repeated custom shell risk. |
| CFR | 1 | 0 | 20 | Main issue is four-way mutual-exclusive sprawl at `005_soviet_collapse_factory_successors.txt:142`, `172`, `204`, `235`. |
| MFR | 8 | 1 | 10 | Mutual-exclusive spread around `005_soviet_collapse_factory_successors.txt:1844`, `1875`, `1905`, `1938`. |

This should be handled by a full reflow pass. Small one-node moves are not enough.

## Icon coverage table

| Check | Result | Notes |
|---|---:|---|
| Focuses missing `icon =` | 0 | All 1,698 focuses have icon assignments. |
| Assigned focus icons without sprite definitions | 0 | Sprite definitions were found across `interface/005_soviet_collapse*.gfx` files. |
| Focus ids missing localisation key | 0 | English localisation key present for each focus id. |
| Focus desc keys missing | 0 | English `_desc` key present for each focus id. |
| Repeated icon ids | Many | No technical breakage, but identity readability suffers. |

Repeated icon examples:

- `GFX_focus_soviet_collapse_guard_the_radio_stations`: 4 uses
- `GFX_ukr_soviet_collapse_democratic`: 4 uses
- `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`: 4 uses
- `GFX_focus_soviet_collapse_steppe_supply_congress`: 4 uses
- `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`: 4 uses
- `GFX_central_asia_soviet_collapse_steppe_federation`: 4 uses
- `GFX_moldova_soviet_collapse_ukrainian_corridor`: 4 uses
- `GFX_focus_FEV_diplomatic_plan`: 4 uses
- `GFX_focus_SZA_diplomatic_plan`: 4 uses
- `GFX_focus_MRC_civil_rule`: 4 uses
- Ancient restoration generic icon families repeat 4 times each for workshop, guard, league, old-border, symbolic, restoration, and endgame icons.

Recommendation: keep existing sprite definitions where possible, but assign sharper route/country icons during rework. Repeated icons are acceptable for repeated shared mechanics, not for identity-defining route payoffs.

## Localisation and reward mismatch list

No missing focus localisation keys were found. The mismatch is semantic: many names/descriptions imply a large political or mechanical shift, while the reward is a flag, variable bump, or helper update.

Priority mismatch patterns:

1. Republic route identity focuses frequently sound like state-defining transformations but only increment institution/recognition/depot/league variables and call `soviet_collapse_update_consolidated_republic_ideas`.
2. Custom splinter identity focuses use evocative country-specific titles but call the same helper families across many countries. This causes the reward surface to feel copy-patterned even when the localisation is distinct.
3. Factory successor focuses, especially CFR and MFR, have strong industrial names but many do not directly add enough factories, building slots, infrastructure, production lines, units, or decisions to meet the "extremely overpowered" design target.
4. Rail, naval, and undead countries have names that promise rail control, fleet warfare, or dead-army conquest, but the focus rewards are not consistently rail/supply hub construction, ships/dockyards/naval invasion tools, war goals, cores, or special units.
5. Some focus filters advertise broad categories like political/stability/army even where the real payoff is hidden in helpers, making the focus browser less useful.

## Focus filter audit

All focuses have `search_filters`, but the distribution shows broad generic tagging:

| Filter | Uses |
|---|---:|
| `FOCUS_FILTER_POLITICAL` | 1040 |
| `FOCUS_FILTER_ARMY_XP` | 734 |
| `FOCUS_FILTER_STABILITY` | 605 |
| `FOCUS_FILTER_INDUSTRY` | 519 |
| `FOCUS_FILTER_MANPOWER` | 182 |
| `FOCUS_FILTER_NAVY_XP` | 46 |
| `FOCUS_FILTER_ANNEXATION` | 41 |
| `FOCUS_FILTER_RESEARCH` | 17 |
| `FOCUS_FILTER_AIR_XP` | 12 |

Issues:

- Expansion/coring/war-goal focuses often lack `FOCUS_FILTER_ANNEXATION` when the effect is hidden in helpers.
- Naval successor and coastal route content does not consistently surface as `FOCUS_FILTER_NAVY_XP`.
- Rail/supply routes do not have a dedicated vanilla focus filter, but their current political/army/stability filter usage does not communicate the intended logistics role.
- Many identity-helper focuses use broad filters even when their visible reward is just route flagging or idea updating.

## AI behavior gaps

`common/ai_strategy/005_soviet_collapse.txt` includes broad crisis strategies, a generic custom/high-chaos signature force route, and route-aware strategy overlays for Ukraine (`:268` through `:431`), Belarus (`:438` through `:573`), and Kazakhstan (`:580` through `:713`). It does not have comparable route-specific coverage for most other Soviet Collapse trees.

Missing or insufficient route-aware AI:

- Baltic shared tree: no clear legal restoration/coastal defense/forest defense/Baltic League route strategy.
- Caucasus shared tree: no clear mountain pass/oil/foreign mediation/Caucasus League strategy.
- Central Asia shared tree: no clear Basmachi, water/rail, border defense, or league strategy.
- Moldova: no clear Dniester defense/Romanian diplomacy/Ukrainian corridor/observer strategy.
- Internal republics: no regionalized AI behavior for Karelia/Komi/Volga-Ural/Crimea/Siberia/Far East/Yakutia/Buryatia/Tuva-style outcomes.
- CFR/MFR/OGB: no route-level construction, arsenal, restored-name, production, or expansion strategy that matches their focus choices.
- PRA/DSC/NRF/TSC/RMC/ICD and most 47-focus custom splinters: mostly rely on generic high-chaos/custom signature AI, not country identity.
- Ancient restorations: no restoration-specific route AI.

Required AI direction:

- Add route flags at real fork nodes and bind `ai_will_do` to route flags.
- Add `ai_strategy` overlays for each major identity: construction build-up, railway logistics, undead conquest, naval invasion/fleet, arsenal production, forest defense, pass defense, league founder/member, foreign patron, and expansion/integration.
- For chaos countries, make aggression explicit and country-specific. DSC should strongly prefer conquest and immediate integration; naval tags should prefer shipbuilding and naval invasion; construction/factory tags should prefer industry and war production.

## High-priority fixes first

1. Reflow Ukraine, Moldova, Kazakhstan, CFR, MFR, BAC, UWD, SZA, and FEV before adding more focuses. The layout risk is already high enough that more content will worsen pathline crossing.
2. Replace helper/idea-update reward spam with visible route mechanics. The first rework pass should target focuses that only call `soviet_collapse_update_consolidated_republic_ideas`, `soviet_collapse_apply_focus_high_chaos_identity`, or repeated custom splinter identity helpers.
3. Rebuild overpowered identity branches for CFR, MFR, PRA, DSC, and NRF. These are the clearest examples from the request and should set the quality bar for other chaos/special countries.
4. Add route-aware AI strategy coverage for every major regional and special tree before calling the rework complete.
5. Reduce mutual exclusions to meaningful lore/strategy choices. Four-way mutually exclusive clusters, especially CFR and MFR, should be collapsed or visually centered unless all choices truly define long-term gameplay.
6. Tie focus payoffs to Soviet Collapse mechanics: release pressure, expansion decisions, league coordination, patronage, terminal collapse, war declarations, coring/integration, factions, unit templates, buildings, and country identity.
7. Re-check focus filters after reward replacement. Filters should match the visible reward category, not the helper wrapper.

## Proposed implementation tranches

Tranche 1: Design and layout foundation

- Choose a compact standard layout for large republic trees: opener trunk, political fork lanes, economy lane, military/diplomacy lane, special/chaos lane, and final payoff row.
- Apply it to Ukraine first because it has the largest crossing count and most route families.
- Define route flags and AI strategy names before adding payoffs.

Tranche 2: Identity proof-of-quality countries

- CFR: direct civilian factory/infrastructure/building slot/supply hub construction, repeatable construction program decisions, construction-corresponding integration.
- PRA: rails, supply hubs, trains, armored trains, rail guard units, rail tolls, rail AI.
- DSC: immediate coring on conquest, many war goals, undead units, no-demobilization economy, high aggression AI.
- NRF: dockyards, convoys, ships, naval invasions, naval AI.
- MFR: military factories, production lines, arsenal guard units, war market/client decisions, production AI.

Tranche 3: Regional republic route systems

- Baltic, Caucasus, Central Asia, Moldova, Belarus, Kazakhstan: replace shared generic payoffs with state-targeted map rewards and decision categories.
- League routes must have founder/member mechanics and AI.
- Patronage routes must have visible sponsor tradeoffs.

Tranche 4: Remaining custom splinters and ancient restorations

- Replace repeated 47-focus helper-template lanes with identity-specific branch families.
- Expand ancient restorations or explicitly document them as compact side trees; if full trees, add distinct restoration/economy/war/diplomacy branches.

## Patch status

No patch.

Reason: the audit did not find a single local focus-tree issue where a tiny patch would materially address the requested outcome. The obvious problems are route architecture, repeated reward design, route-aware AI coverage, and layout reflow. A small coordinate move or helper deletion would be cosmetic and could conflict with the needed full rework.

Changed files:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_200026_soviet_collapse_focus_full_rework_audit_handoff.md`

Changed focus ids:

- None.

Localisation keys and icon ids changed:

- None.

Route behavior before and after:

- Before: existing focus trees remain as currently implemented.
- After: no gameplay behavior changed; this handoff documents the rework requirements and audit evidence.

## Validation run

Audit checks performed:

- Parsed the four focus files and counted focus trees and focus ids.
- Checked duplicate focus ids: none found.
- Checked focus blocks missing `icon`, `ai_will_do`, or `search_filters`: none found.
- Checked English focus localisation keys and `_desc` keys across Event 005 localisation files: no missing keys found.
- Checked assigned focus icon sprite names against `interface/005_soviet_collapse*.gfx`: no missing sprite definitions found.
- Counted direct `add_ideas`, `remove_ideas`, and `swap_ideas` usage in the focus files.
- Counted focus reward helper calls for consolidated idea updates and custom/high-chaos identity helpers.
- Ran a mechanical layout-risk scan for prerequisite-line crossings, line-through-focus risks, and wide mutual-exclusive placement risks.
- Inspected `common/ai_strategy/005_soviet_collapse.txt` for route-aware strategy coverage.
- Inspected related specs/docs and scripted effects enough to understand helper reward surfaces.

Skipped validation:

- No HOI4 runtime load or focus UI screenshot was run. This was an audit-only subagent task with no gameplay patch.
- No validator script was run against the whole dirty repository because unrelated Event 006 and Event 005 files are already modified in the working tree. This handoff avoids changing those files.

## Remaining route risks

- The full rework is not implemented.
- Focus trees are structurally complete but design-incomplete for the requested end state.
- The strongest immediate risk is adding more content without a layout reflow; Ukraine, Moldova, Kazakhstan, CFR, and MFR already show enough pathline/mutual-exclusion risk to make further incremental additions messy.
- The second major risk is preserving the helper-template reward rhythm. If the rework keeps adding identity helper calls without visible decisions, units, buildings, cores, claims, war goals, or route AI, the trees will still feel shallow even with more focus count.
- The third major risk is AI mismatch. Existing focus-level `ai_will_do` is not enough; the route families need persistent AI strategies that match the overpowered country identities.
