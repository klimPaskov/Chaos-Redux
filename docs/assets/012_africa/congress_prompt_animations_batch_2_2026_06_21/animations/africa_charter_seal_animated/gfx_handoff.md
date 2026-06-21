# Africa Charter Seal Animated GFX Handoff

## Sprite Definitions

Register in `interface/012_africa.gfx`:

```txt
spriteType = {
	name = "GFX_africa_charter_seal"
	texturefile = "gfx/interface/animated/012_africa/charter_seal_prompt_static_64x64.dds"
}

frameAnimatedSpriteType = {
	name = "GFX_africa_charter_seal_animated"
	texturefile = "gfx/interface/animated/012_africa/charter_seal_prompt_sheet_512x64.dds"
	noOfFrames = 8
	animation_rate_fps = 6
	looping = yes
	play_on_show = yes
	pause_on_loop = 0.0
	alwaystransparent = yes
}
```

## GUI Use

Intended scripted GUI element ids:

- `africa_continental_congress_charter_seal_static`
- `africa_continental_congress_charter_seal_anim`

Suggested tooltip key:

- `africa_continental_congress_gui_charter_seal_tt`

The animated seal should appear when the Charter League is active or the player has reached the charter mandate branch. The static seal can share that visibility if there is no separate inactive state.

## Final Files

- Static DDS: `gfx/interface/animated/012_africa/charter_seal_prompt_static_64x64.dds`
- Animated sheet DDS: `gfx/interface/animated/012_africa/charter_seal_prompt_sheet_512x64.dds`

## Validation

- Processed frames: `8`, each `64x64 srgba 8-bit`.
- Sheet: `512x64 srgba 8-bit`.
- Static fallback: `64x64 srgba 8-bit`.
- DDS outputs: `srgba 8-bit` with alpha range `0-255`.
- Transparent corners: yes.
- Opaque white/green matte: none detected.
