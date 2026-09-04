# Event 016 Directorate GUI visual-closure handoff

Status: blocked for fresh production MCP evidence; no runtime GUI, GFX, localisation, asset, or gameplay source was changed by this worker.

## Event ownership and scope

Event id and slug: Event 016, `brilliant_scientist`.

The event-owned category `brilliant_scientist_directorate_category` attaches `brilliant_scientist_directorate_scripted_gui` in `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt`.

The scripted GUI declares `context_type = decision_category` and `window_name = "kruger_directorate_container"` in `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.

The independent root `containerWindowType` named `kruger_directorate_container` exists only in `interface/016_brilliant_scientist_directorate.gui`.

This handoff is limited to the named Event 016 window, its presentation wiring, event-scoped textures, linked GUI localisation, and the evidence record.

The compact read-only display keeps four public values: Mandate, Dependence, Exposure, and Capacity.

Independent Capacity and Grievance remain hidden implementation state.

Biological, Alien, and Portal actions remain ordinary decision categories and are not added to this window.

The accepted Overview, Projects, Facilities, Foreign, and Authority contexts remain represented by the compact record and the decision list below it; no removed tab, panel, project card, facility card, foreign card, sovereignty card, or gameplay control was restored.

## Exact identifiers and entry points

| Surface | Identifier | File or consumer |
| --- | --- | --- |
| Event-owned category | `brilliant_scientist_directorate_category` | `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt` |
| Scripted GUI | `brilliant_scientist_directorate_scripted_gui` | `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt` |
| GUI root | `kruger_directorate_container` | `interface/016_brilliant_scientist_directorate.gui` |
| Compact branch | `kruger_directorate_compact_panel` | `interface/016_brilliant_scientist_directorate.gui` |
| Expanded branch | `kruger_directorate_full_panel` | `interface/016_brilliant_scientist_directorate.gui` |
| Open control | `kruger_directorate_open_button`, `kruger_directorate_open_button_click` | GUI and scripted GUI |
| Close control | `kruger_directorate_close_button`, `kruger_directorate_close_button_click` | GUI and scripted GUI |
| Event-owned GFX | `GFX_kruger_directorate_background`, `GFX_kruger_directorate_compact_header` | `interface/016_brilliant_scientist_directorate.gfx` |
| Profile sprites | `GFX_kruger_directorate_profile_human`, `GFX_kruger_directorate_profile_secured`, `GFX_kruger_directorate_profile_sovereign` | `interface/016_brilliant_scientist_directorate.gfx` |
| Meter sprite families | `GFX_kruger_directorate_mandate_*`, `GFX_kruger_directorate_dependence_*`, `GFX_kruger_directorate_exposure_*`, `GFX_kruger_directorate_capacity_*` | `interface/016_brilliant_scientist_directorate.gfx` |
| Portrait consumers | `GFX_portrait_KRG_doctor_warren_kruger_stage_0`, `GFX_portrait_KRG_doctor_warren_kruger_stage_4_machine` | `interface/016_brilliant_scientist.gfx` |
| GUI localisation | `brilliant_scientist_directorate_gui_*` active title, value, tooltip, control, and footer keys | `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml` |
| Scripted localisation | `GetBrilliantScientistDirectorateProfileFrameSprite`, `GetBrilliantScientistDirectoratePortraitSprite`, the four meter sprite functions, `GetBrilliantScientistDirectorateProfileRole`, `GetBrilliantScientistDirectorateFooter` | `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt` |

Representative decision entry points for the board contexts are `brilliant_scientist_convene_public_science_council`, `brilliant_scientist_approve_selected_project`, `brilliant_scientist_formalize_primary_research_campus`, `brilliant_scientist_review_foreign_approaches`, `brilliant_scientist_release_kruger`, and `brilliant_scientist_sovereignty_deadline_mission`.

## Files changed in this pass

Only this handoff was added by this worker: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_directorate_gui_visual_closure_2026-09-05.md`.

No Event 016 runtime byte was changed by this worker.

During the pass, concurrent work appeared on the same scoped files: `git status` reported `MM` for `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt` and `M` for `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml`.

The scripted-GUI working tree still contains the conditional phase-exclusive click gates described below, while its staged index contains an unrelated `always = yes` toggle revision; this worker did not stage, unstage, revert, or reconcile it.

