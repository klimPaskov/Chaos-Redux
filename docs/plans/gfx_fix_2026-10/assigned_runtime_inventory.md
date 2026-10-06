# Final assigned graphics runtime inventory — 2026-10-06

This is the parent-requested current source and texture crosswalk for the assigned 70 plan rows. It records registrations and consumers; it does not claim whole-mod GUI, gameplay, or in-game completion. The detailed row-level paths, dimensions, frame counts, current whole-file and decoded-pixel hashes, direct consumer line hits, aliases, and retired replacements are in [assigned_runtime_inventory.json](assigned_runtime_inventory.json).

The source plan is `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` (SHA-256 `a7d534dca813e1bd8e9245f80db02fb54da5a76a548662950fcfbbfd4a3a46c3`), and the parent-owned initial coverage file is `docs/plans/gfx_fix_2026-10/evidence/initial_assigned_issue_coverage.json` (SHA-256 `208c8cc79946e2b99854286005614d086e9f72c38b786d66b5da8f590088022f`). All 70 coverage rows match the stored plan-row text. No source/runtime edits or commits were made for this review.

## Counts

The 70 original rows expand to 93 runtime slots after expanding the nine 015 categories and sixteen portrait aliases. Status is 60 implemented, 4 pending reserve disposition, and 6 retired. The live rows have 87 current target definitions across 87 unique DDS paths; the six 010/011 originals are absent by design.

There are 5 separately registered same-path aliases across 5 assigned paths. Alias counts are separate from unique texture paths. No missing live target textures, same-name GFX overrides, or duplicate decoded-pixel groups across distinct target paths were found.

| Group | Rows | Implemented | Pending | Retired | Current result |
|---|---:|---:|---:|---:|---|
| 001 | 13 | 13 | 0 | 0 | 13 report sprites are installed and event-consumed, including both newly completed photos. |
| 003 | 17 | 16 | 1 | 0 | The static lotus serves five decision rows; BoP, category, and report art are installed. The 003 report records five raw flag labels localized, and the old Dhyana strip remains a reserve. |
| 008 | 1 | 0 | 1 | 0 | Corrected news photo is registered as a reserve; current event pictures use the report sprite. |
| 010 | 4 | 0 | 0 | 4 | Four original registrations/textures are retired; active category uses a replacement alias. |
| 011 | 2 | 0 | 0 | 2 | Two original category registrations/textures are retired; categories use replacement aliases. |
| 013 | 18 | 17 | 1 | 0 | Fourteen report cards, two category pictures, and the restored damaged panel are installed; meteor icon remains a reserve. |
| 015 | 4 | 3 | 1 | 0 | Nine canonical category bindings and sixteen portraits are current; plural emblem remains a reserve. |
| 017 | 1 | 1 | 0 | 0 | Accepted v2 radio icon is installed at its active decision path. |
| 018 | 1 | 1 | 0 | 0 | Accepted deeper-test icon is installed at its active decision path. |
| 019 | 3 | 3 | 0 | 0 | Two focus badges and one decision icon match the accepted alpha review. |
| 020 | 6 | 6 | 0 | 0 | All six assigned rows are current; 60% fill pair and frame-source proof are documented. |

## Original-row map

The JSON carries the complete per-sprite crosswalk. Macro rows expand into exact current category and portrait registrations there.

