# Event 012 Africa Riverborn Meshy 7 reference-recovery handoff

## Outcome

Status: `blocked_generation_recovery_3_rejected_identity_and_topology`.

The newly generated, model-ready single-image reference passed the reference gate and was submitted exactly once to Meshy 7. The provider task succeeded, but the locked Blender adapter review rejected the resulting geometry because the required shield and spear were both absent and the mesh retained 1,977 loose boundary edges across 355 boundary components. The provider result was archived as rejected evidence and was not promoted, rigged, animated, converted, exported, reimported, or synchronized to runtime.

No blind retry was performed. This recovery consumed 30 credits, moving the live balance from 123 to 93. Downstream spend was zero.

## Source and selected reference lineage

- Source mode: `reference_only_user_authorized`.
- Source page: https://www.pathofexile.com/forum/view-thread/3424044
- Source title: `Kiloava Chieftain Concept Art`, from the Path of Exile Trial of the Ancestors concept-art set.
- Creator/publisher: Grinding Gear Games art team / Grinding Gear Games; the official page does not identify the individual artist.
- Terms observed: copyrighted reference only with no reusable license offered; no explicit `NoAI`, no-derivatives, or equivalent incompatible restriction was observed on the official page.
- Retrieval date: 2026-08-24.
- Source fingerprint SHA-256: `3BB1DD003857D6A36EE7CE41BAC53F0A276658BD993F7588AE24F5F47C6B24A5`.
- Authorization: the user authorized this actual modern designed artwork for reference-only use; source pixels are non-shipping evidence and were not promoted into runtime art.
- Prior rejected Meshy input: `refs/derived/prior_rejected_meshy_input_fb44f05c.png`, SHA-256 `FB44F05C9F19740802AB446B851678766B64C6D9DB8BCB9902CEC65C2ADF4521`.
- New selected Meshy input: `refs/original/meshy_input.png`, SHA-256 `A1FA4DAF0B7DBE72B3284D2A878524F6FD322F56B708BC5DA5937312B724DB59`.
- Reference dimensions and format: 1024x1536 RGBA; alpha extrema 0–255, zero-alpha corners, visible-alpha bounds `[95, 29, 887, 1403]`.
- Refinement mode: native ImageGen source-informed, substantially original full-body A-pose refinement. The prompt required a complete carved shield strapped to the subject's left forearm/hand and a complete long spear gripped normally in the subject's right hand, with period river-clay, reed, leather, carved wood, and mineral-pigment materials; no anime, modern weapons, electronics, text, watermark, cropped limbs, or detached props.
- Alpha handling: both native ImageGen outputs were RGB images with a baked checkerboard despite the transparency request. A documented `rembg 2.0.61` fallback produced the selected RGBA input. The failed native-alpha outputs and rejected alpha-matting alternative remain under `refs/derived/`.
- Comparison and prompt evidence: `refs/briefs/riverborn_reference_recovery_prompt.md`, `refs/derived/riverborn_reference_recovery.md`, and `refs/original/input_manifest.json`.
- Reference-gate result: pass for single humanoid identity, complete full-body composition, riggable neutral pose, left-side shield attachment, right-hand spear grip, period/color requirements, non-anime presentation, and transparent unused canvas.

## Dependency and route evidence

- Official Meshy MCP package: `@meshy-ai/meshy-mcp-server` 0.4.0.
- Locked Meshy route git head: `d8c77d1cb897e345eb41d38b510b8391b1664346`.
- Meshy SDK: 1.29.0.
- Exact generation model: `meshy-7`; no alias or downgrade was used.
- Blender: 5.1.2.
- Repository-owned adapter: `chaosx_blender_hoi4` 1.10.14.
- Adapter health request ID: `77449c3fa1d14045aa6cee5ed5e520ac`; locked socket `127.0.0.1:9876` was listening.
- `io_pdx_mesh`: 0.91.0, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Environment bootstrap and Meshy probe returned no lock or capability findings before the paid call.
- Preflight and request receipts: `provider/credits/generation_recovery_3_preflight.json` and `provider/requests/generation_recovery_3.json`.

