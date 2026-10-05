# Event 025 visual asset audit

Audit date: 2026-10-03.

Status: individual pixel review and several source binding repairs are recorded; Expedition Board MCP inspect and render evidence is recorded below; complete reverse-consumer coverage remains unresolved.

## Scope and evidence roots

This audit covers every Event 025 visual asset introduced or consumed by the active rework, including event reports, news art, the opening super-event, the Expedition Board, decision-category art, ideas, achievement triplets, animation frames, and the linked super-event audio handoff.

The source roots are docs/assets/025_alien_technology_in_antarctica/source_png/, source_art/, and source_audio/.

The processed roots are docs/assets/025_alien_technology_in_antarctica/processed_png/ and animations/.

The package final root is docs/assets/025_alien_technology_in_antarctica/dds/, and the engine-facing final root is gfx/.

The decoded final evidence is under docs/assets/025_alien_technology_in_antarctica/audit/decoded_dds/gfx/.

Contact sheets are under docs/assets/025_alien_technology_in_antarctica/contact_sheets/, and the individual visual review was performed against the source PNGs, processed PNGs, and decoded final DDS PNGs rather than relying on contact sheets alone.

The review opened every source, processed, and decoded final image in the Event 025 package, including all 15 report/news files, all 71 board DDS files, all 42 achievement DDS files, the super-event, the two decision-category files, the five idea files, the eight phase-banner frames, and the four static evolution overlays.

## Inventory totals

| Runtime family | Count | Expected consumer dimensions or frames | Current result |
| --- | ---: | --- | --- |
| Event pictures | 15 | One 397x153 news image and fourteen 210x176 report cards | Present and individually inspected. The crossing card is used by the departure, route-setback and route-cut (`chaosx.nr25.13`) reports and the rescue card by both rescue reports. The field hazard and rare incident events reuse existing report cards without new art: crossing for pack ice (`chaosx.nr25.301`), the clear weather window (314) and the neutral ship (315); outpost for whiteout (302), crevasses (303), radio loss (304) and the abandoned camp (311); mobilisation for engine failure (305), lost sledges (306) and the wrecked aircraft (316); rescue for sickness (307) and the call for help (312); analysis for the meteorite (313), the scientists' dispute (317) and the fragment test (318). None reuses an evolution card, so no incident hints at an evolution. The sabotage binding is repaired below. |
| Expedition Board | 71 | 1024x640 background, scaled panel families, state strips, icons, meters, overlays, and eight sector-state variants | Present and individually inspected; eight standalone sector-state DDS files have no verified live consumer, and layout evidence remains incomplete. |
| Achievements | 42 | Fourteen independent 64x64 normal/grey/not-eligible triplets | Present, individually inspected, and wired. |
| Super-event | 1 | 457x328 | Present, individually inspected, and wired through the dedicated super-event alias. |
| Decision-category art | 2 | 52x40 icon and 114x101 picture | Present, individually inspected, and wired. |
| Event ideas | 5 | Five 64x64 idea pictures | Present, individually inspected, and wired. |
| Total Event 025 DDS inventory | 136 | 15 + 71 + 42 + 1 + 2 + 5 | All engine-facing files exist. |

`interface/025_alien_technology_in_antarctica.gfx` contains 131 texturefile declarations after registering the missing sabotage report alias.
Repeated texture paths and sprite aliases are not unique-asset or live-consumer counts.

The five idea files and two decision-category files are inside that dedicated GFX file's texture declarations, not outside it.
The 136-file inventory establishes file presence, not that every DDS has a live consumer.

### Final-recovery failure report binding

`chaosx.nr25.86` requests `GFX_report_event_025_antarctic_sabotage`, which had no definition anywhere under `interface/`.
The alias now points to the existing 210x176 `gfx/event_pictures/025_alien_technology_in_antarctica/report_event_025_sabotage.dds`.
Its processed PNG and decoded DDS evidence were opened individually: damaged expedition equipment and severed field wiring fit the equipment-setback report without establishing an enemy's identity.
DDS SHA-256: `f81491db9cbea41ec481b31bc2be9976b1e7b33188e394d9595c839a10b21914`.
No pixel generation, resize, replacement, or fallback was used for this repair.
`.tools/test_event025_report_assets.py` checks report alias coverage, texture-file existence, this exact binding, and native DDS dimensions.
Source binding proof does not establish in-game appearance or mandatory MCP render acceptance.

