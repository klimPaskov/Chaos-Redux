# WP1 Africa Strange Forces (012) - Delivery Report

The shared-delivery sections below are the baseline before the WP1 repair pass.
The section `WP1 entity repair pass - 6 October 2026` records the subsequent owned changes and supersedes baseline statements about unchanged entity definitions and plague carrier scale.
The complete WP1 package remains incomplete.

Disposition: `implemented` for this documentation handoff; package mesh/action reconstruction, visual acceptance, final entity wiring, and audio install remain open where the measurements below show gaps. The authorized package scope comes from the user-authored unit-fix plan, SHA-256 `1939b400cba160c6d4903e37952e8e55efdb1bfeacf0b4ab061e89c8792c79b2`.

Package models: gorilla_heavy_infantry, pan_sappers, stone_cohorts, riverborn, forest_giants, oracle_recon, plague_carriers. The full per-model map, DDS, mesh, action, topology, reimport, and entity-lint evidence is in `docs/plans/unit_fix_2026-10/per_model_delivery_metrics.json`.

## Shared delivery facts

Across the shared pipeline, 119 unique active DDS targets are installed (41 diffuse, 39 normal, 39 specular), all 512x512 BC1/BC3 with ten mips. This package references 21 unique DDS paths (7 diffuse, 7 normal, 7 specular). Eighty targets used compression-only conversion and 39 normals received `packed_normal_cleanup` (R=existing G, G/A preserved, B=0). The reviewed T062 mip-7 repair replayed the same QA gates. Unique archived input bytes total 470,825,856; installed bytes total 34,446,104. The item-level JSON records each target's exact before/after dimensions, fourCC, mip count, bytes, SHA-256, decoder QA, and semantic gate results. Runtime cleanup archived nine genuinely unreferenced DDS files (37,749,888 bytes); active shared-variant maps were retained. The global tranche changed no runtime `.mesh` or `.anim` bytes and rewrote no model geometry or actions; native imports created proof checkpoints from the installed mesh bytes.

The material semantic outcomes across this package's unique DDS paths are 6 passed, 1 failed, and 14 unresolved. Normal-map convention outcomes are 6 passed and 1 failed after packed-normal cleanup; cleanup preserves occupied G/A source detail and does not synthesize detail for flat maps. The full decoded per-map statistics and failures are recorded in the JSON.

All 7 model registrations have unchanged installed `.mesh` SHA-256 and unchanged registered `.anim` SHA-256. Each has a native geometry-only Blender reimport checkpoint keyed to its installed mesh SHA. These checkpoints establish readable geometry and stored evidence; `visual_material_acceptance` remains false. Geometry gates are 0 pass and 7 blocked for this package; registered action checks are 5 pass and 51 blocked.

The package's 63 baseline entity states have not been edited by the shared pipeline tranche. Entity lint results are pre-edit evidence; no entity, sound-definition, or particle-definition changes are part of this delivery.

## Per-model reconciliation

