# Event005 Focus Tree Auditor Bounded Reward Patch Handoff

## Scope

Audited only the Event005 Soviet Collapse focus files requested by the parent:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No flag file contents were inspected or edited. The only flag-related operation was the required git status check for flag-path changes.

## References Used

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- Offline wiki snapshot pages for national focus modding, data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding.
- Vanilla documentation:
  - `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- Vanilla focus precedents in `common/national_focus/estonia.txt` and `common/national_focus/germany.txt` showing `custom_effect_tooltip` plus `hidden_effect` reward cleanup.

## Changed Files

- `common/national_focus/005_soviet_collapse_factory_successors.txt`

## Patched Focus IDs

### `MFR_no_peace_without_orders`

Before:

- The focus had an existing summary tooltip, `MFR_no_peace_without_orders_tt`, but still exposed the production boost, artillery stockpile, war support, and `every_neighbor_country` war-goal/AI loop directly in the visible completion reward.

After:

- Kept `unlock_decision_tooltip = mfr_convert_depots_to_arms_lines` visible.
- Kept the existing custom summary tooltip visible.
- Moved the production, equipment, war support, neighbor war-goal loop, and neighbor aggression AI strategy effects into `hidden_effect`.
- Gameplay effect order is preserved after the visible decision unlock.

## Mechanical Audit Findings

- Focus count across the four scoped files remains 1,698.
- No duplicate focus IDs were found.
- The parent-cited `PRA_armored_train_directorate` duplicate helper call is no longer present in the current file. Current call count for `soviet_collapse_update_pra_authority_idea` inside that focus is one.
- Large visible reward offenders remain outside this bounded patch. Current high-risk examples:
  - `OGB_the_old_name_survives_modern_war`
  - ancient restoration expansion focuses: `KZR_expansionist_steppe_levy`, `SOG_expansionist_merchant_claims`, `KHW_expansionist_water_claims`, `ALN_expansionist_mountain_claims`
  - other helper-heavy or long rewards already partly wrapped but still worth parent review: `PRA_rails_over_capitals`, `DSC_congress_of_the_dead_army`, `NRF_northern_revenant_fleet`, `ICD_commissariat_without_end`
- Focus tree size audit confirms several trees are too small for the requested full-depth country identity standard:
  - `PRA_soviet_collapse_focus_tree`: 22 focuses
  - `TSC_soviet_collapse_focus_tree`: 18 focuses
  - `RMC_soviet_collapse_focus_tree`: 18 focuses
  - `DSC_soviet_collapse_focus_tree`: 18 focuses
  - `NRF_soviet_collapse_focus_tree`: 18 focuses
  - `ICD_soviet_collapse_focus_tree`: 18 focuses
  - `OGB_soviet_collapse_focus_tree`: 23 focuses
  - `KZR`, `SOG`, `KHW`, and `ALN` ancient restoration trees: 16 focuses each
- OR prerequisite blocks still frequently merge mutually exclusive choices into shared follow-up pathlines. This is likely visible in game and needs visual/layout review before a completion claim. Examples:
  - `PRA_passport_of_the_moving_state`
  - `DSC_field_hospital_memorials`
  - `DSC_maps_of_lost_armies`
  - `NRF_icebound_marine_guard`
  - `NRF_maps_of_sunken_routes`
  - all template-like `*_industry_plan` convergence focuses in many custom splinter trees
  - ancient restoration charter focuses such as `KZR_khazar_charter`, `SOG_sogdian_city_charter`, `KHW_khwarazmian_water_charter`, and `ALN_alan_pass_charter`
- Same-file coordinate collision counts are high, but many are across separate focus trees stored in the same file. The more actionable pathline audit found nine child focuses with `y` not below their parent, including:
  - `ukr_soviet_collapse_appointed_governors`
  - `ukr_soviet_collapse_breadbasket_empire`
  - `internal_soviet_collapse_sevastopol_road_watch`
  - `internal_soviet_collapse_black_sea_customs_office`
  - `central_asia_soviet_collapse_majlis_elections`
  - `central_asia_soviet_collapse_border_commanders`
  - `central_asia_soviet_collapse_khwarazm_and_older_names`
  - `blr_soviet_collapse_swamp_roads_closed`
  - `blr_soviet_collapse_the_league_depot_at_minsk`

## Remaining Risks and Next Patch Candidates

- Broad route depth is still incomplete for the small custom splinter, OGB, and ancient restoration trees. They need parent-owned expansion into real political, industry, military, diplomacy, expansion, and mechanic branches.
- The ancient restoration expansion focuses should receive dedicated custom tooltips and hidden-effect wrappers in a coordinated pass, because they currently combine claims, manpower/equipment, war goals, AI strategy, hidden assault helpers, and Soviet pressure.
- `OGB_the_old_name_survives_modern_war` needs both reward cleanup and a deeper preceding OGB route. A tooltip-only cleanup would not solve the underlying shallow Old Great Bulgaria tree.
- The recurring `*_industry_plan` OR convergence pattern should be visually reviewed. If the goal is to avoid pathlines through mutually exclusive route choices, these need layout/prerequisite redesign rather than a small local edit.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_factory_successors.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_focus_tree_auditor_bounded_reward_patch_handoff.md`: passed.
- No-flag-touched status check against the touched files plus `gfx/flags` and `interface/flags`: only the national focus file and this handoff appeared.
- Focused parser check:
  - `PRA_armored_train_directorate` has one `soviet_collapse_update_pra_authority_idea = yes` call.
  - `MFR_no_peace_without_orders` has `custom_effect_tooltip = MFR_no_peace_without_orders_tt`.
  - `MFR_no_peace_without_orders` has a `hidden_effect` wrapper.
  - `MFR_no_peace_without_orders` has zero visible `every_neighbor_country` loops before the custom tooltip and one total neighbor loop inside the reward.
