# Event 016 final Directorate GUI closure

Status: bounded Event 016 scripted-GUI closure implemented, rechecked against the installed v3 background, and visually reviewed by the parent; the user owns live consumer acceptance.

## Ownership and scope proof

Event id and slug: Event 016, `brilliant_scientist`.

The dedicated surface is event-owned because `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt` attaches `brilliant_scientist_directorate_scripted_gui` directly to the event-owned `brilliant_scientist_directorate_category`.

The attached scripted GUI declares `context_type = decision_category` and `window_name = "kruger_directorate_container"` in `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.

The independent `containerWindowType` named `kruger_directorate_container` is defined only in `interface/016_brilliant_scientist_directorate.gui`.

The category and decision entry points were inspected read-only; no category, decision, mission, effect, cost, AI, weight, country, focus, or shared interface source was changed.

The accepted surface remains the compact read-only record with four visible values: Mandate, Dependence, Exposure, and Capacity.

Independent Capacity and Grievance remain hidden implementation state and were not promoted to visible values.

The accepted Overview, Projects, Facilities, Foreign, and Authority plan contexts are treated as board-context equivalences, not GUI tabs, and no removed tab or dashboard feature was restored.

## Exact identifiers and source graph

| Surface | Exact identifier | Owning file or route |
| --- | --- | --- |
| Event-owned decision category | `brilliant_scientist_directorate_category` | `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt` |
| Scripted GUI | `brilliant_scientist_directorate_scripted_gui` | `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt` |
| GUI root | `kruger_directorate_container` | `interface/016_brilliant_scientist_directorate.gui` |
| Compact child | `kruger_directorate_compact_panel` | `interface/016_brilliant_scientist_directorate.gui` |
| Expanded child | `kruger_directorate_full_panel` | `interface/016_brilliant_scientist_directorate.gui` |
| Open control | `kruger_directorate_open_button` and `kruger_directorate_open_button_click` | GUI and scripted GUI above |
| Close control | `kruger_directorate_close_button` and `kruger_directorate_close_button_click` | GUI and scripted GUI above |
| Event-owned GFX | `GFX_decision_category_brilliant_scientist_directorate`, `GFX_kruger_directorate_background`, `GFX_kruger_directorate_compact_header` | `interface/016_brilliant_scientist_directorate.gfx` |
| Profile sprites | `GFX_kruger_directorate_profile_human`, `GFX_kruger_directorate_profile_secured`, `GFX_kruger_directorate_profile_sovereign` | `interface/016_brilliant_scientist_directorate.gfx` |
| Meter sprites | `GFX_kruger_directorate_mandate_low`, `GFX_kruger_directorate_mandate_moderate`, `GFX_kruger_directorate_mandate_high`, `GFX_kruger_directorate_mandate_extreme`, `GFX_kruger_directorate_dependence_low`, `GFX_kruger_directorate_dependence_moderate`, `GFX_kruger_directorate_dependence_high`, `GFX_kruger_directorate_dependence_extreme`, `GFX_kruger_directorate_exposure_low`, `GFX_kruger_directorate_exposure_moderate`, `GFX_kruger_directorate_exposure_high`, `GFX_kruger_directorate_exposure_extreme`, `GFX_kruger_directorate_capacity_low`, `GFX_kruger_directorate_capacity_moderate`, `GFX_kruger_directorate_capacity_high`, and `GFX_kruger_directorate_capacity_extreme` | `interface/016_brilliant_scientist_directorate.gfx` |
| Portrait sprites | `GFX_portrait_KRG_doctor_warren_kruger_stage_0` and `GFX_portrait_KRG_doctor_warren_kruger_stage_4_machine` | `interface/016_brilliant_scientist.gfx` |
| GUI localisation | `brilliant_scientist_directorate_gui_compact_title`, `brilliant_scientist_directorate_gui_open_tt`, `brilliant_scientist_directorate_gui_title`, `brilliant_scientist_directorate_gui_close_tt`, `brilliant_scientist_directorate_gui_profile_name`, `brilliant_scientist_directorate_gui_role_control`, `brilliant_scientist_directorate_gui_mandate`, `brilliant_scientist_directorate_gui_dependence`, `brilliant_scientist_directorate_gui_exposure`, `brilliant_scientist_directorate_gui_capacity`, the four `*_tt` keys, and `brilliant_scientist_directorate_gui_footer` | `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml` |
| Scripted localisation | `GetBrilliantScientistDirectorateProfileFrameSprite`, `GetBrilliantScientistDirectoratePortraitSprite`, `GetBrilliantScientistDirectorateMandateSprite`, `GetBrilliantScientistDirectorateDependenceSprite`, `GetBrilliantScientistDirectorateExposureSprite`, `GetBrilliantScientistDirectorateCapacitySprite`, `GetBrilliantScientistDirectorateProfileRole`, and `GetBrilliantScientistDirectorateFooter` | `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt` |

Representative decision entry points that own the board contexts are `brilliant_scientist_convene_public_science_council`, `brilliant_scientist_approve_selected_project`, `brilliant_scientist_formalize_primary_research_campus`, `brilliant_scientist_review_foreign_approaches`, `brilliant_scientist_release_kruger`, and `brilliant_scientist_sovereignty_deadline_mission` in the event-owned 016 decision files.

No broader localisation edit was needed. The parent-installed v3 background is an existing-art replacement at the exact runtime identifier and path; this worker made no GUI or art source edit in this verification pass.

## Files changed

The only gameplay-adjacent source change is the presentation-control patch in `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.

