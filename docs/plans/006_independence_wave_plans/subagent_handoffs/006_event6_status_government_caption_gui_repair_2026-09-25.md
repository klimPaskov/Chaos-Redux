# Event 006 Status/Government Caption Repair Handoff

Disposition: **implemented** for the authorized government-panel caption repair. The acceptance basis is the user's explicit approval in this task (`i approve everything`) and the parent-reviewed scoped reference and MCP evidence recorded below. This disposition applies to the caption repair only; the whole GUI and Event 006 remain **HOLD / PARTIAL**.

## Scope and ownership

The owner is Event 006, “Independence Wave.” The GUI is `independence_wave_status_scripted_gui`, attached to the `decision_category` context and rendered in `independence_wave_status_window`.

The entry point is the Event 006 status decision category in `common/decisions/categories/006_independence_wave_categories.txt`; layout is `interface/006_independence_wave.gui`; scripted wiring is `common/scripted_guis/006_independence_wave_scripted_gui.txt`; the only implementation change in this tranche is `localisation/english/006_independence_wave_gui_l_english.yml`, key `independence_wave_status_gui_government_panel`.

The text changed from `Founding decisions shape the cabinet, constitution, and state institutions.` to `Founding choices shape the cabinet and institutions.` No gameplay or layout files, click effects, or runtime assets changed. The delegated GUI worker applied the exact localization edit but did not return its required handoff; the parent completed the read-only MCP review and records the handoff gap here.

## Reference and mapping

The scoped intended-result image is `../references/006_event6_status_government_caption_reference_2026-09-25.png` (SHA-256 `8A8EC1E7BCA12B4B3E6D3F97E14401C5BB3FEE5C3BFBAC5BBE3F2E3073BFC442`). The accepted mapping is the government caption localization key to `independence_wave_status_government_panel`, an informational `instantTextBoxType` at x=280, y=444 with maxWidth=386 and maxHeight=42. The sentence remains in the government panel and does not change its tab, effects, or state requirements.

## Baseline evidence

The baseline MCP source revision was `879ec4f3fdad07fb01bf98f3fd8efb877aa77353bf1f6437b0784ae2d673449c` at 1920×1080, UI scale 1, CXT, English, with the Government tab selected. The parent baseline crop is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00ad267157e877752d1981805fe467f7f1a8aa15e87c4620be8847dcc9ab95f8/7c66111d367d47c187d9fe75d45bdf268c4f09de3428afd611d933798733e2bc/independence_wave_status_window-cropped.png`; the full-window image is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ecb6ec835d011bedd94b4266f015c44615d4d2a8d868ca2f212c31c4fd80094/9f486c4e605f386ddbdffff964854abf1d89ed9f4a7232f4c033def4389c143a/independence_wave_status_window-full.png`.

The parent baseline visual review found the old caption wrapping into the lower metallic frame. During the final parent review, rereading the archived baseline crop failed with `Artifact provenance manifest is unavailable`; the original baseline URIs and source revision remain recorded, and the same collision was reproduced by the explicit old-text comparison scenario below.

## Post-change MCP evidence

The exact post-change render source revision is `08f8eb96e48292b871ed735339a53eaed9704f35cab47e15ec58f05950659c85`, scenario ID `event006_status_caption_exact_comparison`, with generated scenarios disabled. The fixture used CXT, `l_english`, 1920×1080, UI scale 1, animation off, the Government tab selected with its per-control state set to `active`, all other tab flags off, the government panel visible, and the supplied Event 006 values and scripted-localization outputs. Only the `normal` window state was requested for this exact fixture.

The rendered crop is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d953998863b4b930f0f80087c925bff1e5ccc596a845cb8bd4320065515bf004/3c75df3b4d89bc816355df87e9e8a7261ff49b86813c03a019d6796abba9eb34/independence_wave_status_window-cropped.png` (SHA-256 `d953998863b4b930f0f80087c925bff1e5ccc596a845cb8bd4320065515bf004`). The revised caption renders on one line and clears the lower frame by visible space.

The production comparison artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3829dc735f3a72c01b0af7037ebb01b13fb4919e882329c38792868e024193dd/cdcb11439b0867ffdcd84639e4891d7241598ec6a3dbb8da7b3e47b9e1c72f4f/independence_wave_status_window-comparison.png` (SHA-256 `3829dc735f3a72c01b0af7037ebb01b13fb4919e882329c38792868e024193dd`). It compares the current source to a `comparisonScenario` using the exact old caption, with all other fixture inputs held constant; the renderer reports 2,801 changed pixels (0.0013507908950617284). This isolates the text-wrap change on the current source and is not represented as a source-revision comparison.

The matching explicit-fixture click-region render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4761eb1f66a81c638744f65d4710249dae8ff189ac57f958eaaca48ec92c6ce8/a548197c9856e65e7f73d1781bf5ff0c4e2b88157ab05e2ac2485bfcac9a6d3f/independence_wave_status_window-click-regions.png` (SHA-256 `4761eb1f66a81c638744f65d4710249dae8ff189ac57f958eaaca48ec92c6ce8`). The five tab hitboxes align with their visible controls. Validation reports no button-label centering, click-bound mismatch, conflicting click regions, missing localization, or tab-state conflict for this explicit one-tab fixture.

The explicit render validation passed and parsed the linked GUI source graph. Its 48 overlap warnings include the full-window background behind children, the static and animated icon variants sharing their designed sockets, and a few overlapping logical text/icon rectangles whose rendered glyphs remain visually separated in the reviewed crop. It also reports 12 clipping warnings, mostly floating-point differences of about 1e-14 px on scaled controls plus zero-size hidden panels, and four partial animation warnings because the offline renderer does not execute `gfx/FX/buttonstate_blendframes.lua`. The exact final fixture covers only the normal window state; hover, disabled, selected, warning, completed, boundary-value, and other panel-state coverage remains open. The earlier global `active` sweep produced a mutually exclusive tab-state diagnostic; the explicit per-control active state removed that conflict and matches the skill guidance for tabbed windows.

## Disposition and remaining evidence

The accepted change is the one-line localization repair only. The current visual and old-text comparison support that the caption no longer wraps into the frame under the recorded fixture. The baseline artifact retrieval failure, missing delegated worker handoff, renderer's partial animated-sprite representation, and incomplete broader state matrix remain recorded limits; they do not establish full GUI acceptance. The user owns live-game validation under `AGENTS.md`.
