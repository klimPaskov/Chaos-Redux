# Event 016 Directorate interface restore handoff

Disposition: implemented within the Event 016 interface scope accepted by the parent on 2026-10-13.

## Ownership and acceptance

The owned window is `kruger_directorate_container`, attached by `brilliant_scientist_directorate_scripted_gui` to the Event 016 `decision_category` entry in `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt`.

The accepted basis is the parent task's explicit direction to restore the historical source at `fa96b41479a6961667a916a730fab27741acc170`, restore the pre-5cd geometry and refresh behavior from `00a40a45db77259bbdd1a019a285b97763ec6978`, and restore the conventional-technology sprite path from `390cbbac4db809bcbc778605b622ce36199e2e6e`.

The parent separately authorized restoring the old supporting Directorate GFX entries and exact LFS assets needed by the historical 700x500 window, then authorized a new-only placement for `portfolio_middle` while preserving the two old portfolio columns unchanged.

Event ownership is confirmed by the event-specific window and scripted-GUI names, the dedicated Event 016 category attachment, and the `016_brilliant_scientist_directorate.gfx` registry; no shared interface or framework was edited.

## Changed files and identifiers

| File | Change |
| --- | --- |
| `interface/016_brilliant_scientist_directorate.gui` | Restored the historical 700x500 full window and five-page layout from the parent of `5cdcf1f4dddc`; added the authorized new-only scrolling `portfolio_middle` region beneath the unchanged historical left/right portfolio elements; retained the later frame-over-portrait draw order. |
| `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt` | Restored the full tab, warning, project, facility, foreign-pressure, sovereignty, singularity, and animation-toggle bindings from the parent of `c3548e15daeb`; restored the four player-triggered refresh helper calls and enabled state; retained direct child visibility gates for collapse and tab states. |
| `interface/016_brilliant_scientist_directorate.gfx` | Restored `GFX_kruger_directorate_refresh_control` using its original four-frame texture; all other existing Event 016 sprite registrations remain present. |
| `interface/016_conventional_technology.gfx` | Restored `GFX_decision_category_conventional_technology` to `gfx/interface/decisions/016_brilliant_scientist/decision_category_directorate.dds` from `390cbbac4db809bcbc778605b622ce36199e2e6e`. |
| `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml` | Reinstated only the existing historical `brilliant_scientist_directorate_gui_profile_status`, `brilliant_scientist_directorate_gui_control`, and `brilliant_scientist_directorate_gui_refresh_tt` keys needed by the restored window. |
| `gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds` | Restored the original 700x500 full-window background bytes from the parent of `5cdcf1f4dddc`. |
| `gfx/interface/016_brilliant_scientist/directorate/directorate_compact_header.dds` | Restored the original 700x58 collapsed-header bytes from the parent of `5cdcf1f4dddc`. |
| `gfx/interface/016_brilliant_scientist/directorate/directorate_refresh_control.dds` | Restored the original four-frame refresh-control texture required by the returned refresh button. |

The previously dedicated conventional-technology DDS remains in the repository but is no longer bound by that category sprite.

The earlier 500x620 artwork handoff at `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_directorate_background_refresh_handoff.md` remains historical production evidence; its former runtime hashes do not describe the restored current DDS bytes, and the parent should reconcile that handoff's current-runtime disposition if the event documentation is maintained further.

The handoff preserves the old open/close controls, refresh and animation buttons, five tab buttons, four public telemetry values, control-status warning, active-project marker, facility and foreign cards, sovereignty panel, and singularity states.

The refresh action calls the existing country-scoped `brilliant_scientist_refresh_government_control`, `brilliant_scientist_refresh_project_counts`, `brilliant_scientist_refresh_containment_facility_count`, and `brilliant_scientist_refresh_kruger_portrait_stage` helpers on open and on refresh-button click; it does not change a decision outcome, cost, AI rule, or balance value.

The existing decision category remains the only gameplay action surface, and no cost texticons are required by this read-only display.

## Historical mapping, assets, and visual reference

`GFX_kruger_directorate_background` consumes the restored 700x500 full panel, and `GFX_kruger_directorate_compact_header` consumes the restored 700x58 compact strip.

The restored DDS SHA-256 values match their Git LFS object IDs: background `995fd4f79ab6590fd7955ee92f4604da65bb244ee504de5944fa0c49cf7c22df`, compact header `8e72fe13ab89de1d6713e59465621da21767697a290d17a664c3070b4dae08e6`, and refresh control `d0eea3ece8f75b24e864ace6d7b5463933f27205f6187c6aa767f464e83c6117`.

The refresh DDS is 496x34 with four 124x34 button frames; open and close controls are 144x36 with four 36x36 frames; tab controls are 368x30 with four 92x30 frames; animation controls are 496x34 with four 124x34 frames.

The restored parent source is the reference for the 700x500 composition and native control mapping; it is not a generated mockup, and no new raster art was produced.

The vanilla scripted-GUI precedent inspected is `interface/sov_paranoia_system_scripted_gui.gui`, lines 1-75, source revision `8be15b311ae5688e0ce0620dd9f80ab43da2158a8cbfdc0e2ab96f39ab2970ef`; it demonstrates separate native image and text consumers within a scripted-GUI composition.

The vanilla category precedent is `interface/countrydecisionview.gui`, lines 48-68, SHA-256 `eedea36ade734b67a23181a650464f9168beadb0e024c0cedf2112d1b097194e`; its decision grid is 502 pixels wide.

The native scroll control reference is `interface/core.gui`, lines 247-286, SHA-256 `553b14374957f1a0403b627a5252cce0b9a8578cae1a70be2686e660f2c7c481`; the Event 016 scroller uses its existing `right_vertical_slider` definition without adding a sprite.

