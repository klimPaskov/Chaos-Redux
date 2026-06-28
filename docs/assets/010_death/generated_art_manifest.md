# Event 010 Death generated art manifest

Event id: `010`
Event slug: `death`
Source mode summary: generated non-icon art through official `image_gen`
Contact sheet: `docs/assets/010_death/contact_sheets/death_report_event_images_contact.png`
Legacy mixed contact sheet: `docs/assets/010_death/contact_sheets/death_processed_contact.png`
Additional contact sheet: `docs/assets/010_death/contact_sheets/death_black_oath_routes_contact.png`
Focus icon contact sheet: `docs/assets/010_death/contact_sheets/death_focus_icons_contact.png`
Super-event audit contact sheet: `docs/assets/010_death/contact_sheets/death_super_events_contact.png`
Final DDS super-event alignment check: `docs/assets/010_death/contact_sheets/death_super_events_final_alignment_check.png`

## Current icon override package

The active Death focus and achievement icons listed in `docs/assets/010_death/death_icon_scratch_regen_2026_06_21/manifest.md` are the only accepted completion package for the user-reported Death icon correction. Those icons were regenerated from fresh source artwork, not modified from existing Death icon files. Earlier repair or intermediate focus-only packages were removed from tracked asset docs because they are not valid completion evidence for the scratch-regeneration requirement.

## Super-event audit

- Audit date: `2026-06-15`
- Final DDS alignment check: `2026-06-28`
- Audited active Death super-event image roles: `super_event_death_reveal`, `super_event_death_world_end`, `super_event_death_defeat_aftermath`, `super_event_death_world_consumed`, `super_event_death_black_oath`
- Wiring basis: `interface/chaosx_super_events.gfx`, `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`, `common/script_constants/010_death_constants.txt`, and `common/scripted_effects/010_death_effects.txt`
- Audit result: all five active Death super-event images have source PNG, processed PNG, and final DDS outputs at `457x328`
- Final DDS result: all five final DDS files visually align with the accepted Death super-event set. `super_event_death_world_end.dds` and `super_event_death_world_consumed.dds` were reconverted from their accepted processed PNGs after the final DDS check found stale placeholder textures at the live gameplay paths
- Route note: `Dark Methods` is a Death route surface, but no separate Dark Methods super-event image slot is currently wired in the active Death constants or super-event scripted localisation
- Asset action: no source image regeneration was required. The final DDS outputs now match the selected processed art set

## Complete

### `DTH` flag set

- Asset type: fictional country flag set
- Intended in-game use: Death country default flag
- Source mode: generated
- Source note: a generated near-black concept was produced for the fictional/supernatural DTH tag, then the final wired flag set was normalized to all-black to match the accepted Death country identity.
- Source PNG: `docs/assets/010_death/source_png/DTH_flag_source.png`
- Processed PNG: source used directly for resize/export
- Final path: `gfx/flags/DTH.tga`, `gfx/flags/medium/DTH.tga`, `gfx/flags/small/DTH.tga`
- Target size: `82x52`, `41x26`, `10x7`
- Sprite name: not applicable
- `.gfx` file: not applicable
- Related gameplay use: country flag for `DTH`
- Asset status: `complete`
- Notes: TGA sizes verified with `file`. Final base and ideology flags use the same black variant at each size.

### `leader_zol`

- Asset type: fictional nonhuman leader portrait
- Intended in-game use: Death country leader portrait
- Source mode: generated
- Source note: Zol is fictional/nonhuman, so generated portrait was required
- Prompt note: matte-black hooded absence with white eye glow only, HOI4 bust framing, subdued painterly finish
- Source PNG: `docs/assets/010_death/source_png/leader_zol_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/leader_zol.png`
- Final path: `gfx/leaders/010_death/portrait_DTH_zol.dds`
- Target size: `156x210`
- Sprite name: `GFX_portrait_DTH_zol`
- `.gfx` file: `interface/chaosx_characters.gfx`
- Related gameplay use: Zol leader portrait for DTH
- Asset status: `complete`
- Notes: apparent presentation is nonhuman/ungendered. Gameplay should keep institutional name `Zol` rather than use a human random-name pool

