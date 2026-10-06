# Cannibal Siege Eaters 3D manifest: CURRENT reconciliation

## Installed runtime reconciliation - 6 October 2026

Disposition: implemented installed-byte reconciliation under the user-authorized shared unit-fix task; full model acceptance remains open.
Historical status, numeric summaries and source candidates below are superseded for current installed facts by `docs/plans/unit_fix_2026-10/per_model_delivery_metrics.json` and the matching package report.
This proves current implementation and import facts, not approval of every historical design claim.

Active model: `cannibal_siege_eaters_mesh`.
Installed mesh: `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters.mesh`, SHA-256 `a632f115a093421a1ac8dee441692d72d8799c097b9d7c9c2f16abd4a6bd9772`.
Decoded bones: 24; registered action FPS: 24.0; entity scale: cannibal_siege_eaters_entity=0.8.
Matching native checkpoint: `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/blender/checkpoints/reimport_installed_a632f115a093421a.blend`, SHA-256 `03301792b86851f06891318d57c69bb79352c3ae1905d6d7fcc75134e717ae90`.
The checkpoint proves geometry/skeleton import only; material appearance, real deformation, authored contacts and live consumer acceptance remain pending.
Active DDS maps have hash-bound 512 BC1/BC3 delivery with ten mips; original G/A tangent data is retained and material/detail defects remain explicit in the package report.
Current audio source, format/level changes and held cues are recorded in the shared audio install/provenance/needs reports; candidate existence does not prove runtime installation.
No global mesh/action rewrite, source substitution, or generated production rig/weight/key/sound is asserted by this reconciliation.


Record type: newly reconciled current metadata manifest, not a recovered original JSON.
Status: `needs_user_review`.

The current Event 014 scope is nine gameplay families, seven bespoke model packages, the approved cavalry reuse for `cannibal_bone_riders`, the approved infantry reuse for `cannibal_network_cadre`, and no animation toggle.
This manifest covers only `cannibal_siege_eaters`; the parent owns `cannibal_feast_cohort`, and the prior five-pack worker owns `cannibal_feast_guard`.

The existing partial JSON and Markdown drafts were reviewed and used as inputs.
The selected runtime mesh and eight action sources are the exact `exports/` files named by the accepted 2026-08-25 runtime handoff and the 2026-10-03 installed-bindings audit.
Their current source and installed destination SHA-256 values physically match.
The complete paths, hashes, report receipts, and consumer hashes are recorded in [verified state](../../../../plans/014_cannibalism_plans/evidence/2026-10-03_cannibal_siege_eaters_manifest_recovery/verified_state.json).

The draft's audio mismatch statement was wrong.
All seven role hashes in `evidence/audio_sources/v9_audio_revalidation.json`, including selection, match the current installed WAV files by SHA-256.
The referenced `sound_design_v8.json` and all seven job-root derived WAVs are absent, so original-source attribution, licensing, transformations, and copy history remain unresolved.
The installed sound definitions and animation cue times are recorded in the evidence file.

The three installed diffuse, normal, and specular DDS files match the current installed-bindings audit and the retained conversion hashes.
Provider texture downloads and job-root DDS copies are absent, so direct source-to-runtime byte equality cannot be recomputed.
The three installed counter DDS hashes match the counter handoff; its parent-owned live consumer review remains pending.

Source eligibility remains unresolved.
The recorded provider-input image is absent.
The retained source manifest identifies Christian Hadfield's ArtStation illustration as all-rights-reserved and tagged `NoAI`, explicitly research-only and not approved for ImageGen or Meshy, and does not link it to the recorded provider-input hash.
The 2026-08-22 source-gate override says that input and descendants were superseded/rejected; the 2026-08-25 runtime handoff later calls the unchanged input approved without identifying its source.
No source identity, exact-source authorization, preparation prompt, or source-to-refinement comparison is inferred.

The accepted handoff reports all eight action reimports.
Eight grounded-v3 report JSON files remain, but their referenced checkpoint `.blend` files are absent at the recorded paths.
No standalone mesh reimport receipt was identified.
The retained mesh export report records 29,999 triangles, zero non-manifold or degenerate faces, and 77 loose boundary edges across 16 components; those report values do not establish visual or live acceptance.

The retained job `job.yaml` is absent, and the family inventory row has no `asset_id` or profile field.
`humanoid_unit` is the retained-draft classification supported by the humanoid rig and infantry consumer records, not a recovered job declaration.
The only toolchain record is an August 22 historical audit; it reports Blender 5.1.2 and `io_pdx_mesh` 0.91.0 with a truncated archive checksum, while the accepted August 25 handoff reports adapter 1.10.14 and the old audit says 1.8.1.
Current exact Blender/extension versions are not established.

No Meshy call, balance/key check, Blender operation, runtime asset or wiring edit, or game launch occurred in this metadata reconciliation.
Historical provider lineage records 101 consumed credits; the historical estimate is unavailable, and this pass consumed zero credits.
