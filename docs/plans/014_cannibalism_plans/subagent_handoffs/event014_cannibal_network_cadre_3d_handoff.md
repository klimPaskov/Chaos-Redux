# Event 014 Cannibal Network Cadre 3D handoff

Historical supersession notice: this custom-model handoff is retained for provider, adapter, export, and provenance evidence only. The 2026-08-26 approved visual-reuse decision assigns Network Cadre vanilla `sprite = infantry`, removes the custom model/action/provider requirement, and makes the former animation blocker non-current.

Historical status: **incomplete because all eight provider-sourced animations remained blocked by the serialized Meshy lease**. The mesh, material package, skeleton preparation, locked mesh export/reimport proof, sourced audio candidates, and counter audit were historical evidence, not a current runtime package.

The generated source lineage described below is superseded by the parent’s final artwork gate. The old input, geometry, and descendants remain rejection evidence only; current work requires actual sourced or user-supplied artwork followed by faithful enhancement without redesign.

## Completed artifacts

- Superseded generated exact-one reference: `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/refs/original/meshy_input.png`, SHA-256 `5EAF7F2E58BF7941923D64A9CF1BBC93387F1873EBCCE19E861CF5DEA43585BA`.
- Accepted Meshy 7 task: `01a02992-4c18-781f-b15e-1fec680e83bd`.
- Accepted GLB: `provider/downloads/recovery_weapon_preserved_model.glb`, SHA-256 `4C52FA4B70F9B2287A2C7CE2D61F792CA6B8AC8727B56568461ACAEDF01D8837`.
- Clean zero-action rig/material checkpoint: `blender/checkpoints/03a_rig_dds.blend`.
- Final mesh: `exports/cannibal_network_cadre.mesh`, SHA-256 `4C09483BD52B6383E1B1ECF2A2507A61798A2983A78782E740C90059FA99DAB6`, 4,630,893 bytes.
- Runtime DDS maps: `exports/cannibal_network_cadre_diffuse.dds`, `exports/cannibal_network_cadre_normal.dds`, and `exports/cannibal_network_cadre_specular.dds`.
- Textured reimport proof: `blender/checkpoints/reimport_cannibal_network_cadre_mesh_textured_reimport.blend`; request `5887aa01328a406095560cd78907245b`.
- Six sourced PCM WAV candidates under `audio/derived/`, with complete provenance in `evidence/audio_sources/source_manifest.json`.
- Job/manifest/history: `job.yaml`, `manifest.json`, `manifest.md`, and `history.jsonl`.
- Runtime crosswalk: `runtime/handoff.md`.

## Geometry, calibration, materials, and rig

The accepted silhouette is a gaunt crouched courier with a skull hood, bone strips, coded scraps, light webbing, a short plain bow, and a narrow knife. Review previews show invented culture-neutral paint and no identifiable Indigenous borrowing.

The working mesh is 29,999 triangles and 14,814 position-welded vertices, with no negative scale, degenerates, non-manifold edges, or zero-length normals. The exporter emits one stream with 53,352 split UV/normal vertices, below the 65,535 limit, and no warnings.

Installed vanilla calibration uses `western_european_infantry.mesh` object `polySurface106`, source height 7.351824797689915, forward `-Y`, up `+Z`, and `infantry_rifle_entity` scale 0.8 exactly once. Effective runtime height is 5.881459838151932.

The three 1024-square DDS hashes are:

- Diffuse: `69156065A713141E30A00C0CB2987368DE221D90BEF7079D3786F9EDB8D4C454`.
- Normal: `7248B82951475D110EC0D612254FDBC55A2113AF7934DF7E8BDE054673D22D2A`.
- Specular: `86B2D036D99C70D36E29A3E1F7B70134A89794F8FB8DF72D20AE185F443F552B`.

The accepted crouched geometry failed Meshy rigging with HTTP 422 `Pose estimation failed, please provide a valid model`; no task ID was returned. After this documented failure gate, the locked adapter prepared a 24-bone local HOI4 skeleton with no zero-weight deforming vertices and at most three normalized influences. It is skeleton preparation only.

## Provider lineage and credits

| Stage | Task ID | Result | Confirmed credits |
| --- | --- | --- | ---: |
| Initial Meshy 7 generation | `01a02942-92b8-7324-b0ee-9006dab0f956` | Rejected geometry | 30 |
| Rig of rejected geometry | `01a0295c-6b81-72c2-96bf-b4fc777dcabe` | Succeeded; source rig only | 5 |
| Conversion of rejected geometry | `01a0295e-4c21-7a44-a4ff-cb5cdd7d2c70` | Succeeded; source only | 1 |
| Replacement T-pose generation | `01a02986-c676-7575-a975-14d8eb51081b` | Rejected prop stripping | 30 |
| Weapon-preserving recovery generation | `01a02992-4c18-781f-b15e-1fec680e83bd` | Accepted | 30 |
| Rig of accepted recovery | no task ID | HTTP 422 pose failure | Unknown |

Confirmed consumed credits are 96. The failed accepted-geometry rig cost cannot be isolated because no task ID was returned and the account had concurrent activity. Eight distinct pending custom animations are estimated at 24 credits.

## Dependencies and Blender evidence

The environment verifier returned no findings. The repository-owned client health request `da8c528699434fb88ec6639b184f8f5d` reports adapter `chaosx_blender_hoi4` 1.8.1, Blender 5.1.2 build `ec6e62d40fa9`, and loaded io_pdx_mesh 0.91.0. Meshy is official `@meshy-ai/meshy-mcp-server` 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, with locked exact model identifier `meshy-7`.

Lock and schema hashes, io_pdx_mesh archive hash, wrapper route, and request evidence are in `evidence/dependency_lock_evidence.json`. Mesh export request is `8d5c8972173c486f8e263a49198e8df5`; textured reimport request is `5887aa01328a406095560cd78907245b`.

## Audio and counter handoffs

The sourced audio package covers selection, movement, idle, bow attack, impact, and death. All derived files are 44,100 Hz mono PCM s16le. Sources include CC0 OpenGameArt material, CC-BY 3.0 `Archers shooting` by copyc4t, and the public-domain `Male pain grunts` recording by stilgar. Exact pages, direct downloads, attributions, licences, original and derived hashes, transformations, and pending action synchronization phases are in `evidence/audio_sources/source_manifest.json`.

The bespoke Network Cadre counter package is complete outside this worker's write scope and already registered through `interface/chaosx_subuniticons.gfx` and `interface/chaosx_texticons.gfx`. It contains the two-frame large, on-map, and texticon DDS consumers. Exact paths, hashes, dimensions, vanilla precedents, palette treatment, reference families, and validation evidence are in `runtime/handoff.md`.

## Blockers and remaining parent work

- The parent reserved the Meshy provider route for another Event 014 worker. This worker obeyed the pause and made no balance, status, polling, download, or animation calls during that lease.
- Idle, move, crouched short-bow attack with quick withdrawal, defend, support attack, retreat, training, and death do not yet have genuine provider-sourced final motion.
- Existing locally authored actions are explicitly rejected and must never be exported or semantically aliased.
- No final `.anim`, action preview set, action hash, or animation reimport proof exists.
- Exact audio frame synchronization remains intentionally unset until the real action phases can be inspected.
- Parent must wire the entity, animation, material, and sound definitions and perform final live consumer validation. In-game completion is not claimed.

No unapproved simplification or fallback was used.
