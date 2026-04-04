# chaosx_dynamic_triggers

This file documents reusable dynamic scripted triggers from `common/scripted_effects/chaosx_dynamic_triggers.txt`. The point of these triggers is to keep complex variable/meta logic centralized so events can call one reusable block instead of duplicating large script chunks.

## Reuse guidance

Before adding new dynamic logic, check this file and reuse an existing effect if it already matches the behavior. If no effect matches, create a new one in `chaosx_dynamic_effects.txt` and document it here in the same change with: purpose, scope, inputs, defaults, outputs, side effects, and example usage.

## Table of contents

- [is_desert_state](#is_desert_state)
- [is_special_chaos_country](#is_special_chaos_country)
- [is_actual_nonhuman_country](#is_actual_nonhuman_country)
- [mapmode_state_has_chemical_contamination](#mapmode_state_has_chemical_contamination)
- [mapmode_state_has_disease_contamination](#mapmode_state_has_disease_contamination)
- [mapmode_state_has_nuclear_contamination](#mapmode_state_has_nuclear_contamination)
- [mapmode_state_has_tracked_contamination](#mapmode_state_has_tracked_contamination)
- [mapmode_state_has_civilian_death_history](#mapmode_state_has_civilian_death_history)

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

## mapmode_state_has_chemical_contamination

State-scope trigger. Returns true when the state has the active `chem_state_contamination` dynamic modifier.

Use this for UI, tooltips, or logic that needs a single reusable check for chemical state contamination without repeating the modifier token.

## mapmode_state_has_disease_contamination

State-scope trigger. Returns true when the state has any tracked biological outbreak modifier:

- `anthrax_contaminated_state`
- `plague_contaminated_state`
- `tularemia_contaminated_state`
- `smallpox_contaminated_state`

Use this when the distinction that matters is "any disease contamination" rather than the exact disease.

## mapmode_state_has_nuclear_contamination

State-scope trigger. Returns true when the state has the active `nuclear_fallout_state` dynamic modifier.

## mapmode_state_has_tracked_contamination

State-scope trigger. Aggregates the chemical, disease, and nuclear contamination triggers above.

Use this as the main target filter for contamination-focused state UI so one place controls which hazards count as tracked contamination.

## mapmode_state_has_civilian_death_history

State-scope trigger. Returns true when the state has a positive cumulative `chaos_state_civilian_deaths_total` variable.

This is intended for map and UI systems that need persistent state-level civilian death history rather than short-lived daily effects.
