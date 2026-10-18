# Demon model repair — 18 October 2026

The job is incomplete.
Three gait repairs are installed and checked from exported runtime bytes: demonic zombie move, demonic zombie retreat, and Pan Sappers move.
Head-reference decisions, the complete demonic wing/arm repair, and Pan's mesh-topology defects remain unresolved.
No runtime mesh or texture was replaced, no Meshy call was made, no audio was created, and no commit was made.
No in-game validation is claimed.

## Identification and head decisions

Both candidates qualified for gait repair.
The winged Event 002 model matches the user's screenshot description, and its approved `refs/original/meshy_input.png` and older model-reference renders are bald.
The current head therefore does not demonstrate a lost hair or horn component relative to those references.
A clarification is pending: add ragged hair, add horns/crest, or retain the bald reference.

Pan's shipped head has modeled fur/hair, beard, ears and two horns, resembling `refs/original/meshy_input-v2.png`.
However, `job.yaml` and `refs/original/input_manifest.json` explicitly approve the older curly-haired, four-horned faun in `refs/original/meshy_input.png`, SHA-256 `cef9ae4ae7efd1afeb09fdfa542eca75e8c3e867692c5950e36c81419d048e02`.
The later image's resemblance to the installed model does not establish design approval.
A second clarification is pending: restore the faun's curly hair and four horns, or retain the current two-horned goat head.
Neither head has been altered.

## Installed changes and final SHA-256

Paths are relative to the mod root.
The complete artifact inventory, including this handoff's hash, source checkpoints, receipts, previews and temporary verification files, is `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/evidence/models_1018/artifact_hashes.json`.
That inventory excludes its own recursive self-hash.

| Changed file | Final SHA-256 |
|---|---|
| `gfx/models/units/chaosx_demonic_zombies/chaosx_demonic_zombies_move.anim` | `57eb21f9fd3f1bc979c41422593db0a6d898ffa693b8e6fab3808350704177d7` |
| `gfx/models/units/chaosx_demonic_zombies/chaosx_demonic_zombies_retreat.anim` | `7536fadfc2ff1c355d9b82f637b6ae81f722055d0f4ddef1a344605f9287fd73` |
| `gfx/models/units/012_africa_pan_sappers/chaosx_pan_sappers_move.anim` | `113aeddfec418db08a15a4895632ebb8b4513afe36d7b1b6453325b1c1adc22a` |
| `gfx/entities/chaosx_demonic_zombies.asset` (combined with the concurrent combat/audio edits below) | `2527d9df5831b31afc500cab3b9af902cc7e6657d6ad8fb787fb8dd024219b89` |
| `gfx/entities/chaosx_pan_sappers.asset` | `21f5e97b6440f833d95e53a49f57262bbb8c06a2349360fd478adbfac662c02b` |
| `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/job.yaml` | `0372c108668bc4221a60ea5ff74acf4599023eadcf9970bf5619178883d47c9b` |
| `docs/assets/012_africa/models_3d/pan_sappers/manifest.md` | `539d6f5e790b32426a9b3ece976b9306ea2d1dc599c2576848c0535aee64d898` |

Runtime filenames, animation aliases, entity names, state names and entity scales remain stable.
This job changed the three animation binaries and gait-related text in the two entity files.
Those entity edits synchronize the existing footstep cues with the reviewed plants.
The late concurrent changes below are preserved and are not attributed to this job.
The remaining meshes, maps and registrations are unchanged from the task baseline.

### Late concurrent combat/audio integration

