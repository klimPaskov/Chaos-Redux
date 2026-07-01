# Event 011 Secret Alliance asset manifest

Event id: `011`  
Event slug: `secret_alliance`  
Scope: report images, news image, scripted GUI art, decision category icon, decision icons, idea icons, achievement icons, and three small animated sprite packages.

Source mode summary:
- Transparent icons: generated with built-in `image_gen`, flat `#00ff00` chroma-key background, local alpha cleanup through `remove_chroma_key.py`.
- Achievements: generated full-frame painted squares, then resized to `64x64`.
- Small animations: generated as real `4x2` eight-frame source sheets, sliced into source frames, normalized to `36x36`, sheeted to `288x36`.

Build helper:
- `docs/assets/011_secret_alliance/build_assets.py`

Prompt log:
- `docs/assets/011_secret_alliance/prompts/generated_prompts.md`
- `docs/assets/011_secret_alliance/prompts/generated_event_art_prompts.md`

## Event pictures

| Asset | Source PNG | Processed PNG | Final DDS | Sprite | Size | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `report_event_011_secret_alliance_courier` | `docs/assets/011_secret_alliance/source_png/report_event_011_secret_alliance_courier_source.png` | `docs/assets/011_secret_alliance/processed_png/report_event_011_secret_alliance_courier.png` | `gfx/event_pictures/011_secret_alliance/report_event_011_secret_alliance_courier.dds` | `GFX_report_event_011_secret_alliance_courier` | `210x176` | `complete` |
| `report_event_011_secret_alliance_sabotage` | `docs/assets/011_secret_alliance/source_png/report_event_011_secret_alliance_sabotage_source.png` | `docs/assets/011_secret_alliance/processed_png/report_event_011_secret_alliance_sabotage.png` | `gfx/event_pictures/011_secret_alliance/report_event_011_secret_alliance_sabotage.dds` | `GFX_report_event_011_secret_alliance_sabotage` | `210x176` | `complete` |
| `report_event_011_secret_alliance_defector` | `docs/assets/011_secret_alliance/source_png/report_event_011_secret_alliance_defector_source.png` | `docs/assets/011_secret_alliance/processed_png/report_event_011_secret_alliance_defector.png` | `gfx/event_pictures/011_secret_alliance/report_event_011_secret_alliance_defector.dds` | `GFX_report_event_011_secret_alliance_defector` | `210x176` | `complete` |
| `news_event_011_secret_alliance_reveal` | `docs/assets/011_secret_alliance/source_png/news_event_011_secret_alliance_reveal_source.png` | `docs/assets/011_secret_alliance/processed_png/news_event_011_secret_alliance_reveal.png` | `gfx/event_pictures/011_secret_alliance/news_event_011_secret_alliance_reveal.dds` | `GFX_news_event_011_secret_alliance_reveal` | `397x153` | `complete` |

## Scripted GUI art

| Asset | Source PNG | Processed PNG | Final DDS | Sprite | Size | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `secret_alliance_pact_emblem` | `docs/assets/011_secret_alliance/source_png/secret_alliance_pact_emblem_source.png` | `docs/assets/011_secret_alliance/processed_png/secret_alliance_pact_emblem.png` | `gfx/interface/011_secret_alliance/secret_alliance_pact_emblem.dds` | `GFX_secret_alliance_pact_emblem` | `256x256` | `complete` |
| `secret_alliance_board_bg` | `docs/assets/011_secret_alliance/source_png/secret_alliance_board_bg_source.png` | `docs/assets/011_secret_alliance/processed_png/secret_alliance_board_bg.png` | `gfx/interface/011_secret_alliance/secret_alliance_board_bg.dds` | `GFX_secret_alliance_board_bg` | `1024x768` | `complete` |
| `secret_alliance_suspect_card_frame` | derived UI element | `docs/assets/011_secret_alliance/processed_png/secret_alliance_suspect_card_frame.png` | `gfx/interface/011_secret_alliance/secret_alliance_suspect_card_frame.dds` | `GFX_secret_alliance_suspect_card_frame` | `220x300` | `complete` |
| `secret_alliance_suspect_card_selected` | derived UI element | `docs/assets/011_secret_alliance/processed_png/secret_alliance_suspect_card_selected.png` | `gfx/interface/011_secret_alliance/secret_alliance_suspect_card_selected.dds` | `GFX_secret_alliance_suspect_card_selected` | `220x300` | `complete` |
| `secret_alliance_suspect_card_dim` | derived UI element | `docs/assets/011_secret_alliance/processed_png/secret_alliance_suspect_card_dim.png` | `gfx/interface/011_secret_alliance/secret_alliance_suspect_card_dim.dds` | `GFX_secret_alliance_suspect_card_dim` | `220x300` | `complete` |
| `secret_alliance_suspect_card_locked` | derived UI element | `docs/assets/011_secret_alliance/processed_png/secret_alliance_suspect_card_locked.png` | `gfx/interface/011_secret_alliance/secret_alliance_suspect_card_locked.dds` | `GFX_secret_alliance_suspect_card_locked` | `220x300` | `complete` |
| `secret_alliance_evidence_meter_frame` | derived UI element | `docs/assets/011_secret_alliance/processed_png/secret_alliance_evidence_meter_frame.png` | `gfx/interface/011_secret_alliance/secret_alliance_evidence_meter_frame.dds` | `GFX_secret_alliance_evidence_meter_frame` | `360x56` | `complete` |
| `secret_alliance_evidence_meter_fill_low` | derived UI element | `docs/assets/011_secret_alliance/processed_png/secret_alliance_evidence_meter_fill_low.png` | `gfx/interface/011_secret_alliance/secret_alliance_evidence_meter_fill_low.dds` | `GFX_secret_alliance_evidence_meter_fill_low` | `360x56` | `complete` |
| `secret_alliance_evidence_meter_fill_mid` | derived UI element | `docs/assets/011_secret_alliance/processed_png/secret_alliance_evidence_meter_fill_mid.png` | `gfx/interface/011_secret_alliance/secret_alliance_evidence_meter_fill_mid.dds` | `GFX_secret_alliance_evidence_meter_fill_mid` | `360x56` | `complete` |
| `secret_alliance_evidence_meter_fill_high` | derived UI element | `docs/assets/011_secret_alliance/processed_png/secret_alliance_evidence_meter_fill_high.png` | `gfx/interface/011_secret_alliance/secret_alliance_evidence_meter_fill_high.dds` | `GFX_secret_alliance_evidence_meter_fill_high` | `360x56` | `complete` |

