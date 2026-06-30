# Event 011 Secret Alliance asset manifest

Event id: `011`  
Event slug: `secret_alliance`  
Scope: decision category icon, decision icons, idea icons, achievement icons, and three small animated sprite packages.

Source mode summary:
- Transparent icons: generated with built-in `image_gen`, flat `#00ff00` chroma-key background, local alpha cleanup through `remove_chroma_key.py`.
- Achievements: generated full-frame painted squares, then resized to `64x64`.
- Small animations: generated as real `4x2` eight-frame source sheets, sliced into source frames, normalized to `36x36`, sheeted to `288x36`.

Build helper:
- `docs/assets/011_secret_alliance/build_assets.py`

Prompt log:
- `docs/assets/011_secret_alliance/prompts/generated_prompts.md`

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

Uncertainty:
- `secret_alliance_evidence_meter_highlight` was kept as a centered small emblem/highlight marker because no exact meter overlay geometry was provided in the parent handoff. The sprite name is stable; the parent can either use it directly as a compact highlight or crop/anchor it inside the final GUI surface.
