# Event005 Soviet Collapse Focus Tree Full-Depth Layout Audit

Date: 2026-06-01
Agent: Chaos Redux focus tree subagent

## Scope and Constraints

Audited files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Explicit asset constraint followed: no files under `gfx/flags`, `interface/flags`, or flag assets were edited. I did not patch any focus, localisation, scripted helper, interface, or asset file.

Reference checks used before audit:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `loc_objects_documentation.md`.
- Vanilla focus precedents: `common/national_focus/soviet.txt`, `common/national_focus/baltic_shared.txt`, vanilla focus loading references.

## Mechanical Audit Summary

- Focus trees audited: 39.
- Focus blocks audited: 1,698.
- Duplicate focus ids: 0 found.
- Missing `ai_will_do`: 0 found.
- Missing `search_filters`: 0 found.
- Missing focus name localisation: 0 found.
- Missing focus description localisation: 0 found.
- Event005 localisation BOM check: all `localisation/english/005_soviet_collapse*.yml` files have UTF-8 BOM.
- Direct `add_ideas` / `add_timed_idea` focus reward spam: 0 current direct calls found.
- Direct `add_equipment_to_stockpile` focus rewards: 163 current focuses.
- Flat `ai_will_do` with no modifier: 351 current focuses.
- Focuses with direct claim/core/wargoal effects: 25 current focuses.

The old direct idea spam has been cleaned up, but helper-effect repetition has replaced it. The most repeated current reward helpers are:

| Count | File | Helper |
| ---: | --- | --- |
| 75 | `common/national_focus/005_soviet_collapse_custom_splinters.txt` | `soviet_collapse_apply_focus_military_consolidation` |
| 73 | `common/national_focus/005_soviet_collapse_custom_splinters.txt` | `soviet_collapse_apply_focus_depot_and_supply_control` |
| 65 | `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_apply_focus_depot_and_supply_control` |
| 63 | `common/national_focus/005_soviet_collapse_custom_splinters.txt` | `soviet_collapse_apply_focus_legal_recognition` |
| 57 | `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_apply_focus_military_consolidation` |
| 53 | `common/national_focus/005_soviet_collapse_custom_splinters.txt` | `soviet_collapse_apply_focus_republican_compact_plan` |

## Route Coverage Table

