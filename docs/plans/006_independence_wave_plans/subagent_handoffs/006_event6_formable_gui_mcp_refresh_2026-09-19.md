# Event 006 formable state-puzzle GUI MCP refresh — 2026-09-19

Disposition: current read-only MCP evidence; no GUI or asset source change; formable visual acceptance remains partial.

## Inspection

`hoi4.gui_inspect` completed for `chaosx_independence_wave_formable_state_puzzle_window` under scenario `event006_formable_activated_normal` at source revision `f64910d82b5c3d9ae81785e4ae57357dde6e129485079e1901a0bf5ae8f3e829`. It resolved 93 inspected elements with 652 modelled, 1 approximated, 50 ignored, 0 unsupported, 0 missing, and 0 unresolved elements. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ff7fbbce1282792cae15745f5897a2c4811340f56a23b92e30b0850ddf64f14/fc05f27b92612ea82aeadde4156b1f0fa448d27528582861e4930a7e137f2450/gui-inspect.f64910d82b5c3d9a.json`.

The inspect result has no blocking diagnostics or visible-overlap findings, but it reports repeated `GUI_ACCIDENTAL_CLIPPING` and `GUI_INVALID_SIZE` warnings for dynamic form summaries and state pieces, including `independence_wave_form01_summary`, `independence_wave_form01_state_14_piece`, `independence_wave_form01_state_121_piece`, `independence_wave_form01_state_122_piece`, `independence_wave_form01_state_133_piece`, and corresponding FORM-02 elements. The source uses scripted-GUI `properties.image` getters for these `iconType` consumers, so the current offline route does not establish whether the zero-size result is a renderer limitation or a live layout defect.

## Render

`hoi4.gui_render` completed for the same scenario at 1920x1080 and 1280x720 with `normal`, `warning`, and `long-text` states. It returned `GUI_RENDERED`, 27 linked artifacts, 5 variants, 3 requested states, and 2 resolutions. The primary full render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d202974f6702e6d78f473c71dc4a53874a21ba0aa6996197805f8fa63c769756/fc03ef4eda714de107220379ce658b4e9e493220f1c753c721b9ba9d697a6b08/chaosx_independence_wave_formable_state_puzzle_w-full.svg`; the state-matrix artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86475140e85d59254f4092827c97a8afaa0e432eb2f732dc8ee3da932b2b37e0/774e70f77504fd46469ac87e39721013ca46d1bb59b3c8305ce35f3e84497907/chaosx_independence_wave_formable_state_puzzle_w-state-matrix.svg`; the click-region artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d202974f6702e6d78f473c71dc4a53874a21ba0aa6996197805f8fa63c769756/7fc4952c3f60dd20b1cf2d9715e66f1b949406ff0b0b7abfbb38537e0e9f60da/chaosx_independence_wave_formable_state_puzzle_w-click-regions.svg`.

The render validation passes its source-graph, truncation, comparison-budget, ancestor-budget, and non-blocking-overlap checks, with a zero-pixel self-comparison. The returned raster is extremely small because the unresolved dynamic image properties produce little visible content; this is evidence of the unresolved visual route, not an acceptance pass.

## Boundary

This refresh confirms that the grouped formable surface is source-present and inspectable but does not clear its visual gate. No geometry rewrite, generic emblem, replacement icon, or asset fallback is authorized until a family-isolated live or renderer-equivalent resolution of the dynamic image properties is available. ASSET-046 remains blocked for broader formable and League identity/reachability coverage, and the grouped GUI remains partial.
