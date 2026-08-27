# Event 012 Africa — Gorilla Heavy Infantry Meshy 7 redo handoff

Status: `blocked_live_provider_capability`. The exact colorized reference is parent-approved, but the 2026-08-27 live locked route still cannot produce or accept a gorilla/custom-nonhumanoid rig for `meshy_animate`. No paid Meshy call or in-game completion is claimed.

## Outcome

A better complete named Internet artwork was selected: Black Remnant's “Savage Brute Warlord.” It contains a complete armored ape/gorilla heavy fighter, full visible anatomy, and a readable two-handed heavy hammer. The user-authorized rights mode is `reference_only_user_authorized`; the inspected Etsy listing attributes Black Remnant as designer and NerdyMinis/Jared Olander as a licensed merchant, and no explicit NoAI or no-derivatives restriction was found.

The one faithful-cleanup ImageGen operation preserved the visible design but produced a baked checkerboard rather than native transparency. The one explicitly authorized background-only ImageGen edit also produced an opaque baked checkerboard. Both native outputs were rejected. The parent then authorized the verified plague-carrier `rembg 2.0.61` fallback and deterministic alpha remap. After the hard color gate, one dedicated palette-only ImageGen edit and the same verified alpha route produced the exact active input. The parent visually approved SHA-256 `b943b581bcd92237b645ae4fa26c092afd2ca1829c700c90ad5781d1aa7b634f`.

The current run verified the locked wrapper, tools schema, dependency stack, and bridge. Two consecutive and one concurrent-pair `tools/list` probes exposed exact `meshy-7` and left no surviving provider processes. A free balance probe returned 73 credits. Meshy 7 paid calls: `0`; credits consumed: `0`; provider task IDs and response IDs: none.

## Source lineage

- Source title: “Savage Brute Warlord.”
- Creator/designer: Black Remnant.
- Publisher/merchant: NerdyMinis / Jared Olander.
- Source page: https://www.etsy.com/listing/4347408691/savage-brute-warlord-30mm-32mm-sci-fi.
- Direct inspected render: https://i.etsystatic.com/57719897/r/il/187beb/7133724903/il_794xN.7133724903_l1so.jpg.
- Authorization: `reference_only_user_authorized`; no redistribution licence asserted.
- Transient source SHA-256: `45c3aff750f4e42abc25943cda110cf758ef8c461a046778c62652d8c205bc44`; 128,413 bytes; 794x794 JPEG.
- Source byte retention: the download is under `refs/source/transient/` only because safe deletion was blocked by the available file-operation policy. It is not approved archival evidence or provider input.
- Previous from-scratch candidate: rejected and preserved only at `refs/rejected/previous_from_scratch_meshy_input_50555a252651030f62062ad1a411e89c07423f546f79051e6f30f98e16b083df.png`.

## Cleanup lineage and review

| Attempt | Input | Output SHA-256 | Visual result | Alpha result | Decision |
|---|---|---|---|---|---|
| Faithful cleanup | Selected Black Remnant render | `191261f1add59cb10f4f682eb19d3ff60a14f2c0629c39a4ee1f176ae7999281` | Complete subject, hammer, pose, armor and grayscale resin design remained recognizable; scenery/logo removed. | 1254x1254 `Format24bppRgb`; all 1,572,516 pixels alpha 255. | Rejected: baked checkerboard. |
| Targeted transparency fallback | Rejected faithful cleanup | `e8c3c0ccd73bc1693bd85c51036515a361da3e5a54f47c6aae5742bf395427ca` | Subject remained visually faithful to attempt 1. | 1254x1254 `Format24bppRgb`; all 1,572,516 pixels alpha 255. | Rejected: baked checkerboard again. |

Prompt evidence is under `refs/briefs/`; source and alpha comparison evidence is `validation/source_cleanup_comparison_2026-08-24.md`. No further ImageGen operation is authorized or attempted.

The parent-authorized local fallback used faithful attempt 1 as input. `rembg 2.0.61` supplied the alpha mask, then alpha values were remapped deterministically (`<=128 -> 0`; `129..255 -> 2..255`). Final `refs/original/meshy_input.png` is 1254x1254 RGBA, 1,737,895 bytes, SHA-256 `8cf9cccd4d17c4e28be3a6ea01d7447bfbc9e20a14d690336b57b445a9c8d507`; decoded RGB is exactly unchanged. Alpha extrema are `0..255`, all four corners are zero, and visible bounds are `[77,35,1102,1191]`. Dark/light review `refs/derived/rembg_alpha_review.png` has SHA-256 `9c8aa638096241b086d28f6e4c64bd65c8c28b59b797f8384cdb2f4e4f7c5ab8`.

