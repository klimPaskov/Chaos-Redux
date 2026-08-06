# Event 006 Statehood Ledger GUI handoff

## Scope and ownership

This handoff is limited to Event 006, `chaosx.nr6`, and the dedicated Statehood Ledger scripted GUI introduced for the Independence Wave decision category.

The accepted Event 006 mechanics specification assigns the compact ledger to the Event 006 decision-category presentation surface and names the five founding values, former host, patron, network, founding phase, active commitments, state seals, warning, charter, and formable feedback as its contents.

The entry point is `common/decisions/categories/006_independence_wave_categories.txt:independence_wave_founding_category`, which carries `scripted_gui = independence_wave_status_scripted_gui` and the Event 006 visibility trigger `is_independence_wave_active_country = yes`.

No shared event log, event-details framework, settings UI, super-event UI, shared registry, unrelated scripted GUI, decision outcome, cost, effect, AI weight, or mechanic scope was changed.

## Exact identifiers and files

- Scripted GUI: `independence_wave_status_scripted_gui` in `common/scripted_guis/006_independence_wave_scripted_gui.txt`.
- Window: `independence_wave_status_window` in `interface/006_independence_wave.gui`.
- GFX registration: `interface/006_independence_wave.gfx`.
- Background sprite: `GFX_independence_wave_status_panel` using `gfx/interface/006_independence_wave/independence_wave_status_panel.dds`.
- Static state strips: `GFX_independence_wave_recognition_seal_states` (5 frames), `GFX_independence_wave_dependency_warning_states` (3 frames), `GFX_independence_wave_league_charter_activation_states` (4 frames), and `GFX_independence_wave_formable_eligibility_seal_states` (4 frames).
- Transition animation siblings: `GFX_independence_wave_recognition_seal_animated`, `GFX_independence_wave_dependency_warning_animated`, `GFX_independence_wave_league_charter_activation_animated`, and `GFX_independence_wave_formable_eligibility_seal_animated`.
- Scripted localisation: `common/scripted_localisation/006_independence_wave_gui_scripted_localisation.txt`.
- Player-facing GUI localisation: `localisation/english/006_independence_wave_gui_l_english.yml`.
- GUI asset folder: `gfx/interface/006_independence_wave/` and its `animations/` subfolder.
- Event-owned GUI elements include `independence_wave_status_panel_background`, five metric icons and text boxes, the four static and four animated status elements, title/subtitle, `independence_wave_status_toggle_animation`, `independence_wave_status_refresh`, five mutually exclusive tab buttons, and five tab detail text boxes.

The inspected scripted GUI uses `context_type = decision_category`, `window_name = "independence_wave_status_window"`, `visible = { is_independence_wave_active_country = yes }`, two utility actions, five navigation actions, local tab flags, state-strip frame properties, and visibility triggers for the static/animated siblings and five tab panels.

## References inspected

I read the repository `AGENTS.md`, the required `hoi4-decisions-missions`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-frame-animation` skills, the offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding, and the installed vanilla documentation set.

Vanilla precedents inspected were `interface/countrydecisionview.gui` for the decision-category ledger layout and `interface/usa_congress_scripted_gui.gui` plus `common/scripted_guis/USA_congress_scripted_gui.txt` for a bounded scripted decision-category window with explicit controls and values.

The accepted Event 006 spec part 3 and asset-family registry were inspected, together with the earlier Event 006 statehood-ledger frame-mapping handoff.

## Pre-change MCP evidence

`hoi4.gui_inspect` target `independence_wave_status_window`, scenario `{id: "independence_wave_status_default"}` returned `GUI_INSPECTED`, status `ok`, workspace `mod_chaos_redux_ea3b2d67c2c0`, shared source revision `4bf11e0423f2e38322336695ffbbb7691420e48ef4502577e7f118aab55c5160`, and 48 inspected Event 006 elements.

The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ce944158eb22f168db4d86446822aa12421c0ecb4ed52140fcb0060121fd13d/ccc0c61edda9014a002b0ce9cbeaa1df048e70aaaf375980d04ddfd32ef25e10/gui-inspect.4bf11e0423f2e38322336695ffbbb7691420e48ef4502577e7f118aab55c5160.json`.

