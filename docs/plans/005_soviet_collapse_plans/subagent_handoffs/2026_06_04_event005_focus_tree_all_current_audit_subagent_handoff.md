# Event005 Soviet Collapse Focus Tree Audit Handoff

Date: 2026-06-04
Role: Chaos Redux focus-tree audit subagent
Scope: all Soviet Collapse focus trees in `common/national_focus/005_soviet_collapse_*.txt`

## Required References Consulted

- Repo instructions: `AGENTS.md`
- Skill: `.agents/skills/hoi4-focus-trees/SKILL.md`
- Offline wiki snapshot: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`
- Vanilla focus precedents: `common/national_focus/soviet.txt`, `china_warlord.txt`, `italy.txt`
- Event005 design docs: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`, `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`, `docs/events/005_soviet_collapse.md`

No web references were used. No flag sprites or flag asset files were touched.

## Files Audited

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- Integration reference: `common/scripted_effects/005_soviet_collapse_effects.txt`

## Executive Findings

The current focus set is no longer dominated by direct focus-level idea spam. A direct scan found no `add_ideas`, `swap_ideas`, or `add_timed_idea` usage inside the four Soviet Collapse focus files. Most rewards now route through flags, scripted effects, variables, decisions, construction, and equipment helpers.

The remaining severe issue is not mechanical spam; it is uneven design depth. The strongest republic trees have distinct route surfaces, but several chaos/special trees remain too compact for the requested full rework into political, industrial, military, diplomacy, expansion, and special-mechanic branches. Some 47-focus custom splinters are structurally large but still rely heavily on shared helper patterns, so their aggressive expansion identity is not always visible enough from the focus surface.

Layout is mostly clean in the script-level coordinate audit. I patched one Belarus layout defect. After the patch, the mechanical audit found no duplicate focus coordinates and no straight parent-child pathline intersections through other focus nodes. This does not replace in-game screenshot review, because HOI4 routing can still render bends or mutex lines differently than a script-level edge check.

## Patch Made

### `common/national_focus/005_soviet_collapse_republics.txt`

Severity: Medium

Patched focus ids:

- `blr_soviet_collapse_join_the_league_when_war_comes`
- `blr_soviet_collapse_minsk_supplies_the_front`

Change:

- Moved `blr_soviet_collapse_join_the_league_when_war_comes` from `x = 19, y = 9` to `x = 20, y = 10`.
- Moved `blr_soviet_collapse_minsk_supplies_the_front` from `x = 18, y = 11` to `x = 23, y = 12`.

Reason:

- `blr_soviet_collapse_join_the_league_when_war_comes` overlapped `blr_soviet_collapse_orders_printed_like_timetables` at `(19, 9)`.
- The pathline from `blr_soviet_collapse_prepare_league_freight_tables` to `blr_soviet_collapse_minsk_supplies_the_front` crossed through `blr_soviet_collapse_regular_forest_brigades` at `(21, 11)`.

Validation:

- Belarus duplicate-coordinate check after patch: none.
- Belarus parent-child edge-node hit check after patch: none.
- No flag sprite or flag asset files changed.

## Global Mechanical Audit