## Period-fit re-audit

The focused re-audit under commit `ad0d00305` passes with no exceptions. The skull pauldron, opposite shoulder plate, brow/crest guard, bracers and greaves read as stylized forged fantasy/alternate-history armor. The broad harness, wraps, belt and buckles read as hide/leather and conventional fasteners. The weapon reads as a carved-shaft, hooked-pommel heavy maul with passive rivets/bosses.

The requested audit baseline was `ad0d00305`; the shared worktree HEAD advanced to `1a1c1c94fef1f0f5ebcaf05529af6d04816f04c0` during the tranche. No shared-worktree checkout/reset was attempted. Exact source, grayscale predecessor, active color input and review hashes provide the audit lock.

No electronics, digital devices, advanced optics, obvious plastics, radios, powered joints, synthetic tactical webbing, MOLLE, firearm accessories, cables, motors, pistons, power cells or sci-fi machinery are visible. No periodization edit was required. The later palette-only ImageGen edit is recorded separately below and does not change the period-fit ruling. The exact final hash is parent-approved.

## Hard color gate

The parent prohibited monochrome Meshy inputs after the period-fit pass. The grayscale candidate was moved to rejected lineage. One native ImageGen edit applied only a restrained medieval/fantasy palette: charcoal-brown fur, aged iron/gunmetal, bone/ivory skull, dark worn leather, antique bronze/brass, and dark weathered hardwood. Visual comparison found no substantive redraw, re-pose, anatomy, hammer, armor, material-boundary, value-structure or framing drift, and the period-fit ruling remains unchanged.

The native color result baked its checkerboard, so the authorized `rembg 2.0.61` deterministic alpha fallback produced the active `refs/original/meshy_input.png`. Final SHA-256: `b943b581bcd92237b645ae4fa26c092afd2ca1829c700c90ad5781d1aa7b634f`; 1254x1254 RGBA; alpha `0..255`; four zero-alpha corners; binary-mask IoU `0.9899139659` against the grayscale candidate. Review image: `refs/derived/period_colorization_alpha_review.png`, SHA-256 `a308c4933fb21ea2c8009b6e749175e4644c6af863d50fb023ba933a812fceaf`.

Color gate status: `passed_parent_approved`. Parent approval covers the dedicated colorization, charcoal-brown fur/aged iron/bone/dark leather/antique bronze/weathered-hardwood palette, fantasy/alternate-history period fit, fidelity/no-substantive-drift comparison, and alpha/edge validation. Provider-input count remains zero because Meshy was not called.

## Downstream gates retained

- Profile remains `nonhumanoid_creature`.
- Firearm audit is explicitly zero: the hammer is non-firearm melee equipment, and the package has no firing states, discharge effects/lights, muzzle locator, or firing sound requirement.
- Installed-vanilla `refs/vanilla/asian_infantry.mesh` source height remains `7.516803`. The exact installed entity precedent is `asian_gfx_infantry_entity` at scale `0.8`, effective height `6.0134424`. Intended custom exported/effective runtime height remains `10.147684`, custom entity scale `1.0` applied once, custom/source ratio `1.35`, and custom/installed-effective ratio `1.6875`. Full provider-geometry width/depth/contact remeasurement is blocked because no compliant provider geometry exists.
- The live Meshy rig schema exposes only `input_task_id`/`model_url` plus height, texture, and response fields. It has no creature family, gorilla skeleton, custom bone map, or Blender-rig import, while `meshy_animate` requires a Meshy `rig_task_id` and integer action ID. A local dedicated creature rig cannot be forced through the humanoid route or substituted for provider/professional source motion.
- No professional animation source is user-approved.
- `chaosx_gorilla_idle`, `chaosx_gorilla_move`, `chaosx_gorilla_attack`, `chaosx_gorilla_recovery`, and `chaosx_gorilla_death` remain blocked with no compliant source task/action IDs.
- Audio remains source-verified but runtime-blocked by inherited `pcm_f32le` derivatives and absent compliant action synchronization.
- Counter evidence remains `needs_user_review` because the inherited icon package used a chroma-key-first route rather than the current native-alpha-first contract.