### `report_event_death_missing_island`

- Asset type: report event image
- Intended in-game use: Death maritime errata shoreline report
- Source mode: generated
- Source note: fictional period-documentary scene. Generation was appropriate because the event needs a unique impossible shoreline rather than a real archive location
- Prompt note: black surf swallowing an empty island quay and village, coastline visibly wrong, no people, no text
- Source PNG: `docs/assets/010_death/source_png/report_event_death_missing_island_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/report_event_death_missing_island.png`
- Final path: `gfx/event_pictures/report_event_death_missing_island.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_death_missing_island`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: impossible shoreline / vanished island report card
- Asset status: `complete`
- Notes: regenerated for stronger storm contrast and a visibly wrong coastline. Report-card treatment applied locally

### `report_event_death_mail_boat`

- Asset type: report event image
- Intended in-game use: early Death report event picture
- Source mode: generated
- Source note: fictional period-documentary scene. No archival source exists for this alternate-history island report
- Prompt note: abandoned mail launch drifting back into a blackened harbor, lit cabin, visible sacks, no crew, no text
- Source PNG: `docs/assets/010_death/source_png/report_event_death_mail_boat_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/report_event_death_mail_boat.png`
- Final path: `gfx/event_pictures/report_event_death_mail_boat.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_death_mail_boat`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: empty pier/mail boat report card
- Asset status: `complete`
- Notes: regenerated for stronger harbor mood and clearer crew absence. Report-card treatment applied locally

### `report_event_death_lighthouse`

- Asset type: report event image
- Intended in-game use: Death lighthouse report
- Source mode: generated
- Source note: fictional period-documentary lighthouse scene. Generation was appropriate because the event needs an impossible shoreline swallow rather than a specific archive photograph
- Prompt note: lighthouse beam cutting across a dead sea and swallowed shoreline under storm cloud, no readable text
- Source PNG: `docs/assets/010_death/source_png/report_event_death_lighthouse_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/report_event_death_lighthouse.png`
- Final path: `gfx/event_pictures/report_event_death_lighthouse.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_death_lighthouse`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: lighthouse/empty settlement report card
- Asset status: `complete`
- Notes: regenerated for stronger beam contrast and dead shoreline silhouette. Report-card treatment applied locally

### `report_event_death_census`

- Asset type: report event image
- Intended in-game use: Death census-office report
- Source mode: generated
- Source note: fictional period-documentary records-office scene. No real archival photo exists for the alternate-history missing-records incident
- Prompt note: officials confronting shattered records shelves and blank files, no readable text, no gore
- Source PNG: `docs/assets/010_death/source_png/report_event_death_census_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/report_event_death_census.png`
- Final path: `gfx/event_pictures/report_event_death_census.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_death_census`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: abandoned census office report card
- Asset status: `complete`
- Notes: regenerated for stronger human reaction and wrecked-records staging. Source kept free of readable text before local treatment

### `news_event_death_mainland_reveal`

- Asset type: news event image
- Intended in-game use: public mainland reveal news image
- Source mode: generated
- Source PNG: `docs/assets/010_death/source_png/news_event_death_mainland_reveal_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/news_event_death_mainland_reveal.png`
- Final path: `gfx/event_pictures/news_event_death_mainland_reveal.dds`
- Target size: `397x153`
- Sprite name: `GFX_news_event_death_mainland_reveal`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: black-and-white mainland reveal news image
- Asset status: `complete`
- Notes: final processed image is grayscale press-photo treatment

### `news_event_death_defeated`

- Asset type: news event image
- Intended in-game use: defeat aftermath news image
- Source mode: generated
- Source PNG: `docs/assets/010_death/source_png/news_event_death_defeated_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/news_event_death_defeated.png`
- Final path: `gfx/event_pictures/news_event_death_defeated.dds`
- Target size: `397x153`
- Sprite name: `GFX_news_event_death_defeated`
- `.gfx` file: `interface/chaosx_pictures.gfx`
- Related gameplay use: soldiers/surveyors entering dead land
- Asset status: `complete`
- Notes: final processed image is grayscale press-photo treatment

