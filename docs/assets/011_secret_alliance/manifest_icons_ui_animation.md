# Event 011 Secret Alliance Icon, UI, Achievement, and Animation Manifest

- Event id: `011`
- Event slug: `secret_alliance`
- Source mode: built-in `$imagegen` for every new artwork source; deterministic processing only after source selection
- Runtime conversion: `.tools/convert_to_dds.py`, one mip, 32-bit BGRA/B8G8R8A8-style masks
- Target sprite registry: `interface/011_secret_alliance.gfx`
- Achievement registry: `interface/chaosx_achievements.gfx`
- Prompt ledger: `docs/assets/011_secret_alliance/prompts/icon_ui_animation_prompts.md`
- Conversion ledger: `docs/assets/011_secret_alliance/conversion_manifest.tsv`
- Validation report: `docs/assets/011_secret_alliance/validation_icons_ui_animation.txt`

## Reference inspection and approved dimensions

The asset-type reference subfolders named by the asset skill were absent in this checkout. The parent implementation approved the skill's nearest-reference route. The following real local precedents were inspected before production:

- decision and category icons: `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_decisions.png`
- idea icons: `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_ideas.png`
- achievements and not-eligible treatment: `docs/assets/015_utopia_manifesto/contact_sheets/achievements_regenerated_imagegen_contact.png`
- scripted-GUI panel, card, and meter treatment: `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_abnormal_gui_static_contact.png`
- mixed event asset sizing/readability: `docs/assets/017_random_faction/contact_sheets/event17_processed_static_contact_sheet.png`
- animation wiring: `interface/013_natural_disasters.gfx`, `interface/013_natural_disasters.gui`, and vanilla `interface/alerts.gfx`
- faction logo precedent: `gfx/interface/factions/faction_logos/005_soviet_collapse/`, where full logos are `200x100` and miniatures are `32x32`
- offline wiki: `Graphical asset modding`, `Interface modding`, and `Scripted GUI modding`

The parent implementation confirmed this Event 011 contract before final processing:

- panel `720x360`
- category, decision, and status icons `32x32`
- idea and Event 011 UI emblem `64x64`
- meter frames and fills `256x24`
- suspect-card states `184x96` each, four-frame horizontal sheet `736x96`
- animation frames `128x96`, eight-frame horizontal sheet `1024x96`
- achievements `64x64`

The single Event 011 emblem is a compact scripted-GUI seal at `64x64`, not a replacement for the engine's separate full and miniature faction-logo pair.

## Category and mechanic UI assets

All rows use source mode `$imagegen`; `wired_complete` means the final PNG/DDS exists, its stable sprite is registered, and the gameplay or GUI surface uses that registration.

