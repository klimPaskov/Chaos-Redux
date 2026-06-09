# Event 005 Soviet Collapse Focus Tree Audit Handoff

Timestamp: 2026-05-30 09:07:43 UTC
Subagent scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- Directly related localisation/effects/triggers only if a tiny safe fix was needed.

Parent constraint honored: no `gfx/flags` files, flag assets, or flag references were touched.

## Summary

No gameplay files were patched in this pass. The current scoped focus files already have the direct focus-side `soviet_collapse_update_consolidated_republic_ideas = yes` calls removed, and direct focus reward idea operations are limited to hidden cleanup of starting/rivalry ideas. I did not find a small, clearly safe focus edit that would materially solve the remaining complaint without becoming a route redesign.

The remaining problem is not direct `add_ideas` spam. It is route depth and repeated helper rhythm: the three files still lean heavily on shared helper calls, especially `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_league_preparation`, `soviet_collapse_apply_focus_foreign_channel`, and `soviet_collapse_apply_focus_high_chaos_identity`. These helpers are useful, but the density makes many routes feel mechanically similar unless the parent continues converting endpoints and branch anchors into distinct decisions, claims, war goals, units, local construction, AI strategy, or country-specific mechanics.

## Files Changed

| File | Change |
| --- | --- |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_090743_event005_soviet_collapse_focus_tree_audit_handoff.md` | New audit handoff. |

Changed focus ids: none.
Localisation keys changed: none.
Icon ids changed: none.
Gameplay route behavior before/after: unchanged.

## Current Focus Counts

| File | Trees | Focuses | Notes |
| --- | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 9 | 501 | Ukraine, Belarus, Kazakhstan, regional republic/shared trees. |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | 19 full 47-focus custom splinters plus 6 compact crisis trees. |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 | CFR 47, OGB 23, MFR 58. |

## Idea Spam Audit

| Check | Result | Evidence |
| --- | --- | --- |
| Direct focus completion rewards calling `soviet_collapse_update_consolidated_republic_ideas` | 0 | `rg` over all three scoped files returned no matches. |
| Direct focus `add_ideas`, `swap_ideas`, `add_timed_idea` | 0 | No direct add/swap/timed idea rewards in scoped files. |
| Direct focus `remove_ideas` cleanup | 8 focus rewards | `PRA_the_board_overrules_ministers`, `TSC_the_committee_of_instruments`, `RMC_communes_of_witnesses`, `DSC_witness_officers`, `NRF_living_harbor_committees`, `ICD_commissars_of_last_addresses`, `mrc_protect_village_autonomy`, `OGB_the_council_takes_the_seal`. |
| Visible multi-idea grants | 0 | No focus visibly grants multiple ideas. The `remove_ideas` cases are hidden behind `hidden_effect` and usually paired with a custom tooltip. |

The MRC cleanup at `common/national_focus/005_soviet_collapse_custom_splinters.txt:20117` is a scanner false positive for visible idea cleanup: `mrc_protect_village_autonomy` uses a visible custom tooltip, while the actual `remove_ideas = mrc_pass_confederation_rivalries` sits inside `hidden_effect`.

## Helper Density

Top direct helper calls from focus rewards in the three scoped files:

| Helper | Calls | Risk |
| --- | ---: | --- |
| `soviet_collapse_apply_focus_legal_recognition` | 301 | Repeated recognition/stability rhythm across republic routes. |
| `soviet_collapse_apply_focus_depot_and_supply_control` | 258 | Repeated depot/supply identity across many branches. |
| `soviet_collapse_apply_focus_military_consolidation` | 254 | Military branches often share the same payoff language. |
| `soviet_collapse_apply_focus_league_preparation` | 220 | League branches need more country-specific decision/faction consequences. |
| `soviet_collapse_apply_focus_foreign_channel` | 176 | Foreign paths risk feeling like the same sponsor-recognition lane. |
| `soviet_collapse_apply_focus_high_chaos_identity` | 98 | High-chaos branches need more distinct country-specific consequences. |

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine emergency, politics, grain/industry, logistics, foreign, League, Black Sea, Black Banner, Bread State | `soviet_collapse_ukraine_focus_tree`; selectors include `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_protectorate_debate`; endpoint `ukr_soviet_collapse_last_harvest_plan` | Partial | Large and branched, but still helper-dense. Political routes need stronger distinct government/advisor/law/cosmetic or decision consequences. |
| Belarus rail, forest, corridor, League logistics, high-chaos | `soviet_collapse_belarus_focus_tree`; anchors include `blr_soviet_collapse_which_road_is_belarus`, `blr_soviet_collapse_seal_the_minsk_junction`, `blr_soviet_collapse_join_the_league_when_war_comes` | Partial | Identity is present, but rail/forest/corridor routes need sharper late payoffs and route-specific AI/diplomatic behavior. |
| Kazakhstan steppe, Alash/socialist/military, resources/rail, southern cascade, Central Asian League, Basmachi/high-chaos | `soviet_collapse_kazakhstan_focus_tree`; anchors include `kaz_soviet_collapse_the_congress_chooses_a_past`, `kaz_soviet_collapse_the_steppe_keeps_many_memories`, `kaz_soviet_collapse_the_southern_republics_write_together` | Partial | Largest republic tree in scope and closer to route coverage, but still needs stronger post-expansion/integration consequences. |
| Baltic legal restoration, coast/forest defense, recognition, Baltic League, anti-puppet, intervention | `soviet_collapse_baltic_focus_tree` | Partial | Compact shared tree has route families, but shared-country adaptation and intervention consequences remain limited. |
| Caucasus national council, defense, oil/infrastructure, Turkish/Iranian mediation, Caucasus League, loyalist/high-chaos pressure | `soviet_collapse_caucasus_focus_tree` | Partial | Oil and defense anchors exist; needs more distinct Georgia/Armenia/Azerbaijan adaptation and postwar settlement. |
| Central Asia local council, southern defense, Basmachi pressure, mediation, cotton/water/rail/pass/resource economy, League, ancient/high-chaos pressure | `soviet_collapse_central_asia_focus_tree` | Partial | Multiple route anchors exist, but several are OR convergence nodes with broad helper rewards rather than fully separate playable loops. |
| Moldova Chisinau, Dniester, Romanian diplomacy, Ukraine settlement, agrarian/river economy, League, high-chaos | `soviet_collapse_moldova_focus_tree` | Partial | Route map exists; needs clearer route locks and stronger postwar/settlement handling. |
| Internal republic compact meaningful trees | `soviet_collapse_internal_republic_focus_tree`, `soviet_collapse_breakaway_focus_tree` | Partial/weak | Internal republic tree is meaningful but shared. Breakaway tree is only 4 focuses and should be explicitly treated as a minimal fallback or replaced. |
| Full custom splinter high-chaos successors | Full 47-focus trees: `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` | Partial | Most have branches, endpoints, and some aggression hooks. Many still share the same generic helper spine and need distinct OP identity payoffs. |
| Compact crisis splinters | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` | Partial/weak | 18-22 focus trees. Recent patches added decisions/aggression to some, but they remain shallower than full successors. |
| Factory successors | `CFR_soviet_collapse_focus_tree`, `MFR_soviet_collapse_focus_tree`, `OGB_soviet_collapse_focus_tree` | Mixed | CFR and MFR have real forks and SOV war goals. OGB has claims/wargoals and a Volga route, but only 23 focuses and needs more depth. |