### `super_event_death_reveal`

- Asset type: super-event image
- Intended in-game use: Death mainland reveal super-event
- Source mode: generated
- Source PNG: `docs/assets/010_death/source_png/super_event_death_reveal_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/super_event_death_reveal.png`
- Final path: `gfx/super_events/super_event_death_reveal.dds`
- Target size: `457x328`
- Sprite name: `GFX_super_event_death_reveal`
- `.gfx` file: `interface/chaosx_super_events.gfx`
- Related gameplay use: super-event role 1 mainland reveal
- Asset status: `complete`
- Notes: central composition kept readable for HOI4 super-event framing. Final DDS is converted from the processed Death reveal PNG at the registered gameplay path

### `super_event_death_world_end`

- Asset type: super-event image
- Intended in-game use: Death world-end super-event
- Source mode: generated
- Source PNG: `docs/assets/010_death/source_png/super_event_death_world_end_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/super_event_death_world_end.png`
- Final path: `gfx/super_events/super_event_death_world_end.dds`
- Target size: `457x328`
- Sprite name: `GFX_super_event_death_world_end`
- `.gfx` file: `interface/chaosx_super_events.gfx`
- Related gameplay use: super-event role 2 world-end
- Asset status: `complete`
- Notes: quiet shoreline/tide image rather than creature or abstract effects

### `super_event_death_defeat_aftermath`

- Asset type: super-event image
- Intended in-game use: Death defeat aftermath super-event
- Source mode: generated
- Source PNG: `docs/assets/010_death/source_png/super_event_death_defeat_aftermath_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/super_event_death_defeat_aftermath.png`
- Final path: `gfx/super_events/super_event_death_defeat_aftermath.dds`
- Target size: `457x328`
- Sprite name: `GFX_super_event_death_defeat`
- `.gfx` file: `interface/chaosx_super_events.gfx`
- Related gameplay use: super-event role 3 defeat aftermath
- Asset status: `complete`
- Notes: figures stay secondary to unrecoverable dead terrain

### `super_event_death_world_consumed`

- Asset type: super-event image
- Intended in-game use: Death whole-world-consumed super-event
- Source mode: generated
- Source note: regenerated on 2026-06-28 because the prior office/map-room scene was too quiet for the whole-world-consumed role
- Prompt note: ruined 1936-1945 coastal capital seen from above, vast supernatural black tide swallowing the last city and harbor, tiny foreground witnesses for scale, no office, no map table, no readable text
- Source PNG: `docs/assets/010_death/source_png/super_event_death_world_consumed_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/super_event_death_world_consumed.png`
- Final path: `gfx/super_events/super_event_death_world_consumed.dds`
- Target size: `457x328`
- Sprite name: `GFX_super_event_death_world_consumed`
- `.gfx` file: `interface/chaosx_super_events.gfx`
- Related gameplay use: super-event role 4 whole world consumed
- Asset status: `complete`
- Notes: dramatic exterior end-state composition. The black tide and ruined coast are the subject, while foreground figures only provide scale

### `herald_of_zol` flag set

- Asset type: fictional cosmetic country flag set
- Intended in-game use: Herald of Zol cosmetic identity
- Source mode: generated
- Source note: generated because Herald of Zol is a fictional alternate-history oath state and needed a distinct silhouette from the Death ring flag
- Prompt note: charcoal-black cloth banner with a bone-white spear-and-oath emblem, restrained period cloth treatment, readable at flag sizes
- Source PNG: `docs/assets/010_death/source_png/death_herald_of_zol_flag_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/death_herald_of_zol_flag.png`
- Final path: `gfx/flags/death_herald_of_zol.tga`, `gfx/flags/medium/death_herald_of_zol.tga`, `gfx/flags/small/death_herald_of_zol.tga`
- Target size: `82x52`, `41x26`, `10x7`
- Sprite name: not applicable
- `.gfx` file: not applicable
- Related gameplay use: cosmetic Herald of Zol route flag
- Asset status: `complete`
- Notes: stable filename suggestion is `death_herald_of_zol`. Emblem stays legible at small size and avoids the DTH broken-ring motif. TGA orientation was corrected on 2026-06-28 across normal, medium, and small outputs, with the expected non-top-origin flag header preserved.

