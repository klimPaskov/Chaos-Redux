# Event 014 Network GUI current review

Review date: 2026-10-03.

## Outcome

The Network GUI pass is incomplete and blocked at the required HOI4 MCP visual-evidence gate. Fresh inspect and render calls for cannibalism_network_window never returned a status, diagnostic, workspace id, or artifact. I made no Event 014 source changes, and I do not claim visual or in-game completion.

The selected background and source-bound reference is docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_network_gui_current_review_evidence/network_window_background_reference.png. The annotated source-bound view is docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_network_gui_current_review_evidence/network_window_source_bounds_annotated.png. The evidence folder also holds byte-exact snapshots of the two permitted source files and decoded previews of linked DDS assets.

Files written by this pass are this handoff, the two background reference PNGs, the linked-asset preview PNGs under asset_references, and the two source snapshots under before. No runtime .gui, scripted-GUI, GFX, or localization file was changed.

No source simplification, fallback UI, substitute asset, or gameplay change was introduced. No commit was created, as instructed by the parent assignment.

## Event ownership and acceptance

Event id and slug: 014_cannibalism.

The accepted source is docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md, section Scripted GUI concept, Network window, lines 551-590. It specifies a separate movable five-tab window for Domestic Cells, Islands and Communes, Foreign Links, Warlord States, and Countermeasures, with sortable active-node lists and selected-target evidence.

The current user direction authorizes the full Event 014 rework without simplifications. The parent’s bounded acceptance for this worker is to preserve the accepted tab, list, and target composition and correct only demonstrated visual or native-layout defects. The specification’s existence alone is not treated as approval. This direction is the acceptance basis for the work in this handoff.

The current implementation proves exclusive ownership. cannibalism_early_header_window exposes cannibalism_network_open, which calls cannibalism_gui_open_network_view. The opener is in the Event 014 binding common/scripted_guis/014_cannibalism_scripted_gui.txt, and the separate window is bound as cannibalism_network_scripted_gui with context_type = player_context, parent_window_token = top_bar, and window_name = cannibalism_network_window. The early header is attached to Event 014’s containment and network-alert decision categories. The shared event log, Event Details, settings, super-event framework, registries, and other Event 014 windows are outside this review.

## Exact identifiers and current source identity

| Surface | Current identifiers and source |
| --- | --- |
| Window | cannibalism_network_window in interface/014_cannibalism_frontline_hunger.gui |
| Scripted GUI | cannibalism_network_scripted_gui in common/scripted_guis/014_cannibalism_scripted_gui.txt |
| Entry | cannibalism_network_open calls cannibalism_gui_open_network_view |
| Lists | cannibalism_network_country_dynamic_list and cannibalism_network_state_dynamic_list |
| Row templates | cannibalism_network_country_entry and cannibalism_network_state_entry |
| Row selectors | cannibalism_network_country_entry_select and cannibalism_network_state_entry_select |
| Navigation and view controls | cannibalism_network_tab_domestic, cannibalism_network_tab_islands, cannibalism_network_tab_foreign, cannibalism_network_tab_warlords, cannibalism_network_tab_counter, cannibalism_network_sort, cannibalism_network_refresh, cannibalism_network_close |
| Selection summary | cannibalism_selected_target_card, cannibalism_selected_target_text, cannibalism_selected_country_flag |
| GFX registration | interface/014_cannibalism.gfx |
| Player localization | localisation/english/014_cannibalism_l_english.yml |
| Scripted localization | common/scripted_localisation/014_cannibalism_scripted_localisation.txt |
| Category entry points | common/decisions/categories/014_cannibalism_categories.txt |

Current source SHA-256 identities at snapshot time:

| File | SHA-256 |
| --- | --- |
| interface/014_cannibalism_frontline_hunger.gui | 1c7b33ab8bad6bf26d3505705754ff1d8e10b3edf598a8fb879478fe70fdb591 |
| common/scripted_guis/014_cannibalism_scripted_gui.txt | 70699e7db5e95af1787fef459d077240270f2c4a9bcf324d448c9e5e6e475664 |
| interface/014_cannibalism.gfx | 36a0b2a28c36a4ffe2b1e420b3dceefea6db289958af7f90a6f9b612cd532abb |
| localisation/english/014_cannibalism_l_english.yml | 477b32b7302e77982856acd4bd79cb1269eecb888806b27c2a8a96ad8eba2b9c |
| common/scripted_localisation/014_cannibalism_scripted_localisation.txt | 63cd7e04dd6ad67a7b947895e2939358af11f91f348de3e708f2bd9980c6613c |
| common/decisions/categories/014_cannibalism_categories.txt | 11b87433cc95344a96b6bfbf9612e751f28912fb9030613e3cc3f583cd56a9c6 |

