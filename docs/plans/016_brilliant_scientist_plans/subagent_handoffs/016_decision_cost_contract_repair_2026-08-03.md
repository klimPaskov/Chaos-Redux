# Event 016 decision cost-contract repair

Date: 2026-08-03

## Scope

This narrow repair normalizes Event 016 decisions that displayed a `custom_cost_*` block alongside a regular political-power `cost`. The offline Decision Modding reference and the repository's accepted decision pattern keep the ordinary `cost` for political power and expose concrete-resource eligibility through `custom_trigger_tooltip` inside `available`.

## Changes

- Converted all 62 project-board cost displays in `common/decisions/016_brilliant_scientist_directorate_project_board.txt` to `available > custom_trigger_tooltip > hidden_trigger`, retaining each existing `can_pay_*` trigger and `*_cost` localisation key.
- Converted the high-speed materials trial, portal calibration network, and cross-domain review in `common/decisions/016_brilliant_scientist_directorate_synthesis.txt` using the same pattern. The high-speed trial retains its regular political-power cost and no longer manually debits political power a second time.
- Moved the foreign counter-program support-equipment gate into the existing requirements tooltip in `common/decisions/016_brilliant_scientist_foreign_decisions.txt`; the regular political-power cost and the existing negative equipment settlement remain intact.

## Validation evidence

- Targeted counts after the repair: project board `custom_cost_trigger=0`, `custom_cost_text=0`, `custom_trigger_tooltip=62`, `cost=72`; synthesis `0`, `0`, `3`, `3`; foreign `0`, `0`, `11`, `11`.
- Every converted custom tooltip retains its original `can_pay_*` gate and localisation key. Existing localisation already describes the concrete-resource burdens, including the foreign counter-program's 250 support equipment.
- PowerShell brace counts: project board `open=1716`, `close=1716`; synthesis `open=95`, `close=95`; foreign `open=160`, `close=160`.
- `git diff --check` was clean for the owned decision files before commit.
- No CBRN callback, model, asset, country, or event-chain behavior was changed.

## Remaining limits

Native biological stockpile reservation still requires the documented shared CBRN callback. Quantitative and live in-game decision acceptance remain open and are not claimed by this static repair.