## Missing or Simplified Content

High priority:
1. `common/national_focus/005_soviet_collapse_factory_successors.txt`: `OGB_soviet_collapse_focus_tree` is still the clearest shallow tree in the scoped set. It has political, industry/river, military, and expansion hooks, but only 23 focuses and no full second-stage restoration, internal crisis, postwar integration, or deep Volga/Idel-Ural settlement loop.
2. `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` are compact crisis trees. They have some bespoke decisions and aggression hooks, but remain less developed than the 47-focus successors.
3. `common/national_focus/005_soviet_collapse_republics.txt`: `soviet_collapse_breakaway_focus_tree` has only 4 focuses. It should be documented as a minimal fallback tree or expanded by the parent.
4. `common/national_focus/005_soviet_collapse_republics.txt`: Ukraine, Belarus, Kazakhstan, and shared regional trees have many route anchors, but political and expansion payoffs still depend heavily on repeated helpers instead of visible country-identity changes, route-specific decisions, or postwar settlement.
5. `common/national_focus/005_soviet_collapse_custom_splinters.txt`: many full custom splinter trees use the same generic 47-focus architecture. They need more distinct endgame aggression and special mechanics to feel OP rather than template-complete.

## Icon Coverage Table

| Check | Result | Notes |
| --- | --- | --- |
| Focuses with icon assignment | 1634/1634 | Every parsed focus has `icon =`. |
| Unique icon ids used | 1456 | Several repeated icons remain. |
| Missing icon definitions | 0 | Repo and vanilla `interface/*.gfx` scan found definitions for all used focus icons. |
| Repeated icon risk | Present | Highest repeats include `GFX_focus_soviet_collapse_guard_the_radio_stations` (4), `GFX_ukr_soviet_collapse_democratic` (4), `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow` (4), `GFX_focus_soviet_collapse_steppe_supply_congress` (4), `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards` (4), `GFX_central_asia_soviet_collapse_steppe_federation` (4), `GFX_moldova_soviet_collapse_ukrainian_corridor` (4), and several custom splinter diplomatic/supply icons at 3-4 uses. |

