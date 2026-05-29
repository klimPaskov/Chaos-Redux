# Soviet Collapse Focus Full Audit Handoff

Subagent: Chaos Redux focus tree subagent  
Date: 2026-05-29 18:48 UTC  
Scope: four Soviet Collapse focus files plus this handoff.  

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla references: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `loc_formatter_documentation.md`, `loc_objects_documentation.md`, and `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`.
- Soviet Collapse spec: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`.

## Changed Files

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_184838_focus_full_audit_handoff.md`

No localisation keys or icon ids were changed.

## Changed Focus IDs

| Focus id | File | Before | After | Reason |
|---|---|---|---|---|
| `ukr_soviet_collapse_army_supremacy` | `005_soviet_collapse_republics.txt` | `x = 19`, `y = 6` | `x = 19`, `y = 7` | The line from `ukr_soviet_collapse_the_commander_or_the_cabinet` crossed `ukr_soviet_collapse_socialist_republic_without_moscow` and `ukr_soviet_collapse_republic_of_laws`. |
| `moldova_soviet_collapse_republic_of_crossings` | `005_soviet_collapse_republics.txt` | `x = 19`, `y = 12` | `x = 21`, `y = 12` | The line from `moldova_soviet_collapse_river_command_reserve` crossed `moldova_soviet_collapse_eastern_buffer_missions`; intermediate move was adjusted to avoid `moldova_soviet_collapse_southern_rail_timetables`. |
| `blr_soviet_collapse_foreign_corridor_administration` | `005_soviet_collapse_republics.txt` | `x = 22`, `y = 6` | `x = 23`, `y = 6` | The line from `blr_soviet_collapse_which_road_is_belarus` crossed `blr_soviet_collapse_state_between_armies`. |
| `kaz_soviet_collapse_the_steppe_keeps_many_memories` | `005_soviet_collapse_republics.txt` | `x = 32`, `y = 7` | `x = 33`, `y = 7` | Lines from `kaz_soviet_collapse_the_written_alash_program` and `kaz_soviet_collapse_crush_the_road_militias` crossed sibling focuses. |
| `MFR_rifles_for_the_league` | `005_soviet_collapse_factory_successors.txt` | `x = 24`, `y = 8` | `x = 25`, `y = 9` | The line from `MFR_quota_above_life` crossed `MFR_arms_for_recognition`; final x shift avoids duplicating `MFR_german_orders`. |

## Route Behavior Before And After

Before: six straight prerequisite pathlines passed through unrelated focus nodes, making route lanes look crossed or semantically connected when they were not.  
After: the same prerequisites and route locks remain intact, but the affected child nodes are offset so the audit finds zero pathline-through-focus cases. No rewards, prerequisites, mutual exclusions, AI weights, icons, or localisation were changed.

## Quantified Audit Summary

| Metric | Count |
|---|---:|
| Focus trees audited | 41 |
| Focuses audited | 1698 |
| Direct `add_ideas` occurrences in focus files | 0 |
| Direct repeated `add_ideas` within one focus | 0 |
| Missing `ai_will_do` blocks | 0 |
| Missing icon assignments | 0 |
| Missing focus localisation title/desc pairs | 327 focuses |
| Duplicate focus ids | 0 |
| Duplicate x/y coordinate groups after patch | 0 |
| Same-row mutually-exclusive lines with middle nodes after patch | 0 |
| Pathline-through-focus cases before patch | 6 |
| Pathline-through-focus cases after patch | 0 |
| Unsupported `<=` or `>=` operators in audited focus files | 0 |

## Route Coverage Table

The spec requires distinct political, industry, and expansion branches. This table uses focus filters as a first-pass route signal, then flags trees that need manual route-depth review.

