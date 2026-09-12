# Clone Infantry weapon-free-body repair closure

Disposition: `implemented` for the physical model, source/rig/action/export/reimport evidence and parent runtime payload promotion.
Overall asset status: `needs_user_review` for companion audio acceptance, firing effects/audio synchronization and live consumer evidence.
This does not claim in-game completion.

The deterministic job is `docs/assets/shared_clone_system/models_3d/clone_infantry/` (paths below use this root unless they begin with an engine-facing directory or `.tools/`).
The current source of truth is `runtime/selected_package.json`; the parent-approved physical payloads are in `export/20260912_selected/`.
The parent copied all sixteen selected files into `gfx/models/units/clone_infantry/` and installed eight exact meshsettings in `gfx/entities/clone_infantry.gfx`.
The worker independently verified every destination hash and each stream/material mapping in `evidence/closure_20260912/parent_runtime_promotion.json`.
The parent also removed the obsolete pending-contact comment in `gfx/models/units/clone_infantry/animation_clone_infantry.asset`.

## Accepted scope, source and cost

The explicit parent task retained the existing fresh weapon-free Meshy 7 body and separate Blender-modeled rifle; neither was regenerated.
The clone remains a neutral period-compatible soldier with helmet, uniform, harness/pouches, puttees, boots, complete arms/hands, and a wood/steel bolt-action rifle with sights, trigger, bolt and sling.
The body task `01a07650-77c9-7244-ad86-b0434c78452c` consumed 30 historical task-attributable credits; this resumed closure made zero provider calls and consumed zero credits.
Historical shared-account balance movement is not attributed to this job beyond the task receipt.
The source is explicitly authorized existing native ImageGen artwork, so no Internet artwork URL or new source substitution is claimed.
Its title is “Generic purpose-grown period-compatible clone infantryman”; creator is native ImageGen under recorded user authorization.
Original source SHA-256 is `adfe9bf039975e6048daf64d06c2aa45562adbb96c1074330d04bb3293db5981`; prepared weapon-free source SHA-256 is `1941ab6df4b4422d92fbdee69dc81da965d5127b14756f7ac5c34a0f7ba3b4c9`.
The exact source-preparation prompt, native response IDs, identity comparison, 2026-09-06 parent approval, source status and failed-native-alpha/removal fallback are preserved in `attempts/20260906_weaponfree_blender/input_manifest.json` and `attempts/20260906_weaponfree_blender/alpha_fallback.json`.
Both images remain non-shipping evidence.
The downloaded immutable body GLB SHA-256 is `bd9322faa168b217b141ebd5462e255e268528ba65485c9641a6d1d391e626de`.
The source-informed rifle reconstruction and generated wood/steel material atlas are separately documented in the attempt's `component_design.md`, `components/geometry_design_report.json` and `component_texture_manifest.json`.
The parent's explicit Blender-rifle repair scope takes precedence over later generic workflow language proposing separate gun provider generation.

## Physical result and meaningful validation

The final assembly contains 29,742 triangles, 14,852 position-welded vertices, 31,181 exported vertex records, five rigid/deforming mesh objects and 44 bones.
The repaired body accounts for 29,142 triangles, including thirteen bounded clothing-cap triangles; the separately controllable rifle accounts for 600 triangles.
Every deforming vertex is weighted, every skin sum is normalized, body influences are at most four, and every rifle vertex retains one rigid weight of 1.0 after reimport.
The wood, steel and sling follow `RifleControl`; the bolt follows `RifleBolt`.
No real boundary/non-manifold/degenerate topology remains in the required adapter position-welded diagnostic; raw UV/normal/material seam splits are retained and explained.
Maximum stream size is 8,846 vertices and 24,000 triangle indices, within the calibrated export budget.
All transforms, normals, UVs and six DDS payload/header/channel contracts passed the native/source checks.

The named installed vanilla mesh `gfx/models/units/western_european_infantry.mesh`, measured object `polySurface106` excluding collision geometry, supplies source height `7.3518242835`.
Installed `gfx/entities/units_infantry.asset#infantry_entity` supplies the one entity scale `0.8`, yielding runtime height `5.8814594268`.
Axes are +Z up/-Y forward; animation remains in-place in world XY, with explicit skeletal vertical ground correction.
No arbitrary meter-height or repeated location scaling was used.

