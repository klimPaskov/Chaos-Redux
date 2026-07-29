# Event 020 Rat identity sprite handoff

Runtime-ready DDS and TGA paths are recorded in `rat_identity_asset_manifest.md`. The main agent should add the sprite definitions to the existing Event 020 or shared asset `.gfx` files; this asset tranche does not edit `.gfx` or gameplay files.

Special project: `GFX_sp_black_plague_weaponization` -> `gfx/interface/special_project/project_icons/sp_black_plague_weaponization.dds` (161x98).

Weaponization decisions: `GFX_decision_black_plague_weapon_safety_first`, `GFX_decision_black_plague_weapon_military_acceleration`, `GFX_decision_black_plague_weapon_dual_use`, and `GFX_decision_black_plague_weapon_defensive_conversion` -> matching files under `gfx/interface/decisions/020_black_plague/` (33x32). These names match the live decision icons in `common/decisions/020_black_plague_weaponization_decisions.txt`.

Rat idea pictures should use `GFX_idea_black_plague_rat_brood_instinct`, `GFX_idea_black_plague_rat_no_civilian_economy`, `GFX_idea_black_plague_rat_dominion`, and `GFX_idea_black_plague_rat_king_dominion` from `gfx/interface/ideas/020_black_plague/` (64x64).

Critical Rat focus sprites use the `GFX_goal_black_plague_rat_*` names listed in the plan handoff and `gfx/interface/goals/020_black_plague/` (94x86).

Leader portraits are under `gfx/leaders/020_black_plague/` at 156x210. Add dedicated character portrait definitions before changing the current generic Rat leader consumer. Flags remain root-only and have normal, medium, and small TGA ladders for RTA, RTB, RTC, RTD, RTE, RTF, RTG, RTH, RTI, RTJ, RTK, RTL, RTM, and RTX.

The complete manifest, source PNGs, processed previews, and review contact sheets remain under this active event workspace for parent review.
