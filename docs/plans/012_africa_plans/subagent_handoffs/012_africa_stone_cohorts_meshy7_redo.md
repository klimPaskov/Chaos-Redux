# Event 012 Stone Cohorts Meshy 7 redo handoff

Status: `blocked_provider_schema_capability_and_insufficient_balance`. Across the historical and current attempts, Stone Cohorts has `5` provider request attempts, `4` confirmed paid tasks, and `70` confirmed consumed credits. The latest observed shared-account balance is `13`.

## Current-standard reattempt — 2026-08-27

The mandatory `MESHY_API_KEY` gate passed before repository or job intake; the secret was not recorded. The repository lock, live route, and installed stack verified official `@meshy-ai/meshy-mcp-server` `0.4.0` with exact `meshy-7`, Blender HOI4 adapter `1.10.14`, Blender `5.1.2`, and checksum-locked `io_pdx_mesh` `0.91.0`. Adapter health request `fbc3eccd9f3f47829dd9829d1d65c1c0` passed for `stone_cohorts`, and `127.0.0.1:9876` was independently listening.

The approved input remained exactly `docs/assets/012_africa/models_3d/stone_cohorts/refs/original/meshy_input.png`, SHA-256 `79ec9e39148d734468e20171391c7068704a877c014562cd85b1a1afacc19ccb`, 1013x1552 RGBA. `legacy_identity_guidance.png` was not submitted. The current request was materially different from the four historical calls: Meshy 7 `lowpoly` model mode, inline quad remeshing, image enhancement enabled, no forced pose, PBR/textures enabled, and the locked 25,000-polygon target. Its purpose was to reduce fragmented hard-surface boundaries while preserving the integrated polearm.

The live provider rejected the declared enum with `Invalid request. model_type: lowpoly is not supported for meshy-7`. No task id, response id, thumbnail, model, texture, or downloadable artifact was returned. This exposes a live declaration/provider capability mismatch because `model_type = lowpoly` is present in the locked/live MCP schema but is not accepted by Meshy 7.

The shared-account balance was `73` immediately before the request and `43` immediately after the rejection, then `13` on a later free probe. Multiple sibling 3D workers were using the same account concurrently. Without a task id, neither 30-credit delta can be attributed to Stone Cohorts; current-run confirmed consumption is `0`. Historical confirmed consumption remains `70` credits from generation task `01a0350a-043e-70b0-bc02-6bcd1a726803`, remesh tasks `01a03511-ffc5-7cca-875b-6a6ece7f535c` and `01a03517-e20c-76e4-89ad-da6bd7e8303b`, and T-pose generation `01a0351e-c350-74ce-ac5f-4a1d158a87ee`.

Paid work stopped because `13` credits cannot fund another 30-credit geometry generation, and even the immediate post-rejection `43` could not fund a new generation plus the minimum downstream 17-credit tranche: 5-credit humanoid rig and four distinct paid custom actions for idle, attack, collapse/recovery, and death. Move could only be accepted from a verified rig-included locomotion source. No rejected historical candidate was promoted or sent to rigging.

Consequently, current-run geometry, material, rig, weights, five actions, `.mesh`, `.anim`, export, reimport, and source-to-runtime synchronization are all `blocked`. Historical Meshy 6 and locally authored action/export files remain immutable evidence only and are not accepted runtime candidates.

## Outcome

The restarted source tranche found one complete eligible reference: FromSoftware's *Guardian Golem (Halberd)*, used under the parent's explicit `reference_only_user_authorized` permission. It passes the core identity gate: a complete monumental articulated humanoid stone guardian with a readable full-length polearm. The source may establish its own fine design details under the parent's clarification.

The initial native ImageGen faithful-cleanup call and targeted transparency repair were rejected because both returned 1013x1552 `rgb24` PNGs with baked checkerboards. The parent then authorized the verified local fallback. `rembg` 2.0.61 / `u2net` supplied alpha to the last subject-faithful repair, followed by the deterministic remap `alpha <= 128 -> 0; 129..255 -> 2..255`. RGB/geometry remained byte-identical. The RGBA result passed alpha, silhouette, polearm, bbox, matte/halo, internal-gap and contrast/checker review and was promoted to `refs/original/meshy_input.png` for parent comparison.

