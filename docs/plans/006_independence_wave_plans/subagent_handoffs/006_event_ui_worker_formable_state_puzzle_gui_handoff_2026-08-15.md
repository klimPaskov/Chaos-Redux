# Event 006 state-puzzle GUI worker handoff — 2026-08-15

## Outcome

This tranche audited only the Event 006 grouped formable state-puzzle surface, with the current state-833 FORM-12 and FORM-13 family scenarios requested by the parent.

No source-backed authored defect was isolated, so no GUI source, scripted-GUI source, GFX source, localisation, scripted localisation, gameplay, decision, asset, or workbook file was changed.

No `hoi4.gui_rewrite` call was made because a rewrite would have to change the accepted state geometry or family-overlay selection without a family-isolated defect.

The current owned GUI file remains SHA-256 `D9793AE1F8958AAFFE643390A8C958B48517ECA8014285178F47BECAC5C829E7`.

The only file added by this tranche is this handoff.

## Event ownership proof

The accepted Event 006 specification is `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md`, under “Grouped state-puzzle consumer contract”.

That contract names `group_id = independence_wave_formables`, `group_scripted_gui_id = independence_wave_formable_state_puzzle_scripted_gui`, and `group_window_id = chaosx_independence_wave_formable_state_puzzle_window` for fourteen Event 006 runtime-authored families, including FORM-12 and FORM-13.

The contract explicitly makes the grouped scripted GUI presentation-only for human players and leaves decisions, missions, formation effects, AI, and the shared event framework as their respective owners.

The exact owned identifiers are:

- Window: `chaosx_independence_wave_formable_state_puzzle_window`.
- Scripted GUI: `independence_wave_formable_state_puzzle_scripted_gui`.
- Interface source: `interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui`.
- Scripted-GUI source: `common/scripted_guis/chaosx_formable_state_puzzles.txt`.
- GFX source: `interface/chaosx_formable_state_puzzles.gfx`.
- Scripted localisation source: `common/scripted_localisation/chaosx_formable_state_puzzles.txt`.
- Localisation source: `localisation/english/chaosx_formable_state_puzzles_l_english.yml`.
- FORM-12 activation helper: `independence_wave_formable_state_puzzle_form12_activation`.
- FORM-13 activation helper: `independence_wave_formable_state_puzzle_form13_activation`.
- FORM-12 overlay: `independence_wave_form12_overlay`.
- FORM-13 overlay: `independence_wave_form13_overlay`.

The grouped consumer is attached to the seventeen Event 006 decision categories recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_formable_state_puzzle_category_attachment_audit_2026_08_09.md`.

The prior bounded GUI handoff is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event_ui_worker_formable_state_puzzle_gui_handoff_2026-08-14.md`.

## Source-backed contract review

The interface root is a clipped `440 x 206` `containerWindowType` at `(0, 0)`.

Each family overlay is intentionally co-located at `(0, 0)` with the same `440 x 206` bounds and is selected by a mutually exclusive activation visibility trigger.

FORM-12 and FORM-13 each place a centered summary in a `440 x 22` strip at `y = 0` and a clipped `440 x 180` map at `y = 24`.

The current FORM-12 and FORM-13 map pieces are state IDs `249`, `397`, `399`, `651`, and current state `833` at the generated coordinates `182,126`, `169,8`, `205,101`, `228,126`, and `163,113` respectively.

The state-833 icons are informational `iconType` elements with delayed tooltips and no click regions or scripted effects.

The FORM-12 and FORM-13 consumer manifests under `docs/formables/state_registry/consumers/` both declare a `440 x 180` projection, five candidate state IDs, and `summary_required_count: 4`.

The `/ 4` summary is therefore intentional four-of-five readiness, not a text/layout mismatch.

The state-833 sprite resolvers use the matching qualification helper and fall back to the unresolved GFX sprite, while the tooltip localisation names the state, owner, controller, formation status, and core status.

The concurrent Event 006 additions in `common/scripted_guis/chaosx_formable_state_puzzles.txt` and `interface/chaosx_formable_state_puzzles.gfx` were inspected and preserved unchanged.

## References inspected

The required offline wiki pages were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding.

The installed vanilla documentation consulted included `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, `loc_formatter_documentation.md`, `loc_objects_documentation.md`, and `modifiers_documentation.md`.

The exact vanilla precedent inspected was the USA Congress scripted GUI in `common/scripted_guis/USA_congress_scripted_gui.txt`, `interface/usa_congress_scripted_gui.gui`, and `common/decisions/categories/USA_decision_categories.txt`.

The Chaos Redux guidance consulted was `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-frame-animation`.

The frame-animation guidance was reviewed because the event-asset rules require an animation decision for animated surfaces, but this state-puzzle window uses static generated map pieces only.

## Current MCP inspect receipts

The exact route was `hoi4.gui_inspect` with `windowName = "chaosx_independence_wave_formable_state_puzzle_window"` and workspace `mod_chaos_redux_ea3b2d67c2c0`.

FORM-12 scenario `E6_FORM12_STATE833_FAMILY_2026_08_14` returned `GUI_INSPECTED` with 93 inspected elements at shared revision `b5a5efa535ba49bfba1929f3675985dffb25d1fe715386e0c74c7692391e17a5`.

FORM-12 inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0aba836ef2082beb8f5620cd77fd0269ccf5ba20dfff5ecc5d14846e3abeb52d/8a26fffc959303a2ce8cc00c440c510a61cc86f3e43a9839353f5331b99b7565/gui-inspect.b5a5efa535ba49bf.json`.

