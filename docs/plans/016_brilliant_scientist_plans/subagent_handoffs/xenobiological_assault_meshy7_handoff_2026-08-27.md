# Xenobiological Assault Organism Meshy 7 Handoff

Date: 2026-08-27

Worker package status: **blocked**

Runtime status: **not wired; parent-owned**

Package root: `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/`

Consumer requested by the parent: `kruger_xenobiological_assault`

## Result

The source-informed Meshy 7 geometry candidate and Blender geometry/material checkpoints exist, but the skeletal package is blocked. The downloaded provider rig is not an anatomy-compatible dedicated six-limb creature rig: the inspected candidate contains a 24-bone armature, only two-frame imported clips, an extraneous icosphere that dominates the rig-review scene, 30 unresolved loose boundary edges, and no verified action task lineage. It does not prove independent chains for both ordinary arms and both elevated crab-claw appendages, and no required semantic action has provider-motion or reimport evidence. No `.mesh` or `.anim` is promoted or claimed.

## Files changed by this finishing pass

- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/xenobiological_assault_meshy7_handoff_2026-08-27.md`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/job.yaml`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/history.jsonl`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/blender/checkpoints/03_unrigged_geometry_material_candidate.blend`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/blender/checkpoints/04_unrigged_segmented_geometry.blend`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/blender/reports/creature_components.json`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/audio/source/provenance.md`
- Four immutable originals under `audio/source/originals/` and four mechanically converted WAV candidates under `audio/derived/`.
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/audio/handoff.md`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/counter/handoff.md`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/manifest.md`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/runtime/handoff.md`

The approved reference was checksum-verified and not replaced. No gameplay, entity, `.asset`, `.gfx`, sound-definition, localisation, spreadsheet, skill, or other package file was modified.

## Source and reference provenance

- Source page: `https://opengameart.org/content/insect-humanoid`
- Title: *Insect Humanoid*
- Creator: tidbit
- Publisher: OpenGameArt.org
- Stated terms: CC-BY 3.0, `https://creativecommons.org/licenses/by/3.0/`
- Retrieval date: 2026-08-27
- Source mode: `licensed_search`
- AI-use decision: adaptation permitted with attribution; the recorded page review found no NoAI or no-derivatives restriction.
- Explicit authorization: the parent task authorized source selection and a source-informed ImageGen preparation.
- Immutable non-shipping source: `refs/source/untouched.jpg`
- Source SHA-256: `2F6FBFC42CD3357A50BBDCCF8CFBF982E3373A9A460E701C4A65999E439BDD1D`
- Source-search ledger: `refs/source/source_search.md`
- Provenance record: `refs/source/provenance.json`

The selected source is modern designed creature artwork, not archival/documentary material. It passed the non-anime gate and the alternate-history xenobiological period exception. It shows no equipment or weapon.

## ImageGen preparation and one-image Meshy gate

- Only provider input: `refs/original/meshy_input.png`
- Prepared SHA-256: `2CF327815A331EEBFAABF003E51D917D758F1B7D575453EEF015B19CA03D38C7`
- Dimensions: 1143x1376
- Pose mode: `a_pose`
- Native-alpha attempts: two
- Native-alpha result: both built-in ImageGen results were opaque checkerboard composites.
- Preserved failed native-alpha derivative: `refs/derived/meshy_input_native_alpha_failed_v2.png`
- Failed derivative SHA-256: `EA2E3B31F1129B34CE284D32BE9A1B9BFA4F718D3D847F65446FABC004FF6576`
- Documented fallback: verified installed `rembg` mechanically removed the failed opaque backdrop; the resulting input has transparent corners and was checked for detached fragments.
- Input manifest: `refs/original/input_manifest.json`

Recorded prompt: “Create one substantially original but closely source-informed full-body insectoid derivative in a neutral riggable A-pose on genuine transparency; preserve the defining six-limb anatomy, tan chitin, pale skull plate, red eyes, antennae, dark claws and dorsal spines; no weapon, clothing, branding, text, scenery, base, collage, crop, floating parts, or invented machinery. Targeted revision removed one detached antenna fragment and required exactly two attached antennae.”

