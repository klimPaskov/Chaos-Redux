# Event 005 Soviet Collapse Focus Tree Audit and Layout Patch Handoff

Timestamp: 2026-05-30 11:26:55 UTC

Subagent role: Chaos Redux focus tree audit subagent

Scope audited:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

References read:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki core pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `common/script_constants/documentation.md`
- Vanilla focus precedent: `common/national_focus/generic.txt`, `common/national_focus/soviet.txt`
- Event source spec: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`
- Current redesign follow-up: `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`

## Files Changed

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Moved `ukr_soviet_collapse_black_banner_compact` from `x = 31` to `x = 36`, keeping `y = 8`, to clear the only current same-row focus spacing collision found by the coordinate audit. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_112655_event005_focus_tree_audit_layout_patch_handoff.md` | This handoff. |

Changed focus ids:

- `ukr_soviet_collapse_black_banner_compact`

Localisation keys changed: none.

Icon ids changed: none.

Route behavior before and after:

- Before: `ukr_soviet_collapse_black_banner_compact` was on row `y = 8` at `x = 31`, one x-unit from `ukr_soviet_collapse_anatolian_grain_mission` at `x = 30`, creating a tight same-row placement in the already crowded Ukraine tree.
- After: `ukr_soviet_collapse_black_banner_compact` remains the same route-lock focus, with the same prerequisites, mutual exclusions, availability, rewards, icon, AI weights, and localisation. Only its x-coordinate changed to `x = 36`.

## Route Coverage Table

| Required route or branch family | Implemented route or focus branch | Status | Evidence and notes |
| --- | --- | --- | --- |
| Ukraine political routes | Socialist, black banner, democratic, military, foreign-authority route locks around `ukr_soviet_collapse_question_of_statehood` | Partial | The routes exist and have mutual exclusions, but the selector layout remains visually awkward and political route consequences are uneven. `ukr_soviet_collapse_black_banner_compact` still needs a broader route layout pass beyond the small spacing patch. |
| Ukraine industry | Grain, Dnieper workshops, Black Sea port, arsenal and factory branches | Partial | Branches exist, but only 6 Ukraine focuses contain direct map-building effects and several industry rewards still rely on generic helper/value changes. |
| Ukraine military and expansion | Army, Black Sea, western border, League, Bread Host/high-chaos end states | Partial | Expansion and military branches exist, but the tree has no direct `create_wargoal`, `add_state_claim`, or `add_state_core` in the focus file. It depends on helper effects and decision unlocks, so the parent should verify those helpers produce the promised map pressure. |
| Belarus political routes | National council, socialist autonomy, military transit directorate, foreign corridor administration | Partial | Routes exist, but there are still hidden `has_completed_focus` route checks in availability and the route payoff is weighted toward rail/depot helper effects. |
| Belarus industry and rail | `blr_soviet_collapse_timetable_state`, freight, Minsk dispatch, armored train, League depot | Partial | Mechanic anchors exist, but only 6 Belarus focuses contain direct map-building effects. The branch still needs a spacing and pathline screenshot pass because route convergence is dense around rows 8-11. |
| Kazakhstan major tree | Alash/socialist/resource directorate, southern shield, steppe congress, military, diplomacy, industry | Mostly present | 92 focuses, strong route count and broad branch coverage. Remaining risk is helper-dependent payoff verification rather than tree absence. |
| Shared republic trees | Breakaway, internal republic, Baltic, Caucasus, Central Asia, Moldova | Partial | All have multiple branch families, but several route locks and end-state gates are driven by hidden completed-focus checks and repeated icon families. |
| Custom splinter full trees | FTH, BSC, TNC, ALA, BBH, KRS, UDC, SDZ, GAC, DHC, KHC, FEV, SZA, UWD, MRC, IUL, BAC, ARD, NLC | Partial | Most are 47-focus trees, but many are template-like. Several have no direct decision unlocks and too many rewards are generic equipment/building/value packages. |
| Custom crisis splinters | PRA, TSC, RMC, DSC, NRF, ICD | Partial | 18-22 focus trees are intentionally compact, but violent chaos actors still need a parent pass to confirm war goals, claims/cores, dangerous units, and mechanics are sufficiently OP. DSC/NRF have some war goals; TSC/RMC/ICD remain more limited. |
| Factory successors | CFR, OGB, MFR | Partial | CFR and MFR have larger trees, but OGB remains a 23-focus narrow successor. Construction/factory actors have strong factory/production branches, but route specialization still needs review against the OP identity requirement. |
| Ancient restorations | KZR, SOG, KHW, ALN | Incomplete for major-tree standard | Each has 16 focuses. They have claims and some decisions/buildings, but not enough depth for identity-driven long-lived countries unless parent explicitly classifies them as compact restorations. |

