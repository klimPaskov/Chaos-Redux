# WP2 Cannibal rebuilds (014) - Delivery Report

Disposition: `implemented` for this documentation handoff; package mesh/action reconstruction, visual acceptance, final entity wiring, and audio install remain open where the measurements below show gaps. The authorized package scope comes from the user-authored unit-fix plan, SHA-256 `1939b400cba160c6d4903e37952e8e55efdb1bfeacf0b4ab061e89c8792c79b2`.

Package models: cannibal_scavenger_warband, cannibal_feast_guard, cannibal_feast_cohort, cannibal_island_reavers. The full per-model map, DDS, mesh, action, topology, reimport, and entity-lint evidence is in `docs/plans/unit_fix_2026-10/per_model_delivery_metrics.json`.

## Shared delivery facts

Across the shared pipeline, 119 unique active DDS targets are installed (41 diffuse, 39 normal, 39 specular), all 512x512 BC1/BC3 with ten mips. This package references 12 unique DDS paths (4 diffuse, 4 normal, 4 specular). Eighty targets used compression-only conversion and 39 normals received `packed_normal_cleanup` (R=existing G, G/A preserved, B=0). The reviewed T062 mip-7 repair replayed the same QA gates. Unique archived input bytes total 470,825,856; installed bytes total 34,446,104. The item-level JSON records each target's exact before/after dimensions, fourCC, mip count, bytes, SHA-256, decoder QA, and semantic gate results. Runtime cleanup archived nine genuinely unreferenced DDS files (37,749,888 bytes); active shared-variant maps were retained. The global tranche changed no runtime `.mesh` or `.anim` bytes and rewrote no model geometry or actions; native imports created proof checkpoints from the installed mesh bytes.

The material semantic outcomes across this package's unique DDS paths are 2 passed, 2 failed, and 8 unresolved. Normal-map convention outcomes are 2 passed and 2 failed after packed-normal cleanup; cleanup preserves occupied G/A source detail and does not synthesize detail for flat maps. The full decoded per-map statistics and failures are recorded in the JSON.

All 4 model registrations have unchanged installed `.mesh` SHA-256 and unchanged registered `.anim` SHA-256. Each has a native geometry-only Blender reimport checkpoint keyed to its installed mesh SHA. These checkpoints establish readable geometry and stored evidence; `visual_material_acceptance` remains false. Geometry gates are 0 pass and 4 blocked for this package; registered action checks are 3 pass and 29 blocked.

The package's 32 baseline entity states have not been edited by the shared pipeline tranche. Entity lint results are pre-edit evidence; no entity, sound-definition, or particle-definition changes are part of this delivery.

## Per-model reconciliation

| Model | Original triage concern | Installed mesh SHA-256 | Bones / action FPS / entity scale | Geometry gate; boundary edges at 0.0005 | Action audit | Unique DDS paths and normal QA | Entity lint baseline |
|---|---|---|---|---|---|---|---|
| `cannibal_scavenger_warband` | The headdress shell is 57% of the mesh (5.1 x 3.6 x 4.1 u): a glowing white hair ball with legs; the attack has 20 flips above 40 deg. | `72532f027fd58a7d2f7ef0151a192140b1698a5193df0130132ee390023af308` | 24 / 24 FPS / cannibal_scavenger_warband_entity=0.8 | blocked; 0 / 0 boundary/non-manifold at source tolerance; same-direction edges 0 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 0 pass/1 fail | 8 states, 8 pre-edit findings |
| `cannibal_feast_guard` | The body is 1,619 loose open fragments (38,591 boundary edges): flakes fly off during the swing and the polearm is untextured black. | `be457d575838d7126db2a1da97f516814258e2116eb10e449250daba6ca6e24f` | 24 / 24 FPS / cannibal_feast_guard_entity=0.8 | blocked; 37821 / 0 boundary/non-manifold at source tolerance; same-direction edges 78 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 8 states, 9 pre-edit findings |
| `cannibal_feast_cohort` | 26,327 unwelded vertices with 72% of edges open: a silver-grey mass of shards with no readable body or spear. | `1dc1a1c9720fe36f7a3262a8ab9d64a861fa331df71f59b1d8b0018e5d75a0f5` | 24 / 24 FPS / cannibal_feast_cohort_entity=0.8 | blocked; 21378 / 1 boundary/non-manifold at source tolerance; same-direction edges 32 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 0 pass/1 fail | 8 states, 9 pre-edit findings |
| `cannibal_island_reavers` | Quaternion sign discontinuities: 125-180 deg single-frame limb flips in 7 of 8 actions. | `bfd4ee66828e31496b9c8387e2bac2dc099a963a452b3d40bc8e3166f4f84c56` | 24 / 24 FPS / cannibal_island_reavers_entity=0.8 | blocked; 163 / 0 boundary/non-manifold at source tolerance; same-direction edges 0 | 0 pass, 8 blocked; roles: idle, move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 8 states, 12 pre-edit findings |

