# Event 005 Soviet Collapse Focus Tree Audit and DHC Reward Patch Handoff

Subagent: Chaos Redux focus tree subagent
Date: 2026-05-31
Scope: `common/national_focus/005_soviet_collapse_republics.txt`, `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `common/national_focus/005_soviet_collapse_factory_successors.txt`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

## Summary

Audited the four current Event 005 focus files and made one bounded focus-file-only patch. No flags, gfx, interface, sprites, images, music, sound, or asset manifests were edited.

The direct focus-file idea-spam issue is currently clean: the four scoped focus files have 0 direct `add_ideas` calls inside focus rewards, 0 focuses with multiple direct `add_ideas`, and 0 focuses adding the same idea more than once. The remaining reward-depth issue is mostly shallow focus rewards and helper-driven idea lifecycle outside direct focus rewards.

## Files Changed

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Patched `DHC_winter_road_columns` reward. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_event005_focus_tree_audit_dhc_reward_patch.md` | This audit and patch handoff. |

## Changed Focus Ids

| Focus id | File and line | Before | After |
| --- | --- | --- | --- |
| `DHC_winter_road_columns` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:14414` | Set `dhc_focus_winter_road_columns`, then built 1 random owned-controlled infrastructure level. No helper, no variable progress, no unit-equivalent payoff. | Adds `soviet_collapse_apply_focus_mobile_columns_reward = yes`, keeps the infrastructure reward, and adds `soviet_collapse_add_republic_focus_recovery_progress = yes`. |

Patch rationale: this is a safe local improvement because both helper IDs already exist and are already called from Event 005 focus rewards. It turns a one-building focus into a mobile-column/depot/institution/recovery payoff without adding new helpers, localisation, icons, claims, cores, or assets.

## Route Coverage Table

| Required route or family | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Republic successor trees | Ukraine, breakaway/shared, internal republic, Baltic, Caucasus, Central Asia, Moldova, Belarus, Kazakhstan in `005_soviet_collapse_republics.txt` | Implemented but uneven | 501 focuses across 9 trees. Kazakhstan and Ukraine are large, but dense rows and some reward-light focuses remain. |
| Full custom splinter trees | `FTH/BSC/TNC/ALA/BBH/KRS/UDC/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC` | Implemented but still generic in places | Most have 47 focuses. Many branches use helpers, but 47-focus bodies still include repeated random state-building, equipment, XP, and support rewards. |
| Compact chaos or crisis splinters | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` | Simplified | 18-22 focuses each. They need stronger special mechanics, unit/template hooks, and route-specific aggression to meet the full rework objective. |
| Factory successors | `CFR`, `MFR`, `OGB` in `005_soviet_collapse_factory_successors.txt` | Partly implemented | `CFR` has 47 focuses and `MFR` has 58. `OGB` has 23 and remains shallow for an overpowered restored-memory successor. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN` in `005_soviet_collapse_ancient_restorations.txt` | Simplified | 16 focuses each. Current branches include claims and identity hooks but need deeper route identity and payoff if treated as full playable countries. |
| Chaos countries overpowered/aggressive enough | Crisis splinters, factory successors, ancient restorations, high-chaos custom branches | Not complete | Direct `create_wargoal` appears in only 11 focuses across all four files; direct claims appear in 14 focuses; direct cores appear in 0 focuses. |

## Audit Counts

| Metric | Count |
| --- | ---: |
| Focus files audited | 4 |
| Focus trees found | 41 |
| Focus blocks found | 1698 |
| Direct focus-reward `add_ideas` calls | 0 |
| Focuses with multiple direct `add_ideas` | 0 |
| Focuses adding the same idea more than once | 0 |
| Focuses with assigned icons | 1698 |
| Focuses missing icon assignment | 0 |
| Unique focus icon ids | 1498 |
| Reused icon ids | 140 |
| Missing focus name localisation | 0 |
| Missing focus description localisation | 0 |
| Focuses missing `ai_will_do` | 0 |
| Duplicate exact focus coordinates | 0 |
| Dense same-row clusters, 4 or more focuses with `dx <= 2` | 33 |
| Mutual-exclusion midpoint/pathline suspects | 10 |
| Shallow reward heuristic candidates before patch | 32 |
| Same heuristic candidates after patch | 31 |

Term scan across direct focus rewards:

| Reward surface | Total direct occurrences | Focuses affected |
| --- | ---: | ---: |
| Equipment stockpile | 250 | 207 |
| Manpower | 121 | 121 |
| XP | 200 | 196 |
| Political or command power | 285 | 283 |
| Stability or war support | 333 | 325 |
| Factories or offsite buildings | 140 | 112 |
| State buildings | 712 | 408 |
| Claims | 45 | 14 |
| Cores | 0 | 0 |
| War goals | 11 | 11 |
| Decision unlocks | 98 | 70 |
| Direct unit/template/OOB hooks | 0 | 0 |
| Existing `soviet_collapse_* = yes` helpers | 1717 | 1510 |
| Random owned-controlled state rewards | 396 | 385 |

## Missing or Simplified Content

High-priority gaps:

1. `OGB_soviet_collapse_focus_tree` in `005_soviet_collapse_factory_successors.txt` has only 23 focuses. It has restoration flavor but not enough Volga legitimacy, heritage guard, expansion, settlement, or decision-loop depth for the requested overpowered successor role.
2. `TSC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, and `ICD_soviet_collapse_focus_tree` in `005_soviet_collapse_custom_splinters.txt` are 18-focus crisis trees. They need special mechanics and route payoff, not only stronger numbers.
3. Ancient restoration trees `KZR/SOG/KHW/ALN` in `005_soviet_collapse_ancient_restorations.txt` are 16-focus stubs. Their symbolic-versus-expansion routes exist, but they are not full route families.
4. Direct cores are absent across all four files. This may be intentional to avoid instant snowballing, but it weakens expansion branch payoff unless staged integration decisions or scripted helpers supply the postwar handling elsewhere.
5. Direct unit/template hooks are absent in focus rewards. `DHC_winter_road_columns` now uses the existing mobile-column helper, but broader chaos-country aggression still needs a full pass.

