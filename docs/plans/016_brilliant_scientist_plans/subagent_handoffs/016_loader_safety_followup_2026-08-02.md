# Event 016 loader-safety follow-up

Date: 2026-08-02

## Scope

This bounded correction makes remaining Event 016 core declarations use engine-supported forms without changing project costs, rewards, routes, or model contracts. It is a loader-safety tranche, not a new gameplay route or a whole-event completion claim.

## Corrections

- Replaced static resource, manpower, political-power, experience, and accident-pressure comparisons that used direct relational syntax with `check_variable` comparisons where the affected field is loader-sensitive.
- Replaced four remaining Event 016 `while` effects with the vanilla-compatible `while_loop_effect` form.
- Corrected the Directorate scripted-localisation database key from `localisation_key` to `localization_key` on the affected outputs.
- Moved the cross-domain review cost tooltip into its `complete_effect` block so it is emitted by the decision's supported effect surface.

## Validation

All fifteen touched source files have balanced braces and no `<=` or `>=` operators. The diff is clean under `git diff --check`. The affected changes are value-preserving or syntax-only; no model, entity, unit-provider, event-log, catalog, or asset reference was added. No game launch or live save validation was performed.

## Remaining boundary

Quantitative campaign balance, live GUI and event playback, Event 019 lifecycle scenarios, broader country flavour, and the seven user-deferred 3D packages remain outside this tranche.
