# Event 005 Soviet Collapse Focus Tree Reward, Depth, and Layout Audit

Subagent: Chaos Redux focus tree subagent
Date: 2026-05-30
Scope: `common/national_focus/005_soviet_collapse_republics.txt`, `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `common/national_focus/005_soviet_collapse_factory_successors.txt`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt`, and directly called Event 005 helpers/localisation as needed.

## References read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `loc_formatter_documentation.md`, `loc_objects_documentation.md`, `common/decisions/_documentation.md`, `common/script_constants/documentation.md`.
- Vanilla precedents inspected: `common/national_focus/soviet.txt`, `generic.txt`, `baltic_shared.txt`, `common/decisions/SOV.txt`, `common/decisions/formable_nation_decisions.txt`.

## Patch made

Changed file:

- `common/national_focus/005_soviet_collapse_republics.txt`

Changed focus id:

- `ukr_soviet_collapse_carpathian_security_belt`

Behavior before:

- The prerequisite line from `ukr_soviet_collapse_romanian_grain_and_river_bargain` at `(34, 7)` to `ukr_soviet_collapse_carpathian_security_belt` at `(28, 9)` mechanically passed through `ukr_soviet_collapse_black_banner_compact` at `(31, 8)`.

Behavior after:

- `ukr_soviet_collapse_carpathian_security_belt` is now at `(29, 10)`. The rerun layout detector reports 0 pathline hits, 0 same-row prerequisites, 0 upward prerequisites, and 0 mutual-exclusion midpoint collisions across the audited focus trees.

Localisation keys changed: none.
Icon ids changed: none.
Flags/assets: none touched.

Note: the worktree already contained broad Event 005 edits before this pass. I only claim the coordinate change above.

## Route coverage table

| Required route/content area | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine major republic identity | `soviet_collapse_ukraine_focus_tree`, 83 focuses, `005_soviet_collapse_republics.txt:9` | Present, mechanically improved | Layout pathline issue fixed in this pass. Branches cover statehood, politics, army, foreign support, Black Sea, League, and high-chaos hooks. Still reward-helper heavy. |
| Generic breakaway republic | `soviet_collapse_breakaway_focus_tree`, 36 focuses, `005_soviet_collapse_republics.txt:2369` | Present but simplified | Survival/state-building route exists, but expansion and decision consequences are light. |
| Internal republics | `soviet_collapse_internal_republic_focus_tree`, 62 focuses, `005_soviet_collapse_republics.txt:3166` | Present but generic | Many rewards are construction/stat/helper progress. Route identity needs stronger region-specific decision hooks. |
| Baltic republics | `soviet_collapse_baltic_focus_tree`, 42 focuses, `005_soviet_collapse_republics.txt:4670` | Present but compact | Legal/restoration and defense identity exists; expansion/postwar handling remains limited. |
| Caucasus republics | `soviet_collapse_caucasus_focus_tree`, 40 focuses, `005_soviet_collapse_republics.txt:5634` | Present but compact | Needs stronger mountain security, neighbor conflict, and League settlement hooks. |
| Central Asian republics | `soviet_collapse_central_asia_focus_tree`, 45 focuses, `005_soviet_collapse_republics.txt:6561` | Present with some expansion | Has claims and restoration-debate hooks, but still lacks deeper postwar or decision-driven integration. |
| Moldova | `soviet_collapse_moldova_focus_tree`, 48 focuses, `005_soviet_collapse_republics.txt:7706` | Present | Route mechanics and Prut/Soviet-pressure hooks exist, but many rewards still resolve as flat helper/stat gains. |
| Belarus | `soviet_collapse_belarus_focus_tree`, 53 focuses, `005_soviet_collapse_republics.txt:8867` | Present but needs payoff variety | Forest/security/corridor branches exist. More route-specific diplomacy, expansion, and decision consequences are still needed. |
| Kazakhstan | `soviet_collapse_kazakhstan_focus_tree`, 92 focuses, `005_soviet_collapse_republics.txt:10198` | Broad but reward-heavy | Large route surface exists. It still leans heavily on construction/stat/helper rewards instead of unique state, decision, or postwar systems. |
| Full custom/high-chaos splinters | FTH, BSC, TNC, ALA, BBH, KRS, UDC, SDZ, GAC, DHC, KHC, FEV, SZA, UWD, MRC, IUL, BAC, ARD, NLC, each 47 focuses in `005_soviet_collapse_custom_splinters.txt` | Present but not aggressive enough | These are no longer tiny stubs, but most still use generic identity helpers and flat stockpile/building rewards. Only a subset has focus-level war goals; most need stronger direct aggression, postwar, or decision packages. |
| Shallow crisis splinters | PRA 22 focuses; TSC/RMC/DSC/NRF/ICD 18 focuses in `005_soviet_collapse_custom_splinters.txt` | Still shallow | These now include some war-goal/decision hooks, but they remain short ladders rather than full political/industry/military/expansion branches. |
| Factory successors | CFR 47, OGB 23, MFR 58 focuses in `005_soviet_collapse_factory_successors.txt` | Mixed | CFR/MFR have real forks. OGB has new claims/wargoals but remains only 23 focuses and is still shallow for a high-impact successor. |
| Ancient restorations | KZR/SOG/KHW/ALN, 16 focuses each in `005_soviet_collapse_ancient_restorations.txt` | Shallow | Claims and museum/archivist decision tooltips exist, but the trees are still compact restoration stubs, not full ancient-restoration country identities. |

