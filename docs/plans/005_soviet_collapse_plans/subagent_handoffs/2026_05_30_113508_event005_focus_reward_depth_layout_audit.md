# Event 005 Soviet Collapse Focus Reward, Depth, and Layout Audit

Timestamp: 2026-05-30 11:35:08 UTC

Subagent role: Chaos Redux focus tree subagent

Scope audited:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Hard boundary followed:

- No gfx, flag, sprite, scripted effect, scripted trigger, decision, or localisation files were edited.
- No focus-file gameplay edits were made because the remaining issues are broad reward/helper design problems or unverified in-game pathline risks.
- This handoff is the only file intentionally changed.

References consulted:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`.
- Vanilla focus precedent was sampled from `~/projects/Hearts of Iron IV/common/national_focus`.
- Event source spec: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`.
- Current focus redesign plan: `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.

## Route Coverage Table

| Route or tree family | Current implementation | Status | Evidence |
| --- | --- | --- | --- |
| Ukraine | 83 focuses with statehood, socialist, democratic, military, foreign/protectorate, League, grain, Black Sea, and high-chaos branches. | Partial | Mechanically large, but 38 focuses still match small/variable-heavy reward patterns. Coordinates pass the mechanical row/prerequisite checks, but in-game pathlines remain unverified. |
| Belarus | 53 focuses with corridor, rail, forest, national council, socialist, military transit, foreign corridor, League freight, and forest end states. | Partial | 26 focuses match small/variable-heavy reward patterns. Coordinates pass mechanical checks, but dense rail/forest convergence still needs screenshot validation. |
| Kazakhstan | 92 focuses across Alash/socialist/resource, steppe, military, diplomacy, industry, and regional branches. | Partial | Largest republic tree, but 45 focuses match small/variable-heavy reward patterns. Needs stronger payoff proof, not just more nodes. |
| Shared republic trees | Breakaway, internal republic, Baltic, Caucasus, Central Asia, Moldova. | Partial | Branches exist, but several trees still lean on `soviet_collapse_apply_focus_legal_recognition` and variable progression rather than visible route payoffs. |
| Full custom splinters | 19 main custom splinter trees at 47 focuses each. | Partial | Trees are large by count, but repeated helper patterns make many countries feel templated. Examples: repeated `*_first_guard`, `*_stores`, `*_league`, `*_enemy_front` identity helpers. |
| Compact chaos/crisis splinters | PRA, TSC, RMC, DSC, NRF, ICD at 18-22 focuses. | Partial | These have stronger concept hooks but are still narrow. Violent/chaos identities need more direct overpowered war, claim, unit, or pressure mechanics. |
| Factory successors | CFR 47, MFR 58, OGB 23 focuses. | Partial | CFR/MFR have real branches; OGB remains shallow for a successor with restoration identity. |
| Ancient restorations | KZR, SOG, KHW, ALN at 16 focuses each. | Incomplete for major-tree depth | They have identity hooks and claims, but remain compact stubs compared with the spec's focus-tree standard. |

## Direct and Indirect Idea-Spam Examples

Current focus-file finding:

- Direct `add_ideas`, `swap_ideas`, or `add_timed_idea` inside the four focus files: 0.
- Direct focus-file idea operations found: 7, all `remove_ideas` cleanup, not direct spirit creation.
- Because the parent is patching scripted effects, I did not edit helper logic. I only read helper definitions enough to distinguish confirmed focus-file evidence from helper-side risk.

Direct remove-only examples:

| File:line | Focus id | Direct idea operation |
| --- | --- | --- |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt:1366` | `PRA_the_board_overrules_ministers` | `hidden_effect = { remove_ideas = pra_dispatcher_court_tensions }` |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt:1960` | `TSC_the_committee_of_instruments` | `hidden_effect = { remove_ideas = tsc_field_station_rivalries }` |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt:2394` | `RMC_communes_of_witnesses` | `hidden_effect = { remove_ideas = rmc_credal_cell_rivalries }` |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt:2884` | `DSC_witness_officers` | `hidden_effect = { remove_ideas = dsc_grave_regiment_rivalries }` |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt:3470` | `NRF_living_harbor_committees` | `hidden_effect = { remove_ideas = nrf_drowned_crew_disputes }` |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt:3976` | `ICD_commissars_of_last_addresses` | `hidden_effect = { remove_ideas = icd_grave_commissar_rivalries }` |
| `common/national_focus/005_soviet_collapse_factory_successors.txt:1225` | `OGB_the_council_takes_the_seal` | `hidden_effect = { remove_ideas = ogb_disputed_restored_name }` |

Focus-visible helper risk examples:

| Helper visible in focus files | Count | Example focus ids | Audit note |
| --- | ---: | --- | --- |
| `soviet_collapse_apply_focus_legal_recognition` | 305 | `KZR_returned_names_endgame`, `FTH_diplomatic_plan`, many republic/custom focuses | Broad shared helper creates sameness. It calls recognition/recovery/route payload helpers; the actual staged idea updater is outside the focus files. |
| `soviet_collapse_add_republic_focus_recovery_progress` | 10 direct calls | `FTH_village_delegate_roads`, `DHC_manych_rear_area`, `NLC_ration_and_signal_escorts` | Helper removes startup disorder at thresholds; it does not directly add new staged ideas in the current helper definition. |
| `soviet_collapse_apply_focus_high_chaos_identity` | 98 | `FTH_extreme_path`, `PRA_passport_of_the_moving_state`, `TSC_claim_the_impact_zone` | Current helper is strong but generic: manpower/equipment/war support/claims/AI strategy. It does not directly add ideas, but repeated use flattens chaos identity. |
| `soviet_collapse_apply_custom_splinter_first_guard_identity` | 19 | `FTH_first_guard`, `BSC_first_guard`, `TNC_first_guard` | Repeated country-template helper. Safer to diversify helper payloads in scripted effects than patch individual focus files blindly. |
| `soviet_collapse_apply_custom_splinter_stores_identity` | 19 | `FTH_stores`, `BSC_stores`, `TNC_stores` | Repeated stores/economy identity helper. |
| `soviet_collapse_apply_custom_splinter_league_identity` | 38 | `FTH_league`, `FTH_diplomatic_plan`, `BSC_league` | Repeated diplomatic/League helper. |
| `soviet_collapse_apply_custom_splinter_enemy_front_identity` | 36 | `FTH_enemy_front`, `FTH_war_plan`, `ALA_war_plan` | Repeated front/war helper. |

Conclusion on the complaint: the current focus files do not directly create idea spam with `add_ideas` or `swap_ideas`. The focus-level problem is helper overuse and repeated variable/identity payloads. If idea churn still appears in-game, the parent should inspect `soviet_collapse_update_consolidated_republic_ideas`, `soviet_collapse_clear_republic_staged_ideas`, and focus-called helpers from scripted effects. That is outside this subagent's edit boundary.

## Highest-Impact Shallow Reward Clusters

Mechanical shallow-pattern audit: 529 focuses have reward blocks dominated by variables, equipment, PP/stability/war support, XP, manpower, or command power and no direct building/claim/core/wargoal/decision/unit/faction/country-event/identity helper in the same reward block.

Top clusters:

| Tree | Count | Example focus ids |
| --- | ---: | --- |
| `soviet_collapse_kazakhstan_focus_tree` | 45 | `kaz_soviet_collapse_alma_ata_emergency_congress`, `kaz_soviet_collapse_guard_the_resource_towns`, `kaz_soviet_collapse_resource_defense_directorate` |
| `soviet_collapse_ukraine_focus_tree` | 38 | `ukr_soviet_collapse_emergency_rada`, `ukr_soviet_collapse_question_of_statehood`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_purge_moscow_loyalists` |
| `soviet_collapse_belarus_focus_tree` | 26 | `blr_soviet_collapse_minsk_emergency_office`, `blr_soviet_collapse_forest_committees_report_in`, `blr_soviet_collapse_timetable_state` |
| `soviet_collapse_moldova_focus_tree` | 23 | `moldova_soviet_collapse_chisinau_emergency_council`, `moldova_soviet_collapse_guard_the_dniester_crossings`, `moldova_soviet_collapse_conditional_union` |
| `UDC_soviet_collapse_focus_tree` | 18 | `UDC_birth`, `UDC_emergency_staff_college`, `UDC_command_mediation` |
| `SDZ_soviet_collapse_focus_tree` | 17 | `SDZ_birth`, `SDZ_internal_troop_school`, `SDZ_no_file_burned_order` |
| `GAC_soviet_collapse_focus_tree` | 17 | `GAC_birth`, `GAC_village_delegate_registers`, `GAC_food_for_autonomy_clause` |
| `OGB_soviet_collapse_focus_tree` | 14 | `OGB_open_the_volga_registers`, `OGB_restore_the_bolghar_name`, `OGB_the_council_takes_the_seal` |
| `MFR_soviet_collapse_focus_tree` | 12 | `MFR_arsenal_board_meets`, `MFR_officers_chair_the_board`, `MFR_shells_without_sleep` |

