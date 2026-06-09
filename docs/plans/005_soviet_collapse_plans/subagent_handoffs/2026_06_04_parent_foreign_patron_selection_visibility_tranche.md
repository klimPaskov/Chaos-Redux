# 2026-06-04 Parent Foreign Patron Selection Visibility Tranche

## Scope

Patched a narrow intervention-menu reliability issue where selecting a breakaway could leave the player with no immediately visible foreign-intervention decisions for that target.

No flag files, flag images, or flag interface files were touched.

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`

## Gameplay Change

`soviet_collapse_select_foreign_patron_target` now directly activates the foreign-patron targeted decisions from inside the selected breakaway scope, while `PREV` still points to that selected target.

Added helper:

- `soviet_collapse_activate_foreign_patron_target_decisions_for_prev`

The existing broader activation paths remain in place:

- direct `FROM` activation;
- saved `event_target:soviet_collapse_foreign_patron_menu_target` activation;
- selected-target activation through `global.soviet_collapse_breakaway_countries`.

This makes the Show Decisions click deterministic for dynamically registered breakaways such as Central Asian republics while preserving the existing target triggers and cost gates.

## Validation

- Consulted offline decision wiki targeted-decision semantics: `target_trigger` uses ROOT as the decision owner and FROM as the possible target.
- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt common/national_focus/005_soviet_collapse_factory_successors.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_parent_ogb_future_bulgaria_focus_tranche.md`: clean.
- `rg -n "<=|>="` over touched gameplay/localisation files: no unsupported operators.
- Brace balance over touched gameplay/localisation files: clean.
- Localisation BOM check for the touched localisation file from the OGB tranche: true.
- `git status --short -- gfx/flags interface/flags`: no entries.

## Remaining Gaps

This does not complete the broader influence-system request. It only improves selected-target visibility. Influence values, color explanations, dynamic funding variety, and client-state difficulty still need a separate pass before that system can be considered finished.
