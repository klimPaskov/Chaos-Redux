# Event 002 Humanoid Zombie Meshy Animation Remediation Handoff

## Status

`in_progress_lane_held`

This handoff is a preparation and evidence-recovery record, not a completion claim. The shared Meshy provider route is intentionally occupied by the Alien Infantry job. Per parent direction, no further environment verification, balance query, paid provider call, Blender adapter call, Blender mutation, export, reimport, runtime copy, or runtime wiring has been performed while that lane is occupied.

The six packages remain REDO until a genuine Meshy rig and eight distinct `meshy_animate` source actions have provider task lineage, meaningful visual proof, PDX export/reimport proof, and selected-source-to-runtime hash synchronization.

## Owned scope

- Evidence owner: `docs/assets/002_zombie_outbreak/models_3d/infected_zombies/`.
- Shared recipients: `undead_zombies`, `rabid_zombies`, `parasitic_zombies`, `necrotic_zombies`, and `mutant_zombies` under `docs/assets/002_zombie_outbreak/models_3d/`.
- Candidate runtime roots, parent-owned and not edited: `gfx/models/units/chaosx_infected_zombies/`, `gfx/models/units/chaosx_undead_zombies/`, `gfx/models/units/chaosx_rabid_zombies/`, `gfx/models/units/chaosx_parasitic_zombies/`, `gfx/models/units/chaosx_necrotic_zombies/`, and `gfx/models/units/chaosx_mutant_zombies/`.
- Parent-owned entity and registration files, not edited: the matching `gfx/entities/chaosx_*_zombies.{gfx,asset}` files and `gfx/models/units/chaosx_*_zombies/animation_chaosx_*_zombies.asset` files.
- Required consumer states: `idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death`.

## Required references and locked environment

The preparation pass read `AGENTS.md`, the complete `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents` skills, the offline Graphical Asset Modding and Entity Modding wiki pages, vanilla `gfx/entities/units_infantry.asset`, and the relevant registrations in vanilla `gfx/entities/infantry.gfx`.

The repository locks the official `@meshy-ai/meshy-mcp-server` at `0.4.0` with git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, Meshy SDK `1.29.0` at git head `e12cbd7078db388152f6e839abdbe09ba01f3f32`, compatibility revision `meshy-7-v4`, and the exact generation identifier `meshy-7`. The Blender lock selects Blender `5.1.2` build `ec6e62d40fa9`, Blender HOI4 adapter `1.7.0`, addon `1.0.0` on socket port `9876`, and `io_pdx_mesh` `0.91.0` with SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.

The Meshy API key hard gate passed. A route verification attempt then reported 64 exact-route processes because the Alien Infantry job owned the shared provider lane. The parent confirmed that occupancy is intentional and instructed this worker not to rerun verification or use provider/Blender routes until explicitly released. No balance check or paid operation was made by this remediation pass.

## Vanilla scale and state precedent

The selected read-only vanilla geometry precedent is `gfx/models/units/infantry/western_european_infantry.mesh`, registered through `infantry_rifle_entity`. Its measured collision-excluded source height is `7.351824797689915`, entity scale is `0.8`, and effective runtime height is `5.881459838151932`; forward is `-Y`, up is `+Z`. The six jobs already carry this calibration. Any accepted replacement rig must preserve the calibrated mesh-space height and apply entity scale exactly once.

Vanilla `units_infantry.asset` contains the eight required state roles. Chaos Redux currently exposes four canonical runtime actions and aliases `defend` and `support_attack` to attack, `retreat` to move, and `training` to idle. Those aliases are forbidden for this remediation even though vanilla uses some aliases in other surfaces.

## Recovered owner lineage

The current selected infected geometry is Meshy 7 task `01a023ec-a81c-79d3-b61d-ac696b286812`:

| Artifact | SHA-256 |
| --- | --- |
| `provider/downloads/generation_meshy7_3_model.glb` | `E25EB7EB3CC5A88AAE15A67E2912791F65300A14A76BCE172605A579C118BFEB` |
| `provider/downloads/generation_meshy7_3_model.fbx` | `8226760D7F80F28820E8988EAA730EDB4F8B47A8282627378BD6F6179B8DC8C9` |

