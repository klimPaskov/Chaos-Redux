# Runtime handoff: cw_facility

The parent runtime consumer is the existing `cw_facility` building definition in `common/buildings/chaosx_buildings.txt`.

The active entity chain is `cw_facility` -> `building_cw_facility` -> `cw_facility_mesh` -> `gfx/models/buildings/cw_facility.mesh` -> `cw_facility_diffuse.dds`, `cw_facility_normal.dds`, and `cw_facility_specular.dds`.

No skeletal `.anim` action is required because this is a static map-building model.

The parent runtime wiring is complete in `gfx/entities/chaosx_buildings.asset` and `gfx/entities/chaosx_buildings.gfx`, the duplicate model-side declarations are removed, and the pilot placement is verified as state 122 / province 9364.

User-side in-game confirmation remains the final consumer check because the agent does not launch Hearts of Iron IV.
