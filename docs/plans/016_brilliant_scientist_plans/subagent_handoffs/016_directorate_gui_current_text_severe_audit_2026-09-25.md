# Event 016 Directorate current text and severe-state audit

Disposition: unresolved, read-only audit handoff, 2026-09-25.

## Scope and ownership

Event id and slug: Event 016, brilliant_scientist.

The authorized surface is the dedicated decision-category attachment: brilliant_scientist_directorate_scripted_gui in common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt, attached to brilliant_scientist_directorate_category in common/decisions/categories/016_brilliant_scientist_directorate_categories.txt, with window_name kruger_directorate_container in interface/016_brilliant_scientist_directorate.gui.

This ownership is supported by the source attachment and by the prior Event 016 handoffs. The scripted GUI is a decision_category context, its visibility is limited to the current host or sovereign Kruger State, and the accepted compact design leaves gameplay actions in ordinary decisions below the category.

Only this handoff was written in this task. No GUI, scripted-GUI, GFX, localisation, decision, event, asset, model, or shared-interface source was changed. No 3D assets were created, inspected, or modified.

## Acceptance basis and reference

The accepted surface is the compact Directorate record with four visible mechanic values: Mandate, Dependence, Exposure, and Capacity. The accepted expanded hierarchy is a 500x360 panel; the collapsed header is 500x58. The expanded display contains Kruger’s portrait and name, four meter/value rows, one role/control line, and one footer. Only the open or close utility control is present in a given phase.

The parent acceptance addendum in docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_directorate_compact_redesign_2026-08-15.md records the final title position and accepted compact hierarchy. It points to the parent-reviewed 1366x768 reference artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f444ee55e353657a7c6cfb2743a037b171d2172c710164305fca8d68a2eba40/fe655d71ae7e423de16d93ebfb43b0d833e9bc79a8d610f8da416489fad5ff2e/kruger_directorate_container-full.svg.

The 2026-09-02 closure handoff records stable historical actual-text reference images at docs/plans/016_brilliant_scientist_plans/subagent_handoffs/evidence/016_directorate_gui_current_production_2026-09-02/event016_directorate_actual_normal_expanded-full-1920x1080.png and event016_directorate_actual_severe_host-full-1920x1080.png. Those historical references were not reopened or compared visually during this interrupted audit.

The accepted layout map is:

| Region | Native element and bounds | Content and interaction |
| --- | --- | --- |
| Collapsed header | kruger_directorate_compact_panel, 500x58; header sprite at 0,0 | Compact title at x40,y16 in a 360x24 box; open control at x422,y11 |
| Expanded surface | kruger_directorate_full_panel, 500x360; background at 0,0 | Title at x40,y22 in a 360x28 box; close control at x422,y11 |
| Profile | Frame at x38,y80 and portrait at x42,y84, each scale 0.68; name box x32,y234, 138x22 | Dynamic profile frame and portrait; fixed name Dr. Warren Kruger |
| Four values | Meter icons at x176,y82/126/170/214; value boxes x304,y89/133/177/221, each 154x22 | Mandate, Dependence, Exposure, and Capacity; 44px row pitch |
| Role and control | kruger_directorate_role_control at x36,y272, 428x30 | One dynamic role/control line |
| Footer | kruger_directorate_footer at x36,y326, 428x20 | One dynamic host or sovereign instruction |

The window uses native iconType, instantTextBoxType, and buttonType elements. The backgrounds and meter/profile art are layered behind live text and controls; none of the interactive or dynamic content is flattened into artwork.

## Exact linked identifiers