All nine distinct authored roles were exported and reimported from actual `.mesh`/`.anim` bytes.
The 489-frame audit found worst absolute ground error `0.0000045015476644` source units.
Native all-frame wrist IK target error is at most `0.000249023276813`; palm/grip and shoulder/stock suitability were reviewed visually, not mislabeled as numeric surface-distance measurements.
All five loops have identical decoded endpoints and distinct quarter/middle/three-quarter poses.
Attack, defend and support attack retain independent aim/discharge/recoil/bolt/recovery evidence.
Death V6 retains the parent-accepted collapse/impact/settling choreography with fourteen exact surface vertices across seven support regions and 521 source vertices near the floor.
Support V4 fixes the prior ground penetration; all 73 source/reimport bounds agree within `0.0000064373016358`.
The worker and parent reviewed `evidence/closure_20260912/firing_actual_byte_contact_sheet.png` and `nonfiring_actual_byte_contact_sheet.png`; parent acceptance covers silhouette, grip/attachment, distinct roles and settled death without visible gross deformation or floating in sampled views.
No accepted skeleton or death pose was changed during closure.

Current editable checkpoint: `attempts/20260906_weaponfree_blender/working_pbr/blender/checkpoints/clone_weaponfree_support_attack_v4.blend`, SHA-256 `966f65d66b97f04aa38ee8dd39aeac7a0bc6050aac3e085440bc9cb1c5ba80e6`.
The per-role export source/checkpoint hashes, authoring specs, native receipts, request IDs, all-frame results and reimport proof hashes are in `runtime/selected_package.json` and `evidence/closure_20260912/model_validation.json`.

| Role | Selected action | Frames at 24 FPS | Loop |
|---|---|---|---|
| idle | `clone_weaponfree_idle_v3` | 1-49 | yes |
| move | `clone_weaponfree_move_v3` | 1-25 | yes |
| attack | `clone_weaponfree_attack_v3` | 1-61 | no |
| defend | `clone_weaponfree_defend_v3` | 1-73 | yes |
| support_attack | `clone_weaponfree_support_attack_v4` | 1-73 | no |
| retreat | `clone_weaponfree_retreat_v4` | 1-25 | yes |
| training | `clone_weaponfree_training_v4` | 1-73 | yes |
| wounded | `clone_weaponfree_wounded_v3` | 1-49 | no |
| death | `clone_weaponfree_death_v6` | 1-61 | no |

## Exact physical payload hashes

All rows below have equal selected-source, staged and observed runtime SHA-256 values.
Every runtime destination is `gfx/models/units/clone_infantry/<basename>`.
The worker made no runtime writes; `/root` performed the copies.

