# Event005 Soviet Collapse Focus Tree Fresh Audit

Auditor: `chaosx_focus_tree_auditor`
Date: 2026-06-04 08:19 UTC
Mode: read-only audit, no gameplay patch

## Scope

Audited focus files:

- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`

Directly checked helper/decision/localisation files as needed:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/decisions/categories/005_soviet_collapse_categories.txt`
- `localisation/english/005_soviet_collapse_focus_decisions_l_english.yml`

No gfx, flag, `.tga`, or flag sprite files were inspected or touched.

## Required References Consulted

- Repo guidance: `AGENTS.md`
- Skills: `.agents/skills/hoi4-focus-trees/SKILL.md`, `.agents/skills/hoi4-decisions-missions/SKILL.md`
- Offline Paradox wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `loc_objects_documentation.md`, `loc_formatter_documentation.md`
- Vanilla focus precedents sampled: `generic.txt`, `soviet.txt`, `finland.txt`

## Mechanical Counts

| File | Trees | Focuses | Direct idea add/swap/remove | Decision tooltip calls | Wargoal focuses | Heuristic filter mismatches | Prereq focuses without `relative_position_id` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `005_soviet_collapse_ancient_restorations.txt` | 4 | 64 | 0 | 16 | 4 | 26 | 60 |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | 0 | 37 | 6 | 186 | 980 |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 | 0 | 19 | 5 | 15 | 125 |
| `005_soviet_collapse_republics.txt` | 9 | 501 | 0 | 35 | 0 | 81 | 492 |
| Total | 41 | 1698 | 0 | 107 | 15 | 308 | 1657 |

Other validation results:

- Duplicate focus IDs in scoped files: 0.
- Focus files and directly checked scripted effect file have balanced braces by rough brace-depth smoke check.
- No same-tree duplicate coordinates or same-row spacing below 2 grid units were found by the layout script.
- Heuristic mutual-exclusion/prerequisite line-crossing risks: 193 total, with the highest-risk groups in CFR, Baltic, Central Asia, Kazakhstan, and repeated custom splinter radical/settlement forks.

## Findings

### P1 - Shared helper bundle spam is still the main reward problem

The four focus files no longer directly spam `add_ideas`, `swap_ideas`, or `remove_ideas`, but they call generic Event005 helper bundles at very high frequency. These helpers repeatedly grant similar institution variables, focus recovery progress, pressure deltas, equipment, XP, league support, recognition, and depot control. That makes many focus rewards feel like the same mechanical bundle under different names.

Highest-frequency helper calls in scoped files:

- `soviet_collapse_apply_focus_depot_and_supply_control`: 75 calls in `custom_splinters`, 65 in `republics`
- `soviet_collapse_apply_focus_military_consolidation`: 75 in `custom_splinters`, 57 in `republics`
- `soviet_collapse_apply_focus_legal_recognition`: 53 in `custom_splinters`, 49 in `republics`
- `soviet_collapse_apply_focus_republican_compact_plan`: 53 in `custom_splinters`, 27 in `republics`
- `soviet_collapse_apply_focus_high_chaos_identity`: 41 in `custom_splinters`, 18 in `republics`
- `soviet_collapse_apply_custom_splinter_league_identity`: 38 in `custom_splinters`
- `soviet_collapse_apply_custom_splinter_enemy_front_identity`: 36 in `custom_splinters`

Representative helper definitions checked:

- `common/scripted_effects/005_soviet_collapse_effects.txt:8335` `soviet_collapse_apply_focus_legal_recognition`
- `common/scripted_effects/005_soviet_collapse_effects.txt:8404` `soviet_collapse_apply_focus_military_consolidation`
- `common/scripted_effects/005_soviet_collapse_effects.txt:8426` `soviet_collapse_apply_focus_depot_and_supply_control`
- `common/scripted_effects/005_soviet_collapse_effects.txt:8747` `soviet_collapse_apply_focus_league_preparation`
- `common/scripted_effects/005_soviet_collapse_effects.txt:9129` `soviet_collapse_apply_focus_chaos_assault_plan`

