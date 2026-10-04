# Event 020 Black Plague GUI Evidence Recovery Handoff

## Disposition

Implemented for current-source GUI visual acceptance. The shared GUI route returned current-source inspect and render artifacts on 2026-10-04 for all five accepted fixtures at 1920x1080 and 2560x1440 at UI scale 1, the one real layout finding was repaired, and the returned revisions, artifact hashes and visual review are recorded in [the recovery evidence report](../../../testing/2026-10-03_event020_gui_recovery/README.md). The earlier blocked narrative and its persisted retry requests remain below as history.

## Ownership and accepted basis

Event 020 exclusively owns black_plague_response_category, black_plague_response_category_scripted_gui, and black_plague_response_category_window. The category is defined in common/decisions/categories/020_black_plague_response_categories.txt, attaches the named scripted GUI, and binds the dedicated window in interface/020_black_plague_response.gui. The category picture GFX_decision_cat_picture_black_plague_response remains on the category; the attached window has no picture element.

The parent-authorized acceptance basis is the user-approved CBRN direction recorded in [the 2026-09-27 implementation handoff](2026-09-27_event020_black_plague_gui_visibility_capacity_handoff.md): gate category visibility on an established relevant outbreak or active national response, use one category picture, show “Not organized” for unorganized 0/0 capacity, keep the exhausted warning for positive-total capacity with zero remaining, and show an empty progress bar at 0%.

The decisions and event asset guidance normally reserves category pictures for simple categories without a complex GUI or meter. The parent’s accepted, explicit user direction retains exactly one category picture and removes only the duplicate image inside the attached window; this is a documented exception to the default hierarchy, and this recovery task does not change that accepted choice.

The scoped reference is [the intended PNG](references/020_black_plague_gui_visibility_capacity_intended.png) and [its SVG source](references/020_black_plague_gui_visibility_capacity_intended.svg). The reference maps the 520×282 board into the native category picture/header, title and status, 0–100 meter and fills, deaths and one capacity value, plus the conditional exhaustion warning; the mapping and accepted adaptation are recorded in [the recovery evidence report](../../../testing/2026-10-03_event020_gui_recovery/README.md).

## Identifiers and files

| Surface | Exact identifiers |
| --- | --- |
| Entry point | black_plague_response_category in common/decisions/categories/020_black_plague_response_categories.txt. |
| Scripted GUI | black_plague_response_category_scripted_gui in common/scripted_guis/020_black_plague_response_scripted_guis.txt. |
| Native GUI | black_plague_response_category_window in interface/020_black_plague_response.gui. |
| Category picture | GFX_decision_cat_picture_black_plague_response, backed by gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds. |
| Meter fill | GFX_black_plague_response_progress_fill, used by black_plague_response_gui_progress_fill_1 through _5. |
| Capacity states | black_plague_response_gui_capacity_unorganized_visible, black_plague_response_gui_response_capacity_visible, and black_plague_response_gui_capacity_warning_visible. |
| Category gate | black_plague_response_category_is_visible in common/scripted_triggers/020_black_plague_response_triggers.txt. |
| GUI localisation | localisation/english/020_black_plague_response_l_english.yml, including the unorganized capacity label and tooltip. |
| Decision entry | The dedicated decision category; the board is informational and decisions remain ordinary category entries. |
| Asset handoff | None; all accepted sprites were already registered and no new asset is requested. |

The exact category and panel localisation keys are black_plague_response_category, black_plague_response_category_desc, black_plague_response_gui_title, black_plague_response_gui_programme_status, black_plague_response_gui_identity_tt, black_plague_countermeasure_progress_label, black_plague_countermeasure_progress_value, black_plague_countermeasure_progress_tt, black_plague_response_gui_outbreak_ledger, black_plague_response_gui_outbreak_ledger_tt, black_plague_response_gui_response_capacity, black_plague_response_gui_response_capacity_tt, black_plague_response_gui_capacity_unorganized, black_plague_response_gui_capacity_unorganized_tt, black_plague_response_gui_capacity_warning, and black_plague_response_gui_capacity_warning_tt.

This recovery task changed only the owned documentation outputs: docs/testing/2026-10-03_event020_gui_recovery/README.md, the two request JSON files in that folder, and this handoff. The five implementation source hashes and exact reference mapping are in the evidence report.

## Pre-change evidence and baseline

The prior handoff records a successful exact-window hoi4.gui_inspect in workspace mod_chaos_redux_ea3b2d67c2c0, scenario pre_outbreak, with source graph revision 6d60b9e47cfbd22fa579504fe97546096544a2fb691fcfd81f58cc9cb32ad6b4, 18 inspected elements, and the preserved inspect artifact URI in the evidence report.

The prior handoff also records a successful 27-artifact active_zero_unorganized pre-change render at 1920×1080 and 2560×1440, scale 1.0. The 1920×1080 production image was reported visually reviewed: empty meter, no 0/0 exhaustion warning, and no second picture in the attached board. Full image, crop, click-region, scenario-matrix, and resolution-matrix URIs plus hashes are preserved in the evidence report. These are prior-source evidence, not a current-source review.

The source baseline passed to the prepared render request is Git HEAD:interface/020_black_plague_response.gui at commit 15440b1021799216fc391e9e8375d9e00f66a761, blob 26bac5b07149558d348d5be64bdaa2055ae7859c. The rendered comparison did not return, so there is no current comparison artifact.

## Current MCP recovery attempt

The live exposed schemas were checked for mcp__hoi4_agent_tools__hoi4_gui_inspect and mcp__hoi4_agent_tools__hoi4_gui_render. No separate server version or health capability appeared in the available tool list.

