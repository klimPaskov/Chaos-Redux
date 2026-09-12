# Autonomous Robot asset finalization

Disposition: **physical model, action and biped-counter asset QA implemented and parent promotion verified; sourced-audio acceptance and state/effect/sound integration remain open**.
This handoff supersedes older robot handoffs for source selection, output hashes, current action timings and companion status.
No live-game completion is claimed.

## Exact physical promotion

Job root: `docs/assets/shared_robot_system/models_3d/autonomous_robot/`.
Selected source: `attempts/20260906_weaponfree_blender/pbr_repair/blender/checkpoints/40_final_local_patch.blend` under that root, SHA-256 `2EBBF34D1E1F4506D042C51CB00DDD3CA87F6E74C33A2112824F431259974114`.
The immutable promotion receipt is `attempts/20260906_weaponfree_blender/evidence/finalize_20260912/physical_promotion_manifest.json`, SHA-256 `33BE6318E0240130300E178245C3961F03FA4E29D9A0FA3B79AA10F1E04B7149`.
Its `exports` array gives all 15 full repository source paths, destinations, byte sizes and SHA-256 values; its `roles` array gives every native action/export/reimport receipt.

The parent promoted every payload from `export/final40_20260909/` into `gfx/models/units/autonomous_robot/` with its existing basename.
The set is `autonomous_robot.mesh`, the eight `autonomous_robot_<role>.anim` files, `robot_body_diffuse.dds`, `robot_body_normal.dds`, `robot_body_specular.dds`, `robot_weapon_diffuse.dds`, `robot_weapon_normal.dds` and `robot_weapon_specular.dds`.
Selected mesh SHA-256: `C1B95902D34C299CD4CBA41E1CF262FA08A753A2EB8CC9E9172C4D68DBFE04D9`.
The worker independently verified all 15 promoted runtime files and all six material bindings in `runtime_sync_after_parent_promotion.json` under the fresh evidence folder.
The immutable promotion receipt retains its pre-promotion destination snapshot; the later readback records the completed parent-owned copy.

The parent retained `autonomous_robot_mesh` in `gfx/entities/autonomous_robot.gfx` and replaced obsolete `char1.003` meshsettings with all six streams below.
The shader is `PdxMeshAdvancedSkinned` for every row.
Texture basenames are relative to the model directory.

| Exported object | Index | Diffuse | Normal | Specular |
| --- | ---: | --- | --- | --- |
| `mesh.002` | 0 | `robot_body_diffuse.dds` | `robot_body_normal.dds` | `robot_body_specular.dds` |
| `mesh.002` | 1 | `robot_body_diffuse.dds` | `robot_body_normal.dds` | `robot_body_specular.dds` |
| `RB_Gun_L` | 0 | `robot_weapon_diffuse.dds` | `robot_weapon_normal.dds` | `robot_weapon_specular.dds` |
| `RB_MountFeed_L` | 0 | `robot_weapon_diffuse.dds` | `robot_weapon_normal.dds` | `robot_weapon_specular.dds` |
| `RB_Gun_R` | 0 | `robot_weapon_diffuse.dds` | `robot_weapon_normal.dds` | `robot_weapon_specular.dds` |
| `RB_MountFeed_R` | 0 | `robot_weapon_diffuse.dds` | `robot_weapon_normal.dds` | `robot_weapon_specular.dds` |

Keep `autonomous_robot_entity`, its snow/desert clones and entity scale `0.8` in `gfx/entities/autonomous_robot.asset`.
Scale is applied exactly once; the source geometry height is `7.3518242836`, matching installed `western_european_infantry.mesh#polySurface106` with collision excluded, and effective runtime height is `5.8814594269`.
Retain the eight `autonomous_robot_<role>_animation` definitions in `gfx/models/units/autonomous_robot/animation_autonomous_robot.asset` and matching mesh animation/state IDs.

## Geometry, rig and action acceptance

