# Alien infantry 3D package manifest

Status: `needs_user_review`; the first Meshy 7 candidate is rejected and no recovery call has been launched.

## Identity and consumer

- Event: 016 Brilliant Scientist.
- Asset: `alien_infantry`.
- Exact reusable entity: `alien_infantry_entity`.
- Owning subunit sprite token: `alien_infantry`.
- Required identity: generic bald green alien, large black eyes, field harness, grounded boots, and one readable retro-futurist laser rifle, with no DHR, D'Rhondan, Kruger, country, ideology, event, organization, provider, text, or watermark marks.

## Dependency and route evidence

- Dependency lock: `.tools/3d_pipeline/config/dependencies.lock.json`, schema `1.0.0`.
- Meshy route: official `@meshy-ai/meshy-mcp-server` `0.4.0`, git `d8c77d1cb897e345eb41d38b510b8391b1664346`, compatibility revision `meshy-7-v4`, exact generation model `meshy-7`.
- Meshy tools verified before spend: `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate`.
- Blender: `5.1.2`, build `ec6e62d40fa9`.
- Repository adapter: `chaosx_blender_hoi4` `1.5.0`; health request `103f7c71c86645bc84e1d2efc279ca53`; candidate-prepare request `24b292a4a93948deb8ac38c74d85e108`.
- `io_pdx_mesh`: `0.91.0`; locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Environment verification: `.tools/3d_pipeline/verify_environment.py` completed with zero findings before provider spend.
- Job override: `alien_infantry` resolves to `docs/assets/016_brilliant_scientist/models_3d/alien_infantry`.

## Source lineage

- Immutable ImageGen original: `refs/evidence/imagegen_original_opaque.png`, SHA-256 `360E3679836041B28BABBAEA21D758CB29E84090942C364803208B2978DC61FE`.
- Two native-alpha edit attempts were preserved and rejected because both remained opaque RGB; their checksums are in `refs/original/input_manifest.json`.
- The repository-permitted `rembg` fallback added alpha without editing the soldier's RGB content.
- Exactly one Meshy input was used: `refs/original/meshy_input.png`, 1024x1536 RGBA, SHA-256 `E71F874C68B5E995206B6BD083498642E434C6A89BA64899A3DF13789ADE6CD2`.
- Alpha spans 0-253 with foreground bounds `[195, 9, 923, 1515]`. Maximum alpha 253 is the deterministic rembg probabilistic soft matte, not a colour or geometry edit.
- A faint green/grey antialias fringe around parts of the head and rifle was recorded before submission. Seven-view provider QA found no obvious halo-derived shell or floating backdrop slab.

## Provider lineage and spend

- Before the paid call, the job contained no provider task ID, paid receipt, download, or credit record; no pre-existing paid Meshy task was available to retrieve.
- Generation task: `01a02497-1fb9-7a1b-bec6-ec388d54a016`, exact model `meshy-7`, successful at 100%.
- Planned and consumed attributable generation spend: 30 credits.
- The wider live-balance delta was 60 credits while other agents were active; only the provider task's own 30-credit receipt is attributed here.
- GLB: `provider/downloads/generation_model.glb`, SHA-256 `E22474E3697FEF917E98AF9A3FD6B544A66E10B5C4A45A5FF4967546638A527A`.
- FBX: `provider/downloads/generation_model.fbx`, SHA-256 `B16734164A6A208B0B89349BED24339B0D97DC7092E53B81B19BC676B82171D6`.
- Provider PBR maps and their checksums are preserved in the download manifests. No remesh, rig, animation, conversion, retexture, or paid recovery credits were consumed.

## Candidate decision

- Rejected: the returned T-pose is entirely unarmed and omits the locked laser-rifle component.
- Source density was 1,995,264 triangles; the protected working duplicate was reduced to 29,999 triangles.
- Working topology has 20,163 loose boundary edges, 356 boundary components, and 48 branched boundary components; it has zero non-manifold edges and zero degenerate faces.
- Contact sheet: `blender/previews/alien_infantry_candidate_contact_sheet.jpg`, SHA-256 `C7B1DCC89C298DFAAE21A9880268853320C3C706454C83047FA436A5CB30DD05`.
- Detailed rejection record: `validation/generation_rejection.json`.
- Files named `01_geometry_approved.blend` through `05_pre_export.blend` are automatic adapter checkpoints only. They do not constitute acceptance, rig approval, action approval, or export approval for this rejected candidate.

## Vanilla calibration

- Mesh: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`.
- Entity: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset#infantry_rifle_entity`.
- Axes: forward `-Y`, up `+Z`.
- Measured vanilla source height: `7.351824797689915`.
- Candidate source height: `7.3537750244140625`.
- Entity scale, applied once: `0.8`.
- Candidate effective runtime height: `5.8830200195312505`; delta from calibrated vanilla runtime height: `0.0015605927312503098`.
- Scale gate passed, but it does not override the component rejection.

## Downstream status

- Geometry acceptance: blocked by missing rifle.
- Runtime material and DDS processing: not performed on rejected geometry.
- Rig and weight audit: not performed.
- Required actions `idle`, `move`, `laser_attack`, `defend`, `support_attack`, `retreat`, and `death`: all blocked pending accepted rifle-bearing geometry.
- PDX `.mesh` and `.anim` export: not performed.
- PDX reimport proof: not performed.
- Runtime entity, model, animation, and sound definitions: not written for a rejected model.
- In-game/live-consumer validation: parent/user owned and not claimed.

## Sound and counter packages

- Four CC0 sourced audio candidates and mechanical PCM derivatives exist for laser fire, movement, idle, and death. Provenance, URLs, creators, licenses, transformations, hashes, and deferred synchronization points are in `evidence/audio/provenance/audio_sources.json` and `runtime/sound_handoff.md`.
- Per-subunit selection and acknowledgement voices are explicitly blocked because installed consumers are country/original-tag-wide `TAG_infantry_*`; replacing them would also replace ordinary infantry voices.
- The bespoke large and on-map counters are complete, installed, and registered through `interface/alien_infantry_system.gfx`. Exact consumers, two-frame dimensions, alpha behavior, sampled vanilla greens, processed sources, DDS round trips, and contact-sheet evidence are recorded in `docs/assets/016_brilliant_scientist/dhrondan_icon_package/manifest.md`. Live display acceptance remains user-owned.

## Recovery gate

The bounded recovery proposal is one additional Meshy 7 image-to-3D generation from a rifle-silhouette-preserving alpha cleanup, estimated at 30 extra credits. Because it is failure-driven paid recovery, authorization is pending. No recovery, rig, animation, or export operation may start until the user confirms it.
