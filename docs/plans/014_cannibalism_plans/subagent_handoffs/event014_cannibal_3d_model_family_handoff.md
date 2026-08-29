# Event 014 cannibal 3D model family handoff

> **Historical provider tranche.** The generated and archival source lineage in this file is superseded by the current artwork-source gate in `014_cannibal_model_source_direction_2026-08-22.md`. Retain this handoff for rejected geometry and failure evidence only; its old counter, audio, adapter, and completion wording is not current status. The nine-family counter package is documented separately, and current model/audio status is tracked by the per-family handoffs.

Status: **incomplete and blocked before export**. Eight distinct Meshy 7 source candidates and rigged provider candidates exist, but none is approved for final runtime wiring. No `.mesh` or `.anim` file is claimed complete.

## Completed production

- Confirmed a nonblank process `MESHY_API_KEY` before repository or job intake.
- Verified the repaired repository-owned Meshy MCP route, Meshy 7 schema, Blender 5.1.2, adapter 1.5.0, and checksum-locked io_pdx_mesh 0.91.0 before provider work.
- Created all eight deterministic job roots and one approved 1024x1536 ImageGen reference per slug. Seven references retained native alpha. Bone Guard required two failed native-alpha edits followed by the accepted installed-rembg fallback; its rejected fantasy-adjacent original and opaque correction attempts are preserved under `refs/derived/`.
- Submitted exactly one image to each Meshy 7 generation task with PBR texturing, triangle topology, a 30,000-triangle target, T-pose, bottom origin, GLB+FBX outputs, and saved pre-remesh evidence.
- All eight generation tasks succeeded at 30 credits each. All eight rig tasks succeeded at 5 credits each. Because the Meshy MCP rig-download response exposed URLs but did not write `save_to`, each rig task used one verified 1-credit Meshy conversion and the converted rigged FBX was downloaded locally.
- Provider balance evidence: generation tranche 596 -> 356 (240 credits). The account was replenished externally before rigging; rig tranche began at 1000 and consumed 40 credits, conversion tranche consumed 8 credits, ending at 952.
- Imported the installed vanilla infantry mesh read-only from a checksum-identical staged copy in each job. `polySurface106` measured against source height 7.351824797689915, forward -Y, up +Z; the adapter applied entity scale 0.8 exactly once for effective runtime height 5.881459838151932.
- Normalized and grounded every geometry candidate, triangulated it, reduced it to no more than 30,000 triangles, bound explicit diffuse/roughness-preview/normal sources, and derived PDX packed maps with R=0, G=specular level, B=metallic, A=roughness and the packed normal convention. Provider maps remain immutable.
- Preserved Blender source/checkpoints, seven-view previews, adapter request logs, material pack reports, GLB/FBX downloads, rigged FBX downloads, checksums, per-job manifests, and per-job runtime handoffs.
- Wrote the three-surface counter brief at `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_cannibal_counter_art_handoff.md`.

## Exact lineage