Recorded source-to-refinement comparison: the derivative preserves tan chitin, pale skull plate, red eyes, two attached antennae, segmented abdomen, digitigrade legs, two ordinary grasping arms, two elevated crab-claw appendages, dark extremities, and dorsal spines while neutralizing the running pose. The prior worker recorded visual approval. The immutable approved input was checksum-verified and was not replaced.

## Locked dependencies and route evidence

- Meshy MCP: official `@meshy-ai/meshy-mcp-server` 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, package integrity recorded in `.tools/3d_pipeline/config/dependencies.lock.json`.
- Meshy compatibility revision: `meshy-7-v5`; schema lock revision `meshy-7-compat-live-declaration-2026-08-21`.
- Allowed image model: exact identifier `meshy-7` only.
- Locked Meshy tools: `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate`.
- Blender: 5.1.2, build commit `ec6e62d40fa9`; executable returned Blender 5.1.2 on this pass.
- Blender HOI4 adapter: `chaosx_blender_hoi4` 1.10.14.
- io_pdx_mesh: 0.91.0; installed manifest `C:/Users/klimp/AppData/Roaming/Blender Foundation/Blender/5.1/extensions/user_default/io_pdx_mesh/blender_manifest.toml`.
- Dependency lock SHA-256: `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`.
- Meshy schema lock SHA-256: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- Adapter config SHA-256: `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`.
- The four adapter source checksums match the values pinned in the dependency lock.

## Provider lineage and credits

Downloaded provider artifacts exist, but the interrupted pass did not preserve request/response/task records or task IDs in `provider/requests`, `provider/responses`, `provider/tasks`, `provider/credits`, or `history.jsonl`. Therefore exact provider task lineage and consumed-credit reconciliation are **blocked by missing immutable provider evidence**. Filenames alone are not accepted as task provenance.

Observed artifacts:

| Stage | Local artifact | Bytes | SHA-256 |
|---|---|---:|---|
| Meshy 7 generation | `provider/downloads/generation_model.glb` | 82,833,964 | `07A726663254A395FF58EAD8FE4B8C71C099B7CFCEBC2811043205DFBB5AD779` |
| Meshy 7 generation | `provider/downloads/generation_model.fbx` | 86,617,516 | `F463CE359D5AD5B28775A42C44178DFD5CB07DE81AAA7CA0758D0BC03516F4A1` |
| 100k remesh | `provider/downloads/remesh_100k_model.glb` | 29,633,976 | `824C07DC0AFDFFF4E43C6A971279F2625BE8146EBFD89449FBB43EA28532EFA7` |
| 100k remesh | `provider/downloads/remesh_100k_model.fbx` | 24,865,548 | `EF5EEF51AE5E2949C527FF8A2A44AD6564C880C236467F5FC95B50FCC46DF2DC` |
| rig candidate | `provider/downloads/rigged_model.glb` | 13,256,428 | `3A61E871BF9A7A4E72D7C2BCFA337C7E1D454A99852D5CEF680DA23C903EFBE1` |
| rig candidate | `provider/downloads/rigged_model.fbx` | 13,192,060 | `FB83A04F155B7E927C901150347D1EB3C622CB43FE325F506C6CF211C07BE68E` |

The declared estimate is 30 credits for textured Meshy 7 generation, 5 for remesh, and 5 for rigging: 40 estimated credits for the observed stages. Consumed credits are unknown because balance-before/balance-after receipts and task responses are absent. No action-credit spend is evidenced.

The action IDs recorded in `job.yaml` (idle 0, crawl/move 112, attack 4, defend 138, leap 86, wounded 178, death 184, optional ranged/chemical 125) are proposals only. They were not promoted because no provider task ID, animation response, downloaded action artifact, or semantic preview evidence exists.

