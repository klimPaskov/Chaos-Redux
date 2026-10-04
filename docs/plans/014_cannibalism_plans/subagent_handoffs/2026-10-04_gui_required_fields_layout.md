# Event 014 required-fields GUI layout handoff

Status: the parent approved the proposed composition and existing-asset scope on 2026-10-04. The layout and scripted-GUI binding diffs are concrete review-only proposals; no source changes were applied because the data writer has not yet delivered implementation source IDs.

The parent reviewed and approved the actual proposed reference images. Baseline production MCP inspect/render resolved all three exact windows, but its generated image bytes could not be retrieved for pixel review, so production-pixel acceptance remains open and mandatory post-application MCP review is still required.

## Event ownership and acceptance basis

Event id and slug: 014_cannibalism.

The canonical event entry point is chaosx.nr14.1 in events/014_cannibalism.txt:19.

The exact event-owned windows are cannibalism_network_window, cannibalism_warlord_command_window, and cannibalism_revealed_command_window in interface/014_cannibalism_frontline_hunger.gui.

Their exact bindings are cannibalism_network_scripted_gui, cannibalism_warlord_command_scripted_gui, and cannibalism_revealed_command_scripted_gui in common/scripted_guis/014_cannibalism_scripted_gui.txt.

The Network scripted GUI is player_context attached to top_bar; the Warlord and Revealed command GUIs are decision_category surfaces with their existing Event 014 route gates.

The dedicated categories are cannibalism_containment_category, cannibalism_network_alerts_category, cannibalism_warlord_command_category, and cannibalism_unified_command_category.

The Network opener is cannibalism_network_open in the Event 014 header; its existing scripted-GUI effect calls cannibalism_gui_open_network_view.

The source ownership headers, accepted Event 014 specification, category wiring, and event-specific visibility gates prove these are mechanic windows owned by Event 014.

The accepted requirement basis is the user-directed E014-FINAL-02/03 layout task and docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md, section 6, lines 570–613.

The parent’s 2026-10-04 approval accepts the two-column Network dossier plus selected identity card with all seven required fields, and the Overview/States and Overview/Loyalty compositions inside the existing three windows/assets. Source application remains with the parent after the data writer’s identifiers exist.

The shared event log, Event Details, settings, super-event framework, shared registries, Early window, Wendigo window, and all unrelated interfaces remain out of scope.

## Proposed references and files

The existing annotated baselines were reviewed directly at docs/plans/014_cannibalism_plans/2026-10-03_gui_required_fields_layout/evidence/network_required_fields_reference.png, warlord_required_fields_reference.png, and revealed_required_fields_reference.png.

The proposed Network reference is docs/plans/014_cannibalism_plans/2026-10-04_gui_required_fields_layout/evidence/proposed_network_dossier_reference.svg and its PNG preview.

The proposed Warlord/Revealed tab reference is docs/plans/014_cannibalism_plans/2026-10-04_gui_required_fields_layout/evidence/proposed_command_tabs_reference.svg and its PNG preview.

The references use the existing unmodified DDS-decoded background and card inputs under the 2026-10-03 evidence/reference_inputs folder; the outlined regions map to native elements and do not depict final button art or invented game values.

The source images visually reviewed are network_window_background.png, network_country_card.png, network_state_card.png, network_target_frame.png, warlord_command_background.png, controlled_state_card.png, revealed_command_background.png, warlord_loyalty_card.png, and continental_target_card.png in that reference_inputs folder.

The review-only native layout proposal is docs/plans/014_cannibalism_plans/2026-10-04_gui_required_fields_layout/evidence/proposed_gui_layouts.diff.

The review-only navigation, visibility, dynamic-list, and dirty-refresh proposal is docs/plans/014_cannibalism_plans/2026-10-04_gui_required_fields_layout/evidence/proposed_scripted_gui_bindings.diff.

The mapping, budgets, source precedents, and parent-owned dependencies are recorded in docs/plans/014_cannibalism_plans/2026-10-04_gui_required_fields_layout/evidence/layout_proposal_and_mapping.md.

The MCP inspect/render evidence and exact artifact retrieval blocker are recorded in docs/plans/014_cannibalism_plans/2026-10-04_gui_required_fields_layout/evidence/mcp_baseline_status.md.

