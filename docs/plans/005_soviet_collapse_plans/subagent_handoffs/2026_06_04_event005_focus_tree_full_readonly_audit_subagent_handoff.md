# Event005 Soviet Collapse Focus Trees Read-Only Audit

Date: 2026-06-04

Subagent role: Chaos Redux focus-tree auditor

Scope:
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`

No gameplay files were patched. No flag files or flag assets were inspected or modified.

## Executive Summary

The current Event005 focus-tree set is large and uneven: 4 focus files, 41 focus trees, and 1,698 focus blocks. The largest quality gap is not syntax, but route depth and focus-to-mechanic integration. Many 47-focus splinter trees have enough political, industry, and military reward volume to look complete, but still have no focus-staged decision unlocks and only thin expansion payoffs. Several republic trees also remain disconnected from expansion and decision systems despite having 40-92 focuses.

Direct idea spam inside focus rewards is mostly gone: I found no direct `add_ideas`, `add_timed_idea`, `swap_ideas`, or `remove_ideas` calls in the four focus files. The remaining idea-churn risk is indirect through helpers, especially `soviet_collapse_update_pra_authority_idea`, which removes all other PRA authority ideas and adds the current one. Reward-spam risk also remains in high-chaos payload chains where one focus can call several helpers that create units, claims, cores, war goals, and AI conquer strategies.

Layout has no exact duplicate focus coordinates, and continuous focus panels are generally outside the tree bodies. However, many compact trees have focuses one grid cell apart and multiple crossed prerequisite lines, especially ancient restorations, 18-focus high-chaos trees, and several dense republic trees.

## Scripted Audit Summary

I used inline parser scripts, not repo files. Logic summary:
- Brace-matched all `focus_tree = {}` and nested `focus = {}` blocks in the four scoped focus files.
- Extracted tree id, focus id, line number, coordinates, prerequisites, mutual exclusions, `search_filters`, and `completion_reward`.
- Indexed root-level scripted-effect definitions under `common/scripted_effects/*.txt`, then matched focus reward top-level helper calls to scripted-effect definitions.
- Counted reward category signals: ideas, decisions, expansion, military, industry, diplomacy, special mechanics, AI strategy, filters, and approximate layout crossings.
- Read `common/decisions/005_soviet_collapse_decisions.txt` and `common/decisions/categories/005_soviet_collapse_categories.txt` to verify decision-surface connections.

Counts:
- Focus files: 4
- Focus trees: 41
- Focuses: 1,698
- Direct idea operations in focus rewards: 0
- Focuses with exact duplicate coordinates in the same tree: 0
- Trees with zero focus-staged decision links: 22

## Worst Offenders By Tree

### Idea And Reward Churn

| Severity | Tree / focus | Path | Evidence |
| --- | --- | --- | --- |
| High | PRA authority route | `common/national_focus/005_soviet_collapse_custom_splinters.txt:1209` `PRA_the_timetable_declares_authority`; `:1351` `PRA_the_board_overrules_ministers`; `:1382` `PRA_armored_train_directorate`; `:1549` `PRA_passport_of_the_moving_state`; `:1746` `PRA_flags_on_every_station` | These call `soviet_collapse_update_pra_authority_idea`. Helper at `common/scripted_effects/005_soviet_collapse_effects.txt:7478` removes three competing PRA ideas and adds one of four authority ideas depending on flags. This is controlled, but still risks repeated national-spirit notification churn if route flags change often or decisions call it again. |
| Medium | Republic recovery helper users | `common/national_focus/005_soviet_collapse_republics.txt:3654`, `:3698`; `common/national_focus/005_soviet_collapse_custom_splinters.txt:537`, `:14291`, `:14456`, `:15488`, `:17989`, `:24952`, `:25057`, `:25088`, `:25401` | `soviet_collapse_add_republic_focus_recovery_progress` at `common/scripted_effects/005_soviet_collapse_effects.txt:4670` gates one application only with a temp variable, so it does not persistently prevent repeated focus-stage applications. It also removes startup-disorder ideas once thresholds are met. |
| Medium | Starting tension cleanup helper | `common/national_focus/005_soviet_collapse_factory_successors.txt:1221` `OGB_the_council_takes_the_seal`; `common/national_focus/005_soviet_collapse_custom_splinters.txt:1363`, `:1963`, `:2391`, `:2882`, `:3438`, `:3944` | `soviet_collapse_clear_focus_starting_tension_ideas` at `common/scripted_effects/005_soviet_collapse_effects.txt:5578` removes 7 possible starting-tension ideas. It is hidden and `has_idea` guarded, but broad. |
| High | Ancient returned-name endgames | `KZR_returned_names_endgame` `:348`; `SOG_returned_names_endgame` `:737`; `KHW_returned_names_endgame` `:1130`; `ALN_returned_names_endgame` `:1517` | Each calls `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_spawn_custom_splinter_assault_columns`, `soviet_collapse_apply_custom_splinter_expansion_claims`, and `soviet_collapse_apply_high_chaos_neighbor_expansion_plan` in one reward. |
| High | Ancient route-final war focuses | `KZR_road_beyond_the_caspian` `:371`; `SOG_cities_beyond_the_desert` `:760`; `KHW_delta_without_a_center` `:1153`; `ALN_every_pass_a_border` `:1541` | Each repeats the assault-columns, expansion-claims, and neighbor-expansion helper trio after the preceding endgame can already grant similar power. |
| High | High-chaos helper chain | `common/scripted_effects/005_soviet_collapse_effects.txt:9127`, `:10392` | `soviet_collapse_apply_focus_chaos_assault_plan` grants mobile columns and, for high-chaos successors, custom assault columns, claims, neighbor expansion, and identity payload. `soviet_collapse_apply_focus_high_chaos_identity` then calls high-chaos payload logic and SOV conquer strategy. |

### Shallow Or Mechanically Disconnected Trees

| Tree group | Evidence | Audit finding |
| --- | --- | --- |
| Ancient restorations: `KZR`, `SOG`, `KHW`, `ALN` | 16 focuses each; 2 decision links each | The four trees have compact political/industry/military/expansion signals but are still too small for major event-created successor fantasies. Their expansion payoff is concentrated in 2-4 late focuses and helper bursts. |
| 18-focus high-chaos trees: `TSC`, `RMC`, `ICD` | `TSC` 1 decision link, `RMC` 1, `ICD` 1 | Strong identity names exist, but route depth remains narrow. `DSC` and `NRF` are better because they have 10 and 6 decision links respectively. |
| 47-focus custom splinters with zero decision links | `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `NLC` | These trees often have bespoke categories or generic breakaway decisions available elsewhere, but the focus trees do not stage or evolve decision play. They read like reward ladders rather than trees that unlock mechanics over time. |
| Republic generic trees | `soviet_collapse_breakaway_focus_tree`, `soviet_collapse_internal_republic_focus_tree`, `soviet_collapse_baltic_focus_tree`, `soviet_collapse_moldova_focus_tree` all have 0 focus-staged decision links | These need focus-driven decision phases. Moldova and Baltic especially have enough route concepts that their trees should unlock route-specific action sets. |
| Large republics with thin expansion | `soviet_collapse_baltic_focus_tree`: 0 expansion foci; `soviet_collapse_belarus_focus_tree`: 0; `soviet_collapse_kazakhstan_focus_tree`: 0; `soviet_collapse_moldova_focus_tree`: 0 | These are large or medium trees but do not visibly deliver map ambitions through focuses. They need claims, cores, intervention, settlement, league, or border-decision routes. |

### Chaos Fantasy Failures

The strongest chaos payloads are technically dangerous, but many chaos-country trees do not consistently meet the requested fantasy of extremely dangerous, overpowered, aggressive, identity-specific successors.

Worst gaps:
- `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `NLC`: zero focus-staged decision links despite high-chaos or militant identities.
- Most 47-focus custom splinters have only 2-3 expansion foci, usually `*_enemy_front` and `*_war_plan`.
- Many extreme-route focuses such as `FTH_extreme_gate`, `BSC_extreme_gate`, `UDC_extreme_gate`, `SDZ_extreme_gate`, `GAC_extreme_gate`, `DHC_extreme_gate`, `KHC_extreme_gate`, `FEV_extreme_gate`, `SZA_extreme_gate`, `UWD_extreme_gate`, `MRC_extreme_gate`, `IUL_extreme_gate`, `BAC_extreme_gate`, `ARD_extreme_gate`, and `NLC_extreme_path` rely on generic high-chaos helpers rather than country-specific mechanics or staged decisions.

## Focus Filter Issues

Top mismatch counts from the parser:

| Tree | Mismatch count | Representative focus ids |
| --- | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | 20 | `ukr_soviet_collapse_emergency_rada`, `ukr_soviet_collapse_seal_the_grain_ledgers`, `ukr_soviet_collapse_first_republican_line` |
| `KRS_soviet_collapse_focus_tree` | 18 | `KRS_war_plan`, `KRS_sailors_assembly_registers`, `KRS_petrograd_signal_watch` |
| `soviet_collapse_kazakhstan_focus_tree` | 17 | `kaz_soviet_collapse_karaganda_emergency_board`, `kaz_soviet_collapse_oil_field_protection_orders`, `kaz_soviet_collapse_rail_to_the_mines` |
| `NLC_soviet_collapse_focus_tree` | 16 | `NLC_diplomatic_plan`, `NLC_station_mediation`, `NLC_extreme_gate` |
| `GAC_soviet_collapse_focus_tree` | 15 | `GAC_grain_passage_papers`, `GAC_rural_congress_charter`, `GAC_forest_radio_runners` |
| `ARD_soviet_collapse_focus_tree` | 15 | `ARD_birth`, `ARD_white_sea_observer_board`, `ARD_murmansk_port_records` |
| `soviet_collapse_central_asia_focus_tree` | 15 | `central_asia_soviet_collapse_local_republic_council`, `central_asia_soviet_collapse_turkestan_city_congress`, `central_asia_soviet_collapse_southern_pass_reserve` |

Common pattern: rewards add manpower, equipment, buildings, stability, war support, or political authority variables while filters only list one adjacent category.

## Layout And Pathline Issues

No exact duplicate focus coordinates were found. Continuous focus panels appear outside the nearest node clusters. The closest panel case is `soviet_collapse_breakaway_focus_tree`, whose continuous position maps to grid `(30.0, 1.4)` and is about 4.0 grid units from `soviet_collapse_home_industry_contracts`; this is a watch item, not an immediate collision.

Worst crossed-line or tight-node examples:
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: `KZR_caspian_road_markets -> KZR_league_transit_bargain` crosses `KZR_customs_workshop_compact -> KZR_old_border_files`; similar crossing patterns repeat for `SOG`, `KHW`, and `ALN`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `PRA_omsk_station_guard -> PRA_armored_train_directorate` crosses `PRA_count_the_locomotives -> PRA_repair_crews_without_ministries`.
- `BSC`, `TNC`, `UDC`, `SDZ`, `GAC`, `DHC`, and `KHC` have multiple crossed lines between military, diplomacy, and settlement branches.
- `common/national_focus/005_soviet_collapse_republics.txt`: Baltic, Caucasus, Central Asia, Moldova, Belarus, and Kazakhstan trees all have multiple crossed prerequisite lines in dense route-fork areas.
- Many compact trees place route successors one grid apart, for example `KZR_returned_names_endgame` and `KZR_road_beyond_the_caspian`, or `FTH_first_guard` and `FTH_legitimacy`. This is readable only if the focus icons and tooltips remain short.

## Focus-To-Decision And Mechanic Disconnects

Decision-link counts by focus tree confirm the gap:
- 0 links: `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `NLC`, `soviet_collapse_breakaway_focus_tree`, `soviet_collapse_internal_republic_focus_tree`, `soviet_collapse_baltic_focus_tree`, `soviet_collapse_moldova_focus_tree`.
- Low links: `TSC` 1, `RMC` 1, `ICD` 1, `caucasus` 2, `central_asia` 3, `MFR` 3.
- Stronger examples: `PRA` 14, `DSC` 10, `UKR` 10, `CFR` 8, `NRF` 6, `OGB` 5, `KAZ` 5.

Decision categories exist for generic breakaways, regional factions, and several bespoke successors in `common/decisions/categories/005_soviet_collapse_categories.txt`, but many focus trees do not stage those surfaces. The result is that focuses often grant generic stats or helper payloads while decision play is either generic, always category-visible by country state, or not obviously evolved by focus route.

## Recommendations

### Immediate Safe Patches

- Fix `search_filters` on the highest mismatch trees first: `UKR`, `KRS`, `KAZ`, `NLC`, `GAC`, `ARD`, `central_asia`.
- Add persistent one-time guards around high-chaos helper bundles that grant custom assault columns, cores, claims, and neighbor war plans. Start with ancient endgames and any focus that combines `soviet_collapse_apply_focus_high_chaos_identity` with endgame helpers.
- Harden `soviet_collapse_update_pra_authority_idea` so it changes ideas only when the desired authority stage changes. Prefer a staged flag or current-stage variable over removing non-current ideas on every call.
- Review compact layout crossings in ancient trees and dense republic forks. These are coordinate-only patches and should not change gameplay.
- Add missing focus-stage decision tooltips or route flags where a focus already unlocks a decision through visibility but does not tell the player.

### Medium Route Rewrites

- Give each 47-focus custom splinter at least one focus-staged decision phase: early survival action, middle route action, late expansion or endgame action.
- Expand thin expansion branches beyond `enemy_front` and `war_plan`: add route-specific claims, border settlement decisions, postwar integration, cores, war goals, puppet/protectorate handling, or faction/league consequences.
- Turn high-chaos extreme routes into identity-specific mechanics instead of generic payloads. Examples: UDC command obedience, SDZ security dossiers, GAC rural defense congress, DHC/KHC host musters, NLC polar survival authority.
- Stage generic breakaway and regional decisions through focuses so decision categories evolve rather than appearing as a flat action menu.

### Broad Design Rebuilds

- Rebuild the 16-focus ancient restorations as full successor fantasies if they are meant to be major playable outcomes. Each needs political depth, restoration legitimacy, military doctrine, industry/logistics, diplomacy, expansion, and postwar settlement.
- Rework `soviet_collapse_baltic_focus_tree`, `soviet_collapse_belarus_focus_tree`, `soviet_collapse_kazakhstan_focus_tree`, and `soviet_collapse_moldova_focus_tree` expansion design. Current focus rewards do not visibly support large-tree regional ambition.
- Consolidate high-chaos reward helper layering into explicit route payload stages: first identity, first armed breakout, first regional expansion, endgame escalation. This will reduce duplicated rewards and make balance easier.
- Add route-coverage tables to the Event005 docs/specs so future audits can compare required political, industry, military, diplomacy, expansion, and special-mechanic branches against implementation.

## Validation Commands Run

- `rg --files paradox_wiki | rg 'Data structures|Triggers|Effects|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|National focus'`
- `sed -n` reads of required offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- `sed -n` reads of vanilla docs: `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- `rg -n "focus_tree =|search_filters|continuous_focus_position|mutually_exclusive|ai_will_do|completion_reward" "/home/klim/projects/Hearts of Iron IV/common/national_focus" -g "*.txt" | head -n 160`
- `sed -n '1,220p' "/home/klim/projects/Hearts of Iron IV/common/national_focus/uruguay.txt"`
- `rg --files common/national_focus | rg '^common/national_focus/005_soviet_collapse.*\\.txt$'`
- `wc -l common/national_focus/005_soviet_collapse*.txt`
- Parser pass for tree counts, focus counts, helper calls, direct idea ops, filter mismatch candidates, layout duplicates.
- Targeted `nl -ba ... | sed -n` reads of helper definitions in `common/scripted_effects/005_soviet_collapse_effects.txt`.
- `rg -n "add_ideas|add_timed_idea|swap_ideas|remove_ideas" common/national_focus/005_soviet_collapse*.txt`
- `rg -n "activate_decision|unlock_decision_category_tooltip|activate_mission|activate_targeted_decision|set_country_flag = .*unlock|unlock.*decision|decision" common/national_focus/005_soviet_collapse*.txt`
- Decision-surface check with `rg` against `common/decisions/005_soviet_collapse_decisions.txt` and `common/decisions/categories/005_soviet_collapse_categories.txt`.

## Flag Asset Statement

No files under `gfx/flags`, flag DDS/TGA assets, or flag-related image folders were opened, inspected, edited, or generated. No flag files were touched.
