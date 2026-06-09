# Event 005 Focus Tree Subagent Handoff: Belarus Route Layout Patch

Date: 2026-05-31
Scope: Event 005 Soviet Collapse focus trees only.
Mode: bounded focus-tree audit plus small patch.

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_event005_focus_tree_belarus_route_layout_reward_patch.md`

No `gfx/`, `gfx/flags/`, interface, flag, or asset files were touched.

The worktree already contained unrelated dirty edits in Event 005 and Event 006 files before this pass. This handoff records only the bounded Belarus focus-tree patch made in this pass.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine major republic tree | `soviet_collapse_ukraine_focus_tree`, 83 focuses | Implemented, still risky | Political, military, industry, diplomacy, League, expansion, and high-chaos routes exist, but the tree still needs a dedicated visual pass for long crossing lines and route payoff consistency. |
| Belarus republic tree | `soviet_collapse_belarus_focus_tree`, 53 focuses | Patched | Rail, forest, corridor, political, League, and high-chaos lanes exist. This pass cleaned the statehood-route selector cluster and deepened two selector rewards. |
| Shared/breakaway republic support | `soviet_collapse_breakaway_focus_tree`, 36 focuses; `soviet_collapse_internal_republic_focus_tree`, 62 focuses | Implemented, mixed depth | Shared republic logic exists, but several branches still have compact generic helper payoffs and should be reviewed after parent decision work settles. |
| Regional republic trees | Baltic 42, Caucasus 40, Central Asia 45, Moldova 48, Kazakhstan 92 | Implemented, mixed risk | Core route families exist. Kazakhstan is deeper; other regional trees still need line readability and reward-identity review. |
| Custom splinters | 25 custom trees, 1005 focuses total | Implemented, uneven | Most full splinters are 47 focuses; crisis splinters are 18-22. Several still need non-generic route payoff review. |
| Factory successors | `CFR` 47, `MFR` 58, `OGB` 23 | Partly simplified | CFR/MFR have real branch structure. OGB remains short for an OP successor and should remain a high-priority redesign target. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN`, 16 focuses each | Simplified | These are still compact stubs compared with the spec's ancient-restoration identity promise. Needs broader plan/implementation, not a subagent patch. |

## High-Priority Findings

1. `common/national_focus/005_soviet_collapse_republics.txt`: Belarus route selectors `blr_soviet_collapse_national_council_of_minsk`, `blr_soviet_collapse_socialist_autonomy_without_moscow`, `blr_soviet_collapse_military_transit_directorate`, and `blr_soviet_collapse_foreign_corridor_administration` used hidden `has_completed_focus` exclusions but lacked visible mutual-exclusion lines. This made the statehood fork harder to read and left a midpoint-line problem in the route cluster.
2. `common/national_focus/005_soviet_collapse_republics.txt`: Belarus statehood selector coordinates were staggered across `y = 5` and `y = 6`, while child route focuses sat around `y = 7`. The cluster crowded the rail and forest lanes, especially near `blr_soviet_collapse_swamp_roads_closed`.
3. `common/national_focus/005_soviet_collapse_republics.txt`: `blr_soviet_collapse_national_council_of_minsk` and `blr_soviet_collapse_foreign_corridor_administration` had route-lock rewards that were still too close to generic recognition/foreign-channel helper payoffs.
4. Broader: Ukraine remains visibly dense and line-heavy despite prior movement. Fixing it properly is beyond a one-patch subagent pass because the complaint concerns the whole branch shape and many crosslinks.
5. Broader: ancient restorations and OGB are still shallow relative to the spec and should not be claimed complete without broader route expansion.

## Patch Details

Changed focus ids:

- `blr_soviet_collapse_national_council_of_minsk`
- `blr_soviet_collapse_socialist_autonomy_without_moscow`
- `blr_soviet_collapse_military_transit_directorate`
- `blr_soviet_collapse_foreign_corridor_administration`
- `blr_soviet_collapse_council_bargains_with_forests`
- `blr_soviet_collapse_red_without_the_center`
- `blr_soviet_collapse_orders_printed_like_timetables`