| Surface | Identifier or keys |
| --- | --- |
| Scripted GUI and window | brilliant_scientist_directorate_scripted_gui; kruger_directorate_container |
| Category entry | brilliant_scientist_directorate_category |
| Panels and controls | kruger_directorate_compact_panel; kruger_directorate_full_panel; kruger_directorate_open_button; kruger_directorate_close_button |
| Scripted-GUI actions | kruger_directorate_open_button_click clears brilliant_scientist_directorate_gui_collapsed; kruger_directorate_close_button_click sets it |
| Visibility and click gates | Element visibility and button click-enabled triggers are keyed to brilliant_scientist_directorate_gui_collapsed |
| GFX file | interface/016_brilliant_scientist_directorate.gfx |
| Background/control sprites | GFX_decision_category_brilliant_scientist_directorate; GFX_kruger_directorate_background; GFX_kruger_directorate_compact_header; GFX_kruger_directorate_open_control; GFX_kruger_directorate_close_control |
| Profile and value sprites | GFX_kruger_directorate_profile_human; GFX_kruger_directorate_profile_secured; GFX_kruger_directorate_profile_sovereign; GFX_kruger_directorate_mandate_low/moderate/high/extreme; GFX_kruger_directorate_dependence_low/moderate/high/extreme; GFX_kruger_directorate_exposure_low/moderate/high/extreme; GFX_kruger_directorate_capacity_low/moderate/high/extreme |
| Portrait binding | GFX_portrait_KRG_doctor_warren_kruger_stage_0; the prior handoff records dynamic stage-four portrait variants, including the machine route |
| GUI localisation file | localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml |
| Visible localisation keys | brilliant_scientist_directorate_gui_compact_title; brilliant_scientist_directorate_gui_open_tt; brilliant_scientist_directorate_gui_title; brilliant_scientist_directorate_gui_close_tt; brilliant_scientist_directorate_gui_profile_name; brilliant_scientist_directorate_gui_role_control; brilliant_scientist_directorate_gui_mandate; brilliant_scientist_directorate_gui_dependence; brilliant_scientist_directorate_gui_exposure; brilliant_scientist_directorate_gui_capacity; the four matching value tooltip keys; brilliant_scientist_directorate_gui_control_tt; brilliant_scientist_directorate_gui_footer |
| Dynamic localisation | GetBrilliantScientistDirectorateProfileFrameSprite; GetBrilliantScientistDirectoratePortraitSprite; GetBrilliantScientistDirectorateMandateSprite; GetBrilliantScientistDirectorateDependenceSprite; GetBrilliantScientistDirectorateExposureSprite; GetBrilliantScientistDirectorateCapacitySprite; GetBrilliantScientistDirectorateProfileRole; GetBrilliantScientistGovernmentControl; GetBrilliantScientistDirectorateFooter |
| Decision entry examples from the prior handoff | brilliant_scientist_convene_public_science_council; brilliant_scientist_approve_selected_project; brilliant_scientist_formalize_primary_research_campus; brilliant_scientist_review_foreign_approaches; brilliant_scientist_release_kruger; brilliant_scientist_sovereignty_deadline_mission |

The source uses four visible values, zero gameplay-changing GUI actions, one utility toggle per visible phase, zero spendable GUI costs, and no cost texticons. The existing decisions retain their own requirements, costs, effects, AI behavior, and cleanup.

## Fresh MCP inspection

The only MCP call in this audit was hoi4.gui_inspect with windowName kruger_directorate_container, workspaceId mod_chaos_redux_ea3b2d67c2c0, scenario id event016_directorate_current_expanded, and generatedScenarios disabled.

The route returned GUI_INSPECTED with status ok, complete true, 22 inspected elements, zero skipped sources, and shared revision fbbd753a5879396b76bd31ebb72b05f70e8a02161fc04e2e17ba252da691fa99. Its artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df0f5b272e40bd51793c81d5de599e07592e16575a4218e7edcfc8f164a4111e/15da6cc5efc4142a0b8747348a1308d2e6f4cdebb4e51b44777b15386a070b93/gui-inspect.fbbd753a5879396b.json.

The saved scenario had empty flags, visibility, values, variables, and localisation maps. It did not assert the collapsed or expanded branch and did not supply actual display strings. Its fidelity counts were 196 modelled, 3 approximated, 7 ignored, 0 missing, 2 unsupported, and 7 unresolved.

