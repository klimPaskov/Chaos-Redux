# Paleogenetic Creature Meshy 7 handoff

## Status

`blocked`

The reusable geometry candidate and evidence package are preserved, but the animated runtime model is blocked. The live locked Meshy route exposes only the generic `meshy_rig` pose-estimation endpoint and `meshy_animate` against a completed rig task. It exposes no dedicated multi-limbed creature-rig operation or rig-map arguments. One initial rig submission failed with HTTP 422 pose estimation. The materially different recovery task `01a04285-34b0-7d0f-b256-e2c3f0048d67` succeeded technically but produced a standard 24-bone humanoid, an approximately 1.91-million-triangle two-object result with a large sphere, no usable material binding, 637 non-manifold edges, and only two-frame imported clips. It does not expose the creature's four independent arm chains or both cranial masses and is rejected. No further paid call would be a non-duplicative compatible creature-rig recovery through the currently exposed provider schema.

The rejected humanoid rig was not used for actions or export. No local Blender rig, locally authored motion, procedural motion, transform-only motion, static alias, or semantic action reuse was substituted. No `.mesh` or `.anim` output is claimed.

## Owned scope and parent boundary

- Package root: `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature`
- Parent consumer: `kruger_paleogenetic_beast`
- Proposed entity: `chaosx_paleogenetic_creature_entity`
- Proposed mesh: `chaosx_paleogenetic_creature_mesh`
- Parent owns `.asset`, entity, `.gfx`, sound definitions, gameplay/runtime copies, live-consumer validation, and in-game validation.
- No gameplay, entity, `.asset`, `.gfx`, sound-definition, localisation, spreadsheet, or unrelated package file was edited.

## Source and one-image reference lineage

- Source page: https://opengameart.org/content/mutant-cook
- Direct source URL: https://opengameart.org/sites/default/files/mutant_creature_cook_concept_art.png
- Title: **Mutant Cook**
- Creator: Gman2099
- Publisher: OpenGameArt.org
- Stated terms: CC0, https://creativecommons.org/publicdomain/zero/1.0/
- Retrieval date: 2026-08-27
- Source mode: `licensed_search`
- Archived source status: non-shipping evidence only
- Immutable source: `refs/source/untouched.png`
- Source SHA-256: `2B1F9A01475217BF6925065703FB682822049B8D92F78AC0CD51FA48CDBD0176`
- Authorization: explicit parent task authorization dated 2026-08-27
- Provenance/AI-use decision: accepted because the selected modern game-creature concept is explicitly CC0 and states no incompatible NoAI or no-derivatives restriction.
- Final and only provider input: `refs/original/meshy_input.png`
- Prepared SHA-256: `29091392E7C875AF138DDEA1BE3C7B5A69BF786FB1E2C15609050BC5EDA2DCD5`
- Dimensions/mode: 1178 x 1335 RGBA
- Pose preparation: `creature_a_pose`
- Parent approval: explicit parent task authorization dated 2026-08-27

ImageGen prompt:

> Create one substantially original, model-ready full-body refinement preserving the selected source's asymmetric swollen reddish-brown torso, small screaming primary face, large secondary eye and cranial mass, four long clawed arms, two digitigrade legs, ragged lower wrap, palette and organic identity; isolate one centered subject in a neutral creature A-pose with all limbs unobscured on genuinely transparent canvas; no new components, weapons, machinery, branding, text, scenery, anime styling, shadows, matte or halo.

Source-to-refinement comparison: the derivative retained the two cranial masses, upper-left screaming face, upper-right eye, reddish wet flesh, four tapering arms, two legs, and ragged dark wrap. It clarified limb separation, complete hands/feet, neutral stance, full-body framing, and material readability without equipment or branding.

Transparency evidence: two native-alpha ImageGen attempts encoded an opaque checkerboard. The retained RGBA input used a documented `rembg` fallback. Validation recorded four transparent corner samples, center alpha 254, the complete visible creature, and no retained scenery or cast shadow. The rejected eroded result remains in `refs/derived/rembg_eroded_rejected.png`.

## Dependency and route evidence