| Row | Original plan sprite | Status | Current source evidence |
|---|---|---|---|
| 001-01 | `GFX_report_event_communist_worker_ritual` | implemented | `GFX_report_event_communist_worker_ritual`; 4 exact source consumer hits across current sprite set. |
| 001-02 | `GFX_report_event_communist_dark_worker_rituals` | implemented | `GFX_report_event_communist_dark_worker_rituals`; 1 exact source consumer hit across current sprite set. |
| 001-03 | `GFX_report_event_communist_control_escalates` | implemented | `GFX_report_event_communist_control_escalates`; 1 exact source consumer hit across current sprite set. |
| 001-04 | `GFX_report_event_communist_intervention_backfire` | implemented | `GFX_report_event_communist_intervention_backfire`; 1 exact source consumer hit across current sprite set. |
| 001-05 | `GFX_report_event_communist_war_warning` | implemented | `GFX_report_event_communist_war_warning`; 1 exact source consumer hit across current sprite set. |
| 001-06 | `GFX_report_event_communist_uprising` | implemented | `GFX_report_event_communist_uprising`; 1 exact source consumer hit across current sprite set. |
| 001-07 | `GFX_report_event_communist_unstable_activity` | implemented | `GFX_report_event_communist_unstable_activity`; 1 exact source consumer hit across current sprite set. |
| 001-08 | `GFX_report_event_communist_surprise_revolt` | implemented | `GFX_report_event_communist_surprise_revolt`; 3 exact source consumer hits across current sprite set. |
| 001-09 | `GFX_report_event_communist_state_control` | implemented | `GFX_report_event_communist_state_control`; 1 exact source consumer hit across current sprite set. |
| 001-10 | `GFX_report_event_communist_world_revolution_whispers` | implemented | `GFX_report_event_communist_world_revolution_whispers`; 1 exact source consumer hit across current sprite set. |
| 001-11 | `GFX_report_event_communist_world_revolution_foreshadowing` | implemented | `GFX_report_event_communist_world_revolution_foreshadowing`; 4 exact source consumer hits across current sprite set. |
| 001-12 | `GFX_report_event_communist_emergency_success` | implemented | `GFX_report_event_communist_emergency_success`; 1 exact source consumer hit across current sprite set. |
| 001-13 | `GFX_report_event_communist_insurgency_start` | implemented | `GFX_report_event_communist_insurgency_start`; 2 exact source consumer hits across current sprite set. |
| 003-01 | `GFX_decision_holy_realm_dhyana_seal_animated` | pending | `GFX_decision_holy_realm_dhyana_seal_animated`; Corrected registered reserve has no current consumer. |
| 003-02 | `GFX_decision_holy_realm_dhyana_seal` | implemented | `GFX_decision_holy_realm_dhyana_seal`; 5 exact source consumer hits across current sprite set. |
| 003-03 | `GFX_decision_holy_realm_power_one_becomes_many` | implemented | `GFX_decision_holy_realm_power_one_becomes_many`; 1 exact source consumer hit across current sprite set. |
| 003-04 | `GFX_decision_holy_realm_power_passing_through_walls` | implemented | `GFX_decision_holy_realm_power_passing_through_walls`; 1 exact source consumer hit across current sprite set. |
| 003-05 | `GFX_decision_holy_realm_power_walking_on_water` | implemented | `GFX_decision_holy_realm_power_walking_on_water`; 1 exact source consumer hit across current sprite set. |
| 003-06 | `GFX_decision_holy_realm_power_lotus_bridge` | implemented | `GFX_decision_holy_realm_power_lotus_bridge`; 1 exact source consumer hit across current sprite set. |
| 003-07 | `GFX_decision_holy_realm_power_vanishing_from_sight` | implemented | `GFX_decision_holy_realm_power_vanishing_from_sight`; 1 exact source consumer hit across current sprite set. |
| 003-08 | `GFX_decision_holy_realm_power_seated_in_sky` | implemented | `GFX_decision_holy_realm_power_seated_in_sky`; 1 exact source consumer hit across current sprite set. |
| 003-09 | `GFX_decision_holy_realm_power_touching_sun_moon` | implemented | `GFX_decision_holy_realm_power_touching_sun_moon`; 1 exact source consumer hit across current sprite set. |
| 003-10 | `GFX_decision_holy_realm_power_extinction_defilements` | implemented | `GFX_decision_holy_realm_power_extinction_defilements`; 1 exact source consumer hit across current sprite set. |
| 003-11 | `GFX_decision_holy_realm_dharma_teaching` | implemented | `GFX_decision_holy_realm_dharma_teaching`; 3 exact source consumer hits across current sprite set. |
| 003-12 | `GFX_bop_THR_vow_against_annihilation_side` | implemented | `GFX_bop_THR_vow_against_annihilation_side`; 1 exact source consumer hit across current sprite set. |
| 003-13 | `GFX_bop_THR_final_silence_side` | implemented | `GFX_bop_THR_final_silence_side`; 1 exact source consumer hit across current sprite set. |
| 003-14 | `GFX_decision_category_final_ledger` | implemented | `GFX_decision_category_final_ledger`; 1 exact source consumer hit across current sprite set. |
| 003-15 | `GFX_decision_category_holy_doctrine_balance` | implemented | `GFX_decision_category_holy_doctrine_balance`; 2 exact source consumer hits across current sprite set. |
| 003-16 | `GFX_report_event_holy_realm_arhat` | implemented | `GFX_report_event_holy_realm_arhat`; 4 exact source consumer hits across current sprite set. |
| 003-17 | `GFX_report_event_holy_realm_buddha` | implemented | `GFX_report_event_holy_realm_buddha`; 15 exact source consumer hits across current sprite set. |
| 008-01 | `GFX_news_event_tensions_red_line` | pending | `GFX_news_event_tensions_red_line`; Corrected registered reserve has no current consumer. |
| 010-01 | `GFX_decision_category_death_country` | retired | `GFX_decision_category_death_country`; Original definition removed; current replacement path is recorded in JSON. |
| 010-02 | `GFX_death_coastal_risk_pulse` | retired | `GFX_death_coastal_risk_pulse`; Original definition removed; current replacement path is recorded in JSON. |
| 010-03 | `GFX_death_wither_target_frame` | retired | `GFX_death_wither_target_frame`; Original definition removed; current replacement path is recorded in JSON. |
| 010-04 | `GFX_death_compact_warning_pulse` | retired | `GFX_death_compact_warning_pulse`; Original definition removed; current replacement path is recorded in JSON. |
| 011-01 | `GFX_decision_category_011_secret_alliance_foreign_interference` | retired | `GFX_decision_category_011_secret_alliance_foreign_interference`; Original definition removed; current replacement path is recorded in JSON. |
| 011-02 | `GFX_decision_category_011_secret_alliance_coalition_crisis` | retired | `GFX_decision_category_011_secret_alliance_coalition_crisis`; Original definition removed; current replacement path is recorded in JSON. |
| 013-01 | `GFX_decision_category_nd_meteor_storm_command` | pending | `GFX_decision_category_nd_meteor_storm_command`; Corrected registered reserve has no current consumer. |
| 013-02 | `GFX_report_event_nd_regional_aftermath` | implemented | `GFX_report_event_nd_regional_aftermath`; 5 exact source consumer hits across current sprite set. |
| 013-03 | `GFX_report_event_nd_tropical_cyclone` | implemented | `GFX_report_event_nd_tropical_cyclone`; 1 exact source consumer hit across current sprite set. |
| 013-04 | `GFX_report_event_nd_extreme_wind` | implemented | `GFX_report_event_nd_extreme_wind`; 1 exact source consumer hit across current sprite set. |
| 013-05 | `GFX_report_event_nd_tornado_outbreak` | implemented | `GFX_report_event_nd_tornado_outbreak`; 1 exact source consumer hit across current sprite set. |
| 013-06 | `GFX_report_event_nd_hailstorm` | implemented | `GFX_report_event_nd_hailstorm`; 1 exact source consumer hit across current sprite set. |
| 013-07 | `GFX_report_event_nd_extreme_cold_wave` | implemented | `GFX_report_event_nd_extreme_cold_wave`; 1 exact source consumer hit across current sprite set. |
| 013-08 | `GFX_report_event_nd_heat_wave` | implemented | `GFX_report_event_nd_heat_wave`; 1 exact source consumer hit across current sprite set. |
| 013-09 | `GFX_report_event_nd_wet_mass_movement` | implemented | `GFX_report_event_nd_wet_mass_movement`; 1 exact source consumer hit across current sprite set. |
| 013-10 | `GFX_report_event_nd_ashfall` | implemented | `GFX_report_event_nd_ashfall`; 1 exact source consumer hit across current sprite set. |
| 013-11 | `GFX_report_event_nd_lahar` | implemented | `GFX_report_event_nd_lahar`; 1 exact source consumer hit across current sprite set. |
| 013-12 | `GFX_report_event_nd_storm_surge` | implemented | `GFX_report_event_nd_storm_surge`; 1 exact source consumer hit across current sprite set. |
| 013-13 | `GFX_report_event_nd_meteor_impact` | implemented | `GFX_report_event_nd_meteor_impact`; 1 exact source consumer hit across current sprite set. |
| 013-14 | `GFX_report_event_nd_meteor_shower` | implemented | `GFX_report_event_nd_meteor_shower`; 1 exact source consumer hit across current sprite set. |
| 013-15 | `GFX_report_event_nd_massive_eruption` | implemented | `GFX_report_event_nd_massive_eruption`; 1 exact source consumer hit across current sprite set. |
| 013-16 | `GFX_decision_cat_picture_nd_winter` | implemented | `GFX_decision_cat_picture_nd_winter`; 2 exact source consumer hits across current sprite set. |
| 013-17 | `GFX_decision_cat_picture_nd_cyclone` | implemented | `GFX_decision_cat_picture_nd_cyclone`; 2 exact source consumer hits across current sprite set. |
| 013-18 | `GFX_013_abnormal_disaster_panel_damaged` | implemented | `GFX_013_abnormal_disaster_panel_damaged`; 1 exact source consumer hit across current sprite set. |
| 015-01 | `GFX_decision_category_utopia_league` | implemented | 9 runtime sprites: `GFX_decision_category_utopia_defense`, `GFX_decision_category_utopia_district`, …; 9 exact source consumer hits across current sprite set. |
| 015-02 | `GFX_utopia_manifesto_plural_compact_emblem` | pending | `GFX_utopia_manifesto_plural_compact_emblem`; Corrected registered reserve has no current consumer. |
| 015-03 | `GFX_goal_utopia_harbors` | implemented | `GFX_goal_utopia_harbors`; 1 exact source consumer hit across current sprite set. |
| 015-04 | `GFX_portrait_utopia_manifesto_interpreter_small` | implemented | 16 runtime sprites: `GFX_portrait_utopia_manifesto_advocate_of_limits_small`, `GFX_portrait_utopia_manifesto_chief_surveyor_small`, …; 16 exact source consumer hits across current sprite set. |
| 017-01 | `GFX_decision_random_faction_radio_networks` | implemented | `GFX_decision_random_faction_radio_networks`; 1 exact source consumer hit across current sprite set. |
| 018-01 | `GFX_decision_resources_found_deeper_test` | implemented | `GFX_decision_resources_found_deeper_test`; 1 exact source consumer hit across current sprite set. |
| 019-01 | `GFX_goal_infantry_spawn_derivative_zombie_scavenge_the_abandoned_barracks` | implemented | `GFX_goal_infantry_spawn_derivative_zombie_scavenge_the_abandoned_barracks`; 1 exact source consumer hit across current sprite set. |
| 019-02 | `GFX_goal_infantry_spawn_derivative_zombie_a_realm_of_base_dead` | implemented | `GFX_goal_infantry_spawn_derivative_zombie_a_realm_of_base_dead`; 1 exact source consumer hit across current sprite set. |
| 019-03 | `GFX_decision_infantry_spawn_prototype_cannibalization` | implemented | `GFX_decision_infantry_spawn_prototype_cannibalization`; 1 exact source consumer hit across current sprite set. |
| 020-01 | `GFX_black_plague_crisis_seal_animated` | implemented | `GFX_black_plague_crisis_seal_animated`; 1 exact source consumer hit across current sprite set. |
| 020-02 | `GFX_black_plague_rat_king_terminal_readiness_animated` | implemented | `GFX_black_plague_rat_king_terminal_readiness_animated`; 1 exact source consumer hit across current sprite set. |
| 020-03 | `GFX_black_plague_response_progress_fill` | implemented | `GFX_black_plague_response_progress_fill`; 5 exact source consumer hits across current sprite set. |
| 020-04 | `GFX_decision_black_plague_clean_city_rats` | implemented | `GFX_decision_black_plague_clean_city_rats`; 1 exact source consumer hit across current sprite set. |
| 020-05 | `GFX_goal_black_plague_rat_brood_signal` | implemented | `GFX_goal_black_plague_rat_brood_signal`; 13 exact source consumer hits across current sprite set. |
| 020-06 | `GFX_goal_black_plague_rat_king_the_royal_basin` | implemented | `GFX_goal_black_plague_rat_king_the_royal_basin`; 2 exact source consumer hits across current sprite set. |

