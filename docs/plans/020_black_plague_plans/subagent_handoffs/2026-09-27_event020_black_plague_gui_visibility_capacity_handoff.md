# Event 020 Black Plague Response GUI Visibility and Capacity Handoff

## Disposition

Blocked for GUI completion because the required post-change production MCP inspect/render comparison did not return artifacts. The source patch and accepted-layout reference are present, and the pre-change exact-window inspect/render succeeded.

The final production render request was terminated after 72 seconds without a structured result. An earlier combined post-change inspect/render request for five explicit fixtures was terminated after more than five minutes without a result. The parent directed that no further retry be made this turn. No post-change screenshot, resolution matrix, state matrix, click-region artifact, or source comparison is available.

## Event ownership and acceptance

The UI belongs exclusively to Event 020 Black Plague. The category black_plague_response_category is defined in common/decisions/categories/020_black_plague_response_categories.txt, attaches black_plague_response_category_scripted_gui, and that binding names the event-owned black_plague_response_category_window in interface/020_black_plague_response.gui.

The acceptance basis is the parent’s explicit authorization relaying the user’s approved CBRN-overhaul direction: hide the category until outbreak evidence or country response relevance exists, keep the plague category picture once, distinguish unorganized capacity from exhaustion, and review zero-progress rendering.

The category picture GFX_decision_cat_picture_black_plague_response remains owned by the decision category. The attached window contains no picture element, so it does not paint a second copy. The full-width title and programme-status header were already present before this patch; the supplied 2026-09-20 screenshot records the older duplicate-image state.

## Identifiers and changed files

The decision entry is black_plague_response_category, the attached scripted GUI is black_plague_response_category_scripted_gui, and the native container is black_plague_response_category_window.

The retained category picture sprite is GFX_decision_cat_picture_black_plague_response, backed by gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds. The existing progress sprite is GFX_black_plague_response_progress_fill; its five display elements are black_plague_response_gui_progress_fill_1 through black_plague_response_gui_progress_fill_5.

This patch changed:

- common/decisions/categories/020_black_plague_response_categories.txt to point the category visibility predicate at the dedicated UI trigger.
- common/scripted_guis/020_black_plague_response_scripted_guis.txt to use the dedicated category gate and add mutually exclusive positive-capacity and unorganized-capacity visibility triggers.
- common/scripted_triggers/020_black_plague_response_triggers.txt to add black_plague_response_category_is_visible, requiring either a relevant established, uncured local state or an active national-response flag after global outbreak establishment.
- interface/020_black_plague_response.gui to add black_plague_response_gui_capacity_unorganized at the same center-aligned bounds as the normal capacity value.
- localisation/english/020_black_plague_response_l_english.yml to add the neutral capacity label and tooltip and clarify the positive-capacity exhaustion tooltip.
- docs/plans/020_black_plague_plans/subagent_handoffs/references/020_black_plague_gui_visibility_capacity_intended.svg and .png as the scoped pre-edit correction reference.
- This handoff.

The existing black_plague_strategic_response_category_is_visible helper remains unchanged for its decision callers. Decision effects, costs, action availability, AI, balance, shared disease UI, GFX registrations, and gameplay outcomes were not changed. No new visual asset was required.

## Reference and native-element mapping

The supplied bad reference is C:/Users/klimp/OneDrive/Pictures/Screenshots/Screenshot 2026-09-20 182952.png. The earlier Event020 correction reference is docs/plans/020_black_plague_plans/subagent_handoffs/references/020_black_plague_gui_repair_intended.svg. The new intended reference is docs/plans/020_black_plague_plans/subagent_handoffs/references/020_black_plague_gui_visibility_capacity_intended.svg, with reviewed PNG at the same basename.

The parent’s user-direction authorization is the acceptance basis. The new reference keeps the existing 520×282 board and its hierarchy, and shows four states: hidden before local outbreak/relevance, active at 0% with unorganized 0/0 capacity, active with capacity remaining, and positive-total capacity exhausted.

