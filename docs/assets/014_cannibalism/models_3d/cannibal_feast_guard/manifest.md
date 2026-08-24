# Cannibal Feast Guard 3D package manifest

Status: `package_complete_parent_runtime_wiring_pending`.

The package contains the accepted Meshy 7 dual-cleaver Feast Guard, a preserved provider checkpoint, a material-preserving top-four weight cleanup, eight distinct genuine Meshy actions, PDX mesh/animation exports with grounded reimport proof, 1024×1024 DDS textures, six sourced WAV files, and the bespoke counter-art handoff. Gameplay, `.asset`, entity, GFX, and sound-definition wiring remain parent-owned; no in-game completion is claimed.

## Source and accepted provider lineage

- User-supplied source: `refs/source/untouched.png`, SHA-256 `0627D4AE2AED2997791C439DEBFCDE79DA86CC5BFA1E97F75211C7E085ADF710`.
- Exact-one approved Meshy input: `refs/original/meshy_input.png`, SHA-256 `C67AF852A27E1379590BD84C5175C378D449AE226F895A2D326B45099040D8C9`.
- Accepted Meshy 7 generation: `01a0334e-9b15-7d8f-9613-35480823152c`.
- Accepted triangle remesh: `01a03355-f41d-7165-832b-cc024b02093b`; GLB SHA-256 `77C5FB2A24DE95FECACAA7879B07380D5D64219EF2106CBB2419D44EEE11B694`.
- Accepted humanoid rig: `01a03360-9a5f-7790-b3b8-83e3bb5d1094`; rigged GLB SHA-256 `4D2534B91B6D400CE66DC987E44B4620CC405869C7AEF35C393EEF3E759DCDEF`.
- Immutable raw provider checkpoint: `blender/checkpoints/rigged_raw_01a03360_preserved.blend`, SHA-256 `AC716D74ED0394B52A9E5C4E0A688B7502715CE50C319FE4094715612EC3D01C`.
- Rejected rig lineages `01a03317` and `01a0332e` lost weapons and/or introduced invalid provider geometry. Failed provider rig `01a02a8d-028c-74bb-aec1-dadd88884761` consumed zero credits. Rejected files remain evidence only.
- Total consumed credits for the recorded recovery lineage: 134 (three 30-credit generations, two rejected 5-credit rigs, one 5-credit remesh, one accepted 5-credit rig, eight 3-credit animations; failed rig 0).

## Geometry, materials, rig, and weights

- Final PDX mesh: `export/mesh/cannibal_feast_guard.mesh`, SHA-256 `4F2F8E22B2E479521E48B627D3769383FF48DDD6C95B8EC197639C7068FE7FEE`.
- Reimport result: one skinned mesh, 41,873 vertices, 29,997 triangles, `map1` UV layer, one 24-bone armature, zero degenerate faces, zero non-manifold edges, zero-length normals absent, and no negative-scale object.
- The provider-only standalone `Icosphere` was excluded after proving it had 42 vertices, no vertex groups, no modifiers, and no semantic or topology contact with `char1`. The provider source checkpoint remains unchanged.
- Material-preserving weight-only cleanup affected 293 vertices and removed 302 excess influences. Final state has no vertex above four influences and no zero-weight deforming vertex. Topology, vertex positions, UVs, skeleton metadata, transforms, weapon-bearing mesh, material slots, image nodes, and provider texture identity were preserved.
- Final grounded action checkpoint: `blender/checkpoints/12_grounded_08_death_pbr_v192_01a033bd.blend`, SHA-256 `5BC019D7BE706EA7DAB642AD7A2F663280AD54C19722A1E400E2ABDD76CB1080`.
- Final DDS files are `textures/dds/texture_0.dds` (`FF35B64D...E18622`), `texture_specular.dds` (`34E44845...455BA`), and `texture_normal.dds` (`FD35624E...ACF61`), each 1024×1024 and 4,194,432 bytes. Red body/blood markings remain readable in the PBR preview without changing the approved design.
- Adapter texture processing exposed a documented defect: the operation attempted to JSON-parse `job.yaml`, leaving requested dimensions null and initially producing 4K DDS. The final 1024 maps were mechanically resized with Lanczos and converted through the repository DDS converter from immutable processed bases.

## Actions and PDX reimport

