# Event 012 Africa Dynamic Unit Creation Scope Handoff

## Changed Files

- `common/scripted_effects/012_africa_effects.txt`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_dynamic_unit_creation_scope_handoff.md`

No changes were needed in `common/scripted_triggers/012_africa_triggers.txt` or `common/script_constants/012_africa_constants.txt`.

## Helper IDs And Call Sites

Inspected dynamic `create_unit` helper surface:

- `africa_create_continental_guard_divisions`
  - Calls `africa_calculate_continental_guard_count`
  - Creates `Continental Charter Guard`
  - Call sites found in `common/scripted_effects/012_africa_effects.txt`
- `africa_create_continental_guard_reinforcement_divisions`
  - Calls `africa_calculate_continental_reinforcement_count`
  - Creates `Border Liberation Column`
  - Call sites found in `common/scripted_effects/012_africa_effects.txt` and `common/decisions/012_africa_decisions.txt`
- `africa_create_authority_guard_divisions`
  - Calls `africa_calculate_authority_guard_count`
  - Creates `Charter Authority Guard`
  - Call sites found in `common/scripted_effects/012_africa_effects.txt`
- `africa_create_authority_guard_reinforcement_divisions`
  - Calls `africa_calculate_authority_reinforcement_count`
  - Creates `Charter Authority Relief Guard`
  - Call sites found in `common/national_focus/012_africa_authority_focus.txt`
- `africa_create_high_chaos_guard_divisions`
  - Calls `africa_calculate_high_chaos_guard_count`
  - Creates `Bestiary Seat Guard`
  - Call sites found in `common/scripted_effects/012_africa_effects.txt`
- `africa_create_high_chaos_guard_reinforcement_divisions`
  - Calls `africa_calculate_high_chaos_reinforcement_count`
  - Creates `Bestiary Relief Guard`
  - Call sites found in `common/national_focus/012_africa_authority_focus.txt` and `common/decisions/012_africa_decisions.txt`

## Before And After Behavior

Before:

- The two continental guard `create_unit` blocks spawned in `capital_scope` with `count = var:PREV.africa_*_divisions_to_spawn` and `owner = ROOT`.
- The four authority/high-chaos guard blocks spawned in `capital_scope` with the same scoped-variable count pattern and `owner = PREV`.

After:

- The two continental guard `create_unit` blocks still use the same dynamic spawn counts, but now use `owner = PREV`.
- All six Event 012 dynamic unit creation helpers now tie the unit owner to the country whose `capital_scope` is active.
- Current direct behavior should be unchanged at existing call sites where `ROOT` and the helper country are the same. The patch prevents future nested calls from accidentally assigning continental units to an outer root country.

## Parser Evidence And Validation

- Read the required offline wiki pages and vanilla documentation for scripted effects/triggers, variables, scopes, and `create_unit`.
- Vanilla documentation lists `create_unit count = <int>`, but vanilla game files use the dynamic form directly:
  - `events/TAOG_Indonesia.txt` uses `count = var:PREV.INS_automatic_militias_var_for_target`.
  - `common/scripted_effects/SOV_scripted_effects.txt` uses `count = var:PREV.civil_war_army_size`.
- Event 012 constants clamp all six dynamic spawn counts to positive minimums:
  - `initial_guard_min = 2`
  - `continental_reinforcement_min = 1`
  - `authority_guard_min = 1`
  - `authority_reinforcement_min = 1`
  - `high_chaos_guard_min = 1`
  - `high_chaos_reinforcement_min = 1`
- Targeted grep after the patch confirms all six Event 012 guard `create_unit` blocks still use `count = var:PREV.africa_*` and all six use `owner = PREV`.

## Remaining Parser And Live Risks

- I did not replace `count = var:PREV...` with `meta_effect` or looped one-unit spawns because vanilla uses the exact scoped-variable count pattern. Replacing it would add complexity without reducing a demonstrated parser risk.
- I did not run the HOI4 executable or live in-game validation from this subagent pass. The remaining uncertainty is normal live-engine behavior: whether every call site reaches a valid capital state at the moment the helper runs.
- The helper assumes the scoped country exists and has a valid `capital_scope`. The inspected call sites appear to call these helpers from country scopes, but this pass did not audit every possible campaign state that can make a capital invalid.

## Blockers

- No blocker found for the narrow scripted-helper patch.