| Asset | Type and use | Prompt | Source PNG | Processed PNG | Final DDS | Size | Sprite | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `category_foreign_interference` | decision-category icon; baseline foreign-interference category | prompt-ledger category row | `source_png/decision_category_foreign_interference_source.png` | `processed_png/decision_category_foreign_interference.png` | `gfx/interface/decisions/011_secret_alliance/decision_category_foreign_interference.dds` | 32x32 | `GFX_decision_category_011_secret_alliance_foreign_interference` | `wired_complete` |
| `category_coalition_crisis` | decision-category icon; Evolution III/reveal category | prompt-ledger category row | `source_png/decision_category_coalition_crisis_source.png` | `processed_png/decision_category_coalition_crisis.png` | `gfx/interface/decisions/011_secret_alliance/decision_category_coalition_crisis.dds` | 32x32 | `GFX_decision_category_011_secret_alliance_coalition_crisis` | `wired_complete` |
| `panel_counter_network` | opaque scripted-GUI background with two meter lanes, three card spaces, and status/button region | prompt-ledger panel row | `source_png/counter_network_panel_source.png` | `processed_png/counter_network_panel.png` | `gfx/interface/011_secret_alliance/counter_network_panel.dds` | 720x360 | `GFX_011_secret_alliance_counter_network_panel` | `wired_complete` |
| `meter_evidence_frame` | transparent evidence meter frame | prompt-ledger meter row | `source_png/evidence_meter_frame_source.png` | `processed_png/evidence_meter_frame.png` | `gfx/interface/011_secret_alliance/evidence_meter_frame.dds` | 256x24 | `GFX_011_secret_alliance_evidence_meter_frame` | `wired_complete` |
| `meter_evidence_fill` | transparent evidence fill; generated source art and deterministic exact-size processing | prompt-ledger meter row | `source_png/evidence_meter_fill_source.png` | `processed_png/evidence_meter_fill.png` | `gfx/interface/011_secret_alliance/evidence_meter_fill.dds` | 256x24 | `GFX_011_secret_alliance_evidence_meter_fill` | `wired_complete` |
| `meter_preparedness_frame` | transparent preparedness meter frame | prompt-ledger meter row | `source_png/preparedness_meter_frame_source.png` | `processed_png/preparedness_meter_frame.png` | `gfx/interface/011_secret_alliance/preparedness_meter_frame.dds` | 256x24 | `GFX_011_secret_alliance_preparedness_meter_frame` | `wired_complete` |
| `meter_preparedness_fill` | transparent preparedness fill; generated source art and deterministic exact-size processing | prompt-ledger meter row | `source_png/preparedness_meter_fill_source.png` | `processed_png/preparedness_meter_fill.png` | `gfx/interface/011_secret_alliance/preparedness_meter_fill.dds` | 256x24 | `GFX_011_secret_alliance_preparedness_meter_fill` | `wired_complete` |
| `suspect_card` | four confidence states: unknown, possible, likely, confirmed; one left-to-right multi-frame sheet | prompt-ledger suspect rows | `source_png/suspect_card_{unknown,possible,likely,confirmed}_source.png` | `processed_png/suspect_card_{unknown,possible,likely,confirmed}.png`, `processed_png/suspect_card_states.png` | `gfx/interface/011_secret_alliance/suspect_card_states.dds` | 4x184x96; sheet 736x96 | `GFX_011_secret_alliance_suspect_card_states` | `wired_complete` |
| `status_recent_operation` | recent-operation status icon | prompt-ledger status row | `source_png/status_recent_operation_source.png` | `processed_png/status_recent_operation.png` | `gfx/interface/011_secret_alliance/status_recent_operation.dds` | 32x32 | `GFX_011_secret_alliance_status_recent_operation` | `wired_complete` |
| `status_turned_channel` | turned-channel status icon | prompt-ledger status row | `source_png/status_turned_channel_source.png` | `processed_png/status_turned_channel.png` | `gfx/interface/011_secret_alliance/status_turned_channel.dds` | 32x32 | `GFX_011_secret_alliance_status_turned_channel` | `wired_complete` |
| `status_false_lead` | false-lead status icon | prompt-ledger status row | `source_png/status_false_lead_source.png` | `processed_png/status_false_lead.png` | `gfx/interface/011_secret_alliance/status_false_lead.dds` | 32x32 | `GFX_011_secret_alliance_status_false_lead` | `wired_complete` |
| `status_war_pressure` | Evolution III war-pressure warning icon | prompt-ledger status row | `source_png/status_war_pressure_source.png` | `processed_png/status_war_pressure.png` | `gfx/interface/011_secret_alliance/status_war_pressure.dds` | 32x32 | `GFX_011_secret_alliance_status_war_pressure` | `wired_complete` |
| `faction_anti_target_pact` | fictional procedural coalition emblem for Event 011 GUI/reveal presentation | prompt-ledger emblem row | `source_png/faction_anti_target_pact_emblem_source.png` | `processed_png/faction_anti_target_pact_emblem.png` | `gfx/interface/011_secret_alliance/faction_anti_target_pact_emblem.dds` | 64x64 | `GFX_011_secret_alliance_faction_emblem` | `wired_complete` |

## Decision icons

Every decision icon has its own `$imagegen` source composition designed for `32x32`. No decision icon is a resized idea, focus, category, or status asset.

