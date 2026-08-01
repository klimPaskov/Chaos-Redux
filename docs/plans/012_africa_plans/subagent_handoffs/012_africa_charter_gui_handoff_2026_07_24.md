# Event 012 Charter League GUI handoff

Status: implemented in the shared worktree and ready for parent review. This handoff covers only the decision-category Charter window surface, its scripted GUI bindings, the GUI localisation, and the reserved sprite registrations. No Event 012 action effects, AI weights, opinion logic, event targets, or binary art were changed.

## Files changed

- `common/scripted_guis/012_africa_charter_scripted_gui.txt`
- `interface/012_africa_charter.gui`
- `interface/012_africa_charter.gfx`
- `common/scripted_localisation/012_africa_charter_gui_scripted_localisation.txt`
- `localisation/english/012_africa_charter_gui_l_english.yml`
- `common/decisions/categories/012_africa_categories.txt`

The category attachment is the narrow `scripted_gui = africa_charter_window` line on `africa_charter_council_category`. The GUI remains visible only for a human Event 012 host and deliberately disables the scripted GUI for AI control.

## Surface and call-site map

`africa_charter_window` is a 1000x680 decision-category window with a header, member dossier column, regional congress/overlay column, and rival/diaspora/project/action column. It exposes the four primary values (`africa_charter_authority`, `africa_continental_reach`, `africa_integration_burden`, and `africa_colonial_pressure`), the secondary readiness/trust values, selected-member relationship and confidence, protection and clause flags, obligation/project counts, departure and rival pressure, regional overlap/corridor/restoration/settlement status, and active action/project caps.

Member buttons `africa_charter_member_1` through `africa_charter_member_5` consume only `africa_selected_targets^0` through `africa_selected_targets^4`. They clear and repopulate the existing one-entry `africa_selected_country_targets` cursor, set the existing country-target flag, and call `africa_refresh_selected_action_state_candidates` and `africa_refresh_selected_action_quote`.

State buttons `africa_charter_state_1` through `africa_charter_state_5` consume only `africa_selected_action_state_candidates^0` through `africa_selected_action_state_candidates^4`. Region-mode selections remain bounded by `constant:africa_action_capacity.maximum_region_state_targets`; non-region selections use the existing single-state clear path. All paths call `africa_refresh_selected_action_quote` and do not launch an action.

Family buttons set the existing temporary `africa_requested_action_family` and call `africa_select_action_family_page` for protection, accession, regional congress, integration, economy, diaspora, rival bloc, and high chaos. Costs, proof gates, execution, and AI behavior remain in the existing decision surface.

The nine overlay selectors set the host presentation cursor `africa_charter_gui_selected_overlay` from `constant:africa_overlay.*`. This is intentionally a presentation cursor and does not overwrite the live `africa_regional_overlay` value or perform an overlay action.

The compact diaspora selector groups are:

- `africa_selected_diaspora_origin_group`: north America, South America/Caribbean, Europe, and Indian Ocean, using `constant:africa_achievement_origin_group.*`.
- `africa_selected_diaspora_skill_programme`: education, medicine, engineering, and administration, using `constant:africa_achievement_skill_programme.*`.

Their buttons update host variables only. Scripted localisation displays the current selection in the diaspora panel. The parent agent will copy these host-scoped values into the immutable Action 52 and Action 54 payloads and apply the AI least-unrepresented choice in the action dispatcher.

## Helper, constants, and migration map

No new scripted effect or scripted trigger was introduced because the existing bounded cursor helpers already cover this surface: `africa_clear_selected_country_target`, `africa_refresh_selected_action_state_candidates`, `africa_refresh_selected_action_quote`, `africa_clear_selected_action_state_selection`, and `africa_select_action_family_page`. The new scripted-localisation names are presentation helpers only and have no gameplay side effects.

No new tuning table or script constant was needed. The GUI reuses the existing `africa_overlay`, `africa_action_family`, `africa_action_capacity.maximum_region_state_targets`, `africa_value`, `africa_achievement_origin_group`, and `africa_achievement_skill_programme` constants. This keeps the window aligned with the action dispatcher and avoids a second source of thresholds.

Migration is intentionally narrow: existing decision buttons continue to own action execution; member/state controls only migrate selection into the same arrays those decisions already consume; family controls only call the existing family-page selector; and the parent adds the two diaspora selector copies at the Action 52/54 payload boundary. No duplicated world scan or opinion logic was moved into the GUI.

## Scripted localisation and cleanup

`012_africa_charter_gui_scripted_localisation.txt` provides names for the constitution, overlay, selected relationship, protection, clauses, departure pressure, overlap, corridor, settlement, rival warning, action family, and the two diaspora selectors. Every player-facing key is in the UTF-8-with-BOM `012_africa_charter_gui_l_english.yml` file.

The GUI uses no new event targets. Member and state scope persistence is delegated to the existing bounded arrays and refresh effects. The overlay cursor is a host normal variable intended to live while the decision category is open; there is no category-close scripted GUI callback in the supported surface, so it is not cleared here. The Charter seal animates after League formation is complete, while the authority ring animates when Charter authority reaches the medium threshold. Their static fallbacks remain visible before those semantic states are met.

## Reserved sprite matrix

`interface/012_africa_charter.gfx` registers the exact matrix IDs and future runtime paths:

- `GFX_012_africa_charter_window_background` → `gfx/interface/012_africa/charter_window_background.dds`
- `GFX_012_africa_charter_header_plate` → `gfx/interface/012_africa/charter_header_plate.dds`
- `GFX_012_africa_member_card_frame` → `gfx/interface/012_africa/member_card_frame.dds`
- `GFX_012_africa_regional_card_frame` → `gfx/interface/012_africa/regional_card_frame.dds`
- `GFX_012_africa_relationship_badges` → `gfx/interface/012_africa/relationship_badges.dds`
- `GFX_012_africa_primary_value_icons` → `gfx/interface/012_africa/primary_value_icons.dds`
- `GFX_012_africa_secondary_value_icons` → `gfx/interface/012_africa/secondary_value_icons.dds`
- `GFX_012_africa_clause_tabs` → `gfx/interface/012_africa/clause_tabs.dds`
- `GFX_012_africa_regional_overlay_buttons` → `gfx/interface/012_africa/regional_overlay_buttons.dds`
- `GFX_012_africa_project_progress_frame` → `gfx/interface/012_africa/project_progress_frame.dds`
- `GFX_012_africa_rival_bloc_panel` → `gfx/interface/012_africa/rival_bloc_panel.dds`
- `GFX_012_africa_diaspora_summary_panel` → `gfx/interface/012_africa/diaspora_summary_panel.dds`
- `GFX_012_africa_charter_seal_activation_animated` → `gfx/interface/012_africa/animations/charter_seal_activation_sheet.dds` (8 frames, 8 fps, looping)
- `GFX_012_africa_charter_seal_activation_static` → `gfx/interface/012_africa/animations/charter_seal_activation_static.dds`
- `GFX_012_africa_charter_authority_ring_animated` → `gfx/interface/012_africa/animations/charter_authority_ring_sheet.dds` (10 frames, 6 fps, looping)
- `GFX_012_africa_charter_authority_ring_static` → `gfx/interface/012_africa/animations/charter_authority_ring_static.dds`

All sixteen Event 012 binary texture dependencies are absent from the worktree and remain queued for the separate asset handoff. No generic, vanilla, transparent, or fabricated image was substituted for the matrix. The existing `GFX_tiled_window_transparent` reference used by bounded overlay buttons is also reported missing by the offline validator; that is a pre-existing game-core texture diagnostic, not an Event 012 asset substitution.

## Validation evidence

Initial read-only inspection (before the window existed) recorded `GUI_WINDOW_MISSING` at artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2202a45af9a5971138c37d5739a2312fb9238eac880a51a0df5d81ce0b908b2/f8f38dd9f8f7e9c5152e68d93a6e71b0d00a17c90ea652e5f30e26dc62ffbab4/gui-inspect.75a201eeab03aaa9.json`.

After implementation and trigger-name correction, `hoi4_gui_inspect` returned `GUI_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87c6df359b35c412cb6d9e6c84c0263f73bb84420526d7c37a0e188215e6614b/b47b5f2c06bbb10d68135cf284ce14d5feab6014c67f2feec548bf62acd7c5e5/gui-inspect.5ebd58f5b7d83d78.json`. The previous unresolved references for animation, static fallback, and selected member visibility are gone from the returned diagnostics. The remaining inline errors are repository-wide invalid scripted GUI contexts and the pre-existing core transparent texture; the global source graph still reports 1883 blocking diagnostics and 40 visible-overlap diagnostics because the inspector scans the complete mod and intentionally layered controls.

`hoi4_gui_render` returned `GUI_RENDERED` with 24 artifacts for the normal, warning, long-text, and missing-localisation states at 1920x1080, 1366x768, and 2560x1440. Key artifacts are:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69a6155f13191e38d08af84a6d7c6ef6d6ca9fe07ca4d19960310a6e4220a8a7/bf6e3ce82abe208f22179169b114051e4022d7ecccafae87940b3ddbee07b82a/africa_charter_window-full.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/60cfc101e46c4b293109eaf3266ccf87e9fd2fba4f87f6b464c1306259492d83/dd35c19ee3d96218b06522ad1f078f421f04b646bf8d4bca669a7aedbe2aa250/africa_charter_window-state-matrix.png`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad82258dad94c56833baa6c0f6047d350fcb88b0e13afda9e936c627a6d282aa/34f03853d39c9bdbf77a0f4166a55865b3f8f23745a9cb1b9ebbb0998fbb7809/africa_charter_window-resolution-scale.png`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efc10551b5fdd2318f759dff923dbfb22661b6185ed9d0902ee3f13128a481f4/65d34f11a013c668340bb9452c8a1e0fa57d42a54a8500c5478ff9221e630356/africa_charter_window-state-matrix.json`

The render reports no click-bounds mismatch, invisible click blocker, conflicting click region, missing sprite, missing localisation, animation frame-count, animation sheet-dimension, static-fallback, parent-window, button-effect, button-trigger, cost, or AI-equivalent diagnostic for this surface. Offline fidelity is necessarily approximate for unavailable fonts, dynamic text, masked flags, and the queued DDS files.

Static checks found 63 GUI localisation references with no missing keys, no duplicate localisation keys, and a valid `EF BB BF` localisation BOM. No staged or committed changes were created; the parent agent owns final review and commit decisions.

## Follow-up

The asset producer should deliver the sixteen reserved DDS dependencies at the paths above and update the asset manifest without changing IDs. The parent should wire immutable diaspora selector copies into Actions 52 and 54, add AI least-unrepresented selection, and perform the final decision-category integration audit after those gameplay edits land.

## Release-candidate correction (2026-07-29)

The queued-texture paragraph is historical and is superseded by the current filesystem evidence. Twelve static Charter GUI textures and the two real frame-animation sheets with static fallbacks are present and registered in `interface/012_africa_charter.gfx`. Charter GUI animation/runtime acceptance remains in progress, and the earlier render evidence remains useful only as a prior audit record.