The new period gate also passes. The source is an ancient/medieval-fantasy carved stone-and-metal guardian without electronics, digital devices, advanced optics, plastics, tactical gear, or sci-fi machinery. No periodizing redesign was needed or applied.

Parent visual review approved `refs/original/meshy_input.png` at exact SHA-256 `79ec9e39148d734468e20171391c7068704a877c014562cd85b1a1afacc19ccb`. Colour, period, fidelity, and alpha gates are approved for this immutable hash only. Any byte change invalidates approval and requires another comparison. These exact bytes were submitted twice under the documented no-pose and T-pose provider variants.

Meshy 7 generation task `01a0350a-043e-70b0-bc02-6bcd1a726803` succeeded. Balance reconciled from 395 to 365. The textured/PBR candidate was downloaded immediately as GLB and FBX with immutable hashes and four source PBR maps.

The dependency drift was reconciled before resumed mutation: lock and live adapter both report `1.10.10`; Blender is `5.1.2`; checksum-locked io_pdx_mesh `0.91.0` is loaded.

The no-pose generation preserves the guardian, full double-ended polearm, static right-hand grip feasibility, UVs, and complete provider PBR maps, but strict adapter repair leaves `114` loose boundary edges across `27` components. Official remesh recovery 1 leaves `115` loose boundary edges across `28` components. Official remesh recovery 2, sourced from the generation task's pre-remeshed artifact, improves this only to `103` loose boundary edges across `26` components and loses usable material bindings. All cap attempts roll back rather than introduce non-manifold geometry.

The one authorized non-identical T-pose Meshy 7 generation returns UVs and complete PBR maps/bindings, but multi-view inspection shows that it entirely deletes the defining polearm, replaces the hand/forearm silhouettes with pointed extensions, and leaves `273` loose boundary edges across `65` components. The provider-capability matrix is therefore closed: no candidate passes guardian identity, complete polearm and contact feasibility, clean/repairable topology, UV, and material gates together. Rig, animation, conversion, PDX export, and reimport spend remain zero.

## Source and provenance evidence

- Search and rejection ledger: `docs/assets/012_africa/models_3d/stone_cohorts/refs/source/source_search.md`.
- Machine-readable provenance: `docs/assets/012_africa/models_3d/stone_cohorts/refs/source/provenance.json`.
- Selected source: FromSoftware / Bandai Namco, *ER Golem w Halberd.jpg / Guardian Golem (Halberd)*.
- File page: https://eldenring.wiki.gg/wiki/File:ER_Golem_w_Halberd.jpg
- Context page: https://eldenring.wiki.gg/wiki/Guardian_Golem
- Terms/authorization: copyrighted game art marked `Fairuse` on Eldenpedia; explicit parent authorization for `reference_only_user_authorized` visual-reference cleanup; no explicit NoAI term found on the inspected page.
- Transient fingerprint: SHA-256 `c3ebde674062fed399dbcc7fab27965d9b1c2125544164802d027fd22d180833`; MediaWiki SHA-1 `516e255cdd78ac95eb62f6149f2fba197dd9ceb9`; 941x1441 JPEG; 184,339 bytes.
- Archive decision: source bytes discarded after comparison because the file is fair-use/reference-only; URLs and fingerprints are retained.
- Cleanup prompt: `refs/briefs/faithful_cleanup_prompt.md`.
- Comparison review: `refs/source/source_to_cleanup_review.md`.
- Cleanup output fingerprint: SHA-256 `a9df981b3b091b7d99a1c4e8e655e5b72eb19076270f2c1ea570a9fd1526cf3b`; 1013x1552 `rgb24`; no alpha; rejected and not archived into the job.
- Targeted transparency-repair fingerprint: SHA-256 `89ebea112f031376dccb8e920e654abd06500ee581e20642d48d56ad17d459b6`; 1013x1552 `rgb24`; no alpha; rejected and not archived into the job.
- Archived earlier candidate: `refs/source/candidates/luigi_castellani_spears_of_the_dawn.zip`, 74,517,411 bytes, SHA-256 `812be59a1697041ae531faba3f6a59df611cbf0b9c7fc3049078fcabf560e595`.
- Source page: https://opengameart.org/content/african-inspired-art-by-luigi-castellani-spears-of-the-dawn
- Direct archive URL: https://opengameart.org/sites/default/files/LuigiCastellani.zip
- Creator/publisher: Luigi Castellani / Sine Nomine Publishing.
- Rights: public domain / CC0 according to the publisher statement reproduced by OpenGameArt; attribution requested as a courtesy; no NoAI term was found.
- Closest inspected plate: `LuigiCastellani_ADVENTURESPLASH.tif`, 2468x3509 grayscale, SHA-256 `c05998c04a5c0e74c4f9e759f9f8a44d7336bf50bb4063095c57a08f2bded1e2`.
- Disposition: rejected for identity/fidelity and unusable isolation.
- Legacy identity guide: `refs/original/legacy_identity_guidance.png`, SHA-256 `9a03a8057e8a11bafa3642b707636825f3c3ee104b68f0b4275837cb3ac0b4b0`; provider eligibility `false`.
- Final approved input: `refs/original/meshy_input.png`, SHA-256 `79ec9e39148d734468e20171391c7068704a877c014562cd85b1a1afacc19ccb`, 1013x1552 RGBA; status `reference_approved`; submitted provider input count: `2`, both using the exact immutable bytes under distinct pose settings.
- Processing evidence: `refs/processed/processing.md`, `refs/evidence/rembg_processing_metrics.json`, `refs/evidence/rembg_alpha_mask.png`, and `refs/evidence/rembg_contrast_checker_review.png`.

