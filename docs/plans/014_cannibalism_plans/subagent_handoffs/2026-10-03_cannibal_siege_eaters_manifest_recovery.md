# Event 014 Cannibal Siege Eaters manifest recovery

Disposition: implemented as a metadata-only current reconciliation; package status remains `needs_user_review`.

## Scope and ownership

This pass reviewed the interrupted worker's existing partial `manifest.json` and `manifest.md` drafts, then corrected and completed only the `cannibal_siege_eaters` package record.
The current owner instruction is the acceptance basis for the Event 014 scope: nine gameplay families, seven bespoke model packages closed, approved cavalry reuse for `cannibal_bone_riders`, approved infantry reuse for `cannibal_network_cadre`, and no animation toggle.

Changed paths:

- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/manifest.json`
- `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/manifest.md`
- `docs/plans/014_cannibalism_plans/evidence/2026-10-03_cannibal_siege_eaters_manifest_recovery/verified_state.json`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_cannibal_siege_eaters_manifest_recovery.md`

The parent-owned `cannibal_feast_cohort` package and prior-worker-owned `cannibal_feast_guard` package were not opened or changed.
`family_jobs.json`, gameplay, specs, GUI, runtime model/sound/counter files, old reports, and source archives were not edited.
No commit was created.

## Selection and checksum reconciliation

The selected runtime source set comes from the primary accepted record `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_cannibal_siege_eaters_runtime_wiring_2026-08-25.md` (SHA-256 `d2179f20171b98a597644344044eff246366f29bc6870f71bd5bad43da8107c1`) and the current installed-bindings audit `docs/plans/014_cannibalism_plans/evidence/2026-10-03_runtime_unit_bindings_after.json` (SHA-256 `a9dc4753057922ff00d1c06c0658625a8c79b75a90d8325a394555f91c0ebb76`).
These records select the `exports/` mesh and role actions.
The separate `export/mesh` and `export/anim` paths were not selected by filename or substituted.

Filesystem SHA-256 checks confirmed the selected mesh and all eight selected actions are byte-identical to their installed runtime counterparts:

| Role | Selected source -> installed runtime | SHA-256 |
| --- | --- | --- |
| Mesh | `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/exports/cannibal_siege_eaters.mesh` -> `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters.mesh` | `a632f115a093421a1ac8dee441692d72d8799c097b9d7c9c2f16abd4a6bd9772` |
| Idle | `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/exports/cannibal_siege_eaters_idle.anim` -> `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters_idle.anim` | `dd3a76fe5ebb53d5be754440590b58fb41ab15e48a615adf3ca1326745430a36` |
| Move | `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/exports/cannibal_siege_eaters_move.anim` -> `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters_move.anim` | `a91c331093b364a3741322caa2c38adde28224b32f28ab324198b375306f2632` |
| Attack | `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/exports/cannibal_siege_eaters_attack.anim` -> `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters_attack.anim` | `e2d48c2eb8b9b7e274b8dc221923cb0abc357f4a33a2a4d7442cfe39b8c2e400` |
| Defend | `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/exports/cannibal_siege_eaters_defend.anim` -> `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters_defend.anim` | `47e212329f5b63f8d09680e3bae25ee0668577d82cddde03d988f17c1d88ef2e` |
| Support attack | `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/exports/cannibal_siege_eaters_support_attack.anim` -> `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters_support_attack.anim` | `992022696fb546d1232b05acb69dabc6d7d236798f3596879a9235e32553f0f0` |
| Retreat | `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/exports/cannibal_siege_eaters_retreat.anim` -> `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters_retreat.anim` | `f9acf1d6de9a38eb47469375dd601ebe3daf0c9b4e5f7861699a8020e17b304a` |
| Training | `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/exports/cannibal_siege_eaters_training.anim` -> `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters_training.anim` | `b117d4b6e6905bd7c4fda1a7a023094c7c8fc21a560d2b2ead8c032196007abe` |
| Death | `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/exports/cannibal_siege_eaters_death.anim` -> `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters_death.anim` | `65ca862ce818aa6a591648e1e41006e132d5c6256c1dae6e1418f365dbd5eb5b` |

The three installed DDS paths also physically match the current audit and retained conversion hashes: diffuse `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters_diffuse.dds` (`36bb8558cb4dfb78dfbabf146f88f07075e0c3a524fe21f64f2f12661ea1e441`), normal `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters_normal.dds` (`6c1337e006dec79c599f48c14671a32200ad6566ba686f2d83174f70b60167d3`), and specular `gfx/models/units/014_cannibalism/cannibal_siege_eaters/cannibal_siege_eaters_specular.dds` (`c523e29c6690430c07dd2f0efabba72e337cda78a5de3ffa20a8ce94c46d69fa`).
The provider texture inputs and job-root DDS copies are absent, so direct source-to-runtime byte identity cannot be recomputed.
Copy actor/tool and copy time are not retained for any runtime transfer.