`kruger_directorate_open_button_click_enabled` now requires `has_country_flag = brilliant_scientist_directorate_gui_collapsed`.

`kruger_directorate_close_button_click_enabled` now requires `NOT = { has_country_flag = brilliant_scientist_directorate_gui_collapsed }`.

The patch makes the two existing same-rectangle controls mutually exclusive in runtime state without changing their click effects, costs, outcomes, AI, or decision availability.

The handoff file is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_directorate_gui_closure_2026-09-02.md`.

`interface/016_brilliant_scientist_directorate.gui` was not changed and remains SHA-256 `BC055E2793BE32E9EA2D520259B2EE3F8C03C40AD903E2209844FE4DDDC72E19`.

The post-change scripted-GUI file is SHA-256 `F6DCCA5F96EC0B54961AA630D42E5750E191F33CAA9A3BD64DAE8E9D865EF845`.

`interface/016_brilliant_scientist_directorate.gfx`, linked localisation, scripted localisation, category registration, and decision entry files were not changed.

The parent-installed runtime background is `gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds` under the existing `GFX_kruger_directorate_background` identifier. Its current SHA-256 is `C476E06B722EE6C41A07B85AFDD257B2232744F9D50185A2D0AD5068D080026D`; this asset installation was parent-owned and no art bytes were edited by this worker.

## References inspected

The required offline Paradox wiki pages were read for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, Scripted GUI modding, and Graphical asset modding.

The required installed-game documentation was read from `documentation/script_concept_documentation.md`, `documentation/loc_formatter_documentation.md`, and `documentation/loc_objects_documentation.md`.

The exact vanilla precedent inspected was the decision-category `usa_congress_decision_ui` scripted GUI in `common/scripted_guis/USA_congress_scripted_gui.txt` and its compact `interface/usa_congress_scripted_gui.gui` window.

Chaos Redux precedents inspected were `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_directorate_gui_audit_2026-08-25.md`, `016_current_mcp_audit_2026-08-26.md`, `016_final_closure_baselines_2026-09-01.md`, `016_final_closure_resume_reconcile_2026-09-02.md`, `016_directorate_compact_redesign_2026-08-15.md`, and the accepted Event 016 host-directorate specification.

## Layout hierarchy and coverage map

The root is a clipped 500x360 container at 0,0.

The compact branch is a clipped 500x58 panel at 0,0 with a 500x58 header sprite, title at x40 y16 in a 360x24 text box, and a 36x36 open control at x422 y11.

The expanded branch is a clipped 500x360 panel at 0,0 with the 500x360 Directorate background, title at x40 y22 in a 360x28 text box, and a 36x36 close control at x422 y11.

The profile frame is at x38 y80 with scale 0.68, the canonical portrait is at x42 y84 with scale 0.68, and the profile name is centered at x32 y234 in a 138x22 box.

The four meter icons are at x176 y82, x176 y126, x176 y170, and x176 y214.

The four corresponding values are at x304 y89, x304 y133, x304 y177, and x304 y221 in 154x22 left-aligned boxes.

The role and government-control summary is centered at x36 y272 in a 428x30 box, and the footer is centered at x36 y326 in a 428x20 box.

The compact header artwork covers only the compact panel, and the Directorate artwork covers only the expanded panel; the profile frame, portrait, meter icons, text, and controls intentionally draw above their background artwork.

The overlap diagnostics between a background and its painted children are intentional z-order layering, while the pre-change overlap between the open and close controls was a real action-integrity defect.

## Board-context equivalence map

| Accepted board context | Current compact display equivalence | Action ownership |
| --- | --- | --- |
| Overview | Profile and role/control line plus all four headline meters and the footer | Existing decisions below the category |
| Projects | Capacity meter and capacity tooltip summarize the visible project-work pressure | Project-board decisions remain below the category |
| Facilities | Capacity meter and role/control line summarize laboratory and staff reach | Facility decisions remain below the category |
| Foreign | Exposure meter and government-control line summarize external pressure | Foreign decisions remain below the category |
| Authority | Mandate meter and role/control line summarize authority pressure | Containment and sovereignty decisions remain below the category |

No tab, tab click region, card list, fifth meter, or hidden-state dump was restored.

## Value, action, text, and cost budgets

Visible mechanic values are exactly four: Mandate, Dependence, Exposure, and Capacity.

Independent Capacity and Grievance remain hidden, keeping the visible-value budget within the accepted four-value ceiling.

The surface has one presentation toggle per visible phase: open while collapsed and close while expanded.

Neither control is a gameplay-changing action and neither control displays a spendable cost.

The four meter tooltips remain adjacent to their values and explain the current meaning, the direction of consequence, and which existing decision family changes the pressure.

The title, profile, role/control summary, footer, and four value labels remain concise in the linked localisation.

The reachable scripted-localisation alternatives were enumerated before the targeted production-text run. The title is fixed as `THE KRUGER DIRECTORATE`, the profile name is fixed as `Dr. Warren Kruger`, the role alternatives are `Kruger State director`, `National science director`, `Concealed programme director`, and `Appointment under review`, the control alternatives are `Secure`, `Contested`, `Compromised`, `Lost`, and `Unassessed`, and the footer alternatives are the host and sovereign strings recorded below.

The four displayed variables are clamped to 0..100 by the Event 016 state logic, so the actual maximum display strings are `Mandate 100`, `Dependence 100`, `Exposure 100`, and `Capacity 100` after formatting tags are rendered.

The longest reachable host role/control line is `Concealed programme director | Government control: Compromised`. The longest reachable footer is the sovereign branch `Kruger State orders remain in its sovereign decision categories.`.

The actual production scenarios below use these exact reachable outputs and `state = normal`; they do not use the renderer's synthetic arbitrary long-text samples.

The long-text renderer state was exercised as a synthetic stress state; it injects multi-line samples that exceed the fixed compact text boxes, which is recorded under unresolved renderer evidence below rather than used as a reason to expand the accepted window.

No literal resource-name fallback or spendable texticon is present because the bounded GUI exposes no gameplay cost.

## State matrix

| State or variant | Typed scenario or render coverage | Result |
| --- | --- | --- |
| Expanded normal | `event016_directorate_actual_normal_expanded` | Full panel, human portrait stage, public baseline values, `National science director | Government control: Secure`, host footer, close enabled, open hidden; validation passed |
| Collapsed normal | `event016_directorate_actual_normal_collapsed` | Compact 500x58 panel, exact `Kruger Directorate` title, open enabled, close hidden; validation passed |
| Expanded severe host | `event016_directorate_actual_severe_host` | Secured profile frame, stage-4 machine portrait, all four visible values at 100, longest host role/control line, host footer, close enabled, open hidden; validation passed |
| Expanded severe sovereign | `event016_directorate_actual_severe_sovereign` | Sovereign profile frame, stage-4 machine portrait, all four visible values at 100, sovereign role/control line, longest sovereign footer, close enabled, open hidden; validation passed |
| Hover | Expanded severe and collapsed severe related scenarios plus generic hover gallery state | Only the visible phase control is interactive; offline button sheet is limited to frame 1/4 |
| Disabled | Generic disabled gallery state and the prior synthetic long-text typed probe | Disabled-state coverage is diagnostic only; no dead second control is exposed in the actual expanded/collapsed branches |
| Selected and locked | Generic renderer state gallery | Rendered as state coverage only because this read-only surface has no selected or locked action control |
| Warning and active | Severe expanded and collapsed related scenarios | Visual state coverage with high/extreme meter inputs and severe portrait stage |
| Completed | Generic renderer state gallery | No dynamic list or completion action exists on this compact surface; state is intentionally a no-op presentation probe |
| Empty-list and full-list | Generic renderer state gallery | Empty-list and full-list map to the compact record's no-list surface; no list was added to satisfy a generic state name |
| Minimum-value and maximum-value | Low and high/extreme meter sprite inputs | Four meters remain the only visible mechanic values |
| Long-text | Explicit synthetic long-text related scenario and generic long-text gallery state | Synthetic samples intentionally exceed fixed boxes; the actual reachable maximum-value/role/footer scenarios report no text overflow |
| Missing-localisation | Generic renderer state gallery | Linked Event 016 GUI keys resolve; no localisation file was changed |

## Resolution matrix

| Resolution | UI scale | Coverage | Result |
| --- | --- | --- | --- |
| 1366x768 | 1 | Expanded and collapsed render runs | No resolution drift reported; compact geometry remains within the root |
| 1920x1080 | 1 | Expanded, collapsed, and comparison baseline | Reference scale; no geometry change |
| 2560x1440 | 1 | Expanded and collapsed render runs | No resolution drift reported; compact geometry remains within the root |

The following local production PNGs are the targeted actual-text artifacts. Each `resolution-scale.png` contains the corresponding branch at 1366x768, 1920x1080, and 2560x1440 in its three labeled columns; each `full.png` is the 1920x1080 production view for the same scenario.

The local paths below were verified during the 2026-09-02 targeted production rerender pass; the MCP URIs in the post-v3 evidence section are canonical while their provenance manifests remain available.

The earlier local PNG paths were genuinely evicted from the shared artifact mirror after the prior render batch, while the collapsed artifact survived; the renderer does not expose a retention policy, but the eviction was observed after parallel MCP activity and is not a source or geometry change.

| Actual scenario | Full production PNG | Three-resolution production PNG |
| --- | --- | --- |
| Normal expanded | `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\94\94061c8bcee17dd70985ba088ef5477981f3f9c13970ef122734714cf45c822b\kruger_directorate_container-full.png` | `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\43\430ceeab89b345b249ce342589a29bb84180cad9f303b5279757c7d7e36f8ed1\kruger_directorate_container-resolution-scale.png` |
| Normal collapsed | `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\4b\4be3c43ca18b2c4f63b930e1a93b6e10e00c4d4ca41bf8d43a8903eee4f0a6e9\kruger_directorate_container-full.png` | `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\08\0850c94371215b3d8fdcd5a6a7bd68143190d99e07ccce88fbde31205dd9058c\kruger_directorate_container-resolution-scale.png` |
| Severe host role/control | `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\88\88cb0097637672d0ff9e2be6a0b41529f007766e0b2ef3fe472667b862bd0d5a\kruger_directorate_container-full.png` | `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\d7\d721a272959e8ae25705c1650ba7da070ff22d091bbb2293858062cb4a3a385e\kruger_directorate_container-resolution-scale.png` |
| Severe sovereign role/footer | `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\8a\8ab715b161b6a81d0295c83a8fc7abeb1fbfeb3c433ec6eaaa9d99246a834426\kruger_directorate_container-full.png` | `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\89\892d6a7ff2a7b6adf0ca9b90ff612cec6e86f32599e3279f17e08cb5153ace63\kruger_directorate_container-resolution-scale.png` |

Stable review copies were copied from the verified MCP artifact-cache PNGs into the Event016 evidence folder so parent review does not depend on cache retention: normal expanded full `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/evidence/016_directorate_gui_current_production_2026-09-02/event016_directorate_actual_normal_expanded-full-1920x1080.png` is 284,995 bytes with SHA-256 `94061C8BCEE17DD70985BA088EF5477981F3F9C13970EF122734714CF45C822B`, and severe host full `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/evidence/016_directorate_gui_current_production_2026-09-02/event016_directorate_actual_severe_host-full-1920x1080.png` is 283,872 bytes with SHA-256 `88CB0097637672D0FF9E2BE6A0B41529F007766E0B2EF3FE472667B862BD0D5A`.

## Pre-change MCP evidence

The exact-window baseline inspect used window `kruger_directorate_container` and scenario `event016_directorate_compact_current`.

Baseline inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5956a5b226e0dbf4cf04fb68819fc3c84768086bf1e8911f403d755adbd3274/720fe12c5e5775217dc453e6c8af517b9eeaba8ba2f40307ce090c0adc768490/gui-inspect.99725c6e1ecea142.json`.

