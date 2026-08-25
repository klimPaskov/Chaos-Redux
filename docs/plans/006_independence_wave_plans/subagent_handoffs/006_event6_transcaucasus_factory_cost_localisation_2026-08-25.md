# Event 006 Transcaucasus factory-cost localisation handoff

Date: 2026-08-25

## Scope

The four Transcaucasus decision cost strings that displayed a literal civilian-factory amount now read `constant:independence_wave_decision_cost.civilian_factory_light`:

- `independence_wave_transcaucasus_cost_geo_port_customs`
- `independence_wave_cost_iw070_depots`
- `independence_wave_cost_iw071_rail`
- `independence_wave_cost_iw072_rail`

The decisions continue to reserve one civilian factory through their existing `modifier = { civilian_factory_use = @CR_SC_TRANSCAUCASUS_CIVILIAN_FACTORY_USE }` blocks. Only the display source changed; triggers, payment effects, project timers, AI weights, package gates, and FORM-16 admission are untouched.

The blocked variants wrap the same base strings, so their red disclosures remain synchronized automatically.

## Validation

- The localisation file retains its UTF-8 BOM.
- No `£civ_factory 1` literal remains in the Transcaucasus localisation file.
- All four cost keys and their blocked/tooltips remain present.
- Existing Event 006 allocator, country API, scenario, flag, FORM-16, and Statehood Ledger static audits remain passing.
- No live tooltip or gameplay claim is made here.