| Basename | SHA-256 |
|---|---|
| `clone_infantry.mesh` | `810e83f81c29c5833cb68dcbf04cf587d25a6c5fc0afd34a0fa47e33e70334b6` |
| `clone_infantry_idle.anim` | `340e9cfe03705a722ed4e80ba8476ba8c17322d7427ba25e962b0ae677fc069f` |
| `clone_infantry_move.anim` | `e7c344069af6ee39a84b4a93d156661234c073a5a6fb17fd414190380d1e5019` |
| `clone_infantry_attack.anim` | `6cb11c8141a9e8b5ac976fe7d1cf124b9d131be9aa1bf6fc28ff8e24046ff33b` |
| `clone_infantry_defend.anim` | `658fe9e4948fd7a3f556a72a253ef15e90c4eb6d3343050802bb7716b67cb916` |
| `clone_infantry_support_attack.anim` | `f3d034696546b8ffa4be4b84f5ace38487a36a68684b39c522c06cb5e31a9d42` |
| `clone_infantry_retreat.anim` | `2e6b43fc7d650a417238042ffe9ee956360c46ce8e04e4b4f65b21d66e33bbe0` |
| `clone_infantry_training.anim` | `ee9feacd6ccf2ce8aa3aeebfc002320306b7ecb71305be24d0dc418d4ef8124b` |
| `clone_infantry_wounded.anim` | `86101e24b2652f95b1f199796c224bcb6b40caf5ec47f2122cc17704ba3d4f4b` |
| `clone_infantry_death.anim` | `2f3f44819868da8c03585d23361ce478876c196082701bd28127bb3ede8b7057` |
| `clone_weaponfree_body_diffuse.dds` | `3c579184dc3686062806bd7ffe4d5e28e2b93af85da8c9755e26b7a72b489f2b` |
| `clone_weaponfree_body_normal.dds` | `9f3bae9cd94dd1cf097c0b2df767d54e70c24b493f643e2bb932b16b304628c5` |
| `clone_weaponfree_body_specular.dds` | `c5ae625bf16a54eeb4304b413d24dbe8422ab77022e2f069b431a0decc5b5340` |
| `clone_weaponfree_rifle_diffuse.dds` | `af2f169f402042f75090423bbc040b2aa9241cdafb881cea0639a6b63044b67e` |
| `clone_weaponfree_rifle_normal.dds` | `6e984a113210337330f72a8766880d09c07b84f6415d2cf8d798ee533d69b51f` |
| `clone_weaponfree_rifle_specular.dds` | `4e4c23e5a7439eecc64e8c3f3b5a4d167f040906cedcd6a9fc7b093e45884998` |

## Eight stream/material bindings and states

The parent-installed `meshsettings` are `mesh.001` indices 0/1/2/3 (8000/8000/8000/5142 triangles), `CloneRifleWood` index 0 (136), `CloneRifleSteel` index 0 (384), `CloneRifleBolt` index 0 (44), and `CloneRifleSling` index 0 (36).
All use `PdxMeshAdvanced`.
The four body streams and sling use `clone_weaponfree_body_diffuse.dds`, `_normal.dds`, `_specular.dds` at 1024x1024; wood/steel/bolt use `clone_weaponfree_rifle_diffuse.dds`, `_normal.dds`, `_specular.dds` at 512x512.
Body packed normal RGBA is `(0, source R, 0, source G)`; body specular RGBA is `(0,32,metallic,255-roughness)`.
Rifle wood/steel constants and flat packed normal are recorded in its material manifest.
The actual shader channel mapping and DDS roundtrip, not the importer's preview roughness interpretation, establish the material contract.

Stable runtime identifiers are `clone_infantry_mesh`, `clone_infantry_entity`, `clone_infantry_entity_snow`, `clone_infantry_entity_desert`, and nine `clone_infantry_<role>_animation` declarations.
Current sprite enumeration found only `common/units/clone_infantry.txt#clone_infantry` using `sprite = clone_infantry`, covering normal and Kruger clone formations.
`aryan_clone_infantry` remains on the normal German infantry model/entity family through `gfx/entities/zz_clone_infantry_aryan.asset`; its separate counters are excluded.
The historical unconsumed entrain proposal is superseded by the current explicit nine-role parent scope.

Each firing state requires its own effects/sound synchronization rows; existing entity times belong to the old animation set.
At 24 FPS use `(frame-1)/24`:

| State | Discharge | Recoil | Extraction | Recovery |
|---|---|---|---|---|
| attack |19 /0.75s |21 /0.833333s |39 /1.583333s |61 /2.5s |
| defend |25 /1.0s |27 /1.083333s |45 /1.833333s |73 /3.0s, loop |
| support_attack |25 /1.0s |27 /1.083333s |45 /1.833333s |73 /3.0s |

Both actual-byte locator names, `muzzle` and `cartridge`, remain parented to `RifleControl` with bone-local matrix roundtrip error under 0.00001.
The exact installed rifle precedent uses `rifle_muzzle_particle` and `muzzle_flash` at `muzzle`, plus `rifle_cartridge_particle` at `cartridge`.
The parent owns adding these effects to all three firing states and aligning recorded audio onsets to the visual phases.
Move/retreat step contacts are frames 1/13 (0.0/0.5s); wounded reacts at 7 (0.25s); death body impact is 37 (1.5s) and settle 61 (2.5s).
Training is non-firing.

