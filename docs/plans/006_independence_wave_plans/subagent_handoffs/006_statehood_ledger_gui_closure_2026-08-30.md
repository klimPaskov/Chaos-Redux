# Event 006 Statehood Ledger GUI closure handoff

Date: 2026-08-30.

## Scope, ownership, and disposition

This handoff is limited to Event 006, `chaosx.nr6`, and the dedicated Statehood Ledger scripted GUI introduced for the Independence Wave founding decision category.

The accepted Event 006 mechanics specification assigns this compact ledger to the Event 006 decision-category presentation surface and requires the five founding values, former host, patron, network, founding phase, active commitments, state seals, instability warning, charter feedback, formable feedback, five tabs, and an explicit animation toggle.

The decision entry point is `common/decisions/categories/006_independence_wave_categories.txt:independence_wave_founding_category`, which carries `scripted_gui = independence_wave_status_scripted_gui` and the Event 006 visibility gate `is_independence_wave_active_country = yes`.

No shared event log, event-details framework, settings UI, super-event UI, shared registry, unrelated scripted GUI, decision outcome, cost, effect, AI weight, localization text, gameplay mechanic, or formable puzzle was changed.

The pass is docs-only because the current source has no proven Event 006-local layout defect that can be safely applied through the required rewrite route, while the one concrete bounded gutter proposal remains blocked by the rewrite adapter.

## Exact identifiers and source surfaces

- Scripted GUI: `independence_wave_status_scripted_gui` in `common/scripted_guis/006_independence_wave_scripted_gui.txt`.
- Window: `independence_wave_status_window` in `interface/006_independence_wave.gui`.
- GFX registration inspected but not changed: `interface/006_independence_wave.gfx`.
- Background sprite: `GFX_independence_wave_status_panel` using `gfx/interface/006_independence_wave/independence_wave_status_panel.dds`.
- Static semantic strips: `GFX_independence_wave_recognition_seal_states` with 5 frames, `GFX_independence_wave_dependency_warning_states` with 3 frames, `GFX_independence_wave_league_charter_activation_states` with 4 frames, and `GFX_independence_wave_formable_eligibility_seal_states` with 4 frames.
- Animated siblings: `GFX_independence_wave_recognition_seal_animated`, `GFX_independence_wave_dependency_warning_animated`, `GFX_independence_wave_league_charter_activation_animated`, and `GFX_independence_wave_formable_eligibility_seal_animated`.
- Static fallback registrations present in the GFX file: `GFX_independence_wave_recognition_seal_static`, `GFX_independence_wave_dependency_warning_static`, `GFX_independence_wave_league_charter_activation_static`, and `GFX_independence_wave_formable_eligibility_seal_static`.
- Scripted localization inspected but not changed: `common/scripted_localisation/006_independence_wave_gui_scripted_localisation.txt`.
- Player-facing GUI localization inspected but not changed: `localisation/english/006_independence_wave_gui_l_english.yml`.
- Decision category consumer: `independence_wave_founding_category` in `common/decisions/categories/006_independence_wave_categories.txt`.
- Asset folder: `gfx/interface/006_independence_wave/` and its `animations/` subfolder.
- Animation effect retained by the four animated siblings: `gfx/FX/buttonstate_blendframes.lua`.

The current source hashes are `C5EE3BEEA0B029504737F8C8766002F26D4F4E2E42F5052E5CBCD43BB15E427D` for the scripted GUI, `55896D7F9487538903505800ABFFF1281479D03E1F3FBBDD7C500C131890F533` for the window, and `ED545B4BBF5DCDC08524956D72595B1F74F6322FC0B693CB68F9727E6E4B2119` for the linked GFX registration.

## References inspected

I read the repository `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-frame-animation` skills before reviewing the owned surface.

I consulted the offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding.

The relevant offline wiki rules confirm that a scripted GUI is defined in `common/scripted_guis/`, is attached through `window_name` to an independent `containerWindowType`, and uses scripted-GUI effects and visibility triggers to drive child controls.