Priority fix: keep the common helpers as milestones, but remove them from routine support focuses where direct rewards already give equipment/factories/XP. Add route-specific helpers for capstone branches and gate repeated pressure or recovery gains behind per-branch milestone flags.

### P1 - Several chaos-country trees are not aggressive or distinct enough

Many chaos successor trees have strong names but few direct aggressive surfaces. In `custom_splinters`, only 6 focuses directly create a wargoal:

- `PRA_rails_over_capitals`
- `TSC_starfall_mandate`
- `RMC_resurrection_without_state`
- `DSC_congress_of_the_dead_army`
- `NRF_northern_revenant_fleet`
- `ICD_commissariat_without_end`

The 47-focus custom splinter trees mostly rely on shared identity helpers and have no direct decision or wargoal unlocks in many cases. Examples with zero direct decision unlocks in the parsed counts include `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`; `ARD` and `NLC` have only a small amount of direct decision surfacing.

The 18-focus high-chaos trees are particularly shallow:

- `TSC_soviet_collapse_focus_tree`: 18 focuses, 1 decision focus, 1 wargoal focus.
- `RMC_soviet_collapse_focus_tree`: 18 focuses, 1 decision focus, 1 wargoal focus.
- `ICD_soviet_collapse_focus_tree`: 18 focuses, 1 decision focus, 1 wargoal focus.
- `NRF_soviet_collapse_focus_tree`: 18 focuses, 6 decision focuses, 1 wargoal focus.
- `DSC_soviet_collapse_focus_tree`: 18 focuses, 10 decision focuses, 1 wargoal focus, but still heavily helper-driven.

Priority fix: give each chaos country a visible aggression package: direct claims or wargoals, route-specific raids/ultimata/war-prep decisions, AI conquest/antagonize strategy, and one distinct mechanic or endpoint that is not only shared pressure variables.

### P1 - Layout pathline risk remains broad

The focus files are syntactically balanced and have no duplicate focus IDs, but they overwhelmingly use absolute positions. HOI4 wiki guidance prefers `relative_position_id` for prerequisite branches because path generation is fragile when branches are moved.

Counts of prerequisite focuses without `relative_position_id`:

- 60 in `ancient_restorations`
- 980 in `custom_splinters`
- 125 in `factory_successors`
- 492 in `republics`

Highest-risk line-crossing clusters:

- Ancient symbolic/expansion forks: `KZR_symbolic_crossing_state` / `KZR_expansionist_steppe_levy`, `SOG_symbolic_city_league` / `SOG_expansionist_merchant_claims`, `KHW_symbolic_oasis_authority` / `KHW_expansionist_water_claims`, `ALN_symbolic_pass_principality` / `ALN_expansionist_mountain_claims`.
- `CFR_soviet_collapse_focus_tree`: 31 heuristic crossing risks around `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_invite_the_foreign_contract_board`, `CFR_the_concrete_committee`.
- `soviet_collapse_baltic_focus_tree`: 13 crossing risks around `baltic_soviet_collapse_legal_continuity_government`, `baltic_soviet_collapse_military_border_government`, `baltic_soviet_collapse_baltic_league_first`, `baltic_soviet_collapse_foreign_protection_council`.
- `soviet_collapse_central_asia_focus_tree`: 12 crossing risks around `central_asia_soviet_collapse_local_republic_council`, `central_asia_soviet_collapse_military_border_authority`, `central_asia_soviet_collapse_clear_the_mountain_bands`, `central_asia_soviet_collapse_negotiate_with_the_mountain_bands`.
- `soviet_collapse_kazakhstan_focus_tree`: 9 crossing risks around `kaz_soviet_collapse_alash_memory_restored`, `kaz_soviet_collapse_resource_defense_directorate`, `kaz_soviet_collapse_foreign_technical_missions`, `kaz_soviet_collapse_league_resource_pool`.

