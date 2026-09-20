# Event 006 Statehood Ledger GUI worker continuation — 2026-09-20

Disposition: blocked read-only review; no safe source fix proven; parent review required.

## Scope, ownership, and authorization

This review is limited to Event 006 Independence Wave, `chaosx.nr6`, and the dedicated Statehood Ledger scripted GUI attached to the Event 006 founding decision category.

The event-owned entry point is `common/decisions/categories/006_independence_wave_categories.txt:independence_wave_founding_category`, which contains `scripted_gui = independence_wave_status_scripted_gui` and the Event 006 visibility trigger `is_independence_wave_active_country = yes`.

The accepted Event 006 specification and the prior worker handoff assign the compact 700x500 ledger to this decision-category presentation surface, so the window is event-owned rather than a shared event log, event-details, settings, super-event, registry, or formable surface.

No shared interface, gameplay decision or effect, AI weight, asset, GFX, localisation, workbook, formable GUI, or unrelated interface was edited.

## Exact identifiers and linked surfaces

- Scripted GUI: `independence_wave_status_scripted_gui` in `common/scripted_guis/006_independence_wave_scripted_gui.txt`.
- Window: `independence_wave_status_window` in `interface/006_independence_wave.gui`.
- Context: `decision_category`.
- Decision-category entry: `independence_wave_founding_category` in `common/decisions/categories/006_independence_wave_categories.txt` (inspected only).
- Allowed source files: `interface/006_independence_wave.gui` and `common/scripted_guis/006_independence_wave_scripted_gui.txt`.
- GFX registration inspected but not edited: `interface/006_independence_wave.gfx`.
- Background sprite: `GFX_independence_wave_status_panel`, `gfx/interface/006_independence_wave/independence_wave_status_panel.dds`.
- Static state sprites: `GFX_independence_wave_recognition_seal_states`, `GFX_independence_wave_dependency_warning_states`, `GFX_independence_wave_league_charter_activation_states`, and `GFX_independence_wave_formable_eligibility_seal_states`.
- Animated siblings: `GFX_independence_wave_recognition_seal_animated`, `GFX_independence_wave_dependency_warning_animated`, `GFX_independence_wave_league_charter_activation_animated`, and `GFX_independence_wave_formable_eligibility_seal_animated`.
- Static fallback siblings: `GFX_independence_wave_recognition_seal_animated_static`, `GFX_independence_wave_dependency_warning_animated_static`, `GFX_independence_wave_league_charter_activation_animated_static`, and `GFX_independence_wave_formable_eligibility_seal_animated_static`.
- Animation effect retained by the accepted assets: `gfx/FX/buttonstate_blendframes.lua`.
- Player-facing localisation inspected but not edited: `localisation/english/006_independence_wave_gui_l_english.yml`.
- Scripted localisation registry inspected but not edited: `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`.
- GUI localisation groups include `independence_wave_status_gui_title`, `independence_wave_status_gui_subtitle`, `independence_wave_status_gui_refresh`, `independence_wave_status_gui_toggle_animation`, the five founding-value keys, former-host/patron/network/phase/mission keys, five tab labels and tooltips, and five detail-panel keys.
- Scripted localisation consumers include `GetIndependenceWaveLegitimacyBand`, `GetIndependenceWaveRecognitionBand`, `GetIndependenceWaveCapacityBand`, `GetIndependenceWaveSecurityBand`, `GetIndependenceWaveInstabilityBand`, `GetIndependenceWaveHostStatus`, `GetIndependenceWavePatronName`, `GetIndependenceWavePatronBand`, `GetIndependenceWaveLeaguePhase`, `GetIndependenceWaveFoundingPhase`, and `GetIndependenceWaveMissionStatus`.

## Files changed

