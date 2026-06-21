# Africa Cohesion Warning Border Animated GFX Handoff

## Register In

- Suggested `.gfx` file: `interface/012_africa.gfx`
- Target GUI file already using the card surface: `interface/012_africa_scripted_gui.gui`
- Target scripted-GUI card: `africa_continental_congress_warning_status_card`

## Sprite Definitions

```txt
spriteType = {
	name = "GFX_africa_cohesion_warning_border"
	texturefile = "gfx/interface/animated/012_africa/cohesion_warning_border_static_520x58.dds"
	alwaystransparent = yes
}

frameAnimatedSpriteType = {
	name = "GFX_africa_cohesion_warning_border_animated"
	texturefile = "gfx/interface/animated/012_africa/cohesion_warning_border_sheet_4160x58.dds"
	noOfFrames = 8
	animation_rate_fps = 7
	looping = yes
	play_on_show = yes
	pause_on_loop = 0.0
	alwaystransparent = yes
}
```

## Final Files

- Static DDS: `gfx/interface/animated/012_africa/cohesion_warning_border_static_520x58.dds`
- Animated sheet DDS: `gfx/interface/animated/012_africa/cohesion_warning_border_sheet_4160x58.dds`
- Sheet PNG: `docs/assets/012_africa/congress_prompt_animations_batch_3_2026_06_21/animations/africa_cohesion_warning_border_animated/africa_cohesion_warning_border_animated_sheet_4160x58.png`
- Static PNG: `docs/assets/012_africa/congress_prompt_animations_batch_3_2026_06_21/animations/africa_cohesion_warning_border_animated/africa_cohesion_warning_border_static_520x58.png`

## Intended Use

- Decorative but state-signaling border for the Continental Congress warning docket card
- Intended warning state: rebellion / cohesion crisis / severe warning visibility
- Static fallback behavior: use frame `003` when animation is hidden, unsupported, or gated off

## Precedent Inspected

- `interface/012_africa.gfx`
  - existing `GFX_africa_charter_seal_animated`
  - existing `GFX_africa_bestiary_warning_loop`
- `interface/012_africa_scripted_gui.gui`
  - target card `africa_continental_congress_warning_status_card`

## Validation

- Processed frames: `8`, each `520x58 srgba 8-bit`
- Sheet PNG: `4160x58 srgba 8-bit`
- Static PNG: `520x58 srgba 8-bit`
- DDS outputs: `4160x58` and `520x58`, both `srgba 8-bit`
- Alpha range: `0-255` in PNG and DDS
- Transparent corners: yes
- Text-safe center window: verified transparent in static PNG, sheet PNG first frame, static DDS, and sheet DDS first frame
- Opaque green matte: none detected
- Opaque magenta matte: none detected

## Use Notes

- The processed border keeps both outside area and center area transparent so it can sit directly over the existing scripted-GUI text card.
- The asset package already includes `brief.md`, `frame_plan.md`, source frames, processed frames, sheet PNG, static fallback PNG, preview GIF, contact sheet PNG, manifest, and this handoff.