Baseline render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ecfb9b4e5301c3210d6b950dd6f990003c162cd9ed1eba1d25885bf324c7bfe5/1f84dc7d0ea4103cf6eda57cf5aecab2dbfc5ccd17a67e11228913334d221c54/kruger_directorate_container-full.svg`.

The baseline reported `GUI_CONFLICTING_CLICK_REGIONS` for open and close at 100.0% overlap and `GUI_Z_ORDER_RISK` because the full panel could cover the clickable open control.

The baseline also reported intentional background-child visible overlaps and `GUI_SPRITE_RENDER_PARTIAL` for both four-frame controls because `gfx/FX/buttonstate.lua` is not executed by the offline renderer.

The previous closure artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/479cacfeb9ae0530a784d635e2268745aec6b46c580817152a3fecab4de5b58c/decb4e4b2fb3941cd219f9ceb35f448adc9fe34b1a8bc7485238e0e9adfd3268/gui-inspect.c0a7a76c2f618267.json` recorded the same validation failure and was used as historical evidence only.

## Rewrite route and post-change MCP evidence

An initial `hoi4.gui_rewrite` attempt against `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt` was correctly rejected with `GUI_TEXT_PACKAGE_PATH_UNSUPPORTED` because the main rewrite path must be a `.gui` under the configured interface root.

