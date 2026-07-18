# Utopia Balance to Assignment — GFX and GUI Handoff

The animation package is ready for parent-owned registration and placement. This subtask intentionally does not edit `.gfx` or `.gui` files.

## GFX registration

Target: `interface/015_utopia_manifesto.gfx`

Merge these entries into the file's existing `spriteTypes` block:

```txt
spriteType = {
	name = "GFX_utopia_balance_to_assignment_static"
	texturefile = "gfx/interface/015_utopia_manifesto/utopia_balance_to_assignment_static.dds"
}

frameAnimatedSpriteType = {
	name = "GFX_utopia_balance_to_assignment_animated"
	texturefile = "gfx/interface/015_utopia_manifesto/utopia_balance_to_assignment_sheet.dds"
	noOfFrames = 8
	animation_rate_fps = 5
	looping = no
	play_on_show = yes
	pause_on_loop = 0.0
}
```

## GUI placement

- Target: `interface/015_utopia_manifesto_ledger.gui`.
- Intended surface: the existing Choice–Assignment threshold column, whose available width is 158 pixels.
- Native icon size: `158x24`; do not rescale the sheet or crop individual runtime frames.
- Suggested element: decorative `iconType` centered in the threshold strip with `alwaystransparent = yes` so it cannot intercept clicks.
- Show `GFX_utopia_balance_to_assignment_animated` on the state transition into Assignment.
- After the non-looping transition, show `GFX_utopia_balance_to_assignment_static` while the Assignment state remains reached.
- Do not show both sprites concurrently; keep their positions identical to avoid a visual jump.

The non-looping transition and its reached-state sprite are both requested deliverables. The static sprite is not a substitute for the animated sheet.