| Model | Original triage concern | Installed mesh SHA-256 | Bones / action FPS / entity scale | Geometry gate; boundary edges at 0.0005 | Action audit | Unique DDS paths and normal QA | Entity lint baseline |
|---|---|---|---|---|---|---|---|
| `gorilla_heavy_infantry` | support_attack hips flip 155 deg in one frame (frame 74-75): a headless folded blob for 0.8 s of every cycle. | `730879dd2ea2d59ab0915adc95d47d8d42e07df48a065d045451b344287338eb` | 24 / 30 FPS / chaosx_gorilla_heavy_infantry_entity=0.8 | blocked; 150 / 109 boundary/non-manifold at source tolerance; same-direction edges 3 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 8 states, 13 pre-edit findings |
| `pan_sappers` | Throws an empty fist: no flask or charge prop is ever in the hand and no shovel or cleaver is visible, so the sapper reads as an unarmed faun. | `9f5b97f8702e1ab4c90f41624af453e5fd86c75276aed4fcb82bb95103053e24` | 24 / 30 FPS / chaosx_pan_sappers_entity=0.8 | blocked; 125 / 122 boundary/non-manifold at source tolerance; same-direction edges 4 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 10 states, 7 pre-edit findings |
| `stone_cohorts` | Specular B 52 / A 158 over the whole body turns the stone into wet chrome (blown-white pauldrons and fists). | `2bd521199ae7a11026d8797531b72f56fc3d0ce4bef5f3437e938395f3b0effe` | 24 / 30 FPS / chaosx_stone_cohorts_entity=0.8 | blocked; 88 / 74 boundary/non-manifold at source tolerance; same-direction edges 4 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 8 states, 24 pre-edit findings |
| `riverborn` | support_attack yaw span 137 deg: the warrior turns its back on its front every cycle while the spear passes through the torso. | `7b18bfec64485cb168aba6f1868d327a265682e84cfb33b090df38a4423fa3fb` | 24 / 30 FPS / riverborn_entity=0.8 | blocked; 159 / 175 boundary/non-manifold at source tolerance; same-direction edges 4 | 0 pass, 8 blocked; roles: idle, move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 9 states, 18 pre-edit findings |
| `forest_giants` | The attack blow is too small to read (18 deg hip yaw, no wind-up); the showcase shot filmed the engine reposition instead of the attack. | `9a02e5218e29ca709cdce3a743770bb62b190dbb84171bef9a60c5ebe65b5cb8` | 24 / 30 FPS / chaosx_forest_giants_entity=0.8 | blocked; 176 / 213 boundary/non-manifold at source tolerance; same-direction edges 6 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 9 states, 15 pre-edit findings |
| `oracle_recon` | 23.8 s move loop with pauses guarantees foot sliding; idle, death, observation and select cues are sub-200 Hz drones that play as silence. | `e7f13c7aa14ea47c64bd149985184c102e852c0cf5f203b7654e20bbf2939c96` | 24 / 30 FPS / chaosx_oracle_recon_entity=0.8 | blocked; 322 / 285 boundary/non-manifold at source tolerance; same-direction edges 11 | 0 pass, 8 blocked; roles: idle, move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 1 pass/0 fail | 9 states, 5 pre-edit findings |
| `plague_carriers` | The body root has 0.0 deg of motion in attack and idle: a standing donkey with a swinging basket, at 1.38x a man (scale 1.0). | `32e03d669af9c1c4466e345171861fe568e01a96fb995b26c0a6589af7cd98e8` | 25 / 30 FPS / plague_carriers_entity=1.0 | blocked; 0 / 8 boundary/non-manifold at source tolerance; same-direction edges 0 | 1 pass, 7 blocked; roles: move, attack, defend, support_attack, retreat, training, death | 3 paths; normal 0 pass/1 fail | 10 states, 12 pre-edit findings |

## Hash-bound native geometry checkpoints

The parent's serialized imports use installed bytes and preserve a per-model receipt and checkpoint path. The exact paths and complete hashes below are also in the JSON crosswalk. The import was geometry-only and does not approve textures, poses, or appearance.