## Vanilla calibration and numeric scale crosswalk

Primary scale reference:

- Mesh: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`
- Entity: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset#infantry_rifle_entity`
- Measured source geometry height excluding collision: 7.351824797689915 HOI4 mesh units.
- Declared calibration height: 7.3518242835 HOI4 mesh units.
- Entity scale: 0.8.
- Effective reference runtime height: 5.8814594268 HOI4 units.
- Axes: forward `-Y`, up `+Z`; measured ground contact 0.00841899961233139.

Declared creature target:

- Provider target height: 2.2 m from a 1.7 m provider reference.
- Provider-to-Blender fit factor: 4.324602519705882.
- Blender target height: 9.514125543352941 HOI4 mesh units.
- Target entity scale: 0.8, applied once.
- Target effective runtime height: 7.611300434682353 HOI4 units.
- Creature/reference runtime-height ratio: 1.2941176470588236.
- Persisted accepted geometry checkpoint height: 9.51412582397461, delta 0.0000002806216681250362 from target.

Creature behavior precedent:

- Mesh: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/cavalry_horse.mesh`
- Registration: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/horse_variations.gfx#infantry_cavalry_horse_chestnut_0_mesh`
- Entity: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_cavalry.asset#infantry_cavalry_horse_entity`
- PDX mesh scale 0.45; entity scale 0.65.

`scale_crosswalk_status`: complete for the static geometry checkpoint.

## Geometry and material evidence

The interrupted rig-review operation overwrote the ordinary checkpoint names, including `05_pre_export.blend`, with the rejected rig-review scene. The clean unrigged checkpoint survived as Blender's `05_pre_export.blend1` backup and was preserved under a stable name at `blender/checkpoints/03_unrigged_geometry_material_candidate.blend`, SHA-256 `9D80A606DE36709E88E8E8D29729E416B6D8FC0AA7C846426BD5D510B869464C`.

- One working mesh object.
- 14,994 vertices.
- 30,000 triangular faces.
- Bounds: X -3.1239361763..3.1742191315, Y -1.6360695362..1.6627763510, Z 0..9.5141258240.
- No final boundary edges, non-manifold edges, degenerates, negative-scale objects, or zero-length normals in the accepted unrigged checkpoint.
- Controlled reduction: 1,999,472 to 30,000 triangles after seam welding and bounded repair.
- UV map: `UVMap`.
- Provider maps retained: base color, normal, metallic, roughness.
- Intended shader: `PdxMeshAdvanced`.
- Material processing/export remains incomplete: the report still references 2048x2048 provider maps and maps metallic directly as the provisional specular role. No final 1024px PDX packed specular DDS with the verified R unused/mask, G specular, B metallic, A roughness contract is present. This blocks material/export acceptance.

## Segmentation, rig, weights, and actions

Dedicated rig requirement: lower-abdomen root, abdomen/thorax/neck/head chain, two independent antenna chains, two digitigrade leg chains, two ordinary arm chains, and two separate elevated crab-claw arm chains.

Observed rig candidate:

- `blender/source/chaosx_xenobiological_assault_rig_review_provider_source.blend`, SHA-256 `E29FF4CE0A7A3C895A1026796C96D537F110896AE2384CBBB05C84D567E50BC4`.
- One 24-bone armature.
- Two imported two-frame clips covering frames 7-8, not substantive runtime actions.
- Extraneous `Icosphere.001` appears as a large sphere under/around the creature in all rig-review views.
- Rig-review working geometry has two mesh objects, 15,148 triangles, 30 loose boundary edges, and unresolved skipped/component-rejection evidence.
- No recorded vertex-weight audit, zero-weight audit, influence audit, deformation test, or independent-chain proof.
- The rig-review visuals show the organism perched on/embedded in the extraneous sphere and do not prove control of the full digitigrade legs or independent six-limb articulation.

