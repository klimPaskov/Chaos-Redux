# Event 019 richer GUI background coverage crosswalk

Requirement `event19_gui_background_richer` comes from the parent task requesting a new compact 960x640 HOI4-style background richer than the existing flat parchment.

The requirement is satisfied by `metadata.json` and `manifest.json` entry `019_infantry_spawn_muster_board_background_richer`.

The source package is `source_png/infantry_spawn_muster_board_background_richer_imagegen_1536x1024.png`, processed output is `processed_png/infantry_spawn_muster_board_background_richer_960x640.png`, runtime output is `runtime_dds/infantry_spawn_muster_board_background_richer_960x640.dds`, and review evidence is `review/infantry_spawn_muster_board_background_richer_contact_sheet.png`.

The intended runtime registration is the parent-owned sprite `GFX_infantry_spawn_muster_board_background` consuming `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds` after promotion.

The live consumer is the parent Event 019 scripted GUI implementation, and no gameplay or interface source file was edited in this asset-only pass.

The asset is static, so no conditional state binding or animation family is required.

Row status: complete pending parent promotion into the engine-facing runtime path.
