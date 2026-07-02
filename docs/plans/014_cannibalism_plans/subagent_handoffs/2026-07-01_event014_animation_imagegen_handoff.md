# Event 014 Cannibalism Animation Imagegen Handoff

Date: 2026-07-01

Scope: generated animated scripted-GUI/icon assets only. No `.gfx`, `.gui`, gameplay, localisation, focus, decision, country, spreadsheet, or leader portrait files were edited.

Source rule: every animation uses built-in imagegen source artwork. Each imagegen atlas was copied into the package and sliced into separate source frame PNGs before chroma-key removal and resizing. No final DDS was made from procedural shapes, CSS/SVG-only art, contact-sheet strips, or transform-only animation.

Recommended `.gfx` pattern for all assets: `frameAnimatedSpriteType`, `noOfFrames = 8`, `animation_rate_fps = 8`, `looping = yes`, `play_on_show = yes`. Static fallback sprites use `spriteType`.

Suggested target `.gfx` file: parent implementation should add these to the existing Event 014 scripted-GUI/interface `.gfx` file used for Cannibalism GUI assets. The asset worker did not inspect or edit gameplay/UI wiring files per scope.

## cannibalism_frontline_hunger_seal

- Final static DDS: `gfx/interface/animated/014_cannibalism/cannibalism_frontline_hunger_seal_static.dds`
- Final sheet DDS: `gfx/interface/animated/014_cannibalism/cannibalism_frontline_hunger_seal_sheet.dds`
- Sheet PNG: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_frontline_hunger_seal/sheets/cannibalism_frontline_hunger_seal_sheet.png`
- Static sprite name: `GFX_cannibalism_frontline_hunger_seal_static`
- Animated sprite name: `GFX_cannibalism_frontline_hunger_seal_animated`
- Target frame size: 64x64
- Frame count: 8
- Calculated sheet size: 512x64
- Animation rate: 8 fps recommended
- Looping: yes
- play_on_show: yes
- Anchor: center
- Source frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_frontline_hunger_seal/source_frames/`
- Processed frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_frontline_hunger_seal/processed_frames/`
- GIF preview: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_frontline_hunger_seal/previews/cannibalism_frontline_hunger_seal_preview.gif`
- Contact sheet: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_frontline_hunger_seal/previews/cannibalism_frontline_hunger_seal_contact.png`
- Behavior: decorative/state-driven scripted GUI visual; parent owns triggers and visibility wiring.

Ready-to-copy snippet, subject to parent verification against the chosen `.gfx` file:

```txt
spriteType = {
	name = "GFX_cannibalism_frontline_hunger_seal_static"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_frontline_hunger_seal_static.dds"
}
frameAnimatedSpriteType = {
	name = "GFX_cannibalism_frontline_hunger_seal_animated"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_frontline_hunger_seal_sheet.dds"
	noOfFrames = 8
	animation_rate_fps = 8
	looping = yes
	play_on_show = yes
}
```

## cannibalism_cult_pressure_warning

- Final static DDS: `gfx/interface/animated/014_cannibalism/cannibalism_cult_pressure_warning_static.dds`
- Final sheet DDS: `gfx/interface/animated/014_cannibalism/cannibalism_cult_pressure_warning_sheet.dds`
- Sheet PNG: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_cult_pressure_warning/sheets/cannibalism_cult_pressure_warning_sheet.png`
- Static sprite name: `GFX_cannibalism_cult_pressure_warning_static`
- Animated sprite name: `GFX_cannibalism_cult_pressure_warning_animated`
- Target frame size: 64x64
- Frame count: 8
- Calculated sheet size: 512x64
- Animation rate: 8 fps recommended
- Looping: yes
- play_on_show: yes
- Anchor: center
- Source frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_cult_pressure_warning/source_frames/`
- Processed frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_cult_pressure_warning/processed_frames/`
- GIF preview: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_cult_pressure_warning/previews/cannibalism_cult_pressure_warning_preview.gif`
- Contact sheet: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_cult_pressure_warning/previews/cannibalism_cult_pressure_warning_contact.png`
- Behavior: decorative/state-driven scripted GUI visual; parent owns triggers and visibility wiring.

Ready-to-copy snippet, subject to parent verification against the chosen `.gfx` file:

```txt
spriteType = {
	name = "GFX_cannibalism_cult_pressure_warning_static"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_cult_pressure_warning_static.dds"
}
frameAnimatedSpriteType = {
	name = "GFX_cannibalism_cult_pressure_warning_animated"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_cult_pressure_warning_sheet.dds"
	noOfFrames = 8
	animation_rate_fps = 8
	looping = yes
	play_on_show = yes
}
```

## cannibalism_island_signal_card

- Final static DDS: `gfx/interface/animated/014_cannibalism/cannibalism_island_signal_card_static.dds`
- Final sheet DDS: `gfx/interface/animated/014_cannibalism/cannibalism_island_signal_card_sheet.dds`
- Sheet PNG: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_island_signal_card/sheets/cannibalism_island_signal_card_sheet.png`
- Static sprite name: `GFX_cannibalism_island_signal_card_static`
- Animated sprite name: `GFX_cannibalism_island_signal_card_animated`
- Target frame size: 64x64
- Frame count: 8
- Calculated sheet size: 512x64
- Animation rate: 8 fps recommended
- Looping: yes
- play_on_show: yes
- Anchor: center
- Source frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_island_signal_card/source_frames/`
- Processed frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_island_signal_card/processed_frames/`
- GIF preview: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_island_signal_card/previews/cannibalism_island_signal_card_preview.gif`
- Contact sheet: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_island_signal_card/previews/cannibalism_island_signal_card_contact.png`
- Behavior: decorative/state-driven scripted GUI visual; parent owns triggers and visibility wiring.

Ready-to-copy snippet, subject to parent verification against the chosen `.gfx` file:

```txt
spriteType = {
	name = "GFX_cannibalism_island_signal_card_static"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_island_signal_card_static.dds"
}
frameAnimatedSpriteType = {
	name = "GFX_cannibalism_island_signal_card_animated"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_island_signal_card_sheet.dds"
	noOfFrames = 8
	animation_rate_fps = 8
	looping = yes
	play_on_show = yes
}
```

## cannibalism_hannibal_resonance_seal

- Final static DDS: `gfx/interface/animated/014_cannibalism/cannibalism_hannibal_resonance_seal_static.dds`
- Final sheet DDS: `gfx/interface/animated/014_cannibalism/cannibalism_hannibal_resonance_seal_sheet.dds`
- Sheet PNG: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_hannibal_resonance_seal/sheets/cannibalism_hannibal_resonance_seal_sheet.png`
- Static sprite name: `GFX_cannibalism_hannibal_resonance_seal_static`
- Animated sprite name: `GFX_cannibalism_hannibal_resonance_seal_animated`
- Target frame size: 64x64
- Frame count: 8
- Calculated sheet size: 512x64
- Animation rate: 8 fps recommended
- Looping: yes
- play_on_show: yes
- Anchor: center
- Source frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_hannibal_resonance_seal/source_frames/`
- Processed frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_hannibal_resonance_seal/processed_frames/`
- GIF preview: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_hannibal_resonance_seal/previews/cannibalism_hannibal_resonance_seal_preview.gif`
- Contact sheet: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_hannibal_resonance_seal/previews/cannibalism_hannibal_resonance_seal_contact.png`
- Behavior: decorative/state-driven scripted GUI visual; parent owns triggers and visibility wiring.

Ready-to-copy snippet, subject to parent verification against the chosen `.gfx` file:

```txt
spriteType = {
	name = "GFX_cannibalism_hannibal_resonance_seal_static"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_hannibal_resonance_seal_static.dds"
}
frameAnimatedSpriteType = {
	name = "GFX_cannibalism_hannibal_resonance_seal_animated"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_hannibal_resonance_seal_sheet.dds"
	noOfFrames = 8
	animation_rate_fps = 8
	looping = yes
	play_on_show = yes
}
```

## cannibalism_council_portrait_overlay