Priority fix: convert the highest-risk fork areas to relative positioning and place mutually exclusive choices so the parent is centered above the split and later OR-join focuses sit clearly below the two branches.

### P2 - Decision integration exists, but many route branches still do not change the decision layer enough

All `unlock_decision_tooltip` targets in the scoped focus files resolve to decision definitions in `common/decisions/005_soviet_collapse_decisions.txt`. No missing decision definition was found.

However, decision surfacing is concentrated:

- `PRA_soviet_collapse_focus_tree`: 14 decision focuses, strong integration.
- `DSC_soviet_collapse_focus_tree`: 10 decision focuses, stronger than most high-chaos trees.
- Ukraine has 7 direct league decision focuses.
- Kazakhstan has 4 direct route decision focuses despite 92 focuses.
- `soviet_collapse_republics.txt` has 501 focuses but only 19 decision focuses and no direct wargoal focuses.
- Many custom splinter 47-focus trees have zero direct decision unlocks.

There is also player-facing localisation debt in `localisation/english/005_soviet_collapse_focus_decisions_l_english.yml`: cost strings at lines 4, 8, 12, 16, 20, and 24 include `Unlock:` wording. That reads like implementation metadata rather than in-world action text and should be moved to focus tooltips or documentation.

Priority fix: add route-specific decision families to under-integrated trees, especially high-chaos and Kazakhstan/republic capstones. Replace `Unlock:` wording in cost text with concise icon-first requirements or route-state phrasing.

### P2 - Shallow or disconnected branch families remain

The ancient restoration trees are compact but skeletal: each has 16 focuses, 2 decision focuses, 3 claim focuses, 1 wargoal focus, and no direct politics package such as leader, party, law, council, advisor, or visible country identity changes inside the audited focus files.

Factory successor depth is uneven:

- `CFR` has 47 focuses and 8 decision focuses, but only 4 focuses with direct industry construction in the focus file; much of the construction identity is helper-hidden.
- `OGB` has 23 focuses, 5 decision focuses, 2 wargoal focuses, and 1 claim focus, but its route families are still small.
- `MFR` has 58 focuses but only 3 decision focuses and 1 wargoal focus; its arsenal-state identity is mostly helper reward flow rather than an evolving decision/military-production system.

Republic depth is uneven:

- Ukraine is broad and politically active, but has no direct focus wargoals; its expansion lives through decisions.
- Kazakhstan has 92 focuses but only 4 direct decision focuses and no direct claims/wargoals in the focus file.
- Baltic, Central Asia, Moldova, Belarus, and Kazakhstan still have multiple pathline risks in route fork areas.

Priority fix: for each shallow tree, add at least one route-specific political consequence, one industry or logistics map action, one military or expansion decision family, and one endpoint payoff that is not another generic variable bundle.

### P3 - Focus filters often do not match rewards

Heuristic filter mismatch count: 308. This includes false positives where helper payloads hide the true reward, but enough examples are clear to justify a filter pass.

Representative mismatches:

- `KZR_old_border_files`, `SOG_old_city_border_files`, `KHW_old_oasis_border_files`, `ALN_old_pass_border_files`: focus filters emphasize annexation but rewards also unlock decisions and build industry/logistics.
- `PRA_omsk_station_guard`, `PRA_count_the_locomotives`, `PRA_repair_crews_without_ministries`, `PRA_armored_train_schools`: decision/industry effects are not consistently reflected.
- `CFR_the_builder_state_marches_east`: annexation/industry focus also has political/AI-strategy effects.
- `MFR_factory_guard_columns` and `MFR_workers_own_the_arsenal`: military/manpower filters miss industry effects.
- `ukr_soviet_collapse_first_republican_line`, `soviet_collapse_military_defense_council`, `internal_soviet_collapse_ural_mobile_defense`, `baltic_soviet_collapse_the_port_economy`, `central_asia_soviet_collapse_border_commanders`, `kaz_soviet_collapse_the_steppe_arsenal`: rewards or helpers imply missing industry, political, or army filters.