Other recorded rejections include Derek Bentley's *Highguard - Summit - Golem Army* (weapon separate in orthographic art; critical crops in scene renders), rights-clean but identity-incompatible OpenGameArt golems, a weapon-only game-wiki page with insufficient underlying image rights, an all-rights-reserved DeviantArt design, and a CC BY-NC-ND design that cannot undergo the required isolation edit. An interrupted substantially-original ImageGen candidate was also rejected for redesign and absent alpha and was never copied into the job.

## Profile, vanilla calibration, and rig assessment

- Proposed profile: `humanoid_unit` / humanoid mechanical guardian, not the legacy `nonhumanoid_creature` route.
- Entity/runtime stem: `chaosx_stone_cohorts`.
- Installed vanilla reference: `docs/assets/012_africa/models_3d/stone_cohorts/refs/vanilla/asian_infantry.mesh`.
- Recorded source height: `7.516803`.
- Locked target/effective runtime height: `11.275205`.
- Entity scale: `1.0` once.
- Geometry ceiling: `25,000` triangles; model textures at most `1024`; `30` FPS.

The identity guide has a conventional two-arm/two-leg skeleton and visibly separated principal joints, so the standard provider humanoid rig is plausible only as a candidate. Acceptance cannot be inferred: the returned rig must keep rigid stone armour from bending, place pivots at the mechanical joints, retain the integrated polearm, and maintain hand/weapon contact across all actions. No local replacement rig or motion is authorized.

## Required action route

Required distinct roles remain:

- `chaosx_stone_idle`
- `chaosx_stone_move`
- `chaosx_stone_attack`
- `chaosx_stone_collapse_recovery`
- `chaosx_stone_death`

The locked repository schema records verified Meshy action IDs only for idle `0`, attack `4`, and death `8`. It does not establish distinct approved move or collapse/recovery IDs. The existing package actions were locally authored in Blender and are invalid under the current motion-source gate. No alias, transform-only clip, or local replacement is accepted. With provider calls paused and no explicitly approved professional source, every redo `.anim` remains blocked.

## Provider and credit lineage

