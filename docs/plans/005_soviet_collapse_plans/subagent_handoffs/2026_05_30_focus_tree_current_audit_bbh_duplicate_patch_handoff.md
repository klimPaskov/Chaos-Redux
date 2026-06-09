# Event 005 Soviet Collapse Focus Tree Current Audit and BBH Duplicate Reward Patch

Date: 2026-05-30
Agent role: Chaos Redux focus tree subagent
Scope: focus tree audit with one bounded focus-file patch

## Scope and Constraints

- Audited primary focus files:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Read-only evidence checked outside focus files:
  - `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`
  - `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`
  - `common/scripted_effects/005_soviet_collapse_effects.txt` for indirect idea-spam evidence only
  - `interface/*.gfx`, vanilla `interface/*.gfx`, and `localisation/**/*.yml` for icon/localisation evidence only
- Explicit flag constraint followed: no `gfx/flags` files or flag artwork were opened, touched, or modified.
- Existing dirty worktree was present before this pass in the three focus files listed by `git status`; this pass did not revert or normalize those unrelated changes.

## Patch Made

| File | Focus id | Change | Before | After |
| --- | --- | --- | --- | --- |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt:8178` | `BBH_column_schools` | Removed one duplicate direct `support_equipment_1` grant. | The focus granted `support_equipment_1` twice in the same `completion_reward`, then called `soviet_collapse_apply_focus_military_consolidation = yes`. | The focus grants the larger `support_equipment` amount once, keeps doctrine reduction, infrastructure, and military helper behavior. |

Changed files from this subagent:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- This handoff file.

Changed focus ids:

- `BBH_column_schools`

Localisation keys changed: none.

Icon ids changed: none.

Route behavior before and after:

- Before: `BBH_column_schools` had repeated visible support-equipment stockpile output with no additional route meaning.
- After: the Black Banner Host column-school branch keeps its military reward and doctrine payoff, but no longer repeats the same equipment type directly in one focus reward.

## Current Counts

| File | Trees | Focuses |
| --- | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 9 | 501 |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1005 |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 |
| `005_soviet_collapse_ancient_restorations.txt` | 4 | 64 |
| Total audited | 41 | 1698 |

## Route Coverage Table

| Required route family from spec | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Political branch for all playable/long-lived tags | Present in all audited trees by focus filters and route selectors. | Partial | All trees have political focuses, but several still use flat AI and generic variable/helper payoffs rather than visible leader, law, advisor, or government identity changes. Key risks: republic shared trees, `OGB_soviet_collapse_focus_tree`, ancient restorations. |
| Industry branch | Present in all audited trees. | Partial | Industry exists, but many branches are direct factories, infrastructure, rail, or equipment without a distinct route mechanic. Factory successors are strongest; ancient restorations and crisis splinters are weakest. |
| Military branch | Present in all audited trees. | Partial | `NRF_soviet_collapse_focus_tree` has only 1 focus with `FOCUS_FILTER_ARMY_XP`; it is naval-themed but still thin as a military branch. `CFR_soviet_collapse_focus_tree` has only 6 military-filtered focuses. |
| Diplomacy branch | Present in many custom/republic trees through recognition, League, foreign channel, and liaison rewards. | Partial | No dedicated diplomacy filter exists, so evidence is through focus names, `soviet_collapse_apply_focus_foreign_channel`, recognition variables, and decision hooks. Many 47-focus custom trees have no direct decision hooks, making diplomacy feel helper-driven. |
| Expansion, settlement, reunification, or regional ambition | Strongest in `CFR`, `OGB`, ancient restorations, and high-chaos crisis trees; weak or hidden in many republic/custom trees. | Weak | Expansion filter count is 0 in all republic trees and most 47-focus custom splinter trees. Direct claims/war-goal foci exist mainly in `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, `CFR`, `OGB`, `MFR`, and ancient restorations. |
| Special mechanic branch | Present through Soviet Collapse variables and helpers. | Partial | Helpers update recovery, recognition, depot control, League support, local authority, and custom-splinter identity values, but many focus branches do not expose a clear visible mechanic loop. |
| Late-game/endgame payoff | Present by endgame focuses and `soviet_collapse_complete_*_endgame` helpers. | Partial | Endgame hooks exist, but several countries still reach them through shallow or generic reward ladders. |
| AI behavior | Every focus has `ai_will_do`. | Partial | 351 of 1698 focuses have flat base-only AI. Kazakhstan has 61 flat AI focuses; ancient restorations have 12 flat AI focuses per tree. |

## Missing or Simplified Content

High priority first:

1. `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `PRA_soviet_collapse_focus_tree`
   - `DSC` and `NRF` remain 18-focus crisis trees; `PRA` is 22 focuses.
   - They have route flavor and some claims/decision hooks, but do not meet the full political, industrial, military, diplomacy, expansion, mechanic, and late-game depth standard for strong chaos countries.
   - `NRF` remains especially reward-heavy: 13 direct equipment-stockpile lines across 18 focuses, and only 1 army-filtered focus.

2. `common/national_focus/005_soviet_collapse_factory_successors.txt`: `OGB_soviet_collapse_focus_tree`
   - 23 focuses, with political, industry, military, and expansion elements present.
   - Still shallow for an OP successor: only 1 decision hook, 3 building foci, and 1 direct equipment focus. It needs a broader Volga restoration mechanic or a documented narrow classification.

3. `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: `KZR`, `SOG`, `KHW`, `ALN`
   - Each has 16 focuses.
   - They contain political, industry, military, expansion-filtered, claims, and old-name decision hooks, but they are compact stubs compared with the ancient-restoration identity standard.
   - No full route family should be added by this subagent; this remains improvement-loop scope.

4. `common/national_focus/005_soviet_collapse_republics.txt`: all republic trees
   - No audited republic tree has `FOCUS_FILTER_ANNEXATION`.
   - Direct claim/war-goal focus count is 0 for Ukraine, breakaway shared, internal republic, Baltic, Caucasus, Moldova, Belarus, and Kazakhstan; Central Asia has 1.
   - Some regional ambition exists through League, recognition, Southern Shield, grain, corridor, and resource routes, but expansion/settlement is not consistently exposed as a distinct branch.

5. `common/national_focus/005_soviet_collapse_custom_splinters.txt`: 47-focus custom trees
   - Most full custom splinters have all basic branch labels, but many still have 0 direct decision hooks and 0 direct claim/war-goal foci.
   - This makes several trees play as helper/variable ladders instead of visible diplomatic or expansion branches.

6. Repeated low-value reward patterns remain
   - Direct equipment-stockpile foci remain high in `ARD` 16 lines, `KHC` 15, `UWD` 14, `DSC` 13, `NRF` 13, `DHC` 12, `PRA` 11, `BSC` 11, `BBH` 11 before this patch and 10 after, and `moldova` 10.
   - These are not all bugs, but they should be converted where possible into route-specific decisions, missions, claims, construction programs, advisors, laws, templates, or mechanic thresholds.

## Idea-Spam Audit

| Surface | Result | Evidence |
| --- | --- | --- |
| Direct focus rewards | No direct `add_ideas`, `remove_ideas`, or `swap_ideas` found in the four focus files. | Parser checked 1698 focus rewards. |
| Same-focus direct repeated ideas | None found. | No direct `add_ideas` lines in focus files. |
| Indirect staged republic ideas | Mostly guarded. | `soviet_collapse_update_consolidated_republic_ideas` wraps staged idea clear/add logic in `hidden_effect`, checks `NOT = { has_idea = ... }`, and uses `soviet_collapse_republic_staged_idea_recently_changed` cooldown. |
| Visible recovery idea | Remaining risk, not patched. | `soviet_collapse_check_republic_recovery` can visibly add `soviet_collapse_emergency_administration_stabilized` when focus/decision recovery crosses the completion threshold. It is not repeated in one focus path, but it is still a visible helper-side idea add triggered by many focus helpers. Patching this correctly belongs to scripted-effect scope, not this focus-only pass. |

## Icon Coverage Table

| Metric | Result |
| --- | ---: |
| Focuses with icon assignment | 1698 / 1698 |
| Unique icon ids | 1498 |
| Missing icon definitions in mod or vanilla interface files | 0 |
| Icon ids reused more than once | 140 |

Notable repeated icon clusters:

- `CFR_soviet_collapse_focus_tree`: 47 focuses, 32 unique icons, 11 reused icon ids.
- `FEV_soviet_collapse_focus_tree`: 47 focuses, 32 unique icons, 13 reused icon ids.
- `IUL_soviet_collapse_focus_tree`: 47 focuses, 24 unique icons, 15 reused icon ids.
- `UWD_soviet_collapse_focus_tree`: 47 focuses, 28 unique icons, 15 reused icon ids.
- Ancient restorations reuse family icons across different trees, e.g. `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_guard_old_routes`, `GFX_focus_soviet_collapse_ancient_league_bargain`, `GFX_focus_soviet_collapse_ancient_old_border_files`, `GFX_focus_soviet_collapse_ancient_symbolic_state`, `GFX_focus_soviet_collapse_ancient_restoration_survives`, and `GFX_focus_soviet_collapse_ancient_returned_names_endgame` are each reused 4 times.

## Localisation and Reward Mismatch List