The inspect model resolved the Event 006 window, background, 48 elements, click-capable controls, scripted-GUI context, sprite links, and animation/state assets. The event-owned layout had a 700x500 window, full 700x500 background coverage, no event-specific layout overlap in `layout.json`, and fidelity counts of 498 modelled, 6 approximated, 65 ignored, 1 missing, 4 unsupported, and 12 unresolved.

The global inspect validation is not a clean repository pass: it reports 1,894 blocking diagnostics and 75 visible-overlap diagnostics caused by the wider GUI graph, plus unrelated scripted-GUI context errors. These diagnostics were not patched because they are outside Event 006 ownership.

`hoi4.gui_render` covered the normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states at 1920x1080, 1280x720, and 1024x768, with a long-text comparison scenario. It returned `GUI_RENDERED`, 24 artifacts, 14 states, 3 resolutions, and an offline representation.

Key pre-change render artifacts were the full view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8af67bf8c35fb7c1dd61be592b2777e5d34225021bdf7a04d7b052c0accb5682/bf425dc3f00f50b365f949fa05e56a00e939909ff89b587c2932365e429d4dda/independence_wave_status_window-full.png`, cropped review `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90564658806b56ad82129b3d6e66fd84ba49368025a2c3c148bf2cf02708aab4/d7750b836a3000782d6cd017623c84cd517e7a1d0419a21f77bee05e3ef16aa4/independence_wave_status_window-cropped.png`, annotated view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6e80d5bd8964f66769e7fc984ba9d457eab6d5920ba683fc955af118ed6807a/709bd39503773262b21c063667a07bbfa86b376bacd7abcd20c3feec9e0bc9e6/independence_wave_status_window-annotated.png`, click-region view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69f9745da53a124aa9cb5671d60b1b241dee1112a4b190b9ccbd7b23b1be33e0/d9132904d06d4b83f445c4fc6a46f05d400106f216dbdbcb334ea2bf6fe18c23/independence_wave_status_window-click-regions.png`, hierarchy `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40b0348cbb9ebe16bb52961973cc43606e4ec85bc3b4e03524e0b6fd83c5cf3a/4e7489c8af7c8cd2db4d65f0134068bb8664fb4ad4f0828d67d74fbde4e240cc/independence_wave_status_window-hierarchy.svg`, and source layout `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dcd2731b2f7084caa28db1801e7a3bc35236d3b175de9fc80862956d561d09b6/8de80b8060f5282343a54a21ddbb07392f3e9e20e677915efc6ff37d7ceefcf8/independence_wave_status_window-layout.json`.

The state matrix is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b40200a6672d8c7a474361450798c723eea28970470c244788fe54be48e669c/bd5607de80d38d029a5eaba7e6d08e69c13e46ce4be6b8e7f2d1966af4faf2cc/independence_wave_status_window-state-matrix.json`, the resolution evidence is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc057f220654e730b006a7752b6e58f9ad7323e5e95f551c5d8b581bc2bc7436/aa3f3ba95d48c69f0a2cc332f1adc405b64c66ee4f909683ad4f42524114ba84/independence_wave_status_window-resolution-scale.json`, and the comparison evidence is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/b5d6f59f45a399e2597af7b4b0641d262cfcf7dda73cc8855b8aa6f9c6671887/independence_wave_status_window-comparison.json`.

The offline fidelity report records that the four `buttonstate_blendframes.lua` animation effects are retained in the source graph but not executed by the renderer, so the static primary frame is shown for review. Missing scripted variables and fonts also leave placeholder dynamic localisation in the offline image; this is not live consumer validation.

## Layout hierarchy and budgets

The hierarchy is background first, title and subtitle with two utility controls, five left-column founding metrics, five right-column state cards, and a lower tab navigator with one selected detail panel.