### `black_apostolate` flag set

- Asset type: fictional cosmetic country flag set
- Intended in-game use: Black Apostolate cosmetic identity
- Source mode: generated
- Source note: generated because the Black Apostolate is a hidden fictional route and needed a harsher institutional identity separate from both DTH and Herald visuals
- Prompt note: pitch-black cloth banner with a bone-white apostolic obelisk and winged office-seal motif, readable at flag sizes
- Source PNG: `docs/assets/010_death/source_png/death_black_apostolate_flag_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/death_black_apostolate_flag.png`
- Final path: `gfx/flags/death_black_apostolate.tga`, `gfx/flags/medium/death_black_apostolate.tga`, `gfx/flags/small/death_black_apostolate.tga`
- Target size: `82x52`, `41x26`, `10x7`
- Sprite name: not applicable
- `.gfx` file: not applicable
- Related gameplay use: cosmetic Black Apostolate hidden-route flag
- Asset status: `complete`
- Notes: stable filename suggestion is `death_black_apostolate`. Composition favors a stark central state-seal shape rather than another void emblem. TGA orientation was corrected on 2026-06-28 across normal, medium, and small outputs, with the expected non-top-origin flag header preserved.

### `super_event_death_black_oath`

- Asset type: super-event image
- Intended in-game use: Herald oath reveal super-event
- Source mode: generated
- Source note: generated because the scene is a fictional alternate-history government oath tableau rather than a real archival event
- Prompt note: 1936-1945 government chamber, officials around sealed oath table, looming void witness behind them, no readable text
- Source PNG: `docs/assets/010_death/source_png/super_event_death_black_oath_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/super_event_death_black_oath.png`
- Final path: `gfx/super_events/super_event_death_black_oath.dds`
- Target size: `457x328`
- Sprite name: `GFX_super_event_death_black_oath`
- `.gfx` file: `interface/chaosx_super_events.gfx`
- Related gameplay use: optional Herald oath reveal super-event
- Asset status: `complete`
- Notes: scene keeps the supernatural force present but restrained. Composition remains readable in the HOI4 super-event crop

### Main-agent wired UI icon set

- Asset type: decisions, focus icons, idea icons, and achievements
- Source mode: generated PNGs from this manifest package, converted to uncompressed DDS with ImageMagick
- `.gfx` files:
  - `interface/010_death.gfx`
  - `interface/chaosx_ideas.gfx`
  - `interface/chaosx_achievements.gfx`
- Decision sprites:
  - `GFX_decision_category_death_country` -> `gfx/interface/decisions/death/decision_category_death_country.dds`
  - `GFX_decision_death_survey_boat` -> `gfx/interface/decisions/death/decision_death_survey_boat.dds`
  - `GFX_decision_death_living_compact` -> `gfx/interface/decisions/death/decision_death_living_compact.dds`
  - `GFX_decision_death_quarantine_line` -> `gfx/interface/decisions/death/decision_death_quarantine_line.dds`
  - `GFX_decision_death_coastal_watch` -> `gfx/interface/decisions/death/decision_death_coastal_watch.dds`
  - `GFX_decision_death_wasteland_gear` -> `gfx/interface/decisions/death/decision_death_wasteland_gear.dds`
  - `GFX_decision_death_dead_zone_outpost` -> `gfx/interface/decisions/death/decision_death_dead_zone_outpost.dds`
  - `GFX_decision_death_black_book` -> `gfx/interface/decisions/death/decision_death_black_book.dds`
  - `GFX_decision_death_black_oath` -> `gfx/interface/decisions/death/decision_death_black_oath.dds`