Priority fix: after reward-helper cleanup, run a focused search-filter pass. Avoid adding every possible filter; make the top two or three player-relevant filters match the visible reward.

## Validation Commands And Results

Commands run:

```bash
wc -l common/national_focus/005_soviet_collapse_ancient_restorations.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_republics.txt
```

Result: 42,159 total lines across the four focus files.

```bash
rg -n "load_focus_tree|mark_focus_tree_layout_dirty|complete_national_focus|unlock_decision|activate_mission|available =|completion_reward|add_ideas|swap_ideas|remove_ideas|ai_will_do|search_filters|mutually_exclusive|prerequisite|relative_position_id" "/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md" "/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md"
```

Result: confirmed vanilla docs entries for focus loading, decision tooltips, idea effects, and related effects/triggers.

```bash
rg -n "unlock_decision|activate_mission|completion_reward|search_filters|mutually_exclusive|prerequisite|relative_position_id|ai_will_do|allow_branch|bypass|add_ideas|swap_ideas|remove_ideas" "/home/klim/projects/Hearts of Iron IV/common/national_focus/soviet.txt" "/home/klim/projects/Hearts of Iron IV/common/national_focus/finland.txt" "/home/klim/projects/Hearts of Iron IV/common/national_focus/generic.txt"
```

Result: sampled vanilla focus syntax, reward, filter, AI, prerequisite, and relative-position precedent.

```bash
python3 - <<'PY'
# Parsed the four scoped focus files for tree/focus counts, reward calls, helper calls,
# duplicate IDs, filter mismatches, decision tooltip targets, coordinates, and pathline risks.
PY
```

Key results:

- 41 focus trees, 1698 focuses.
- 0 duplicate focus IDs.
- 0 direct `add_ideas`, `swap_ideas`, or `remove_ideas` calls in scoped focus files.
- 107 `unlock_decision_tooltip` calls; all referenced decision IDs exist.
- 15 direct wargoal focuses.
- 308 heuristic filter mismatches.
- 1657 prerequisite focuses without `relative_position_id`.
- 193 heuristic mutual-exclusion/prerequisite pathline risks.

```bash
python3 - <<'PY'
# Rough brace-depth smoke check over the four focus files and common/scripted_effects/005_soviet_collapse_effects.txt.
PY
```

Result: final brace depth 0 and no negative-depth point for all five checked files.

## Compact Parent Implementation Plan

1. Fix pathline/layout first in bounded clusters: CFR governance fork, Baltic legal/military/foreign fork, Central Asia local/military/basmachi forks, Kazakhstan Alash/resource forks, the repeated custom splinter `radical_turn`/`settlement` joins, and all four ancient symbolic/expansion forks.
2. Replace high-frequency helper spam with route-specific reward helpers. Keep common helpers for milestones, not routine support focuses. Add one-time branch milestone flags where repeated pressure or recovery gain can stack too freely.
3. Deepen underpowered chaos trees. Start with `TSC`, `RMC`, and `ICD`, then the 47-focus custom splinters with zero direct decision unlocks. Add decisions, direct claims/wargoals or ultimata, AI strategy, and a unique mechanic payoff.
4. Expand focus-decision integration for Kazakhstan, MFR, OGB, and generic 47-focus custom splinters. Use existing decision categories where possible, but make route unlocks visibly change available decisions and costs.
5. Run a final search-filter pass after reward cleanup so filters match visible rewards rather than hidden helper implementation.

## Files Changed By This Audit

- Added this report only.

No gameplay, localisation, gfx, flag, `.tga`, or sprite files were edited.
