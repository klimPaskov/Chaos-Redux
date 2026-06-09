# Event005 Soviet Collapse Focus Tree Rework Audit

Date: 2026-06-04 17:47 UTC
Agent: chaosx_focus_tree_auditor
Mode: read-only audit

## Scope

Inspected repo files only:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

Required references were opened before auditing: offline Paradox wiki core pages, National focus modding, and relevant vanilla documentation/examples. No gameplay patch was made. No gfx, flags, or flag sprite paths were edited.

## 1. Duplicate Idea / Reward Spam Findings

I did not find a focus completion reward in the four focus files that directly applies the same idea twice. In fact, these four focus files currently contain no direct `add_ideas =`, `remove_ideas =`, or `swap_ideas =` lines. Idea application is routed through scripted effects.

The concrete spam source I did find is duplicate reward-helper display/application chains: a focus calls a reward helper directly and also calls a broader plan/depth helper that can call the same reward helper again. This can display the same custom tooltip twice and can re-run the same payload in one focus completion. For `soviet_collapse_apply_focus_rail_authority_reward`, this also means repeated PRA idea churn, because that helper removes and re-adds PRA rail authority ideas in `common/scripted_effects/005_soviet_collapse_effects.txt:7847`.

Relevant helper definitions:

- `soviet_collapse_apply_focus_rail_authority_reward` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:7815` and displays `soviet_collapse_apply_focus_rail_authority_reward_tt`; localisation at `localisation/english/005_soviet_collapse_l_english.yml:213`.
- `soviet_collapse_apply_focus_mobile_columns_reward` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:8063` and displays `soviet_collapse_apply_focus_mobile_columns_reward_tt`; localisation at `localisation/english/005_soviet_collapse_l_english.yml:215`.
- `soviet_collapse_advance_depot_focus_depth` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:8633` and can call the rail helper at depot milestones.
- `soviet_collapse_apply_focus_depot_and_supply_control` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:8815` and calls depot depth, depot payloads, and route payloads.
- `soviet_collapse_apply_focus_military_consolidation` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:8794`.
- `soviet_collapse_apply_focus_security_supply_plan` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:9440`.
- `soviet_collapse_apply_focus_foreign_league_plan` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:9493`.
- `soviet_collapse_apply_focus_lawful_supply_plan` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:9550`.
- `soviet_collapse_apply_focus_foreign_supply_plan` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:9576`.
- `soviet_collapse_apply_focus_chaos_assault_plan` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:9740`.
- `soviet_collapse_apply_focus_league_logistics_plan` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:9768`.
- `soviet_collapse_apply_focus_chaos_supply_plan` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:9852`.

Exact focus ids with direct rail helper plus another helper that can call or re-run rail-authority payloads:

| Focus id | File line | Chain |
| --- | --- | --- |
| `soviet_collapse_rail_hub_or_mountain_pass` | `common/national_focus/005_soviet_collapse_republics.txt:2966` | direct rail helper + `soviet_collapse_apply_focus_depot_and_supply_control` -> depot depth |
| `internal_soviet_collapse_northern_timber_rail_fund` | `common/national_focus/005_soviet_collapse_republics.txt:3360` | direct rail helper + depot/supply control |
| `moldova_soviet_collapse_odessa_contact_posts` | `common/national_focus/005_soviet_collapse_republics.txt:8292` | direct rail helper + `soviet_collapse_apply_focus_foreign_league_plan` route payloads |
| `moldova_soviet_collapse_smugglers_and_border_committees` | `common/national_focus/005_soviet_collapse_republics.txt:8659` | direct rail helper + `soviet_collapse_apply_focus_chaos_supply_plan` |
| `blr_soviet_collapse_depot_cars_without_labels` | `common/national_focus/005_soviet_collapse_republics.txt:9299` | direct rail helper + depot/supply control |
| `kaz_soviet_collapse_turkmen_rail_and_desert_talks` | `common/national_focus/005_soviet_collapse_republics.txt:10769` | direct rail helper + `soviet_collapse_apply_focus_league_logistics_plan` |
| `kaz_soviet_collapse_rail_guard_brigades` | `common/national_focus/005_soviet_collapse_republics.txt:11813` | direct rail helper + depot/supply control |
| `PRA_coal_water_and_spare_parts` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:1462` | direct rail helper + depot/supply control |
| `TNC_economy` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:5653` | direct rail helper + `soviet_collapse_apply_focus_chaos_supply_plan` and `soviet_collapse_apply_focus_lawful_supply_plan` |

