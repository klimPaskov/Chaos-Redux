# Chaos Redux 3D runtime contract

This contract applies to every static HOI4 map-building model shipped by Chaos Redux.

## Scale and footprint

Measure a comparable installed vanilla mesh and its actual entity consumer before normalizing a candidate. A height-only comparison is not sufficient for map buildings.

The current building profile uses `facility_land.mesh` with `building_land_facility` at source height `3.4697628021`, entity scale `0.6`, and effective runtime height `2.0818576813`. The profile rejects a candidate whose runtime X/Y footprint exceeds `4.0` meters unless the job explicitly requests `fit_to_budget`; that option applies one uniform X/Y fit and records the factor.

The model must be grounded, use one authoritative exported mesh object, and pass the pre-export topology gate. Reimport evidence must record the object name, triangle count, dimensions, and the position-welded topology diagnostic.

## Materials

Map-building GFX follows the installed vanilla consumer shader, currently `PdxMeshAdvancedSnow`. The GFX meshsettings name must match the object name in the exported `.mesh`, not a provider or job label.

Runtime maps are rebuilt from immutable provider sources. Diffuse is `Image_0`, packed PDX specular is `Image_1` with R=0, G=32, B=metallic, alpha=roughness, and packed PDX normal is `Image_2` with the repository PDX tangent-channel layout. The material pack reports channel statistics and runtime DDS dimensions.

## Placement

Never attach a custom map-building model to the vanilla shared `special_project_facility_spawn` pool. A facility that is itself a map building uses a dedicated `type = province`, `max = 1` spawn pool.

When gameplay is state-level but the visual must appear once, keep the gameplay building non-map and create a hidden provincial visual-anchor building with `province_max = 1`, `state_max = 1`, a dedicated spawn pool, and `construct_building_in_random_province` from state scope. Add explicit cleanup and conversion logic for the anchor.

This workflow does not require `map/buildings.txt`. The only permanent placement evidence required is the dedicated spawn declaration, the state-scope construction helper, and a runtime consumer audit.

## Completion evidence

A production handoff includes the calibrated vanilla reference, pre-export and reimport reports, material channel statistics, runtime mesh and DDS hashes, the exact GFX/entity/building consumers, the placement/anchor contract, and a parent-owned live screenshot. Static map buildings have no skeletal `.anim` deliverable unless the consumer is intentionally changed to an animated entity.
