# Event005 Focus Tree Subagent Handoff - NLC/CFR/War-Plan Patch

Date: 2026-06-01

Scope:
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Out of scope:
- No files under `gfx/flags` were read, inspected, converted, or edited.
- No broad route redesigns, new formable chains, or new mechanics were added.

## High-Priority Fixes Applied

| Priority | File | Focus ids | Issue | Patch |
| --- | --- | --- | --- | --- |
| High | `common/national_focus/005_soviet_collapse_factory_successors.txt` | `CFR_cities_first` | The cities-first strategy was gated by `CFR_the_board_becomes_the_cabinet` and `CFR_the_engineers_overrule_the_party`, which are mutually exclusive governance follow-ups outside the site-committee route. This could make the strategy branch impossible despite its visible prerequisite. | Removed the unrelated completed-focus requirements and kept the hidden mutual-exclusion guard against the other strategy siblings. |
| High | `common/national_focus/005_soviet_collapse_custom_splinters.txt` | `NLC_winter_guarantees`, `NLC_ration_and_signal_escorts`, `NLC_heated_workshop_contracts` | Several focuses used a single prerequisite block with multiple `focus = ...` entries while duplicating an AND-style `available` check. In focus script this draws OR pathlines, so the tree showed a softer path than the actual gate. | Split the requirements into separate prerequisite blocks and removed the duplicated availability gates. |
| High | `common/national_focus/005_soviet_collapse_custom_splinters.txt` | `NLC_diplomatic_plan`, `NLC_special_arm`, `NLC_enemy_front`, `NLC_settlement`, `NLC_polar_neutrality_statute`, `NLC_industry_plan`, `NLC_endgame` | Hard route requirements were hidden in `available`, which blocked completion without drawing the intended route geometry. | Converted the hard route requirements into visible `prerequisite` entries. |
| Medium | `common/national_focus/005_soviet_collapse_custom_splinters.txt` | `FTH_war_plan`, `NLC_war_plan` | War-plan focuses were defensive or stockpile-heavy compared to the requested high-chaos successor identity. | Added existing helper payloads for assault columns and expansion claims in the hidden route-identity reward block. |

## Route Coverage Table

| Tree or route | Implemented route surface reviewed | Status after patch | Remaining gap |
| --- | --- | --- | --- |
| CFR factory successor strategy route | `CFR_minutes_from_every_workshop` into `CFR_cities_first` and strategy siblings | `CFR_cities_first` is no longer blocked by mutually exclusive governance follow-ups. | Other CFR/MFR/OGB depth and reward variety were not fully rebalanced in this bounded pass because the scoped files already contain broad in-progress edits. |
| FTH Free Territory aggressive war route | `FTH_radical_turn` into `FTH_war_plan` | War plan now uses existing aggressive custom-splinter helpers for assault columns and expansion claims, in addition to command, manpower, equipment, and supply-plan rewards. | The broader FTH route still relies on repeated custom-splinter identity helpers in several places; a deeper route pass should collapse or diversify repeated helper stacks. |
| NLC Northern Lights political/league/war/industry route | NLC political, diplomatic, inner-faction, enemy-front, winter, industry, and endgame gates | Hard gates now render as focus prerequisites; major AND gates no longer masquerade as OR pathlines. `NLC_war_plan` now carries aggressive assault-column and expansion-claim payloads. | NLC still has pre-existing formatting irregularities and could use a broader route-specific AI strategic-plan pass for endurance versus extreme-path choices. |
| Ancient restorations | Shared ancient-restoration focus file was brace/operator checked and scanned at a high level | No local patch made in this pass. | Several ancient restoration mini-trees still appear to share repeated icon and reward patterns. Bespoke icon/reward differentiation is broader than this local patch. |

## Missing or Simplified Content

| Area | File and identifiers | Finding | Recommendation |
| --- | --- | --- | --- |
| Repeated helper payloads | `common/national_focus/005_soviet_collapse_custom_splinters.txt`, multiple custom splinter route nodes | Many splinter focuses still use similar identity helper packages. This is better than direct idea spam, but some branches can still feel mechanically repetitive. | In a future route-depth tranche, collapse repeated stacks into route-specific hidden packages only where the package represents a real route milestone, and replace smaller nodes with claims, units, decisions, or state construction tied to identity. |
| NLC strategic AI | `NLC_polar_commune_endurance`, `NLC_extreme_path`, nearby NLC route ids | Focus-level weights exist, but there is no broader route-aware AI plan deciding stable polar compact versus radical pressure posture. | Add a small route-aware AI plan or helper strategy if the parent opens AI strategy scope. |
| Ancient icon/reward differentiation | `common/national_focus/005_soviet_collapse_ancient_restorations.txt`, ancient restoration shared mini-tree ids | No direct issue was safe enough to patch without expanding beyond a local audit. Shared icons and similar reward rhythms remain visible across restoration routes. | Queue a focused ancient-restoration identity pass to diversify icons/rewards and connect endgame nodes to route-specific cores, claims, or restoration mechanics. |

## Icon Coverage Table