- `gorilla_heavy_infantry`: mesh `730879dd2ea2d59ab0915adc95d47d8d42e07df48a065d045451b344287338eb` -> `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/blender/checkpoints/reimport_installed_730879dd2ea2d59a.blend` (checkpoint SHA-256 `8394bc5e04461ee162e1a2660a0feff8d11e82d911c9026149853418ea3c0d76`); receipt `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/validation/reimport_installed_730879dd2ea2d59a.json`; visual/material acceptance is false.
- `pan_sappers`: mesh `9f5b97f8702e1ab4c90f41624af453e5fd86c75276aed4fcb82bb95103053e24` -> `docs/assets/012_africa/models_3d/pan_sappers/blender/checkpoints/reimport_installed_9f5b97f8702e1ab4.blend` (checkpoint SHA-256 `8bc7db4ea2c212e94fa4613b367ea13fc9c8b4b14546eba657faff36bed90cd0`); receipt `docs/assets/012_africa/models_3d/pan_sappers/validation/reimport_installed_9f5b97f8702e1ab4.json`; visual/material acceptance is false.
- `stone_cohorts`: mesh `2bd521199ae7a11026d8797531b72f56fc3d0ce4bef5f3437e938395f3b0effe` -> `docs/assets/012_africa/models_3d/stone_cohorts/blender/checkpoints/reimport_installed_2bd521199ae7a110.blend` (checkpoint SHA-256 `04c86fbb1e1f023087fefcb7976ed8668932849a3d968a1e1e03c2c264bb6d88`); receipt `docs/assets/012_africa/models_3d/stone_cohorts/validation/reimport_installed_2bd521199ae7a110.json`; visual/material acceptance is false.
- `riverborn`: mesh `7b18bfec64485cb168aba6f1868d327a265682e84cfb33b090df38a4423fa3fb` -> `docs/assets/012_africa/models_3d/riverborn/blender/checkpoints/reimport_installed_7b18bfec64485cb1.blend` (checkpoint SHA-256 `f809ff6c66f5d44a57f28c04a6a3f37e30be92c152ce9f927b45452652587bbf`); receipt `docs/assets/012_africa/models_3d/riverborn/validation/reimport_installed_7b18bfec64485cb1.json`; visual/material acceptance is false.
- `forest_giants`: mesh `9a02e5218e29ca709cdce3a743770bb62b190dbb84171bef9a60c5ebe65b5cb8` -> `docs/assets/012_africa/models_3d/forest_giants/blender/checkpoints/reimport_installed_9a02e5218e29ca70.blend` (checkpoint SHA-256 `eaa1d6e398cd2c17ac483be25041c67a9e6d841da37e904045d104166f8256f8`); receipt `docs/assets/012_africa/models_3d/forest_giants/validation/reimport_installed_9a02e5218e29ca70.json`; visual/material acceptance is false.
- `oracle_recon`: mesh `e7f13c7aa14ea47c64bd149985184c102e852c0cf5f203b7654e20bbf2939c96` -> `docs/assets/012_africa/models_3d/oracle_recon/blender/checkpoints/reimport_installed_e7f13c7aa14ea47c.blend` (checkpoint SHA-256 `595e12186c838941e95667cb5beae812d17c247076b75b8c28748a48af940971`); receipt `docs/assets/012_africa/models_3d/oracle_recon/validation/reimport_installed_e7f13c7aa14ea47c.json`; visual/material acceptance is false.
- `plague_carriers`: mesh `32e03d669af9c1c4466e345171861fe568e01a96fb995b26c0a6589af7cd98e8` -> `docs/assets/012_africa/models_3d/plague_carriers/blender/checkpoints/reimport_installed_32e03d669af9c1c4.blend` (checkpoint SHA-256 `1fc9ee0aeebdd0cafd2697c8c483f349d78743689961dd0eec8af83516957a3f`); receipt `docs/assets/012_africa/models_3d/plague_carriers/validation/reimport_installed_32e03d669af9c1c4.json`; visual/material acceptance is false.

## Package work still open

- `gorilla_heavy_infantry`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 150; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; death has 428 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u support_attack; final entity lint remains 13 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `pan_sappers`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 125; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; death has 272 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u attack; final entity lint remains 7 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `stone_cohorts`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 88; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; training has 622 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u attack; final entity lint remains 24 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `riverborn`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 159; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 8 action role(s) are blocked in the unchanged installed bytes; death has 278 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u death; final entity lint remains 18 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `forest_giants`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 176; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; training has 269 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u death; final entity lint remains 15 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `oracle_recon`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 322; see topology-by-tolerance and winding data in the JSON); 2 texture semantic gate(s) unresolved for missing material provenance; 8 action role(s) are blocked in the unchanged installed bytes; training has 203 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u death; final entity lint remains 5 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.
- `plague_carriers`: geometry audit gate is blocked (worst recorded 0.0005 positional-tolerance boundary count 0; see topology-by-tolerance and winding data in the JSON); normal semantic failure(s): g_std=3.037625 is outside 15..35.; a_std=2.962563 is outside 15..35.; 2 texture semantic gate(s) unresolved for missing material provenance; 7 action role(s) are blocked in the unchanged installed bytes; move has 54 single-frame-limit violation(s), while maximum measured root planar drift is 0.000 u idle; final entity lint remains 12 finding(s) across the registered state rows; all visible content still needs stationary filming with a crop locked to the entity map position.

## Capture and remaining acceptance work