- Focus sprites:
  - `GFX_focus_death_the_first_silence`
  - `GFX_focus_death_country_on_the_island`
  - `GFX_focus_death_shroud_whispers`
  - `GFX_focus_death_no_mail_before_spring`
  - `GFX_focus_death_weather_on_paper`
  - `GFX_focus_death_island_pattern`
  - `GFX_focus_death_hunger_shore`
  - `GFX_focus_death_lowest_names_first`
  - `GFX_focus_death_ports_without_voices`
  - `GFX_focus_death_mainland_smell`
  - `GFX_focus_death_black_census`
  - `GFX_focus_death_no_graves_needed`
  - `GFX_focus_death_first_ghost_muster`
  - `GFX_focus_death_public_death`
  - `GFX_focus_death_tide_learns_roads`
  - `GFX_focus_death_another_shoreline`
  - `GFX_focus_death_no_ferry_returns`
  - `GFX_focus_death_wasteland_roads`
  - `GFX_focus_death_every_road_slows`
  - `GFX_focus_death_empty_supply`
  - `GFX_focus_death_state_without_state`
  - `GFX_focus_death_mourning_host`
  - `GFX_focus_death_ruin_host`
  - `GFX_focus_death_orders_without_breath`
  - `GFX_focus_death_last_shores`
  - `GFX_focus_death_world_consumed`
- Idea sprites:
  - `GFX_idea_country_without_breath`
  - `GFX_idea_death_first_silence`
  - `GFX_idea_death_public_death`
  - `GFX_idea_death_last_shores`
  - `GFX_idea_death_black_census`
  - `GFX_idea_death_black_book_offices` -> `gfx/interface/ideas/death/idea_black_book_offices.dds`
  - `GFX_idea_death_black_oath` -> `gfx/interface/ideas/death/idea_black_oath.dds`
- Achievement sprite bases:
  - `death_no_one_heard_the_first_boat`
  - `death_not_on_my_continent`
  - `death_the_names_do_not_come_back`
  - `death_last_ferry`
  - `death_counted_every_name`
  - `death_black_tide_reversed`
  - `death_no_witnesses`
  - `death_before_the_name`
  - `death_the_living_conference`
  - `death_six_continents_one_color`
  - `death_friend_of_zol`
  - `death_book_burner`
  - `death_black_apostolate`
- Asset status: `complete`
- Notes: route achievements are active because Dark Methods, Black Oath, Herald of Zol, and Black Apostolate are implemented. All active Death focus sprites now have source PNGs, processed PNGs, and stable DDS files. Accidental duplicated placeholder hashes were eliminated during the final asset pass. The final Death focus set is a coherent HOI4 badge pass: every focus icon was rebuilt to `94x86` with transparent outer canvas, visible dark-metal or bronze badge framing, and a painted interior motif matched to the focus subject rather than leaving any full-bleed square thumbnail in the final output.

### `death_focus_icon_regeneration_pass`

- Asset type: national focus icon family
- Intended in-game use: all 26 Death country national focuses
- Source mode: regenerated in themed batches, then locally rebuilt into a coherent HOI4 medallion/badge presentation
- Source PNG paths: `docs/assets/010_death/source_png/focus_death_*_source.png`
- Frame source helpers: `docs/assets/010_death/source_png/overlay_focus_frame_ledger_source.png`, `docs/assets/010_death/source_png/overlay_focus_frame_round_source.png`, `docs/assets/010_death/source_png/overlay_focus_frame_shield_source.png`
- Processed PNG paths: `docs/assets/010_death/processed_png/focus_death_*.png`
- Final DDS paths: `gfx/interface/goals/death/focus_death_*.dds`
- Target size: `94x86`
- Sprite names: `GFX_focus_death_*` existing registered names preserved
- `.gfx` file: `interface/010_death.gfx` existing registration preserved
- Related gameplay use: Death national focus tree
- Asset status: `complete`
- Prompt/process note: this pass intentionally discarded the old square-thumbnail presentation. All 26 focuses now use transparent outer alpha, visible badge framing, and a central painted motif sized for HOI4 focus readability.
- Contact sheet: `docs/assets/010_death/contact_sheets/death_focus_icons_contact.png`
- Requested regeneration, 2026-06-28: `focus_death_state_without_state`, `focus_death_world_consumed`, `focus_death_empty_supply`, `focus_death_every_road_slows`, `focus_death_last_shores`, `focus_death_mourning_host`, `focus_death_orders_without_breath`, and `focus_death_ruin_host` were regenerated from new source art. Package manifest: `docs/assets/010_death/focus_icon_regen_2026_06_28/manifest.md`. Contact sheet: `docs/assets/010_death/contact_sheets/death_focus_icons_requested_regen_2026_06_28.png`.

