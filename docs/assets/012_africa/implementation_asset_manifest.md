# Event 012 Africa Implementation Asset Manifest

Updated: 2026-06-21

This manifest records which Event 012 Africa assets are wired into gameplay/interface files and which asset surfaces remain blocked.

## Wired Interface File

- `interface/012_africa.gfx`
- `interface/012_africa_scripted_gui.gui`

## Event Images

| Sprite | DDS path | Source |
| --- | --- | --- |
| `GFX_report_event_012_charter_league_africa_is_one` | `gfx/event_pictures/012_africa/report_event_012_charter_league_africa_is_one.dds` | `docs/assets/012_africa/generated_art/processed_png/report_event_012_charter_league_africa_is_one_processed.png` |
| `GFX_news_event_012_authority_atlas_archive_old_seats` | `gfx/event_pictures/012_africa/news_event_012_authority_atlas_archive_old_seats.dds` | `docs/assets/012_africa/generated_art/processed_png/news_event_012_authority_atlas_archive_old_seats_processed.png` |
| `GFX_news_event_012_scramble_for_africa_reversal` | `gfx/event_pictures/012_africa/news_event_012_scramble_for_africa_reversal.dds` | `docs/assets/012_africa/generated_art/processed_png/news_event_012_scramble_for_africa_reversal_processed.png` |

## Super-Event Images and Audio

Twelve super-event presentation roles have registered images and final text localisation. Thirteen Event 012 audio roles have music-mode OGG audio and sound-mode WAV audio; the World Root terminal cue is audio-only and reuses the shared slot `72` World Is One presentation.

| Sprite | DDS path | Source |
| --- | --- | --- |
| `GFX_super_event_012_africa_unification` | `gfx/super_events/super_event_012_africa_unification.dds` | `docs/assets/012_africa/generated_art/processed_png/super_event_012_africa_unification_candidate_processed.png` |
| `GFX_super_event_012_scramble_for_africa` | `gfx/event_pictures/012_africa/news_event_012_scramble_for_africa_reversal.dds` | `docs/assets/012_africa/generated_art/processed_png/news_event_012_scramble_for_africa_reversal_processed.png` |
| `GFX_super_event_012_archive_bestiary` | `gfx/super_events/super_event_012_archive_bestiary.dds` | `docs/assets/012_africa/generated_art/processed_png/super_event_012_archive_bestiary_candidate_processed.png` |
| `GFX_super_event_012_counterfeit_crowns` | `gfx/super_events/super_event_012_counterfeit_crowns.dds` | `docs/assets/012_africa/super_events/counterfeit_crowns_image/processed_png/super_event_012_counterfeit_crowns_processed.png` |
| `GFX_super_event_012_continent_sponsor` | `gfx/super_events/super_event_012_continent_sponsor.dds` | `docs/assets/012_africa/generated_art/processed_png/super_event_012_continent_sponsor_candidate_processed.png` |
| `GFX_super_event_012_rsa_peace` | `gfx/super_events/super_event_012_rsa_peace.dds` | `docs/assets/012_africa/generated_art/processed_png/super_event_012_rsa_peace_candidate_processed.png` |
| `GFX_super_event_012_dynamic_cross_continent_union` | `gfx/super_events/super_event_012_dynamic_cross_continent_union.dds` | `docs/assets/012_africa/generated_art/processed_png/super_event_012_dynamic_cross_continent_union_processed.png` |
| `GFX_super_event_012_world_is_one_gate` | `gfx/super_events/super_event_012_world_is_one_gate.dds` | `docs/assets/012_africa/generated_art/processed_png/super_event_012_world_is_one_gate_candidate_processed.png` |
| `GFX_super_event_012_forest_parliament` | `gfx/super_events/super_event_012_forest_parliament.dds` | `docs/assets/012_africa/super_events/variant_images_batch_forest_root/processed_png/super_event_012_forest_parliament_processed.png` |
| `GFX_super_event_012_world_root_mandate` | `gfx/super_events/super_event_012_world_root_mandate.dds` | `docs/assets/012_africa/super_events/variant_images_batch_forest_root/processed_png/super_event_012_world_root_mandate_processed.png` |
| `GFX_super_event_012_root_and_fang` | `gfx/super_events/super_event_012_root_and_fang.dds` | `docs/assets/012_africa/super_events/variant_images_batch_root_archive/processed_png/super_event_012_root_and_fang_processed.png` |
| `GFX_super_event_012_archive_world` | `gfx/super_events/super_event_012_archive_world.dds` | `docs/assets/012_africa/super_events/variant_images_batch_root_archive/processed_png/super_event_012_archive_world_processed.png` |

