# Event 006 formable state-puzzle explicit fixture recheck (2026-09-20)

## Disposition

`BLOCKED / source unchanged`.

This continuation records the narrowest family-isolated MCP fixture attempted after the aggregate renderer continued to report unresolved dynamic values and clipping.

No gameplay, decision, mission, AI, formable effect, GUI source, asset, GFX, scripted-localisation, localisation, or workbook file was changed.

## Fixture contract

The inspected window is `chaosx_independence_wave_formable_state_puzzle_window` with scripted GUI `independence_wave_formable_state_puzzle_scripted_gui`.

The fixture disables generated scenarios and activates only the FORM01 overlay through the explicit `visibility` object.

The supplied dynamic values set `GetChaosxFormableIndependenceWaveForm01QualifyingCount` to `3` and `GetChaosxFormableIndependenceWaveForm01SummaryStatus` to `Requirements incomplete`.

The supplied FORM01 image values resolve state pieces 14, 121, and 133 to qualifying sprites and state piece 122 to the unresolved sprite.

All other family overlay visibility values are false.

A parallel flag-based fixture was discarded because it activated cross-family overlays and therefore did not represent a family-isolated state.

## MCP inspection evidence

The shared source revision is `698cfd70186681fd53824a079357f373ff0da18af649a110818b462c17f8a6c2`.

The explicit resolved FORM01 inspection returned `GUI_INSPECTED` for 93 elements with no blocking diagnostics.

Its fidelity report counted 562 modelled, 1 approximated, 50 ignored, and 1 unresolved item.

The inspection still reports one intra-FORM01 overlap between state pieces 121 and 133.

Hidden-family branches retain zero-size or clipping diagnostics in the aggregate element collection even though their family visibility values are false in the fixture.

The inspection does not establish clean visual acceptance because the hidden-family diagnostics and one unresolved fidelity item remain present.

## MCP render evidence

The explicit normal FORM01 render at the requested 1920 by 1080 resolution returned `GUI_RENDERED` with one scenario, one state, five variants, source maps, click-region output, and no blocking diagnostics.

The full PNG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98c8d10fde0239c4ab4424899529047ef7dbe47a61324bf78ba43f85a4d8a276/b16dfeb4c73eb61fbdc160cccebee59c861f3b1897de94b67998e997bd2c2981/chaosx_independence_wave_formable_state_puzzle_w-full.png`.

The full SVG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5871c1a252f1f1310f365afee35a546d00d99a0aa1e6ebce30cb93433858d50/668f26df10f6abf6994db674103231469ff42cd863e138e268f2e60fde6ab13b/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The render fidelity report matches the inspection at 562 modelled, 1 approximated, 50 ignored, and 1 unresolved item.

The normal-only render reports missing state-coverage variants, the 121/133 intra-family overlap, and hidden-family zero-size or clipping diagnostics.

The explicit normal FORM01 render requested at 1280 by 720 returned `GUI_RENDERED`, but every returned full, cropped, annotated, click-region, and source-map variant was normalized to 1920 by 1080 by the adapter.

The normalized 1280-request full PNG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98c8d10fde0239c4ab4424899529047ef7dbe47a61324bf78ba43f85a4d8a276/c22d56fabe2cd0b1bbc6798f99e8bd4e0dc75bf0b33e85417be15fbd30383233/chaosx_independence_wave_formable_state_puzzle_w-full.png`.

The normalized 1280-request SVG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5871c1a252f1f1310f365afee35a546d00d99a0aa1e6ebce30cb93433858d50/b4c21915662d3c6e0b716a47ed75982544b2da979bc61e093c5763bee05d807f/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The 1280-request result is therefore not target-resolution evidence.

## Source decision

The existing reviewed 440 by 206 window, 440 by 22 summary strip, 440 by 180 map canvas, family overlay hierarchy, exact state coordinates, qualifying sprites, unresolved sprites, and delayed tooltips remain unchanged.

The offline GUI references and installed vanilla precedents still do not document a supported child-icon footprint field that would justify adding an undocumented size property.

The explicit fixture makes the dynamic-value contract more concrete, but it does not remove the unresolved fidelity item, hidden-family diagnostics, accepted geometry overlap, or target-resolution normalization.

No source-local GUI repair or `chaosx_event_ui_worker` implementation is justified by this evidence.

The next valid evidence is an engine-equivalent family-isolated fixture that resolves all visible dynamic summary and image getters at both target resolutions, or a documented native footprint contract followed by a matched before-and-after MCP render.

The formable state-puzzle GUI remains presentation-source present but visual-acceptance blocked.

No simplification, fallback art, geometry change, undocumented property, or gameplay change was introduced.
