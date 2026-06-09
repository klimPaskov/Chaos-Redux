# Event 005 Soviet Collapse Focus Tree Audit Handoff

Date: 2026-05-30 08:01 UTC
Role: Chaos Redux focus tree subagent
Scope: `common/national_focus/005_soviet_collapse_republics.txt`, `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `common/national_focus/005_soviet_collapse_factory_successors.txt`, and `common/national_focus/005_soviet_collapse_ancient_restorations.txt`.
User constraint honored: no `gfx/flags` files and no flag artwork were inspected for editing or touched.

## Summary

This pass is an audit handoff, not a gameplay patch. The current focus files already contain pending worktree edits, and the remaining issues are mostly broad route-depth and reward-identity problems rather than one-line safe fixes. I did not patch focus gameplay.

The trees are no longer primarily direct `add_ideas` spam. Direct `add_ideas` in focus rewards is zero across all four audited focus files. The remaining churn is mostly hidden remove-idea cleanup and helper-driven idea lifecycle calls, especially custom splinter endgame helpers and consolidated republic idea updates.

The larger quality gap is still branch purpose: Ukraine, Belarus, Kazakhstan, PRA, DSC, CFR, MFR, OGB, ARD, NRF, and NLC have visible branches, but several are still reward-heavy ladders with repeated equipment/building grants, flat AI blocks, or OR-joins from mutually exclusive parents that can create confusing path lines.

## Focus Counts

| File | Trees | Focuses |
| --- | ---: | ---: |
| `common/national_focus/005_soviet_collapse_republics.txt` | 9 | 501 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 25 | 1005 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 3 | 128 |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 4 | 64 |

## Route Coverage Table

| Required route/country | Implemented tree or branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine political paths | `soviet_collapse_ukraine_focus_tree`, 83 focuses | Partial | Five visible route locks exist: socialist, Black Banner, democratic, military, protectorate. Several focuses still rely on generic helper/stat rewards, and two OR-join children from mutually exclusive parents create pathline risk: `ukr_soviet_collapse_free_soil_compromise` and `ukr_soviet_collapse_last_harvest_plan`. |
| Ukraine industry | Ukraine Dnieper/grain/ports/arsenal lane | Partial | Has map construction and some foreign/League hooks, but many rewards remain `add_stability`, `add_command_power`, helper calls, or small buildings. Needs route-specific industry payoffs tied to Bread State, Black Sea, military, democratic, or protectorate outcomes. |
| Ukraine expansion/diplomacy | League, Black Sea, border arbitration, protectorate and foreign liaison lanes | Partial | Decision hooks exist in later League/Black Sea focuses, but claims/war/postwar handling is still thin for an 83-focus major route. |
| Belarus political paths | `soviet_collapse_belarus_focus_tree`, 53 focuses | Partial | National council, socialist autonomy, military transit, and foreign corridor paths exist. Route locks are hidden `available` checks without visible mutual exclusions, so route meaning is less readable than Ukraine/CFR. |
| Belarus industry/logistics | Rail map, junction, corridor, depot, forest lanes | Partial | Strong rail identity, but rail/corridor rewards repeat depot helpers and small construction. Needs fewer rail-stat repeats and more decision/misson evolution. |
| Belarus expansion/diplomacy | Green rail pact/corridor/foreign administration | Partial | Diplomacy exists but no claim or war-goal count was detected for the BLR prefix; expansion payoff is mostly recognition, rail, and League preparation. |
| Kazakhstan political/federal paths | `soviet_collapse_kazakhstan_focus_tree`, 92 focuses | Partial | Steppe congress/federation and lone-state framing exist with Central Asia interactions. Large size gives depth, but AI is often flat and expansion is mostly League/federation hooks rather than hard territorial consequence. |
| Kazakhstan industry/resources | Mines, oil boards, rail-to-mines, Caspian resource lanes | Partial | Better map/resource grounding than most trees, with 18 building reward focuses and 4 decision hooks. Still contains repeated convoy/equipment/building patterns. |
| Kazakhstan military/diplomacy | Mobile district, cavalry, rail guards, foreign technical missions | Partial | Several branches exist, but many important focuses are `ai_will_do = { base = ... }` only. |
| PRA railway successor | `PRA_soviet_collapse_focus_tree`, 22 focuses | Shallow but improving | Clear railway identity and 12 decision hooks. Still short for an overpowered aggressive chaos country; `PRA_passport_of_the_moving_state` joins mutually exclusive parents at (0,5) and (4,5), producing a likely pathline readability risk. |
| DSC dead army successor | `DSC_soviet_collapse_focus_tree`, 18 focuses | Shallow | Aggressive and overpowered hooks exist (`create_wargoal`, assault columns, neighbor AI strategies), but the tree is still 18 focuses and heavily military/equipment weighted. Two join risks: `DSC_field_hospital_memorials`, `DSC_maps_of_lost_armies`. |
| Construction chaos country | `CFR_soviet_collapse_focus_tree`, 47 focuses | Partial | Governance and strategy forks exist. Stronger than OGB, but `CFR_apartment_blocks_for_loyalty` joins `CFR_cities_first` and `CFR_rails_first`, which are mutually exclusive. |
| Factory/munitions chaos country | `MFR_soviet_collapse_focus_tree`, 58 focuses | Partial | Has real production, board, arms-order, and military industry structure. Needs more distinct route end states and fewer generic stat/building payoffs before final completion. |
| Railway chaos country | `PRA_soviet_collapse_focus_tree`, 22 focuses | Shallow | Railway mechanics and decision hooks exist, but branch count and endgame payoff are still light relative to requested extreme power and aggression. |
| Naval chaos countries | `ARD_soviet_collapse_focus_tree` 47, `NRF_soviet_collapse_focus_tree` 18, plus NLC arctic/polar adjacent content | Partial to shallow | ARD has 47 focuses but 13 equipment and 16 building reward focuses; NRF is only 18 and repeats convoy/naval equipment patterns. Need deeper naval aggression, port control, fleets, sea-lane claims, and postwar handling. |

## Idea Churn Counts

| File | Focuses with direct `add_ideas` | Focuses with direct `remove_ideas` | Duplicate same idea inside one focus | Focuses calling idea-churn helpers |
| --- | ---: | ---: | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 0 | 0 | 0 | 0 |
| `005_soviet_collapse_custom_splinters.txt` | 0 | 7 | 0 | 52 |
| `005_soviet_collapse_factory_successors.txt` | 0 | 1 | 0 | 1 |
| `005_soviet_collapse_ancient_restorations.txt` | 0 | 0 | 0 | 0 |

Direct remove-idea examples:

| Focus | File:line | Direct idea operation |
| --- | --- | --- |
| `PRA_the_board_overrules_ministers` | `005_soviet_collapse_custom_splinters.txt:1370` | Hidden `remove_ideas = pra_dispatcher_court_tensions` |
| `DSC_witness_officers` | `005_soviet_collapse_custom_splinters.txt:2893` | Hidden `remove_ideas = dsc_grave_regiment_rivalries` |
| `NRF_living_harbor_committees` | `005_soviet_collapse_custom_splinters.txt:3469` | Hidden `remove_ideas = nrf_drowned_crew_disputes` |
| `ICD_commissars_of_last_addresses` | `005_soviet_collapse_custom_splinters.txt:3974` | Hidden `remove_ideas = icd_grave_commissar_rivalries` |
| `OGB_the_council_takes_the_seal` | `005_soviet_collapse_factory_successors.txt:1190` | Hidden `remove_ideas = ogb_disputed_restored_name` |

Helper-driven idea churn examples:

| Focus | File:line | Helper |
| --- | --- | --- |
| `FTH_doctrine` | `005_soviet_collapse_custom_splinters.txt:146` | `soviet_collapse_apply_custom_splinter_doctrine_identity` |
| `FTH_endgame` | `005_soviet_collapse_custom_splinters.txt:1186` | `soviet_collapse_complete_black_banner_endgame` |
| `PRA_rails_over_capitals` | `005_soviet_collapse_custom_splinters.txt:1716` | `soviet_collapse_complete_pale_railway_endgame` |
| `PRA_the_pale_line_endures` | `005_soviet_collapse_custom_splinters.txt:1788` | `soviet_collapse_complete_pale_railway_endgame` |
| `DSC_armies_that_do_not_demobilize` | `005_soviet_collapse_custom_splinters.txt:3195` | `soviet_collapse_complete_dead_soldiers_endgame` |
| `DSC_congress_of_the_dead_army` | `005_soviet_collapse_custom_splinters.txt:3288` | `soviet_collapse_complete_dead_soldiers_endgame` |
| `OGB_the_old_name_survives_modern_war` | `005_soviet_collapse_factory_successors.txt:1674` | `soviet_collapse_complete_old_great_bulgaria_endgame` |

Transitive setup churn outside focus rewards remains heavy in `common/scripted_effects/005_soviet_collapse_effects.txt`, especially release setup helpers such as `soviet_collapse_setup_pra_successor` adding `pra_timetable_sovereignty_board`, `pra_railway_guard`, and `pra_dispatcher_court_tensions`, and many `soviet_collapse_setup_*_successor` helpers adding two or three starting ideas. These are not focus-spam problems by themselves, but they make focus cleanup paths important.

## Shallow Reward Patterns

| File | `add_equipment_to_stockpile` focuses | `add_building_construction` focuses | `add_political_power` focuses | `add_stability` focuses | `add_war_support` focuses | `add_manpower` focuses |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 27 | 115 | 38 | 91 | 15 | 33 |
| `005_soviet_collapse_custom_splinters.txt` | 174 | 256 | 79 | 133 | 54 | 80 |
| `005_soviet_collapse_factory_successors.txt` | 2 | 12 | 9 | 19 | 6 | 4 |
| `005_soviet_collapse_ancient_restorations.txt` | 8 | 18 | 4 | 6 | 8 | 4 |

Examples of repeated small reward patterns:

| Pattern | Examples |
| --- | --- |
| Small equipment in custom splinters | `PRA_omsk_station_guard`, `PRA_count_the_locomotives`, `PRA_the_board_overrules_ministers`, `DSC_grave_ordnance_claims`, `DSC_rearguard_supply_bureau`, `NRF_salvage_the_dark_berths` |
| One-state construction as main payoff | `ukr_soviet_collapse_first_republican_line`, `blr_soviet_collapse_seal_the_minsk_junction`, `kaz_soviet_collapse_airstrips_on_the_steppe`, `PRA_repair_crews_without_ministries`, `CFR_emergency_cement_accounts` |
| Political/stability filler | `ukr_soviet_collapse_workers_congress_in_kharkiv`, `ukr_soviet_collapse_coalition_of_three_ministries`, `PRA_ticket_courts_for_every_platform`, `OGB_restore_the_bolghar_name` |
| Naval/convoy repeats | `kaz_soviet_collapse_caspian_security_detachments`, `kaz_soviet_collapse_iranian_caspian_notes`, ARD and NRF convoy/port focuses, several KRS dockyard/naval focuses |

The best next pass should replace some repeated reward dumps with existing decisions, missions, route locks, AI strategy changes, postwar settlement hooks, claims/cores where intended, or country-specific mechanics. Do not solve this by adding new ideas to every focus.

## Requested Country Depth Matrix

| Prefix | Focuses | Direct idea focus count | Helper idea-churn count | Equipment focuses | Building focuses | Decision/mission hooks | Claims/wargoals |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `ukr_soviet_collapse` | 83 | 0 | 0 | 2 | 6 | 7 | 0 |
| `blr_soviet_collapse` | 53 | 0 | 0 | 0 | 6 | 3 | 0 |
| `kaz_soviet_collapse` | 92 | 0 | 0 | 5 | 18 | 4 | 0 |
| `PRA` | 22 | 1 | 2 | 9 | 12 | 12 | 1 |
| `DSC` | 18 | 1 | 2 | 7 | 4 | 5 | 2 |
| `CFR` | 47 | 0 | 0 | 0 | 5 | 4 | 2 |
| `MFR` | 58 | 0 | 0 | 1 | 4 | 3 | 1 |
| `OGB` | 23 | 1 | 1 | 1 | 3 | 1 | 3 |
| `ARD` | 47 | 0 | 2 | 13 | 16 | 3 | 0 |
| `NRF` | 18 | 1 | 2 | 11 | 6 | 4 | 1 |
| `NLC` | 47 | 0 | 4 | 6 | 15 | 0 | 0 |

High-priority depth gaps:

1. `PRA`, `DSC`, `NRF`, and `OGB` are too short for major high-chaos successors. They should either be explicitly documented as crisis/minor trees or expanded through a main-agent route design pass.
2. `Ukraine`, `Belarus`, and `Kazakhstan` are large enough, but several routes need sharper political end states and branch interaction. They should not be considered finished just because they have high focus counts.
3. `ARD` and `NLC` have enough focus count but shallow reward signatures. ARD especially leans on equipment/building rewards; NLC has no detected decision/mission unlocks in focus rewards.
4. `CFR` and `MFR` have stronger route structure than most, but CFR still has one OR-join pathline risk through mutually exclusive strategic choices.

## Layout, Mutual Exclusion, and Pathline Risks

No duplicate focus coordinates were found in the audited focus files.

The parser found 35 focuses whose prerequisite group OR-joins mutually exclusive parent focuses. This is not always invalid, but it is a pathline risk because focus lines can visually connect through incompatible choices. Highest-priority examples:

| Focus | File:line | Mutually exclusive parents joined | Risk |
| --- | --- | --- | --- |
| `ukr_soviet_collapse_free_soil_compromise` | `005_soviet_collapse_republics.txt:802` | `ukr_soviet_collapse_black_banner_compact` (30,7) and `ukr_soviet_collapse_elections_under_shellfire` (20,4) | Lines may cross political route space and imply a combined democratic/Black Banner path. |
| `ukr_soviet_collapse_last_harvest_plan` | `005_soviet_collapse_republics.txt:2243` | `ukr_soviet_collapse_the_commune_war` (21,16) and `ukr_soviet_collapse_the_double_republic` (25,16) | May be intentional convergence, but it visually rejoins incompatible late routes. |
| `PRA_passport_of_the_moving_state` | `005_soviet_collapse_custom_splinters.txt:1563` | `PRA_the_board_overrules_ministers` (0,5) and `PRA_armored_train_directorate` (4,5) | Child at (6,6) is offset right, likely drawing a long line through the fork. |
| `DSC_field_hospital_memorials` | `005_soviet_collapse_custom_splinters.txt:2996` | `DSC_revenant_staff_line` (6,3) and `DSC_witness_officers` (2,3) | Converges incompatible identity fork immediately after choice. |
| `DSC_maps_of_lost_armies` | `005_soviet_collapse_custom_splinters.txt:3083` | Same DSC fork | Same risk; map line may visually erase the choice. |
| `CFR_apartment_blocks_for_loyalty` | `005_soviet_collapse_factory_successors.txt:517` | `CFR_cities_first` (3,8) and `CFR_rails_first` (8,9) | Strategic choices are mutually exclusive but child visibly joins both. |
| `BSC_industry_plan`, `TNC_industry_plan`, `ALA_industry_plan`, `BBH_industry_plan`, `KRS_industry_plan`, `FEV_industry_plan`, `SZA_industry_plan`, `UWD_industry_plan`, `MRC_industry_plan`, `IUL_industry_plan`, `BAC_industry_plan`, `ARD_industry_plan`, `NLC_industry_plan` | `005_soviet_collapse_custom_splinters.txt` various | `radical_turn` and `settlement` pairs | Repeated template pattern: industry child often joins mutually exclusive ideological/settlement forks. This needs a design decision: visible convergence, duplicate route-specific industry child, or hidden availability only. |
| `KZR_khazar_charter`, `SOG_sogdian_city_charter`, `KHW_khwarazmian_water_charter`, `ALN_alan_pass_charter` | `005_soviet_collapse_ancient_restorations.txt` | symbolic vs expansionist fork pairs | Ancient restoration trees deliberately converge, but this undercuts route exclusivity and line clarity. |

## Icon Coverage Table

This audit checked icon assignment strings only. It did not inspect, edit, or request flag art, and it did not edit `.gfx`.

| File | Missing `icon =` | Repeated icon ids | Notes |
| --- | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 0 | 22 | Reuse includes `GFX_ukr_soviet_collapse_democratic`, `GFX_ukr_soviet_collapse_industry`, `GFX_focus_soviet_collapse_guard_the_radio_stations`, and other shared families. Some reuse may be intentional; major route payoffs need unique icons. |
| `005_soviet_collapse_custom_splinters.txt` | 0 | 99 | Reuse is widespread in shared template trees (`GFX_focus_BSC_legitimacy`, `GFX_focus_TNC_legitimacy`, etc.). This supports the user's complaint that many trees still read generically. |
| `005_soviet_collapse_factory_successors.txt` | 0 | 11 | CFR reuses several icon identities across related construction focuses; acceptable for families, but final route payoffs should be unique. |
| `005_soviet_collapse_ancient_restorations.txt` | 0 | 8 | Four 16-focus ancient trees intentionally share icon families. This reinforces that they are still stub-like. |

## Localisation and Reward Mismatch List

Localisation key audit result: no missing focus title keys and no missing `_desc` keys were found across the audited focus ids in Event 005 English localisation files.

Potential title/reward mismatch examples requiring manual review:

| Focus | File:line | Mismatch risk |
| --- | --- | --- |
| `blr_soviet_collapse_the_rail_map_on_the_wall` | `005_soviet_collapse_republics.txt:8918` | Rail title but reward is mainly a flag and depot helper; no immediate rail, train, supply node, or decision hook. |
| `blr_soviet_collapse_nationalize_the_rail_schedules` | `005_soviet_collapse_republics.txt:9279` | Rail title but reward is political power plus depot helper. Consider a rail/supply/decision effect or clearer localisation. |
| `ukr_soviet_collapse_direct_national_claims` | `005_soviet_collapse_republics.txt:1765` | Title promises claims; mechanical audit did not detect direct `add_state_claim`, `create_wargoal`, or decision unlock in the focus reward. This may be hidden helper-driven and should be verified manually. |
| `DSC_grave_ordnance_claims` | `005_soviet_collapse_custom_splinters.txt:2958` | Title says claims, but current reward is manpower/equipment/assault columns and conditional generic expansion claims helper. Needs tooltip clarity if helper is the real claim payoff. |
| `NRF_claim_the_white_sea_lane` | `005_soviet_collapse_custom_splinters.txt:3719` | Title says claim; audit did not detect direct claim/wargoal/decsion unlock. Verify hidden helper or add explicit payoff. |
| `FEV_free_port_merchants`, `FEV_amur_river_ports`, `SZA_yenisei_river_ports`, ARD/NRF port lanes | `005_soviet_collapse_custom_splinters.txt` | Port/naval titles should consistently map to dockyard/naval-base/convoy/navy/sea-lane mechanics, not only generic construction or political rewards. |

## AI Behavior Gaps

Every audited focus has an `ai_will_do` block, but many are still flat base-only blocks:

| File | Flat `ai_will_do` focuses | Route-aware/non-flat focuses |
| --- | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 219 | 282 |
| `005_soviet_collapse_custom_splinters.txt` | 84 | 921 |
| `005_soviet_collapse_factory_successors.txt` | 0 | 128 |
| `005_soviet_collapse_ancient_restorations.txt` | 48 | 16 |

AI concerns:

1. Ukraine has many flat AI blocks on important route and branch nodes, including early statehood/military/industry focuses. Some route selectors have modifiers, but many follow-up payoffs do not react to war state, SOV pressure, old-movement pressure, sponsor risk, or route flags.
2. Belarus route selectors are mostly route-aware, but several rail and payoff focuses are flat. Hidden route locks also make AI intent harder to verify.
3. Kazakhstan's 92-focus tree has many flat support/payoff focuses despite being a major regional actor. AI should explicitly prefer federation, lone-state, resource, or foreign liaison paths based on Central Asian breakaway state, war, resources, and foreign appetite.
4. Ancient restoration trees have mostly flat AI and remain shallow.
5. High-chaos successors should be more aggressive. DSC has some strong hidden AI strategies against SOV/neighbors; PRA and NRF need stronger route-aware aggression and expansion preference if they are meant to be extreme chaos actors.

## High-Priority Fixes First

1. Decide route convergence rules for mutually exclusive forks. For each OR-join risk, choose one:
   - split the child into route-specific copies,
   - move the child to a neutral trunk before the fork,
   - remove visible OR prerequisites and gate through `available`/tooltip only,
   - or document the convergence as intentional and position it so no line runs through mutually exclusive focuses.
2. Deepen shallow high-chaos successors before adding more small rewards. Priority: `DSC`, `PRA`, `NRF`, `OGB`.
3. Replace repeated equipment/building rewards with existing decision and mission hooks. Priority files: `005_soviet_collapse_custom_splinters.txt` and `005_soviet_collapse_republics.txt`.
4. Give Ukraine/Belarus/Kazakhstan route end states visible consequences: government identity, leader/advisor/law/cosmetic hooks where already available, route-specific AI strategy, and postwar/expansion handling.
5. Audit icon reuse only after gameplay route roles are stable. Do not touch flag artwork; if icons need new assets, route through the asset skill with placeholders and a separate handoff.
6. Review title/reward mismatches manually, especially rail, claim, port, naval, and factory titles with no matching mechanical reward.

## Small Patches Made

No gameplay patches were made in this audit pass.

Changed files:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_080110_event005_focus_tree_audit_handoff.md`