The evidence folder’s before snapshots of the .gui and scripted-GUI files match the recorded hashes byte for byte. The four authorized source surfaces had no dirty-worktree entries in the scoped Git status check. The shared checkout contains extensive unrelated pending work, which this pass left untouched.

## Reference, background, and native-element mapping

The retained 860x620 network_window_background.dds is the design blueprint. It was decoded to PNG for review without changing the runtime asset. The evidence copy retains the original canvas, and the annotated copy draws only source-derived element bounds for comparison.

| Background or reference region | Native elements and usable bounds | Content and interaction | Assets and states | Constraint or adaptation |
| --- | --- | --- | --- | --- |
| Whole 860x620 board | cannibalism_network_window, 860x620, centered with y=15, moveable=yes, click_to_front=yes, clipping=yes | Separate movable Network ledger | GFX_cannibalism_network_window_background | Canvas and window dimensions match. Background remains decorative artwork. |
| Upper map and header area | Title at x=22,y=16, max 430x32. Summary at x=22,y=46, max 520x44. Close button at x=720,y=14, sprite scale 0.86. | Title, confirmed actor/node counts, Network Reach, close and clear selection | GFX_cannibalism_network_window_background | Dynamic summary remains native text. No names of hidden individuals appear in the inspected visible strings. |
| Tab and view-control band | Five tab buttons at x=18,150,282,414,546 and y=88 or 89. Sort at x=682,y=88. Refresh at x=770,y=90. | Five tab filters, sort order, refresh | GFX_sort_button_100x29 and GFX_chaosx_button_123x34 | Selected tab image changes through scripted localization properties. Labels are native button text. |
| Central thread field | Network threads at x=18,y=130. Island alert at x=770,y=142. | Decorative network threads. Island alert appears on the islands tab when independent nodes exist. | GFX_cannibalism_network_threads_animated/static and GFX_cannibalism_island_alert_animated/static | Threads are informational decoration. They do not identify an individual. |
| Left paper ledger bay | Country list panel x=18,y=290,size=394x222. Grid x=4,y=0,size=374x222, absolute x=22..396. | Clipped, scrollable country actors with dynamic rows | GFX_cannibalism_network_country_card and GFX_flag_small2 | Source uses a transparent tiled background, clipping, scrollbar, and smooth scrolling. |
| Right paper ledger bay | State list panel x=431,y=290,size=394x222. Grid x=4,y=0,size=374x222, absolute x=435..809. | Clipped, scrollable state nodes with dynamic rows | GFX_cannibalism_network_state_card | Same native list structure as the country side. |
| Row content | Country and state row templates are each 374x64. Select buttons start at 0,0 and use a 374x64 x/y size. Country flag begins at 10,12. Country text begins at 58,8 with max 304x56. State text begins at 14,8 with max 346x56. | Country or state identity and current type/stage and strength data. Full-row target selection. | Country/state card sprites and transparent button sprite | Row text and flag are alwaysTransparent=yes so the button can receive clicks. Source hitbox dimensions match the row template dimensions. Effective rendered hit areas still need MCP evidence. |
| Lower selected-target bay | Card and overlay at x=243,y=530,size=374x64. Flag at x=255,y=543. Text at x=302,y=540,max 300x45. | Selected country or state identity, or No confirmed target selected | GFX_cannibalism_network_target_frame and selected-target overlay static/animated | Selection and overlay are conditional. The selected target remains informational and does not execute a countermeasure. |

The annotated reference shows the exact native list and target rectangles over the retained artwork. It suggests that the painted ledger insets may be narrower than the 374-pixel row assets, with the left row bounds extending over the side apparatus and both rows extending beyond the apparent paper insets. This is a reference-to-source risk, not a confirmed production-render defect. I did not move or resize elements without the required MCP visual baseline.

## Linked asset and state findings

