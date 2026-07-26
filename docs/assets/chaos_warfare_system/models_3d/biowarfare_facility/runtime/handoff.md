# Runtime handoff: biowarfare_facility

The parent runtime consumer is the existing `biowarfare_facility` building definition in `common/buildings/chaosx_buildings.txt`.

The active entity chain is `biowarfare_facility` -> `building_biowarfare_facility` -> `biowarfare_facility_mesh` -> `gfx/models/buildings/biowarfare_facility.mesh` -> `biowarfare_facility_diffuse.dds`, `biowarfare_facility_normal.dds`, and `biowarfare_facility_specular.dds`.

No skeletal `.anim` action is required because this is a static map-building model.

The parent runtime wiring is complete in `gfx/entities/chaosx_buildings.asset` and `gfx/entities/chaosx_buildings.gfx`, the duplicate model-side declarations are removed, and the pilot placement is verified as state 338 / province 6351.

User-side in-game confirmation remains the final consumer check because the agent does not launch Hearts of Iron IV.
