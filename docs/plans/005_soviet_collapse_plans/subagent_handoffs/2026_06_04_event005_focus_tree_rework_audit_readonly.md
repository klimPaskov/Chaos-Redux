# Event005 Soviet Collapse Focus Tree Rework Audit

Scope: read-only audit of current Event005 Soviet Collapse focus trees. No gameplay, localisation, gfx, or flag files were edited.

Required local references read before audit:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- Vanilla focus precedent: `~/projects/Hearts of Iron IV/common/national_focus/generic.txt`, `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`

## Files Audited

- `common/national_focus/005_soviet_collapse_republics.txt`: 9 focus trees, 501 focuses.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: 29 focus trees, 1,055 focuses.
- `common/national_focus/005_soviet_collapse_factory_successors.txt`: 3 focus trees, 128 focuses.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: 4 focus trees, 64 focuses.
- `common/scripted_effects/005_soviet_collapse_effects.txt`: checked for direct one-helper idea applications and visible helper tooltips.

## Reward Spam And Helper Stacking

Mechanical scan found no direct or one-helper duplicate `add_ideas` / `add_timed_idea` application inside a single focus. The remaining problem is visible reward stacking: focuses still combine a focus-specific tooltip with two or more helper effects that each surface another helper tooltip, or stack repeated stockpile/building rewards.

Current counts:

- 305 focuses have two or more direct helper calls in one completion reward.
- 537 focuses have two or more direct or one-helper-surfaced tooltip rewards.
- 188 focuses have repeated direct or one-helper stockpile rewards.
- 0 focuses had duplicate direct or one-helper idea application by exact idea key.

Exact high-priority helper-stacking cases:

| File line | Focus | Problem |
| --- | --- | --- |
| `005_soviet_collapse_factory_successors.txt:53` | `CFR_the_trust_office_takes_the_seal` | `soviet_collapse_apply_cfr_focus_public_works` plus `soviet_collapse_advance_cfr_site_registry_depth`; visible helper stack in first branch step. |
| `005_soviet_collapse_factory_successors.txt:418` | `CFR_factories_first` | `soviet_collapse_apply_cfr_focus_civilian_build` plus `soviet_collapse_advance_cfr_contract_network_depth`; conceptually one factory-directorate payoff should be one helper. |
| `005_soviet_collapse_factory_successors.txt:567` | `CFR_a_civilian_factory_in_every_capital` | `soviet_collapse_apply_cfr_focus_foreign_factory_network` plus `soviet_collapse_apply_cfr_builder_state_buildout`, two unlock tooltips, and factory-city belt unlock. |
| `005_soviet_collapse_factory_successors.txt:1000` | `CFR_pour_the_final_foundation` | `soviet_collapse_apply_cfr_builder_state_buildout` plus `soviet_collapse_apply_cfr_raise_factory_city_belt`; final payoff should collapse into one construction-directorate effect. |
| `005_soviet_collapse_custom_splinters.txt:1272` | `PRA_omsk_station_guard` | Decision unlock, depot variables, rail guard spawn, and military consolidation helper in one reward. |
| `005_soviet_collapse_custom_splinters.txt:1296` | `PRA_count_the_locomotives` | Decision unlock, custom tooltip, rail/supply construction, corridor helper, and depot helper in one focus. |
| `005_soviet_collapse_custom_splinters.txt:1405` | `PRA_armored_train_directorate` | Custom tooltip, rail/supply construction, rail authority helper, idea update, guard spawn, and military helper. |
| `005_soviet_collapse_custom_splinters.txt:1691` | `PRA_seize_the_junction_cities` | Decision unlock, custom tooltip, train reward, construction, military helper, guard spawn, expansion claims, and SOV pressure. |
| `005_soviet_collapse_custom_splinters.txt:1732` | `PRA_rails_over_capitals` | Wargoal, custom route tooltip, AI strategies, high-chaos identity, endgame helper, and rail construction. |
| `005_soviet_collapse_custom_splinters.txt:3005` | `DSC_grave_ordnance_claims` | Chaos assault, front-road claims, front-road cores, generic expansion claims, and assault columns in one focus. |
| `005_soviet_collapse_custom_splinters.txt:3213` | `DSC_claim_the_soldiers_road` | Front-road claims, cores, high-chaos identity, generic expansion claims, assault columns, and dead-army neighbor wars in one focus. |
| `005_soviet_collapse_custom_splinters.txt:3309` | `DSC_congress_of_the_dead_army` | Dead-army campaign helper plus endgame helper; should be the OP route climax, but the reward is helper-stack opaque. |
| `005_soviet_collapse_custom_splinters.txt:3349` | `DSC_memorial_frontier_state` | Endgame helper plus lawful supply helper; living-state branch payoff remains generic. |
| `005_soviet_collapse_custom_splinters.txt:3489` | `NRF_living_harbor_committees` | Tooltip, tension cleanup, decision unlock, infantry stockpile, convoy stockpile, variables, and coastal construction. |
| `005_soviet_collapse_custom_splinters.txt:3831` | `NRF_northern_revenant_fleet` | Decision unlock, high-chaos identity, wargoal, custom route tooltip, AI strategies, expansion claims, assault columns, and endgame helper. |