## Files created or changed in this tranche

- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/job.yaml`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/manifest.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/history.jsonl`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/source/source_search.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/source/provenance.json`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/original/input_manifest.json`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/briefs/faithful_cleanup_prompt_2026-08-24.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/briefs/targeted_transparency_prompt_2026-08-24.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/derived/faithful_cleanup_processing.json`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/derived/rembg_alpha_candidate.png`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/derived/rembg_alpha_review.png`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/original/meshy_input.png`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/briefs/period_colorization_prompt_2026-08-24.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/derived/period_colorization_imagegen.png`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/derived/period_colorization_alpha_candidate.png`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/derived/period_colorization_alpha_review.png`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/rejected/previous_grayscale_meshy_input_8cf9cccd4d17c4e28be3a6ea01d7447bfbc9e20a14d690336b57b445a9c8d507.png`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/validation/source_cleanup_comparison_2026-08-24.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/rejected/previous_from_scratch_meshy_input_50555a252651030f62062ad1a411e89c07423f546f79051e6f30f98e16b083df.png`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/rejected/failed_faithful_cleanup_fake_checkerboard_191261f1add59cb10f4f682eb19d3ff60a14f2c0629c39a4ee1f176ae7999281.png`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/rejected/failed_targeted_transparency_e8c3c0ccd73bc1693bd85c51036515a361da3e5a54f47c6aae5742bf395427ca.png`
- This handoff.

The 2026-08-27 blocker pass changed `job.yaml`, `manifest.md`, `history.jsonl`, `runtime/handoff.md`, `evidence/dependency_verification.md`, `validation/source_gate_and_action_feasibility.md`, and this handoff. The repository verifier also refreshed the shared diagnostic `.tools/3d_pipeline/reports/environment_report.json`; it was not included in this handoff commit. The pass did not alter the approved reference, provider artifacts, Blender artifacts, inherited audio binaries, counter art, or runtime/gameplay/GFX/entity/sound/localisation files.

Transient research downloads remain under `refs/source/transient/` and are explicitly excluded from approved archival and provider-input lineage.

No runtime/gameplay/GFX/entity/sound-definition/localisation/spreadsheet file, model export, action export, audio binary, or counter art was intentionally changed in this tranche. Existing unrelated workspace edits were preserved.

## Parent decisions and remaining work

1. Keep both opaque cleanup outputs and the grayscale predecessor rejected; only the parent-approved exact color hash may be used as provider input.
2. Resume only when a verified provider can produce a gorilla-compatible rig accepted by `meshy_animate`, or the user explicitly approves a professional gorilla source covering idle, move, hammer attack, recovery, and articulated death.
3. After that route exists, submit only the approved exact image, select geometry only after multi-view QA, measure the complete non-collision geometry crosswalk, and then perform action/export/reimport work.

The only accepted fallback remains the parent-authorized verified `rembg 2.0.61` alpha extraction. No design simplification was accepted. Audio remains source-verified but runtime-blocked pending compliant signed-16-bit derivatives and accepted action timing. Counters remain `needs_user_review` because the inherited chroma-key-first package has not been accepted or replaced by a native-alpha icon-artist package. The model package is incomplete and blocked, with zero paid calls.

## 2026-08-27 evidence-file checksums

- `job.yaml`: `3d2a07bfe2a5dac58e6e9c5b0617dd3905b473691b86644acb0c3c0c89bac394`.
- `manifest.md`: `7322daf8a9e2ade208756e74b9e07fc1852137aa775916005f443f77fd664725`.
- `history.jsonl`: `f0b80bfeca81295987e5f57e8875994d13b252ad04bd395d816f774b35053917`.
- `runtime/handoff.md`: `5de385e390a78c5f3e8d5f93dcbc3d3f042381c8dac7e42c9c2142d7f048f39e`.
- `evidence/dependency_verification.md`: `6a74dcdd7c983a922e7416a8dc546be467925b9512f3b78c55e0403754691eb5`.
- `validation/source_gate_and_action_feasibility.md`: `ed26d08e625692bbfaa9e87a2e64267a1a009e9b382eb164f5db4223a2c25866`.