The localisation working-tree change is the unrelated dormant key `brilliant_scientist_directorate_gui_singularity_verified_nonterminal`; this worker did not touch or reconcile it.

The GUI layout and GFX files were unchanged during the pass: `interface/016_brilliant_scientist_directorate.gui` and `interface/016_brilliant_scientist_directorate.gfx`.

The current hashes are `F6DCCA5F96EC0B54961AA630D42E5750E191F33CAA9A3BD64DAE8E9D865EF845` for the scripted GUI, `BC055E2793BE32E9EA2D520259B2EE3F8C03C40AD903E2209844FE4DDDC72E19` for the GUI layout, `A6C7E027D4E4E12D4181378F057EB54F790716D3BA9DB5C83F08A1363288DCDB` for GFX, and `F1903837A1990CF19A8708F4D1ED186C29679BDF5E13749EBFA5C470179C674C` for localisation.

`docs/events/016_brilliant_scientist/systems/directorate.md` was reviewed and left unchanged.

## References inspected

The required offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding were read before source review.

The installed vanilla documentation `documentation/script_concept_documentation.md`, `documentation/loc_formatter_documentation.md`, `documentation/loc_objects_documentation.md`, and `common/scripted_guis/_documentation.md` were consulted.

Vanilla decision-category precedents inspected were `common/scripted_guis/USA_congress_scripted_gui.txt` with `interface/usa_congress_scripted_gui.gui` and `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt` with `interface/sov_paranoia_system_scripted_gui.gui`.

Event 016 precedents inspected were the 2026-09-02 final closure handoff, the 2026-08-25 GUI audit, the 2026-08-15 compact redesign, the background refresh and colour-pass handoffs, and the current Directorate system document.

## Layout hierarchy and background coverage

The root is a clipped 500x360 container at `(0,0)`.

The collapsed branch is a clipped 500x58 panel with the 500x58 `GFX_kruger_directorate_compact_header` at `(0,0)`, the compact title at `(40,16)` in a 360x24 box, and the 36x36 open control at `(422,11)`.

The expanded branch is a clipped 500x360 panel with the 500x360 `GFX_kruger_directorate_background` at `(0,0)`, the centered title at `(40,22)` in a 360x28 box, and the 36x36 close control at `(422,11)`.

The profile frame is at `(38,80)` with scale `0.68`, the portrait is at `(42,84)` with scale `0.68`, and the centered profile name occupies `(32,234)` with width 138 and height 22.

The four meter sprites are at `(176,82)`, `(176,126)`, `(176,170)`, and `(176,214)`.

The matching value boxes are left-aligned at `(304,89)`, `(304,133)`, `(304,177)`, and `(304,221)` with width 154 and height 22.

The role and government-control summary is centered at `(36,272)` with width 428 and height 30, and the footer is centered at `(36,326)` with width 428 and height 20.

The compact header covers the collapsed panel only, and the Directorate background covers the expanded panel only.

The profile frame, portrait, meter sprites, text, and phase control intentionally draw above their matching background artwork.

The current parent-installed background is `gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds`, registered as `GFX_kruger_directorate_background`, with SHA-256 `C476E06B722EE6C41A07B85AFDD257B2232744F9D50185A2D0AD5068D080026D`.

## Budget and text-density audit

Visible mechanic values are exactly four: Mandate, Dependence, Exposure, and Capacity.

The surface has one presentation toggle in each mutually exclusive phase and zero gameplay-changing controls.

No cost is displayed, so the spendable-cost count is zero and texticon coverage is not applicable.

The four meter tooltips stay adjacent to the meters and explain what the value measures, what changes it, why the threshold matters, and which existing decision family responds to it.

The title, profile name, four value labels, role/control line, footer, open tooltip, and close tooltip are concise.

The active surface contains no raw trigger dump, requirement dump, project ledger, facility list, foreign roster, authority history, or mixed cost string.

The dormant legacy localisation keys remain unbound and were not removed because this pass does not own a broad localisation cleanup.

## Context and state matrix