| Tree | Focuses | Direct ideas | Decision unlocks | Direct war/claim effects | Layout result |
| --- | ---: | ---: | ---: | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | 83 | 0 | 13 | 0 | clean |
| `soviet_collapse_breakaway_focus_tree` | 36 | 0 | 0 | 0 | clean |
| `soviet_collapse_internal_republic_focus_tree` | 62 | 0 | 0 | 0 | clean |
| `soviet_collapse_baltic_focus_tree` | 42 | 0 | 0 | 0 | clean |
| `soviet_collapse_caucasus_focus_tree` | 40 | 0 | 4 | 0 | clean |
| `soviet_collapse_central_asia_focus_tree` | 45 | 0 | 6 | 7 | clean |
| `soviet_collapse_moldova_focus_tree` | 48 | 0 | 0 | 0 | clean |
| `soviet_collapse_belarus_focus_tree` | 53 | 0 | 6 | 0 | patched clean |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | 0 | 6 | 0 | clean |
| `FTH_soviet_collapse_focus_tree` | 47 | 0 | 0 | 0 | clean |
| `PRA_soviet_collapse_focus_tree` | 22 | 0 | 14 | 1 | clean |
| `TSC_soviet_collapse_focus_tree` | 18 | 0 | 1 | 1 | clean |
| `RMC_soviet_collapse_focus_tree` | 18 | 0 | 1 | 1 | clean |
| `DSC_soviet_collapse_focus_tree` | 18 | 0 | 12 | 1 | clean |
| `NRF_soviet_collapse_focus_tree` | 18 | 0 | 6 | 1 | clean |
| `ICD_soviet_collapse_focus_tree` | 18 | 0 | 1 | 1 | clean |
| 18 shared custom splinter trees | 47 each | 0 | 0-3 | mostly 0 | clean |
| `KZR_soviet_collapse_focus_tree` | 16 | 0 | 4 | 9 | clean |
| `SOG_soviet_collapse_focus_tree` | 16 | 0 | 4 | 9 | clean |
| `KHW_soviet_collapse_focus_tree` | 16 | 0 | 4 | 9 | clean |
| `ALN_soviet_collapse_focus_tree` | 16 | 0 | 4 | 12 | clean |
| `CFR_soviet_collapse_focus_tree` | 47 | 0 | 10 | 0 | clean |
| `OGB_soviet_collapse_focus_tree` | 23 | 0 | 5 | 2 | clean |
| `MFR_soviet_collapse_focus_tree` | 58 | 0 | 8 | 2 | clean |

Note: direct war/claim counts only catch focus-file effect names. Scripted helpers may add claims, cores, states, decisions, or units indirectly.

## Findings By Tree Or Tag

### Ukraine

Severity: Medium

Relevant focus ids:

- `ukr_soviet_collapse_black_banner_compact`
- `ukr_soviet_collapse_the_commune_war`
- `ukr_soviet_collapse_black_sea_hegemony`
- `ukr_soviet_collapse_league_security_zone_mandates`
- `ukr_soviet_collapse_the_western_question_cannot_wait`
- `ukr_soviet_collapse_breadbasket_empire`
- `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map`

Assessment:

- The tree is one of the stronger Event005 trees and already has a large reward/mechanic surface.
- It still needs stronger visible map aggression in the route endpoints to meet the current requirement that chaos countries be very overpowered and aggressive.
- The breadbasket, League, Black Sea, and commune routes should produce more direct state changes, war-goal decisions, units, protectorates, or postwar settlement mechanics instead of relying only on scripted helper rewards.

Recommended fixes:

- Add endpoint decisions for Black Sea mandates, western border settlement, and breadbasket protectorates.
- Make the aggressive route tooltips explicitly show claims, cores, generated units, or decision unlocks.
- Add AI strategy hooks for high-chaos Ukraine routes to attack vulnerable neighbors and contest former Soviet assets.

### Belarus

Severity: Medium

Relevant focus ids:

- `blr_soviet_collapse_join_the_league_when_war_comes`
- `blr_soviet_collapse_minsk_supplies_the_front`
- `blr_soviet_collapse_the_corridor_everyone_wants`
- `blr_soviet_collapse_the_green_border`
- `blr_soviet_collapse_partisans_or_army`
- `blr_soviet_collapse_regular_forest_brigades`

Assessment:

- One layout overlap/pathline issue was patched.
- The tree has decision unlocks and a clear rail/forest identity, but it has no direct focus-file equipment rewards and no direct focus-file war/claim effects.
- For the requested aggressive chaos-country standard, the corridor and League-war branches need stronger map consequences.

Recommended fixes:

- Add rail-corridor security decisions that claim or core contested border states when controlled.
- Add forest-brigade unit or template rewards tied to `blr_soviet_collapse_regular_forest_brigades` and `blr_soviet_collapse_partisans_or_army`.
- Add high-chaos AI aggression toward corridor states and exposed neighbors.

### Kazakhstan

Severity: Medium

Relevant focus ids:

- `kaz_soviet_collapse_call_the_steppe_congress`
- `kaz_soviet_collapse_resource_sovereignty`
- `kaz_soviet_collapse_the_southern_republics_write_together`
- `kaz_soviet_collapse_steppe_defense_council`
- `kaz_soviet_collapse_the_steppe_outlives_the_union`

