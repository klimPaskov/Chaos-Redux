# Africa Formable Ready Emblem Animated GFX Handoff

## Sprite Definitions

Register in `interface/012_africa.gfx`:

```txt
spriteType = {
	name = "GFX_africa_formable_ready_emblem"
	texturefile = "gfx/interface/animated/012_africa/formable_ready_prompt_static_64x64.dds"
}

frameAnimatedSpriteType = {
	name = "GFX_africa_formable_ready_emblem_animated"
	texturefile = "gfx/interface/animated/012_africa/formable_ready_prompt_sheet_512x64.dds"
	noOfFrames = 8
	animation_rate_fps = 7
	looping = yes
	play_on_show = yes
	pause_on_loop = 0.0
	alwaystransparent = yes
}
```

## GUI Use

- Intended surface: Continental Congress scripted GUI formable/world-order readiness emblem
- Static fallback sprite id: `GFX_africa_formable_ready_emblem`
- Animated sprite id: `GFX_africa_formable_ready_emblem_animated`
- Recommended use: show the animated sprite when the formable/world-order readiness gate is satisfied, and use the static fallback for non-animated or paused display states

## Final Files

- Static DDS: `gfx/interface/animated/012_africa/formable_ready_prompt_static_64x64.dds`
- Animated sheet DDS: `gfx/interface/animated/012_africa/formable_ready_prompt_sheet_512x64.dds`

## Validation

- Processed frames: `8`, each `64x64 srgba 8-bit`
- Sheet PNG: `512x64 srgba 8-bit`
- Static PNG: `64x64 srgba 8-bit`
- DDS outputs: `64x64` and `512x64`, both `srgba 8-bit`
- Alpha range across validated outputs: `0-255`
- Transparent corners: yes, all corners decode as `(0, 0, 0, 0)`
- Transparent-edge white fringe: `0`
- Transparent-edge green fringe: `0`
- Transparent-edge magenta fringe: `0`
