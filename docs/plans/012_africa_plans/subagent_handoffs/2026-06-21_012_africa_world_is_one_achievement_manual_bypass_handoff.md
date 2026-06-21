# 012 Africa World Is One Achievement Manual-Scenario Guard Handoff

Date: 2026-06-21

## Scope

This patch keeps the manual `SCN-008` World Is One triggerable scenario from satisfying the ordinary-route terminal Africa achievements.

## Files changed

- `common/achievements/chaos_redux_achievements.txt`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`

## Achievement ids

- `ACH_AFR_CHARTER_HAS_TOO_MANY_SIGNATURES`
- `ACH_AFR_WORLD_IS_ONE_ONLY_AFTER_AFRICA`
- `ACH_AFR_WORLD_IS_ONE`

## Implementation

`africa_apply_triggerable_world_is_one_opening` sets `africa_triggerable_scenario_world_is_one` before it prepares the external proof chain and calls `africa_force_triggerable_world_is_one_terminal`. Those helper effects intentionally set terminal flags for the manual scenario, so the three ordinary-route terminal achievements now include:

```txt
NOT = { has_country_flag = africa_triggerable_scenario_world_is_one }
```

The achievement tooltips say the player must enter World Is One through the ordinary route.

## Validation targets

- Confirm the three terminal achievement blocks contain the manual-scenario rejection.
- Confirm localisation remains UTF-8 with BOM.
- Confirm the achievement file remains brace-balanced.
- Run `git diff --check` before commit.

## Remaining risk

This closes only the manual-scenario achievement bypass. It does not prove the ordinary `AFR_the_world_is_one` focus route is live-validated, nor does it close the broader Event 012 GUI, asset, balance, country-package, spreadsheet, and completion-audit blockers.
