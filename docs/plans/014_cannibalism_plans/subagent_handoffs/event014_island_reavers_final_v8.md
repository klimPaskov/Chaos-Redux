# Event 014 Island Reavers final v8 handoff

> Historical v8 blocked handoff. Superseded by the accepted v11 Island Reavers runtime receipt; retain this file for failed-provider lineage only.

Date: 2026-08-24.

Status: `blocked_meshy_http_402_insufficient_funds`.

The source and one-image approval gate is complete. The exact locked Meshy 7 generation request failed before task creation with `Error: API request failed with status 402. Insufficient funds`. The balance remained 25 credits, zero credits were consumed, no task or response id exists, and no downgrade or provider substitution was used. The required model, rig, eight skeletal actions, Blender processing, DDS rebuild, `.mesh`/`.anim` exports, and reimport proof therefore remain blocked.

## Owned scope

- Package: `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/`.
- Handoff: `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_island_reavers_final_v8.md`.
- Runtime entity, gameplay, GFX, localisation, event, and sound-definition files were not edited.

## Dependency and route evidence

- Final verifier: `python .tools/3d_pipeline/verify_environment.py --probe-meshy`; result `findings: []`.
- Meshy route: official `@meshy-ai/meshy-mcp-server` 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, compatibility revision `meshy-7-v4`, exact model identifier `meshy-7`.
- Schema lock: `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`, revision `meshy-7-compat-live-declaration-2026-08-21`.
- Repository adapter: `chaosx_blender_hoi4` 1.10.0 from the authoritative dependency lock.
- Blender: 5.1.2, build commit `ec6e62d40fa9`.
- `io_pdx_mesh`: 0.91.0, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Two earlier verifier runs transiently left only their probe-owned wrapper/Node pairs (`39660`/`28636`, then `39508`/`39856`). Each exact pair was terminated after normal teardown did not complete and followed by `CLEAN`; the successful final verifier proves the actual environment is clean. This is a transient verifier cleanup defect, not a permanent provider blocker.
- Detailed receipt: `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/evidence/dependency_and_route_audit_v8.md`.

The required offline wiki pages consulted for this model surface were Graphical Asset Modding, Entity Modding, Unit Modding, and Sound Modding. The installed vanilla documentation tree contained no relevant model-export markdown in the standard documentation folder. The named vanilla model precedent is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`; its earlier package calibration records object `polySurface106`, source height `7.351824797689915`, `-Y/+Z` axes, `infantry_rifle_entity` scale `0.8`, and effective runtime height `5.881459838151932`. Fresh v8 import/measurement was not reached.

## Source, rights, and approved refinement

- Source file: `refs/source/bestiarum_painted_fleshmad_guide_01.jpg`.
- Source SHA-256: `3A832598C0AB2A23378AB8A5E6BA64985025C8DC84B94AEDBAA5DA77A137214D`.
- Source page: `https://bestiarumgames.com/blogs/news/the-remade-nasty-wet-flesh-painting-guide`.
- Title: `The Remade & Nasty Wet Flesh | Painting Guide`.
- Creator/publisher: Marcus Harland / Bestiarum Games.
- Archived page: `refs/source/pages/bestiarum/painting_guide.html`.
- Archived page SHA-256: `47C8AAF5C258DA4606A5E276AAF54FF119C16CBA29CC905DA5B484DBB10B99DA`.
- Rights mode: `reference_only_user_authorized`; commercial copyrighted art, no open license, and no explicit NoAI marker found in the archived evidence.
- Retrieval date: 2026-08-24 handoff lineage; source bytes remain non-shipping evidence.
- Explicit authorization: reference-only use for the exact Bestiarum painted Fleshmad, with native ImageGen cleanup and the bounded club-to-harpoon adaptation.

Native ImageGen preserved the living painted warrior identity, body, anatomy, bone kit, paint, clothing, and silhouette; isolated one full subject; removed the miniature base/scenery; improved clarity; changed the long held weapon into a crude period-fit fishing harpoon; and added only restrained culture-neutral coastal wear. It did not introduce living Indigenous or sacred motifs, modern equipment, knights, undead anatomy, or archival imagery.

The first result baked a checkerboard and was rejected as `refs/derived/imagegen_v8_attempt1_baked_checker.png`, SHA-256 `0513C79059FC02A590FB68417170DCA04F2DB89418F08CF499B7BCF9C167BDE9`. A targeted native-transparency edit produced RGBA; a deterministic alpha-only cleanup then changed alpha 1-15 to 0 and alpha 254 to 255 without changing RGB or semantic design.

- Final provider input: `refs/original/meshy_input.png`.
- Final SHA-256: `1483DCD005F218C2A625B0B18674A2B5E7918924F6DCFAA1A6F5B32720D0A804`.
- Dimensions/mode: 1024x1536 RGBA.
- Alpha min/max: 0/255.
- Pixels: 1,064,434 fully transparent; 508,430 nontransparent; 6,059 alpha 16-127; 492,212 alpha 128-253; 10,159 fully opaque; zero alpha 1-15 and zero alpha 254.
- Tight nontransparent bounds: x207-951, y10-1515, 745x1506.
- Alpha contact sheet: `validation/alpha_qa_v8/meshy_input_alpha_contact_sheet.png`, SHA-256 `184227FF9EBB1F8658902206FF261762CFF21F1003FAF861558666A6070FA713`.
- Source/refinement comparison: `refs/derived/source_to_refinement_v8.png`, SHA-256 `90411F2F3AD234E4DA48F1E903BB90FD41FF9F3334C59C873571498B0208332A`.
- Prompt/provenance: `refs/original/imagegen_prompt_v8.md` and `refs/original/input_manifest.json`.
- Parent approval: exact SHA-256 approved on 2026-08-24 after review of black, white, and checker composites; the parent explicitly confirmed the living/crazed identity, skull mask, body paint, bone trophies, harpoon silhouette, and clean separation.