Exact focus ids with direct mobile-columns helper plus another helper that can re-run mobile/military-column payloads:

| Focus id | File line | Chain |
| --- | --- | --- |
| `internal_soviet_collapse_ural_cavalry_roads` | `common/national_focus/005_soviet_collapse_republics.txt:3619` | direct mobile helper + `soviet_collapse_apply_focus_security_supply_plan` |
| `internal_soviet_collapse_ural_mobile_defense` | `common/national_focus/005_soviet_collapse_republics.txt:3787` | direct mobile helper + security/supply plan |
| `internal_soviet_collapse_tuvan_steppe_guard` | `common/national_focus/005_soviet_collapse_republics.txt:4382` | direct mobile helper + `soviet_collapse_apply_focus_league_security_plan` |
| `kaz_soviet_collapse_the_army_that_crosses_distance` | `common/national_focus/005_soviet_collapse_republics.txt:10746` | direct mobile helper + `soviet_collapse_apply_focus_military_consolidation` |
| `FTH_doctrine` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:148` | direct mobile helper + `soviet_collapse_apply_focus_chaos_assault_plan` |
| `BSC_doctrine` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:4494` | direct mobile helper + chaos assault plan |
| `TNC_doctrine` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:5630` | direct mobile helper + chaos assault plan |
| `UDC_doctrine` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:10303` | direct mobile helper + chaos assault plan |
| `UDC_signal_truck_yards` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:11104` | direct mobile helper + military consolidation |
| `NLC_doctrine` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:24542` | direct mobile helper + chaos assault plan |

Related idea-chain note: `soviet_collapse_republican_startup_disorder` is added by `soviet_collapse_apply_breakaway_setup_package` at `common/scripted_effects/005_soviet_collapse_effects.txt:3961`, but that package is guarded by `soviet_collapse_setup_breakaway_country` at `common/scripted_effects/005_soviet_collapse_effects.txt:3653`. The guard uses `NOT = { has_country_flag = soviet_collapse_breakaway }`, so this does not look like the active repeated focus reward spam source.

