# GFX handoff: Event 006 icon and ornamental ring assets

All listed DDS textures are installed at the exact consumer paths. The parent has repointed the four optional animated status sprites to the shared state-neutral ring sheet and changed their static overlay aliases to the ring static fallback.

| Surface | Existing sprite names | Existing GFX file | Installed DDS path |
| --- | --- | --- | --- |
| Recognition idle seal | GFX_independence_wave_recognition_seal_static | interface/006_independence_wave.gfx | gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_static.dds |
| League Reserve cost | GFX_independence_wave_form03_league_reserve_texticon | interface/006_independence_wave_small_assets.gfx | gfx/texticons/006_independence_wave/independence_wave_form03_league_reserve_texticon.dds |
| Network category | GFX_decision_category_independence_wave_network | interface/visual_consistency_repair.gfx | gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_network.dds |
| Borders category | GFX_decision_category_independence_wave_borders | interface/visual_consistency_repair.gfx | gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_borders.dds |
| FORM11 state 234/245 | GFX_independence_wave_form11_state_234/245_unresolved and _qualifying | interface/chaosx_formable_state_puzzles.gfx | gfx/interface/formables/state_puzzles/006_form11_state_puzzle/states/independence_wave_form11_state_234/245_unresolved.dds and _qualifying.dds |
| FORM18 state 413/676/1001 | GFX_independence_wave_form18_state_413/676/1001_unresolved and _qualifying | interface/chaosx_formable_state_puzzles.gfx | gfx/interface/formables/state_puzzles/006_form18_state_puzzle/states/independence_wave_form18_state_413/676/1001_unresolved.dds and _qualifying.dds |
| Shared ornamental ring loop | GFX_independence_wave_recognition_seal_animated; GFX_independence_wave_dependency_warning_animated; GFX_independence_wave_league_charter_activation_animated; GFX_independence_wave_formable_eligibility_seal_animated | interface/006_independence_wave.gfx | gfx/interface/006_independence_wave/animations/independence_wave_ornamental_ring_sheet.dds |
| Shared ornamental ring static overlay | The four corresponding _animated_static aliases | interface/006_independence_wave.gfx | gfx/interface/006_independence_wave/animations/independence_wave_ornamental_ring_static.dds |
| Recognition state-0 strip | GFX_independence_wave_recognition_seal_states | interface/006_independence_wave.gfx | gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_sheet.dds |

The ornamental ring sheet is 512x64 with eight 64x64 frames in left-to-right clockwise order, 5 FPS, looping and play-on-show. Its centre remains transparent so the current status symbol stays visible underneath.

The parent-owned GFX repoint is present in interface/006_independence_wave.gfx: the four animated aliases share the ornamental_ring_sheet.dds texture with noOfFrames = 8, and their animated-static aliases share ornamental_ring_static.dds. The recognition state strip remains a separate five-frame texture, and its first cell now contains the new ornate idle seal. The other four cells remain pixel-identical to their accepted source frames.

The GUI consumer remains interface/006_independence_wave.gui. No GFX or GUI source was edited by this asset subagent.

The parent still owns updating the FORM11 and FORM18 puzzle manifests with the selected processed/source paths and runtime DDS hashes. FORM03 state 36 remains unchanged because the exact map geometry shows real Friesland island pieces.