Final wired audio:

| Role | Music OGG | Sound WAV | Super-event slot |
| --- | --- | --- | --- |
| `africa_is_one_unification` | `music/super_event_africa_unification.ogg` | `sound/chaosx_super_event_africa_unification.wav` | `68` |
| `africa_scramble_reaction` | `music/super_event_africa_scramble.ogg` | `sound/chaosx_super_event_africa_scramble.wav` | `69` |
| `africa_old_seats_reveal` | `music/super_event_africa_old_seats.ogg` | `sound/chaosx_super_event_africa_old_seats.wav` | `70` |
| `africa_counterfeit_crowns` | `music/super_event_africa_counterfeit_crowns.ogg` | `sound/chaosx_super_event_africa_counterfeit_crowns.wav` | `71` |
| `africa_world_is_one_terminal` | `music/super_event_africa_world_is_one.ogg` | `sound/chaosx_super_event_africa_world_is_one.wav` | `72` |
| `africa_continent_sponsor` | `music/super_event_africa_continent_sponsor.ogg` | `sound/chaosx_super_event_africa_continent_sponsor.wav` | `73` |
| `africa_rsa_allies_peace` | `music/super_event_africa_rsa_allies_peace.ogg` | `sound/chaosx_super_event_africa_rsa_allies_peace.wav` | `74` |
| `africa_dynamic_cross_continent_union` | `music/super_event_africa_dynamic_cross_continent_union.ogg` | `sound/chaosx_super_event_africa_dynamic_cross_continent_union.wav` | `75` |
| `africa_forest_parliament_reveal` | `music/super_event_africa_forest_parliament.ogg` | `sound/chaosx_super_event_africa_forest_parliament.wav` | `76` |
| `africa_world_root_mandate` | `music/super_event_africa_world_root.ogg` | `sound/chaosx_super_event_africa_world_root.wav` | `77` |
| `africa_parliament_of_root_and_fang_escalation` | `music/super_event_africa_root_and_fang.ogg` | `sound/chaosx_super_event_africa_root_and_fang.wav` | `78` |
| `africa_archive_world_union_terminal` | `music/super_event_africa_archive_world.ogg` | `sound/chaosx_super_event_africa_archive_world.wav` | `79` |
| `africa_world_is_one_root_variant_terminal` | `music/super_event_africa_world_is_one_root_terminal.ogg` | `sound/chaosx_super_event_africa_world_is_one_root_terminal.wav` | `80` audio id, visible slot `72` |

The final source, licensing, hashes, and conversion notes remain in `docs/assets/012_africa/super_events/audio/manifest.md`.

Variant trigger notes:

- slot `76` fires from `AFR_forest_parliament`;
- slot `77` fires from `AFR_world_root_mandate`;
- slot `78` fires from `AFR_treaty_of_teeth_and_roots`;
- slot `79` is an Archive-Bestiary route presentation variant of the existing terminal `AFR_the_world_is_one` gate and does not bypass the World Is One prerequisites.
- audio id `80` is selected by `africa_emit_world_is_one_terminal_super_event` when the World Root route reaches the shared terminal `AFR_the_world_is_one` gate; it does not create a separate presentation slot or bypass the World Is One prerequisites.

## Focus, Idea, Decision, and Achievement Icons

Current focus and idea icons were rebuilt again on 2026-06-21 to remove the reported white background / white matte issue and hidden RGB bleed risks. The live DDS filenames and `interface/012_africa.gfx` sprite names did not change. Focus/goal icons and idea/national-spirit icons are maintained as separate asset families; idea icons are distinct 64x64 spirit icons and are not smaller goal icons.

Current focus/goal icon source package:

- `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v6_2026_06_21/`

Current idea/national-spirit icon source package:

- `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v7_2026_06_20/`

Final checker review sheets:

- `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v6_2026_06_21/contact_sheets/processed_checker_contact.png`
- `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v6_2026_06_21/contact_sheets/live_dds_checker_contact.png`
- `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v6_2026_06_21/validation/validation_summary.md`
- `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v7_2026_06_20/contact_sheets/idea_icons_processed_checker_contact.png`
- `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v7_2026_06_20/contact_sheets/idea_icons_live_dds_checker_contact.png`
- `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v7_2026_06_20/validation/validation_summary.md`