### `idea_public_death`

- Asset type: idea icon
- Intended in-game use: public recognition of Death as a world threat
- Source mode: generated through official `image_gen`, then locally processed for transparent alpha and HOI4 idea-size readability
- Source PNG: `docs/assets/010_death/source_png/idea_public_death_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/idea_public_death.png`
- Auxiliary alpha/source helper: `docs/assets/010_death/processed_png/idea_public_death_alpha.png`
- Final path: `gfx/interface/ideas/death/idea_public_death.dds`
- Target size: `64x64`
- Sprite name: `GFX_idea_death_public_death`
- `.gfx` file: `interface/chaosx_ideas.gfx`
- Related gameplay use: Death public-reveal national spirit
- Asset status: `complete`
- Notes: fully regenerated from scratch as a stark public notice sheet with a void-black official seal and dead-coast vignette, with transparent outer alpha. The final icon stands on its own and keeps no focus-icon dependency.

### Route achievement and idea icon finals

- `death_friend_of_zol`
  - Source PNG: `docs/assets/010_death/source_png/achievement_death_friend_of_zol_source.png`
  - Processed PNG: `docs/assets/010_death/processed_png/achievement_death_friend_of_zol.png`
  - Final paths: `gfx/achievements/death_friend_of_zol.dds`, `gfx/achievements/death_friend_of_zol_grey.dds`, `gfx/achievements/death_friend_of_zol_not_eligible.dds`
  - Target size: `64x64`
  - Asset status: `complete`
- `death_book_burner`
  - Source PNG: `docs/assets/010_death/source_png/achievement_death_book_burner_source.png`
  - Processed PNG: `docs/assets/010_death/processed_png/achievement_death_book_burner.png`
  - Final paths: `gfx/achievements/death_book_burner.dds`, `gfx/achievements/death_book_burner_grey.dds`, `gfx/achievements/death_book_burner_not_eligible.dds`
  - Target size: `64x64`
  - Asset status: `complete`
- `death_black_apostolate`
  - Source PNG: `docs/assets/010_death/source_png/death_black_apostolate_flag_source.png`
  - Processed PNG: `docs/assets/010_death/processed_png/achievement_death_black_apostolate.png`
  - Final paths: `gfx/achievements/death_black_apostolate.dds`, `gfx/achievements/death_black_apostolate_grey.dds`, `gfx/achievements/death_black_apostolate_not_eligible.dds`
  - Target size: `64x64`
  - Asset status: `complete`
- `death_black_book_offices`
  - Source PNG: `docs/assets/010_death/source_png/decision_death_black_book_source.png`
  - Processed PNG: `docs/assets/010_death/processed_png/idea_black_book_offices.png`
  - Final path: `gfx/interface/ideas/death/idea_black_book_offices.dds`
  - Target size: `64x64`
  - Asset status: `complete`
- `death_black_oath`
  - Source PNG: `docs/assets/010_death/source_png/decision_death_black_oath_source.png`
  - Processed PNG: `docs/assets/010_death/processed_png/idea_black_oath.png`
  - Final path: `gfx/interface/ideas/death/idea_black_oath.dds`
  - Target size: `64x64`
  - Asset status: `complete`