| Reference region | Native element or source | Mapping and state |
| --- | --- | --- |
| Category identity picture | black_plague_response_category.picture = GFX_decision_cat_picture_black_plague_response | One picture remains in the native decision-category header, outside the attached window. |
| Panel background | black_plague_response_category_window and GFX_tiled_window | Existing 520×282 non-movable panel, clipped to its bounds. |
| Header | black_plague_response_gui_title and black_plague_response_gui_programme_status | Existing full-width title and current cure-programme status. |
| Primary value | black_plague_response_gui_progress_label, black_plague_response_gui_progress_value, black_plague_response_gui_progress_meter | Existing 0–100 progress label, live value, vanilla tiled background, and five threshold-gated fill icons. At 0%, all five fills are hidden. |
| Supporting values | black_plague_response_gui_outbreak_ledger, black_plague_response_gui_response_capacity, black_plague_response_gui_capacity_unorganized | National deaths stays in the left half of the summary band. Positive total capacity uses remaining/total on the right; missing or zero total uses “Not organized” in the same bounds. |
| Exhaustion state | black_plague_response_gui_capacity_warning and its existing scripted visibility trigger | Existing warning remains limited to positive total capacity with missing or zero remaining capacity. The 0/0 state suppresses it. |

The reference’s schematic bars and text explain state mapping only; they are not runtime art or controls. The engine uses native text, containers, icons, visibility triggers, and existing sprites. The design has one primary numeric mechanic value and two supporting numeric values, zero gameplay-changing GUI actions, zero GUI costs, and no click regions. Tooltips do not introduce additional mechanic values or costs.

## Visibility and state behavior

black_plague_register_current_state adds tracked states to global.black_plague_active_states without requiring establishment. The earlier category helper tested only that a relevant state was not cured, so an in-array tracked state could expose the category before an established local outbreak.

The new category-only helper adds black_plague_state_is_established = yes and the cured-state exclusion to the country-relevant local-state branch. black_plague_state_is_established covers incubating, infected, severe, collapsed, contained, recovering, and rat-controlled states. The second branch preserves the category for a country actively running countermeasure setup, a countermeasure programme, or a medical-reserve batch after black_plague_state_was_established is globally set.

| State | Expected category and board |
| --- | --- |
| Before any established outbreak and with no active national response | Category and attached board hidden. |
| Local established outbreak, 0% progress, total capacity 0 | Category shown; meter empty; “Response Capacity — Not organized”; no exhaustion warning. |
| Relevant established outbreak with positive capacity remaining | Category shown; capacity uses remaining/total; no exhaustion warning. |
| Relevant established outbreak with positive total and no capacity remaining | Category shown; capacity uses remaining/total and the exhaustion warning appears. |
| Fully recovered local outbreak with no active national response | Category hidden. A still-recovering state remains established until its cured state is reached. |
| Hover, selected, disabled | Not applicable because this board has no controls. |

The numeric text budget remains one primary progress value plus national deaths and response capacity. The programme stage remains one short qualitative status. There are no gameplay-changing buttons, costs, or displayed resource texticons in the attached GUI; action-integrity, cost-count, and cost-texticon audits are not applicable to this read-only panel.

## References and precedents inspected

The installed C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md was read at revision 43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838, lines 1–146. It documents decision_category context, window_name, visibility triggers, and native element binding.

The offline Scripted GUI modding context section was read at revision b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30, lines 144–164. It states that decision_category is the attachment context and that the scripted GUI should not have its own parent window.

The offline Scripted GUI modding window-assignment section was read at revision b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30, lines 40–67. The offline Interface modding elements section was read at revision b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c, lines 150–177. The offline Decision modding picture section was read at revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162, lines 182–185. The offline Localisation basics section was read at revision 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064, lines 73–105.

The vanilla precedent inspected was interface/sov_paranoia_system_scripted_gui.gui with common/scripted_guis/SOV_paranoia_system_scripted_gui.txt. It demonstrates separate native meter, text, and image elements inside an independent decision_category-context container. The vanilla category-pictures source rule confirms the picture belongs on the decision category; the Event020 attached window does not need another image element.

Source lookups found black_plague_strategic_response_category_is_visible in common/scripted_triggers/020_black_plague_response_triggers.txt:30-50 at source revision 51cb2aea0c92da065474ac2a9086c800781c4dd999246fc18b77d6d0c6d5a88a. The source lookup for black_plague_state_is_established found common/scripted_triggers/020_black_plague_triggers.txt:129-139 at revision 9ee03947c4b9b97c2f68066c351f72e11fdff4f31891670eeee017b79e7b4935.