Worst shallow reward candidates still visible after this patch include:

| Focus id | File and line | Evidence |
| --- | --- | --- |
| `ukr_soviet_collapse_moscows_officers_in_our_barracks` | `005_soviet_collapse_republics.txt:193` | Direct XP-only reward by heuristic. |
| `baltic_soviet_collapse_university_volunteer_lists` | `005_soviet_collapse_republics.txt:5298` | Direct manpower plus XP, no helper/decision/map hook in reward. |
| `kaz_soviet_collapse_oil_field_protection_orders` | `005_soviet_collapse_republics.txt:10346` | Equipment plus random state building, no helper/decision/map hook in reward. |
| `PRA_armored_train_schools` | `005_soviet_collapse_custom_splinters.txt:1520` | Equipment, XP, command power, but no train/unit/template/decision hook in direct reward. |
| `NRF_living_harbor_committees` | `005_soviet_collapse_custom_splinters.txt:3411` | Equipment-only by heuristic, weak for a fleet identity branch. |
| `ICD_black_seal_requisitions` | `005_soviet_collapse_custom_splinters.txt:3970` | Equipment plus random state building, no direct helper/decision/unit hook. |
| `BSC_caravan_supply_hubs` | `005_soviet_collapse_custom_splinters.txt:4805` | One random state building, no helper/decision/map hook. |
| `CFR_construction_battalions` | `005_soviet_collapse_factory_successors.txt:671` | Manpower plus XP, weak for construction battalions. |
| `KZR_caspian_patrol_letters` | `005_soviet_collapse_ancient_restorations.txt:129` | XP-only by heuristic. |
| `KHW_canal_recognition_letters` | `005_soviet_collapse_ancient_restorations.txt:864` | Equipment plus random state building, no direct helper/decision/map hook. |

