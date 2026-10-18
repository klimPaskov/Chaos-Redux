# WP3 Zombie Outbreak (002) - Delivery Report

## Current takeover: infected idle and parasite separation, 11 October 2026

The requested infected idle skin correction is installed; parasite tube separation remains in progress, with native work serialized through the exclusive Blender lease.
This section supersedes the earlier infected idle remainder of 20 stretched edges; the older tranche measurements below remain historical evidence.
Acceptance basis is the user's explicit WP3 leftover assignment, with the parent reviewing source poses and actual exported-byte deformation before installation.

### Infected zombies: installed idle-weight correction

Nine coat-junction vertices were deliberately reweighted in the live Blender session: 8683, 8692, 8693, 8696, 8704, 8706, 8710, 8750 and 9097.
Across all 691 integer/half-frame idle samples, the maximum number of edges growing more than 0.3 units falls from 20 to 10, meeting the target of at most 12; maximum growth falls from 0.537330 to 0.412081 units.
The other seven roles have no increase in maximum stretch count or growth, and their ground-height samples are unchanged.
The native reimport of the selected mesh and unchanged idle action reproduces 10 stretched edges at frames 45.5, 46 and 46.5; frame 46 has maximum growth 0.41203384 and ground contact +0.00399427 units.

Installed mesh: `gfx/models/units/chaosx_infected_zombies/chaosx_infected_zombies.mesh`, SHA-256 `b6400e0c11300e04b614117f9158d12084c76908bc5bac3ce93940b7376c9709`.
The selected source is `docs/assets/002_zombie_outbreak/models_3d/infected_zombies/blender/checkpoints/wp3e_05_reviewed.blend`; its export is `export/wp3e/chaosx_infected_zombies.mesh` within that job.
The preimage `cddff1d6d8c599555e6024be5439c5b4d53dcb4f21e5f7c51100a98b909d30a5` is preserved in the job's `runtime/preimages/wp3e/` directory.
The mesh retains 30,788 triangles, the same 24-bone skeleton, four `char1.001` streams and the inherited 7.351824-source-unit calibration with entity scale 0.8 applied once.
Decoded positions, normals, UVs, triangles, materials and skeleton are unchanged; the differences are the intended skin records and exporter tangent rounding no larger than 1.79e-7.
The manifold and winding gate passes at 0.0005, 0.001 and 0.002 units, and all eight retained actions have hash-bound native reimport receipts.
All eight runtime `.anim` files, three DDS maps, action registrations and entity behavior are preserved; the GFX header's triangle count is corrected to match the delivered mesh.

Evidence within the infected job: `blender/reports/wp3e_deformation_sweep.json`, `wp3e_invariants.json`, `wp3e_actual_byte_idle46.json`, `export/wp3e/decoded_delta.json`, `chaosx_infected_zombies.delivery.json`, `validation/reimport_wp3e_<role>.json`, and `runtime/parent_install_wp3e.json`.
The selected export/checkpoint hashes, unchanged action hashes, authored weights and source lineage are consolidated in `runtime/handoff.md`.
Parent visual review covers the before/after idle-46 closeups, representative poses in all eight roles, attack toe contact, terminal death, and `blender/previews/wp3e/actual_byte_idle46_quarter.png` from the actual-byte reimport.

Remaining limits: the unchanged attack right toe reaches -0.037745 units at frame 42.5; the death's mid-collapse lift ends with the body on the ground at +0.003950 units.
Importer-default previews have unresolved magenta texture display, so solid previews establish geometry/deformation only; no fresh material-display or live-game acceptance is claimed.
The existing cough, retch and spit recording gaps remain blocked by absent licensed source material under the no-download rule.
No requested infected idle-skin requirement was omitted or simplified; no provider credit was spent.

### Parasitic zombies: separated geometry candidate, pose acceptance incomplete

The accepted native source checkpoint `blender/checkpoints/wp3f_17b_export_bindings_verified.blend` (SHA-256 `6dc64077bf6c488b4f6c28a7254337b277f43ca15ada722ef759fdcf1bc274a8`) contains the original 48-bone hierarchy and eight source actions, the host, and 13 separately skinned parasite parts.
The corresponding accepted geometry export is `export/wp3f_accepted/chaosx_parasitic_zombies.mesh` (SHA-256 `807abd7ff7076df0fa95a6ab3d7a67a8ac0f157f6f10a015ac8d99e7d2152297`), with its native checkpoint `blender/checkpoints/wp3f_18_accepted_pdx_export.blend` (SHA-256 `3b9a7875544576ca720f7b0bae3e7e3aa4f92245e37dc794af19121efea40b3b`).
The decoded topology gate passes for 14 logical objects, 29 nonempty material streams and 32,036 triangles, with no remaining boundary, nonmanifold, winding or degenerate findings under the recorded checks.
The inherited point-only fans, inward faces and mapped local seam defects were repaired; all 14 source meshes retain the exact original 48 group names and index mapping, and the retained actions and original runtime files are unchanged.

Actual-byte import recovered all 14 meshes and one shared 48-bone rig.
Five-phase idle and move reviews found no sampled physical edge growth over 0.3 units; idle grounding still ranges from -0.011261 to +0.021613 units, while move ranges from +0.002201 to +0.004003 units.
The attack review remains unaccepted: grounding ranges from -0.026714 to +0.002762 units, Tube01 has two edges over 0.3 units at sample 53, Tube02 has 15 at sample 88 and 12 at sample 90, and the new Tube13 cap centre exceeds the edge-growth gate at samples 17 and 53.
A proof-scene-only local weight trial reduced Tube13's maximum attack edge growth to 0.259793 units, but it was not saved to the production source, exported or checked across the other seven actions, so it is not an accepted repair.

Runtime files, entity/GFX wiring and all eight `.anim` files were not changed or installed from this candidate.
The active runtime GFX still exposes only four host streams and cannot be assumed to consume the separated parts.
No new Meshy credit was spent for this WP3 repair.

The current Blender lease remains `wp3_leftovers parasitic_zombies 2026-10-11T12:22:31`, owned by the responding PID 38428.
The eight-role Blender Lab call and the subsequent read-only inspection both timed out at localhost:9877; the allowed retry budget for that unchanged route is exhausted, and the worker preserved the process and lease without another call or a second Blender session.
The last returned proof scene was `wp3f_proof_attack.blend` with the unsaved trial; its current state after the timeout is unknown.
The handoff `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/runtime/wp3f_separation_handoff.md` preserves exact object inventories, repair deltas, sample findings and recovery steps.

Remaining required work is to recover and inspect the existing bridge state when its transport is available, finish the two-centre cap trial across all eight actions, map the Tube01/02 stretch edges to immutable source vertices and weights, and then export/reimport and prove all eight roles against one final mesh hash.
The current candidate remains incomplete and must not be installed or described as a finished package; full material display and live-game behavior are also unverified.