| Tree | Focuses | Political filters | Industry filters | Expansion filters | Status |
|---|---:|---:|---:|---:|---|
| `soviet_collapse_ukraine_focus_tree` | 83 | 58 | 18 | 0 | Missing visible expansion filter; route rewards need manual expansion audit. |
| `soviet_collapse_breakaway_focus_tree` | 36 | 23 | 9 | 0 | Missing visible expansion filter. |
| `soviet_collapse_internal_republic_focus_tree` | 62 | 33 | 24 | 0 | Missing visible expansion filter. |
| `soviet_collapse_baltic_focus_tree` | 42 | 28 | 9 | 0 | Missing visible expansion filter and full localisation. |
| `soviet_collapse_caucasus_focus_tree` | 40 | 28 | 13 | 0 | Missing visible expansion filter and full localisation. |
| `soviet_collapse_central_asia_focus_tree` | 45 | 32 | 9 | 0 | Missing visible expansion filter and full localisation. |
| `soviet_collapse_moldova_focus_tree` | 48 | 35 | 12 | 0 | Missing visible expansion filter and full localisation. |
| `soviet_collapse_belarus_focus_tree` | 53 | 34 | 22 | 0 | Missing visible expansion filter and full localisation. |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | 54 | 26 | 0 | Missing visible expansion filter and full localisation. |
| Custom 47-focus splinters | 19 trees | Present | Present | Mostly 0 | Need manual expansion reward review; many rely on helper-led identity nodes. |
| Crisis splinters `PRA/TSC/RMC/DSC/NRF/ICD` | 18-22 each | Present | Present | 1-3 | Shallow/crisis-depth trees, not full major depth. |
| `CFR_soviet_collapse_focus_tree` | 47 | 34 | 30 | 3 | Present but helper-heavy. |
| `OGB_soviet_collapse_focus_tree` | 23 | 17 | 6 | 3 | Shallow for a high-chaos successor. |
| `MFR_soviet_collapse_focus_tree` | 58 | 42 | 38 | 1 | Present but expansion route is thin. |
| Ancient restoration trees `KZR/SOG/KHW/ALN` | 16 each | Present | 2-3 | 5 | Too shallow for ancient-restoration identity depth. |

## Worst 10 Trees Or Routes By Shallow Reward Pattern

Columns: focus count, focuses without an obvious concrete reward token, focuses with generic rewards, helper-only/no-concrete count.

| Tree | Focuses | No concrete token | Generic reward | Helper-only/no-concrete |
|---|---:|---:|---:|---:|
| `OGB_soviet_collapse_focus_tree` | 23 | 16 | 15 | 4 |
| `RMC_soviet_collapse_focus_tree` | 18 | 12 | 12 | 9 |
| `ICD_soviet_collapse_focus_tree` | 18 | 12 | 12 | 10 |
| `TSC_soviet_collapse_focus_tree` | 18 | 13 | 10 | 10 |
| `NRF_soviet_collapse_focus_tree` | 18 | 8 | 14 | 7 |
| `DSC_soviet_collapse_focus_tree` | 18 | 8 | 13 | 7 |
| `KZR_soviet_collapse_ancient_focus_tree` | 16 | 10 | 7 | 9 |
| `SOG_soviet_collapse_ancient_focus_tree` | 16 | 9 | 7 | 9 |
| `PRA_soviet_collapse_focus_tree` | 22 | 7 | 14 | 7 |
| `KHW_soviet_collapse_ancient_focus_tree` | 16 | 9 | 6 | 9 |

Also high priority despite larger size: `soviet_collapse_ukraine_focus_tree`, `soviet_collapse_belarus_focus_tree`, `UDC_soviet_collapse_focus_tree`, and `GAC_soviet_collapse_focus_tree` score poorly because many rewards are helper-only or generic and route payoffs are hard to inspect from the focus surface.

## Generic Helper Overuse

Most common helper calls across focus rewards:

| Helper | Calls |
|---|---:|
| `soviet_collapse_apply_focus_legal_recognition` | 305 |
| `soviet_collapse_apply_focus_depot_and_supply_control` | 257 |
| `soviet_collapse_apply_focus_military_consolidation` | 252 |
| `soviet_collapse_apply_focus_league_preparation` | 220 |
| `soviet_collapse_apply_focus_foreign_channel` | 176 |
| `soviet_collapse_apply_focus_high_chaos_identity` | 96 |

These helpers are useful, but the current volume makes many focus rewards read as repeated identity increments unless paired with visible decisions, buildings, units, claims, cores, war goals, events, leaders, laws, or route-specific unlocks.

## Icon Coverage Table