The closed assembly has 14,783 source vertices, 29,262 triangles, five export objects and 22 bones.
The body has 26,206 triangles; each gun has 860; each mount/feed assembly has 668.
Every required identity component exists: armored biped, sensor goggles, limbs, backpack, feet, two complete independent guns and their mounts/feed boxes.
All export objects have valid normalized weights, no zero-weight deforming vertices, no opposite-side influence, no indexed holes/nonmanifold edges, no degenerate triangles, no negative scale and no exporter warning.
The two gun objects are rigidly bound to `Gun_L` / `Gun_R`; feed assemblies are rigidly bound to their matching forearms.
Permanent mounting makes human grip, support-hand and stock contacts inapplicable.

All six engine streams stay under the vertex/index budget; the largest is 33,349 stream vertices and 60,060 triangle-index entries.
Body textures are 1024×1024 and weapon textures 512×512.
Final body gloss is exactly `LanczosResize(255 - provider_roughness, 1024×1024)`; inversion occurs before resize.
Normal channels follow the verified PDX layout: R=0, G=tangent X, B=0, A=tangent Y.

| Role | Blender action | Source frames at 24 FPS | Loop | Role evidence |
| --- | --- | --- | --- | --- |
| idle | `RB_idle` | 0–96 | yes | Sensor scanning |
| move | `RB_move` | 0–48 | yes | Alternating heavy forward march |
| attack | `RB_attack` | 0–96 | no | Aim, bilateral firing/recoil, recovery |
| defend | `RB_defend` | 0–96 | yes | Distinct nonfiring guard |
| support_attack | `RB_support_attack` | 0–120 | no | Supporting-fire stance and longer aim/recovery sequence |
| retreat | `RB_retreat` | 0–48 | yes | Backward withdrawal march |
| training | `RB_training` | 0–120 | yes | Nonfiring systems and weapon drill |
| death | `RB_death_contact_v3` | 0–96 | no | Articulated buckle, collapse, body impact and prone settling |

All roles use in-place XY roots with deliberately keyed vertical grounding.
The fresh read-only audit checked all 728 native evaluated source frames; assembly floor bounds remain `0.00099945–0.00100065`.
Five actual-byte reimport phases per action match source bounds within `0.000005236` source units.
Oriented triangle/position and weight parity are exact; maximum UV error is `2.98e-8`.
All 80 actual-byte muzzle-locator samples remain within `0.000001864` source units of their modeled tips and `0.00004189°` of the barrel axis.
Actual exported normals retain source corner normals within `0.009521°`, below the strict guard.
Blender's later custom-normal reimport encoding reaches `0.769382°` on a small body subset; this is a documented reimport precision difference, not a defect in the actual engine normal bytes.
The 28-edge position-weld diagnostic results from merging separate coincident face fans; indexed source topology is closed.

GPT-6-astra reviewed the source40 detailed attack/death/training frames and all four five-phase actual-byte contact sheets, covering all eight roles from left and three-quarter views.
The prone death settles on body/forearms/knees with horizontal barrels, and its first chest/forearm impact is source frame 69.
The parent previously accepted visible source40 material identity and death on 2026-09-09.
This finalization changed no skeleton, geometry, keyed actions, PDX mesh or animation bytes.

## Sound and effects handoff

The exact revised event table is `attempts/20260906_weaponfree_blender/evidence/finalize_20260912/runtime_sync_crosswalk.json`.
Source frames and exported sample indices start at 0; reimport frames start at 1; runtime time is `source_frame / 24`.
Do not double-emit the duplicated endpoint of a looping animation.
Muzzle locators are `robot_muzzle_l` and `robot_muzzle_r`, parented to `Gun_L` and `Gun_R`.
Use installed vanilla `mg_muzzle_particle`, `mg_muzzle_smoke_particle` and `mg_muzzle_flash` at the recorded muzzle events; the installed `units_infantry.asset` provides the exact consumer precedent.

