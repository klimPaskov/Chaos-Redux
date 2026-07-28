# Event 019 Infantry Spawn GFX Handoff

This handoff records visual consumers and engine identifiers. The file `interface/019_infantry_spawn.gfx` contains sprite definitions only. It does not create or replace the sole Event 019 unit registry in `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`.

> **Regional flag approval (2026-07-18):** The current source/runtime chain is 91 unmodified full-flag ImageGen raws, 91 deterministic 820 by 520 spot masters, 273 native PNGs, and 273 bottom-left-origin runtime TGAs. The independent remediation re-audit is PASS and the final whole-event audit `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_completion_audit_2026_07_18.md` is PASS with P0/P1/P2 = 0. The machine JSON deliberately retains the literal processor status `candidate_requires_independent_visual_review`; this is a processor candidate-state field, superseded for approval by the separate PASS handoff and not edited. Parent workbook/catalog export and reconciliation are complete, Event 19 and SCN-013 now read `Fully Functional`, and package inventory verifies 33/33 current files. No closure gate remains. The older `regional_variants/` composites, 7/16 motif/composite notes, 7/16 validation/checksum pair, and 7/16 contact sheets are archival superseded evidence.

## Report sprites

| Sprite | Texture |
| --- | --- |
| `GFX_report_event_infantry_spawn` | `gfx/event_pictures/019_infantry_spawn/report_event_019_infantry_spawn_manifestation.dds` |
| `GFX_report_event_infantry_spawn_evolution_i` | `gfx/event_pictures/019_infantry_spawn/report_event_019_infantry_spawn_organized.dds` |
| `GFX_report_event_infantry_spawn_evolution_ii` | `gfx/event_pictures/019_infantry_spawn/report_event_019_infantry_spawn_arsenal.dds` |
| `GFX_report_event_infantry_spawn_evolution_iii` | `gfx/event_pictures/019_infantry_spawn/report_event_019_infantry_spawn_claimant.dds` |
| `GFX_report_event_infantry_spawn_evolution_iv` | `gfx/event_pictures/019_infantry_spawn/report_event_019_infantry_spawn_anomalous.dds` |
| `GFX_report_event_infantry_spawn_zombie_release` | `gfx/event_pictures/019_infantry_spawn/report_event_019_infantry_spawn_zombie_release.dds` |
| `GFX_report_event_infantry_spawn_zombie_defeat` | `gfx/event_pictures/019_infantry_spawn/report_event_019_infantry_spawn_zombie_defeat.dds` |
| `GFX_report_event_infantry_spawn_ghost_release` | `gfx/event_pictures/019_infantry_spawn/report_event_019_infantry_spawn_ghost_release.dds` |
| `GFX_report_event_infantry_spawn_ghost_defeat` | `gfx/event_pictures/019_infantry_spawn/report_event_019_infantry_spawn_ghost_defeat.dds` |
| `GFX_report_event_infantry_spawn_golem_release` | `gfx/event_pictures/019_infantry_spawn/report_event_019_infantry_spawn_golem_release.dds` |
| `GFX_report_event_infantry_spawn_golem_defeat` | `gfx/event_pictures/019_infantry_spawn/report_event_019_infantry_spawn_golem_defeat.dds` |

## Fixed portrait-slot army/host sprites

- `GFX_portrait_infantry_spawn_claimant_01` through `GFX_portrait_infantry_spawn_claimant_20` map to the same numbered files under `gfx/leaders/019_infantry_spawn/`. Each fixed slot now displays a distinct regional army/muster scene, not an individual claimant.
- The exact 27-row claimant, derivative, and technical-default source PNG, processed PNG, runtime DDS, sprite, source mode, dimensions, army/host identity contract, checksum, and validation record is `notes/claimant_portrait_asset_crosswalk_2026_07_16.md`.
- The linked 27-row retained reproduction specifications and per-output built-in ImageGen provenance are in `prompts/claimant_portrait_reproduction_specs_2026_07_16.md`. These are normalized reproduction specifications, not a claim that verbatim original submission strings survived.
- Profiles 04 and 12 are Asia/Australasia diaspora-compatible; profile 20 is Australia-only. The handoff defines no global, catch-all, or regionally mismatched fallback. Male-only gameplay names and leader metadata remain unchanged even though the art depicts forces rather than people.
- `GFX_portrait_infantry_spawn_zombie_host_commander` → `portrait_019_zombie_host_commander.dds`.
- `GFX_portrait_infantry_spawn_zombie_host_council` → `portrait_019_zombie_host_council.dds`.
- `GFX_portrait_infantry_spawn_ghost_host_commander` → `portrait_019_ghost_host_commander.dds`.
- `GFX_portrait_infantry_spawn_ghost_host_council` → `portrait_019_ghost_host_council.dds`.
- `GFX_portrait_infantry_spawn_golem_master_builder` → `portrait_019_golem_master_builder.dds`.
- `GFX_portrait_infantry_spawn_golem_pattern_council` → `portrait_019_golem_pattern_council.dds`.
- `GFX_portrait_infantry_spawn_unassigned_muster` → `portrait_019_unassigned_muster.dds`; this identity-neutral army scene initializes the Muster Board, covers unresolved technical selector states, and deliberately represents all four Event Log evolution-detail rows. It never substitutes a claimant or family profile.

Commander-labelled derivative slots show one collective massed host with no focal individual. Council-labelled derivative slots show exactly three formations or cohorts. All 27 visible scenes exclude an individual focal human/person; the `portrait` token is retained solely because filenames, sprite IDs, and GUI consumers are frozen compatibility interfaces.

