# Rat model repair — final handoff, 18 October 2026

Status: requested rat repair installed and reviewed offline from the exact exported bytes.
No game was launched and no in-game validation is claimed.
No commit was created; the parent owns review and commit.

## Result and root cause

The shipped mesh had 35 boundary loops totalling 145 edges.
The prior preparation discarded arbitrary incident faces at non-manifold fur junctions as though they were duplicates, then decimated the result.
The original provider geometry contained no exact duplicate faces; deleting those faces opened the shell.
The repair restores that original UV/geometry lineage, closes reviewed fur fins and junctions, separates point contacts, repairs seam normals and retains the texture bake.
The oral pouch is closed, with a manually placed jaw hinge and reviewed local weights; the tail has ten manually positioned joints and corrected skinning.
The final mesh is one closed outward shell: 31,278 triangles, 15,597 exact-position vertices, 36 bones, two streams, zero open/non-manifold/inconsistently wound edges.
All eight roles use different already-downloaded presets, ingested with immutable receipts and cleaned up live in Blender with deliberate poses and reviewed native contact baking.
The final attack has a forward claw strike and jaw closure, with the guarding arm moved aside after closeup review exposed wrist/muzzle occlusion.
Defend is a compact guard and counter-swipe; support is a rearing screech/rake; movement alternates planted feet; retreat scurries back with a shoulder check; idle breathes/sniffs/shifts weight; training alternates claw drills; death buckles, falls and settles prone.
Runtime filenames, mesh/animation identifiers, entity and state names remain stable.
The three DDS maps, calibrated scale and existing counters are retained.

## Exact delivery and reviewed evidence

The installed bundle is `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/export/models_1018_final/`.
The editable authoring checkpoint is `blender/checkpoints/models_1018_68_attack_muzzle_clearance.blend` beneath that job root.
Seven actions and the mesh retain v3 byte evidence; the attack uses the separately accepted v4 revision.
All eight applicable animation delivery checks pass, including in-place roots, per-frame motion limits, loop closure and raw quaternion loop-wrap continuity.
Move and retreat each measure exactly one certain plant for each foot per cycle.
Actual imported interpolation was sampled at every integer and half-frame.
The largest sole/body excursion is 0.0385 source units below the preview plane (about 0.52% of rest height), within the documented 0.05 sole-contact tolerance; no material sinking was visible in the reviewed phases.
This is a measured offline tolerance, not a claim of mathematical zero penetration or terrain-specific game behavior.

The parent personally inspected every final action sheet from map, front and side cameras, including every listed phase below.
Back faces are transparent in the review shader, so a missing/back-facing surface cannot be hidden by two-sided preview rendering.
Final material previews decode the installed packed normal and gloss maps; no replacement diffuse or normal map was substituted.
The requested combined PNG is `evidence/models_1018_final_actions_contact_sheet.png`.
Full sheets are `evidence/models_1018/final/<role>_sheet.png` for seven roles and `evidence/models_1018/final/attack_v4/attack_sheet.png` for attack.
The repaired muzzle/bite closeup is `evidence/models_1018/final/attack_v4/head_closeup/attack_head_sheet.png`.
The accepted render paths and hashes are enumerated in `evidence/models_1018/final/parent_acceptance.json`.
Independent geometry and final motion reviews are `evidence/models_1018/independent_geometry_review.json` and `evidence/models_1018/final/independent_motion_review.json`.
Installed vanilla GER infantry move, attack, idle and death actions were reimported and reviewed in `evidence/models_1018/vanilla_reference/*_visible_sheet.png` for timing, in-place behavior and readable phase comparison.
The final static consumer check is `evidence/models_1018/final/runtime_consumer_validation.json`.

| Role | Final reviewed frames | Sampled span at 24 FPS |
|---|---|---|
| attack | [1, 19, 28, 33, 41, 53, 67] | 2.750 s |
| defend | [1, 9, 17, 23, 33] | 1.333 s |
| support_attack | [1, 17, 22, 34, 42, 52, 62] | 2.542 s |
| move | [1, 3, 10, 18, 20, 27, 35] | 1.417 s |
| retreat | [1, 4, 9, 16, 19, 24, 31] | 1.250 s |
| idle | [1, 13, 25, 37, 49, 61, 73] | 3.000 s |
| training | [1, 17, 29, 45, 61, 73, 89] | 3.667 s |
| death | [1, 14, 27, 44, 56, 71, 82, 94] | 3.875 s |