I read the installed vanilla documentation set, including `documentation/script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, `loc_formatter_documentation.md`, `loc_objects_documentation.md`, and `modifiers_documentation.md`.

Vanilla precedents inspected were `interface/countrydecisionview.gui` for the decision-category presentation pattern and `interface/usa_congress_scripted_gui.gui` plus `common/scripted_guis/USA_congress_scripted_gui.txt` for an explicit decision-category scripted GUI with a bounded window, frame properties, text values, and no gameplay action layer.

The accepted Event 006 mechanics specification part 3, acceptance specification part 7, Statehood Ledger frame-mapping handoff dated 2026-07-25, prior GUI worker handoff dated 2026-08-06, and read-only GUI re-audit dated 2026-08-22 were reviewed.

## Pre-change and refresh MCP evidence

The current mandatory `hoi4.gui_inspect` query targeted `independence_wave_status_window` with scenario `{ id: "independence_wave_status_default" }`.

The inspect route returned `GUI_INSPECTED` with status `ok`, workspace `mod_chaos_redux_ea3b2d67c2c0`, shared revision `62a990d694fed292b5f02f07c85cec8fea01f0450f2ccee6c2a736bcfd05e723`, and 48 selected Event 006 elements.

The complete current inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0680b6c1e7c77b7856f4325935404d281f431190696ad3074451857410e209c/b1095a537f1a834961ede92342f1ee6a93539ded5f2732297df504cd024ac37e/gui-inspect.62a990d694fed292.json`.

The selected graph contains 153 nodes, 325 edges, 48 elements, 16 linked sprites, 2 linked fonts, 39 localization references, 1 scripted GUI, and no scripted-localization graph node.

The current fidelity counts are 557 modelled, 5 approximated, 15 ignored, 0 missing, 4 unsupported, and 0 unresolved.

The inspect checks report no Event 006-local text overflow, missing sprite, missing texture, missing font, missing localization, invalid animation frame count, invalid animation sheet dimensions, invalid parent, unknown scripted context, z-order risk, scroll-row cutoff, resolution drift, tab-state conflict, missing button effect, missing button trigger, cost mismatch, cost-display conflict, or AI equivalent warning.

The inspect route reports 4 `GUI_ANIMATION_STATIC_FALLBACK_MISSING` warnings for the four `frameAnimatedSpriteType` registrations because no resolvable fallback link is present in `interface/006_independence_wave.gfx`.

The same GFX source registers all four named static sibling sprites, so this warning is a registration-link finding rather than evidence that the static assets are absent.

The inspect route reports 21 `GUI_ACCIDENTAL_CLIPPING` warnings where the 0.72-scaled 64-pixel icons are clipped by floating-point epsilon, such as 46.08x46.08 becoming 46.08x46.079999999999984.

The inspect route reports 64 `GUI_VISIBLE_OVERLAP` warnings, 4 `GUI_SPRITE_RENDER_PARTIAL` warnings, 4 `GUI_ANIMATION_SOURCE_PROVENANCE_UNAVAILABLE` informational findings, 14 `GUI_INCONSISTENT_ALIGNMENT` informational findings, and 1 `GUI_INCONSISTENT_SPACING` informational finding.

The overlap findings are expected background-to-content coverage, static/animated sibling co-location under mutually exclusive live triggers, or co-located tab-panel text boxes whose visibility is controlled by the scripted GUI.

The current inspect scenario is offline and leaves the tab flags and animation flag empty, so its projection can mark all five panel siblings and both strip families visible at once even though the live triggers make the panels mutually exclusive and make each static/animated pair mutually exclusive.

The mandatory current `hoi4.gui_render` query targeted the same window and scenario with the accepted states normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation at 1920x1080, 1280x720, and 1024x768.