Assessment:

- This is one of the deepest trees at 92 focuses.
- The focus surface has strong construction, equipment, and helper usage, but direct focus-file war/claim effects are absent despite Kazakhstan being a natural Central Asian hegemon in the collapse scenario.

Recommended fixes:

- Add steppe-federation claims, cores, protectorate decisions, and war goals as visible branch rewards.
- Tie resource sovereignty to map control, foreign contracts, or extraction decisions instead of only flat development.
- Give high-chaos Kazakhstan AI stronger expansion strategy against isolated southern and Siberian rivals.

### Shared Breakaway, Internal Republic, Baltic, Caucasus, Central Asia, Moldova Trees

Severity: High

Relevant focus ids:

- `soviet_collapse_assemble_emergency_government`
- `soviet_collapse_the_republic_defines_itself`
- `soviet_collapse_depots_choose_flags_branch`
- `soviet_collapse_a_small_state_with_teeth`
- `internal_soviet_collapse_convene_republic_presidium`
- `internal_soviet_collapse_idel_ural_congress`
- `internal_soviet_collapse_bashkir_cavalry_oath`
- `internal_soviet_collapse_karelian_finnish_border_mission`
- `internal_soviet_collapse_komi_river_and_mine_committees`
- `baltic_soviet_collapse_baltic_league_first`
- `baltic_soviet_collapse_baltic_defense_compact`
- `baltic_soviet_collapse_ports_before_patronage`
- `caucasus_soviet_collapse_caucasus_route_fork`
- `caucasus_soviet_collapse_oil_emergency_directorate`
- `caucasus_soviet_collapse_council_of_passes`
- `caucasus_soviet_collapse_caucasus_defense_compact`
- `central_asia_soviet_collapse_southern_route_fork`
- `central_asia_soviet_collapse_turkestan_federation_road`
- `central_asia_soviet_collapse_federation_delegates`
- `central_asia_soviet_collapse_southern_republics_coordinate`

Assessment:

- These trees avoid direct idea spam and have usable layout, but several remain closer to shared-release scaffolds than bespoke collapse-country experiences.
- The shared breakaway tree has no direct decision unlocks or direct war/claim effects. This makes weak countries feel survivable rather than overpowered or aggressively concept-driven.
- Internal republic, Baltic, Caucasus, Central Asia, and Moldova trees need more tag-specific overlays so the same tree does not play too similarly across distinct regions.

Recommended fixes:

- Add tag-sensitive scripted effects or decisions for state claims, emergency cores, faction pulls, and local war aims.
- Add distinct special-mechanic branches per region: Baltic naval league, Caucasus pass/oil politics, Central Asian federation, internal republic border congresses, Moldova corridor/sponsor mechanics.
- Add route-specific AI strategies so aggressive branches behave aggressively without requiring whole-world on-action loops.

### Compact Special Chaos Trees: TSC, RMC, ICD, DSC, NRF, PRA

Severity: High

Relevant focus ids:

- `TSC_the_sky_keeps_records`
- `TSC_recover_the_burned_glass`
- `TSC_claim_the_impact_zone`
- `TSC_starfall_mandate`
- `TSC_observatory_state`
- `TSC_the_quiet_sky_settlement`
- `RMC_open_the_red_martyrology`
- `RMC_claim_the_burial_roads`
- `RMC_procession_columns`
- `RMC_resurrection_without_state`
- `RMC_shrine_state`
- `ICD_open_the_dead_rolls`
- `ICD_claim_the_unburied_front`
- `ICD_grave_columns_march`
- `ICD_commissariat_without_end`
- `ICD_state_of_last_addresses`
- `DSC_the_rearguard_state`
- `DSC_every_retreat_needs_a_depot`
- `DSC_last_train_out`
- `NRF_the_northern_front_remembers`
- `NRF_claim_the_frozen_line`
- `NRF_no_surrender_in_the_snow`
- `PRA_the_authority_survives`
- `PRA_railway_governance`
- `PRA_emergency_timely_orders`

Assessment:

- TSC, RMC, and ICD are the clearest depth failures at 18 focuses each.
- DSC and NRF are more reward-dense than their size implies, and PRA has many decision unlocks, but the compact trees still cannot satisfy the full branch requirement without expansion.
- Several concepts are strong enough for special mechanics but currently read as short event chains.

