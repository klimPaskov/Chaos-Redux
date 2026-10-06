> Current parent status: all 47 runtime DDS files were independently reviewed, installed and pixel-verified on 2026-10-06. The worker staging statements below are historical handoff evidence. Final MCP rendering returned Transport closed; live acceptance is pending.

# BBH focus icon staging handoff

**Status:** 47 focus icons are complete in the asset staging package and await parent visual review and runtime promotion.

The mod runtime DDS files and `interface/005_soviet_collapse_focus_icons.gfx` were left untouched.

The current runtime continues to show the old placeholder set until the parent promotes the staged DDS files.

## Scope and evidence

The consumer is `BBH_soviet_collapse_focus_tree` in `common/national_focus/005_soviet_collapse_custom_splinters.txt`.

The parent-provided sprite names remain `GFX_focus_BBH_<suffix>` and `GFX_focus_BBH_<suffix>_shine` in `interface/005_soviet_collapse_focus_icons.gfx`.

Each existing base and shine sprite already points to the matching path under `gfx/interface/goals/005_soviet_collapse/`.

The focused source and localisation review covered all 47 BBH focus ids, titles, descriptions, and completion-reward blocks; the exact source details and visual-subject mapping are recorded per row in `manifest.json`.

The canonical national-focus contact sheet was inspected before individual vanilla references, followed by the focus-piece and focus-background contact sheets and the visual-components catalog.

The component shelves were used as references only; no reference PNG, focus piece, or background component was layered into generated art.

The installed vanilla `GFX_goal_generic_national_unity` sprite and DDS were inspected as the 94x86 consumer precedent.

The canonical reference PNG family is 100x88, while the current BBH placeholders and verified runtime consumer target are 94x86; this package follows the exact 94x86 consumer target, and the existing 100x88 endgame art is normalized without changing its design.

Forty-six final sources are native-alpha ImageGen outputs with retained prompts: 43 direct generations and three focused ImageGen edits.

The birth wing-and-star identity is preserved in a new framed ImageGen edit; only the bespoke endgame artwork is retained from its current DDS source.

All final processed PNGs preserve native alpha, keep a minimum 3 px safe margin, and have a visible-subject mean alpha above 200.

No background-removal fallback was used.

## Package files

`source/` contains the untouched original PNG source for every one of the 47 icons.

`prompts/` contains the exact ImageGen prompts for the generated icons and preserved prompt revisions.

`processed/` contains the centered 94x86 transparent PNGs used for conversion.

`runtime/` contains the staged 94x86 BGRA32 DDS files; these are not installed runtime files.

`previews/after_native_checker.png`, `previews/after_native_dark.png`, and `previews/after_enlarged_review.png` are the before-promotion visual review sheets.

`evidence/before_native_checker.png`, `evidence/before_native_dark.png`, and `evidence/before_focus_raster.png` preserve the pre-change baseline.

`evidence/dds_roundtrip.json` contains strict header inspection and exact decoded-RGBA equality proof for all 47 DDS files.

`evidence/coverage_audit.json` contains the exact source, processed, sprite-alias, staged-DDS, and runtime-target crosswalk.

`evidence/candidate_lineage.json` preserves the rejected candidate sources and prompts for five revised subjects.

`evidence/mcp_focus_review.md` records the bounded read-only focus inspection and raster evidence.

## Conversion and review

All 47 final DDS files were produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

Every staged DDS is an uncompressed one-level BGRA32 texture with a 128-byte header, exact `DDS_PIXELFORMAT` fields and masks, `DDSCAPS_TEXTURE`, 94x86 dimensions, and 32,464 total bytes.

All 47 DDS files decode pixel-for-pixel equal to their processed PNG previews, preserve alpha range 0-255, and have distinct whole-file and decoded-pixel hashes.

The final 47 source PNGs, DDS files, and decoded pixel arrays are unique.

The two pre-existing BBH layout detour warnings and one unrelated continuous-focus localisation warning are recorded in `evidence/mcp_focus_review.md`.

