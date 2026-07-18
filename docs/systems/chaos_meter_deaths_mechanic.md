# Chaos Meter Deaths Mechanic

## What This Adds

This mechanic introduces a global deaths tracker tied to war-crime style systems and large-scale warfare pressure.

It tracks:

- civilian deaths,
- military casualties,
- combined total deaths,
- a recent changes log.

The deaths total contributes directly to chaos:

- every `1,000,000` additional tracked deaths adds `+1` chaos.

## Sources of Deaths

Deaths are currently registered from:

1. Global military casualty growth (from country casualties aggregation).
2. Strategic bombing recency in states.
3. Chemical contamination application and monthly chemical contamination state effects.
4. Biowarfare contamination application (anthrax/plague/tularemia/smallpox) and monthly outbreak state effects.
5. Nuclear and thermonuclear strikes.
6. Genocide crisis camp, gulag, experiment-site, biowarfare experiment-site, and restricted chemical site monthly processing.
7. Event 20 Black Plague state mortality through the exact state-population transaction.
8. Fallout's one-time grade-based state loss through an observed post-mutation Deaths transaction.
9. Event 19 ghost-derivative decline through its long-cadence exact state-population transaction.

Nuclear and thermonuclear strikes also add direct chaos through the shared nuclear-use ladder documented in `docs/systems/nuclear_chaos_ladder.md`; that direct gain is separate from any later deaths-to-chaos contribution.

## State Population Impact

When a death source is marked as civilian/state-linked, the shared transaction applies one negative state-scope `add_manpower` delta. Because the engine also credits recruitable manpower when this effect is negative, the transaction snapshots the state's owner and distinct controller, measures their actual `manpower_k` change, and removes only an observed positive credit. This decreases real state population without deliberately granting military reserves and remains safe for occupied states without assuming which country the engine credits.

The official effect surface exposes no population-only replacement. If an engine build does not expose its recruitable credit through `manpower_k` in the same effect chain, the script does not guess an amount or recipient; this residual engine behavior remains a validation risk rather than a hidden compensation assumption.

Fallout uses a stricter order because its world rewrite must be idempotent across phase-event retries. It calculates intent from frozen population and grade, clamps the commit against live population, writes a mutation-issued flag, and calls the population-only helper once. It then reads the live population difference. Only an exact observed result is registered through `chaos_meter_register_deaths`, with `chaos_deaths_apply_state_pop` set to zero. The optional `chaos_deaths_record_state_ledger` input records that observed amount in the state Deaths map ledger without mutating population again. A mismatch leaves the Fallout blackout active and never receives a Deaths entry.

## UI Integration (Chaos Meter)

A fifth tab was added: `Deaths`.

Top section:

- total deaths,
- civilian deaths,
- military casualties,
- chaos generated from deaths,
- latest change.

Bottom section:

- separator line,
- scrollable country totals list with each country's latest recorded update,
- no per-country drilldown log overlay in the deaths view.

## Script Integration

Primary scripted effects:

- `chaos_meter_register_deaths`
- `record_chaos_meter_deaths_log_entry`
- `chaos_meter_sync_chaos_from_deaths_delta`
- `chaos_meter_record_state_civilian_deaths_from_deaths_change`
- `rebuild_chaos_meter_deaths_view`
- `process_chaos_meter_country_deaths_totals_rebuild`
- `apply_state_population_loss_without_recruitable_manpower_gain`
- `apply_exact_state_civilian_population_loss`
- `fallout_apply_state_population_loss`

Country totals are now maintained on country-scoped variables and the deaths view backfills legacy saves through bounded chunked rebuild passes instead of scanning the full raw history in one UI refresh.

Biowarfare helper:

- `bio_register_state_civilian_deaths`

Chemical helper:

- `chem_register_state_civilian_deaths`

Genocide crisis helpers:

- `genocide_apply_monthly_concentration_state_effects`
- `genocide_apply_monthly_extermination_state_effects`
- `genocide_apply_monthly_gulag_state_effects`
- `genocide_apply_monthly_experiment_site_effects`
- `genocide_apply_monthly_biowarfare_experiment_site_effects`
- `genocide_apply_monthly_restricted_chemical_site_effects`

These helpers route state population loss through the same Chaos Meter Deaths pipeline used by chemical and biological contamination systems.

Fallout uses Deaths reason `19`, `fallout_aftermath`. Its recorded losses use the normal `1` chaos per `1,000,000` deaths conversion. Stored before, after, and delta receipts cover the global Deaths total, Deaths log sequence, and state Deaths ledger. When the optional Deaths display is disabled, the exact state mutation still occurs and the receipt records a disabled accounting outcome with zero Deaths-ledger movement.

Event 19 ghost decline uses Deaths reason `20`, `infantry_spawn_ghost_decline`,
and a `0.10` deaths-to-chaos weight. It records the real population loss once
through the shared pipeline while keeping the cause separate from Event 10's
`death_consumption` attribution and progression.

## Icons and GFX Wiring

No new sprites are required for this feature.

The deaths tab reuses existing UI assets:

- window and entry backgrounds from `interface/chaosx.gfx`,
- existing sort/tab button sprites already used by the chaos meter.

If custom art is wanted later, add sprites in:

- `gfx/interface/`

and register names in:

- `interface/chaosx.gfx`

## Future Plans

1. Add filter/sort controls for death log reasons and magnitude.
2. Add per-country attribution in the deaths log where source context is available.
3. Add adjustable balancing constants for source-specific death curves by war phase.
4. Add decision/event systems that can reduce civilian deaths at economic/political cost.
