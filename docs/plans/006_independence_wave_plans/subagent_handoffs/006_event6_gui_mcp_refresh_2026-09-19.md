# Event 006 Statehood Ledger GUI MCP refresh — 2026-09-19

Disposition: current read-only MCP evidence; source unchanged; ASSET-039 remains `needs_user_review`.

## Inspection

`hoi4.gui_inspect` completed for `independence_wave_status_window` under scenario `independence_wave_status_default` at source revision `2fec735a4cb2861ef843935a14b0731e026a574b908673083d97022304a38e4d`. It resolved 48 inspected Event 006 elements, with 557 modelled, 5 approximated, 15 ignored, 4 unsupported, 0 missing, and 0 unresolved elements. The inspection returned no blocking diagnostics. The linked inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0899584e102c64970e17a0600bc769bca54b640625c20f32444344a7319cad55/a2c90fbe54d8ae503f9546f95a42e5f43a40d509c900d0032fe913ec139427bc/gui-inspect.2fec735a4cb2861e.json`.

The inspect response still reports expected background/child overlap diagnostics from the shared panel composition and partial-sprite warnings because the offline renderer does not execute `buttonstate_blendframes.lua`. These are non-blocking renderer findings, not a source edit authorization.

## Render

`hoi4.gui_render` completed for the same scenario at 1920x1080 and 1280x720 with `normal`, `warning`, `long-text`, and `missing-localisation` states. It returned `GUI_RENDERED`, 27 linked artifacts, 5 rendered variants, 4 requested states, 2 resolutions, and a zero-pixel self-comparison (`changedPixels = 0`, `changedRatio = 0`). The primary full render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b99b885160040885227d523486db7f07661d750dfa11c7f2dba43d0b987aabd6/6669bc43dc5388c45c44daeb90b45397faefcd6366e0eea8a2d9555d4e616a24/independence_wave_status_window-full.svg`; the state matrix is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1daadc4c07b621c84d32c463b6016769ed9af14640eceb3fa0bfa0ea52aa6f47/0adeeeee81bf3cca65226f30eb361bf543e3e3e37c605e05b841c43b540b9c5e/independence_wave_status_window-state-matrix.svg`; the click-region view is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a50b599b98fba23ec84a0396b163e4c79c5a54056055b32aef81962e30df1b7/75450781335418d59fb473904393ef0dbc593388765d4f4515248b1e5d90fb99/independence_wave_status_window-click-regions.svg`.

The render validation passes its source-graph, truncation, comparison-budget, ancestor-budget, and non-blocking-overlap checks. It does not execute live scripted visibility, blendframe playback, save/load, or user-owned in-game interaction. The requested render states also do not cover every generic hover/selected/locked/disabled/active/completed/list/value state; those remain part of the open dynamic-state acceptance gate.

## Boundary

This refresh strengthens current GUI evidence but does not change the Statehood Ledger source, assets, or ownership. ASSET-039 remains `needs_user_review` until dynamic state coverage, blendframe execution, representative interaction, and live consumer proof are available. No GUI rewrite was attempted because the current evidence exposes no isolated source defect safe to patch.
