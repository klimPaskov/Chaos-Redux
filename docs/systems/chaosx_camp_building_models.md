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

The state gameplay buildings are `concentration_camp` and `extermination_camp`. They render directly through `building_chaosx_concentration_camp_visual_anchor_spawn` and `building_chaosx_extermination_camp_visual_anchor_spawn`; the older site entities remain registered only for save and script compatibility.

The PDX mesh keys are `chaosx_concentration_camp_mesh` and `chaosx_extermination_camp_mesh`.

The model source scale is calibrated against vanilla `facility_land.mesh` at source height 3.4697628021 and entity scale 0.6, for an effective runtime height of 2.0818576813. Every export is also checked against a 4-meter maximum runtime footprint.

The geometry briefs target realistic proportions, muted materials, and restrained medium detail so the buildings fit the vanilla HOI4 map-building language while remaining readable at map distance.

## Runtime wiring

The parent implementation owns the `.gfx` meshsettings, `.asset` entity bindings, runtime `.mesh` and DDS files, and the final live consumer validation. The meshsettings use the exported `Mesh_0.001` object name and the vanilla map-building `PdxMeshAdvancedSnow` shader.

The existing camp icon keys remain `GFX_building_concentration_camp` and `GFX_building_extermination_camp`; this model package does not replace those 2D icons.

The existing destroyed entities are not silently replaced by an intact custom mesh.

## Map placement contract

The mod ships a generated `map/buildings.txt` override that preserves the complete installed vanilla table and adds custom spawn coordinates inside every land province covered by the vanilla special-project facility pool.

Both gameplay buildings are direct map consumers. Their dedicated spawn pools each provide five positions, so every existing concentration or extermination level receives its own visible model. Separate pools are required because HOI4 resolves one map entity per spawn point and the two camp types use different meshes.

The two buildings share the `chaosx_camp_network` state cap of five. Concentration camps are normally buildable. Extermination camps remain non-buildable and can only be produced when a decision or scripted event removes one concentration level and adds one extermination level. Once the first extermination level exists, its state modifier blocks further concentration-camp construction. Historical heavy sites begin above level one; the Auschwitz program establishes three total camp levels and converts one of them for the experimental extermination layer.

The camp spawn pools disable automatic nudging because their complete custom coordinate coverage is generated and maintained in `map/buildings.txt`.

`chaosx_refresh_camp_visual_anchor` is now compatibility cleanup: it removes obsolete hidden anchor levels left by earlier implementations. Creation, conversion, annexation cleanup, and dismantlement operate on the gameplay buildings themselves. The generated coordinate table keeps all five concentration and all five extermination positions spatially distinct where province geometry permits it.

## Future extensions

If destroyed-state readability is required, add separate custom destroyed meshes through the same one-image and reimport gates rather than aliasing the intact models.

Future work can add separate destroyed-state meshes if the direct gameplay consumers opt into `has_destroyed_mesh`. Any such package must retain the five-position-per-type contract and the same vanilla scale and footprint gates.