## Hash-bound native geometry checkpoints

The parent's serialized imports use installed bytes and preserve a per-model receipt and checkpoint path. The exact paths and complete hashes below are also in the JSON crosswalk. The import was geometry-only and does not approve textures, poses, or appearance.

- `cannibal_scavenger_warband`: mesh `72532f027fd58a7d2f7ef0151a192140b1698a5193df0130132ee390023af308` -> `docs/assets/014_cannibalism/models_3d/cannibal_scavenger_warband/blender/checkpoints/reimport_installed_72532f027fd58a7d.blend` (checkpoint SHA-256 `027b8f5a4fac7be9cc5d799e1e0a2e720d5ccbbe1a1dea5c64f63a3463bc1a34`); receipt `docs/assets/014_cannibalism/models_3d/cannibal_scavenger_warband/validation/reimport_installed_72532f027fd58a7d.json`; visual/material acceptance is false.
- `cannibal_feast_guard`: mesh `be457d575838d7126db2a1da97f516814258e2116eb10e449250daba6ca6e24f` -> `docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/blender/checkpoints/reimport_installed_be457d575838d712.blend` (checkpoint SHA-256 `7cea45503139a9575b1d30d03ff45336eabe7b6a5aacaa3776fb3b95d81c7460`); receipt `docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/validation/reimport_installed_be457d575838d712.json`; visual/material acceptance is false.
- `cannibal_feast_cohort`: mesh `1dc1a1c9720fe36f7a3262a8ab9d64a861fa331df71f59b1d8b0018e5d75a0f5` -> `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/blender/checkpoints/reimport_installed_1dc1a1c9720fe36f.blend` (checkpoint SHA-256 `fefb03184f0e51d67d595a218ee6ce081904029358fc8e92f5649824f236dc47`); receipt `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/validation/reimport_installed_1dc1a1c9720fe36f.json`; visual/material acceptance is false.
- `cannibal_island_reavers`: mesh `bfd4ee66828e31496b9c8387e2bac2dc099a963a452b3d40bc8e3166f4f84c56` -> `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/blender/checkpoints/reimport_installed_bfd4ee66828e3149.blend` (checkpoint SHA-256 `8ed8a6c7657012021864080e848a3b57661eb825f7cedb1c0032702e1e54448c`); receipt `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/validation/reimport_installed_bfd4ee66828e3149.json`; visual/material acceptance is false.

## Package work still open

- `cannibal_scavenger_warband`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 0; see topology-by-tolerance and winding data in the JSON); normal semantic failure(s): g_std=4.042912 is outside 15..35.; a_std=4.136264 is outside 15..35.; 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; attack has 399 single-frame-limit violation(s), while maximum measured root planar drift is 4.825 u training; final entity lint remains 8 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `cannibal_feast_guard`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 37821; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; training has 629 single-frame-limit violation(s), while maximum measured root planar drift is 0.413 u death; final entity lint remains 9 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `cannibal_feast_cohort`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 21378; see topology-by-tolerance and winding data in the JSON); normal semantic failure(s): g_std=43.457634 is outside 15..35.; a_std=47.608285 is outside 15..35.; 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; death has 478 single-frame-limit violation(s), while maximum measured root planar drift is 2.296 u death; final entity lint remains 9 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `cannibal_island_reavers`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 163; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 8 action role(s) are blocked in the unchanged installed bytes; death has 431 single-frame-limit violation(s), while maximum measured root planar drift is 1.551 u death; final entity lint remains 12 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.

## Capture and remaining acceptance work