FORM-13 scenario `E6_FORM13_STATE833_FAMILY_2026_08_14` returned `GUI_INSPECTED` with 93 inspected elements at the same shared revision.

FORM-13 inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8482f0d64af37dafe04c5366f70f77197a433ec31846459f8db17bb157e43afa/49a1ec29218f006fcee1e21636c431974da82b97f449e0ea4bab87569b419c4e/gui-inspect.b5a5efa535ba49bf.json`.

Both family requests reported fidelity counts of 615 modelled, 15 approximated, 64 ignored, 14 missing, zero unsupported, and 15 unresolved.

Both requests retained the global graph and validation ceilings, including 521 `GUI_VISIBLE_OVERLAP`, 48 `GUI_SCRIPTED_CONTEXT_INVALID`, 14 `GUI_UNRESOLVED_DYNAMIC_VALUE`, two inconsistent-alignment findings, and one inconsistent-spacing finding.

Those diagnostics are workspace-wide/index-level and are not sufficient evidence of a FORM-12 or FORM-13 authored overlap because all fourteen family overlays intentionally share one rectangle and only one activation helper is visible at runtime.

## Current MCP render receipts

The exact route was `hoi4.gui_render` for the same window and family scenarios.

Each request covered resolutions `1920 x 1080` and `1366 x 768` at `uiScale = 1` and states `normal`, `hover`, `selected`, `locked`, `disabled`, `warning`, `active`, `completed`, `empty-list`, `full-list`, `minimum-value`, `maximum-value`, `long-text`, and `missing-localisation`.

FORM-12 returned `GUI_RENDERED` with one linked full-window SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9654598f01c40a19da62a51464f8e7698112a52589404fd484b76aaf61e8203f/2eef703f239594c6566c7cb9d2f38067b0b497666579392a99ac114b12fecf92/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

FORM-13 returned `GUI_RENDERED` with one linked full-window SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9654598f01c40a19da62a51464f8e7698112a52589404fd484b76aaf61e8203f/9a85d96095930705c90e102586325b9c82e00e0f9952b81d20d5b727a4e6ab19/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

Reading both linked SVGs confirmed a `1920 x 1080` full-window canvas, nine image elements, two summary labels, and the offline renderer watermark.

Both SVGs emitted two generic `Qualifying states:` summaries with `[dynamic_loc] / 3`, although the authored FORM-12 and FORM-13 localisation and manifests require `/ 4`.

Both SVGs emitted the same nine-image aggregate output even when the scenario selected one family, so the route did not honor the requested family isolation.

Both render responses reported `MCP_RESPONSE_TRUNCATED` with `actualBytes = 41876` and `maxBytes = 32768`, and validation `passed = false`.

The route returned no separate crop, annotation, hierarchy, click-region, state-gallery, resolution-gallery, or comparison artifact.

The render evidence is therefore useful for proving route availability and the renderer isolation failure, but it is not a valid family-specific visual acceptance receipt.

## Layout hierarchy, budgets, and state matrix

The hierarchy is one summary value above one exact generated map for the active family.

The primary visible value is qualifying-state count versus the family required count and readiness status.

Supporting context is supplied by the delayed state tooltips, which show owner, controller, formation status, and core status.

The action budget is zero inside this surface because every state piece is informational and the formation decisions remain the actionable owners.

The background coverage map is the transparent clipped root, the `y = 0..22` summary strip, and the `y = 24..204` generated map area.

The state matrix is unresolved or qualifying sprite treatment, delayed tooltip on hover, one active family overlay, and no selected, locked, disabled, warning, completed, list, or action-specific control state.

The generic renderer states that do not correspond to this informational surface cannot prove runtime-specific dynamic localisation behavior.

## Rewrite decision and behavior

Before and after behavior are identical because this tranche made no source change.

The intended behavior remains one human-only active Event 006 family overlay, dynamic unresolved or qualifying map pieces, and informational delayed tooltips.

Moving or deleting co-located overlays would break exact generated map geometry or family selection, and changing `/ 4` would contradict the accepted five-state consumer manifests.

No source diff exists for the owned GUI surface.

There is no post-change comparison receipt because there was no source change; the 2026-08-15 inspect and render receipts above are a current read-only recheck.

## Assets and parent-owned follow-up

No asset was created, routed, replaced, or simplified.

The existing static DDS pieces under `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/` and `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/` remain the approved dependencies, with their unresolved and qualifying registrations in the concurrent GFX source.

The parent retains gameplay admission, formation effects, decision costs, AI behavior, package readiness, event-log integration, runtime loading, live HOI4 validation, and final whole-event completion claims.

## Blockers, unresolved evidence, and simplifications

The MCP route is available and resolves the exact Event 006-owned window, so this is not a route-unavailable blocker.

Family-isolated visual acceptance is unresolved because the inspect route retains workspace-wide aggregate diagnostics and the render route ignores family isolation, emits `/ 3`, and returns only one 1920 x 1080 full-window SVG for a two-resolution request.

Separate crop, annotation, hierarchy, click-region, state, resolution, and comparison receipts remain unavailable from the installed MCP response.

No gameplay simplification, UI simplification, fallback art, placeholder art, localisation rewrite, geometry change, or unrelated interface audit was made.

This handoff does not claim in-game completion.