The inspect validation failed because it rendered both mutually exclusive controls into one untyped scenario: GUI_CONFLICTING_CLICK_REGIONS reported 100% overlap between kruger_directorate_open_button and kruger_directorate_close_button. Validation also counted 26 GUI_VISIBLE_OVERLAP findings and 3 GUI_Z_ORDER_RISK findings. The inline response returned 12 overlap entries, 2 GUI_SPRITE_RENDER_PARTIAL warnings, and the click conflict; the collection-limit notice says the linked artifact contains bulk evidence. The partial-sprite warnings state that gfx/FX/buttonstate.lua is retained but not executed by the offline renderer.

This call does not establish that the game shows both controls together. The source gates their visibility and click availability on brilliant_scientist_directorate_gui_collapsed, while the inspect scenario supplied no visibility or flag values. The prior 2026-09-02 typed-state handoff records that explicit branch fixtures cleared the conflicting-click finding. The fresh empty fixture therefore leaves actual runtime branch behavior unresolved.

The tool result’s shared revision differs from the scenario revisions recorded in the 2026-09-25 baseline handoff. No source diff was made in this task, and the revision tokens are not treated as proof that the source changed.

## Render, state, and comparison evidence

No fresh hoi4.gui_render call, image review, click-region render, hierarchy view, or current-source comparison was performed after the parent directed this task to finish from evidence already obtained and not start further long MCP calls. This is an explicit evidence gap, not an MCP route failure.

The supplied 2026-09-25 baseline handoff has historical collapsed/expanded production images and a three-resolution view at 1366x768, 1920x1080, and 2560x1440, all at UI scale 1. That handoff says its generic expanded fixture leaves numeric values and dynamic localisation unresolved, so those images cannot establish current actual-text fidelity. The 2026-09-02 closure handoff records actual normal-expanded, normal-collapsed, severe-host, and severe-sovereign fixtures and historical render artifacts; their source revision predates the fresh inspect revision above.

| Requested state | Relevance to this surface | Current audit status |
| --- | --- | --- |
| Normal expanded and collapsed | Both branches are required and mutually exclusive | Unresolved for current source; fresh inspect had no visibility or text overrides |
| Hover | Applies to the visible open or close control | Historical renderer warning says buttonstate.lua is not executed; no fresh hover image reviewed |
| Selected | No persistent selected action exists in the accepted window | Not applicable as a game state; no fresh generic probe |
| Disabled | The alternate phase control is hidden by branch state; neither branch adds a disabled gameplay action | No fresh render; exact engine treatment unverified |
| Warning/severe | Compromised control, high/extreme meter stages, and stage-four portrait are reachable visual cases | Historical severe-host and severe-sovereign results only; current-source review unresolved |
| Empty-list/full-list | The accepted window contains no list; decision-list density belongs to its parent category | Not applicable to this window |
| Minimum/maximum values | Four values use the accepted 0..100 display range and low/extreme meter sprites | Historical boundary coverage only; current values and images unresolved |
| Long text | Longest recorded host role/control is “Concealed programme director &#124; Government control: Compromised”; longest sovereign footer is “Kruger State orders remain in its sovereign decision categories.” | Historical actual-text review only; no current image comparison |
| Missing localisation | Relevant to the visible Event 016 keys | Fresh render not performed; current visual status unresolved |
| Active/completed | No gameplay action or completion control exists in this read-only attachment | Not applicable as a control state; no fresh generic probe |

The previous handoff records the actual maximum strings as Mandate 100, Dependence 100, Exposure 100, and Capacity 100, and says the value variables are clamped to 0..100. These are historical typed-fixture assertions, not values supplied by the fresh inspect call.

No current full-window, cropped, annotated, hierarchy, click-region, resolution, or comparison image was reviewed. No current visual defect is confirmed, and no source edit can be justified from the fixture-induced overlap alone.

## Reference mapping and engine limits

The accepted 500x360 background maps to kruger_directorate_background; the 500x58 header maps to kruger_directorate_compact_background. The profile, four meters, text boxes, and open/close buttons remain separate native elements over the art.

The scripted GUI contains individual child visibility gates because the earlier source notes that decision-category consumers do not reliably honor visibility on nested containers. The offline route requires explicit scenario visibility to model this branch; its generic empty scenario does not test the country flag or parent-context behavior.