The exact event-owned GFX registrations are in interface/014_cannibalism.gfx. The background decoded as 860x620. Country and state row cards and the selected-target frame each decoded as 374x64. All linked files listed below exist and were decoded from their runtime DDS paths.

| Sprite family | Runtime paths | Decoded dimensions and registered behavior |
| --- | --- | --- |
| Background | gfx/interface/014_cannibalism/network_window_background.dds | 860x620 |
| Country and state cards | gfx/interface/014_cannibalism/network_country_card.dds and network_state_card.dds | Both 374x64 |
| Selected target frame | gfx/interface/014_cannibalism/network_target_frame.dds | 374x64 |
| Network threads | gfx/interface/animated/014_cannibalism/cannibalism_network_threads_static.dds and cannibalism_network_threads_sheet.dds | Static 824x120. Sheet 9888x120, matching 12 frames of 824x120 at 8 fps, looping, play_on_show=yes. |
| Island alert | gfx/interface/animated/014_cannibalism/cannibalism_island_alert_static.dds and cannibalism_island_alert_sheet.dds | Static 64x64. Sheet 512x64, matching 8 frames of 64x64 at 8 fps, looping, play_on_show=yes. |
| Selected-target overlay | gfx/interface/animated/014_cannibalism/cannibalism_selected_target_overlay_static.dds and cannibalism_selected_target_overlay_sheet.dds | Static 374x64. Sheet 2244x64, matching 6 frames of 374x64 at 6 fps, looping, play_on_show=yes. |

The animated entries use the registered blend-frames effect and transparent sprite behavior. The animated threads are always visible under the current scripted trigger. The island alert is limited to the islands tab with a positive independent-node count. The selected-target frame, text, flag, and overlay are tied to country or state selection. The matching static fallback sprites exist, although the current Network binding sets the three static visibility triggers to always=no.

The source uses fonts hoi_24header, hoi_18b, and hoi_16mbs. Their emitted glyph bounds, line spacing, and optical centering are unverified because no production render returned. No custom asset was missing or routed for production.

## Current visible text and coverage findings

The localization keys read for this surface include cannibalism.gui.network.title, network.summary, network.summary.tt, tab.domestic and tab.domestic.tt, tab.islands and tab.islands.tt, tab.foreign and tab.foreign.tt, tab.warlords and tab.warlords.tt, tab.counter and tab.counter.tt, sort, refresh, close, country_entry, state_entry, entry.select.tt, selected_target, and selected_target.tt.

The current title is The Uncertain Network. The summary shows known country actors, confirmed nodes, and Network Reach, for three simultaneous mechanic values. Country rows show name, stage, and cell strength. State rows show name, node type, and strength. The selected card shows confirmed country or state identity and a short instruction to use the associated decision category. The inspected visible strings do not reveal a named individual.

Two source-to-spec content differences need parent review. The accepted spec names Islands and Communes and Warlord States, while the current button labels are Islands and Warlords. The accepted node-card information list also includes known route, last incident, selected counteraction, and uncertainty level. The current country row text shows stage and cell strength, the state row shows type and strength, and the selected-target text shows identity. The inspected strings do not demonstrate the remaining four fields. I did not expand visible data or alter wording because the parent authorized visual/native-layout corrections only and the production render route was unavailable.

## Layout hierarchy and interaction budgets

The source hierarchy is:

cannibalism_network_window
- Background, title, summary, close
- Five tabs, sort, refresh
- Network-thread and conditional island-alert sprites
- Country heading and clipped country list panel
  - Country dynamic grid
    - Country row with transparent full-row selection button, flag, and text
- State heading and clipped state list panel
  - State dynamic grid
    - State row with transparent full-row selection button and text
- Conditional selected-target frame, overlay, flag, and text

The dynamic lists consume cannibalism_network_gui_country_entries and cannibalism_network_gui_state_entries with scoped row values and indices. The tabs set the selected-tab variable and rebuild the view. Sort and refresh are view operations. Row selectors choose the displayed target. Close clears the selection and closes the window.

The screen has three summary values, within the four-value ceiling. No gameplay-changing button or spendable GUI cost is present. The count of gameplay actions is zero. The window has five tab controls, sort, refresh, close, and two selection controls. These are navigation, view, and informational selection controls. No cost texticon applies.

## Source references and engine adaptation