Only those proposal, reference, evidence, and handoff documents were created; no game source or shared interface file was edited.

The files written are evidence/proposed_gui_layouts.diff, evidence/proposed_scripted_gui_bindings.diff, evidence/proposed_network_dossier_reference.svg, evidence/proposed_network_dossier_reference.png, evidence/proposed_command_tabs_reference.svg, evidence/proposed_command_tabs_reference.png, evidence/layout_proposal_and_mapping.md, evidence/mcp_baseline_status.md, and this subagent handoff under docs/plans/014_cannibalism_plans.

Both proposed diffs passed git apply --check against their current source files; this was a read-only patch-context check and did not apply either patch.

## Exact UI, entry, asset, and localisation identifiers

The Network surface remains cannibalism_network_window / cannibalism_network_scripted_gui, retaining the existing country/state arrays, tabs, selection controls, and selected target.

The proposed Network text elements use the data API plan’s proposed keys cannibalism.gui.network.node_type, cannibalism.gui.network.strength_band, cannibalism.gui.network.known_route, cannibalism.gui.network.last_incident, cannibalism.gui.network.counteraction, and cannibalism.gui.network.uncertainty, plus a concise per-node selection instruction.

The Warlord surface remains cannibalism_warlord_command_window / cannibalism_warlord_command_scripted_gui.

The proposed native list identifiers are cannibalism_controlled_state_dynamic_list and cannibalism_controlled_state_entry, with raid receipt key cannibalism.gui.raid_target. The accepted raid design is an enemy-front supply-node strike at 0.50 with an actual target receipt; the receipt writer is pending, so no raid target is shown until the receipt exists.

The Revealed surface remains cannibalism_revealed_command_window / cannibalism_revealed_command_scripted_gui.

The proposed list identifiers are cannibalism_loyalty_integrated_dynamic_list / cannibalism_loyalty_integrated_entry and cannibalism_loyalty_live_dynamic_list / cannibalism_loyalty_live_entry; the target card uses the existing key cannibalism.gui.continental_target and only a real committed campaign record.

The new button element identifiers are cannibalism_warlord_tab_overview, cannibalism_warlord_tab_states, cannibalism_revealed_tab_overview, and cannibalism_revealed_tab_loyalty.

The proposed button labels, tooltips, list headings, row text, and empty-selection message require parent-owned localisation in localisation/english/014_cannibalism_l_english.yml; no localisation keys were written. The accepted heading identifiers are cannibalism.gui.loyalty.integrated_heading and cannibalism.gui.loyalty.live_heading.

The proposed new localisation keys are cannibalism.gui.network.node_type, cannibalism.gui.network.strength_band, cannibalism.gui.network.known_route, cannibalism.gui.network.last_incident, cannibalism.gui.network.counteraction, cannibalism.gui.network.uncertainty, and cannibalism.gui.network.select_entry.

The remaining proposed keys are cannibalism.gui.controlled_state_entry, cannibalism.gui.raid_target, cannibalism.gui.raid_target.tt, cannibalism.gui.loyalty_integrated_entry, cannibalism.gui.loyalty_live_entry, cannibalism.gui.tab.overview, cannibalism.gui.tab.overview.tt, cannibalism.gui.tab.states, cannibalism.gui.tab.states.tt, cannibalism.gui.tab.loyalty, and cannibalism.gui.tab.loyalty.tt.

The proposal reuses the existing campaign target keys cannibalism.gui.continental_target and cannibalism.gui.continental_target.tt. Its card is 278x72 at local y304, ending at y376 inside the existing 380px window. Long real campaign names and target/date wrapping must be proven in the matched production render without truncation or clipping.

The existing entry decisions were read as ownership context only: Warlord actions include cannibalism_consume_controlled_state, cannibalism_raise_scavenger_warband, cannibalism_raise_feast_cohort, cannibalism_raise_origin_specialist, and cannibalism_raise_bone_guard; Revealed actions include cannibalism_unified_absorb_warlord and cannibalism_unified_issue_continental_command.

