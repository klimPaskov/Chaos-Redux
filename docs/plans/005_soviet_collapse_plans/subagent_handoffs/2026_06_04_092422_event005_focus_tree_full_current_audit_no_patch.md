# Event005 Soviet Collapse Focus Tree Full Current Audit

Timestamp: 2026-06-04 09:24:22 UTC

Subagent role: `chaosx_focus_tree_auditor`

Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Directly related decision/scripted-effect/localisation checks only where needed for focus-tree audit evidence.

Parent constraints honored:
- No `gfx/flags`, `.tga`, flag sprite, or flag orientation files were touched.
- No gameplay focus file was patched in this pass.
- No commit was made.

Skills and references used:
- Read `AGENTS.md`.
- Used `hoi4-focus-trees`, `chaos-redux-events`, and `chaos-redux-subagents`.
- Consulted the offline Paradox wiki snapshot for national focus, decision, localisation, data structures, triggers, modifiers, scopes, on actions, event modding, idea modding, and AI modding. The offline snapshot does not contain a standalone `Effects - Hearts of Iron 4 Wiki.md` file, so vanilla `effects_documentation.md` was used for effect syntax.
- Consulted vanilla docs in `~/projects/Hearts of Iron IV/documentation/` and inspected vanilla `common/national_focus/soviet.txt` for focus structure precedent.

## Files Changed

| File | Change |
| --- | --- |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_092422_event005_focus_tree_full_current_audit_no_patch.md` | New audit handoff only. |

Changed focus ids: none.

Localisation keys changed: none.

Decision ids changed: none.

Gameplay behavior before/after: unchanged.

## No Patch Rationale

I did not find a small, safe focus patch that matched the allowed patch categories and materially improved the current complaint.

Concrete checks:
- Duplicate repeated direct reward calls inside a single focus: no real duplicated helper/equipment/variable reward call was found. Parser noise from repeated braces and repeated generic block openers was ignored.
- Bad or missing focus filters: every parsed focus has `search_filters`.
- Missing focus basics: every parsed focus has `icon`, `completion_reward`, `ai_will_do`, and coordinates.
- Missing decision unlock tooltips for existing decisions: all 113 `unlock_decision_tooltip` references resolve to existing decision/category ids.
- Duplicate focus ids: none.
- Duplicate coordinates within the same tree: none.

The remaining issues are broad route depth, reward rhythm, and layout/pathline design. Fixing them would require moving or redesigning many focuses and is outside a bounded safe subagent patch.

## Current Focus Counts

| File | Trees | Focuses | Notes |
| --- | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 9 | 501 | Ukraine, generic breakaway, internal republic, Baltic, Caucasus, Central Asia, Moldova, Belarus, Kazakhstan. |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | 19 full 47-focus custom splinters, 1 22-focus PRA compact tree, 5 18-focus compact crisis trees. |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 | CFR 47, OGB 23, MFR 58. |
| `005_soviet_collapse_ancient_restorations.txt` | 4 | 64 | KZR, SOG, KHW, ALN at 16 focuses each. |
| Total | 41 | 1698 | Current workspace state. |

Smallest current trees:
- `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, `ALN_soviet_collapse_ancient_focus_tree`: 16 focuses each.
- `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree`: 18 focuses each.
- `PRA_soviet_collapse_focus_tree`: 22 focuses.
- `OGB_soviet_collapse_focus_tree`: 23 focuses.
- `soviet_collapse_breakaway_focus_tree`: 36 focuses.

## Reward and Mechanic Surface

Direct idea spam is not present on the focus surface:
- `add_ideas`: 0
- `swap_ideas`: 0
- `add_timed_idea`: 0
- `remove_ideas`: 0
- `soviet_collapse_update_consolidated_republic_ideas`: 0

Mechanic hooks by focus file:

| File | Decision tooltips | Wargoals | AI strategies | Direct claims | Assault columns | High-chaos neighbor plan |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 35 | 0 | 0 | 7 | 0 | 1 |
| `005_soviet_collapse_custom_splinters.txt` | 43 | 6 | 22 | 0 | 9 | 0 |
| `005_soviet_collapse_factory_successors.txt` | 19 | 5 | 23 | 3 | 0 | 0 |
| `005_soviet_collapse_ancient_restorations.txt` | 16 | 4 | 8 | 35 | 12 | 12 |

Top repeated direct focus helper calls:

| Helper | Calls | Risk |
| --- | ---: | --- |
| `soviet_collapse_apply_focus_depot_and_supply_control` | 141 | Depot/supply payoff rhythm is still heavily repeated. |
| `soviet_collapse_apply_focus_military_consolidation` | 132 | Military branches often converge into the same reward feel. |
| `soviet_collapse_apply_focus_legal_recognition` | 108 | Political/governance branches often resolve through the same recognition package. |
| `soviet_collapse_apply_focus_republican_compact_plan` | 80 | Compact branches feel generic unless paired with country-specific mechanics. |
| `soviet_collapse_apply_focus_foreign_channel` | 65 | Foreign routes risk becoming one sponsor-recognition lane. |
| `soviet_collapse_apply_focus_high_chaos_identity` | 60 | High-chaos identity is still shared heavily across unrelated actors. |
| `soviet_collapse_apply_focus_security_supply_plan` | 58 | Security/supply rewards repeat across survival branches. |
| `soviet_collapse_apply_focus_league_preparation` | 52 | League branches need more distinct faction/decision consequences. |

The parent tranches have improved aggression: ancient restoration focuses now use claims, SOV wargoals, assault columns, and `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`. The full current complaint is still not solved because many branches still use the same helper spine.

## Branch Depth Audit

Republic file:
- Ukraine is the most developed republic tree at 83 focuses. It has political, industry, foreign, military, League, Black Sea, high-chaos, and late-game families. Remaining risk is layout density and helper-heavy politics around `ukr_soviet_collapse_question_of_statehood`, `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_black_banner_compact`, and `ukr_soviet_collapse_protectorate_debate`.
- Kazakhstan is large at 92 focuses and has the best route coverage among shared republics, but post-expansion/integration consequences are still thinner than the branch names imply. Watch `kaz_soviet_collapse_steppe_federation_charter`, `kaz_soviet_collapse_lone_steppe_state`, `kaz_soviet_collapse_resource_sovereignty`, and `kaz_soviet_collapse_caspian_security_detachments`.
- Belarus at 53 focuses has rail/forest/corridor/League paths, but payoff is still route-helper heavy around `blr_soviet_collapse_prepare_league_freight_tables`, `blr_soviet_collapse_every_track_through_minsk`, and `blr_soviet_collapse_the_league_depot_at_minsk`.
- Moldova at 48, Central Asia at 45, Baltic at 42, and Caucasus at 40 are meaningful but still compact shared trees. They need stronger tag-specific adaptations and postwar settlement logic.
- `soviet_collapse_breakaway_focus_tree` is no longer a 4-focus fallback; it has 36 focuses. It remains generic relative to major released actors. Worst generic anchors: `soviet_collapse_the_republic_defines_itself`, `soviet_collapse_route_consolidation_congress`, `soviet_collapse_rail_hub_or_mountain_pass`, `soviet_collapse_armed_neutrality`, `soviet_collapse_the_republic_endures`, `soviet_collapse_a_republic_worth_naming`.

Factory successors:
- `CFR_soviet_collapse_focus_tree` has a real industrial mandate tree and stronger late mechanics through `CFR_the_builder_state_marches_east`, `CFR_build_the_border_bend_the_border`, `CFR_rebuild_russia_without_moscow`, and reconstruction decisions. Its mutex and pathline geometry remains crowded.
- `MFR_soviet_collapse_focus_tree` is the deepest factory tree at 58 focuses, with arms-production branches, war-market/arsenal routes, and late SOV aggression.
- `OGB_soviet_collapse_focus_tree` is still the weakest factory successor at 23 focuses. Worst concrete anchors: `OGB_scholars_guard_the_charter`, `OGB_clerics_guard_the_charter`, `OGB_treat_with_idel_ural`, `OGB_the_volga_cannot_have_two_seals`, `OGB_claim_the_old_trade_cities`, `OGB_future_bulgaria_file`, `OGB_volga_restoration_state`, `OGB_the_old_name_survives_modern_war`. It has IUL/SOV aggression and decision unlocks, but not enough second-stage Volga/Idel-Ural settlement, scholar-vs-cleric consequences, or postwar integration.

Custom splinters:
- Full 47-focus trees exist for `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`.
- The 47-focus architecture provides political/industry/war/diplomatic/high-chaos lanes, but many IDs still prove a template spine: `*_industry_plan`, `*_hidden_doctrine`, `*_extreme_gate`, `*_extreme_path`, `*_war_plan`, `*_enemy_front`, `*_diplomatic_plan`, and `*_endgame`.
- Weakest compact crisis trees: `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree` at 18 focuses, plus `PRA_soviet_collapse_focus_tree` at 22.
- Worst compact anchors needing deeper mechanics: `TSC_starfall_mandate`, `RMC_resurrection_without_state`, `DSC_grave_ordnance_claims`, `NRF_northern_revenant_fleet`, `ICD_commissariat_without_end`, `PRA_rails_over_capitals`, `PRA_the_pale_line_endures`.