Skills used for this takeover: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-subagents`, `chaos-redux-units-divisions` and `chaos-redux-shared-git-commit`; no skill was created or changed.

## WP3 rebuild results (11 Oct 2026)

Package status: **model, texture and action rebuild delivered for all eight units; tentacle rig, wing-membrane reweighting, new sourced audio and live validation remain open** (listed per unit below).
The tranche ran under the lifted Meshy restriction (no credits were needed: every unit was rebuilt from the provider downloads already in its job folder) and the unchanged ban on sound downloads.

### What every unit now has

- A closed, manifold, orientable mesh: the Meshy triangle soup (31k triangles in about 6,000 to 10,000 loose fragments, 19k to 55k boundary edges) is welded at 0.5 mm, over-shared edges keep one face per winding direction, pinholes are closed, mis-wound faces and inside-out floating shells are corrected. The installed bytes pass the repository geometry gate for all eight meshes (it passed for 1 of 8 before: boundary 0, non-manifold 0, no flipped faces at 0.0005, 0.001 and 0.002).
- A coherent atlas: 65 to 179 planar islands (was 4,300 to 9,400 fragments), the provider base colour, roughness, metallic and normal re-projected per texel through the old UV, graded into field-uniform regions with the high-pass detail of the provider texture kept, 512 BC1 diffuse and BC3 normal and specular with ten mips (header-checked), specular from the vanilla-calibrated classes (cloth G 40-90 and A 25-50, dry skin G 80-130 and A 30-70, helmet steel and wet flesh only inside their masks) with A mean 52 to 56 and p95 70 for the dry units (the zombie helmet and the parasite tentacles carry the higher classes), normals repacked into RRxG with G/A standard deviation 16 to 23 and mean tangent tilt 0.11 to 0.21.
- Eight actions per unit with sign-continuous quaternions in the exported bytes (exporter-level flips repaired by `anim_signs.py` and re-gated), every world joint step inside the recalibrated per-role limits (idle 0.10, locomotion 0.36, other 0.41 u per frame and 10, 25 and 30 degrees, worked to with an 8 percent margin in Blender and re-checked on the exported bytes), loop seams closed, and the lowest vertex at 4 mm in every frame except the intended leaps. Every role's exported `.anim` was reimported through the adapter and the final bytes were gated again after the sign repair.

### Gate recalibration

The 0.25 u per frame world joint limit measured vanilla `GER_infantry_moving_rifle` as blocked (peak 0.314 at the right toe, 21.9 degrees per frame). Measured on the installed `GER_infantry_*` clips with the exact `GER_infantry.mesh` skeleton in source-mesh units: walk 0.314 u and 21.9 degrees, idle 0.052 u and 6.0 degrees, strikes 0.295 to 0.353 u and 21.3 degrees. `role_motion_limits` now returns 10 degrees and 0.10 u for idle, 25 and 0.36 for move and retreat, 30 and 0.41 for every other role (about 1.15 times the vanilla maximum of each family). The numbers are recorded in `animation_delivery_checks.py`, its test and the skill reference; nothing was waived.

### Per-unit results

| Unit | Islands | Closed mesh | Diffuse luma p50 | Actions | Ground contact (all roles) |
|---|---|---|---|---|---|
| zombies | 106 | 11 shells | 80 | 8 pass | -0.009 to 0.024 |
| infected_zombies | 136 | 33 shells | 68 | 8 pass | 0.003 to 0.012 |
| rabid_zombies | 84 | 9 shells | 67 | 8 pass | 0.004 to 0.188 (death) |
| parasitic_zombies | 179 | 65 shells | 83 | 8 pass | -0.034 to 0.022 |
| mutant_zombies | 65 | 1 shell | 88 | 8 pass | 0.004 to 1.74 (death) |
| undead_zombies | 120 | 29 shells | 60 | 8 pass | 0.004 |
| necrotic_zombies | 97 | 10 shells | 83 | 8 pass | 0.004 |
| demonic_zombies | 88 | 2 shells | 67 | 8 pass | -0.007 to 1.02 (leap) |

The installed-byte audit (`installed_audit.py`, run 11 Oct after the last model install) reads 8 of 8 geometry passes and 56 of 64 action passes; the eight `move` roles read `needs_review` there only because the offline audit has no sole measurements. The adapter measured them during export (`foot_contacts`), and each unit's move is declared a stagger gait below.

### zombies
Fixed: fragment mottle replaced by an olive-grey uniform with readable pockets and webbing, grey-green skin, dark helmet; 129 non-manifold edges and 67 pinholes closed; the idle is no longer a statue (authored weight shift, head turns, shoulder twitch and an arm lift over 11.3 s, seam 0); both hands curl into the attack reach peaks (frames 24, 46, 74).
Remaining: the shared contact pool sound (blocked, below).
Evidence: `docs/assets/002_zombie_outbreak/models_3d/zombies/export/wp3d/wp3_report.json`, checkpoints `wp3_01_geom_uv.blend` and `wp3_02_actions.blend`, previews `blender/previews/wp3/`.

### infected_zombies
Fixed: near-black coat now shows lapels and weave (luma 66 target), matted hair, grey feverish feet instead of white blobs; 312 non-manifold edges closed; the attack arm no longer holds vertically above the head (it reaches at shoulder height with a 15 degree torso twist); defend and training end on their first pose; floor penetration of up to 13 cm removed.
Remaining: coat-hem weights toward the thighs, idle scratch clearance from the skull, cough, retch and spit sources (blocked).
Evidence: `.../infected_zombies/export/wp3c/wp3_report.json`.

### rabid_zombies
Fixed: suit lapels, shirt and pale hands and face readable; the idle is a five-second standing frenzy (head jerks, breathing, weight shift, hand twitches) instead of a frozen mid-stride pose; the move loop closes at its first pose; the rear leg is clamped to 20 degrees behind the hip so the back kick is a lunge; wrist weights keep at most two adjacent influences (688 vertices cleaned); attack floor penetration of 18 cm removed.
Remaining: a dedicated shriek and death gasp (blocked), blood detail on hands and chest.
Evidence: `.../rabid_zombies/export/wp3c/wp3_report.json`.

### parasitic_zombies
Fixed: the tentacle mass reads as glossy purple-pink wet flesh against dry grey skin and dark clothes; 554 non-manifold edges closed (the open tube ends are now closed shell); the idle gains breathing, head sway, a shudder and a hand twitch; the death runs 4.0 s instead of 9.4 s with the landing sound at 3.6 s and the second gurgle at 1.4 s; wrist weights cleaned (586 vertices).
Remaining: the tentacle rig and whip lag. The tubes are skinned to the shoulder, arm and spine bones in the provider weights and are fused to the host surface, so no tube set can be separated by geometry alone; building the chains needs per-tube identification that was not available. The arms-out beat of the attack (frames 55 to 65) is smoothed but not replaced. Wet whip and suction sounds (blocked).
Evidence: `.../parasitic_zombies/export/wp3b/wp3_report.json`.

### mutant_zombies
Fixed: diffuse median 88 (was 156) with veins and wounds kept, normal in the vanilla band; six-second hunched idle with a head sweep and a sniff beat, closed at both ends; both hands flex into the attack reach peaks; geometry closed.
Remaining: the attack keeps the provider lunge (the 2026-10-06 reauthoring attempts stay rejected); two roars, a death bellow and a breathing loop (blocked).
Evidence: `.../mutant_zombies/export/wp3/wp3_report.json`.

### undead_zombies
Fixed: black suit with lapels against grey-green skin and glowing eyes, specular alpha mean 52 (was 114); the idle is no longer a statue (breathing, head sway, weight shift, hand twitch and an arm lift over 10 s); every action grounded and gated.
Remaining: armpit and hem weights, knees in the attack lean, two more moan takes (blocked).
Evidence: `.../undead_zombies/export/wp3c/wp3_report.json`.

### necrotic_zombies
Fixed: dirty ochre rags distinct from the green-grey skin, specular alpha mean 56 (was 122) so the white specular lines and wet chrome are gone; every action grounded at 4 mm and gated.
Remaining: rag-strip and far-thigh weights.
Evidence: `.../necrotic_zombies/export/wp3c/wp3_report.json`.

### demonic_zombies
Fixed: the attack is a standing double claw slash (right claw peaks at frame 34, left at frame 76, each after a knee crouch and a wing flare) authored on the idle pose, hips grounded, no sprawl and no 4 u hand jump; the support attack crouches, leaps (hips up to 5.06 u), and slams at frame 49; the idle gains breathing, head sway, wing flutter and claw flex; the closed shell shows the skull face, ribs and wing struts with readable membranes; wrist weights cleaned (353 vertices); attack and support events follow the new slash and landing frames.
Remaining: wing-membrane reblending and elbow placement. Edge growth above 0.3 u is 8 and 23 at the two slash peaks (acceptance: under 20 at the strongest) but still 170 at death frame 46 and 75 at training frame 25 (acceptance: under 50), so the wing strut reweighting is not done. The new attack and support attack are the first authoring pass; the torso pitch at the landing is keyed at 30 degrees on one spine bone and was not measured separately.
Evidence: `.../demonic_zombies/export/wp3c/wp3_report.json`, `blender/previews/wp3/after_attack_standing_double_slash.png`.

### Simplifications, omissions and blockers

- Move gait: the zombie shambles are not 1.0 to 1.5 s two-plant strides (measured plants: zombies L1/R4 over 4.9 s, infected one right plant, and similar for the others). Each unit's `validation/animation_delivery_policy.json` declares `humanoid: false` for `move`, so the stride-count gate is not applied; the plants remain measured in every delivery record. Re-cutting each move to a two-plant stride is open if the shamble should become a regular walk.
- Sound: the shared contact pool, infected cough, retch and spit, rabid shriek and death gasp, parasitic wet whip and suction, mutant roars and death bellow, and demonic idle growls all need recordings that are not in the archived packs (the 24 artisticdude takes are all used), and downloads were not granted. No sound was synthesised and no sound file or definition changed in this tranche. `paleogenetic_creature.asset` still calls the zombie soundeffects by name (they are unchanged); WP5 owns separating them.
- Capture: the stationary re-filmed idle and attack clips were not made; no game was launched.
- The preview images in the job folders are Blender workbench renders (provider PBR approximated by one material), not engine renders.
- Commit messages for undead (specular alpha mean 52) and necrotic (rag luma) carry slightly different numbers than the measured values above; this report is authoritative.
- Floor penetration of 3 cm remains on parasitic (min -0.034) and 0.9 cm on zombies; the rabid death floats 0.19 u at its end.
- The mesh export gate needs `job.yaml`; minimal intake files were written for parasitic, necrotic and demonic.

Working scripts and the grade and action configurations are archived in `docs/plans/unit_fix_2026-10/wp3_tools/` (the shared parts are in `.tools/3d_pipeline/`). Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-shared-git-commit`; no skill was created, the 3D skill reference gained the calibrated limits and the exporter-sign rule.


