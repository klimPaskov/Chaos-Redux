# Event 005 Soviet Collapse Focus Current-State Audit

Date: 2026-05-30
Mode: audit-only focus-tree subagent
Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse*.yml`

Flags and flag assets were not touched.

## Result

No gameplay patch was made. The current files pass the basic mechanical checks I ran, but they still fail the requested design bar in several places: repeated helper-led rewards, shallow special trees, insufficient country-specific aggression for some high-chaos successors, route-aware AI gaps outside Ukraine/Belarus/Kazakhstan, and severe pathline crossing clusters.

Changed files:
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_092942_event005_soviet_collapse_focus_current_state_audit.md`

Changed focus ids:
- None.

Route behavior before and after:
- Before: current Event 005 focus trees as already present in the dirty worktree.
- After: unchanged.

Localisation keys and icon ids changed:
- None.

## Route Coverage Table

| Required route or surface | Implemented tree/branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine major successor: politics, industry, military, diplomacy, expansion, League/Black Sea/Bread-State hooks | `soviet_collapse_ukraine_focus_tree`, `005_soviet_collapse_republics.txt:18`, 83 focuses | Partial | Strong focus count and 16 direct hook focuses, but 58 helper-without-direct-hook rewards, 47 small/no-direct-hook reward focuses, and 153 crossing risks. Needs route reflow and more visible payoff per route. |
| Generic breakaway republic baseline | `soviet_collapse_breakaway_focus_tree`, `005_soviet_collapse_republics.txt:2370`, 36 focuses | Simplified | 0 direct hook focuses, 31 helper-without-direct-hook rewards, 22 small/no-direct-hook reward focuses. Functions as a survival ladder, not a full political/industrial/expansion tree. |
| Internal republics | `soviet_collapse_internal_republic_focus_tree`, `005_soviet_collapse_republics.txt:3167`, 62 focuses | Simplified | 2 direct hook focuses, 58 helper-without-direct-hook rewards, 41 small/no-direct-hook reward focuses. Needs regional decision/mechanic payoffs. |
| Baltic shared tree | `soviet_collapse_baltic_focus_tree`, `005_soviet_collapse_republics.txt:4671`, 42 focuses | Partial | Legal/military/League labels exist, but only 1 direct hook focus and 18 base-only AI blocks. Needs legal restoration, coastal defense, forest defense, and Baltic League strategy/payoffs. |
| Caucasus shared tree | `soviet_collapse_caucasus_focus_tree`, `005_soviet_collapse_republics.txt:5635`, 40 focuses | Partial | Oil/mountain/foreign/ancient labels exist, but only 2 direct hook focuses and 23 base-only AI blocks. Needs oilfield, mountain-pass, and defense compact mechanics. |
| Central Asia shared tree | `soviet_collapse_central_asia_focus_tree`, `005_soviet_collapse_republics.txt:6562`, 45 focuses | Partial | Basmachi, water/rail, cotton, and southern shield concepts exist. 4 direct hook focuses but 40 helper-without-direct-hook rewards and 24 crossing risks. |
| Moldova | `soviet_collapse_moldova_focus_tree`, `005_soviet_collapse_republics.txt:7707`, 48 focuses | Partial, layout risk | 2 direct hook focuses, 35 small/no-direct-hook rewards, 91 crossing risks. Dniester/Prut/Ukraine/Romania routes need reflow and decision integration. |
| Belarus | `soviet_collapse_belarus_focus_tree`, `005_soviet_collapse_republics.txt:8868`, 53 focuses | Partial | 4 direct hook focuses and route AI exists, but 46 helper-without-direct-hook rewards and 33 crossing risks remain. Corridor/forest/rail branches need stronger mechanics. |
| Kazakhstan | `soviet_collapse_kazakhstan_focus_tree`, `005_soviet_collapse_republics.txt:10199`, 92 focuses | Partial, major layout risk | Largest tree. 4 direct hook focuses, 74 helper-without-direct-hook rewards, 66 small/no-direct-hook rewards, 61 base-only AI blocks, 120 crossing risks, 13 line-through-node risks. |
| Full custom splinters | `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` in `005_soviet_collapse_custom_splinters.txt` | Partial | Most are 47-focus templates. Many have only 2-5 direct hook focuses and 31-43 helper-without-direct-hook rewards. Country text is distinct but reward structure is heavily cloned. |
| Pale Railway Authority | `PRA_soviet_collapse_focus_tree`, `005_soviet_collapse_custom_splinters.txt:1216`, 22 focuses | Better compact tree, still short | 12 direct hook focuses and real railway decisions. Still 10 small/no-direct-hook rewards; OP rail state should get stronger rail-junction claims, rail guard units, armored trains, and rail AI. |
| Dead Soldiers Congress | `DSC_soviet_collapse_focus_tree`, `005_soviet_collapse_custom_splinters.txt:2773`, 18 focuses | Better compact tree, too short | 8 direct hook focuses and aggressive effects exist. Still 18 focuses is thin for a death-state; needs more conquest/coring/no-demobilization economy and route-specific AI. |
| Northern Revenant Fleet | `NRF_soviet_collapse_focus_tree`, `005_soviet_collapse_custom_splinters.txt:3370`, 18 focuses | Better compact tree, too short | 7 direct hook focuses and naval claims exist. Needs more dockyard/ship/naval-invasion/port-control mechanics and naval AI. |
| Other crisis splinters | `TSC`, `RMC`, `ICD` in `005_soviet_collapse_custom_splinters.txt` | Simplified | 18 focuses each. TSC has only 1 direct hook focus; RMC/ICD have 3. Needs either documented crisis-tree status or deeper special mechanics. |
| Factory successors | `CFR`, `MFR`, `OGB` in `005_soviet_collapse_factory_successors.txt` | Mixed | CFR and MFR are now larger and more mechanical. OGB remains 23 focuses and needs route depth. |
| CFR construction directorate | `CFR_soviet_collapse_focus_tree`, `005_soviet_collapse_factory_successors.txt:16`, 47 focuses | Partial | Stronger than earlier: direct SOV war goals at `CFR_the_builder_state_marches_east` and `CFR_rebuild_russia_without_moscow`. Still many governance/strategy branches are locked four-way and need distinct operating-model payoffs. |
| MFR arsenal state | `MFR_soviet_collapse_focus_tree`, `005_soviet_collapse_factory_successors.txt:1776`, 58 focuses | Partial | Stronger than earlier: 7 direct hook focuses and final SOV war goal. Needs route-level arsenal/production AI and more distinct officer/delegate/merchant/eternal arsenal gameplay. |
| OGB restored Volga state | `OGB_soviet_collapse_focus_tree`, `005_soviet_collapse_factory_successors.txt:1171`, 23 focuses | Simplified | 5 direct hook focuses, but still narrow for an OP high-chaos restoration. `OGB_kazan_ferry_offices` remains a random-state factory reward despite a named Kazan focus. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN` in `005_soviet_collapse_ancient_restorations.txt` | Simplified | 16 focuses each. Claims and decision hooks exist, but the trees remain compact side branches rather than real restoration politics/economy/war/diplomacy routes. |

## Idea and Helper Audit

Direct idea effects in focus completion rewards:
- No direct `add_ideas`, `swap_ideas`, or `add_timed_idea` in the four focus files.
- Direct focus `remove_ideas` exists in hidden cleanup/settlement rewards:
  - `PRA_the_board_overrules_ministers`, `005_soviet_collapse_custom_splinters.txt:1367`
  - `TSC_the_committee_of_instruments`, `005_soviet_collapse_custom_splinters.txt:1961`
  - `RMC_communes_of_witnesses`, `005_soviet_collapse_custom_splinters.txt:2395`
  - `DSC_witness_officers`, `005_soviet_collapse_custom_splinters.txt:2885`
  - `NRF_living_harbor_committees`, `005_soviet_collapse_custom_splinters.txt:3471`
  - `ICD_commissars_of_last_addresses`, `005_soviet_collapse_custom_splinters.txt:3977`
  - `mrc_protect_village_autonomy`, `005_soviet_collapse_custom_splinters.txt:20106`
  - `OGB_the_council_takes_the_seal`, `005_soviet_collapse_factory_successors.txt:1226`

Scripted-effect idea adders:
- `common/scripted_effects/005_soviet_collapse_effects.txt:5514` `soviet_collapse_update_consolidated_republic_ideas` remains the main tiered idea updater.
- Duplicate idea adders by scan:
  - `cfr_construction_mandates`: setup at `:15087` and focus helper `soviet_collapse_apply_cfr_survey_unfinished_sites` at `:9754`.
  - `mfr_arsenal_quotas`: setup at `:15103` and focus helper `soviet_collapse_apply_mfr_audit_arsenal_orders` at `:10252`.
  - `krs_sailors_assembly`: setup at `:15121` and custom doctrine helper at `:13317`.
  - `soviet_collapse_returned_names_pressure`: setup for `KZR`, `SOG`, `KHW`, `ALN` at `:15414`, `:15431`, `:15448`, `:15465`, and focus helper at `:14705`.

Helper-led focus reward examples:
- `soviet_collapse_breakaway_focus_tree`: 31 helper-without-direct-hook rewards. Examples: `soviet_collapse_guard_the_radio_stations` `005_soviet_collapse_republics.txt:2401`, `soviet_collapse_secure_ministry_ledgers` `:2416`, `soviet_collapse_foreign_liaison_government` `:2607`.
- `soviet_collapse_internal_republic_focus_tree`: 58 helper-without-direct-hook rewards. Examples: `internal_soviet_collapse_convene_republic_presidium` `:3195`, `internal_soviet_collapse_map_union_property` `:3227`, `internal_soviet_collapse_karelian_finnish_border_mission` `:3448`.
- `soviet_collapse_ukraine_focus_tree`: 58 helper-without-direct-hook rewards. Examples: `ukr_soviet_collapse_guard_the_telegraph_house` `:55`, `ukr_soviet_collapse_black_banner_compact` `:267`, `ukr_soviet_collapse_officers_above_parties` `:541`.
- `soviet_collapse_kazakhstan_focus_tree`: 74 helper-without-direct-hook rewards. Examples: `kaz_soviet_collapse_the_southern_wires_are_cut` `:10233`, `kaz_soviet_collapse_guard_the_resource_towns` `:10268`, `kaz_soviet_collapse_resource_concessions_debate` `:10561`.
- Full custom templates such as `FEV` and `SZA` still run many `soviet_collapse_apply_custom_splinter_*_identity` helpers without direct hooks. Examples: `FEV_first_guard` `005_soviet_collapse_custom_splinters.txt:16211`, `FEV_league` `:16410`, `SZA_first_guard` `:17384`, `SZA_league` `:17585`.

## Repeated Generic Rewards

Highest-risk reward patterns:
- `soviet_collapse_republics.txt`: 293 small/no-direct-hook reward focuses by broad scan. Kazakhstan alone has 66; Ukraine has 47; internal republics have 41; Moldova has 35.
- `005_soviet_collapse_custom_splinters.txt`: many 47-focus templates have 24-31 small/no-direct-hook reward focuses. Worst examples include `NLC` 31, `FTH` 29, `BSC`/`BBH` 28, `KRS`/`TNC`/`ALA` 27.
- `005_soviet_collapse_factory_successors.txt`: CFR/MFR are better but still have 15 small/no-direct-hook reward focuses each; OGB has 17 of 23.

Representative repeated rewards to replace with branch identity:
- `PRA_count_the_locomotives` and `PRA_coal_water_and_spare_parts`: train/rail/supply rewards are on-theme but should scale into rail-junction control, rail guard templates, and rail AI.
- `DSC_voronezh_rearguard_archives`, `DSC_grave_ordnance_claims`, `DSC_rearguard_supply_bureau`: manpower/equipment loops should become dead-regiment mechanics, conquest/coring pressure, or no-demobilization economy.
- `NRF_count_the_drowned_crews`, `NRF_maps_of_sunken_routes`, `NRF_dead_convoy_supply_board`: convoy/dockyard loops need ship, port-control, naval-invasion, and fleet AI payoffs.
- `OGB_kazan_ferry_offices`: currently random owned/core civilian factory; needs Kazan/Volga-state targeting or an OGB ferry-office decision upgrade.
- `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`: repeated route-shell focuses need country-specific military/industrial/diplomatic mechanics instead of mostly variables plus shared helpers.

## Pathline and Route-Lock Risks

Mechanical layout scan:

| Tree | Focuses | Prerequisite crossing risks | Line-through-node risks | Priority |
| --- | ---: | ---: | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | 83 | 153 | 4 | Critical |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | 120 | 13 | Critical |
| `soviet_collapse_moldova_focus_tree` | 48 | 91 | 4 | Critical |
| `BAC_soviet_collapse_focus_tree` | 47 | 44 | 0 | High |
| `UWD_soviet_collapse_focus_tree` | 47 | 35 | 2 | High |
| `soviet_collapse_belarus_focus_tree` | 53 | 33 | 0 | High |
| `SZA_soviet_collapse_focus_tree` | 47 | 29 | 0 | High |
| `soviet_collapse_central_asia_focus_tree` | 45 | 24 | 0 | Medium |
| `soviet_collapse_caucasus_focus_tree` | 40 | 18 | 2 | Medium |
| `FEV_soviet_collapse_focus_tree` | 47 | 18 | 0 | Medium |
| `ARD_soviet_collapse_focus_tree` | 47 | 16 | 0 | Medium |
| `soviet_collapse_baltic_focus_tree` | 42 | 14 | 2 | Medium |
| `NLC_soviet_collapse_focus_tree` | 47 | 14 | 1 | Medium |
| `UDC`, `SDZ`, `DHC`, `KHC`, `IUL` | 47 each | 12-13 each | 0 | Medium |

No duplicate coordinates were found. No asymmetric mutual exclusions were found. No missing prerequisite references were found.

Wide OR prerequisites that increase pathline and route-readability risk:
- `soviet_collapse_armed_neutrality`, `005_soviet_collapse_republics.txt:3090`, 7 prerequisite options.
- `baltic_soviet_collapse_the_baltic_question_resolved`, `005_soviet_collapse_republics.txt:5347`, 6 options.
- `central_asia_soviet_collapse_the_southern_shield`, `005_soviet_collapse_republics.txt:7329`, 5 options.
- `moldova_soviet_collapse_republic_of_crossings`, `005_soviet_collapse_republics.txt:8750`, 8 options.
- `moldova_soviet_collapse_the_river_state`, `005_soviet_collapse_republics.txt:8793`, 9 options.
- `blr_soviet_collapse_join_the_league_when_war_comes`, `005_soviet_collapse_republics.txt:9865`, 5 options.
- `kaz_soviet_collapse_the_steppe_keeps_many_memories`, `005_soviet_collapse_republics.txt:11437`, 5 options.
- `FEV_endgame`, `005_soviet_collapse_custom_splinters.txt:17299`, 9 options.
- `SZA_endgame`, `005_soviet_collapse_custom_splinters.txt:18475`, 9 options.
- `BAC_endgame`, `005_soviet_collapse_custom_splinters.txt:23155`, 6 options.
- `ARD_endgame`, `005_soviet_collapse_custom_splinters.txt:24351`, 6 options.

Flat terminal-line risks:
- `CFR_count_the_cranes` to `CFR_the_unfinished_city_speaks`, `005_soviet_collapse_factory_successors.txt:33-119`.
- `MFR_orders_outlive_ministries` to `MFR_who_owns_the_rifle`, `005_soviet_collapse_factory_successors.txt:1792-1889`.
- `OGB_raise_the_heritage_guard` to `OGB_guard_the_old_capital`, `005_soviet_collapse_factory_successors.txt:1430-1671`.
- `soviet_collapse_military_defense_council` to `soviet_collapse_border_militia_standard`, `005_soviet_collapse_republics.txt:2552-2718`.

## Icon Coverage Table

| File | Focuses | Missing `icon =` | Unique icon ids | Repeated icon ids | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 501 | 0 | 436 | 22 | Top repeats include `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_steppe_supply_congress`. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | 786 | 99 | Repeated template icons dominate: `GFX_focus_FEV_diplomatic_plan`, `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_civil_rule`, `GFX_focus_MRC_foreign`, `GFX_focus_IUL_supply`, `GFX_focus_IUL_war_plan`. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | 102 | 11 | CFR repeats construction icons such as `GFX_focus_CFR_municipal_board_elections`, `GFX_focus_CFR_concrete_republic`, `GFX_focus_CFR_the_builder_state`. |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | 36 | 8 | Ancient trees deliberately share many restoration icons, but the spec asks for unique focus icon assignments. |

Sprite definition scan:
- 1,698 focus icon assignments.
- 1,498 unique assigned icon ids.
- 0 assigned icon ids missing sprite definitions across `interface/005_soviet_collapse*.gfx`.

## Localisation and Reward Mismatch List

Mechanical localisation:
- 0 missing focus title keys across `localisation/english/005_soviet_collapse*.yml`.
- 0 missing focus `_desc` keys.

Semantic mismatches or weak payoffs:
- `CFR_build_the_border_bend_the_border`, `005_soviet_collapse_factory_successors.txt:974`: title and `FOCUS_FILTER_ANNEXATION` imply direct border action; reward only calls `soviet_collapse_apply_cfr_focus_border_permit_network` and generic custom splinter expansion claims. Needs a visible decision unlock or direct target logic.
- `OGB_kazan_ferry_offices`, `005_soviet_collapse_factory_successors.txt:1321`: named Kazan focus gives a random owned/core civilian factory. Needs Kazan/Volga targeted construction or a ferry-office decision upgrade.
- `PRA_claim_the_branch_lines`, `005_soviet_collapse_custom_splinters.txt:1656`: claims wording is now partially supported by `pra_drive_the_junction_columns`, but the focus still lacks `FOCUS_FILTER_ANNEXATION` and should clarify rail-junction claims in tooltip or effect.
- `TSC_claim_the_impact_zone`, `005_soviet_collapse_custom_splinters.txt:2156`: title implies territorial claims; route payoff appears delayed to later expansion/endgame effects.
- Ancient charter/endgame focuses such as `KZR_khazar_charter`, `SOG_sogdian_city_charter`, `KHW_khwarazmian_water_charter`, and `ALN_alan_pass_charter` read larger than their 16-focus tree depth.

## AI Behavior Gaps

`common/ai_strategy/005_soviet_collapse.txt` includes:
- broad Soviet crisis containment
- broad breakaway survival
- broad custom splinter signature force strategy
- broad high-chaos signature force strategy for `OGB`, `PRA`, `TSC`, `RMC`, `ICD`, `DSC`, `NRF`
- route-aware Ukraine, Belarus, and Kazakhstan strategies
- foreign patron response

Gaps:
- Baltic, Caucasus, Central Asia, Moldova, generic breakaway, and internal republic trees lack route-specific AI strategy families.
- CFR, MFR, and OGB lack route-level construction, arsenal, restored-name, production, expansion, and diplomacy strategies.
- PRA, DSC, NRF, TSC, RMC, ICD share a broad high-chaos signature-force AI instead of identity-specific rail/death/naval/supernatural behavior.
- FEV, SZA, UWD, MRC, IUL, BAC, ARD, NLC and most other 47-focus custom splinters rely on generic signature-force behavior and focus-level weights.
- Ancient restorations lack restoration-specific AI.
- Many trees have base-only `ai_will_do` blocks: Kazakhstan 61, Ukraine 27, internal republics 25, Caucasus 23, Moldova 20, breakaway 18, Baltic 18.

## Decision and Mechanic Unlock Gaps

Existing decision hooks are present for many high-chaos tags:
- CFR: `cfr_survey_unfinished_sites`, `cfr_issue_reconstruction_contracts`.
- MFR: `mfr_audit_arsenal_orders`, `mfr_convert_depots_to_arms_lines`.
- OGB: `ogb_consolidate_volga_registers`, `ogb_guard_kazan_ferry_line`, `ogb_declare_the_volga_restoration_state`.
- PRA: `pra_consolidate_timetable_courts`, `pra_mobilize_station_guard`, `pra_repair_the_branch_lines`, `pra_raise_mobile_supply_yards`, `pra_drive_the_junction_columns`, `pra_declare_the_moving_state`.
- DSC: `dsc_verify_the_roll_call`, `dsc_raise_dead_regiment_columns`, `dsc_convene_the_dead_army`.
- NRF: `nrf_recover_drowned_ship_logs`, `nrf_raise_icebound_marines`, `nrf_call_the_revenant_fleet`.
- FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC: generic `*_consolidate_claim`, `*_mobilize_signature_forces`, `*_push_extreme_route` families.

Remaining unlock gaps:
- `soviet_collapse_breakaway_focus_tree`: 0 direct decision/mission/claim/war/faction hook focuses. Add existing decision hooks for defense goals, depot seizure, foreign liaison, and League survival where appropriate.
- `soviet_collapse_internal_republic_focus_tree`: only 2 direct hook focuses despite 62 focuses. Regional branches should unlock or strengthen local settlement, border, and League decisions.
- `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`: generic decision families exist, but route focus rewards rarely make the country behave aggressively enough without explicit war goals, target claims, or AI strategy.
- `OGB`: decisions exist, but tree depth and named Volga/Kazan mechanics are too thin.
- Ancient restorations: claim decisions exist, but no full restoration mechanic chain should be assumed without parent approval.

## High-Priority Fix Plan

1. Reflow before adding more content.
   - Start with Ukraine, Kazakhstan, Moldova, BAC, UWD, Belarus, and SZA. Their current pathline risk is already high enough that incremental additions will make the UI worse.

2. Replace helper-only reward rhythm with visible mechanics.
   - First targets: `soviet_collapse_breakaway_focus_tree`, `soviet_collapse_internal_republic_focus_tree`, Ukraine opener/political routes, Kazakhstan route families, and the 47-focus custom templates.
   - Use existing decisions, missions, claim/war/core helpers, unit helpers, map construction, and AI strategies instead of more direct idea grants.

3. Build high-chaos identity standards.
   - CFR: repeatable construction programs, state-targeted rebuilding, construction-client protectorates, and route AI.
   - MFR: military factories, production lines, arsenal guard units, client war-market decisions, and production AI.
   - PRA: rail-junction claims, rail guard units, armored trains, supply hubs, rail tolls, and rail AI.
   - DSC: many war goals, dead-regiment units, conquest/coring rules, no-demobilization economy, and high aggression AI.
   - NRF: dockyards, convoys, ships, naval invasions, port control, White Sea/Arctic claims, and naval AI.
   - OGB: Volga/Kazan targeted mechanics, old-trade-city integration, restored-name diplomacy, IUL rivalry/compact depth, and restored-state AI.
   - FEV and other high-chaos 47-focus successors: replace generic shell branches with country-specific expansion, sponsor, internal-faction, and special-mechanic payoffs.

4. Add route-aware AI strategy coverage.
   - Add persistent AI strategy plans for Baltic, Caucasus, Central Asia, Moldova, generic breakaway/internal republics, CFR, MFR, OGB, PRA, DSC, NRF, FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC, and ancient restorations.

5. Clean semantic mismatches.
   - Make `CFR_build_the_border_bend_the_border`, `OGB_kazan_ferry_offices`, `PRA_claim_the_branch_lines`, and `TSC_claim_the_impact_zone` either deliver the promised map/mechanic payoff or retune their title/filter/tooltip.

6. Icon identity pass.
   - Do not touch flags. For focus icons, keep existing sprite definitions but reduce repeated icon assignments on route-defining focuses. This is a wiring/design task, not a flag-asset task.

## Validation Run

Commands/checks run:
- Read required repo instructions and focus/event/decision/assets/improvement/subagent skills.
- Read offline wiki core pages and National Focus Modding page.
- Read vanilla documentation from `~/projects/Hearts of Iron IV/documentation`.
- Parsed all four focus files.
- Brace balance: all four focus files ended at depth 0 with no negative depth.
- Duplicate focus id scan: 0 duplicates across 1,698 focus ids.
- Direct `add_ideas`/`swap_ideas`/`add_timed_idea` in focus rewards: 0.
- Direct `remove_ideas` in focus rewards: 8 hidden cleanup cases listed above.
- Missing focus title localisation: 0.
- Missing focus description localisation: 0.
- Missing `icon =`: 0.
- Missing assigned focus icon sprite definitions in `interface/005_soviet_collapse*.gfx`: 0.
- Missing `search_filters`: 0.
- Unsupported `<=`/`>=` scan across scoped focus/effects/decision files: 0 matches.
- Duplicate coordinate scan: 0 duplicate coordinates inside a tree.
- Mutual exclusion asymmetry scan: 0 asymmetric mutual exclusions.
- Missing prerequisite references: 0.
- Pathline scan: crossing and line-through-node counts listed above.

Skipped validation:
- No HOI4 runtime load.
- No focus UI screenshots.
- No whole-repo validator, because the worktree already contains unrelated dirty Event 005 files and untracked handoffs from other agents.

## Remaining Route Risks

- The basic script surface is mechanically clean, but the design surface is incomplete against the spec's real-branch standard.
- More focus content should not be added before major reflow in Ukraine, Kazakhstan, Moldova, BAC, UWD, Belarus, and SZA.
- Direct idea spam is mostly avoided in focus files, but helper-led idea lifecycle and shared custom-splinter helpers still make many rewards feel generic.
- High-chaos countries are stronger than earlier passes, but several still need country-specific aggression and mechanics before they feel OP enough.
- Existing `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` remains valid and should be treated as the broad rework backlog. This audit updates it with current counts and specific current-state evidence.