## Parent-required 015, portraits, categories, and alpha checks

All 111 current 015 goal DDS files match the parent final-selection SHA-256, independent review SHA-256, and alpha-results output; dimensions match in all 111 cases. The independent reviewer accepted 114 rows total (111 for 015 and 3 for 019), with zero rejects and zero unlisted alpha deltas. Source alpha is byte-exact in 108 015 files; the three explicitly bounded cleanup exceptions are auditors, granaries, and measures. Their removal coordinates, intact main masks, and the rejected storehouse-trim comparison remain in the JSON.

The 111 paths have 222 registrations: one base and one same-path `_shine` alias per DDS. Source scanning finds 74 paths with direct consumers and 37 registered paths with none. The exact unconsumed rows and path/hash evidence are in `alias_and_orphan_audit.015_goal_unconsumed_registered_paths`; the separate token scan found no exact full-basename or dynamic-prefix consumer for them.

All 16 of 16 v2 advisor DDS hashes match the accepted runtime-install manifest and their current GFX names still appear in character aliases. All 9 canonical Utopia category sprites are referenced by their active category definitions. Nine older `GFX_decision_category_repair_utopia_*` registrations remain on distinct DDS paths without direct consumers.

## Current package hash crosschecks

| Package | Current paths checked | Matching hashes | Evidence |
|---|---:|---:|---|
| Event 001 selected new photos | 2 | 2 | `docs/assets/gfx_fix_reports_2026-10/notes/001_communism_spread/dds_validation.json` |
| Event 001 existing accepted package | 11 | 11 | `docs/assets/gfx_fix_reports_2026-10/notes/001_communism_spread/package_runtime_audit.json` |
| 13 accepted other-icon outputs | 13 | 13 | `docs/assets/gfx_fix_other_icons_resume/notes/runtime_validation.json` |
| Event 003 static icon package | 14 | 14 | `docs/assets/gfx_fix_holy_resume/evidence/dds_roundtrip_audit.json` |
| Event 013 report cards | 14 | 14 | `docs/assets/gfx_fix_reports_2026-10/notes/013_natural_disasters/dds_validation.json` |
| Event 013 category pictures | 2 | 2 | `docs/assets/gfx_fix_reports_2026-10/notes/013_natural_disasters/dds_validation.json` |
| 003 dynamic Mandala package | 14 | 14 | `docs/assets/003_holy_realm_buddhahood/release_animation_20261006/notes/runtime_promotion_report.json` |
| 013 damaged panel | 1 | 1 | `docs/plans/gfx_fix_2026-10/013_panel_handoff.md` |