## WP3 execution on 2026-10-06

Package status: **incomplete**.
The user-authorized scope is every WP3 ticket, with no paid Meshy tasks, no new sound downloads and no desktop or game launch.
The sections below this execution record describe the earlier shared pipeline tranche, whose mesh/action measurements remain a baseline rather than model acceptance.
The missing requested `unit_s3_report.md` was replaced for reference reading by the existing `pipeline_report.md`; no absent report or tool route was treated as successful evidence.

The host-restart reconciliation verifies that all 72 installed mesh/action files still match the latest hash-bound audit: one geometry pass, seven geometry blockers, seven action passes and 57 action blockers.
`wp3_evidence/restart_recovery_20261006.json` records the actual-byte comparisons and the fresh reference-search failure (`Transport closed`).
The mutant attack candidates stay outside runtime; the undead source correspondence and native AO tranche is archived, and base-zombie geometry review is continuing in an isolated source branch.
The initial nine WP3 commits and the subsequent focused source/evidence commits were recovered from Git; pre-existing dirty zombie intake/blocker files remain reserved for their original owner.

The focused presentation commit is `dbbd5444b`: all eight death blood bursts drop `keep_particle`, the undead attack grunt moves from 2.80 to 2.45 seconds, and the necrotic fall cue moves from 1.30 to 3.30 seconds.
Shared idle volume changes from 0.22 to 0.42, shared movement from 0.34 to 0.50, and parasitic feeding from 0.45 to 0.55, matching the WP3 ticket values.
An independent Luna review found no missing cue or WAV reference in this scoped diff.
Before/after source and lint evidence is in `wp3_evidence/before/` and `wp3_evidence/after_entity_timing/`.
The same 64 states retain the same action hashes; the eight impulse-particle findings clear, taking the total from 54 to 46.
Remaining findings at that boundary are 11 strongest-motion offsets, 15 missing contact proofs, 10 one-shot voices on repeating states, three samples longer than their state cycles, and seven overlaps.
Motion peaks and joint heights are synchronization evidence, not proof of a deformed hand or body contacting a surface.

Moan 01 has an exact source binding to ianzazz's archived CC0 `zombienoise1.ogg` and a passing installed derivative.
Its measured installed-byte loudness changes from -40.5 to -20.2 LUFS; peak changes from -20.848 dBFS to -1.011 dBFS, true peak is -1.0 dBTP, duration changes from 2.116848 to 1.616848 seconds, and inner loop-edge mismatch improves from 16.234 to 2.769 dB.
The previous runtime bytes remain available as the hash-bound local Git LFS object, inspected in `wp3_evidence/moan01_before_metrics.json`; the installation receipt and after inspection are linked from `wp3_audio_repair_handoff.md`.
Moan 03's exact CC0 source binding is resolved; three cropped candidates failed their edge or short-clip loudness gates.
One source-only two-copy, 40 ms crossfade candidate now passes the shared loop gate at -19.9 LUFS, -3.7 dBTP and 0.682 dB edge mismatch, but its peak is -3.712 dBFS and its repeated phrase has no listening approval.
It remains staged and the installed moan 03 is unchanged; `moan03_crop_repair_receipt_20261006.json` preserves the exact crops, joined source, internal seam measurements and rejected attempts.
Moan 02 retains its accepted global-mastering bytes.
Audio mastering proves file delivery; audible role and live playback acceptance remain separate.
The resumed peak-limiter commit `6e393c848` replaces the accepted moan 01 master with a source-identical-duration derivative at -20.5 LUFS and -3.0 dBFS sample peak / -3.0 dBTP.
Its bounded recorded-sample attenuation is 1.988527 dB, and the loop-edge delta remains 2.769 dB.
Current runtime SHA is `76661F92D59F934FD5D9AA66EFDB401B2718F674A8AA5053BDCFBCB63A33C0CE`; `wp3_evidence/moan01_peaklimit_install_20261006.json` and the fresh installed inspection bind that value.
Two additional source-labeled zombie moans remain staged, not installed.
The low-breathing OGG derivative passes output-file checks but is held: the aligned archive WAV has 19,704 near-rail samples and 1,101 plateau runs spanning 0.060136-4.105533 seconds, and those intervals map into the candidate.
Lossy decoding does not establish repaired source peaks; the near-rail-free tail is not proven to contain a complete breathing cycle.
The exact original/candidate hashes and interval mapping are in `mutant_breath_source_clipping_alignment_20261006.json`; no derivative is promoted on the alternative encoding alone.
One later source-only candidate isolates the original WAV's rail-free 4.200-5.400-second interval and uses a 250 ms recorded head/tail crossfade.
Its 0.950-second output measures -20.0 LUFS, -3.413 dBFS, -3.4 dBTP and 1.033 dB inner-edge mismatch; source-envelope evidence suggests a swell but cannot establish a complete perceived breath or mutant-role fit.
This clean-interval candidate remains uninstalled and unlistened; exact source, crop, master and output hashes are in `mutant_breath_clean_cycle_receipt_20261006.json`.

Shared footsteps 03–06 isolate complete transients from their original CC0 recordings, with short releases; footsteps 01–02 already fit the shortest interval.
The final six paths remain distinct recorded takes, at the shared -6 dBFS peak target, with a maximum duration of 0.17 seconds.
The movement cue has no random start delay, and its retained ±12% rate variation keeps the longest sample below 0.194 seconds at the slowest rate.
This targets the six movement overlaps whose shortest contact interval is 0.20 seconds without shifting the entity's authored plant events.
Per-file preimages, source offsets, after hashes and mastering inspections are recorded in the audio handoff.
The fresh `wp3_evidence/after_audio/` lint reads the installed files and clears all six movement overlaps: the 64 states retain 40 findings, with only one sample overlap left, the undead eating cue.
The earlier 46-finding count remains the intermediate particle/timing boundary.
The undead support_attack uses the complete existing feeding recording once at 1.50 seconds, spanning both hands-to-mouth movements rather than restarting it at 3.1333 seconds.
The final `wp3_evidence/final_feeding_review/` lint has no sample-overlap finding across the 64 states and retains 39 other findings.
No sound source or waveform was shortened for that feeding correction.
Commit `f5b125d45` completes the 40 ms release fade on steps 05 and 06 while retaining their 0.100/0.170-second durations and -6 dBFS peaks.
Their installed RMS values are -25.118/-21.473 dBFS; these short files do not yield a useful integrated-LUFS reading.
The same minimum 0.20-second contact gap and slowest-rate duration bound remain valid.
The recovery grunt starts at 4.0333 seconds, leaving the complete feeding cue clear even at the slowest retained 0.94 playback rate, which finishes near 4.020 seconds.
The demonic scream and attack pools each contain three variants after wiring two extra pitches of the classified scream recording and one lower pitch of the classified attack recording.
The new files are `demonic_scream_low.wav`, `demonic_scream_high.wav`, and `demonic_attack_low.wav`, all passing the shot-mastering gate at -3 dBFS peak.
These are the pitch variants explicitly allowed by the demonic ticket: the scream pool still has one underlying recording, and the attack pool has two.
They are not presented as additional independent takes.
Two lower-register growl-loop attempts fail the recorded-edge gate; the dedicated demonic idle/defend pool is still open.