Only this handoff was created:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_statehood_ledger_gui_worker_continuation_2026-09-20.md`.

The two allowed source files are byte-identical to their review-start state and have no working-tree status entries.

- `interface/006_independence_wave.gui`: SHA256 `D8B2A3DDE2E33B6643664EB4560243647A9069DA3BA58987C33BD284F52E677F`.
- `common/scripted_guis/006_independence_wave_scripted_gui.txt`: SHA256 `BA8F9E9DCCFA5B9DBED9B369D9BCC0C427AFBD1646E63BC4D6582F6CEAB4709C`.

## References and acceptance basis

The accepted reference images were inspected before the source decision:

- `docs/assets/006_independence_wave/source_png/gui/independence_wave_status_panel_source.png`.
- `docs/assets/006_independence_wave/processed_png/gui/independence_wave_status_panel.png`.
- `docs/assets/006_independence_wave/prompts/006_gui_status_panel.txt`.

The reference is a dark 1930s industrial 700x500 panel with decorative frame and an intentionally empty text-safe centre. It does not contain flattened labels, fake controls, people, flags, readable lettering, map labels, or geometry-dictating artwork.

The prior accepted evidence was read from `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw006_statehood_ledger_gui_worker_2026_08_06.md`, the read-only refresh from `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_gui_mcp_refresh_2026-09-19.md`, and the current authority from `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_completion_audit_2026-09-20.md`.

Required repository guidance was read before review, including `AGENTS.md`, `chaos-redux-scripted-gui`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-frame-animation`.

The offline `Interface modding` and `Scripted GUI modding` wiki pages were read together with the installed vanilla scripted GUI documentation in `common/scripted_guis/_documentation.md` and the installed script concept documentation.

The exact vanilla precedent inspected was `interface/sov_paranoia_system_scripted_gui.gui` with `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`, which confirms the supported `decision_category` context, independent native window, native icon/text/button elements, and scripted frame properties used by this Event 006 surface.

## Reference-to-native mapping and accepted layout

The accepted composition maps to native HOI4 elements as follows:

- The full reference panel maps to `iconType` `independence_wave_status_panel_background` at `(0,0)` with `700x500` bounds.
- The left column maps to five native `iconType` metric icons and five fixed `instantTextBoxType` values at y positions 92, 142, 192, 242, and 292.
- The right column maps to native `instantTextBoxType` state groups for former host, patron, network, founding phase, and active commitments, plus native static/animated `iconType` seal siblings.
- The title, subtitle, `Animate` utility control, and `Refresh` utility control map to native fixed text and `buttonType` elements in the top band.
- The lower navigation maps to five native mutually exclusive `buttonType` tabs and five native detail text boxes sharing the accepted detail-panel bound.
- Dynamic state is represented by scripted-GUI visibility triggers, country flags, ROOT variables, and `frame` properties; it is not flattened into the background art.

The accepted hierarchy is background, title/subtitle and utility controls, five founding metrics, five supporting state groups and seals, then the lower tab navigator with one visible detail panel.

The accepted visible-value budget is five founding values: legitimacy, recognition, government capacity, security readiness, and post-release instability.

The accepted supporting-state budget is five groups: former-host status and obligations, strongest patron and influence, independence-network standing and league phase, founding phase, and active commitments.

The accepted action budget is two utility controls and five navigation tabs. These controls only refresh presentation state, toggle the visual animation mode, or select a local ledger tab; decisions and missions remain the gameplay action layer.

The accepted design uses no gameplay-changing GUI control, so the cost-count audit is zero displayed spendable cost types and no cost texticon is required on this presentation surface. The tab and utility tooltips are concise and state-specific; the dynamic values are sourced through the existing localisation and scripted-localisation contract.

The text-density audit remains within the accepted contract: five primary values, five supporting state groups, and one detail panel visible at a time in live scripted-GUI state. The offline renderer can leave all tab panels visually present when live country flags are not populated, so this audit is not a live acceptance claim.

## Pre-change MCP inspection

`hoi4.gui_inspect` was run for `independence_wave_status_window` with scenario `{id: "independence_wave_status_default"}`, `generatedScenarios.enabled = false`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

The current inspect completed with code `GUI_INSPECTED`, shared source revision `d9b4ac90188aeb58698ea75fc2ec9ab6312b8fca9922b9bec1c65eb1e9991036`, 48 inspected Event 006 elements, and no missing source elements. Its fidelity counts were 556 modelled, 5 approximated, 15 ignored, 4 unsupported, and 12 unresolved.

