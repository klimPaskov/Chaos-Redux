# Event 012 Focus-Family Icon Coverage Crosswalk

## Coverage result

The current Event 012 focus tree uses 13 unique family-level icon sprite IDs 276 times. Every ID maps directly to an exact `asset_key` row in `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix.csv`. No derived, substituted, or unmatched asset was needed.

All textures are complete. Runtime registration is deliberately pending because this asset-only tranche does not edit `.gfx` files. The ready-to-copy registration is in `gfx_handoff.md`.

| Matrix disposition | Count |
| --- | ---: |
| Direct exact-row match | 13 |
| Derived from a broader row | 0 |
| Unmatched requirement | 0 |

## Requirement-to-runtime crosswalk

| Matrix asset key | Exact live sprite consumer | Uses in current tree | Final texture | State binding | Runtime status |
| --- | --- | ---: | --- | --- | --- |
| `focus_family_host_proclamation` | `GFX_goal_africa_focus_family_host_proclamation` | 12 | `gfx/interface/goals/012_africa/goal_africa_focus_family_host_proclamation.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_host_legitimacy` | `GFX_goal_africa_focus_family_host_legitimacy` | 34 | `gfx/interface/goals/012_africa/goal_africa_focus_family_host_legitimacy.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_charter_law` | `GFX_goal_africa_focus_family_charter_law` | 25 | `gfx/interface/goals/012_africa/goal_africa_focus_family_charter_law.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_continental_representation` | `GFX_goal_africa_focus_family_continental_representation` | 36 | `gfx/interface/goals/012_africa/goal_africa_focus_family_continental_representation.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_protection_guarantee` | `GFX_goal_africa_focus_family_protection_guarantee` | 32 | `gfx/interface/goals/012_africa/goal_africa_focus_family_protection_guarantee.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_volunteer_intervention` | `GFX_goal_africa_focus_family_volunteer_intervention` | 1 | `gfx/interface/goals/012_africa/goal_africa_focus_family_volunteer_intervention.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_aid_and_relief` | `GFX_goal_africa_focus_family_aid_and_relief` | 23 | `gfx/interface/goals/012_africa/goal_africa_focus_family_aid_and_relief.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_regional_congress` | `GFX_goal_africa_focus_family_regional_congress` | 33 | `gfx/interface/goals/012_africa/goal_africa_focus_family_regional_congress.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_road_corridor` | `GFX_goal_africa_focus_family_road_corridor` | 1 | `gfx/interface/goals/012_africa/goal_africa_focus_family_road_corridor.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_rail_corridor` | `GFX_goal_africa_focus_family_rail_corridor` | 32 | `gfx/interface/goals/012_africa/goal_africa_focus_family_rail_corridor.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_army_common_reserve` | `GFX_goal_africa_focus_family_army_common_reserve` | 23 | `gfx/interface/goals/012_africa/goal_africa_focus_family_army_common_reserve.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_resource_sovereignty` | `GFX_goal_africa_focus_family_resource_sovereignty` | 23 | `gfx/interface/goals/012_africa/goal_africa_focus_family_resource_sovereignty.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |
| `focus_family_rival_bloc` | `GFX_goal_africa_focus_family_rival_bloc` | 1 | `gfx/interface/goals/012_africa/goal_africa_focus_family_rival_bloc.dds` | static; regular and `_shine` use the same DDS | texture ready; registration pending |

## Consumer and evidence locations

- Current consumer surface: `common/national_focus/012_africa_continental_focus_tree.txt`
- Source matrix: `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix.csv`
- Pixel and DDS audit: `validation/focus_icon_validation.tsv`
- Visual review: `contact_sheets/focus_icon_processed_checker_contact_sheet.png`
- DDS decode review: `contact_sheets/focus_icon_dds_decoded_contact_sheet.png`

## Matrix scope note

The matrix rows describe coordinated icon families and ultimately require one distinct icon for every final focus. The current tree instead consumes the 13 family-level sprite IDs above. This package supplies a distinct static baseline for every live family-level consumer; it does not mark the matrix's eventual per-focus expansion as complete, and the source matrix remains untouched and `planned`.