`rig_route_status`: **blocked — the only downloaded provider rig candidate is not accepted as a dedicated anatomy-compatible six-limb creature rig, and the required task/action lineage is missing.**

`segment_creature_components` status: **passed for the unrigged geometry candidate.** Adapter request `89935bf12e194198ab7755f08fd551eb` wrote `blender/checkpoints/04_unrigged_segmented_geometry.blend`, SHA-256 `28E97C6165DD5A7F3C241CBF277AEB58E60F0F0AF66E4584A95C75C275F9DB8F`, and `blender/reports/creature_components.json`, SHA-256 `92ED8472B0D21CDCA5818E2633DABB5417FF7D2C37E9B2F2D6D78C14F8ED2CFA`. The report contains one component, `xenobiological_component_000`, with 30,000 polygons and 14,994 vertices; `discarded_degenerate_components` is empty, so no zero-face fragment was promoted. This segmentation result does not rescue the rejected rig or satisfy the action/export gates.

All required actions are blocked. Crawl and move cannot share action 112 unless provider evidence proves genuinely distinct locomotion; no such evidence exists. The optional ranged/chemical strike is omitted because the geometry has no discharge organ and no genuine discharge action evidence. No action proves idle loop behavior, locomotion contacts, attack strike/recovery, defend behavior, leap trajectory, wounded response, or death collapse/impact/settling.

## Export and reimport

No `.mesh` or `.anim` bytes exist under `export/`. No locked exporter log, parser receipt, reimport scene, per-action frame/FPS/root/contact evidence, or output checksum exists. Export was correctly not attempted from the rejected rig/action candidate.

`provider_export_route_status`: **blocked — valid dedicated rig and required provider actions are absent; final PDX textures and segmentation receipt are also absent.**

## Sourced audio package

Status: **needs_user_review for source suitability; exact runtime selection and action-frame synchronization remain blocked.** Full URLs, titles, creators, terms, retrieval dates, and transformation permissions are recorded in `audio/source/provenance.md`; role mapping and synchronization phases are recorded in `audio/handoff.md`.

Source pages: `https://commons.wikimedia.org/wiki/File:%E8%9D%89%E9%B8%A3.ogg`, `https://commons.wikimedia.org/wiki/File:Alligatorhiss.ogg`, `https://commons.wikimedia.org/wiki/File:Dull_thud.ogg`, and `https://commons.wikimedia.org/wiki/File:Knuckle_crack.ogg`. Each corresponding direct download is the Wikimedia `Special:Redirect/file/` URL recorded in the provenance ledger.

| Candidate | License | Immutable original SHA-256 | Derived WAV SHA-256 | Role coverage |
|---|---|---|---|---|
| Wikimedia `蝉鸣.ogg`, Ngguls | CC0 | `1DAD0233D8EF729A489386857C938FABD7645F5FFC0E33E58CCA7D940B1FF73F` | `1168B85A7B53A3E65A5728EC04720A5C4A5DE97B61439661B29B6F2AAB209667` | idle/ambient |
| USFWS alligator hiss | public domain | `B019246ADE92F25EA00C2185E1B5F2E023770513691BA9EF71E47E6B3D0CA4B1` | `A7E360921FE93C16CE06C0EDCD1F11DB78B180E6D13D341E3B040F3B863DA4AA` | selection, attack warning, defend, wounded |
| gregoryweir/PDSounds dull thud | public domain | `5B91906D41BD57F1F6551E446D30FBFF06EC59A39D22725140293EF4AEC6CDB3` | `6D83805C2FFE8F427FF14DBC770BA227A518151A9C331A4B8208DC193D4B4903` | movement contact, attack contact, leap landing, death impact |
| pwausc1 knuckle crack | CC0 | `4E0C06C862F795AA5307D5B5E00E14901D1F6BB1B67DD3F8134DD30D852579E7` | `12342CCC0361A09547026C70C78616F19F6DE698F52B69AE0AB3DB22439D31FC` | joint/claw articulation, leap preparation |