Its rig-target remesh task `01a023f5-45f1-7ff5-b693-6c074b9a784b` produced GLB SHA-256 `9115697C758AC0FD3F1981A21794261B5E3621001124BE35D9DC3548DDA931DA` and FBX SHA-256 `773745F9D9D5180D5B3A0651228B6F19B6756BEB0298C633AA12DA5DEB5574A0`. Three subsequent rig tasks failed: `01a023fc-4ca6-7d2c-b77f-f7a17c268b15`, `01a0240b-11e3-70dd-9d54-91f58edcf0dc`, and `01a02426-f3b4-78b8-b17c-05f97644ffea`. This geometry therefore remains a candidate, not an accepted rig source.

An earlier Meshy 7 recovery chain did rig successfully: geometry `01a02060-98d3-7db3-a2fd-5e866e669f7c`, remesh `01a02068-fc04-72ee-bc44-3ca23db564b3`, and rig `01a0206c-4e74-783e-893e-4002a518741b`. The frozen rig artifacts are GLB SHA-256 `4A176B1145193845CEE471512C9F904B41825F1349CD514E06E212D8ECAD9EC2` and FBX SHA-256 `A1C9A830B041E1C8FEB1AF9FDF9F1EC456E0449EF5A646FD03A75E534486EFD6`.

Three earlier `meshy_animate` outputs are preserved only as recovery candidates:

| Role | Meshy action ID | Task ID | GLB SHA-256 | FBX SHA-256 | Credits |
| --- | ---: | --- | --- | --- | ---: |
| idle | `0` | `01a02070-0ba2-72b2-a002-eece4df96ec4` | `01B8B2B938E681548FF34F9D93B7B76856B2D94937FDC1525C4DBBAB043A122A` | `5DF89292AC6FEAAE7AF7BD595613FB0074A7A31AE8B5244A18D32595BF803D43` | 3 |
| attack | `4` | `01a02070-7eef-759b-ba5c-fd94788f9e2f` | `DA047A7C3A6440129235298F35D266BAEE8F5EEB9FEE326B5C2FB44F89D4F562` | `8BFBEF21749A86F57EF788794C17B1DA9F66463545F471EFC2BF1A7D16D1A55B` | 3 |
| death | `8` | `01a02071-21d2-7027-81ca-b46b87ba0a6b` | `E368C78397D06B379E233FDA01E729226C5BB3F0DA70E53BE59D456B6123ED15` | `582F7E9798C8B8FD8D9B39AAF45318E426C5AB01C83B2FE753E1E1A9DC3CB88A` | 3 |

All five `provider/shared_humanoid_lineage.json` files record byte-identical copies of these rig, idle, attack, and death artifacts, and zero recipient paid calls. This proves copy provenance but does not accept the final runtime actions because the later Blender reports say the provider rig was not used and the final motions were locally authored.

## Selected recipient geometry

| Recipient | Meshy 7 task | Selected GLB SHA-256 | Selected FBX SHA-256 |
| --- | --- | --- | --- |
| `undead_zombies` | `01a024f0-6e2d-7f35-80ec-cdfe1d4deb66` | `6F1340A7B13CC86C801A79C8273A6D4F4C587D32F2153AD0DDC304E6AF814E07` | `2AF06AB6FCB79480891C75721BB7392C0872A767A79D993AE9A9DB88AB40C824` |
| `rabid_zombies` | `01a024d5-8afa-748e-a682-b8e2cfbae869` | `CC0BBEAAE734CEEE64F8E1CC633A199812922E32EED0A6FC2C6611E6EFE20E8A` | `9A1348ABCFABA8AAB09EEAE5A5434FB362613BD90A65A126890D5260ACA552B1` |
| `parasitic_zombies` | `01a024a4-b01b-7bc7-a929-f17756dd61ba` | `57D32B4077F4A26F69D355EC18DD845A90F36C3445227F2570A4092512902758` | `B0A409C2D0B421FDE701DD5F67943EFC12DDD3112109DA83C1A2758970A18123` |
| `necrotic_zombies` | `01a0249a-343c-72b1-8316-cf3fa0062967` | `F63ED867E2E9945540C2DECD0A97E1CC74F796AD8275BB78F02CD3BC96575747` | `C0937507F40803D3359BC48FBE1D8857EC7352442A2670C2D920960E64E621F8` |
| `mutant_zombies` | `01a02493-edb6-78a7-b1c8-ddbe4aba2399` | `4A42A8762C2C2BDE48DAC806067C4A7F8D79E96CE8D15B65523027AAAB73E533` | `99732A9A1CCA6EE1D16B5D77572B889CF94C3D2B4443632650C2152D3F1686D8` |

