# Event 033 Acid Rain asset prompt

The Event 033 visual package is delivered and registered in `interface/033_acid_rain.gfx`; Part 10 and the event overview list every file and sprite.
The remaining production is the D37 regional state strips, accepted and queued in [the agent decision log](../../../plans/033_acid_rain_plans/agent_decisions_2026-10-04.md).

Read [the asset skill](../../../../.claude/skills/chaos-redux-event-assets/SKILL.md), [the frame-animation skill](../../../../.claude/skills/chaos-redux-frame-animation/SKILL.md) for anything animated, [the scripted GUI skill](../../../../.claude/skills/chaos-redux-scripted-gui/SKILL.md) and [the subagent skill](../../../../.claude/skills/chaos-redux-subagents/SKILL.md) before producing anything.
Route generated art to `chaosx_generated_event_art` or `chaosx_icon_artist`; the parent owns GFX and gameplay wiring, and `chaosx_event_ui_worker` owns only the dedicated Acid Rain window.

## D37 regional state strips

- Keep `GFX_acid_rain_map_base` and its fit unchanged.
- Replace the seven region overlays at the same sprite names and paths (`GFX_acid_rain_region_overlay_1` to `_7`, `gfx/interface/033_acid_rain/gui/acid_rain_region_overlay_1.dds` to `_7.dds`) with four-frame static strips of 560 by 300 frames on a 2240 by 300 canvas: inactive, visited, approaching and active.
- Visited history and danger must differ in both colour and treatment, and no frame may repaint, move or replace the base map's geography.
- The active frame uses generated cloud and rain art with native transparency, requested through the `gptimage` MCP route with the alpha checked on the saved PNG; the other frames may use exact mask processing.
- The strips replace the broad visited, ordinary and warning veils; record each replaced consumer before retiring it.
- Correct the marker anchors from the painted bounds on the neutral base.
- Preserve the old runtime bytes until synchronized promotion, and complete source review, native-size review and strict DDS round-trip checks first.

## Visual direction

Use 1930s and 1940s civil defense, corroded steel, stained stone, damaged rail and contaminated water in grey, yellow-brown, muted green and rust red.
Avoid neon green, modern hazmat suits, readable text in art and copied photographs; the reference board is `research/033_acid_rain_visual_reference_board.md`.