A correct `.gui` source-package rewrite including the presentation-only scripted GUI file was attempted after baseline inspect and render, but the MCP call timed out after 180 seconds without changing either source file.

A correct targeted rewrite pass then checked the root `clipping = yes` scalar in `interface/016_brilliant_scientist_directorate.gui` with the current source hash and returned `GUI_CHANGES_UNCHANGED` with validation passed.

Rewrite validation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50f3643bb0a6432b4be600b03adeb0cd2c0a0b341ca892017a36a2820b24dac9/e8e6b6245b7b03854d463996d54873a9fbd177ef1a424b28f2e93e8061ad5e85/kruger_directorate_container-rewrite-validation.json`.

Rewrite proposed fidelity artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c151035bc3c00cbe56fd0731b616bb645bca08d499942460e5660fd0e70093a9/4466e550e429aee0c2a455dfb2571a5b61bc596ad42020879d596d724080b021/kruger_directorate_container-proposed-fidelity.json`.

Rewrite before, proposed, and visual-diff artifacts were generated for the no-op geometry comparison.

Rewrite before PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a03999ac80cee083fc5d780f9b8125e2c62c2803f79bdb23f9c7872013a85e5/58c3c44b8078c6b1f3511ade56b707388513e1d6ef58adf535aad341c4ce1963/kruger_directorate_container-before.png`.

Rewrite proposed PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a03999ac80cee083fc5d780f9b8125e2c62c2803f79bdb23f9c7872013a85e5/9fc9a07d7532c72b7ef5a920f7c6ca65f0051ba2623b7ce16be0f13af91c8bb9/kruger_directorate_container-proposed.png`.

