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

Nuclear and thermonuclear strikes also add direct chaos through the shared nuclear-use ladder documented in `docs/systems/nuclear_chaos_ladder.md`; that direct gain is separate from any later deaths-to-chaos contribution.

## State Population Impact

When a death source is marked as civilian/state-linked, the state scope receives a negative `add_manpower` delta.

This decreases state population directly rather than only changing recruitable manpower modifiers.

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
- `rebuild_chaos_meter_deaths_view`
- `process_chaos_meter_country_deaths_totals_rebuild`

Country totals are now maintained on country-scoped variables and the deaths view backfills legacy saves through bounded chunked rebuild passes instead of scanning the full raw history in one UI refresh.

Biowarfare helper:

- `bio_register_state_civilian_deaths`

Chemical helper:

- `chem_register_state_civilian_deaths`

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