All four derivatives are metadata-free PCM S16LE, 44.1 kHz, mono WAVs verified with ffprobe. No audio was generated, synthesized, recorded, or manually authored. Chemical/ranged discharge remains omitted because no discharge anatomy or genuine provider action exists. The installed infantry voice templates route selection/idle by tag/original tag rather than subunit sprite, so a per-subunit selection binding is not defensible until the parent proves an isolated consumer.

## Bespoke vanilla-green counters

Current consumer: `common/units/016_brilliant_scientist_project_forces.txt#kruger_xenobiological_assault`, currently `sprite = infantry` and `map_icon_category = armored`.

Required parent-facing sprites and textures:

- `GFX_unit_xenobiological_assault_icon_medium` -> `gfx/interface/counters/divisions_large/unit_xenobiological_assault_icon.dds`.
- `GFX_unit_xenobiological_assault_icon_medium_white` -> `gfx/interface/counters/divisions_small/onmap_unit_xenobiological_assault_icon.dds`.

Exact installed consumer inspection is complete. `interface/subuniticons.gfx` defines both infantry and cavalry families as two-frame strips. The inspected large DDS files are 152x42 with two 76x42 cells; the inspected map DDS files are 60x12 with two 30x12 cells. The closest creature precedent is cavalry: large SHA-256 `F17C1865E48D3AC542F34751FD151BAF0C5700DA661E6C800008020A33B87306`, map SHA-256 `249C498E73DC22DEE532C7648EDFF1A1347DD72AB2314AE31ED973CD370524B1`. The current infantry references are large SHA-256 `B33A8E3B69CC789EB0E31BA99F4E5BA4E5B0A8B51EC1A7A7F709C3516F720C23` and map SHA-256 `58AB78662C2A64A519B8D5D144582E7B2785915BD0A0A822696D87A9DE6F766C`.

The matching skill-local families and contact sheets were inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `map_counters/`. Sampled installed large-counter greens range from dark anchors such as `(68,99,68)` and `(73,106,73)` through highlights such as `(125,149,125)` and `(129,152,129)`; exact shading and alpha requirements are in `counter/handoff.md`.

Counter status: **blocked only on original `chaosx_icon_artist` production and parent review/wiring.** No copied, recolored, renamed, placeholder, or arbitrary-green counter was made.

## Proposed runtime identifiers

- Entity: `chaosx_xenobiological_assault_entity`
- Mesh: `chaosx_xenobiological_assault_mesh`
- Idle: `chaosx_xenobiological_assault_idle`
- Crawl: `chaosx_xenobiological_assault_crawl`
- Move: `chaosx_xenobiological_assault_move`
- Attack: `chaosx_xenobiological_assault_attack`
- Defend: `chaosx_xenobiological_assault_defend`
- Leap: `chaosx_xenobiological_assault_leap`
- Wounded: `chaosx_xenobiological_assault_wounded`
- Death: `chaosx_xenobiological_assault_death`
- Optional ranged strike: `chaosx_xenobiological_assault_ranged_strike`, currently omitted/blocked.

These are proposals only. No runtime copies were synchronized. Selected-source-to-runtime hashes and final synchronization result are `not_applicable`: the source selection is known, but there is no accepted export and the parent owns runtime synchronization.

## Meaningful validation performed