Before:

- Belarus' four statehood routes were locked only through hidden completion checks.
- Selector positions were `x/y`: national `11/5`, socialist `14/6`, military `18/6`, foreign `23/6`.
- The national council route only applied legal recognition. The foreign corridor route only applied the foreign-channel helper.

After:

- Added visible pairwise `mutually_exclusive` entries for the four Belarus statehood routes.
- Repositioned the selector row into cleaner vertical lanes: national `7/5`, socialist `12/5`, military `18/5`, foreign `24/5`.
- Aligned immediate child lanes by fixing `blr_soviet_collapse_orders_printed_like_timetables` to `x = 18`, and normalized indentation on the three direct route follow-up focuses.
- Added `soviet_collapse_apply_focus_republican_compact_plan = yes` to `blr_soviet_collapse_national_council_of_minsk`.
- Added `soviet_collapse_apply_focus_foreign_recognition_plan = yes` to `blr_soviet_collapse_foreign_corridor_administration`.

## Icon Coverage Table

| Surface | Result | Notes |
| --- | --- | --- |
| Patched Belarus focus icons | No icon ids changed | Existing icon ids were preserved. |
| Four bounded focus files vs `interface/` icon definitions | No missing focus icon definitions found by command-line compare | Used referenced `icon = GFX_*` values from the four focus files against `name = "GFX_*"` in `interface/`. |
| Asset/flag files | Not touched | User explicitly forbade gfx/flags and asset changes. |

## Localisation And Reward Mismatch List

- No localisation keys were added, renamed, or edited.
- No focus ids were renamed.
- No icon ids were changed.
- The two reward-depth changes use existing scripted effect helper ids, so no new player-facing localisation keys were required.
- Remaining mismatch risk: several Ukraine and custom-splinter rewards still read as broad helper payloads rather than focus-specific route payoffs. This is a design-depth issue, not a safe local patch.

## AI Behavior Gaps

- Patched Belarus route selectors kept their existing `ai_will_do` logic. The visible mutual exclusions do not change AI route eligibility because hidden availability checks already enforced exclusivity.
- Ukraine still has many flat or semi-flat AI bases in route follow-ups and needs a route-aware AI pass once parent decisions/effects settle.
- Ancient restorations and OGB have insufficient route-specific AI depth for their intended identities.

## Validation Run

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt` passed.
- `rg -n "<=|>="` on the four bounded focus files returned no unsupported operators.
- Focus count check on bounded files:
  - `005_soviet_collapse_republics.txt`: 501 focuses
  - `005_soviet_collapse_custom_splinters.txt`: 1005 focuses
  - `005_soviet_collapse_factory_successors.txt`: 128 focuses
  - `005_soviet_collapse_ancient_restorations.txt`: 64 focuses
- Icon reference compare for the four focus files returned no missing `GFX_*` definitions in `interface/`.
- `git diff --name-only -- gfx/flags` returned empty.

## Skipped Validation

- No in-game focus-tree screenshot validation was run from this subagent session.
- No full HOI4 load test was run.
- No localisation file validation was run because this patch did not touch localisation.

## Remaining Route Risks

- Ukraine is still the highest-priority visual/readability target. Its branch count and crosslinks make a safe one-hunk fix insufficient.
- Belarus is improved but still has lower-tree line density around League/forest integration, especially `blr_soviet_collapse_join_the_league_when_war_comes`, `blr_soviet_collapse_prepare_league_freight_tables`, and `blr_soviet_collapse_minsk_supplies_the_front`.
- OGB and ancient restorations remain shallow compared with the focus-tree spec.
- Custom splinters still need a reward-identity pass for repeated rail/convoy/equipment-style rewards.

## Plan Handoff

No new broad improvement plan was written. The existing follow-up plan remains the correct broader design handoff:

- `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`
