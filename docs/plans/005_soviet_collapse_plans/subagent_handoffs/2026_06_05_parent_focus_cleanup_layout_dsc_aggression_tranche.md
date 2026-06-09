# Parent Handoff: Focus Cleanup, Layout, And DSC Aggression Tranche

## Scope

This tranche addresses three concrete Event005 focus-tree problems from the active audit trail:

- broad starting-tension idea cleanup hiding too much helper churn behind focuses
- named Belarus, Kazakhstan, and GAC pathline clutter points
- Dead Soldiers Congress needing stronger map-facing aggression instead of more idea rewards

No flag files were touched.

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

This pass also reviewed the focus-auditor handoff:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/20260605T145855Z_event005_focus_tree_auditor_current_state_handoff.md`

## Gameplay Changes

- `soviet_collapse_clear_focus_starting_tension_ideas` now removes only the calling country's own starting-tension idea:
  - PRA dispatcher-court tensions
  - TSC field-station rivalries
  - RMC credal-cell rivalries
  - DSC grave-regiment rivalries
  - NRF drowned-crew disputes
  - ICD grave-commissar rivalries
  - OGB restored-name dispute
- `DSC_dead_regiment_columns` now adds existing chaos expansion and neighbor-conflict pressure through hidden helpers while keeping a concise visible tooltip.
- `DSC_maps_of_lost_armies` now marks neighboring breakaways as unfinished fronts through the existing high-chaos neighbor expansion helper and has a matching visible tooltip.

## Layout Changes

- Moved `blr_soviet_collapse_belarusian_question_answered` from `x = 16` to `x = 14` to clear the timetable column.
- Moved `kaz_soviet_collapse_a_state_across_distances` from `x = 23` to `x = 22` to clear the mine-rail/arsenal column.
- Moved `kaz_soviet_collapse_restore_alash_names` from `x = 25` to `x = 26` to clear the resource-town column.
- Moved `GAC_harvest_truce_guarantees` from `x = 18` to `x = 20`.
- Moved `GAC_rural_congress_charter` from `x = 18` to `x = 20`.

## Validation

- `git diff --check` on touched gameplay/localisation/handoff files.
- Brace balance check on touched script/focus files.
- `rg -n "<=|>="` on touched script/focus files.
- Per-tree coordinate scan across all four Event005 focus files:
  - `0` in-tree coordinate overlaps.
- Localisation encoding check:
  - `localisation/english/005_soviet_collapse_custom_countries_l_english.yml` still has UTF-8 BOM.
  - `DSC_dead_regiment_columns_tt` and `DSC_maps_of_lost_armies_tt` are present.

## Remaining Gaps

- Ukraine and Belarus route-choice focuses still need a real route-row redesign before visible mutual exclusions should be added. Adding pairwise mutual exclusions on the current single-row layout would likely draw red route-lock lines through other route focuses.
- The broader focus-tree depth goal remains incomplete: many cloned 47-focus splinters and helper-heavy rewards still need bespoke political, industrial, expansion, and special-mechanic branches.
