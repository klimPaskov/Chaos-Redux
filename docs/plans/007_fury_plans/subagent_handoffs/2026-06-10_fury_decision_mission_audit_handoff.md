# Event 007 Fury Decision/Mission Audit Handoff

Date: 2026-06-10

## Files Changed

- `common/decisions/007_fury_decisions.txt`
- `common/scripted_effects/007_fury_effects.txt`
- `localisation/english/007_random_expansion_l_english.yml`

## Changed IDs

Decision and mission ids:

- `fury_garrison_the_names_mission`
- `fury_restore_the_registers_mission`

Scripted effect ids:

- `fury_garrison_the_names_success`
- `fury_garrison_the_names_failure`
- `fury_restore_the_registers_success`
- `fury_restore_the_registers_failure`
- `fury_cleanup_actor`

Country flags:

- `fury_garrison_names_recently_resolved`
- `fury_restore_registers_recently_resolved`

Localisation keys:

- Added `_blocked` and `_tooltip` companion keys for all 17 custom Fury decision cost ids used by `custom_cost_text`.

## Before And After

Before:

- `fury_garrison_the_names_mission` could immediately re-activate after a failure if the capital remained lost and registered settlement states still existed.
- `fury_restore_the_registers_mission` could immediately re-activate after success or failure while occupation crisis conditions remained true.
- Fury custom cost ids had base localisation, but missing `_blocked` and `_tooltip` companions, so blocked custom-cost display could fall through to missing or weak UI text.

After:

- `fury_garrison_the_names_mission` sets a 75-day resolved cooldown on success or failure and checks it in activation.
- `fury_restore_the_registers_mission` sets a 60-day resolved cooldown on success or failure and checks it in activation.
- Fury actor cleanup clears both new timed mission cooldown flags.
- All custom cost ids used by Fury and anti-Fury decisions have normal, blocked, and tooltip localisation.

## Why This Is Bounded

The patch only changes existing Fury decision/mission lifecycle guards and existing localisation cost companions. It does not add a new decision family, new target logic, new event chain, broad balance model, scripted GUI, or formable behavior.

## Validation

Ran scoped checks over Fury decision, category, effect, trigger, constant, idea, event, localisation, and GFX files:

- brace balance remained zero for all audited Fury script files
- 17 `custom_cost_text` ids all have base, `_blocked`, and `_tooltip` localisation
- 24 visible Fury decision/category ids all have name and `_desc` localisation
- all Fury decision/category icon references resolve to `interface/007_fury.gfx` sprite definitions
- `007_random_expansion_l_english.yml` remains UTF-8 with BOM
- no `<=` or `>=` syntax found in the scoped Fury files

## Remaining Issues And Risks

- The Fury category is AI-first, and several actions remain intentionally visible if a player tag-switches into a Fury actor. Ordinary selection still excludes player-linked countries through `fury_can_be_selected` and `fury_is_valid_target`.
- Anti-Fury missions are intentionally capital-hold timers rather than state-targeted border missions. They are functional, but more regional specificity would require a larger design pass outside this narrow patch.
- `anti_fury_staff_talks_active` remains a one-shot persistent blocker until Fury cleanup, matching its current persistent idea behavior.