## Resolved findings

| Finding | Current evidence |
|---|---|
| D003 — resolved_active_binding | All nine 015 category definitions now point to the canonical GFX_decision_category_utopia_* sprites and matching accepted 52x40 textures. |
| D006 — resolved | Both 003 BoP sprites now use dedicated accepted 72x88 runtime DDS files instead of focus-goal textures. |
| D007 — resolved | The 003 doctrine-balance category now points to its bespoke accepted 52x40 texture. |
| D008 — resolved | All thirteen 001 report-picture rows are installed and event-consumed, including communist_state_control and communist_insurgency_start. |
| D009 — resolved | All sixteen 015 advisor portraits are installed; current hashes match the accepted v2 runtime manifest and character aliases. |
| D010 — resolved_asset_selection | The 013 damaged panel currently hashes to the restored candidate and has matching synthetic baseline/post renders at 1920x1080 and 1366x768. |
| D011 — resolved_asset_package | All fourteen 013 report cards and both category pictures are accepted and installed at their existing paths. |
| D012 — resolved | The accepted 017 Radio Networks v2 DDS is installed at the existing 32x32 decision path. |
| D013 — resolved_asset_package | Assigned 003 static icons, report images, both BoP icons, and both bespoke category icons are accepted and currently registered. |

## Pending dispositions and actionable findings

