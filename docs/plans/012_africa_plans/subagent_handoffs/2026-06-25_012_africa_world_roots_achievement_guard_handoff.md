# Event 012 World Roots Achievement Guard Handoff

Date: 2026-06-25

## Scope

Local parent audit after subagent token failures. This patch closes one static manual-scenario bypass risk in the Event 012 achievement layer.

## Files Changed

- `common/achievements/chaos_redux_achievements.txt`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`

## Finding

The manual `SCN-008` World Is One scenario intentionally seeds external proof flags and world-order readiness through `africa_apply_triggerable_world_is_one_opening`. The three terminal World Is One achievements already reject `africa_triggerable_scenario_world_is_one`, but `ACH_AFR_WORLD_HAS_ROOTS` could combine a pre-existing Nature Courts route with those seeded proof flags.

## Implemented

`ACH_AFR_WORLD_HAS_ROOTS` now rejects countries marked with `africa_triggerable_scenario_world_is_one`. Its tooltip describes the ordinary-route requirement.

## Remaining Risk

This is static achievement-bypass hardening, not live route proof. Ordinary World Is One validation, exploit checks, GUI render proof, achievement route proof, and spreadsheet final status remain open.
