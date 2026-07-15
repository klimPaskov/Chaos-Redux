# Fallout World End GFX Handoff

## Scope

This handoff covers two dedicated Fallout textures. Both sprites are registered in `interface/fallout_world_end.gfx` and retain dedicated Fallout paths.

Registration file: `interface/fallout_world_end.gfx`

## Registered sprite definitions

```text
spriteTypes = {
	spriteType = {
		name = "GFX_fallout_blackout_tile"
		texturefile = "gfx/interface/fallout_world_end/fallout_blackout_tile.dds"
	}

	spriteType = {
		name = "GFX_idea_fallout_state_grade"
		texturefile = "gfx/interface/ideas/fallout_world_end/idea_fallout_state_grade.dds"
	}
}
```

## Texture details

### `GFX_fallout_blackout_tile`

- Final path: `gfx/interface/fallout_world_end/fallout_blackout_tile.dds`
- Dimensions: `10x10`
- Format: legacy one-level uncompressed 32-bit BGRA, equivalent to `B8G8R8A8`
- Alpha: fully opaque, alpha `255` on every pixel
- Intended element: the full-screen blackout background or click-blocking overlay icon
- Vanilla precedent: a small black tile sprite scaled across a full-screen window

### `GFX_idea_fallout_state_grade`

- Final path: `gfx/interface/ideas/fallout_world_end/idea_fallout_state_grade.dds`
- Dimensions: `64x64`
- Format: legacy one-level uncompressed 32-bit BGRA, equivalent to `B8G8R8A8`
- Alpha: real transparency outside the painted subject
- Intended element: Fallout state-grade status icon or modifier presentation
- Visual identity: ash, cracked shelter, and cold sky

## Wiring notes

- Keep the blackout inside the dedicated Fallout scripted GUI. It is not an ordinary super-event presentation.
- Scale or size the blackout element in `interface/fallout_world_end.gui` so it covers the supported screen area.
- Use the modifier icon at native `64x64` where possible. Downscaling is safe, but enlarging it will expose raster pixels.
- Keep both sprite names and texture paths dedicated to Fallout.
- No localisation key is required until the main implementation attaches a tooltip or player-facing label.

## Review artifact

Use `docs/assets/fallout_world_end/contact_sheets/fallout_ui_asset_contact_sheet.png` to review the source, alpha extraction, final icon alignment, DDS decode, and opaque tile.

## Remaining uncertainty

The blackout sprite is referenced by `interface/fallout_world_end.gui`. Its exact all-resolution binding, draw order, and input-blocking behavior remain unresolved GUI proof obligations. The state-grade sprite is referenced by the seven Fallout grade dynamic modifiers.