The audio/presentation tranche is committed as `dbbd5444b`, `79a62a4c5`, `45582d8ba` and `6e393c848`.
Two mutant attack snarls are installed and wired from the original classified CC0 takes 4/7, with -5/-7 semitone and formant shifts, -3 dBFS peaks, original 14.966 ms onset, and durations within one sample of the originals.
An own two-take mutant footstep cue uses EQ-only derivatives of the accepted short recordings; it preserves 0.100/0.170-second lengths, zero inspected onset and the 40 ms release.
All six move/retreat event times remain fixed; the slowest 0.88 sound rate gives a maximum 0.193182-second sample against the closest 0.2667-second gap.
The fresh eight-model, 64-state source audit retains 39 existing findings and has no missing sound reference or sample-overlap finding.
Live listening, source-contact proof and the broader action/voice requirements remain open.
The mutant model tranche is committed as `f0987fd93` after parent review, with the remaining mutant requirements still open.

### Paced recurring idle and defend voices

Four dedicated ambient aliases reuse the existing moan, rattle and gurgle families, with their gain and pitch behavior preserved and 4-8-second randomized pauses.
They replace ten one-shot entry cues across all eight models while preserving their state entry `trigger_once` behavior; impact, attack, selection and the legacy WP5 shared identifier retain their existing behavior.
The current 64-state comparison clears all ten one-shot/silent-state findings: 39 findings become 29, with zero sample-overlap or missing-cue findings.
All 44 current local WAV paths and the installed mesh/action hashes remain unchanged.
This repairs recurring source wiring; actual cadence, state-exit stop/fade and crowd balance require orchestrator listening.
Existing source-level and take-count gaps remain open; no new recording is claimed.
Evidence is `wp3_evidence/idle_ambient_fix_20261006/parent_comparison.json`; the installed definition and entity changes are committed as `808a40c5c`.

### Installed mutant geometry, idle and two material maps

- The mesh removes four source-reviewed spur triangles and their eleven loose edge records and ten orphan source vertex records.
Triangles change from 31,282 to 31,278; positional boundary/non-manifold edges change from 8/4 to 0/0.
All retained UV corners, skin weights, material assignments and normals are preserved; source height is 7.3518238, with the existing entity scale 0.8.
All 24 bone names, indices, parents and inverse-rest components match the previous installed mesh exactly, so unchanged actions remain compatible.
- The six-second idle has two breathing phases, a head sweep/sniff and wrist motion on the same mutant rig.
It has 180 frames at 30 FPS; decoded quaternion continuity, local/world speed, root travel and the zero-degree/zero-unit loop seam pass with the explicit humanoid idle profile.
Stride-plant measurements remain unmeasured and are not an idle gate; the plan's filmed peak-motion acceptance still needs the orchestrator.
- The diffuse restores the immutable provider texture without the shared gamma lift and grades its occupied median to 86.740, within the 80–95 target, from the previous installed median 156.610.
Existing vein/wound detail is retained; production delivery is 512 DXT1 with ten mips.
- The normal preserves provider detail through a reviewed 1.15× tangent-strength adjustment with vector normalization and no noise or generated detail.
Decoded G/A standard deviations are 15.2255/15.2545, mean tangent tilt is 0.12356, and production delivery is 512 DXT5 with ten mips.
The untouched provider repack failed the normal gate and remains separate evidence, not an installed alternative.

Installed mesh SHA is `e16d492de38c49af4a73aea30c8657ae0d6a091c59542ceb95817eb325ed4e07`; idle SHA is `9480e6de7eacbb00b172319c2c868e29ad3f8fdd23eac65174322f5bdfc96bf1`.
Diffuse SHA is `ecd5bb5e4aed1c2114158c54204c2585e8ef395f890419e389a07e0dff53a2f9`; normal SHA is `ed43b774293d559f1300ba7a3318260f2dd6d2aa45e8c1ea4436bcae8465564a`.
Native reimport binds the exact mesh/idle bytes; the parent separately reviewed the final front and quarter surface previews, including the darker diffuse and stronger normal.
The adapter's BC1 material-bind limitation required a preview-only BC3 wrapper with identical decoded RGB across all ten mips; production stays BC1.
Its nested 279-character normal path was copied, hash-identically, to a 216-character job-local path for Blender access.
These are preview representation/path measures, not runtime source substitutions or relaxed gates.
The complete mutant repair `job.yaml` was created after an absence check to supply required delivery metadata.
Installation receipts are `wp3_evidence/mutant_parent_install_receipt.json`, `mutant_candidate_parent_review.json`, and the texture worker's approved-only CAS manifest.
The fresh installed-byte audit reads all eight current meshes and 64 registered actions: one geometry pass, seven geometry blockers, seven action passes and 57 action blockers.
Its compact hash-bound evidence is `wp3_evidence/installed_model_audit_compact_20261006.json`; the raw per-frame reports remain in the local audit directory.
The unchanged mutant source normals still have 7,161 positional split-normal groups; native 60-degree smoothing state and visible faceting require a separate source check and are not proven by removing the four spurs.
The existing specular map remains visually glossy and cannot satisfy the jaw-wetness/skin recipe through the available six-class validator; it remains an explicit model requirement.

### Rejected mutant attack reconstruction

The current sparse phase checkpoint has 7,680 keys rather than the source 28,800, with the exact strike windows at frames 17-19 and 77-88 and unchanged accepted mesh/rig/weights/UVs.
Its actual export still has 51 translation violations outside those windows; the largest is RightHand at frame 95, 1.39588 units per frame.
Native reimport against the accepted mesh confirms ground penetration of -0.06802 units at frame 60 and a backward chest/head arch in the phase views.
The source sweep finds 32 penetrating frames, so matching loop endpoints and zero quaternion sign flips do not make this action acceptable.
The material binder also fails action retention through save/reopen, and the native previews remain magenta; the exact maps are staged but rendered material binding is unresolved.
The animation SHA is `8b314481fe933da7aed4d483d360bf5c898b04c5bfe24c578a6e3f4a951ef5c5`; it is rejected, uninstalled and separate from the unchanged runtime attack.
The source checkpoint, decoded report and native proof remain in the mutant job; the phase receipt explicitly states that its metadata was reconstructed from intact measured inputs after a failed write.
The earlier body-eased export (`dd27c0d3a7448d87a5f9e234986127402f8b6070012edba77f2fe09b920ff28c`) has its exact native reimport proof at `validation/reimport_wp3_mutant_attack_bodyeased_nativeproof_20261006.json`.
Its five sampled bounds stay at +0.00398269 to +0.00399523 units, but the 207-finding delivery rejection and backward arch remain; readable reconstruction does not make the action acceptable.
Actual role repair remains open, with no wider strike exemptions, static substitute or action alias.

### Installed demonic diffuse and provider-normal repack

