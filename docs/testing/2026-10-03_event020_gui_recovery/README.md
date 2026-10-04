# Event 020 GUI evidence recovery

Disposition: **implemented** for current-source visual acceptance. The 2026-10-04 round returned current-source inspect and render results for all five accepted fixtures at both required resolutions; the earlier blocked status and its retry plan are recorded below as history.

This report covers only the Event 020-owned black_plague_response_category_window in interface/020_black_plague_response.gui. No gameplay source, production GUI source, GFX, localisation, asset, or shared interface was edited in this recovery task.

## Ownership and accepted layout

The dedicated black_plague_response_category is registered in common/decisions/categories/020_black_plague_response_categories.txt; it attaches black_plague_response_category_scripted_gui, which names the exact window black_plague_response_category_window. The category source uses the Event020-only category and picture identifiers, and the attached window contains no separate category picture, establishing the bounded event-owned surface.

The accepted correction basis is the parent’s explicit authorization relaying the user-approved CBRN direction recorded in the 2026-09-27 handoff: hide the category until an established relevant outbreak or active national response exists, retain one category picture, distinguish unorganized 0/0 capacity from exhausted positive-total capacity, and keep the meter empty at 0%.

The decision and event asset guidance normally reserves category pictures for simple categories without a complex GUI or meter. The parent’s accepted, explicit user direction retains exactly one Event020 category picture while removing only the duplicate image inside the attached window; this is a documented accepted exception to the default presentation hierarchy. No new picture or other asset is produced by this recovery task.

The scoped intended reference is [020_black_plague_gui_visibility_capacity_intended.png](../../plans/020_black_plague_plans/subagent_handoffs/references/020_black_plague_gui_visibility_capacity_intended.png), with its source [SVG](../../plans/020_black_plague_plans/subagent_handoffs/references/020_black_plague_gui_visibility_capacity_intended.svg). I visually reviewed the PNG: it preserves the 520×282 board and shows hidden pre-outbreak/recovered, active 0% with 0/0 capacity, organized active capacity, and exhausted positive-total capacity.

## Reference-to-native mapping

| Reference region | Native source and identifiers | Intended bounds and behavior | Assets and state |
| --- | --- | --- | --- |
| Category identity | black_plague_response_category.picture = GFX_decision_cat_picture_black_plague_response in common/decisions/categories/020_black_plague_response_categories.txt | One picture lives in the native decision category header outside the attached window. | Existing gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds. |
| Board background | black_plague_response_category_window and GFX_tiled_window | Existing 520×282 panel at (0,0), clipped to its bounds. | Vanilla tiled window. |
| Header | black_plague_response_gui_title and black_plague_response_gui_programme_status | Title at (20,14), programme status at (20,53). | Native text using hoi_24header and hoi_18mbs. |
| Primary value and meter | black_plague_response_gui_progress_label, black_plague_response_gui_progress_value, black_plague_response_gui_progress_meter, fills black_plague_response_gui_progress_fill_1 through _5 | Label/value at y=98; meter at (20,131), 480×27; five threshold-gated fills display progress from 0–100%. | Existing GFX_tiled_progress_bar and GFX_black_plague_response_progress_fill; all fills hidden at 0%. |
| Summary values | black_plague_response_gui_outbreak_ledger, black_plague_response_gui_response_capacity, black_plague_response_gui_capacity_unorganized | In the summary panel at (20,167), 480×70; deaths occupy the left half and one capacity label occupies the right half, both at y=21 inside the panel. | Existing GFX_tiled_window_transparent; positive total shows remaining/total, absent or zero total shows “Not organized”. |
| Capacity warning | black_plague_response_gui_capacity_warning | At (20,246), 480×22; visible only when positive total capacity exists and none remains. | Existing warning text; hidden for 0/0. |