The inspected current March raid source has no target receipt, while the parent has since accepted a targeted enemy-front supply-node strike at 0.50 with receipt-pending implementation. Until that writer supplies the real receipt, the card must show a truthful pending/unassigned state; the selected controlled state is never presented as an operation target.

The exact owner effect cannibalism_begin_march_supply_raid_operation in common/scripted_effects/014_cannibalism_effects.txt:17331–17343 pays the operation costs and adds the timed modifier without storing a target pointer.

The Revealed API proposal supports one last committed campaign subject and date; it does not establish a multi-target campaign array.

The existing event assets are reused: GFX_cannibalism_network_window_background, GFX_cannibalism_network_country_card, GFX_cannibalism_network_state_card, GFX_cannibalism_network_target_frame, GFX_cannibalism_warlord_command_background, GFX_cannibalism_controlled_state_card, GFX_cannibalism_revealed_command_background, GFX_cannibalism_warlord_loyalty_card, and GFX_cannibalism_continental_target_card.

The existing animation families remain the Network threads and island alert, Warlord route emblem, critical-Larder glow and Frenzy border, and Revealed portrait, unification seal, and ordinary terminal frame.

Their existing sprite identifiers are GFX_cannibalism_network_threads_animated/static, GFX_cannibalism_island_alert_animated/static, GFX_cannibalism_selected_target_overlay_animated/static, GFX_cannibalism_warlord_route_emblem_animated/static, GFX_cannibalism_critical_larder_glow_animated/static, GFX_cannibalism_frenzy_border_animated/static, GFX_cannibalism_revealed_portrait_animated/static, GFX_cannibalism_revealed_portrait_frame, GFX_cannibalism_unification_seal_animated/static, and GFX_cannibalism_ordinary_terminal_frame_animated/static.

The parent’s GFX-only portrait comment change is committed as 3ab66fa0; current interface/014_cannibalism.gfx hash is f28d0ca3fffba23effa0b4aafd1d3c41d035407a002e99d5e77883bcf6099b4c and was not edited.

No asset production or GFX handoff is needed for these layout proposals.

## Before and proposed behavior

Before, the Network cards use 374×64 rows with only identity, type/stage, and strength; the existing selected-target card has no space for the four accepted additional fields.

The proposal retains the row affordance and gives the selected subject a separate full-width native detail panel for the remaining six fields, with identity in the existing selected-target card.

The panel is sized for three rows of two text fields at 16-pixel font; the last-incident and counteraction boxes allow two-line content, and no field is hidden behind a tooltip.

Before, the Warlord window has no space for both controlled-state identity cards and an honest raid-target card while its four existing value groups and animations remain visible.

The proposal adds an Overview/States view pair, moves the existing four status elements down 28 pixels to make room for the tab row, and uses the state-card region for two full controlled-state cards plus a separate actual raid-target card.

Before, the Revealed window’s loyalty card is an aggregate display, the continental target card has no consumer, and the target-card candidate intersects the seal and terminal-progress regions.

The proposal adds an Overview/Loyalty view pair, separates historical and live loyalty lists, places the existing target card at x184/y304, preserves the seal between the lists and target card, and gates the conflicting terminal-progress frame/text to Overview when eligible.

The portrait and all animation sprite families retain their existing assets; the proposal introduces no static substitute and no new gameplay action.

The proposed presentation-only page flags are cannibalism_warlord_gui_states_view and cannibalism_revealed_gui_loyalty_view; absence selects Overview. The parent must extend cannibalism_gui_clear_command_view and route/terminal cleanup to clear both flags.

Those flags describe only which informational page is open and must not become gameplay requirements, costs, AI facts, or route conditions.

The scripted-GUI binding diff binds both command contexts to cannibalism_command_gui_dirty. Each tab click sets or clears only its presentation flag and calls the accepted owner helper cannibalism_gui_rebuild_command_view, which owns array refresh and dirty increment. Network retains cannibalism_network_gui_dirty and its existing country/state selection effects; the selected identity card, six dossier fields, flag, and empty-selection prompt all use cannibalism_gui_validate_selected_network_target.

