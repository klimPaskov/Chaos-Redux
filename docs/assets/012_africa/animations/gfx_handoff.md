# Event 012 animation GFX handoff

The asset tranche is complete; the parent owns `.gfx`, `.gui`, scripted-GUI, decision, focus, and runtime registration. Use the exact texture paths and sprite names in `manifest.md`.

```txt
spriteTypes = {
	frameAnimatedSpriteType = {
		name = "<animated_sprite_name>"
		texturefile = "<runtime_sheet_dds_path>"
		noOfFrames = <frame_count>
		animation_rate_fps = <fps>
		looping = yes|no
		play_on_show = yes
	}
	spriteType = {
		name = "<static_sprite_name>"
		texturefile = "<runtime_static_dds_path>"
	}
}
```

Use `play_on_show = yes` for state-entry feedback where supported. `africa_is_one_completion` is non-looping and retains its final-frame fallback. The host overlay/proof kit and federal deadlock rows are state sequences rather than ambient loops. Route each remaining loop only while its listed state trigger is true.

Reference precedent inspected: canonical `assets/vanilla_reference/icons/decisions/contact_sheet.png`, the existing repository animation packages under this folder, and the local `chaos-redux-frame-animation` `frameAnimatedSpriteType` contract. No GFX or gameplay files were edited.

Review GIFs and contact sheets are evidence only. No runtime texture path points into `docs/assets/`.