## Layout Red Flags

No exact duplicate focus coordinates were found.

Dense rows remain a readability risk. Worst clusters:

| Tree | Row | Evidence |
| --- | --- | --- |
| `soviet_collapse_kazakhstan_focus_tree` | `y = 3` | 11 focuses from `x = 5` through `x = 25`, including `kaz_soviet_collapse_the_steppe_cannot_be_encircled`, `kaz_soviet_collapse_oasis_and_steppe_congress`, and `kaz_soviet_collapse_oil_field_protection_orders`. |
| `FTH_soviet_collapse_focus_tree` | `y = 10` | 9 focuses from `x = 0` through `x = 16`, including `FTH_tachanka_front`, `FTH_extreme_gate`, and `FTH_hidden_workshop_cells`. |
| `soviet_collapse_baltic_focus_tree` | `y = 2` | 7 focuses from `x = 2` through `x = 14`. |
| `DHC_soviet_collapse_focus_tree` | `y = 6` | 7 focuses from `x = 4` through `x = 16`. |
| `KHC_soviet_collapse_focus_tree` | `y = 6` | 7 focuses from `x = 4` through `x = 16`. |

Mutual-exclusion midpoint/pathline suspects:

| Tree | Suspect |
| --- | --- |
| `soviet_collapse_ukraine_focus_tree` | `ukr_soviet_collapse_british_caution` is directly between same-row mutually exclusive `ukr_soviet_collapse_elections_under_shellfire` and `ukr_soviet_collapse_officers_above_parties`. |
| `soviet_collapse_ukraine_focus_tree` | `ukr_soviet_collapse_socialist_republic_without_moscow` is directly between same-row mutually exclusive `ukr_soviet_collapse_officers_above_parties` and `ukr_soviet_collapse_protectorate_debate`. |
| `soviet_collapse_internal_republic_focus_tree` | `internal_soviet_collapse_legal_autonomy_congress` sits below midpoint between `internal_soviet_collapse_security_council` and `internal_soviet_collapse_border_and_rail_liaisons`. |
| `soviet_collapse_central_asia_focus_tree` | `central_asia_soviet_collapse_turkestan_federation_road` sits below midpoint between `central_asia_soviet_collapse_local_republic_council` and `central_asia_soviet_collapse_military_border_authority`. |
| `soviet_collapse_kazakhstan_focus_tree` | `kaz_soviet_collapse_socialist_steppe_republic` sits below midpoint between `kaz_soviet_collapse_alash_memory_restored` and `kaz_soviet_collapse_resource_defense_directorate`. |
| `ARD_soviet_collapse_focus_tree` | `ARD_industry_plan` sits below midpoint between `ARD_settlement` and `ARD_radical_turn`. |
| `KZR/SOG/KHW/ALN ancient trees` | Charter focus sits below midpoint between symbolic and expansionist mutually exclusive siblings in all four 16-focus ancient trees. This may be intentional convergence, but the line geometry should be visually checked. |

## Icon Coverage

| Icon audit item | Status | Notes |
| --- | --- | --- |
| Missing icon assignment | Clean | 0 missing among 1698 focuses. |
| Unique icon ids | Partial | 1498 unique icon ids for 1698 focuses. |
| Reused icon ids | Needs art/wiring pass | 140 icon ids are reused. This was not patched because the parent constraint forbids asset/interface/gfx work. |
| Icons changed by this patch | None | `DHC_winter_road_columns` keeps `GFX_focus_DHC_winter_road_columns`. |

Most repeated icon ids found:

- `GFX_focus_soviet_collapse_guard_the_radio_stations`: 4 uses.
- `GFX_ukr_soviet_collapse_democratic`: 4 uses.
- `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`: 4 uses.
- `GFX_focus_soviet_collapse_steppe_supply_congress`: 4 uses.
- `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`: 4 uses.
- `GFX_moldova_soviet_collapse_ukrainian_corridor`: 4 uses.
- `GFX_focus_soviet_collapse_ancient_workshop_compact`: 4 uses.
- `GFX_focus_soviet_collapse_ancient_guard_old_routes`: 4 uses.

