# BBH focus MCP evidence

The read-only `hoi4_focus_inspect` route succeeded for `BBH_soviet_collapse_focus_tree` from `common/national_focus/005_soviet_collapse_custom_splinters.txt`, reporting 47 focuses, source revision `5e097fb6ceb61b1a56cb0a828aaff2c6c0a474a03778966faa01ce4f60aa7852`, layout hash `125f20f301f210f16f56f5349ef22ea7443221d8c3baa44a26d7f635558be8d1`, and no blocking diagnostics.

Inspection reported two BBH layout warnings: the linear connector from `BBH_anti_protectorate_letters` to `BBH_temporary_free_city_pacts` takes an unnecessary horizontal detour, and the connector from `BBH_enemy_front` to `BBH_war_plan` also takes an unnecessary detour; this icon package does not edit focus layout.

The same inspection reported the unrelated game focus `continuous_restrict_freedom` is missing `continuous_restrict_freedom_desc` localisation; this asset package does not edit that source.

The first raster call was rejected because national mode does not accept `columns` and `reviewScale` is limited to 1; a corrected call with `mode = national`, `reviewScale = 1`, and no `columns` succeeded.

The pre-art raster is `before_focus_raster.png`, 3824×1744, SHA-256 `aaa9daafd568a869f04451347a9b318e3f31c7578298843c2b065276542a9fbd`; it showed the repeated placeholder emblem across the BBH tree.

The parent reported the HOI4 MCP connection later returned `Transport closed`; this worker left runtime textures and `.gfx` unchanged, so there is no post-promotion raster or engine verification claim.