Four accepted corrected sprites remain registered without source consumers because reserve-versus-retire decisions are unanswered: the original 003 1152x96 Dhyana strip, the 008 red-line news image, the 013 meteor-command icon, and the 015 plural emblem. Their active replacements and current hashes are recorded in the row data. No runtime changes were authorized.

Two additional findings need disposition. The nine superseded 015 repair aliases remain registered and unused after the canonical category rebind. Separately, 37 accepted 015 goal textures remain registered without direct source consumers; their image acceptance and hashes are intact. Keep or retire decisions remain open.

| Finding | Current state | Owner action |
|---|---|---|
| D001 — pending_disposition | The accepted 397x153 GFX_news_event_tensions_red_line is a corrected registered reserve with no current event, GUI, or picture-path consumer; current Event 008 event pictures use GFX_report_event_tensions_rising. | Choose whether to keep the corrected news sprite as a reserve or retire it; no runtime edit was authorized. |
| D002 — pending_disposition | Five 003 concentration decisions use the accepted 34x34 static GFX_decision_holy_realm_dhyana_seal. The original 1152x96, 12-frame animated sprite has no current consumer. | Choose reserve or retirement for the original animation strip; no separate live GUI consumer was identified. |
| D004 — pending_disposition | GFX_utopia_manifesto_plural_compact_emblem is a corrected, parent-accepted registered reserve without a visual consumer; the similarly named country flag is not a sprite consumer. | Choose whether to keep the corrected emblem as a reserve or retire it; no runtime edit was authorized. |
| D005 — pending_disposition | The accepted 53x40 GFX_decision_category_nd_meteor_storm_command is a registered reserve; the active Event 013 category uses GFX_decision_category_nd_recovery_overview with triggered pictures. | Choose whether to keep the meteor icon as a reserve or retire it; no runtime edit was authorized. |
| D014 — pending_alias_disposition | Nine GFX_decision_category_repair_utopia_* sprites and distinct DDS paths remain registered in interface/visual_consistency_repair.gfx after all nine live category files returned to canonical names. None has a current source consumer. | Decide whether the superseded repair alias set should remain reserved or be retired; no runtime/GFX edit was authorized. |
| D015 — pending_source_disposition | All 111 accepted 015 goal DDS paths match the final alpha review, but 37 registered paths have no current direct source consumer; each has a same-path _shine alias. | Review the exact unconsumed goal entries in alias_and_orphan_audit before any cleanup or wiring change; current alpha acceptance is unaffected. |