The narrow inspect request for black_plague_response_category_window, workspace chaos_redux_probe, explicit active_zero_unorganized fixture, and generated scenarios disabled returned immediate structured error WORKSPACE_NOT_REGISTERED. The same inspect was retried against mod_chaos_redux_ea3b2d67c2c0; it remained pending for about 63 seconds with no structured result, job id, diagnostics, artifact, or source revision, and the outer execution was terminated.

A one-fixture render then targeted active_zero_unorganized on the same earlier workspace at 1920×1080 and scale 1, with all four numeric values supplied under scenario.values, generated scenarios disabled, and the Git pre-patch .gui supplied through sourceBaseline. It remained pending for about 60 seconds; the outer execution was terminated without an artifact, diagnostics, source identity, or comparison. No 2560×1440 or additional fixture was attempted after that first render did not return.

The prior scenario artifact was also requested directly through hoi4_agent_tools resources. It failed with “Artifact provenance manifest is unavailable”; no image or fixture data could be recovered from that URI in this route.

The source and precedent material was rechecked within this narrow GUI surface. The installed common/scripted_guis/_documentation.md revision 43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838 and offline Interface modding, Scripted GUI modding, Decision modding, and Localisation sections and revisions are listed in the evidence report. The vanilla precedent is interface/sov_paranoia_system_scripted_gui.gui with common/scripted_guis/SOV_paranoia_system_scripted_gui.txt.

## State matrix and review

| Fixture | Expected state | Current-source result |
| --- | --- | --- |
| pre_outbreak_hidden | Category hidden before an established local outbreak unless an active response follows global establishment. | Not rendered. |
| active_zero_unorganized | Progress 0%, empty meter, “Not organized”, no exhaustion warning. | Narrow render call pending/terminated; no image. |
| active_organized | Positive remaining/total capacity; no warning. | Not rendered. |
| exhausted_capacity | Positive total with zero remaining; exhaustion warning shown. | Not rendered. |
| recovered_no_active_response | Category hidden after recovery absent active response. | Not rendered. |

The reference PNG was visually inspected. Current-source glyph centering, measured layout bounds, clipping, spacing, z-order, click regions, hierarchy, state coherence, and resolution scaling remain unreviewed. The prior handoff’s pre-change diagnostics included unresolved dynamic values and zero-size/clipping warnings on hidden fills and the warning text box; those are baseline findings, not post-change diagnostics.

Before the accepted correction, a tracked local state could satisfy the older category helper before establishment, and the attached summary had no distinct neutral presentation for zero or missing total capacity. The accepted source patch now requires an established relevant local state or an active national response after global establishment, and shows “Not organized” when total capacity is absent or zero; positive-total exhaustion remains separate. These are current-source findings, not rendered post-change proof.

The value budget is three numeric values: progress, national deaths, and response capacity. The action budget is zero, costs and distinct spendable cost types are zero, and cost-texticon coverage is not applicable. No missing or routed assets are reported. No animated frame sheet is part of this accepted UI.

## Parent request wrappers and follow-up

The parent private SDK requests are persisted at [gui-inspect.request.json](../../../testing/2026-10-03_event020_gui_recovery/gui-inspect.request.json) and [gui-render.request.json](../../../testing/2026-10-03_event020_gui_recovery/gui-render.request.json). Both use chaos_redux_probe, the explicit active_zero_unorganized fixture under scenario.values, disabled generated scenarios, and expected visibility for the unorganized capacity label, normal capacity label, warning, and progress fills. The render request uses only 1920×1080 at scale 1 and embeds the pre-patch GUI baseline.

The fixture does not supply country/state scope facts because the shared live schema result did not establish a supported field for them. Its explicit element expectations are render assumptions, not runtime proof of category visibility. The parent should use a registered private workspace and record the actual returned source revision, scenario id, artifact URIs, render resolution, state diagnostics, and reviewed PNG before advancing to the remaining fixtures and 2560×1440.

The parent retains final review of the category visibility helper, neutral capacity wording, game outcomes, costs, AI, balance, and integration. The user performs live consumer validation. This worker did not launch the game or make production source or asset edits.

## Blockers and simplifications

- Post-change GUI completion is blocked pending the parent’s private SDK inspect/render route and visual review of actual production PNGs.
- The shared route returned WORKSPACE_NOT_REGISTERED for chaos_redux_probe and did not return results from the earlier workspace within the recorded bounds.
- No post-change resolution, state, hierarchy, click-region, or source-comparison evidence exists.
- The pre-change images could not be independently fetched here because their MCP artifact provenance manifest was unavailable; the prior handoff retains their URIs and review result.
- No UI mechanic, action, asset, or layout scope was simplified by this recovery task; the acceptance gate remains open.

## 2026-10-04 closeout

The narrow shared route responded. The pre-fix inspect of `active_zero_unorganized` reported one genuine layout finding, `GUI_INCONSISTENT_SPACING` with sibling vertical gaps from 3px to 16px, alongside hidden-element `0x0` reports and one unresolved scripted-localisation token.

The board was given one rhythm, 14px top and bottom padding with a uniform 9px gap between rows, and the summary panel's labels were centred inside it. After the change the spacing finding is absent from all five fixtures, `gui_visible_overlap` passes everywhere, and the render of five fixtures at both required resolutions returns no layout diagnostic at all.

The unaccepted six-lane response proposal in `../2026-09-27_shared_response_interaction_and_cost_budget_addendum.md` was not implemented.

Two declared limits remain and belong to the orchestrator's live session: the offline renderer does not evaluate `[GetBlackPlagueCountermeasureStatus]`, and the fixture cannot set the country and global flags that `black_plague_response_category_is_visible` reads, so category-level visibility is proven in source rather than in a rendered image.