The Event Log consumer is `common/scripted_guis/chaosx_scripted_gui_events_log.txt` (`events_log_evolution_details_portrait`), resolved through `GetEventsLogSelectedEvolutionPortrait` in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`. Event ID 19, evolution type 19, and stages 1 through 4 all select the identity-neutral muster scene before the shared unknown-image branch.

## Muster-board GUI sprites

| Sprite | Texture | Frames / use |
| --- | --- | --- |
| `GFX_infantry_spawn_muster_board_background` | `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds` | static 1120×760 |
| `GFX_infantry_spawn_muster_seal_animated` | `gfx/interface/019_infantry_spawn/muster_seal_pulse_sheet.dds` | 8 frames at 8 fps |
| `GFX_infantry_spawn_muster_seal_static` | `gfx/interface/019_infantry_spawn/muster_seal_pulse_static.dds` | fallback |
| `GFX_infantry_spawn_critical_command_border_animated` | `gfx/interface/019_infantry_spawn/critical_command_border_sheet.dds` | 8 frames at 6 fps |
| `GFX_infantry_spawn_critical_command_border_static` | `gfx/interface/019_infantry_spawn/critical_command_border_static.dds` | fallback |
| `GFX_infantry_spawn_anomalous_registry_emblem_animated` | `gfx/interface/019_infantry_spawn/anomalous_registry_emblem_sheet.dds` | 10 frames at 5 fps |
| `GFX_infantry_spawn_anomalous_registry_emblem_static` | `gfx/interface/019_infantry_spawn/anomalous_registry_emblem_static.dds` | fallback |

The current background composition is documented in `docs/assets/019_infantry_spawn/gui_background_rebuild_2026_07/`. It is deliberately restrained: a quiet charcoal/brass header band carries the title and tab controls, one broad uninterrupted paper field hosts the direct Event 19 surfaces, and one shallow lower band receives overview actions. The GUI owns all text, list rows, army scenes, and click targets without painting decorative wells or slot grids. The runtime sprite identifier and DDS path above remain stable.

### Animation runtime contract

| Package | Frame size | Frames | Horizontal sheet | FPS | Loop | Play on show |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `muster_seal_pulse` | 64 by 64 | 8 | 512 by 64 | 8 | yes | yes |
| `critical_command_border` | 156 by 210 | 8 | 1248 by 210 | 6 | yes | yes |
| `anomalous_registry_emblem` | 64 by 64 | 10 | 640 by 64 | 5 | yes | yes |

These values and the seven sprite identifiers above are the authoritative existing wiring in `interface/019_infantry_spawn.gfx`; `interface/019_infantry_spawn_muster_board.gui` consumes those same identifiers. The animation repair did not edit either runtime definition file.

### Animation source and continuity handoff

| Package | Frozen source atlas | Atlas SHA-256 | Identity lock | Processed validation |
| --- | --- | --- | --- | --- |
| `muster_seal_pulse` | `docs/assets/019_infantry_spawn/animations/muster_seal_pulse/source_atlas/muster_seal_pulse_animation_source_atlas.png` | `58456dfdbf1bf3e7a877bee6e178547f3bda5dffb3f7e856a188c5b165bccad1` | mount points, rivets, torn paper, wax disk, camera | 8 unique states; anchor deviation at most 0.455 px; nonzero-alpha silhouette IoU at least 0.8838 |
| `critical_command_border` | `docs/assets/019_infantry_spawn/animations/critical_command_border/source_atlas/critical_command_border_animation_source_atlas.png` | `4bbf16da40a7dddae4e16c8b9059609a8e415b6726b25946626c7f3d68d45246` | four rails, corner plates, rivets, open aperture, camera | 8 unique states; anchor deviation at most 0.438 px; nonzero-alpha silhouette IoU at least 0.9441; aperture alpha remains zero |
| `anomalous_registry_emblem` | `docs/assets/019_infantry_spawn/animations/anomalous_registry_emblem/source_atlas/anomalous_registry_emblem_animation_source_atlas.png` | `f634899a432dd8317412de13f8ae31cbf2e47c5d97f2c8e563ced6e1a8f4cd85` | brass perimeter, clasps, clamps, stone doors, ivory band, camera | 10 unique states; anchor deviation at most 0.495 px; nonzero-alpha silhouette IoU at least 0.9278 |

Each atlas was generated as retained animation source art with built-in ImageGen, not as a review contact sheet. The processor slices every cell row-major, removes chroma and disconnected atlas-edge debris, uses one shared scale and center anchor for the sequence, and builds the exact runtime sheet and static fallback. The package briefs and frame plans contain the prompt contracts, per-frame authored changes, complete source-frame hashes, and original-detail inspection findings. No animation package uses a transform-only, filter-only, or duplicated-frame fallback.

## Focus icons

Each listed base sprite has a same-texture `<sprite>_shine` definition in
`interface/019_infantry_spawn.gfx` with `effectFile = "gfx/FX/buttonstate.lua"`.
The 45 shine definitions require no duplicate texture files.

| Focus id | Sprite | Texture |
| --- | --- | --- |
| `infantry_spawn_derivative_hold_the_first_ground` | `GFX_goal_infantry_spawn_derivative_hold_the_first_ground` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_hold_the_first_ground.dds` |
| `infantry_spawn_derivative_count_the_surviving_host` | `GFX_goal_infantry_spawn_derivative_count_the_surviving_host` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_count_the_surviving_host.dds` |
| `infantry_spawn_derivative_inventory_the_seized_districts` | `GFX_goal_infantry_spawn_derivative_inventory_the_seized_districts` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_inventory_the_seized_districts.dds` |
| `infantry_spawn_derivative_restore_a_chain_of_orders` | `GFX_goal_infantry_spawn_derivative_restore_a_chain_of_orders` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_restore_a_chain_of_orders.dds` |
| `infantry_spawn_derivative_name_the_future_host` | `GFX_goal_infantry_spawn_derivative_name_the_future_host` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_name_the_future_host.dds` |
| `infantry_spawn_derivative_mark_the_muster_depots` | `GFX_goal_infantry_spawn_derivative_mark_the_muster_depots` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_mark_the_muster_depots.dds` |
| `infantry_spawn_derivative_reopen_captured_workshops` | `GFX_goal_infantry_spawn_derivative_reopen_captured_workshops` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_reopen_captured_workshops.dds` |
| `infantry_spawn_derivative_open_the_living_corridor` | `GFX_goal_infantry_spawn_derivative_open_the_living_corridor` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_open_the_living_corridor.dds` |
| `infantry_spawn_derivative_count_every_obligation` | `GFX_goal_infantry_spawn_derivative_count_every_obligation` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_count_every_obligation.dds` |
| `infantry_spawn_derivative_crown_the_claimant` | `GFX_goal_infantry_spawn_derivative_crown_the_claimant` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_crown_the_claimant.dds` |
| `infantry_spawn_derivative_assign_command_estates` | `GFX_goal_infantry_spawn_derivative_assign_command_estates` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_assign_command_estates.dds` |
| `infantry_spawn_derivative_one_voice_over_the_host` | `GFX_goal_infantry_spawn_derivative_one_voice_over_the_host` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_one_voice_over_the_host.dds` |
| `infantry_spawn_derivative_convene_the_host_council` | `GFX_goal_infantry_spawn_derivative_convene_the_host_council` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_convene_the_host_council.dds` |
| `infantry_spawn_derivative_bind_the_district_councils` | `GFX_goal_infantry_spawn_derivative_bind_the_district_councils` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_bind_the_district_councils.dds` |
| `infantry_spawn_derivative_no_host_abandoned` | `GFX_goal_infantry_spawn_derivative_no_host_abandoned` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_no_host_abandoned.dds` |
| `infantry_spawn_derivative_obey_the_family_instinct` | `GFX_goal_infantry_spawn_derivative_obey_the_family_instinct` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_obey_the_family_instinct.dds` |
| `infantry_spawn_derivative_mark_the_family_domain` | `GFX_goal_infantry_spawn_derivative_mark_the_family_domain` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_mark_the_family_domain.dds` |
| `infantry_spawn_derivative_end_the_old_chain_of_rule` | `GFX_goal_infantry_spawn_derivative_end_the_old_chain_of_rule` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_end_the_old_chain_of_rule.dds` |
| `infantry_spawn_derivative_quiet_the_fragmented_columns` | `GFX_goal_infantry_spawn_derivative_quiet_the_fragmented_columns` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_quiet_the_fragmented_columns.dds` |
| `infantry_spawn_derivative_outlast_the_former_state` | `GFX_goal_infantry_spawn_derivative_outlast_the_former_state` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_outlast_the_former_state.dds` |
| `infantry_spawn_derivative_make_an_army_of_the_host` | `GFX_goal_infantry_spawn_derivative_make_an_army_of_the_host` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_make_an_army_of_the_host.dds` |
| `infantry_spawn_derivative_concentrate_the_host` | `GFX_goal_infantry_spawn_derivative_concentrate_the_host` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_concentrate_the_host.dds` |
| `infantry_spawn_derivative_scatter_the_bands` | `GFX_goal_infantry_spawn_derivative_scatter_the_bands` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_scatter_the_bands.dds` |
| `infantry_spawn_derivative_arm_the_captured_auxiliaries` | `GFX_goal_infantry_spawn_derivative_arm_the_captured_auxiliaries` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_arm_the_captured_auxiliaries.dds` |
| `infantry_spawn_derivative_a_method_fit_for_the_host` | `GFX_goal_infantry_spawn_derivative_a_method_fit_for_the_host` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_a_method_fit_for_the_host.dds` |
| `infantry_spawn_derivative_read_the_neighboring_frontiers` | `GFX_goal_infantry_spawn_derivative_read_the_neighboring_frontiers` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_read_the_neighboring_frontiers.dds` |
| `infantry_spawn_derivative_issue_the_submission_terms` | `GFX_goal_infantry_spawn_derivative_issue_the_submission_terms` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_issue_the_submission_terms.dds` |
| `infantry_spawn_derivative_absorb_the_conquered_districts` | `GFX_goal_infantry_spawn_derivative_absorb_the_conquered_districts` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_absorb_the_conquered_districts.dds` |
| `infantry_spawn_derivative_turn_the_host_outward` | `GFX_goal_infantry_spawn_derivative_turn_the_host_outward` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_turn_the_host_outward.dds` |
| `infantry_spawn_derivative_become_the_regional_predator` | `GFX_goal_infantry_spawn_derivative_become_the_regional_predator` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_become_the_regional_predator.dds` |
| `infantry_spawn_derivative_zombie_scavenge_the_abandoned_barracks` | `GFX_goal_infantry_spawn_derivative_zombie_scavenge_the_abandoned_barracks` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_zombie_scavenge_the_abandoned_barracks.dds` |
| `infantry_spawn_derivative_zombie_number_the_devouring_bands` | `GFX_goal_infantry_spawn_derivative_zombie_number_the_devouring_bands` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_zombie_number_the_devouring_bands.dds` |
| `infantry_spawn_derivative_zombie_teach_the_base_dead_to_muster` | `GFX_goal_infantry_spawn_derivative_zombie_teach_the_base_dead_to_muster` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_zombie_teach_the_base_dead_to_muster.dds` |
| `infantry_spawn_derivative_zombie_keep_the_hunger_in_column` | `GFX_goal_infantry_spawn_derivative_zombie_keep_the_hunger_in_column` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_zombie_keep_the_hunger_in_column.dds` |
| `infantry_spawn_derivative_zombie_a_realm_of_base_dead` | `GFX_goal_infantry_spawn_derivative_zombie_a_realm_of_base_dead` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_zombie_a_realm_of_base_dead.dds` |
| `infantry_spawn_derivative_ghost_mark_the_first_anchors` | `GFX_goal_infantry_spawn_derivative_ghost_mark_the_first_anchors` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_ghost_mark_the_first_anchors.dds` |
| `infantry_spawn_derivative_ghost_call_a_second_procession` | `GFX_goal_infantry_spawn_derivative_ghost_call_a_second_procession` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_ghost_call_a_second_procession.dds` |
| `infantry_spawn_derivative_ghost_bind_the_procession_to_place` | `GFX_goal_infantry_spawn_derivative_ghost_bind_the_procession_to_place` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_ghost_bind_the_procession_to_place.dds` |
| `infantry_spawn_derivative_ghost_thin_the_hunger_for_life` | `GFX_goal_infantry_spawn_derivative_ghost_thin_the_hunger_for_life` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_ghost_thin_the_hunger_for_life.dds` |
| `infantry_spawn_derivative_ghost_a_pale_dominion` | `GFX_goal_infantry_spawn_derivative_ghost_a_pale_dominion` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_ghost_a_pale_dominion.dds` |
| `infantry_spawn_derivative_golem_recover_the_broken_coal` | `GFX_goal_infantry_spawn_derivative_golem_recover_the_broken_coal` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_golem_recover_the_broken_coal.dds` |
| `infantry_spawn_derivative_golem_reconstruct_the_binding_marks` | `GFX_goal_infantry_spawn_derivative_golem_reconstruct_the_binding_marks` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_golem_reconstruct_the_binding_marks.dds` |
| `infantry_spawn_derivative_golem_turn_workshops_into_foundries` | `GFX_goal_infantry_spawn_derivative_golem_turn_workshops_into_foundries` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_golem_turn_workshops_into_foundries.dds` |
| `infantry_spawn_derivative_golem_share_the_living_pattern` | `GFX_goal_infantry_spawn_derivative_golem_share_the_living_pattern` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_golem_share_the_living_pattern.dds` |
| `infantry_spawn_derivative_golem_a_march_of_living_stone` | `GFX_goal_infantry_spawn_derivative_golem_a_march_of_living_stone` | `gfx/interface/goals/019_infantry_spawn/infantry_spawn_derivative_golem_a_march_of_living_stone.dds` |

## Decision and mission consumers

| Consumer id | Sprite | Texture concept |
| --- | --- | --- |
| `infantry_spawn_open_muster_board` | `GFX_decision_infantry_spawn_board_open` | `gfx/interface/decisions/019_infantry_spawn/board_open.dds` |
| `infantry_spawn_select_next_ordinary_lot` | `GFX_decision_infantry_spawn_lot_cycle` | `gfx/interface/decisions/019_infantry_spawn/lot_cycle.dds` |
| `infantry_spawn_audit_selected_lot` | `GFX_decision_infantry_spawn_audit` | `gfx/interface/decisions/019_infantry_spawn/audit.dds` |
| `infantry_spawn_assign_territorial_roles` | `GFX_decision_infantry_spawn_territorial_roles` | `gfx/interface/decisions/019_infantry_spawn/territorial_roles.dds` |
| `infantry_spawn_open_standardization_cycle` | `GFX_decision_infantry_spawn_standardization` | `gfx/interface/decisions/019_infantry_spawn/standardization.dds` |
| `infantry_spawn_supervised_demobilization` | `GFX_decision_infantry_spawn_demobilization` | `gfx/interface/decisions/019_infantry_spawn/demobilization.dds` |
| `infantry_spawn_emergency_field_integration` | `GFX_decision_infantry_spawn_emergency_integration` | `gfx/interface/decisions/019_infantry_spawn/emergency_integration.dds` |
| `infantry_spawn_establish_muster_districts` | `GFX_decision_infantry_spawn_muster_district` | `gfx/interface/decisions/019_infantry_spawn/muster_district.dds` |
| `infantry_spawn_appoint_integration_staff` | `GFX_decision_infantry_spawn_integration_staff` | `gfx/interface/decisions/019_infantry_spawn/integration_staff.dds` |
| `infantry_spawn_issue_common_tables` | `GFX_decision_infantry_spawn_standardization` | `gfx/interface/decisions/019_infantry_spawn/standardization.dds` |
| `infantry_spawn_preserve_specialist_companies` | `GFX_decision_infantry_spawn_specialist_preservation` | `gfx/interface/decisions/019_infantry_spawn/specialist_preservation.dds` |
| `infantry_spawn_preserve_prototype_formation` | `GFX_decision_infantry_spawn_prototype_preservation` | `gfx/interface/decisions/019_infantry_spawn/prototype_preservation.dds` |
| `infantry_spawn_cannibalize_advanced_lot` | `GFX_decision_infantry_spawn_prototype_cannibalization` | `gfx/interface/decisions/019_infantry_spawn/prototype_cannibalization.dds` |
| `infantry_spawn_recognize_emergency_reserve` | `GFX_decision_infantry_spawn_emergency_reserve` | `gfx/interface/decisions/019_infantry_spawn/emergency_reserve.dds` |
| `infantry_spawn_survey_formation_lots` | `GFX_decision_infantry_spawn_audit` | `gfx/interface/decisions/019_infantry_spawn/audit.dds` |
| `infantry_spawn_open_training_cycle` | `GFX_decision_infantry_spawn_training_cycle` | `gfx/interface/decisions/019_infantry_spawn/training_cycle.dds` |
| `infantry_spawn_reserve_rail_corridors` | `GFX_decision_infantry_spawn_rail_corridor` | `gfx/interface/decisions/019_infantry_spawn/rail_corridor.dds` |
| `infantry_spawn_request_field_reinforcement` | `GFX_decision_infantry_spawn_request_field` | `gfx/interface/decisions/019_infantry_spawn/request_field.dds` |
| `infantry_spawn_request_mobile_reserve` | `GFX_decision_infantry_spawn_request_mobile` | `gfx/interface/decisions/019_infantry_spawn/request_mobile.dds` |
| `infantry_spawn_request_territorial_defenders` | `GFX_decision_infantry_spawn_request_territorial` | `gfx/interface/decisions/019_infantry_spawn/request_territorial.dds` |
| `infantry_spawn_request_specialist_firepower` | `GFX_decision_infantry_spawn_request_firepower` | `gfx/interface/decisions/019_infantry_spawn/request_firepower.dds` |
| `infantry_spawn_request_numbers` | `GFX_decision_infantry_spawn_request_numbers` | `gfx/interface/decisions/019_infantry_spawn/request_numbers.dds` |
| `infantry_spawn_request_discipline` | `GFX_decision_infantry_spawn_request_discipline` | `gfx/interface/decisions/019_infantry_spawn/request_discipline.dds` |
| `infantry_spawn_request_firepower` | `GFX_decision_infantry_spawn_request_firepower` | `gfx/interface/decisions/019_infantry_spawn/request_firepower.dds` |
| `infantry_spawn_request_mobility` | `GFX_decision_infantry_spawn_request_mobile` | `gfx/interface/decisions/019_infantry_spawn/request_mobile.dds` |
| `infantry_spawn_request_anything` | `GFX_decision_infantry_spawn_request_anything` | `gfx/interface/decisions/019_infantry_spawn/request_anything.dds` |
| `infantry_spawn_request_selected_anomalous_family` | `GFX_decision_infantry_spawn_request_anomalous` | `gfx/interface/decisions/019_infantry_spawn/request_anomalous.dds` |
| `infantry_spawn_open_selected_family_cantonment_decision` | `GFX_decision_infantry_spawn_cantonment` | `gfx/interface/decisions/019_infantry_spawn/cantonment.dds` |
| `infantry_spawn_appoint_selected_family_liaison_decision` | `GFX_decision_infantry_spawn_liaison` | `gfx/interface/decisions/019_infantry_spawn/liaison.dds` |
| `infantry_spawn_restrict_selected_family_deployment_decision` | `GFX_decision_infantry_spawn_restricted_deployment` | `gfx/interface/decisions/019_infantry_spawn/restricted_deployment.dds` |
| `infantry_spawn_sustain_selected_family_decision` | `GFX_decision_infantry_spawn_family_sustainment` | `gfx/interface/decisions/019_infantry_spawn/family_sustainment.dds` |
| `infantry_spawn_seal_selected_family_breach_decision` | `GFX_decision_infantry_spawn_breach_sealing` | `gfx/interface/decisions/019_infantry_spawn/breach_sealing.dds` |
| `infantry_spawn_disperse_selected_anomalous_lot_decision` | `GFX_decision_infantry_spawn_anomalous_disperse` | `gfx/interface/decisions/019_infantry_spawn/anomalous_disperse.dds` |
| `infantry_spawn_formation_roll_call_mission` | `GFX_decision_infantry_spawn_audit` | `gfx/interface/decisions/019_infantry_spawn/audit.dds` |
| `infantry_spawn_standardization_cycle_mission` | `GFX_decision_infantry_spawn_standardization` | `gfx/interface/decisions/019_infantry_spawn/standardization.dds` |
| `infantry_spawn_supervised_demobilization_mission` | `GFX_decision_infantry_spawn_demobilization` | `gfx/interface/decisions/019_infantry_spawn/demobilization.dds` |
| `infantry_spawn_training_cycle_mission` | `GFX_decision_infantry_spawn_training_cycle` | `gfx/interface/decisions/019_infantry_spawn/training_cycle.dds` |
| `infantry_spawn_muster_districts_mission` | `GFX_decision_infantry_spawn_muster_district` | `gfx/interface/decisions/019_infantry_spawn/muster_district.dds` |
| `infantry_spawn_officer_search_mission` | `GFX_decision_infantry_spawn_integration_staff` | `gfx/interface/decisions/019_infantry_spawn/integration_staff.dds` |
| `infantry_spawn_specialist_preservation_mission` | `GFX_decision_infantry_spawn_specialist_preservation` | `gfx/interface/decisions/019_infantry_spawn/specialist_preservation.dds` |
| `infantry_spawn_prototype_maintenance_trial_mission` | `GFX_decision_infantry_spawn_prototype_preservation` | `gfx/interface/decisions/019_infantry_spawn/prototype_preservation.dds` |
| `infantry_spawn_rail_corridor_mission` | `GFX_decision_infantry_spawn_rail_corridor` | `gfx/interface/decisions/019_infantry_spawn/rail_corridor.dds` |
| `infantry_spawn_request_cooldown_mission` | `GFX_decision_infantry_spawn_request_cooldown` | `gfx/interface/019_infantry_spawn/cooldown_marker.dds` |
| `infantry_spawn_recognize_claimant` | `GFX_decision_infantry_spawn_claimant_recognize` | `gfx/interface/decisions/019_infantry_spawn/claimant_recognize.dds` |
| `infantry_spawn_accept_claimant_demand` | `GFX_decision_infantry_spawn_claimant_accept` | `gfx/interface/decisions/019_infantry_spawn/claimant_accept.dds` |
| `infantry_spawn_refuse_claimant_demand` | `GFX_decision_infantry_spawn_claimant_refuse` | `gfx/interface/decisions/019_infantry_spawn/claimant_refuse.dds` |
| `infantry_spawn_counter_command_claimant` | `GFX_decision_infantry_spawn_claimant_counter_command` | `gfx/interface/decisions/019_infantry_spawn/claimant_counter_command.dds` |
| `infantry_spawn_discredit_claimant` | `GFX_decision_infantry_spawn_claimant_discredit` | `gfx/interface/decisions/019_infantry_spawn/claimant_discredit.dds` |
| `infantry_spawn_arrest_claimant` | `GFX_decision_infantry_spawn_claimant_arrest` | `gfx/interface/decisions/019_infantry_spawn/claimant_arrest.dds` |
| `infantry_spawn_derivative_secure_muster_depot_decision` | `GFX_decision_infantry_spawn_derivative_sustainment_site` | `gfx/interface/decisions/019_infantry_spawn/derivative_sustainment_site.dds` |
| `infantry_spawn_derivative_authorize_base_zombie_training_decision` | `GFX_decision_infantry_spawn_derivative_zombie_training` | `gfx/interface/decisions/019_infantry_spawn/derivative_zombie_training.dds` |
| `infantry_spawn_derivative_rally_zombie_band_decision` | `GFX_decision_infantry_spawn_derivative_zombie_rally` | `gfx/interface/decisions/019_infantry_spawn/derivative_zombie_rally.dds` |
| `infantry_spawn_derivative_manifest_ghost_host_decision` | `GFX_decision_infantry_spawn_derivative_ghost_manifest` | `gfx/interface/decisions/019_infantry_spawn/derivative_ghost_manifest.dds` |
| `infantry_spawn_derivative_bind_golem_host_decision` | `GFX_decision_infantry_spawn_derivative_golem_bind` | `gfx/interface/decisions/019_infantry_spawn/derivative_golem_bind.dds` |
| `infantry_spawn_derivative_pay_family_sustainment_decision` | `GFX_decision_infantry_spawn_family_sustainment` | `gfx/interface/decisions/019_infantry_spawn/family_sustainment.dds` |
| `infantry_spawn_derivative_establish_sustainment_site_decision` | `GFX_decision_infantry_spawn_derivative_sustainment_site` | `gfx/interface/decisions/019_infantry_spawn/derivative_sustainment_site.dds` |
| `infantry_spawn_derivative_integrate_conquered_district_decision` | `GFX_decision_infantry_spawn_derivative_integrate_district` | `gfx/interface/decisions/019_infantry_spawn/derivative_integrate_district.dds` |
| `infantry_spawn_derivative_integrate_conquered_district_mission` | `GFX_decision_infantry_spawn_derivative_integrate_district` | `gfx/interface/decisions/019_infantry_spawn/derivative_integrate_district.dds` |
| `infantry_spawn_derivative_suppress_fragmentation_decision` | `GFX_decision_infantry_spawn_derivative_suppress_fragmentation` | `gfx/interface/decisions/019_infantry_spawn/derivative_suppress_fragmentation.dds` |
| `infantry_spawn_derivative_break_former_parent_command_net_decision` | `GFX_decision_infantry_spawn_derivative_break_command_net` | `gfx/interface/decisions/019_infantry_spawn/derivative_break_command_net.dds` |
| `infantry_spawn_derivative_demand_local_submission_decision` | `GFX_decision_infantry_spawn_derivative_demand_submission` | `gfx/interface/decisions/019_infantry_spawn/derivative_demand_submission.dds` |
| `infantry_spawn_derivative_submission_warning_mission` | `GFX_decision_infantry_spawn_derivative_demand_submission` | `gfx/interface/decisions/019_infantry_spawn/derivative_demand_submission.dds` |
| `infantry_spawn_derivative_preserve_claimant_decision` | `GFX_decision_infantry_spawn_derivative_preserve_claimant` | `gfx/interface/decisions/019_infantry_spawn/derivative_preserve_claimant.dds` |
| `infantry_spawn_derivative_replace_claimant_decision` | `GFX_decision_infantry_spawn_derivative_replace_claimant` | `gfx/interface/decisions/019_infantry_spawn/derivative_replace_claimant.dds` |
| `infantry_spawn_derivative_survive_former_parent_front` | `GFX_decision_infantry_spawn_derivative_survive_front` | `gfx/interface/decisions/019_infantry_spawn/derivative_survive_front.dds` |

## Decision categories

| Category | Sprite | Texture |
| --- | --- | --- |
| `infantry_spawn_formation_management_category` | `GFX_decision_category_infantry_spawn_formation_management` | `gfx/interface/019_infantry_spawn/formation_management_category.dds` |
| `infantry_spawn_claimant_category` | `GFX_decision_category_infantry_spawn_claimants` | `gfx/interface/019_infantry_spawn/claimant_command_category.dds` |
| `infantry_spawn_derivative_operations_category` | `GFX_decision_category_infantry_spawn_derivative_operations` | `gfx/interface/019_infantry_spawn/derivative_operations_category.dds` |

## Idea picture tokens

| Picture token | Sprite | Texture |
| --- | --- | --- |
| `infantry_spawn_muster_control` | `GFX_idea_infantry_spawn_muster_control` | `gfx/interface/ideas/019_infantry_spawn/infantry_spawn_muster_control.dds` |
| `infantry_spawn_army_congestion` | `GFX_idea_infantry_spawn_army_congestion` | `gfx/interface/ideas/019_infantry_spawn/infantry_spawn_army_congestion.dds` |
| `infantry_spawn_claimant_command` | `GFX_idea_infantry_spawn_claimant_command` | `gfx/interface/ideas/019_infantry_spawn/infantry_spawn_claimant_command.dds` |
| `infantry_spawn_anomalous_saturation` | `GFX_idea_infantry_spawn_anomalous_saturation` | `gfx/interface/ideas/019_infantry_spawn/infantry_spawn_anomalous_saturation.dds` |
| `infantry_spawn_supply_strain` | `GFX_idea_infantry_spawn_supply_strain` | `gfx/interface/ideas/019_infantry_spawn/infantry_spawn_supply_strain.dds` |
| `infantry_spawn_command_confusion` | `GFX_idea_infantry_spawn_command_confusion` | `gfx/interface/ideas/019_infantry_spawn/infantry_spawn_command_confusion.dds` |
| `infantry_spawn_training_saturation` | `GFX_idea_infantry_spawn_training_saturation` | `gfx/interface/ideas/019_infantry_spawn/infantry_spawn_training_saturation.dds` |
| `infantry_spawn_equipment_debt` | `GFX_idea_infantry_spawn_equipment_debt` | `gfx/interface/ideas/019_infantry_spawn/infantry_spawn_equipment_debt.dds` |
| `infantry_spawn_family_registry` | `GFX_idea_infantry_spawn_family_registry` | `gfx/interface/ideas/019_infantry_spawn/infantry_spawn_family_registry.dds` |

## Muster-board state markers

| Sprite | Texture |
| --- | --- |
| `GFX_infantry_spawn_formation_quality_marker` | `gfx/interface/019_infantry_spawn/formation_quality_marker.dds` |
| `GFX_infantry_spawn_formation_coherence_marker` | `gfx/interface/019_infantry_spawn/formation_coherence_marker.dds` |
| `GFX_infantry_spawn_dynamic_cost_marker` | `gfx/interface/019_infantry_spawn/dynamic_cost_marker.dds` |
| `GFX_infantry_spawn_warning_marker` | `gfx/interface/019_infantry_spawn/warning_marker.dds` |
| `GFX_infantry_spawn_cooldown_marker` | `gfx/interface/019_infantry_spawn/cooldown_marker.dds` |
| `GFX_infantry_spawn_invalid_target_marker` | `gfx/interface/019_infantry_spawn/invalid_target_marker.dds` |

## Cosmetic flags and localisation

| Cosmetic tag | Display name | Runtime files |
| --- | --- | --- |
| `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY` | Claimant's Muster | `gfx/flags/INFANTRY_SPAWN_CLAIMANT_BREAKAWAY.tga`, `gfx/flags/medium/INFANTRY_SPAWN_CLAIMANT_BREAKAWAY.tga`, `gfx/flags/small/INFANTRY_SPAWN_CLAIMANT_BREAKAWAY.tga` |
| `INFANTRY_SPAWN_ZOMBIE_BASE` | Unbidden Dead Host | `gfx/flags/INFANTRY_SPAWN_ZOMBIE_BASE.tga`, `gfx/flags/medium/INFANTRY_SPAWN_ZOMBIE_BASE.tga`, `gfx/flags/small/INFANTRY_SPAWN_ZOMBIE_BASE.tga` |
| `INFANTRY_SPAWN_ZOMBIE_CLAIMANT` | Command of the Devouring Bands | `gfx/flags/INFANTRY_SPAWN_ZOMBIE_CLAIMANT.tga`, `gfx/flags/medium/INFANTRY_SPAWN_ZOMBIE_CLAIMANT.tga`, `gfx/flags/small/INFANTRY_SPAWN_ZOMBIE_CLAIMANT.tga` |
| `INFANTRY_SPAWN_ZOMBIE_COLLECTIVE` | Council of Devouring Bands | `gfx/flags/INFANTRY_SPAWN_ZOMBIE_COLLECTIVE.tga`, `gfx/flags/medium/INFANTRY_SPAWN_ZOMBIE_COLLECTIVE.tga`, `gfx/flags/small/INFANTRY_SPAWN_ZOMBIE_COLLECTIVE.tga` |
| `INFANTRY_SPAWN_ZOMBIE_SPECIES` | Realm of the Base Dead | `gfx/flags/INFANTRY_SPAWN_ZOMBIE_SPECIES.tga`, `gfx/flags/medium/INFANTRY_SPAWN_ZOMBIE_SPECIES.tga`, `gfx/flags/small/INFANTRY_SPAWN_ZOMBIE_SPECIES.tga` |
| `INFANTRY_SPAWN_GHOST_BASE` | Unanchored Procession | `gfx/flags/INFANTRY_SPAWN_GHOST_BASE.tga`, `gfx/flags/medium/INFANTRY_SPAWN_GHOST_BASE.tga`, `gfx/flags/small/INFANTRY_SPAWN_GHOST_BASE.tga` |
| `INFANTRY_SPAWN_GHOST_CLAIMANT` | Commanded Pale Host | `gfx/flags/INFANTRY_SPAWN_GHOST_CLAIMANT.tga`, `gfx/flags/medium/INFANTRY_SPAWN_GHOST_CLAIMANT.tga`, `gfx/flags/small/INFANTRY_SPAWN_GHOST_CLAIMANT.tga` |
| `INFANTRY_SPAWN_GHOST_COLLECTIVE` | Chorus of Anchors | `gfx/flags/INFANTRY_SPAWN_GHOST_COLLECTIVE.tga`, `gfx/flags/medium/INFANTRY_SPAWN_GHOST_COLLECTIVE.tga`, `gfx/flags/small/INFANTRY_SPAWN_GHOST_COLLECTIVE.tga` |
| `INFANTRY_SPAWN_GHOST_SPECIES` | Pale Dominion | `gfx/flags/INFANTRY_SPAWN_GHOST_SPECIES.tga`, `gfx/flags/medium/INFANTRY_SPAWN_GHOST_SPECIES.tga`, `gfx/flags/small/INFANTRY_SPAWN_GHOST_SPECIES.tga` |
| `INFANTRY_SPAWN_GOLEM_BASE` | Broken Pattern Host | `gfx/flags/INFANTRY_SPAWN_GOLEM_BASE.tga`, `gfx/flags/medium/INFANTRY_SPAWN_GOLEM_BASE.tga`, `gfx/flags/small/INFANTRY_SPAWN_GOLEM_BASE.tga` |
| `INFANTRY_SPAWN_GOLEM_CLAIMANT` | Master-Bound March | `gfx/flags/INFANTRY_SPAWN_GOLEM_CLAIMANT.tga`, `gfx/flags/medium/INFANTRY_SPAWN_GOLEM_CLAIMANT.tga`, `gfx/flags/small/INFANTRY_SPAWN_GOLEM_CLAIMANT.tga` |
| `INFANTRY_SPAWN_GOLEM_COLLECTIVE` | Council of Living Patterns | `gfx/flags/INFANTRY_SPAWN_GOLEM_COLLECTIVE.tga`, `gfx/flags/medium/INFANTRY_SPAWN_GOLEM_COLLECTIVE.tga`, `gfx/flags/small/INFANTRY_SPAWN_GOLEM_COLLECTIVE.tga` |
| `INFANTRY_SPAWN_GOLEM_SPECIES` | March of Living Stone | `gfx/flags/INFANTRY_SPAWN_GOLEM_SPECIES.tga`, `gfx/flags/medium/INFANTRY_SPAWN_GOLEM_SPECIES.tga`, `gfx/flags/small/INFANTRY_SPAWN_GOLEM_SPECIES.tga` |

These thirteen un-suffixed files remain the identity precedents and non-regional compatibility flags. The current region-aware candidate uses the same thirteen identity stems with the suffixes `EUROPE`, `MIDDLE_EAST`, `AFRICA`, `ASIA`, `AUSTRALIA`, `NORTH_AMERICA`, and `SOUTH_AMERICA`:

```text
INFANTRY_SPAWN_<IDENTITY>_<REGION>
gfx/flags/INFANTRY_SPAWN_<IDENTITY>_<REGION>.tga
gfx/flags/medium/INFANTRY_SPAWN_<IDENTITY>_<REGION>.tga
gfx/flags/small/INFANTRY_SPAWN_<IDENTITY>_<REGION>.tga
```

This is exactly 91 regional cosmetic tags and 273 runtime TGA files. Flags are filename-driven and require no `.gfx` sprite or cosmetic-tag registry file. Every regional tag has `TAG`, `TAG_DEF`, `TAG_ADJ`, and ideology aliases in the existing UTF-8-BOM Event 19 localisation file, `localisation/english/019_infrantry_spawn_l_english.yml`. The main implementation owns regional classification and `set_cosmetic_tag` timing; the current dynamic assignment builds `INFANTRY_SPAWN_[IDENTITY]_[REGION]`. The raw, spot-master, processed PNG, and runtime evidence is owned by `regional_flag_validation_2026_07_18.json` and `regional_flag_checksums_2026_07_18.sha256`.

## Achievement files

Achievement art is filename-driven for the achievement loader. Each ID has completed, grey, and not-eligible files under `gfx/achievements/`, and all 33 textures are also registered as `GFX_achievement_<achievement_id>{,_grey,_not_eligible}` in the shared `interface/chaosx_achievements.gfx` for explicit wiring and reuse.

- `019_infantry_spawn_every_rifle_accounted_for{,_grey,_not_eligible}.dds`
- `019_infantry_spawn_one_battalion_wonder{,_grey,_not_eligible}.dds`
- `019_infantry_spawn_the_army_has_voted{,_grey,_not_eligible}.dds`
- `019_infantry_spawn_order_from_noise{,_grey,_not_eligible}.dds`
- `019_infantry_spawn_combined_arms_accident{,_grey,_not_eligible}.dds`
- `019_infantry_spawn_no_room_on_the_train{,_grey,_not_eligible}.dds`
- `019_infantry_spawn_borrowed_future{,_grey,_not_eligible}.dds`
- `019_infantry_spawn_three_false_apocalypses{,_grey,_not_eligible}.dds`
- `019_infantry_spawn_barracks_of_babel{,_grey,_not_eligible}.dds`
- `019_infantry_spawn_quiet_demobilisation{,_grey,_not_eligible}.dds`
- `019_infantry_spawn_every_barracks_a_front{,_grey,_not_eligible}.dds`

## Validation ownership

The 7/18 regional flag tranche is reproduced and validated with this exact
recorded invocation from the repository root:

```powershell
& "C:/Program Files/Python39/python.exe" -B docs/assets/019_infantry_spawn/_tooling/process_event_019_regional_flags.py --palette-colours 8 --master-width 820 --master-height 520 --hue-bins 16 --neutral-saturation 64 --dark-value 48 --minimum-colour-share 0.0005 --run-date 2026-07-18
```

The processor SHA-256 is `d87e879184d5a28a52736b80af4bc0ce70abd9744de47210b1f6a7c3db15ece6`. Evidence paths are `docs/assets/019_infantry_spawn/regional_flag_validation_2026_07_18.json` and `docs/assets/019_infantry_spawn/regional_flag_checksums_2026_07_18.sha256`. The validator status remains the immutable literal `candidate_requires_independent_visual_review` processor-state value. Approval is supplied by the separate PASS handoff `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`, which clears the regional asset gate. Do not rewrite the JSON or infer approval from that field alone.