## Pre-change MCP evidence

The exact-window hoi4.gui_inspect succeeded in workspace mod_chaos_redux_ea3b2d67c2c0 for black_plague_response_category_window with scenario pre_outbreak. It returned 18 inspected elements and scenario/source graph revision 6d60b9e47cfbd22fa579504fe97546096544a2fb691fcfd81f58cc9cb32ad6b4.

The inspect artifact is [gui-inspect.6d60b9e47cfbd22f.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88671c364b84c036fbffa131030fa620c5f8b917335d6e8e98fc3949a35b9d93/24ed8b2a4c82b6052b317a5e07f15404eea866ddaaaf66637e4a0e462d23ff07/gui-inspect.6d60b9e47cfbd22f.json). Its incomplete fixture produced unresolved dynamic-localisation/value warnings and zero-size/clipping warnings on hidden fill icons and the warning textbox. The warning and fill text did not appear in the zero-value production image. Those initial diagnostics are retained as baseline findings rather than treated as post-change evidence.

The exact-window pre-change hoi4.gui_render succeeded with status GUI_RENDERED and produced 27 artifacts for active_zero_unorganized: progress 0, deaths 0, capacity 0/0, with 1920×1080 and 2560×1440 at UI scale 1.0 requested. The full production PNG was visually reviewed at 1920×1080; the meter was empty, the 0/0 exhaustion warning was absent, and the attached board itself painted no second plague picture.

The [baseline full PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86a61f83fe9859c5c7c43ad1ab18a499f3789e056cc377a8f255ac405692e51b/14ae4441305b0ea10c8eec50ec100c31afc45718b46ef93b3e66b37e627529ec/black_plague_response_category_window-full.png) has SHA-256 86a61f83fe9859c5c7c43ad1ab18a499f3789e056cc377a8f255ac405692e51b. The [baseline crop](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8f6f7e977ee7556ce1208f47514f8648d87bcac4bdfe7bf57755df2d1ec311f/45a538048ea8646652e4f22ba00d75b40a38335fd376e53ed9812d4138642851/black_plague_response_category_window-cropped.png), [click-region image](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86a61f83fe9859c5c7c43ad1ab18a499f3789e056cc377a8f255ac405692e51b/0a987e1ca8f67c9e354cd3a7444c13205d320347b121a359fbaccf128240a530/black_plague_response_category_window-click-regions.png), [scenario matrix](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/725ea9614ebaaccd9eee4a49b0e32ba5f56fe6eb632040b512f8f09924687f35/7f34c2fb3ce7b78fe113a93231eb2fffd136a6fe38297933ffe8d979bbe825ea/black_plague_response_category_window-scenario-matrix.png), and [resolution-scale matrix](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bfb6832013f80e1d65fbe08e36a7516245c5bd135b3d33614b0a1c6975664138/4086ce3b7f257387748fcc0fd8707f27d0088de71fc6a7626426484d4f46ce61/black_plague_response_category_window-resolution-scale.png) preserve additional baseline evidence.

The zero-state baseline’s scenario artifact is [black_plague_response_category_window-scenario.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ac7728239f0378bd6bfc7767c62f4a68fe4a53601bdeeb9636758e851606db7/20711165e1f1f2e407d2c2f20af48810f63886b0cb35b38602de61aa6c9ac7a3/black_plague_response_category_window-scenario.json). The production render also returned hierarchy, source-map, fidelity, layout, state, click-region, validation, and comparison artifacts in the 27-artifact family.

The existing 2026-09-25 Event020 GUI evidence records earlier successful post-change renders for organized, 0/0, and exhausted capacity states. That evidence predates this patch and is not counted as post-change validation here.

## Post-change MCP evidence and blocker

On 2026-10-03 the parent recovered the archived `active_zero_unorganized` scenario JSON through the `hoi4_agent_tools` MCP resource and submitted the same explicit fixture to current-source `hoi4.gui_inspect` for `black_plague_response_category_window`, with generated scenarios disabled. The request remained live through three bounded polls without a structured result or job ID and was then terminated. This confirms the current-source inspection route is still unavailable; it adds no post-change image or comparison evidence.