## Installation and changed-file hashes

Every runtime copy records the candidate source, old destination hash and final destination hash in `evidence/models_1018/final/runtime_install_receipt.json`.
That receipt also lists every deleted gravel file with its preimage SHA-256.
The complete owned changed/new artifact inventory, including native sources, receipts, renders, documentation and this handoff, is `evidence/models_1018/final/changed_files_sha256.json`; the checksum index excludes itself.
Scratch scripts remain under ignored `.tmp/models_1018/rat/` and are not maintained tooling.

| Runtime file | Final SHA-256 |
|---|---|
| `gfx/models/units/020_black_plague_rat/black_plague_rat.mesh` | `dedb6c5dcb7433b7d9d55b5dc1e5d3756cb9ad72e1a0d7fd075e0446b998adf7` |
| `gfx/models/units/020_black_plague_rat/black_plague_rat_attack.anim` | `d2ad0cb9ba098424e669ebf5b9ffb634ac67e459ec615cd0e1f3133ce8496502` |
| `gfx/models/units/020_black_plague_rat/black_plague_rat_defend.anim` | `99da8e84ec984de746e092e2c559e213ff69013bdd4def0c6ef76a31db15329b` |
| `gfx/models/units/020_black_plague_rat/black_plague_rat_support_attack.anim` | `2f2b1c4ae5c8f18b0d791525a9c47326f8ea8fb1d9cabc804fa05c0d9b95d641` |
| `gfx/models/units/020_black_plague_rat/black_plague_rat_move.anim` | `e7c9e8efa74e15ae990acf965967d379d8642241e11d9ab42578eb022dcff92b` |
| `gfx/models/units/020_black_plague_rat/black_plague_rat_retreat.anim` | `db0e2f4e609c143409c6b17b3171747f263875c5593d130b863e318b98da8a2f` |
| `gfx/models/units/020_black_plague_rat/black_plague_rat_idle.anim` | `d37a979b77364066b6984e7dfaba332090ef0d24448fafabda6b6aeb876e3111` |
| `gfx/models/units/020_black_plague_rat/black_plague_rat_training.anim` | `25d4531851eaf7d1b50c42bd0964ef37a9f2b7093de355ec446494af32b88adb` |
| `gfx/models/units/020_black_plague_rat/black_plague_rat_death.anim` | `0301da42ff9884c105789c42aec8fcf1f9c515e85103d511ba6dd121aee05ac8` |
| `gfx/entities/020_black_plague_rat.asset` | `2609ff9cb827b300dd9f494c7623de181ca49bbc0ba5e9f795bc43a403434f85` |
| `gfx/entities/020_black_plague_rat.gfx` | `307ba08fce5c662fc03ab6c4371f3d045911af5ce8f679d9af5e4c09b2e28467` |
| `sound/020_black_plague_rat_units_sound.asset` | `00184a4a63ab729c2e8cc213a843e0ba392a1b345822aa6b74240de35e1197ff` |

## Presets and provider accounting

This repair made zero Meshy/provider calls and consumed zero credits.
The following historical task IDs identify existing downloaded inputs, not new jobs:

| Role | Retained preset | Historical task ID |
|---|---|---|
| attack | Thrust_Slash | `01a038a0-6bdc-7f0d-b983-623b14fe255e` |
| defend | Two_Handed_Parry | `01a038a0-6ded-721f-bdb1-8b2cea58a05b` |
| support_attack | Double_Combo_Attack_6ec2e49 | `01a038a0-6fca-7291-bbff-fb896c70f200` |
| move | walking_man | `01a0389d-7bb4-7139-800e-81e6527363b0` |
| retreat | Walk_Fight_Back_inp_c01d6da | `01a038a0-71d9-7221-abf0-9ae9612f38e8` |
| idle | Combat_Stance | `01a038a0-691d-721e-baea-072334706658` |
| training | Weapon_Combo | `01a038a0-7448-7f0f-a12d-595ac09a0d11` |
| death | Shot_and_Fall_Forwa_4a3aeb9 | `01a038a0-767e-713b-a4c3-5dba4318ae7b` |

Input hashes and adapter ingestion receipts are in `provider/provenance/manual_presets/`.
No generated rig, generated animation, synthesized audio or paid retry was used.

## Recorded audio and synchronization

The package retains eleven verified WAVs from three recorded sources:

- Bamboo-rat calls: British Library Board, recordist Richard Ranft, CC BY 4.0, [source](https://commons.wikimedia.org/wiki/File:Bamboo_Rat_(Dactylomys_dactylinus)_(W_DACTYLOMYS_DACTYLINUS_R1_C1).ogg).
- Eating/bite recording: admin_phpbb (metadata: Stephan), public domain, [source](https://commons.wikimedia.org/wiki/File:Cat_eating_noisily.ogg).
- Impact and footstep foley: gregoryweir, public domain, [source](https://commons.wikimedia.org/wiki/File:Dull_thud.ogg).

The unproven gravel recording and current rat-brute derivatives were removed after the source review could not establish an eligible original grant.
The movement wrapper retains its stable name but plays the existing verified thud as individual footfalls.
Move contacts are at 0 and 0.708333 s; retreat contacts are at 0 and 0.583333 s.
Attack claw contact is 1.125 s and bite closure 1.333333 s; death body contact is 2.916667 s.
Support uses its vocal at 0.875 s, with no false bite/impact cue, and the empty-handed training drill has no false impact.
Attribution, original hashes and mechanical adaptations are documented in `sound/020_black_plague/rat_units/rat_brutes/ATTRIBUTION.md`.
The source receipts and waveform evidence are `audio/models_1018_sources/receipt.json` and `evidence/models_1018_parent/manual_audio_verification.json`.

## Simplifications, omissions and limitations

No requested action or model region was omitted or replaced by a duplicate-role animation.
No design simplification was used.
The jaw uses a reviewed six-degree working opening; larger trial openings visibly stretched the small oral walls and were rejected.
The bite is a forward head lunge with a small jaw closure, not a large exaggerated gape.
Audio provenance, formats, waveform content and timing were checked, but this session could not audition audio and makes no auditory acceptance claim.
The offline camera/material checks approximate HOI4 presentation; no live engine rendering or terrain test is claimed.
Legacy gravel cues retained for other xenobiological consumers remain outside this rat job’s ownership; their provenance review is a separate parent follow-up.
No requested output remains blocked.

## Ownership, tools and reusable findings

Only the rat job root, rat runtime/entity/sound surfaces and this handoff were changed.
The owned Blender Lab process on port 9881 was used for native authoring; no other interactive Blender port was used.
The locked adapter handled export/reimport workers through its serialized lock.
The session close receipt is `evidence/models_1018/final/blender_shutdown.json`.
Skills used: `chaos-redux-3d-model-pipeline` and its required start/export/rebuild/audio-counter references, `chaos-redux-event-assets`, and `chaos-redux-subagents`.
No skill was changed because this job’s explicit edit scope excludes shared guidance.
Useful parent follow-ups: native visual baking can leave obsolete fractional keys; exported quaternion signs need adjacent and loop-wrap checks; Blender 5.2 pose selection uses PoseBone.select; render previews must not hold MeshPolygon RNA references across material/render updates.
The following notes preserve earlier findings and failed candidates as historical evidence; their progress labels are superseded by the final result above.

## Historical working notes

# Rat model repair â€” 18 October 2026

Status: in progress; all eight v3 candidate animation delivery checks pass, but final actual-byte visual review and runtime installation remain pending.
Scope and acceptance basis: the explicit `models_1018_rat` assignment, limited to the Event 020 shared oversized rat model, its eight actions, textures, entity and rat-owned sounds.
The user owns in-game validation; this job makes no in-game validation claim and creates no commit.

## Baseline and production ownership

The installed mesh SHA-256 is `c8fe70d1d10164d39ac87b4d82f5ab245ac349b17521811a477d0c171b2aa5ec`.
It matches the earlier WP5 source lineage: `export/r2_v4/black_plague_rat.mesh` and `blender/working/r2/ck/06d_partition.blend` beneath `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/`.
Earlier WP5 source repairs were not delivered to this rat, so historical export or native-import receipts do not prove a repaired model.
The model specialist owns the isolated Blender Lab session on port 9881, candidate model work and actual-byte export/reimport evidence; the parent owns audio review, final candidate review, runtime copies and entity timing.
No other Blender port or sibling model may be used or modified.
The relaunch verified that every captured runtime file still matches the stopped launch's baseline.
The specialist started a fresh owned Blender Lab process on port 9881 (PID 29412), verified Blender 5.2.2 build `d13f752e3b9c` and the locked io_pdx archive/installed patch hashes, and selected targeted Blender repair without a provider call.

The initial neutral source renders preserve the approved muscular rat-man, loincloth and tail identity.
They do not display a large open snout cavity in the neutral pose; posed geometry, winding and actual final material interpretation remain under investigation.
The baseline contains 35 localized boundary loops totalling 145 edges and a visibly sharp distal tail kink.
Initial renders use the active diffuse with simplified preview shading and are not final material acceptance.
Parent-reviewed images: `evidence/models_1018/baseline_map.png`, `baseline_head.png`, `baseline_side.png`, and `refs/original/meshy_input.png` under the job root.
The parent also reviewed `evidence/models_1018/pre_sheet_<role>.jpg` for all eight roles, each with five phases from map, front and side views.
These baseline sheets show the severe distal-tail fold, an overhead-swat attack, a double overhead support slam, a retreat gait closely resembling move, and a squat training action.
The baseline death sheet crops the terminal silhouette; final evidence must frame the complete body.
The corrected material preview interprets packed specular alpha as gloss (`roughness = 1 - alpha`); the raw importer reverses that interpretation.
An intact head in that corrected preview does not yet identify or resolve the user's reported in-game white cavity.

## Audio evidence

The current 13 rat-specific WAVs were decoded and measured in `evidence/models_1018_parent/audio_current.json` under the job root.
They are mono, 44,100 Hz, signed PCM16, with no directly detected clipped plateaus.
The report is file-level evidence only; its zero cue count reflects the intentionally omitted global cue inventory and is not a missing-binding finding.
The exact pre-edit runtime files, hashes and WAV durations are preserved in `evidence/models_1018_parent/baseline_files.json`.
No audio derivative or runtime sound definition has been changed at this stage.
Source/format checks do not establish perceptual playback acceptance; no auditory review is claimed.

The four historical source originals were recovered from their published URLs into `audio/models_1018_sources/`, and every recovered SHA-256 matches the original checksum recorded in the historical provenance.
The download receipt is `audio/models_1018_sources/receipt.json`.
These recovered source recordings are non-shipping evidence, not new runtime replacements.
The relaunch rechecked all four original hashes and all 13 installed rat-specific WAVs against their selected derivative hashes; the exact result is `evidence/models_1018_parent/resume_audio_verification.json`.
The shipping attribution file was updated to identify the recovered originals; sound bytes and definitions remain unchanged at this stage.

| Source | Author / recording credit | Licence | Uses and limitation |
|---|---|---|---|
| [Bamboo Rat calls](https://commons.wikimedia.org/wiki/File:Bamboo_Rat_(Dactylomys_dactylinus)_(W_DACTYLOMYS_DACTYLINUS_R1_C1).ogg) | British Library Board; recordist Richard Ranft | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Existing selection, acknowledgement, attack, idle, retreat, training and death vocal derivatives; genuine bamboo-rat recording. |
| [Dull thud](https://commons.wikimedia.org/wiki/File:Dull_thud.ogg) | gregoryweir | Public domain | Existing impact derivative. |
| [Walking on gravel](https://commons.wikimedia.org/wiki/File:Walking-on-gravel-38827.ogg) | Author unidentified; Commons uploader Fdsfds2.0 | Commons states CC0 1.0 | Existing movement derivatives; original-author mapping remains unavailable. |
| [Cat eating noisily](https://commons.wikimedia.org/wiki/File:Cat_eating_noisily.ogg) | admin_phpbb | Public domain | Existing wet-bite derivatives; rat-bite perceptual suitability remains unverified. |

Original source licence pages were reviewed on 18 October 2026.
Historical mechanical transformations are recorded in `evidence/audio/derivation_and_ffprobe.md`, with the installed short takes mapped by `.tmp/wp5wp6_audio/candidates.json` and the earlier `wp5_wp6_audio_handoff.md`.
No sound was synthesized, generated, recorded or hand-authored by this job.

## Reference and route evidence

The HOI4 reference context/search/read routes are exposed and respond.
The offline Entity modding Event section, lines 139â€“150, revision `74ff51b8ea0924281eb1c067300b52dc373ea9d112341bbb9c34fcb1a11d2d6a`, was read for time, trigger_once and sound events.
An initial request outside that section returned `REFERENCE_POSITION_OUTSIDE_SECTION`; one corrected request read the exact section successfully.
Installed `effects_documentation.md`, `sound_effect`, lines 7981â€“7989, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, documents gameplay sound playback but does not define entity-state timing.
The installed entity-state precedent is `gfx/entities/units_infantry.asset`, lines 10â€“38, and the sound wrapper precedent is `sound/soundeffects.asset`, lines 907â€“927, with sample declaration `sound/sound.asset`, lines 2042â€“2046.
`hoi4.source_lookup` did not return the vanilla GER entity definition from its workspace index; installed source was read directly instead.
The initial and corrected MCP results are in `evidence/models_1018_parent/reference_results.json`.

## Remaining outputs

### Manual-rig relaunch investigation

The no-Meshy relaunch initially owned Blender Lab PID 27212 on port 9881, started hidden from the locked Blender 5.2.2 executable with a factory scene.
The current owned Lab PID is 28256 on port 9881.
PIDs 27212 and 28172 crashed during diagnostic highlighting; the captured native backtrace identifies `MeshPolygon_material_index_set` on stored polygon references.
The corrected diagnostic renderer retains integer face indices and writes the material-index attribute in bulk; subsequent CPU render batches completed.
The own crash evidence is `.tmp/models_1018/rat/model/cpu_crash.txt`.
No other actor's process was contacted or terminated.
The checked-in general Lab configuration still names port 9877, so this job uses the existing repository stdio wrapper with an explicit `BLENDER_MCP_PORT=9881` override; no other port was contacted.
The live adapter health check confirms version 1.11.0 and the installed export functions, and the current adapter source hashes match the dependency lock.
The HOI4 reference tools are absent from this relaunch's exposed inventory, so pertinent offline Entity modding sections and installed infantry/entity and shader sources were read directly.

The earlier `models_1018_06_closed_shell_v2.blend` candidate is unaccepted: it has zero boundary edges but 17 pinched vertices, four face-connected components and contradictory winding constraints.
The new read-only source comparison identifies a concrete preparation defect: `blender_worker.py` treats `edge.link_faces[2:]` as duplicate faces without comparing triangle identity.
The retained preparation receipt records 64 such deletions, followed by reduction from 31,113 to 29,999 triangles.
The original retained rigged GLB has no exact duplicate triangles, and a specialist's independent offline decoding identifies fur flaps and small closed pockets attached at multi-face edges instead.
Its source topology is 31,177 triangles, 42 three-face edges, 12 four-face edges and 71 boundary edges; 69 boundaries belong to thin flaps.
Deleting arbitrary incident faces therefore cannot serve as the repair.
No shared tool was edited by this job.

`blender/checkpoints/models_1018_07_restored_source.blend` restores the retained original geometry, UVs, corner normals and provider-authored body weights as a separate unaccepted working source.
The source GLB SHA-256 is `88a6edf3a4fc71042b513dde2d3dcf71912a7b9bc76ce8f255827d30223b341d`.
Its body rest skeleton matches the current skeleton after the recorded 3.869381409465341 scale conversion: maximum joint-head error is 0.000034074 units, with zero measured orientation difference and matching parents.
`models_1018_08_manual_working.blend` removes only disposable reference objects and old actions from that working scene; it is not export-approved.
Original archives and installed runtime bytes remain intact.

The parent reviewed the approved reference, the prior patch sheet and attack sheet, the new `raw_source_head.png` and `raw_source_tail.png`, and `wedge_review_first10.png` under `evidence/models_1018/`.
The first ten wedge proposals preserve each fur flap while replacing a verified adjacent host face with connecting sides.
Further review covered `fin_review_part1.png` through `fin_review_part3.png` and `junction_review_part1.png` through `junction_review_part4.png`, including additional views of flap 4964.
Two initial local-authoring calls stopped at pre-mutation index-map assertions because GLB and Blender vertex ordering differ; neither changed mesh data.
The subsequent positional mapping is retained in `blender_alias_map.json`; its tool response was lost after the report was written, and the saved report established the required face correspondence without repeating the operation.
An earlier read-only edge-detail call similarly lost its response, and one corrected retry succeeded.
No unreviewed cap, blanket normal reset, generated rig or procedural action has been accepted.

Preset ingestion uses only the eight existing rat FBX archives and their historical provenance through the locked `inspect_animation_source` and `import_animation_action` operations.
All eight distinct source presets have been ingested successfully.
The per-role records under `provider/provenance/manual_presets/` distinguish ingestion from manual correction and final acceptance.
The independent `chaosx_3d_model_pipeline` topology review was read-only and returned exact face memberships, positional aliases and bounded repair proposals under `.tmp/models_1018/rat/topology_review/`.
It did not operate Blender, mutate assets or approve any candidate.

The current combined working checkpoint is `blender/checkpoints/models_1018_57_v2_loop_closure.blend`.
Live geometry authoring preserved the original visible fur flaps, repaired their attachment wedges and sixteen compound junctions, removed only two independently inside-tested internal triangles, and separated seven point-touching fur fans by approximately 0.002 source units without changing their weights.
The repaired pre-mouth candidate has 31,226 triangles and one face-connected shell.
`shell_topology_check_after_tips.json` records zero boundary edges, non-manifold edges, non-manifold vertices and inconsistent winding at both 0.000001 and 0.0005 source-unit tolerances.
Exact-seam consolidation in checkpoint 15 preserved every surface triangle, per-corner UV and skin influence while producing 15,571 native vertices and removing 147 unused raw wire edges.
The native consolidated mesh is a single closed manifold surface; corner-normal drift remained below 0.181 degrees.
Six newly authored triangle UV projections that crossed the atlas border were corrected from nearby source-face UV mappings in `uv_repairs.json`.
These are source-checkpoint results, not exported-runtime acceptance.

The repaired rest views use the actual active DDS maps, installed RRxG normal decoding and gloss inversion, with back-facing geometry explicitly rendered transparent in Cycles.
The parent reviewed `repaired_rest_map.png`, `repaired_rest_head.png`, `repaired_rest_mouth.png` and `repaired_rest_left_hand.png`; the head and snout show opaque exterior geometry in these views.
The full view list and preview-only shader interpretation are in `repaired_rest_material_review.json`.
No replacement DDS, mesh or animation has been installed.
Live rig repair added a nondeforming export root, placed the ten tail joints along measured tail sections, and restored short arm, foot and spine bone endpoints to their existing child joints without moving those joints.
Tail skin repair affects 809 explicitly reviewed vertices; outside weights remain unchanged.
Opposite distributed tail stress poses reduced maximum physical-edge growth from approximately 0.151/0.118 units to 0.056/0.039 units, with close-up material review recorded in `tail_bend_review_v2.json` and the associated tail-root renders.
The remaining worst ratios concern microscopic cloth-interface edges; final action deformation remains subject to export review.
The five-digit hand measurement review is retained under `.tmp/models_1018/rat/hand_review/`; connected claw tips are not missing fingers, and no digit has been removed.

The movement draft preserves the ingested alternating gait, uses a one-second native timeline edit, and adds individually authored hunched torso and tail phases.
The first broad tail curl was rejected after visual review and replaced by a lower anatomical curve.
Measured vertical grounding places the source draft's lowest vertex between 0.0039989 and 0.0040001 units across all 25 frames; this is not exported-runtime or foot-plant acceptance.
The parent reviewed `preset_move_sheet.png`, `preset_defend_sheet.png`, `preset_support_attack_sheet.png`, `preset_retreat_sheet.png` and `draft_move_sheet.png` under `evidence/models_1018/`.
The attack draft has seven deliberately authored guard, wind-up, forward claw-contact, bite-lunge, follow-through, recovery and seam phases while retaining its distinct provider lower-body motion.
All eight roles have live-authored cleanup drafts using their distinct retained presets.
The source reviews cover the claw-and-bite lunge, guarded counter-swipe, rearing screech and short rake, digitigrade lope, backward scurry with an over-shoulder turn, sniffing idle, alternating claw drill and collapse with a half-second settle.
`source_review_index.json` lists the 56 reviewed phases and 168 map/front/side views; the parent inspected all eight current contact sheets.
Native IK controls fixed both idle feet and the attack/defend starting stances, with stretch disabled and their reviewed poses baked into the original actions.
The attack forward plant was brought closer and its stance deepened after the native reach check rejected an unreachable target; the final maximum target error was 0.000140 units and the bake preserved world matrices within 0.000021.
Defend and idle bake parity errors were below 0.000014.
Late death leg/toe poses prevent the retargeted left leg from entering the floor, and explicit tail poses cover the fall and settle.
Measured grounding uses sole geometry for standing roles and body geometry for death; the tail never determines standing foot height.
Complete-frame source checks found and corrected three short tail intersections, and exact starting-pose copies close the four looping roles.
The current source has 15,597 vertices, 31,278 triangles, one closed manifold component, consistent winding, 36 bones and no more than four skin influences per vertex.
`source_audit.json` and `all_action_grounding.json` retain the measurements; exported-runtime proof is still outstanding.
The read-only oral-region proposal identifies a connected 21-face disk behind the upper incisors; its current live face aliases are retained in `mouth_live_aliases.json`.
A native inset and inward extrusion created a closed oral pouch while retaining the upper incisors, followed by a manually placed jaw hinge and four reviewed skin-weight bands.
The 20- and 35-degree stress openings were rejected because they stretched the small mouth walls; the reviewed working poses use at most six degrees.
The parent inspected the closed, six-degree and ten-degree close-ups, and retained the narrower working range for the authored actions.
Source continuity cleanup negates equivalent quaternion keys and handles without changing key times or counts.
Obsolete fractional provider keys were then removed only from channels replaced by native contact baking or measured grounding; all integer-frame bone matrices were preserved exactly.
Those operations are recorded in `source_export_staging.json` and `fractional_key_cleanup.json`.
The half-frame source check still reports small interpolation excursions, including approximately 0.0415 units below the floor in attack; these must be resolved or cleared by actual-byte interpolation evidence before installation.
No runtime installation or final animation acceptance is claimed at this stage.

The first exported candidate under `export/models_1018_v1/` passes the actual-byte mesh topology and winding gate.
An independent review of its defend/idle reimports found no geometry defect in the sampled body and focused views; `independent_geometry_review.json` records the exact mesh, animation and DDS hashes.
The exported mesh has 31,278 triangles in one closed outward-oriented logical shell.
The v1 exporter used the mesh datablock name `char1.001`; the live source datablock has been corrected to `char1.002` to preserve the installed meshsettings consumer.
The next partition will retain two bounded streams rather than the first candidate's four conservative batches.

Defend and idle passed the first animation delivery checks, while the other six roles exposed concrete motion, plant or serialized-quaternion findings.
The revised movement candidate passes motion limits and measures exactly one certain sole plant per foot; its small endpoint mismatch has been corrected in the combined source.
Movement and retreat use shorter deliberate strides and contact holds, and the movement stride received a readability pass after visual review.
Attack/support/drill cleanup removes provider clavicle motion competing with the authored limb poses, the drill uses a compact planted stance and small pelvic weight shifts, and death uses controlled bracing limbs instead of the delivered flails.
The support preparation and death fall have explicit timing changes; existing keys and handles were retimed rather than replacing their roles.
Serialized `.anim` sign correction is required after export because matrix decomposition can reintroduce equivalent quaternion sign flips despite continuous Blender curves.
The next actual-byte validation and final reimport review remain in progress; no failed candidate has been installed.

The fresh audio verification is `evidence/models_1018_parent/manual_audio_verification.json`.
All four retained original recordings and all thirteen installed WAV hashes match their recorded provenance.
The historical `.tmp/wp5wp6_audio/candidates.json` intermediate manifest is absent, so current derivatives were checked against the retained hash-bound resume receipt instead.
This session cannot consume audio input; no auditory acceptance is claimed and no runtime sound bytes were changed.

Model repair, eight authored action roles, final material review, actual-byte reimport contact sheets, measured sound synchronization and runtime installation remain in progress.
No design simplification is accepted.
Provider calls and credits for this job: none at this stage.
Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents`; no skill changed.

## Current checkpoint after complete candidate export

The current native authoring source is `blender/checkpoints/models_1018_67_v3_export_source.blend` and the candidate bundle is `export/models_1018_v3/` beneath the job root.
All eight final delivery reports pass their applicable motion, root, seam and measured foot-contact gates.
Move and retreat each have exactly one certain plant per foot per cycle, with no ambiguous plant.
Every loop also passes the extra raw quaternion last-to-first sign check in `export/models_1018_v3/loop_wrap_sign_review.json`.
The v2/v3 mesh difference consists only of tangent rounding below 1.8e-7; geometry, UVs, weights and rest skeleton are identical.
The parent viewed all five revised v3 action sheets; unchanged move, defend and idle retain their prior source review.
Final native reimports are being produced for all eight roles, followed by map/front/side renders with actual DDS decoding and transparent back faces.
The gravel recording has no established CC0, public-domain or CC BY grant from its original author and is rejected for the current rat package.
The planned replacement is the already verified public-domain gregoryweir thud recording, triggered at measured foot plants; no audio is synthesized.
No runtime candidate has been installed at this checkpoint.