| Tree group | Icon status |
|---|---|
| All 41 trees | Every focus has an icon assignment. |
| Full unique icon coverage | `soviet_collapse_kazakhstan_focus_tree`, `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, `UDC`, `SDZ`, `GAC`, `OGB`, `MFR`, `KZR`, `SOG`, `KHW`, `ALN`. |
| Worst reuse | `IUL` 24/47 unique, `UWD` 28/47, `MRC` 31/47, `FEV` 32/47, `SZA` 32/47, `CFR` 32/47. |
| Moderate reuse | Ukraine 76/83, breakaway 34/36, internal republic 56/62, Baltic 37/42, Caucasus 37/40, Central Asia 39/45, Moldova 43/48, Belarus 51/53, most custom splinters 44/47. |

## Localisation And Reward Mismatch List

Missing focus localisation is concentrated in `005_soviet_collapse_republics.txt`:

| Tree | Missing focus title/desc pairs |
|---|---:|
| `soviet_collapse_ukraine_focus_tree` | 7 |
| `soviet_collapse_baltic_focus_tree` | 42 |
| `soviet_collapse_caucasus_focus_tree` | 40 |
| `soviet_collapse_central_asia_focus_tree` | 45 |
| `soviet_collapse_moldova_focus_tree` | 48 |
| `soviet_collapse_belarus_focus_tree` | 53 |
| `soviet_collapse_kazakhstan_focus_tree` | 92 |

Ukraine missing keys: `ukr_soviet_collapse_emergency_rada`, `ukr_soviet_collapse_seal_the_grain_ledgers`, `ukr_soviet_collapse_count_the_depot_keys`, `ukr_soviet_collapse_first_republican_line`, `ukr_soviet_collapse_moscows_officers_in_our_barracks`, `ukr_soviet_collapse_open_the_liaison_offices`, `ukr_soviet_collapse_army_of_the_republic`.

No localisation files were patched because adding 327 focus strings is outside the bounded small-patch scope and risks tone drift across multiple large route families.

Reward mismatch risk: focus titles frequently imply concrete programs, but many rewards are helper-only or generic. The parent should manually review the worst 10 list first, then Ukraine, Belarus, UDC, and GAC.

## AI Behavior Gaps

- Every audited focus has `ai_will_do`.
- Many AI blocks are simple `base = N` or route pressure multipliers. This is valid script, but not enough for the user objective that chaos countries be extremely strong and aggressive.
- Expansion behavior is uneven. Some endpoints add `add_ai_strategy = { type = conquer ... }`, but many trees have no visible `FOCUS_FILTER_ANNEXATION` and no obvious conquest/claim/war-goal focus lane.
- Parent should add route-aware AI plans for OP/chaos countries: aggressive conquest, anti-SOV antagonism, war-prep priority, League/faction logic, and invalid-route zeroing where sponsors, enemies, or target regions do not exist.

## High-Priority Fixes For Parent

1. Add localisation for the 327 missing republic focus titles/descriptions, preserving route tone and matching actual rewards.
2. Give every major tree a visible expansion route or clearly documented equivalent with claims, cores, war goals, protectorates, regional leagues, postwar integration, or diplomacy reactions.
3. Replace helper-only reward ladders in the worst 10 trees with concrete gameplay: decisions, missions, buildings, units, claims, cores, wargoals, events, advisors, laws, or mechanic unlocks.
4. Deepen `OGB` and the four ancient restoration trees; current 16-23 focus depth is too shallow for the requested high-chaos/ancient identity.
5. Review icon reuse in `IUL`, `UWD`, `MRC`, `FEV`, `SZA`, and `CFR`.
6. Add aggressive route-aware AI behavior for chaos countries and route endpoints, especially when focus rewards imply expansion or regional dominance.

## Validation Run

- Parser audit over all four focus files:
  - `focuses 1698`
  - `missing_ai 0`
  - `missing_icon 0`
  - `coord_dup_groups 0`
  - `same_row_mut_middle 0`
  - `path_through_focus 0`
- Brace depth check:
  - all four audited focus files ended at `brace_depth 0`, `min_depth 0`.
- Unsupported operator check:
  - `rg -n "<=|>=" ...` returned no matches.

## Skipped Validation

- No in-game launch or focus tree screenshot pass was run in this subagent scope.
- No scripted effect expansion or decision validation was run; the task allowed only bounded focus/localisation/helper docs edits and parent owns broad redesign.
- No localisation patch validation was run because localisation was audited but not changed.

## Remaining Route Risks

- The route-depth goal is not complete. This pass only fixed obvious layout pathlines and quantified the remaining work.
- Missing localisation is a major blocker for seven republic/shared republic trees.
- Many trees technically have political and industry filters but lack a clearly visible expansion branch.
- Helper-heavy rewards make it hard to prove that focus names/descriptions match actual gameplay without a deeper manual route pass.
- Current chaos-country aggression is not strong enough to satisfy the user objective across all routes.

## Plan Handoff

Existing broad redesign plan remains the correct parent handoff path:

`docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`

No new broad plan was written in this pass.