No icon patch was made because repeated icons are not missing references, and replacing them would require new asset requests or broader art direction. I did not touch flags.

## Localisation and Reward Mismatch List

| Check | Result | Notes |
| --- | --- | --- |
| Missing focus title localisation | 0 | All 1634 focus ids have title keys. |
| Missing focus description localisation | 0 | All 1634 focus ids have `_desc` keys. |
| Unsupported `<=`/`>=` in scoped focus files | 0 | No matches. |
| Reward/name mismatch risk | Present | The largest mismatch risk is conceptual rather than missing loc: route names often promise government, expansion, or country identity changes while rewards still use shared helper stacks and variables. |

Specific mismatch risks for parent review:
- `OGB_the_old_name_survives_modern_war`: has SOV wargoal and custom splinter expansion claims, but the broader OGB tree lacks a full postwar/integration route to support the title's ambition.
- `soviet_collapse_breakaway_focus_tree`: four-focus fallback does not meet the spec's "compact but meaningful" standard for long-lived countries.
- Full custom splinter `*_endgame` focuses: many are more aggressive than before, but route-specific OP payoffs are inconsistent across the family.

## AI Behavior Gaps

All focuses in the three scoped files have `ai_will_do`, but many route choices remain shallow:
- Several route selectors use flat bases plus simple war/stability/SOV-variable modifiers. Parent should add route-aware AI strategy or stronger weighting for ideology, chaos tier, nearby enemies, available targets, faction status, and route flags.
- Custom splinter AI often follows the same architecture across many tags. This makes high-chaos countries functional but not as distinctive or aggressive as the complaint requests.
- OGB has useful rivalry AI against IUL and SOV, but its route is too short to create a sustained aggressive AI plan.
- Shared republic trees need country/tag adaptation so Baltic, Caucasus, Central Asian, internal republic, Moldova, and breakaway variants do not pick mechanically identical solutions.

## Layout and Pathline Audit

| Check | Result | Notes |
| --- | --- | --- |
| Duplicate coordinates in same tree | 0 | Parser found no same-tree duplicate focus coordinates. |
| Adjacent same-row focuses at distance 0 or 1 | 0 | No immediate same-row focus crowding found in parsed coordinates. |
| Continuous panel clearance | Mostly acceptable | Estimated clearance from max focus x to continuous panel grid position is usually 4+ columns. |
| Risky OR prerequisites | Present | Many convergence focuses use `prerequisite = { focus = a focus = b }`, which is OR. Some are likely intended convergence, but several broad endpoint ORs should be manually reviewed against route design. |

Pathline/layout risks for parent:
- `common/national_focus/005_soviet_collapse_republics.txt`: wide OR endpoint prerequisites such as `soviet_collapse_armed_neutrality`, `baltic_soviet_collapse_the_baltic_question_resolved`, `moldova_soviet_collapse_republic_of_crossings`, and `moldova_soviet_collapse_the_river_state` need semantic review so OR convergence is intentional and visible.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: repeated OR merges such as `*_industry_plan`, `*_enemy_front`, `*_endgame`, and regional compact endpoints create many crossing-line risks if the parent moves branches later.
- `common/national_focus/005_soviet_collapse_factory_successors.txt`: OGB has several OR convergence endpoints (`OGB_claim_the_old_trade_cities`, `OGB_future_bulgaria_file`, `OGB_volga_restoration_state`, `OGB_the_old_name_survives_modern_war`) that are probably intentional but should be checked visually after any OGB expansion.