## Missing or simplified content

1. Shallow crisis splinters remain the highest route-depth issue: `PRA_soviet_collapse_focus_tree` at `005_soviet_collapse_custom_splinters.txt:1215`, `TSC_soviet_collapse_focus_tree` at `:1814`, `RMC_soviet_collapse_focus_tree` at `:2289`, `DSC_soviet_collapse_focus_tree` at `:2772`, `NRF_soviet_collapse_focus_tree` at `:3369`, and `ICD_soviet_collapse_focus_tree` at `:3873`.
2. Full 47-focus custom splinters still need more high-chaos aggression: `FTH_soviet_collapse_focus_tree` at `:4`, `BSC` at `:4346`, `TNC` at `:5472`, `ALA` at `:6606`, `BBH` at `:7722`, `KRS` at `:8923`, `UDC` at `:10164`, `SDZ` at `:11361`, `GAC` at `:12602`, `DHC` at `:13781`, `KHC` at `:14982`, `FEV` at `:16176`, `SZA` at `:17349`, `UWD` at `:18525`, `MRC` at `:19727`, `IUL` at `:20905`, `BAC` at `:22060`, `ARD` at `:23202`, and `NLC` at `:24399`.
3. `OGB_soviet_collapse_focus_tree` at `005_soviet_collapse_factory_successors.txt:1170` is still a 23-focus successor. It has claims/wargoals and Volga-restoration hooks now, but remains thin compared with CFR/MFR.
4. Ancient restorations at `005_soviet_collapse_ancient_restorations.txt:5`, `:381`, `:751`, and `:1124` are 16-focus stubs with claims and a few decision tooltips. They need broader political, industry, military, diplomacy, and endgame identity before completion can be claimed.
5. Reward style remains helper-heavy. Direct idea spam is gone, but 1,234 focuses call helper effects that expand to at least one `add_ideas`, with 1,644 total helper-call instances.

## Focus reward idea audit

Direct focus rewards:

- Direct `add_ideas` or `add_timed_idea` in audited focus completion rewards: 0 focuses.
- Duplicate same idea within one focus reward: 0.

Helper-expanded idea grants:

| Helper effect | Focus call count | Expanded ideas | Definition |
| --- | ---: | ---: | --- |
| `soviet_collapse_apply_focus_legal_recognition` | 305 | 1 `add_ideas` | `common/scripted_effects/005_soviet_collapse_effects.txt:7963` |
| `soviet_collapse_apply_focus_depot_and_supply_control` | 258 | 1 `add_ideas` | `common/scripted_effects/005_soviet_collapse_effects.txt:8015` |
| `soviet_collapse_apply_focus_military_consolidation` | 254 | 1 `add_ideas` | `common/scripted_effects/005_soviet_collapse_effects.txt:7996` |
| `soviet_collapse_apply_focus_league_preparation` | 220 | 1 `add_ideas` | `common/scripted_effects/005_soviet_collapse_effects.txt:8333` |
| `soviet_collapse_apply_focus_foreign_channel` | 176 | 1 `add_ideas` | `common/scripted_effects/005_soviet_collapse_effects.txt:9102` |
| `soviet_collapse_apply_custom_splinter_league_identity` | 38 | 1 `add_ideas` | `common/scripted_effects/005_soviet_collapse_effects.txt:13856` |
| `soviet_collapse_apply_custom_splinter_enemy_front_identity` | 36 | 1 `add_ideas` | `common/scripted_effects/005_soviet_collapse_effects.txt:13736` |
| `soviet_collapse_apply_focus_socialist_sovereignty` | 23 | 1 `add_ideas` | `common/scripted_effects/005_soviet_collapse_effects.txt:7979` |

Assessment: the parent already removed direct focus idea spam successfully. The remaining visible idea churn is consolidated through helpers, but the helper density is still high enough to create repetitive focus-effect tooltips and reward sameness.

## Icon coverage table

| Check | Result |
| --- | ---: |
| Audited focus trees | 41 |
| Audited focus blocks | 1,698 |
| Missing focus icon assignments | 0 |
| Unique icon ids | 1,498 |
| Repeated icon groups | 140 |
| Flag sprites/assets touched | 0 |

