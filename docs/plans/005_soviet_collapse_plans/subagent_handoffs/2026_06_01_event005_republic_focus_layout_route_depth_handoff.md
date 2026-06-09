# Event005 Soviet Collapse Republic Focus Layout Handoff

Scope: `common/national_focus/005_soviet_collapse_republics.txt` only.

Flag constraint: no `gfx/flags` path was read, inspected, edited, or touched.

Context note: the worktree already had uncommitted edits in the focus file before this pass. This handoff lists only the bounded layout/prerequisite edits made in this subagent pass.

## High-Priority Fixes Applied

| Priority | Focus id | Before | After | Reason |
| --- | --- | --- | --- | --- |
| High | `ukr_soviet_collapse_question_of_statehood` | One `prerequisite = { ... }` block with `guard_the_telegraph_house` and `seal_the_grain_ledgers`, making the requirement OR. | Two separate `prerequisite` blocks, making the requirement AND. | The focus is a statehood convergence point and was reachable after only one of the two setup focuses. |
| High | `ukr_soviet_collapse_black_sea_defense_staff` | `x = 23`, `y = 3`, one unit from `ukr_soviet_collapse_depot_motor_columns`. | `x = 20`, `y = 3`. | Removed same-row overlap/too-close spacing inside the Ukraine tree. |
| High | `blr_soviet_collapse_rail_war_state` | `x = 7`, `y = 8`, one unit from `blr_soviet_collapse_brest_is_not_a_gift`. | `x = 10`, `y = 8`. | Removed same-row overlap/too-close spacing inside the Belarus tree. |
| Medium | `blr_soviet_collapse_join_the_league_when_war_comes` | `x = 15`, `y = 9`, stacked on the central League pathline. | `x = 17`, `y = 9`. | Separated non-parent/child League focuses from the same vertical pathline. |
| Medium | `blr_soviet_collapse_prepare_league_freight_tables` | `x = 15`, `y = 10`, stacked on the central League pathline. | `x = 13`, `y = 10`. | Separated non-parent/child League focuses from the same vertical pathline. |
| Medium | `ukr_soviet_collapse_carpathian_security_belt` | `x = 29`, `y = 10`, one unit from `ukr_soviet_collapse_ports_need_soldiers`. | `x = 31`, `y = 10`. | Removed same-row overlap/too-close spacing inside the Ukraine tree. |
| Medium | `ukr_soviet_collapse_black_banner_takes_the_villages` | `x = 22`, `y = 13`, one unit from `ukr_soviet_collapse_appointed_governors`. | `x = 20`, `y = 13`. | Removed same-row overlap/too-close spacing inside the Ukraine tree. |
| Medium | `baltic_soviet_collapse_rail_to_the_ports` | `x = 7`, `y = 1`, one unit from `baltic_soviet_collapse_emergency_border_guard`. | `x = 9`, `y = 1`. | Removed same-row overlap/too-close spacing found during full per-tree scan. |
| Low | `ukr_soviet_collapse_depot_motor_columns`, `blr_soviet_collapse_timetable_state`, `baltic_soviet_collapse_emergency_border_guard` | Inconsistent leading tab indentation on focus body lines. | Normalized to surrounding one-tab focus-body style. | Style cleanup only; no behavior change. |

## Route Coverage Table

No external source spec was inspected in this one-file subagent scope, so required routes are inferred from focus-tree ids, branch comments, and implemented branch structure.

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine emergency/statehood trunk | `ukr_soviet_collapse_emergency_rada` to `ukr_soviet_collapse_question_of_statehood` | Patched | Statehood now requires both telegraph and grain setup focuses. |
| Ukraine political route family | Democratic, socialist, military, black-banner, protectorate route locks | Present | Lore-important mutual exclusions preserved; no decorative exclusions added. |
| Ukraine military/foreign/League/expansion/high-chaos lanes | Army, foreign liaison, League charter, Black Sea/steppe, bread-state branches | Present | Layout spacing patched where same-row focus distance was one unit. |
| Generic breakaway republic tree | Emergency government, route definition, survival, League/neutrality/depot branches | Present | No coordinate overlap found in per-tree scan. |
| Internal republic tree | Forest, Volga/Ural, Crimea, Siberian/Far East, old-name, survival branches | Present | No coordinate overlap found in per-tree scan. |
| Baltic republic tree | Legal state, foreign protection, defense compact, ports, country-specific lanes | Patched | One same-row spacing issue patched in the early branch. |
| Caucasus republic tree | Oil, mountain federal, national restoration, Black Sea/Caspian, defense, crown/federal endings | Present | No coordinate overlap found in per-tree scan. |
| Central Asia republic tree | Local council, military border, federation, Basmachi, oasis/cotton, Khwarazm/desert lanes | Present | No coordinate overlap found in per-tree scan. |
| Moldova republic tree | Romanian question, independent republic, Dniester defense, neutrality, river/Prut endings | Present | No coordinate overlap found in per-tree scan. |
| Belarus republic tree | Minsk trunk, rail, forest, corridor, route locks, League/high-chaos branches | Patched | Rail-war and League pathline spacing patched. |
| Kazakhstan republic tree | Congress, Alash/socialist/resource/military/federation/diplomacy/endurance branches | Present | No coordinate overlap found in per-tree scan. |