Final audio delivery for this package's active mod sound paths: 24 unique paths are installed and verified; 3 paths remain held (1 blocked source rows, 1 without a review row, 1 eligible but not installed). Installed file roles are loop 4, shot 16, step 4. All installed paths are provenance-eligible; their exact before/after hashes and audio measurements are in `docs/plans/unit_fix_2026-10/audio_evidence/install/manifest.json`. Held paths and source-to-runtime needs are itemized in `docs/plans/unit_fix_2026-10/wp2_cannibal_rebuilds_audio_needs.md`. All 135 installed files are pcm_s16le, 44.1 kHz mono 16-bit; actual file hashes match the manifest, every recorded role peak target passed, no direct flat top was detected, and max lead silence was 19.95 ms. This is file mastering and integrity evidence, not cue suitability or acceptance. The current entity lint remains 32 states with 38 findings: contact_evidence_required 20, measured_contact_peak_offset 13, one_shot_then_silent_repeating_state 5. Sound definitions and entity/action files remain unchanged. Recovery2 contains 4 staged, 4 of those exact output hashes present in final install, 0 staged outputs absent from install, and 0 unresolved result(s).

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
- Package held-source report `docs/plans/unit_fix_2026-10/wp2_cannibal_rebuilds_audio_needs.md` - SHA-256 `8032f44639ecc508f383253389c004bcb20b1cec7842793f57b7f9030a4e3a5d`.

## WP2 rebuild results (10 Oct 2026)

### cannibal_island_reavers

Fixed: the one-frame full-body glitch poses that flipped the torso, thighs, arms, toes and head up to 180 degrees in seven of eight actions (attack frames 67 and 79, idle 63 and 91, defend 59 and 67, move 7, retreat 27 and 43, training eight frames including the 3.06 u Hips jump at frame 87, death thirteen) are removed from the live F-curves; the remaining exporter-level quaternion sign flips (33 attack, 13 training, 46 death) are normalised so every exported action has 0 negative-dot samples; horizontal Hips travel is held at the first-frame value (death keeps only its vertical fall and its forward Z travel is 0); the move and training loop seams were closed (1.2 and 0.8 degrees); the 0.79 s support_attack stub is replaced by an authored 2.0 s harpoon jab (ready, coil, thrust at 0.79 s, hold, recover, final pose equal to the first); the 49 pinholes are filled (0 boundary, 0 non-manifold, one component); eight vertices at the polearm point that were weighted to the Head are weighted to LeftHand; the mesh is reduced from 30,042 to 20,500 triangles (28,892 export vertices, 0 open edges) so it clears the 65,535 triangle-index export ceiling; diffuse black islands are inpainted and glossiness/metalness are regraded from the staged texture tranche (`wp2_evidence/textures`); entity events are re-timed to the measured strikes (impacts 1.25 s and 2.21 s, support 0.79 s) and the death vocal moved to the start of the collapse.

| action | length | sign flips fixed | worst per-frame rotation | gate violations (declared windows / none) | loop seam deg, u | root | declared strike windows |
|---|---|---|---|---|---|---|---|
| idle | 5.92 s | 0 | 1.9 | 4/4 | pass [0.0, 0.0] | pass | - |
| move | 1.17 s | 0 | 18.8 | 47/47 | pass [1.2, 0.006] | pass | - |
| attack | 5.08 s | 33 | 0 | 0/44 | not_applicable [0.0, 0.0] | pass | [[7, 16], [25, 38], [50, 58], [98, 101], [103, 105]] |
| defend | 5.08 s | 0 | 0 | 0/0 | pass [0.0, 0.0] | pass | - |
| support_attack | 2.0 s | 0 | 0 | 0/23 | not_applicable [0.0, 0.0] | pass | [[18, 23]] |
| retreat | 1.83 s | 0 | 12.1 | 21/21 | pass [0.0, 0.0] | pass | - |
| training | 5.25 s | 13 | 9.7 | 7/7 | pass [0.8, 0.002] | pass | - |
| death | 2.29 s | 46 | 0 | 0/325 | not_applicable [129.1, 2.428] | pass | [[1, 53]] |

Evidence: `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/` (checkpoints `wp2_01f_pinholes_smooth` -> `wp2_03_actions_fixed` -> `wp2_04_decimated` -> `wp2_05b_spear_weights` -> `wp2_06_support_v4`; exports and `gate_summary.json` in `export/wp2`; `validation/wp2_reimport_summary.json` holds the eight native reimport proofs of the exact installed bytes; before and after stills in `blender/previews`).

