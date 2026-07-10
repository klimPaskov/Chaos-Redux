# Event 011 Secret Alliance Icon, UI, Achievement, and Animation GFX/GUI Handoff

This handoff covers the non-event-picture tranche only. It does not edit GFX, GUI, scripted GUI, gameplay, localisation, or achievement registries.

## Stable runtime contract

- Target event GFX: `interface/011_secret_alliance.gfx`
- Target event GUI: `interface/011_secret_alliance.gui`
- Target scripted GUI: `common/scripted_guis/011_secret_alliance_scripted_gui.txt`
- Target achievement GFX: `interface/chaosx_achievements.gfx`
- Panel: `720x360`
- Meter frames/fills: `256x24`
- Suspect states: four `184x96` frames in one `736x96` horizontal sheet, order `unknown`, `possible`, `likely`, `confirmed`
- Category/status/decision icons: `32x32`
- Idea/emblem icons: `64x64`
- Coalition warning: eight `128x96` frames in one `1024x96` horizontal sheet, `8` FPS

## Ready-to-copy Event 011 sprite definitions

```txt
spriteTypes = {
	spriteType = { name = "GFX_decision_category_011_secret_alliance_foreign_interference" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_category_foreign_interference.dds" }
	spriteType = { name = "GFX_decision_category_011_secret_alliance_coalition_crisis" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_category_coalition_crisis.dds" }

	spriteType = { name = "GFX_011_secret_alliance_counter_network_panel" texturefile = "gfx/interface/011_secret_alliance/counter_network_panel.dds" }
	spriteType = { name = "GFX_011_secret_alliance_evidence_meter_frame" texturefile = "gfx/interface/011_secret_alliance/evidence_meter_frame.dds" }
	spriteType = { name = "GFX_011_secret_alliance_evidence_meter_fill" texturefile = "gfx/interface/011_secret_alliance/evidence_meter_fill.dds" }
	spriteType = { name = "GFX_011_secret_alliance_preparedness_meter_frame" texturefile = "gfx/interface/011_secret_alliance/preparedness_meter_frame.dds" }
	spriteType = { name = "GFX_011_secret_alliance_preparedness_meter_fill" texturefile = "gfx/interface/011_secret_alliance/preparedness_meter_fill.dds" }
	spriteType = {
		name = "GFX_011_secret_alliance_suspect_card_states"
		texturefile = "gfx/interface/011_secret_alliance/suspect_card_states.dds"
		noOfFrames = 4
	}
	spriteType = { name = "GFX_011_secret_alliance_status_recent_operation" texturefile = "gfx/interface/011_secret_alliance/status_recent_operation.dds" }
	spriteType = { name = "GFX_011_secret_alliance_status_turned_channel" texturefile = "gfx/interface/011_secret_alliance/status_turned_channel.dds" }
	spriteType = { name = "GFX_011_secret_alliance_status_false_lead" texturefile = "gfx/interface/011_secret_alliance/status_false_lead.dds" }
	spriteType = { name = "GFX_011_secret_alliance_status_war_pressure" texturefile = "gfx/interface/011_secret_alliance/status_war_pressure.dds" }
	spriteType = { name = "GFX_011_secret_alliance_faction_emblem" texturefile = "gfx/interface/011_secret_alliance/faction_anti_target_pact_emblem.dds" }

	spriteType = { name = "GFX_011_secret_alliance_coalition_closure_warning" texturefile = "gfx/interface/011_secret_alliance/coalition_closure_warning_static.dds" alwaystransparent = yes }
	frameAnimatedSpriteType = {
		name = "GFX_011_secret_alliance_coalition_closure_warning_animated"
		texturefile = "gfx/interface/011_secret_alliance/coalition_closure_warning_sheet.dds"
		noOfFrames = 8
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
		pause_on_loop = 0.0
		alwaystransparent = yes
	}

	spriteType = { name = "GFX_decision_011_secret_alliance_compare_traffic" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_compare_traffic.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_trace_courier" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_trace_courier.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_compare_sabotage" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_compare_sabotage.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_compartmentalize" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_compartmentalize.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_secure_industry" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_secure_industry.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_harden_border" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_harden_border.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_quiet_approach" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_quiet_approach.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_security_guarantee" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_security_guarantee.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_feed_false_plans" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_feed_false_plans.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_turn_member" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_turn_member.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_disrupt_conference" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_disrupt_conference.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_border_intercept" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_border_intercept.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_release_dossier" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_release_dossier.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_emergency_mobilization" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_emergency_mobilization.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_preempt_coalition" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_preempt_coalition.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_offer_separate_terms" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_offer_separate_terms.dds" }
	spriteType = { name = "GFX_decision_011_secret_alliance_strike_depots" texturefile = "gfx/interface/decisions/011_secret_alliance/decision_strike_depots.dds" }

	spriteType = { name = "GFX_idea_011_secret_alliance_unexplained_interference" texturefile = "gfx/interface/ideas/011_secret_alliance/idea_unexplained_interference.dds" }
	spriteType = { name = "GFX_idea_011_secret_alliance_compromised_channels" texturefile = "gfx/interface/ideas/011_secret_alliance/idea_compromised_channels.dds" }
	spriteType = { name = "GFX_idea_011_secret_alliance_hardened_networks" texturefile = "gfx/interface/ideas/011_secret_alliance/idea_hardened_networks.dds" }
	spriteType = { name = "GFX_idea_011_secret_alliance_public_coalition_pressure" texturefile = "gfx/interface/ideas/011_secret_alliance/idea_public_coalition_pressure.dds" }
	spriteType = { name = "GFX_idea_011_secret_alliance_known_enemy_plans" texturefile = "gfx/interface/ideas/011_secret_alliance/idea_known_enemy_plans.dds" }
	spriteType = { name = "GFX_idea_011_secret_alliance_coalition_opening_coordination" texturefile = "gfx/interface/ideas/011_secret_alliance/idea_coalition_opening_coordination.dds" }
	spriteType = { name = "GFX_idea_011_secret_alliance_fractured_coalition" texturefile = "gfx/interface/ideas/011_secret_alliance/idea_fractured_coalition.dds" }
}
```