| Asset | Intended decision | Prompt | Source PNG | Processed PNG | Final DDS | Sprite | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `decision_compare_traffic` | compare covert traffic | prompt-ledger decision row | `source_png/decision_compare_traffic_source.png` | `processed_png/decision_compare_traffic.png` | `gfx/interface/decisions/011_secret_alliance/decision_compare_traffic.dds` | `GFX_decision_011_secret_alliance_compare_traffic` | `wired_complete` |
| `decision_trace_courier` | trace courier | prompt-ledger decision row | `source_png/decision_trace_courier_source.png` | `processed_png/decision_trace_courier.png` | `gfx/interface/decisions/011_secret_alliance/decision_trace_courier.dds` | `GFX_decision_011_secret_alliance_trace_courier` | `wired_complete` |
| `decision_compare_sabotage` | compare sabotage signatures | prompt-ledger decision row | `source_png/decision_compare_sabotage_source.png` | `processed_png/decision_compare_sabotage.png` | `gfx/interface/decisions/011_secret_alliance/decision_compare_sabotage.dds` | `GFX_decision_011_secret_alliance_compare_sabotage` | `wired_complete` |
| `decision_compartmentalize` | compartmentalize state information | prompt-ledger decision row | `source_png/decision_compartmentalize_source.png` | `processed_png/decision_compartmentalize.png` | `gfx/interface/decisions/011_secret_alliance/decision_compartmentalize.dds` | `GFX_decision_011_secret_alliance_compartmentalize` | `wired_complete` |
| `decision_secure_industry` | secure industry | prompt-ledger decision row | `source_png/decision_secure_industry_source.png` | `processed_png/decision_secure_industry.png` | `gfx/interface/decisions/011_secret_alliance/decision_secure_industry.dds` | `GFX_decision_011_secret_alliance_secure_industry` | `wired_complete` |
| `decision_harden_border` | harden border | prompt-ledger decision row | `source_png/decision_harden_border_source.png` | `processed_png/decision_harden_border.png` | `gfx/interface/decisions/011_secret_alliance/decision_harden_border.dds` | `GFX_decision_011_secret_alliance_harden_border` | `wired_complete` |
| `decision_quiet_approach` | quiet diplomatic approach | prompt-ledger decision row | `source_png/decision_quiet_approach_source.png` | `processed_png/decision_quiet_approach.png` | `gfx/interface/decisions/011_secret_alliance/decision_quiet_approach.dds` | `GFX_decision_011_secret_alliance_quiet_approach` | `wired_complete` |
| `decision_security_guarantee` | offer security guarantee | prompt-ledger decision row | `source_png/decision_security_guarantee_source.png` | `processed_png/decision_security_guarantee.png` | `gfx/interface/decisions/011_secret_alliance/decision_security_guarantee.dds` | `GFX_decision_011_secret_alliance_security_guarantee` | `wired_complete` |
| `decision_feed_false_plans` | feed false plans | prompt-ledger decision row | `source_png/decision_feed_false_plans_source.png` | `processed_png/decision_feed_false_plans.png` | `gfx/interface/decisions/011_secret_alliance/decision_feed_false_plans.dds` | `GFX_decision_011_secret_alliance_feed_false_plans` | `wired_complete` |
| `decision_turn_member` | turn a pact member | prompt-ledger decision row | `source_png/decision_turn_member_source.png` | `processed_png/decision_turn_member.png` | `gfx/interface/decisions/011_secret_alliance/decision_turn_member.dds` | `GFX_decision_011_secret_alliance_turn_member` | `wired_complete` |
| `decision_disrupt_conference` | disrupt conference | prompt-ledger decision row | `source_png/decision_disrupt_conference_source.png` | `processed_png/decision_disrupt_conference.png` | `gfx/interface/decisions/011_secret_alliance/decision_disrupt_conference.dds` | `GFX_decision_011_secret_alliance_disrupt_conference` | `wired_complete` |
| `decision_border_intercept` | border intercept | prompt-ledger decision row | `source_png/decision_border_intercept_source.png` | `processed_png/decision_border_intercept.png` | `gfx/interface/decisions/011_secret_alliance/decision_border_intercept.dds` | `GFX_decision_011_secret_alliance_border_intercept` | `wired_complete` |
| `decision_release_dossier` | public dossier release | prompt-ledger decision row | `source_png/decision_release_dossier_source.png` | `processed_png/decision_release_dossier.png` | `gfx/interface/decisions/011_secret_alliance/decision_release_dossier.dds` | `GFX_decision_011_secret_alliance_release_dossier` | `wired_complete` |
| `decision_emergency_mobilization` | emergency mobilization | prompt-ledger decision row | `source_png/decision_emergency_mobilization_source.png` | `processed_png/decision_emergency_mobilization.png` | `gfx/interface/decisions/011_secret_alliance/decision_emergency_mobilization.dds` | `GFX_decision_011_secret_alliance_emergency_mobilization` | `wired_complete` |
| `decision_preempt_coalition` | preempt coalition | prompt-ledger decision row | `source_png/decision_preempt_coalition_source.png` | `processed_png/decision_preempt_coalition.png` | `gfx/interface/decisions/011_secret_alliance/decision_preempt_coalition.dds` | `GFX_decision_011_secret_alliance_preempt_coalition` | `wired_complete` |
| `decision_offer_separate_terms` | offer separate terms | prompt-ledger decision row | `source_png/decision_offer_separate_terms_source.png` | `processed_png/decision_offer_separate_terms.png` | `gfx/interface/decisions/011_secret_alliance/decision_offer_separate_terms.dds` | `GFX_decision_011_secret_alliance_offer_separate_terms` | `wired_complete` |
| `decision_strike_depots` | strike coalition depots | prompt-ledger decision row | `source_png/decision_strike_depots_source.png` | `processed_png/decision_strike_depots.png` | `gfx/interface/decisions/011_secret_alliance/decision_strike_depots.dds` | `GFX_decision_011_secret_alliance_strike_depots` | `wired_complete` |