Interpretation: Kazakhstan, Ukraine, and Belarus have many focuses, but too many rewards are still progression-value packets. OGB and the ancient restorations are shallow by total branch count.

## Ukraine and Belarus Layout Findings

Mechanical coordinate checks:

| Tree | Same-row spacing <= 1 | Prerequisite not above child | Mechanical result |
| --- | ---: | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | 0 | 0 | No simple coordinate collision or upside-down prerequisite was found. |
| `soviet_collapse_belarus_focus_tree` | 0 | 0 | No simple coordinate collision or upside-down prerequisite was found. |

Unverified in-game pathline risks:

- Ukraine still has an ugly visual risk because route selectors and later route content share a wide, dense mid-tree field: rows 4-10 contain democratic, socialist, military, foreign, Black Sea, protectorate, and grain/League branches. The mechanical audit cannot prove that HOI4's pathline sprites look clean.
- Belarus is mechanically spaced, but rows 5-11 remain visually dense around `blr_soviet_collapse_national_council_of_minsk`, `blr_soviet_collapse_socialist_autonomy_without_moscow`, `blr_soviet_collapse_military_transit_directorate`, `blr_soviet_collapse_foreign_corridor_administration`, `blr_soviet_collapse_join_the_league_when_war_comes`, `blr_soviet_collapse_prepare_league_freight_tables`, and `blr_soviet_collapse_the_league_depot_at_minsk`.
- I did not move coordinates because the current mechanical checks are clean and a true fix needs in-game screenshot/pathline review or a deliberate route-layout pass.

