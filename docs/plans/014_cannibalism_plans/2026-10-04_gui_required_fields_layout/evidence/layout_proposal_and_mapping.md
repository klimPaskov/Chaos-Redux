# Event 014 required-fields GUI layout proposal

Disposition: the parent accepted the proposed composition and existing-asset scope on 2026-10-04; both source diffs remain review-only and unapplied until the data owner’s implemented source IDs are ready.

Acceptance basis: the parent explicitly approved the two-column Network dossier plus selected identity card with seven required fields, and the Overview/States and Overview/Loyalty tab compositions within the three existing Event 014 windows and assets on 2026-10-04. The accepted requirements remain bounded by docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md, section 6, lines 570–613.

The existing 2026-10-03 annotated references were reviewed directly and remain the design basis; the new references show only the proposed corrections and preserve the existing backgrounds and hierarchy.

The event-owned surfaces are cannibalism_network_window / cannibalism_network_scripted_gui, cannibalism_warlord_command_window / cannibalism_warlord_command_scripted_gui, and cannibalism_revealed_command_window / cannibalism_revealed_command_scripted_gui in interface/014_cannibalism_frontline_hunger.gui and common/scripted_guis/014_cannibalism_scripted_gui.txt.

The entry point is chaosx.nr14.1 in events/014_cannibalism.txt; the dedicated decision categories are cannibalism_containment_category, cannibalism_network_alerts_category, cannibalism_warlord_command_category, and cannibalism_unified_command_category.

The Network scripted GUI is player_context, attached to top_bar; the Warlord and Revealed command GUIs are decision_category surfaces gated to their Event 014 route states.

The shared event log, Event Details, settings, super-event framework, shared registries, Early window, Wendigo window, and all unrelated GUI surfaces remain out of scope.

## Proposed composition

Network keeps its title, five category tabs, sort/refresh/close controls, paired country/state columns, and existing full-row selection controls.

Each Network list retains two full 374×64 rows in a 128-pixel viewport, with scrolling for additional rows.

Selecting an existing country or state row exposes a 102-pixel native dossier pane below the lists and keeps the existing selected-target card as the identity row.

The identity row plus six separate native text boxes expose all seven required fields: identity, node type, strength band, known route, last incident, selected counteraction, and uncertainty.

When nothing is selected, the dossier pane can state the clear per-node action, “Select a country or state to inspect its observed details”; it does not show fabricated values or a fake selected subject.

The proposed Network scroll control uses the vanilla right_vertical_slider precedent because the baseline diagnostics name clipping on right_vertical_slider_intel; production image and click-region review remain required after the parent applies the accepted proposal.

Warlord adds Overview and States tabs beneath the title, shifting the four existing value groups down 28 pixels while preserving the 470×340 window and every existing animation position.

The Warlord States tab shows a scrollable list of actually controlled states using cannibalism_controlled_state_dynamic_list and the existing GFX_cannibalism_controlled_state_card; the separate raid card reads only the owner’s real raid-target record.

The accepted raid design is an enemy-front supply-node strike at 0.50 with an actual operation-target receipt; that target-writing code is pending, so the card must remain explicitly pending or unassigned until the real receipt exists. A selected controlled state is never presented as the raid target.

Revealed adds Overview and Loyalty tabs below the portrait. Overview retains the current portrait, global meters, loyalty summary slot, and eligible terminal-progress slot.

The Loyalty tab displays separate historical-integrated and surviving-live lists from the data API’s distinct arrays, plus one card for the last committed continental campaign target or an explicit empty result.

The existing unification seal remains in its current position between the lists and target card; portrait and seal art are unchanged.

The terminal-progress frame and text are visible on Overview when eligible and hidden on Loyalty, so they do not overlap the campaign card.

The parent presentation triggers show the Network dossier fields only for a valid existing selected country/state pointer and show the per-node prompt when no valid pointer exists.

The Warlord States tab hides cannibalism_larder_meter/value, cannibalism_frenzy_meter/value, cannibalism_alignment_meter/value, cannibalism_controlled_state_card, and cannibalism_warlord_capacity; the Overview tab hides the state-list panel and raid card.