## Layout Audit Table

| Focus tree | Focus count | Focus x bounds | Focus y bounds | Continuous focus position | Layout result |
| --- | ---: | --- | --- | --- | --- |
| `soviet_collapse_ukraine_focus_tree` | 83 | 4-34 | 0-18 | `x = 3936`, about focus unit 41 | Patched; no duplicate or one-unit same-row spacing remains. |
| `soviet_collapse_breakaway_focus_tree` | 36 | 2-26 | 0-14 | `x = 2880`, about focus unit 30 | No duplicate or one-unit same-row spacing found. |
| `soviet_collapse_internal_republic_focus_tree` | 62 | 0-27 | 0-10 | `x = 3264`, about focus unit 34 | No duplicate or one-unit same-row spacing found. |
| `soviet_collapse_baltic_focus_tree` | 42 | 2-30 | 0-9 | `x = 3264`, about focus unit 34 | Patched; no duplicate or one-unit same-row spacing remains. |
| `soviet_collapse_caucasus_focus_tree` | 40 | 0-26 | 0-8 | `x = 2880`, about focus unit 30 | No duplicate or one-unit same-row spacing found. |
| `soviet_collapse_central_asia_focus_tree` | 45 | -2-24 | 0-11 | `x = 3264`, about focus unit 34 | No duplicate or one-unit same-row spacing found. |
| `soviet_collapse_moldova_focus_tree` | 48 | 2-26 | 0-13 | `x = 2880`, about focus unit 30 | No duplicate or one-unit same-row spacing found. |
| `soviet_collapse_belarus_focus_tree` | 53 | 3-29 | 0-16 | `x = 3264`, about focus unit 34 | Patched; no duplicate or one-unit same-row spacing remains. |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | 2-36 | 0-12 | `x = 3936`, about focus unit 41 | No duplicate or one-unit same-row spacing found. |

Continuous focus panel audit: no tree has its continuous focus panel at or inside the rightmost focus lane after this patch.

## Missing Or Simplified Content

| Area | Finding | Status |
| --- | --- | --- |
| Ukraine reward stack | `ukr_soviet_collapse_the_directory_state` still has a visible stack of three major helper/direct reward calls: `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_unlock_league_unit_deployment_decisions`, and `soviet_collapse_spawn_focus_mobile_column`, plus direct XP/command power/AI strategy effects. | Not patched. Replacing this cleanly would need an existing route package or a localised custom tooltip/helper outside this one-file scope. |
| Route depth | The file already contains deep branch families for each republic tree. | No broad route plan written; no shallow-route blocker found that fit this bounded layout pass. |
| Mutual exclusions | Ukraine and Belarus route locks use a mix of actual `mutually_exclusive` links and `available` hidden route guards. | Preserved. No mutual exclusions were added for decoration. |

## Icon Coverage Table

Icon audit was limited to icon assignments inside the focus file. Actual `.gfx` definition existence was not cross-checked because this pass was scoped to one file and the user explicitly forbade flag asset inspection.

| Focus tree | Missing icon assignments | Reused icon ids noted | Status |
| --- | ---: | --- | --- |
| `soviet_collapse_ukraine_focus_tree` | 0 | 4 reused ids, mostly thematic democratic/industry/expansion pairs | Acceptable for this pass; no icon ids changed. |
| `soviet_collapse_breakaway_focus_tree` | 0 | 2 reused ids | Acceptable for this pass. |
| `soviet_collapse_internal_republic_focus_tree` | 0 | 3 reused ids | Acceptable for this pass. |
| `soviet_collapse_baltic_focus_tree` | 0 | 3 reused ids | Acceptable for this pass. |
| `soviet_collapse_caucasus_focus_tree` | 0 | 2 reused ids | Acceptable for this pass. |
| `soviet_collapse_central_asia_focus_tree` | 0 | 2 reused ids | Acceptable for this pass. |
| `soviet_collapse_moldova_focus_tree` | 0 | 2 reused ids | Acceptable for this pass. |
| `soviet_collapse_belarus_focus_tree` | 0 | 2 reused ids: socialist and counterintelligence themes | Acceptable for this pass. |
| `soviet_collapse_kazakhstan_focus_tree` | 0 | 0 reused ids | Clean in-file icon assignment audit. |