| File | Tree | Line | Focuses | Required route coverage | Status |
| --- | --- | ---: | ---: | --- | --- |
| republics | `soviet_collapse_ukraine_focus_tree` | 18 | 83 | Political, military, industry, diplomacy, League, Black Sea, expansion | Partial. Deep enough by count, but route layout is tangled and political route locks are not fully visible. |
| republics | `soviet_collapse_breakaway_focus_tree` | 2326 | 36 | Generic political, industry, military, foreign, League | Partial. Usable generic breakaway, but weak identity and no direct expansion focus payload. |
| republics | `soviet_collapse_internal_republic_focus_tree` | 3117 | 62 | Regional development, survival, league, military, local economy | Partial. Broad regional coverage, but many one-building/development ladders are not mechanics. |
| republics | `soviet_collapse_baltic_focus_tree` | 4583 | 42 | Legal restoration, military, League, foreign protection, coastal/forest defense | Partial. Has routes, but row-3 mutual exclusions span through other route choices. |
| republics | `soviet_collapse_caucasus_focus_tree` | 5541 | 40 | Oil, mountain defense, national restoration, diplomacy, expansion | Partial. The oil/pass identity mostly resolves as stockpile/building/helper rewards. |
| republics | `soviet_collapse_central_asia_focus_tree` | 6446 | 45 | Republic/federation, desert/mountain defense, oasis economy, southern pact | Partial. Some claims exist, but industry/development is still a ladder. |
| republics | `soviet_collapse_moldova_focus_tree` | 7566 | 48 | Dniester/Prut survival, Romanian/Ukraine roads, neutrality, river defense | Partial. More route detail than most, but route row has crossing mutual exclusions. |
| republics | `soviet_collapse_belarus_focus_tree` | 8710 | 53 | Rail, forest, corridor, national/socialist/military/foreign routes, League | Partial. Real routes exist, but route selectors are too close/crossed and no direct expansion route exists. |
| republics | `soviet_collapse_kazakhstan_focus_tree` | 10013 | 92 | Steppe politics, resources, Alash/socialist/military/foreign, Central Asia League | Partial. Strong by count, but 61 flat AI weights and only indirect expansion behavior. |
| custom splinters | `FTH_soviet_collapse_focus_tree` | 15 | 47 | Anarchist Ukraine successor politics, military, economy, diplomacy, endgame | Partial. Real-sized tree, no direct claim/core/wargoal and repeated template helpers. |
| custom splinters | `PRA_soviet_collapse_focus_tree` | 1201 | 22 | Rail authority, corridor economy, military rail state, expansion | Shallow. Good rail variables/decisions, but too small for a high-chaos rail state. |
| custom splinters | `TSC_soviet_collapse_focus_tree` | 1787 | 18 | Tunguska science/laboratory state, perimeter, signal/sky mechanics, expansion | Shallow. Lacks a living science/special-project loop. |
| custom splinters | `RMC_soviet_collapse_focus_tree` | 2254 | 18 | Reliquary/resurrection cult, dead volunteers, coercion, expansion | Shallow. Lore payoff is mostly ordinary support-equipment and helper rewards. |
| custom splinters | `DSC_soviet_collapse_focus_tree` | 2728 | 18 | Dead soldier congress, veteran/dead army sovereignty, aggressive routes | Shallow. Has decision hooks, but focus tree is compressed. |
| custom splinters | `NRF_soviet_collapse_focus_tree` | 3300 | 18 | Revenant fleet, ports, dockyards, convoy authority, naval expansion | Shallow. Naval identity is stronger than its direct mechanics. |
| custom splinters | `ICD_soviet_collapse_focus_tree` | 3797 | 18 | Death commissariat, coercive politics, memorial mobilization, expansion | Shallow. Needs coercive state mechanics, not support-equipment ladders. |
| custom splinters | `BSC_soviet_collapse_focus_tree` | 4262 | 47 | Basmachi route, raids, mountain/desert expansion, autonomy | Partial. No direct claim/core/wargoal and 7 stockpile rewards. |
| custom splinters | `TNC_soviet_collapse_focus_tree` | 5381 | 47 | Turkestan national route, city militia, regional ambition | Partial. No direct expansion and few decision hooks. |
| custom splinters | `ALA_soviet_collapse_focus_tree` | 6510 | 47 | Alash restoration, steppe defense, southern/eastern diplomacy | Partial. No direct expansion and template-helper heavy. |
| custom splinters | `BBH_soviet_collapse_focus_tree` | 7619 | 47 | Black banner host, column warfare, stateless/revolutionary route | Partial. No direct expansion and 6 stockpile rewards. |
| custom splinters | `KRS_soviet_collapse_focus_tree` | 8808 | 47 | Kronstadt soviet, naval/port worker state, anti-party route | Partial. No direct expansion and 6 stockpile rewards. |
| custom splinters | `UDC_soviet_collapse_focus_tree` | 10034 | 47 | Ukrainian directorate/custom successor branch | Partial. Hidden route locks and no direct expansion. |
| custom splinters | `SDZ_soviet_collapse_focus_tree` | 11218 | 47 | Security/custody successor branch | Partial. Hidden route locks and no direct expansion. |
| custom splinters | `GAC_soviet_collapse_focus_tree` | 12452 | 47 | Grain/agriculture successor branch | Partial. Hidden route locks and no direct expansion. |
| custom splinters | `DHC_soviet_collapse_focus_tree` | 13622 | 47 | Dnieper/host/convoy identity | Partial. Hidden route locks, no direct expansion, 7 stockpile rewards. |
| custom splinters | `KHC_soviet_collapse_focus_tree` | 14821 | 47 | Kuban/host/grain route | Partial. Worst current stockpile tree with 11 stockpile rewards. |
| custom splinters | `FEV_soviet_collapse_focus_tree` | 16010 | 47 | Far Eastern revival, harbor/rail diplomacy, eastern patronage | Partial. No direct expansion, 12 flat AI weights. |
| custom splinters | `SZA_soviet_collapse_focus_tree` | 17173 | 47 | Siberian zemstvo, river/rail/settlement route | Partial. No direct expansion, 13 flat AI weights. |
| custom splinters | `UWD_soviet_collapse_focus_tree` | 18338 | 47 | Ural workers/directorate, heavy industry, defense | Partial. No direct expansion, 8 stockpile rewards. |
| custom splinters | `MRC_soviet_collapse_focus_tree` | 19525 | 47 | Mountain republic, pass guards, Caucasus diplomacy | Partial. No direct expansion, 9 flat AI weights. |
| custom splinters | `IUL_soviet_collapse_focus_tree` | 20698 | 47 | Idel-Ural league, Volga politics, federation/compact | Partial. No direct expansion, 6 stockpile rewards. |
| custom splinters | `BAC_soviet_collapse_focus_tree` | 21840 | 47 | Birobidzhan commune, Amur defense, commune settlement | Partial. No direct expansion, 7 stockpile rewards. |
| custom splinters | `ARD_soviet_collapse_focus_tree` | 22975 | 47 | Arctic directorate, ports/convoys, league/rival route | Partial. No direct expansion, 11 stockpile rewards. |
| custom splinters | `NLC_soviet_collapse_focus_tree` | 24176 | 47 | Northern league/commune, ports, polar endgame | Partial. No direct expansion, 7 stockpile rewards. |
| factory successors | `CFR_soviet_collapse_focus_tree` | 16 | 47 | Construction state, governance fork, strategy fork, rebuild/war | Mostly present. Strongest mechanic integration, but visible route-lock presentation still needs cleanup. |
| factory successors | `OGB_soviet_collapse_focus_tree` | 1140 | 23 | Old Great Bolghar, Volga trade, Idel-Ural question, restoration war | Shallow. Better than before, but too compact for a lore-heavy high-chaos successor. |
| factory successors | `MFR_soviet_collapse_focus_tree` | 1746 | 58 | Military factory state, arms economy, foreign contracts, arsenal war | Mostly present. Good depth, but route locks are hidden and payoff polish remains. |
| ancient restorations | `KZR_soviet_collapse_ancient_focus_tree` | 13 | 16 | Khazar toll/Volga restoration, trade, military, diplomacy, expansion | Shallow. Has claims/endpoints but not full politics/economy/military/diplomacy branches. |
| ancient restorations | `SOG_soviet_collapse_ancient_focus_tree` | 395 | 16 | Sogdian city league, Silk Road commerce, expansion | Shallow. Stub-depth restoration. |
| ancient restorations | `KHW_soviet_collapse_ancient_focus_tree` | 778 | 16 | Khwarazm water/canal authority, oasis economy, expansion | Shallow. Water law should be a mechanic, not a compact ladder. |
| ancient restorations | `ALN_soviet_collapse_ancient_focus_tree` | 1164 | 16 | Alan pass principality, mountain roads, expansion | Shallow. Pass control needs missions/claims/integration beyond 16 focuses. |