Rewrite visual-diff JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/e8be6ebec3114d1302debd364116e21552cb9edc61763c2674950c09713a5750/kruger_directorate_container-visual-diff.json`.

The no-op visual diff reports `changedPixels: 0` and `changedRatio: 0` at 1920x1080, confirming that compact geometry and existing art were preserved.

Post-change typed expanded inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06ec5d6caab29c6e063e8da1c390352b4421905b0726400646acc479af0c3d61/7d8d4046977ba85b8831cc5e3ac8c2af8f5df81b780618314604dd48a2085342/gui-inspect.795ea34da9ca711c.json`.

Post-change typed collapsed inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d96412ad6c30a21e79bb413e0686c4c9f1e891f4f23aa07f444f4d441c688436/14646b8fb2d047f5b567fc9becb39df6945694c3c924ce35bd0a100091075b/gui-inspect.795ea34da9ca711c.json`.

Post-change typed related-state inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c5ffc18bc8ef2caf2988a8127d0c3f5af85bf250f6dc6c03f909754e2a569f9/a243c68a19a3d9c2a84c871eb5f0da1ce78a3ae1e698f5b5f6f9acd6c33aa480/gui-inspect.795ea34da9ca711c.json`.

Latest post-change typed expanded/collapsed inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4aef0a3d84eb918a8b387d16080dfa6dc07a9cca0146a934d1a2833a203a2946/8f938fedca08e90b249c16f26a29e11f2875eb0e0bb5f8e7455819bb51cd0ec5/gui-inspect.78b4693606898a63.json`.

Targeted actual-text inspect artifact for `event016_directorate_actual_normal_expanded`, `event016_directorate_actual_normal_collapsed`, `event016_directorate_actual_severe_host`, and `event016_directorate_actual_severe_sovereign`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87966aa070af399bfecf8f2c360d6ae5c79cc34ad3882eb48b9fa98c2240e761/4d6c8d9129ad1d90cbf4471603450cc2cb232e244ef1caa3d67f162b59a663ba/gui-inspect.00130a76834307f9.json`.

Post-change typed inspect validation passed, with 22 elements, no missing assets, no conflicting click-region diagnostic, and only non-blocking painted-background overlaps plus hidden-branch zero-size diagnostics.