## Licensed sound handoff

Ten recorded-source PCM16/44.1 kHz/mono candidates exist in `audio/closure_20260912/derived/`.
Sources are kurt's original human soldier voices (CC BY 3.0), thebardofblasphemy's recorded grunts (CC0), Joseph SARDIN's recorded marching-machine foley and casing contact (CC0), kyles's real Lee-Enfield report (CC0), and leonelmail's dirt body-fall recording (CC0).
`audio/closure_20260912/source_review.md` records exact pages/direct URLs, creators, licenses, source variants, retrieval basis and attribution.
`audio/closure_20260912/audio_manifest.json` and `audio/closure_20260912/body_impact_manifest.json` record immutable source hashes and exact trim/resample/conversion commands.
Float resampling peaks above full scale required bounded linear gains for the right step, rifle and case recording before PCM quantization.
`audio/closure_20260912/headroom_repair.json` preserves prior candidates and records gains of 0.8910038798584571, 0.812845695768363 and 0.7579406636082411 respectively; their resulting peaks are approximately -1 dBFS, with all ten selected PCM candidates free of full-scale samples.
The other seven candidates retain their previous bytes, and no source recording was modified.
`evidence/closure_20260912/audio_candidate_verification.json` records file probes, sample amplitudes and current runtime observations.
One additional licensed audio source was downloaded in this closure; no audio was generated, synthesized, composed, recorded or manually authored.
The body-fall source page and URL were recorded before download.
The Freesound sources are official full-duration MP3 previews, not login-only original files.
The inherited marching input is explicitly foley, not claimed as authentic marching boots.
The simulated `Gunshots_8.ogg` source and absent historical OGG derivatives are rejected.

| Role / candidate basename | SHA-256 |
|---|---|
| selection / `clone_infantry_selection_01.wav` | `2b4c3e47333a1d852abed3c729ba9a94cc460fe8b9c8a38be0795b7c78af7ece` |
| ack / `clone_infantry_ack_01.wav` | `754362887347c0a08fdead9723c689eff0e105dd4762dadf8e6ecf596b1e99f7` |
| step_left / `clone_infantry_step_left_01.wav` | `6151822bf77e278d18af747d46f350f4adce3407dd121d68cac6b707dbf1202e` |
| step_right / `clone_infantry_step_right_01.wav` | `e4b7dc251935e5d290b760304020ac0f487f9c166bac7f7dc4bff60f44b74e37` |
| attack_voice / `clone_infantry_attack_voice_01.wav` | `60e9b8b659f8db18567159bd08168f05f057a1a85362b58b6df54a2510992094` |
| rifle / `clone_infantry_rifle_01.wav` | `f5419c3e428b4364f1d3a6f844958b37d456b2ec850b091ff829d60cfea6e9a1` |
| casing / `clone_infantry_casing_01.wav` | `5e8c8f8ab7e1b7d225aef9555714e7e9bf8f86381dee7d527f72c93d6b2918c8` |
| wounded / `clone_infantry_wounded_01.wav` | `461952f64ad748ec62dfaa700bcbba644ce584418f27a7bd59f04238d329013e` |
| death / `clone_infantry_death_01.wav` | `23dd22893473bd5a76648c86d11c1f61829b4669a2d338164989db197e68fd0f` |
| body_impact / `clone_infantry_body_impact_01.wav` | `55f20808d0da9fd43e46499d2eda59aecfa18e2a3f0e899d7453539058eed7ef` |

The source/license and original/derived lineage are complete; audio semantics, utterance cuts, perceived volume, lead-in and audible phase sync remain `needs_user_review` because no audio-understanding route was available.
The full rifle candidate has source lead-in and must not be treated as a sample-zero discharge.
`audio/sound_design_handoff.md` names the current source/wrapper IDs and exact visual timing.
Parent audio files are `sound/clone_infantry_sound.asset`, `sound/chaosx_sound.asset`, and `sound/shared_clone_system/clone_infantry/`; entity events belong in `gfx/entities/clone_infantry.asset`.
Generic clone-only selection/acknowledgement remains `blocked`: the verified vanilla `Voices` consumer selects country/original-tag infantry groups (`GER_infantry_idle`, `GER_infantry_move_out`), with no demonstrated per-subunit clone route.
Do not replace ordinary infantry voice pools or use idle events as UI-selection substitutes.
No idle/engine loop or unauditioned movement bed is selected for this human profile.
A separate projectile-hit cue has no demonstrated consumer in the current entity; the authored collapse impact is covered by the recorded body-fall source.

