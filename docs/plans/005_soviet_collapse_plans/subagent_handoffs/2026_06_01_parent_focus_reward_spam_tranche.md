# Event005 Parent Focus Reward Spam Tranche

## Scope

Parent patch for the current Soviet Collapse focus-tree cleanup. This tranche only touched Event005 focus files and did not touch `gfx/flags`.

Changed files:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`

## Problem Addressed

The current focus trees still had many visible focus rewards made of repeated equipment lines. The worst case was custom splinter focuses with two or three direct `add_equipment_to_stockpile` effects in one focus, often on top of an existing scripted reward helper. That made focus rewards read as clutter instead of a route payoff.

## Behavior Changed

Converted the remaining multi-stockpile focus rewards in the checked Event005 focus files into existing custom-tooltip scripted helpers and route-specific state changes:

- War-plan and radical-turn focuses now use `soviet_collapse_apply_focus_chaos_assault_plan` where appropriate.
- Supply/depot focuses now use `soviet_collapse_apply_focus_chaos_supply_plan`, `soviet_collapse_apply_focus_security_supply_plan`, `soviet_collapse_apply_focus_foreign_supply_plan`, or `soviet_collapse_apply_focus_rail_authority_reward`.
- Guard/militia focuses now rely on military/security helpers instead of direct visible infantry/support/artillery bundles.
- `DSC_armies_that_do_not_demobilize` keeps the Dead Soldiers Congress claims, cores, expansion decisions, and neighbor-war launch path while removing direct equipment clutter.
- `PRA_coal_water_and_spare_parts` and Moldova smuggling/relief focuses now route through rail/foreign supply helpers instead of showing separate train/convoy/support lines.
- `OGB_notables_and_workshops` now uses `soviet_collapse_apply_focus_civil_military_authority_plan` rather than direct militia equipment.

## Validation

Commands/checks run after the patch:

- Brace balance for all four Event005 focus files: `balance=0`, `min=0`.
- Direct duplicate `add_ideas` inside a focus: `0`.
- Focuses with three-or-more direct idea rewards: `0`.
- Focuses with two-or-more direct `add_equipment_to_stockpile` effects: `0` across:
  - `005_soviet_collapse_republics.txt`
  - `005_soviet_collapse_custom_splinters.txt`
  - `005_soviet_collapse_factory_successors.txt`
  - `005_soviet_collapse_ancient_restorations.txt`
- Current direct stockpile effect count after this tranche: `170`.
  - `005_soviet_collapse_custom_splinters.txt`: `137`
  - `005_soviet_collapse_republics.txt`: `24`
  - `005_soviet_collapse_ancient_restorations.txt`: `8`
  - `005_soviet_collapse_factory_successors.txt`: `1`
- Duplicate focus IDs across the four files: none found.
- Parent-not-above-child pathline coordinate risks across the four files: `0` found by parser.
- `rg "<=|>="` on touched focus files: no unsupported operators found.
- `git diff --check` on touched focus files: clean.
- `git diff --name-only -- gfx/flags`: no output.

## Remaining Gaps

This tranche does not complete the requested focus-tree rework.

Known remaining issues:

- Many focuses still have one direct equipment stockpile line, especially support equipment and convoys in `005_soviet_collapse_custom_splinters.txt`.
- The parser can catch parent-above-child pathline risks, but it cannot prove every in-game pathline is visually clean.
- Branch depth still needs a broader design pass. Several special splinters remain shallow and need stronger political, industrial, and expansion route interaction.
- Ukraine and Belarus layout quality still need visual/design review beyond coordinate heuristics.
- The separate focus audit subagent finished and wrote `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_01_event005_focus_full_current_audit.md`. Its direct-stockpile counts were taken before this parent tranche, so this handoff's `170` direct-stockpile count is the newer current-state value.
