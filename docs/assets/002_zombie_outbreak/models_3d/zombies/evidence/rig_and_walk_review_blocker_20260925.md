# Base Zombie Rig and Walk Review

**Current status: incomplete and blocked for promotion.** The Meshy rig task succeeded as a provider operation, but its skeleton fails the required complete-segment review, and the included walk does not meet zombie-shamble semantics. A later paid Frankenstein walk was also rejected. Seven paid action FBXs passed receipt hash checks and remain unaccepted source candidates. The isolated 90k body candidate still needs topology and full visual review; manual rig/action capability, PDX texture binding, exports, actual-byte reimport proof, and parent runtime wiring remain open. Approval of the optional CC0 Quaternius zombie walk is pending. The sections below preserve the earlier 40-credit review snapshot unless this continuation explicitly updates them.

## Approved input and provider lineage

The user approved `refs/original/meshy_input.png` with SHA-256 `3723991B3EFC92D573CA1CB94CDC6177EB1D501EE5F207DB1613D4E50C3EB3BB` and a maximum planned spend of 64 credits on 2026-09-25. Candidate 01 (`843CDC9D40F0E8FF442517EB8A0E700D9E0BD6C772EC37B98D8D32C5AE830A19`) remains rejected by the user as “too human” and was not used.

| Stage | Provider task | Actual credits | Preserved artifact and SHA-256 |
| --- | --- | ---: | --- |
| Meshy 7 body | `01a0d867-77fa-77c6-8978-54811dc54881` | 30 | `provider/downloads/base_zombie_body_01a0d867.glb` — `91E33DB67199BC3C1EBF60DF81F2C3D955F2B2C9A9AA170EB8275F2ECC813705` |
| One remesh | `01a0d87a-2242-722b-a67f-e8caabc60527` | 5 | `provider/downloads/base_zombie_remesh_01.glb` — `94AE4BC290FC6A559530D9755063288193722C112DC1F901BC602DD47396181C` |
| One rig attempt | `01a0d8ab-75d5-73b0-9861-44b202bf341a` | 5 | `provider/downloads/base_zombie_rig_01.glb` — `60295C0C92ED32991186B5B9E94DC9F3420560BB65C568DD5641E51C8747670D` |
| Included walking artifact | Same rig task | 0 additional | `provider/downloads/base_zombie_rig_01_walking.glb` — `1FA11380CD97B5ACA02F1957F112FE495F78CABFBF96D4B193026108E9C96E58` |

At this review snapshot, total Meshy spend was 40 of 64 authorized credits, leaving 24 under the ceiling. Subsequent paid animation tasks consumed all 24 remaining credits; the current total is 64 of 64, with zero available under the approved ceiling. No repeated body, remesh, rig, or individual animation task was submitted.

## Paid animation continuation

The one Frankenstein Walk task `01a0d8e5-fc14-7142-ac18-1358d38fcb77` cost 3 credits and was rejected for `move_shamble`. Seven distinct 3-credit action tasks cost the remaining 21 credits. Their FBXs passed receipt hash checks recorded in `provider/downloads/meshy_animation_download_manifest.json`, but none is accepted as a runtime action.

| Candidate role | Paid task |
| --- | --- |
| `idle` | `01a0d901-756e-74cf-92f0-5e81b0628a65` |
| `attack_unarmed` | `01a0d901-df3b-75f3-9f5a-94c16fcf3a28` |
| `defend` | `01a0d901-ce9a-7161-aa19-aba0cefbd0b2` |
| `support_attack` | `01a0d901-d24e-7637-b96e-7b9d75da6c34` |
| `retreat` | `01a0d901-d56b-7426-9c5d-5d7bfc5473ad` |
| `training` | `01a0d901-d925-7661-83b1-079545900a76` |
| `death` | `01a0d901-dc85-7472-a71a-6beae45c2d9e` |

## Geometry and rig review

The one remesh measured 181,493 triangles and 173,692 vertices, with 132,585 loose boundary edges, 62 branched boundary components, no non-manifold edges, and no degenerate faces. The original generated body measured 951,880 triangles and 508,656 vertices, with 64,158 loose boundary edges. The installed vanilla `western_european_infantry.mesh` reference measured 3,018 triangular polygons and 2,021 vertices in the read-only adapter review at `blender/reports/component_review_77deab26cb3a460c8085e9ae8caa5b25.json`; its copied source is `blender/working/meshy_rig_review_02/reference/western_european_infantry.mesh` with SHA-256 `F00FBADFDACDD1046F7119E62E2C47D644EA7A92D0F686B71D230BC843AEF8BA`.

The first walk import exposed a second source mesh named `Icosphere`. Adapter inspection showed that it has 42 vertices, no vertex groups, no armature modifier, and a spherical 1.90 × 2 × 2 m source bound; after normalization it obscured the zombie in previews. It is excluded by exact source-object name in the isolated review import because it has no character anatomy or authored rig relation. The untouched provider GLBs remain preserved.

The isolated review import used the exact walking GLB copy with SHA-256 `1FA11380CD97B5ACA02F1957F112FE495F78CABFBF96D4B193026108E9C96E58` and excluded only `Icosphere`. The resulting working body is one rigged mesh, `char1.001`, with 161,215 triangles and 156,926 vertices, normalized to 7.351824 m mesh height for vanilla entity scale 0.8 (5.881459 m effective runtime height). Body topology still reports 124,443 loose boundary edges and 2,044 branched boundary components; no non-manifold edges, degenerate faces, zero-length normals, or negative-scale objects were reported. The remaining open-edge count is unresolved and high risk.