## Missing or Simplified Content

- Ukraine is still the highest-risk layout target. The current tree has 83 focuses and many branches, but the route selectors are spread across the same visual field as later military, industry, and diplomacy branches. The patch fixed only the exact same-row spacing collision; it did not redesign Ukraine.
- Belarus has real branch content, but rows around `blr_soviet_collapse_join_the_league_when_war_comes`, `blr_soviet_collapse_prepare_league_freight_tables`, `blr_soviet_collapse_partisans_or_army`, and `blr_soviet_collapse_the_league_depot_at_minsk` remain dense and should be checked in-game or via screenshot after parent movement.
- `OGB_soviet_collapse_focus_tree` has only 23 focuses and should be either expanded or explicitly documented as a narrower restoration actor.
- Ancient restoration trees have only 16 focuses each: `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, `ALN_soviet_collapse_ancient_focus_tree`.
- Most full custom splinter trees have branch families by count, but several still look template-like by reward structure and icon repetition. They need a design pass that makes each country identity visibly change gameplay.
- Direct map aggression is uneven. Across the focus files, several trees depend on helper effects instead of visible direct focus-level `create_wargoal`, `add_state_claim`, or `add_state_core` entries. The parent should verify helper effects and decision unlocks provide the promised OP expansion behavior.
- Violent chaos actors such as `DSC`, `NRF`, `ICD`, and similar compact trees still need a parent pass for dangerous units, recurring pressure, claims/cores/wargoals, and postwar handling.

## Icon Coverage Table

| File | Focuses | Unique icon ids | Repeated icon groups | Missing sprite defs |
| --- | ---: | ---: | ---: | ---: |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 64 | 42 | 8 | 0 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 1005 | 885 | 99 | 0 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 128 | 113 | 11 | 0 |
| `common/national_focus/005_soviet_collapse_republics.txt` | 501 | 458 | 22 | 0 |

High-priority repeated icon clusters:

- Ukraine: `GFX_ukr_soviet_collapse_democratic` is used by 4 focuses; `GFX_ukr_soviet_collapse_industry` by 3 focuses.
- Belarus: `GFX_blr_soviet_collapse_counterintel` and `GFX_blr_soviet_collapse_socialist` each repeat.
- Factory successors: CFR has 11 repeated icon groups, including several 3-use clusters for construction/governance icons.
- Custom splinters: FEV, SZA, UWD, MRC, and IUL have the largest repeated-icon clusters and should be prioritized for icon identity cleanup.

## Localisation and Reward Mismatch List

- Mechanical localisation audit result: 1,698 focus ids checked, 0 missing name keys, 0 missing `_desc` keys.
- No localisation keys were changed by this patch.
- Remaining mismatch risk is qualitative, not missing-key mechanical failure:
  - Some focus names promise map-changing or actor-defining behavior while the file shows only helper/value rewards. Parent should verify helper effects for Ukraine expansion, Belarus rail authority, and violent chaos successor endpoints.
  - Several custom splinter trees repeat generic support equipment, convoy, and small resource/trickle patterns. ARD is the clearest example: 13 focuses still match tiny reward patterns in the current audit.
  - Ancient restoration focus text appears more ambitious than the 16-focus branch depth can support.

## AI Behavior Gaps

- Mechanical audit: every focus in the four files has an `ai_will_do` block.
- Remaining AI gaps are route-quality gaps:
  - Many `ai_will_do` blocks use simple base weights or one/two scalar modifiers. They do not always reflect route validity, war state, foreign appetite, existing faction membership, sponsor presence, or current regional targets.
  - Ukraine routes have some AI modifiers but need route-family behavior so the AI deliberately chooses socialist, democratic, military, foreign-authority, or black-banner futures based on campaign state.
  - Belarus should weight neutrality, rail-war state, forest defense, and League freight behavior by threat, existing League membership, SOV condition, and corridor pressure.
  - Violent chaos tags should aggressively prefer war/expansion branches when valid instead of drifting through normal stabilization branches.

## High-Priority Fixes First

1. Ukraine broad layout pass. Move route selectors and downstream branch starts into clean columns so no route line crosses through unrelated mutually exclusive choices or late-branch content. Re-run the same-row spacing and pathline visual check after movement.
2. Ukraine reward/helper proof pass. For `ukr_soviet_collapse_direct_national_claims`, `ukr_soviet_collapse_black_sea_hegemony`, `ukr_soviet_collapse_breadbasket_empire`, `ukr_soviet_collapse_great_steppe_and_sea_plan`, and black-banner endpoints, verify helpers grant claims, cores, decisions, units, or wargoals matching the names.
3. Belarus pathline pass. Focus on the rail/freight/forest convergence around rows 8-15 and route locks for national council/socialist/military/foreign corridor choices.
4. OGB and ancient restorations depth plan. Either expand OGB/KZR/SOG/KHW/ALN or explicitly classify them as compact restoration trees with narrower expectations.
5. Custom splinter reward identity pass. Prioritize `ARD`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, and compact violent actors. Replace repeated tiny equipment/convoy rewards with route-specific decisions, units, claims, war goals, map buildings, or mechanics.
6. Icon identity pass. Repeated icon clusters are mechanically wired, but the spec asks for unique icon assignments. Replace the largest repeated groups first.

## Validation Run

Commands run from `/home/klim/projects/chaos_redux`:

- Brace depth and duplicate id audit over `common/national_focus/005_soviet_collapse_*.txt`
  - Result: all four files ended at brace depth 0; duplicate ids: 0.
- Focus localisation and icon audit
  - Result: focus count 1,698; missing focus names 0; missing focus descriptions 0; icons used 1,698; unique icons 1,498; missing sprite definitions 0.
- Unsupported operator grep
  - Command checked `<=` and `>=` in the four focus files.
  - Result: no matches.
- Same-row spacing audit after patch
  - Result: `same_row_spacing_le_1 0`.

Skipped validation:

- No in-game load or screenshot validation was run in this subagent environment.
- No commit was created because the repository already contains a large dirty parent worktree across Event 005 and Event 006. This handoff isolates the subagent's touched id and validation instead of bundling unrelated parent changes.

## Remaining Route Risks

- The Ukraine tree still needs major route layout/depth attention. The patch only removed one coordinate collision.
- Belarus spacing likely needs visual screenshot review even though same-row mechanical spacing is clean.
- Several broad content gaps require parent ownership or an improvement-loop plan, not a subagent-local patch.
- Because the worktree was dirty before this pass, `git diff` includes many pre-existing parent changes in `common/national_focus/005_soviet_collapse_republics.txt`; this subagent only intentionally changed `ukr_soviet_collapse_black_banner_compact` coordinate `x = 31` to `x = 36`.

## Prioritized Patch Plan for Parent

1. Run a dedicated Ukraine route layout pass with all route selectors and endpoint branches visible at once.
2. Audit helper effects called by Ukraine and Belarus focus rewards for actual decision, claim, core, wargoal, faction, unit, and map-building payoffs.
3. Expand or formally scope down OGB and the four ancient restoration trees.
4. Replace remaining tiny repeated equipment/convoy reward clusters in custom splinters, starting with ARD and the compact violent actors.
5. Replace repeated icon groups with unique variants or rename focus ids to existing more specific icon ids where the intended sprite already exists.
