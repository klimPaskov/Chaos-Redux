# Event 012 Africa Charter animation-consumer audit

Date: 2026-08-09.

Status: audit complete with no source patch required. The current Event 012 GUI-owned runtime integration was inspected in place, and this worker changed only this handoff file. The parent retains ownership of the GUI and scripted-GUI integration and its commit history.

## Ownership and exact integration surface

Event 012 owns the window exclusively through `africa_charter_council_category` in `common/decisions/categories/012_africa_categories.txt`, whose entry is `scripted_gui = africa_charter_window` and whose visibility requires `africa_is_current_host = yes`.

The exact event-owned identifiers are:

- Scripted GUI: `africa_charter_window` in `common/scripted_guis/012_africa_charter_scripted_gui.txt`, with `context_type = decision_category` and `window_name = "africa_charter_window"`.
- GUI container: `africa_charter_window` in `interface/012_africa_charter.gui`, positioned at the origin with the accepted `1000x680` canvas.
- Existing static GUI sprite registry: `interface/012_africa_charter.gfx`.
- Animation sprite registry consumed by this window: `interface/012_africa_animations.gfx`.
- Existing scripted localisation: `common/scripted_localisation/012_africa_charter_gui_scripted_localisation.txt`.
- Existing GUI localisation: `localisation/english/012_africa_charter_gui_l_english.yml`.

No new localisation key is required because the twenty consumers are transparent `iconType` overlays and do not paint text or create actions.

## Files and ownership boundary

Files reviewed inside the granted scope:

- `interface/012_africa_charter.gui`.
- `common/scripted_guis/012_africa_charter_scripted_gui.txt`.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_charter_animation_consumers_2026-08-09.md` (this file).

The animation `.gfx`, DDS, PNG, frame-sheet, preview, contact-sheet, and manifest files were read as external handoff evidence only. No gameplay costs, effects, AI, decision entry, shared interface, GFX registration, localisation, or asset binary was edited.

Current inspected source hashes are `012_africa_charter.gui = 75D934F80E86C07D43BAA2A715C9D24D68711ED3004798D94D6F783C46A818C3` and `012_africa_charter_scripted_gui.txt = 77B867C886E82DBD04C3AC4E36B51777D9AB1D51B86A2C969A721046BC40F2E2`.

## Consumer inventory

Each row is one animated/static fallback pair. Both `iconType` elements share the listed position and scale, and only one member of a pair is permitted by the paired `_visible` triggers.

| GUI pair | Animated sprite / static sprite | Position and scale | Runtime frame canvas | Visibility pair |
| --- | --- | --- | --- | --- |
| `africa_charter_host_overlay_animated` / `africa_charter_host_overlay_static` | `GFX_012_africa_host_overlay_federal_amalgamation` / `GFX_012_africa_host_overlay_federal_amalgamation_static` | `{ x = 468 y = 12 }`, `1.0` | `64x64`, 3 frames, 4 fps, non-loop | `africa_charter_host_overlay_animated_visible` / `_static_visible` |
| `africa_charter_route_capstone_animated` / `africa_charter_route_capstone_static` | `GFX_012_africa_route_capstone_seal_family_animated` / `GFX_012_africa_route_capstone_seal_family_static` | `{ x = 468 y = 12 }`, `1.0` | `64x64`, 8 frames, 8 fps, non-loop | `africa_charter_route_capstone_animated_visible` / `_static_visible` |
| `africa_charter_selected_confidence_animated` / `africa_charter_selected_confidence_static` | `GFX_012_africa_selected_member_confidence_animated` / `GFX_012_africa_selected_member_confidence_animated_static` | `{ x = 244 y = 326 }`, `0.72` | `64x64`, 8 frames, 8 fps, loop | `africa_charter_selected_confidence_animated_visible` / `_static_visible` |
| `africa_charter_selected_departure_animated` / `africa_charter_selected_departure_static` | `GFX_012_africa_member_departure_warning_animated` / `GFX_012_africa_member_departure_warning_animated_static` | `{ x = 240 y = 322 }`, `0.72` | `72x72`, 10 frames, 8 fps, loop | `africa_charter_selected_departure_animated_visible` / `_static_visible` |
| `africa_charter_colonial_pressure_animated` / `africa_charter_colonial_pressure_static` | `GFX_012_africa_colonial_pressure_border_animated` / `GFX_012_africa_colonial_pressure_border_animated_static` | `{ x = 306 y = 98 }`, `0.58` | `96x96`, 8 frames, 6 fps, loop | `africa_charter_colonial_pressure_animated_visible` / `_static_visible` |
| `africa_charter_ecological_wrath_animated` / `africa_charter_ecological_wrath_static` | `GFX_012_africa_ecological_wrath_active_animated` / `GFX_012_africa_ecological_wrath_active_animated_static` | `{ x = 306 y = 98 }`, `0.58` | `96x96`, 10 frames, 6 fps, loop | `africa_charter_ecological_wrath_animated_visible` / `_static_visible` |
| `africa_charter_congress_ready_animated` / `africa_charter_congress_ready_static` | `GFX_012_africa_congress_ready_emblem_animated` / `GFX_012_africa_congress_ready_emblem_animated_static` | `{ x = 574 y = 194 }`, `0.72` | `72x72`, 8 frames, 6 fps, loop | `africa_charter_congress_ready_animated_visible` / `_static_visible` |
| `africa_charter_africa_is_one_animated` / `africa_charter_africa_is_one_static` | `GFX_012_africa_africa_is_one_completion_animated` / `GFX_012_africa_africa_is_one_completion_animated_static` | `{ x = 486 y = 184 }`, `0.72` | `128x128`, 12 frames, 8 fps, non-loop | `africa_charter_africa_is_one_animated_visible` / `_static_visible` |
| `africa_charter_continent_war_animated` / `africa_charter_continent_war_static` | `GFX_012_africa_continent_war_terminal_animated` / `GFX_012_africa_continent_war_terminal_animated_static` | `{ x = 486 y = 184 }`, `0.72` | `128x128`, 12 frames, 8 fps, loop | `africa_charter_continent_war_animated_visible` / `_static_visible` |
| `africa_charter_rival_alert_animated` / `africa_charter_rival_alert_static` | `GFX_012_africa_rival_bloc_alert_animated` / `GFX_012_africa_rival_bloc_alert_animated_static` | `{ x = 902 y = 108 }`, `0.72` | `72x72`, 8 frames, 6 fps, loop | `africa_charter_rival_alert_animated_visible` / `_static_visible` |

The runtime DDS paths are the matching rows under `gfx/interface/012_africa/animations/`, `gfx/interface/012_africa/host_overlays/`, and `gfx/interface/012_africa/routes/`. The ten animation manifests and `docs/assets/012_africa/animations/manifest.md` document separately authored source frames, processed frames, horizontal sheets, static fallbacks, review GIFs, and contact sheets. `docs/assets/012_africa/animations/gfx_handoff.md` is the registration contract.

The read-only consumer audit returned `missing_visible = []`, `missing_registration = []`, `missing_or_bad_dds = []`, and `out_of_bounds = []` for all twenty rows. Each DDS header declares the expected logical canvas and has the exact uncompressed BGRA payload length required by the asset workflow.

## Visibility and mutual-exclusion review

- Host overlay animation requires no committed constitutional route plus host depth `full` or `promoted`; its static fallback requires no committed route plus host depth `compact`.
- Route capstone animation requires `africa_constitutional_route_committed` and no `africa_is_one`; the static seal requires the same committed route and `africa_is_one`.
- Selected departure animation requires a selected country whose relationship is leaving or whose departure-pressure flag is active; its static notice requires a selected country with the transition-notice flag and neither animated pressure condition.
- Selected confidence animation requires a selected country with no departure or transition-notice status and confidence at least `africa_measure.high`; the static confidence mark uses the same status guard and confidence below that threshold.
- Ecological wrath animation is used at `africa_measure.high` or above; the static wrath mark covers medium-or-above below high.
- Colonial-pressure animation is high pressure only while ecological wrath is below medium; its static mark covers medium-or-above below high with the same ecological guard.
- Congress-ready animation requires the congress-unlocked flag and selected action family `regional_congress`; the static mark requires the unlock flag and another action family.
- Continent-war animation requires any active continental-war flag; the static protocol mark requires the protocol-open flag and no active-war flag.
- Africa-Is-One animation requires `africa_is_one` without world-order/protocol/war flags; the static completion mark requires `africa_is_one` plus world-order-open and no protocol/war flags.
- Rival-alert animation requires an escalated rival crisis or a selected rival-bloc member; the static alert requires a rival-block or warning-ledger record and explicitly excludes either animated condition.

All twenty visibility predicates are existing flags, variables, constants, and relationship triggers. No GUI-only state was introduced. Pair conditions are disjoint at each threshold or state branch; values below the first threshold intentionally show neither ornament.

## Bounds, hierarchy, and action integrity

The parent `africa_charter_window` background covers `{ x = 0 y = 0 }` through `1000x680`. The added overlays map to the accepted header, selected-member dossier, regional card, regional result, and rival-warning zones:

| Zone | Consumer positions | Scaled visible bounds |
| --- | --- | --- |
| Header host/route | `{468,12}`, scale `1.0` | `x 468..532`, `y 12..76` |
| Selected-member dossier | `{244,326}` or `{240,322}`, scale `0.72` | `x 240..291.84`, `y 322..373.84` |
| Regional pressure/wrath border | `{306,98}`, scale `0.58` | `x 306..361.68`, `y 98..153.68` |
| Regional result emblems | `{574,194}`, scale `0.72` or `{486,184}`, scale `0.72` | `x 486..625.84`, `y 184..276.16` |
| Rival warning | `{902,108}`, scale `0.72` | `x 902..953.84`, `y 108..159.84` |

All twenty bounds are within the `1000x680` canvas. The overlays are transparent `iconType` elements, not buttons, and have no click regions, `on_click`, cost, effect, AI, or tooltip action. The pre-existing 35 buttons and their names are byte-for-byte unchanged by the animation additions; no click-region contract moved.

The accepted value budget remains one primary value (`Authority`) and three supporting values (`Reach`, `Burden`, `Pressure`). The animation consumers communicate status and state transitions rather than adding numeric values. The existing action budget and phase grouping are unchanged.

## MCP evidence

Parent-provided animation-tranche evidence was a pre-change `GUI_INSPECTED` artifact named `gui-inspect.32d29d2e0381a364.json` and a pre-change full render named `africa_charter_window-full.svg` under the `eb1f09.../eb4c2a...` artifact branch. Parent-provided post evidence was `gui-inspect.0a5855830a76f62f.json` with 107 inspected elements and no Event 012 blocker, plus successful 1920 and 1366/2560 render branches under `a5c9e61.../84d78...` and `a5c9e61.../e673ec...`.

The older accepted layout bundle supplies the detailed full, cropped, annotated, click-region, hierarchy, state-matrix, resolution-scale, and comparison views. Representative artifacts are:

- Full 1920 view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb1f09f29ad212122a2e00ec45d9e4dd9a9590e3656b113b10803bec4261b2f6/7f24f7c358e394bee5b66ac25cd1bd17a54981d4551529746ff21f434a477cbb/africa_charter_window-full.svg`.
- Click-region view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d53b00f51eece2891fdf3a5162fa25ffe52b7c214212d4b21fcb6de60a388aa3/bc08496e22fbb3e6aca3bce08d4756396cfa4e44f2108032e317288f44cc16ed/africa_charter_window-click-regions.svg`.
- State matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64f764bd299a80db27941af29357e4f9ba408c4b3cfa9da7aa07fb704b30640f/01f8e4cedbf26a10f5bfeb2ae6c0485d0d50ab7e1734fbf2838b0d828a371fc2/africa_charter_window-state-matrix.svg`.
- Comparison: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/eec27f870ab28d66ae46cdfb6a1b7b55991e8b4d8c665018eafcc58d373a5384/africa_charter_window-comparison.json`.
- Hierarchy: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5da8c6da1af5477466f7153c257ea23d8a0a726ec663aff91e4aec9a39f5b901/72e9bfa5b4dac19d54389152446a36be8f2a015f2e010b12262cfd5843527748/africa_charter_window-hierarchy.svg`.