Changed focus ids: none.

Route behavior before/after: unchanged.

Localisation keys changed: none.

Icon ids changed: none.

## Validation

Validation run:

- `git diff --check`: passed, no whitespace errors reported.
- `rg -n '<=|>='` over audited Event 005 focus files: passed, no unsupported operators found.
- Brace-depth check over audited Event 005 focus files and this handoff: passed.
  - `005_soviet_collapse_republics.txt`: final depth 0, minimum depth 0.
  - `005_soviet_collapse_custom_splinters.txt`: final depth 0, minimum depth 0.
  - `005_soviet_collapse_factory_successors.txt`: final depth 0, minimum depth 0.
  - `005_soviet_collapse_ancient_restorations.txt`: final depth 0, minimum depth 0.
  - this handoff: final depth 0, minimum depth 0.

Skipped validation:

- No in-game validation was run.
- No `.gfx`, `gfx/flags`, or flag artwork validation was run because the user explicitly excluded flag/gfx work.

## Remaining Route Risks

The event focus package still should not be called complete. Known remaining risks:

- broad route depth gaps remain for shallow high-chaos trees;
- repeated small reward patterns are still common;
- several routes lack strong route-specific AI;
- pathline risks remain around OR-joins from mutually exclusive focuses;
- icon assignment exists, but repeated icon families are too common for final route identity;
- no flag/gfx work was done due to user constraint.