| Focus id | Icon id | Changed? | Notes |
| --- | --- | --- | --- |
| `CFR_cities_first` | `GFX_focus_CFR_housing_before_flags` | No | Route lock only. |
| `FTH_war_plan` | `GFX_focus_FTH_war_plan` | No | Reward helper payload expanded. |
| `NLC_diplomatic_plan` | `GFX_focus_NLC_diplomatic_plan` | No | Prerequisite geometry only. |
| `NLC_special_arm` | `GFX_focus_NLC_special_arm` | No | Prerequisite geometry only. |
| `NLC_enemy_front` | `GFX_focus_NLC_enemy_front` | No | Prerequisite geometry only. |
| `NLC_war_plan` | `GFX_focus_NLC_war_plan` | No | Reward helper payload expanded. |
| `NLC_winter_guarantees` | `GFX_focus_NLC_legitimacy` | No | AND prerequisite geometry fixed. |
| `NLC_settlement` | `GFX_focus_NLC_settlement` | No | Prerequisite geometry only. |
| `NLC_ration_and_signal_escorts` | `GFX_focus_NLC_ration_and_signal_escorts` | No | AND prerequisite geometry fixed. |
| `NLC_heated_workshop_contracts` | `GFX_focus_NLC_heated_workshop_contracts` | No | AND prerequisite geometry fixed. |
| `NLC_polar_neutrality_statute` | `GFX_focus_NLC_polar_neutrality_statute` | No | Prerequisite geometry only. |
| `NLC_industry_plan` | `GFX_focus_NLC_industry_plan` | No | Prerequisite geometry only. |
| `NLC_endgame` | `GFX_focus_NLC_endgame` | No | Prerequisite geometry only. |

No icon ids were changed. No localisation keys were added or renamed.

## Localisation and Reward Mismatches

| File and id | Finding | Resolution |
| --- | --- | --- |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `FTH_war_plan` | The focus title/reward intent reads like a war plan, but the previous payoff was mostly command, manpower, stockpile, resilience, and supply. | Added existing assault-column and expansion-claim helpers under the existing route-identity tooltip payload. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `NLC_war_plan` | Similar war-plan mismatch: useful supply/air/resilience rewards, but limited direct aggressive payoff. | Added existing assault-column and expansion-claim helpers under the existing route-identity tooltip payload. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt`, `CFR_cities_first` | The visible focus chain suggested this strategy should follow `CFR_minutes_from_every_workshop`, but hidden availability demanded unrelated governance focuses. | Removed the bad gates. Localisation did not need a change because the focus id and displayed intent stayed the same. |

## AI Behavior Gaps

| File and ids | Current behavior | Gap |
| --- | --- | --- |
| `FTH_war_plan`, `NLC_war_plan` | Existing `ai_will_do` weights remain; added helpers can create aggressive claims/war payoff through existing scripted logic. | No new route-level AI strategy was added in this bounded patch. |
| NLC endgame route | Focus weights favor stability/war conditions locally. | The polar-commune endurance versus extreme-path split would benefit from a small route-aware AI plan in a broader pass. |
| Ancient restorations | Existing focus weights were not altered. | Ancient restoration AI identity may still be too generic where routes share reward patterns. |

## Patch Details

Changed files:
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_01_event005_focus_tree_subagent_nlc_cfr_warplan_patch_handoff.md`

Reviewed but not patched:
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Changed focus ids:
- `CFR_cities_first`
- `FTH_war_plan`
- `NLC_diplomatic_plan`
- `NLC_special_arm`
- `NLC_supply`
- `NLC_enemy_front`
- `NLC_war_plan`
- `NLC_civil_rule`
- `NLC_winter_guarantees`
- `NLC_settlement`
- `NLC_ration_and_signal_escorts`
- `NLC_heated_workshop_contracts`
- `NLC_polar_neutrality_statute`
- `NLC_industry_plan`
- `NLC_endgame`

Route behavior before and after:
- Before: `CFR_cities_first` could be blocked by unrelated governance branch completion checks. After: it opens from its actual site-committee prerequisite while remaining mutually exclusive with sibling strategies through the hidden guard.
- Before: several NLC hard gates were hidden in availability checks, producing misleading or missing route lines. After: hard gates are visible prerequisites.
- Before: NLC AND gates used OR-style prerequisite geometry with duplicated AND availability. After: each required parent is a separate prerequisite.
- Before: `FTH_war_plan` and `NLC_war_plan` lacked a strong direct aggressive payoff. After: both call existing assault-column and expansion-claim helpers in their route-identity hidden reward block.

Localisation keys changed:
- None.

Icon ids changed:
- None.

## Validation

Ran:
- Brace balance on all three scoped focus files:
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `brace_balance=0`, `min_balance=0`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`: `brace_balance=0`, `min_balance=0`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: `brace_balance=0`, `min_balance=0`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - No matches.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - No output.
- `git diff --name-only -- gfx/flags`
  - No output.
- `git status --short -- gfx/flags`
  - No output.

Skipped validation:
- Full-game load validation was not run from this subagent environment.
- No commit was created because the worktree already contained broad pre-existing changes, including pre-existing modifications in the scoped focus files and many unrelated files.

## Remaining Route Risks

- NLC still has pre-existing indentation/style irregularities around some focus blocks. This pass did not normalize broad formatting to avoid unrelated churn.
- The custom splinter file still contains many repeated helper-style focus rewards outside the patched nodes. These need a broader route-depth pass if the parent wants full removal of repetitive reward cadence.
- Ancient restoration branches were not locally changed; shared icon/reward rhythm remains a follow-up candidate.
- This handoff is the plan handoff for the bounded patch. No separate improvement plan was written.