Each selected geometry is only a rig candidate. It must pass a clean Meshy rig and deformation/contact review. Regeneration is required if the provider rig rejects it or if meaningful animation reveals unsuitable topology; forcing the local recovery rig is not permitted.

## Prepared eight-role Meshy action mapping

The official Meshy animation library was inspected at `https://docs.meshy.ai/en/api/animation-library`. The following is a source-candidate matrix, not visual acceptance. Every result must be downloaded immediately, hashed, imported through the locked adapter, and reviewed from meaningful phases before selection.

| Runtime role | Candidate Meshy action | ID | Root policy | Loop policy | Required visual gate |
| --- | --- | ---: | --- | --- | --- |
| idle | Idle | `0` | in place | loop | Visible breathing/sway with moving limbs and stable feet; reject a static or near-static pose. |
| move | Mummy Stagger Inplace | `650` | in place | loop | Repeating articulated zombie gait, clean foot contacts, no skate, no forward root drift. |
| attack | Punch Combo | `198` | in place | non-loop | Visible wind-up, two or more articulated strikes, follow-through, and recovery; reject weapon-dependent or transform-only motion. |
| defend | Block1 | `138` | in place | non-loop or held endpoint after engine review | Distinct guard raise and impact-ready defensive posture, with no reuse of attack keys. |
| support_attack | Grip and Throw Down | `389` | in place after contact correction | non-loop | Distinct grappling/lunge sequence with torso and arm articulation; reject if an invisible partner makes the action semantically incoherent. |
| retreat | Injured Walk Backward Inplace | `638` | in place | loop | Clearly backward defensive withdrawal, alternating foot contacts, and no alias to move. |
| training | Boxing Warmup | `385` | in place | loop only if endpoints are clean | Distinct active drill/warmup motion; no idle alias and no weapon requirement. |
| death | Fall Dead from Abdominal Injury | `188` | in place after contact correction | non-loop | Articulated injury reaction, collapse, ground impact, and settled ending pose; reject floating or abrupt terminal keys. |

`support_attack` ID `389` is the highest semantic-risk candidate and must be rejected if its implied partner produces obvious empty-air interaction. Prepared alternates, also pending visual inspection, are `386` Zombie Scream for a supporting intimidation action and `609` Boxing Practice Inplace for a distinct close-combat support sequence. Move alternates are `669` Slow Orc Walk Inplace and `678` Unsteady Walk Inplace. No alternate may silently replace the named role after a failed/rejected paid result; failure-driven extra recovery must follow the applicable credit authorization rule.

All calls should request provider source motion first and normalize to 24 FPS through the provider `post_process = change_fps` capability when supported by the locked live schema. Blender cleanup may remove scale channels, correct contact/root translation, retarget, bake, and trim only while preserving substantive provider motion. It may not create replacement keys, procedural cycles, whole-rig motion, static actions, or semantic aliases.

## Owner-first execution plan after lane release

1. Re-run the dependency verifier only after the parent confirms the provider lane is free, require zero exact-route processes, then probe the locked Blender socket separately as specified by the lock.
2. Check the live Meshy balance immediately before the paid owner tranche and record available balance, estimates, actual charges, request IDs, response IDs, and task IDs.
3. Submit the infected selected/remeshed geometry to the clean Meshy rig gate. If its existing three failures recur, use the earlier successful Meshy rig only if its corresponding geometry still passes current geometry and visual acceptance; otherwise regenerate suitable Meshy 7 geometry under the already authorized necessary regeneration path.
4. Run eight distinct `meshy_animate` calls against the accepted owner rig using the candidate matrix, download GLB and FBX immediately, checksum both, and preserve raw outputs.
5. Import each result to a protected source collection, create working duplicates, normalize/bake non-destructively, and render contact sheets or motion previews that show meaningful phases. Attack and death require explicit articulated phase evidence.
6. Export and reimport all eight owner actions through the locked `io_pdx_mesh` path. Record FPS, range, loop policy, driven bones, root policy, deformation, contact checks, export hash, reimport hash, and proof blend per role.
7. Only after owner acceptance, propagate the exact accepted action sources with task/action IDs and source hashes. Each recipient selected geometry must pass a clean Meshy rig/deformation gate. Retargeting may be used only as a non-destructive transfer of the accepted provider motion, with per-recipient previews, action reports, export/reimport evidence, and hashes.
8. Update the six jobs, provider histories, lineage ledgers, action manifests, QA reports, and package handoffs only from selected final evidence. Do not preserve `pdx_exported` or `ready_for_user_live_validation` claims for the rejected local-action set.
9. Hand the parent the eight exact runtime action identifiers per package. The parent owns `.asset`, `.gfx`, entity state binding, and final runtime copy/synchronization.