All actions are 24 FPS, semantically distinct, substantive Meshy motion sourced from rig `01a03360`, and exported with zero io_pdx_mesh warnings. Blender performed only import/retarget, transform normalization, baking, and Hips-only per-frame ground correction.

| Role | Meshy task | Action id | Frames | Loop policy | Final `.anim` SHA-256 |
| --- | --- | ---: | ---: | --- | --- |
| idle | `01a033bd-5e75-723f-b607-b9d5d70e092a` | 89 | 0–41 | loop | `252C0C0D99979DC2DAFCF7F12F185479EFE276799CFC9FB92243362C67A9F39F` |
| move | `01a033bd-68a7-7c44-99f7-7d2b258241e9` | 689 | 0–43 | loop, in-place | `01DB21B0829DD7E4E38128687828795605F6FC34D2667D42C5585C8954317049` |
| attack | `01a033bd-7235-7b58-bb63-a7f23c1f0c87` | 241 | 0–110 | one-shot | `E1AC0813D172F654B6C4F03EFDC5E29E3CCDD1320D6AAB1833CEF6D795EAD16E` |
| defend | `01a033bd-7d93-7c48-8dde-d5a716ca2aa1` | 138 | 0–84 | one-shot/held by consumer | `3CE1A3E5C0B92A64B1AF82C0FC6E68EE14A02ACA3A68374649DD140095133691` |
| support_attack | `01a033bd-8737-724b-9d42-c74d202122e9` | 237 | 0–185 | one-shot | `FD0C3745C446B08BEC9B9FD315691AC3E7BCA75B4FD26E61CFBB0373BDB876CC` |
| retreat | `01a033bd-913a-7c51-a123-d236a70cd4f2` | 688 | 0–43 | loop, in-place | `0AEE8AC41890C557F8ECCD5128AED12260016E7EA52C174316421427FD855BEC` |
| training | `01a033bd-9b28-7a8d-a0f0-4243c25b501e` | 87 | 0–165 | loop | `1457F1B0C04C76BC5DCB247E2683928512CE4854A280FE69828A349895B4A199` |
| death | `01a033bd-a693-7a8f-9282-4a80d9c5824c` | 184 | 0–54 | one-shot, hold final | `55A8C6B44322DA7A2E6DC86D81495345A0054D2F45E76B21FB12F02B73B8FA67` |

Grounded reimport reports live under `validation/reimport_cannibal_feast_guard_*_grounded_reimport.json`. Sampled contact values are within approximately ±0.00002 engine units except the death transition at frame 28 (`0.001576`), with start, impact, and settle effectively at zero. Multi-view proofs under `blender/previews/reimport_*_grounded_reimport_*` retain the complete living cannibal silhouette and both oversized cleavers without tearing or explosion.

## Audio and counters

The six files under `audio/derived/` are sourced, licensed mechanical derivatives verified as mono 44.1 kHz 16-bit PCM. Full URLs, attribution, licences, source hashes, transformations, and probes are in `evidence/audio_sources/ffprobe_and_hash_receipt.json` and the archived source pages. Proposed sync: movement footfalls at move frames 1 and 22; attack swishes near frames 28 and 56 with impact near frame 84; support-attack swish near frame 94 and impact near frame 140; death vocal spans frames 14–42.

The bespoke vanilla-green counter package is documented in `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_cannibal_counter_art_handoff.md`. Required tokens are `GFX_unit_cannibal_feast_guard_icon_medium`, `GFX_unit_cannibal_feast_guard_icon_medium_white`, and `GFX_unit_cannibal_feast_guard_icon_small`; parent owns GFX registration.

## Dependency and ownership boundary

- Environment verification on 2026-08-24 returned `findings: []`; current lock declares official Meshy MCP 0.4.0, exact `meshy-7`, Blender 5.1.2, io_pdx_mesh 0.91.0, and repository adapter 1.10.0.
- Production checkpoints were created through the verified repository adapter line as it advanced during the shared run. Final export/reimport responses recorded embedded adapter metadata 1.8.2; current repository lock verification is clean, and the discrepancy is preserved rather than concealed.
- Parent must copy the named outputs to runtime, create the entity/`.asset`/GFX/sound definitions, bind actions and sounds, and perform live consumer validation. No runtime source file was edited here.

No model, action, texture, audio, or counter simplification remains. The only pending work is parent-owned runtime wiring and in-game validation.
