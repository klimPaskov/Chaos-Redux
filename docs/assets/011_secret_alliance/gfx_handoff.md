# Event 011 Secret Alliance `.gfx` handoff

Suggested `.gfx` files:
- Implemented target for all Event 011 sprites: `interface/011_secret_alliance.gfx`

## Event picture and scripted GUI sprites

| Sprite | DDS path | Related id | Size |
| --- | --- | --- | --- |
| `GFX_report_event_011_secret_alliance_courier` | `gfx/event_pictures/011_secret_alliance/report_event_011_secret_alliance_courier.dds` | `report_event_011_secret_alliance_courier` | `210x176` |
| `GFX_report_event_011_secret_alliance_sabotage` | `gfx/event_pictures/011_secret_alliance/report_event_011_secret_alliance_sabotage.dds` | `report_event_011_secret_alliance_sabotage` | `210x176` |
| `GFX_report_event_011_secret_alliance_defector` | `gfx/event_pictures/011_secret_alliance/report_event_011_secret_alliance_defector.dds` | `report_event_011_secret_alliance_defector` | `210x176` |
| `GFX_news_event_011_secret_alliance_reveal` | `gfx/event_pictures/011_secret_alliance/news_event_011_secret_alliance_reveal.dds` | `news_event_011_secret_alliance_reveal` | `397x153` |
| `GFX_secret_alliance_pact_emblem` | `gfx/interface/011_secret_alliance/secret_alliance_pact_emblem.dds` | `secret_alliance_pact_emblem` | `256x256` |
| `GFX_secret_alliance_board_bg` | `gfx/interface/011_secret_alliance/secret_alliance_board_bg.dds` | `secret_alliance_board_bg` | `1024x768` |
| `GFX_secret_alliance_suspect_card_frame` | `gfx/interface/011_secret_alliance/secret_alliance_suspect_card_frame.dds` | `secret_alliance_suspect_card_frame` | `220x300` |
| `GFX_secret_alliance_suspect_card_selected` | `gfx/interface/011_secret_alliance/secret_alliance_suspect_card_selected.dds` | `secret_alliance_suspect_card_selected` | `220x300` |
| `GFX_secret_alliance_suspect_card_dim` | `gfx/interface/011_secret_alliance/secret_alliance_suspect_card_dim.dds` | `secret_alliance_suspect_card_dim` | `220x300` |
| `GFX_secret_alliance_suspect_card_locked` | `gfx/interface/011_secret_alliance/secret_alliance_suspect_card_locked.dds` | `secret_alliance_suspect_card_locked` | `220x300` |
| `GFX_secret_alliance_evidence_meter_frame` | `gfx/interface/011_secret_alliance/secret_alliance_evidence_meter_frame.dds` | `secret_alliance_evidence_meter_frame` | `360x56` |
| `GFX_secret_alliance_evidence_meter_fill_low` | `gfx/interface/011_secret_alliance/secret_alliance_evidence_meter_fill_low.dds` | `secret_alliance_evidence_meter_fill_low` | `360x56` |
| `GFX_secret_alliance_evidence_meter_fill_mid` | `gfx/interface/011_secret_alliance/secret_alliance_evidence_meter_fill_mid.dds` | `secret_alliance_evidence_meter_fill_mid` | `360x56` |
| `GFX_secret_alliance_evidence_meter_fill_high` | `gfx/interface/011_secret_alliance/secret_alliance_evidence_meter_fill_high.dds` | `secret_alliance_evidence_meter_fill_high` | `360x56` |

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

Registered script-facing idea aliases:
- `GFX_idea_secret_alliance_unexplained_friction` -> `idea_secret_alliance_friction.dds`
- `GFX_idea_secret_alliance_counter_pact_bureau` -> `idea_secret_alliance_bureau.dds`
- `GFX_idea_secret_alliance_prepared_security_network` -> `idea_secret_alliance_prepared_network.dds`
- `GFX_idea_secret_alliance_compromised_ministries` -> `idea_secret_alliance_friction.dds`
- `GFX_idea_secret_alliance_hidden_compact_discipline` -> `idea_secret_alliance_prepared_network.dds`
- `GFX_idea_secret_alliance_exposed_pact_government` -> `idea_secret_alliance_exposed_member.dds`
- `GFX_idea_secret_alliance_revealed_compact` -> `idea_secret_alliance_exposed_member.dds`
- `GFX_idea_secret_alliance_public_war_command` -> `idea_secret_alliance_prepared_network.dds`

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
- `secret_alliance_evidence_meter_highlight` is registered as a compact highlight marker for the decision category or a future scripted GUI meter.
- Operation-specific decision sprite aliases are registered in `interface/011_secret_alliance.gfx` and intentionally point to the five generated decision icon families.
- Achievement icons are present as visible, grey, and not-eligible DDS triplets in `gfx/achievements/`; the event-owned `.gfx` file also exposes `GFX_achievement_sa_*` aliases for custom UI use.
