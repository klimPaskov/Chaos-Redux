# ASSET-043 formable eligibility seal animation brief

In-game use: scripted GUI status-panel feedback for formable discovery, eligibility, and proclamation.

Target surface: the planned Event 6 status panel; the parent implementation owns the final GUI attachment and formable-state trigger.

Resolved implementation-defined size: 64x64 pixels per frame because this is a compact status-panel heraldic seal.

Frame plan: four authored state frames in the accepted order hidden, discovered, eligible, proclaimed.

Sheet: one horizontal 256x64 PNG and DDS sheet with no gaps.

Animation: 5 FPS, 200 ms per frame, looping for review; `play_on_show = no` so parent state controls the visible formable beat.

Anchor: centered with transparent corners and stable circular heraldic seal silhouette.

Source mode: built-in ImageGen, one independent chroma-key source per state, then deterministic key removal and normalization only.

Fallback: `independence_wave_formable_eligibility_seal_static.dds` uses hidden state.

Runtime ownership: the asset package supplies DDS files and sprite-name recommendations only; the parent owns `.gfx`, `.gui`, scripted GUI, and formable eligibility wiring.