## Counter handoff

The generic clone owns original large/map strips plus clone-cohort capsule archetype/technology art under `counter_art/`.
A bounded `chaosx_icon_artist` audit corrected the inherited large-counter olive palette to the exact installed vanilla family and corrected the old map-frame wording.
It preserved source artwork, all alpha bytes and frame geometry, while excluding `counter_art/aryan_clone_infantry/`.
The worker reviewed the comparison sheet and accepted the palette, distinct states, source identity and retained capsule/cohort companion art.
The final current record is `counter_art/palette_closure_20260912.md`, `counter_art/manifest.md` and `counter_art/gfx_handoff.md`.
Installed references are `interface/subuniticons.gfx`, `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` (152x42, two 76x42 frames) and `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds` (60x12, two 30x12 frames), plus the matching skill-local `units/land/counters_large/` and `map_counters/` families.
Current tokens are `GFX_group_clone_infantry_icon`, `GFX_unit_clone_infantry_icon_medium`, `GFX_unit_clone_infantry_icon_medium_white`, `GFX_archetype_clone_equipment_medium`, and `GFX_clone_infantry_access_tech_medium` in `interface/clone_system.gfx`.
The large normal state uses the sampled vanilla green and the schematic state uses white; both small-map states follow the installed white/gray family.
The equipment/technology identity remains clone-growth capsules/cohort, not the rejected rifle experiment.
The processed large strip SHA-256 is `867dc2aa8fc163c8f9bb95648ca4d21075a61e18c176a0914c774d90dc3db348`; its final DDS SHA-256 is `f722640e4f51f279248ba04263232dcef766d63289896f26291513e34cf9abc9`.
The processed map strip SHA-256 is `533693dcf189c5321adc2c43d8ac00fcf2e1bc6ceb907d549bdd4b68b4242955`; its final DDS SHA-256 is `d14f74de0ed3009ca85bf7683b045d168006a50420d9127b054e1f2d3a47304e`.
The strict one-level BGRA8 DDS files decode with zero pixel difference against their processed PNGs.
Large normal retains 561 exact reference-green pixels with R=B and no warm chromatic pixels; large schematic and both map states have zero visible chromatic pixels.
The comparison sheet SHA-256 is `f52152812353385bbbe8fb57b9aef939efb5c19fdad6a933e2ff41fd6f12c700`; machine-readable palette validation SHA-256 is `0e90e656102219f1be5b4863d057ab9bf2ed33d53444a8eed031a905cbb9d6c4`.
All four selected counter/equipment runtime destinations match their package bytes in `evidence/closure_20260912/counter_acceptance_and_runtime.json`.
The parent visually accepted both repaired counters, promoted them through the existing `noOfFrames = 2` consumers, and committed the runtime copies as `f51b3446a`.
Counter production and physical runtime integration are complete; no in-game counter validation is claimed.

## Dependency and validation limits

