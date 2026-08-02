# Event 012 Africa Charter GUI inspection handoff

Date: 2026-08-02.

## Scope

Read-only inspection of `africa_charter_window` under the `default` scenario using the HOI4 GUI inspection tool. No source files, GUI tokens, sprites, decisions, or scripted GUI handlers were changed by this inspection.

## Result

The inspection returned `GUI_INSPECTED` with `status = ok` for workspace `mod_chaos_redux_ea3b2d67c2c0`. The graph is complete for the requested window (`complete = true`, `skippedSourceCount = 0`), and the scenario identifier was `default`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e62beda9df8ad399ff241163346b5542a0708bfe2c03a8dee2ad9727c1bd9ab/27885ed8baa5410f18df82fc2d104308ea8faebf22ad42cad6fdc45615cdfdde/gui-inspect.11d6e402c5d25a75.json`.

## Diagnostics and interpretation

The workspace-wide result is not a clean validation pass. It reports 1,976 blocking GUI graph diagnostics, 204 visible-overlap diagnostics, six missing fidelity elements, 54 unsupported elements, and 13 unresolved dynamic values in the complete graph. The inline response also reports unrelated vanilla/core and other-event context errors, including a missing core tiled-window texture and scripted GUI context-type errors outside Event 012.

The inspection did not identify a missing `africa_charter_window` definition or a skipped Event 012 source. Existing Event 012 handoffs continue to own the narrower runtime questions: click acceptance, state-dependent enablement, text overflow at consumer resolutions, and live in-game interaction. Those remain open because the graph tool cannot isolate all Event 012 diagnostics from the workspace-global result and live consumer validation belongs to the user.

## Follow-up

Do not treat this artifact as evidence that the Charter is presentation-complete. Keep the window registration and scripted GUI wiring in the release candidate, but retain the GUI acceptance row as `Needs Testing` until the Event 012-specific resolution and click scenarios are run and the workspace-global diagnostics are either isolated or dispositioned.