Recommended fixes:

- Expand TSC, RMC, and ICD to at least 35-45 focuses or add dense branch modules for politics, industry, military, diplomacy, expansion, special mechanic, and late crisis.
- Give each compact chaos tree a signature aggressive mechanic: TSC impact-zone mandates, RMC martyr processions and shrine states, ICD grave-front commissariats, DSC retreat depot state, NRF frozen-line offensive, PRA railway emergency authority.
- Add named units, decision categories, claim/core conversion, and high-chaos AI war plans to endpoint focuses.

### Shared Custom Splinter Family: BSC, TNC, ALA, BBH, KRS, UDC, SDZ, GAC, DHC, KHC, FEV, SZA, UWD, MRC, IUL, BAC, ARD, NLC

Severity: High

Relevant focus ids:

- `BBH_war_plan`
- `BBH_endgame`
- `BBH_extreme_path`
- `KRS_war_plan`
- `KRS_endgame`
- `UDC_war_plan`
- `UDC_endgame`
- `SDZ_war_plan`
- `SDZ_endgame`
- `GAC_war_plan`
- `GAC_endgame`
- `DHC_war_plan`
- `DHC_endgame`
- `KHC_war_plan`
- `KHC_endgame`
- `FEV_war_plan`
- `FEV_endgame`
- `SZA_war_plan`
- `SZA_endgame`
- `UWD_war_plan`
- `MRC_war_plan`
- `IUL_war_plan`
- `BAC_war_plan`
- `ARD_war_plan`
- `NLC_war_plan`

Assessment:

- These trees are structurally healthy at 47 focuses each and avoid direct idea spam.
- The family still risks same-play because many rewards come through shared helper patterns.
- Several tags have no direct focus-file decision unlocks, so their endpoint aggression may be too hidden or too dependent on generic scripted effects.

Recommended fixes:

- Give every tag a visible war-plan payoff with claims, cores, assault-column units, or decisions against Soviet remnants and nearby rivals.
- Add tag-specific special mechanics where the concept demands it, such as ARD artillery orders, NLC tundra watch, DHC death-state evacuation, FEV far-eastern arsenal, or KHC fortress-carrier logistics.
- Increase high-chaos AI aggression with local strategy plans and route flags, not whole-world on-actions.

### Ancient Restorations: KZR, SOG, KHW, ALN

Severity: High

Relevant focus ids:

- `KZR_old_border_files`
- `KZR_expansionist_steppe_levy`
- `KZR_khazar_charter`
- `KZR_returned_names_endgame`
- `KZR_road_beyond_the_caspian`
- `SOG_old_city_border_files`
- `SOG_expansionist_merchant_claims`
- `SOG_sogdian_city_charter`
- `SOG_cities_beyond_the_desert`
- `KHW_old_oasis_border_files`
- `KHW_expansionist_water_claims`
- `KHW_khwarazmian_water_charter`
- `KHW_delta_without_a_center`
- `ALN_old_pass_border_files`
- `ALN_expansionist_mountain_claims`
- `ALN_alan_pass_charter`
- `ALN_every_pass_a_border`

Assessment:

- These trees have high direct war/claim density for their size and are more aggressive than most compact trees.
- At 16 focuses each, they still compress politics, industry, military, diplomacy, expansion, and special identity into too little space.
- The restoration concepts need more modern-state implementation detail so they are not just symbolic claimant trees.

Recommended fixes:

- Expand each ancient tree into separate administration, army/guard, diplomacy, industrial extraction, ancient-claim, and mythic-high-chaos branches.
- Add postwar settlement effects that rename, core, or reorganize claimed regions when controlled.
- Tie ancient identity to concrete units, state modifiers, decision categories, and AI aggression.

### Factory Successors: CFR, OGB, MFR

Severity: Medium to High

Relevant focus ids:

- `CFR_the_builder_state_marches_east`
- `CFR_build_the_border_bend_the_border`
- `CFR_reconstruction_protectorates`
- `CFR_rebuild_russia_without_moscow`
- `OGB_future_bulgaria_file`
- `OGB_claim_the_old_trade_cities`
- `OGB_volga_restoration_state`
- `OGB_the_volga_cannot_have_two_seals`
- `OGB_the_old_name_survives_modern_war`
- `MFR_the_arsenal_state`
- `MFR_no_peace_without_orders`
- `MFR_eternal_arsenal_marches`
- `MFR_arm_all_clients`
- `MFR_every_border_needs_guns`

