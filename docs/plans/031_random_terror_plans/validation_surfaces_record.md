# Event 31 validation surfaces record

Archived verbatim from [overview.md](../../events/031_random_terror/overview.md). Headings and references are as they stood in that file.

## Validation surfaces

Event 31 is registered as repeatable and enabled by default in the Event Logs settings through `event_log_event_is_reworked_default_enabled` in `common/scripted_triggers/chaosx_settings_triggers.txt`.
Every design decision taken during the takeover (D1-D13 and R1-R43) is recorded with its basis, its implementation commit and its live-game limits in `docs/plans/031_random_terror_plans/agent_decisions_20261004.md`.

The visual inventory is recorded row by row in `docs/plans/031_random_terror_plans/031_random_terror_visual_asset_inventory.md`, and every portrait identity has a recruitment or selection consumer (D11).
Actor operations raise, move or remove real formations (D9), every mission has a reachable progress producer and outcome (D5), carrier reuse and scenario capacity follow one availability predicate (D1, D2), and a contained crisis recovers and closes (R30).

Source checks in round 2 covered brace balance with comments stripped, localisation keys for every new decision, tooltip, option, modifier and scripted text, script-constant categories with schemas, and UTF-8 with BOM for the localisation file.
The probability route (`hoi4.probability_inspect`) returned "Invalid tool arguments" for narrow decision and event-option queries, so the AI and random weights added in round 2 (first-emphasis options, spread odds, the cannibal-clash draw and the raid capacity bonus) are reviewed in source only.

Still to be seen in a live game: cross-border spread, distant attacks and safe-haven demands on the map, the command-capital `on_state_control_changed` refresh and the live values of the three final-strength modifiers, the opening uprising wave's civil wars and missions, inherited technology and the fourth research slot, and the cannibal rivalry AI strategies.

Detected daily control changes disqualify only the changed country, preserving unrelated player countries' eligibility.
Same-day round trips and swaps between already-human countries remain unresolved because the daily country marker does not identify individual clients.

The Event 31 CXT daily hook registers newly discovered content and marks it pending for manual application.

The compact scenario-list label is `#016`, while the stable Global Jihad catalog identifier is SCN-016; the adjacent `#018` scenario label and SCN-018 identifier are preserved.

Capital-dependent achievement tracking stores each government's exact original state and separately records the capital at Maximum scenario confirmation.
Retaking and restoration proof requires a matching country-owned identity, current control is checked at completion, and repeated loss cannot extend the recovery deadline.
The achievement active-state count credits the government owning the counted states, including when the global wave's event root is a different country.
`random_terror_apply_exact_state_loss` records the measured applied loss rather than the requested loss, and the major-loss threshold stays above 400 people.

The workbook mirrors Event 31 localisation and contains Global Jihad as SCN-016; the Events-sheet status change for Event 31 from `To Be Reworked` to `Needs Testing` is queued in `docs/plans/031_random_terror_plans/catalog_changes_pending.md`.
No Internal Fracture cluster is registered by this implementation. Event 31 is an optional trigger row (row 16003, Medium) of the Domestic Unrest cluster, runtime cluster 16, together with Events 1 and 6.

The focus tree has 114 focuses with titles, no connector crossings and no same-row spacing violations in the last structural render.
The scenario window GUI inspector reported no missing fields for `chaosx_scenarios_window` with Event 31 selected, and its shared-window overlap and alignment findings remain open for the window's owner.