The UI is read-only, has no button-like controls, no click effects, no gameplay-changing actions, no costs, and no GUI click regions. The intended adaptation keeps interactive decisions in their existing decision category and uses native text, containers, meter background, and fill icons for all dynamic information.

The exact category and panel localisation keys are black_plague_response_category, black_plague_response_category_desc, black_plague_response_gui_title, black_plague_response_gui_programme_status, black_plague_response_gui_identity_tt, black_plague_countermeasure_progress_label, black_plague_countermeasure_progress_value, black_plague_countermeasure_progress_tt, black_plague_response_gui_outbreak_ledger, black_plague_response_gui_outbreak_ledger_tt, black_plague_response_gui_response_capacity, black_plague_response_gui_response_capacity_tt, black_plague_response_gui_capacity_unorganized, black_plague_response_gui_capacity_unorganized_tt, black_plague_response_gui_capacity_warning, and black_plague_response_gui_capacity_warning_tt.

## Content and action budgets

The three visible numeric mechanic values are countermeasure progress, national deaths, and response capacity; the short cure-programme status is qualitative. This is within the four-value maximum and the normal one-primary-plus-two-supporting-value budget. There are zero primary GUI actions, zero costs, and zero spendable cost types; texticon coverage is not applicable because no costs are displayed. The UI is information-only, so hover, selected, disabled, locked, and action click-region states do not apply.

The accepted text density is one title, one short programme status, one progress label/value, two concise summary values, and a conditional short capacity warning. Relevant tooltips are attached to the information elements in the native GUI. No text or numeric dump is flattened into artwork.

## Evidence and source identity

The 2026-09-27 handoff records the pre-change exact-window inspect as successful for black_plague_response_category_window in workspace mod_chaos_redux_ea3b2d67c2c0, scenario pre_outbreak, with source graph revision 6d60b9e47cfbd22fa579504fe97546096544a2fb691fcfd81f58cc9cb32ad6b4. It reports 18 inspected elements and retains an inspect artifact at [gui-inspect.6d60b9e47cfbd22f.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88671c364b84c036fbffa131030fa620c5f8b917335d6e8e98fc3949a35b9d93/24ed8b2a4c82b6052b317a5e07f15404eea866ddaaaf66637e4a0e462d23ff07/gui-inspect.6d60b9e47cfbd22f.json).

The same handoff records a pre-change render for active_zero_unorganized with progress, deaths, and capacity at 0 and capacity 0/0, requesting 1920×1080 and 2560×1440 at UI scale 1.0. It reports 27 artifacts and visual review of the 1920×1080 full image, with the meter empty, 0/0 exhaustion warning absent, and no second picture painted by the attached board. The prior [full render](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86a61f83fe9859c5c7c43ad1ab18a499f3789e056cc377a8f255ac405692e51b/14ae4441305b0ea10c8eec50ec100c31afc45718b46ef93b3e66b37e627529ec/black_plague_response_category_window-full.png) has SHA-256 86a61f83fe9859c5c7c43ad1ab18a499f3789e056cc377a8f255ac405692e51b; the handoff also preserves a [crop](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8f6f7e977ee7556ce1208f47514f8648d87bcac4bdfe7bf57755df2d1ec311f/45a538048ea8646652e4f22ba00d75b40a38335fd376e53ed9812d4138642851/black_plague_response_category_window-cropped.png), [click-region view](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86a61f83fe9859c5c7c43ad1ab18a499f3789e056cc377a8f255ac405692e51b/0a987e1ca8f67c9e354cd3a7444c13205d320347b121a359fbaccf128240a530/black_plague_response_category_window-click-regions.png), [scenario matrix](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/725ea9614ebaaccd9eee4a49b0e32ba5f56fe6eb632040b512f8f09924687f35/7f34c2fb3ce7b78fe113a93231eb2fffd136a6fe38297933ffe8d979bbe825ea/black_plague_response_category_window-scenario-matrix.png), and [resolution-scale matrix](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bfb6832013f80e1d65fbe08e36a7516245c5bd135b3d33614b0a1c6975664138/4086ce3b7f257387748fcc0fd8707f27d0088de71fc6a7626426484d4f46ce61/black_plague_response_category_window-resolution-scale.png).

