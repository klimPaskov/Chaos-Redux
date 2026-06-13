# Fury Leader Flame Overlay GFX Handoff

## Sprite Definitions

Implemented in `interface/007_fury.gfx`:

```txt
spriteType = {
	name = "GFX_fury_leader_flame_overlay_static"
	texturefile = "gfx/interface/leader_frames/fury/fury_leader_flame_overlay_static.dds"
	alwaystransparent = yes
}

frameAnimatedSpriteType = {
	name = "GFX_fury_leader_flame_overlay_animated"
	texturefile = "gfx/interface/leader_frames/fury/fury_leader_flame_overlay_sheet.dds"
	noOfFrames = 8
	animation_rate_fps = 8
	looping = yes
	play_on_show = yes
	pause_on_loop = 0.0
	alwaystransparent = yes
}
```

## GUI Wiring

Implemented in `interface/007_fury_leader_overlay.gui` and `common/scripted_guis/007_fury_scripted_guis.txt`.

- `fury_diplomacy_leader_overlay_scripted_gui`
  - context: `diplomacy_target_context`
  - parent token: `selected_country_view_diplomacy`
  - scripted GUI visibility: `is_fury_actor = yes`
  - icon-level visibility: `fury_diplomacy_leader_flame_overlay_visible = { is_fury_actor = yes }`
  - position matches the vanilla diplomacy `leader_portrait` placement inside `diplomacy_tab_top` at `x = 20`, `y = 10`, `scale = 0.74`

## Validation

- Frame PNGs: `8`, each `156x210`.
- Sheet PNG: `1248x210`.
- Sheet DDS: `1248x210`, `srgba`.
- Static DDS: `156x210`, `srgba`.
- Review GIF exists for visual loop inspection.
- No other leader surface is wired; the animated flame icon is visible only when the active diplomacy target scope is a Fury actor.
