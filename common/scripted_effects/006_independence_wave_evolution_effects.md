# Event 006 evolution feedback effects

These effects keep the five-stage evolution state aligned with the reusable Independence Wave allocator without creating a second origin system.

## `independence_wave_clamp_replicable_opening_confidence`

- Scope: global or country scope that can address global variables.
- Inputs: none.
- Output: initializes and clamps `global.independence_wave_replicable_opening_confidence` to the centralized 0–100 range.
- Side effects: none beyond the global value.

## `independence_wave_record_evolution_feedback`

- Scope: country or transaction callback scope.
- Inputs: temporary `independence_wave_evolution_feedback_delta` and `independence_wave_evolution_feedback_type_input`.
- Output: applies the delta to the global Replicable Independence opening-confidence value.
- Side effects: increments `global.independence_wave_evolution_feedback_count` and records the last feedback type/date.

## `independence_wave_record_evolution_failure_feedback`

- Scope: active Event 006 country.
- Inputs: current lifecycle failure flags and the global league phase.
- Output: records copied-institution, dormant-identity, armed-border, congress, and open-sovereignty feedback once per generation or once per shared congress incident.
- Side effects: sets generation-safe witness flags and updates the global opening-confidence value.

## `independence_wave_record_origin_loss_feedback`

- Scope: active Event 006 country at an on-action transaction boundary.
- Inputs: temporary feedback type and delta for annexation, puppetry, or capitulation.
- Output: records one origin-loss penalty for the current generation.
- Side effects: sets a generation-safe witness flag. Annexation callers then invoke `independence_wave_end_active_origin` separately.

The effects do not iterate over all countries. The normal country refresh hook and the narrow `on_annex`, `on_puppet`, and `on_capitulation` callbacks are the only runtime entry points.