The Warlord list binds cannibalism_command_gui_state_entries / cannibalism_command_gui_state / cannibalism_command_gui_state_index with change_scope = yes and revalidates each state with is_controlled_by = ROOT. The historical loyalty list binds cannibalism_integrated_warlord_generation_entries / cannibalism_loyalty_generation / cannibalism_loyalty_index with change_scope = no and cannibalism_ui_integrated_row_valid. The live list binds cannibalism_command_gui_warlord_entries / cannibalism_loyalty_country / cannibalism_loyalty_country_index with change_scope = yes and cannibalism_ui_live_warlord_row_valid. These exact identifiers follow docs/plans/014_cannibalism_plans/2026-10-04_gui_data_implementation/evidence/owner_api_proposal.md and remain unapplied until implementation source IDs are ready.

The four active-tab image properties propose presentation-only selectors GetCannibalismWarlordOverviewTabSprite, GetCannibalismWarlordStatesTabSprite, GetCannibalismRevealedOverviewTabSprite, and GetCannibalismRevealedLoyaltyTabSprite, derived from the page flags using the existing Event 014 Network tab-selector pattern. Parent source/localisation work must define them; they are not data facts.

The Overview keeps the existing cannibalism.gui.warlord_loyalty summary and tooltip unchanged. The Loyalty tab uses the distinct approved keys cannibalism.gui.loyalty.integrated_heading and cannibalism.gui.loyalty.live_heading; neither heading overwrites the summary meaning.

## Visual budgets and checklist

The Warlord Overview stays at or below its current four simultaneous mechanic values; its States view displays identity records and one honest target status rather than adding a fifth meter.

The Revealed Overview keeps its existing value area; the Loyalty view phases those values out and displays the accepted history/live records and committed-target identity card.

The Network’s seven required per-node fields are treated as one dossier record, not as seven mechanic meters; no new numeric mechanic is added.

The only added controls are four native navigation tabs; they are not gameplay-changing actions and have no costs, AI equivalents, or cost texticons.

No displayed spendable cost or texticon is introduced; the cost-type count for the new presentation controls is zero.

The reference-to-native bounds, backgrounds, animations, state gating, and layout hierarchy are explicit in layout_proposal_and_mapping.md.

The reference images and visible-value/action/text-density/cost audits are complete for the proposed design.

Pixel alignment, clipping, overflow, z-order, text fit, state coherence, actual click regions, and background contrast are not accepted because the production MCP image artifacts were not readable.

The tab active-state appearance, selected/crowded list scrolling, long identity strings, two-line incident/counteraction text, empty lists, pre-reveal visibility, post-reveal visibility, and all resolution scaling remain unreviewed in production renders.

| Surface | Required matched scenarios after source application | Current evidence |
| --- | --- | --- |
| Network | Normal empty Domestic; selected country; selected state; empty category; crowded country/state lists; warning and stale uncertainty; longest real identity, incident, and counteraction; 1920×1080, 1366×768, and 2560×1440 | Exact-window normal empty-Domestic inspect/render only at 1920×1080 / scale 1; render artifacts unreadable |
| Warlord | Overview before Evolution II; Overview after Evolution II with all four existing values; States tab with empty, one-row, and crowded controlled-state lists; raid target unassigned; longest real state identity; 1920×1080, 1366×768, and 2560×1440 | Exact-window normal ID-only inspect/render only at 1920×1080 / scale 1; 9 unresolved inspector facts; render artifacts unreadable |
| Revealed | Hidden before reveal and visible after reveal; Overview with terminal progress ineligible/eligible; Loyalty tab with empty and crowded historical/live lists; no committed campaign and a real committed target; longest real identity; 1920×1080, 1366×768, and 2560×1440 | Exact-window post-reveal ID-only inspect/render only at 1920×1080 / scale 1; 7 unresolved inspector facts and existing animation/layout warnings; render artifacts unreadable |

## MCP and source evidence

The current Network inspect revision is 8af1d4503f6b19dd4dde62a440838470413fa4d5d186b5ee9547b51a7e9c6ef3; the current Revealed inspect revision is 257e17ae7e4121f612997faca28fed1030d67503ad3c8c58489124bf3cd5929f; the cached Warlord source hashes match current files as documented in mcp_baseline_status.md.