Repeated icons are not load-breaking. They remain a visual-quality issue where route identity is still generic, especially the ancient restorations and recurring custom-splinter route roles.

## Localisation and reward mismatch list

| Check | Result |
| --- | ---: |
| Event 005 English localisation files scanned | 12 |
| Focus name keys missing | 0 |
| Focus description keys missing | 0 |

Reward mismatch findings:

1. Many high-chaos splinter names/descriptions imply dangerous expansion or strange-state authority, but most 47-focus splinter trees still resolve through the same identity helpers, construction, equipment, manpower, XP, stability, and political power rewards. Relevant trees are listed in the full custom/high-chaos row above.
2. The ancient restoration descriptions imply state restoration and old territorial memory, but each tree remains 16 focuses with limited decision hooks and no full route family. Relevant starts: `005_soviet_collapse_ancient_restorations.txt:5`, `:381`, `:751`, `:1124`.
3. OGB now has Volga claims/wargoals and restoration hooks, but its 23-focus size still underserves the “OP/high-impact successor” expectation. Start: `005_soviet_collapse_factory_successors.txt:1170`.

## AI behavior gaps

1. Every audited focus has an `ai_will_do` block, but many are local flat `base` weights rather than route strategy.
2. High-chaos/custom splinters need stronger AI pressure toward aggression, claims, war goals, and postwar settlement. The shallow crisis splinters have some direct war-goal hooks now, but the larger 47-focus custom splinters still mostly rely on helper/stat rewards.
3. Republic trees need more route-aware AI for League, foreign dependency, expansion, and high-chaos escalation. Existing focus weights do not replace AI strategy plans or decision AI.
4. OGB and ancient restorations should receive route AI only after their route depth is expanded; adding detailed weights to current short trees would preserve shallow structure.

## High-priority fixes for parent

1. Expand or explicitly scope down PRA/TSC/RMC/DSC/NRF/ICD crisis splinters. They remain too shallow for high-chaos actors.
2. Add aggressive route payoffs for the 47-focus custom splinters: claims, war goals, cores, targeted decisions, special units, AI strategy, and postwar settlement hooks.
3. Expand OGB beyond the 23-focus shape or document it as intentionally compact.
4. Expand KZR/SOG/KHW/ALN ancient restorations beyond 16-focus stubs with real branch families.
5. Reduce helper-expanded idea tooltip noise by converting more focus payoffs into route flags, decisions, state work, units, postwar hooks, or hidden updates with clearer player-facing tooltips.
6. Run an icon differentiation pass after route redesigns settle. Do not touch `gfx/flags` unless flag work is explicitly in scope.

## Validation run

- Brace balance on audited focus files plus `common/scripted_effects/005_soviet_collapse_effects.txt`: final depth 0, no early closes.
- Unsupported operators in touched focus/script files: no `<=` or `>=`.
- Duplicate focus IDs: 0.
- Duplicate coordinates by tree: 0.
- Mechanical layout/pathline audit after patch: 0 pathline hits, 0 same-row prerequisites, 0 upward prerequisites, 0 mutual-exclusion midpoint collisions.
- Direct `add_ideas`/`add_timed_idea` in focus rewards: 0 focuses.
- Duplicate direct same-idea grants in one focus: 0.
- Helper-expanded idea helper usage: 1,234 focuses, 54 helper names, 1,644 helper-call instances.
- Localisation coverage across `localisation/english/005_soviet_collapse*_l_english.yml`: 0 missing focus name keys, 0 missing focus description keys.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt common/scripted_effects/005_soviet_collapse_effects.txt`: passed.
- `git diff --no-index --check /dev/null docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_102305_event005_focus_tree_reward_depth_layout_audit.md`: passed for the new untracked handoff file.
- `git diff --name-only -- gfx/flags`: empty.

## Skipped validation

- No in-game visual screenshot pass was run. The layout audit is mechanical and straight-line based; HOI4 can still render subjective line density differently.
- No full game launch validation was run from this subagent.
- No flag asset validation was run because `gfx/flags` and flag sprites/assets were explicitly out of scope.

## Remaining route risks

- Broad route depth remains incomplete for shallow crisis splinters, OGB, and all ancient restorations.
- Full custom splinters are present but not consistently strong/aggressive enough for high-chaos countries.
- Helper-expanded ideas are consolidated, but still overused as the main reward language.
- Repeated focus icons remain a visual-quality issue, though no missing icons were found.

## Plan handoff path

This handoff is the current audit/patch handoff:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_102305_event005_focus_tree_reward_depth_layout_audit.md`

Existing broader redesign plan still applies and should not be duplicated without parent decision:

- `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`