## High-Priority Findings and Suggested Patch Groups

### P0 - Ancient Restoration Trees Are Stub-Depth

Files and ids:

- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:13` `KZR_soviet_collapse_ancient_focus_tree`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:395` `SOG_soviet_collapse_ancient_focus_tree`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:778` `KHW_soviet_collapse_ancient_focus_tree`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1164` `ALN_soviet_collapse_ancient_focus_tree`

Evidence:

- Each tree has 16 focuses.
- Each tree has only one symbolic/expansion fork and a short endpoint chain.
- Flat AI weights dominate: 12 flat `ai_will_do` blocks in each ancient tree.
- Repeated generic ancient icons occur across all four trees: `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_guard_old_routes`, `GFX_focus_soviet_collapse_ancient_league_bargain`, `GFX_focus_soviet_collapse_ancient_old_border_files`, `GFX_focus_soviet_collapse_ancient_symbolic_state`, `GFX_focus_soviet_collapse_ancient_restoration_survives`, and `GFX_focus_soviet_collapse_ancient_returned_names_endgame`.

Reward mismatch examples:

- `KZR_returned_names_endgame` at `005_soviet_collapse_ancient_restorations.txt:332`, loc at `005_soviet_collapse_custom_countries_l_english.yml:3666`, promises old roads and hardline charter but mainly calls generic assault/claim helpers.
- `SOG_returned_names_endgame` at `005_soviet_collapse_ancient_restorations.txt:715`, loc at `005_soviet_collapse_custom_countries_l_english.yml:3698`, promises Silk Road expansion but is a compact endpoint.
- `KHW_returned_names_endgame` at `005_soviet_collapse_ancient_restorations.txt:1101`, loc at `005_soviet_collapse_custom_countries_l_english.yml:3730`, promises water law into wider claim but lacks an irrigation/river authority loop.
- `ALN_returned_names_endgame` at `005_soviet_collapse_ancient_restorations.txt:1481`, loc at `005_soviet_collapse_custom_countries_l_english.yml:3762`, promises highland-road claims but lacks pass-control missions.