## Decision category and decision icons

| Asset | Source PNG | Processed PNG | Final DDS | Sprite | Size | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `decision_category_secret_alliance` | `docs/assets/011_secret_alliance/source_png/decision_category_secret_alliance_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_category_secret_alliance.png` | `gfx/interface/decisions/011_secret_alliance/decision_category_secret_alliance.dds` | `GFX_decision_category_secret_alliance` | `32x32` | `complete` |
| `decision_secret_alliance_investigate` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_investigate_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_investigate.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_investigate.dds` | `GFX_decision_secret_alliance_investigate` | `32x32` | `complete` |
| `decision_secret_alliance_security` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_security_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_security.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_security.dds` | `GFX_decision_secret_alliance_security` | `32x32` | `complete` |
| `decision_secret_alliance_split` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_split_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_split.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_split.dds` | `GFX_decision_secret_alliance_split` | `32x32` | `complete` |
| `decision_secret_alliance_border_watch` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_border_watch_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_border_watch.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_border_watch.dds` | `GFX_decision_secret_alliance_border_watch` | `32x32` | `complete` |
| `decision_secret_alliance_confront` | `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_confront_source.png` | `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_confront.png` | `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_confront.dds` | `GFX_decision_secret_alliance_confront` | `32x32` | `complete` |

## Idea icons

| Asset | Source PNG | Processed PNG | Final DDS | Sprite | Size | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `idea_secret_alliance_friction` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_friction_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_friction.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_friction.dds` | `GFX_idea_secret_alliance_friction` | `64x64` | `complete` |
| `idea_secret_alliance_bureau` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_bureau_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_bureau.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_bureau.dds` | `GFX_idea_secret_alliance_bureau` | `64x64` | `complete` |
| `idea_secret_alliance_prepared_network` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_prepared_network_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_prepared_network.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_prepared_network.dds` | `GFX_idea_secret_alliance_prepared_network` | `64x64` | `complete` |
| `idea_secret_alliance_exposed_member` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_exposed_member_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_exposed_member.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_exposed_member.dds` | `GFX_idea_secret_alliance_exposed_member` | `64x64` | `complete` |
| `idea_secret_alliance_patron_shield` | `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_patron_shield_source.png` | `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_patron_shield.png` | `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_patron_shield.dds` | `GFX_idea_secret_alliance_patron_shield` | `64x64` | `complete` |

Script-facing idea aliases registered in `interface/011_secret_alliance.gfx` reuse these completed art families:
- `GFX_idea_secret_alliance_unexplained_friction`
- `GFX_idea_secret_alliance_counter_pact_bureau`
- `GFX_idea_secret_alliance_prepared_security_network`
- `GFX_idea_secret_alliance_compromised_ministries`
- `GFX_idea_secret_alliance_hidden_compact_discipline`
- `GFX_idea_secret_alliance_exposed_pact_government`
- `GFX_idea_secret_alliance_revealed_compact`
- `GFX_idea_secret_alliance_public_war_command`

## Achievement icons

All achievements are `64x64` and complete with base, grey, and not-eligible DDS variants under `gfx/achievements/`.

