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


# Paid evolution incident resolutions

The former `006_independence_wave_evolution_incident_effects.txt` registry is consolidated into the canonical effect file below. Its public effect identifiers and option behavior remain unchanged.

`common/scripted_effects/006_independence_wave_evolution_effects.txt`
# Event 006 evolution incident effects

## Purpose

These effects resolve the five shared Independence Wave evolution incident families after a paid decision opens its country event. They keep the visible outcome on the canonical country, former-host, Network, League, and revisionist-pressure ledgers.

## Scope and inputs

- Scope is the active Event 006 country receiving `chaosx.nr6.360` through `chaosx.nr6.364`.
- The caller supplies no external country target. Former-host changes are applied only when `has_independence_wave_living_former_host` is true.
- The options use temporary `independence_wave_decision_*_delta` values consumed by the existing country, host, and League transaction helpers.
- Revisionist outcomes use temporary `independence_wave_incident_revisionist_delta` with `independence_wave_change_revisionist_pressure`.

## Side effects

Each option clears its pending flag, sets one generation-scoped outcome flag, applies the selected ledger deltas, and may set a concrete identity, command, congress, sovereignty, or League-discredit flag. Generation reset and origin cleanup clear those flags. No effect creates political power, free units, tags, or advisor assets.

## Usage example

```text
option = {
	name = chaosx.nr6.364.a
	independence_wave_resolve_open_synchronized_claims = yes
}
```
