# Africa Green Covenant Seal Animated GFX Handoff

## Sprite Definitions

Register in `interface/012_africa.gfx`:

```txt
spriteType = {
	name = "GFX_africa_green_covenant_seal"
	texturefile = "gfx/interface/animated/012_africa/green_covenant_seal_static_64x64.dds"
}

frameAnimatedSpriteType = {
	name = "GFX_africa_green_covenant_seal_animated"
	texturefile = "gfx/interface/animated/012_africa/green_covenant_seal_sheet_768x64.dds"
	noOfFrames = 12
	animation_rate_fps = 8
	looping = yes
	play_on_show = yes
	pause_on_loop = 0.0
	alwaystransparent = yes
}
```

## GUI Use

- Intended surface: Continental Congress scripted GUI Green Covenant seal state ornament
- Static fallback sprite target: `GFX_africa_green_covenant_seal`
- Animated sprite target: `GFX_africa_green_covenant_seal_animated`
- Suggested behavior: use the animated sprite for the active Green Covenant state and the static sprite when animation is not available or when the parent wants a non-looping fallback

## Final Files

- Static DDS: `gfx/interface/animated/012_africa/green_covenant_seal_static_64x64.dds`
- Animated sheet DDS: `gfx/interface/animated/012_africa/green_covenant_seal_sheet_768x64.dds`

## Validation

- Processed frames: `12`, each `64x64 srgba 8-bit`
- Sheet PNG: `768x64 srgba 8-bit`
- Static fallback PNG: `64x64 srgba 8-bit`
- Final DDS outputs: `768x64 srgba 8-bit` and `64x64 srgba 8-bit`
- Alpha range: `0-255` on all processed PNGs and both DDS outputs
- Transparent corners: yes, all four corners are alpha `0` on all processed PNGs and both DDS outputs
- Fringe or matte check: `0` opaque white, `0` opaque green, and `0` opaque magenta pixels detected across all processed PNGs and both DDS outputs