The render route returned `GUI_RENDERED` with one aggregate full-window SVG artifact at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88bd788eda04b50906456c333781fe71b6988c7eab3ef250151ad66bdd0b7aae/5baa8f086c904fbed4d521ded1d34737ef8999a03d7ba63c208a4dcd8f074df9/independence_wave_status_window-full.svg`.

The aggregate SVG reports 1,638,709 bytes and the render response reports `MCP_RESPONSE_TRUNCATED actualBytes34849 max32768`.

The current renderer did not expose separate cropped, annotated, hierarchy, click-region, state, resolution, or comparison artifacts from that request, so those views remain route-unresolved rather than being represented by source-only evidence.

The prior accepted 24-artifact render bundle remains recorded in `006_iw006_statehood_ledger_gui_worker_2026_08_06.md`, including full, cropped, annotated, click-region, hierarchy, layout, state-matrix, resolution-scale, and comparison artifact references.

The older full PNG artifact cannot currently be reopened because `resources/read` returns `Mcp error: -32603: Artifact provenance manifest is unavailable`; this is recorded as an artifact retrieval limitation, not a visual completion claim.

## Layout hierarchy and background coverage

The root is an independent `containerWindowType` named `independence_wave_status_window` at `position = { x = 0 y = 0 }` with `size = { width = 700 height = 500 }`, `moveable = yes`, and `clipping = yes`.

The background is the first child at `(0,0)` and uses the full 700x500 `GFX_independence_wave_status_panel` surface, so every functional region is mapped onto the painted panel.

The upper band contains the title and subtitle at x=26 and x=28, followed by the explicit Animate and Refresh controls at x=526 and x=610.

The left ledger column contains the five metric icons and five matching text boxes at y=92, 142, 192, 242, and 292, with icons at x=24 and text at x=74.

The right ledger column contains the host block, patron block, network block, founding phase block, and active-mission block at x=366, with semantic state strips placed beside their relevant status bands.

The lower band contains the tabs header at y=350, five navigation buttons at y=380, 412, and 444, and five co-located detail text boxes beginning at x=280 and y=444.

The hierarchy preserves the accepted background-first ordering, the four static/animated semantic sibling pairs, and the default Government detail panel.

## Value, action, text, and cost audits

The primary value budget is the five accepted founding values: legitimacy, recognition, government capacity, security readiness, and post-release instability.

The accepted Event 006 specification requires all five founding values, which is recorded as a design exception to the generic four-visible-mechanic-value ceiling; no sixth mechanic value was introduced by this pass.

The supporting context groups are former-host status and obligations, strongest patron and influence, independence-network standing, founding phase, and active commitments.

The action budget is two utility controls, Animate and Refresh, plus five mutually exclusive navigation tabs, Government, Recognition, Security, League, and Ambitions.

The two utility controls only toggle the presentation or refresh the cached ledger state, and the five tab controls only set and clear local tab flags.

Event 006 decisions and missions remain the only gameplay-changing action layer, so this window displays zero spendable costs and requires zero cost texticons.

Every visible text box is fixed-size with a bounded maxWidth and maxHeight, and the longest accepted panel text is bounded to 42 pixels.

The current inspect reports no `GUI_TEXT_OVERFLOW`, and the route exposes no missing-localization finding; the separate missing-localisation render request was not emitted as an independent artifact.

## State matrix and click regions

| State or mode | Source behavior | MCP evidence and disposition |
| --- | --- | --- |
| Normal | Static semantic strips show the live frame selected by scripted-GUI properties, and Government is the default panel when no tab flag is set. | Covered by the current render request; aggregate artifact only. |
| Hover | Vanilla button hover treatment is supplied by the shared button sprite and the seven controls remain real click targets. | Covered by the current render request; no button-label or click-region defect detected. |
| Selected | A tab click sets one tab flag and clears the other four. | Scripted-GUI source confirms mutual exclusion; offline projection does not execute flags. |
| Locked or disabled | No locked or disabled gameplay action exists on this reporting window, and all seven UI controls have explicit always-enabled triggers. | Covered as requested; no missing trigger or fake control detected. |
| Warning | The severe-instability warning is visible only when `has_independence_wave_severe_instability = yes`. | Source gate is explicit; aggregate render does not expose an isolated warning artifact. |
| Active | The Animate toggle sets `independence_wave_status_gui_show_animation`, hiding static siblings and showing the four real frame-sheet animated siblings. | Source and GFX retain real 5/3/4/4-frame sheets; offline renderer does not execute `buttonstate_blendframes.lua`. |
| Completed | League and formable semantic strips select activated or proclaimed frames through the live cached frame properties. | Frame mapping is documented by the 2026-07-25 handoff; no isolated state artifact was emitted. |
| Empty list | The active-mission localization key can describe no active commitment without creating a dynamic list. | Covered by the empty-list request; no text overflow finding. |
| Full list | The active-mission localization key summarizes active commitments in the bounded mission box. | Covered by the full-list request; no text overflow finding. |
| Minimum value | Dynamic localization reports the lowest current band for each ledger value. | Covered by the minimum-value request; no independent artifact emitted. |
| Maximum value | Dynamic localization reports the highest current band for each ledger value. | Covered by the maximum-value request; no independent artifact emitted. |
| Long text | Fixed-size text boxes and maxWidth/maxHeight bounds constrain expansion. | Covered by the long-text request; no `GUI_TEXT_OVERFLOW` finding. |
| Missing localisation | The source references resolve in inspect, while the renderer did not expose a separate missing-localisation artifact. | Unresolved as a standalone render artifact only. |

The click-region graph resolves exactly seven interactive regions: `independence_wave_status_toggle_animation`, `independence_wave_status_refresh`, and the five tab buttons.

The background, metric icons, semantic strips, text boxes, and decorative elements are non-clickable or click-through, and the inspect checks report no click-bounds mismatch or conflicting click regions.

## Concrete defect review and rewrite result

The earlier cropped review identified a narrow localization-safety risk between the severe-instability seal at x=306 and the final metric text box with maxWidth=300.

The bounded proposed source change was to move the severe-instability seal to x=318, reduce the first four metric widths to 280, and reserve 238 pixels for the instability metric while preserving its two-line height.

The required `hoi4.gui_rewrite` route rejected the initial composite patch with `GUI_PATCH_PRECONDITION_FAILED`, rejected the corrected composite range with `GUI_UNSAFE_PATCH_RANGE`, rejected scalar-only patches with `REWRITE_STRUCTURE_LIMIT`, and rejected a source-mode submission of the same bounded source with `REWRITE_STRUCTURE_LIMIT`.

The current source hash exactly matches the source hash recorded after those rejected attempts, so retrying the same rewrite would add no evidence and no safe change.

The four fallback warnings are linked to the separate GFX registration file, not either of the two exact GUI source files granted for this closure, so no out-of-scope GFX edit was made.

No manual source edit was substituted for the failed rewrite route.

## Before and after disposition

Before this closure, the accepted GUI source already contained the five tabs, four static/animated sibling pairs, semantic strips, explicit Animate toggle, default Government panel, visibility gates, and state-frame properties.

After this closure, those source files remain byte-for-byte unchanged, with the current hashes recorded above.

There is therefore no source before/after visual delta to claim.

The prior no-op post-check recorded in the 2026-08-06 worker handoff returned the same 48-element inspect graph and render set, and its comparison artifact reported `changedPixels = 0` and `changedRatio = 0`.

That no-op comparison is source-preservation evidence and not evidence that the proposed gutter adjustment landed.

## Assets and routed follow-up

The background and all four frame-sheet families are present under the Event 006 asset folder, with static sibling DDS files and real frame-by-frame animation sheets documented in `docs/assets/006_independence_wave/manifest.md` and the frame-animation handoff.

No new asset was requested, created, renamed, or replaced.

The four `GUI_ANIMATION_STATIC_FALLBACK_MISSING` findings require a future owner to resolve the explicit animated-to-static registration link in `interface/006_independence_wave.gfx` after confirming the engine-supported fallback syntax.

The renderer-only `buttonstate_blendframes.lua` limitation and the lack of a project-owned animation source manifest remain asset/runtime evidence gaps, not permission to replace the real animation with a transform-only mockup.

## Parent-owned remaining work

The parent retains the GFX fallback-link decision, live game/runtime validation, decision-category consumer behavior, dynamic variable population, localization expansion review, animation playback confirmation, and all gameplay, balance, event-outcome, and save/load validation.

This handoff makes no live HOI4 claim.

## Blockers, unresolved states, and simplifications

- The current MCP render route exposes only one aggregate full-window SVG and truncates its response, so separate current cropped, annotated, hierarchy, click-region, state, resolution, and comparison artifacts remain unavailable.
- Reopening the older PNG artifact failed with `Mcp error: -32603: Artifact provenance manifest is unavailable`.
- `hoi4.gui_rewrite` remains blocked by the exact errors recorded above, so the proposed gutter improvement is not installed.
- The inspector reports four unresolved animated fallback links in the GFX file, which is outside the exact two-file source edit scope of this closure.
- The offline renderer does not execute the animation effect or live scripted-GUI visibility flags, so its simultaneous sibling and tab-panel projection is not a live-state claim.
- The accepted specification's five primary values remain visible despite the generic four-value ceiling because removing one would violate the accepted Event 006 design; no additional value or action was added.
- No gameplay, localization, asset, shared-interface, or unrelated-UI simplification was made.
