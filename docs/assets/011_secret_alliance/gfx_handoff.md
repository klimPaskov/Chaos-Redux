# Event 011 Secret Alliance GFX Handoff

Suggested sprite registry: `interface/011_secret_alliance.gfx`

No `.gfx`, `.gui`, gameplay, localisation, or achievement script files were edited in this asset pass.

## Decision And Idea Sprites

```txt
spriteTypes = {
	spriteType = {
		name = "GFX_decision_category_secret_alliance_dossier"
		texturefile = "gfx/interface/decisions/011_secret_alliance/decision_category_secret_alliance_dossier.dds"
	}
	spriteType = {
		name = "GFX_decision_secret_alliance_courier"
		texturefile = "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_courier.dds"
	}
	spriteType = {
		name = "GFX_decision_secret_alliance_rail_guard"
		texturefile = "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_rail_guard.dds"
	}
	spriteType = {
		name = "GFX_decision_secret_alliance_expose"
		texturefile = "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_expose.dds"
	}
	spriteType = {
		name = "GFX_decision_secret_alliance_backchannel"
		texturefile = "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_backchannel.dds"
	}
	spriteType = {
		name = "GFX_decision_secret_alliance_border_watch"
		texturefile = "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_border_watch.dds"
	}
	spriteType = {
		name = "GFX_decision_secret_alliance_factory_shield"
		texturefile = "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_factory_shield.dds"
	}
	spriteType = {
		name = "GFX_decision_secret_alliance_false_leak"
		texturefile = "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_false_leak.dds"
	}
	spriteType = {
		name = "GFX_decision_secret_alliance_strike_first"
		texturefile = "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_strike_first.dds"
	}
	spriteType = {
		name = "GFX_idea_secret_alliance_dossier_pressure"
		texturefile = "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_dossier_pressure.dds"
	}
	spriteType = {
		name = "GFX_idea_secret_alliance_counter_network"
		texturefile = "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_counter_network.dds"
	}
	spriteType = {
		name = "GFX_idea_secret_alliance_protocol_discipline"
		texturefile = "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_protocol_discipline.dds"
	}
	spriteType = {
		name = "GFX_idea_secret_alliance_patron_liaisons"
		texturefile = "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_patron_liaisons.dds"
	}
	spriteType = {
		name = "GFX_idea_secret_alliance_exposed_signatory"
		texturefile = "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_exposed_signatory.dds"
	}
	spriteType = {
		name = "GFX_idea_secret_alliance_war_coordination"
		texturefile = "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_war_coordination.dds"
	}
	spriteType = {
		name = "GFX_idea_secret_alliance_credibility_restored"
		texturefile = "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_credibility_restored.dds"
	}
}
```

## Animated UI Sprites

All animated UI assets use generated frame sources, eight frames, `looping = yes`, and `play_on_show = yes`. GIF files are review previews only and should not be used in `.gfx`.

```txt
spriteTypes = {
	spriteType = {
		name = "GFX_secret_alliance_evidence_pulse_static"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_pulse_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_secret_alliance_evidence_pulse_animated"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_pulse_sheet.dds"
		noOfFrames = 8
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
	}
	spriteType = {
		name = "GFX_secret_alliance_readiness_warning_static"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_readiness_warning_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_secret_alliance_readiness_warning_animated"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_readiness_warning_sheet.dds"
		noOfFrames = 8
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
	}
	spriteType = {
		name = "GFX_secret_alliance_exposed_card_glow_static"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_exposed_card_glow_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_secret_alliance_exposed_card_glow_animated"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_exposed_card_glow_sheet.dds"
		noOfFrames = 8
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
	}
	spriteType = {
		name = "GFX_secret_alliance_war_countdown_ticker_static"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_war_countdown_ticker_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_secret_alliance_war_countdown_ticker_animated"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_war_countdown_ticker_sheet.dds"
		noOfFrames = 8
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
	}
	spriteType = {
		name = "GFX_secret_alliance_hidden_protocol_overlay_static"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_protocol_overlay_static.dds"
	}
	frameAnimatedSpriteType = {
		name = "GFX_secret_alliance_hidden_protocol_overlay_animated"
		texturefile = "gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_protocol_overlay_sheet.dds"
		noOfFrames = 8
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
	}
}
```

## Achievement Runtime Files

Achievements use the root achievement DDS convention. The exact runtime files are:

- `gfx/achievements/secret_alliance_empty_chair.dds`
- `gfx/achievements/secret_alliance_empty_chair_grey.dds`
- `gfx/achievements/secret_alliance_empty_chair_not_eligible.dds`
- `gfx/achievements/secret_alliance_all_names.dds`
- `gfx/achievements/secret_alliance_all_names_grey.dds`
- `gfx/achievements/secret_alliance_all_names_not_eligible.dds`
- `gfx/achievements/secret_alliance_three_knocks.dds`
- `gfx/achievements/secret_alliance_three_knocks_grey.dds`
- `gfx/achievements/secret_alliance_three_knocks_not_eligible.dds`
- `gfx/achievements/secret_alliance_lone_target.dds`
- `gfx/achievements/secret_alliance_lone_target_grey.dds`
- `gfx/achievements/secret_alliance_lone_target_not_eligible.dds`
- `gfx/achievements/secret_alliance_counter_protocol.dds`
- `gfx/achievements/secret_alliance_counter_protocol_grey.dds`
- `gfx/achievements/secret_alliance_counter_protocol_not_eligible.dds`
- `gfx/achievements/secret_alliance_wrong_room.dds`
- `gfx/achievements/secret_alliance_wrong_room_grey.dds`
- `gfx/achievements/secret_alliance_wrong_room_not_eligible.dds`
- `gfx/achievements/secret_alliance_no_patrons.dds`
- `gfx/achievements/secret_alliance_no_patrons_grey.dds`
- `gfx/achievements/secret_alliance_no_patrons_not_eligible.dds`
- `gfx/achievements/secret_alliance_paid_in_promises.dds`
- `gfx/achievements/secret_alliance_paid_in_promises_grey.dds`
- `gfx/achievements/secret_alliance_paid_in_promises_not_eligible.dds`

## Animation Metadata

| Sprite stem | Frame size | Sheet size | Frames | FPS | Runtime state |
| --- | --- | --- | --- | --- | --- |
| `secret_alliance_evidence_pulse` | `64x64` | `512x64` | 8 | 8 | Exposure decision available |
| `secret_alliance_readiness_warning` | `64x64` | `512x64` | 8 | 8 | Near war threshold |
| `secret_alliance_exposed_card_glow` | `96x64` | `768x64` | 8 | 8 | Country confirmed/exposed |
| `secret_alliance_war_countdown_ticker` | `128x32` | `1024x32` | 8 | 8 | Public pact crisis countdown |
| `secret_alliance_hidden_protocol_overlay` | `96x96` | `768x96` | 8 | 8 | Public reveal or super-event support |

Uncertainty:

- Target `.gui` file and exact state trigger names are implementation-owned and were not inspected or edited in this asset pass.
- The non-64x64 animation dimensions are proposed by this asset pass because the parent prompt did not provide exact dimensions: exposed member card glow uses `96x64`, countdown ticker uses `128x32`, and hidden protocol overlay uses `96x96`.
