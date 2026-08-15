# Event 006 generation-reset route-exclusion cleanup

## Disposition

Source-level lifecycle hardening is complete for shared route-exclusion markers. The central generation reset and active-origin end path now clear the radical-sovereignty, traditional, emergency-military, popular-council, and patron-client exclusion flags. These markers are generation-local package state and must not survive a defensive reset or a reused Event 006 origin.

## Changed surface

- `common/scripted_effects/006_independence_wave_effects.txt`
  - `independence_wave_reset_current_generation` clears all five shared route-exclusion markers.
  - `independence_wave_end_active_origin` clears the same five markers during origin teardown.
  - Existing package-specific cleanup remains unchanged; the central clears are defensive fallbacks.

## Validation

- Static source scan confirms each of the five markers has central reset and end-path cleanup.
- Existing Event 006 allocator, scenario-matrix, strict-flag, GUI-matrix, and country-tag audits remain the relevant repository checks; no package admission or Join order changed.
- A fresh Event 006 MCP trace was attempted after the edit and remains blocked before source scanning by `ARTIFACT_MANIFEST_INVALID` (`Artifact provenance manifest is invalid`) for workspace `mod_chaos_redux_ea3b2d67c2c0`.

## Scope and limits

No new package was admitted, no attestation or deterministic Join list was widened, and no live save/load or in-game validation is claimed. Whole Event 006 remains HOLD/PARTIAL under the current authority and MCP provenance outage.