## Idea and national-spirit icons

Every idea icon has its own `$imagegen` source composition designed for `64x64`, without a focus-icon frame.

| Asset | Lifecycle role | Prompt | Source PNG | Processed PNG | Final DDS | Sprite | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `idea_unexplained_interference` | early mixed pressure | prompt-ledger idea row | `source_png/idea_unexplained_interference_source.png` | `processed_png/idea_unexplained_interference.png` | `gfx/interface/ideas/011_secret_alliance/idea_unexplained_interference.dds` | `GFX_idea_011_secret_alliance_unexplained_interference` | `wired_complete` |
| `idea_compromised_channels` | penetration penalty | prompt-ledger idea row | `source_png/idea_compromised_channels_source.png` | `processed_png/idea_compromised_channels.png` | `gfx/interface/ideas/011_secret_alliance/idea_compromised_channels.dds` | `GFX_idea_011_secret_alliance_compromised_channels` | `wired_complete` |
| `idea_hardened_networks` | preparedness benefit | prompt-ledger idea row | `source_png/idea_hardened_networks_source.png` | `processed_png/idea_hardened_networks.png` | `gfx/interface/ideas/011_secret_alliance/idea_hardened_networks.dds` | `GFX_idea_011_secret_alliance_hardened_networks` | `wired_complete` |
| `idea_public_coalition_pressure` | Evolution III pressure | prompt-ledger idea row | `source_png/idea_public_coalition_pressure_source.png` | `processed_png/idea_public_coalition_pressure.png` | `gfx/interface/ideas/011_secret_alliance/idea_public_coalition_pressure.dds` | `GFX_idea_011_secret_alliance_public_coalition_pressure` | `wired_complete` |
| `idea_known_enemy_plans` | Evidence conversion benefit | prompt-ledger idea row | `source_png/idea_known_enemy_plans_source.png` | `processed_png/idea_known_enemy_plans.png` | `gfx/interface/ideas/011_secret_alliance/idea_known_enemy_plans.dds` | `GFX_idea_011_secret_alliance_known_enemy_plans` | `wired_complete` |
| `idea_coalition_opening_coordination` | coalition readiness conversion | prompt-ledger idea row | `source_png/idea_coalition_opening_coordination_source.png` | `processed_png/idea_coalition_opening_coordination.png` | `gfx/interface/ideas/011_secret_alliance/idea_coalition_opening_coordination.dds` | `GFX_idea_011_secret_alliance_coalition_opening_coordination` | `wired_complete` |
| `idea_fractured_coalition` | low-Resolve penalty | prompt-ledger idea row | `source_png/idea_fractured_coalition_source.png` | `processed_png/idea_fractured_coalition.png` | `gfx/interface/ideas/011_secret_alliance/idea_fractured_coalition.dds` | `GFX_idea_011_secret_alliance_fractured_coalition` | `wired_complete` |