The complete inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96446eeb4e408686cdfd80b146cd90ba49639ff70ae5fca14695aacc36b3a421/20fbb3d10b2c065739ef63f08af5d0da0cceffb9f9b08e2a278a63fd23580889/gui-inspect.d9b4ac90188aeb58.json`.

The inspect reported 63 non-blocking `GUI_VISIBLE_OVERLAP` findings, mostly the intentional full-background overlap and source coexistence of static and animated siblings whose live triggers are mutually exclusive. The four animated seal entries also carry the known partial-render warning because the offline renderer retains but does not execute `gfx/FX/buttonstate_blendframes.lua`.

The inspect graph reported 48 Event 006 window elements and resolved the `.gui`, scripted-GUI, GFX, sprite, font, animation, state, resolution, parent, and click-region links relevant to this owned surface. Global diagnostics from unrelated GUI files were not treated as Event 006 defects and were not edited.

## Pre-change MCP render evidence

An exact normal-state render was run with `generatedScenarios.enabled = false` at 1920x1080 and `uiScale = 1`.

The normal render returned `GUI_RENDERED`, 27 artifacts, five render variants, a 700x500 scene, and source revision `a94fd28034400b702058613cdab97aaf67e7799d5befac7afacfcc3f8446f107`.

The primary full render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7e16cf09518e23ca3fb5593aa8c3af1f18934c15f4a2cdb3e23c0bb8557350e/0764eec54a5f0d75734123f8891a4526ad788b28a7cf21804ee9664cbc7b25c6/independence_wave_status_window-full.svg`.

The returned normal-state PNG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53aefdbe7e4a7e0980126db1cc6ff63b986ad146c1463fa752e8d0935c76e404/f18896ae40ab5d6b17f7a6fce877c2e0afca04355209c4b314fe2b0524d78039/independence_wave_status_window-full.png`.

The cropped, annotated, click-region, source-map, hierarchy, layout, state-matrix, resolution-scale, fidelity, validation, scenario, and comparison artifacts were returned in the same 27-artifact set. The cropped PNG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e9f30eb962758ee93d79dbcb9aca2e75eacdce13392f2540cfd9f4f8319365c/f204ace865f146eee01757153288b3e13d5b3dd354b5be6fb9dcc2170b3703e9/independence_wave_status_window-cropped.png`.

The annotated PNG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e579bbd78e705aa2666112fb489db70fce5edc77c07afa90d7026af2e7a612a/eb5ae9a2300720ed26acf60cb6c40b267b236ebe9b8f32711afa51b380e53a1a/independence_wave_status_window-annotated.png`.

The click-region PNG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95a5006fc0d8cd3942baa6321b87f2c95d01ed7a7d2d477678eaaf399d59b096/7a7b984f78fcfbc046340a12f74c9966a760d9f4d2ebe1964d162dbc1f2a370e/independence_wave_status_window-click-regions.png`.

The source layout JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8dec228c57098fd173f11305db9705b96a79389e496447d5df6124e3ba519553/d65c499e9a84391db4f757acd4fc35ba6a0538d066fe6b74a800e3108c375bed/independence_wave_status_window-layout.json`.

The split lower-resolution normal render route at 1280x720 and `uiScale = 1` also returned `GUI_RENDERED` with 27 artifacts. Its compact response was used to confirm route completion, but its full artifact list was not retained in the final tool output and is not used as matching before/after comparison evidence.

The all-state 1920x1080 route requested `normal`, `hover`, `selected`, `locked`, `disabled`, `warning`, `active`, `completed`, `empty-list`, `full-list`, `minimum-value`, `maximum-value`, `long-text`, and `missing-localisation` with generated scenarios disabled. It returned `GUI_RENDERED`, but the MCP wire response was truncated at `actualBytes = 36637` against `maxBytes = 32768`, returning only the aggregate full SVG URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7e16cf09518e23ca3fb5593aa8c3af1f18934c15f4a2cdb3e23c0bb8557350e/0764eec54a5f0d75734123f8891a4526ad788b28a7cf21804ee9664cbc7b25c6/independence_wave_status_window-full.svg`.

