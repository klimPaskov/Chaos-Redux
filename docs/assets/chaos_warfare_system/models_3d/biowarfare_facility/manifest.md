# biowarfare_facility model manifest

Status: Runtime candidate complete through export and reimport proof; user-owned live HOI4 validation remains.

The sole Meshy reference is `refs/original/meshy_input.png`, a 1536x1024 RGB PNG with SHA-256 `1860B4D1B7328DE3ADD4803C2FAFA4AB6749E821E9E940978E85E40C08F8C68C`.

The reference was generated with the built-in Codex image-generation route from `refs/briefs/meshy_input_prompt.md` because no ready repository reference exists for this facility.

The authorized tranche was one Meshy-6 image-to-3D call, one attempt, textured GLB output, and no rigging or animation. Meshy reported 30 credits for this task, versus the 20-credit per-asset estimate and 40-credit two-asset authorization recorded before submission, so the actual two-asset total was 60 credits with no paid retry, remesh, rigging, or animation call.

The downloaded canonical GLB is `provider/downloads/generation_model.glb`, 44,569,916 bytes with SHA-256 `773C6956ACC78310C4C76B3C12B5933AE84368590201132A0F6A3E92702C1803`.

The candidate was calibrated against vanilla `gfx/models/buildings/TEST_building3.mesh` at source height 2.464908123 meters and runtime scale 2.0, producing a 2.459402084-meter source height and 4.918804168-meter effective runtime height.

The final export is `export/mesh/biowarfare_facility.mesh`, 1,744,835 bytes with SHA-256 `73EACE3A6E4ACABEE0E3EA01816771E3E513907DD291A82B02CB0027C1B3ECA0` and 30,000 triangles.

The reimport proof is `blender/checkpoints/reimport_biowarfare_facility_mesh.blend` with report `validation/reimport_biowarfare_facility_mesh.json`; it contains one mesh, no armature, no actions, and clean position-welded topology.

The runtime DDS set is `Image_0.dds` diffuse, `Image_1.dds` packed PDX specular, and `Image_2.dds` packed PDX normal, each converted at 1024x1024 and relinked to `PdxMeshAdvanced`.

The parent runtime chain is wired through `building_biowarfare_facility` and `biowarfare_facility_mesh` in `gfx/entities/chaosx_buildings.asset` and `gfx/entities/chaosx_buildings.gfx`, with the duplicate model-side definitions removed.

The documented pilot placement is vanilla state 338, Gloucestershire, province 6351, as used by the existing startup-history facility effect and verified against the installed state and province data.
