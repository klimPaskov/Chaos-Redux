# Shared unit delivery report

Scope: section 3.1–3.9 of the approved unit-fix plan.
Section 3.10 remains the orchestrator's capture work.
This report covers common pipeline implementation and safe installed-byte changes; individual unit package acceptance remains open.

## Delivered changes

All 119 active texture files were converted without upscaling to 512×512 legacy BC1/BC3 DDS with complete ten-level mip chains.
Diffuse alpha is retained when used, normal/specular maps use BC3, and padding follows the actual installed UVs rather than a brightness threshold.
Thirty-nine normal maps received G-to-R mirroring, unused-B cleanup and flat padding while retaining the existing G/A tangent information.
Active texture storage fell from 470,825,856 to 34,446,104 bytes.
Nine unused legacy maps were archived and removed, saving another 37,749,888 bytes.
The focused installed-texture commit is `7f4b8dc5867ac7b14253c3d36ae948f0aefa1205`.

The native BC encoder, complete DDS parser, per-mip decoded fidelity checks, occupancy dilation, class-mask specular recipes and packed/provider normal routes are implemented.
One ray-pistol 4×4 mip failed the unchanged red-channel error threshold; source-derived endpoint fitting corrected that mip, kept the other nine payloads identical and passed an independent re-encode.
The shared texture processor, provider map converter and pilot grading/final-map paths use BC/mip delivery rather than the 2D uncompressed converter.

The geometry inspector reports non-manifold islands rather than stopping the whole read, combines material streams per logical object, records split normals and checks provider boundary budgets.
Preparation uses bounded weld/hole/duplicate/normal operations; mesh export refuses failed topology or winding.
Action export and retime enforce existing-key quaternion sign continuity and check local/world motion, loop seams, root policy and measured soles.
Footstep event proposals carry the exact action hash and require certain measured contacts.
The assembly review preserves separate live-authored item/body materials and UVs and creates no skin or action keys.

The winding face-count correction is committed as `b85220482cedd329859aa082d3e2a9737e13672a`.
Actual installed meshes were reread for all 38 registrations and 48 logical objects; non-manifold edge counts are unchanged, while the face count records only faces incident to those edges.
For example, the alien body records zero such faces rather than all 52,098 triangles; the robot body records 107 rather than all 26,206.
The eleven focused winding tests pass, and the fresh adapter health confirms version 1.11.0, Blender 5.2.2 and the native smoothing/export/import routes.
The raw correction inspector is explicitly not an acceptance pass; the required intake/manifold gate results remain 34 blocked and four passing registrations.

All 38 active model registrations have matching hash-bound native mesh reimport checkpoints.
These are geometry/skeleton import proofs, with visual material and deformation acceptance explicitly pending.
An actual gorilla attack export was refused by the new motion/loop gate, and its rejected bytes were natively reimported as evidence rather than installed.

The final mastering-only installation comprises 135 licensed, measured recordings, committed as `654768c6e5ad6dd63c02a3c54d55b81dfcf85ca1` and recorded in `audio_evidence/install/manifest.json`.
Every installed WAV hash was checked against that manifest and its header verified as mono PCM16 at 44.1 kHz.
Of 209 active mod sound paths, 74 retain their original bytes pending source evidence or suitable source audio.
Final provenance review accepts 137 of the 189 attributed inputs and holds 52; another 20 active inputs lacked an allowlist source mapping.
The two licensed-but-uninstalled cues are island-reavers death (clipped source) and march idle (unresolved recorded-edge loop mismatch); their concrete recording needs are in the WP2/WP6 reports.
One portal electrical pulse with contradictory recording attribution was restored to its exact original bytes before committing.
The shared master performs PCM16/44.1 kHz/mono conversion, onset/tail/fade/DC checks, role levels, actual flat-top detection, spectral checks, loop-edge checks, recorded-edge crossfades and bounded true-peak limiting.
The original batch has 168 passing candidates; the final recovery adds 17 passing candidates from the same recorded inputs.
Only passing candidates with reviewed source/license evidence and unchanged runtime preimages were installed.
The shared tools and reusable skill rules are committed as `5180aec22ff885184ab2dae562e2803a44cd5648`.
The full pipeline suite passed 254 tests.
That suite includes pre-existing temporary synthetic rig/weight test fixtures for legacy scale and weight contracts; they were never production assets or model acceptance evidence.
The follow-up passed eight entity-lint tests and 21 audio tests, with one source-dependent lead-trim test skipped because the installed recording already met that gate.
The complete cue adapter and positive-motion timing corrections are committed as `c1fd22bb8ce251c3f48b42993255cc68c3a0a0db`.

