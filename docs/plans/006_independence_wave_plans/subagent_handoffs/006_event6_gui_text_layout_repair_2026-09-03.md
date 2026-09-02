# Event 006 GUI text-layout repair handoff — 2026-09-03

## Outcome

No source edit was made. The reported explanatory-text overlap is reproducible in the no-flag generated scenario used by the production MCP route, but it disappears when the scenario supplies the real Event 006 tab state. The source already places the five explanatory text boxes at one intentional panel slot and the Event 006 scripted GUI makes exactly one slot visible at a time. Moving the five boxes to separate coordinates would create five simultaneous panels and would break the accepted tab surface, while removing the default Government fallback or replacing the five boxes with dynamic localisation would require an out-of-scope scripted-GUI change.

## Ownership and exact surface

- Event ownership is established by the Event 006 root `chaosx.nr6.1` in `events/006_independence_wave.txt:12`, the founding decision category in `common/decisions/categories/006_independence_wave_categories.txt:54-60`, and its `scripted_gui = independence_wave_status_scripted_gui` registration at line 60.
- GUI: `independence_wave_status_window` in `interface/006_independence_wave.gui:9-69`.
- Scripted GUI: `independence_wave_status_scripted_gui` in `common/scripted_guis/006_independence_wave_scripted_gui.txt:9-104`.
- GFX: `GFX_independence_wave_status_panel` and the Event 006 state/animated/static sprite families in `interface/006_independence_wave.gfx:65-77`.
- Event 006 GUI localisation: `localisation/english/006_independence_wave_gui_l_english.yml:2-102`, with the five explanatory strings at lines 50-54.
- The dedicated decision-category surface is gated by `is_independence_wave_active_country = yes`; no pre-event surface gate was changed.

## Source and vanilla evidence

- `interface/006_independence_wave.gui:64-68` defines `independence_wave_status_government_panel`, `independence_wave_status_recognition_panel`, `independence_wave_status_security_panel`, `independence_wave_status_league_panel`, and `independence_wave_status_ambitions_panel` at the same `{ x = 280 y = 444 }` panel slot with `maxWidth = 386`, `maxHeight = 42`, and `fixedsize = yes`.
- `common/scripted_guis/006_independence_wave_scripted_gui.txt:27-60` sets one tab flag and clears the other four on every tab click.
- `common/scripted_guis/006_independence_wave_scripted_gui.txt:73-87` exposes the Government panel only when no other tab flag is set and exposes each other panel only for its own tab flag.
- `interface/006_independence_wave.gfx:67,70,73,76` are the four animated families with the known adapter-only `GUI_ANIMATION_STATIC_FALLBACK_MISSING` warnings; static siblings remain present at lines 68, 71, 74, and 77.
- The offline `Interface modding - Hearts of Iron 4 Wiki.md` documents fixed-position text boxes, `maxWidth`, `maxHeight`, `format`, and `fixedsize`; the offline `Scripted GUI modding - Hearts of Iron 4 Wiki.md` documents per-element scripted-GUI visibility and independent decision-category windows.
- Vanilla `interface/AST_cabinet_trust_scripted_gui.gui` plus `common/scripted_guis/AST_cabinet_trust_scripted_gui.txt` provide the exact `context_type = decision_category` and `window_name` precedent.
- Vanilla `interface/RAJ_eic_tax_fraud.gui` plus `common/scripted_guis/RAJ_tax_fraud_scripted_gui.txt` provide the matching fixed textbox and `<element>_visible` trigger precedent.

## Pre-change MCP artifacts and findings

