# Event 006 formable state-puzzle GUI worker recheck (2026-09-20)

## Disposition

`BLOCKED / source unchanged`.

This bounded recheck covers only the Event 006 formable state-puzzle window `chaosx_independence_wave_formable_state_puzzle_window` and its presentation-only scripted GUI.

No safe native source fix was proven for the dynamic icon footprint or unresolved summary route.

No gameplay, decision, mission, AI, formable effect, shared GUI, asset, GFX, scripted localisation, localisation, or workbook file was changed.

## Authorized surface

The interface source is `interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui`.

The scripted-GUI source is `common/scripted_guis/chaosx_formable_state_puzzles.txt`.

The scripted GUI is `independence_wave_formable_state_puzzle_scripted_gui` with `decision_category` context and no gameplay-changing effects.

The accepted composition remains a clipped 440x206 independent window with a 440x22 summary strip at y=0 and a 440x180 family map at y=24.

The fourteen family overlays remain intentionally co-located and are selected by mutually exclusive activation visibility triggers.

The qualifying and unresolved dynamic sprite branches, exact state-piece positions, and delayed informational tooltips remain unchanged.

## MCP inspection evidence

The current source revision is `1c312e1b9c0161da9ccb88c11580d3d436f94576ac59f4c7133efb9e9b323dc2`.

The 1920x1080 inspection used `scenario = { id = "event006_formable_activated_normal" }` with generated scenarios disabled and returned `GUI_INSPECTED` for 93 elements.

The 1920x1080 inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/675b1559559f48af244bdf7064fcca97fdb813256c6676f9cd62dd5ed5afaf01/c386b5f3fda05e66d35cbb0bb57b71f2bfb72c5f6f7848c615335621ebeaa291/gui-inspect.1c312e1b9c0161da.json`.

The 1280x720 inspection used the same scenario with `resolution = { width = 1280 height = 720 }` and `uiScale = 1` and returned `GUI_INSPECTED` for the same 93 elements.

The 1280x720 inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8503f58238bb1475419badae10a2ad17224f4b3419138c1a4001e770084a2a33/e36cf38c57b7cc08412bc89b61c9adbcd1792ba03d8abc7bab63b6e05dfaf746/gui-inspect.1c312e1b9c0161da.json`.

Both inspections report 643 modelled, 1 approximated, 50 ignored, 0 missing, 0 unsupported, and 15 unresolved elements.

The 1280x720 inspection reports `GUI_ACCIDENTAL_CLIPPING` for FORM01 state pieces 14, 121, 122, and 133 and FORM02 state pieces 100, 121, 133, 331, and 337.

The 1280x720 inspection reports unresolved dynamic summary getters including `GetChaosxFormableIndependenceWaveForm01QualifyingCount` and `GetChaosxFormableIndependenceWaveForm01SummaryStatus`.

The same inspection reports the intended co-located family overlays and overlapping state pieces as aggregate `GUI_VISIBLE_OVERLAP` diagnostics because the inspection route does not evaluate family activation visibility as a runtime-isolated fixture.

The 1920x1080 inspection reports the same unresolved summary route and aggregate overlay diagnostics without proving a clean family-isolated visual state.

## MCP render evidence

The matching render used `event006_formable_activated_normal`, generated scenarios disabled, states `normal`, `warning`, and `long-text`, and resolutions 1920x1080 and 1280x720 at UI scale 1.

The render returned `GUI_RENDERED` with one linked full-window SVG at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2349cbee9b6ef7425a0fbd3c50e73ffe3881e9bf02339aa65d160cbf35c5cf44/0274a7449d6bf623ab17d966bec8450a4ba65e3d9ee27f598eebafc6103d31c5/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The render response emitted `MCP_RESPONSE_TRUNCATED` because the complete response was 33689 bytes against a 32768-byte wire budget.

The route returned no separate family-isolated, crop, annotation, click-region, state-gallery, resolution-gallery, or matched comparison artifact.

The render therefore proves route availability but does not prove visual acceptance or clear the clipping and unresolved-value findings.

## Safe-fix review

The offline Interface and Scripted GUI wiki pages document `iconType` sprite, frame, tooltip, transparency, and position fields but do not document an explicit child footprint or size field.

The installed scripted-GUI documentation and the inspected vanilla SOV paranoia and war-escalation precedents likewise provide no source-backed dynamic icon footprint override for this consumer.

Adding an undocumented `size` or CSS-like field would be speculative and is not applied.

Wrapping the state icons in sized containers would change the accepted hierarchy without proving the rendered sprite footprint or preserving tooltip geometry.

Replacing dynamic image getters with an unresolved-only static branch would violate the accepted qualifying-state behavior.

Changing state coordinates or the 440x180 projection would discard the accepted asset manifests and reviewed map geometry.

No safe source-local correction is therefore justified by the current engine evidence.

## Source integrity and next required evidence

The unchanged interface source hash is `D9793AE1F8958AAFFE643390A8C958B48517ECA8014285178F47BECAC5C829E7`.

The unchanged scripted-GUI source hash is `5B9092A71399DE26CB0418DA0B596D80D914B824D72844EFFF104B7777DF5FE6`.

The unchanged GFX source hash is `1FCBA2BC179A0A03F6E26D4893B78FA9DF2A083A185AC13963A42FAD20756591`.

The next valid tranche requires an engine-equivalent family-isolated fixture that resolves the dynamic summary and image getters at both target resolutions, or a documented native footprint contract demonstrated by a vanilla consumer and a matched before/after MCP render.

Until that evidence exists, the GUI remains presentation-source present but visual-acceptance blocked.

No simplification, fallback art, geometry change, undocumented property, or gameplay change was introduced.