## Installed-byte evidence

| Surface | Evidence and result |
|---|---|
| Consumer inventory | `pipeline_evidence/baseline_inventory.json` and final inventory resolve all 38 active registrations, actual override maps, clone inheritance and additional selection/order recordings. |
| Textures | `pipeline_evidence/texture_delivery/manifest.json`: all 119 installed, decoded fidelity checked at every mip, input/output/preimage hashes retained. |
| Local mip repair | `texture_delivery/repair_t062/t062_repair_proof.json` and `verified_t062/manifest.json`: independent identical re-encode, thresholds unchanged. |
| Geometry/actions | `per_model_delivery_metrics.json` and `geometry_counts_corrected.json`: 4 geometry passes, 34 blocked registrations; 48 passing and 258 blocked registered actions under the measured scenario contract. |
| Event/sound/particle lint | `pipeline_evidence/entity_lint_before.json` and `entity_lint_after.json`: 313 states, 186 resolved particles; measured actual-action timing and post-mastering duration findings remain open. |
| Native checkpoints | `pipeline_evidence/runtime_reimport.json`: all 38 mesh hashes match their checkpoints; geometry-only proof limits are explicit. |
| Actual export gate | `pipeline_evidence/export_gate_smoke.json` and `rejected_export_reimport.json`: a real invalid action cannot reach runtime installation. |
| Runtime cleanup | `pipeline_evidence/runtime_cleanup/manifest.json`: nine preimages archived; assassin shared-variant maps were retained. |
| Audio | `audio_evidence/sound_tree_audit.json`, recovery reports, provenance review and final install manifest retain format, peak/RMS/LUFS/true-peak, lead, DC, spectral and source facts. |
| References | `pipeline_evidence/reference_context.json`, `reference_read.json` and `local_reference_citations.json` preserve route results, paths, line spans and revisions. |

The sound-tree audit read 311 files with zero analysis errors, resolved 209 active mod sound paths and 24 installed vanilla references, and flagged 54 undeclared duplicate-source groups and 173 single-sample cues.
The final audit reads all 311 files without analysis errors, resolves 209 cues and retains 173 single-sample cues and 52 undeclared current shared-source groups.
These are package acceptance findings, not repaired merely by changing WAV format or gain.
The final entity lint retains 84 sample-overlap, 53 sample-longer-than-cycle, 100 strongest-motion-peak offset and 163 missing authored-contact findings.
The measured peaks belong to the unchanged installed action hashes; they are synchronization leads rather than accepted weapon strikes.
All model mesh, action and entity data in the baseline/final inventory compare equal.
Installed audio has maximum leading silence 19.95 ms, maximum absolute DC offset 0.00067015, and zero probable flat-top or nonfinite sample findings; role-level ranges are retained in `audio_evidence/installed_verification.json`.
The source lookup route returned source-location structure but no entity definition ownership; installed shader, entity and io_pdx_mesh source were inspected directly alongside the offline wiki.
Installed documentation markdown contains no detailed DDS/entity-particle chapter; that reference coverage gap is recorded.
The locked binary parser does not read vanilla `@@t@` text animations; no claim of text-animation parser coverage is made.

## Simplifications, omissions, and blockers

There is no global material reclassification without explicit class masks.
Flat or noisy normal detail is not invented, missing equipment is not painted over, and real loop/root/weight/pose defects are not concealed by generated keys.
Each package must provide its authored repairs, material masks, distinct sourced takes, correct role/state/particle wiring, actual contact markers and visual acceptance before closing its model tickets.
The cave mesh retains the stale embedded `resources_found_cave_monster_spec.dds` label; its active GFX override resolves `resources_found_cave_monster_specular.dds`, so delivery uses that valid map, while source-label cleanup belongs to its authored mesh re-export.
Hash-bound native checkpoints and large raw per-frame audit tables remain in the local job/evidence workspace; compact measurements, proof receipts and source revisions are committed with the reports.
The per-package reports and `per_model_delivery_metrics.json` list each model's delivered changes and measured remaining defects.
Audio inputs with missing/ambiguous licensed source evidence, clipped originals or unsuitable loop edges keep their existing runtime cues and appear in the package audio-needs files.