Final audio delivery for this package's active mod sound paths: 13 unique paths are installed and verified; 30 paths remain held (21 blocked source rows, 9 without a review row, 0 eligible but not installed). Installed file roles are loop 2, shot 9, step 2. All installed paths are provenance-eligible; their exact before/after hashes and audio measurements are in `docs/plans/unit_fix_2026-10/audio_evidence/install/manifest.json`. Held paths and source-to-runtime needs are itemized in `docs/plans/unit_fix_2026-10/wp1_africa_audio_needs.md`. All 135 installed files are pcm_s16le, 44.1 kHz mono 16-bit; actual file hashes match the manifest, every recorded role peak target passed, no direct flat top was detected, and max lead silence was 19.95 ms. This is file mastering and integrity evidence, not cue suitability or acceptance. The current entity lint remains 63 states with 94 findings: contact_evidence_required 29, keep_particle_on_impulse_emitter 4, measured_contact_peak_offset 10, one_shot_then_silent_repeating_state 7, sample_longer_than_cycle_without_single_loop 15, sound_samples_overlap 29. Sound definitions and entity/action files remain unchanged. Recovery2 contains 4 staged, 2 of those exact output hashes present in final install, 2 staged outputs absent from install, and 0 unresolved result(s).

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

## WP1 entity repair pass - 6 October 2026

Acceptance basis: the user's explicit WP1 assignment, the plan's common rules, every WP1 ticket, and section 3.
The required `unit_s3_report.md` is absent.
The existing `pipeline_report.md` and the geometry/animation, texture, and audio handoffs supply the completed shared-tool work and its limits.

### Implemented entity repairs

Plague carrier scale is `0.75` in its entity and job; its current manifest matches that scale.
The locked parser reads source Y-height `8.2684822083` from the installed mesh, giving effective height `6.2013616562` instead of `8.2684822083`.
Rest minimum Y remains zero; this is rest-bounds evidence and does not accept posed hooves, cargo, withers ratio, or animation.
The attack state no longer plays `chaosx_plague_carriers_deploy_sfx`; the deploy state retains the cue.
A suitable recorded donkey bray is still required.

Gorilla heavy infantry, pan sappers, riverborn, and oracle recon death states no longer persist their finite blood bursts.
The installed blood emitter has duration `0.1` seconds and particle life `0.5-1.0` seconds.
The section 3 event lint reads all 63 WP1 states and reduces `keep_particle_on_impulse_emitter` from four findings to zero.
No action timing was retuned from a guessed contact or a strongest-motion proxy.

Owned entity paths: `gfx/entities/chaosx_gorilla_heavy_infantry.asset`, `chaosx_pan_sappers.asset`, `chaosx_riverborn.asset`, `chaosx_oracle_recon.asset`, and `chaosx_plague_carriers.asset`.
Plague metadata paths: `docs/assets/012_africa/models_3d/plague_carriers/job.yaml` and `manifest.md`.
Design decisions: `docs/plans/012_africa_plans/agent_decisions_2026-10-05.md`.
Reference evidence: `wp1_evidence/reference_routes.json` and `local_references.json`, retaining source paths, line spans, and SHA revisions.

### Installed-byte baseline and remaining acceptance

The existing section 3 parsers reread seven meshes, 56 registered actions, and 21 active DDS maps.
Every DDS map is 512 square, BC1/BC3, with ten mips; material-class recipes, atlas repairs, and normal detail remain separate requirements.
Every mesh fails the manifold gate; 51 action roles fail the delivery scenario and five pass its numerical checks.
Even a numerical action pass does not prove semantic performance, sole contacts, or live appearance.
The compact hash-bound measurements are `wp1_evidence/measured_baseline_compact.json`.
No mesh, action, or texture replacement was installed by this entity pass, so their before/after measurements are equal.