## High-Priority Parent Implementation List

1. Deepen OGB first.
   - File: `common/national_focus/005_soviet_collapse_factory_successors.txt`.
   - Focus anchors: `OGB_scholars_guard_the_charter`, `OGB_clerics_guard_the_charter`, `OGB_treat_with_idel_ural`, `OGB_the_volga_cannot_have_two_seals`, `OGB_claim_the_old_trade_cities`, `OGB_volga_restoration_state`, `OGB_the_old_name_survives_modern_war`.
   - Add: postwar Volga/Idel-Ural settlement, restored trade-city integration, scholar/cleric branch consequences, more aggressive late route behavior, and OP but bounded endgame payoffs.

2. Convert compact crisis splinters from "short crisis trees" into distinct dangerous actors or document them as intentionally short.
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`.
   - Trees: `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`.
   - Add: one unique mechanic or recurring decision family per tree, plus stronger AI aggression for SOV/local rivals.

3. Replace helper-dense endpoint rewards with visible mechanics.
   - Files: all three scoped files.
   - Start with endpoint and branch selector focuses that only combine route flags, variables, and common helpers.
   - Prefer: decision unlocks, targeted war/claim/core hooks, unit/template unlocks, local state construction, route AI strategies, faction rules, postwar settlement missions.

4. Make high-chaos full custom splinters more OP and less template-identical.
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`.
   - Focus on `*_endgame`, `*_extreme_path`, `*_war_plan`, `*_enemy_front`, `*_industry_plan`, and route-specific regional compact endpoints.
   - Keep direct idea spam at zero; use claims, assault columns, war goals, decisions, production lines, and AI strategies instead.

5. Review OR prerequisites before moving layout.
   - The current coordinate scan is clean, but route semantics may still be wrong where a focus should require both parents. Check every broad OR endpoint before adding or moving branches.

## Validation Run

Commands and results:
- `rg -n "soviet_collapse_update_consolidated_republic_ideas" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt`
  - Result: no matches.
- `rg -n "\\b(add_ideas|remove_ideas|swap_ideas|add_timed_idea)\\b" ...`
  - Result: 8 `remove_ideas` cleanup references, no direct `add_ideas`, `swap_ideas`, or `add_timed_idea`.
- Parsed focus counts, AI blocks, search filters, direct updater calls, idea ops, helper calls, duplicate coordinates, close same-row coordinates, and repeated icons with a read-only parser.
  - Result: 1634 focuses; 0 missing `ai_will_do`; 0 missing `search_filters`; 0 duplicate same-tree coordinates; 0 close same-row coordinate pairs.
- Localisation scan across `localisation/english/*.yml`.
  - Result: 0 missing focus title keys, 0 missing `_desc` keys.
- Icon definition scan across repo and vanilla `interface/*.gfx`.
  - Result: 1456 unique icon ids, 0 missing definitions.
- `rg -n "<=|>="` over scoped focus files.
  - Result: no unsupported operators found.
- Brace balance over the three scoped focus files and this handoff.
  - Result: final brace depth 0 and minimum brace depth 0 for all checked files.
- Duplicate focus id scan over the three scoped focus files.
  - Result: 1634 focus ids, 0 duplicate focus ids.
- `git diff --check --` over the three scoped focus files and `git diff --no-index --check /dev/null` over this handoff.
  - Result: no whitespace errors reported.

Skipped validation:
- In-game visual pathline screenshots were not run in this subagent pass.
- Full scripted-effect transitive idea lifecycle rewrite was not attempted; it is broader than a safe focus-tree subagent patch.
- No asset validation beyond `.gfx` icon definition presence; flags were explicitly out of scope.

## Remaining Route Risks

- Current files were already dirty before this audit, including the three scoped focus files. I audited the current workspace state and did not revert or overwrite existing changes.
- The complaint about idea spam is largely resolved on the direct focus surface, but helper-side staged idea churn may still be felt indirectly through repeated shared helper rewards.
- Route-depth completion is not achieved. The parent still needs a focused route redesign pass, especially OGB, compact crisis splinters, breakaway fallback, and full custom splinter OP differentiation.
- Layout is mechanically cleaner than prior reports, but OR prerequisite semantics and in-game pathline screenshots remain necessary after any parent redesign.

No separate improvement plan was written; this handoff is the actionable audit for the parent.
