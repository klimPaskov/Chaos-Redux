# Legacy humanitarian cost quote projection

Source: [humanitarian_legacy_cost_effects.txt](humanitarian_legacy_cost_effects.txt).
Tuning: [humanitarian_legacy_cost_constants.txt](../script_constants/humanitarian_legacy_cost_constants.txt).
Fresh affordability: [humanitarian_legacy_cost_triggers.md](../scripted_triggers/humanitarian_legacy_cost_triggers.md).

## `humanitarian_project_legacy_cost_quote`

Purpose: project the 15 positive nominal legacy fees into existing country-local display context.
Scope: COUNTRY, namely the country whose decision row or tooltip will display the quote.
Inputs: no caller-provided inputs, variables, parameters, flags or event targets.
The helper reads the 15 fresh positive `humanitarian_legacy_cost` constants.
Outputs: 15 normal country variables named `humanitarian_cost_quote_<key>`.
The complete key set is `pp_light`, `pp_standard`, `pp_heavy`, `train_light`, `train_heavy`, `convoy_light`, `convoy_heavy`, `support_light`, `support_heavy`, `infantry_light`, `infantry_heavy`, `fuel_light`, `fuel_heavy`, `transport_planes`, and `air_xp`.
Each output equals its corresponding positive constant in native resource units.
There are no temporary scalar/array return values or caller-owned output storage requirements.
Defaults: none, because every quote is assigned explicitly and no missing caller data is inferred.
Side effects: overwrites those 15 normal display variables on the current country only.
Repeated calls are idempotent at unchanged tuning and repair missing or stale quotes.
It never charges resources, checks action eligibility, changes policy, reveals a category, moves people, grants services, registers a price source or writes paid receipts.

Cached quotes must never govern affordability, payments, refunds or receipt matching.
Those paths consume fresh central constants and the pure inclusive predicates.
The parent owns calls from the existing bounded `famine_refresh_decision_phase_from_country` and `migration_refresh_decision_phase_from_country` paths and any existing registration seam needed for first visible quotes.
This file adds no timer, on-action hook, global registry, periodic scan or public metric.
The normal variables persist on each country, and a later bounded projection overwrites them.
No cleanup event target or flag is created.
The quote fields may remain when a category closes because they carry no pending work, grants, actor identity or eligibility.

## Usage

```text
# Current COUNTRY phase/registration scope.
humanitarian_project_legacy_cost_quote = yes
```

The corresponding existing YML key may display `[?humanitarian_cost_quote_pp_standard|.0]` after parent-owned localisation integration.
Formatting and texticons stay in localisation consumers.
This helper is not a payment quote cache or a dynamic named-argument API.

## References and limits

The existing bounded projection precedent is `migration_decision_phase_effects.txt:6-17`.
Installed `documentation/script_concept_documentation.md:216-245` documents shared fixed-point constants and scoped-variable support.
Installed `common/script_constants/documentation.md` documents the required first-entry schema.
Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:435-449` distinguishes normal scoped variables from temporary storage.
Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:4683-4715` documents `= yes` scripted-effect calls.
The implementation handoff records source-level tests and the outstanding native parser, MCP and probability comparison limits.
No assets or icons are introduced, and the existing humanitarian cost texticons remain parent-owned consumers.