Template-generated custom splinters repeat the same issue heavily. Exact tree starts and helper-stack counts from the current scan:

- `FTH_soviet_collapse_focus_tree` starts at `005_soviet_collapse_custom_splinters.txt:16`; 23 helper-stacked focuses, starting with `FTH_first_guard` at line 53, `FTH_stores` at line 78, `FTH_legitimacy` at line 102, `FTH_rival` at line 126, `FTH_economy` at line 173, `FTH_league` at line 197, `FTH_foreign` at line 221, `FTH_inner_faction` at line 245, `FTH_special_arm` at line 269, `FTH_supply` at line 294, `FTH_enemy_front` at line 318.
- `BSC_soviet_collapse_focus_tree` starts at `005_soviet_collapse_custom_splinters.txt:4361`; 20 helper-stacked focuses, same route-label pattern beginning with `BSC_first_guard` at line 4397.
- `UDC_soviet_collapse_focus_tree` starts at `005_soviet_collapse_custom_splinters.txt:10167`; many focuses stack command-network helpers with generic chaos/security helpers, beginning with `UDC_first_guard` at line 10204.
- `SDZ_soviet_collapse_focus_tree` starts at `005_soviet_collapse_custom_splinters.txt:11375`; many focuses stack archive-control helpers with generic route helpers, beginning with `SDZ_first_guard` at line 11416.
- `KRS_soviet_collapse_focus_tree` starts at `005_soviet_collapse_custom_splinters.txt:8942`; helper-tooltips repeat across `KRS_first_guard` at line 8979 through `KRS_extreme_gate` at line 9870.

These should be consolidated into route-specific scripted effects that own the visible tooltip and call payload-only helpers internally. For example, a dead-army focus should call one `dsc_apply_dead_congress_aggression_payoff` effect instead of five generic high-chaos helpers.

## Trees Missing Clear Branch Families

These trees do not clearly separate political, industry, and expansion branches, or the branch labels exist but do not create enough distinct gameplay:

| Tree | File line | Audit finding |
| --- | --- | --- |
| `KZR_soviet_collapse_ancient_focus_tree` | `005_soviet_collapse_ancient_restorations.txt:14` | 16-focus mini-tree; ancient identity, trade, war, and state-building are compressed into reward clusters instead of distinct branch families. |
| `SOG_soviet_collapse_ancient_focus_tree` | `005_soviet_collapse_ancient_restorations.txt:425` | Same 16-focus structure; politics and economy are mostly name/restoration flavor, expansion is concentrated in border-file/payoff focuses. |
| `KHW_soviet_collapse_ancient_focus_tree` | `005_soviet_collapse_ancient_restorations.txt:830` | Irrigation/oasis identity is present but not a real industry branch; expansion and legitimacy are payoff helpers. |
| `ALN_soviet_collapse_ancient_focus_tree` | `005_soviet_collapse_ancient_restorations.txt:1239` | Mountain/pass concept is strong, but branches are too short and expansion helpers carry the actual gameplay. |
| `PRA_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:1222` | Has rail identity, but politics, industry, military, and expansion interleave in one rail ladder. Needs rail/supply network branch, construction/rolling stock branch, neutral corridor diplomacy, and conquest-by-junction branch. |
| `TSC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:1831` | Observatory/signals concept exists; industry is mostly random labs/radar, expansion starts late and is not tied to a distinct anomaly mechanic. |
| `RMC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:2343` | Martyr politics dominates; industry and expansion are shallow shrine/reliquary payoffs. |
| `DSC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:2819` | OP dead congress concept exists, but focus structure is only 18 focuses and relies on helper blobs. Needs a dedicated dead-army politics branch, grave ordnance industry, and neighbor aggression/core branch. |
| `NRF_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:3389` | Naval/dead fleet flavor is clear but political/industry/expansion branches are not separated; final conquest route is a reward stack. |
| `ICD_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:3893` | Death-commissariat tree mirrors RMC/DSC shapes; lacks separate bureaucracy, industry, and expansion branches. |
| `OGB_soviet_collapse_focus_tree` | `005_soviet_collapse_factory_successors.txt:1059` | Better than most mini-trees, but industry and expansion are short Volga/heritage side lanes. Needs clearer trade-city economy versus Idel-Ural aggression/diplomacy. |
| `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` | starts from `005_soviet_collapse_custom_splinters.txt:16` through `24345` | Many are 47-focus generated route-label trees. They have labels like `war_plan`, `industry_plan`, `diplomatic_plan`, `settlement`, `extreme_gate`, but rewards still come from generic helper mixes rather than country-specific political/industry/expansion mechanics. |

Republic trees generally have branch families, but several are too crowded to read cleanly: Ukraine (`005_soviet_collapse_republics.txt:53`), Kazakhstan (`:10130`), Belarus (`:8813`), Central Asia (`:6532`), Moldova (`:7663`).

## Pathline And Mutex Geometry

Exact current line-crossing and layout issues:

| Tree | Exact pathline issue |
| --- | --- |
| `soviet_collapse_ukraine_focus_tree` | `ukr_soviet_collapse_army_of_the_republic` at `005_soviet_collapse_republics.txt:1123` to `ukr_soviet_collapse_general_staff_war_college` at line 605 crosses near `ukr_soviet_collapse_open_the_liaison_offices` at line 227. |
| `soviet_collapse_ukraine_focus_tree` | `ukr_soviet_collapse_army_of_the_republic` line 1123 to `ukr_soviet_collapse_direct_national_claims` line 1736 runs through the diplomatic lane near `ukr_soviet_collapse_open_the_liaison_offices` line 227 and `ukr_soviet_collapse_protectorate_debate` line 1702. |
| `soviet_collapse_ukraine_focus_tree` | `ukr_soviet_collapse_army_of_the_republic` line 1123 to `ukr_soviet_collapse_the_western_question_cannot_wait` line 1986 runs through `ukr_soviet_collapse_open_the_liaison_offices` line 227 and `ukr_soviet_collapse_german_liaison_question` line 1364. |
| `soviet_collapse_ukraine_focus_tree` | `ukr_soviet_collapse_black_soil_oath` line 2100 to `ukr_soviet_collapse_grain_census_of_everyone` line 2156 runs across the late-game lane near `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map` line 2043. |
| `soviet_collapse_central_asia_focus_tree` | Four-way route selector is visually unclear: `central_asia_soviet_collapse_southern_route_fork` line 6599 feeds `local_republic_council` line 6621, `military_border_authority` line 6814, `foreign_border_patronage` line 7020, and `turkestan_federation_road` line 7052. `turkestan_federation_road` sits between other mutually locked options and the military line to `border_commanders` line 6844 passes near it. |
| `soviet_collapse_moldova_focus_tree` | `moldova_soviet_collapse_prut_relief_depots` line 8374 to `moldova_soviet_collapse_bucharest_observer_mission` line 8400 runs through `moldova_soviet_collapse_union_with_romania_question` line 7939, which is the visual route selector for `alliance_not_union` line 8015, `conditional_union` line 8046, and `reject_the_union_question` line 8076. |
| `soviet_collapse_belarus_focus_tree` | `blr_soviet_collapse_minsk_central_dispatch` line 9928 to `blr_soviet_collapse_armored_train_workshops` line 9948 crosses near `blr_soviet_collapse_league_supply_timetables` line 9333. |
| `soviet_collapse_belarus_focus_tree` | `blr_soviet_collapse_decentralized_detachments` line 9602 to `blr_soviet_collapse_the_forest_state_rumor` line 9877 passes directly through `blr_soviet_collapse_minsk_does_not_own_every_tree` line 9672. |
| `soviet_collapse_kazakhstan_focus_tree` | `kaz_soviet_collapse_alash_memory_restored` line 10288 to `kaz_soviet_collapse_the_alash_courts` line 10359 passes near `kaz_soviet_collapse_lone_steppe_state` line 10844. |
| `soviet_collapse_kazakhstan_focus_tree` | `kaz_soviet_collapse_the_army_that_crosses_distance` line 10736 to `kaz_soviet_collapse_steppe_federation_charter` line 10788 crosses near `kaz_soviet_collapse_no_steppe_without_the_south` line 11147 and `kaz_soviet_collapse_border_cavalry_schools` line 11169. |
| `soviet_collapse_kazakhstan_focus_tree` | `kaz_soviet_collapse_steppe_federation_charter` line 10788 to `kaz_soviet_collapse_the_steppe_arbitration_court` line 11314 crosses near `kaz_soviet_collapse_kyrgyz_border_cavalry` line 11289. |
| `NLC_soviet_collapse_focus_tree` | `NLC_greenhouse_boards` line 24986 to `NLC_heated_workshop_contracts` line 25112 passes near `NLC_settlement` line 24855. |
| `UWD_soviet_collapse_focus_tree` | `UWD_workers_canteen_compact` line 19252 to `UWD_kama_foundry_contracts` line 19286 crosses near `UWD_radical_turn` line 19028. |

The worst mutex geometry remains route selectors stretched across unrelated nodes:

- `CFR_elect_the_site_committees` line 136, `CFR_publish_the_planners_charter` line 166, `CFR_invite_the_foreign_contract_board` line 198, and `CFR_the_concrete_committee` line 229 sit on one wide row. The endpoints mutually exclude through intermediate options, producing long horizontal locklines.
- `central_asia_soviet_collapse_local_republic_council` line 6621, `central_asia_soviet_collapse_military_border_authority` line 6814, `central_asia_soviet_collapse_foreign_border_patronage` line 7020, and `central_asia_soviet_collapse_turkestan_federation_road` line 7052 have the same selector problem.
- `moldova_soviet_collapse_alliance_not_union` line 8015, `moldova_soviet_collapse_conditional_union` line 8046, and `moldova_soviet_collapse_reject_the_union_question` line 8076 are tied to the union-question selector, but nearby Prut/Bucharest pathlines confuse the visual choice.

## Rework Priorities