## Complete: Optional Animated Portrait

### `leader_zol_world_end_animated`

- Asset type: animated leader portrait package
- Intended in-game use: world-end Zol portrait replacement and registered animated portrait surface
- Source mode: edited frame-by-frame from approved static portrait
- Source note: user correction required a much subtler animation that preserves the existing static portrait almost exactly, so the frame set was rebuilt from the approved static fallback with only a restrained eye-glow pulse
- Source frames: `docs/assets/010_death/source_png/portrait_DTH_zol_world_end_frame_00_source.png` through `docs/assets/010_death/source_png/portrait_DTH_zol_world_end_frame_07_source.png`
- Processed frames: `docs/assets/010_death/processed_png/portrait_DTH_zol_world_end_frame_00.png` through `docs/assets/010_death/processed_png/portrait_DTH_zol_world_end_frame_07.png`
- Static processed PNG: `docs/assets/010_death/processed_png/portrait_DTH_zol_world_end.png`
- Sheet PNG: `docs/assets/010_death/animations/portrait_DTH_zol_world_end/sheets/portrait_DTH_zol_world_end_sheet.png`
- Contact sheet: `docs/assets/010_death/contact_sheets/portrait_DTH_zol_world_end_contact.png`
- Preview GIF: `docs/assets/010_death/previews/portrait_DTH_zol_world_end_preview.gif`
- Final path: `gfx/leaders/010_death/portrait_DTH_zol_world_end_animated.dds`
- Static fallback: `gfx/leaders/010_death/portrait_DTH_zol_world_end.dds`
- Target size: `156x210`
- Sheet size: `1248x210`
- Frame count: `8`
- Animation rate: `4 fps`
- Sprite name: `GFX_portrait_DTH_zol_world_end` and `GFX_portrait_DTH_zol_world_end_animated`
- `.gfx` file: `interface/chaosx_characters.gfx`
- Related gameplay use: static world-end leader portrait fallback plus registered animated portrait return for Death world-end surfaces
- Asset status: `complete`
- Notes: apparent presentation remains nonhuman/ungendered. Gameplay should keep institutional name `Zol`. Motion is eyes-glow-only. The static fallback DDS remains unchanged. Validation: processed frames are all `156x210`. Final sheet and DDS are `1248x210`. Preview GIF loops at 8 frames. Identity drift check outside the eye mask is zero or effectively zero. No `.gfx` change is needed because frame count and rate remain unchanged.

## Complete: Death Black Atlas UI Package

### `death_black_atlas_background`

- Asset type: scripted-GUI background panel
- Intended in-game use: Black Atlas main background
- Source mode: generated
- Source note: generated because this is fictional UI art for an alternate-history atlas, not a historical scanned map
- Source PNG: `docs/assets/010_death/source_png/death_black_atlas_background_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/death_black_atlas_background.png`
- Final path: `gfx/interface/death/black_atlas/death_black_atlas_background.dds`
- Target size: `520x236`
- Sprite name: `GFX_death_black_atlas_background`
- `.gfx` file: `interface/010_death.gfx`
- Related gameplay use: Black Atlas panel background
- Asset status: `complete`
- Notes: black administrative sea-map atlas with pale registry lines and no readable text

### `death_black_atlas_header`

- Asset type: scripted-GUI header strip
- Intended in-game use: Black Atlas static header fallback
- Source mode: generated
- Source PNG: `docs/assets/010_death/source_png/death_black_atlas_header_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/death_black_atlas_header.png`
- Final path: `gfx/interface/death/black_atlas/death_black_atlas_header.dds`
- Target size: `500x36`
- Sprite name: `GFX_death_black_atlas_header`
- `.gfx` file: `interface/010_death.gfx`
- Related gameplay use: Black Atlas header fallback
- Asset status: `complete`
- Notes: central atlas notch stays readable at small height

### `death_black_atlas_header_animated`

