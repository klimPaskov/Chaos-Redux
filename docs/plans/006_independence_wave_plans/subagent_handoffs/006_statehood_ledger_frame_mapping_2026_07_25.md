# Event 006 Statehood Ledger semantic frame mapping handoff

Date: 2026-07-25.

Scope: bounded repair of the parent-owned Statehood Ledger GUI wiring. No
country package, portrait, advisor, focus, decision, event, or audio surface was
changed.

## Change

The four authored ASSET-040 through ASSET-043 sheets contain semantic states,
not a safe persistent loop. The ledger now selects one frame from each sheet
using `common/script_constants/006_independence_wave_gui_constants.txt`, the
country-scoped `independence_wave_refresh_status_frame_state` effect, and the
scripted-GUI `properties` block. Recognition follows the five recognition
thresholds; dependency follows patron warning and severe-instability state;
league follows the global charter phase; and formable follows hidden,
discovered, eligible, and committed transaction state.

The prior free-running animation sprites remain registered as transition-only
hooks. They are no longer shown by the persistent readout, so a country cannot
display an unrelated danger, vote, or proclaimed frame while its live ledger is
calm, drafting, or undiscovered.

Origin cleanup now clears all five tab flags and the four cached frame variables,
preventing a stale tab or frame from leaking into a later Event 006 generation.

## Files

- `common/script_constants/006_independence_wave_gui_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_guis/006_independence_wave_scripted_gui.txt`
- `interface/006_independence_wave.gfx`
- `interface/006_independence_wave.gui`
- `docs/assets/006_independence_wave/manifest.md`
- `docs/events/006_independence_wave/overview.md`

## Validation

- `hoi4_gui_inspect` targeted `independence_wave_status_window` with scenario
  `independence_wave_status_default`: `GUI_INSPECTED`, status `ok`.
- `hoi4_gui_render` targeted the same window at 1920x1080 and 1280x720 across
  normal, warning, active, and long-text states: `GUI_RENDERED`, 24 artifacts.
- The returned MCP report still carries the repository-wide diagnostic ceiling
  and reports 10 global `GUI_STATE_COVERAGE_MISSING` entries; those are not
  treated as an Event 006 pass. The focused source now has explicit state-strip
  frame selection and cleanup evidence.

## Remaining boundary

The authored strips are still not a complete persistent animation consumer;
their free-running siblings are deliberately transition-only until a transition
trigger and state-specific motion package are authored. This handoff does not
claim whole-event completion or close the broader Event 006 GUI/runtime audit.