Suggested patch group:

- Write an ancient-restoration expansion plan first, then implement as a parent tranche. Add politics, state economy, military order, diplomacy, expansion, and postwar/integration routes for each ancient tree. Do not create a new formable chain unless explicitly approved. Use existing returned-name/old-claim decisions if possible.

### P0 - Shallow High-Chaos/Special Trees Do Not Match Lore or Power Target

Files and ids:

- `PRA_soviet_collapse_focus_tree` at `005_soviet_collapse_custom_splinters.txt:1201`, 22 focuses.
- `TSC_soviet_collapse_focus_tree` at `005_soviet_collapse_custom_splinters.txt:1787`, 18 focuses.
- `RMC_soviet_collapse_focus_tree` at `005_soviet_collapse_custom_splinters.txt:2254`, 18 focuses.
- `DSC_soviet_collapse_focus_tree` at `005_soviet_collapse_custom_splinters.txt:2728`, 18 focuses.
- `NRF_soviet_collapse_focus_tree` at `005_soviet_collapse_custom_splinters.txt:3300`, 18 focuses.
- `ICD_soviet_collapse_focus_tree` at `005_soviet_collapse_custom_splinters.txt:3797`, 18 focuses.

Evidence and exact weak rewards:

- `TSC_portable_laboratory_trains` at `005_soviet_collapse_custom_splinters.txt:1909`, loc at `005_soviet_collapse_custom_countries_l_english.yml:3277`, adds infantry equipment and a field-station depth helper, not a science/lab mechanic.
- `RMC_dead_volunteer_columns` at `005_soviet_collapse_custom_splinters.txt:2492`, loc at `005_soviet_collapse_custom_countries_l_english.yml:3415`, adds support-equipment style payload and reliquary depth, not distinctive resurrection-cult recruitment.
- `DSC_congress_of_the_dead_army` at `005_soviet_collapse_custom_splinters.txt:3220`, loc at `005_soviet_collapse_custom_countries_l_english.yml:3500`, is an endpoint conceptually big enough for a state-power loop, but the tree is only 18 focuses.
- `NRF_northern_revenant_fleet` at `005_soviet_collapse_custom_splinters.txt:3736`, loc at `005_soviet_collapse_custom_countries_l_english.yml:3565`, promises ports, convoy routes, dockyards, and shore parties, but the tree only has one direct claim/wargoal cluster and 5 stockpile focuses.
- `ICD_commissariat_without_end` at `005_soviet_collapse_custom_splinters.txt:4202`, loc at `005_soviet_collapse_custom_countries_l_english.yml:3364`, promises a death-state commissariat but the branch around `ICD_penza_memorial_workshops` `:3847`, `ICD_black_seal_requisitions` `:3957`, `ICD_memorial_battalions` `:4031`, and `ICD_letters_to_grieving_cities` `:4087` is support-equipment/building heavy.
- `PRA_the_pale_line_endures` at `005_soviet_collapse_custom_splinters.txt:1755`, loc at `005_soviet_collapse_custom_countries_l_english.yml:3240`, promises a corridor authority, but the entire tree is still 22 focuses despite better rail variables and decision hooks.

Suggested patch group:

- Expand these as identity mechanics, not focus count padding. Priority mechanics: PRA rail authority/corridor tolls, TSC laboratory/signal pressure, RMC reliquary recruitment and martyr roll missions, DSC dead-army mobilization, NRF revenant fleet/naval port system, ICD coercive memorial commissariat.

### P1 - Most 47-Focus Custom Splinters Lack Direct Expansion Mechanics

Affected trees:

- `FTH` at `005_soviet_collapse_custom_splinters.txt:15`
- `BSC` at `:4262`
- `TNC` at `:5381`
- `ALA` at `:6510`
- `BBH` at `:7619`
- `KRS` at `:8808`
- `UDC` at `:10034`
- `SDZ` at `:11218`
- `GAC` at `:12452`
- `DHC` at `:13622`
- `KHC` at `:14821`
- `FEV` at `:16010`
- `SZA` at `:17173`
- `UWD` at `:18338`
- `MRC` at `:19525`
- `IUL` at `:20698`
- `BAC` at `:21840`
- `ARD` at `:22975`
- `NLC` at `:24176`