## Consumer-to-file mapping

| Consumer and definition | Sprite or GFX alias | Source PNG | Processed PNG | Final DDS | Review and wiring result |
| --- | --- | --- | --- | --- | --- |
| Opening super-event definition in interface/chaosx_super_events.gfx | GFX_super_event_025_discovery | source_png/super_event_025_discovery_source.png | processed_png/super_event_025_discovery.png | gfx/super_events/025_alien_technology_in_antarctica/super_event_025_discovery.dds | 457x328 opaque scene, individually opened and dedicated to the opening super-event. |
| Discovery news event chaosx.news.25 in events/_chaosx_news.txt | GFX_news_event_025_discovery | source_png/news_event_025_winner_source.png | processed_png/news_event_025_winner.png | gfx/event_pictures/025_alien_technology_in_antarctica/news_event_025_winner.dds | Repaired to use the 397x153 news consumer instead of the 457x328 super-event canvas. |
| Winner news event chaosx.news.26 in events/_chaosx_news.txt | GFX_news_event_025_winner | source_png/news_event_025_winner_source.png | processed_png/news_event_025_winner.png | gfx/event_pictures/025_alien_technology_in_antarctica/news_event_025_winner.dds | Correct 397x153 aspect and shared news asset intentionally reused. |
| Event reports in events/025_alien_technology_in_antarctica.txt | GFX_report_event_025_antarctic_* | source_png/report_event_025_*_source.png | processed_png/report_event_025_*.png | gfx/event_pictures/025_alien_technology_in_antarctica/report_event_025_*.dds | Fourteen 210x176 report consumers are present and individually inspected. |
| Board root nr25_expedition_board_window in interface/025_alien_technology_in_antarctica.gui | GFX_025_expedition_board_background | source_png/board_background_025_source.png | processed_png/board_background_025.png | gfx/interface/025_alien_technology_in_antarctica/board_background_025.dds | 1024x640 opaque canvas, full-canvas consumer. |
| Board central operations and Antarctic map | GFX_025_expedition_operations_panel, GFX_025_expedition_sector_map | source_png/expedition_board/operations_panel_source.png and board_sector_map_025_source.png | processed_png/expedition_board/expedition_operations_panel.png and board_sector_map_025.png | Matching final DDS under gfx/interface/025_alien_technology_in_antarctica/ | Source art remains 700x430 and is displayed at scale 0.63 inside the 441x271 central display region. |
| Board status column | GFX_025_expedition_status_panel_compact, GFX_025_expedition_status_panel_tall | source_png/expedition_board/status_panel_source.png | processed_png/expedition_board/expedition_status_panel.png | gfx/interface/025_alien_technology_in_antarctica/expedition_status_panel.dds | The 272x180 texture is drawn as two 272x104 cornered tiles and one 272x196 tile at y 92, 196 and 300, so the cards no longer overlap; the tall card also holds the route, outpost and target rows. Only Progress, Logistics Readiness, and Exposure Risk (or Dependence) are main values. |
| Rival rail and cards | GFX_025_expedition_rivals_panel, GFX_025_expedition_rival_card, GFX_025_expedition_rival_selected | source_png/expedition_board/rivals_panel_source.png, rival_card_source.png, and rival_selected_source.png | Matching processed files under processed_png/expedition_board/ | Matching final DDS under gfx/interface/025_alien_technology_in_antarctica/ | Rival rail is displayed at scale 0.92; cards use public or intelligence-derived text only. |
| Phase action tray and five primary action cards | GFX_025_expedition_action_tray, GFX_025_expedition_action_card, GFX_025_expedition_action_state | source_png/expedition_board/action_tray_source.png, action_card_source.png, and action_state_source.png | Matching processed files under processed_png/expedition_board/ | Matching final DDS under gfx/interface/025_alien_technology_in_antarctica/ | Tray is displayed at scale 1.394; five cards are displayed at scale 0.78 and retain separate click regions. |
| Sector click regions | GFX_025_expedition_sector_hitbox | source_png/expedition_board/sector_hitbox_source.png and four state source variants | processed_png/expedition_board/sector_hitbox.png at 384x58 | gfx/interface/025_alien_technology_in_antarctica/sector_hitbox.dds at 384x58, four 96x58 frames | Repaired from the erroneous 2800x430 full-panel atlas; package and runtime SHA-256 are both 2252a63e5ee95a48a8582e046bcdf5f8982c7174b9e04130f71e61c8b1bda616. |
| Sector state and selection | GFX_025_expedition_sector_state, GFX_025_expedition_sector_selected_1 to _6 | source_png/expedition_board/sector_state_source.png; the highlights derive from board_sector_map_025.dds by the recipe in manifest_expedition_board.md | processed_png/expedition_board/sector_state_strip.png and sector_selected_1.png to sector_selected_6.png | Matching final DDS under gfx/interface/025_alien_technology_in_antarctica/ | Eight state frames are scaled to 0.5 over the six nodes and selected per sector from ROOT.chaosx_nr25_sector_N_frame; each sector's own highlight is drawn only while that sector is selected. |
| Phase banner | GFX_025_expedition_phase_banner_animated, GFX_025_expedition_phase_banner_static | source_png/phase_banner/phase_000_source.png through phase_007_source.png | processed_png/phase_banner/expedition_phase_banner.png and expedition_phase_banner_static.png | expedition_phase_banner.dds and expedition_phase_banner_static.dds | Real eight-frame frameAnimatedSpriteType sheet is accepted; static frame-000 fallback is wired for disabled animation. |
| Evolution overlays | GFX_025_expedition_<signal, survivor, fragment, dependence, militarised>_animated and their static fallbacks GFX_025_expedition_<same> | animations/overlay_*/source_frames/ (signal) and animations/overlay_*/source_layers/ (base plus eight motion layers) | animations/overlay_*/processed_frames/, sheets/ and previews/ | overlay_*_sheet.dds (3528x271, eight 441x271 frames) and overlay_*_static.dds (441x271, frame 000) under gfx/interface/025_alien_technology_in_antarctica/ | Real per-frame native-alpha art; see the overlay animation section below. The former 700x430 statics, two of which carried painted checkerboards, were replaced. |
| Decision category and picture | GFX_decision_category_025_antarctic_expedition, GFX_decision_cat_picture_025_antarctic_expedition | source_png/decision_category_expedition_source.png and decision_cat_picture_expedition_source.png | Matching processed decision files | gfx/interface/decisions/025_alien_technology_in_antarctica/decision_category_expedition.dds and decision_cat_picture_expedition.dds | 52x40 and 114x101 consumers are present and individually opened. |
| Event ideas | GFX_idea_025_antarctic_civilian_commitment, GFX_idea_025_antarctic_analysis, GFX_idea_025_antarctic_survey, GFX_idea_025_antarctic_fragment, GFX_idea_025_antarctic_dependence | source_png/ideas/025_alien_technology_in_antarctica/*_source.png | processed_png/ideas/025_alien_technology_in_antarctica/*.png | gfx/interface/ideas/025_alien_technology_in_antarctica/*.dds | Five 64x64 opaque idea pictures are present and individually opened. |
| Achievements | GFX_achievement_025_alien_technology_* aliases in interface/025_alien_technology_in_antarctica.gfx | source_png/achievements/025_alien_technology_*_source.png | processed_png/achievements/025_alien_technology_*.png | gfx/achievements/025_alien_technology_*.dds | All fourteen normal/grey/not-eligible triplets were individually opened and checked. |

The fourteen achievement IDs are antarctic_vanguard, long_way_south, white_science, nobody_left_on_ice, false_map, without_escort, reclaim_the_station, fragments_of_a_losing_cause, six_fields_of_debris, listen_without_answering, human_factors, system_prefers_us, first_among_equals, and two_crashes_one_answer, each under the runtime prefix 025_alien_technology_.

## Pixel and DDS review

All 136 final DDS files were decoded with the repository image tooling and the decoded PNGs were opened individually or through a named family contact sheet followed by individual confirmation for every source, processed, and final file.

Opaque scene files have full alpha, while transparent overlays, icons, meters, state strips, controls, and achievement variants retain native zero and non-zero alpha where the consumer requires it.

The final DDS files use one mip level and the repository BGRA conversion path; the corrected sector hitbox is 384x58 with four 96x58 frames and its package mirror is byte-identical to the runtime file.

No source or processed image contains readable generated text, a watermark, an unintended logo, a face, or an accidental opaque background in a transparent consumer family.

The visual language is consistent across the family: Antarctic parchment, dark iron, brass, blue-grey ice, and restrained cyan or amber state cues.

## Runtime wiring repairs

The news alias GFX_news_event_025_discovery now points to the 397x153 winner-news DDS because chaosx.news.25 is a news-window consumer; the 457x328 canvas remains on the dedicated GFX_super_event_025_discovery alias.

The central 700x430 operations/map family is displayed at scale = 0.63 and begins at x=300, keeping its rendered width within the 1024x640 board beside the scaled rival rail.

The 280x430 rival rail is displayed at scale = 0.92, and the 700x96 action tray is displayed at scale = 1.394 with five 0.78-scaled action card click regions.

The single map-level selection overlay showed one fixed wedge for any selection; it was replaced by six per-sector highlights controlled by nr25_sector_1_selected_visible to nr25_sector_6_selected_visible.

The former sector_hitbox.dds was a 2800x430 atlas of four full-panel images and could not be a 96x58 click region; it was regenerated from the correct processed four-state atlas and mirrored into the package evidence tree.

## Animation and fallback accounting

The phase banner uses eight separately authored 700x120 frames assembled into a 5600x120 sheet and registered through frameAnimatedSpriteType at two frames per second with a static frame-000 fallback.

The signal, survivor-trace, fragment-instability, dependence and militarised overlays are real eight-frame loops; see the overlay animation section.

This static-only treatment remains an unresolved simplification for four evolution loops.
It is not an approved waiver under the user's no-simplifications requirement; the phase-banner animation is a real frame-by-frame package.

## Reverse orphan scan and exclusions

The source mappings above are an audit inventory, not a completed consumer-coverage pass.
Several rows still use provisional family subfolders instead of the actual flat PNG paths; reconcile them against the package before claiming asset completion.
Board state, privacy, click-region, resolution, and sprite consumer evidence remain mandatory.

The old UFO-race assets and aliases under gfx/event_pictures/025_antarctic_ufo_race/, gfx/interface/decisions/025_antarctic_ufo_race/, gfx/interface/ideas/025_antarctic_ufo_race/, interface/chaosx_pictures.gfx, interface/chaosx_decisions.gfx, interface/chaosx_decision_category_pictures.gfx, and interface/chaosx_ideas.gfx are legacy compatibility consumers gated by ufo_race and are not active Event 025 board assets.

The legacy antarctica_success idea and in_antarctica trait remain referenced by Event 016 compatibility code, so deleting them would expand this task into an unrelated Event 016 migration; they are deliberately preserved and excluded from the Event 025 active path.

No Event 025 portrait, flag, unit counter, 3D model, or equipment visual is introduced by this package.

## Audio handoff

The runtime audio is sound/025_alien_technology_in_antarctica/super_event_025_antarctic_first_reveal.ogg, with WAV source and receipts under source_audio/.

The OGG SHA-256 is 7c7a7d48b54b5a1e3e494ec7afd2611ae9e937d611053204c040733c22b35e23, and the WAV SHA-256 is bcb9ee95809f01413a947d10d684859b8d20da1b0319a1f1d384263e431eb126.

The audio handoff verified 115 seconds of stereo PCM16 source at 44.1 kHz and sound ID 109 with six volume wrappers; the edited OGG source receipt mentioned by the handoff is unavailable, so the prior edited hash cannot be independently rechecked.

The event source sets current_super_event_audio_id and calls play_current_super_event_audio, but the gameplay-side audio playback could not be verified through a completed live event render.

## MCP and worker evidence

hoi4.reference_context returned installed-game and offline-wiki citations for GUI, event, technology, and AI surfaces, and the returned GUI documentation was read before the source repair.

The earlier Event 025 entry inspect returned status=ok with code EVENT_INSPECTED_PARTIAL, but its validation was false because the workspace analysis was deferred and the scan was limited to 64 of 368 inline source files.
Later narrow event `.84`, exact-window GUI, and probability inspections timed out after 600 seconds; the exact meta-effect reference and its four-line retry also timed out after 600 seconds.

The targeted hoi4.gui_inspect request for nr25_expedition_board_window with a 1920x1080 baseline scenario timed out after 180 seconds without an artifact.

Earlier GUI render attempts also timed out, so source-level geometry evidence is not being presented as production MCP render evidence.

Targeted technology inspections for brilliant_scientist_portal_warfare_tech, brilliant_scientist_temporal_guard_tech, and brilliant_scientist_alien_infantry_tech each timed out after 180 seconds.

The first round of required custom workers returned not_found, and a fresh isolated batch was reissued with fork_context=false; the current retry remains pending at the time of this audit and will be reconciled in the completion handoff.

No live HOI4 process was launched by this audit.

## Expedition Board MCP evidence (2026-10-04)

`hoi4.gui_inspect` of `nr25_expedition_board_window` (scenario `nr25_board_final_inspect_20261004`) returned `GUI_INSPECTED`, complete, 131 inspected elements, no skipped sources, shared revision `4e60a60d31be5f7c`.

`hoi4.gui_render` ran with named scenarios and explicit localisation fixtures, because live scripted localisation and country flags cannot resolve offline. Fixture text matches the in-game strings and the card cost structure.

| Pass | Scenario | Resolutions | Finding |
| --- | --- | --- | --- |
| Before (stopped-thread geometry) | `nr25_board_survey_pass2_20261004` | 1920x1080 | Root used `origo = center` with clipping and showed one quadrant; fonts `hoi_12mbs` and `hoi_14mbs` are undefined in vanilla. Fixed earlier in this pass. |
| Before (this tranche) | `nr25_board_survey_pass3_20261004` | 1920x1080 | Status cards overlapped by 80 px, value text sat on its meter, route and outpost text truncated, action text overlapped the emblem and its own cost line. |
| After | `nr25_board_final_20261004` and `nr25_board_final_confirm_20261004` | 1920x1080, 1600x900, 1366x768 at UI scale 1 | Full board inside every viewport; three stacked status cards with separate value, meter and threshold rows; route, outpost and target rows readable; per-sector highlight aligned with its wedge; rival names and flags visible; action cards show a label plus cost or status within the card; confirmation window clean. |

The after-render cropped image SHA-256 is `3a9e8720d58326cd2fa54cffe54f8c784edbe094fd8d9104486b60df7678df4b`, the resolution matrix is `70101cbae675e89c8aa609a8903cc5f4ca7b67222c5f3770a849010edd908fc9`, and the confirmation render is `52467ef8d010224d9eb9cea7b2f320b6a855a1e55fe3c91e27920991fd9d02a8`; all are under the hoi4-agent-tools workspace artifacts.

Remaining renderer notes: `GUI_SPRITE_DECLARED_SIZE_MISMATCH` on the two status-panel cornered tiles is expected, because a cornered tile declares its drawn size; `GUI_ANIMATION_STATIC_FALLBACK_MISSING` on the phase banner is a naming check, since the static banner is a separate element toggled by the scripted GUI; `GUI_RESOLUTION_DRIFT` reflects the centred board at smaller viewports. Hover, pressed and disabled card states were not rendered. The disabled action-card frame had been fitted with its icicles and sat 25 px narrower than the other states; it was re-fitted by its card body so all four frames share one footprint (see `manifest_expedition_board.md`).

## Evolution overlay animations (2026-10-04)

The four recommended loops and the militarised-zone overlay of spec 008 are eight-frame `frameAnimatedSpriteType` sheets drawn over the sector map at its displayed size (441x271, scale 1, x 300, y 132), under the sector buttons, emblems and labels.
Every frame and layer is a separate native-alpha generation from the session's image tool (no model selector exposed); no frame is a transform or filter of another.
The signal loop is eight full frames aligned on the map hub; the other four are one fixed generated base layer (footprint trail, shards, border tendrils, warships and zones) plus eight generated motion layers registered on the base canvas, with one recorded normalisation (survivor frame 004 scaled 0.64 about the figure's feet).
Rejected candidates are kept beside the accepted `_rN` revisions in the source folders.
The former 700x430 static overlays were replaced by frame 000 of each loop; the survivor-trace and fragment statics had painted checkerboard pixels.

| Overlay | Gate flag | fps | Sheet SHA-256 | Static SHA-256 |
| --- | --- | --- | --- | --- |
| Signal | `chaosx_nr25_evolution_active_signal` | 4 | `fe77b19e78a6e48b146a08c2d41c0ccf41fa1c76b8470e6955aad19b21d9443a` | `13b06fec33d545dddb1ca8b9dc4cc8a80e3ddad40ed6e68223504d2aeb0ec182` |
| Survivor trace | `chaosx_nr25_evolution_something_survived` | 4 | `838f8e7c3099c1fc0f810e8c65cb551c3eb51fa43796e6cb1358f3d6ef883d36` | `cfc047134a2350e92c51a168180c83c3f210d0b4485470034f227d801de80e9b` |
| Fragment instability | `chaosx_nr25_evolution_wreck_breaking_apart` | 6 | `8d5e6e8353e9702b884fff53d6720c59153f087e0d703ddca0c19b9821e80afc` | `1713acfae7f140025c781ea490e484aed7366f2ba7337bc2252976a846956eea` |
| Dependence | `chaosx_nr25_evolution_technology_changes_users` | 4 | `8f56dfa0ecef689841ae41f4440d32fde6c82bbcaff6499ceb23a341c60f55dc` | `4b78496c8a72a16d66ecd5abd0aada6728c13adaa6ccaf2f7e42a0e81cdfd507` |
| Militarised | `chaosx_nr25_evolution_militarised_antarctica` | 4 | `2fdeede159a9135456aab723107e62f63ab09478295af189dd255c1ed276c99e` | `42a912ffe87ecdec8248b459f00014f6b61ee5cdcb25209d83202cb7b074d826` |

Every DDS round-trips to its sheet or static PNG with zero pixel difference.
The new header control `nr25_board_animation` (`GFX_025_expedition_control_animation`, a 128x32 four-state strip generated to match the existing control family) toggles `chaosx_nr25_animations_disabled`, so the static frames and the static phase banner are reachable for the first time.
The static fallbacks now carry the animated sprites' base names (`GFX_025_expedition_signal` for `GFX_025_expedition_signal_animated`, and `GFX_025_expedition_phase_banner` for the banner, replacing an unused eight-frame banner registration), which clears the renderer's missing-fallback warnings.

`hoi4.gui_inspect` (scenario `nr25_overlays_animated_20261004`) returned `GUI_INSPECTED` with 138 elements and no skipped sources.
`hoi4.gui_render` scenario `nr25_overlays_all_animated_20261004b` at 1920x1080, UI scale 1, with explicit visibility for the five animated overlays, no selected sector and the resolved panel hidden, at animation time 0.75 s (frame 003), returned `GUI_RENDERED` (SVG SHA-256 `b5c81a4180ec36d120f83fdeb43f3236d20c9c21fe18f5f33d0d3e93ae192f52`): the hub pulse, footprint trail and figure, shards, border tendrils and warships sit on their intended map features beneath the emblems and labels, and the new control sits left of refresh in the header.
Only the overlap of all five overlays was rendered; real campaigns show one overlay per active evolution, and the animation itself (timing and loop seams) is verified only through the review GIFs, not in game.

## Rival paging control (2026-10-05)

The rival column keeps its three cards and gains `nr25_rivals_next` (`GFX_025_expedition_control_next_rivals`, a 128x32 four-state strip in the control family, double-chevron glyph, native ImageGen alpha with no background removal) at board position x 952, y 432.
It sits in the free strip right of the cards: the card click regions end at x 939, so the 32x32 control does not overlap any card, and its lower edge lines up with the third card.
It is shown only while the viewer's last card build counted more than three valid rivals (`chaosx_nr25_rival_candidate_count` above `chaosx_nr25_board.rival_cards`).

| Pass | Scenario | Resolutions | Artifact | Finding |
| --- | --- | --- | --- | --- |
| Inspect, before | `nr25_rival_paging_before_20261005` | generated default | `gui-inspect` SHA-256 `ba8c0559515e9dbaf0bbb66141d3c9bf7474790f533a7ecb34d1827043faf49f`, revision `c7cc4c60a37ff2ec` | 138 elements, no skipped sources. |
| Render, before | `nr25_rival_paging_before_20261005` | 1920x1080, UI 1 | full SVG `f9fb893a470ad5b585607f1d46420da723255783c8031a8e3c61348576f5c063`, source revision `9e2a0521` | Three cards, no way to reach a fourth or fifth rival. |
| Render, after | `nr25_rival_paging_after_20261005` (normal, hover, disabled) | 1920x1080, 1600x900, 1366x768, UI 1 | full PNG `25f3f40e5a4d8ff62af87f2628f3d55e22682876998d1623ec6806f1b2240112`, click regions `5d045c10b9af016a685accfc66efbbc2b53cab712f77b507748de407ca405fd1`, resolution matrix `cb9e58f8abf378227dbaff1bba9793ea29c5f9cd1b5bb3480baa7e4e77a0bd7a`, state matrix `a9e15151ddb1d100e38501848cff84a726e9a778164df6dbdc50f0ed4d61ab2c`, source revision `5c994b7b` | Control drawn right of the third card inside the rival panel; its click region is separate from the three card regions; the whole board stays inside every viewport. |
| Render, after (off-page selection) | `nr25_rival_paging_after_1366_20261005` (hover) | 1366x768, UI 1 | full SVG `b98d525d328fbbbe7bca46507b4f93ded1c6f5dccaed318b77125ff0d0774cca`, source revision `4d29ef75` | Selected-target row names a rival whose card is on another page while three other rivals are shown. |

The render fixtures supply the card names, card text and the selected-target name as localisation values, because live country scopes and scripted localisation do not resolve offline; the selected-target row prints `[?chaosx_nr25_rival_target_id.GetName]` in game. The paging itself (offset skip, wrap to the first page, kept selection) is source-reviewed and `needs_live_game`.

## Evolution V outcome idea pictures (2026-10-05)

The five institutional outcome ideas no longer reuse the analysis, survey, fragment and dependence pictures.
Each has its own 64x64 opaque painted picture in the existing Event 025 idea family (dark vignette, brass, frost and teal light), generated with the session's image tool from a reference sheet of the five existing ideas (`source_png/ideas/idea_family_reference.png`), resized once with Lanczos to 64x64 and converted with the skill's DDS converter; each DDS decodes to its processed PNG with zero pixel difference.
No two Event 025 ideas now share a picture.

| Sprite | Consumer | Source (SHA-256) | DDS (SHA-256) |
| --- | --- | --- | --- |
| `GFX_idea_025_outcome_contained` | `chaosx_nr25_outcome_contained` (Contained) | `source_png/ideas/idea_outcome_contained_source.png` (`73c4840f6e19eee2dbd696b26d10ababab79d4c373a2fcf142a8f595a4f88844`) | `gfx/interface/ideas/025_alien_technology_in_antarctica/idea_outcome_contained.dds` (`9776526d464f2b00416aeb349487737a54543308f24a05bebe485ab8f4912157`) |
| `GFX_idea_025_outcome_independent` | `chaosx_nr25_outcome_independent` (Independent Adaptation) | `source_png/ideas/idea_outcome_independent_source.png` (`e98bc87feff168b3996bfc3232443729a053a7e6fd399e2f789051f40c500660`) | `gfx/interface/ideas/025_alien_technology_in_antarctica/idea_outcome_independent.dds` (`f6eafb45ca15fad43628e68124bc957a769e5e54b2e720f0881ab0fdc8f8b008`) |
| `GFX_idea_025_outcome_integrated` | `chaosx_nr25_outcome_integrated` (Integrated) | `source_png/ideas/idea_outcome_integrated_source.png` (`c5ca914b3325b40a98a8826f6e85449e3392f0cfd2c526c84b2f223bb6d4c3ed`) | `gfx/interface/ideas/025_alien_technology_in_antarctica/idea_outcome_integrated.dds` (`64926502c99cdb3de841ddd4f027ff752b76dcba4c359f3454e84b932aac6b47`) |
| `GFX_idea_025_outcome_reliance` | `chaosx_nr25_outcome_reliance` (Reliance) | `source_png/ideas/idea_outcome_reliance_source.png` (`39e06a7fd08bf1d94750f2046b22a9582103fce46dfcffbf13c17bbbb974ac1b`) | `gfx/interface/ideas/025_alien_technology_in_antarctica/idea_outcome_reliance.dds` (`4e11ebf66d43cab750c3fa42f80804793f2c77f9b7390a8e65240302e4d98a58`) |
| `GFX_idea_025_outcome_autonomous` | `chaosx_nr25_outcome_autonomous` (Autonomous Network) | `source_png/ideas/idea_outcome_autonomous_source.png` (`366459997c331b47fb26b801ab1003a9f8e1255cbda58134160dd571d373372b`) | `gfx/interface/ideas/025_alien_technology_in_antarctica/idea_outcome_autonomous.dds` (`ccf6d1ee75def71e3790523faab1150ce88d3d9a819e3fa803c8b72d1cf06822`) |

## Remaining limits

Neither complete asset wiring nor overall Event 025 acceptance is established.
Missing consumers, provisional paths, accepted animation requirements, hover and disabled GUI states, baseline/post-patch probability evidence, independent audits, catalog updates, and live runtime evidence remain open.
Recording a blocker documents a failed gate; it does not turn that gate into a pass.