| Check | Result | Notes |
| --- | --- | --- |
| Focus title localisation | 1698 / 1698 present | Parsed `localisation/**/*.yml`; no missing focus title keys. |
| Focus description localisation | 1698 / 1698 present | Parsed `localisation/**/*.yml`; no missing `_desc` keys. |
| Duplicate direct equipment in one focus reward | Fixed one issue | `BBH_column_schools` no longer grants `support_equipment_1` twice. |
| Focus reward/title semantic mismatch | Remaining design risk | Repeated tiny equipment, trains, convoy, AA, and generic construction rewards still make several route titles feel stronger than their mechanical payoff. Examples: `NRF_dead_convoy_supply_board`, `NRF_ghost_convoy_escorts`, `ARD_winter_convoy_columns`, `ARD_white_sea_port_tolls`, `DHC_grain_convoy_escorts`, `KRS_icebound_supply_ledger`, `IUL_rail_and_river_patrols`. |
| Noisy idea hover spam | Mostly clean in focus files | Direct focus rewards no longer add idea spam. Remaining risk is helper-side visible recovery idea noted above. |

## AI Behavior Gaps

Every audited focus has an `ai_will_do`, but many are base-only and do not react to route, war state, stability, threat, foreign pressure, League position, or high-chaos context.

| Tree or group | Flat base-only AI count | Examples |
| --- | ---: | --- |
| `soviet_collapse_kazakhstan_focus_tree` | 61 | `kaz_soviet_collapse_alma_ata_emergency_congress`, `kaz_soviet_collapse_steppe_district_inventories`, `kaz_soviet_collapse_the_alash_courts` |
| `soviet_collapse_ukraine_focus_tree` | 27 | `ukr_soviet_collapse_emergency_rada`, `ukr_soviet_collapse_question_of_statehood`, `ukr_soviet_collapse_moscows_officers_in_our_barracks` |
| `soviet_collapse_internal_republic_focus_tree` | 25 | `internal_soviet_collapse_convene_republic_presidium`, `internal_soviet_collapse_write_the_autonomy_statute` |
| `soviet_collapse_caucasus_focus_tree` | 23 | `caucasus_soviet_collapse_mountain_federal_compact`, `caucasus_soviet_collapse_hold_the_passes` |
| Ancient restoration trees | 12 each | Opening, law, register, market/workshop, and end-state focuses in each ancient tree. |
| Custom 47-focus trees | 5-13 each in weaker cases | `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` still need more route-aware AI. |

## Layout and Prerequisite Audit

| Check | Result |
| --- | --- |
| Duplicate coordinates inside a tree | None found with corrected x/y parser. |
| Too-close same-row coordinates with x distance <= 1 | None found. |
| Missing prerequisite parent inside same tree | None found. |
| Isolated focus blocks | None found. |
| Continuous focus positions | Present for all 41 trees. |
| Unsupported `<=` or `>=` operators | None found in audited focus files. |
| OR prerequisites | 160 focus blocks use OR prerequisite semantics. |

OR prerequisite notes:

- No obvious local OR/AND syntax bug was patched.
- Several OR joins intentionally merge mutually exclusive or alternate branch parents, e.g. ancient charter joins and factory successor route joins.
- Some OR joins still need route semantics review during broader design work so incompatible political paths do not converge into identical end states without visible consequences.

## Validation Commands and Results

Ran:

```bash
python3 - <<'PY'
# parser over the four focus files:
# - counts focus trees/focuses
# - checks balanced braces
# - checks duplicate direct helper calls and duplicate direct equipment grants inside a single focus reward
PY
```

Result:

```text
focuses_checked 1698
ok: balanced braces and no repeated direct helper/equipment grants in one focus reward
```

Ran:

```bash
rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt
```

Result: no matches.

Ran icon and localisation parsers:

- 1698 / 1698 focus icons assigned.
- 0 missing icon definitions in mod or vanilla interface files.
- 0 missing focus title localisation keys.
- 0 missing focus description localisation keys.

Skipped validation:

- No in-game load test was run from this subagent context.
- No flag/art validation was run because flags are explicitly out of scope and must remain untouched.
- No scripted-effect patch validation was run because scripted helper changes were intentionally avoided.

## Remaining Route Risks

- Broad route-depth gaps remain and should continue under the existing follow-up plan: `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.
- `OGB`, all four ancient restorations, `DSC`, `NRF`, and `PRA` are still the highest-priority depth risks.
- Repeated low-value equipment/convoy/train rewards remain outside the single same-focus duplicate fixed here.
- Republic expansion/settlement branches are still not consistently visible as distinct branch families.
- Many AI weights are present but too flat for route-aware behavior.
- Some icon reuse is intentional family reuse, but high-reuse trees should get an icon-identity pass if the art pipeline is active.

## Flags Untouched

No files under `gfx/flags` were opened, inspected for edit, modified, generated, or validated. No flag artwork was touched.