- Official provider package: `@meshy-ai/meshy-mcp-server` `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, package integrity locked in `.tools/3d_pipeline/config/dependencies.lock.json`
- Dependency-lock SHA-256: `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`
- Meshy tool-schema-lock SHA-256: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`
- MCP SDK: `@modelcontextprotocol/sdk` `1.29.0`, git head `e12cbd7078db388152f6e839abdbe09ba01f3f32`
- Wrapper: `.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd` through compatibility revision `meshy-7-v5`
- Schema lock: `meshy-7-compat-live-declaration-2026-08-21`
- Verified generation model: exact identifier `meshy-7`; no alias or downgrade
- Live provider tools observed: `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate`
- `meshy_rig` accepts only `input_task_id` or `model_url`, plus optional `height_meters` and `texture_image_url`; it exposes no creature rig family, rig map, extra-limb, or joint-layout input.
- `meshy_animate` requires a completed `rig_task_id` and integer `action_id`; therefore it cannot repair an anatomically rejected rig.
- Live balance observed after dependency/schema review: 140 credits. No additional paid recovery was attempted.
- Blender: 5.1.2 build `ec6e62d40fa9`
- Blender bridge: `127.0.0.1:9876`, explicitly started hidden and re-probed listening; owning process recorded during this run.
- Repository adapter: `chaosx_blender_hoi4` version `1.10.14`; every locked adapter-source checksum matched. Health request id: `c1b9d6461576435abee712d45b82ec79`.
- Adapter config SHA-256: `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`; health-result SHA-256: `BC1D091E20047ED1ECC5E37BC7407E0806F5ADFE54E41B4672FA7D552E0FE072`.
- `io_pdx_mesh`: extension `0.91.0`, locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`; adapter health confirmed mesh/animation export functions and loaded extension.

## Provider tasks, credits, and immutable downloads

| Stage | Task/response | Result | Credits |
|---|---|---:|---:|
| Meshy 7 image-to-3D | `01a0427d-0a5f-746f-8270-f64b4ba409c1` | `SUCCEEDED`, rechecked live | 30 consumed |
| First rig submission | provider HTTP 422 pose-estimation failure; no completed task id returned | `FAILED`, refunded/not consumed | 0 consumed |
| Materially different rig recovery | `01a04285-34b0-7d0f-b256-e2c3f0048d67` | technically `SUCCEEDED`, anatomically rejected | 5 consumed |

Selected immutable provider downloads:

| File | SHA-256 |
|---|---|
| `provider/downloads/generation_01_model.glb` | `AF53CF07DE8FE610F30D8676566980DF89D420C4DC703EDB67E5DCB490F2D0FD` |
| `provider/downloads/generation_01_model.fbx` | `0390E40FBF9D943EC03F3CE92357489D99542F7A55125AFB83CB903809BEB8A1` |
| `provider/downloads/rig_01_primary.glb` | `3BCFBD1DC58E7F2542EBA4764DC78F12207F97AC4DC533A349FD56D42A4CB4D0` |
| `provider/downloads/rig_01_primary.fbx` | `595FBAFAC61222763AC35AFE4882C4814A14EF6C1A28124BDB48DDA5029F40B1` |
| `provider/downloads/rig_01_walking.fbx` | `EC0A501847193CCCE3956BCC6BDF37F14C76D8D22FEB5B662697C85A327A76D4` |
| `provider/downloads/rig_01_running.fbx` | `BC9FF6AAD1148A601DBEA5D7579B43A1D71EC98BAB827822E6560A38A8D93993` |

The rig downloads remain rejected evidence only and must not be copied to runtime.

## Vanilla scale calibration and geometry

- Vanilla mesh: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`
- Package calibration copy: `blender/reference/western_european_infantry.mesh`, SHA-256 `F00FBADFDACDD1046F7119E62E2C47D644EA7A92D0F686B71D230BC843AEF8BA`
- Vanilla entity: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset`, `infantry_rifle_entity`
- Selected reference object: `polySurface106`, collision-only `pCube1` excluded
- Vanilla source-mesh height: 7.3518242835 m
- Vanilla entity scale: 0.8
- Vanilla effective runtime height: 5.8814594268 m
- Axes/contact: forward `-Y`, up `+Z`, ground contact Z 0.0084189996 m
- Provider candidate source height: 1.9058682919 m
- Blender target source-mesh height: 7.3518242835 m
- Recorded normalization factor: 3.8574672473 from measured imported bounds; job planning factor from declared 1.9 m provider height is 3.8693812018
- Proposed entity scale: 1.35, applied exactly once by the parent
- Proposed effective runtime height: 9.9249627827 m
- Ratio to vanilla infantry effective height: 1.6875
- Candidate final bounds: 6.2483215332 x 2.5114848614 x 7.3518238068 m; proposed runtime bounds approximately 8.4352340698 x 3.3905045629 x 9.9249621391 m

Geometry candidate results:

- 29,999 final triangles / 14,928 vertices / one object
- Uniform scale and ground contact passed; final height delta was under `5e-7` m
- Triangulated, no degenerate faces, no non-manifold edges, no negative-scale objects, one UV layer
- 59 boundary edges remain across small closed boundary components after bounded repair. Two cap candidates were rolled back because repair would introduce non-manifold topology. This is not silently approved for export.
- Loose-part segmentation produced one substantive component with 29,999 polygons and no discarded zero-face or degenerate fragments. `creature_components.json` status remains `review_required`.
- The provider base is protected in `blender/source/chaosx_paleogenetic_creature_provider_source.blend`; working checkpoints exist through `blender/checkpoints/05_pre_export.blend` and the segmentation checkpoint `02b_segmented_creature.blend`.
- Provider PBR base-color, normal, metallic, and roughness maps are preserved. No PDX DDS package was promoted because rig/action/export acceptance did not pass; raw grayscale roughness was not misused as a PDX specular map.

## Rig, weights, actions, export, and reimport

Written required rig map: ground root; asymmetric torso; independent primary and secondary cranial chains; four separate shoulder/elbow/wrist/tip chains; two hip/knee/ankle/toe chains.

Rig result: `blocked`. The only live Meshy recovery route produced a 24-bone humanoid that fails this map. Its candidate contained approximately 1,914,184 triangles across `char1.001` and `Icosphere.001`, no approved material, 637 non-manifold edges, and a two-frame clip. No weighting approval exists.

Required actions and proposed ids:

- `idle` -> `chaosx_paleogenetic_creature_idle`
- `stalk` -> `chaosx_paleogenetic_creature_stalk`
- `move` -> `chaosx_paleogenetic_creature_move`
- `charge` -> `chaosx_paleogenetic_creature_charge`
- `attack` -> `chaosx_paleogenetic_creature_attack`
- `defend` -> `chaosx_paleogenetic_creature_defend`
- `roar/special` -> `chaosx_paleogenetic_creature_roar`
- `wounded` -> `chaosx_paleogenetic_creature_wounded`
- `death` -> `chaosx_paleogenetic_creature_death`

All are `blocked`: there is no compatible accepted provider rig on which to request or validate substantive motion. Death therefore has no approved impact/collapse/settling source. Walking/running files from the rejected humanoid rig do not satisfy `stalk`, `move`, or `charge`.

Export/reimport status: not run by design. Exporting the static geometry or the rejected humanoid rig would violate the animated creature requirement. There is no `.mesh`, no `.anim`, no exporter receipt, and no reimport proof to hand to runtime.

## Sourced audio evidence and current disposition

- Source page: https://opengameart.org/content/monster-sound-effects-2
- Title: **Monster Sound Effects 2**
- Creator: Ogrebane
- Publisher: OpenGameArt.org
- Published: 2010-12-19
- License: CC0
- Source page describes 17 WAV files covering monster/beast/creature idle, attack, defend, hit and death use.
- Original ZIP: `audio/originals/monster_sfx_pack_2.zip`
- ZIP SHA-256: `8D9831E5596446EBAFB8E6A958E757F07CBD385F9E417B4D9704D63A05A2CD63`
- Direct-download URL to retain in provenance: `https://opengameart.org/sites/default/files/monster_sfx_pack_2.zip`
- Retrieval date: 2026-08-27
- The 17 immutable WAVs are 44.1 kHz, stereo, 24-bit PCM and approximately 0.319-1.000 seconds each. No derived file was manufactured, synthesized, or generated.

