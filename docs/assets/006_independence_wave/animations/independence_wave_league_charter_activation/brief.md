# ASSET-042 league charter activation animation brief

In-game use: scripted GUI status-panel emblem for league congress and charter activation.

Target surface: the planned Event 6 status panel; the parent implementation owns the final GUI attachment and congress-state trigger.

Resolved implementation-defined size: 64x64 pixels per frame because this is a compact status-panel charter emblem.

Frame plan: four authored state frames in the accepted order rest, drafting, vote, activated.

Sheet: one horizontal 256x64 PNG and DDS sheet with no gaps.

Animation: 5 FPS, 200 ms per frame, looping for review; `play_on_show = no` so parent state controls whether a beat is shown.

Anchor: centered with transparent corners and stable circular medallion silhouette.

Source mode: built-in ImageGen, one independent chroma-key source per state, then deterministic key removal and normalization only.

Fallback: `independence_wave_league_charter_activation_static.dds` uses rest state.

Runtime ownership: the asset package supplies DDS files and sprite-name recommendations only; the parent owns `.gfx`, `.gui`, scripted GUI, and league-state wiring.