1. `PRA_soviet_collapse_focus_tree`: make rail country mechanically distinct and OP. Split into rail/supply network, rolling-stock industry, armored train military, neutral corridor diplomacy, and junction conquest. Reward style should build railways, supply hubs, infrastructure, train equipment, armored train tech/units, transit toll decisions, and aggressive neighbor rail seizures. Avoid generic high-chaos helper chains in `PRA_seize_the_junction_cities` and `PRA_rails_over_capitals`.
2. `DSC_soviet_collapse_focus_tree`: make dead congress a war machine. Add a dead-congress political branch, grave ordnance/factory branch, field hospital/rearguard branch, and neighbor aggression branch with claims, cores, war goals, and AI conquer strategies. `DSC_grave_ordnance_claims`, `DSC_claim_the_soldiers_road`, and `DSC_congress_of_the_dead_army` should each call one dead-army scripted payoff, not several generic helpers.
3. `CFR_soviet_collapse_focus_tree`: make construction directorate equal factories. The tree should visibly create civilian factories, shared slots, infrastructure, construction decisions, contract networks, and client-city protectorates. Replace stacked public-works/site-registry/factory-network helpers with one construction-directorate payoff per focus.
4. `NRF_soviet_collapse_focus_tree` and `ICD_soviet_collapse_focus_tree`: expand death-state branches. NRF should own ports, convoys, dockyards, coastal forts, naval bases, marines, ghost convoy aggression. ICD should own memorial bureaucracy, dead labor, last-address claims, and unstoppable commissariat expansion.
5. Ancient restoration trees (`KZR`, `SOG`, `KHW`, `ALN`): convert 16-focus symbolic trees into real restoration packages. Each needs old-name politics, trade/industry, military survival, and expansion/restoration endgame paths.
6. Generated custom splinter 47-focus trees: keep template only as a skeleton. Rewrite per country so `war_plan`, `industry_plan`, `diplomatic_plan`, `settlement`, and `extreme_gate` unlock country-specific mechanics rather than generic helper combinations.
7. Republic layout pass: Ukraine, Kazakhstan, Belarus, Moldova, Central Asia need pathline cleanup after reward redesign. Avoid route selectors with four mutually locked siblings on one row.

## Validation Commands Used

No web access was used.

Commands run:

- `sed -n '1,220p' /home/klim/projects/chaos_redux/.agents/skills/hoi4-focus-trees/SKILL.md`
- `sed -n '1,220p' 'paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md'`
- `sed -n '1,80p'` over the required core wiki pages listed above.
- `sed -n '1,180p' '/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md'`
- `sed -n '1,160p' '/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md'`
- `sed -n '1,140p' '/home/klim/projects/Hearts of Iron IV/documentation/modifiers_documentation.md'`
- `sed -n '1,180p' '/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md'`
- `rg -n "mutually_exclusive|relative_position_id|prerequisite|ai_will_do|completion_reward|add_ideas|add_timed_idea|load_focus_tree" '/home/klim/projects/Hearts of Iron IV/common/national_focus/generic.txt' '/home/klim/projects/Hearts of Iron IV/common/national_focus/soviet.txt'`
- `find common/national_focus -maxdepth 1 -type f -name '005_soviet_collapse*.txt' -print | sort`
- `rg -n "add_ideas|add_timed_idea|swap_ideas|remove_ideas|custom_effect_tooltip|hidden_effect|tooltip =|soviet_collapse_apply|soviet_collapse_unlock|soviet_collapse_.*focus" common/scripted_effects/005_soviet_collapse_effects.txt common/national_focus/005_soviet_collapse*.txt`
- Read-only Python parser over the four focus files and `common/scripted_effects/005_soviet_collapse_effects.txt` to count focuses, focus trees, helper stacks, duplicate ideas, stockpile spam, tooltip spam, and pathline hits.
- `rg -n` targeted focus-id checks for Ukraine, Central Asia, Moldova, Belarus, Kazakhstan, PRA, DSC, CFR, and NLC focus ids.
- `git status --short`

## Completion Notes

This was a read-only audit. No simplification was used in the findings: the report records exact current line references for the highest-priority remaining reward, branch, and geometry issues. The helper-stack scan found many more instances than are practical to individually rewrite here; the counts above identify the full scale and the exact priority lines identify the first rework targets.