Current post-v3 typed inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8ccb9cdc9a5a2dca85641ee8e55d4f75c6da9b8d65977e81b7b2881f11d8561/5dd8f2d5f43bdc60b3d4a465cd61615fd13b808b12c5d39642186032bd757911/gui-inspect.e95d541052b101b4.json`. Its shared source revision is `e95d541052b101b4e13315b29229f29a2bf93d10d61d274f501932f2acc3d415`, and validation passed with 22 inspected elements, no missing assets, and no conflicting click-region diagnostic.

Current post-v3 production full-window and three-resolution artifacts are retained at the following MCP URIs: normal expanded PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94061c8bcee17dd70985ba088ef5477981f3f9c13970ef122734714cf45c822b/e3c5b9278be8c74fac6f7c1dc9310931b7ce899039d3ed103ca9aa58d85dd341/kruger_directorate_container-full.png` with matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/430ceeab89b345b249ce342589a29bb84180cad9f303b5279757c7d7e36f8ed1/4e7f1b404ea563d3b54670c1f89f1af1704f453f5d01786d6a325ade0e6ad0b7/kruger_directorate_container-resolution-scale.png`; normal collapsed PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4be3c43ca18b2c4f63b930e1a93b6e10e00c4d4ca41bf8d43a8903eee4f0a6e9/8148ea0da512c3af0e84f6feb5c5dbcdc96c8fad40bd18d226a3aa75e097d82e/kruger_directorate_container-full.png` with matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0850c94371215b3d8fdcd5a6a7bd68143190d99e07ccce88fbde31205dd9058c/d252ac46b09585be129835f60bb1ae8a0647d31754132be40febda181ede52e2/kruger_directorate_container-resolution-scale.png`; severe host PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88cb0097637672d0ff9e2be6a0b41529f007766e0b2ef3fe472667b862bd0d5a/de137f1f7c7da548b13fe1c09c2e7ee1971d5abfff3c10bf451b2fb60f124ae9/kruger_directorate_container-full.png` with matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d721a272959e8ae25705c1650ba7da070ff22d091bbb2293858062cb4a3a385e/3cccdc8b832a184b74e01492447430bb108b0bf654469a00baf579ad98adc6a7/kruger_directorate_container-resolution-scale.png`; and severe sovereign PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ab715b161b6a81d0295c83a8fc7abeb1fbfeb3c433ec6eaaa9d99246a834426/aa9ca0edadbd8f8cc0fed8c17eee15949536fd7fb75fa84ad1f6444a34d10e75/kruger_directorate_container-full.png` with matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/892d6a7ff2a7b6adf0ca9b90ff612cec6e86f32599e3279f17e08cb5153ace63/194bab88eeb36a6f3e695791b80e0b789e3d02750ff85a02957b55a901572362/kruger_directorate_container-resolution-scale.png`.

The refreshed PNG resource links were read successfully through the `hoi4_agent_tools` artifact template with complete byte ranges: normal expanded full 284,995 bytes, normal expanded matrix 49,416 bytes, normal collapsed full 66,429 bytes, normal collapsed matrix 19,326 bytes, severe host full 283,872 bytes, severe host matrix 49,565 bytes, severe sovereign full 284,238 bytes, and severe sovereign matrix 49,527 bytes; the corresponding volatile cache paths above had provenance manifest sidecars at capture time, and the two stable review copies are retained in the Event016 evidence folder.

The collapsed branch was rerendered with `generatedScenarios = { enabled = false }`, the exact typed normal-collapsed text, all three resolutions, and `comparisonScenario = event016_directorate_actual_normal_expanded`; the current comparison artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4511578f776b77b1d752e9a08947dbae3744b463d03c56da92aa4aae011ea899/90b2048b19a6f21d3f429b40ecdaa8f6dc70b5740c28ffb12407f7e648dc3294/kruger_directorate_container-comparison.json` and reports `changedPixels = 166334`, `changedRatio = 0.0802150848765432` for the intentional expanded-versus-collapsed branch difference at 1920x1080.

Post-change expanded render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/280d66693fd7bbb0ce07a1803c12c5c220b62cedd66e69790e3591e18669d8a0/c66e5914e3261c8ab77d675117bf9c0993c0048ba07cb8831cc0f1a0da1c7c24/kruger_directorate_container-full.svg`.

Post-change collapsed render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0da546cdde6fad20460bf66dd5bcfcf4e37f0750f139f2e5f86d78898dfc0bdd/43128bfa01aff4f7b5cae564c6ab6385269648d373dafe3bb6c887bffb47c76a/kruger_directorate_container-full.svg`.

Targeted actual-text render artifacts were produced separately for the four scenarios above with `generatedScenarios = false`, `state = normal`, and resolutions 1366x768, 1920x1080, and 2560x1440. The linked MCP full PNGs were retained, and their exact local PNG paths are listed in the resolution matrix section.