## Localisation And Reward Mismatch List

| Area | Finding | Status |
| --- | --- | --- |
| Localisation keys | No focus ids were renamed and no new player-facing keys were added. | No localisation edits needed from this patch. |
| Localisation cross-check | Localisation files were not inspected due the one-file task scope. | Skipped; parent can run a localisation-specific audit if required. |
| Reward/name mismatch | No obvious focus-name-to-reward mismatch was found in the edited focuses. | No reward edits made. |
| Reward helper clutter | One Ukraine finisher remains helper-heavy as noted above. | Remaining risk. |

## AI Behavior Gaps

| Audit item | Result |
| --- | --- |
| Missing `ai_will_do` blocks | None found across 501 focus blocks in this file. |
| Route-aware AI | Many route and pressure checks already exist. This pass did not redesign AI because the request was layout/prereq bounded. |
| Changed AI behavior | None directly, except `ukr_soviet_collapse_question_of_statehood` now waits for both prerequisite setup focuses. |

## Changed Files

| File | Change type |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Layout/prerequisite/indentation patch only. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_01_event005_republic_focus_layout_route_depth_handoff.md` | This handoff. |

## Changed Focus IDs

| Focus id | Changed coordinates/prerequisites/rewards |
| --- | --- |
| `ukr_soviet_collapse_question_of_statehood` | Prerequisites changed from OR block to two AND prerequisite blocks. |
| `ukr_soviet_collapse_black_sea_defense_staff` | `x = 23` to `x = 20`. |
| `ukr_soviet_collapse_depot_motor_columns` | Indentation normalized on the `x = 22` line only. |
| `ukr_soviet_collapse_carpathian_security_belt` | `x = 29` to `x = 31`. |
| `ukr_soviet_collapse_black_banner_takes_the_villages` | `x = 22` to `x = 20`. |
| `blr_soviet_collapse_timetable_state` | Focus block indentation normalized only. |
| `blr_soviet_collapse_rail_war_state` | `x = 7` to `x = 10`. |
| `blr_soviet_collapse_prepare_league_freight_tables` | `x = 15` to `x = 13`. |
| `blr_soviet_collapse_join_the_league_when_war_comes` | `x = 15` to `x = 17`. |
| `baltic_soviet_collapse_emergency_border_guard` | Indentation normalized on the `x = 6` line only. |
| `baltic_soviet_collapse_rail_to_the_ports` | `x = 7` to `x = 9`. |

Rewards changed by this subagent: none.

Localisation keys changed: none.

Icon ids changed: none.

## Route Behavior Before And After

| Area | Before | After |
| --- | --- | --- |
| Ukraine statehood convergence | `ukr_soviet_collapse_question_of_statehood` could be taken after either the telegraph guard or grain ledger focus. | It requires both focuses, matching convergence semantics and avoiding an early partial-setup route unlock. |
| Ukraine layout | Several branches had same-row one-unit spacing, risking overlapping focus icons/pathlines. | Patched same-row spacing in the Black Sea, Carpathian, and black-banner/governor-adjacent lanes. |
| Belarus layout | Rail-war focus sat one unit from Brest focus; League branch stacked several unrelated focuses at `x = 15`. | Rail-war moved apart; League join/preparation focuses now use separate lanes. |
| Baltic layout | `rail_to_the_ports` sat one unit from `emergency_border_guard`. | Port rail lane moved right. |

## Validation Run

| Check | Result |
| --- | --- |
| Brace-depth check for `common/national_focus/005_soviet_collapse_republics.txt` | Passed: final depth 0, minimum depth 0, no negative depth events. |
| `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt` | Passed with no output. |
| `rg -n '<=|>=' common/national_focus/005_soviet_collapse_republics.txt` | Passed: no matches. |
| `git diff --name-only -- gfx/flags` | Passed: empty output. |
| Per-tree coordinate scan | Passed after patch: no duplicate coordinates and no one-unit same-row spacing remain. |

## Skipped Validation

| Check | Reason |
| --- | --- |
| In-game load test | Not available in this subagent pass. |
| Focus localisation file audit | One-file scope; no focus ids renamed or added. |
| `.gfx` sprite definition audit | One-file scope, and no icon ids changed. |
| Flag asset audit | Explicitly forbidden by the user. |

## Remaining Route Risks

1. `ukr_soviet_collapse_the_directory_state` remains reward-dense and may still produce visible effect clutter unless an existing package/helper or localised tooltip is introduced outside this one-file scope.
2. Several icon ids are intentionally reused inside thematic route families. No missing icon assignments were found in-file, but sprite definition existence was not checked.
3. The file has many pre-existing uncommitted changes unrelated to this subagent pass; parent review should distinguish this patch from earlier dirty-worktree edits.
