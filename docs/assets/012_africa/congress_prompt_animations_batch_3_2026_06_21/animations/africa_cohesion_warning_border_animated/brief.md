# Africa Cohesion Warning Border Animated Brief

- Asset name: `africa_cohesion_warning_border_animated`
- Event id / slug: `012_africa`
- In-game use: Continental Congress scripted GUI warning / rebellion / cohesion crisis border around `africa_continental_congress_warning_status_card`
- Target GUI file: `interface/012_africa_scripted_gui.gui`
- Target card footprint: `x=8 y=332 maxWidth=508 maxHeight=46`
- Target frame size: `520x58`
- Frame count: `8`
- Sheet size: `4160x58`
- Static fallback sprite: `GFX_africa_cohesion_warning_border`
- Animated sprite: `GFX_africa_cohesion_warning_border_animated`
- FPS: `7`
- Looping: `yes`
- Play on show: `yes`
- Pause on loop: `0.0`
- Anchor point: centered full-frame border
- Source mode: generated per-frame fictional symbolic UI art via `$imagegen`, using one generated eight-frame source sheet and extracting each frame as its own source frame
- Subject type: fictional symbolic UI-only ornament
- Final static DDS path: `gfx/interface/animated/012_africa/cohesion_warning_border_static_520x58.dds`
- Final sheet DDS path: `gfx/interface/animated/012_africa/cohesion_warning_border_sheet_4160x58.dds`
- Reference / precedent inspected:
  - `interface/012_africa.gfx`
  - `interface/012_africa_scripted_gui.gui`
  - `docs/assets/012_africa/congress_prompt_animations_batch_2_2026_06_21/animations/africa_charter_seal_animated/`

## Visual Direction

Engraved brass and dark red emergency filigree border with charter beads, side warning lamps, faint radio-warning ticks, and a restrained rebellion / cohesion pulse. Transparent center and transparent outside. No text.

## Source Prompt

Used with built-in `$imagegen`:

```text
Create a single horizontal source sheet containing exactly eight equal animation frames in one row for a fictional warning border around a 520x58 UI card. Each frame must show the same ornate border design from a straight-on orthographic view, with subtle frame-to-frame drawn changes: warning pulse rising and falling, tiny charter beads brightening then dimming, faint radio-warning ticks flickering, and a few fine edge cracks appearing strongest at the pulse peak then receding. The loop should go rest -> rising -> stronger -> peak -> peak aftermath -> falling -> near rest -> rest-ready.

The entire image must use a perfectly flat solid #00ff00 chroma-key background anywhere there is no border art, including the center/interior of the border and the outside of the border. No shadows, no floor, no gradients, no texture in the background.

Subject: engraved brass and dark red emergency filigree border, period-appropriate HOI4 ornament, small charter beads, subtle rebellion/cohesion warning energy, transparent center intended after chroma removal.

Style: polished 2D game UI ornament, painterly-engraved metal, not photorealistic, not a modern HUD.
```

## Processing Summary

- The first generation pass produced a usable one-row eight-frame source sheet on chroma green.
- Each frame was cropped out to its own source PNG.
- Chroma was removed with the official `remove_chroma_key.py` helper.
- Frames were normalized to the exact `520x58` target.
- The inner text-safe center window was enforced as transparent after chroma cleanup.
- Static fallback uses frame `003`, the strongest readable warning state without overfilling the interior.