| Slug | Meshy 7 generation | Meshy rig | Meshy conversion | Geometry QA |
| --- | --- | --- | --- | --- |
| `cannibal_scavenger_warband` | `01a02942-5d92-730c-96c9-bdbd51194575` | `01a0295b-9c38-7aa0-9cb5-bb1fa4bb0ec6` | `01a0295e-2bed-7a71-983f-8b3ac3219cdd` | Rejected: spear floats across waist without hand contact. |
| `cannibal_feast_guard` | `01a02942-49ca-743e-986b-c4cde2204341` | `01a0295b-b8cb-729b-9273-785978ecbf5a` | `01a0295e-2ec2-7a74-b04f-1a394b27bf21` | Provisional only: cleaver/shield placement is plausible, but the single welded mesh prevents audited rigid weapon binding. |
| `cannibal_feast_cohort` | `01a02942-6f38-730e-a6f4-7cff846fd25b` | `01a0295b-d54f-79b9-8ae5-4bc3d2d94567` | `01a0295e-311e-7a75-8a1a-071aaead67e1` | Rejected: forked polearm omitted. |
| `cannibal_bone_guard` | `01a02942-75a0-730f-9206-12250094a62f` | `01a0295b-f18f-79bc-9b10-e35324146164` | `01a0295e-3396-7a76-91be-4f27e2f76db2` | Rejected: heavy poleaxe omitted. |
| `cannibal_island_reavers` | `01a02942-7a8f-7314-b7b9-c21f375eab99` | `01a0295c-0eb8-72a8-959c-529e802a88c9` | `01a0295e-36ee-7b58-8c9b-a7b481f5dfa8` | Rejected: harpoon lies on ground. |
| `cannibal_siege_eaters` | `01a02942-8444-72c9-bf93-33f27b94ce1f` | `01a0295c-2e04-7ad8-8362-31270674fa6d` | `01a0295e-4554-7b5a-9632-41d024181407` | Rejected: sledgehammer omitted and entrenching tool is stowed. |
| `cannibal_march_predation_column` | `01a02942-8c1f-7316-bdd3-e35952e1790b` | `01a0295c-4c62-79ec-9b20-fafb3cd8a6f5` | `01a0295e-48d8-7a7e-b622-998f902ca67d` | Rejected: bow stays stowed and cannot execute draw/release. |
| `cannibal_network_cadre` | `01a02942-92b8-7324-b0ee-9006dab0f956` | `01a0295c-6b81-72c2-96bf-b4fc777dcabe` | `01a0295e-4c21-7a44-a4ff-cb5cdd7d2c70` | Rejected: bow is fused across shoulder/arm. |

## Fail-closed blockers

1. Required weapon identity and hand contact fail for seven jobs; Feast Guard remains provisional because its weapon and shield are welded into the body mesh. The locked callable adapter cannot isolate a weapon component from a single welded humanoid mesh. Exporting these candidates would create deforming/floating equipment and invalid weapon-specific attacks.
2. The locked `author_humanoid_actions` operation exposes idle, move, attack, defend, support_attack, retreat, and death only on its armed route. It does not author the mandatory real training action. A renamed locomotion action, static action, or transform-only stand-in is forbidden.
3. Provider rigging succeeded, but provider animations available through the verified schema are only idle 0, attack 4, death 8 plus bundled walk/run. They do not satisfy the complete distinct eight-action contract or the weapon-specific attack briefs.
4. Candidate topology reports retain nonzero boundary components/loose boundary edges after bounded repair. They therefore are evidence candidates, not final approved geometry.
5. Mandatory legally sourced audio was not completed. No generated, synthetic, placeholder, recorded, or unlicensed audio was substituted. The installed root paths named `sound/units_sfx.asset` and `sound/vo.asset` are absent in this installation; relevant infantry entity move events were inspected in `gfx/entities/units_infantry.asset`. Selection/acknowledgement remains country/original-tag-level through CBA-CBH and CBL `<TAG>_infantry_idle` templates, not a per-subunit consumer. Required roles still missing for every family: selection/acknowledgement, movement/footfalls, idle/vocal loop where appropriate, weapon attack, weapon impact, and death.
6. Bespoke counter art is not present. Exact large, on-map, and text-icon requirements are in the counter handoff and remain owned by `chaosx_icon_artist`.
7. No runtime `.gfx`, `.asset`, entity, sound definition, localisation, gameplay, or final runtime copies were edited. No in-game completion is claimed.
8. During final validation, a concurrent pipeline repair changed the adapter source/config to 1.6.0 and added weapon-review/isolation operations, while the active dependency lock and registered MCP surface still described 1.5.0. `verify_environment.py` therefore failed closed on the version, operation set, and source/config checksums. No unregistered 1.6 operation was invoked and no further Blender mutation/export occurred after that mismatch appeared.

## Parent consumer contract

For every slug: `common/units/014_cannibalism_irregular_infantry.txt#<slug> -> <slug>_entity`.

Parent-owned runtime roots remain:

- `gfx/models/units/014_cannibalism/<slug>/`
- `gfx/entities/014_cannibalism_units.gfx`
- `gfx/entities/014_cannibalism_units.asset`

Do not synchronize these candidates into runtime until replacement geometry passes equipment contact, the locked route can author and export all eight real actions at 24 fps, sourced audio exists, counter art exists, io_pdx_mesh export/reimport passes, and the parent completes live consumer validation.
