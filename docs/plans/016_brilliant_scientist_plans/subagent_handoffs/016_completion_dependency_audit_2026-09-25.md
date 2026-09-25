# Event 016 completion dependency audit, 2026-09-25

Disposition: unresolved. This is current source and MCP evidence for the owner queue, not design acceptance or whole-event completion.

## Directorate GUI click regions

The current root is `kruger_directorate_container` in `interface/016_brilliant_scientist_directorate.gui`, attached by `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`. The scripted GUI gives the compact and full panels opposing `brilliant_scientist_directorate_gui_collapsed` visibility and opposing open/close click-enabled triggers. The no-runtime-visibility MCP fixture reported a 100% open/close overlap in both named scenarios; setting the country flag alone still reported that overlap because the inspector did not resolve nested panel visibility from the scripted GUI.

A current explicit expanded fixture with `visibility = { kruger_directorate_compact_panel = false kruger_directorate_full_panel = true }`, open hidden, and close visible passed `hoi4.gui_inspect` with no conflicting click-region diagnostic. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90502ec5212b280c01db76312a574d003170cb5ba65ece548f5f4e43829ba17c/f01bce99ab0942e8fa3a748e2ff951987329298ed921622224743b4fc9f3cdf1/gui-inspect.00337f6998d2bb24.json`. This validates that exact expanded fixture, not the current collapsed state or a visual render. The collapsed inspection did not return a usable result on two attempts and remains unresolved. The existing 2026-09-02 GUI closure handoff contains historical expanded/collapsed renders, but this audit does not promote those to current-source evidence. No GUI source was changed.

## Private provider portfolio

`common/scripted_effects/016_mengele_project_stage_effects.txt` still marks Biological Weapons and Strategic Singularity Deployment/Weaponization as `mengele_event016_stage_output_gap`, so a matching paid receipt is refunded at settlement. `common/decisions/016_mengele_conventional_stage_decisions.txt` has the conventional-family stage rows but no Biological Weapons or Singularity rows. A late-output-only patch would therefore not create a playable paid route. Biological completion requires provider decision and callback wiring plus native project, equipment, and raid predicates while retaining the authoritative native biological stockpile and eighteen raid transactions in `docs/events/016_brilliant_scientist/systems/biological_operations.md`. Singularity additionally requires the provider-local Fallout lock and retry path described in the accepted portfolio plan. These remain accepted and queued; this audit makes no fallback choice and no gameplay source edit.

## Project board and model source

The six generic Directorate selection controls in `common/decisions/016_brilliant_scientist_directorate_project_board.txt` read selection-ready/family/stage values that have no writer in the current source. The working direct family rows use active project receipts. The interaction contract for replacing or removing those six controls and the fifteen-row action budget remain unresolved, as identified in `016_project_board_selection_flow_2026-09-08.md`.

The Temporal Guard runtime model files remain under `gfx/models/units/temporal_guard/`, but the authored job root named by `016_temporal_visual_repair_2026-09-06.md` is absent from this checkout. The accepted geometry-preserving seam/winding repair cannot be reproduced from that handoff alone. Existing geometry was not regenerated or edited.

## Next owner work

Complete one source-proven provider family slice through decisions, late outputs, native receipt gates, localisation, documentation, and targeted validation before calling the portfolio closed. Rerun the Directorate collapsed GUI with a stable explicit visibility fixture and inspect current production renders before a GUI completion claim. Resolve the project-board interaction contract and recover the authored Temporal Guard source job before those surfaces are changed.
