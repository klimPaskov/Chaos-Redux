# Event 006 focus coordinate trials — 2026-08-25

> Superseded for current focus-layout authority by commit `314642488` and `subagent_handoffs/006_event6_focus_geometry_closure_current_2026-08-25.md`. This handoff preserves rejected-trial and five-warning baseline evidence; current geometry is 184 focuses, 195 connectors, zero crossings, zero node intersections, zero long connectors, zero too-close same-row pairs, and zero Event 006 layout diagnostics.

## Scope

This is a read-only MCP follow-up to the accepted Event 006 focus source. It tested two narrow coordinate candidates against the current focus graph. The accepted source is unchanged; no focus rewrite was requested or applied.

## Baseline evidence

The current source rendered and inspected successfully with 184 focuses, 195 connectors, zero crossings, zero node intersections, and `longConnectorCount=2`. The accepted render retains five authored Event 006 layout warnings and one unrelated vanilla continuous-focus localisation warning. The source-linked artifacts are:

- Inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/395f37a3a841908a62e43efe9be30c1d68d35420eb4b37fb92a8af0db174ecfa/e88a60a339b9a3116bdf6085b42cbf542acdf4fb7b9961c6a11b7ae1a4dc2857/focus-inspect.8b4d96975359f307.json`
- Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b51625b54ace049dcbb824687cf2eb4e99fd85eb0d463bcca95854d4c651721a/97d41d297beeb519f75431a246790d47a17257240b48d84edf0702117e4caf80/independence_wave_focus_tree.focus.html`
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/876c81a53cdcdcbfdcbb5dba0f85b683f051598e4e608b57cada7f6b66eb9731/b2078234e3c52e5b0ddbc5450ea0f3f90d87667d499e7d2c5bdfec8d8a4a438c/independence_wave_focus_tree.focus.svg`
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fbcd5faa465ff3ebfc485c96a0186fb244cb79c5bafff72a3dbc9b1169653f72/5eac954f14e8df475b6ad7956badf53e1c0f3f9dc3e256e751ef0aec99af4af9/independence_wave_focus_tree.focus.json`

## Rejected trials

- `independence_wave_create_independent_treasury`: x=28/y=8 -> x=32/y=7. This removed the economy detour warning but introduced one connector crossing and one node intersection in the inspect result. The candidate was reverted. Trial inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e751c266f104aef22e245e844f693995d635858173022dd0c612858aa4937799/f457f8aa430527934f50445479bc2bdee293b2737cdfe49e136f3850528680dd/focus-inspect.27c04b013f42ec24.json`
- `independence_wave_focus_discover_regional_identity`: x=52/y=12 -> x=50/y=12. This kept the graph free of crossings and intersections but only moved the detour warning to the next connector into `independence_wave_prepare_union_congress`. The candidate was reverted. Trial render HTML artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7073137f4e144c0c61f7a80e4ba81f48f77189de8d328d2993b709650f83791d/a9ecf1136c03b6e93a08db18d08c057d6798335622431ba6afadc3b4d7ffa80a/independence_wave_focus_tree.focus.html`.

## Boundary

These trials changed no focus IDs, prerequisites, rewards, AI, localisation, icons, route gates, or package files. The accepted focus surface remains **HOLD**. This handoff is source and MCP evidence only; it contains no live game or save/load evidence.