Offline wiki evidence is `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`, `Parent window`, lines 68-92 and `Template`, lines 549-573, revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`.

Offline wiki evidence for container ownership and native scrolling is `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`, `Containers`, lines 73-80 and scrolling/vertical-scrollbar rules, lines 110-127, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`.

Installed scripted-GUI documentation was read from `common/scripted_guis/_documentation.md`, lines 1-25, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`.

The offline wiki and installed documentation references were read through `hoi4.reference_context` and `hoi4.reference_read`; direct vanilla files were also read to confirm the scroll control and exact category width.

Both `hoi4.reference_search` calls for `verticalScrollbar` stalled without returning a result, including one narrower retry; the local wiki and vanilla references above supplied the needed syntax, and no further search retry was made.

## Layout, states, and source bounds

The hierarchy is a 700x500 decision-category root with 700x58 compact and 700x500 full children; the full panel retains the five historical tabs and the original 480x230 page area at `(202,202)`.

The five 92x30 tab hit regions begin at local x positions 202, 299, 396, 493, and 590 on y=166; the final tab ends at x=682 within the 700-pixel root.

Open and close controls each use their native 36x36 frame at `(646,11)`; refresh uses a 124x34 frame at `(202,449)`; animation uses a 124x34 frame at `(334,449)`; their source hit bounds do not overlap the footer at `(474,448)`.

The new `portfolio_middle` scroller is inside the Projects panel at local `(214,190)`, 250x36, with a 232x108 text child and the existing vanilla `right_vertical_slider`; in root coordinates it occupies `(416,392)` through `(666,428)`, within the 480x230 panel ending at `(682,432)`.

The original left and right portfolio text boxes remain at local `(214,4)` and `(344,4)` with their historical widths and heights unchanged; the new middle list follows beneath them and scrolls inside its own clipped viewport.

At 1920x1080 and 1366x768 with UI scale 1, the 700x500 root is within the viewport bounds; these are source-coordinate checks, not rendered artifacts.

The restored root is 198 pixels wider than the vanilla 502-pixel decision-grid column identified above; the historical 700-pixel width is explicitly requested, so it is retained for parent review rather than silently narrowed.

The normal/open state shows the profile role and condition, government-control value, and four named Mandate, Dependence, Exposure, and Capacity values.

The default overview tab shows its two historical text regions; Projects, Facilities, Foreign, and Authority/Sovereignty are mutually exclusive through their tab flags, and the sovereignty tab remains conditional on `brilliant_scientist_directorate_sovereignty_surface_is_available`.

The Projects tab shows the active-project state plus the unchanged historical left/right stage ledgers and the new scrollable middle ledger; active-project animated and static markers follow the animation preference and active-family variable.

Compromised or lost control shows the animated warning when animations are enabled and the static warning when they are disabled; ordinary control hides both warning variants.

The sovereignty view selects the dynamic singularity indicator; armed singularity uses the animated sheet when enabled and its static fallback when animations are disabled.

The collapsed state shows only the compact background, compact title, and open control; the open control clears the collapse flag, the close control sets it, and direct child gates keep the full panel hidden or visible consistently.

The animation toggle and refresh button are presentation controls, not gameplay actions; the tab buttons are navigation, and every button has its own scripted click-enabled binding.

There are four scalar telemetry values at most; portfolio stage lines are a record list, not additional scalar controls, and the newly restored middle records use a native scroll viewport.

No costs or cost strings appear in this window, so there are no missing cost texticons or mixed-cost labels.

## Source review and visual-check limits

The pre-edit bytes and pre-existing diffs for the initially assigned GUI, scripted-GUI, and conventional-technology GFX files were captured under ignored `.tmp/interface_restore_handoff2/event016/`; the expanded Directorate GFX and current background/header bytes were captured before their restoration as well.

The final source cross-check found no missing GUI localisation keys, no missing direct visibility gate for a named Event 016 GUI element, no orphan visibility trigger, and no missing mod texture path among the Event 016 GFX registrations.

The two historical portfolio text boxes were compared against the 700x500 parent source and remain unchanged; the only new data control is `kruger_directorate_project_portfolio_middle_scroll` and its text child.

No baseline, intermediate, annotated, hierarchy, click-region, state, resolution, or final `hoi4.gui_inspect`/`hoi4.gui_render` artifacts were produced because the parent explicitly reserved MCP GUI health and final renders; no HOI4 instance was launched.

The parent should run the matched visual review for normal, hover, selected, disabled, warning, active-project, empty/no-active-project, sovereignty, armed-singularity, collapsed, and Projects-scroll states at 1920x1080 and 1366x768, UI scale 1, using the exact restored source and asset revisions.

The source-level 502-versus-700 width difference and the scroll viewport's rendered text/track clearance remain visually unchecked; this handoff does not claim in-game validation.

## Gameplay integration and remaining work

The Event 016 category attachment and gameplay decisions were read but not edited; all decision costs, requirements, outcomes, AI behavior, cooldowns, and cleanup remain parent/decision-owner surfaces.

No custom asset is missing and no art owner follow-up is required; the three historical DDS objects and the shared conventional-technology artwork are present at their registered paths.

No gameplay simplification was made; the historical two-column ledger, all four telemetry values, five tabs, warning and singularity states, animation preference, refresh control, and the new-only middle portfolio are present.

Parent integration remains responsible for the matched MCP visual pass and final action-integrity review; live-game validation remains user-owned.

Skills used: `chaos-redux-scripted-gui`, `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.

## Parent integration follow-up

The parent restored the missing `brilliant_scientist_directorate_gui_refresh` label from the exact `00a40a45` source after an independent integration check.
The presentation action and its tooltip remain unchanged.
The MCP render route timed out after 600 seconds; screenshot coverage is assigned to Handoff 1.