Consolidated staged ideas are also not a direct duplicate-add culprit. `soviet_collapse_clear_republic_staged_ideas` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:5611`, `soviet_collapse_update_consolidated_republic_ideas` starts at `common/scripted_effects/005_soviet_collapse_effects.txt:5766`, and `has_soviet_collapse_republic_staged_idea` starts at `common/scripted_triggers/005_soviet_collapse_triggers.txt:2850`. The current pattern clears old staged ideas before consolidated updates.

## 2. Shallow / Generic Route Surfaces

The largest shallow surface is the repeated 47-focus high-chaos custom splinter pattern. These trees generally present `birth`, `first_guard`, `stores`, `legitimacy`, `rival`, `doctrine`, `economy`, `league`, `foreign`, and `inner_faction` blocks with stacked generic helper rewards rather than country-specific political, industry, and expansion lanes.

Highest-priority shallow custom splinter trees:

| Tree | Starts | Audit signal |
| --- | --- | --- |
| `FTH_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:15` | 47 focuses, 0 decision hooks, 0 war hooks, 0 claims/cores; visible template opener; direct duplicate mobile chain on `FTH_doctrine`. |
| `BBH_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:7752` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores. |
| `KRS_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:8946` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores. |
| `SDZ_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:11394` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores. |
| `GAC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:12657` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores. |
| `DHC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:13827` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores; also has a pathline issue. |
| `KHC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:15026` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores; also has a pathline issue. |
| `FEV_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:16215` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores. |
| `SZA_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:17414` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores. |
| `UWD_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:18578` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores; also has a pathline issue. |
| `MRC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:19765` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores. |
| `IUL_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:20938` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores. |
| `BAC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:22078` | 47 focuses, 0 decisions, 0 war hooks, 0 claims/cores. |

Second-priority custom trees have a few hooks but still lack enough OP country-specific mechanics: `BSC`, `TNC`, `ALA`, `UDC`, `ARD`, and `NLC` each have 2-3 decision references and no direct war/claim/core hooks in focus rewards. `BSC_doctrine`, `TNC_doctrine`, `UDC_doctrine`, `UDC_signal_truck_yards`, and `NLC_doctrine` are also in the duplicate mobile-helper list above.

The short chaos trees have more identity than the repeated 47-focus family but are too compressed:

- `TSC_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1832`: 18 focuses, 3 decisions, 2 war hooks, 0 claims/cores, pathline issue.
- `RMC_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2344`: 18 focuses, 1 decision, 2 war hooks, 2 claims, pathline issue.
- `DSC_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2820`: 18 focuses, 13 decisions, 3 war hooks, pathline issue; better staged mechanics but still too small for a marquee chaos state.
- `NRF_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:3390`: 18 focuses, 6 decisions, 2 war hooks, 2 claims, pathline issue.
- `ICD_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:3894`: 18 focuses, 1 decision, 2 war hooks, 2 claims, pathline issue.

Republic/fallback trees with especially shallow reward surfaces:

- `soviet_collapse_breakaway_focus_tree` at `common/national_focus/005_soviet_collapse_republics.txt:2322`: 36 focuses, 0 decisions, 0 war hooks, 0 claims/cores, 34 helper calls. This should not be the playable fallback for important states.
- `soviet_collapse_baltic_focus_tree` at `common/national_focus/005_soviet_collapse_republics.txt:4621`: 42 focuses, 0 decisions, 0 war hooks, 0 claims/cores.
- `soviet_collapse_moldova_focus_tree` at `common/national_focus/005_soviet_collapse_republics.txt:7641`: 48 focuses, 0 decision hooks, 0 war/claim/core hooks, and a duplicate rail-helper chain.
- `soviet_collapse_internal_republic_focus_tree` at `common/national_focus/005_soviet_collapse_republics.txt:3123`: 62 focuses, 0 decisions, 0 war hooks, 1 claim hook, multiple duplicate rail/mobile chains.
- `soviet_collapse_caucasus_focus_tree` at `common/national_focus/005_soviet_collapse_republics.txt:5584`: 40 focuses, 4 decisions, 0 war/claim/core hooks.

Large republic trees are denser but still need route identity cleanup:

- `soviet_collapse_ukraine_focus_tree` at `common/national_focus/005_soviet_collapse_republics.txt:18`: 83 focuses and 16 decision hooks, but 0 direct war/claim/core hooks and several line-crossing issues.
- `soviet_collapse_kazakhstan_focus_tree` at `common/national_focus/005_soviet_collapse_republics.txt:10109`: 92 focuses and 7 decision hooks, but 0 direct war/claim/core hooks and multiple duplicate rail/mobile helper chains.
- `soviet_collapse_belarus_focus_tree` at `common/national_focus/005_soviet_collapse_republics.txt:8791`: 53 focuses and 12 decision hooks, but 0 direct war/claim/core hooks and a pathline issue.

Ancient restorations are short but less broken mechanically: `KZR`, `SOG`, `KHW`, and `ALN` are each 16 focuses with 4 decision hooks, 2 war hooks, 1 core/transfer hook, and 8-11 claim hooks. They need branch depth, but they are not the first place to fix "no mechanics".

## 3. Political / Industry / Expansion Lanes and Layout Risks

The high-chaos 47-focus custom splinter family lacks clear political/industry/expansion lanes. The repeated route pattern makes countries feel interchangeable, and the reward surface leans on generic helper stacks instead of distinct mechanics. These trees should be rebuilt as:

- Political lane: route locks, internal faction choice, legitimacy mechanic, patron/league stance, and crisis consequences.
- Industry lane: factories, rails, supply hubs, special production, resource extraction, and local decision category unlocks.
- Expansion lane: claims, war goals, cores/compliance, border incidents, postwar pacification decisions, and elite/unit rewards.

Highest-risk mutex layout surfaces:

- `CFR_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_factory_successors.txt:18`: 47 focuses with 12 mutex declarations. This is the highest mutex-density tree in scope and should be checked for pointless route blocking.
- `PRA_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1222`: 22 focuses with 4 mutex declarations.
- The 18-focus chaos trees `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` each have 4 mutex declarations inside very small trees.
- `NLC_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:24410`: 47 focuses with 4 mutex declarations; also has a pathline issue.

Pathline and layout issues found by focus graph geometry:

- `soviet_collapse_ukraine_focus_tree`:
  - `ukr_soviet_collapse_army_of_the_republic` -> `ukr_soviet_collapse_general_staff_war_college` has the child above/level with the parent; child at `common/national_focus/005_soviet_collapse_republics.txt:604`.
  - `ukr_soviet_collapse_first_republican_line` -> `ukr_soviet_collapse_war_without_a_declaration` line passes through `ukr_soviet_collapse_foreign_courts_notice_kyiv`; child at `common/national_focus/005_soviet_collapse_republics.txt:179`.
  - `ukr_soviet_collapse_foreign_courts_notice_kyiv` -> `ukr_soviet_collapse_open_the_liaison_offices` line passes through `ukr_soviet_collapse_war_without_a_declaration`; child at `common/national_focus/005_soviet_collapse_republics.txt:226`.
  - `ukr_soviet_collapse_workers_congress_in_kharkiv` -> `ukr_soviet_collapse_left_league_delegation` line passes through `ukr_soviet_collapse_village_soviets_without_requisition`; child at `common/national_focus/005_soviet_collapse_republics.txt:473`.
  - `ukr_soviet_collapse_officers_above_parties` -> `ukr_soviet_collapse_officer_patronage_lists` line passes through `ukr_soviet_collapse_grain_loan`; child at `common/national_focus/005_soviet_collapse_republics.txt:576`.
  - `ukr_soviet_collapse_foreign_courts_notice_kyiv` -> `ukr_soviet_collapse_german_liaison_question` line passes through `ukr_soviet_collapse_war_without_a_declaration` and `ukr_soviet_collapse_open_the_liaison_offices`; child at `common/national_focus/005_soviet_collapse_republics.txt:1363`.
- `soviet_collapse_baltic_focus_tree`: `baltic_soviet_collapse_a_port_without_a_master` -> `baltic_soviet_collapse_the_baltic_question_resolved` line passes through `baltic_soviet_collapse_tallinn_riga_vilnius_rotation`; child at `common/national_focus/005_soviet_collapse_republics.txt:5300`.
- `soviet_collapse_central_asia_focus_tree`: `central_asia_soviet_collapse_khwarazm_restoration_debate` -> `central_asia_soviet_collapse_the_southern_shield` has same-row parent/child risk; child at `common/national_focus/005_soviet_collapse_republics.txt:7270`.
- `soviet_collapse_belarus_focus_tree`: `blr_soviet_collapse_decentralized_detachments` -> `blr_soviet_collapse_the_forest_state_rumor` line passes through `blr_soviet_collapse_minsk_does_not_own_every_tree`; child at `common/national_focus/005_soviet_collapse_republics.txt:9887`.
- `TSC_soviet_collapse_focus_tree`: `TSC_the_committee_of_instruments` -> `TSC_night_survey_columns` line passes through `TSC_observatory_guard`; child at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2126`.
- `RMC_soviet_collapse_focus_tree`: `RMC_communes_of_witnesses` -> `RMC_hagiographers_of_every_front` line passes through `RMC_reliquary_guard`; child at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2609`.
- `DSC_soviet_collapse_focus_tree`: `DSC_witness_officers` -> `DSC_maps_of_lost_armies` line passes through `DSC_field_hospital_memorials`; child at `common/national_focus/005_soviet_collapse_custom_splinters.txt:3131`.
- `NRF_soviet_collapse_focus_tree`: `NRF_living_harbor_committees` -> `NRF_maps_of_sunken_routes` line passes through `NRF_icebound_marine_guard`; child at `common/national_focus/005_soviet_collapse_custom_splinters.txt:3668`.
- `ICD_soviet_collapse_focus_tree`: `ICD_commissars_of_last_addresses` -> `ICD_archives_of_every_front` line passes through `ICD_funeral_guard`; child at `common/national_focus/005_soviet_collapse_custom_splinters.txt:4155`.
- `DHC_soviet_collapse_focus_tree`: `DHC_stanitsa_mediation` -> `DHC_convoy_autonomy_guarantees` line passes through `DHC_stanitsa_autonomy_statute`; child at `common/national_focus/005_soviet_collapse_custom_splinters.txt:14615`.
- `KHC_soviet_collapse_focus_tree`: `KHC_stanitsa_mediation` -> `KHC_grain_passage_guarantees` line passes through `KHC_stanitsa_autonomy_statute`; child at `common/national_focus/005_soviet_collapse_custom_splinters.txt:15808`.
- `UWD_soviet_collapse_focus_tree`: `UWD_league_arsenal_bargain` -> `UWD_arsenal_federation_terms` line passes through `UWD_industry_plan`; child at `common/national_focus/005_soviet_collapse_custom_splinters.txt:19566`.
- `NLC_soviet_collapse_focus_tree`: `NLC_greenhouse_boards` -> `NLC_heated_workshop_contracts` line passes through `NLC_settlement`; child at `common/national_focus/005_soviet_collapse_custom_splinters.txt:25177`.

## 4. Too Few Focus-Staged Decisions or Expansion Mechanics

Trees with no or near-no focus-staged decisions, wars, claims, cores, or unit mechanics should be treated as rework candidates, not cleanup candidates.

No focus-staged decision hooks in scope:

- `soviet_collapse_breakaway_focus_tree`: 36 focuses, 0 decisions, 0 wars, 0 claims/cores.
- `soviet_collapse_internal_republic_focus_tree`: 62 focuses, 0 decisions, 0 wars, 1 claim.
- `soviet_collapse_baltic_focus_tree`: 42 focuses, 0 decisions, 0 wars, 0 claims/cores.
- `soviet_collapse_moldova_focus_tree`: 48 focuses, 0 decisions, 0 wars, 0 claims/cores.
- `FTH`, `BBH`, `KRS`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, and `BAC`: each 47 focuses with 0 decisions, 0 wars, 0 claims/cores.

Low focus-staged decision hooks:

- `RMC`: 18 focuses, 1 decision, 2 wars, 2 claims.
- `ICD`: 18 focuses, 1 decision, 2 wars, 2 claims.
- `BSC`, `TNC`, `ALA`, `UDC`, and `NLC`: each 47 focuses with only 2 decision references and no direct wars/claims/cores.
- `ARD`: 47 focuses with 3 decision references and no direct wars/claims/cores.
- `TSC`: 18 focuses with 3 decisions, 2 wars, 0 claims/cores.
- `soviet_collapse_caucasus_focus_tree`: 40 focuses with 4 decisions and no direct wars/claims/cores.

Category shell note: decision category files contain Event005 categories for many of these tags, but the focus trees often do not stage or unlock enough active decision content. The parent should wire focus rewards into existing or expanded decision families rather than adding more passive helper stacks.

## 5. Prioritized Patch Order for Parent

1. Fix duplicate helper spam first. Split visible tooltip helpers from payload helpers or add one-shot focus-completion flags so one focus cannot display/apply `soviet_collapse_apply_focus_rail_authority_reward` or `soviet_collapse_apply_focus_mobile_columns_reward` twice through direct and plan-helper calls. Start with the exact focus ids in section 1.
2. Rebuild the repeated 47-focus high-chaos custom splinter family into distinct lane trees. Start with `FTH` as the template repair, then apply bespoke identity passes to `BBH`, `KRS`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, and `BAC`. These are the worst "OP chaos country but not OP" surfaces because they have no decision, war, claim, or core hooks.
3. Add focus-staged decision and expansion mechanics to custom splinters. Each chaos tree should have at least one political mechanic category, one industry/logistics category or mission chain, and one expansion chain that produces claims, war goals, cores/compliance, units, or postwar decisions.
4. Rework the generic/republic fallback surfaces: `soviet_collapse_breakaway_focus_tree`, `soviet_collapse_baltic_focus_tree`, `soviet_collapse_moldova_focus_tree`, `soviet_collapse_internal_republic_focus_tree`, and `soviet_collapse_caucasus_focus_tree`. These should stop being helper-stack trees and gain clear political, industry, and expansion lanes.
5. Sweep pathlines and mutexes after mechanic changes. Fix the exact pathline blockers in section 3, then reassess `CFR`, `PRA`, the 18-focus chaos trees, and `NLC` for pointless mutex density.
6. Expand ancient restorations after the worst shallow trees are fixed. `KZR`, `SOG`, `KHW`, and `ALN` already have basic war/claim/core hooks, so the next pass should deepen their political and industry lanes rather than merely adding more conquest.

## Validation

Audit commands included:

- `rg` checks for focus idea effects, helper definitions, helper tooltips, and setup/idea cleanup chains.
- Scripted focus-block parsing to count focuses, mutexes, decision hooks, war hooks, claim/core hooks, helper calls, and duplicate coordinates.
- Focus graph geometry checks for parent/child line crossings and same-row parent-child risks.

No gameplay files were patched. No simplifications were used beyond the explicit read-only audit scope.