| Model | Boundary / non-manifold edges at 0.002 units | Attack seam degrees / units | Support-attack seam degrees / units | Ticket disposition |
|---|---:|---:|---:|---|
| gorilla_heavy_infantry | 150 / 109 | 108.40 / 0.2388 | 17.57 / 0.1925 | Support pose, attack easing/recovery, idle breathing/shift/tap, per-class specular and manifold repair remain required. Finite death particle implemented. |
| pan_sappers | 125 / 122 | 74.11 / 0.0259 | 111.89 / 1.3994 | Flask release and shovel/cleaver slots, sub-three-second throw, idle motion, support return, two-plant move, thigh/underarm rebake and manifold repair remain required. Finite death particle implemented. |
| stone_cohorts | 88 / 74 | 19.32 / 0.1134 | 16.79 / 0.0212 | Stone/iron specular masks, shaft contact/fingers, easing/end-height repair, two-plant move, halberd painting and manifold repair remain required. |
| riverborn | 159 / 175 | 16.28 / 0.0450 | 88.05 / 0.0865 | Front-facing spear/shield performance, chest clearance, easing/support return, large-loop/shell repair and class-aware atlas remain required. Finite death particle implemented. |
| forest_giants | 176 / 213 | 17.14 / 0.0003 | 25.04 / 0.1656 | Wind-up/hold/follow-through, enlarged axe and thick haft, readable log/islands, bark specular and slit/manifold repair remain required. Capture in-point remains orchestrator-owned. |
| oracle_recon | 322 / 285 | 74.30 / 0.0709 | 45.79 / 0.0411 | Move is still 715 frames, not 30-36. Two-plant recut, idle neck look-around, action returns, staff-tip locator/light, staff painting, skin/bone specular and manifold repair remain required. Finite death particle implemented. |
| plague_carriers | 0 / 8 | 1.03 / 0.0000 | 0.77 / 0.0000 | Scale and wrong attack cue repaired. Chest/pelvis stamps, neck/ear/idle performance, source-backed normal rebake, smooth joint weights and rigid cargo review remain required. |

Plague carrier exported stream vertices have `75.048%` single-influence weights, including UV splits and rigid cargo, versus the ticket's less-than-40% target.
That read-only diagnostic is `wp1_evidence/plague_weight_distribution.json`; deliberate neck/leg deformation review remains required.
Scale measurements are `wp1_evidence/plague_scale_rest_bounds.json`.

### Authoring and source blockers

The locked Blender 5.2.2 / adapter 1.11.0 / io_pdx_mesh 0.91.0 export route is healthy.
Initial Blender Lab TCP and direct-read probes failed at `localhost:9877`.
A subsequent read-only live probe succeeded and verified Blender 5.2.2 build `d13f752e3b9c`, installed add-on 1.0.3, and module SHA `ba2f57daeca7c3fb2ad50aad75992dfb85c928345918da8bbda7bd08a038e061`.
The observed live session then held WP3's `mutant_zombies/blender/working/v1/blender/checkpoints/21d_export_batches.blend`; WP1 did not load or modify it.
The WP1 background pose inspection timed out after 1,800 seconds on the serialized worker lock, without producing a result or leaving an owned Blender worker.
The current authoring blocker is exclusive session availability, requested from the orchestrator, rather than continued connection failure.
The exposed client tool count differs from the full locked server inventory, but that count alone is not evidence of incompatibility.
The user prohibits opening desktop windows; no window was opened.
The pipeline requires bones, weights, and keys to be authored in a verified exclusive live session, so the blocked repairs cannot be completed through repository-generated motion or weights.
Safe background export capability is not a substitute for live authoring.
Source-backed class masks, prop rebakes, and normal-detail repairs also remain unaccepted.
No paid Meshy task or Internet audio download was started.

The source lookup query for `plague_carriers_entity` did not return after approximately 100 seconds; the waiting orchestration cell was terminated and local definitions were read.
The narrow installed-documentation search returned no `soundeffect` chapter, so exact vanilla sound/entity/particle definitions were inspected alongside the offline wiki.
These are recorded reference-route limits, not engine acceptance.

### Simplifications, omissions, and blockers

The complete WP1 assignment is incomplete.
Every unimplemented authored/model/material/audio requirement stays open as listed above and in the audio needs and worker handoffs.
No static pose, alias, generated rig/weight/key, painted geometry substitute, or fabricated audio take was delivered as a requested repair.
No model re-export is claimed for this entity pass; existing native import receipts establish their earlier geometry imports only.
User/orchestrator runtime evidence and locked-crop re-filming are still required for full acceptance.

### Exact orchestrator checks

Use the showcase batch-1 setup save, camera 1920x1080, UI scale 1, and the existing divisions from `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/plan.json`.
Keep the crop locked to each listed friendly province; opposing provinces below identify the existing combat setup.

| Model | Friendly / opposing province |
|---|---|
| gorilla_heavy_infantry | 1954 / 2037 |
| pan_sappers | 2019 / 12811 |
| stone_cohorts | 3834 / 2069 |
| riverborn | 5038 / 2104 |
| forest_giants | 5044 / 5071 |
| oracle_recon | 5061 / 2060 |
| plague_carriers | 7920 / 8012 |