Remaining defects and limits for this model:
- The repository animation gate still flags the idle (4 transitions at 0.25-0.27 u per frame), move (47), retreat (21) and training (7) actions on world joint translation speed above 0.25 u per frame; no rotation, root, sign or loop gate fails except the move worst rotation of 18.8 degrees per frame against the 15 degree locomotion limit. The same gate marks the vanilla GER_infantry_moving_rifle walk blocked (peak 0.31 u per frame at 30.75 fps), so the 0.25 u threshold reads as miscalibrated for this scale rather than as a defect of these provider walk and idle clips. Nothing was waived: those actions are shipped with the flags recorded.
- The death gate passes only through a declared window covering the whole collapse (frames 1-53); without it 325 transitions exceed the limits during the fall.
- The move cycle has one measured sole plant (right foot at 0.0 s) and no left plant; the second footstep event at 0.583 s is an estimate. The provider walk is not re-authored.
- The polearm is still part of the body mesh (skinned to LeftHand, not a separate rigid prop), so the item-fit requirement of the skill is not met for this model. A separate welded polearm needs the original provider geometry, which is no longer in the job folder.
- Normal map: the packed G/A maps were kept; baking from a provider high-poly is blocked because the provider downloads were removed after the original export (re-downloading the completed Meshy tasks is free but needs download permission).
- The showcase re-film with the locked crop is capture work and was not done.

### cannibal_scavenger_warband

Fixed: the headdress shell (57 percent of the mesh, 5.1 x 3.6 x 4.1 u) was cut to a compact crest in Blender from the installed shell (27,541 to 7,258 vertices, 15,164 triangles, Head-dominated vertices 7.9 percent) and cleaned under the repository gate's own clustering at 0.0005, 0.001 and 0.002 (0 boundary, 0 non-manifold, 0 degenerate, 0 duplicate; export gate pass, 14,584 export vertices); the one-frame glitch poses in the attack (frames 12, 28, 32, 36, 48, 56, 64 and 68, 21 outlier keys including the 2.82 u Hips jump at 46-47) are removed and exporter quaternion sign flips normalised in every action (0 negative-dot samples); the death retarget slide was moved from the horizontal axis to the vertical fall (Hips drift now -2.37 u vertical with 0.0 u forward travel; it previously rose 0.88 u and slid 2.37 u); horizontal Hips travel is stripped from attack, support_attack and training (support_attack and training previously glided 3.2 u); the move and retreat loop seams were closed (1.4 and 1.3 degrees); the diffuse hair is regraded to ash grey and the specular recalibrated by the staged texture tranche; the entity gets a training exertion cue twice per loop, strike-timed attack and support_attack events (impacts at 0.83 s, 1.42 s, 0.72 s and 1.25 s) and the death vocal at the start of the collapse.

| action | length | sign flips fixed | worst rotation after windows | violations with/without declared windows | loop | root | declared strike windows |
|---|---|---|---|---|---|---|---|
| idle | 1.75 s | 0 | 0 | 0/0 | pass [0.1, 0.0] | pass | - |
| move | 1.17 s | 0 | 17.1 | 14/14 | pass [1.4, 0.002] | pass | - |
| attack | 3.08 s | 4 | 0 | 0/137 | not_applicable [1.8, 0.001] | pass | [[6, 42], [47, 64]] |
| defend | 1.46 s | 16 | 0 | 0/0 | pass [1.3, 0.0] | pass | - |
| support_attack | 2.92 s | 6 | 0 | 0/214 | not_applicable [9.1, 0.001] | pass | [[4, 52]] |
| retreat | 1.79 s | 37 | 0 | 0/0 | pass [1.3, 0.0] | pass | - |
| training | 3.75 s | 0 | 0 | 0/221 | pass [2.3, 0.001] | pass | [[9, 24], [28, 42], [45, 79]] |
| death | 2.29 s | 72 | 0 | 0/109 | not_applicable [130.5, 2.374] | pass | [[5, 53]] |

Evidence: `docs/assets/014_cannibalism/models_3d/cannibal_scavenger_warband/` (checkpoints `wp2_01_headdress_compact` -> `wp2_02_actions_imported` -> `wp2_03_actions_fixed` -> `wp2_03b_clean` -> `wp2_04_weights` -> `wp2_05_named`; `export/wp2/gate_summary.json`; reimport proofs `validation/wp2_reimport_summary.json` for the eight actions and `wp2_reimport_summary_mesh_named.json` for the final mesh; before and after stills in `blender/previews`).