Guidance read and applied: AGENTS.md, .agents/skills/chaos-redux-scripted-gui/SKILL.md, .agents/skills/chaos-redux-decisions-missions/SKILL.md, .agents/skills/chaos-redux-events/SKILL.md, .agents/skills/chaos-redux-event-assets/SKILL.md, .agents/skills/chaos-redux-frame-animation/SKILL.md, and .agents/skills/chaos-redux-subagents/SKILL.md. The two earlier Event 014 GUI handoffs named in the parent prompt were read as historical evidence only.

The offline Interface modding page was read directly at paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md, including container sizing and clipping at lines 83-95, scroll-container requirements at 110-128, button elements at 227-250, and relative position/orientation at 369-373.

The offline Scripted GUI modding page was read directly at paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md, including parent-window and top-bar behavior at lines 71-114, context and dirty updates at 144-171, effects and element triggers at 179-208, dynamic lists at 249-300, and properties at 391-420.

The installed common/scripted_guis/_documentation.md was read directly at the installed game path. Its opening documentation comments identify context types and parent-window tokens, dynamic-list arrays and values, scripted button effects and element triggers, properties, and dirty-variable updates. The HOI4 reference_context and reference_search routes stalled, and no revision-bound result was returned. reference_read was not called because no revision was available.

Vanilla precedents inspected directly:
- interface/countryarmyview.gui, filter_button at lines 112-117, uses size = { x = 80 y = 29 } with GFX_tiled_window_transparent and an always-transparent label.
- interface/RAJ_famine.gui, RAJ_famine_ui_window at lines 14-17, is a compact decision-category window precedent.
- common/scripted_guis/RAJ_famine_scripted_gui.txt, RAJ_famine_scripted_ui at lines 1-10, binds a native window to decision_category context.
- Chaos Redux’s own row selectors use the same native x/y size vector for a button and transparent click-through row content.

The current adaptation keeps the background as decorative art and implements labels, tab state, country flags, dynamic rows, scrolling, selection, and click regions as native HOI4 elements. It does not flatten interactive controls or dynamic values into artwork.

## MCP pre-change evidence and route blockers

No fresh pre-change MCP artifact was returned in this pass. The exposed schemas confirmed the exact GUI tools are callable and exposed top-level scenario and rendering fields, but their nested scenario type was unknown. I used only a scenario id and generatedScenarios = { enabled = false }, without inventing actor, flag, value, or scripted-GUI fields. The service did not return a scenario interpretation or an error explaining whether additional fields were needed.

Fresh route attempts were:
- hoi4.gui_inspect, selector cannibalism_network_window, scenario id event014_network_empty_domestic_20261003, generated scenarios disabled.
- hoi4.gui_inspect retry, same exact window selector, scenario id event014_network_normal_empty_domestic_retry_20261003, generated scenarios disabled.
- hoi4.gui_render, selector cannibalism_network_window, scenario id event014_network_normal_empty_domestic_20261003, states normal and empty-list, 1920x1080 at scale 1, generated scenarios disabled.
- hoi4.gui_render retry, same exact window, scenario id event014_network_normal_empty_domestic_retry_20261003, normal state only, 1920x1080 at scale 1, generated scenarios disabled.

Each inspect and render call remained running through two waits and was stopped under the assignment’s route-attempt limit. No returned error, status, source revision, resolution, diagnostic, hierarchy, click-region, image, or artifact URI is available. The empty and populated list fixtures, other tabs, selected targets, hover, long labels, warning state, and alternate resolutions were not reviewed. No production view is substituted by the local background image.

hoi4.reference_context stalled on the GUI context request. hoi4.reference_search stalled on the query for dynamic lists and list clipping. hoi4.source_lookup stalled on the exact symbol cannibalism_network_scripted_gui. Each yielded no result after two waits. The relevant local wiki, installed documentation, and source files were read directly as fallback. The exact current MCP route gap is absence of any returned result from the connected documentation, source lookup, GUI inspection, and GUI render calls.

Historical evidence read from earlier handoffs is not a current baseline:
- The 2026-08-26 inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2027fb79400aa4c2e2bee84d06a83dc6ad64f1a2fdf4cdda77c60b96426a25b7/3ca28e89eb6d436c06e865465b0bb29dfbb5167e0f7ed68fdc7c581505a77e6e/gui-inspect.a4f84d3e76676744.json.
- The 2026-08-26 normal render artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/14ca74fc2d4120165140404d28c9511d4875641c4e0c9d3e2bf34e517a22ca68/cannibalism_network_window-full.svg.
- The 2026-08-24 hitbox inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2cf69dd308c3d8f82edf75c3c7e40113774113f8ace97ce21aa492f5715f7d5/123a3ab6485197b608d3600052f17cb59916a63ceb87b4e434a01ba8450c8074/gui-inspect.418adc0dfb6f7e8d.json.