An exact-window post-change hoi4.gui_inspect and hoi4.gui_render batch was issued for the same workspace and GUI with sourceBaseline from the pre-edit HEAD .gui. Its scenarios were pre_outbreak_hidden, active_zero_unorganized, active_organized, exhausted_capacity, and recovered_no_active_response, each requesting 1920×1080 and 2560×1440 at UI scale 1.0. The batch also requested normal, active, warning, completed, minimum-value, and maximum-value states. The combined call remained pending for over five minutes and was terminated on the parent’s instruction without a structured result, diagnostics, or artifacts.

A final single-scenario hoi4.gui_render then targeted black_plague_response_category_window with the explicit active_zero_unorganized fixture, sourceBaseline from HEAD:interface/020_black_plague_response.gui, both requested resolutions at UI scale 1.0, and visible/hidden expectations for the two capacity labels and warning. It remained pending for 72 seconds and was terminated on the parent’s instruction without a result or artifact.

Therefore no post-change gui_inspect, production render, state/resolution matrix, click-region review, or source comparison can be claimed. The exact route was mcp__hoi4_agent_tools__hoi4_gui_inspect and mcp__hoi4_agent_tools__hoi4_gui_render on workspace mod_chaos_redux_ea3b2d67c2c0, selector black_plague_response_category_window; the first request used the five named fixtures and the final request used active_zero_unorganized. Neither route returned an error payload, so the blocker is a non-returning tool call terminated by the parent-authorized wait bound.

## Files and source hashes

The current source and reference SHA-256 identities are:

| File | SHA-256 |
| --- | --- |
| common/decisions/categories/020_black_plague_response_categories.txt | 2d738e5b90b52c63d79f627ff5d7e9fa01beb2b03a4c9c6c818d56a638800f0d |
| common/scripted_guis/020_black_plague_response_scripted_guis.txt | c2669749de9103c29c3b62485c07433a1bff14a207e715489c81dd814bd1f04d |
| common/scripted_triggers/020_black_plague_response_triggers.txt | f1d6740aa2ca13d749225a156478be11eac641930b32c0ad1485a7231754300e |
| interface/020_black_plague_response.gui | f0459e1be83e1f698042c5ec6ff3df95ee4ccf39aa0771e796f8114d9e9c9df6 |
| localisation/english/020_black_plague_response_l_english.yml | feb610fc727b708a518d0a9b1b7484a7dcc1e7ab158d673519275e3b4ba3a5dc |
| docs/plans/020_black_plague_plans/subagent_handoffs/references/020_black_plague_gui_visibility_capacity_intended.svg | 950dedf8de7c529903141d2f3bdccb1df4147c8979a70f22df614e53905bdd19 |
| docs/plans/020_black_plague_plans/subagent_handoffs/references/020_black_plague_gui_visibility_capacity_intended.png | c86afc597821167afcd078ac17474f168817c708c1da59961be8389cd838bf2b |

The English localisation file retains its UTF-8 BOM. Current working-tree status includes unrelated changes from other repository work; no unrelated files were changed, staged, or committed by this GUI task.

## Remaining parent and user validation

The parent must review the Event020 trigger’s category-only effect and the new neutral capacity wording. The parent must also obtain the post-change inspect/render and compare artifacts before calling the GUI visually complete.

No live Hearts of Iron IV session was launched. User live-consumer validation remains pending.

## Simplifications, omissions, and blockers

- Post-change production MCP visual validation is unresolved because the exact inspect/render calls did not return before the parent-directed wait bounds.
- Pre-outbreak, active-zero, active-organized, exhausted, and recovered post-change rendered images are unavailable; only the pre-change active-zero production render was visually reviewed this turn.
- The category picture, full-width title header, zero-progress meter behavior, and positive-total exhaustion gate were already present in source before this patch; the duplicate-picture symptom in the supplied screenshot reflects an older rendered state. This patch keeps those existing pieces and does not change the GFX registration.
- No other gameplay simplification or substitute asset was introduced.
