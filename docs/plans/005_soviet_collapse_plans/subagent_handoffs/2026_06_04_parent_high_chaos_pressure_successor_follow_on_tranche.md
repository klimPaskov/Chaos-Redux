# Event005 parent tranche: high-chaos pressure-successor follow-ons

## Scope

Parent-side Event005 Soviet Collapse release pacing tranche.

Files changed:

- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`

No flag files were touched.

## Problem

The active follow-on release scheduler already releases many ordinary and internal republics at gathering storm and higher chaos, but special pressure successors such as FEV, NRF, OGB, and other high-chaos splinters still depended mostly on the slower progressive family roll. The older weighted pressure-successor family also only gave direct family weights to a small subset of pressure tags, so high chaos could still feel like ordinary republic secession rather than special successor mutation.

## Implementation

Added tuning constants under `soviet_collapse_release_mtth`:

- `follow_on_chaos_tier_3_pressure_successors = 2`
- `follow_on_chaos_tier_4_pressure_successors = 6`
- `follow_on_chaos_tier_5_pressure_successors = 12`
- `follow_on_pressure_successor_cap = 18`

Added helpers:

- `soviet_collapse_release_dynamic_pressure_successor_follow_on`
- `soviet_collapse_release_dynamic_pressure_successor_follow_ons`
- `soviet_collapse_ensure_cfr_construction_mandates_idea`

The helper scans `every_possible_country` with the existing `is_soviet_collapse_pressure_successor_progressive_candidate = yes` trigger, chooses random eligible pressure successors, and passes them through the existing `soviet_collapse_release_selected_progressive_republics` pipeline. That means the existing spawn helpers, setup logic, high-chaos successor flags, and reports remain the source of truth.

Hooked the new batch helper into `soviet_collapse_release_dynamic_follow_on_republics` after ordinary/internal follow-on releases. It is inert below chaos tier 3 and clamps through script constants.

The CFR construction helper cleanup moves repeated visible `add_ideas = cfr_construction_mandates` grants behind `soviet_collapse_ensure_cfr_construction_mandates_idea`. The construction mandate idea still gets ensured, but the reward surface now relies on the existing construction-mechanic tooltip and building/variable rewards instead of exposing the same idea grant from several helper paths.

## Verified Existing Behavior

The triggerable Soviet Collapse scenario already:

- sets `soviet_collapse_triggerable_scenario_suppressed_fire_once`
- removes Event005 from `global.fire_once_events`
- adds Event005 to `global.disabled_events` and `global.fired_events`
- sets Event005 weight to 0 through `set_event_weight`
- forces terminal release via `soviet_collapse_force_triggerable_scenario_terminal_release`
- disables active Soviet Collapse flags after scenario launch

Mission/progressive-release report events checked in `events/005_soviet_collapse.txt` already use `minor_flavor = yes` and `major = no` for the inspected mission report range.

## Validation

Commands run:

- `git diff --check -- common/script_constants/005_soviet_collapse_constants.txt common/scripted_effects/005_soviet_collapse_effects.txt`
- brace-depth scan for both touched files
- `rg -n "<=|>=" common/script_constants/005_soviet_collapse_constants.txt common/scripted_effects/005_soviet_collapse_effects.txt`
- `git status --short -- gfx/flags interface/flags`

Results:

- no diff whitespace errors
- final brace depth was 0 for both touched files
- no unsupported `<=` or `>=`
- no flag-folder changes

Additional scan:

- Event005 focus files currently contain no direct `add_ideas`, `add_timed_idea`, `swap_ideas`, or `remove_ideas` inside focus blocks.
- Per-focus duplicate helper-key scan found no repeated helper key within a single focus block.
- Remaining visible `add_ideas = cfr_construction_mandates` outside the new ensure helper is the initial CFR setup path.

## Remaining Work

This tranche does not complete the broad Event005 goal. Remaining high-priority items:

- full focus-tree rewrite/audit integration
- focus reward depth and duplicate/meaningless reward cleanup
- in-game pathline/mutex layout verification
- evolution-detail spreadsheet/localisation alignment
- decision visibility bugs for dynamically expanded breakaway republics
- broader high-chaos country identity passes
