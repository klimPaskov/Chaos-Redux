# Chaos warfare facility models

This package provides two production static map-building models for the existing Chaos Redux warfare buildings: `biowarfare_facility` and `cw_facility`.

The biological model presents a secure biological research and containment complex with sealed laboratory blocks, cleanroom volumes, quarantine airlocks, decontamination entrances, filtered ventilation towers, containment tanks, and a controlled loading bay.

The chemical model presents a distinct chemical research, production, storage, and decontamination complex with sealed production halls, pressure vessels, scrubber towers, pipe racks, chemical storage tanks, bermed loading bays, and decontamination structures.

Both assets are static map entities and intentionally have no armature, skeletal action, `.anim` file, animated state, people, vehicles, terrain, roads, trees, smoke, explosions, floating scenery, readable text, decals, logos, damaged state, or alternate variant.

## Runtime chain

The existing building definitions remain the gameplay owners for `biowarfare_facility` and `cw_facility` in `common/buildings/chaosx_buildings.txt`.

Each building uses the existing `special_project_facility_spawn` map spawn point and resolves to its dedicated entity through the `building_<building_id>` naming convention.

The active runtime chain is `biowarfare_facility` -> `building_biowarfare_facility` -> `biowarfare_facility_mesh` -> `gfx/models/buildings/biowarfare_facility.mesh` -> the three stable biological DDS files.

The active runtime chain is `cw_facility` -> `building_cw_facility` -> `cw_facility_mesh` -> `gfx/models/buildings/cw_facility.mesh` -> the three stable chemical DDS files.

Both entities are declared in `gfx/entities/chaosx_buildings.asset` with an `idle` default state and are backed by the sole active model declarations in `gfx/entities/chaosx_buildings.gfx`.

The duplicate `gfx/models/buildings/chaosx_mesh.gfx`, `gfx/models/buildings/biowarfare_facility.asset`, and `gfx/models/buildings/cw_facility.asset` definitions were removed so each custom mesh name has one authoritative declaration.

## Vanilla scale crosswalk

The installed vanilla reference is `gfx/models/buildings/TEST_building3.mesh`, whose imported object is `TEST_building3`, source height is 2.464908123 meters, and vanilla special-project entity scale is 2.0.

The reference therefore has an effective runtime height of 4.929816246 meters, and the custom entities use the same single runtime scale of 2.0 in `gfx/entities/chaosx_buildings.gfx`.

The biological candidate is 2.459402084 meters at source scale and 4.918804168 meters at runtime scale, which is 0.011012077 meters below the reference effective height.

The chemical candidate is 2.462154865 meters at source scale and 4.924309731 meters at runtime scale, which is 0.005506516 meters below the reference effective height.

Both packages use Z-up and -Y-forward orientation with ground contact at the world origin.

## Geometry and materials

The biological export contains 30,000 triangles, dimensions 7.789175 by 8.022599 by 2.459402 meters, and zero boundary, loose-edge, non-manifold, degenerate-face, and zero-length-normal defects in the export audit.

The chemical export contains 58,002 triangles, dimensions 6.674174 by 6.674461 by 2.462155 meters, and zero boundary, loose-edge, non-manifold, degenerate-face, and zero-length-normal defects in the export audit.

The chemical 30,000-triangle decimation was rejected because its preview had a spiky artifact, and the accepted 58,002-triangle result was produced by a free local reprocess of the same downloaded GLB without another paid provider call.

Each material uses one `PdxMeshAdvanced` slot with diffuse `Image_0.dds`, packed PDX specular `Image_1.dds`, and packed PDX normal `Image_2.dds` before the runtime filenames are assigned in the GFX declarations.

The packed PDX specular convention is R=0, G=32, B=metallic, and alpha=roughness, and the packed normal convention is the repository pipeline’s PDX normal layout.

The authoritative source GLB is retained in each job’s `provider/downloads/` directory, and the proof checkpoints are retained under each job’s `blender/checkpoints/` directory.

## Meshy and animation policy

Each facility used exactly one generated 1536x1024 RGB reference image as the sole Meshy input, with no multi-view sheet, turnaround board, side-profile sheet, or second image.

Meshy-6 produced one textured GLB for each facility, and no animation or rigging call was made because the requested consumers are static map-building entities.

The two provider calls reported 30 credits each despite the pre-call estimate of 20 credits per asset and the recorded two-asset authorization of 40 credits, so the actual total was 60 credits with no paid retry, remesh, rigging, or animation call.

## Icons and UI references

No new icon files are required for these model packages.

The existing building definition icon keys are `GFX_building_biowarfare_facility` and `GFX_building_cw_facility`.

Those keys are declared in `interface/chaosx_buildings.gfx` and reuse `gfx/interface/special_project/specialization_biowarfare.dds` and `gfx/interface/special_project/specialization_cw.dds` respectively.

The associated specialization keys are `GFX_specialization_biowarfare` and `GFX_specialization_cw`, and no gameplay or localisation key was changed by the model integration.

## Pilot placement evidence

The biological pilot pair is state 338, Gloucestershire, province 6351, and the exact pair is already used by `chaosx_add_startup_biowarfare_facility_6351`.

The chemical pilot pair is state 122, Wales, province 9364, and the exact pair is already used by `chaosx_add_startup_cw_facility_9364`.

The installed vanilla state files contain those provinces, and the installed province definitions classify both as land provinces, so no permanent `map/buildings.txt` row was added that would force a building into every new game.

## Future plans

Future work can add a separate destroyed-state mesh only if the building definitions later opt into `has_destroyed_mesh`, and that should be treated as a new asset profile rather than reusing these intact static packages.

Future work can add snow-aware material variants only after a runtime map review demonstrates that the current `PdxMeshAdvanced` material needs seasonal treatment.

Future work can add a non-transform-only idle animation only if the building consumer changes from static map geometry to a real skeletal entity, with a separate `.anim` export and reimport proof.