## Exact staged-to-runtime crosswalk

The manifest and coverage receipt contain every source PNG, prompt, processed PNG, sprite alias, staged DDS, runtime texture target, source hash, and final hash.

| Focus id | Existing sprite aliases | Staged DDS | Runtime target |
| --- | --- | --- | --- |
| `BBH_birth` | `GFX_focus_BBH_birth` / `GFX_focus_BBH_birth_shine` | `runtime/focus_005_bbh_birth.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_birth.dds` |
| `BBH_first_guard` | `GFX_focus_BBH_first_guard` / `GFX_focus_BBH_first_guard_shine` | `runtime/focus_005_bbh_first_guard.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_first_guard.dds` |
| `BBH_stores` | `GFX_focus_BBH_stores` / `GFX_focus_BBH_stores_shine` | `runtime/focus_005_bbh_stores.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_stores.dds` |
| `BBH_legitimacy` | `GFX_focus_BBH_legitimacy` / `GFX_focus_BBH_legitimacy_shine` | `runtime/focus_005_bbh_legitimacy.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_legitimacy.dds` |
| `BBH_rival` | `GFX_focus_BBH_rival` / `GFX_focus_BBH_rival_shine` | `runtime/focus_005_bbh_rival.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_rival.dds` |
| `BBH_doctrine` | `GFX_focus_BBH_doctrine` / `GFX_focus_BBH_doctrine_shine` | `runtime/focus_005_bbh_doctrine.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_doctrine.dds` |
| `BBH_economy` | `GFX_focus_BBH_economy` / `GFX_focus_BBH_economy_shine` | `runtime/focus_005_bbh_economy.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_economy.dds` |
| `BBH_league` | `GFX_focus_BBH_league` / `GFX_focus_BBH_league_shine` | `runtime/focus_005_bbh_league.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_league.dds` |
| `BBH_foreign` | `GFX_focus_BBH_foreign` / `GFX_focus_BBH_foreign_shine` | `runtime/focus_005_bbh_foreign.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_foreign.dds` |
| `BBH_diplomatic_plan` | `GFX_focus_BBH_diplomatic_plan` / `GFX_focus_BBH_diplomatic_plan_shine` | `runtime/focus_005_bbh_diplomatic_plan.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_diplomatic_plan.dds` |
| `BBH_anti_protectorate_letters` | `GFX_focus_BBH_anti_protectorate_letters` / `GFX_focus_BBH_anti_protectorate_letters_shine` | `runtime/focus_005_bbh_anti_protectorate_letters.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_anti_protectorate_letters.dds` |
| `BBH_temporary_free_city_pacts` | `GFX_focus_BBH_temporary_free_city_pacts` / `GFX_focus_BBH_temporary_free_city_pacts_shine` | `runtime/focus_005_bbh_temporary_free_city_pacts.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_temporary_free_city_pacts.dds` |
| `BBH_no_masters_clause` | `GFX_focus_BBH_no_masters_clause` / `GFX_focus_BBH_no_masters_clause_shine` | `runtime/focus_005_bbh_no_masters_clause.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_no_masters_clause.dds` |
| `BBH_foreign_fear_mediation` | `GFX_focus_BBH_foreign_fear_mediation` / `GFX_focus_BBH_foreign_fear_mediation_shine` | `runtime/focus_005_bbh_foreign_fear_mediation.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_foreign_fear_mediation.dds` |
| `BBH_black_banner_war_council` | `GFX_focus_BBH_black_banner_war_council` / `GFX_focus_BBH_black_banner_war_council_shine` | `runtime/focus_005_bbh_black_banner_war_council.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_black_banner_war_council.dds` |
| `BBH_no_hostage_committees` | `GFX_focus_BBH_no_hostage_committees` / `GFX_focus_BBH_no_hostage_committees_shine` | `runtime/focus_005_bbh_no_hostage_committees.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_no_hostage_committees.dds` |
| `BBH_inner_faction` | `GFX_focus_BBH_inner_faction` / `GFX_focus_BBH_inner_faction_shine` | `runtime/focus_005_bbh_inner_faction.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_inner_faction.dds` |
| `BBH_special_arm` | `GFX_focus_BBH_special_arm` / `GFX_focus_BBH_special_arm_shine` | `runtime/focus_005_bbh_special_arm.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_special_arm.dds` |
| `BBH_column_schools` | `GFX_focus_BBH_column_schools` / `GFX_focus_BBH_column_schools_shine` | `runtime/focus_005_bbh_column_schools.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_column_schools.dds` |
| `BBH_supply` | `GFX_focus_BBH_supply` / `GFX_focus_BBH_supply_shine` | `runtime/focus_005_bbh_supply.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_supply.dds` |
| `BBH_enemy_front` | `GFX_focus_BBH_enemy_front` / `GFX_focus_BBH_enemy_front_shine` | `runtime/focus_005_bbh_enemy_front.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_enemy_front.dds` |
| `BBH_war_plan` | `GFX_focus_BBH_war_plan` / `GFX_focus_BBH_war_plan_shine` | `runtime/focus_005_bbh_war_plan.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_war_plan.dds` |
| `BBH_mobile_court_posts` | `GFX_focus_BBH_mobile_court_posts` / `GFX_focus_BBH_mobile_court_posts_shine` | `runtime/focus_005_bbh_mobile_court_posts.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_mobile_court_posts.dds` |
| `BBH_armored_car_raids` | `GFX_focus_BBH_armored_car_raids` / `GFX_focus_BBH_armored_car_raids_shine` | `runtime/focus_005_bbh_armored_car_raids.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_armored_car_raids.dds` |
| `BBH_prison_break_networks` | `GFX_focus_BBH_prison_break_networks` / `GFX_focus_BBH_prison_break_networks_shine` | `runtime/focus_005_bbh_prison_break_networks.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_prison_break_networks.dds` |
| `BBH_roving_artillery_crews` | `GFX_focus_BBH_roving_artillery_crews` / `GFX_focus_BBH_roving_artillery_crews_shine` | `runtime/focus_005_bbh_roving_artillery_crews.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_roving_artillery_crews.dds` |
| `BBH_scorched_prison_roads` | `GFX_focus_BBH_scorched_prison_roads` / `GFX_focus_BBH_scorched_prison_roads_shine` | `runtime/focus_005_bbh_scorched_prison_roads.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_scorched_prison_roads.dds` |
| `BBH_civil_rule` | `GFX_focus_BBH_civil_rule` / `GFX_focus_BBH_civil_rule_shine` | `runtime/focus_005_bbh_civil_rule.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_civil_rule.dds` |
| `BBH_commune_mediation` | `GFX_focus_BBH_commune_mediation` / `GFX_focus_BBH_commune_mediation_shine` | `runtime/focus_005_bbh_commune_mediation.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_commune_mediation.dds` |
| `BBH_non_domination_pacts` | `GFX_focus_BBH_non_domination_pacts` / `GFX_focus_BBH_non_domination_pacts_shine` | `runtime/focus_005_bbh_non_domination_pacts.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_non_domination_pacts.dds` |
| `BBH_propaganda` | `GFX_focus_BBH_propaganda` / `GFX_focus_BBH_propaganda_shine` | `runtime/focus_005_bbh_propaganda.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_propaganda.dds` |
| `BBH_settlement` | `GFX_focus_BBH_settlement` / `GFX_focus_BBH_settlement_shine` | `runtime/focus_005_bbh_settlement.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_settlement.dds` |
| `BBH_radical_turn` | `GFX_focus_BBH_radical_turn` / `GFX_focus_BBH_radical_turn_shine` | `runtime/focus_005_bbh_radical_turn.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_radical_turn.dds` |
| `BBH_industry_plan` | `GFX_focus_BBH_industry_plan` / `GFX_focus_BBH_industry_plan_shine` | `runtime/focus_005_bbh_industry_plan.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_industry_plan.dds` |
| `BBH_captured_rail_stores` | `GFX_focus_BBH_captured_rail_stores` / `GFX_focus_BBH_captured_rail_stores_shine` | `runtime/focus_005_bbh_captured_rail_stores.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_captured_rail_stores.dds` |
| `BBH_column_supply_ledgers` | `GFX_focus_BBH_column_supply_ledgers` / `GFX_focus_BBH_column_supply_ledgers_shine` | `runtime/focus_005_bbh_column_supply_ledgers.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_column_supply_ledgers.dds` |
| `BBH_workshop_cells` | `GFX_focus_BBH_workshop_cells` / `GFX_focus_BBH_workshop_cells_shine` | `runtime/focus_005_bbh_workshop_cells.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_workshop_cells.dds` |
| `BBH_red_and_black_depots` | `GFX_focus_BBH_red_and_black_depots` / `GFX_focus_BBH_red_and_black_depots_shine` | `runtime/focus_005_bbh_red_and_black_depots.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_red_and_black_depots.dds` |
| `BBH_field_hospital_columns` | `GFX_focus_BBH_field_hospital_columns` / `GFX_focus_BBH_field_hospital_columns_shine` | `runtime/focus_005_bbh_field_hospital_columns.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_field_hospital_columns.dds` |
| `BBH_hidden_doctrine` | `GFX_focus_BBH_hidden_doctrine` / `GFX_focus_BBH_hidden_doctrine_shine` | `runtime/focus_005_bbh_hidden_doctrine.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_hidden_doctrine.dds` |
| `BBH_black_column_registers` | `GFX_focus_BBH_black_column_registers` / `GFX_focus_BBH_black_column_registers_shine` | `runtime/focus_005_bbh_black_column_registers.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_black_column_registers.dds` |
| `BBH_railway_state_sabotage` | `GFX_focus_BBH_railway_state_sabotage` / `GFX_focus_BBH_railway_state_sabotage_shine` | `runtime/focus_005_bbh_railway_state_sabotage.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_railway_state_sabotage.dds` |
| `BBH_borderless_column_schools` | `GFX_focus_BBH_borderless_column_schools` / `GFX_focus_BBH_borderless_column_schools_shine` | `runtime/focus_005_bbh_borderless_column_schools.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_borderless_column_schools.dds` |
| `BBH_banner_without_borders` | `GFX_focus_BBH_banner_without_borders` / `GFX_focus_BBH_banner_without_borders_shine` | `runtime/focus_005_bbh_banner_without_borders.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_banner_without_borders.dds` |
| `BBH_extreme_gate` | `GFX_focus_BBH_extreme_gate` / `GFX_focus_BBH_extreme_gate_shine` | `runtime/focus_005_bbh_extreme_gate.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_extreme_gate.dds` |
| `BBH_endgame` | `GFX_focus_BBH_endgame` / `GFX_focus_BBH_endgame_shine` | `runtime/focus_005_bbh_endgame.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_endgame.dds` |
| `BBH_extreme_path` | `GFX_focus_BBH_extreme_path` / `GFX_focus_BBH_extreme_path_shine` | `runtime/focus_005_bbh_extreme_path.dds` | `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_extreme_path.dds` |

## Parent promotion

Review the native-size checker and dark sheets, enlarged sheet, manifest, candidate lineage, and DDS round-trip receipt before promotion.

After review, promote each file from `runtime/focus_005_bbh_<suffix>.dds` to the matching `gfx/interface/goals/005_soviet_collapse/focus_005_bbh_<suffix>.dds` target shown in the crosswalk.

No sprite-name or `.gfx` edits are required because the registered base and shine aliases already use these exact paths.

After promotion, rerender `BBH_soviet_collapse_focus_tree` through the HOI4 focus raster route if that MCP route is available.

This package contains staging evidence only and makes no in-game acceptance claim.

The repository ignores `docs/assets/` at `.gitignore:80`; parent-owned commit work must explicitly add the reviewed package if it is intended for version control.
