# cw_facility model manifest

Status: Runtime candidate complete through export and reimport proof; user-owned live HOI4 validation remains.

The sole Meshy reference is `refs/original/meshy_input.png`, a 1536x1024 RGB PNG with SHA-256 `A963051B9E724478410441B242D0AA15C46D6B4F095AF51236489AD859CCEA08`.

The reference was generated with the built-in Codex image-generation route from `refs/briefs/meshy_input_prompt.md` because no ready repository reference exists for this facility.

The authorized tranche was one Meshy-6 image-to-3D call, one attempt, textured GLB output, and no rigging or animation. Meshy reported 30 credits for this task, versus the 20-credit per-asset estimate and 40-credit two-asset authorization recorded before submission, so the actual two-asset total was 60 credits with no paid retry, remesh, rigging, or animation call.

The downloaded canonical GLB is `provider/downloads/generation_model.glb`, 90,329,256 bytes with SHA-256 `0E9E4514B9EFA31F69A7FC3926EDF2D6C48D37F0A0AE754E9C4DDD0D66D30725`.

The candidate was calibrated against vanilla `gfx/models/buildings/TEST_building3.mesh` at source height 2.464908123 meters and runtime scale 2.0, producing a 2.462154865-meter source height and 4.924309731-meter effective runtime height.

The final export is `export/mesh/cw_facility.mesh`, 4,987,547 bytes with SHA-256 `D728E222725EBE56F6BF3FFB4383643D91073B543414BB50992C20BFECBCD6C7` and 58,002 triangles.

The 30,000-triangle decimation produced a spiky artifact and was rejected; the accepted 58,002-triangle result was a free local reprocess of the downloaded GLB and passed the hard geometry metrics after repair.

The reimport proof is `blender/checkpoints/reimport_cw_facility_mesh.blend` with report `validation/reimport_cw_facility_mesh.json`; it contains one mesh, no armature, no actions, and clean position-welded topology.

The runtime DDS set is `Image_0.dds` diffuse, `Image_1.dds` packed PDX specular, and `Image_2.dds` packed PDX normal, each converted at 1024x1024 and relinked to `PdxMeshAdvanced`.

The parent runtime chain is wired through `building_cw_facility` and `cw_facility_mesh` in `gfx/entities/chaosx_buildings.asset` and `gfx/entities/chaosx_buildings.gfx`, with the duplicate model-side definitions removed.

The documented pilot placement is vanilla state 122, Wales, province 9364, as used by the existing startup-history facility effect and verified against the installed state and province data.
