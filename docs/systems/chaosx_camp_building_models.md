# Chaos Redux camp building models

This document is the source of truth for the custom static 3D models used by the existing `concentration_camp` and `extermination_camp` building consumers.

## Scope

The concentration-camp model is a guarded timber-and-brick compound with weathered barracks, a modest administration gatehouse, watchtowers, a practical fence, and a grounded footprint.

The extermination-camp model is a restrained industrial brick compound with one processing hall, one chimney, a utility building, a watchtower, a practical fence, and a grounded footprint.

Both assets are static unrigged map models with no skeletal animations.

Both assets use exactly one clean three-quarter reference image for the Meshy image-to-3D input.

## Asset records

The full production records live under `docs/assets/system_camp_repression_rework/models_3d/concentration_camp_building/` and `docs/assets/system_camp_repression_rework/models_3d/extermination_camp_building/`.

The runtime stems are `chaosx_concentration_camp` and `chaosx_extermination_camp`.

The state gameplay buildings are `concentration_camp` and `extermination_camp`. The visible provincial anchor entities are `building_concentration_camp_site` and `building_extermination_camp_site`.

The PDX mesh keys are `chaosx_concentration_camp_mesh` and `chaosx_extermination_camp_mesh`.

The model source scale is calibrated against vanilla `facility_land.mesh` at source height 3.4697628021 and entity scale 0.6, for an effective runtime height of 2.0818576813. Every export is also checked against a 4-meter maximum runtime footprint.

The geometry briefs target realistic proportions, muted materials, and restrained medium detail so the buildings fit the vanilla HOI4 map-building language while remaining readable at map distance.

## Runtime wiring

The parent implementation owns the `.gfx` meshsettings, `.asset` entity bindings, runtime `.mesh` and DDS files, and the final live consumer validation. The meshsettings use the exported `Mesh_0.001` object name and the vanilla map-building `PdxMeshAdvancedSnow` shader.

The existing camp icon keys remain `GFX_building_concentration_camp` and `GFX_building_extermination_camp`; this model package does not replace those 2D icons.

The existing destroyed entities are not silently replaced by an intact custom mesh.

## Map placement contract

The current mod intentionally has no `map/buildings.txt` override.

The state gameplay buildings do not declare `show_on_map`, `show_on_map_meshes`, `has_destroyed_mesh`, or a spawn point, so the state interface cannot create one map mesh for every state-level camp value.

Each state-level camp is represented by one hidden provincial anchor building. `concentration_camp_site` uses `chaosx_concentration_camp_visual_anchor_spawn`, while `extermination_camp_site` uses `chaosx_extermination_camp_visual_anchor_spawn`; each pool has `max = 1`, and each anchor has `province_max = 1` and `state_max = 1`. They are created with `construct_building_in_random_province` from state scope. Separate pools are required because HOI4 resolves one map entity per spawn point and the two anchors use different meshes.

`chaosx_refresh_camp_visual_anchor` removes stale opposing anchors, preserves an existing same-type anchor, and creates one random valid provincial anchor when the corresponding state gameplay building exists. Extermination sites take visual precedence when both state values coexist. Removing or dismantling the state camp removes both anchor types.

This keeps the `map/buildings.txt` folder removed while retaining a single valid map model per state. The helper is called at creation, registration, refresh, conversion, annexation cleanup, and dismantlement cleanup, so later model replacements cannot reintroduce state-wide visual duplication through a shared pool.

## Future extensions

If destroyed-state readability is required, add separate custom destroyed meshes through the same one-image and reimport gates rather than aliasing the intact models.

Future work can add separate destroyed-state meshes for the provincial anchors only if the anchor definitions opt into `has_destroyed_mesh`. Any such package must retain the one-anchor-per-state contract and the same vanilla scale/footprint gates.