Attack discharges: L16,22,28,34,40,46,52,58,64,70,76; R19,25,31,37,43,49,55,61,67,73,79.
Support discharges: L24,30,36,42,48,54,60,66,72,78,84; R27,33,39,45,51,57,63,69,75,81,87.
Recoil peaks at discharge+1, returns at discharge+3, and shifts each gun 0.04 local units along its barrel axis.
Defend and training must not emit firing sounds, muzzle particles or bullets.
The old long MG cue ends above the measured threshold before the last recoil phases and is rejected for this fire window.
The preserved 0.12-second MG pulse candidate has SHA-256 `73C5689911146D75B1A5131CAEEB826384979F6D4936A5E3A1AFC7BBA6BC25CB` and fits the 0.125-second alternating discharge spacing.
Its numerical lead-in is 0.0180952381 seconds, which is subtracted from each cue's `sound_trigger_seconds`; particles stay at the exact discharge time.
Candidate sound IDs are `autonomous_robot_mg_discharge_pulse_source` and `autonomous_robot_mg_discharge_pulse_sfx`; candidate destination is `sound/shared_robot_system/autonomous_robot/autonomous_robot_mg_discharge_pulse.wav`.

Idle motor repeats over four seconds; move/retreat servo repeats over two seconds, with footfalls at source frames 0 and 24.
Death destruction starts at frame 8; body impact is frame 69 (2.875 seconds).
The two-second servo window and 0.95-second footfall window have exact recipes/hashes in the attempt's `evidence/audio_final40/manifest.json`.
The fresh evidence folder's `audio/` contains original-source revalidation, exact candidate/retained WAV copies and their manifests.
`audio_probe.json` records PCM16 mono 44.1 kHz, clipping and boundary checks.
Four original audio files were restored exactly; six historical OGG intermediates remain absent while originals and WAV descendants remain preserved.

The motor recording is Maximilian Schönherr's CC BY-SA 4.0 Cordless Screwdriver and requires attribution, adaptation notice and ShareAlike.
The impact is stephan's public-domain Metal drop thump and the optional acknowledgement is Mx. Granger's CC0 Door knocker audio.
Lubini's CC BY 4.0 MG source explicitly adds undocumented layers; their rights are unresolved.
tcpp's public-domain Explosion 10 source does not establish recording versus synthesis; the recording requirement remains unresolved.
The Army Signal Corps MG film is preserved as CC0 research evidence but no firing-only soundtrack excerpt has been accepted.
Full source/download URLs, source and derivative hashes, terms and recipes are in `audio/source_revalidation.md`, `audio/mg_pulse_manifest.json`, the restored-original receipt and the original source ledger.
No audio was synthesized, generated, recorded, mixed or time-stretched here.
Additional researched recordings are preserved under `audio/replacement_research/`: unfa's raw Firecracker Explosion (CC0, Zoom H2 recording) and Cymeon's film-shoot machinegun blank fire (CC0, exact gun model unspecified).
Their pre-download source/URL/terms plan, original high-quality preview bytes and plain PCM review decodes have complete hashes in `download_receipt.json`.
Both decodes have no clipped samples; audible role selection and a firing-only excerpt remain pending.
`mechanical_candidates.json` provides a provisional 0.12-second excerpt around the recorded gun file's peak transient and the full raw destruction candidate with edge fades, with exact source offsets, hashes and measured onset leads.
Neither provisional excerpt nor its threshold measurement substitutes for audible semantic review.
These alternatives were not silently substituted into runtime or the existing pulse crosswalk.
No exposed tool could perform audible assessment of these non-speech effects; numeric checks do not prove seamless motor loops or perceived firing onset.

The parent owns `sound/autonomous_robot_sound.asset`, `sound/chaosx_sound.asset` and state-sound/effect changes in `gfx/entities/autonomous_robot.asset`.
Do not replace country-wide infantry voices: the inspected engine consumer has no per-subunit selection binding.

## Counter handoff