After this job's render pass and Blender shutdown, the zombie job installed `gfx/models/units/chaosx_demonic_zombies/chaosx_demonic_zombies_support_attack.anim`, SHA-256 `5658c671514806ac7426b976eb3ffa0dab8f0052682e6fdcd82697ed7c124933`, and changed the demonic support-attack events and idle/defend sound bindings.
Its ownership, selected source, actual-byte reviews and copy receipt are documented in `docs/plans/unit_fix_2026-10/models_1018_zombies_handoff.md`.
That handoff explicitly preserves this job's move/retreat edits and leaves the mesh/weights to this job.
I inspected its current same-model overview at `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/final_demonic_zombies_actions_contact_sheet.png`.
The older support-attack row in this job's sheet is visibly marked superseded, and its captured hash remains in the review JSON alongside the current hash and companion evidence link.
The gait bindings were rechecked against the combined entity file; all three still resolve to the installed reviewed gait bytes and their measured contact intervals.
Do not restore the whole entity preimage over these concurrent changes; this job owns only its header and move/retreat timing hunks.

For the paths below, `D` means `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies` and `P` means `docs/assets/012_africa/models_3d/pan_sappers`.

| Selected source | Runtime destination | Source and destination SHA-256 |
|---|---|---|
| `D/export/models_1018/move_ready_v5.anim` | `gfx/models/units/chaosx_demonic_zombies/chaosx_demonic_zombies_move.anim` | `57eb21f9fd3f1bc979c41422593db0a6d898ffa693b8e6fab3808350704177d7` |
| `D/export/models_1018/retreat_ready.anim` | `gfx/models/units/chaosx_demonic_zombies/chaosx_demonic_zombies_retreat.anim` | `7536fadfc2ff1c355d9b82f637b6ae81f722055d0f4ddef1a344605f9287fd73` |
| `P/export/models_1018/move_ready_120_v4.anim` | `gfx/models/units/012_africa_pan_sappers/chaosx_pan_sappers_move.anim` | `113aeddfec418db08a15a4895632ebb8b4513afe36d7b1b6453325b1c1adc22a` |

Each job's `export/models_1018/install_record.json` records source/destination/preimage hashes, copy time and actor.
Preimages are preserved under the same export directory's `preimage/` folder.
Pan's earlier 30-FPS intermediate installation is retained in that history and is superseded by the final 120-FPS file above.

## Gait findings and validation

The shipped demonic move and retreat used markedly asymmetric support and path lengths.
Pan's shipped move kept the right hoof near the floor for 85 of 87 samples and the left for only four.
These observations come from the actual shipped meshes and actions, not from an older working blend.

The full before/after measurements are in `D/evidence/models_1018/gait_comparison.json`, with the per-frame samples in each job's `move_baseline.json`, `retreat_baseline.json` and `metrics_final_*_baseline.json`.
The path-length metric below is the front-to-back ankle excursion in an in-place clip, explicitly a stride-path proxy rather than a claim of world travel.
Near-floor observations use evaluated foot/toe-weighted geometry; stationary plants are separately established by the delivery receipts.

| Action | Left/right path discrepancy before → after | Left/right mean hip-height difference before → after, model units |
|---|---:|---:|
| Demonic move | 14.49% → 5.46% | 0.02985 → 0.01736 |
| Demonic retreat | 23.97% → 3.11% | 0.07417 → 0.05335 |
| Pan move | 22.54% → 5.84% | 0.10670 → 0.00802 |

| Final action | Frames / FPS | Footstep events, seconds | Reimported half-frame clearance range, model units |
|---|---:|---|---|
| Demonic move | 180 / 120 | Left 0.475; right 1.225 | 0.001066–0.010201 |
| Demonic retreat | 241 / 120 | Left 0.4; right 1.4 | 0.001036–0.010686 |
| Pan move | 177 / 120 | Left 0.4; right stable hold 1.133333 | 0.001061–0.010179 |

The demonic move has exactly 0.75 seconds between alternating footfalls.
Pan's right-foot stationary interval begins at frame 136, with the sound at the stronger ground hold on frame 137; that event lies inside the measured certain-contact interval.
The demonic retreat also has a late left-foot pause within the same stance, which does not receive a duplicate footfall sound.
Pan's separate crouched retreat was inspected and retained; it does not reuse its old move action.

