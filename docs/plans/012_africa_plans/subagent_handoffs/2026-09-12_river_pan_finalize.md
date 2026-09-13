# Riverborn and Pan Sappers finalization handoff

Status: `in_progress`; this document is a current repair/resume packet, not a model completion or promotion claim.
Owner: `/root/river_sapper_finalize`.
The parent authorized repair of the existing nonfirearm Riverborn Meshy 7 recovery-4 body and legacy Meshy 6 Pan Sappers body, including missing components and GPT-6-astra skeletal actions.
No Meshy call was required or made, and estimated/consumed Meshy credits are zero.

## Current native sources

| Package | Checkpoint beneath its package root | SHA-256 | Current result |
|---|---|---|---|
| `docs/assets/012_africa/models_3d/riverborn` | `blender/checkpoints/74_attack_contact_finalize_20260912.blend` | `33AE1B026B7470E7EA2CD498132157A9D86AC1DCA8AAD6E16F8AA79574DF6940` | 32 bones, 25,000 closed triangles, separate spear/shield and modeled shield handle, packed PDX material, saved move/attack contact corrections and settled death |
| `docs/assets/012_africa/models_3d/pan_sappers` | `blender/checkpoints/70_flask_clearance_finalize_20260912.blend` | `B6D2DB6B574E117DAAE8F486DAB6940DAE54B00B5C0F3627DE1FBE519F3F6AD1` | 34 bones, 24,916 closed triangles, shovel/cleaver/alchemy kit/flask, packed body/tool materials, settled death clear through every frame, genuine ground-placement sabotage candidate |

The authoritative working status for each package is `evidence/finalize_20260912/status.md`.
Its reconciled `runtime/handoff.md` names the existing consumer, stable runtime IDs, scale relationship and exact parent integration risks.
Provider sources, approved references and historical failed/rejected candidates remain preserved.
The Pan source is explicitly the authorized legacy body; this work does not relabel it as Meshy 7.

The saved Riverborn move and attack corrections preserve the original skeletal body keys while adjusting only measured world-Z contact.
Riverborn's settled death clears all 81 native frames.
Pan's corrected death also clears all 81 frames after repairing intermediate shovel and kit penetration.
Pan's distinct construction action has a visually and numerically reviewed two-hand shovel grip; the .035-unit blade entry in frames 25–32 is deliberate earth contact.
Pan sabotage reaches the ground at frame 49 with a planted crouch, braced shovel and released flask.
The gradual-release repair saved in checkpoint 70 removes the predecessor fingertip dip according to its all-91-frame authoring receipt; fresh reopened inspection and visual acceptance remain pending.

## Pending native work

The exact gradual finger-release repair from Pan's `flask_placement_clearance_request.json` is saved at checkpoint 70.
Its request `f50404248a45424dbc3c192abe1b4473` completed on adapter 1.10.47, preserves body geometry, and reports minimum contact clearance .000389575958 across 91 frames.
The native action SHA-256 is `B4C2081E2D317DFC19E4FCDB704B450A03325945692FB10B12FCC5FA7225A13D`.
The exact Riverborn water-depth/contact repair is prepared in `water_transition_depth_request.json` for checkpoint 76.
Both requests are under their package's `evidence/finalize_20260912/` and name verified source hashes.
Only the Riverborn request remains unsubmitted.
Pan movement still needs measured world-Z grounding.
Two measured locator definitions per package are prepared in `measured_locator_specs.json` but are not authored.

Remaining gates are final all-frame/phase/grip/deformation/loop review, conservative PDX stream partition if needed, coordinate export checkpoints, both `.mesh` files, all ten `.anim` files, staged exact DDS maps, actual-byte reimports, native/export/reimport parity, previews, final manifests and copy hashes.
No repaired 3D runtime export is selected, and historical legacy exports must not be promoted as these repair outputs.

## Dependency and resource status

The last used coherent adapter is 1.10.47 through the locked fresh `BlenderAdapterClient` wrapper, with Blender 5.1.2 and checksum-locked io_pdx_mesh 0.91.0.
Fresh verification recorded all 18 source hashes, all 51 tools and a separately responsive TCP bridge.
The parent then imposed a transport hold after an intermittent wrapper stdin/EOF response race was reproduced; 1.10.48 is being prepared.
All calls are drained; no new Blender inspection, mutation or export is permitted until the parent publishes the coherent release.
The already-exposed direct MCP route remains stale at 1.10.44 and must not be used.
Refresh the dependency/source/schema checks, independently probe the locked socket, and verify the fresh wrapper health after release.

The accepted deployed io_pdx source receipt is `.tools/3d_pipeline/reports/io_pdx_deployed_source_verification_20260912.json`, SHA-256 `9498FB8E634D53C3E290B4542E19A3AB7888DC672C4C3EB4999618AF78687866`.
It records 37 exact present files, three expected absences and zero mismatches, with the accepted upstream/deployed reconciliation links.
Per-package preflight and 1.10.45/1.10.47 verification/schema records remain under `evidence/finalize_20260912/`.

## Companion packages

The icon artist completed both original large and map counter strips in commit `f0c582283`.
This worker accepted their actual-size and enlarged comparisons after two bounded schematic contrast/border revisions.
The parent then visually accepted, promoted, hash-verified and committed all four runtime DDS files in `ee831d8cc`.
Each package's `counter_final_visual_review.json` and `counter_parent_promotion_receipt.json` records the exact source/runtime hashes and ownership evidence.
Riverborn map identity retains its documented alpha-only background-removal fallback after native transparency failed; no identity substitution was used.

The sound-design handoffs are `audio/finalize_20260912/sound_design_handoff.md` in each package.
They contain original sourced recordings, source and direct-download pages, licenses, immutable source hashes, mechanical-transform receipts, derived hashes, role mappings and provisional action synchronization.
The ten new derivatives pass source/derived hash and mono 44.1 kHz signed-16-bit PCM checks.
Riverborn has sourced spear air/contact and body-impact candidates alongside retained public-domain water recordings.
Pan has goat-timbre, hoof, body-impact, real shovel-in-dirt and organic glass-vial contact candidates alongside optional licensed tool rattle.
No audio was created, synthesized or mixed from scratch.
Listening acceptance remains `needs_user_review` because the available agent audio route reports audio input unsupported.
The exact per-subunit selection/acknowledgement consumer remains blocked; vanilla country-tag infantry voice families do not prove that hook.

## Parent integration limits

The parent owns every shared 3D GFX/entity/sound definition and final runtime model promotion.
The current shared death states return to idle and must not do so with the settled death actions.
Riverborn's water transition needs a genuine water-plane context rather than an assumed generic land deployment.
Pan sabotage leaves the flask on the ground, so the persistent placed-flask/effect and next held-flask transition must be resolved explicitly.
Each package has exact source-reviewed consumer evidence in `evidence/finalize_20260912/runtime_consumer_review.json`.
The documented explicit map-entity effects do not establish a native division water-dispatch handle or detached-flask ownership, so these limits remain explicit parent consumer blockers.
Actual exported stream names and material indices must replace the old single `Mesh_0.001` meshsettings rows after export evidence exists.

The worker has not changed any shared runtime file or run Hearts of Iron IV.
Most model working assets remain under the repository's ignored `docs/assets/` tree; no large Blender/provider binaries have been force-added by this worker.
No model-finalization commit is appropriate before the remaining gates pass.
Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets` and `chaos-redux-subagents`; the icon artist also used `imagegen`.