No source substitutions or weaker production stand-ins were used.
No generated production bones, weights, skeletal actions, noise, tones or placeholder audio were installed.
The source-informed per-model repairs and re-filmed acceptance footage remain required; the entire showcase/model goal is not complete at this boundary.

## Orchestrator live checks and re-filming

1. Use a fresh showcase setup save with the two spawn batches in `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/plan.json`.
Load each batch paused and identify each model at its listed `us` province; retain the listed opposing `mx` province only where the capture setup needs it.
Use the existing showcase division setup, the same camera zoom, 1920×1080 and a fixed UI scale of 1.
2. Lock each crop to that model's known province position rather than motion detection.
Keep the unit stationary for attack capture, or choose a shot in-point after the engine's move to the province edge has completed.
Confirm every review tile contains the intended custom unit throughout the clip and no distant vanilla unit supplies the idle crop.
3. For every model, record idle at near, normal and far map zoom, then at least two complete attack/support-attack cycles.
Check that mip transitions do not produce new sparkle, missing islands, black gutter seams or lost alpha cutouts.
Check the known package defects against the listed topology/pose/material thresholds; compression alone does not close those defects.
4. Exercise move/retreat, defend, training, selection/order and death for the applicable model.
Compare contact sounds to the actual strikes/plants/landings, watch for repeated beds or particles hiding the unit, and compare audible levels with an adjacent vanilla unit at the same zoom.
Installed source-derived cues should have prompt onsets, soft releases and no clipping; deliberately held cues remain identified in the audio-needs report.
5. Re-film all 38 models as `SC_<model>_idle.mkv` and `SC_<model>_attack.mkv` with those locked crops after their package repairs pass.
Regenerate the review sheets before model acceptance so empty attack tiles are not mistaken for model defects.
6. From the trailer workspace, refresh `python tools/unit_sounds.py` and `python tools/anim_durations.py`, then run `python project/showcase_v1.py`.
Rebuild both `python tools/edit.py audio` and `python tools/edit.py credits` from that same timeline, inspect the still/preview output, and only then run the final video render.
The exact trailer commands and output paths are documented in `records/showcase/README.md`; this task did not edit or publish the video.

## Models requiring re-filming

WP1: `forest_giants`, `gorilla_heavy_infantry`, `oracle_recon`, `pan_sappers`, `plague_carriers`, `riverborn`, `stone_cohorts`.

WP2: `cannibal_feast_cohort`, `cannibal_feast_guard`, `cannibal_island_reavers`, `cannibal_scavenger_warband`.

WP3: `demonic_zombies`, `infected_zombies`, `mutant_zombies`, `necrotic_zombies`, `parasitic_zombies`, `rabid_zombies`, `undead_zombies`, `zombies`.

WP4: `alien_infantry`, `autonomous_robot`, `assassin_cadre`, `master_assassin`, `mechanized_assassin`, `shadow_company`, `silent_guard`, `clone_infantry`, `portal_raider`.

WP5: `rat_brutes`, `paleogenetic_creature`, `temporal_guard`, `cave_monster_brood`, `xenobiological_assault_organism`.

WP6: `cannibal_bone_guard`, `cannibal_march_predation_column`, `cannibal_siege_eaters`, `chaos_battalion`, `death_hollow_ghost_host`.

## Skills and commit ownership

Used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-subagents` and `chaos-redux-shared-git-commit`.
Updated: the 3D pipeline and event-assets skills with reusable delivery/proof rules; no event-specific state was inserted into them.
Focused commits use isolated indexes, compare-and-swap HEAD updates and owned-path-only real-index reconciliation.
The io_pdx compatibility builder/archive edits present at task start remain outside this task's commit ownership.
