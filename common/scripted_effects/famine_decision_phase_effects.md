# Famine decision phase effects

## `humanitarian_refresh_decision_phase_from_country`

This legacy scheduler entry point is a neutral compatibility dispatcher. It calls `famine_refresh_decision_phase_from_country` and `migration_refresh_decision_phase_from_country` in sequence and owns no lifecycle flag.

## `famine_refresh_decision_phase_from_country`

Scope: COUNTRY.

The famine owner reads only already-published food-security state facts (`famine_food_security_active`, `famine_food_stage_famine`, and `famine_food_stage_catastrophic`). A starting save with a real food problem therefore receives an independent famine phase even when the migration registry is empty.

The helper sets `famine_decision_emerging` for a first observed crisis, promotes a returning `famine_decision_resolution` to `famine_decision_active` when food pressure returns, and retires an already-observed resolution to `famine_decision_dormant` only after food crisis and famine relief mission facts are clear. It never reads cohort arrays, reception load, flight, trapped population, or migration lifecycle flags.

The dispatcher remains reachable from the existing registered-country scheduler without adding a recurring world scan. The famine category also has a direct sparse-state reveal fallback for a real starting problem.

At the same country-local boundary, `humanitarian_project_legacy_cost_quote` refreshes the 15 display-only legacy fee amounts from central tuning.
The exact active-state registration also projects those quotes to its valid owner and, when different, valid controller so a first visible targeted action has country-scoped text values.
These assignments reveal no category and grant no food, resources, services, capacity or paid work; fresh cost predicates and central debit values remain payment authority.

No localisation, icon, or scripted-GUI key is owned by this helper.
