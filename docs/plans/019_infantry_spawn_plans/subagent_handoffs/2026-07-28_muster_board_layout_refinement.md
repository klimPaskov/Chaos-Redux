# Event 019 Muster Board Layout Refinement Handoff

> Superseded by the user-directed compact-background correction recorded in `event19_compact_background_handoff.md` and `2026-07-28_compact_gui_mcp_review.md`. The six-well rail, authored slot/plate zones, and 1120x760 dimensions described below are historical context only.

The regenerated board background remains wired through the existing `GFX_infantry_spawn_muster_board_background` identifier and remains the only runtime background asset. This handoff documented an earlier authored-zone layout; the current correction replaces it with one restrained header band, one broad central paper field, and one narrow lower action band without decorative slots or wells.

Parent-owned layout changes are in `interface/019_infantry_spawn_muster_board.gui`. The current source keeps functional lists and three-column action rows transparent over the broad field, retains the army-only command scene, and uses a shared inset for title/subtitle and tabs. No decorative ledger rail, repeated card plate, or registry well remains.

Review evidence for the superseded layout was rendered with the HOI4 MCP fixture at 1280 by 720, 1366 by 768, 1920 by 1080, and 2560 by 1440 at uiScale 1 and 1.25 across normal, hover, selected, warning, and long-text states. It is retained as historical evidence only; the current simple correction has its own MCP pass in the parent completion report.

The MCP source graph still reports its known offline limitations: valid `player_context` scripted GUIs are classified as unknown, vanilla font metrics and some sprite aliases are not modelled, and the fixture includes unrelated Event Log diagnostics. These are tool limitations, not runtime fallbacks. This historical tranche did not change gameplay wiring; its layout is superseded by the simple user-directed pass.
