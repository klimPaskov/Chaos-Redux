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

The Event 014 completion audit remains `PARTIAL / NOT COMPLETION-READY` until a bounded five-window matrix exposes attributable state and resolution evidence or the adapter limitation is explicitly accepted by the parent.
