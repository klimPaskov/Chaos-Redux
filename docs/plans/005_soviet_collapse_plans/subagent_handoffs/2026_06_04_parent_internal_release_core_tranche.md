# Event005 parent internal release core tranche

Date: 2026-06-04

## Scope

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- No flag files touched.

## Findings

- The terminal and triggerable scenario release flow already uses dynamic release passes:
	- `soviet_collapse_release_terminal_all_ordinary_republics`
	- `soviet_collapse_force_terminal_all_possible_core_countries_exhaustive`
	- `soviet_collapse_free_terminal_soviet_subjects`
	- `soviet_collapse_spawn_terminal_high_chaos_successors`
	- `soviet_collapse_apply_triggerable_scenario_initial_forces`
- `DON` and `KUB` were listed in internal release weighting and focus-tree routing, but `soviet_collapse_restore_internal_republic_release_cores` did not seed any cores for them.
- Vanilla defines `DON` and `KUB` as releasable tags, but the sampled vanilla state files do not give them state cores. Without core seeding, the exhaustive release loop cannot find them.

## Patch

Added internal release cores before the existing Bukharan/Altai/etc. core seeds:

- `DON`: state `218` Rostov
- `KUB`: state `234` Krasnodar
- `KUB`: state `235` Stavropol

These tags now enter the same progressive, terminal, and triggerable-scenario release paths as other internal republics. The patch does not hardcode major-country influence or release selection; it only supplies missing core data for tags already present in the dynamic Soviet Collapse internal republic lists.

## Parent reward-spam scan

Direct focus scan across the four Event005 focus files found:

- `005_soviet_collapse_republics.txt`: 501 focuses, 0 direct duplicate `add_ideas`
- `005_soviet_collapse_custom_splinters.txt`: 1005 focuses, 0 direct duplicate `add_ideas`
- `005_soviet_collapse_factory_successors.txt`: 128 focuses, 0 direct duplicate `add_ideas`
- `005_soviet_collapse_ancient_restorations.txt`: 64 focuses, 0 direct duplicate `add_ideas`

The remaining spam risk is helper-driven and design-level:

- many focuses still call generic helpers such as `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_legal_recognition`, and `soviet_collapse_apply_focus_high_chaos_identity`
- `soviet_collapse_update_pra_authority_idea` is idempotent and hidden, but remains a visible-design risk because several PRA route focuses still revolve around authority-idea state changes rather than unique rail-state actions

## Validation

Pending final parent validation after the focus audit subagent returns.

## Remaining gaps

- Full focus-tree redesign remains incomplete.
- Helper-driven generic reward rhythm remains the main source of shallow focus feel.
- The focus audit subagent is still expected to provide a fresh layout/depth handoff for parent follow-up.