## Audio and counter reconciliation

The partial draft's statement that zero audio hashes matched was false.
All seven role hashes in `evidence/audio_sources/v9_audio_revalidation.json` match the current installed runtime WAV bytes, including the selection role.
The runtime paths, hashes, and action cue times are recorded in the current manifest and evidence JSON.
The v9 receipt only validates WAV media properties and hashes; it points to `evidence/audio_sources/sound_design_v8.json`, which is absent.
The seven job-root `audio/derived` WAVs are also absent.
Source URLs, attribution, license terms, original source bytes, and allowed transformations therefore remain unverified.

The existing counter handoff records these exact tokens and installed files: `GFX_unit_cannibal_siege_eaters_icon_medium` -> `gfx/interface/counters/divisions_large/unit_cannibal_siege_eaters_icon.dds` (`38bb73744db081350aa35aa2f7075dffcd98561652a422294c5a1f93e1ada2fa`); `GFX_unit_cannibal_siege_eaters_icon_medium_white` -> `gfx/interface/counters/divisions_small/onmap_unit_cannibal_siege_eaters_icon.dds` (`062969fb55e754d2332f2110460c2cb618f30c0b414620ca27f31f05cb9cf17c`); and `GFX_unit_cannibal_siege_eaters_icon_small` -> `gfx/texticons/unit_cannibal_siege_eaters_icon_small.dds` (`d5637f955bc8115ade3f2d09772924fe0b146ee61657d27b6cafd5276688470c`).
These hashes were physically verified.
The counter handoff records the installed infantry consumer/DDS dimensions, matching skill-local reference family, green anchor `(73,106,73)`, neutral on-map treatment, and selected-frame behavior.
Parent live review remains pending.

## Proof boundaries and blockers

The retained provider receipt `evidence/v9_provider_lineage.json` records Meshy 7 task lineage and 101 consumed credits.
The selected provider downloads and model-ready input image are absent.
The provider-input hash recorded there is `1ac18b9b008cccc70bc0af30605ca72adcc9030a1c233732559400c9a6744f75`; its bytes and source-page link are absent.

The retained `refs/sourced/manifest.json` names Christian Hadfield's ArtStation illustration, marked all-rights-reserved and `NoAI`, as research-only and explicitly ineligible for ImageGen or Meshy.
It does not prove that source was the provider input.
The retained `evidence/source_gate_override_2026-08-22.md` says the input and descendants were superseded/rejected after the user's correction; the later August 25 handoff says the unchanged input was approved but does not identify its source or document a later rights decision.
Exact-source identity, terms, authorization, preparation prompt, and source-to-refinement comparison remain unresolved.

Eight grounded-v3 reimport report JSON files are present, but each named `blender/checkpoints/reimport_cannibal_siege_eaters_<role>_grounded_v3.blend` file is absent at its recorded path.
The August 25 handoff reports successful action reimports, but this reconciliation did not rerun them.
No standalone mesh reimport receipt was identified.
The existing mesh export report records 29,999 triangles, zero non-manifold or degenerate faces, and 77 loose boundary edges across 16 components; this is retained report data, not visual or live acceptance.

`job.yaml` is absent.
The matching `family_jobs.json` row lacks `asset_id` and profile fields; `humanoid_unit` remains the partial-draft profile supported by retained humanoid-rig and infantry-consumer records.
The August 22 dependency audit is historical and says Blender 5.1.2, `io_pdx_mesh` 0.91.0 with a truncated archive hash, and adapter 1.8.1.
The accepted August 25 handoff reports adapter 1.10.14.
Current exact Blender and extension versions are unresolved.

No Meshy call, key/balance check, Blender operation, health check, runtime asset or wiring write, or game launch occurred in this pass.
This reconciliation used zero paid credits; the historical 101 consumed credits are receipt data, and no historical estimate was found.
No tests or in-game validation were run.

## Evidence

`docs/plans/014_cannibalism_plans/evidence/2026-10-03_cannibal_siege_eaters_manifest_recovery/verified_state.json` contains the selected paths and SHA-256 values, the physical checks, current consumer hashes, source/task receipts, the eight report hashes and missing checkpoint checks, counter hashes, and explicit unresolved fields.