The Revealed Loyalty tab hides cannibalism_global_larder_meter/value, cannibalism_global_network_meter/value, cannibalism_warlord_loyalty_card/text, cannibalism_ordinary_terminal_frame_animated/static, and cannibalism_terminal_progress_text; the Overview tab hides the new loyalty lists and continental-target card.

The Overview keeps the existing cannibalism.gui.warlord_loyalty summary and tooltip unchanged. The Loyalty tab uses the distinct approved semantic heading keys cannibalism.gui.loyalty.integrated_heading and cannibalism.gui.loyalty.live_heading; neither heading overwrites the Overview summary meaning.

## Reference-to-native mapping

| Reference region | Native elements and bounds | Content / interaction | Existing asset and state |
| --- | --- | --- | --- |
| Network country and state columns | Existing list panels at local x18 and x431, y290, each 394×128; existing grid rows remain 374×64 | Existing full-row selection controls select an actual country/state record; scrolling stays native | Existing country/state card sprites and top-bar player_context |
| Network selected identity | Existing target frame at local x243, y530, 374×64, with existing flag and text children | Actual selected subject identity; the existing selection effect remains information-only | Existing target frame and selection overlay, selected pointer validated by parent data API |
| Network dossier | New native tiled panel at local x18, y422, 807×102; six two-column, three-row instantTextBoxType cells | Node type, strength band, known route, uncertainty, last incident, and actual counteraction/status; no numeric mechanic meter | Existing vanilla GFX_tiled_window_transparent; selected record state only |
| Warlord tabs | Two native buttonType bounds at local x18/x126, y48, 100×29 | Overview and States navigation only; parent supplies active styling and presentation-only tab state | Existing GFX_sort_button_100x29; no gameplay effects |
| Warlord controlled-state list | Native clipped/scrollable panel at local x18, y82, 296×146, with 278×72 rows | Actual controlled state name, stage, and supported state record; rows are informational | Existing controlled-state card and native scrollbar |
| Warlord raid card | Existing controlled-state-card art reused at local x20, y232, 278×72 | Real operation target if available; otherwise explicit unassigned state | Existing GFX_cannibalism_controlled_state_card; no target is fabricated |
| Revealed tabs | Two native buttonType bounds at local x18/x104, y268, each scaled from the existing 100×29 button | Overview and Loyalty navigation only; parent supplies active styling and presentation-only tab state | Existing GFX_sort_button_100x29; no gameplay effects |
| Revealed historical loyalty list | Native heading and clipped list at local x184, y54–148, 278px wide; 260×72 row viewport | Historical identity from the accepted aligned integration receipt list | Existing dark native tiled panel; change_scope = no per data API |
| Revealed live loyalty list | Native heading and clipped list at local x184, y150–228, 278px wide; 260×58 row viewport | Existing live warlord identity, disposition, and pending response | Existing dark native tiled panel; change_scope = yes per data API |
| Revealed campaign card | Existing continental target card at local x184, y304, 278×72; its bottom edge is y376 inside the existing 380px window | Actual committed campaign target and date, or explicit no-target state; no pre-click target is inferred | Existing GFX_cannibalism_continental_target_card |
| Revealed portrait and seal | Existing portrait at x20,y54 and unification seal at x356,y234 | Portrait and seal remain visible and in place; terminal progress remains on Overview when eligible | Existing portrait, seal, and terminal animation families |

The binding proposal uses the exact proposed readers, row-valid triggers, list arrays, values, indices, scope behavior, and rebuild helper in docs/plans/014_cannibalism_plans/2026-10-04_gui_data_implementation/evidence/owner_api_proposal.md; it does not invent an independent gameplay fact.

The proposed presentation-only page flags are cannibalism_warlord_gui_states_view and cannibalism_revealed_gui_loyalty_view; absence selects Overview. The parent must extend cannibalism_gui_clear_command_view and route/terminal cleanup to clear both flags.