1. Inspect plague carrier idle and move beside gorilla/vanilla infantry at the same zoom.
Expected scalar result: the entire donkey and cargo are 75% of their previous dimensions; no proportional distortion is introduced.
Measure hoof contact and basket/pole clearance through move and idle; do not accept rest height alone.
2. Run two complete plague attack cycles, then deployment/support-attack.
Expected attack result: no containment deployment hiss at the head drop; existing hoof impacts remain.
Expected deployment result: its existing deployment cue still plays.
The missing bray and remaining articulation/weight defects are open findings.
3. Trigger death for gorilla, pan, riverborn, and oracle.
Expected particle result: one finite blood burst that clears, with the existing death and landing cues preserved.
4. After the remaining model tickets pass, re-film each model's idle and two stationary attack/support cycles, plus move/retreat, defend/training, selection/orders and death.
For forest giant attack, use an in-point at 4.6 seconds or later, after movement to the province edge.
Measure the ticket-specific pose, plant, loop, crop, gloss, prop-readability and sound-contact thresholds before accepting the model.
All seven WP1 models need re-filming: gorilla_heavy_infantry, pan_sappers, stone_cohorts, riverborn, forest_giants, oracle_recon, plague_carriers.

Skills used: chaos-redux-3d-model-pipeline, chaos-redux-event-assets, chaos-redux-subagents, and chaos-redux-shared-git-commit.
No skill was created or updated because the existing skills already specify these route, source and acceptance rules.

## Forest idle sound lifecycle and model handoff

Implemented: `chaosx_forest_giants_idle_loop_sfx` uses two distinct source-derived wood-creak beds with `max_audible = 1` and random repetition prevention.
Only the forest giant idle state's `trigger_once` event consumes it; attack and defend retain the existing one-shot wrapper.
The two compiled beds use source intervals 18.50-21.00 and 22.50-25.00 seconds from the verified claretcanelon CC0 recording; they measure `-20.8/-20.0` LUFS, `-1.0/-1.6` dBTP, and `1.584/1.211` dB inner-edge RMS difference.
The old one-shot WAV stays byte-identical to SHA `4a8c467aba711a2aaf744a2711dfa37c0dd3e67b6480e57f18cd6705ebbeefe5`; its uncertain exact source interval is not counted as a third take.
The forest idle state's source-lint findings are empty, and the WP1 one-shot-then-silent count falls from seven to six.
Current evidence is `wp1_evidence/audio_install/installed_verification.json` and `wp1_sound_attribution.md`.
The heavy attack/tree-fall/root-tear sound requirements remain open.

The reviewed model worker handoff is `wp1_model_worker_handoff.md`.
It lists every numbered ticket step, the healthy export dependencies, the shared-session ownership blocker, and the timed-out read-only adapter request.
Plague `export/v4` matches all eight installed action hashes; its current-hash idle/move native receipts are usable, whereas the older per-hoof move receipt is stale.
At scale `0.75`, their sampled whole-mesh minima are about `0.00301` units for idle and `0.00300` for move frames 1, 11, 31 and 41.
Move frame 21 has minimum `0.03410357` units, above the `0.01` planted-frame tolerance, so its ground contact still needs authored correction.
Per-part hoof identification and basket/pole clearance are unmeasured; no posed-contact pass is claimed.

The installed `standardfuncsgfx.fxh` normal unpacker reads X from G and Y from negative A.
The plague ticket's X-in-A/Y-in-G phrase conflicts with that consumer; a subsequent source-backed rebake must follow the actual shader and preserve verified source handedness.
No normal texture was changed here.

Additional live check: keep the forest giant idle for at least 20 seconds at province 5044, then change to attack, movement and death.
Expected result: the wood-creak bed continues beyond its first 2.5-second sample, does not stack on every idle cycle, and stops when idle ends.
Attack/defend wood cues remain individual sounds, with their existing timing; live transition and playback proof are pending.

## Installed sound pools and final offline verification

The parent reviewed the audio handoff `wp1_audio_worker_handoff.md` and installed twelve recorded-sample WAVs across four complete cue pools.
Source/cut/output hashes, original preimages, licenses and processing commands are retained in `wp1_evidence/audio_install/manifest.json`.
The permanent per-file credit and consumer handoff is `wp1_sound_attribution.md`.
No recording was downloaded or synthesized; only the existing collection's licensing metadata was read online.