The expanded and collapsed production render calls requested all supported generic states and all three requested resolutions, returned `GUI_RENDERED`, and reported validation passed.

The renderer returned `MCP_RESPONSE_TRUNCATED` because the complete gallery payload exceeded the wire budget; its linked full-window production artifacts were retained and the rewrite transaction retained the before/proposed/comparison and validation artifacts.

## Before and after behavior

Before the patch, both existing controls were always click-enabled, so their identical x422 y11 36x36 regions conflicted whenever the renderer exposed both branches.

After the patch, the open control is enabled only in the collapsed branch and the close control is enabled only in the expanded branch.

The open effect still clears `brilliant_scientist_directorate_gui_collapsed`, and the close effect still sets it.

The compact and expanded child visibility gates remain unchanged, and the source geometry, backgrounds, profile art, portrait art, meter sprites, tooltips, and footer remain unchanged.

The typed expanded and collapsed scenarios explicitly model the runtime flag results because the offline renderer does not execute dynamic `has_country_flag` triggers against a decision-category context.

## Visual review and unresolved diagnostics

The parent-installed v3 `GFX_kruger_directorate_background` fully covers the 500x360 expanded panel, and the existing 500x58 header fully covers the compact panel.

The profile frame and portrait share their intended layered slot, and the four meter icons align on a 44px vertical rhythm with values aligned to the same baselines.

The current v3 normal expanded production PNG shows `THE KRUGER DIRECTORATE`, `Dr. Warren Kruger`, the public role/control line, four public baseline values, and the host footer inside their declared boxes; the title and top ornament are centered and clear.

The current v3 severe host production PNG shows the longest host role/control line, all four maximum values at 100, the secured frame, and the machine-stage portrait without text clipping or overlap; the meter rows retain their 44px rhythm and color-stage contrast.

The current v3 severe sovereign production PNG shows the sovereign role/control line and the longest sovereign footer without text clipping or overlap; the lower trim and both lower corners are closed and remain behind the footer's readable glyph area.

The current collapsed production PNG shows only the compact header, exact `Kruger Directorate` title, and open control inside the 500x58 branch; the compact branch is unchanged by the expanded-background replacement.

The current v3 three-resolution production matrices show the same actual text envelopes at 1366x768, 1920x1080, and 2560x1440 with no reported resolution drift. The current actual-text inspect and render validations report no `GUI_TEXT_OVERFLOW`, `GUI_MISSING_LOCALISATION`, or `GUI_CONFLICTING_CLICK_REGIONS` finding.

The current annotated and click-region renders preserve the title, profile, meter, role, and footer boxes and show only the close control in expanded branches; the collapsed branch's current rerender shows only the open control. No visible click region is duplicated across the mutually exclusive branches.

The v3 bottom trim begins near y344 and closes the lower frame across y344..359, while the footer glyphs remain visually clear above that trim; no footer-versus-trim clipping or contrast defect was observed in the normal, severe host, or severe sovereign production PNGs.

These are worker-side production observations only; the parent must inspect the refreshed PNGs or image resources before treating them as accepted evidence, and the user retains live consumer acceptance.

The synthetic `long-text` state intentionally fabricates multi-line text and reports `GUI_TEXT_OVERFLOW` for title, profile name, and value boxes when the samples exceed the compact boxes; this remains a diagnostic stress result only and is separate from the actual reachable text evidence above.

The offline renderer reports `GUI_ACCIDENTAL_CLIPPING` and `GUI_INVALID_SIZE` for children hidden by an explicit typed branch because it models hidden elements as 0x0; those elements are not visible in their respective production branch.

The offline renderer reports `GUI_SPRITE_RENDER_PARTIAL` for the existing open and close four-frame sheets because `gfx/FX/buttonstate.lua` is retained but not executed; normal, hover, pressed, and disabled frame behavior remains user-owned for live consumer acceptance.

The offline renderer requires explicit scenario text overrides for dynamic scripted-localisation calls; the current scenarios supplied exact outputs from every reachable role, control, and footer branch, and no missing Event 016 asset was reported.

## Asset handoff

All frames, portraits, meter sprites, controls, and dormant animation registrations remain existing Event 016 assets; the parent installed the v3 replacement only at the existing `GFX_kruger_directorate_background` runtime path.

The v3 source PNG is `docs/assets/016_brilliant_scientist/directorate_ui/closure_background_2026_09_02/source_png/directorate_background_closure_edit_source_v3.png`, `1478x1064` opaque RGB, SHA-256 `EE5535A9EE6ACA89C3DC59CCB05241200BD24A94BC915D246C068986A80D356F`.