The background coverage map is the full Event 006 panel sprite at `(0,0)` with `700x500` bounds; left metric icons occupy y=92, 142, 192, 242, and 292; right status seals occupy the host/patron/network/phase/mission side; and the tab/detail region occupies y=350 through y=492.

The visible value budget is five primary founding values: legitimacy, recognition, government capacity, security readiness, and post-release instability.

The supporting value budget is five mandated state groups: former-host status and obligations, strongest patron and influence, independence-network standing and league phase, founding phase, and active commitments. They are separate because the accepted Event 006 spec requires each state family to remain legible and decision-linked.

The action budget is two utility actions (`Animate` and `Refresh`) plus five mutually exclusive navigation tabs (`Government`, `Recognition`, `Security`, `League`, and `Ambitions`). These controls do not execute gameplay outcomes; Event 006 decisions and missions remain the action layer.

## State matrix and interaction findings

The rendered state matrix contains 14 requested states: normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation.

The click-region evidence resolves the two utility buttons and five tab buttons as the only interactive regions in this window. The metric icons, status seals, background, text, and decorative frame elements are non-clickable or click-through.

The scripted-GUI triggers provide one visible tab panel at a time in the live game, with the government panel as the default when no tab flag is set. The offline renderer leaves all scripted visibility variables empty, so the cropped artifact visually shows overlapping panel prose; this is an MCP representation limitation and remains unresolved without live consumer validation.

## Attempted bounded improvement and result

The cropped review identified a narrow localisation-safety risk: the severe-instability seal at `x = 306` is adjacent to the final metric text box with `maxWidth = 300`, so a long band or translated value can occupy the ornament gutter.

I prepared a bounded layout-only change to move that seal to `x = 318`, reduce the first four left metric widths to `280`, and reserve `238` for the instability metric while preserving its two-line height.

The required `hoi4.gui_rewrite` route did not accept the change. A patches-mode attempt returned `GUI_PATCH_PRECONDITION_FAILED` for the initial composite range, a corrected composite range returned `GUI_UNSAFE_PATCH_RANGE`, scalar-only patches returned `REWRITE_STRUCTURE_LIMIT`, and a source-mode submission of the same bounded source returned `REWRITE_STRUCTURE_LIMIT`.

No source edit was substituted after the adapter failure. `interface/006_independence_wave.gui` remains byte-for-byte unchanged with SHA256 `55896D7F9487538903505800ABFFF1281479D03E1F3FBBDD7C500C131890F533`.

## Post-change MCP evidence

Because the rewrite was not accepted and the source hash did not change, the post-check was an explicit no-op integrity pass. `hoi4.gui_inspect` again returned `GUI_INSPECTED` with the same source revision, 48 Event 006 elements, and the same global diagnostics. `hoi4.gui_render` again returned `GUI_RENDERED` with the same 24-artifact set, 14 states, 3 resolutions, fidelity counts, and offline representation. The comparison artifact reports `changedPixels = 0` and `changedRatio = 0`.

The post-check reuses the exact artifact URIs listed above because the adapter produced identical content for the unchanged source. This is evidence of source preservation, not a claim that the proposed gutter improvement landed.

## Files changed

Only this handoff file was created. The Event 006 `.gui`, scripted-GUI, GFX, sprites, scripted localisation, and player-facing localisation files were inspected but not modified.

## Parent-owned remaining work

The parent retains the adapter/tooling decision for the bounded gutter change, live game/runtime validation, dynamic variable population, localisation expansion review, decision-category consumer behavior, animation playback confirmation, and any gameplay or balance changes.

## Blockers and simplifications

- `hoi4.gui_rewrite` is blocked by `REWRITE_STRUCTURE_LIMIT` for this source, so the proposed layout improvement is not installed.
- MCP renders are offline approximations and do not execute `gfx/FX/buttonstate_blendframes.lua` or live scripted-GUI visibility state.
- Global inspect validation remains red because unrelated GUI files contribute 1,894 blocking diagnostics and 75 visible-overlap diagnostics.
- No gameplay, decision-cost, AI, event-outcome, or shared-interface simplification was made.