Remaining defects and limits for this model:
- The move action has no measured sole plant, so the movement events at 0.0 s and 0.583 s (retreat 0.0 s and 0.896 s) are half-cycle estimates; the attack, support_attack, training and death gates pass only through declared windows that cover most of each action (attack 6-64 of 74 frames, support_attack 4-52 of 70, training 9-79 of 90, death 5-53 of 55), and the move action still reports 14 transitions at up to 0.3 u per frame and 17.1 degrees per frame against the 15 degree locomotion limit.
- The idle pose measures 5.07 u wide including the polearm held out to the side, against the plan's 3.5 u target; the headdress itself is no longer the cause. Reducing it needs a re-authored idle with the polearm held closer, which was not done.
- The polearm remains part of the body mesh skinned to RightHand (the fused-weapon limitation of the provider body); a separate item mesh needs the original provider geometry.
- Normal map is the retained original (G/A std 4); baking one needs the provider high-poly, which is no longer on disk (a free re-download of the completed Meshy tasks needs download permission). The sourced hair texture detail beyond the regrade was not re-authored.
- The in-game re-film with locked crop was not done (capture work).

### cannibal_feast_cohort

Fixed: the shard soup (26,398 vertices, 21,378 open boundary edges in 273 components) was welded in Blender at 0.02 u, refilled and cleaned under the delivery gate's own transitive clustering (0 boundary, 0 non-manifold, 0 degenerate, 0 duplicate at 0.0005, 0.001 and 0.002; one connected closed shell), then reduced to 20,000 triangles (9,979 vertices, 16,663 export vertices, export gate pass) to clear the 65,535 triangle-index export ceiling; the original skin weights were kept on the surviving vertices and re-limited to four influences; the death slide on the horizontal axis (2.2 u) is stripped; the 6.2 s defend whose loop snapped 109 degrees was cut to a 2.5 s loop section (frames 4-64) with a 2.7 degree seam; the move loop seam is closed; horizontal Hips travel is held in every non-death action; exporter quaternion sign flips are normalised in defend, support_attack, training and death (0 negative-dot samples); the attack, support_attack and training hand swings stay inside declared strike windows; the diffuse and specular come from the staged tranche (black islands inpainted, glossiness lowered to about 100, metalness zero); entity events are re-timed to the measured thrusts (attack 0.62 s and 1.38 s, support_attack 0.80 s and 1.21 s) with two training cues per loop and the death vocal at 0.45 s.

| action | length | sign flips fixed | worst rotation after windows | violations with/without declared windows | loop | root | declared strike windows |
|---|---|---|---|---|---|---|---|
| idle | 1.75 s | 0 | 0 | 0/0 | pass [0.1, 0.0] | pass | - |
| move | 1.17 s | 0 | 17.4 | 20/20 | pass [1.4, 0.001] | pass | - |
| attack | 2.92 s | 0 | 0 | 0/229 | not_applicable [7.8, 0.0] | pass | [[5, 52]] |
| defend | 2.5 s | 39 | 0 | 0/0 | pass [2.7, 0.009] | pass | - |
| support_attack | 3.08 s | 42 | 0 | 0/104 | not_applicable [2.1, 0.002] | pass | [[10, 41], [48, 62]] |
| retreat | 1.79 s | 0 | 11.8 | 1/1 | pass [2.0, 0.0] | pass | - |
| training | 3.75 s | 10 | 0 | 0/237 | pass [2.2, 0.0] | pass | [[10, 24], [27, 42], [46, 68]] |
| death | 2.29 s | 10 | 0 | 0/300 | not_applicable [127.8, 2.474] | pass | [[2, 8], [10, 43], [45, 53]] |

Evidence: `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/` (checkpoints `wp2_01_prepped` -> `wp2_01w_clean` -> `wp2_01x_dec` -> `wp2_02_geometry` -> `wp2_03_actions_fixed` -> `wp2_04_weights`; `export/wp2/gate_summary.json`; eight native reimport proofs in `validation/wp2_reimport_summary.json`; before and after stills in `blender/previews`).

Remaining defects and limits for this model:
- The weld removes about a third of the original triangles and pulls neighbouring shards together by up to 0.02 u, so fine surface detail of the provider body is lost where it was already fragmented; the figure is now one closed shell but is not the provider's original topology, which would need the original provider download (a free re-download of the completed Meshy tasks needs download permission).
- The spear is still part of the body mesh, not a separate rigid prop.
- The normal map is the retained original (G/A std 49, noise padding); baking a tangent normal needs the provider high-poly that is no longer on disk.
- The move and retreat actions have no measured sole plant, so their footstep events are half-cycle estimates, and move still reports 20 transitions up to 0.37 u per frame and 17.4 degrees per frame against the locomotion limits; the declared strike windows cover most of attack (5-52 of 70 frames), training and death.
- The in-game re-film with locked crop was not done (capture work).