## Achievement sprite definitions

Add these inside the existing shared achievement sprite hierarchy in `interface/chaosx_achievements.gfx`; preserve the shared registry structure.

```txt
	spriteType = { name = "GFX_achievement_011_secret_alliance_the_empty_chair" texturefile = "gfx/achievements/011_secret_alliance_the_empty_chair.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_the_empty_chair_grey" texturefile = "gfx/achievements/011_secret_alliance_the_empty_chair_grey.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_the_empty_chair_not_eligible" texturefile = "gfx/achievements/011_secret_alliance_the_empty_chair_not_eligible.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_every_thread" texturefile = "gfx/achievements/011_secret_alliance_every_thread.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_every_thread_grey" texturefile = "gfx/achievements/011_secret_alliance_every_thread_grey.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_every_thread_not_eligible" texturefile = "gfx/achievements/011_secret_alliance_every_thread_not_eligible.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_their_man_in_the_room" texturefile = "gfx/achievements/011_secret_alliance_their_man_in_the_room.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_their_man_in_the_room_grey" texturefile = "gfx/achievements/011_secret_alliance_their_man_in_the_room_grey.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_their_man_in_the_room_not_eligible" texturefile = "gfx/achievements/011_secret_alliance_their_man_in_the_room_not_eligible.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_divide_the_table" texturefile = "gfx/achievements/011_secret_alliance_divide_the_table.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_divide_the_table_grey" texturefile = "gfx/achievements/011_secret_alliance_divide_the_table_grey.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_divide_the_table_not_eligible" texturefile = "gfx/achievements/011_secret_alliance_divide_the_table_not_eligible.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_surrounded_not_buried" texturefile = "gfx/achievements/011_secret_alliance_surrounded_not_buried.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_surrounded_not_buried_grey" texturefile = "gfx/achievements/011_secret_alliance_surrounded_not_buried_grey.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_surrounded_not_buried_not_eligible" texturefile = "gfx/achievements/011_secret_alliance_surrounded_not_buried_not_eligible.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_two_giants_one_grave" texturefile = "gfx/achievements/011_secret_alliance_two_giants_one_grave.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_two_giants_one_grave_grey" texturefile = "gfx/achievements/011_secret_alliance_two_giants_one_grave_grey.dds" }
	spriteType = { name = "GFX_achievement_011_secret_alliance_two_giants_one_grave_not_eligible" texturefile = "gfx/achievements/011_secret_alliance_two_giants_one_grave_not_eligible.dds" }
```

## GUI handoff

The panel artwork was generated around this compact layout contract. Coordinates are a safe first placement within a `720x360` container; the implementation agent may tune only within that contract.

| UI element | Suggested position | Size / frame |
| --- | --- | --- |
| panel background | `{ x = 0 y = 0 }` | 720x360 |
| Evidence frame/fill | `{ x = 232 y = 38 }` | 256x24 |
| Preparedness frame/fill | `{ x = 232 y = 88 }` | 256x24 |
| suspect card 1 | `{ x = 34 y = 154 }` | 184x96 |
| suspect card 2 | `{ x = 268 y = 154 }` | 184x96 |
| suspect card 3 | `{ x = 502 y = 154 }` | 184x96 |
| recent-operation/status icon | `{ x = 40 y = 300 }` | 32x32 |
| coalition warning animated/static | `{ x = 560 y = 24 }` | 128x96 |

Use `frame = 0`, `1`, `2`, or `3` on the suspect-card icon according to unknown/possible/likely/confirmed. If scripted GUI properties control the frame, the offline Scripted GUI wiki documents the `frame` property on multi-frame textures.

For the warning, define two `iconType` elements at the same position: one references `GFX_011_secret_alliance_coalition_closure_warning_animated`, the other the static sprite. Gate both with the same Evolution III/offensive-countdown trigger. Show the animated element when animations are enabled; show the static element when the player's animation-disable state is active. Both are decorative and should use `alwaystransparent = yes`.

The animation uses the verified horizontal `frameAnimatedSpriteType` pattern from the offline Graphical Asset Modding page, vanilla `interface/alerts.gfx`, and Chaos Redux Event 013. The GIF is review-only and must never appear in a texture path.

## Validation and unresolved wiring

- Every texture path above exists.
- Every DDS is one-mip 32-bit BGRA/B8G8R8A8-style with the registered dimensions.
- The suspect sheet order and animation sheet order were validated against their processed source frames.
- The animation has eight unique generated source frames and eight unique processed frames.
- The faction emblem is only an Event 011 scripted-GUI/UI seal. If implementation later requires the engine's full faction-logo surface, create a separately designed `200x100` full logo and `32x32` miniature rather than resizing this `64x64` emblem.
- No GFX or GUI file was edited by this asset tranche.

No asset blocker remains. The registrations in `interface/011_secret_alliance.gfx` and `interface/chaosx_achievements.gfx`, together with `interface/011_secret_alliance.gui`, complete the handoff. The final manifest status is `wired_complete`.
