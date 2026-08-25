# Event 006 formable decision registry merge — 2026-08-25

## Scope

This source-layout pass folds the small FORM-08 Danubian Confederation and FORM-09 Balkan Federation decision files into `common/decisions/006_independence_wave_formable_decisions.txt`.

The two categories remain independent inside the receiver. No decision ID, category ID, cost key, timer, trigger, effect, tooltip, or AI weight was changed. The SCN-008 decision ledger and package-owned decision files remain separate because they have different scenario or package ownership boundaries.

## Preservation evidence

The receiver retains all four executable decision IDs: `independence_wave_form08_convene_river_congress`, `independence_wave_form08_arbitrate_minorities`, `independence_wave_form08_standardize_rail_authority`, and `independence_wave_form09_ratify_border_board`.

The receiver retains both category IDs: `independence_wave_form08_danube_category` and `independence_wave_form09_balkan_category`. Normalized semantic subsequence comparison against the two pre-merge files found both complete bodies in the receiver, and the source scan found no live references that depend on the removed filenames.

## Boundary

This is a source-layout consolidation only. It does not change formable admission, state anchors, costs, GUI surfaces, package readiness, SCN-008 reachability, or the Event 006 32/29/40/161 boundary. It does not claim live parser, tooltip, or in-game acceptance evidence.

## Changed paths

- `common/decisions/006_independence_wave_formable_decisions.txt`
- removed `common/decisions/006_independence_wave_form08_decisions.txt`
- removed `common/decisions/006_independence_wave_form09_decisions.txt`