Those earlier handoffs report truncated global diagnostics and incomplete multi-state and multi-resolution coverage. Their source hash and artifact identities do not match the source hash recorded here, so they do not establish current visual acceptance.

## Before and after disposition

There is no source behavior or visual delta from this pass. The permitted .gui, scripted-GUI, and localization files were not changed. No after-source inspect or render exists, and no matched before/after comparison can be claimed. gui_rewrite was not used.

The source-derived correction candidate is the apparent list-card and background-inset width alignment. The annotated reference is a scoped source-bounds illustration, not a production GUI render. The remaining text and node-field differences require parent design and data-owner review. Neither finding was patched without attributable MCP production evidence and explicit bounded visual review.

## Visual checklist and state matrix

| Check | Local source/reference result | MCP or runtime result |
| --- | --- | --- |
| Reference selection and native mapping | Completed from the retained 860x620 background and exact source bounds | Production comparison blocked |
| Layout hierarchy and parent context | Source mapped to player_context and top_bar | MCP hierarchy artifact unavailable |
| Background and card coverage | Linked files decode. The annotated map shows a possible card-to-inset mismatch | Production render unavailable |
| Text and value budget | Three summary values. Concise title, summary, row, and target strings | Glyph bounds, centering, wrapping, and clipping unresolved |
| Tab states | Five tab sprites switch from inactive to selected based on tab variable | Selected-state image unavailable |
| Empty Domestic list | Requested by scenario label only. No actual actor, flags, arrays, or values supplied | Inspect/render unavailable |
| Populated Domestic list | Dynamic-array source mapped | Fixture and render unavailable |
| Other tabs and conditional warning | Tab and alert triggers mapped from source | State render unavailable |
| Selected country or state | Target visibility, flag, overlay, and dynamic text mapped | Selected-state and click-region evidence unavailable |
| Hover and long actual labels | Native buttons and fixed text bounds mapped | Hover and long-text renders unavailable |
| Crowded list and scrolling | Clipped panel, scrollbar, and smooth-scrolling source mapped | Crowded-state render unavailable |
| Disabled or completed | No gameplay action has a disabled or completed presentation state in this window | Not applicable to the source-defined controls |
| Resolution and UI scale | Requested 1920x1080 at 1.0 | No returned render. 1920x1080 at 1.25 and 1366x768 at 1.0 were not attempted because the initial route remained blocked |
| Effective click bounds, z-order, and overlaps | Source selector equals row dimensions. Click-through is set on row text and flag | MCP evidence unavailable |
| Hidden identity and neutral presentation | The visible title and selected-none text preserve uncertainty. Inspected UI strings do not name an individual | Scenario-specific identity checks unavailable |

## Remaining parent work, blockers, and live evidence

The parent should reopen the exact Network window pass when the GUI MCP routes return. The required work is an exact-window inspect, a coherent normal empty Domestic fixture and a populated Domestic fixture, other tab and selected-target states, hover and longest actual labels, followed by the supported resolution and scale checks. The production PNG, hierarchy, diagnostics, state views, and effective click regions must be inspected before any layout patch. Matching before and after source and scenario artifacts remain required if a patch is made.

The parent and gameplay owner should review whether the accepted node-card fields for route, last incident, selected counteraction, and uncertainty are available to this visual surface, then resolve whether the short Islands and Warlords labels remain accepted. This handoff does not change the data owner’s gameplay logic or invent new data.

No missing linked asset was found in the local DDS decode. No asset handoff was routed. No gameplay cost, requirement, AI behavior, outcome, or cleanup rule was changed or re-audited. The parent retains final Event 014 integration. User-supplied live consumer and in-game validation remain pending.

## Simplifications and omissions

This worker introduced no simplification, fallback, asset substitution, gameplay change, or source change. The requested visual correction remains unresolved because fresh MCP inspect and production-render evidence could not be obtained. The possible background alignment defect and the visible content differences above are reported for parent review and are not presented as completed fixes.