Final checks use the same physical speed and plant-duration limits as the 30-FPS contract.
At 120 FPS, translation is limited to 0.09 model units/sample, rotation to 6.25 degrees/sample, stationary motion to 0.0075 units/sample, and a certain plant requires eight consecutive contact intervals.
The three final actions pass these stricter per-sample checks, loop and root-motion checks, and the source-to-runtime binding checks.
The final selected receipts are `D/export/models_1018/move_ready_v5_delivery.json`, `D/export/models_1018/retreat_ready_delivery.json`, and `P/export/models_1018/move_ready_120_v4_delivery.json`.
`D/evidence/models_1018/runtime_wiring_verification.json` resolves each entity state through its GFX alias and animation registry to the installed bytes and verifies the footstep times against certain-contact intervals.

The shared exporter still applies its 30-FPS per-frame contact defaults at higher FPS and can report spurious additional plants.
Its raw rejection is preserved; it is not reported as a pass.
The final files were checked with the explicit time-normalized measurements above, and exporter q/-q discontinuities were corrected with the approved existing-sample sign tool before reimport.
No speed limit was relaxed to obtain acceptance.
An early higher-rate trial exposed fractional pre-export keys between reviewed poses; the final refinement starts from the reviewed serialized pose sequence and preserves its motion.

## Sources, live authoring and selected checkpoints

New provider tasks: none.
Meshy calls, balance calls and credits used: **0**.

- Move source for both units: historical rig task `019fd311-4488-7174-905a-ae7b87d7e378`, the included `Armature|Armature|Armature|walking_man|baselayer` motion, source FBX SHA-256 `3478812e8536074cb8668987a88dc50bd0255b9d4811dffaefa4d19d0fa776ca`.
- Demonic retreat source: historical animation task `019fd5d8-fb91-77f7-ba72-1cae105975d9`, `Armature|Armature|Armature|Walk_Fight_Back|baselayer`, source FBX SHA-256 `ee7752900fc6bb3cb3588d6681095bc195f95d6237664caa0d676542c334f16d`.

The copied source files and verified receipts are under each job's `provider/reuse_1018/`.
They link the original clone-package download manifests and the fresh source inspections.
The walking file was included with the historical rig output; `meshy_animate` in its receipt is the adapter ingestion category, not a new provider request.

The existing rigs were retained, and each preset was ingested through the supported receipt-verified action importer with measured Foot-to-Head scale references.
Manual work in the live Lab session covered explicit contact-height corrections, stance holds and release poses on the hips/thigh/shin/foot/toe chains, timing cleanup, loop continuity, and small separate WingL_Arm/WingR_Arm follow-through poses for the demon.
The body motion remains distinct provider-derived movement, not a procedural or static stand-in.
The ordinary IK trial was discarded because the imported PDX display-bone tails were unsuitable two-segment IK endpoints; no such controls or changed rest skeleton were retained.

Selected editable sources:

- `D/blender/checkpoints/models_1018_move_baked120_v5.blend`
- `D/blender/checkpoints/models_1018_retreat_baked120_v1.blend`
- `P/blender/checkpoints/models_1018_move_baked120_v4.blend`

Actual-byte native proofs:

- `D/blender/checkpoints/reimport_models_1018_move_ready_v5.blend`
- `D/blender/checkpoints/reimport_models_1018_retreat_ready.blend`
- `P/blender/checkpoints/reimport_models_1018_pan_ready_v4.blend`

The coordinate/export checkpoints, raw exports, corrected exports, text dumps and receipts remain alongside them.
Earlier `models_1018_baseline`, `models_1018_runtime_baseline`, `models_1018_runtime_move_baseline` and `models_1018_walk_authoring_01` partial checkpoints were not selected as production sources.

## Review renders

