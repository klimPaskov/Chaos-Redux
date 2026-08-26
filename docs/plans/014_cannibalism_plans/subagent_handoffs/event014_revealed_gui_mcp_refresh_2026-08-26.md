# Event 014 revealed command GUI MCP refresh

Audit date: 2026-08-26.

Mode: read-only MCP evidence refresh. No gameplay, GUI source, asset, localisation, spreadsheet, focus, AI, or 3D source was changed.

The exact-selector inspect targeted `cannibalism_revealed_command_window` with scenario `event014_targeted_revealed_normal_2026_08_26` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

The call returned `GUI_INSPECTED` with status `ok`, `complete: true`, `skippedSourceCount: 0`, shared revision `3833aa9ed3dfe5ceb6fb71339d42db99c9cc145f501bb1fe1b62e0428815f43c`, and `inspectedElementCount: 17`.

The fidelity summary was modelled 139, approximated 8, ignored 5, missing 4, unsupported 3, and unresolved 5.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/595ce176e37732d4370d2e66da290c24a3e0e0ef4dc7a4f8a113a73b428ef5fb/877a4ba89ad924336e5a8d58145d9d2a9ad26fd4d11b802bd8ebb20244004e12/gui-inspect.3833aa9ed3dfe5ce.json`.

The result still carries global graph and validation truncation, unrelated Event 003 and Event 005 index-collision diagnostics, and unattributed GUI diagnostics including overlap, text overflow, alignment, spacing, unresolved dynamic values, and static-animation fallback/provenance findings.

This refresh proves that the revealed window is fully inspected by the source selector, but it does not prove Event 014-specific click bounds, hover or disabled states, long-text behavior, clipping, hierarchy, resolution scaling, or before/after comparison. No GUI rewrite is justified from unattributed diagnostics.

A bounded visual render was also requested for `normal`, `hover`, `disabled`, and `long-text` states at 1280x720 under scenario `event014_targeted_revealed_visual_states_2026_08_26`.

The render returned `GUI_RENDERED` with no blockers and produced `cannibalism_revealed_command_window-full.svg` at a normalized 1920x1080 canvas: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f441cea9faf5d200fedd25fd95fadad86bb775973942db14d40b7501c6effc9/0020d729626119fb494450e25a55653c959e147c038201e124e4bc09724c1e4d/cannibalism_revealed_command_window-full.svg`.

The render response exceeded the wire budget and returned only the linked SVG, so the requested state-specific diagnostics and click-region metadata remain unavailable for attribution.

## Wendigo command follow-up

The exact-selector inspect targeted `cannibalism_wendigo_command_window` with scenario `event014_targeted_wendigo_normal_2026_08_26`.

The call returned `GUI_INSPECTED` with status `ok`, `complete: true`, `skippedSourceCount: 0`, shared revision `e5ed163e9ee42a018130a43889b988fe48fe78d47471c5eec3dbd60129de5315`, and `inspectedElementCount: 17`.

The fidelity summary was modelled 137, approximated 8, ignored 5, missing 4, unsupported 3, and unresolved 4.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9efbefec4c9c16c95c5ac40517c16a33e9eb87ee72aeb76b2ee44d75950804f3/57f688d04bb18842f9fc08aa69c8aa86be793e872bd2b428db075892e1b9c26d/gui-inspect.e5ed163e9ee42a01.json`.

The result still reports global graph and validation truncation, so its 25 overlap, alignment, spacing, text-overflow, animation fallback/provenance, unresolved dynamic, and scripted-context diagnostics cannot be attributed to this Event 014 window. No GUI rewrite is justified.

The Event 014 completion audit remains `PARTIAL / NOT COMPLETION-READY` until a bounded five-window matrix exposes attributable state and resolution evidence or the adapter limitation is explicitly accepted by the parent.

## Early header command follow-up

The exact-selector inspect targeted `cannibalism_early_header_window` with scenario `event014_targeted_early_current_2026_08_26` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

The call returned `GUI_INSPECTED` with status `ok`, `complete: true`, `skippedSourceCount: 0`, shared revision `28a47b94e0e8c2cbb1014a40ea91f43bec2ac6a812e32cde804f4c5b62838df7`, and `inspectedElementCount: 17`.

The fidelity summary was modelled 149, approximated 7, ignored 9, missing 4, unsupported 2, and unresolved 6.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8f87a27d3e82880e2f466c30b7df60136b7a79a216c12368c94edcf21ed01ad/9b17c5ddaba374bdb4c659c40cb6438bc4e229bf7358b4e00919e53551f7ba1e/gui-inspect.28a47b94e0e8c2cb.json`.

The source-selector result still carries the fixed global graph and validation ceilings, including unrelated index collisions and unattributed overlap, overflow, spacing, alignment, dynamic-value, and animation-fidelity diagnostics. This is current early-window reachability evidence, not a clean Event 014-specific visual acceptance result.