This worker then ran a fresh `hoi4.gui_inspect` for `africa_charter_window`, scenario `default`, at shared revision `6a55cd2872a3385e90cb25d3566a6398de7311e3d7d00dd1eacecb2e6fa4a755`. It returned `GUI_INSPECTED`, `complete = true`, and `inspectedElementCount = 107` with no Event 012 blocker. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2df02d4bf52ae633c23ef335939086c7fab553376dfdf737ffd8ab31cf8cccff/703ee1e0ae3d437600fe9b96a6e5ab7e371bea9cd58870be6d23478d1d85a1bd/gui-inspect.6a55cd2872a3385e.json`.

The fresh render requested normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states at `1920x1080`, `1366x768`, and `2560x1440`, `uiScale = 1`, with a same-scenario comparison. It returned `GUI_RENDERED` with no blockers. The full artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5c9e61baff52025d967ac043cf4a9074674c5aa855f7340bb5d225e9de986a6/79eb7e7fcc5f695347a1d0dfbfb8820fb46a5dc052ebc171ee6dd4a427e01c35/africa_charter_window-full.svg`.

The render response emitted `MCP_RESPONSE_TRUNCATED` because the linked full SVG exceeded the wire budget; the parent's detailed view bundle above remains the source for cropped, annotated, click-region, hierarchy, and state-matrix inspection. The offline renderer models frame 1 or a primary texture for frame-sheet sprites and does not execute live scripted visibility or the in-game animation shader.

The earlier `hoi4.gui_rewrite` attempts against this window failed with `GUI_UNSAFE_PATCH_RANGE` and produced no source change. No fresh rewrite was attempted because the current inspect/render evidence showed no concrete correction to apply; invoking a rewrite would have been an unbounded no-op rather than a validated fix.

## Remaining parent-owned validation

The parent still owns final `.gfx` and runtime synchronization, gameplay outcome/cost/effect/AI validation, live scripted visibility with real country/flag/variable states, in-game animation playback and static fallback behavior, localisation expansion review, save/load behavior, and the exact scoped commit.

No missing asset handoff, placeholder, fallback substitution, or simplification was introduced by this audit. The only unresolved items are the offline MCP renderer's documented approximation/global-diagnostic limitations and the user-owned live HOI4 validation.