- Final static DDS: `gfx/interface/animated/014_cannibalism/cannibalism_council_portrait_overlay_static.dds`
- Final sheet DDS: `gfx/interface/animated/014_cannibalism/cannibalism_council_portrait_overlay_sheet.dds`
- Sheet PNG: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_council_portrait_overlay/sheets/cannibalism_council_portrait_overlay_sheet.png`
- Static sprite name: `GFX_cannibalism_council_portrait_overlay_static`
- Animated sprite name: `GFX_cannibalism_council_portrait_overlay_animated`
- Target frame size: 64x64
- Frame count: 8
- Calculated sheet size: 512x64
- Animation rate: 8 fps recommended
- Looping: yes
- play_on_show: yes
- Anchor: center
- Source frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_council_portrait_overlay/source_frames/`
- Processed frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_council_portrait_overlay/processed_frames/`
- GIF preview: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_council_portrait_overlay/previews/cannibalism_council_portrait_overlay_preview.gif`
- Contact sheet: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_council_portrait_overlay/previews/cannibalism_council_portrait_overlay_contact.png`
- Behavior: decorative/state-driven scripted GUI visual; parent owns triggers and visibility wiring.

Ready-to-copy snippet, subject to parent verification against the chosen `.gfx` file:

```txt
spriteType = {
	name = "GFX_cannibalism_council_portrait_overlay_static"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_council_portrait_overlay_static.dds"
}
frameAnimatedSpriteType = {
	name = "GFX_cannibalism_council_portrait_overlay_animated"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_council_portrait_overlay_sheet.dds"
	noOfFrames = 8
	animation_rate_fps = 8
	looping = yes
	play_on_show = yes
}
```

## cannibalism_world_end_progress_border

- Final static DDS: `gfx/interface/animated/014_cannibalism/cannibalism_world_end_progress_border_static.dds`
- Final sheet DDS: `gfx/interface/animated/014_cannibalism/cannibalism_world_end_progress_border_sheet.dds`
- Sheet PNG: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_world_end_progress_border/sheets/cannibalism_world_end_progress_border_sheet.png`
- Static sprite name: `GFX_cannibalism_world_end_progress_border_static`
- Animated sprite name: `GFX_cannibalism_world_end_progress_border_animated`
- Target frame size: 64x64
- Frame count: 8
- Calculated sheet size: 512x64
- Animation rate: 8 fps recommended
- Looping: yes
- play_on_show: yes
- Anchor: center
- Source frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_world_end_progress_border/source_frames/`
- Processed frames: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_world_end_progress_border/processed_frames/`
- GIF preview: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_world_end_progress_border/previews/cannibalism_world_end_progress_border_preview.gif`
- Contact sheet: `docs/assets/014_cannibalism/animations_imagegen/cannibalism_world_end_progress_border/previews/cannibalism_world_end_progress_border_contact.png`
- Behavior: decorative/state-driven scripted GUI visual; parent owns triggers and visibility wiring.

Ready-to-copy snippet, subject to parent verification against the chosen `.gfx` file:

```txt
spriteType = {
	name = "GFX_cannibalism_world_end_progress_border_static"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_world_end_progress_border_static.dds"
}
frameAnimatedSpriteType = {
	name = "GFX_cannibalism_world_end_progress_border_animated"
	texturefile = "gfx/interface/animated/014_cannibalism/cannibalism_world_end_progress_border_sheet.dds"
	noOfFrames = 8
	animation_rate_fps = 8
	looping = yes
	play_on_show = yes
}
```

## Validation Notes

- Processed PNG frames are 64x64 RGBA for all six packages.
- Horizontal sheet PNGs and DDS files are 512x64 for all six packages.
- Static fallback DDS files are 64x64 for all six packages.
- Processed frames report zero opaque chroma-green pixels after removal.
- DDS files reopen through Pillow at the expected dimensions.
- The asset worker did not delete old procedural assets `cannibalism_table_pulse_*`, `cannibalism_warning_larder_*`, and `cannibalism_signal_map_*`.
- Hannibal leader DDS unchanged: `True`.

Parent cleanup note: after parent `.gfx` wiring no longer referenced them, the old procedural DDS files were deleted from `gfx/interface/animated/014_cannibalism/`.

## Remaining Risks / Needs Parent Review

- Parent must wire sprites into the correct `.gfx`/`.gui`/scripted-GUI surfaces; this package intentionally did not edit wiring files.
- Parent should review the GIF previews/contact sheets for art-direction acceptance before replacing the old procedural live assets.
- Sprite names are final for this asset package: `GFX_<assigned_slug>` for static fallbacks and `GFX_<assigned_slug>_animated` for animated sheets, using the six assigned slugs exactly.

Manifest: `docs/assets/014_cannibalism/animations_imagegen/manifest.md` and `docs/assets/014_cannibalism/animations_imagegen/manifest.json`
## Post-cleanup chroma validation

- Rebuilt processed frames, sheets, DDS files, GIF previews, and contact sheets after strict chroma cleanup.
- Manifest validation reports zero opaque green/chroma pixels in all processed frames.