| Accepted context | Compact-display equivalence | Action owner |
| --- | --- | --- |
| Overview | Profile, role/control line, four headline meters, and footer | Existing Event 016 decisions below the category |
| Projects | Capacity meter and capacity tooltip | Event 016 project-board decisions |
| Facilities | Capacity meter and role/control line | Event 016 facility decisions |
| Foreign | Exposure meter and government-control line | Event 016 foreign decisions |
| Authority | Mandate meter and role/control line | Event 016 containment and sovereignty decisions |

| State | Existing typed scenario or prior gallery evidence | Current disposition |
| --- | --- | --- |
| Expanded normal | `event016_directorate_actual_normal_expanded` | Last-known v3 production evidence shows the human frame, stage-0 portrait, baseline values, host role/control line, and footer without clipping |
| Collapsed normal | `event016_directorate_actual_normal_collapsed` | Last-known v3 production evidence shows only the compact header, title, and open control |
| Expanded severe host | `event016_directorate_actual_severe_host` | Last-known v3 production evidence shows the secured frame, machine-stage portrait, maximum values, longest host role/control line, and host footer without clipping |
| Expanded severe sovereign | `event016_directorate_actual_severe_sovereign` | Last-known v3 production evidence shows the sovereign frame and longest sovereign footer without clipping |
| Hover, selected, locked, disabled, warning, active, completed | Prior generic gallery coverage in the 2026-09-02 closure handoff | Fresh rerender blocked by current MCP timeout; no selected or locked gameplay action exists on this read-only surface |
| Empty-list, full-list, minimum-value, maximum-value | Prior generic gallery and typed low/high-value coverage | Fresh rerender blocked; no list was added and the four meters remain the only visible values |
| Long-text and missing-localisation | Prior synthetic stress gallery | Fresh rerender blocked; actual reachable Event 016 strings were previously reported within their boxes, while synthetic arbitrary long text intentionally exceeds fixed boxes |

## MCP evidence

The fresh exact-window inspect selector was `mcp__hoi4_agent_tools__hoi4_gui_inspect` with `windowName = "kruger_directorate_container"`, workspace `mod_chaos_redux_ea3b2d67c2c0`, and scenario objects such as `{ "id": "event016_directorate_actual_normal_expanded" }`.

The related-scenario inspect request timed out after the server's 180-second boundary.

The single-scenario inspect requests with `event016_directorate_compact_current`, `event016_directorate_actual_normal_expanded`, and `generatedScenarios = { "enabled": false }` each timed out after 180 seconds.

The same single-scenario inspect without an explicit workspace id also timed out after 180 seconds.

The exact fresh render selector was `mcp__hoi4_agent_tools__hoi4_gui_render` with `windowName = "kruger_directorate_container"`, scenario `{ "id": "event016_directorate_actual_normal_expanded" }`, resolutions 1366x768, 1920x1080, and 2560x1440 at UI scale 1, and the requested normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states.

That fresh render timed out after 180 seconds and returned no artifact.

No fresh inspect or render artifact was produced in this pass, so source review and the retained 2026-09-02 captures are not presented as current production evidence.