I reviewed both head comparisons, all frames of the initially retargeted walk and retreat candidates, the contact/release corrections, the final action sheets, and the vanilla comparison.
The final sheets use fixed front, side and approximately 53-degree-down three-quarter cameras with a non-exported review floor.
Workbench evidence covers decoded geometry, deformation and diffuse appearance; engine shading and lighting remain outside this check.
They contain all eight action roles for each model, at least five phases per role, and an additional demonic death frame 46.
The other captured roles are actual-byte imports of the files present at review, not another model's evidence.
The subsequently replaced demonic support-attack is covered by the separate concurrent-combat note above, not by this job's superseded row.

- Demonic final sheet: `D/evidence/models_1018/final_reimport_actions.png`.
- Pan final sheet: `P/evidence/models_1018/final_reimport_actions.png`.
- Exact source hashes, individual render paths, FPS and half-frame measurements: each job's `evidence/models_1018/final_package_review.json`.
- Head views: each job's `evidence/models_1018/head_front.png`, `head_side.png`, and `head_map.png`.
- Source-frame and intermediate reviews: `walk_candidate_frames.png`, `retreat_candidate_frames.png`, `timed_walk_frames.png`, and the role/phase PNGs in the same evidence folders.
- Vanilla comparison: `D/evidence/models_1018/vanilla_comparison.png` and `D/evidence/models_1018/vanilla/`.

The installed GER infantry reference was imported read-only, excluding `collision_box`.
Its measured source height is 7.414978 units and its entity scale is 0.8; the custom meshes retain their existing 7.351825-unit source height and 0.8 scale.
The serialized vanilla walk is 41 samples at 30.75 FPS (1.333333 seconds), and retreat is 51 samples at approximately 30.6 FPS (1.666667 seconds).
Native preview FPS is rounded by the importer, so the timing comparison uses the serialized floating values.
Native world-motion measurements are in `vanilla/motion_calibration_native.json`.
The combined binary skeleton analysis could not reconcile the collision/body hierarchies; the initial failure and one diagnostic request are recorded in `motion_calibration_parser.json`, followed by the native read-only fallback.

## Wing and geometry work — not installed

The current demonic runtime mesh is SHA-256 `1f22772883c2e1b16ba4ed6c64752602b59048bf19d6592cf3dd87a24386eacc`, not the older `776595...` mesh in the October 6 handoff.
`D/evidence/models_1018/geometry_baseline.json` reports zero boundary/nonmanifold edges and outward winding at the declared source tolerances.
It contains a 30,908-triangle main component and a separate four-triangle component, so this report does not claim one connected shell.
Pan's unchanged mesh, SHA-256 `9f5b97f8702e1ab4c90f41624af453e5fd86c75276aed4fcb82bb95103053e24`, retains 125 boundary edges and fails the complete manifold gate.

The demonic wing/arm deformation defect is real.
`wing_edge_audit.json` scans every frame of the baseline action hashes captured before the concurrent combat update and explicitly reports seam-inclusive edge records, not unique physical-edge counts.
At death frame 29, the posterior-arm edge between vertices 3116 and 3462 grows from 0.081181 to about 0.563827 units because the arm also follows WingR_D1.
A manually reviewed 136-vertex arm-weight candidate removes wing/non-adjacent torso influences while retaining the same-side limb ratios; that edge then measures 0.078173 units in the same pose.
A further 32-vertex lower-left membrane candidate uses explicit adjacent-strut weights after rear/side/map region review.
These are staged edits, not accepted replacement skinning.
The central-back edge 13618/14089 still grows from 0.009482 to 0.143600 units in death frame 29, and complete wing deformation acceptance remains unfinished.

Latest staged mesh candidate: `D/blender/checkpoints/models_1018_membrane_weights_v1.blend`.
Exact arm changes are in `D/evidence/models_1018/forearm_weight_correction.json`; membrane changes and candidate death previews are under `D/evidence/models_1018/arm_fix/`.
The candidate still needs further regional work, complete PDX material rebinding, all-action review, mesh export and actual-byte reimport before any runtime promotion.
Its preview material setup is not a completed material handoff.
The temporary candidate death-prefix collision was corrected by isolating the candidate previews under `arm_fix/` and regenerating the baseline phases, including 29 and 46, from unchanged runtime bytes.

