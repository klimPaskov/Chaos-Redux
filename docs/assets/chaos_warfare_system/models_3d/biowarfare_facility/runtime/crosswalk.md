# Runtime crosswalk: biowarfare_facility

| Requirement | Evidence | Runtime surface | State |
| --- | --- | --- | --- |
| Exactly one Meshy input | `refs/original/meshy_input.png` and `refs/original/input_manifest.json` | Meshy image-to-3D request | ready |
| Biological facility identity | `refs/briefs/meshy_input_prompt.md` | `biowarfare_facility_mesh` | complete |
| Static building profile | `job.yaml` | map building entity | calibrated and complete |
| PDX material channels | `textures/processed/`, `textures/dds/` | three stable runtime DDS names | complete |
| `.mesh` export and reimport | `export/mesh/`, `validation/` | `gfx/models/buildings/biowarfare_facility.mesh` | exported and reimported |
| Runtime building consumer | `common/buildings/chaosx_buildings.txt`, `gfx/entities/chaosx_buildings.asset`, `gfx/entities/chaosx_buildings.gfx` | `biowarfare_facility` | wired and deduplicated |
| Valid pilot placement | `validation/placement.json` | startup-history scripted placement | verified against vanilla map data |