- Asset type: scripted-GUI animated header sheet
- Intended in-game use: Black Atlas animated header
- Source mode: generated
- Source PNG: `docs/assets/010_death/source_png/death_black_atlas_header_animated_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/death_black_atlas_header_static.png`
- Final path: `gfx/interface/death/black_atlas/death_black_atlas_header_animated.dds`
- Target size: `500x36` frames, `4000x36` sheet
- Sprite name: `GFX_death_black_atlas_header_animated`
- `.gfx` file: `interface/010_death.gfx`
- Related gameplay use: Black Atlas animated header
- Asset status: `complete`
- Notes: `8` frames, `8 fps`, looping, source frames at `docs/assets/010_death/animations/death_black_atlas_header/source_frames/`, sheet PNG at `docs/assets/010_death/animations/death_black_atlas_header/sheets/death_black_atlas_header_sheet.png`

### `death_coastal_risk_pulse`

- Asset type: scripted-GUI animated warning mark
- Intended in-game use: coastal-risk pulse
- Source mode: generated
- Source PNG: `docs/assets/010_death/source_png/death_coastal_risk_pulse_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/death_coastal_risk_pulse_static.png`
- Final path: `gfx/interface/death/black_atlas/death_coastal_risk_pulse.dds`
- Static fallback: `gfx/interface/death/black_atlas/death_coastal_risk_pulse_static.dds`
- Target size: `36x36` frames, `288x36` sheet
- Sprite name: `GFX_death_coastal_risk_pulse` for the animated sheet. `GFX_death_coastal_risk_pulse_static` for the static fallback
- `.gfx` file: `interface/010_death.gfx`
- Related gameplay use: small coastal-risk indicator
- Asset status: `complete`
- Notes: `8` frames, `8 fps`, looping, with source/processed frame package under `docs/assets/010_death/animations/death_coastal_risk_pulse/`

### `death_wither_target_frame`

- Asset type: scripted-GUI animated target frame
- Intended in-game use: wither-target overlay
- Source mode: generated
- Source PNG: `docs/assets/010_death/source_png/death_wither_target_frame_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/death_wither_target_frame_static.png`
- Final path: `gfx/interface/death/black_atlas/death_wither_target_frame.dds`
- Static fallback: `gfx/interface/death/black_atlas/death_wither_target_frame_static.dds`
- Target size: `36x36` frames, `288x36` sheet
- Sprite name: `GFX_death_wither_target_frame` for the animated sheet. `GFX_death_wither_target_frame_static` for the static fallback
- `.gfx` file: `interface/010_death.gfx`
- Related gameplay use: target-frame overlay
- Asset status: `complete`
- Notes: `8` frames, `8 fps`, looping, with source/processed frame package under `docs/assets/010_death/animations/death_wither_target_frame/`

### `death_compact_warning_pulse`

- Asset type: scripted-GUI animated compact warning mark
- Intended in-game use: compact warning pulse
- Source mode: generated
- Source PNG: `docs/assets/010_death/source_png/death_compact_warning_pulse_source.png`
- Processed PNG: `docs/assets/010_death/processed_png/death_compact_warning_pulse_static.png`
- Final path: `gfx/interface/death/black_atlas/death_compact_warning_pulse.dds`
- Static fallback: `gfx/interface/death/black_atlas/death_compact_warning_pulse_static.dds`
- Target size: `36x36` frames, `288x36` sheet
- Sprite name: `GFX_death_compact_warning_pulse` for the animated sheet. `GFX_death_compact_warning_pulse_static` for the static fallback
- `.gfx` file: `interface/010_death.gfx`
- Related gameplay use: compact warning indicator
- Asset status: `complete`
- Notes: `8` frames, `8 fps`, looping, with source/processed frame package under `docs/assets/010_death/animations/death_compact_warning_pulse/`

## Workflow note

- The repository DDS helper `.tools/convert_to_dds.py` was attempted and failed here on its FFmpeg fallback path with a `struct.pack` header error. Final DDS files were exported with ImageMagick `convert -define dds:compression=none`. Dimensions and file presence were verified after export.