## Achievement triplets

Each completed icon is a distinct opaque `$imagegen` composition. The grey variant is an exact black-and-white conversion. The not-eligible variant composites `source_png/achievement_not_eligible_overlay_recovered.png` over the grey icon. The overlay is the accepted repository treatment recovered for Event 013 from eight grey/not-eligible pairs; its documented mean reconstruction error is `0.07/255`, and its alpha coverage remains 939 pixels.

| Achievement ID | Prompt | Source PNG | Processed variants | Final DDS triplet | Size | Sprite triplet | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `011_secret_alliance_the_empty_chair` | prompt-ledger achievement row | `source_png/011_secret_alliance_the_empty_chair_source.png` | `processed_png/011_secret_alliance_the_empty_chair{,_grey,_not_eligible}.png` | `gfx/achievements/011_secret_alliance_the_empty_chair{,_grey,_not_eligible}.dds` | 64x64 | `GFX_achievement_011_secret_alliance_the_empty_chair{,_grey,_not_eligible}` | `wired_complete` |
| `011_secret_alliance_every_thread` | prompt-ledger achievement row | `source_png/011_secret_alliance_every_thread_source.png` | `processed_png/011_secret_alliance_every_thread{,_grey,_not_eligible}.png` | `gfx/achievements/011_secret_alliance_every_thread{,_grey,_not_eligible}.dds` | 64x64 | `GFX_achievement_011_secret_alliance_every_thread{,_grey,_not_eligible}` | `wired_complete` |
| `011_secret_alliance_their_man_in_the_room` | prompt-ledger achievement row | `source_png/011_secret_alliance_their_man_in_the_room_source.png` | `processed_png/011_secret_alliance_their_man_in_the_room{,_grey,_not_eligible}.png` | `gfx/achievements/011_secret_alliance_their_man_in_the_room{,_grey,_not_eligible}.dds` | 64x64 | `GFX_achievement_011_secret_alliance_their_man_in_the_room{,_grey,_not_eligible}` | `wired_complete` |
| `011_secret_alliance_divide_the_table` | prompt-ledger achievement row | `source_png/011_secret_alliance_divide_the_table_source.png` | `processed_png/011_secret_alliance_divide_the_table{,_grey,_not_eligible}.png` | `gfx/achievements/011_secret_alliance_divide_the_table{,_grey,_not_eligible}.dds` | 64x64 | `GFX_achievement_011_secret_alliance_divide_the_table{,_grey,_not_eligible}` | `wired_complete` |
| `011_secret_alliance_surrounded_not_buried` | prompt-ledger achievement row | `source_png/011_secret_alliance_surrounded_not_buried_source.png` | `processed_png/011_secret_alliance_surrounded_not_buried{,_grey,_not_eligible}.png` | `gfx/achievements/011_secret_alliance_surrounded_not_buried{,_grey,_not_eligible}.dds` | 64x64 | `GFX_achievement_011_secret_alliance_surrounded_not_buried{,_grey,_not_eligible}` | `wired_complete` |
| `011_secret_alliance_two_giants_one_grave` | prompt-ledger achievement row | `source_png/011_secret_alliance_two_giants_one_grave_source.png` | `processed_png/011_secret_alliance_two_giants_one_grave{,_grey,_not_eligible}.png` | `gfx/achievements/011_secret_alliance_two_giants_one_grave{,_grey,_not_eligible}.dds` | 64x64 | `GFX_achievement_011_secret_alliance_two_giants_one_grave{,_grey,_not_eligible}` | `wired_complete` |