## Localisation and Reward Mismatch List

Localisation key presence is clean for the scoped files:

- Missing focus name localisation: 0.
- Missing focus description localisation: 0.
- Localisation changed by this patch: none.

Reward mismatch risks:

- `PRA_armored_train_schools` implies armored train schooling but direct reward is equipment, XP, and command power; no direct train/unit/template hook in the focus reward.
- `NRF_living_harbor_committees` and broader `NRF` branch names imply naval/fleet identity, but direct rewards lean on equipment/convoys and only 4 decision unlocks in earlier scoped counts.
- `CFR_construction_battalions` implies organized construction units but direct reward is manpower plus XP.
- Ancient restoration focus names imply restored polities and old claims, but each tree is 16 focuses and relies on shallow reward surfaces in several places.
- `DHC_winter_road_columns` mismatch was patched: it now has a mobile-column helper and recovery progress in addition to the road infrastructure.

## AI Behavior Gaps

- All 1698 focuses have `ai_will_do`; the gap is route-aware behavior, not missing blocks.
- Many `ai_will_do` blocks remain local base weights plus simple war/stability/pressure modifiers. Full rework should add or verify route-level AI strategy behavior for compact chaos splinters, `OGB`, factory successors, and ancient restorations.
- Aggressive chaos countries need AI that prefers expansion and special-route payoffs when viable. Direct focus rewards currently show only 11 war goals and 14 claim-granting focuses across all four files.
- Dense or convergent route layouts should be rechecked after AI route changes because OR prerequisites and hidden `available = { has_completed_focus = ... }` gates can make AI select confusing branches if prerequisites are widened without visible route locks.

## High-Priority Fixes First

1. Full route rework for `OGB_soviet_collapse_focus_tree`: add restoration decisions, Volga legitimacy pressure, heritage guard or unit hooks, old-border settlement, and aggressive AI behavior.
2. Compact chaos tree deepening for `TSC`, `DSC`, `NRF`, `ICD`, and the remaining 18-22 focus crisis trees. Prioritize mechanics and unit/decision hooks over more flat equipment.
3. Ancient restoration depth pass for `KZR/SOG/KHW/ALN`, or explicitly document them as compact crisis trees. If kept playable, they need more than 16 focuses each.
4. Replace the remaining shallow reward candidates with existing helpers, decision unlocks, staged claims/settlements, or unit/template hooks. Do not add direct idea stacks.
5. Layout pass for dense rows and the 10 midpoint suspects after the route design is settled.
6. Icon reuse pass only after asset/interface work is allowed again.

## Validation

Ran after the focus patch:

- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt`: passed.
- Brace balance on `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `final_brace_depth=0`, no negative lines.
- `rg -n '<=|>=' common/national_focus/005_soviet_collapse_custom_splinters.txt`: no matches.
- `git diff --name-only -- gfx/flags`: no output.
- Post-patch shallow heuristic with the same scanner: `DHC_winter_road_columns` no longer appears; candidate count changed from 32 to 31.

Skipped validation:

- No in-game validation was run.
- No localisation BOM validation was needed because no `.yml` files were edited.
- No icon definition or asset validation was run because the direct parent constraint forbids asset/gfx/interface edits.

## Remaining Route Risks

This is not a full focus-tree rework. The current state still has shallow rewards, compact trees that are too thin for major playable chaos countries, dense path geometry, repeated icon ids, and limited direct expansion/coring/unit payoff. The parent should treat this handoff as a current-state audit plus one narrow patch, not completion evidence for the full Soviet Collapse tree rework.

No separate broad improvement plan was added in this pass. Existing plan `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` remains aligned with the same full-rework gaps found here.