## Provider task and costs

- Tool route: the verified official `meshy_image_to_3d`, followed by `meshy_get_task_status` and `meshy_download_model`.
- Task ID: `01a03d82-1562-72f3-99ea-68e83fc2cebf`.
- Model and generation settings: `meshy-7`, standard mode, A-pose, triangles, 25,000 target topology, provider remesh enabled, pre-remeshed preservation requested, PBR textures, image enhancement off, remove lighting on, multiview off, GLB and FBX output.
- Provider status: succeeded.
- Estimated and consumed credits: 30.
- Live balance: 123 before, 93 after; delta `-30`.
- Paid follow-ups: zero. Rig spend: zero. Animation spend: zero. Total downstream spend: zero.
- The provider exposed a pre-remeshed GLB only through a signed URL, while the locked official download selector had no pre-remesh artifact option. No direct REST request was made and no signed provider URL was retained.

## Downloaded immutable artifacts

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `provider/downloads/generation_recovery_3/riverborn_generation_recovery_3.glb` | 17,144,220 | `28AFD995E514EF443D78BA113C0AF5DA4B69069836170D8F20B3841A3A46A878` |
| `provider/downloads/generation_recovery_3/riverborn_generation_recovery_3.fbx` | 17,698,124 | `0F60EDB827663C85DD8473113F80902384007F56673B05EBB6871B94BCFC163B` |
| `provider/downloads/generation_recovery_3/riverborn_generation_recovery_3_textures/base_color.png` | 5,607,482 | `61DB4EAF8B1997D0F644505EA5D71B624926679A890E627CBEAEBA1803E6734B` |
| `provider/downloads/generation_recovery_3/riverborn_generation_recovery_3_textures/metallic.png` | 385,989 | `90F611DA313C4228BF7A2587ABF399E9361A7D8F439AA24AAC5F16E7DAAE0019` |
| `provider/downloads/generation_recovery_3/riverborn_generation_recovery_3_textures/normal.png` | 8,719,466 | `097B455CBECA99D1D89384A9772508F7FE6C99C1A01C8660AAE829DFEB4EEABF` |
| `provider/downloads/generation_recovery_3/riverborn_generation_recovery_3_textures/roughness.png` | 1,656,779 | `1118B286B153AD8940F3DC6EB5EECC83400253A5A5BAE1A521B4A76F3AB77A76` |

The redacted task, response, credit, and artifact lineage is in `provider/tasks/generation_recovery_3.json`, `provider/responses/generation_recovery_3_submission.json`, `provider/responses/generation_recovery_3_status.json`, `provider/credits/generation_recovery_3_postflight.json`, and `provider/downloads/generation_recovery_3/download_manifest.json`. No API key or signed URL is stored in these receipts.

## Blender adapter gate and rejection

- Vanilla reference: `refs/vanilla/asian_infantry.mesh`.
- Measured vanilla source height: 7.516803.
- Calibrated target source height: 9.396004.
- Entity scale: 1.0, applied exactly once; ground contact 0.
- Adapter operation: `prepare_candidate`.
- Adapter request ID: `b812812f789040319a701ba7fa0782f6`.
- Prepare report: `blender/reports/chaosx_riverborn_recovery_3_prepare.json`, SHA-256 `62C2DB9841DC8F07D9B3219CE17F6A5C9F665555BE750C2828CA67C3BCE51ED9`.
- Geometry: 24,165 triangles and 11,802 vertices.
- Topology blockers: 1,977 loose boundary edges, 355 boundary components, and 76 branched boundary components.
- Clean checks: no degenerate triangles, non-manifold edges, negative scale, or zero normals were reported.
- Identity blockers: front, three-quarter, left, and right adapter previews show that the provider omitted both the shield and the spear.
- Decision: reject. The acceptable triangle count and otherwise clean checks do not outweigh the missing required identity components or the open fragmented topology.
- Rejection evidence: `blender/reports/generation_recovery_3_rejection.md` and the recovery-3 adapter previews under `blender/previews/`.

