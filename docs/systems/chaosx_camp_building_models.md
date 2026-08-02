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

The intact entities are `building_concentration_camp` and `building_extermination_camp`.

The PDX mesh keys are `chaosx_concentration_camp_mesh` and `chaosx_extermination_camp_mesh`.

The model source scale is calibrated against vanilla `TEST_building3.mesh` at source height 2.4649081230 and entity scale 2.0.

The geometry briefs target realistic proportions, muted materials, and restrained medium detail so the buildings fit the vanilla HOI4 map-building language while remaining readable at map distance.

## Runtime wiring

The parent implementation owns the `.gfx` meshsettings, `.asset` entity bindings, runtime `.mesh` and DDS files, and the final live consumer validation.

The existing camp icon keys remain `GFX_building_concentration_camp` and `GFX_building_extermination_camp`; this model package does not replace those 2D icons.

The existing destroyed entities are not silently replaced by an intact custom mesh.

## Map placement constraint

The current mod intentionally has no `map/buildings.txt` override.

The vanilla building-model rules require a map position keyed by the building name unless a validated shared `spawn_point` is used.

The camp definitions use the vanilla `special_project_facility_spawn` point, whose existing map positions are shared by the mod's other static facility buildings.

This keeps the mod's `map/buildings.txt` folder removed while retaining valid map positions for dynamically created camps.

The visual test pair is concentration camp in state 64, province 375, and extermination camp in state 88, province 417; both provinces have vanilla `special_project_facility_spawn` rows.

## Future extensions

If destroyed-state readability is required, add separate custom destroyed meshes through the same one-image and reimport gates rather than aliasing the intact models.

If a dedicated map-placement solution is approved, preserve all required vanilla `map/buildings.txt` rows and record the generated camp rows in each asset manifest.