The baseline image and fixture artifacts are references from the 2026-09-27 handoff, not newly retrieved evidence. A read attempt against hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ac7728239f0378bd6bfc7767c62f4a68fe4a53601bdeeb9636758e851606db7/20711165e1f1f2e407d2c2f20af48810f63886b0cb35b38602de61aa6c9ac7a3/black_plague_response_category_window-scenario.json failed with “Artifact provenance manifest is unavailable”, so the underlying PNG/JSON could not be independently opened in this workspace.

The Git pre-patch baseline supplied in the render request is HEAD:interface/020_black_plague_response.gui at commit 15440b1021799216fc391e9e8375d9e00f66a761, Git blob 26bac5b07149558d348d5be64bdaa2055ae7859c. This is the source snapshot passed as sourceBaseline; because the render did not return, no comparison result is available.

| Working source on 2026-10-03 | SHA-256 |
| --- | --- |
| common/decisions/categories/020_black_plague_response_categories.txt | 2d738e5b90b52c63d79f627ff5d7e9fa01beb2b03a4c9c6c818d56a638800f0d |
| common/scripted_guis/020_black_plague_response_scripted_guis.txt | c2669749de9103c29c3b62485c07433a1bff14a207e715489c81dd814bd1f04d |
| common/scripted_triggers/020_black_plague_response_triggers.txt | f1d6740aa2ca13d749225a156478be11eac641930b32c0ad1485a7231754300e |
| interface/020_black_plague_response.gui | f13f89cb4bfdcd050fa77198a490456e288bbdc85b2252d68d3d78f7b1b11ac1 |
| localisation/english/020_black_plague_response_l_english.yml | feb610fc727b708a518d0a9b1b7484a7dcc1e7ab158d673519275e3b4ba3a5dc |

Four of the five current working source hashes match the values recorded in the 2026-09-27 handoff. interface/020_black_plague_response.gui changed in the 2026-10-04 round, which repaired its sibling spacing; that round is recorded below.

## Before and after behavior

Before the accepted correction, a tracked local state could satisfy the older category helper before establishment, and the attached summary had no distinct neutral presentation for zero or missing total capacity. The accepted source patch now requires an established relevant local state or an active national response after global establishment, and shows “Not organized” when total capacity is absent or zero; positive-total exhaustion remains separate. Those behaviors are visible in the current source, and the 2026-10-04 round below supplies the after-images and matching inspect results.

## Documentation and vanilla precedent

The prior handoff cites the installed common/scripted_guis/_documentation.md at revision 43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838, lines 1–146, covering decision_category context, window_name, visibility triggers, and native element bindings. The offline Scripted GUI modding window-assignment section was read at revision b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30, lines 40–67; its context section was read at the same revision, lines 144–164. The offline Interface modding elements section was read at revision b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c, lines 150–177. The Decision modding category-picture section was read at revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162, lines 182–185, and Localisation basics at revision 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064, lines 73–105.

The exact vanilla precedent inspected is interface/sov_paranoia_system_scripted_gui.gui with common/scripted_guis/SOV_paranoia_system_scripted_gui.txt. Its independent decision_category-context window separates meter/background sprites, text, and image elements, matching the native-element approach used here.

## 2026-10-03 route retries (history)

The direct tool schemas were exposed as mcp__hoi4_agent_tools__hoi4_gui_inspect and mcp__hoi4_agent_tools__hoi4_gui_render; the schema declares windowName, scenario, generatedScenarios, resolutions, and sourceBaseline. The session exposed no separate server version or health tool, so exposure alone does not establish backend health.