## Provider attempt and cost

Live balance before the tranche: 25 credits. The submitted request used only the approved local PNG and specified `ai_model=meshy-7`, standard model, T-pose, triangle topology, 30,000 target polygons, provider remesh, saved pre-remesh model, textures, PBR, image enhancement, lighting removal, bottom origin, alpha/cardinal thumbnails, and GLB/FBX outputs. The texture prompt preserved the approved materials and prohibited modern gear, Indigenous/sacred motifs, armor, undead decay, extra weapons, base, scenery, and background.

Exact provider response: `Error: API request failed with status 402. Insufficient funds`.

- Task id: none.
- Response id: none.
- Balance after: 25 credits.
- Credits consumed: 0.
- Receipt: `provider/receipts/meshy_v8_402.json`.
- No retry was made because the parent explicitly required the 402 hard stop and forbade downgrade or substitution.

The live tool schedule implies a minimum 49-credit clean path for one exact Meshy 7 generation (20), one rig (5), and eight distinct animations (24), before any optional conversion/remesh or failure recovery. The current 25-credit balance does not cover the required lineage.

## Geometry, materials, rig, actions, and export

No accepted v8 geometry exists. Consequently no multi-view Blender QA, scale normalization, protected source/working checkpoint, geometry repair, triangulation audit, PBR-to-PDX DDS conversion, rig/weight audit, action import/cleanup, sound synchronization, `.mesh` export, eight `.anim` exports, or reimport verification was possible.

All older provider downloads, Blender checkpoints, textures, `.mesh`, and action reports in the package descend from rejected references. They remain historical evidence only and must not be promoted, copied, or runtime-wired.

Required actions blocked: `idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death`. No static, transform-only, locally authored, or semantically aliased replacement was created.

## Unit audio

Six legally sourced derived files exist at 44,100 Hz, mono, PCM signed 16-bit for selection, movement, idle vocal, weapon attack, weapon impact, and death. Their source pages, direct-download provenance, creators, licenses, original/derived checksums, and mechanical transformations are recorded in `evidence/audio_sources/source_manifest.json`, `evidence/audio_sources/ffprobe_and_hash_receipt.json`, and `audio/sound_design_handoff.md`.

The separately required training role is missing and is explicitly blocked; no existing sound was relabeled. Exact harpoon/spear timing and all action synchronization points are also blocked until the final provider actions exist. Parent-owned sound and soundeffect definitions were not edited.

## Existing bespoke counter handoff

The already-created green Island Reavers counter package was reused only as a handoff consumer and was not overwritten.

- Consumers: `GFX_unit_cannibal_island_reavers_icon_medium`, `GFX_unit_cannibal_island_reavers_icon_medium_white`, and `GFX_unit_cannibal_island_reavers_icon_small`.
- Installed-vanilla definition precedent: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx` lines represented in the audit.
- Installed-vanilla DDS precedents: `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`.
- Exact frame sizes, two-state behavior, green-palette evidence, final DDS hashes, and comparison/validation paths: `evidence/counter_audit.md`.
- Parent-owned GFX/runtime status: definitions and DDS consumers already exist; live consumer proof remains parent/user work.

## Files created or materially updated in v8

- `refs/original/meshy_input.png`.
- `refs/original/input_manifest.json`.
- `refs/original/imagegen_prompt_v8.md`.
- `refs/derived/imagegen_v8_attempt1_baked_checker.png`.
- `refs/derived/meshy_input_v8_pre_alpha_cleanup.png`.
- `refs/derived/source_to_refinement_v8.png`.
- `validation/alpha_qa_v8/*`.
- `provider/receipts/meshy_v8_402.json`.
- `evidence/dependency_and_route_audit_v8.md`.
- `job.yaml`, `history.jsonl`, `manifest.json`, `manifest.md`, `runtime/handoff.md`, and `audio/sound_design_handoff.md`.
- This handoff.

## Simplifications, omissions, and blockers

- Provider blocker: HTTP 402 before Meshy task creation despite a reported 25-credit balance.
- Model blocker: no accepted v8 geometry, remesh, rig, textures, Blender checkpoints, or scale evidence.
- Animation blocker: all eight required real Meshy skeletal actions are absent.
- Export blocker: no v8 `.mesh`, `.anim`, DDS, preview, or reimport artifacts.
- Audio blocker: training role missing; all exact action synchronization pending.
- Runtime blocker: all wiring and live validation remain parent-owned and were not attempted.
- No design simplification, model downgrade, fallback source, alternate provider, local replacement motion, counter overwrite, or unauthorized runtime edit was used.

No commit was created because the requested production package is incomplete and repository policy forbids committing a misleading half-finished package. Resume only after sufficient Meshy balance is available for the exact locked `meshy-7` lineage.