- `hoi4.gui_inspect` selector: `windowName = independence_wave_status_window`, scenario id `event6_gui_text_layout_repair_baseline_2026_09_03`.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/404fcde11cf9beb957fb26876cbee24bd8287ba9068e59a6d8c40ec981f62367/37bb4d2b3399eb6ac493907141a081b9020c78f5496b6e7cf8e7bf5e6224903e/gui-inspect.df5bebbd63e8218f.json`.
- Inspect result: `GUI_INSPECTED`, complete source graph, 48 inspected elements, 64 nonblocking visible-overlap findings, 557 modelled elements, 5 approximated, 15 ignored, 4 unsupported, and 0 unresolved.
- `hoi4.gui_render` selector: the same window with states `normal`, `active`, `warning`, and `long-text` at `{ width = 1920, height = 1080, uiScale = 1 }` and `{ width = 1366, height = 768, uiScale = 1 }`.
- Baseline full PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/83630047ffd3732e987e95db37ca5c60fe1b67724b7341c88adf2c57971f3234/710d00893c2907c9ae447a29c87b0cabd1773258b3aa97ae67c82a041da5f921/independence_wave_status_window-full.png`.
- Baseline cropped PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51cf23cc1338beff2f4ea21ff3f8594a92168488994b8a21d853c0df9873a1ba/ab6fdeae1504b01ee804023f61d04008213e5d223ba670e0fd70cbf0ac025f3e/independence_wave_status_window-cropped.png`.
- Baseline annotated PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3653e6cbc9ef456c52e9d95f2fb9b2d7d76014e910329049a936a6c994c560a0/2bece647889c9724213c943571f33b6e932ee357a505e8a0a000dcce95098cb9/independence_wave_status_window-annotated.png`.
- Baseline render also emitted click-region, source-map, hierarchy, scenario-matrix, state-matrix, resolution-scale, fidelity, and comparison views; those views were reviewed with the full/cropped PNGs and layout/validation JSON artifacts below.
- Baseline layout JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c29200f01938f3d9f6696398f8675514f8250519502e29de13b722112a73b22/3c4d856e0e88690aa9f91c3ec4ed19e11c4f7511281b693832ae5134d61d90c4/independence_wave_status_window-layout.json`.
- Baseline validation JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5a8b063850f92d0b62c5eccdd1a3502b12bf4047e13682c4428752a88e910ee/aed73e1d8f1d33004751e0141cabc56321b55f1df49d682aa40a5b4f8c539933/independence_wave_status_window-validation.json`.
- Baseline fidelity, scenario, source-graph, scenario-matrix, state-matrix, and resolution-scale JSON artifacts were emitted by the same render; the primary layout and validation artifacts above are the retained evidence for this decision.

## Exact generated-scenario blocker