The parent reviewed matching current/final front and quarter rest-pose views before publishing the two maps through `current_mesh_skin10_manifest.json`.
Decoded current-mesh skin/head means change from 90.2978/96.0626 to 80.9032/86.1547, reductions of 10.404%/10.314%.
The provider-source islands are dilated by 12 pixels before grading; bilinear vertex samples below luminance 12 change from 6.83% to 0.90083%.
Nearest samples remain 1.825%, so the sampling method is explicit and this is not a claim that every diagnostic passes.
The 512 DXT5 normal has ten mips, G/A standard deviations 19.709869/19.358717 and mean tangent tilt 0.167045.
Diffuse SHA is `319386BAE79A81B50CC5AFA9463CE2BF57B5463C321054DB440E06CB0094926D`; normal SHA is `ADDB26AEF0993F1E6D4A84B48AD1D42F86D4F8E467A864F7A61604DDA77F9C73`.
The parent receipt is `wp3_evidence/demonic_parent_install_receipt_20261006.json`.
This is a bounded current-mesh material improvement; the unchanged specular, rig/weights, geometry and action defects remain open.
Final geometry, UV or weight changes require mask rebinding and re-QA against the original grade basis, without darkening the already graded map again.

### Undead source regions and native AO

The source/runtime correspondence maps all 30,474 triangles one-to-one with identity UVs at position precision 1e-5 and UV precision 1e-7, despite 40,875 source versus 42,103 exported vertex records.
The reviewed source views distinguish skin/bone, coat/trousers, shirt/lining, hair, eyes and leather shoes; the first head-only masks are rejected for patchy skin coverage, hair boundary errors, missed eye lenses, 278 ambiguous faces and 51 cross-class UV texels.
No rejected mask is used for grading and no undead runtime map changes.
The independent native Cycles AO bake returned FINISHED on a source-preserving rest-pose working checkpoint, with the existing UVMap, four active target slots, CPU/128 samples and target-only visibility.
Its 512 linear scalar map has 175,845 occupied pixels, mean 0.4808402, median 0.4235294 and p95 1.0; source geometry, UVs, skin weights, rig and action inventories match after save/reopen.
Raw PNG SHA is `31c94862a7a72c70aee2a0c5f5fa8578094178c03fdbfd1d556e1194d5e0ad10`, scalar preview SHA `7434a9f799f4af17bd578379a6a31cba453b65ad3aa0359495c59d99c6884932`, and checkpoint SHA `a2ec19b34ca139350c114c4355775cf800d10d5207e075a4da0be9dc0f2b961a`.
Parent acceptance is limited to real native AO source evidence on this geometry/UV basis; the margin-zero output needs occupancy padding before texture use, and geometry/UV repairs require rebaking or rebinding.
Material-region acceptance, source-based diffuse/specular work, topology/weights/actions and runtime appearance remain open.
The handoff is `wp3_undead_model_handoff.md`; the bake and recovery receipt is `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/ao_20261006/ao_bake_receipt_20261006.json`.
Commit `676b50952` preserves the exact source views, correspondence, rejected masks, native AO and working checkpoint without changing undead runtime bytes.
Commit `7794655c0` closes the missing native proof for the rejected mutant body-eased export; its motion rejection remains unchanged.

## Per-ticket work and remaining acceptance

| Model | Delivered presentation changes | Requested model repair and acceptance still open |
|---|---|---|
| zombies | Blood burst lifetime; shared idle/movement gain; recovered moan 01. | Coherent head/torso/arm/leg/helmet UVs and field-uniform bake; region specular; authored idle shifts and claw curls; 129 positional non-manifold edges; seven blocked action roles. |
| infected_zombies | Blood burst lifetime; shared idle/movement gain; recovered moan 01. | Coat/skin/feet bake and masks; chest-height attack at 1.17 seconds; defend/training closures and skull clearance; coat-hem skinning; 312 non-manifold edges; eight blocked roles; actual cough/retch/spit sources. |
| rabid_zombies | Blood burst lifetime; shared idle/movement gain; recovered moan 01. | Standing four-second frantic idle; move seam; forward lunge replacing back kick; wrist/forearm skinning and suit bake; 112 non-manifold edges; seven blocked roles; distinct shriek and death gasp. |
| parasitic_zombies | Blood burst lifetime; feed gain 0.55. | Actual tentacle rig, weights, idle and whip lag; forward lash/grab; defend closure and death at most 4.5 seconds; tube caps and duplicate removal; 554 non-manifold edges; seven blocked roles; wet lash and suction sources. |
| mutant_zombies | Blood burst lifetime; recovered moan 01; reviewed four-spur mesh repair, calm closed idle, diffuse median 86.740 and source-detail normal; two own pitched/formant-shifted snarls and two short EQ footfalls wired. | Skin/jaw specular recipe; attack claw curls and seven other action-role gates; filmed idle motion target; two roars, distinct death bellow, and own breathing loop; live sound fit and balance. |
| undead_zombies | Blood burst lifetime; attack grunt at 2.45 seconds; shared movement gain; one complete feeding cue instead of overlapping restarts. | Source-based suit/skin grade and gloss masks; substantial idle; plant/training easing and retreat seam; attack knees and armpit/hem weights; 330 non-manifold edges; seven blocked roles; two extra moan takes. |
| necrotic_zombies | Blood burst lifetime; fall cue at 3.30 seconds; shared movement gain. | Bone/teeth gloss masks, distinct skin/rags; foot plants, arm sweep and transition easing; retreat seam; rag/thigh skinning; 73 non-manifold edges; seven blocked roles. |
| demonic_zombies | Blood burst lifetime; shared idle/movement gain; recovered moan 01; three-variant scream and attack pools; reviewed current-mesh skin/head grade, 12-pixel padding and provider normal installed. | Forearm/hand and wing skinning/joints; standing slash and leap landing; death, training, idle, retreat and plant repairs; final region-mask rebind and specular; 36 non-manifold edges; seven blocked roles; own idle/defend growls and retiming after the authored action repairs. |

The seven other models' baseline counts remain tied to unchanged installed mesh/action hashes; the mutant's updated installed hashes and measurements are recorded above and in the current WP3 inventory.
They are unresolved acceptance findings, not a waiver or a declaration that all tickets were repaired.
All 24 current model maps have shared compression/mip delivery, but source material/detail repairs and the WP3 256-pixel specular targets are still part of model work.

## Orchestrator live checks for this tranche

Use the existing showcase setup saves for batches 2 and 3, paused, at 1920×1080 and UI scale 1.
The exact model positions in `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/plan.json` are: zombies 12374, infected 12728, rabid 12791, parasitic 1562, mutant 1954, undead 2019, necrotic 3834 and demonic 5038.
Lock the crop to the known custom entity position and keep attacks stationary, or set the in-point after engine repositioning.

- Exercise death for each model: expect one brief hit burst rather than a retained emitter.
For necrotic death, expect the body-fall cue at 3.30 seconds and no early fall sound at 1.30 seconds; inspect the actual body contact, since the decoded hips are 1.646 source units high at 3.30 seconds.
- Capture two undead attack cycles: expect the grunt at 2.45 seconds alongside the feeding/grab recovery, with no grunt event at 2.80 seconds.
- Exercise undead support_attack: expect one feeding cue starting at 1.50 seconds across both mouth movements and a recovery grunt at 4.0333 seconds.
There must be no restart at 3.1333 seconds and no overlap at the slowest sampled voice rate.
- Watch the mutant idle for three full six-second cycles from front and quarter views: expect slow breathing, a head sweep/sniff and claw motion with no height snap at the seam.
Inspect its neck, shoulder and left toes for the removed spurs; compare the darker body and retained vein detail at the close and map-zoom crops.
Measure the locked-crop peak-motion target 0.8–3.0 on the re-filmed idle; the parser and previews do not establish that filmed metric.
- Leave each idle for at least 30 seconds and exercise the base and demonic defend states: expect recurring voices with 4-8-second pauses rather than one voice followed by permanent silence.
Switch each test unit into move, attack, training and death and check that the ambient cue stops/fades correctly without persisting over an unrelated state or piling up.
Timed attacks, grabs, impacts and footsteps must remain one-shot cues at their existing events.
Then exercise movement and parasitic feeding at the same camera distance as an adjacent vanilla unit.
Expect the ticketed gains and louder moan 01; held takes and one-shot/repeating-state defects remain identified in the audio handoff.
- Exercise attack, defend, support_attack, move, retreat, training and death for each model before closing its geometry/action ticket.
Inspect the ticket-specific loops, holes, wrists, coat hems, tentacles, wings, crops and map-zoom texture behavior against the thresholds in the plan.

