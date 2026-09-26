# GUI date and controller request qualification

Disposition: implemented for the live MCP schema and one declared source fixture; full interaction and engine evidence remains unresolved.
Acceptance basis: the user's request to fix explicit GUI date/controller rejection and retain honest source evidence.

The built `hoi4-agent-tools` 3.5.0 server accepted `hoi4.gui_inspect` and `hoi4.gui_render` over stdio for `repression_ledger_window`.
The request declared `date = 1944.6.1` and `controls = { "88": "GER" }` in the scenario.
`generatedScenarios = { enabled: false }` belongs at the tool request root alongside `scenario`.
The exact request, source revision, fixture hash, server identity, response summary, and PNG hashes are in [qualification.json](qualification.json).
The archived PNG bytes match the hashes returned by the MCP.

The [cropped render](repression_ledger_window-cropped.png) was visually reviewed at its declared 1920Ã—1080, 125% setting.
The role labels fit their controls and the hovered conversion control has a visible hover highlight.
Inspection of the declared fixture passed its source/layout checks and retained three nonblocking tab-label/button overlap notices.
The render reports 1,787 modelled, three approximated, 137 ignored, 58 unresolved, and three unsupported fidelity items, with no missing assets.
No native tooltip popup or game click was executed by this qualification.
This evidence does not finish the full hover/click/edge matrix or prove actual campaign control, transfers, or engine timer receipts.

Inspection took 112,884 ms and rendering took 201,953 ms.
The Codex workflow allows 600 seconds per tool call so this source workload can finish; this is functional qualification, not an interactive-latency claim.