## Icon Coverage Table

| File | Focuses | Unique icon ids | Repeated icon groups | Missing sprite defs |
| --- | ---: | ---: | ---: | ---: |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 64 | 42 | 8 | 0 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 1005 | 885 | 99 | 0 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 128 | 113 | 11 | 0 |
| `common/national_focus/005_soviet_collapse_republics.txt` | 501 | 458 | 22 | 0 |

Repeated icon examples:

- Ancient restorations reuse `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_guard_old_routes`, `GFX_focus_soviet_collapse_ancient_league_bargain`, and several end-state icons across all four 16-focus trees.
- Custom splinters repeat large identity families, including `GFX_focus_FEV_diplomatic_plan`, `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_civil_rule`, `GFX_focus_MRC_foreign`, `GFX_focus_IUL_supply`, and `GFX_focus_IUL_war_plan`.
- Republics still repeat `GFX_ukr_soviet_collapse_democratic`, `GFX_ukr_soviet_collapse_industry`, and several shared regional icons.

## Localisation and Reward Mismatch List

Mechanical localisation result:

- Focus ids checked: 1,698.
- Missing focus name keys: 0.
- Missing focus description keys: 0.

Qualitative mismatches and risks:

- Ukraine focus names like `ukr_soviet_collapse_direct_national_claims`, `ukr_soviet_collapse_black_sea_hegemony`, `ukr_soviet_collapse_breadbasket_empire`, and `ukr_soviet_collapse_great_steppe_and_sea_plan` promise major territorial or economic identity. The focus files often rely on variables/helpers instead of direct visible claims, cores, war goals, units, or decisions.
- Belarus focus names around rail/freight identity are coherent, but rewards still cluster around variable progression, rail helpers, equipment, and recognition. The corridor identity needs stronger decision/mission or map-control payoff.
- Custom splinter names are more country-specific than before, but repeated helper families still make rewards feel templated.
- Ancient restoration descriptions likely over-promise depth relative to 16-focus trees.