### cannibal_feast_guard

Fixed: the body was 1,619 loose open fragments (41,873 vertices, 38,591 boundary edges) that a position weld could not close (welding at 0.02 to 0.035 u and deleting the unclosable pockets left only about 3,300 triangles). It was therefore rebuilt as one closed shell in Blender: the shard mesh was solidified, voxel-remeshed at 0.035 u and decimated to 20,000 triangles (9,986 vertices, 21,252 export vertices, 0 boundary and 0 non-manifold edges, one connected component, export gate pass); the installed mesh's provider skin weights were reprojected onto the new vertices (nearest source face, barycentric blend, four influences, renormalised) and the posed attack renders show the shell deforming cleanly; the shell was unwrapped with a smart UV (33 percent of the 1024 sheet covered) and the regraded diffuse and specular were reprojected onto it (no black islands: the weapon samples real texels), then dilated 12 pixels and compressed to BC1 and BC3 with full mips; the support_attack was trimmed from 7.75 s to the moving 4.04 s window (frames 37-133), the forearm spikes in the training were smoothed, horizontal Hips travel is held, the defend, move and retreat seams are closed (0.8, 0.0 and 0.0 degrees) and exporter quaternion signs are normalised in support_attack (61), training (3) and death (2); entity events are re-timed to the measured strikes (attack impacts 1.17 s, 2.00 s and 3.04 s, support_attack 2.96 s) and the death vocal moved to the start of the collapse.

| action | length | sign flips fixed | worst rotation after windows | violations with/without declared windows | loop | root | declared strike windows |
|---|---|---|---|---|---|---|---|
| idle | 1.75 s | 0 | 0 | 0/0 | pass [0.1, 0.0] | pass | - |
| move | 1.83 s | 0 | 27.4 | 39/39 | pass [0.0, 0.0] | pass | - |
| attack | 4.62 s | 0 | 0 | 0/220 | not_applicable [2.8, 0.021] | pass | [[12, 33], [36, 59], [61, 80], [83, 100]] |
| defend | 3.5 s | 0 | 10.4 | 13/13 | pass [0.8, 0.011] | pass | - |
| support_attack | 4.04 s | 61 | 0 | 0/55 | not_applicable [110.3, 0.145] | pass | [[23, 27], [33, 38], [44, 57], [68, 74]] |
| retreat | 1.83 s | 0 | 11.9 | 23/23 | pass [0.0, 0.0] | pass | - |
| training | 6.92 s | 3 | 0 | 0/610 | pass [0.2, 0.001] | pass | [[8, 102], [106, 114], [127, 130]] |
| death | 2.29 s | 2 | 0 | 0/363 | not_applicable [129.3, 2.217] | pass | [[2, 53]] |

Evidence: `docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/` (checkpoints `wp2_01_prepped` -> `wp2_01r_remesh` -> `wp2_02_geometry` -> `wp2_03_actions_fixed` -> `wp2_04b_weights`; projected textures in `textures/processed`; texture batch `docs/plans/unit_fix_2026-10/wp2_evidence/textures_guard`; `export/wp2/gate_summary.json`; eight native reimport proofs in `validation/wp2_reimport_summary.json`; before and after stills in `blender/previews`). The original job had no `job.yaml`; a minimal one declaring the `humanoid_unit` profile was written so the delivery gate could run.

Remaining defects and limits for this model:
- The rebuilt shell is a reconstruction of the fragmented surface, not the provider's original topology: surface detail finer than about 0.035 u is gone and the 20,000-triangle shell is smoother than the original; the weights are a reprojection of the provider's installed weights, reviewed in posed renders but not hand-painted. Restoring the original would need the provider geometry, which is no longer on disk (a free re-download of the completed Meshy tasks needs download permission).
- The cleavers are still part of the body mesh and skinned to the hands, not separate rigid items.
- The normal map is a flat tangent map (G and A 128): the old one was noise, and a bake needs a provider high-poly that is not on disk, so the model has no surface relief from the normal map.
- The move, defend and retreat actions still report 39, 13 and 23 world-speed transitions (up to 0.58 u per frame, 27.4 degrees per frame in the move against the 15 degree limit), the attack, support_attack, training and death gates pass only through declared windows (training covers 8-102 of 166 frames), and move has one measured plant (right foot, 0.0 s) with the second footstep a half-cycle estimate.
- The in-game re-film with locked crop was not done (capture work).

