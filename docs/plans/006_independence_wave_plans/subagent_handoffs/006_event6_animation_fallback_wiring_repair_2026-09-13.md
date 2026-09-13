# Event 006 animation fallback registry repair, 2026-09-13

Date: 2026-09-13.

Disposition: implemented bounded source wiring repair; ASSET-040 through ASSET-043 remain `needs_user_review` for source-alpha provenance and live animation evidence.

## Scope and source change

The four authored Statehood Ledger animation families already had valid frame sources, processed frames, sheets, static DDS files, and runtime paths. The read-only GUI inspector exposed one concrete registry defect: each `frameAnimatedSpriteType` lacked the installed vanilla fallback naming convention expected by the inspector, so all four animated siblings reported `GUI_ANIMATION_STATIC_FALLBACK_MISSING`.

Only `interface/006_independence_wave.gfx` was changed. Each family now has a `GFX_independence_wave_<family>_animated_static` sprite alias pointing to its existing static DDS, while the pre-existing `<family>_static` identifier remains unchanged for current GUI consumers. The static alias is declared beside the state strip and animated sibling. The four frame-animated definitions also use the installed vanilla `loadType = "INGAME"` and `transparencecheck = yes` properties. No PNG, DDS, frame order, effect file, GUI controller, scripted GUI, gameplay, or localisation file changed.

The aliases are registry compatibility entries, not new artwork or an unapproved visual fallback. They reuse the already audited static family outputs and preserve the existing `*_states`, `*_animated`, and `*_static` identifiers.

## MCP evidence

The post-change read-only `hoi4_gui_inspect` targeted `independence_wave_status_window` with `scenario = { id = "event006_animation_fallback_alias_repair_2026_09_13" }` and `generatedScenarios = { enabled = false }`. It returned `GUI_INSPECTED` at source revision `20c038b7a4b70b57ecdd652c252cec21bf7bceb21b006acd088d72381f854002`, resolving all 48 Event 006 elements. The four `GUI_ANIMATION_STATIC_FALLBACK_MISSING` diagnostics disappeared. The remaining diagnostics are the known 63 synthetic overlap notices and offline `GUI_SPRITE_RENDER_PARTIAL` blendframe limitations; no blocking source-graph diagnostic or missing fallback remains. The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f862e12b08fa644bc55b77ce96503001b151e0d723a67db75c78141ca4f17af/3859fa5962fde13bcb1bafa9be11449dd89655618d7e78acd03e3590493834f0/gui-inspect.20c038b7a4b70b57.json`.

The matching `hoi4_gui_render` used `windowName = "independence_wave_status_window"`, the same scenario, 1920x1080 at uiScale 1, `states = ["normal"]`, and generated scenarios disabled. It returned `GUI_RENDERED` with `validation.passed = true`, `comparison.changedPixels = 0`, `changedRatio = 0`, and `offlineRepresentation = true`. The final full SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7e16cf09518e23ca3fb5593aa8c3af1f18934c15f4a2cdb3e23c0bb8557350e/e09c367224d0b20d852ab456809231e6fa517b855b6a2b1b4e71a69213508f5b/independence_wave_status_window-full.svg`, the validation receipt is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ca48d8d2c57c0436d446068e86f6b7be6f58ae302eaefdc79552a89c691db54/ee1bb0117fec33a63fcf1c1dc39cadbf297052de5af9977941b1da5b9d9af130/independence_wave_status_window-validation.json`, and the comparison receipt is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/bd3fb8e626c5f48315bd1419b0dfb70179ac63edb820140186d8fb95bb0ed0e7/independence_wave_status_window-comparison.json`.

A render requesting all four mutually exclusive tab states together was not used as acceptance evidence because the synthetic fixture correctly reported `GUI_TAB_STATE_CONFLICT`. The single-state render is the valid source-wiring receipt.

## Validation and limits

The Event 006 GUI semantic matrix remains passing, and the normal-state MCP render no longer reports a missing static fallback. The static icon, flag, allocator, country API, FORM-16, and SCN-008 checks remain unchanged and passing from the current asset tranche.

This repair does not prove live engine blendframe playback, dynamic tab visibility, click-region behavior, or fallback selection in a running campaign. The four source masters remain opaque chroma-key RGB images and the documented remover helper is absent from this checkout, so provenance and live visual gates remain open. No live Hearts of Iron IV launch or save/load claim is made.

Skills used for this bounded repair: `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-scripted-gui`, and `chaos-redux-subagents`.
