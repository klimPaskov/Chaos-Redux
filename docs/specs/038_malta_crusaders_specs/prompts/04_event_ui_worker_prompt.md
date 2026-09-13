# Prompt for `chaosx_event_ui_worker`

Work with no inherited conversation context. This is an Event 38 owned GUI task, not a shared UI audit.

Event: `038_malta_crusaders`

Read `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-subagents`, and these Event 38 specs:

- `04_crusade_council_mechanic.md`
- `06_focus_tree_architecture.md`
- `07_decisions_missions_and_failure.md`
- `17_assets_3d_audio_animation.md`
- `20_event_logs_details_catalog_localisation.md`
- `21_multiplayer_dlc_performance_cleanup.md`
- `22_scripted_architecture_and_file_map.md`
- `23_acceptance_scenarios.md`
- `29_asset_requirement_matrix.md`

The parent must append the locked GUI identifiers, exact owning `.gui`, `.gfx`, scripted GUI and localisation files, entry point, gameplay helper IDs, approved asset paths, supported resolutions, and allowed file list before dispatch. Stop and return a blocker when any required identifier or asset contract is missing.

Implement or improve only the dedicated **Crusade Council** mechanic window introduced by Event 38. It presents:

- Crusade Authority
- Order Cohesion
- Sacred Legitimacy
- active military orders and one dominant-order state
- one active demand or dispute
- current government route
- selected principality or relic summary only when the accepted layout includes it
- concise state labels, threshold tooltips, and buttons backed by parent-owned gameplay helpers

The window must not expose hidden route conditions, raw variables, debug histories, full probability breakdowns, or more than the three persistent public values. It must not modify the shared Event Log, Event Details, settings, super-event framework, or unrelated interfaces.

Use the mandatory MCP sequence:

1. `hoi4.gui_inspect`
2. pre-change `hoi4.gui_render` for full window, key crops, hierarchy, click regions, all relevant states, and all supported resolutions
3. an in-scope `hoi4.gui_rewrite`
4. post-change inspect and render over the same states and resolutions
5. comparison evidence

Treat the production render as the in-game visual surface. Fix every visible alignment, centering, symmetry, spacing, clipping, overflow, background, scaling, text, state, hover, click-region, and overlap defect. Decorative overlays must not intercept clicks. Button text must be centered and fit every dynamic branch. Tooltips should normally remain two to four short lines.

Use the least cluttered hierarchy. Normal state should make the three values, current pressure, and next useful actions clear without reading a paragraph. Use visual thresholds and qualitative order states. Animation is allowed only through approved real frame packages and must have a static fallback.

Do not alter gameplay effects, costs, AI, balance, event outcomes, shared helpers, or non-GUI source. Write a handoff to `docs/plans/038_malta_crusaders_plans/subagent_handoffs/event_ui_worker.md` with changed files, exact identifiers, before and after evidence, MCP revisions or artifact URIs, remaining visual risks, and parent integration tasks.
