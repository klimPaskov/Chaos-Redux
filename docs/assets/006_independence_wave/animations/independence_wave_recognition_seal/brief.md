# ASSET-040 recognition seal animation brief

In-game use: scripted GUI status-panel recognition feedback for the Independence Wave release and recognition state.

Target surface: the planned Event 6 status panel; the parent implementation owns the final GUI attachment and state trigger.

Resolved implementation-defined size: 64x64 pixels per frame because this is a small status-panel sprite, matching the accepted Event 6 idea-icon scale and the panel's compact marker role.

Frame plan: five authored state frames in the accepted order hidden, weak, rising, strong, entrenched.

Sheet: one horizontal 320x64 PNG and DDS sheet with no padding between frames.

Animation: 5 FPS, 200 ms per frame, looping for review and state-preview continuity, `play_on_show = no` so the parent GUI can show the appropriate state without an autoplay burst.

Anchor: centered; each normalized frame is 64x64 with a stable centered seal and transparent corners.

Source mode: built-in ImageGen, one independent chroma-key source per state, then deterministic key removal and normalization only.

Fallback: `independence_wave_recognition_seal_static.dds` uses the hidden state; parent may select a safer inactive fallback if its GUI trigger suppresses hidden state.

Runtime ownership: the asset package supplies DDS files and sprite-name recommendations only; the parent owns `.gfx`, `.gui`, scripted GUI, state predicates, and wiring.