Blender 5.1.2 build `ec6e62d40fa9` and `io_pdx_mesh 0.91.0` were used.
The upstream ZIP SHA-256 is `a683df08318cb700014c7fe9a3d15139e5fb2313c7e98715204263e48931f7c2`.
Closure operations used the exact guarded adapter 1.10.44 wrapper and its fresh live schemas, not unrestricted Blender Python.
The independently verified bridge listened on 127.0.0.1:9876.
The closure lock SHA-256 was `abebc252014ef5c9d7f6f3f45f1760b8192de7e7a2a81d7d26e7eeb18b3601a2`; schema-lock SHA-256 was `43d1f4665d4f776f30e47b99acd1297b862303f42bafb741650cf5a99f3825ba`.
The source/config hash checks and exact requests are in `evidence/closure_20260912/dependency_preflight.json` and the attempt's call/request/response/transport files.
The deployed compatibility modernization is parent-accepted: 37 exact present-file matches, 3 expected absences and 0 mismatches.
Fresh shared verification is `.tools/3d_pipeline/reports/io_pdx_deployed_source_verification_20260912.json`, SHA-256 `9498fb8e634d53c3e290b4542e19a3ab7888dc672c4c3eb4999618af78687866`.
The parent subsequently accepted 1.10.45, lock `3911b1aaea062abacdeda21639a5a3c33472574e79500234f77403f60ee38680` and worker `690eaf9b3c33c37f8eefb7ca5b737efd47de7fa24677f03cf494196927cf84a0`; no additional Blender call was needed.
Later shared maintenance holds did not trigger new calls or reexports.
The direct MCP exposure still reporting 1.10.44 was not treated as proof for a newer publication.
The original active Meshy 7 body used the pinned official Meshy MCP 0.4.0 route, with its schema/integrity/task evidence preserved in the attempt; provider gates were not applicable to this Blender-only continuation.

The standalone Technology Tree Viewer was not found in the inspected installed HOI4 tool package or its registered commands; scoped evidence is `evidence/closure_20260912/technology_viewer_availability.json`.
No viewer capability or service health was inferred from exposed tool names.
No live-game validation was performed, and engine actor speed, final particles/light/audio, voice consumers and counter appearance are not claimed as live-validated.

## Document reconciliation and ownership

| Surface relative to the job | Disposition |
|---|---|
| `job.yaml` | implemented: active Meshy 7 body/direct Blender scope, nine roles, selected hashes and current runtime status |
| `manifest.md` | implemented: 44-bone physical closure, current materials/evidence/costs and explicit companion limits |
| `runtime/selected_package.json` | implemented: sixteen selected source/staged/runtime hashes and nine actual-byte action records |
| `runtime/handoff.md`, `runtime/crosswalk.md`, `runtime/integration.md` | implemented: exact streams/identifiers/timings, consumers and completed physical/counter integration; historical attachment blocker archived |
| `attempts/20260906_weaponfree_blender/final_source_selection.json` | implemented: Support V4 selected, Death V6 retained, export/reimport and runtime promotion linked |
| `audio/sound_design_handoff.md`, `audio/evidence/provenance.md` | implemented: licensed PCM candidates, rejection of simulated gunshot, real current paths and UI/audio limits |
| `history.jsonl` | implemented: appended this closure selection, runtime parity, cost and remaining companion limits without changing historical rows |
| Previous active versions | superseded: preserved unchanged under `evidence/closure_20260912/historical_active_docs/`, with checksums |
| Old provider/source/checkpoint evidence | retained historical lineage; never overwritten or selected as an active fallback |
| Counter records | implemented: exact vanilla palette, preserved alpha/frames and capsule identity, DDS roundtrip and source/runtime hashes; current review status in the main counter acceptance receipt |

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.
No skill or shared dependency was edited by this worker.
No required 3D component or consumed action was omitted, aliased or replaced by a static/whole-rig substitute.
The inherited transparency fallback, preserved generated-reference authorization, recorded marching foley, MP3 source quality, missing UI voice route and unauditioned sound/effect synchronization are explicit limits rather than hidden simplifications.
Overall completion remains with the parent after companion review/integration and the user's live consumer evidence.

## Final evidence inventory and commit boundary

`evidence/closure_20260912/closure_checksums.json` records the final selected source, export, actual-byte reimport, preview, manifest, audio and counter evidence hashes.
`evidence/closure_20260912/closure_changed_files.json` lists this closure's exact package artifacts and reconciled documents, distinguishing preserved inputs from newly produced or updated files.
The permanent handoff is the only tracked-scope document authored by this worker; the repository ignores the `docs/assets/` package tree.
The parent explicitly retained final Git commits in the shared worktree, so this worker made no commit and did not stage or force-add ignored assets.
The parent runtime counter commit is `f51b3446a`; model payload copies remain evidenced by their exact source/staged/runtime hashes.