Assessment:

- MFR is the closest to the current requirement because it has 58 focuses, decisions, war/claim effects, equipment rewards, and a coherent arsenal-state identity.
- CFR is structurally large and decision-rich, but direct map aggression is still weaker than its builder-state concept should support.
- OGB has some claims and decisions but remains compact at 23 focuses.

Recommended fixes:

- CFR should receive construction-protectorate war goals, factory-city decisions, and high-chaos AI expansion targets.
- OGB should expand into a deeper Volga restoration package with old-city claims, trade-city wars, modern administrative consolidation, and postwar cores.
- MFR should keep avoiding duplicated flat arms rewards and push more payload into client-state, proxy-war, and arsenal-contract decisions.

## Reward And Idea Spam Findings

Severity: Low for direct focus files, Medium for future implementation risk

Findings:

- Direct focus files currently contain no `add_ideas`, `swap_ideas`, or `add_timed_idea` calls.
- The direct reward surface no longer shows repeated focus-level trains/trucks/AA bloat as the dominant issue.
- Some setup effects outside focus files add one founding idea guarded by `NOT = { has_idea = ... }`; that pattern is acceptable and not repeated focus idea spam.

Recommended guardrails:

- Keep focus rewards centered on decision unlocks, state changes, unit/template unlocks, claims, cores, route flags, and scripted mechanics.
- If a future focus needs an idea, use one route-defining idea and modify/replace it intentionally; do not stack multiple small flat ideas.
- Avoid long `completion_reward` lists that grant unrelated factories, trains, trucks, AA, manpower, and stability at once. Split them into concept-bound mechanics.

## Layout Findings

Severity: Low after patch

Findings:

- Script-level duplicate coordinate audit is clean after the Belarus patch.
- Script-level straight parent-child pathline intersection audit is clean after the Belarus patch.
- Mutex lines and HOI4's actual rendered bends should still be checked with screenshots for dense trees.

Recommended screenshot-review priority:

- `soviet_collapse_ukraine_focus_tree`
- `soviet_collapse_belarus_focus_tree`
- `soviet_collapse_kazakhstan_focus_tree`
- `MFR_soviet_collapse_focus_tree`
- `CFR_soviet_collapse_focus_tree`

## Implementation Follow-Up Plan

Priority 1:

- Expand TSC, RMC, ICD, OGB, and the ancient restoration trees into full branch structures.
- Add visible aggression endpoints to every chaos-country war route: claims, cores, war goals, units, decisions, and AI strategy hooks.

Priority 2:

- Add tag-specific overlays to shared breakaway/internal/Baltic/Caucasus/Central Asia/Moldova trees.
- Convert hidden helper-only payloads into clear tooltips and decision unlocks where player expectation requires it.

Priority 3:

- Run in-game screenshot review of dense focus panels after the next layout tranche.
- Re-run the direct idea/reward spam scan after every focus tranche.

## Validation Performed

- Read required offline wiki pages and vanilla references before conclusions.
- Parsed all four Soviet Collapse focus files for focus counts and direct reward categories.
- Scanned all four Soviet Collapse focus files for direct focus-level idea grants: no matches.
- Scanned focus coordinates for duplicate nodes: clean after the Belarus patch.
- Scanned straight parent-child paths for focus-node intersections: clean after the Belarus patch.
- Confirmed no flag sprite or flag asset files were edited.

## Simplifications, Omissions, And Blockers

- This was an audit and bounded-layout-patch pass, not a full focus-tree rework.
- No broad reward/depth rework was implemented because the identified gaps affect many routes and belong in parent-owned implementation tranches.
- No commit was created because the worktree already contains extensive unrelated tracked and untracked changes, including dirty Event005 files. Committing the touched shared focus file would risk including unrelated user or parent-agent work unless the parent isolates this patch deliberately.
- No in-game screenshot review was performed by this subagent; the script-level layout audit cannot prove every rendered mutex/pathline shape.
