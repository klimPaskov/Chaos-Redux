# Event 019 Muster Board Runtime Border Cleanup

The direct Event 019 Muster Board review found that the critical-command frame was registered at the root window level even when the command panel and claimant portrait were absent, leaving a loose empty frame below the utility controls.

The frame sprites now live inside `infantry_spawn_muster_command_panel` beside the claimant portrait, so their position is owned by the command surface and they cannot float over Overview, Lots, Anomalous, or History.

Both animated and static frame visibility helpers now require the command panel and claimant portrait to be visible in addition to the existing warning or critical claimant condition.

The source changes are in `interface/019_infantry_spawn_muster_board.gui` and `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt`.

## MCP review evidence

The temporary MCP workspace, fixture, client, generated artifacts, renders, and logs were kept under `.tmp`.

`hoi4.gui_inspect` and `hoi4.gui_render` completed for Overview, Lots, Command, Anomalous, and History at 1280×720, with additional Overview renders at 1366×768, 1920×1080, and 2560×1440.

The clean visual review shows the full board background, aligned utility controls, correctly scoped tabs, resolved fixture values, and no empty critical frame on non-command surfaces.

The Command surface keeps the claimant portrait and its command actions together; the frame is eligible only when the warning or critical claimant state is active.

The MCP fixture deliberately contains only Event 019 GUI, scripted-GUI, localisation, and referenced asset sources because scanning the full mod hit the tool's `SCAN_BYTE_LIMIT` before visual artifacts were produced.

The fixture reports the tool's `GUI_SCRIPTED_CONTEXT_INVALID` warning for the valid HOI4 `player_context` declaration, repeated goal-texture collision diagnostics from the existing Event 019 GFX registry, and inline collection truncation; no Event 019 sprite or texture is missing from the fixture.

## Scope and fallbacks

No runtime fallback, source placeholder, or gameplay simplification was introduced by this cleanup.
