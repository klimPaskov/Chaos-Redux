# Event 006 status-window warning placement repair

Disposition: **implemented as a narrow source repair; broader GUI acceptance remains unresolved**.
Date: 2026-09-12.
Event: `006_independence_wave`.

## Scope and source change

The owned surface is `independence_wave_status_window` in `interface/006_independence_wave.gui`.
The accepted five-value status contract was preserved: legitimacy, recognition, administrative capacity, security, and instability remain visible and unchanged.
The only source edit moves `independence_wave_status_instability_warning` from `position = { x = 306 y = 292 }` to `position = { x = 318 y = 384 }`, keeping its existing sprite, scale, and transparency settings.
The previous position occupied the instability text rectangle at approximately x74–374, y292–328; the replacement is in the unused gap above the tab row and below the right-side summary content.
No gameplay, scripted-GUI controller, localisation, asset, animation, cost, AI, or fallback behavior changed.

## MCP evidence

The post-edit `hoi4.gui_inspect` query targeted `independence_wave_status_window` with scenario `event006_status_repair_baseline_post_warning`, `generatedScenarios.enabled = false`, 1920 × 1080 resolution, and UI scale 1.
It returned `GUI_INSPECTED`, 48 resolved Event 006 elements, validation success, and source revision `4df34107e11d2a719f1b76688f7aaf908ff301e0ad2174dcd0b1662efa5e63bc`.
Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1cdc77bcfe3b4e724caaba79731c40ddf1f3c770ad77cc4e4a4ed95e0deabb12/7309923e6f3026e14799d4c11a98c098363397b749043fd73eac8457d9e73052/gui-inspect.4df34107e11d2a71.json`.
The post-edit `hoi4.gui_render` query requested normal and warning states at 1920 × 1080 and 1366 × 768, both at UI scale 1, and returned `GUI_RENDERED` with 27 artifacts across two states, one scenario, two resolutions, and five variants.
The reviewed cropped render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e9f30eb962758ee93d79dbcb9aca2e75eacdce13392f2540cfd9f4f8319365c/c5f147265017bd9309b074a83c303200ce1fb5a7a89778c0b7358bb21ea927cb/independence_wave_status_window-cropped.png`.
The matching full render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53aefdbe7e4a7e0980126db1cc6ff63b986ad146c1463fa752e8d0935c76e404/09ba0984e0fea53a66f1f18a36d0acd204e4e64afec7f2230c6254134cd9e0d6/independence_wave_status_window-full.png`.
The renderer's `changedPixels: 0` comparison is a self-comparison because no pre-edit source revision was supplied, so it is not claimed as matched before/after proof.

## Validation and remaining limits

The focused source matrix validator passed and confirmed five mutually exclusive tab click contracts, recognition/dependency/league/formable frame families, cleanup of four frame variables plus the animation flag, and four static/animated sibling surfaces.
The MCP run still reports the pre-existing empty-fixture limitations: unresolved dynamic text and state coverage, missing static-fallback resolution for four animated surfaces, unsupported `gfx/FX/buttonstate_blendframes.lua` cases, and visible tab-panel overprint in the renderer's empty fixture.
The source controller still clears the other tab flags on each tab click, so no speculative panel redesign was applied.
The accepted five-value design remains in tension with the generic four-value GUI density ceiling, but no metric was hidden or merged without a new accepted design decision.
This handoff does not claim complete GUI or Event 006 visual acceptance, live/save-load validation, or resolution of the broader ASSET-039 blocker set.