The prior handoffs report that the renderer does not execute gfx/FX/buttonstate.lua and needs explicit scenario text for dynamic scripted localisation. They also report a synthetic long-text probe overflowing small fixed text boxes, while the longest previously enumerated reachable role and footer strings did not overflow in historical production renders. Neither limitation was rechecked against current-source images in this audit.

The dynamic portrait selector has historical stage-four animated portrait variants. Their current frame selection and visual fidelity were not refreshed here. No animation asset was created or changed, and no 3D/model work was performed.

## Before/after behavior and source-edit disposition

There was no source edit in this audit, so there is no new before/after behavior change. Existing open and close effects still clear or set brilliant_scientist_directorate_gui_collapsed, and their visibility/click gates remain in the exact Event 016 scripted GUI file.

Source-edit requirement: unresolved. The only fresh blocking click diagnostic came from the inspect fixture with empty visibility and flag maps. It is insufficient evidence for a source correction. A current-source typed render and actual image review are still needed to decide whether any layout or state correction is required.

## Reading and validation limits

Reviewed for this handoff: the supplied AGENTS.md instructions; chaos-redux-scripted-gui skill; the relevant chaos-redux-subagents handoff requirements; the Event 016 host-directorate spec passage; the current category, scripted-GUI, and window source; the GUI localisation; and the two named prior handoffs.

Not independently verified to completion in this interrupted audit: the full offline wiki core pages and GUI pages; the full installed vanilla documentation and vanilla precedent contents; the full chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-event-assets, and chaos-redux-frame-animation skill contents; and the complete current scripted-localisation file.

The requested references/visual-review.md was absent at .agents/skills/chaos-redux-scripted-gui/references/visual-review.md, and a filename search under docs and .agents/skills returned no copy. This absence is recorded as a review-material gap; the visual checklist in the scripted-GUI skill and prior accepted handoff supplied the available criteria.

## Remaining work and blockers

- Current actual-text and severe-state rendering remains unresolved because no typed hoi4.gui_render call or image review was made after the parent requested a prompt handoff without further long MCP calls. The user's separate instruction prohibited model work.
- The exact current flag-dependent collapsed/expanded branch behavior is not established by the empty inspect fixture; the fresh scenario omitted its visibility and flag inputs.
- The fresh inspect surfaced a 100% click-region collision under that untyped fixture, 26 validation-counted painted overlaps, 3 z-order risks, 2 partial button-sprite warnings, and 7 unresolved fidelity bindings. These findings need a typed current-source render before they can be separated into intended layering, fixture artifacts, or actual defects.
- Current hover frames, minimum/maximum images, reachable long-text bounds, missing-localisation state, all three requested resolutions, and matching visual comparison remain unverified.
- No current visual defect was confirmed, so no correction plan or source diff is included.
- Live in-game consumer validation remains user-owned. No game was launched.
- No model, 3D asset, sound, or counter work was performed.

Simplifications and omissions in this audit: current-source render and visual comparison were omitted under the parent's bounded handoff instruction; the remaining state, source-reading, and image-review gaps are reported as unresolved rather than passed.

## Parent follow-up: explicit branch fixture

The parent reran `hoi4.gui_inspect` for `kruger_directorate_container` with `generatedScenarios.enabled = false` and explicit visibility: compact panel and open button hidden, full panel and close button visible. It returned `GUI_INSPECTED` with validation passed and no blocking click-region conflict at scenario `e016_severe_typed`; [inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90cca14c31b147f46f6b305189ac2dbcca51b2910f4b177c2c2714ab0e41a87f/f1a584fcb7b7774ff7deb9f064cf3cdcef68ab26f06861eaf1852bd423e3aa83/gui-inspect.c13e9987cfa736fb.json). Despite the scenario ID, only visibility was supplied; no severe-state values or actual text were supplied. The inspector still counted 16 nonblocking visible overlaps from layered elements. This resolves the generic fixture's 100% open/close collision as an omitted-visibility input, without asserting that actual engine flag evaluation was tested. Dynamic text and severe-state image review remain unresolved.