- Meshy 7 image-to-3D task: `01a0350a-043e-70b0-bc02-6bcd1a726803`, succeeded.
- Generation GLB: `provider/downloads/generation_1/stone_cohorts_meshy7.glb`, SHA-256 `c4698f98a09405ef8f9eb8c2650553bf39f0c1c988286772744066baf3a0097b`.
- Generation FBX: `provider/downloads/generation_1/stone_cohorts_meshy7.fbx`, SHA-256 `3d78a452dfff887cfe77d2c568a43b6a703f83d926bc3b9b4aff95dce2e1f049`.
- Official remesh recovery 1: `01a03511-ffc5-7cca-875b-6a6ece7f535c`, `5` credits, rejected for `115` loose boundary edges across `28` components.
- Official remesh recovery 2: `01a03517-e20c-76e4-89ad-da6bd7e8303b`, `5` credits, rejected for `103` loose boundary edges across `26` components and absent usable material bindings. GLB SHA-256 `8fa424b177f597f8bf0419b98a640dae4661d6e6a882a88c49bec14d91872bda`; FBX SHA-256 `f3e8437f926cf80c7f6ec652a065043e7947b1c50fd9cb832c58a14c9e8b2f18`.
- T-pose capability-matrix generation: `01a0351e-c350-74ce-ac5f-4a1d158a87ee`, `30` credits, rejected for missing polearm/contact identity and `273` loose boundary edges across `65` components. GLB SHA-256 `4ffbbca6c2fd3fac1c8f20cbf95162e6bb30aa9036e2cc78ddff05c23c260e13`; FBX SHA-256 `28659d34d1b68ffbe9affd22548bcd2dd0e62c1658ec19da990706e14da997ac`.
- Retexture/rig/convert tasks: none.
- Meshy animation tasks: none.
- Paid calls: `4` (`30` generation 1 + `5` remesh recovery 1 + `5` remesh recovery 2 + `30` T-pose generation 2).
- Credits consumed: `70`.
- Balance: `395` initially, `365` after generation 1, `360` after remesh recovery 1, `355` after remesh recovery 2, and `325` after generation 2; every tranche reconciled exactly.
- Rig status: not submitted because every candidate fails at least one mandatory pre-rig geometry/identity/material gate.
- Rig, animation, conversion, and export paid calls: `0`.
- The historical Meshy 6 task and its downloads remain preserved in the job root but are not redo outputs.

## Audio revalidation

Approved originals remain unchanged:

- `audio/source/quern_stones.ogg`, Work With Sounds / recordist Monika Widzicka, CC BY 4.0, SHA-256 `2b281cec5a193a20e7c969d7cd79b990cd920822a2685087cd2ce18bf20557d7`. Source: https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg
- `audio/source/metal_clanging.ogg`, Camshaft64, CC BY-SA 4.0, SHA-256 `b3f1a16f5dda28d20c8b16689050647478812d92ee3c06a66ec4a425a85bb408`. Source: https://commons.wikimedia.org/wiki/File:Metal_Clanging_Noises.ogg

The six retained derivatives were mechanically converted from PCM 32-bit float to the installed-precedent format `pcm_s16le`, 44,100 Hz, mono, 16-bit, with metadata removed. Current FFprobe and hash evidence is `audio/evidence/ffprobe_revalidation_2026-08-27.json`.

| Role | Derived file SHA-256 | Status |
|---|---|---|
| select | `f31f41c0d58a037387ea73e17a9ba7a8d24b66963457523da0baffd837d2eaf0` | exact unit-selection consumer blocked |
| idle | `d18fb5226e6aecc5f5633376069dac7c518ed603409035405fe59905e9c0caad` | resync after accepted provider action |
| move | `dcd1815b6d900e47e2bd574aed3438000f497c70342bd9be2949ca49211d2345` | resync after accepted provider action |
| attack | `102b77c251e5056458d5e062a6734a43c1981976f1458f50f1e55912b85326cf` | resync to accepted contact/recoil phases |
| collapse/recovery | `4b76b3c3342c17fd286d9c67c0c671c3aa81fe334456d2000ec54afd2709421e` | resync after distinct provider action |
| death | `2c28148dc2bd58125fda0e2b3f594fb33cbe50a1153d20227e84ddb94e2fbe13` | resync to accepted impact/settling phases |