| Consumer | Before / after takes | Delivered behavior | Remaining acceptance |
|---|---:|---|---|
| forest_giants idle | 1 one-shot / 2 looping beds | Distinct CC0 wood-creak beds continue during idle, without restarting on every animation cycle. The attack/defend one-shot stays separate. | Live transition/stop and auditory review; heavy attack and tree-fall sources remain missing. |
| plague_carriers move/retreat | 1 / 4 | Four distinct outdoor horse-hoof contacts replace the long repeated movement cue. Their 45-75 ms durations fit the inherited 0.3333-second event gaps. | Anatomical hoof plants and field playback remain unverified; no donkey bray was found. |
| pan_sappers death | 1 / 3 | Three distinct recorded goat calls are paired with a clean body fall on dirt. One cue contains voice and landing; the former landing hoof cue is removed. | Live body/voice fit and animation landing; no claim that the death pose is repaired. |
| stone_cohorts collapse recovery | 1 / 3 | Three non-overlapping CC BY 4.0 stone-grind recordings replace the shared tool clatter. Existing event times and volumes remain. | Live grinding/settling fit; rockslide death and thrust impact sources remain open. |

Pan death keeps voice at `0.1000` seconds and the intended body phase at the inherited `0.9667` seconds.
The clean body source is trimmed at `0.420` seconds, faded in over 10 ms and delayed 37,339 samples; its source transient gives a relative `0.866689`-second placement.
Fresh installed-waveform 10 ms RMS centres put all three body contacts at `0.977834` seconds, within `11.134` ms of the inherited target.
This proves waveform placement, not anatomical ground contact in the unchanged action.
The clipped remaxim/qubodup recording, with 82 near-rail samples and a 58-sample plateau, was rejected even though an attenuated derivative looked clean.
The parent accepted the existing clean CC0 leonelmail dirt fall as the same physical component as the named BigSoundBank example; source choice preserves the planned role and avoids a new recording or weakened substitute.

Fresh destination-byte analysis reads all twelve installed WAVs as PCM16, 44.1 kHz mono and passes the unchanged role gates, including lead, direct clipping, spectral, peak and loop-edge checks.
Short hoof EBU values are gated and unavailable; the tool's `-70` sentinel is not interpreted as actual loudness.
New WAV hashes are not shared with another active unit family.
The source sound/particle audit covers 63 states, clears all four persistent blood findings, reduces silent-idle findings from seven to six, and reduces sample-overlap findings from 29 to 27.
The remaining 27 overlaps, 29 missing-contact findings, ten measured-peak offsets and 15 sample/cycle findings remain open; a lower count is not a full sound-system pass.
All 84 original mesh/action/texture payloads remain hash-identical, so this pass does not claim any mesh, rig, material, action or export repair.

Additional orchestrator checks:

1. At province 7920, move and retreat the plague carrier through two complete strides.
Expected sound result: one short hoof contact for each existing event, four real variants and no movement bed overlapping the next plant.
Check the frame-21 floating support finding separately; sound clips do not fix it.
2. At province 2019, trigger Pan death at least three times across separate units.
Expected result: varied goat cries at entry, one dirt body contact near the existing landing beat, and no second hoof clop on landing.
3. At province 3834, trigger stone support-attack and death.
Expected recovery result: stone grinding/settling, without the old shared workshop clatter; the still-pending death rockslide must not be reported as delivered.
4. For the trailer, refresh `python tools/unit_sounds.py` in the trailer workspace after the orchestrator's replacement recordings are final, then rebuild `project/showcase_v1.py`, audio, credits and final video from the same timeline.
No showcase clip or video was recorded, rendered or published by WP1.
- Per-model metrics `docs/plans/unit_fix_2026-10/per_model_delivery_metrics.json` - SHA-256 `89c6d0d0954719a09a8f9dd66eafbd5f3f42e3d2a28b4c29ff29b6f067b9e365`.
- Package held-source report `docs/plans/unit_fix_2026-10/wp1_africa_audio_needs.md` - SHA-256 `01e1d7a045c1f48228934a39f05f433600b0d4fa0726f21336b3c3a74e6a6a12`.
