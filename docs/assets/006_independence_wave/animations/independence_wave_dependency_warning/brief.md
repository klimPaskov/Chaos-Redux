# ASSET-041 dependency warning animation brief

In-game use: scripted GUI status-panel warning feedback for patron dependency thresholds.

Target surface: the planned Event 6 status panel; the parent implementation owns the final GUI attachment and warning trigger.

Resolved implementation-defined size: 64x64 pixels per frame because this is a compact status-panel warning marker.

Frame plan: three authored state frames in the accepted order calm, watch, danger.

Sheet: one horizontal 192x64 PNG and DDS sheet with no gaps.

Animation: 5 FPS, 200 ms per frame, looping for review; `play_on_show = no` because warning visibility and state timing are parent-controlled.

Anchor: centered with transparent corners and a stable shield silhouette.

Source mode: built-in ImageGen, one independent chroma-key source per state, then deterministic key removal and normalization only.

Fallback: `independence_wave_dependency_warning_static.dds` uses calm state.

Runtime ownership: the asset package supplies DDS files and sprite-name recommendations only; the parent owns `.gfx`, `.gui`, scripted GUI, and patron-dominance predicates.