## AI Behavior Gaps

Mechanical AI result:

- Missing `ai_will_do`: 0.

Remaining AI quality gaps:

- Many AI blocks are scalar pressure checks rather than route plans. They react to SOV variables, war, stability, or foreign appetite, but not enough to make Ukraine/Belarus/chaos tags pursue distinct strategies.
- Ukraine AI should deliberately choose between socialist, democratic, military, foreign-authority, Black Banner, League, and grain-hegemony futures.
- Belarus AI should distinguish rail neutrality, League freight, military transit, foreign corridor, and forest-state risks.
- Violent chaos successors should prefer expansion/war/OP branches when valid instead of spending too long on ordinary stabilization.

## High-Priority Fixes First

1. Parent-side scripted helper cleanup for staged spirits. The focus files no longer directly add/swap ideas, so the actual idea-churn fix belongs in scripted effects, especially staged idea updater and helper lifecycle code.
2. Ukraine route layout screenshot pass. Mechanical coordinates are clean, but visual pathlines remain unproven.
3. Belarus route layout screenshot pass around rail/freight/forest convergence.
4. Replace shallow reward clusters in Ukraine, Belarus, Kazakhstan, OGB, and compact chaos tags with direct decisions, missions, claims, wargoals, units, industrial map changes, or recurring mechanics.
5. Diversify custom splinter helper payloads per tag. Repeated `first_guard`, `stores`, `league`, and `enemy_front` helpers are the biggest source of template feel.
6. Expand or explicitly scope down OGB and the four ancient restoration trees.
7. Replace repeated icon clusters when the parent resumes asset/icon work. Do not touch flags.

## Patch Status

Gameplay patch made: none.

Changed focus ids: none.

Changed localisation keys: none.

Changed icon ids: none.

Route behavior before and after:

- No route behavior changed in this pass.
- The audit intentionally avoids focus-file reward edits because the strongest fixes require scripted helper/localisation work owned by the parent and because the current Ukraine/Belarus mechanical coordinate checks do not justify blind coordinate moves.

## Validation Run

Commands were run from `/home/klim/projects/chaos_redux` by mechanical parser/grep over `common/national_focus/005_soviet_collapse_*.txt` plus localisation/interface lookups.

Results:

- Brace depth: all four focus files ended at depth 0 with no negative depth.
- Duplicate focus ids: 0.
- Unsupported `<=` or `>=`: 0 matches.
- Missing `ai_will_do`: 0.
- Direct focus-file `add_ideas`/`swap_ideas`/`add_timed_idea`: 0.
- Direct focus-file `remove_ideas`: 7, listed above.
- Missing focus localisation names/descriptions: 0/0.
- Focus icon ids used: 1,698.
- Unique focus icon ids: 1,498.
- Missing focus sprite definitions across mod and vanilla interface: 0.
- Ukraine/Belarus same-row spacing <= 1: 0.
- Ukraine/Belarus prerequisite-not-above-child mechanical cases: 0.

Skipped validation:

- No in-game load test.
- No screenshot/pathline validation.
- No scripted helper patch validation, because scripted effects are outside this subagent's edit boundary and parent is patching them.
- No commit created because the worktree was already dirty with parent work across Event 005 and Event 006.

## Remaining Route Risks

- Current user complaints are not fully resolved by focus-file-only work.
- Idea spam, if still present in-game, is likely helper-side rather than direct focus reward syntax.
- Ukraine and Belarus may still look ugly in-game despite clean mechanical coordinates.
- Chaos countries remain underpowered by identity design in several places because rewards still skew toward variables, equipment, and shared helper payloads.
- OGB and ancient restorations remain shallow by count and branch depth.
