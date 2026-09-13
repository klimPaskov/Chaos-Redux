# Event 028 mineral index trigger repair

Disposition: implemented, with partial MCP evidence and runtime validation unresolved.
Acceptance basis: the parent authorized a bounded startup repair of the twelve invalid mineral index triggers, without changing selection, tuning, cleanup, or helper calls.

## Changes and proof

- Changed `common/scripted_effects/028_asteroid_incoming_runtime_effects.txt` at lines 1745–1750 and 1767–1772 inside `asteroid_incoming_refresh_mineral_control`.
- Wrapped each existing `asteroid_incoming_mineral_site_index = constant:asteroid_incoming_runtime.fragment_slot_*` equality in `check_variable = { ... }`.
- Saved the exact pre-edit source in `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event28_index14/028_asteroid_incoming_runtime_effects.txt`.

The parent-supplied `logs/launch_13/logs/error.log` contains 24 `Invalid trigger` entries for these twelve lines, plus their associated `Unknown trigger-type` messages.
The engine was interpreting the bare variable name as a trigger type.
The documented short equality form makes the existing expression a variable comparison.

Both loops reset the temporary index to `constant:asteroid_incoming_runtime.zero` and increment it once per entry in `global.asteroid_incoming_fragment_site_states`.
The six slot constants are the integers 1 through 6, and the increment is 1.
The first loop assigns matching `asteroid_incoming_fragment_1_controller` through `asteroid_incoming_fragment_6_controller` global event targets.
The second loop grants the matching `asteroid_incoming_fragment_material_1` through `asteroid_incoming_fragment_material_6` ideas while minerals are active.
Each existing `CONTROLLER = { exists = yes }` guard remains alongside the equality.
The index is a temporary variable and therefore retains its unqualified access inside the state loop.

This helper dispatches over an already populated fragment array.
The repaired conditions do not select random targets or alter a weighted pool, so no weighted surface was patched and no probability baseline was required.

## Documentation and unchanged contracts

References consulted include AGENTS.md, the events and subagent skills, the eleven mandatory offline wiki pages, and the shared dynamic effect registry and its documentation.
The specific syntax evidence is `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, its `check_variable` entry, and installed vanilla `documentation/triggers_documentation.md` lines 2110–2132.
Installed vanilla `common/scripted_effects/GER_scripted_effects.txt` lines 2115 and 2121 demonstrate the same short equality form in effect limits.
Vanilla effect documentation for temporary variables and global event targets, plus both script constant documentation files, support the existing surrounding contracts.

No helper was added or extracted.
Existing helper scope, inputs, outputs, side effects, and call sites remain unchanged apart from the supported comparison syntax documented above.
No constants, tuning values, cleanup logic, target lifecycle, localisation, assets, or catalog facts changed.
This handoff documents the repair without expanding the shared helper registry.

## Validation and MCP evidence

An exact inverse replacement recovered the entire pre-edit text, proving that all twelve changes consist solely of the `check_variable` wrappers.
Manual source review verified the two six-slot dispatch sequences against their controller target and material idea suffixes, including the unchanged controller guard and mineral activation gate.

Backup SHA-256: `36991AFDB22367979DE9B1DCF2F4F16275F4636D4A9F6969D660C82E9A44568D`.
Post-edit SHA-256: `2E8E3DAE0DC5D35805E015C4580A41C8B770D79A5E4F2567364DA9801459B46E`.

`hoi4.event_inspect` used selector `{ kind: "event", eventId: "chaosx.nr28.1" }`, trace depth 2, 12 nodes, 20 edges, and helper expansion disabled.
It returned `EVENT_INSPECTED_PARTIAL`, revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`, graph hash `c6850dd8ad35035c9a83ff251c3df14e4e6123af303e2037d032ccbf5ea51b2e`.
Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e6f3595aa99ca36f331a8ded410e6c9d539dacee55797ed0662289423a0dacff/3aa77ba389fdd06908cfaab723a100ac6573d39de0293c355a6230edfcea1766/event-trace-1102e50fad94.json`.

`hoi4.event_render` used the same event selector with neighborhood depth 1 and 8 nodes.
It returned `EVENT_RENDERED_PARTIAL` with layout hash `28ffd45c3917c970256db6dbcb75ebee376826e79936f7abfafe78c99791d05b`.
Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/807dda439b98dafcd0267400f5f1865edb3585a8a0bc00cb7508b24c4808d8d3/555d116d3efcde4cc5bdbbacb51b0d9887d6ef3fe765ebdf9b716d603f90a621/event-neighborhood-1102e50fad94-manifest.json`.

Both successful routes reported `validation.passed = false` because large-workspace analysis deferred workspace-wide helper projections and lifecycle passes.
The focused event evidence does not prove this helper's runtime evaluation.
The subsequent `hoi4.event_compare` call with the recorded baseline revision and `refresh = true` returned `EVENT_REVISION_NOT_CACHED`, stating that the requested event graph revision is not cached.
No successful MCP before-and-after comparison or full engine validation is claimed.
Initial selector and comparison schema probes were rejected before analysis, then corrected to the accepted argument shapes described above.

## Simplifications, omissions, and blockers

No gameplay simplification or fallback was made.
MCP comparison remains blocked by the missing cached revision, and the available event inspection and render are partial.
The game was not launched, and disappearance of the startup errors has not been verified in a live session.
No commit was created, as the parent explicitly retained that responsibility.
The parent should review this bounded source delta and carry these validation limits into its final report.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skills were created or changed.