Because of that wire truncation, the full state-matrix artifact set was not available for a complete returned-image review in this continuation. This is recorded as unresolved rather than waived.

## Visual and interaction review result

The accepted 700x500 bounds, full background coverage, source order, five-metric column, right-hand state groups, lower tab/detail region, and seven expected native click regions were preserved by the current source.

No blocking Event 006 layout diagnostic identified a proven clipping, overflow, missing asset, or unsafe click-region defect that can be corrected within the two allowed files using documented native fields.

The prior narrow gutter proposal remains uninstalled. It would move the instability warning seal from x=306 to x=318 and reserve narrower text widths for the five left metrics, but `hoi4.gui_rewrite` rejected the reviewed patch with `GUI_PATCH_PRECONDITION_FAILED`, then `GUI_UNSAFE_PATCH_RANGE`, and finally `REWRITE_STRUCTURE_LIMIT` for scalar and source-mode attempts. The current MCP evidence does not justify applying a speculative manual geometry change after that rejection.

The current offline render can show placeholder dynamic localisation and overlapping detail-panel text when the country tab flags and variables are not populated. The scripted-GUI source explicitly defines one visible tab by default and mutually exclusive tab effects, so replacing or moving those panels to satisfy an offline-only state would risk breaking the accepted live behavior.

The exact PNG resource blobs returned by `read_mcp_resource` were available as MCP artifacts, but this continuation’s image-output channel could not process those returned blobs for direct visual display. The layout JSON, SVG metadata, diagnostics, reference images, source geometry, and click-region artifacts were inspected; therefore final live visual acceptance remains unresolved rather than claimed.

## State and action matrix

The accepted state matrix is: normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation.

The source-backed state wiring is static versus animated seal visibility, severe-instability warning visibility, five mutually exclusive tab panels, and four frame properties sourced from ROOT variables.

Dynamic tab visibility, live variable population, real clicks, hover/selected/disabled behavior, blendframe playback, save/load persistence, and runtime localisation expansion remain unproven by the offline MCP route.

The only accepted actions are `independence_wave_status_toggle_animation_click`, `independence_wave_status_refresh_click`, and the five tab click effects. The scripted GUI marks their seven click-enabled triggers as `always = yes`; no gameplay cost, requirement, AI equivalent, probability, decision outcome, or cleanup rule was touched.

## Post-change evidence status

There was no source change, so there is no legitimate post-change source revision, before/after visual comparison, or changed-pixel comparison to report.

The normal render’s zero-pixel comparison result is a same-source/no-op comparison and is explicitly not completion evidence. The all-state route’s wire-truncated result is also not a substitute for a matching post-change state matrix.

No post-change `hoi4.gui_inspect` or matching post-change `hoi4.gui_render` was run because no source edit occurred. The current inspect and render records above are the pre-change/no-op integrity evidence for parent review.

## Assets, handoffs, and simplifications

No asset is missing from the accepted Event 006 package according to the current inspect. No new art, GFX registration, DDS, animation, or localisation handoff was created or routed.

The existing animation assets remain subject to the `chaos-redux-frame-animation` boundary: static siblings are retained as fallback, while offline MCP cannot execute the blendframe effect. No animation was flattened or replaced.

No gameplay, decision-cost, AI, probability, event-outcome, shared-interface, asset, localisation, workbook, formable, or runtime-integration simplification was made.

The only unresolved simplifications are evidence limitations: the all-state aggregate response exceeded the MCP wire budget, the lower-resolution compact response did not retain its artifact URI list in this handoff, offline scripted visibility and blendframe playback are not live proofs, and the returned PNG blobs could not be displayed through the current tool channel.

## Parent-owned continuation and live validation

The parent owns any future decision about whether to retry or manually apply the rejected gutter proposal, final integration review, live variable fixtures, tab interaction, animation playback, localisation expansion, save/load behavior, and all gameplay/runtime validation.

The user still owns live consumer validation in Hearts of Iron IV. This handoff does not claim in-game completion or final GUI acceptance.
