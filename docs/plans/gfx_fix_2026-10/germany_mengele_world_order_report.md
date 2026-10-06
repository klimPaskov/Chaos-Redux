# Germany Mengele World Order asset report

Status: the assigned severity-3 decision-icon repair is implemented, parent-approved, and converted to the existing runtime path.

## Finding and consumer

`GFX_decision_mengele_hidden_clone_network` had a 32x32 visible emblem with only 6.7% fully opaque pixels; the three connected network nodes read as a dark smudge.

The sprite remains registered in `interface/germany_mengele_world_order.gfx` at `gfx/interface/decisions/germany_mengele/decision_mengele_hidden_clone_network.dds`.

The two active decision consumers are `germany_final_solution_category::dispatch_biomedical_aid_mission` and `germany_final_solution_category::deepen_foreign_tank_network` in `common/decisions/germany_mengele_decisions.txt`.

## Source and runtime evidence

The parent approved the reviewed three-node connected-network candidate on 2026-10-06.

| Before DDS SHA-256 | Native ImageGen source and SHA-256 | Processed PNG and SHA-256 | Final runtime DDS and SHA-256 |
|---|---|---|---|
| `5d065a262e8ea8d215c9ace35a84e19a3ed39413e20d376a7cbfba1a1400d066` | `docs/assets/gfx_fix_germany_mengele_world_order/source_generated/decision_mengele_hidden_clone_network_candidate_v1_source.png` (`2336a26c1bcf4103b8b1f28c01b0d89198b27a4f86798f48ae1ed1b988d54aac`) | `docs/assets/gfx_fix_germany_mengele_world_order/processed/decision_mengele_hidden_clone_network_candidate_v1.png` (`cc7ebbb55153260b9298ceb1d779cb76faf111ce39d44df53d583288f7807358`) | `gfx/interface/decisions/germany_mengele/decision_mengele_hidden_clone_network.dds` (`12254baeba0fb8391e20d7ef350255fe34ba76e898c327f57879361f646fb4a7`) |

The 32x32 final has a visible alpha bound of 26x22, centered with a 3px horizontal margin and 5px vertical margin. The three pale nodes and red links remain connected and legible, all four canvas corners are transparent, and the alpha range is 0-255.

## Validation and handoff

The final file was converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` using the repository DirectXTex converter. The uncompressed BGRA header is valid, the DDS round-trip matches the processed PNG pixel-for-pixel, and the final path keeps the existing sprite and texture registration unchanged.

The candidate-review sheet is `docs/assets/gfx_fix_germany_mengele_world_order/contact_sheets/decision_mengele_clone_network_candidate_review_v1.png` (SHA-256 `e46261a1178ee7278cd1388d910d9e9b5db24042c0aaad99d59182db8012a378`). The native-source and final-DDS evidence is `docs/assets/gfx_fix_germany_mengele_world_order/contact_sheets/decision_mengele_clone_network_dds_roundtrip_v2.png` (SHA-256 `343b4105dc55ece91595e7b4a0c06ea47fc7ebceb796be0c1ec71f3ca3a48023`) and `docs/assets/gfx_fix_germany_mengele_world_order/processed/decision_mengele_hidden_clone_network_dds_roundtrip_v1.json` (SHA-256 `ba2b80f2367cba9768304aded2de1e4aa85761e68a4399343982da8704e0afb1`).

No `.gfx`, decision, GUI, gameplay, event, or localization file was edited. The parent owns final source integration, and the user owns live-game validation. The parent reports the current HOI4 MCP transport is closed; this handoff relies on direct local source and texture evidence and makes no engine-render claim.

## Orchestrator art check

Use a disposable 1936 Germany fixture on the Mengele Clone Directorate branch with `mengele_clone_decision_hidden_network_unlocked` and `mengele_clone_decision_deepen_network_unlocked` set and `world_end` unset.
Open `germany_final_solution_category` and inspect `dispatch_biomedical_aid_mission` and `deepen_foreign_tank_network` at UI scale 1 without executing either action.
Both rows must show the same three bright pale nodes and connected red links, with clear transparent margins and no dark smudge or clipping.