## Coalition-closure warning animation

| Field | Value |
| --- | --- |
| Asset | `coalition_closure_warning` |
| Use | Evolution III active with offensive countdown running |
| Source mode | eight separate `$imagegen` source frames; frame 004 generated first, seven explicit state edits using frame 004 as the identity reference |
| Source frames | `animations/coalition_closure_warning/source_frames/coalition_closure_warning_000_source.png` through `_007_source.png` |
| Processed frames | `animations/coalition_closure_warning/processed_frames/coalition_closure_warning_000.png` through `_007.png` |
| Frame size | 128x96 |
| Sheet PNG | `animations/coalition_closure_warning/sheets/coalition_closure_warning_sheet.png` |
| Sheet DDS | `gfx/interface/011_secret_alliance/coalition_closure_warning_sheet.dds` |
| Sheet size | 1024x96 |
| Static PNG | `animations/coalition_closure_warning/sheets/coalition_closure_warning_static.png`, approved frame 004 |
| Static DDS | `gfx/interface/011_secret_alliance/coalition_closure_warning_static.dds` |
| Static sprite | `GFX_011_secret_alliance_coalition_closure_warning` |
| Animated sprite | `GFX_011_secret_alliance_coalition_closure_warning_animated` |
| Timing | 8 FPS, looped, `play_on_show = yes`, `pause_on_loop = 0.0` |
| Anchor | centered broken seal and fixed outer arm pivots |
| Preview | `animations/coalition_closure_warning/previews/coalition_closure_warning_preview.gif`, review only |
| Contact sheet | `animations/coalition_closure_warning/previews/coalition_closure_warning_contact.png` |
| Brief and plan | `animations/coalition_closure_warning/brief.md`, `animations/coalition_closure_warning/frame_plan.md` |
| Status | `wired_complete` |

Every source frame has a unique SHA-256 hash. The processed frames remain unique. The sheet contains eight exact left-to-right frame columns. No source or final frame was made by moving, scaling, rotating, warping, blurring, recoloring, or filtering one still.

## Review contact sheets

- `contact_sheets/event011_decision_icons_contact.png`
- `contact_sheets/event011_idea_and_faction_icons_contact.png`
- `contact_sheets/event011_counter_network_ui_contact.png`
- `contact_sheets/event011_achievement_triplets_contact.png`
- `animations/coalition_closure_warning/previews/coalition_closure_warning_contact.png`

## Processing and validation notes

- Official imagegen chroma removal used `remove_chroma_key.py --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill` for all transparent sources.
- QA rejected three independently generated suspect-card elevations and replaced them with precise edits of the approved unknown card; the selected four-state family now keeps one frame, camera, flag aperture, paper field, and scale.
- All 57 runtime DDS targets use one-mip 32-bit BGRA/B8G8R8A8-style masks.
- The transparency audit checked 38 transparent runtime files, 143,172 visible alpha pixels, transparent corners, and found zero visible bright chroma-green pixels.
- Decision sources: 17 unique. Idea sources: 7 unique. Animation sources: 8 unique. Animation processed frames: 8 unique.
- No gameplay, localisation, GUI, GFX, achievement registry, decision, idea, or spreadsheet file was edited by the asset-production tranche. Final wiring was subsequently completed in the registered Event 011 and shared achievement interfaces.

## Simplifications, omissions, and blockers

No requested asset was simplified or omitted. No asset blocker remains. The missing skill-pack reference subfolders and canonical overlay file were resolved through the parent-approved repository precedent route: real Event 013/015/017 contact sheets and the accepted recovered repository overlay. This changed no requested filename, sprite name, target dimension, asset count, or visual family.