The installed land-unit selection surface resolves the global `select_army` soundeffect in `sound/soundeffects.asset`; no per-subunit selection hook was found in the inspected unit/entity consumer. The earlier formation-creation cue is not actual selection-consumer evidence. Proposed IDs remain `chaosx_stone_cohorts_<role>_sound` and `chaosx_stone_cohorts_<role>_sfx`, but the mandatory selection role remains blocked unless the parent proves a real per-unit binding.

The unit is explicitly `non_firing`. Its polearm is melee. Firing states, muzzle/discharge locators, muzzle particles, discharge lights, firearm sounds, cartridges, projectiles, and beam effects are all zero; the sourced attack/impact cue must synchronize only to a future accepted polearm-contact phase.

## Counter revalidation

Authoritative 2026-08-27 replacement status: `needs_user_review`. The bounded `chaosx_icon_artist` route produced four original native-alpha polearm-bearing sources, frame-aware processed strips, final DDS files, decoded round trips, and a comparison contact sheet. Package-owner visual review found the defining polearm readable in both large and on-map families; parent aesthetic promotion and GFX/runtime wiring remain pending.

- `counters/dds/unit_stone_cohorts_icon.dds`: 152x42, two 76x42 frames, SHA-256 `28bdd9654cb095f3f555f4f4dd11aaf9f3f97ab8b46bd588d8bbb9506821be63`.
- `counters/dds/onmap_unit_stone_cohorts_icon.dds`: 60x12, two 30x12 frames, SHA-256 `c583c4b23a1c02906b5ffecafd936a5cd169946fd0d798519dc0409d62fa0ee6`.
- `counters/contact_sheet.png`: SHA-256 `b9af42541079a8b1e51d828f2a43524eb47b42cb66301ecbb4f9407ed6386aca`.
- `counters/validation.json` confirms uncompressed BGRA8 DDS headers, alpha 0-255, exact canvases/frame bounds, and pixel-identical decoded round trips.

The historical blocked counter assessment below describes the superseded inherited chroma-key package and is retained only as lineage.

Exact consumers and tokens:

- `unit_stone_cohorts_icon`: 152x42 strip, two 76x42 frames.
- `onmap_unit_stone_cohorts_icon`: 60x12 strip, two 30x12 frames.

Installed references still match:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, `GFX_unit_infantry_icon_medium`, `noOfFrames = 2`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds`, SHA-256 `b33a8e3b69cc789eb0e31ba99f4e5ba4e5b0a8b51ec1a7a7f709c3516f720c23`.
- The same definition file, `GFX_unit_infantry_icon_medium_white`, `noOfFrames = 2`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`, SHA-256 `58ab78662c2a64a519b8d5d144582e7b2785915bd0a0a822696d87a9de6f766c`.
- Skill-local families: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `units/land/map_counters/`, including their contact sheets.
- Recorded large-counter green: dominant RGB `(73,106,73)`, range `(20,34,21)` through `(154,175,147)`.

Packaged DDS hashes still match their manifest:

- `counters/dds/unit_stone_cohorts_icon.dds`: `93312189d4c19f15e32aa5e1de81c2f20c3450b992cf596afc769fd6c50b5718`.
- `counters/dds/onmap_unit_stone_cohorts_icon.dds`: `fb5b72cf6a56b2f8531a6ae1243d7bf1b17aa7f68a01df3e88d47f9c61f9adb7`.

Technical dimensions, frames, DDS headers, alpha, references, and hashes pass. Visual identity does not: the current counter shows a shield-bearing knight and omits the defining polearm. It is blocked from promotion. Required follow-up is a bounded `chaosx_icon_artist` redo using native transparent ImageGen, the same two consumer families, the sampled palette, original source PNG, processed PNG, DDS round-trip, contact sheet, manifest, and GFX handoff. This worker authored no 2D replacement.

## Files changed or created

Only the model job root and this handoff were changed. Material changes include:

- `job.yaml`, `manifest.md`, and `history.jsonl` updated to the `needs_parent_review` source-gate state. The pre-existing `runtime/handoff.md` remains parent-owned and was not changed in this fallback tranche.
- `refs/source/source_search.md` and `refs/source/provenance.json` created; the Castellani candidate archive and inspection derivatives were preserved under `refs/source/candidates/`.
- `refs/original/legacy_identity_guidance.png` preserves the prior identity guide; `refs/original/meshy_input.png` and `refs/original/input_manifest.json` now contain the single unsubmitted RGBA review candidate.
- `refs/processed/rembg_alpha_candidate.png`, `refs/processed/processing.md`, and `refs/evidence/rembg_*` preserve the deterministic alpha processing and review evidence.
- Six `audio/derived/*.wav` files mechanically converted to signed 16-bit PCM; `audio/manifest.md`, `audio/handoff.md`, and FFprobe evidence updated.
- `counters/manifest.md`, `counters/manifest.json`, `counters/gfx_handoff.md`, and `counters/validation.json` updated for the native-alpha polearm-bearing replacement and `needs_user_review` status.

No gameplay, event, focus, decision, localisation, GUI, GFX, entity, `.asset`, sound-definition, on-action, history, AI, spreadsheet, or active runtime file was edited.

## Meaningful validation

- Visually inspected the legacy identity guide and the rights-clean source archive candidates.
- Re-audited the selected Guardian Golem against the 1936–45-era period gate; no forbidden modern or sci-fi technology is present.
- FFprobe confirmed the promoted candidate is 1013x1552 `rgba`; all four corners are zero-alpha and its nonzero-alpha bbox is `[135, 20, 933, 1531)`.
- Confirmed output RGB bytes are identical to the last subject-faithful ImageGen candidate; the guardian and full polearm form one connected alpha component.
- Reviewed the result over checker, black, white, and magenta backgrounds for matte/halo, clipping, cast-shadow remnants, internal gaps, and full silhouette.
- Recomputed the archived source, original audio, derived audio, packaged counter, and installed vanilla counter hashes.
- FFprobe confirmed all six derived WAVs are `pcm_s16le`, 44,100 Hz, mono, 16-bit.
- Rechecked installed `subuniticons.gfx` consumer rows and their two-frame DDS paths.
- Visually inspected the counter contact sheet and identified the polearm identity mismatch.
- Used adapter `1.10.10` with Blender `5.1.2` and io_pdx_mesh `0.91.0` to inspect all provider candidates against the calibrated vanilla infantry source.
- Reviewed front, left/right, rear, three-quarter, top, and underside previews for guardian identity, complete polearm, grip/contact feasibility, scale, and grounding.
- Confirmed generation 1 and remesh recovery 1 preserve identity, polearm, UV and PBR maps but retain `114`/`115` loose boundary edges; recovery 2 retains identity/polearm but has `103` loose boundary edges and no material bindings; T-pose generation 2 has UV/PBR bindings but omits the polearm and has `273` loose boundary edges.

Skipped: rigging, animation, final PDX texture packing, conversion, `.mesh`/`.anim` export, reimport, source-to-runtime action synchronization, and live/in-game validation. These were correctly gated off because no provider candidate passed identity, polearm/contact, topology, UV, and materials together.

## Required parent decisions and remaining work

1. Do not repeat the evaluated no-pose/remesh/T-pose variants. Resume only after a newly approved provider capability or parent-approved materially different source/reference strategy can preserve the long polearm in a riggable pose and return closed or bounded-repairable textured geometry.
2. After a future geometry candidate passes, test the provider humanoid rig for rigid stone pivots and continuous weapon contact before any animation spend.
3. Establish distinct provider action IDs or explicitly approved professional sources for move and collapse/recovery in addition to idle, attack, and death.
4. Resynchronize the preserved sourced audio package to accepted actions and solve the exact selection consumer.
5. Review the completed polearm-bearing large/on-map counter package, then promote its two DDS files and wire the parent-owned GFX consumers if accepted.
6. Parent retains all runtime/GFX/entity/sound-definition wiring and live/in-game validation.

No unapproved fallback or simplification was used. The documented local alpha fallback and provider recovery calls were explicitly authorized, and no rejected output was promoted.