## MCP coverage limits

The 003 Mandala state sprites and scripted-localisation selection are installed, but the documented post-change GUI render timed out without artifacts; dynamic state selection remains unverified.

The 013 panel has matched synthetic baseline/post proof at 1920x1080 and 1366x768, and the current DDS hash matches the restored candidate. `gui_inspect` timed out after 600 seconds; the root human-player visibility fact and generic state coverage remain unresolved.

The 020 progress fill has a matching 60% before/after pair and supplemental 0%/100% post-only renders. The shared-board crisis-seal inspector timed out after 600 seconds, and the renderer did not select an animation frame (`selectedFrames={}` with `GUI_SPRITE_RENDER_PARTIAL` under `buttonstate_blendframes.lua`). Source-frame proof is valid, while motion at the 28.8px consumer size remains unverified.

No repository-wide MCP queries or in-game checks were run for this read-only source crosswalk.

## Package evidence

- [docs/plans/gfx_fix_2026-10/001_report.md](docs/plans/gfx_fix_2026-10/001_report.md)
- [docs/assets/gfx_fix_reports_2026-10/notes/001_communism_spread/package_runtime_audit.json](docs/assets/gfx_fix_reports_2026-10/notes/001_communism_spread/package_runtime_audit.json)
- [docs/assets/gfx_fix_reports_2026-10/notes/001_communism_spread/dds_validation.json](docs/assets/gfx_fix_reports_2026-10/notes/001_communism_spread/dds_validation.json)
- [docs/plans/gfx_fix_2026-10/003_report.md](docs/plans/gfx_fix_2026-10/003_report.md)
- [docs/plans/gfx_fix_2026-10/003_icons_handoff.md](docs/plans/gfx_fix_2026-10/003_icons_handoff.md)
- [docs/assets/gfx_fix_holy_resume/evidence/dds_roundtrip_audit.json](docs/assets/gfx_fix_holy_resume/evidence/dds_roundtrip_audit.json)
- [docs/assets/003_holy_realm_buddhahood/release_animation_20261006/notes/runtime_promotion_report.json](docs/assets/003_holy_realm_buddhahood/release_animation_20261006/notes/runtime_promotion_report.json)
- [docs/assets/003_holy_realm_buddhahood/release_animation_20261006/gfx_handoff.md](docs/assets/003_holy_realm_buddhahood/release_animation_20261006/gfx_handoff.md)
- [docs/plans/gfx_fix_2026-10/008_report.md](docs/plans/gfx_fix_2026-10/008_report.md)
- [docs/plans/gfx_fix_2026-10/010_report.md](docs/plans/gfx_fix_2026-10/010_report.md)
- [docs/plans/gfx_fix_2026-10/011_report.md](docs/plans/gfx_fix_2026-10/011_report.md)
- [docs/plans/gfx_fix_2026-10/013_report.md](docs/plans/gfx_fix_2026-10/013_report.md)
- [docs/plans/gfx_fix_2026-10/013_panel_handoff.md](docs/plans/gfx_fix_2026-10/013_panel_handoff.md)
- [docs/plans/gfx_fix_2026-10/015_report.md](docs/plans/gfx_fix_2026-10/015_report.md)
- [docs/plans/gfx_fix_2026-10/015_portraits_handoff.md](docs/plans/gfx_fix_2026-10/015_portraits_handoff.md)
- [docs/assets/gfx_fix_portraits_2026-10/metadata/runtime_install_validation.json](docs/assets/gfx_fix_portraits_2026-10/metadata/runtime_install_validation.json)
- [docs/plans/gfx_fix_2026-10/other_icons_handoff.md](docs/plans/gfx_fix_2026-10/other_icons_handoff.md)
- [docs/assets/gfx_fix_other_icons_resume/notes/runtime_validation.json](docs/assets/gfx_fix_other_icons_resume/notes/runtime_validation.json)
- [docs/plans/gfx_fix_2026-10/019_report.md](docs/plans/gfx_fix_2026-10/019_report.md)
- [docs/plans/gfx_fix_2026-10/020_report.md](docs/plans/gfx_fix_2026-10/020_report.md)
- [docs/plans/gfx_fix_2026-10/020_gui_handoff.md](docs/plans/gfx_fix_2026-10/020_gui_handoff.md)
- [docs/plans/gfx_fix_2026-10/alpha_independent_review.md](docs/plans/gfx_fix_2026-10/alpha_independent_review.md)
- [docs/assets/gfx_fix_alpha_review/alpha_independent_review_rows.json](docs/assets/gfx_fix_alpha_review/alpha_independent_review_rows.json)
- [docs/assets/gfx_fix_parent_2026-10/alpha_results.json](docs/assets/gfx_fix_parent_2026-10/alpha_results.json)