- Recomputed immutable source, prepared-reference, provider-download, Blender-checkpoint, dependency-lock, schema-lock, adapter-config, and adapter-source SHA-256 values.
- Confirmed Blender 5.1.2 and io_pdx_mesh 0.91.0 from the installed executable/manifest.
- Confirmed the locked Meshy route exposes all eight required tool names and exact `meshy-7`; the unapproved `latest` alias was not used. Live balance was 140 and no paid operation was initiated on this finishing pass.
- Confirmed the Blender bridge on `127.0.0.1:9876`; adapter health request `a303eb5381c949e483660cb93295e8b` reported Blender 5.1.2 and io_pdx_mesh 0.91.0.
- Reviewed the unrigged and rig-review geometry from front and three-quarter views and inspected the full multi-view report set paths.
- Compared the static geometry report against the numeric infantry scale crosswalk.
- Inspected the rig report for bone count, frame ranges, topology defects, component count, and normalization.
- Segmented the clean unrigged checkpoint through the locked adapter and verified one positive-face component with no discarded degenerate/zero-face fragments.
- Verified all four derived audio files as PCM S16LE, 44.1 kHz, mono and recorded immutable source/derived checksums.
- Inspected the exact installed infantry/cavalry large and map counter DDS files, frame contracts, alpha, sampled green palette, and skill-local contact sheets.
- Confirmed there are no `.mesh`, `.anim`, final counter DDS, or provider task-receipt files hidden elsewhere in the package tree.

## Skipped validation and why

- Live Meshy task inspection and action generation: exact prior rig task ID is absent, so `meshy_animate` cannot be called without guessing lineage or paying for an ungrounded replacement route.
- Export/reimport: blocked by rejected rig, missing actions, incomplete PDX textures, and missing segmentation receipt.
- Animation semantic/contact/deformation QA: no provider action artifacts exist.
- Audio synchronization: no accepted action timing exists; the licensed source research and phase mapping are complete, but exact frame numbers and selection binding are not.
- Counter visual approval: no counter package exists.
- In-game validation: parent/user-owned and explicitly out of scope.

## Remaining parent work and exact blockers

1. Decide whether to authorize a fresh Meshy rig recovery from the known accepted Meshy geometry when the original generation/remesh task IDs cannot be recovered. This is not a silent retry: the current package lacks the immutable provider lineage needed to bind the operation safely.
2. If a new dedicated creature rig succeeds, preserve its exact task ID and download, verify the written six-limb rig map, segment components with positive face counts, audit weights/deformation, and request separate substantive provider actions for every role.
3. Complete final 1024px PDX diffuse/normal/packed-specular DDS textures from immutable provider maps.
4. Only after rig/action acceptance, export and reimport actual `.mesh` and `.anim` bytes through locked io_pdx_mesh and capture parser evidence.
5. Review the licensed audio candidates, prove an isolated selection consumer if selection is required, and bind exact action frames only after accepted actions exist.
6. Route the fully specified bespoke vanilla-green package in `counter/handoff.md` to `chaosx_icon_artist`.
7. Parent wires entity, `.asset`, `.gfx`, sounds, counters, live consumer, and runtime copies, then the user performs in-game validation.

No fallback or simplification was promoted. The package is **blocked**, not fallback-complete.

## Recovery audit addendum — 2026-08-27

This addendum records the bounded existing-mesh recovery audit requested after the finishing pass above. No ImageGen, image-to-3D, new base model, local skeleton authoring, local weighting, local action authoring, transform-only motion, semantic action alias, gameplay wiring, entity wiring, GFX wiring, or sound-definition wiring was performed.

### Files created or refreshed by this recovery audit

- Refreshed dependency evidence: `.tools/3d_pipeline/reports/environment_report.json`, 20,372 bytes, SHA-256 `8AB8A91BED9AD3AAC98170CA684278D70CAB6F5E87C28164244BBE6EE5E94724` at the time of this audit. This shared generated report is not a runtime asset.
- Blender adapter health request: `logs/adapter/1c923a29cfdf4b44ba0d953714814013.json`, SHA-256 `802F622FE3AD1FF156DE0C2D07EC29F389AD9B865533757E20E5A1ABAAB21EC1`; result `logs/adapter/1c923a29cfdf4b44ba0d953714814013.result.json`, SHA-256 `BC1D091E20047ED1ECC5E37BC7407E0806F5ADFE54E41B4672FA7D552E0FE072`.
- Accepted static-checkpoint inspection request: `logs/adapter/5d00ac5f6d4c4d69aab56562d5f393fc.json`, SHA-256 `C6BB21C9CBD850E9DDFCC209899A805C75023B65829B5C724022AF64EFE6D318`; result `logs/adapter/5d00ac5f6d4c4d69aab56562d5f393fc.result.json`, SHA-256 `E1C081BA7AAF3130FFFC1AEF1FD2D20D614C3393BF1F6A512D63DFAEB7756489`.
- Rejected-rig inspection request: `logs/adapter/d586a0cddf00485cbb13973237751e17.json`, SHA-256 `DC0F843E6799FC63702B4A22700DE47C6BD12FBD9783E2FBDD7B22749AED1A47`; result `logs/adapter/d586a0cddf00485cbb13973237751e17.result.json`, SHA-256 `F7DE371B0AF946262DD471AE1FD2C0BC2FDCC65634AF7C9759BE7B13F1DFF47E`.
- This dated handoff was updated. No existing model, texture, audio, counter, checkpoint, provider download, job, manifest, runtime handoff, gameplay file, or runtime file was changed.