The current normal renders returned GUI_RENDERED for the three exact windows at 1920×1080 / scale 1 and produced full, cropped, annotated, hierarchy, click-region, source-map, scenario, fidelity, validation, and matrix artifacts.

The full/cropped/annotated/click-region image URIs and hashes are recorded in mcp_baseline_status.md.

The artifact template and byte-range route were verified, but read_mcp_resource failed for all three current full PNGs and for a manifest query with the exact error MCP error -32603: Artifact provenance manifest is unavailable.

Therefore the render production images could not be visually inspected, and source/render diagnostics are not treated as visual acceptance.

The 1366 and 2560 resolution matrix, non-normal states, matched before/after comparisons, and all post-change evidence remain pending until the data writer delivers implementation source IDs, the parent applies the proposal, and the production MCP artifacts are readable. Parent acceptance of the references does not waive that visual evidence.

Offline documentation read: Interface modding, Scrolling lines 110–128 and container bounds lines 83–109, revision b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c; Scripted GUI modding, Dynamic Lists lines 249–328, revision b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30.

Installed documentation read: common/scripted_guis/_documentation.md lines 78–105, revision 43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838.

Vanilla precedent inspected: game:interface/countryarmyview.gui lines 388–410, including item_grid at lines 400–407; source_lookup revision a516eeb4e2f730fe2bdf9f642d0cdb46b7b4ad731a432b9199b1e8957c88858b.

Source lookup confirmed the exact Network GUI container in interface/014_cannibalism_frontline_hunger.gui lines 51–110, revision 0623ac263c2c4c3e9d7e5251051118c3862d44206c2da439515e871420b0f1c4c.

The relevant skills read were chaos-redux-scripted-gui, chaos-redux-decisions-missions, chaos-redux-events, chaos-redux-event-assets, chaos-redux-frame-animation, and chaos-redux-subagents.

## Remaining parent work, blockers, and simplifications

The composition and reference images are parent-approved. Applying the diffs remains pending until the data writer delivers implemented source IDs and the parent applies/reconciles them.

The parent/data owner retains all observation writers, reader helpers, target receipts, integration history storage, view-state effects/triggers/properties, localisation, cleanup, costs, AI behavior, and final gameplay integration.

The shared worktree reports localisation/english/014_cannibalism_l_english.yml as modified; this worker did not edit that file and leaves its concurrent changes untouched.

The current inspected raid source still lacks the accepted enemy-front supply-node 0.50 target receipt; the parent-owned raid/data writer must supply that real receipt before the UI can identify a target. Until then the UI reports pending/unassigned and never reuses the selected controlled state.

The target card API currently supports one last committed continental campaign record; the parent must confirm that this satisfies the accepted plural target-card wording or supply real target-list data before implementation.

The loyalty localisation conflict is resolved: preserve cannibalism.gui.warlord_loyalty as the Overview summary and use the separate accepted integrated/live heading keys on the Loyalty tab.

The existing animation fallback/partial-render warnings are outside the granted GFX/assets scope and remain parent-owned findings; this worker did not alter the parent’s GFX comment or introduce animation fallback sprites.

The MCP artifact provenance manifest failure blocks required pixel review and any GUI visual-completion claim.

No gameplay feature was intentionally simplified in the proposed layout, but no source implementation, post-change comparison, or live in-game validation is claimed.

No source commit was made; the parent owns final application and commit after review.

The user’s live-game consumer validation remains pending after parent source application; it remains a user-owned step.

Skills used: chaos-redux-scripted-gui, chaos-redux-decisions-missions, chaos-redux-events, chaos-redux-event-assets, chaos-redux-frame-animation, and chaos-redux-subagents. No skill was created or updated.

## Parent reconciliation, 2026-10-04

Network part: `implemented` with these reconciliations, recorded in agent decision D5.
The dossier is a one-row native list on a dark `GFX_mini_bg` panel below the two lists instead of a separate six-text panel, the lists are 200 pixels high, the window uses an explicit centred position because `origo = center` clipped it in the production render, and production render evidence is in `2026-10-04_network_dossier_mcp_evidence.md`.
Warlord and Revealed parts: `accepted and queued` for their own items in the same remaining-work list.