Role synchronization cannot be finalized until the corresponding provider actions exist. Proposed phase binding after action recovery is: selection/idle at state entry; move at first planted contact and alternating contacts; attack/contact at the strike apex; impact at visible contact; special/roar at the first open-mouth peak; death at body impact followed by silence during settling. Exact frame numbers are blocked with the missing actions.

## Counter inspection and handoff

- Installed definition: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`
- Large reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds`
- On-map reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`
- Matching skill-local families: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `.../map_counters/`
- Large strip: 152 x 42 RGBA, `noOfFrames = 2`, two 76 x 42 frames, transparent unused canvas, black/gray silhouette and border treatment with muted vanilla green shading. Dominant sampled opaque green is RGB `73,106,73`; observed shade family includes `74,107,74`, `83,114,83`, `100,128,100`, `116,141,116`, and `125,149,125`.
- On-map strip: 60 x 12 RGBA, `noOfFrames = 2`, two 30 x 12 frames, transparent unused canvas, compact black/grayscale/white state treatment; it is not an arbitrary-green miniature.
- Required large token: `GFX_unit_paleogenetic_creature_icon_medium`
- Required on-map token: `GFX_unit_paleogenetic_creature_icon_medium_white`
- Proposed paths: `gfx/interface/counters/divisions_large/unit_paleogenetic_creature_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_paleogenetic_creature_icon.dds`
- Art brief: an original instantly readable asymmetrical two-headed/four-armed creature silhouette, preserving both two-frame state variants, exact strip geometry, transparent canvas, border/value hierarchy, and the sampled vanilla palette family. Do not reuse or rename the infantry art.
- Counter production remains parent/`chaosx_icon_artist` owned. No DDS or `.gfx` entry was created in this package, so the counter requirement is `blocked/pending artist handoff`, not complete.

## Selected source-to-runtime synchronization

No runtime synchronization was performed. The selected source geometry hash is the Meshy 7 GLB `AF53CF07DE8FE610F30D8676566980DF89D420C4DC703EDB67E5DCB490F2D0FD`, but it is not an accepted animated runtime source. Destination hashes and copy-provenance rows do not exist because the animation/export gate failed. Parent must not copy provider or `docs/assets` files into runtime until a compatible rig, all nine approved actions, PDX materials, export, and reimport proofs exist.

## Files created or changed by this finishing pass

- This handoff.
- Package-local manifest, runtime handoff/crosswalk, audio and counter evidence, and append-only history are updated in the package by the finishing pass and should be reviewed together with this file.
- Adapter health receipt `logs/adapter/c1b9d6461576435abee712d45b82ec79.result.json` was written by the mandatory health operation inside the package.

## Meaningful validation performed

- Rechecked both provider task outcomes through the live locked Meshy MCP route and reconciled consumed credits (30 + 5).
- Confirmed the live schema has no dedicated multi-limbed creature-rig operation or rig-map input, so another `meshy_rig` call would repeat the failed/incompatible capability rather than provide a genuine recovery.
- Verified all dependency-locked adapter source checksums, Blender 5.1.2, bridge reachability, adapter 1.10.14, and loaded `io_pdx_mesh` 0.91.0.
- Verified source/refinement, provider-download, Blender-reference/report, ZIP, and WAV checksums.
- Reconciled numeric scale facts against the installed vanilla infantry mesh/entity and inspected the installed counter definitions, exact DDS dimensions, frame counts, alpha behavior, reference-family assets, and sampled palette.
- Confirmed the segmentation report contains one substantive component and no discarded zero-face fragments.

## Skipped validation and remaining blockers

- No Meshy animation calls: an anatomically rejected rig cannot serve as a valid source, and no dedicated creature rig capability exists in the live route.
- No weight/deformation/contact/action preview audit: no valid rig/action candidate exists.
- No PDX texture conversion: it would not unblock the rejected rig/action gate and no runtime export is permitted yet.
- No `.mesh`/`.anim` export or reimport: required rig, weights, and all nine substantive action sources are absent.
- No sound frame synchronization proof: action frames are absent.
- No bespoke counter art: it must be produced through the separate icon-artist route after this recorded vanilla inspection.
- No active-runtime copy or hash synchronization: parent-owned and unsafe before a valid package exists.
- No HOI4 launch or in-game validation was performed.

The package can advance only if Meshy exposes and successfully returns a dedicated compatible multi-limbed creature rig and action set, or the user explicitly approves a professional licensed animation source after the provider-incapability gate. Local replacement rigging/motion and the rejected humanoid rig remain forbidden.