## Paid-operation estimate

No credits were consumed by this remediation pass. The minimum fresh owner tranche is one rig at the locked historical estimate of 5 credits plus eight animations at 3 credits each, or 29 credits. If each of the five distinct recipient geometries requires its own provider rig while reusing the accepted owner action sources through allowed retargeting, add 25 credits, for a 54-credit minimum shared-batch plan. This estimate excludes geometry regeneration/remesh and any failure-driven retry. The live balance and live tool estimates must be recorded before each paid tranche.

Running eight animations independently on every recipient rig would be 174 credits for six rigs and 48 animations. That is not the prepared default because the shared-owner design calls for traceable accepted owner action propagation, but it becomes necessary if provider/Blender evidence shows that retargeting does not preserve deformation or semantic fidelity. Do not assume either cost path until the infected owner rig/action gate is visually accepted.

## Exact parent runtime wiring after accepted exports

For each slug, the model worker will propose eight stable action identifiers using `chaosx_<slug>_<role>` and deliver eight `.anim` artifacts under `gfx/models/units/chaosx_<slug>/`. The parent must register all eight identifiers in `animation_chaosx_<slug>.asset` and bind the matching entity states in `gfx/entities/chaosx_<slug>.asset` without aliases:

- `idle -> chaosx_<slug>_idle`
- `move -> chaosx_<slug>_move`
- `attack -> chaosx_<slug>_attack`
- `defend -> chaosx_<slug>_defend`
- `support_attack -> chaosx_<slug>_support_attack`
- `retreat -> chaosx_<slug>_retreat`
- `training -> chaosx_<slug>_training`
- `death -> chaosx_<slug>_death`

The parent must also synchronize any corresponding `.gfx` animation declarations and compare the model-worker export hash, reimported evidence hash, and final runtime hash for every role. The worker will not edit these parent-owned runtime files.

## Files changed in this preparation tranche

- Created this handoff: `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/002_humanoid_zombie_meshy_animation_remediation_handoff_2026-08-22.md`.
- `.tools/3d_pipeline/reports/environment_report.json` was refreshed by the single pre-lane-clarification verifier attempt and recorded the occupied exact route. It is a shared generated report and was not reverted or manually edited.

No package job, manifest, provider ledger, Blender checkpoint, preview, runtime model, `.asset`, `.gfx`, gameplay, localisation, audio, or counter file was changed.

## Blockers and pending evidence

- Temporary coordination hold: the parent has not released the shared Meshy lane. This is not a final task blocker and must not be reported as a completed or blocked package.
- No fresh provider rig or animation task IDs exist yet.
- No fresh balance/credit evidence exists yet.
- The eight action IDs are library candidates only; none has passed visual phase, contact, deformation, semantics, export, or reimport gates.
- Geometry suitability remains unproven for all six selected candidates until the Meshy rig gate and articulated action review run.
- No runtime action is accepted, copied, or wired by this tranche.
- Sound and counter packages were outside this animation-only remediation ownership and were not changed. Their existing status must remain under the parent package audit; this handoff makes no package-completion claim.
- Live in-game consumer validation remains parent/user-owned and cannot be claimed by the model worker.

## Simplifications and omissions

No animation simplification has been substituted. Work is deliberately incomplete while the shared provider lane is held: there are no locally authored fallback actions, static poses, transform-only actions, whole-rig actions, semantic aliases, unverified provider substitutions, or runtime completion claims in this tranche.