| Attempt | Exact request | Result |
| --- | --- | --- |
| A | mcp__hoi4_agent_tools__hoi4_gui_inspect, workspace chaos_redux_probe, window black_plague_response_category_window, generated scenarios disabled, fixture active_zero_unorganized with the four values in scenario.values. | Immediate structured error WORKSPACE_NOT_REGISTERED; no artifact or source revision. |
| B | Same inspect selector and fixture on the earlier workspace mod_chaos_redux_ea3b2d67c2c0. | No structured result after about 63 seconds; the outer execution was terminated while the MCP call remained pending. No job id, diagnostics, or artifact was returned. |
| C | mcp__hoi4_agent_tools__hoi4_gui_render, workspace mod_chaos_redux_ea3b2d67c2c0, fixture active_zero_unorganized, generated scenarios disabled, 1920×1080 at scale 1, and Git HEAD .gui supplied as sourceBaseline. | No structured result after about 60 seconds; the outer execution was terminated while the MCP call remained pending. No production PNG, diagnostics, source identity, or comparison was returned. |

No 2560×1440 render or other current-source fixture was attempted because the first current-source render did not return. The prior 2026-09-27 handoff also records an older batch/final attempt that was terminated without structured evidence.

## 2026-10-03 state matrix (history)

| Fixture | Expected state | Current-source MCP evidence |
| --- | --- | --- |
| pre_outbreak_hidden | Category hidden before an established local outbreak unless an active response follows global establishment. | Not attempted after the narrow route remained unavailable. |
| active_zero_unorganized | Board shown, progress 0%, 0/0 capacity rendered as “Not organized”, no warning, empty meter. | Attempted at 1920×1080 and scale 1; no result or image. |
| active_organized | Board shown with positive remaining/total capacity and no warning. | Not attempted after the narrow route remained unavailable. |
| exhausted_capacity | Positive total and zero remaining capacity show the exhaustion warning. | Not attempted after the narrow route remained unavailable. |
| recovered_no_active_response | Category hidden after local recovery with no active national response. | Not attempted after the narrow route remained unavailable. |

The pre-change full render findings above are carried from the earlier handoff only; they are not a post-change visual review. Current review remains outstanding for full-window and cropped views; painted, logical, glyph, and hit bounds; two-axis label centering; margins, rhythm, and symmetry; parent placement and scaling; clipping and overflow; fonts and contrast; backgrounds and assets; z-order; visibility and state coherence; click regions; tooltips; hierarchy; and the declared resolution/UI-scale matrix. No current PNG or diagnostic artifact was returned.

There are no known missing assets or routed asset handoffs in the accepted layout. The category picture sprite is registered in interface/020_black_plague_response.gfx; no duplicate picture element or new artwork is part of the accepted correction.

## Persisted parent requests

The schema-correct request wrappers are [gui-inspect.request.json](gui-inspect.request.json) and [gui-render.request.json](gui-render.request.json). They target the parent’s private probe workspace chaos_redux_probe, disable generated scenarios, use explicit values under scenario.values, and assert the intended capacity-label/warning/fill visibility. The render request uses only 1920×1080 at UI scale 1 and embeds the Git pre-patch .gui as sourceBaseline.

The active-zero fixture sets progress, national deaths, total response capacity, and remaining capacity to 0. It does not invent country/state scope facts because the live schema result did not identify a supported scope-fact field; therefore category-level outbreak visibility is not proven by this fixture. Any explicit visibility expectation remains a declared render assumption, not runtime evidence.

## 2026-10-03 remaining work (history)

The parent must invoke the saved requests through its available private SDK route using an actually registered private workspace, inspect any returned production PNGs and diagnostics, add the 2560×1440 scale-1 render if the 1920 render succeeds, and continue through all five accepted fixtures before updating visual status. Compare only artifacts whose scenario values, source revision, language, UI scale, resolution, and source baseline match.