Event 012 focus filter sprites are registered in `interface/012_africa.gfx`. The live 27x27 DDS files are derived from the regenerated Event 012 goal icons and have processed PNG sources under `docs/assets/012_africa/focus_filter_icons/processed_png/`.

| Filter sprite | DDS path | Source |
| --- | --- | --- |
| `GFX_FOCUS_FILTER_AFR_CHARTER` | `gfx/interface/focusview/filter/012_africa/filter_africa_charter.dds` | `docs/assets/012_africa/focus_filter_icons/processed_png/filter_africa_charter.png` |
| `GFX_FOCUS_FILTER_AFR_AUTHORITY_ATLAS` | `gfx/interface/focusview/filter/012_africa/filter_africa_authority_atlas.dds` | `docs/assets/012_africa/focus_filter_icons/processed_png/filter_africa_authority_atlas.png` |
| `GFX_FOCUS_FILTER_AFR_SCRAMBLE` | `gfx/interface/focusview/filter/012_africa/filter_africa_scramble.dds` | `docs/assets/012_africa/focus_filter_icons/processed_png/filter_africa_scramble.png` |
| `GFX_FOCUS_FILTER_AFR_BESTIARY` | `gfx/interface/focusview/filter/012_africa/filter_africa_bestiary.dds` | `docs/assets/012_africa/focus_filter_icons/processed_png/filter_africa_bestiary.png` |
| `GFX_FOCUS_FILTER_AFR_WORLD_ORDER` | `gfx/interface/focusview/filter/012_africa/filter_africa_world_order.dds` | `docs/assets/012_africa/focus_filter_icons/processed_png/filter_africa_world_order.png` |

The older `docs/assets/012_africa/icons_animation/static/` focus and idea outputs are superseded by the regenerated packages above. The `icons_animation` package is still retained for decision-category icon source notes and animated UI seal source material, documented in:

- `docs/assets/012_africa/icons_animation/manifest.md`
- `docs/assets/012_africa/icons_animation/gfx_handoff.md`
- `docs/assets/012_africa/achievement_icons_foundation_batch_1/manifest.md`
- `docs/assets/012_africa/achievement_icons_batch_2/manifest.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_achievement_icons_foundation_batch_1_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_achievement_icons_batch_2_handoff.md`

Wired destinations:

- Focus icons: `gfx/interface/goals/012_africa/`
- Idea icons: `gfx/interface/ideas/012_africa/`
- Decision category icons: `gfx/interface/decisions/012_africa/`
- Achievement icons: `gfx/achievements/ACH_AFR_*.dds`

The achievement placeholders for Event 012 were replaced with themed generated icons and generated grey / not-eligible variants.

Foundation achievement icons are live for:

- `ACH_AFR_CHARTER_WITH_TEETH`
- `ACH_AFR_ARCHIVE_OF_OLD_SEATS`
- `ACH_AFR_BESTIARY_HAS_A_SEAT`
- `ACH_AFR_NOT_PAPER_ANYMORE`
- `ACH_AFR_ALLIES_MADE_PEACE`
- `ACH_AFR_WORLD_IS_ONE_ONLY_AFTER_AFRICA`

Each has normal, `_grey`, and `_not_eligible` DDS variants in `gfx/achievements/` plus source/processed PNGs, DDS copies, and contact sheets under `docs/assets/012_africa/achievement_icons_foundation_batch_1/`.

Batch 2 achievement icons are live for:

- `ACH_AFR_CHARTER_WITHOUT_CHAINS`
- `ACH_AFR_NO_SECOND_SCRAMBLE`
- `ACH_AFR_PAPER_TO_LIVING`
- `ACH_AFR_ONE_BUT_NOT_ALONE`
- `ACH_AFR_RSA_THE_UNION_BREAKS`
- `ACH_AFR_RETURN_PASSAGES`
- `ACH_AFR_KILWA_TO_KUSH_LEDGER`
- `ACH_AFR_CHARTER_HAS_TOO_MANY_SIGNATURES`
- `ACH_AFR_CONTINENTS_HAVE_A_CONGRESS`

Each has normal, `_grey`, and `_not_eligible` DDS variants in `gfx/achievements/` plus source/processed PNGs and contact sheets under `docs/assets/012_africa/achievement_icons_batch_2/`.

Archive/Bestiary batch 3 achievement icons are live for:

- `ACH_AFR_NO_COUNTERFEIT_CROWNS`
- `ACH_AFR_THE_FOREST_SIGNED_BACK`
- `ACH_AFR_BAOBAB_FILIBUSTER`
- `ACH_AFR_OLD_SEATS_NEW_UNION`

Each has normal, `_grey`, and `_not_eligible` DDS variants in `gfx/achievements/` plus source/processed PNGs, DDS copies, and contact sheets under `docs/assets/012_africa/achievement_icons_archive_bestiary_batch_3/`.

Prompt-completion achievement icon batches 4-6 are live for:

- `ACH_AFR_THE_ALLIES_SIGN`
- `ACH_AFR_ELEPHANTS_REMEMBER`
- `ACH_AFR_ANANSE_WROTE_THE_ORDERS`
- `ACH_AFR_TIDE_TOOK_THE_PORT`
- `ACH_AFR_FOREST_GUARDIAN_PACT`
- `ACH_AFR_BIGGER_CARAVAN`
- `ACH_AFR_NOT_A_MAP_COLOUR`
- `ACH_AFR_CONGRESS_OVER_COMMAND`
- `ACH_AFR_COMMAND_OVER_CONGRESS`
- `ACH_AFR_OLD_THRONES_VOTE`
- `ACH_AFR_EVERY_CAPITAL_HEARD_THE_DRUM`
- `ACH_AFR_WORLD_SCHOOL`
- `ACH_AFR_AFRO_ASIAN_VECTOR`
- `ACH_AFR_AFRO_EURASIAN_QUESTION`
- `ACH_AFR_WORLD_IS_ONE`
- `ACH_AFR_NO_FALSE_BEASTS`
- `ACH_AFR_FOREST_VOTES_NO`
- `ACH_AFR_NO_IVORY_TREASURY`
- `ACH_AFR_TREATY_WITH_TEETH`
- `ACH_AFR_WORLD_HAS_ROOTS`
- `ACH_AFR_SMALL_THRONES_SIT_TOGETHER`
- `ACH_AFR_NO_MAP_CAN_HOLD_THIS`
- `ACH_AFR_WALKING_WALLS`
- `ACH_AFR_ARCHIVE_UNBROKEN`
- `ACH_AFR_CORAL_ADMIRALTY`
- `ACH_AFR_KUOMBOKA_ARMY`

Each has normal, `_grey`, and `_not_eligible` DDS variants in `gfx/achievements/`, sprite registrations in `interface/chaosx_achievements.gfx`, and source/processed PNGs, DDS copies, contact sheets, and manifests under `docs/assets/012_africa/achievement_icons_prompt_completion_batch_4/`, `docs/assets/012_africa/achievement_icons_prompt_completion_batch_5/`, and `docs/assets/012_africa/achievement_icons_prompt_completion_batch_6/`.

The missing high-chaos actor achievement package is live for:

- `ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE`
- `ACH_AFR_GENTLE_VETO`
- `ACH_AFR_BIRD_WAS_RIGHT`
- `ACH_AFRICA_TERRACOTTA_LINE`

Each has normal, `_grey`, and `_not_eligible` DDS variants in `gfx/achievements/`, sprite registrations in `interface/chaosx_achievements.gfx`, and source/processed PNGs, DDS copies, contact sheets, and manifest notes under `docs/assets/012_africa/missing_high_chaos_actor_assets/`.

## Animated Assets

Frame sources and contact sheets live under `docs/assets/012_africa/icons_animation/frames/` and `docs/assets/012_africa/icons_animation/previews/`.

Wired frame sheets:

| Sprite | DDS path | Frames | Source |
| --- | --- | --- | --- |
| `GFX_africa_authority_atlas_seal_loop` | `gfx/interface/animated/012_africa/authority_atlas_seal_loop_sheet.dds` | 4 | `docs/assets/012_africa/icons_animation/previews/authority_atlas_seal_loop_sheet.png` |
| `GFX_africa_charter_league_banner_pulse` | `gfx/interface/animated/012_africa/charter_league_banner_pulse_sheet.dds` | 4 | `docs/assets/012_africa/icons_animation/previews/charter_league_banner_pulse_sheet.png` |
| `GFX_africa_bestiary_warning_loop` | `gfx/interface/animated/012_africa/bestiary_warning_loop_sheet.dds` | 4 | `docs/assets/012_africa/icons_animation/previews/bestiary_warning_loop_sheet.png` |

The sprites are registered as `frameAnimatedSpriteType` in `interface/012_africa.gfx`. Static fallback sprites are also registered and copied into the final animated asset folder:

- `GFX_africa_authority_atlas_seal_static`: `gfx/interface/animated/012_africa/authority_atlas_seal_loop_fallback_128x128.dds`
- `GFX_africa_charter_league_banner_static`: `gfx/interface/animated/012_africa/charter_league_banner_pulse_fallback_160x96.dds`
- `GFX_africa_bestiary_warning_static`: `gfx/interface/animated/012_africa/bestiary_warning_loop_fallback_96x96.dds`

Status note: this three-sprite visual strip is useful and wired, but it is not accepted as the full prompt-equivalent Continental Congress GUI/animation package. The asset prompt still queues the prompt-named families `africa_charter_seal_animated`, `africa_cohesion_warning_border_animated`, `africa_green_covenant_seal_animated`, and `africa_formable_ready_emblem_animated`, plus their static fallbacks and the broader background/header/meter/card/warning/seal/formable UI families, unless a later handoff proves an explicit parent-approved equivalence. Current disposition: `docs/plans/012_africa_plans/2026-06-21_continental_congress_gui_animation_gap_handoff.md`.

## Scripted GUI

The live Continental Congress decision-category panel is wired through:

- `common/scripted_guis/012_africa_scripted_gui.txt`
- `interface/012_africa_scripted_gui.gui`

It reuses the existing `GFX_goal_africa_political_congress` icon and displays live mandate values, World Is One prerequisite counters, active dossier, and active Bestiary case. The panel now includes a visual strip with the Charter banner, Authority Atlas seal, and Bestiary warning seal. Static fallback sprites remain visible under route-gated animated overlays, and the scripted GUI hides Archive/Bestiary seals until the related systems are open.

This static/scripted wiring evidence does not replace live in-game render/readability proof for the panel or animated playback.

## High-Chaos Identity Portraits

The nonhuman / supernatural Event 012 portrait gap is covered for the live 15 Bestiary actor tags. `GHP` reuses the existing Independence Wave gorilla chair portrait. The first generated identity package covers `BBS`, `TDM`, `ANW`, `OVN`, and `CRR`; the expanded Bestiary actor package covers `CTL`, `OKP`, `TRM`, `HGD`, and `GHC`; the missing high-chaos actor package covers `BON`, `HYR`, `BIR`, and `SAO`. All generated portraits are converted, registered in `interface/012_africa.gfx`, and referenced by the corresponding country history files.

Package:

- `docs/assets/012_africa/high_chaos_identity/manifest.md`
- `docs/assets/012_africa/high_chaos_identity/gfx_handoff.md`
- `docs/assets/012_africa/bestiary_actor_assets/`
- `docs/assets/012_africa/missing_high_chaos_actor_assets/`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_bestiary_actor_assets_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_missing_high_chaos_actor_parent_handoff.md`

Converted portrait DDS files:

- `gfx/leaders/012_africa/leader_012_africa_bbs_baobab_senate.dds`
- `gfx/leaders/012_africa/leader_012_africa_tdm_tidemark_dominion.dds`
- `gfx/leaders/012_africa/leader_012_africa_anw_ananse_web.dds`
- `gfx/leaders/012_africa/leader_012_africa_ovn_nature_courts.dds`
- `gfx/leaders/012_africa/leader_012_africa_crr_river_council.dds`
- `gfx/leaders/012_africa/leader_012_africa_ctl_chimpanzee_telegraph_league.dds`
- `gfx/leaders/012_africa/leader_012_africa_okp_okapi_court.dds`
- `gfx/leaders/012_africa/leader_012_africa_trm_termite_citadel_engineers.dds`
- `gfx/leaders/012_africa/leader_012_africa_hgd_honeyguide_commons.dds`
- `gfx/leaders/012_africa/leader_012_africa_ghc_great_herds.dds`
- `gfx/leaders/012_africa/leader_012_africa_bonobo_kinship_congress.dds`
- `gfx/leaders/012_africa/leader_012_africa_hyena_radio_dominion.dds`
- `gfx/leaders/012_africa/leader_012_africa_bird_of_the_walls.dds`
- `gfx/leaders/012_africa/leader_012_africa_sao_terracotta_host.dds`

Status:

- `BBS`, `TDM`, `ANW`, `OVN`, `CRR`, `CTL`, `OKP`, `TRM`, `HGD`, and `GHC` no longer need generic human portraits as an asset-source gap.
- Parent wiring is complete for `.gfx` sprite registration and `history/countries/` leader portrait references.

## Regional Authority Portraits

The ten human regional authority tags now use distinct generated institutional leader portraits and direct institutional leader names. These are separate from the high-chaos actor portraits and are not scaled versions of focus or idea icons.

Package:

- `docs/assets/012_africa/regional_authority_portraits/manifest.md`
- `docs/assets/012_africa/regional_authority_portraits/gfx_handoff.md`
- `docs/assets/012_africa/regional_authority_portraits/contact_sheets/regional_authority_portraits_contact_sheet.png`
- `docs/assets/012_africa/regional_authority_portraits/contact_sheets/regional_authority_portraits_live_dds_contact_sheet.png`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_regional_authority_portraits_handoff.md`