The old tracked robot counter remains immutable rejected evidence because it conflicts with the accepted biped.
The scoped `chaosx_icon_artist` replacement package is `evidence/counter_biped_20260912/` under the job root.
The package owner independently accepted the final DDS byte set after inspecting its actual-DDS neutral-matte proof and checking exact PNG/DDS equality, both frame states, alpha, palette, dimensions and every handoff hash.
The parent accepted the filled pale alternate fields with dark sparse biped glyphs; the final antialias processing retains that visual contract.
The promotion receipt is `attempts/20260906_weaponfree_blender/evidence/finalize_20260912/counter_independent_review.json`; it records both source and runtime destination paths, exact bytes and hashes, three consumer IDs and the frozen reviewed preview.
The artist's handoff is `2026-09-12_autonomous_robot_biped_counter_replacement.md` in this folder.
Large DDS SHA-256: `95E8A0816A614FEA7449494A026A1C57ED6B76D384C3ADEF933F1DE964E7CDDC` (25,664 bytes).
Map DDS SHA-256: `1115AACD9A57653E07BF30915649B0DDDB399253A0ACE59E6078C89ACB01E3C2` (3,008 bytes).
The parent promoted these exact DDS files in commit `475839ff206ac0a8261343eb3b52ee8cfcf6f179`.
The worker independently read both runtime destinations and verified exact byte equality in `runtime_counter_sync_after_parent_promotion.json` under the fresh evidence folder.
The parent promotion paths are `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds` (152×42, two 76×42 frames) and `gfx/interface/counters/divisions_small/onmap_unit_autonomous_robot_icon.dds` (60×12, two 30×12 frames).
Consumer IDs in `interface/autonomous_robot_system.gfx` are `GFX_group_autonomous_robot_icon` and `GFX_unit_autonomous_robot_icon_medium` for the large strip, and `GFX_unit_autonomous_robot_icon_medium_white` for the small strip; every consumer has `noOfFrames = 2`.
The unit owner is `common/units/016_brilliant_scientist_project_forces.txt#autonomous_robot` with sprite `autonomous_robot`.
Exact installed `interface/subuniticons.gfx`, infantry/mechanized DDS dimensions, state layouts, alpha and sampled green-palette evidence are in `counter_vanilla_inspection.json`.
The matching skill-local families are `units/land/counters_large/` and `units/land/map_counters/` under the event-assets vanilla reference assets.
Only the reviewed final replacement may be promoted; existing technology/equipment illustrations are outside this counter scope.
The map source required a documented chroma-key fallback after native-alpha attempts failed; original failed outputs remain archived, and final map pixels are grayscale with transparent outer canvas.
No physical counter identity was simplified: the tracked visual is rejected and the replacement depicts the accepted biped.

## Dependency and completion limits

Blender 5.1.2 build `ec6e62d40fa9` and io_pdx_mesh 0.91.0 are retained.
The exact deployed extension receipt is `.tools/3d_pipeline/reports/io_pdx_deployed_source_verification_20260912.json`, SHA-256 `9498FB8E634D53C3E290B4542E19A3AB7888DC672C4C3EB4999618AF78687866`, with 37 exact present matches, 3 expected absences and 0 mismatches.
`dependency_refresh_1_10_45.json` confirms the refreshed adapter 1.10.45 lock and all 17 source checks.
Native export/reimport receipts retain their actual 1.10.42/1.10.43 versions; fresh read-only channels used 1.10.44.
The direct MCP exposure remains 1.10.44; future 1.10.45 mutations must use the verified fresh locked wrapper/BlenderAdapterClient and explicit source guards.
No new Blender mutation or export was needed.
The installed hoi4-agent-tools 3.0.7 package contains technology MCP analysis/render routes, but no standalone Technology Tree Viewer binary was found among its three CLI registrations; standalone viewer availability is not claimed and is unrelated to this physical asset proof.

The protected fresh Meshy 7 body task is `01a07650-7b7a-713a-ae14-bb0a933eedb6`, with 30 provider-reported credits; this pass spent 0 and made 0 provider calls.
The inherited native ImageGen reference, complete weapon-removal prompts, two rejected alpha attempts, accepted clean gray input and parent approval remain archived.
No Internet artwork source is fabricated for that inherited user-authorized reference.
`job.yaml`, `manifest.json` and `manifest.md` select source40; earlier manifest bytes remain archived under `historical_manifests/`.

No requested physical component or semantic action was simplified or omitted.
Remaining work: source/audio audible acceptance, parent-owned state/effect/sound integration and review of user-owned live consumer evidence.
The physical asset package is promoted with independent byte and material-binding proof; overall custom-unit completion remains open for those explicit items.
Skills used: chaos-redux-3d-model-pipeline, chaos-redux-event-assets and chaos-redux-subagents.
The worker staged and committed no files; the parent owns integration commits, and unrelated staged changes were present during finalization.