The parent retains review of category visibility logic, neutral capacity wording, gameplay outcomes, decision costs, AI behavior, balance, and final integration. Live consumer validation remains with the user. The task is incomplete for GUI visual acceptance until the post-change inspect/render artifacts are returned and visually reviewed.

## 2026-10-03 blockers (history)

The 2026-10-04 round below closes the first two blockers and the open visual gate; the artifact-retrieval limit stays recorded for the pre-change baseline only.

- Current-source post-change MCP inspection and production rendering remain unresolved because the narrow old-workspace calls did not return and the new private probe id was not registered on the shared tool route.
- Current-source images for pre-outbreak hidden, organized capacity, exhausted capacity, and recovered-without-response were not produced; 2560×1440 was not attempted because the single 1920×1080 render did not return.
- Cross-workspace retrieval of the prior fixture artifact failed with “Artifact provenance manifest is unavailable”; the historical pre-change evidence is preserved by its URI and prior handoff record only.
- No source or asset simplification was introduced by this recovery task; the visual gate is still open.

## 2026-10-04 round: returned evidence

The narrow shared route responded in this round, so every fixture below has a real returned result. Workspace `mod_chaos_redux_ea3b2d67c2c0`, generated scenarios disabled, explicit `scenario.values` only.

### Before: one real layout defect

The first inspect ran the accepted `active_zero_unorganized` fixture against the tranche source as it stood, shared revision `f68cea36a612fe6f22cd8232ea5117ea28420e97046d76b14410af2e72d18551`, artifact `gui-inspect.f68cea36a612fe6f.json` SHA-256 `345df8d0f9e5df6d3ac89650c3f0de2025adcc2b3eefa975e48e2c5124cdd71f`, code `GUI_INSPECTED`, 19 inspected elements, no blockers.

It reported one genuine layout finding: `GUI_INCONSISTENT_SPACING` on `black_plague_response_gui_outbreak_summary`, "Sibling vertical gaps vary from 3.00px to 16.00px". The measured gaps were 5, 13, 3, 16 and 11 pixels with a 15px top and 10px bottom padding.

The other fourteen warnings were `GUI_ACCIDENTAL_CLIPPING` and `GUI_INVALID_SIZE` pairs reported as `0x0` for elements the fixture hides, and one `GUI_UNRESOLVED_DYNAMIC_VALUE` for `[GetBlackPlagueCountermeasureStatus]` in `black_plague_response_gui_programme_status`. Every element that the fixture shows was sized and placed normally, so both groups are renderer limits rather than defects, and neither is dismissed as a renderer discrepancy for a visible element.

### The fix

The board now uses one rhythm: 14px padding at the top and bottom of the 282px window and a uniform 9px gap between every sibling row, giving title y=14, programme status y=53, progress label y=98, meter y=131, summary panel y=167 and capacity warning y=246. Inside the 70px summary panel both capacity labels and the deaths label moved to y=21 so the row is centred. The repeated 20px margin and 480px content width became `@BLACK_PLAGUE_RESPONSE_GUI_MARGIN` and `@BLACK_PLAGUE_RESPONSE_GUI_CONTENT_WIDTH`, and the five meter band offsets became named constants beside the existing segment-width constant, which is documented as matching the 96x27 `GFX_black_plague_response_progress_fill` sprite.

### After: inspect

| Fixture | Shared revision | Artifact SHA-256 | Result |
| --- | --- | --- | --- |
| active_organized | `7a6e6dadb716782f2c64cd36a9c544756fb84aea2951fdb32622e65b81849f17` | `1b45601e3bfc801d9bb80d00cd6473c69fc7b28a931997434f7c11b1e63b658c` | `GUI_INSPECTED`, no blockers, no spacing finding |
| exhausted_capacity, with recovered_no_active_response, pre_outbreak_hidden and active_zero_unorganized as related scenarios | `86746cc45f6bfe6dbd77a56870429bec9e1f82f23f38b2e806179a8700c8573f` | `814da3a06d561fc3e75918177e27e54319c3da1cade45768f944d6d10394dfa9` | `GUI_INSPECTED`, no blockers, no spacing finding |