Evidence:

- All listed 47-focus custom splinter trees currently show 0 direct focus blocks with claim/core/wargoal payloads in the mechanical parse.
- Top stockpile-heavy custom trees: `KHC` 11, `ARD` 11, `UWD` 8, `BSC` 7, `GAC` 7, `DHC` 7, `FEV` 7, `BAC` 7, `NLC` 7.
- Many route endings are named as settlement/radical/endurance choices, but they resolve through repeated helpers rather than claims, cores, war goals, missions, protectorates, or postwar settlement.

Layout/route-lock examples:

- `UDC_settlement` `:11008` vs `UDC_radical_turn` `:11044` has `UDC_loyalist_statute_guarantees` between them on the same row.
- `SDZ_settlement` `:12237` vs `SDZ_radical_turn` `:12273` has `SDZ_chain_of_custody_statutes` between them.
- `GAC_settlement` `:13420` vs `GAC_radical_turn` `:13456` has `GAC_harvest_truce_guarantees` between them.
- `DHC_settlement` `:14534` vs `DHC_radical_turn` `:14570` has `DHC_convoy_autonomy_guarantees` between them.
- `KHC_settlement` `:15725` vs `KHC_radical_turn` `:15761` has `KHC_grain_passage_guarantees` between them.

Suggested patch group:

- Pick the 10 worst custom splinters first: `KHC`, `ARD`, `UWD`, `BSC`, `GAC`, `DHC`, `FEV`, `BAC`, `NLC`, `KRS`. Replace stockpile/helper endpoints with direct route mechanics: claims/war goals where lore supports it, identity units, targeted decisions, League/rival consequences, and aggressive AI strategies.

### P1 - Ukraine Is Not Linear, But Its Route Locks and Layout Are Ugly

File: `common/national_focus/005_soviet_collapse_republics.txt`

Relevant focus ids and lines:

- `ukr_soviet_collapse_socialist_republic_without_moscow` at `:234`
- `ukr_soviet_collapse_black_banner_compact` at `:271`
- `ukr_soviet_collapse_elections_under_shellfire` at `:314`
- `ukr_soviet_collapse_officers_above_parties` at `:540`
- `ukr_soviet_collapse_protectorate_debate` at `:1699`

Evidence:

- The five main route selectors are split across very distant y positions: four are on y=5, while `ukr_soviet_collapse_protectorate_debate` is at `:1699`.
- Several route locks are enforced by hidden `has_completed_focus` checks instead of complete visible mutual exclusion pairs. Examples:
  - `ukr_soviet_collapse_socialist_republic_without_moscow` hides `ukr_soviet_collapse_officers_above_parties` and `ukr_soviet_collapse_protectorate_debate` at `:247` and `:250` without visible mutual exclusions.
  - `ukr_soviet_collapse_black_banner_compact` hides `ukr_soviet_collapse_officers_above_parties` and `ukr_soviet_collapse_elections_under_shellfire` at `:291-292`.
  - `ukr_soviet_collapse_elections_under_shellfire` hides `ukr_soviet_collapse_black_banner_compact` and `ukr_soviet_collapse_protectorate_debate` at `:329-330`.
  - `ukr_soviet_collapse_officers_above_parties` hides socialist, black-banner, and protectorate routes at `:553-555`.
- Same-row visible mutual-exclusion spans:
  - `ukr_soviet_collapse_black_banner_compact` `:271` vs `ukr_soviet_collapse_socialist_republic_without_moscow` `:234`, y=5, x span 4.
  - `ukr_soviet_collapse_elections_under_shellfire` `:314` vs `ukr_soviet_collapse_officers_above_parties` `:540`, y=5, x span 4.
- The route layout mixes political, military, and foreign protectorate lanes, making the tree read like disconnected ladders despite having 83 focuses.

Suggested patch group:

- Do a layout-only route selector cleanup first. Keep all current route logic, but make the five route choices visible in one coherent cluster with complete visible mutual exclusions or clear custom tooltips. Then do a reward-pass that gives each route a distinct government/advisor/law/decision/AI outcome.

### P1 - Belarus Route Row Is Too Tight and Crosses Itself

File: `common/national_focus/005_soviet_collapse_republics.txt`

Relevant focus ids and lines:

- `blr_soviet_collapse_which_road_is_belarus` at `:8796`
- `blr_soviet_collapse_national_council_of_minsk` at `:8880`, x=7, y=5
- `blr_soviet_collapse_socialist_autonomy_without_moscow` at `:8911`, x=12, y=5
- `blr_soviet_collapse_military_transit_directorate` at `:8944`, x=18, y=5
- `blr_soviet_collapse_foreign_corridor_administration` at `:8976`, x=25, y=5
- `blr_soviet_collapse_decentralized_detachments` at `:9515`, x=27, y=11
- `blr_soviet_collapse_regular_forest_brigades` at `:9541`, x=21, y=11
- `blr_soviet_collapse_prepare_league_freight_tables` at `:9666`
- `blr_soviet_collapse_join_the_league_when_war_comes` at `:9695`

Evidence:

- The four main route selectors all sit on y=5 with spans up to 18 columns and mutual exclusions across intervening choices.
- `blr_soviet_collapse_foreign_corridor_administration` to `blr_soviet_collapse_national_council_of_minsk` spans x=25 to x=7 with two route focuses between them.
- The forest pair at `:9515` / `:9541` is a same-row mutual exclusion with x span 6, which is readable but still tight in the already crowded forest branch.
- `blr_soviet_collapse_which_road_is_belarus` uses one `prerequisite = { focus = rail focus = forest focus = corridor }` block at `:8802-8806`, which is OR by HOI4 semantics, then an `available` block at `:8807-8822` requiring two of the three. This is probably intentional, but it creates confusing pathline semantics.

Suggested patch group:

- Layout patch only: spread the route selectors vertically or diagonally, keep a single visible choice cluster, and replace confusing OR prerequisite plus two-of-three `available` presentation with clearer route tooltiping if the design must remain two-of-three.

### P1 - OGB Is Still Too Compact for a High-Chaos Restoration

File: `common/national_focus/005_soviet_collapse_factory_successors.txt`

Relevant focus ids and lines:

- Tree start `OGB_soviet_collapse_focus_tree` at `:1140`, 23 focuses.
- `OGB_open_the_volga_registers` at `:1157`
- `OGB_scholars_guard_the_charter` at `:1219`
- `OGB_clerics_guard_the_charter` at `:1239`
- `OGB_reopen_volga_trade_tolls` at `:1259`
- `OGB_the_volga_cannot_have_two_seals` at `:1497`
- `OGB_claim_the_old_trade_cities` at `:1583`
- `OGB_volga_restoration_state` at `:1682`
- `OGB_the_old_name_survives_modern_war` at `:1705`

Evidence:

- OGB does have Volga legitimacy, river authority, Idel-Ural compact/rivalry, claims, and endgame wargoal hooks now.
- It is still only 23 focuses and lacks enough branch depth for a restoration identity comparable to the bigger high-chaos successors.
- Several branch focuses are gated by hidden checks for the scholar/cleric fork rather than visible continuation routing, e.g. `OGB_reopen_volga_trade_tolls` `:1265-1269`, `OGB_friday_schools_and_court_records` `:1338-1342`, and `OGB_raise_the_heritage_guard` `:1404-1408`.

Suggested patch group:

- Add a bounded OGB depth tranche: scholar vs cleric politics, Volga trade toll decisions, Idel-Ural treaty/rival aftermath, old trade city integration, and a final restoration ambition. This is broader than a safe subagent patch.

### P2 - Factory Successor Route Locks Are Functionally Safer Than Before, But Still Too Hidden

File: `common/national_focus/005_soviet_collapse_factory_successors.txt`

Relevant focus ids and lines:

- CFR governance fork:
  - `CFR_elect_the_site_committees` at `:133`
  - `CFR_publish_the_planners_charter` at `:161`
  - `CFR_invite_the_foreign_contract_board` at `:191`
  - `CFR_the_concrete_committee` at `:220`
- CFR strategy fork:
  - `CFR_cities_first` at `:349`
  - `CFR_rails_first` at `:379`
  - `CFR_factories_first` at `:419`
  - `CFR_contracts_first` at `:452`
- MFR route fork:
  - `MFR_officers_chair_the_board` at `:1877`
  - `MFR_armorers_elect_delegates` at `:1905`
  - `MFR_merchants_of_ammunition` at `:1932`
  - `MFR_eternal_arsenal` at `:1962`

Evidence:

- These route sets use partial visible mutual exclusions plus hidden `has_completed_focus` gates. The player sees some conflicts but not the full exclusivity logic.
- CFR and MFR are mechanically stronger than most trees, so this is not a rewrite blocker. It is a route readability issue.