## Audio and counters

Only existing sound-event times changed.
No recording was downloaded, generated, recorded, remastered, renamed or copied, and no sound definitions or counter assets changed.

- `chaosx_zombie_move` retains the shared zombie step pool, attributed by the existing review to GboxMikeFozzy, **Footsteps**, CC0: https://opengameart.org/content/footsteps-0 .
  The inherited provenance review records an original-member archival-hash gap; this job does not invent that missing original evidence.
  Source: `docs/plans/unit_fix_2026-10/audio_evidence/provenance_review.json`.
- `chaosx_pan_sappers_move_sfx` retains the muffled/grass hoof recordings credited to congusbongus / MrFizzywig and congusbongus / StephenSaldanha, CC0 member credits within the CC BY 4.0 collection: https://opengameart.org/content/horse-gallop-on-different-surfaces .
  Exact source/member hashes and credit lines remain in `sound/012_africa/units/pan_sappers/ATTRIBUTION.md`.

## References, isolation and completion limits

Skills used: `chaos-redux-3d-model-pipeline` and its start-gates, Blender-processing/export, reference-image, audio/counter and rebuild references; `chaos-redux-event-assets` and its reference-library/unit-visual references.
No skill was created or changed.
No unit definition was edited, so the units/divisions implementation skill was not applied.

The offline Entity modding reference was read at lines 25–44, 124–160 and 169–186, revision `74ff51b8ea0924281eb1c067300b52dc373ea9d112341bbb9c34fcb1a11d2d6a`.
The graphical-asset page has no skeletal rules in its Object Types heading (lines 246–248, revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`); the relevant rules are in Entity modding.
The installed reference root is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
Installed precedents are `gfx/entities/units_infantry.asset`, lines 11–53 and 1927–1948 (default infantry states/scale and GER entity, SHA-256 `6ab4be22bc0757c93f8132f7e247910592a5d8595eaf431d33f23df03f32aa2d`), and the `GER_infantry_rifle_mesh` block in `gfx/entities/infantry.gfx`, lines 1712–1743 (SHA-256 `6439fb7fc1a94e9b2f20368f18bd73526b2abb9a559b62e58a2c2768396e71d4`).
Reference MCP routes were available; source lookup returned no indexed definition for the vanilla mesh, so its source was read directly.
Generic context omissions and unrelated event rules are not claimed as graphical-documentation coverage.

The locked stack is Blender 5.2.2, adapter 1.11.0 and io_pdx_mesh 0.91 compatibility build.
The dependency lock SHA-256 is `ad0ff2c979e02ec02e5b3758225e931de7755973671e6bf67ff8150e82a99c66`; adapter source hashes, operation-array parity, compatibility archive and installed patch-file hashes matched.
The job used only its hidden Lab on port 9883, PID 28948, verified against the live tool PID and executable/command line.
That process was closed and both the PID and port listener were confirmed absent; `.tmp/models_1018/demon/session_closed.json` retains the shutdown evidence.
No other Blender process or port was reused or stopped, and HOI4 was not launched or controlled.

## Simplifications, omissions and blockers

- Full model repair is **not complete**.
- The winged head choice and Pan's conflicting head references require decisions; no head restoration has been installed.
- Demonic wing/arm skinning is only a staged partial candidate, with a known remaining stretched region.
- Pan's topology defects and the demonic extra component remain unresolved; no replacement mesh has been promoted.
- This job did not change other actions; the concurrent support-attack replacement is separately attributed, and neither set of renders closes the remaining model-quality findings.
- There is no in-game validation claim.

No approved reduction of these requirements or substitute head/mesh was used.
The installed gaits are a bounded partial delivery, and the remaining requirements stay open.
All changes are left in the shared working tree for parent review; no commit was made.