| Achievement id | Source PNG | Processed PNG | Final DDS triplet |
| --- | --- | --- | --- |
| `sa_every_thread_named` | `docs/assets/011_secret_alliance/source_png/achievement_sa_every_thread_named_source.png` | `docs/assets/011_secret_alliance/processed_png/achievement_sa_every_thread_named.png` | `gfx/achievements/sa_every_thread_named.dds`, `_grey.dds`, `_not_eligible.dds` |
| `sa_paper_collapse` | `docs/assets/011_secret_alliance/source_png/achievement_sa_paper_collapse_source.png` | `docs/assets/011_secret_alliance/processed_png/achievement_sa_paper_collapse.png` | `gfx/achievements/sa_paper_collapse.dds`, `_grey.dds`, `_not_eligible.dds` |
| `sa_turn_the_knife` | `docs/assets/011_secret_alliance/source_png/achievement_sa_turn_the_knife_source.png` | `docs/assets/011_secret_alliance/processed_png/achievement_sa_turn_the_knife.png` | `gfx/achievements/sa_turn_the_knife.dds`, `_grey.dds`, `_not_eligible.dds` |
| `sa_prepared_for_every_border` | `docs/assets/011_secret_alliance/source_png/achievement_sa_prepared_for_every_border_source.png` | `docs/assets/011_secret_alliance/processed_png/achievement_sa_prepared_for_every_border.png` | `gfx/achievements/sa_prepared_for_every_border.dds`, `_grey.dds`, `_not_eligible.dds` |
| `sa_small_country_large_shadow` | `docs/assets/011_secret_alliance/source_png/achievement_sa_small_country_large_shadow_source.png` | `docs/assets/011_secret_alliance/processed_png/achievement_sa_small_country_large_shadow.png` | `gfx/achievements/sa_small_country_large_shadow.dds`, `_grey.dds`, `_not_eligible.dds` |
| `sa_ten_signatures` | `docs/assets/011_secret_alliance/source_png/achievement_sa_ten_signatures_source.png` | `docs/assets/011_secret_alliance/processed_png/achievement_sa_ten_signatures.png` | `gfx/achievements/sa_ten_signatures.dds`, `_grey.dds`, `_not_eligible.dds` |
| `sa_bad_evidence_backfire` | `docs/assets/011_secret_alliance/source_png/achievement_sa_bad_evidence_backfire_source.png` | `docs/assets/011_secret_alliance/processed_png/achievement_sa_bad_evidence_backfire.png` | `gfx/achievements/sa_bad_evidence_backfire.dds`, `_grey.dds`, `_not_eligible.dds` |
| `sa_no_factory_lost` | `docs/assets/011_secret_alliance/source_png/achievement_sa_no_factory_lost_source.png` | `docs/assets/011_secret_alliance/processed_png/achievement_sa_no_factory_lost.png` | `gfx/achievements/sa_no_factory_lost.dds`, `_grey.dds`, `_not_eligible.dds` |

## Animated small sprites

| Asset | Source grid | Source frames | Processed frame size | Static fallback | Animated sheet | Frame count | Rate | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `secret_alliance_hidden_seal` | `docs/assets/011_secret_alliance/animations/secret_alliance_hidden_seal/source_frames/secret_alliance_hidden_seal_grid_source.png` | `docs/assets/011_secret_alliance/animations/secret_alliance_hidden_seal/source_frames/secret_alliance_hidden_seal_000_source.png` through `_007_source.png` | `36x36` | `gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_seal.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_seal_animated.dds` | `8` | `8 fps` | `complete` |
| `secret_alliance_evidence_meter_highlight` | `docs/assets/011_secret_alliance/animations/secret_alliance_evidence_meter_highlight/source_frames/secret_alliance_evidence_meter_highlight_grid_source.png` | `docs/assets/011_secret_alliance/animations/secret_alliance_evidence_meter_highlight/source_frames/secret_alliance_evidence_meter_highlight_000_source.png` through `_007_source.png` | `36x36` | `gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_meter_highlight.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_meter_highlight_animated.dds` | `8` | `8 fps` | `complete` |
| `secret_alliance_crisis_frame` | `docs/assets/011_secret_alliance/animations/secret_alliance_crisis_frame/source_frames/secret_alliance_crisis_frame_grid_source.png` | `docs/assets/011_secret_alliance/animations/secret_alliance_crisis_frame/source_frames/secret_alliance_crisis_frame_000_source.png` through `_007_source.png` | `36x36` | `gfx/interface/animated/011_secret_alliance/secret_alliance_crisis_frame.dds` | `gfx/interface/animated/011_secret_alliance/secret_alliance_crisis_frame_animated.dds` | `8` | `8 fps` | `complete` |

Review contacts:
- `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_icons_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_achievements_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_animation_statics_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/011_secret_alliance_event_art_contact_sheet.png`
- `docs/assets/011_secret_alliance/contact_sheets/011_secret_alliance_ui_contact_sheet.png`

Usage note:
- `secret_alliance_evidence_meter_highlight` is registered as a compact highlight marker for the decision category or a future scripted GUI meter. Its static fallback and animated sheet are both present and share the same stable sprite stem.

Wiring note:
- `interface/011_secret_alliance.gfx` registers every final Event 011 sprite, including operation-specific decision aliases that resolve to the five generated decision icon families requested in the asset prompt.
