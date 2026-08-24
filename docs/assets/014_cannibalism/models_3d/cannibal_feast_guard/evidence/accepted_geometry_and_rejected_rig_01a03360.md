# Accepted Feast Guard geometry and recovered rig `01a03360`

## Accepted provider source

- Meshy 7 T-pose generation `01a0334e-9b15-7d8f-9613-35480823152c`, 30 credits.
- Exact input `refs/original/meshy_input.png`, SHA-256 `C67AF852A27E1379590BD84C5175C378D449AE226F895A2D326B45099040D8C9`.
- Original generation GLB `provider/downloads/tpose_recovery_01a0334e.glb`, SHA-256 `B56C924892CFC88BD8897E1B5A89DF0A84A4957E2A1766ED445EC802BCF420AC`.
- Triangle remesh `01a03355-f41d-7165-832b-cc024b02093b`, 5 credits; accepted GLB SHA-256 `77C5FB2A24DE95FECACAA7879B07380D5D64219EF2106CBB2419D44EEE11B694`.
- Humanoid rig `01a03360-9a5f-7790-b3b8-83e3bb5d1094`, 5 credits; rigged GLB SHA-256 `4D2534B91B6D400CE66DC987E44B4620CC405869C7AEF35C393EEF3E759DCDEF`.

The accepted geometry passes the user gate: living exposed flesh, visible red/blood markings, rough hides/scavenged cloth, horned skull mask and bone trophies, and two separate oversized crude cleavers. It is not knightly, undead, skeletal, goblin-like, polished, or culturally identifiable.

## Bounded provider-defect recovery

The raw rig added a standalone object named `Icosphere`. It has 42 vertices, zero vertex groups, no armature modifier, no semantic role, and no topology contact with the character. Parent authorized excluding only that object from a duplicated working collection. The raw provider checkpoint remains unchanged at `blender/checkpoints/rigged_raw_01a03360_preserved.blend`, SHA-256 `AC716D74ED0394B52A9E5C4E0A688B7502715CE50C319FE4094715612EC3D01C`.

The earlier sanitizer path was rejected because it destroyed material image nodes. After the repository adapter exposed material-preserving `weight_only=true`, the rig was rebuilt from the immutable checkpoint, the exact provider PBR maps were relinked, and the bounded top-four cleanup was repeated. The accepted request affected 293 vertices, removed 302 excess influences, renormalized 47,141 vertices, and left zero over-four and zero zero-weight deforming vertices. Topology, positions, UVs, material slots, image nodes, textures, both cleavers, armature metadata, parenting, and transforms were preserved. Accepted bind checkpoint: `blender/checkpoints/09_feast_guard_bind_pbr_weight_only_v192_01a03360.blend`, SHA-256 `B3BB03B5B08EDDC924333599075AB0101BDE26848C665E6113E518CF169C5F3F`.

## Deformation and final acceptance

All eight distinct Meshy actions were imported against this recovered bind and visually reviewed across multiple phases. Both cleavers remain attached and readable; there is no sphere/blob, tearing, geometry explosion, material loss, or static/transform-only fallback. Hips-only per-frame ground correction removed hover and penetration while preserving the provider body and weapon keys. Final checkpoint: `blender/checkpoints/12_grounded_08_death_pbr_v192_01a033bd.blend`, SHA-256 `5BC019D7BE706EA7DAB642AD7A2F663280AD54C19722A1E400E2ABDD76CB1080`.

The final PDX mesh and all eight animations reimport successfully. Detailed lineage, action ids, hashes, contact samples, texture evidence, costs, and runtime paths are in `manifest.md`, `manifest.json`, `provider/provider_lineage.json`, and `runtime/handoff.md`.