- In the baseline render scenario JSON, all five panel visibility values are `true` while `flags` and `scriptedGui` are empty.
- The baseline layout JSON therefore reports all five text boxes visible at the identical rectangle `{ x = 280, y = 444, width = 386, height = 42 }`, producing the reported stacked text region around x≈280–665 and y≈449–480.
- The panel text itself is not overlong: the baseline layout manifest resolves Government to two lines (`Founding decisions shape the cabinet, constitution, and state` / `institutions.`), Recognition to two lines, Security to two lines, League to two lines, and Ambitions to two lines.
- Explicit MCP Government-tab fixture selector: scenario id `event6_gui_text_layout_repair_government_fixture_2026_09_03` with `flags.independence_wave_status_tab_government = true`, matching scripted-GUI state, Government visibility `true`, and the other four panel visibility values `false`.
- Explicit fixture full PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b6ec2746e9debf4a38574c049fd0ba039c9d285cc2455639a4fa7b6369bf6c2/9e29dca269afc7ebd0ffb4fa074f930dcbc081b91657191bf21d1cdbc10ef867/independence_wave_status_window-full.png`.
- Explicit fixture cropped PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8433a26ed98bca43a37c27a90f143c102a4828d5d2df8d54a4dc5ac3ea395094/4fc0e779fff7559803b3c5983da2007850ad7003552274c404e15a14b61c06ca/independence_wave_status_window-cropped.png`.
- Explicit fixture layout JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98b41c92a4dd4c486253bcec2a271e0c88902da0870f85e956f54ea36ff2680c/e64663d5aef8a373e4e1ddb881b355c89d29142913585f520f029de0b65f90da/independence_wave_status_window-layout.json`.
- Explicit fixture scenario JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24fc292b803f044c2f7dce50340f9649c8a115df0e4207d30003dda2178405b2/34b1a3b50ca21917836730c63fcab7817214cb55065a91e6bcfdc4f0e2d69cc9/independence_wave_status_window-scenario.json`.
- Explicit fixture validation JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db5b0e91807cdc1e618e6e477713efd31bccd21688c4708e17e3e7af3ebcc550/425532511c45224cb18cc3205123d17f8f69798c6462beea8d8df861ea0d747a/independence_wave_status_window-validation.json`.
- Explicit fixture result passed validation, showed one visible Government panel at the same two-line rectangle, and produced no panel/text/tab diagnostics.

## Layout, budget, and state audit

- Hierarchy: 700×500 `independence_wave_status_window` root, full-window `GFX_independence_wave_status_panel` background, left founding-value rows, right host/patron/network/phase/mission readouts, five navigation tabs, and one tab-owned explanatory text slot.
- Background coverage: the existing `GFX_independence_wave_status_panel` covers the entire root; no new panel, frame, or asset is required.
- Value budget: the existing window exposes five left founding values plus host, patron, network, phase, and mission readouts; this exceeds the usual compact scripted-GUI value budget but is pre-existing accepted Event 006 content and was not changed during this bounded overlap audit.
- Action budget: two presentation controls (`Animate`, `Refresh`) and five mutually exclusive navigation tabs; no gameplay-changing control or cost is introduced here.
- Cost-count audit: zero spendable costs are shown in this window, so no texticons are applicable.
- Text-density audit: the five explanatory strings each resolve to two lines within 386×42 in the baseline layout manifest; no localisation edit is warranted.
- State matrix exercised: normal, active, warning, long-text, 1920×1080, and 1366×768 in the baseline render, plus a normal Government-tab fixture at 1920×1080.
- Preserved state wiring: severe-instability warning visibility and static/animated sibling visibility remain owned by the existing scripted GUI; no state trigger or animation property was changed.
- Click regions remain source-aligned to the five button rectangles at GUI lines 58-62; no click-region edit was made.

## Changed files and rewrite decision

- Owned GUI, GFX, and localisation files changed: none.
- The only file added by this tranche is this handoff document.
- `hoi4.gui_rewrite` was not invoked because there is no source-safe rewrite to apply after the explicit fixture proved the tab visibility logic; invoking a rewrite without an accepted source patch would risk changing the intended five-tab surface.
- No fallback keys, duplicate aliases, assets, animation frames, or localisation strings were added.

## Remaining warnings and parent-owned validation

- Retain the four adapter-only `GUI_ANIMATION_STATIC_FALLBACK_MISSING` warnings at `interface/006_independence_wave.gfx:67,70,73,76`; static siblings at lines 68, 71, 74, and 77 are already wired and no unsupported fallback key is safe.
- Retain the renderer's floating-point `GUI_ACCIDENTAL_CLIPPING` notices for 46.08-scaled icons and the intentional background/icon overlap notices; neither is the reported text defect or a safe bounded text repair.
- The generic no-flag render reports `GUI_TAB_STATE_CONFLICT` because the generated scenario sets all five panels visible; the explicit Government fixture passes without that conflict.
- The baseline route also reports unsupported or unrequested state coverage for hover, selected, locked, disabled, completed, empty-list, full-list, minimum-value, maximum-value, and missing-localisation variants; no source edit was justified by these route limitations.
- Parent-owned work remains live HOI4/save-load verification, any gameplay or state-trigger changes, decision/effect integration, and the final determination of whether the production adapter should supply a tab-state fixture rather than the empty generated scenario.
- This handoff does not claim live HOI4 proof.

## Simplifications and blockers

- Simplification: none to the Event 006 source surface.
- Blocker: the production MCP no-flag generated scenario does not model the decision-category country tab flags and therefore paints all five mutually exclusive fixed-position panel text boxes together.
- Safe next step if the MCP route is improved: rerun the same baseline render with a tab-aware generated scenario and compare the existing layout without changing Event 006 source.