The selected v3 processed PNG is `docs/assets/016_brilliant_scientist/directorate_ui/closure_background_2026_09_02/processed_png/directorate_background_closure_candidate_v3.png`, `500x360` RGBA, SHA-256 `EB35B3C4159BA58D1981E113B3AEE722E6BD8CA7DAAB7A288D9C18C6AC75DE66`.

The selected v3 DDS candidate and the parent-installed runtime DDS are byte-identical at `500x360`, uncompressed 32-bit BGRA, pitch `2000`, file length `720128`, and SHA-256 `C476E06B722EE6C41A07B85AFDD257B2232744F9D50185A2D0AD5068D080026D`. The decoded v3 evidence PNG is `docs/assets/016_brilliant_scientist/directorate_ui/closure_background_2026_09_02/evidence/directorate_background_closure_candidate_v3_decoded.png`, SHA-256 `0BC6F1C5C60A757F6BF192555828EC540FADF270F70C24E5CD05A44E2A56B4BB`.

The old compact-refresh decoded PNG is `500x360`, SHA-256 `381E2BA8C1A0B6DB21F2CEFC72BB6DA5DB30FE4FEB43B7A3DC5AC0AB51725056`. A direct RGB pixel comparison against the decoded v3 PNG finds `179898/180000` changed pixels (`0.999433`), mean absolute delta `5.779` per channel, and maximum channel-sum delta `602`; the y344..359 lower-trim band changes `7995/8000` pixels (`0.999375`) with mean absolute delta `22.118` per channel, which is the expected closure correction rather than a GUI geometry change.

The old processing manifest documents width-fit to `500x619` followed by `scaled.crop((0, 0, 500, 360))` from the `1127x1396` v2 source, leaving the lower frame outside the runtime canvas. The v3 source is an ordinary full-canvas resize to the fixed 500x360 target with no crop; visual inspection of the decoded v3 evidence and current production renders shows a continuous lower brass trim and both closed lower corners.

The current MCP collapsed-versus-expanded comparison artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4511578f776b77b1d752e9a08947dbae3744b463d03c56da92aa4aae011ea899/90b2048b19a6f21d3f429b40ecdaa8f6dc70b5740c28ffb12407f7e648dc3294/kruger_directorate_container-comparison.json`; it reports `changedPixels = 166334` and `changedRatio = 0.0802150848765432` at 1920x1080 for the intentional branch difference. The MCP `comparisonScenario` route compares typed GUI states and does not substitute a historical texture file, so the exact old-v3 asset delta above is the applicable background comparison evidence.

No GUI source or art bytes were changed by this worker in the v3 verification pass, and no re-layout is indicated. The runtime path and `GFX_kruger_directorate_background` identifier remain stable.

## Parent-owned remainder

The parent inspected the durable normal-expanded and severe-host 1920×1080 production PNG bytes, the collapsed resolution matrix, and the decoded v3 background.
The inspected views show four aligned colour-coded meter rows, unobstructed portraits and names, readable role/control text, and a footer above the intact bottom frame.
The two-line control-state diff preserves all geometry and click effects, while only the visible open or close control is enabled.
The remaining scenario and three-resolution evidence is recorded above; typed offline states and the unexecuted buttonstate shader remain explicit evidence limits, not live acceptance.
The ordinary decision category work remains independent of this reviewed presentation-only slice.

The user owns all live in-game acceptance, reload, and consumer validation; this worker and the parent do not launch, reload, or game-check Hearts of Iron IV.

The parent also retains gameplay outcomes, costs, effects, AI behavior, weights, event resolution wiring, and any broader localisation or asset decisions.

No in-game completion claim is made by this handoff.

## Simplifications, omissions, and blockers

No tab, project card, facility card, foreign card, sovereignty panel, extra meter, or hidden-state value was added because those were removed from the accepted compact design and the plan contexts are represented by existing headline meters and the decision list.

No `.gui` geometry change was applied because the accepted compact layout passed typed branch and resolution validation after the control action-integrity fix.

The `.gui` source-package rewrite timed out once after the required pre-change inspect and render; the later scalar targeted rewrite route completed with `GUI_CHANGES_UNCHANGED` and validation passed.

The normal flag-only offline preview remains unresolved because MCP cannot evaluate `has_country_flag` in this decision-category context; typed visibility and enabled-state scenarios are the required evidence for the mutually exclusive runtime branches.

The renderer wire budget truncated the complete render gallery response, so only linked production full-window artifacts were returned inline; the render call itself completed with validation passed and the rewrite transaction retained comparison and validation artifacts.

No live game run or game log search was used; the v3 provider-generated art was parent-owned and only inspected here.