Converted portrait DDS files:

- `gfx/leaders/012_africa/leader_012_africa_wac_west_african_congress.dds`
- `gfx/leaders/012_africa/leader_012_africa_sah_sahel_caravan.dds`
- `gfx/leaders/012_africa/leader_012_africa_mag_maghreb_coast.dds`
- `gfx/leaders/012_africa/leader_012_africa_nhr_nile_horn_league.dds`
- `gfx/leaders/012_africa/leader_012_africa_eac_east_african_railway_congress.dds`
- `gfx/leaders/012_africa/leader_012_africa_glk_great_lakes_council.dds`
- `gfx/leaders/012_africa/leader_012_africa_cbc_congo_basin_charter.dds`
- `gfx/leaders/012_africa/leader_012_africa_zsc_zambezi_stone_cities.dds`
- `gfx/leaders/012_africa/leader_012_africa_slc_south_african_liberation_congress.dds`
- `gfx/leaders/012_africa/leader_012_africa_ioc_indian_ocean_congress.dds`

Status:

- `WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, and `IOC` no longer reference `GFX_portrait_generic_africa`.
- Parent wiring is complete for `.gfx` sprite registration and `history/countries/` leader portrait references.

## Country Flags

The created Event 012 country tags now have generated symbolic flag families under `gfx/flags/`. These are final generated flags for the created Event 012 tags, not attested historical flags for dossier polities.

Generated package:

- `docs/assets/012_africa/generated_flags/manifest.md`
- `docs/assets/012_africa/generated_flags/source_png/`
- `docs/assets/012_africa/generated_flags/contact_sheets/012_africa_generated_flags_contact_sheet.png`
- `docs/assets/012_africa/missing_high_chaos_actor_assets/manifest.md`

Live generated coverage:

- Root flags: `gfx/flags/<TAG>.tga`, root DDS where generated by the package, and ideology variants for all 25 created Event 012 tags.
- Medium flags: `gfx/flags/medium/<TAG>.tga` and ideology variants for all 25 created Event 012 tags.
- Small flags: `gfx/flags/small/<TAG>.tga` and ideology variants for all 25 created Event 012 tags.

Covered tags:

- Regional authorities: `WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, `IOC`
- High-chaos actors: `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, `CRR`, `CTL`, `OKP`, `TRM`, `HGD`, `GHC`, `BON`, `HYR`, `BIR`, `SAO`

Source split:

- `generated_flags/` covers the ten regional authorities and the first eleven high-chaos actors.
- `missing_high_chaos_actor_assets/` covers `BON`, `HYR`, `BIR`, and `SAO`.

Historical flag/symbol candidates and confidence levels for old-seat dossier surfaces remain tracked separately in `docs/assets/012_africa/source_research/manifest.md`.

## Dynamic Union Cosmetic Flags

Dynamic cross-continent cosmetic identities are registered in `common/countries/cosmetic.txt` and localised in `localisation/english/chaosx_countries_l_english.yml`.

Live generated symbolic flags exist in root, medium, and small flag folders, with root DDS variants for the cosmetic identities. Source PNGs live under `docs/assets/012_africa/generated_flags/dynamic_union/source_png/`.

- `AFR_AFRICAN_MIDDLE_EASTERN_UNION`
- `AFR_AFRO_ASIAN_UNION`
- `AFR_AFRO_EURASIAN_UNION`
- `AFR_AFRO_ATLANTIC_UNION`
- `AFR_CONGRESS_OF_CONTINENTS`

## Blockers

- Generated art and icon package handoffs now exist under `docs/assets/012_africa/generated_art/` and `docs/assets/012_africa/icons_animation/`. This file remains the current record of which of those package assets were copied into live game folders and registered in `.gfx`.