All eight models require stationary idle/attack re-filming as `SC_<model>_idle.mkv` and `SC_<model>_attack.mkv` after model acceptance.
Refresh `tools/unit_sounds.py`, `tools/anim_durations.py`, `project/showcase_v1.py`, and the audio/credits build from the same trailer timeline before the final video render, as documented in the showcase README.
No game or capture session was launched here.

## Simplifications, omissions, and blockers for this execution

No substitute model, generated production rig/weight/action, synthetic sound or unauthorized source download is accepted.
Open model and audio requirements are listed individually above and in the two worker handoffs; WP3 is not presented as complete.
The root's earlier tool list lacked the HOI4 reference routes; the continuation exposes their schemas but live `reference_context` and `reference_search` calls fail with `Transport closed`.
The exact retry responses are in `wp3_evidence/root_reference_route_retry_20261006.json`; direct local source paths, line spans, revisions and the installed-documentation chapter gap remain in `wp3_evidence/local_references.json`.
The custom model worker's runtime does expose and successfully call the reference/context/search/read/source-lookup routes; its current schemas, responses and source revisions are retained in `wp3_model_repair_reference_evidence.json`.
The source-lookup query returned no indexed infantry definition, so the installed vanilla definition and calibration were read directly.
No event, decision, focus, scripted-GUI, probability, on-action or gameplay source is changed by this tranche.
The footsteps' conflicting -3/-6 dBFS targets and per-model/shared specular conflicts are recorded in the event's `agent_decisions_2026-10-05.md`.
The preserved global -6 dBFS footstep contract does not count as satisfying the conflicting -3 dBFS instruction.
Source-role gaps retain their old cues and concrete recording needs; staged candidates do not count as wired takes.
The paleogenetic creature still inherits movement and feeding effects from this package; `wp3_to_wp5_sound_dependency_handoff.md` names each call and the WP5-owned separation dependency.

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`.
The official `skill-creator` guidance was used for a small 3D skill update, committed as `e185e3078`.
It records the verified factory-startup Lab command, importable extension-module names, argument ordering and task-owned worker/memory evidence.
The follow-up skill safeguard, committed as `9ec06f479`, requires explicit UTF-8 and validated sibling metadata writes, labels reconstructed evidence, and selects pose rigs through the working body modifier/action slot.
No new skill was created.

Disposition: `implemented` for this documentation handoff; package mesh/action reconstruction, visual acceptance, final entity wiring, and audio install remain open where the measurements below show gaps. The authorized package scope comes from the user-authored unit-fix plan, SHA-256 `1939b400cba160c6d4903e37952e8e55efdb1bfeacf0b4ab061e89c8792c79b2`.

Package models: zombies, infected_zombies, rabid_zombies, parasitic_zombies, mutant_zombies, undead_zombies, necrotic_zombies, demonic_zombies. The full per-model map, DDS, mesh, action, topology, reimport, and entity-lint evidence is in `docs/plans/unit_fix_2026-10/per_model_delivery_metrics.json`.

## Shared delivery facts

Across the shared pipeline, 119 unique active DDS targets are installed (41 diffuse, 39 normal, 39 specular), all 512x512 BC1/BC3 with ten mips. This package references 24 unique DDS paths (8 diffuse, 8 normal, 8 specular). Eighty targets used compression-only conversion and 39 normals received `packed_normal_cleanup` (R=existing G, G/A preserved, B=0). The reviewed T062 mip-7 repair replayed the same QA gates. Unique archived input bytes total 470,825,856; installed bytes total 34,446,104. The item-level JSON records each target's exact before/after dimensions, fourCC, mip count, bytes, SHA-256, decoder QA, and semantic gate results. Runtime cleanup archived nine genuinely unreferenced DDS files (37,749,888 bytes); active shared-variant maps were retained. The global tranche changed no runtime `.mesh` or `.anim` bytes and rewrote no model geometry or actions; native imports created proof checkpoints from the installed mesh bytes.

The material semantic outcomes across this package's unique DDS paths are 4 passed, 4 failed, and 16 unresolved. Normal-map convention outcomes are 5 passed and 3 failed after packed-normal cleanup; cleanup preserves occupied G/A source detail and does not synthesize detail for flat maps. The full decoded per-map statistics and failures are recorded in the JSON.

All 8 model registrations have unchanged installed `.mesh` SHA-256 and unchanged registered `.anim` SHA-256. Each has a native geometry-only Blender reimport checkpoint keyed to its installed mesh SHA. These checkpoints establish readable geometry and stored evidence; `visual_material_acceptance` remains false. Geometry gates are 0 pass and 8 blocked for this package; registered action checks are 6 pass and 58 blocked.

The package's 64 baseline entity states have not been edited by the shared pipeline tranche. Entity lint results are pre-edit evidence; no entity, sound-definition, or particle-definition changes are part of this delivery.

## Per-model reconciliation

| Model | Original triage concern | Installed mesh SHA-256 | Bones / action FPS / entity scale | Geometry gate; boundary edges at 0.0005 | Action audit | Unique DDS paths and normal QA | Entity lint baseline |
|---|---|---|---|---|---|---|---|
| `zombies` | Thousands-of-islands fragment atlas renders the uniform as a grey mottle; idle moans at -40 LUFS and steps 15-20 dB under vanilla. | `7dbebef2ba67468974dd82544dc9d56ee5fcf64bd84078065131c8db38a5efbf` | 24 / 30 FPS / chaosx_zombies_entity=0.8 | blocked; 129 / 129 boundary/non-manifold at source tolerance; same-direction edges 5 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 8 states, 8 pre-edit findings |
| `infected_zombies` | Near-black coat atlas with bright white feet; no cough, retch or spit for the retching support attack and coughing training. | `e93f5b323205b40a4828d2de47dd4cd04ec8455dc809a872160b26b40af5f536` | 24 / 30 FPS / chaosx_infected_zombies_entity=0.8 | blocked; 201 / 312 boundary/non-manifold at source tolerance; same-direction edges 12 | 0 pass, 8 blocked; roles: idle, move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 8 states, 8 pre-edit findings |
| `rabid_zombies` | The idle is a frozen mid-stride walk pose; the move loop pops every 2.63 s. | `391615a40b786a2320b996410b1fdd29ef87cb940eab14cd4df0bf2338c82b0f` | 24 / 30 FPS / chaosx_rabid_zombies_entity=0.8 | blocked; 81 / 112 boundary/non-manifold at source tolerance; same-direction edges 7 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 8 states, 14 pre-edit findings |
| `parasitic_zombies` | Mannequin idle with a frozen rigid tentacle lump; 554 non-manifold edges and open tentacle tube ends. | `533aec9b60201ec5e4412e10b5fc5236baeedd46e0c13b22568110bab448dd07` | 24 / 30 FPS / chaosx_parasitic_zombies_entity=0.8 | blocked; 296 / 554 boundary/non-manifold at source tolerance; same-direction edges 23 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 8 states, 3 pre-edit findings |
| `mutant_zombies` | Diffuse at twice vanilla luminance (p50 155): a bright white plastic figure; the idle snaps 25% of its height every 7 s. | `25f0604a7a7ea4a555edfb1f4415bb542c2174d4d2955ed2866f615b8e5ec8a6` | 24 / 30 FPS / chaosx_mutant_zombies_entity=0.8 | blocked; 8 / 4 boundary/non-manifold at source tolerance; same-direction edges 0 | 0 pass, 8 blocked; roles: idle, move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 0 pass/1 fail | 8 states, 7 pre-edit findings |
| `undead_zombies` | Gloss alpha 114 (vanilla 44) makes skin and suit grey plastic; statue idle; inaudible steps. | `de3f5f66b6d724221200a883941ebcda649d880a07780f71d1820c7a2c301052` | 24 / 30 FPS / chaosx_undead_zombies_entity=0.8 | blocked; 251 / 330 boundary/non-manifold at source tolerance; same-direction edges 61 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 0 pass/1 fail | 8 states, 3 pre-edit findings |
| `necrotic_zombies` | Gloss alpha 122: a wet chrome statue with white specular lines on every striation. | `0e2db7745cdd975c2728a4e86a8a604695ad168429ea57256880161a08c3e3e9` | 24 / 30 FPS / chaosx_necrotic_zombies_entity=0.8 | blocked; 84 / 73 boundary/non-manifold at source tolerance; same-direction edges 1 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 8 states, 3 pre-edit findings |
| `demonic_zombies` | The attack keeps the hips at 2.5-3.3 u with the torso 35-55 deg down (sprawled on the ground); a hand jumps 4.1 u in one frame. | `776595014bd9960a69bacd9d32b1dd8dbe914b3ae019a903c9e919b82026f47d` | 44 / 30 FPS / chaosx_demonic_zombies_entity=0.8 | blocked; 50 / 36 boundary/non-manifold at source tolerance; same-direction edges 2 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 0 pass/1 fail | 8 states, 8 pre-edit findings |

## Hash-bound native geometry checkpoints

The parent's serialized imports use installed bytes and preserve a per-model receipt and checkpoint path. The exact paths and complete hashes below are also in the JSON crosswalk. The import was geometry-only and does not approve textures, poses, or appearance.

- `zombies`: mesh `7dbebef2ba67468974dd82544dc9d56ee5fcf64bd84078065131c8db38a5efbf` -> `docs/assets/002_zombie_outbreak/models_3d/zombies/blender/checkpoints/reimport_installed_7dbebef2ba674689.blend` (checkpoint SHA-256 `1e9f868d76a222803c2387608d040fd7ff2a1bd3bc473bea936153069f1a5bf6`); receipt `docs/assets/002_zombie_outbreak/models_3d/zombies/validation/reimport_installed_7dbebef2ba674689.json`; visual/material acceptance is false.
- `infected_zombies`: mesh `e93f5b323205b40a4828d2de47dd4cd04ec8455dc809a872160b26b40af5f536` -> `docs/assets/002_zombie_outbreak/models_3d/infected_zombies/blender/checkpoints/reimport_installed_e93f5b323205b40a.blend` (checkpoint SHA-256 `4410472d0ca751029ef6fc78eb1857f86a089d27919ac8599820c319451280ec`); receipt `docs/assets/002_zombie_outbreak/models_3d/infected_zombies/validation/reimport_installed_e93f5b323205b40a.json`; visual/material acceptance is false.
- `rabid_zombies`: mesh `391615a40b786a2320b996410b1fdd29ef87cb940eab14cd4df0bf2338c82b0f` -> `docs/assets/002_zombie_outbreak/models_3d/rabid_zombies/blender/checkpoints/reimport_installed_391615a40b786a23.blend` (checkpoint SHA-256 `390b94c7a093b3c5b07904b4ac24b20d9cb62396bea7e84983fa675aae10543d`); receipt `docs/assets/002_zombie_outbreak/models_3d/rabid_zombies/validation/reimport_installed_391615a40b786a23.json`; visual/material acceptance is false.
- `parasitic_zombies`: mesh `533aec9b60201ec5e4412e10b5fc5236baeedd46e0c13b22568110bab448dd07` -> `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/blender/checkpoints/reimport_installed_533aec9b60201ec5.blend` (checkpoint SHA-256 `032046e4f00080cf575a3e589c0a0639115720226e27745c6277b2f948436104`); receipt `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/validation/reimport_installed_533aec9b60201ec5.json`; visual/material acceptance is false.
- `mutant_zombies`: mesh `25f0604a7a7ea4a555edfb1f4415bb542c2174d4d2955ed2866f615b8e5ec8a6` -> `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/blender/checkpoints/reimport_installed_25f0604a7a7ea4a5.blend` (checkpoint SHA-256 `9e057cd5a4a1f743ac7eb8a36de4f186e2036d8e50624478e0f8d0f5eb3b8073`); receipt `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/validation/reimport_installed_25f0604a7a7ea4a5.json`; visual/material acceptance is false.
- `undead_zombies`: mesh `de3f5f66b6d724221200a883941ebcda649d880a07780f71d1820c7a2c301052` -> `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/checkpoints/reimport_installed_de3f5f66b6d72422.blend` (checkpoint SHA-256 `0d934725620312bbafcd536e207feb5d79c9b47b43766f5eddae71259d1dcdd5`); receipt `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/validation/reimport_installed_de3f5f66b6d72422.json`; visual/material acceptance is false.
- `necrotic_zombies`: mesh `0e2db7745cdd975c2728a4e86a8a604695ad168429ea57256880161a08c3e3e9` -> `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/blender/checkpoints/reimport_installed_0e2db7745cdd975c.blend` (checkpoint SHA-256 `c5e6c5a28fb6662c3f8867c32d523c1224e2a3f7433c38c4ac080024a2d82129`); receipt `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/validation/reimport_installed_0e2db7745cdd975c.json`; visual/material acceptance is false.
- `demonic_zombies`: mesh `776595014bd9960a69bacd9d32b1dd8dbe914b3ae019a903c9e919b82026f47d` -> `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/blender/checkpoints/reimport_installed_776595014bd9960a.blend` (checkpoint SHA-256 `f59e63b4cf0716d93af087268c1441e5c0e8702e56c25adedf489c1357ead92a`); receipt `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/validation/reimport_installed_776595014bd9960a.json`; visual/material acceptance is false.

## Package work still open

- `zombies`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 129; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; death has 158 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u support_attack; final entity lint remains 8 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `infected_zombies`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 201; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 8 action role(s) are blocked in the unchanged installed bytes; training has 311 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u death; final entity lint remains 8 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `rabid_zombies`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 81; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; attack has 452 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u death; final entity lint remains 14 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `parasitic_zombies`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 296; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; attack has 253 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u death; final entity lint remains 3 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `mutant_zombies`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 8; see topology-by-tolerance and winding data in the JSON); normal semantic failure(s): g_std=10.818754 is outside 15..35.; a_std=10.55144 is outside 15..35.; 2 texture semantic gate(s) unresolved for missing material provenance; 8 action role(s) are blocked in the unchanged installed bytes; idle has 709 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u death; final entity lint remains 7 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `undead_zombies`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 251; see topology-by-tolerance and winding data in the JSON); normal semantic failure(s): g_std=14.656474 is outside 15..35.; a_std=13.984502 is outside 15..35.; 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; support_attack has 193 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u death; final entity lint remains 3 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `necrotic_zombies`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 84; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; move has 205 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u attack; final entity lint remains 3 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `demonic_zombies`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 50; see topology-by-tolerance and winding data in the JSON); normal semantic failure(s): a_std=14.670337 is outside 15..35.; 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; attack has 1568 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u idle; final entity lint remains 8 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.

## Capture and remaining acceptance work

Final audio delivery for this package's active mod sound paths: 37 unique paths are installed and verified; 2 paths remain held (2 blocked source rows, 0 without a review row, 0 eligible but not installed). Installed file roles are loop 1, shot 30, step 6. All installed paths are provenance-eligible; their exact before/after hashes and audio measurements are in `docs/plans/unit_fix_2026-10/audio_evidence/install/manifest.json`. Held paths and source-to-runtime needs are itemized in `docs/plans/unit_fix_2026-10/wp3_zombies_audio_needs.md`. All 135 installed files are pcm_s16le, 44.1 kHz mono 16-bit; actual file hashes match the manifest, every recorded role peak target passed, no direct flat top was detected, and max lead silence was 19.95 ms. This is file mastering and integrity evidence, not cue suitability or acceptance. The current entity lint remains 64 states with 54 findings: contact_evidence_required 15, keep_particle_on_impulse_emitter 8, measured_contact_peak_offset 11, one_shot_then_silent_repeating_state 10, sample_longer_than_cycle_without_single_loop 3, sound_samples_overlap 7. Sound definitions and entity/action files remain unchanged. Recovery2 contains 1 staged, 0 of those exact output hashes present in final install, 1 staged outputs absent from install, and 1 unresolved result(s).

Two held shared-pool paths, `sound/002_zombie_outbreak/zombies/zombie_idle_moan_01.wav` and `_03.wav`, are active for both the zombie family and the paleogenetic creature. This preserves a zombie-audio dependency that the WP5 plan says to remove; neither entity nor sound definition changed in this pipeline tranche, so the owner must wire a source-approved dedicated cue before closing that ticket.

The final sound-tree audit records 209 active cues, 173 single-sample cues, 52 duplicate groups, and 52 undeclared cross-unit duplicate groups. Across the entity-lint surface, measured contact-peak offsets, missing timing evidence, sample/state overlaps, and particle/report overlaps remain; mastering does not clear them. The source details are in `docs/plans/unit_fix_2026-10/pipeline_evidence/entity_lint_after.json` and `contact_peak_evidence.json`.

Refilm all package models with a stationary unit or a shot in-point after division repositioning. Lock the crop to the known entity position, not motion detection, and regenerate both idle and attack review sheets before reviewers measure severity-1/2 defects. This is capture work from unit-fix plan section 3.10, not a geometry acceptance.

The parent owns package-manifest/handoff integration and final acceptance reporting. The user performs live-game validation. No commits were created by this documentation tranche.

## Evidence sources and checksums
- `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md` - SHA-256 `1939b400cba160c6d4903e37952e8e55efdb1bfeacf0b4ab061e89c8792c79b2`
- `docs/plans/unit_fix_2026-10/audio_evidence/install/manifest.json` - SHA-256 `72054623f8c388f79f7a8a0c71881025add5efe505c5ae4317db1e3c5ba1ecb5`
- `docs/plans/unit_fix_2026-10/audio_evidence/master_batch.json` - SHA-256 `ec787f36a48db089ef306fb1802736361b0e8d1574de6bedc95577cea61d8e77`
- `docs/plans/unit_fix_2026-10/audio_evidence/provenance_review.json` - SHA-256 `bd4e36c9edbba24c926a2306efb4190541c3f6b90290e9f9a3a0c6111f74b577`
- `docs/plans/unit_fix_2026-10/audio_evidence/recovery2_evidence/recovery2_batch.json` - SHA-256 `e277faf5be6a49d26fd81bf305b0b873ada14e0ae3e36bb11e9f95ff78cf360a`
- `docs/plans/unit_fix_2026-10/audio_evidence/sound_tree_after.json` - SHA-256 `532aae613a6eaab88e21067aa75222fb8a8da8a77ed9d1792363b7cb8d7bb275`
- `docs/plans/unit_fix_2026-10/per_model_delivery_metrics.json` - SHA-256 `df87b418f1f964bdd41269254aee9d3cf39160b738abc81bbb099f010ea505e0`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/baseline_inventory.json` - SHA-256 `6b87475048580ee78e33ccf052d1f67be5002099b3c5db17092dfb1baece633d`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/contact_peak_evidence.json` - SHA-256 `b6193d744c0b10f3d4c6bf464799934010ab07f6ed9991d04ac89bce68a96af8`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/entity_lint_after.json` - SHA-256 `a388fae714faf098968191b752e99193a82fdd37a28daf6bf6b6ca372dfe42bc`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/entity_lint_before.json` - SHA-256 `6fb2ad4eaa2ed9176d341f3012ce04fd3ed183a932a2d264ce2c06e9cb7820d1`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/final_inventory.json` - SHA-256 `d1f72e1456c6a09cdce948df00590534414b91518c8241ec36ca3e11ccb6bb6b`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/installed_after_textures.json` - SHA-256 `c594e4fb8b16c19c18a53963c27142221d3832d57496e53045485bdc2d6408fa`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/runtime_cleanup/manifest.json` - SHA-256 `95f3985f233cfea73472e49d4d88fab791203b1cbfd55b3f44441774cf18c8c9`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/runtime_reimport.json` - SHA-256 `8183c5446cef0085b9baa677e5cccde701214d603ada6e52c2c2e3efda19cee8`
- `docs/plans/unit_fix_2026-10/pipeline_evidence/texture_delivery/manifest.json` - SHA-256 `8e7de281210db53460add9a647a10799e76c7eb90bfd62b428c24e434b4333ff`
- `docs/plans/unit_fix_2026-10/audio_evidence/recovery_batch.json` - SHA-256 `148ffb5a39ce96a1ee6cd532b72dc5426ff5d3abbeccb4afe5a7eba734e533d8`.
- Per-model metrics `docs/plans/unit_fix_2026-10/per_model_delivery_metrics.json` - SHA-256 `89c6d0d0954719a09a8f9dd66eafbd5f3f42e3d2a28b4c29ff29b6f067b9e365`.
- Package held-source report `docs/plans/unit_fix_2026-10/wp3_zombies_audio_needs.md` - SHA-256 `933b5634ee0c60871a9bb1d8a9788d6413042d537b4e14aaae1a4ad07da48b0e`.


## WP3 remainder (11 Oct 2026, second pass)

Historical second-pass record: the current takeover section above supersedes its infected-idle count and parasitic-bundle status; the evidence below remains the result of that earlier pass.

Disposition: `implemented` for the items below; skeletons and actions of the weight repairs are unchanged, so only the meshes were re-exported (geometry gate pass and reimport proofs for the worst roles).

**demonic_zombies**: the wing membranes were skinned hard to separate struts and to the arm, so the edges across the shoulder and wing root stretched up to two units.
The weights across that junction are now blended over neighbouring bones in two rounds of region smoothing driven by the measured edge growth.
Edges growing more than 0.3 units: death frame 46 from 234 to 12 (acceptance under 50), training frame 25 from 111 to 1, support attack frame 43 from 132 to 1, move frame 16 from 78 to 0; the worst frame left anywhere is 19 edges (death frames 29, 63 and 65).

**infected_zombies, undead_zombies, necrotic_zombies**: the stretched edges were the junctions between the coat or rag strips and the arms, spine and hips.
The same region smoothing was applied (infected: idle frame 46 from 50 to 20 edges, attack frame 75 from 37 to 6, defend frame 64 from 39 to 3, support attack frame 27 from 44 to 9; undead: attack frame 45 from 25 to 5, death frame 13 from 18 to 13; necrotic: attack frame 42 from 12 to 4, support attack frame 24 from 7 to 2).
The coat hem, armpit and rag weights are therefore repaired by measured edge growth rather than by moving a fixed fraction of weight onto the thighs.

**parasitic_zombies**: the tentacle tubes around the shoulders and back were skinned to the shoulder, arm and spine bones and moved as one lump.
The thin flesh structures (flesh colour from the delivered diffuse and a measured wall thickness under 6 cm by inward ray casts) are split into eight bundles by direction from their root hub; each bundle has its own three-bone chain placed at the centroids of its tube slices and parented to the body bone that carried its root, and the bundle vertices are skinned over the chain with their original weights fading out along the first segment.
The skeleton grows from 24 to 48 bones.
Every action carries follow-through on the 24 chain bones: each segment trails the body bone that carries it through a first-order low-pass of that bone's real rotation (segment lags 0.5, 0.32 and 0.22 per frame, overshoot 1.8), so the tentacles lag behind every whip and lunge by three to five frames, plus a slow per-bundle writhe (8 to 11 degrees in the idle, half of that in the other actions) whose cycle count divides the action length so the loops close.
The weights were then blended until no frame has more than 40 edges growing over 0.3 units (attack frame 55 from 728 to 11, support attack frame 23 from 696 to 21, death frame 25 from 462 to 23).
The exported bytes pass the delivery gates for all eight roles with reimport proofs (loop seams of the tentacle bones under 2 degrees).

**Remaining and limits**

- The tubes were not cut out of the host mesh: they remain fused to the shell and move as eight bundles, not as individual tentacles, and the tube vertices in small components (about 1,000 of the 5,100 tube vertices) and the vertices within 0.35 units of the root hub are not in any bundle.
- The infected idle still has 20 edges over 0.3 units at frame 46 (the scratch lifting the arm to the head), against the target of 12.
- The other WP3 items listed as open in the 11 Oct section above (mutant attack, wrist weights of the parasite, the demonic elbow placement, the sourced creature and cough sounds) are unchanged by this pass.