`GUI_INCONSISTENT_SPACING` does not appear in any of the five fixtures after the fix, and `gui_visible_overlap` passes in every one, which is the engine-side proof that the organized and not-organized capacity labels are mutually exclusive: they share the same position and are never both painted. Their triggers are exact complements, `has_variable AND capacity > 0` against `NOT has_variable OR NOT capacity > 0`.

The exhaustion warning appears only in `exhausted_capacity`, where the total is positive and nothing remains; it is hidden in `active_zero_unorganized`, `pre_outbreak_hidden` and `recovered_no_active_response`, where the total is zero, and in `active_organized`, where capacity remains.

### After: render

One render covered all five fixtures at 1920x1080 and 2560x1440, UI scale 1, state `normal`: code `GUI_RENDERED`, source revision `cba66cab2b458ab31882dad5aa46ccc5ca6eba0b31b187228bcabdc7c8aa0c88`, 5 scenarios, 2 resolutions, no blockers, validation passed and no layout diagnostic of any kind.

| Artifact | SHA-256 |
| --- | --- |
| black_plague_response_category_window-full.png | `9525a3f5aefe451088692a7e54d37f3a4cce1d3c31abdcec184eefedcab6dfc9` |
| black_plague_response_category_window-cropped.png | `d803bac5f24eb9dcab2876244ced5252db68dcb9b92f464c587f76eb81ffa3c6` |
| black_plague_response_category_window-annotated.png | `c9c340dbea82c171cc9f470dc5f808f86fd543a943b42f48a1cd3a5f128c80a5` |
| black_plague_response_category_window-click-regions.png | `9525a3f5aefe451088692a7e54d37f3a4cce1d3c31abdcec184eefedcab6dfc9` |
| black_plague_response_category_window-source-map.png | `9514495c30a6e33a04cb8020ce92826c677ae4fa68bec03c2b4170b9b649a2e1` |
| black_plague_response_category_window-hierarchy.svg | `c32bb71e541548d4ad8969c2ab4c437afce40cb2b567de237a183eb3767604d2` |
| black_plague_response_category_window-scenario-matrix.png | `d2c510f19c85c2501eec538cac18680534ebd017af3b285683d66c7917b66151` |
| black_plague_response_category_window-resolution-scale.png | `efb0d770454c51ba0ce2f2251ef067fc577e7e62dc6c19b4114cd747145d5ed5` |
| black_plague_response_category_window-layout.json | `f4b6904ce05e1d8be2a0f5378399e78bba664bf9a526dfeabf398437513bf9c7` |
| black_plague_response_category_window-validation.json | `3d7af6e24dc7427c410af00bf6b3fe5e0c3d44c091dc049cbdc7d2bb91f436b0` |

### Visual review

I opened the scenario matrix and the 1920x1080 crop. The board reads as one panel: the title, the programme-status line, the progress label with its right-aligned value, the five-band meter, the deaths and capacity row and the warning row sit on an even rhythm with no crowding and no overlap. Nothing is cut off at either resolution and the window needs no scrolling.

Band filling matches the fixtures: none at 0%, two at 45%, three at 62% and five at 100%. The deaths label is centred in the left half of the summary panel and the capacity label in the right half, and the two centres are symmetric about the window centre. The red exhaustion line is centred across the full content width.

Two renderer limits remain, both declared rather than dismissed. `[GetBlackPlagueCountermeasureStatus]` renders as a placeholder because the offline renderer does not evaluate scripted localisation, and window-level category visibility depends on country and global flags that the fixture cannot set, so `pre_outbreak_hidden` exercises the element-level fixture rather than proving the category is hidden. The category gate itself is `black_plague_response_category_is_visible`, reviewed in source.