Ancient restorations:
- `KZR`, `SOG`, `KHW`, and `ALN` each have a clean 16-focus compact tree and now have aggressive endgame hooks. They remain too short for long-lived playable countries unless intentionally treated as compact high-chaos actors.
- Worst shallow payoff IDs: `KZR_restoration_survives_modern_war`, `SOG_restoration_survives_modern_war`, `KHW_restoration_survives_modern_war`, `ALN_restoration_survives_modern_war`.
- Stronger but still compact aggressive IDs: `KZR_returned_names_endgame`, `KZR_road_beyond_the_caspian`, `SOG_returned_names_endgame`, `SOG_cities_beyond_the_desert`, `KHW_returned_names_endgame`, `KHW_delta_without_a_center`, `ALN_returned_names_endgame`, `ALN_every_pass_a_border`.

## Layout and Pathline Risks

Mechanical layout checks:
- Duplicate focus ids: 0.
- Duplicate same-tree coordinates: 0.
- Missing coordinates: 0.
- Same-row crowding from duplicate coordinates: none.

Mutual-exclusion geometry risks:
- `soviet_collapse_breakaway_focus_tree`: `soviet_collapse_socialist_sovereignty_committee`, `soviet_collapse_military_defense_council`, and `soviet_collapse_foreign_liaison_government` are wide same-row route selectors with many focuses between or near the line.
- `soviet_collapse_baltic_focus_tree`: `baltic_soviet_collapse_legal_continuity_government`, `baltic_soviet_collapse_foreign_protection_council`, `baltic_soviet_collapse_military_border_government`, and `baltic_soviet_collapse_baltic_league_first` create diagonal mutual-exclusion geometry.
- `soviet_collapse_central_asia_focus_tree`: `central_asia_soviet_collapse_local_republic_council`, `central_asia_soviet_collapse_military_border_authority`, and `central_asia_soviet_collapse_foreign_border_patronage` are wide/diagonal selectors.
- `soviet_collapse_moldova_focus_tree`: `moldova_soviet_collapse_alliance_not_union`, `moldova_soviet_collapse_conditional_union`, and `moldova_soviet_collapse_reject_the_union_question` still need visual review.
- `CFR_soviet_collapse_focus_tree`: political/economic selectors including `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_invite_the_foreign_contract_board`, `CFR_the_concrete_committee`, `CFR_rails_first`, `CFR_factories_first`, and `CFR_contracts_first` have the worst same-row mutual-exclusion line risks.
- Ancient restorations: symbolic-vs-expansion forks (`KZR_symbolic_crossing_state` vs `KZR_expansionist_steppe_levy`, equivalent SOG/KHW/ALN pairs) are horizontally separated but clean enough to keep unless the parent expands the trees.

Pathline crossing examples found by coordinate scan:
- Ukraine has dense crossing lines around early statehood and political/military route geometry, including `ukr_soviet_collapse_guard_the_telegraph_house -> ukr_soviet_collapse_question_of_statehood` crossing grain/industry lines, and multiple crossings around `ukr_soviet_collapse_foreign_courts_notice_kyiv -> ukr_soviet_collapse_army_supremacy`.
- `UDC_soviet_collapse_focus_tree` and `SDZ_soviet_collapse_focus_tree` show repeated crossing patterns around `*_supply`, `*_civil_rule`, `*_proaganda`, `*_radical_turn`, `*_war_plan`, and `*_industry_plan`.
- `DHC_soviet_collapse_focus_tree` and `KHC_soviet_collapse_focus_tree` show crossing clusters around `*_enemy_front`, `*_river_customs`, `*_league_passage/corridor_bargain`, and winter road/settlement branches.
- `FEV`, `SZA`, `UWD`, `BAC`, `ARD`, and `NLC` have late-tree crossing clusters, especially where settlement/diplomacy/industry/war lanes converge into `*_endgame`.
- Factory successor examples: `CFR_the_board_becomes_the_cabinet -> CFR_cities_first` crosses the `CFR_rails_first -> CFR_apartment_blocks_for_loyalty` line; `MFR_factory_war_cabinet -> MFR_artillery_from_broken_foundries` crosses `MFR_rifles_before_speeches -> MFR_standardize_the_rifle_line`.
- Ancient examples: `KZR_caspian_road_markets -> KZR_league_transit_bargain` crosses `KZR_customs_workshop_compact -> KZR_old_border_files`; equivalent compact diamond crossings exist in SOG/KHW/ALN.

These are not single-line safe fixes because moving any one focus would disturb branch spacing and often requires route layout redesign.

## Decision Unlock Audit