Suggested patch group:

- Small focus-file patch is possible: add complete visible mutual exclusions where layout can tolerate it, or add custom route lock tooltips to the selector focuses. Avoid changing rewards until parent chooses broader route polish.

## Icon Coverage Table

| File | Focuses | Missing icon assignments | Unique icon ids | Repeated icon ids | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 501 | 0 | 458 | 22 | Repeats include `GFX_focus_soviet_collapse_guard_the_radio_stations` x4, `GFX_ukr_soviet_collapse_democratic` x4, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow` x4. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | 885 | 99 | Many repeated per-tag template icons such as `*_legitimacy`, `*_doctrine`, `*_civil_rule`, `*_war_plan`, and `*_diplomatic_plan`. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | 113 | 11 | CFR repeats several construction identity icons 2-3 times. |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | 42 | 8 | Ancient trees visibly reuse generic ancient icon families across all four trees. |

Icon conclusion: no missing focus icon assignments from focus files, but repeated icons reinforce the template/stub feeling. Any icon refresh must not touch flag folders.

## Localisation and Reward Mismatch List

Localisation coverage is complete, but several titles/descriptions promise more than the reward payload currently delivers.

| Severity | File:line | Focus id | Localisation line | Mismatch |
| --- | --- | --- | --- | --- |
| P0 | `custom_splinters.txt:1909` | `TSC_portable_laboratory_trains` | `005_soviet_collapse_custom_countries_l_english.yml:3277` | Moving research state text needs a lab/signal/special-project loop, not infantry equipment plus field-station depth. |
| P0 | `custom_splinters.txt:2492` | `RMC_dead_volunteer_columns` | `005_soviet_collapse_custom_countries_l_english.yml:3415` | Dead volunteer concept needs recruitment/memorial/route mechanics, not a support-equipment style reward. |
| P0 | `custom_splinters.txt:3736` | `NRF_northern_revenant_fleet` | `005_soviet_collapse_custom_countries_l_english.yml:3565` | Text promises ports, convoy routes, dockyards, and shore parties; focus tree is too compact and stockpile-heavy. |
| P0 | `custom_splinters.txt:4202` | `ICD_commissariat_without_end` | `005_soviet_collapse_custom_countries_l_english.yml:3364` | Death-commissariat sovereignty needs coercive state and expansion mechanics. |
| P0 | `ancient_restorations.txt:332` | `KZR_returned_names_endgame` | `005_soviet_collapse_custom_countries_l_english.yml:3666` | Old roads/charter payoff should unlock trade/integration/claim play beyond generic helpers. |
| P0 | `ancient_restorations.txt:1101` | `KHW_returned_names_endgame` | `005_soviet_collapse_custom_countries_l_english.yml:3730` | Water law and delta identity should become an irrigation/river authority mechanic. |
| P1 | `custom_splinters.txt:1755` | `PRA_the_pale_line_endures` | `005_soviet_collapse_custom_countries_l_english.yml:3240` | Corridor authority text is good, but the tree is too short and needs stronger rail-state expansion. |
| P1 | `republics.txt:8880` | `blr_soviet_collapse_national_council_of_minsk` | `005_soviet_collapse_blr_focus_l_english.yml:19` | Political route title is distinct, but the surrounding route cluster is visually crowded and mechanically helper-led. |
| P1 | `republics.txt:1699` | `ukr_soviet_collapse_protectorate_debate` | `005_soviet_collapse_l_english.yml:1361` | Protectorate route is far from the primary route selector row and hidden-locked against it. |

## AI Behavior Gaps

- All focuses have `ai_will_do`, but 351 focus blocks are flat with no modifier.
- Biggest flat-AI counts by tree:
  - `soviet_collapse_kazakhstan_focus_tree`: 61 flat AI focuses.
  - `soviet_collapse_ukraine_focus_tree`: 27 flat AI focuses.
  - `soviet_collapse_internal_republic_focus_tree`: 25 flat AI focuses.
  - `soviet_collapse_caucasus_focus_tree`: 23 flat AI focuses.
  - `soviet_collapse_moldova_focus_tree`: 20 flat AI focuses.
  - Each ancient tree: 12 flat AI focuses.
- The republic file has 501 focuses but 0 direct aggressive AI strategy focus rewards.
- The 47-focus custom splinters mostly have 0 direct claim/core/wargoal payloads and no direct aggressive focus rewards, despite being high-chaos successors.
- Factory successor AI is better: CFR, OGB, and MFR include direct `add_ai_strategy` and wargoal hooks at endpoint focuses such as `CFR_rebuild_russia_without_moscow` `factory_successors.txt:1114`, `OGB_the_old_name_survives_modern_war` `:1705`, and `MFR_eternal_arsenal` `:1962`.

Suggested AI patch groups:

- Add route-aware AI to Ukraine/Belarus/Kazakhstan selectors based on stability, war with SOV, foreign appetite, old movement pressure, League membership, and chaos tier.
- Give ancient and special high-chaos endpoints strategic AI arcs before the endpoint, not only final aggression.
- For each custom splinter tranche, add direct aggressive AI only where the route has claims/wargoals or an existing decision war plan.

## Missing or Simplified Content List

High priority:

- Ancient restorations lack full political/industrial/military/diplomatic/expansion branches: `KZR`, `SOG`, `KHW`, `ALN` at `ancient_restorations.txt:13`, `:395`, `:778`, `:1164`.
- Special chaos trees are underpowered or under-expressed: `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` at `custom_splinters.txt:1201`, `:1787`, `:2254`, `:2728`, `:3300`, `:3797`.
- OGB remains a compact 23-focus restoration tree at `factory_successors.txt:1140`.
- Ukraine route logic is deep but visually ugly and route locks are partially hidden: `republics.txt:234`, `:271`, `:314`, `:540`, `:1699`.
- Belarus route selectors are too close and mutually exclusive lines span unrelated choices: `republics.txt:8880`, `:8911`, `:8944`, `:8976`.
- 47-focus custom splinters frequently have branch labels without direct expansion, integration, protectorate, or postwar settlement mechanics.

Medium priority:

- Shared regional trees still lean on development/reward ladders: internal republics `republics.txt:3117`, Baltic `:4583`, Caucasus `:5541`, Central Asia `:6446`, Moldova `:7566`.
- Several focus route selectors use hidden lock semantics when visible mutual exclusions or route-lock tooltips would be clearer.
- Repeated icons and repeated helper names create a template feeling even when focus ids/localisation are unique.

## Suggested Parent Patch Groups

1. Ancient restoration expansion plan and implementation: `KZR/SOG/KHW/ALN`.
2. Special shallow chaos expansion: `PRA/TSC/RMC/DSC/NRF/ICD`.
3. OGB compact restoration expansion.
4. Ukraine layout and route-lock visibility pass.
5. Belarus route layout pass.
6. Kazakhstan route-aware AI and payoff pass.
7. Shared regional republic development-to-mechanics pass.
8. Ten worst template custom splinter reward pass: `KHC/ARD/UWD/BSC/GAC/DHC/FEV/BAC/NLC/KRS`.
9. Icon repeat/art request plan, excluding all flag assets.
10. Final validation after patches: bracket parse, duplicate focus ids, missing localisation, icon assignments, unsupported operators, focus filter presence, pathline screenshot/manual layout review.

## Validation Run

Commands run:

- `rg --files` over Event005 specs, plans, national focus, decision, idea, localisation, interface, scripted-effect surfaces while excluding flag folders.
- Mechanical parse of all four Event005 focus files for tree counts, focus ids, icons, prerequisites, mutual exclusions, rewards, helper calls, stockpile rewards, claims/cores/wargoals, flat AI weights, and same-row mutual-exclusion span risks.
- Localisation parse of `localisation/english/005_soviet_collapse*.yml` for focus name/description coverage and UTF-8 BOM presence.
- Targeted `nl -ba` inspections for Ukraine, Belarus, PRA, OGB, and shallow chaos tree focus blocks.

Skipped validation:

- No HOI4 runtime validation was run.
- No Playwright/screenshot layout check was run.
- No `.gfx` sprite-definition audit was performed beyond focus-file icon assignment counts.
- No flag paths were inspected or changed because flags are explicitly out of scope.

## Patch Status

No gameplay patch was made. This audit writes only this report.

Changed files:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_01_focus_tree_full_depth_layout_audit.md`

Remaining route risks:

- Broad focus-depth work remains open and should be done by the parent agent or a bounded implementation tranche, not by this audit subagent.
- Any future focus edits that add icons must keep flag assets untouched and route icon work through the non-flag focus/idea icon workflow.