Those flags describe only which informational page is open and must not become gameplay requirements, costs, AI facts, or route conditions.

The review-only binding diff proposes the exact flag effects, exclusive visibility triggers, active-tab properties, dynamic lists, and dirty refresh calls. The parent must wire overview defaults and extend cannibalism_gui_clear_command_view to clear both presentation-only page flags.

## Content and action budgets

The Warlord Overview stays at or below its current four simultaneous mechanic values, while the States tab shows identity records and one truthful raid-target card without adding a meter.

The Revealed Overview retains the existing value placements; the Loyalty tab contains identity records and a committed-target identity card rather than a second metric dump.

The Network dossier is one selected node record with seven required fields, split across native text cells; long incident and counteraction fields receive two lines at the existing 16-pixel font.

The new tab controls are navigation only, and the state/loyalty cards are informational; they have no costs, gameplay effects, AI actions, or texticon requirements.

No displayed spendable cost or cost-type count is introduced.

The network row hitboxes remain the current full 374×64 row buttons; the proposed cards and list entries do not add click regions.

The active-tab look must follow the existing Event 014 Network tab sprite-selector pattern, with matched post-change hit-region review; the wireframe reference outlines are annotations, not fake controls.

## Parent-owned dependencies and unresolved design points

The exact proposed binding diff is evidence/proposed_scripted_gui_bindings.diff. It wires Network selected-record validation to all six dossier fields and the empty-selection prompt; Warlord page state and controlled-state list; and Revealed page state with separate historical/live loyalty arrays.

The parent data/API owner must provide the exact localization values for the six network detail fields, controlled-state rows, raid target, historical/live loyalty rows, and campaign target card.

The parent raid/data owner must write the accepted enemy-front supply-node 0.50 strike receipt before the UI can show a real raid target; until then the target getter must return pending/unassigned, never the selected controlled state.

The Revealed data API proposes one last committed campaign record; if the accepted requirement means a multi-target campaign list, that requires parent reconciliation with actual target arrays before applying this layout.

The loyalty-key conflict is resolved: preserve cannibalism.gui.warlord_loyalty as the Overview summary, and use cannibalism.gui.loyalty.integrated_heading plus cannibalism.gui.loyalty.live_heading for the two Loyalty lists.

The four tab buttons are new presentation controls. The proposed image getters GetCannibalismWarlordOverviewTabSprite, GetCannibalismWarlordStatesTabSprite, GetCannibalismRevealedOverviewTabSprite, and GetCannibalismRevealedLoyaltyTabSprite are presentation-only derived selectors modeled on the existing Event 014 Network tab selectors; the parent must define them from the page flags and existing selected/default sort-button sprites. No decision, mission, target, payment, probability, or route effect is added here.

The campaign card remains 278×72 at y304, ending at y376 within the existing 380px window. Long real campaign names and wrapped target/date text remain a mandatory matched MCP render check; the proposed 16px text box must not truncate or clip them.

No background, frame, icon, portrait, DDS, GFX registration, localisation file, decision, event, scripted effect, trigger, constant, or workbook is changed by this proposal.

## Engine and vanilla adaptation

The dynamic rows use native gridBoxType, explicit pixel bounds, clipped containers with a background, and vertical scrollbars, following offline Interface modding and Scripted GUI modding.

The exact vanilla precedent is the item_grid scroll container in game:interface/countryarmyview.gui, lines 388–410, plus the installed scripted-GUI dynamic-list schema in game:common/scripted_guis/_documentation.md, lines 78–105.

New list and dossier text uses the existing Event 014 hoi_16mbs font; source_lookup found no definition for hoi_14mbs, so that unverified font is excluded from the proposal.

The proposal uses the vanilla right_vertical_slider name in place of the currently diagnosed right_vertical_slider_intel; the parent must inspect the production image and click regions before accepting it.

No window size, aspect ratio, animation sheet, portrait, or painted background is changed. The reference composition is accepted; actual production pixels remain unreviewed because the MCP artifact provenance route failed, and post-application MCP review remains mandatory.