All current `unlock_decision_tooltip` focus references resolve to existing decision ids.

Counts:
- 113 total tooltip references.
- 62 unique decision ids.
- 0 missing decision ids.

Most repeated decision tooltips:
- `cfr_issue_reconstruction_contracts`: 5
- `soviet_collapse_set_regional_defense_goal`: 4
- `soviet_collapse_found_steppe_federation`: 4
- `soviet_collapse_open_museum_cabinets`: 4
- `soviet_collapse_recruit_archivists`: 4
- `soviet_collapse_commission_old_banner`: 4
- `pra_repair_the_branch_lines`: 3
- `pra_raise_mobile_supply_yards`: 3
- `pra_drive_the_junction_columns`: 3
- `dsc_verify_the_roll_call`: 3
- `dsc_mark_the_unfinished_front_roads`: 3
- `mfr_convert_depots_to_arms_lines`: 3

## High-Priority Redesign Plan

1. Deepen OGB before adding more factory-successor polish.
   - Add a second-stage Volga/Idel-Ural settlement branch after `OGB_treat_with_idel_ural` and `OGB_the_volga_cannot_have_two_seals`.
   - Give `OGB_scholars_guard_the_charter` and `OGB_clerics_guard_the_charter` visible route consequences beyond early authority.
   - Convert `OGB_volga_restoration_state` and `OGB_the_old_name_survives_modern_war` into real postwar/integration endpoints.

2. Decide whether the compact crisis trees are intentionally compact.
   - If yes, document them as short crisis actors.
   - If no, expand `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, and `PRA` with one unique decision loop or recurring mechanic each.

3. Reduce helper-spine sameness in full custom splinters.
   - Start with `*_war_plan`, `*_industry_plan`, `*_enemy_front`, `*_extreme_path`, and `*_endgame`.
   - Prefer concrete payloads: target decisions, route-specific AI strategies, wargoals, assault columns, production lines, state construction, postwar integration, and special units.

4. Give shared republic trees tag-aware follow-through.
   - Baltic, Caucasus, Central Asia, Moldova, and internal breakaway trees need country/tag adaptations so shared trees do not play identically.
   - Add postwar settlement decisions or route-specific regional pact outcomes after major expansion or league focuses.

5. Treat pathline cleanup as a deliberate layout pass.
   - Do not patch one coordinate at a time.
   - Group by tree family: Ukraine first, then CFR/MFR, then compact custom splinters with dense late-tree crossings, then ancient compact diamonds if those trees are expanded.

## Validation Run

Commands run:
- `sed -n` on `AGENTS.md`, `hoi4-focus-trees`, `chaos-redux-events`, and `chaos-redux-subagents`.
- `sed -n` on offline wiki pages for national focus, decision, localisation, data structures, triggers, modifiers, scopes, on actions, event modding, idea modding, and AI modding.
- `sed -n` on vanilla `effects_documentation.md`, `triggers_documentation.md`, and `common/national_focus/soviet.txt`.
- Parsed the four scoped focus files for tree/focus counts, ids, coordinates, icons, rewards, AI blocks, search filters, prerequisites, mutual exclusions, helper calls, direct idea operations, duplicate coordinates, OR prerequisites, and approximate pathline intersections.
- Parsed `common/decisions/*.txt` and `common/decisions/categories/*.txt` to verify focus `unlock_decision_tooltip` targets.
- `git status --short` to confirm the worktree was already dirty and to avoid reverting unrelated changes.

Results:
- 41 focus trees and 1698 focuses parsed.
- 0 missing icons.
- 0 missing `completion_reward`.
- 0 missing `ai_will_do`.
- 0 missing `search_filters`.
- 0 missing coordinates.
- 0 duplicate focus ids.
- 0 duplicate same-tree coordinates.
- 0 missing decision ids for `unlock_decision_tooltip`.
- 0 direct focus-side `add_ideas`, `swap_ideas`, `add_timed_idea`, `remove_ideas`, or `soviet_collapse_update_consolidated_republic_ideas`.

Skipped validation:
- No in-game screenshot/pathline validation was run.
- No gameplay file diff validation was needed because no gameplay file was patched.
- No localisation encoding changes were made.

## Remaining Issues

- Event005 focus-tree route depth is not complete.
- Reward spam is no longer direct idea spam, but repeated helper rhythm remains visible.
- High-chaos trees are stronger than earlier reports, especially ancient and some special successors, but many still feel template-derived rather than uniquely overpowered.
- Layout/pathline risks are real and broad; they need a planned layout pass, not a one-focus patch.
- The worktree was dirty before this subagent pass; this handoff does not revert or overwrite unrelated parent/user changes.