The 24 bones are `Hips`, `LeftUpLeg`, `LeftLeg`, `LeftFoot`, `LeftToeBase`, `RightUpLeg`, `RightLeg`, `RightFoot`, `RightToeBase`, `Spine02`, `Spine01`, `Spine`, `LeftShoulder`, `LeftArm`, `LeftForeArm`, `LeftHand`, `RightShoulder`, `RightArm`, `RightForeArm`, `RightHand`, `neck`, `Head`, `head_end`, and `headfront`. There are no finger/thumb or jaw segments. The adapter reports 156,926 weighted vertices, 29,651 with one influence, 68,757 with two, 23,515 with three, and 35,003 with four; all weights sum approximately to one, with no zero-weight vertices and no vertex above four influences.

This rig **fails** the skill’s complete-segment requirement, which forbids missing finger and jaw segments. The hands can only move as whole hand meshes, and the mouth cannot articulate for a bite. The reviewed clip therefore cannot serve as the complete zombie rig, even though sampled large-limb motion did not show an obvious exterior tear.

## Included walk review

The working action is `Armature|walking_man|baselayer_WORKING`, 27 frames at 24 FPS. It contains 168 bone-channel rows over the 24 bones. The adapter removed 72 bone-scale curves from the working action; the resulting action curve hash is `82D3E8106C9359953B022373ADFCBF592627106A88914E409F5A235572768C3E`. The sampled clip is an upright ordinary alternating gait with arms nearly static, not a zombie shamble. It is rejected as the `move_shamble` action. Frames 0, 13, and 26 show no obvious visible body tear in front, side, and rear renders, but this limited visual sample does not resolve the open-edge topology risk or establish full-deformation acceptance.

The nine isolated renders are preserved under `blender/previews/`:

- `zombies_walk_review_02_f0_focused_dac8b95b89ff_front.png`
- `zombies_walk_review_02_f0_focused_dac8b95b89ff_left.png`
- `zombies_walk_review_02_f0_focused_dac8b95b89ff_rear.png`
- `zombies_walk_review_02_f13_focused_64f0af733e0f_front.png`
- `zombies_walk_review_02_f13_focused_64f0af733e0f_left.png`
- `zombies_walk_review_02_f13_focused_64f0af733e0f_rear.png`
- `zombies_walk_review_02_f26_focused_e28a7d9cf122_front.png`
- `zombies_walk_review_02_f26_focused_e28a7d9cf122_left.png`
- `zombies_walk_review_02_f26_focused_e28a7d9cf122_rear.png`

The isolated import’s final normalized checkpoint is `blender/working/meshy_rig_review_02/blender/checkpoints/05_pre_export.blend`, 26,326,578 bytes, SHA-256 `7697D1EE728B9B0090C9C4A662CD5ADB23F07871897D619F712E97BCA7883988`. The input GLB, all checkpoints, provider artifacts, and renders are retained. Checkpoints named `03_rig_approved.blend` and `04_actions_approved.blend` are pipeline scaffold outputs and are not acceptance evidence.

## Blocker and role status

The locked Blender adapter is `chaosx_blender_hoi4` 1.10.51. Its allowlist in `.tools/3d_pipeline/config/blender_hoi4_adapter.json` has no bone-creation, vertex-group-creation, or keyframe-authoring operation. `author_locator` only creates a bone-parented Empty; `edit_explicit_mesh_vertices` can edit exact positions or weights only against existing deform bones; the import and retime operations ingest existing authored actions and do not create new motion. The live tool inventory confirmed the same boundary. Manual completion of the missing rig segments and skeletal actions is blocked until an approved locked adapter route can author them.

| Required role | Status | Evidence or blocker |
| --- | --- | --- |
| `idle` | blocked | No accepted complete rig or authored action; Blender keyframe-authoring operation is absent. |
| `move_shamble` | blocked | Included walk and paid Frankenstein walk rejected; optional CC0 Quaternius zombie walk approval pending. |
| `attack_unarmed` | blocked | No finger or jaw controls, and no live keyframe authoring route for a distinct claw attack. |
| `defend` | blocked | No live keyframe authoring route for a distinct performance. |
| `support_attack` | blocked | No live keyframe authoring route for a distinct performance. |
| `retreat` | blocked | No live keyframe authoring route for a distinct performance. |
| `training` | blocked | No live keyframe authoring route for a distinct performance. |
| `death` | blocked | No live keyframe authoring route for an articulated collapse, impact, and settle. |

No `.mesh` or `.anim` runtime candidate has been accepted or exported, and no export/reimport proof exists. The remesh material currently has no verified PDX texture bindings. The three bespoke counter DDS files have passed parent visual review and are installed at their active paths with matching staged hashes; this satisfies only the counter leg, with live consumer review still pending. A CC0 zombie vocal source archive and its licence record are staged under `audio_sources/`, but no attack/death role selection or action synchronization has been accepted. This handoff does not claim runtime completion.

## Recovery path

Keep the exact approved input, provider GLBs, isolated checkpoints, seven receipt-verified action FBXs, and renders as evidence. Do not repeat any paid task or submit another paid task under the exhausted 64-credit ceiling. Resolve the 90k candidate's topology and complete visual review, then use a verified approved live Blender authoring route for missing rig segments and any required action repairs. Re-audit weights and deformation; separately obtain approval before using the optional CC0 Quaternius zombie walk. Complete PDX texture processing, `.mesh`/`.anim` export, byte-bound reimport proof, sound role selection and synchronization, and parent runtime review. The three bespoke counters are already at their active runtime DDS paths with matching staged hashes; their live consumer review remains with the user.