### Current dependency and route evidence

- `MESHY_API_KEY` hard gate passed without exposing or persisting the secret.
- Repository verifier `python -B .tools/3d_pipeline/verify_environment.py --probe-meshy` returned zero findings at `2026-08-27T13:07:26Z`.
- Current live Meshy balance: **13 credits**. The parent explicitly directed that no paid call be made, and none was made.
- Official Meshy route: `@meshy-ai/meshy-mcp-server` 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, compatibility revision `meshy-7-v5`, schema revision `meshy-7-compat-live-declaration-2026-08-21`.
- The verified exact image model remains `meshy-7`. No alias was used.
- Locked production tools remain `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate`.
- Live `meshy_rig` accepts only `input_task_id` or `model_url` as the source selector. The package preserves neither a provider task ID nor an official provider model URL for the accepted geometry. A local GLB/FBX path is not an accepted rig input.
- Live `meshy_animate` requires an accepted `rig_task_id` and integer `action_id`. The package has no accepted rig task ID.
- Blender bridge `127.0.0.1:9876` was listening independently of process-presence checks.
- Blender adapter health verified Blender 5.1.2, adapter `chaosx_blender_hoi4` 1.10.14, io_pdx_mesh 0.91.0, and both locked export functions.
- Dependency lock SHA-256: `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`; Meshy schema lock SHA-256: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`; adapter config SHA-256: `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`.

### Exact rig incompatibility evidence

The accepted static checkpoint remains a clean, visually verified six-limb organism: two digitigrade legs, two ordinary grasping arms, and two elevated crab-claw appendages, plus two antennae. The fresh adapter inspection of `blender/checkpoints/03_unrigged_geometry_material_candidate.blend` reconfirmed one 30,000-triangle working mesh, 14,994 vertices, no boundary/non-manifold/degenerate geometry, no armature, and no actions.

The fresh adapter inspection of `blender/source/chaosx_xenobiological_assault_rig_review_provider_source.blend` reconfirmed a standard 24-bone humanoid armature. Its bone list contains hips, a bilateral leg set, one bilateral arm set, spine, neck, head, and head-front/end bones. It contains no independent bones for either antenna and no second bilateral arm chain for the elevated crab-claw appendages. Therefore it cannot preserve or articulate the required six-limb anatomy.

The rig candidate also retains an unparented `Icosphere` and a copied `Icosphere.001`; the visible working sphere has 42 zero-weight vertices. The provider character mesh itself reports normalized one-to-four-bone influences and no zero-weight vertices, but those numerical weight facts do not rescue the anatomically incomplete bone map. Its two recorded actions cover only frames 7 and 8 at 24 FPS, both with identical evaluated bounds. They provide no substantive motion and cannot satisfy any semantic role.

This is a provider-rig failure, not authorization for local recovery. The parent explicitly forbade manual skeleton authoring, weighting, and animation, and the package remains fail-closed.

### Required action disposition

| Requested role | Provider evidence | Disposition |
|---|---|---|
| idle | proposed library ID 0 only; no accepted rig task/action artifact | `blocked` |
| crawl/walk | proposed ID 112 only; the locked schema does not verify 112 and no action artifact exists | `blocked` |
| attack | proposed library ID 4 only; no accepted rig task/action artifact or strike/recovery evidence | `blocked` |
| defend | proposed ID 138 only; unverified by the lock and no action artifact exists | `blocked` |
| support attack/leap | leap proposal 86 only; unverified by the lock and no crouch/launch/airborne/landing evidence exists | `blocked` |
| retreat | absent from the existing job and provider evidence | `blocked` |
| wounded | proposed ID 178 only; unverified by the lock and no recoil/withdrawal evidence exists | `blocked` |
| articulated death | proposed ID 184 only; unverified by the lock and no collapse/impact/settling evidence exists | `blocked` |
| ranged/chemical attack | existing anatomy shows no verified discharge organ, locator, or provider discharge action | `not_applicable`; omitted rather than invented |

The job currently proposes one ID, 112, for both crawl and move. Even if that ID were later verified, one action may not be semantically aliased to both roles without distinct provider evidence. The current schema lock verifies only library IDs 0 (`idle`), 4 (`attack`), and 8 (`death`); all other numeric proposals remain unverified suggestions.

At the current 13-credit balance, even a technically valid rig source would not cover the complete requested tranche: rigging is estimated at 5 credits and each required custom action at 3 credits, while the full non-aliased set exceeds the remaining balance. This budget fact is secondary to the harder missing-input and anatomy-capability blockers, and no paid attempt was made.

### Audio verification

The four immutable originals and four mechanical derivatives were rehashed and match `audio/source/provenance.md` and `audio/handoff.md`. Fresh `ffprobe` receipts reconfirm every derived WAV as `pcm_s16le`, 44.1 kHz, mono, 16-bit: ambient 33.097143 s, contact thud 0.391837 s, hiss 11.328005 s, and joint crack 6.793288 s. The source pages, direct-download URLs, creators, CC0/public-domain terms, allowed transformations, original hashes, and derived hashes remain recorded.

Audio remains `needs_user_review` for source suitability and `blocked` for exact synchronization. There is no accepted provider action from which to derive foot-contact, strike, landing, wounded, or death-impact frames. Per-subunit selection is also blocked because the verified infantry voice consumer is tag/original-tag scoped, not isolated to `kruger_xenobiological_assault`.

### Counter verification

The exact installed definitions in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx` were rechecked. Cavalry and infantry large/map sprites each declare `noOfFrames = 2`. Fresh DDS-header inspection reconfirmed the cavalry and infantry large files as valid `DDS ` files with 124-byte DDS headers and 152x42 canvases, and the map files as 60x12 canvases. Their SHA-256 values match `counter/handoff.md`.

The current consumer still declares `sprite = infantry` and `map_icon_category = armored`. The matching skill-local large and map contact sheets were visually reviewed. No bespoke `chaosx_icon_artist` source PNG, processed PNG, DDS round-trip, contact sheet, or parent review exists, so both required xenobiological counter surfaces remain `blocked`. No vanilla counter, recolor, renamed file, primitive drawing, or arbitrary-green substitute was created.

### Export, synchronization, and completion state

No `.mesh` or `.anim` export was attempted because there is no accepted anatomy-compatible rig or verified provider action. No action can be retargeted, cleaned, grounded, baked, exported, or reimported without violating the provider-motion gate. Final PDX diffuse/normal/packed-specular DDS files also remain absent. No runtime source was synchronized, so source-to-runtime hashes and synchronization status remain `not_applicable`.

Final recovery status: **blocked**. Every required skeletal role is explicitly blocked except ranged/chemical attack, which is not applicable to the observed anatomy and was correctly omitted. Sourced audio evidence exists but cannot be frame-synchronized, and bespoke vanilla-green counters remain absent. No fallback or simplification was used.
