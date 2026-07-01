# Event 011 Secret Alliance `.gfx` handoff

Suggested `.gfx` files:
- Decisions and animated sprites: `interface/011_secret_alliance.gfx`
- Ideas: `interface/chaosx_ideas.gfx` or a new event-owned ideas block if the parent prefers
- Achievements: `interface/chaosx_achievements.gfx`

## Static icon sprites

| Sprite | DDS path | Related id | Size |
| --- | --- | --- | --- |
| `GFX_decision_category_secret_alliance` | `gfx/interface/decisions/011_secret_alliance/decision_category_secret_alliance.dds` | `decision_category_secret_alliance` | `32x32` |
| `GFX_decision_secret_alliance_investigate` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_investigate.dds` | `decision_secret_alliance_investigate` | `32x32` |
| `GFX_decision_secret_alliance_security` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_security.dds` | `decision_secret_alliance_security` | `32x32` |
| `GFX_decision_secret_alliance_split` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_split.dds` | `decision_secret_alliance_split` | `32x32` |
| `GFX_decision_secret_alliance_border_watch` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_border_watch.dds` | `decision_secret_alliance_border_watch` | `32x32` |
| `GFX_decision_secret_alliance_confront` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_confront.dds` | `decision_secret_alliance_confront` | `32x32` |
| `GFX_idea_secret_alliance_friction` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_friction.dds` | `idea_secret_alliance_friction` | `64x64` |
| `GFX_idea_secret_alliance_bureau` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_bureau.dds` | `idea_secret_alliance_bureau` | `64x64` |
| `GFX_idea_secret_alliance_prepared_network` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_prepared_network.dds` | `idea_secret_alliance_prepared_network` | `64x64` |
| `GFX_idea_secret_alliance_exposed_member` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_exposed_member.dds` | `idea_secret_alliance_exposed_member` | `64x64` |
| `GFX_idea_secret_alliance_patron_shield` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_patron_shield.dds` | `idea_secret_alliance_patron_shield` | `64x64` |

## Animated sprite package

Suggested HOI4 pattern:

```txt
spriteTypes = {
	spriteType = {
		name = "GFX_secret_alliance_hidden_seal"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_seal.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_secret_alliance_hidden_seal_animated"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_seal_animated.dds"
		noOfFrames = 8
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
	}
}
```

Repeat the same pattern for:
- `GFX_secret_alliance_evidence_meter_highlight` -> `gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_meter_highlight.dds`
- `GFX_secret_alliance_evidence_meter_highlight_animated` -> `gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_meter_highlight_animated.dds`
- `GFX_secret_alliance_crisis_frame` -> `gfx/interface/animated/011_secret_alliance/secret_alliance_crisis_frame.dds`
- `GFX_secret_alliance_crisis_frame_animated` -> `gfx/interface/animated/011_secret_alliance/secret_alliance_crisis_frame_animated.dds`

Animated metadata:

| Sprite pair | Frame size | Sheet size | Frames | Rate | Loop | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `GFX_secret_alliance_hidden_seal` / `GFX_secret_alliance_hidden_seal_animated` | `36x36` | `288x36` | `8` | `8 fps` | `yes` | small compact seal pulse |
| `GFX_secret_alliance_evidence_meter_highlight` / `GFX_secret_alliance_evidence_meter_highlight_animated` | `36x36` | `288x36` | `8` | `8 fps` | `yes` | compact evidence shimmer marker |
| `GFX_secret_alliance_crisis_frame` / `GFX_secret_alliance_crisis_frame_animated` | `36x36` | `288x36` | `8` | `8 fps` | `yes` | crisis-active warning frame |

Notes:
- All three animated assets were built from real eight-state source frames, not transform-only motion.
- `secret_alliance_evidence_meter_highlight` is the only package with mild placement uncertainty because the parent did not provide final meter geometry.
