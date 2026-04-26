# chaosx_dynamic_triggers

This file documents reusable dynamic scripted triggers from `common/scripted_effects/chaosx_dynamic_triggers.txt`. The point of these triggers is to keep complex variable/meta logic centralized so events can call one reusable block instead of duplicating large script chunks.

## Reuse guidance

Before adding new dynamic logic, check this file and reuse an existing effect if it already matches the behavior. If no effect matches, create a new one in `chaosx_dynamic_effects.txt` and document it here in the same change with: purpose, scope, inputs, defaults, outputs, side effects, and example usage.

## Table of contents

- [is_desert_state](#is_desert_state)
- [is_special_chaos_country](#is_special_chaos_country)
- [is_actual_nonhuman_country](#is_actual_nonhuman_country)

## is_desert_state

## is_special_chaos_country

Country-scope trigger. Returns true for system actors and special scenario countries that should not be treated like normal civilian societies.

Current coverage includes:

- `ZZZ`
- dynamic zombie outbreak countries
- weaponized zombie outbreak countries
- `ZIN`
- `THR` / countries using the `The Holy Realm` cosmetic tag

## is_actual_nonhuman_country

Country-scope trigger. Returns true only for countries that should currently be treated as actually nonhuman rather than merely unusual or scenario-specific.

Current coverage includes:

- `ZZZ`
- dynamic zombie outbreak countries
- weaponized zombie outbreak countries
- `ZIN`
