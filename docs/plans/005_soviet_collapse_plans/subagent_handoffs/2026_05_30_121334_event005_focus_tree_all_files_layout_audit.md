# Event 005 Soviet Collapse Focus Tree All-Files Layout Audit

Timestamp: 2026-05-30 12:13:34 UTC

Role: Chaos Redux focus-tree audit subagent.

User scope: audit all Event 005 focus files, apply only small safe focus reward or pathline/layout patches, do not touch `gfx/flags`, flag sprites, image files, or visual asset files.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`
- Vanilla precedent: `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`
- Event 005 source spec: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`
- Current broad follow-up plan: `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`
- Recent handoff context: `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_120242_event005_focus_tree_idea_layout_audit_mfr_patch.md`

## Files Inspected

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/*005_soviet_collapse*_l_english.yml`
- `interface/*.gfx`
- Vanilla `interface/*.gfx` for focus icon sprite lookup

No `gfx/flags`, flag sprite, image, `gfx/`, or visual asset file was edited.

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_121334_event005_focus_tree_all_files_layout_audit.md`

Changed focus id:

- `moldova_soviet_collapse_ukrainian_border_compact`

No localisation keys changed.

No icon ids changed.

No reward, prerequisite, mutual exclusion, AI, availability, bypass, decision, idea, leader, flag, claim, core, war goal, or formable logic changed.

## Patch Behavior

Before:

- `moldova_soviet_collapse_ukrainian_border_compact` was at `(11, 3)`.
- `moldova_soviet_collapse_independent_republic_council` was at `(11, 4)`.
- These mutually exclusive route choices were stacked in one column, making the visible mutual-exclusion geometry cramped and easy to read as a vertical pathline through the route choices.

After:

- `moldova_soviet_collapse_ukrainian_border_compact` is at `(13, 3)`.
- `moldova_soviet_collapse_independent_republic_council` remains at `(11, 4)`.
- The two route choices are no longer adjacent by the static layout scan.

Safety:

- The patch changes only one `x =` coordinate in one focus block.
- It does not affect route eligibility, rewards, icons, localisation, focus timing, or AI weights.
- Post-patch static pathline scan reports `PATHLINE_HITS 0`.

## Route Coverage Table

Static columns:

- `Focuses`: parsed `focus = { ... }` count.
- `Direct hooks`: direct focus-reward occurrences of decision, war goal, claim/core, unit, faction, cosmetic, AI-strategy, or explicit Soviet Collapse unlock helpers. Shared helper effects are not counted here.
- `Small reward focuses`: focuses with direct small stat/equipment/XP/manpower/fuel/PP style rewards.
- `Helper focuses`: focuses that call one or more broad `soviet_collapse_apply_focus_*` helpers.
- `Multi-helper`: focuses that call more than one broad helper and are likely route-depth substitutes.

| Focus tree | Focuses | Direct hooks | Small reward focuses | Helper focuses | Multi-helper | Coverage status |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | 83 | 22 | 51 | 72 | 29 | Broad but still helper-heavy; political, Black Sea, grain, and League routes need clearer direct mechanics. |
| `soviet_collapse_breakaway_focus_tree` | 36 | 0 | 18 | 32 | 13 | Shallow survival baseline; lacks direct decision, expansion, and postwar hooks. |
| `soviet_collapse_internal_republic_focus_tree` | 62 | 0 | 19 | 60 | 40 | Large enough, but very helper-dependent and route-disconnected. |
| `soviet_collapse_baltic_focus_tree` | 42 | 0 | 12 | 36 | 18 | Restoration identity exists, but direct legal, port, defense, and League gameplay is thin. |
| `soviet_collapse_caucasus_focus_tree` | 40 | 5 | 18 | 39 | 21 | Some hooks exist; mountain, oil, border, and compact routes still need stronger direct surfaces. |
| `soviet_collapse_central_asia_focus_tree` | 45 | 14 | 16 | 43 | 24 | Better hooks than most republic trees, but still helper-heavy and needs route-specific missions. |
| `soviet_collapse_moldova_focus_tree` | 48 | 0 | 23 | 47 | 17 | Layout patched locally; still lacks direct river, Dniester, Romanian, and Ukrainian corridor mechanics. |
| `soviet_collapse_belarus_focus_tree` | 53 | 9 | 31 | 48 | 16 | Rail and corridor identity exists; needs more direct rail authority, forest defense, and League freight mechanics. |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | 7 | 47 | 85 | 31 | Largest tree, but resource, Alash, socialist, federation, and patron routes are too helper-dependent. |
| `FTH_soviet_collapse_focus_tree` | 47 | 0 | 21 | 26 | 10 | Full-size but lacks direct aggressive route mechanics. |
| `PRA_soviet_collapse_focus_tree` | 22 | 15 | 16 | 20 | 7 | Compact rail actor with hooks; still short for an overpowered rail authority. |
| `TSC_soviet_collapse_focus_tree` | 18 | 3 | 10 | 12 | 4 | Shallow crisis tree. |
| `RMC_soviet_collapse_focus_tree` | 18 | 3 | 12 | 11 | 5 | Shallow crisis tree. |
| `DSC_soviet_collapse_focus_tree` | 18 | 17 | 14 | 15 | 6 | Direct aggression exists; too short for full Dead Soldiers' Congress ambitions. |
| `NRF_soviet_collapse_focus_tree` | 18 | 12 | 14 | 12 | 4 | Naval identity exists, but needs more naval missions, ports, ships, and convoy warfare. |
| `ICD_soviet_collapse_focus_tree` | 18 | 3 | 13 | 12 | 4 | Shallow crisis tree. |
| `BSC_soviet_collapse_focus_tree` | 47 | 0 | 24 | 14 | 4 | Full-size but lacks direct mechanics. |
| `TNC_soviet_collapse_focus_tree` | 47 | 0 | 22 | 14 | 4 | Full-size but lacks direct mechanics. |
| `ALA_soviet_collapse_focus_tree` | 47 | 0 | 21 | 17 | 4 | Full-size but lacks direct mechanics. |
| `BBH_soviet_collapse_focus_tree` | 47 | 0 | 21 | 22 | 7 | Full-size but lacks direct mechanics. |
| `KRS_soviet_collapse_focus_tree` | 47 | 0 | 24 | 28 | 10 | Full-size, high helper load, no direct hooks by scan. |
| `UDC_soviet_collapse_focus_tree` | 47 | 0 | 23 | 20 | 8 | Full-size, but route mechanics are mostly helper calls. |
| `SDZ_soviet_collapse_focus_tree` | 47 | 0 | 22 | 20 | 8 | Full-size, but route mechanics are mostly helper calls. |
| `GAC_soviet_collapse_focus_tree` | 47 | 0 | 25 | 18 | 10 | Full-size, but route mechanics are mostly helper calls. |
| `DHC_soviet_collapse_focus_tree` | 47 | 0 | 22 | 11 | 6 | Full-size, but route mechanics are mostly helper calls. |
| `KHC_soviet_collapse_focus_tree` | 47 | 0 | 24 | 12 | 6 | Full-size, but route mechanics are mostly helper calls. |
| `FEV_soviet_collapse_focus_tree` | 47 | 0 | 20 | 21 | 12 | Full-size, but direct Far Eastern port/foreign/rail mechanics are absent by scan. |
| `SZA_soviet_collapse_focus_tree` | 47 | 0 | 19 | 20 | 11 | Full-size, but direct railhead and foreign-route mechanics are absent by scan. |
| `UWD_soviet_collapse_focus_tree` | 47 | 0 | 20 | 21 | 6 | Full-size, but direct route mechanics are absent by scan. |
| `MRC_soviet_collapse_focus_tree` | 47 | 0 | 20 | 22 | 4 | Full-size, but direct route mechanics are absent by scan. |
| `IUL_soviet_collapse_focus_tree` | 47 | 0 | 19 | 22 | 10 | Full-size, but Volga/Ural mechanics remain mostly helper-based. |
| `BAC_soviet_collapse_focus_tree` | 47 | 0 | 18 | 22 | 7 | Full-size, but Amur/commune route mechanics remain mostly helper-based. |
| `ARD_soviet_collapse_focus_tree` | 47 | 3 | 24 | 24 | 8 | Arctic naval hooks exist but are not enough for an OP naval successor. |
| `NLC_soviet_collapse_focus_tree` | 47 | 0 | 26 | 19 | 7 | Full-size, but lacks direct polar state mechanics. |
| `CFR_soviet_collapse_focus_tree` | 47 | 13 | 13 | 1 | 0 | Stronger than most; still needs construction contract missions and state-targeted build mandates. |
| `OGB_soviet_collapse_focus_tree` | 23 | 14 | 15 | 3 | 0 | Improved hooks, still shallow for a high-impact successor. |
| `MFR_soviet_collapse_focus_tree` | 58 | 15 | 14 | 1 | 0 | Stronger arsenal identity; still needs arms export/client-state mechanics and persistent aggression. |
| `KZR_soviet_collapse_ancient_focus_tree` | 16 | 14 | 7 | 2 | 0 | Compact ancient restoration, not a full route family. |
| `SOG_soviet_collapse_ancient_focus_tree` | 16 | 14 | 7 | 1 | 0 | Compact ancient restoration, not a full route family. |
| `KHW_soviet_collapse_ancient_focus_tree` | 16 | 14 | 6 | 1 | 0 | Compact ancient restoration, not a full route family. |
| `ALN_soviet_collapse_ancient_focus_tree` | 16 | 17 | 8 | 1 | 0 | Compact ancient restoration, not a full route family. |

## Missing Or Simplified Content

- The four ancient restoration trees remain 16-focus compact trees. They do not satisfy the spec's full political, industry, expansion, military, diplomacy, and late-game route standard unless intentionally downgraded by the parent.
- `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` remain compact crisis trees. Several have good hooks, but the shallow shape does not match the requested aggressive overpowered chaos-country tree standard.
- Most 47-focus custom splinter trees have route labels but no direct decision, war, claim, core, unit, faction, cosmetic, or AI-strategy hooks by static scan. They depend on helper effects for visible gameplay.
- Republic trees generally have political, industry, and expansion labels, but many route payoffs are helper bundles instead of decisions, missions, units, advisors, leaders, war plans, claims, cores, postwar settlement, or map-building programs.
- Moldova layout was locally improved, but Moldova still lacks direct river, Dniester, Romanian, Ukrainian corridor, and bridge-state decision surfaces.
- Kazakhstan remains wide and branch-dense; `kaz_soviet_collapse_alash_memory_restored` and `kaz_soviet_collapse_socialist_steppe_republic` are still diagonally adjacent mutually exclusive route choices at `(35, 3)` and `(34, 4)`. I did not move them because the surrounding resource, Alash, socialist, and follow-up lines are wide enough that a one-coordinate patch could create worse route geometry without a rendered layout pass.

## Idea-Spam Findings

Direct focus-file idea spam:

- Direct `add_ideas`, `add_timed_idea`, `swap_ideas`, or direct visible `remove_ideas` in the four focus files: none found in parsed completion rewards.

Helper-caused visible/repeated idea churn:

- `common/scripted_effects/005_soviet_collapse_effects.txt:5466` defines `soviet_collapse_update_consolidated_republic_ideas`, the staged idea updater.
- `common/scripted_effects/005_soviet_collapse_effects.txt:5375` defines `soviet_collapse_mark_republic_staged_idea_recently_changed`, which gates repeated staged swaps with a timed flag.
- The focus files still heavily call broad helper effects that feed variables and staged idea recalculation. The visible result is fewer direct idea rewards in focus files, but many focuses still feel like repeated institutional-spirit churn because the same helper families carry most route payoffs.

High-volume helper calls:

| Helper | Definition | Focus calls | Issue |
| --- | --- | ---: | --- |
| `soviet_collapse_apply_focus_legal_recognition` | `common/scripted_effects/005_soviet_collapse_effects.txt:8121` | 305 | Generic legal recognition replaces too many route-specific political payoffs. |
| `soviet_collapse_apply_focus_depot_and_supply_control` | `common/scripted_effects/005_soviet_collapse_effects.txt:8182` | 258 | Often substitutes for rail, supply hub, depot, and logistics missions. |
| `soviet_collapse_apply_focus_military_consolidation` | `common/scripted_effects/005_soviet_collapse_effects.txt:8160` | 254 | Often substitutes for units, templates, doctrine, commander, and war-plan surfaces. |
| `soviet_collapse_apply_focus_league_preparation` | `common/scripted_effects/005_soviet_collapse_effects.txt:8503` | 220 | Often substitutes for League decisions, guarantees, member votes, and joint operations. |
| `soviet_collapse_apply_focus_foreign_channel` | `common/scripted_effects/005_soviet_collapse_effects.txt:9275` | 176 | Often substitutes for sponsor desks, aid corridors, relation work, and diplomatic missions. |
| `soviet_collapse_apply_focus_high_chaos_identity` | current helper call scan | 98 | Helps high-chaos identity, but it cannot carry whole route families alone. |
| `soviet_collapse_apply_focus_socialist_sovereignty` | current helper call scan | 23 | Smaller count, but many socialist routes still need direct institutions. |

## Pathline And Mutual-Exclusion Findings

Patched:

- `common/national_focus/005_soviet_collapse_republics.txt:7892` `moldova_soviet_collapse_ukrainian_border_compact`
  - Before: `(11, 3)`, adjacent to mutually exclusive `moldova_soviet_collapse_independent_republic_council` at `(11, 4)`.
  - After: `(13, 3)`.

Current static layout scan after patch:

- Duplicate focus ids: 0.
- Duplicate coordinates within the same tree: 0.
- Straight prerequisite pathline through another focus: 0.
- Same-row prerequisite line risks by heuristic: 0.
- Adjacent mutually exclusive pairs: 1 remaining pair, counted bidirectionally by parser:
  - `kaz_soviet_collapse_alash_memory_restored` `(35, 3)` and `kaz_soviet_collapse_socialist_steppe_republic` `(34, 4)`.

Remaining visual-review risks:

- Kazakhstan political-past selector should be checked in a rendered view before moving nodes.
- Ukraine, Belarus, Kazakhstan, CFR, and MFR have wide route geometry from prior worktree changes. Static scan passes, but rendered pathline review is still needed before parent completion.
- Many route forks use hidden `available = { has_completed_focus = ... }` semantics instead of player-obvious route structure. This is a parent redesign item, not a safe one-line patch.

## Icon Coverage Table

Sprite definition lookup found no missing focus icon sprite ids for parsed focus icons.

| File | Focus icons | Unique icon ids | Repeated icon groups | Repeated icon uses | Missing sprite defs |
| --- | ---: | ---: | ---: | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 501 | 458 | 22 | 65 | 0 |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 885 | 99 | 219 | 0 |
| `005_soviet_collapse_factory_successors.txt` | 128 | 113 | 11 | 26 | 0 |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 42 | 8 | 30 | 0 |

Repeated icon clusters to prioritize later:

- Republics: `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_steppe_supply_congress`, `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`.
- Custom splinters: `GFX_focus_FEV_diplomatic_plan`, `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_civil_rule`, `GFX_focus_MRC_foreign`, `GFX_focus_IUL_supply`.
- Factory successors: `GFX_focus_CFR_municipal_board_elections`, `GFX_focus_CFR_concrete_republic`, `GFX_focus_CFR_the_builder_state`, `GFX_focus_CFR_civilian_hegemony_project`, `GFX_focus_CFR_cement_allocation_boards`.
- Ancient restorations: `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_guard_old_routes`, `GFX_focus_soviet_collapse_ancient_league_bargain`, `GFX_focus_soviet_collapse_ancient_old_border_files`, `GFX_focus_soviet_collapse_ancient_symbolic_state`.

No icon asset or `.gfx` file was changed in this pass.

## Localisation And Reward Mismatches

Mechanical localisation coverage:

- Parsed focus ids: 1,698.
- Missing focus name keys: 0.
- Missing focus `_desc` keys: 0.

Reward/localisation mismatch risks:

- `*_diplomatic_plan`, `*_industry_plan`, `*_war_plan`, `*_hidden_doctrine`, and `*_endgame` focuses frequently promise route identity while their rewards are broad helper bundles.
- Naval language in `NRF`, `ARD`, and Black Sea-adjacent Ukraine should more consistently surface ships, naval bases, dockyards, convoy warfare, coastal forts, or naval missions.
- Rail/supply language in `PRA`, Belarus, Kazakhstan, and internal republic routes should more consistently surface railways, supply hubs, depot missions, armored trains, or logistics decisions.
- Construction language in `CFR` should keep moving toward contract decisions, construction missions, named state building programs, and debt/permit consequences.
- Ancient restoration localisation sounds distinct, but route payloads are compact and repeated across four trees.

## AI Behavior Gaps

Mechanical status:

- All parsed focuses have `ai_will_do`.

Gaps:

- Many `ai_will_do` blocks are local static weights, not route-family strategies.
- AI route behavior does not consistently react to collapse pressure, war state, neighboring breakaways, League membership, foreign appetite, route commitments, or already chosen political identities.
- Many 47-focus custom splinter trees have no direct `add_ai_strategy` hooks by static scan, so route behavior is likely focus-weight-only.
- Parent should add route-aware AI behavior while adding direct mechanics, not as a separate cosmetic pass.

## High-Priority Parent Fixes

1. Replace helper clusters with direct route mechanics in the highest-impact trees first: Ukraine, Belarus, Kazakhstan, PRA, DSC, NRF, ARD, CFR, MFR, OGB.
2. Decide whether compact crisis and ancient trees are intentionally short. If not, expand them through a parent-level redesign plan, not subagent one-line patches.
3. Add decision and mission integration where route text promises rail, supply, river, port, Dniester, League, border, grain, oil, foreign patron, construction, arsenal, convoy, or postwar settlement actions.
4. Add route-aware AI strategies at major route selectors and route endpoints.
5. Render-check Kazakhstan, Ukraine, Belarus, CFR, and MFR after any coordinate movement. The static parser cannot prove all HOI4 pathline sprites will look correct.
6. Reduce repeated icon clusters through the asset/icon workflow later. This pass did not touch visuals by user instruction.

## Validation

Ran:

- `python3` brace balance over all four Event 005 focus files.
  - `005_soviet_collapse_republics.txt`: `brace_balance=0`
  - `005_soviet_collapse_custom_splinters.txt`: `brace_balance=0`
  - `005_soviet_collapse_factory_successors.txt`: `brace_balance=0`
  - `005_soviet_collapse_ancient_restorations.txt`: `brace_balance=0`
- `rg -n '<=|>=' common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - No matches.
- Static parser for focus counts, missing icon field, missing `ai_will_do`, missing `completion_reward`, duplicate ids, duplicate same-tree coordinates, localisation coverage, icon sprite definition coverage, pathline hits, adjacent mutually exclusive pairs, helper counts, route summaries.
  - Missing icon field: 0.
  - Missing `ai_will_do`: 0.
  - Missing `completion_reward`: 0.
  - Missing localisation names: 0.
  - Missing localisation descriptions: 0.
  - Missing parsed focus icon sprite definitions: 0.
  - Straight pathline hits after patch: 0.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - Clean.
- `git diff --name-only -- gfx/flags`
  - Empty.

Skipped:

- In-game validation and rendered focus-tree screenshot review. This subagent pass is script/static audit only.
- Full route redesign. The user explicitly bounded this pass to small safe patches and handoff evidence.

## Remaining Route Risks

- The parent objective remains incomplete. Event 005 focus trees are still not fully reworked into distinct, mechanically rich, aggressive, overpowered chaos-country trees.
- Broad helper effects have reduced visible direct idea spam, but they also mask shallow route payoffs.
- The surviving Kazakhstan diagonal route-selector adjacency should be handled only during a rendered layout pass or a broader Kazakhstan branch movement.
- No visual assets were touched; repeated icons remain a known backlog item for a later asset-safe pass.