The last-known post-v3 inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8ccb9cdc9a5a2dca85641ee8e55d4f75c6da9b8d65977e81b7b2881f11d8561/5dd8f2d5f43bdc60b3d4a465cd61615fd13b808b12c5d39642186032bd757911/gui-inspect.e95d541052b101b4.json`.

That retained inspect reported 22 elements, no missing Event 016 assets, no conflicting click-region diagnostic, intentional background-child layering overlaps, hidden-branch zero-size diagnostics from offline visibility modeling, and partial four-frame button-state rendering because `gfx/FX/buttonstate.lua` is not executed by the offline renderer.

The last-known post-v3 production artifacts are the normal-expanded full and 1366x768/1920x1080/2560x1440 matrix at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94061c8bcee17dd70985ba088ef5477981f3f9c13970ef122734714cf45c822b/e3c5b9278be8c74fac6f7c1dc9310931b7ce899039d3ed103ca9aa58d85dd341/kruger_directorate_container-full.png` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/430ceeab89b345b249ce342589a29bb84180cad9f303b5279757c7d7e36f8ed1/4e7f1b404ea563d3b54670c1f89f1af1704f453f5d01786d6a325ade0e6ad0b7/kruger_directorate_container-resolution-scale.png`.

The retained severe-host full and matrix artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88cb0097637672d0ff9e2be6a0b41529f007766e0b2ef3fe472667b862bd0d5a/de137f1f7c7da548b13fe1c09c2e7ee1971d5abfff3c10bf451b2fb60f124ae9/kruger_directorate_container-full.png` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d721a272959e8ae25705c1650ba7da070ff22d091bbb2293858062cb4a3a385e/3cccdc8b832a184b74e01492447430bb108b0bf654469a00baf579ad98adc6a7/kruger_directorate_container-resolution-scale.png`.

The retained severe-sovereign full and matrix artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ab715b161b6a81d0295c83a8fc7abeb1fbfeb3c433ec6eaaa9d99246a834426/aa9ca0edadbd8f8cc0fed8c17eee15949536fd7fb75fa84ad1f6444a34d10e75/kruger_directorate_container-full.png` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/892d6a7ff2a7b6adf0ca9b90ff612cec6e86f32599e3279f17e08cb5153ace63/194bab88eeb36a6f3e695791b80e0b789e3d02750ff85a02957b55a901572362/kruger_directorate_container-resolution-scale.png`.

The retained collapsed full and matrix artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4be3c43ca18b2c4f63b930e1a93b6e10e00c4d4ca41bf8d43a8903eee4f0a6e9/8148ea0da512c3af0e84f6feb5c5dbcdc96c8fad40bd18d226a3aa75e097d82e/kruger_directorate_container-full.png` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0850c94371215b3d8fdcd5a6a7bd68143190d99e07ccce88fbde31205dd9058c/d252ac46b09585be129835f60bb1ae8a0647d31754132be40febda181ede52e2/kruger_directorate_container-resolution-scale.png`.

The retained no-op rewrite comparison reports `changedPixels = 0` and `changedRatio = 0` at 1920x1080 in `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/e8be6ebec3114d1302debd364116e21552cb9edc61763c2674950c09713a5750/kruger_directorate_container-visual-diff.json`.

Because this pass made no runtime source change, no fresh `hoi4.gui_rewrite` or post-change comparison was invoked; the retained no-op rewrite evidence remains the applicable source comparison.

## Before and after behavior and visual rationale

The current source preserves the 2026-09-02 action-integrity fix: the open control is enabled only while `brilliant_scientist_directorate_gui_collapsed` is set, and the close control is enabled only while that flag is absent.

The open effect still clears the flag and the close effect still sets it.

The compact and expanded visibility gates, background coverage, profile layering, four meter rows, text boxes, tooltips, and footer were not changed.

The retained production captures show the intended 44px meter rhythm, aligned value baselines, centered title, readable profile name, readable role/control line, intact lower trim, and no visible clipping or overflow in the reachable normal and severe strings.

No proven visual defect was available to justify a geometry or localisation edit after the current MCP route failed to return.

## Assets and handoff routing

All active background, header, profile-frame, meter, portrait, and open/close-control sprites resolve to Event 016 package paths under `gfx/interface/016_brilliant_scientist/directorate/` or the existing Event 016 portrait GFX file.

No missing or placeholder asset was exposed by the retained inspect or production captures.

The v3 background replacement was parent-owned and is not regenerated or edited here.

No new asset handoff was routed because the current package already contains the required static decoration and no production render exposed an asset defect.

## Parent-owned remainder and blockers

The parent retains gameplay outcomes, decision and mission costs, effects, AI, weights, runtime state setup, Event Log and Event Details, the decision-category host, and live in-game validation.

The user retains live save, reload, consumer, resolution, and button-state acceptance.

The fresh MCP blocker is the exact 180-second timeout for `hoi4.gui_inspect` and `hoi4.gui_render` on `kruger_directorate_container` in workspace `mod_chaos_redux_ea3b2d67c2c0`; no fresh artifact, hierarchy view, click-region view, state gallery, resolution matrix, or current comparison was returned.

The offline renderer's synthetic long-text overflow, hidden-branch zero-size diagnostics, and unexecuted four-frame buttonstate shader remain unresolved evidence limits rather than source changes.

The compact design intentionally does not materialize five tabs; Overview, Projects, Facilities, Foreign, and Authority are context equivalences backed by existing decisions. Converting them into tabs would be a design and gameplay-surface expansion outside this bounded visual pass.

This handoff therefore records the UI as visually unchanged and last-known post-v3 clean, but does not claim fresh MCP visual completion until the exact route responds.