## Required actions, material/export state, and no-promotion boundary

The required semantic actions remain `chaosx_riverborn_idle`, `chaosx_riverborn_move`, `chaosx_riverborn_attack`, `chaosx_riverborn_water_transition`, and `chaosx_riverborn_death`. None was requested from Meshy or authored locally because the base geometry failed before the rig/action gate. There are no accepted provider rig, weights, action sources, action manifests, PDX material conversions, `.mesh` or `.anim` exports, exporter results, reimport proofs, or source-to-runtime synchronization results for this recovery.

Legacy/local-motion files are not accepted as recovery substitutes. The recovery-3 GLB/FBX and Blender checkpoints are rejected evidence only. They must not be wired or promoted.

## Existing audio and counter packages

No audio or counter file was synthesized, edited, or wired during this recovery.

The existing sourced audio evidence remains unchanged. It uses the public-domain Wikimedia Commons sources `Flowing-water-100019.ogg` by Fg2 and `Ducks_landing_in_water.ogg` by the U.S. Fish and Wildlife Service, with source SHA-256 values `6CAB6C85A0B9159AA9E98F30BEF16E5F8976A3154D8CEC4E00925AAC21289F0B` and `C95C1641721CB80645D58FB05CEED871DCB74D1A62AD14E5D26F3B73F7BFA816`. Exact derived-file hashes and transformations remain in `audio/manifest.md`. Proposed identifiers remain `chaosx_riverborn_<role>_sound` and `chaosx_riverborn_<role>_sfx`. Animation synchronization is provisional because the accepted action set does not exist.

The bespoke counter package also remains unchanged. Its consumers are `unit_riverborn_icon` and `onmap_unit_riverborn_icon`. It contains a 152x42 two-frame large strip and a 60x12 two-frame on-map strip. The inspected vanilla definitions are `GFX_unit_infantry_icon_medium` and `GFX_unit_infantry_icon_medium_white` in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`; the corresponding vanilla DDS references are `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`. Reference-family evidence is retained under `counters/reference/`, and the sampled infantry-green evidence records dominant RGB `(73,106,73)` with mapped range `(20,34,21)` through `(154,175,147)`. Engine-facing DDS promotion, GFX/runtime ownership, and live consumer validation remain parent-owned.

## Files updated or created

- `docs/assets/012_africa/models_3d/riverborn/job.yaml`
- `docs/assets/012_africa/models_3d/riverborn/history.jsonl`
- `docs/assets/012_africa/models_3d/riverborn/manifest.md`
- `docs/assets/012_africa/models_3d/riverborn/runtime/handoff.md`
- Riverborn-only reference evidence under `refs/original/`, `refs/derived/`, and `refs/briefs/`
- Riverborn-only provider requests, responses, credits, tasks, and immutable downloads under `provider/`
- Riverborn-only Blender reports, previews, protected source/checkpoint evidence, and rejected prior-candidate snapshots under `blender/`
- This handoff: `docs/plans/012_africa_plans/subagent_handoffs/012_africa_riverborn_meshy7_reference_recovery.md`

Pre-existing modified Riverborn audio source and derived files were not touched or reverted by this recovery worker.

## Validation and remaining blocker

Meaningful validation included exact-image visual inspection, RGBA and alpha-bound checks, dependency-lock/bootstrap verification, exact `meshy-7` schema confirmation, live balance preflight/postflight, provider completion inspection, immediate artifact download and SHA-256 verification, vanilla-scale calibration through the locked adapter, multi-view geometry inspection, and adapter topology statistics.

Rigging, animation, PDX texture conversion, `.mesh`/`.anim` export, export reimport, and runtime synchronization were deliberately skipped because the provider mesh failed the mandatory identity and topology gates. Hearts of Iron IV was not launched; live consumer validation belongs to the user and parent.

The Riverborn Meshy 7 package remains incomplete and blocked. Parent action is required to choose whether to authorize a materially different future reference/provider strategy. This handoff authorizes no additional provider task and makes no in-game completion claim.
