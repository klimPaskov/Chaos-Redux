# 3D model pipeline documentation audit

Read-only audit of the 3D model pipeline documentation surface, cross-checked against the pipeline code.

Audit scope: `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`, `.tools/3d_pipeline/README.md`, the `chaosx_3d_model_pipeline` paragraphs of `.agents/skills/chaos-redux-subagents/SKILL.md` (lines 56 and 159-169), `.codex/agents/chaosx_3d_model_pipeline.toml`, `docs/systems/3d_model_pipeline/**`, and the top level of `docs/plans/3d_model_workflow_plans/*.md` (the `adapter_recovery_drafts/**` subtree was excluded from the audit scope).

Cross-checked code: `.tools/3d_pipeline/config/blender_hoi4_adapter.json`, `.tools/3d_pipeline/config/dependencies.lock.json`, `.tools/3d_pipeline/config/asset_profiles.json`, `.tools/3d_pipeline/run_pilot.py`, `.tools/3d_pipeline/adapter/blender_worker.py`, `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py`, `.codex/config.toml`.

Method: every finding below carries a path, a line number, and a short quote from the file as it exists in the working tree at audit time. No file was edited, created, moved, or deleted by this audit other than writing this report. No game launch, no Blender session, no provider call, no network access.

Working-tree state at audit time: `.tools/3d_pipeline/adapter/blender_worker.py` SHA-256 `99EB86B5D0849DDEE1985B02E9058E8425B5BD66B3530E9750FC1EDD22023A65` (6,568 lines), `dependencies.lock.json` mtime `2026-09-22 20:15:41Z`, five adapter sources mtime `2026-09-22 20:33:45Z`.

## 0. Live state facts that change what the next agent should do

These are not documentation defects on their own, but they invalidate part of the documentation surface while an edit is in flight, so they are reported first.

### 0.1 Five locked adapter sources do not match the working tree

`.tools/3d_pipeline/config/dependencies.lock.json:89-108` records `source_sha256` for 18 adapter files, and the 3D skill makes that agreement a publication requirement: `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:139` says "For adapter publication, verify exact operation-array agreement between `.tools/3d_pipeline/config/blender_hoi4_adapter.json` and `routes.blender_hoi4_adapter.operations` in the dependency lock, matching source hashes, and the complete local import closure."

Observed mismatch (`Get-FileHash -Algorithm SHA256` against each locked path, read-only):

| Locked source | Recorded in lock | Actual in working tree |
| --- | --- | --- |
| `.tools/3d_pipeline/adapter/blender_worker.py` | `BF2D5ABB46EEF36A73F4A7B37C33F0C62CD95A9467157CF57FD59CC3487339F3` | `99EB86B5D0849DDEE1985B02E9058E8425B5BD66B3530E9750FC1EDD22023A65` |
| `.tools/3d_pipeline/adapter/explicit_vertex_remap.py` | `397BF088BF0D45FC2E2FFD0901143CC65D42F8C843096ED57725D77208FA0482` | `E2378D8BD91D488A031F5B33DA7304F5E7226978DD2D6FCFAA6E8FD38515F34A` |
| `.tools/3d_pipeline/adapter/mesh_patch_repair.py` | `95831B135DB79631C298A6C979E8946BEF5246A488B93F460EB680E6A4F25F26` | `AB924862C6FDF443EA3F31A0A283CE2600BC62BB58C8AA2BEA5A65C7D237AE1E` |
| `.tools/3d_pipeline/adapter/skeletal_export_partition.py` | `747BBE923740A4A3024F8A44F487C82B1FD40F855BFE742E20E5859E3FCD8406` | `8A2CF2D63E9ED9B3D048472B79683AE6E3B921CEE3B3F43806F7AAE5EDEA77AA` |
| `.tools/3d_pipeline/blender_client.py` | `48EEF0AE32AF4C0D182B5126323F49A1DD09B202860811231B9E6BF84ADCDA42` | `B86961A4B097F1BF16FEFD1D08039AE3731382CFCBD8511A0589472265D0552B` |

The five files were all written at `2026-09-22 20:33:45Z`, after the lock (`20:15:41Z`) and after `run_pilot.py` (`20:28:59Z`), and `git status` reports `.tools/3d_pipeline/adapter/blender_worker.py`, `explicit_vertex_remap.py`, `mesh_patch_repair.py`, `skeletal_export_partition.py`, and `blender_client.py` as modified with `mesh_winding_seam.py`, `pdx_skin_membership.py`, and `tests/test_mesh_winding_seam.py` deleted.

Impact: by the skill's own rule the adapter publication is currently incoherent, and any worker that verifies hashes before mutation (`.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:115` "If route resolution, live schema, add-on installation, bridge reachability, compatibility, or checksum verification fails, stop") will stop. Either the lock must be regenerated after the in-flight edit settles or the edit must be reverted, and no document in the audited scope currently states which.

### 0.2 The 3D skill and four generated agent definitions are mid-edit in the working tree

`git diff --stat` reports `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` at `12 +-` (6 lines changed) and untracked `docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/SUPERSEDED.md`.

The changed skill lines are line 18 (`currently handles only` to `handles only`), line 82 (`weapon-free body` to `item-free body`), line 88 (adds the firearm special-case sentence), line 91 (`held item` to `equipped item`), line 94 (replaces the shortcut sentence with a `No shortcuts in model work` reference), and line 153 (removes the trailing "An operation that would generate a rig..." sentence).

Impact: the skill is the authoritative document for this surface and it is not in a settled state. Findings below quote the working-tree text, which is what a future agent reads, but the parent should confirm the edit is finished before acting on any skill-line finding.

## 1. Contradictions

### C1. Firearm units: ingest the Meshy rig and actions, or bypass Meshy rigging and animation entirely

Side A, current policy in the skill and README:

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:82` "Download each firearm as its own asset, ingest the Meshy rig and the receipt-verified Meshy actions for the body, and author firearm fitting and attachment, rigid weapon controls, locators, and contact corrections live in Blender."
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:378` "ingest the Meshy rig and its receipt-verified provider actions for the body, and author firearm cleanup and fitting, rigid attachment, weapon controls, and held-prop completion in the live Blender session. Provider work on this route supplies the weapon-free body, its textures, its humanoid rig, its preset or Text-to-Motion actions, and the separate firearm geometry".
- `.tools/3d_pipeline/README.md:378` repeats the same route.
- `.agents/skills/chaos-redux-subagents/SKILL.md:165` "then the Meshy rig and its receipt-verified provider actions for that body, and live Blender firearm fitting, attachment, and prop work."

Side B, contradicting text in the agent definition and an in-scope plan:

- `.codex/agents/chaosx_3d_model_pipeline.toml:104` "Rig and animate firearm units directly in Blender, without Meshy rig/animate calls. Model and attach their firearms and other required held objects in Blender. This firearm-specific route takes precedence over the general one-attempt Meshy rig/action route."
- `.codex/agents/chaosx_3d_model_pipeline.toml:2` "Firearm-bearing units regenerate as weapon-free Meshy bodies and go directly to Blender for rigs, modeled weapons, held objects, and animations."
- `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md:11` "This firearm-specific route bypasses Meshy rigging and animation calls."
- `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md:26` "No Meshy rig or animation call belongs to this firearm route."

Code evidence for side A: `.tools/3d_pipeline/run_pilot.py:1309` sets `"humanoid_rig_route": "meshy_standard_humanoid_rig_with_separate_rigid_weapon_attachment"` for the firearm-bearing `alien_infantry` spec, and its seven `required_actions` entries carry `"provider_action_id"` values plus `"authoring_route": "meshy_animate_then_blender_retarget_cleanup"` (`run_pilot.py:1310-1374`).

Blast radius: the stale text is propagated verbatim into the generated definitions that a worker actually loads, at `.claude/agents/chaosx-3d-model-pipeline.md:102`, `.cursor/agents/chaosx-3d-model-pipeline.md:103`, `.opencode/agent/chaosx-3d-model-pipeline.md:103`, and `.qoder/agents/chaosx-3d-model-pipeline.md:105` ("Rig and animate firearm units directly in Blender, without Meshy rig/animate calls.").

This is the highest-impact contradiction in the audit: the agent definition and its four generated copies instruct the exact opposite of the current policy for every firearm-bearing unit.

### C2. The subagents routing gate contradicts the paragraph two lines below it

- `.agents/skills/chaos-redux-subagents/SKILL.md:161` requires the parent prompt to contain "firearm weapon-free body/direct Blender route, general Blender fallback, or non-firearm repair mode".
- `.agents/skills/chaos-redux-subagents/SKILL.md:165` requires the reverse: "Firearm-bearing units, including current firearm models, must receive a fresh Meshy 7 weapon-free body from exactly one weapon-free input, then the Meshy rig and its receipt-verified provider actions for that body".

The same document therefore tells a parent to route firearm units to Blender for rigging and animation and to require the Meshy rig and actions for the same units. Line 161 also still carries "one-attempt Meshy rig/action limits", which is directionally compatible with the skill's "a paid rig or animation attempt is not repeated" (`.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:276`) but is not the phrasing the skill now uses.

### C3. Provider rig eligibility: humanoid-only, or any provider-eligible biped

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:18` "A provider-eligible biped is a bipedal asset with clearly defined limbs and body structure, and it does not have to be human; a bipedal creature or machine that meets that structure may use the provider route."
- `.tools/3d_pipeline/README.md:44` repeats it.
- `.codex/agents/chaosx_3d_model_pipeline.toml:117` "Meshy rigging is limited to a suitable clear standard humanoid biped under the current endpoint rules. Nonhumanoid, mechanical, building, air, and naval assets use Blender rigs when animation is required, with manual Blender action authoring when Meshy does not support the profile."

A bipedal non-humanoid creature is simultaneously eligible at `SKILL.md:18` and excluded at `TOML:117`. The same stale sentence is at `.claude/agents/chaosx-3d-model-pipeline.md:115`, `.cursor/agents/chaosx-3d-model-pipeline.md:116`, `.opencode/agent/chaosx-3d-model-pipeline.md:116`, and `.qoder/agents/chaosx-3d-model-pipeline.md:118`. `.codex/agents/chaosx_3d_model_pipeline.toml:118` and the generated copies add "For new non-firearm packages only, try Meshy rigging at most once per model and each required Meshy animation at most once on a usable supported rig", which is consistent with `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:276` ("a paid rig or animation attempt is not repeated") but is scoped to non-firearm packages only, which C1 already covers.

### C4. The MESHY_API_KEY gate and Blender-only work

- `docs/systems/3d_model_pipeline/overview.md:10-12` "Every entry point checks `MESHY_API_KEY` before path discovery, image generation, balance checks, or local Blender work."
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:101` "Existing-model Blender-only repair may inspect the approved model, job, dependency lock, and Blender routes without this key and must not start a provider call."
- `.tools/3d_pipeline/README.md:18` "For work that calls Meshy, first verify a non-blank `MESHY_API_KEY` environment variable. Blender-only repairs of existing models skip this provider gate."
- `.tools/3d_pipeline/README.md:36` "Blender-only repairs verify their job boundary, Blender adapter, and export stack without a provider dependency."
- `.codex/agents/chaosx_3d_model_pipeline.toml:29` "Blender-only repair may proceed through the verified Blender and export routes."

`overview.md` blocks local Blender work without a provider key; the skill, README, and agent definition all say the opposite. `overview.md` is the first document a reader reaches through `docs/systems/3d_model_pipeline/README.md:7`, so this contradiction affects exactly the Blender-only repair route that the rest of the set authorizes.

### C5. "The locked adapter cannot create a hand locator" versus `author_locator`

- `docs/systems/3d_model_pipeline/clone_equipment_and_infantry.md:67` "Attack, support-attack, and training use their exact exported actions and have complete runtime references, but combined rifle contact remains visually unaccepted because the locked adapter cannot create a hand locator or preview a second mesh attached to the recovered skeleton."
- `.tools/3d_pipeline/README.md:118` "`author_locator` creates or updates one job-owned bone-parented Empty and never geometry or motion."
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:153` "`author_locator` creates or updates one job-owned bone-parented Empty and never geometry or motion."
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json:112` lists `"author_locator"` in the published operation array, `.codex/config.toml:72` enables `"chaosx_blender_hoi4_author_locator"` for production runs, and `.tools/3d_pipeline/adapter/blender_worker.py:4630` defines `def author_locator(req: Dict[str, Any])`.

The runtime gap described in the clone document may still be real, but the stated cause is wrong: the adapter now publishes a locator operation, and `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:312` requires that operation to be used for "A measured muzzle, attachment, or effect locator". A future agent reading `clone_equipment_and_infantry.md` would conclude the capability is unavailable and might not attempt the locator.

### C6. Per-role action identity versus documented entity-state aliasing

- `docs/systems/3d_model_pipeline/chaosx_chaos_assault_battalion_model.md:13` "Entity state aliases use the real attack action for `support_attack`, the real movement action for `retreat`, and the real idle action for `training`."
- `docs/systems/3d_model_pipeline/resources_found_cave_monster_model.md:36` binds `resources_found_cave_monster_attack` to "attack/defend/support attack" and line 35 binds `_move` to "move/retreat".
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:37` "no reuse or light retiming of one role's action for another role".
- `.agents/skills/chaos-redux-subagents/SKILL.md:165` "whole-rig/static substitutes and semantic aliases remain forbidden".
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:384` requires `attack`, `defend`, and `support_attack` to be covered "separately" for every firing state.

Two shipped, documented packages state as accepted practice exactly what the current policy forbids, and the skill never distinguishes an additional entity state from a required role. This needs one authoritative statement rather than two defensible readings, because it decides whether an existing package is complete or queued for re-authoring.

### C7. Whether failed provider stages may be retried automatically

- `.codex/agents/chaosx_3d_model_pipeline.toml:58` "Continue automatically through paid retry or recovery operations made necessary by a failed or rejected generation, remesh, retexture, or conversion attempt while live balance and provider capability permit them. Never ask for another credit-spend confirmation".
- `.tools/3d_pipeline/config/dependencies.lock.json:204-205` records the machine-readable policy `"paid_generation_attempts_per_pilot": 1, "retry_paid_calls": false`.
- `.tools/3d_pipeline/run_pilot.py:1029-1030` writes `"paid_attempts": spec.get("provider_paid_attempts", 1)` and `"retry_paid_calls": spec.get("provider_retry_paid_calls", False)` into every job document, and `run_pilot.py:1307-1308` sets both to the restrictive values for the humanoid pilot spec.
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:290` "do not repeat an identical input after two failures. Where separately authorized and supported by the official MCP schema, `model_url` may use an official `https://assets.meshy.ai/` artifact URL".

The agent definition pre-authorizes automatic repeated paid recovery; the lock policy and the runner's job document say retries are off, and the skill requires separate authorization. This governs money spend, so the divergence should be resolved explicitly.

### C8. The white-box payload key `dual_source_base_rig` is still advertised by the live schema evidence while the code rejects it

- `.tools/3d_pipeline/config/dependencies.lock.json:89-108` locks `blender_worker.py` as the `prepare_candidate` implementation, and `.tools/3d_pipeline/adapter/blender_worker.py:2247-2250` raises "prepare_candidate does not bind geometry to a rig:" for the binding keys tuple at `blender_worker.py:2234-2245`, which includes `"dual_source_base_rig"` at `:2242`.
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:338` states the contract as "Every rig-binding payload key is rejected outright".

No audited document mentions `dual_source_base_rig`, so there is no stale prose claim here. The contradiction is between the code and live schema evidence retained in the repository: `docs/testing/live_qa/20260913_main_menu_startup/model_evidence/adapter_1_10_49_tools.json:122` and `docs/testing/live_qa/20260913_main_menu_startup/model_evidence/adapter_1_10_49_preflight.json:266` record `"dual_source_base_rig"` in the published 1.10.49 tool schema. Those files are outside this audit's scope and are dated evidence, but a worker that greps for the live schema may find a key the current adapter rejects.

## 2. Stale statements

### S1. An in-scope plan still orders every worker onto adapter 1.10.48

`docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md:233` "The transport hold is lifted; every remaining worker must use adapter 1.10.48 through the committed lock-selected route and verify its returned version and source/config hashes before mutation."

The lock records `1.10.51` (`.tools/3d_pipeline/config/dependencies.lock.json:87`), and the skill states "the lock records `1.10.51`" (`.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:141`). This is an operative instruction, not merely a historical note, so it can send a worker to a version that is not the locked one.

### S2. "Current" dependency checks recorded at 1.10.40 with a wrong hash count

`docs/plans/3d_model_workflow_plans/2026-09-09_meshy_motion_endpoint.md:39` "Current read-only dependency checks match all sixteen adapter source hashes at 1.10.40, Blender 5.1.2 build `ec6e62d40fa9`, io_pdx_mesh 0.91.0 archive and installed manifest, and official package/SDK integrity."

The lock's `source_sha256` block contains 18 entries (`.tools/3d_pipeline/config/dependencies.lock.json:89-108`) and the adapter version is `1.10.51`. The sentence opens with "Current", so it reads as live state rather than as the dated validation note its section heading implies.

### S3. The adapter recovery handoff opens with a superseded status

`docs/plans/3d_model_workflow_plans/2026-09-06_adapter_recovery_handoff.md:3` "Status: first tranche published as adapter 1.10.24 after parent review and exact baseline recheck; dependency lock refresh and actual Blender route tests remain parent coordinated."

The document is the named release-evidence companion of the plan surface (`2026-09-06_existing_unit_blender_repairs.md:150` "workers must consult the current lock rather than a version copied into this progress note"), so its leading `Status:` line is read as the current state of a document a worker is told to consult.

### S4. Stale "current lock" hash and operation count in the release log

- `docs/plans/3d_model_workflow_plans/2026-09-06_adapter_recovery_handoff.md:132-133` "Current lock SHA256: `512F41E60A1A76887BAE62A5B4577140F2E407CFF54EB31DB30637EDCB5EE90F`. There are47 operations in both config and dependency lock."
- `:162` "Current47-operation lock SHA is `B553D3A5...`".
- `:177` "Current lock SHA `EAC981D22B8D778A4B8B94AB9C8BDD3C4D7C7032D79946BE55A931A1BF4360F1`; native retry pending."

The current adapter publishes 32 operations at version 1.10.51 (`.tools/3d_pipeline/config/blender_hoi4_adapter.json:4` and `:101-134`, counted 32; `.tools/3d_pipeline/config/dependencies.lock.json:87` and `:151-184`). The count fell from 48 to 32 because the authoring operations were removed, so a reader reconciling the lock against these lines sees an apparent 16-operation regression rather than a deliberate deletion.

### S5. Additional stale version and operation counts in the same append-only log

`docs/plans/3d_model_workflow_plans/2026-09-06_adapter_recovery_handoff.md:44` "released the coherent 1.10.24 dependency lock with 40 operations"; `:224` "Release1.10.40 remains47 operations"; `:260` "Blender release 1.10.41 has 48 operations"; `:277` "with 48 operations and preserved Meshy fields"; `:290` "The coherent 48-operation lock SHA is ..."; `:301` "Release 1.10.44 retains 48 operations".

A reader scanning this log for the operation surface finds six different counts and no pointer to the lock as the authoritative source beyond the in-scope plan's generic advice.

### S6. Stale operation name and stale model name

`docs/plans/3d_model_workflow_plans/2026-09-06_adapter_recovery_handoff.md:19` "`action_provenance` accepts manual GPT-6-astra actions only with retained source-checkpoint and declarative-spec SHA-256, without pretending they are provider actions."

`action_provenance` is not an adapter operation in the 32-op surface; it is an internal worker helper (`blender_worker.py:4906`). The model name is also stale: the canonical definition is `.codex/agents/chaosx_3d_model_pipeline.toml:3` `model = "gpt-6-luna"`, while `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md:5` and `:10` still say "GPT-6-astra".

### S7. Removed operations are still presented as released surface

- `docs/plans/3d_model_workflow_plans/2026-09-06_adapter_recovery_handoff.md:40` "only `repair_explicit_mesh_winding` and `ground_existing_action` were added to the config allowlist." `ground_existing_action` is not in the current operation array (`.tools/3d_pipeline/config/blender_hoi4_adapter.json:101-134`) and is listed as a removed operation in `docs/plans/3d_model_workflow_plans/rig_reauthoring_queue.md:35-45`.
- `:42` lists changed functions including "`author_measured_creature_rig`, `attach_rigid_component`, `author_measured_creature_action`", all removed.
- `:305` "The existing explicit phase patch accepts death phases `standing`, `falling`, `impact`, `rebound`, `settling`, `terminal_hold`", describing the removed phase-patch operation (`rig_reauthoring_queue.md:45` lists `patch_existing_humanoid_action_phases` as removed).
- `:12` "Weight regions accept optional `mesh_names`" describes a removed weight-region operation.

### S8. Present-tense claims that removed authoring operations are live

- `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md:31` "Live discovery confirmed manual bone-phase editing and creature operations in addition to humanoid operations."
- `:53` "The live wrapper returned 28 tools with the key absent, including manual bone-phase editing and creature rig/action operations."
- `:146` "The shared adapter provides measured rest geometry/bone inspection, explicit bone/weight-region authoring, rigid component geometry and manual role phase keys."

All three describe deleted operations in the present or recent-past tense with no date or disposition, directly above the sentence at `:150` that tells workers to trust the lock instead. A worker following `:31` or `:53` will look for tools that no longer exist.

### S9. Files claimed untouched are deleted

`docs/plans/3d_model_workflow_plans/2026-09-06_adapter_recovery_handoff.md:120` "Unreferenced external `mesh_winding_seam.py` and `pdx_skin_membership.py` are excluded from this release inventory and remain untouched."

`git status` reports both `.tools/3d_pipeline/adapter/mesh_winding_seam.py` and `.tools/3d_pipeline/adapter/pdx_skin_membership.py` as deleted, along with `.tools/3d_pipeline/tests/test_mesh_winding_seam.py`. Neither file exists in `.tools/3d_pipeline/adapter/`.

### S10. Stale pilot inventory in the system overview

- `docs/systems/3d_model_pipeline/overview.md:56` "The runner holds the asset specifications for its own slugs, currently the `anomaly_signal_beacon` pilot and the `alien_infantry` unit."
- `docs/systems/3d_model_pipeline/overview.md:103` "The retained bounded pilot is `anomaly_signal_beacon`, a static occult signal beacon prop with one mesh."

Both are consistent with the code (`run_pilot.py:1198-1383` defines exactly those two specs), but line 103 describes one retained pilot while line 56 names two, so the reader cannot tell whether `alien_infantry` is still a supported runner slug. The word "currently" dates line 56 to whenever it was written.

### S11. Stale "Meshy 7 is required for future generation" framing on legacy packages

`docs/systems/3d_model_pipeline/chaos_warfare_facility_models.md:57` "Legacy Meshy provider tasks produced one textured GLB for each facility, and no animation or rigging call was made because the requested consumers are static map-building entities. Meshy 7 is required for future generation."

This is accurate for those two static buildings and is not a policy conflict, but it is the only Meshy statement in that document and it omits the current provider-route policy entirely, so a reader of the facility page alone does not learn that a provider-eligible biped is expected to take the Meshy rig and animation route.

### S12. Durable system docs present queued packages as accepted

`docs/plans/3d_model_workflow_plans/rig_reauthoring_queue.md` queues 20 job roots for re-authoring, including:

- `:26` `002_zombie_outbreak/models_3d/zombies` with "rig, skin weights, actions".
- `:43` `chaos_warfare_system/models_3d/chaos_assault_battalion` with "skin weights, actions, component assembly / scale".
- `:44` `shared_clone_system/models_3d/clone_infantry` with "rig, actions, component assembly / scale".

The matching durable system pages present those packages as accepted without any reference to the queue:

- `docs/systems/3d_model_pipeline/chaosx_zombie_unit_sound_design.md:7` "the parent accepted the repaired Blender v1 rig/actions and controlled death v9".
- `docs/systems/3d_model_pipeline/chaosx_chaos_assault_battalion_model.md:19` "The mesh, all four actions, materials, and all DDS maps were reimported through the locked Blender and `io_pdx_mesh` route."
- `docs/systems/3d_model_pipeline/clone_equipment_and_infantry.md:53` "its entity, mesh, materials, actions, and audio live under the shared clone asset package and are registered without Event 016 or Mengele names."

A grep for `rig_reauthoring_queue` across all of `docs/systems/**` returns zero matches. The queue's own stance is that these rigs and actions were produced by now-forbidden shortcuts (`rig_reauthoring_queue.md:13` "Work produced that way is exactly the shortcut output the policy forbids"), so a reader of `docs/systems` alone would treat shortcut-derived rigs as accepted work.

### S13. The agent definition lists a subset of the verified Meshy tools as the current names

`.codex/agents/chaosx_3d_model_pipeline.toml:59` "Use only actual tool names and arguments discovered from the locked route, including the current verified `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate` identifiers when the live schema confirms them."

The lock's `verified_tools` has 13 entries (`.tools/3d_pipeline/config/dependencies.lock.json:16-30`), and both `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:117` and `.tools/3d_pipeline/README.md:68` list all 13, including `meshy_text_to_motion`, `meshy_get_motion_status`, `meshy_list_motion_tasks`, `meshy_download_motion`, and `meshy_animation_library`. The agent definition's five-missing list is the one a worker reads first.

### S14. In-flight terminology split between "weapon-free" and "item-free"

The working-tree skill was partially rewritten to describe the general rule as items and the firearm case as a special case, while the rest of the surface still says weapon-free:

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:82` (working tree) "require a fresh Meshy 7 item-free body from exactly one item-free prepared input".
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:91` (working tree) "Each required equipped item is generated through its own Meshy 7 geometry task".
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:248` still says "this body image must be weapon-free".
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:549` still says "the weapon-free body at `refs/original/meshy_input.png`".
- `.tools/3d_pipeline/README.md:246` "Every current equipped unit must receive a fresh item-free Meshy 7 body", while `.tools/3d_pipeline/README.md:248` says "Prepare exactly one body-only reference with every held item excluded".
- `.agents/skills/chaos-redux-subagents/SKILL.md:165` "fresh Meshy 7 weapon-free body from exactly one weapon-free input".
- `.tools/3d_pipeline/run_pilot.py:1257` "generated as a clean weapon-free true T-pose humanoid".

Until the edit is completed across the whole set, the same requirement has two names and the firearm-only path is stated inconsistently.

## 3. Duplication

### D1. The skeleton, skinning, and action policy block is copied four times

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:14` and `:16` and `:18` (authoritative version).
- `.tools/3d_pipeline/README.md:40` and `:42` and `:44` (near-verbatim copy).
- `.agents/skills/chaos-redux-subagents/SKILL.md:163` and `:165` (paraphrase).
- `.codex/agents/chaosx_3d_model_pipeline.toml:104`, `:118`, and the four generated copies.

Every policy change currently has to be made in seven places, and C1 and C3 show that five of them are already out of date. The skill should own the rule text; the README, the subagents skill, and the agent definition should carry a one-line pointer to `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` plus only the facts that are unique to them (the agent definition's tool policy, the routing gate's prompt checklist).

### D2. The deterministic job layout tree exists twice and the copies have diverged

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:178-220` includes `refs/source/` with `untouched.<ext>`, `provenance.json`, and `source_search.md`.
- `.tools/3d_pipeline/README.md:132-170` omits `refs/source/` entirely and starts at `refs/original/`.

Neither tree lists `refs/firearms/` or `refs/equipment/`, which the held-item route requires (see M1). One document should own the tree, most naturally the README because it is the job-layout reference for the wrapper, and the skill should link to it rather than restate it.

### D3. The three ingestion-operation contracts are duplicated verbatim

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:153`.
- `.tools/3d_pipeline/README.md:122-126`.

The two texts agree today, but they are the most argument-dense paragraphs in the set and they are also the ones most likely to drift with the next adapter release. The skill should own the behavioural contract and the README should link to it.

### D4. The held-item input path rule is stated in three places with different completeness

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:91` gives both `refs/firearms/<firearm_id>/meshy_input.png` and `refs/equipment/<item_id>/meshy_input.png`.
- `.tools/3d_pipeline/README.md:250` gives both.
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:248` gives only the firearm path.
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:549` gives only the firearm path.

The general rule should be stated once, in the section that owns input preparation, and the prompt sections should reference it rather than restate half of it.

### D5. The adapter operation surface is enumerated in four places

- `.tools/3d_pipeline/config/blender_hoi4_adapter.json:101-134` (32 entries).
- `.tools/3d_pipeline/config/dependencies.lock.json:151-184` (32 entries).
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:141-151` (grouped and annotated).
- `.tools/3d_pipeline/README.md:98-110` (grouped).

Agreement between the first two is a hard publication gate (`SKILL.md:139`), so the grouped lists in the skill and README add nothing checkable and already have to be maintained in parallel. The annotated grouping belongs in the skill only, with both config files named as the machine-readable source.

### D6. The equipped-item rule is stated three times with drifting wording

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:86-95`.
- `.tools/3d_pipeline/README.md:242-258`.
- `.agents/skills/chaos-redux-subagents/SKILL.md:165`.

The README adds rules the skill does not have ("Every current equipped unit must receive a fresh item-free Meshy 7 body, even when its armed predecessor was considered complete" at `README.md:246`), and the skill adds rules the README does not have (per-frame contact re-check wording at `SKILL.md:94`). One of the three should be the rule text; the others should link.

## 4. Unclear or overloaded sections

### U1. `SKILL.md:153` is one 2,400-character paragraph carrying eight operation contracts

The line covers `inspect_mesh_landmarks`, `repair_explicit_mesh_winding`, `author_locator`, `inspect_animation_source`, `sanitize_runtime_candidate`, `prepare_export_coordinate_checkpoint`, `import_animation_action`, `import_bvh_animation_action`, `retime_animation_action`, the `.codex/config.toml` production subset, and the surface prohibition. A reader cannot act on it: required arguments, optional arguments, and failure conditions for nine operations are interleaved with no structure. The in-flight edit already trimmed its tail, which shows the paragraph is being carried rather than maintained.

### U2. `SKILL.md:517` is a single-sentence manifest field list

"Each model manifest entry records the asset ID/slug, profile, source mode, source reference, ... and status." The sentence lists roughly 45 required fields, including nested conditional requirements such as "explicit `attack`, `defend`, `support_attack`, and additional-state discharge and muzzle/effect/sound synchronization rows or a zero firing-state/effect/sound audit for `non_firing`". A manifest author cannot verify compliance against it, and a reviewer cannot check it. This is the single largest actionability problem in the skill after U1.

### U3. "Allowlisted" means two different things and the required static-building gate is not in the allowlist

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:486` "the final working checkpoint must pass the allowlisted `bake_static_mesh_transforms` gate before export".
- `.tools/3d_pipeline/README.md:355` "Before a static-building export, run the allowlisted `bake_static_mesh_transforms` operation on the approved working checkpoint."
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:336` uses "the verified repository-owned allowlisted adapter" for the whole 32-operation surface.

The production MCP subset at `.codex/config.toml:66-83` enables 16 tools and does not include `chaosx_blender_hoi4_bake_static_mesh_transforms`, `chaosx_blender_hoi4_partition_static_mesh_export_batches`, `chaosx_blender_hoi4_partition_skeletal_mesh_export_batches`, or `chaosx_blender_hoi4_inspect_mesh_landmarks`. A worker taking "allowlisted" to mean "available through the configured MCP tools" cannot run the mandatory static-building gate. The one document that resolves this is out of scope (`docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md:30` "structured calls through `BlenderAdapterClient.call` or `lib.mcp_stdio` and `wrappers/run_blender_hoi4_adapter.cmd` when the session tool list is stale"), so the in-scope docs need one sentence stating which route reaches a non-enabled operation.

### U4. The same term is used for two scopes of asset

The set uses "provider-eligible biped", "provider-eligible bipedal model", "provider-eligible bipedal body", "provider-eligible bipedal profile", and (in the agent definition) "a suitable clear standard humanoid biped". The first four mean the same thing; the last means something narrower, which is the substance of C3. The skill should define one term with the anatomy constraints and use it everywhere.

### U5. `overview.md` "Live-validation status" mixes dated history with an undated current claim

`docs/systems/3d_model_pipeline/overview.md:121` contains "The 2026-07-22 launch waiver is retained as historical evidence, but it is no longer the current runtime state", then "The showcase uses an idempotent `on_startup` consumer and a tag-specific `on_daily_GER` repair hook", then "The latest user-run session still reports renderer geometry corruption and a missing building, so live completion remains unclaimed." "The latest user-run session" has no date, so a reader cannot tell whether this is the current blocker or a superseded observation, and the paragraph sits in a document whose index entry says it "describes the shared production, conversion, export, and validation workflow" (`docs/systems/3d_model_pipeline/README.md:7`).

### U6. The repairs plan mixes accepted scope, dispatch contract, progress log, and a live instruction with no disposition

`docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md` contains an "Accepted scope" section (`:3-13`), a "Firearm worker dispatch contract" (`:15-46`), a "Workflow implementation" log (`:48-56`), a "Repair register" with per-package dispositions (`:58-73`), an "Active repair coverage" table (`:92-116`), dated progress sections (`:118`, `:152`, `:192`, `:207`), and the stale worker instruction at `:233`. There is no header disposition (`implemented`, `superseded`, `unresolved`, and so on) even though `AGENTS.md` requires one for plan documents, so a reader cannot tell which sections are binding instructions and which are history.

### U7. The zombie sound-design page carries three competing "current" states

`docs/systems/3d_model_pipeline/chaosx_zombie_unit_sound_design.md:5` "Current disposition: runtime WAVs and sound definitions are installed, while sonic clip choice is **needs_user_review** ... and subunit-specific acknowledgement selection has no verified consumer." Then `:79` "Five older attack/death files do not yet have an equally durable per-file source-to-runtime mapping", then `:91` "The earlier specialized-zombie intake ... is a dated snapshot", then the section at `:103` "Current movement provenance closure, 2026-09-20" which supersedes part of `:79`, then `:109` "The movement provenance gap is closed" while "the five older attack/death files remain installed only for specialized wrappers and still lack durable per-file source-to-runtime mappings". The reader must assemble the actual open-item list from four places, and the disposition at line 5 is not updated by the later sections.

### U8. The re-authoring queue does not say what a reader should do

`docs/plans/3d_model_workflow_plans/rig_reauthoring_queue.md:3-8` states the queue exists and that it "does not itself accept or reject any existing asset", `:47-51` states what re-authoring must produce, and `:51` states the fallback statuses. But no per-model disposition is recorded, there is no owner column, and `:55` "36 plan and handoff documents under `docs/plans/` still describe work performed with the removed operations" is followed by a 36-entry list that includes this document and `2026-09-06_adapter_recovery_handoff.md`. A model worker cannot tell from this document whether its package is `accepted and queued`, `blocked`, or already re-authored.

### U9. The system index describes a document that does not match its content

`docs/systems/3d_model_pipeline/README.md:7` says `overview.md` "describes the shared production, conversion, export, and validation workflow", but `overview.md:101-129` is a pilot-specific status page with a "Pilot profile", a dated "Live-validation status", and a "Known review items" list. Four of the ten pages in the directory are per-package runtime records while six are listed as contracts, and the index does not separate the two kinds.

## 5. Missing coverage

### M1. The job layout does not contain the item input directories the route requires

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:91` requires "firearms under `refs/firearms/<firearm_id>/meshy_input.png` and other items under `refs/equipment/<item_id>/meshy_input.png`".
- `.tools/3d_pipeline/README.md:250` requires the same.
- The layout tree at `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:178-220` lists `refs/source/`, `refs/original/`, `refs/derived/`, and `refs/briefs/` only.
- The layout tree at `.tools/3d_pipeline/README.md:132-170` lists `refs/original/`, `refs/derived/`, and `refs/briefs/` only, and omits `refs/source/` even though `SKILL.md:161` requires the intake to carry "immutable Internet source path or documented search record".

A worker creating a job root from either documented tree produces a layout in which the mandated item inputs have no home, and the README's tree omits the immutable source location that the same README's evidence rules rely on.

### M2. `import_animation_action` and `import_bvh_animation_action` required arguments are under-specified

The live signatures are `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py:793-808` for `chaosx_blender_hoi4_import_animation_action` (required: `job_id`, `blend_rel`, `source_rel`, `provenance_rel`, `checkpoint_rel`, `source_action_name`, `target_armature_name`, `target_action_name`, `source_kind`, `source_reference_id`, `source_sha256`; optional: `bone_chains`, `promote_audited_target`, `source_armature_name`, `root_scale_reference`) and `:838-857` for `chaosx_blender_hoi4_import_bvh_animation_action` (required additionally including `semantic_role`, `source_fps`, `target_fps`, `bone_chains`, `root_motion_policy`).

The documented contract at `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:153` and `.tools/3d_pipeline/README.md:122` names only "a new sibling checkpoint, a new target action name, an explicit 64-character source SHA-256 digest, and a provenance receipt" plus the receipt's matching fields. It never names `source_rel`, `provenance_rel`, `source_action_name`, `source_armature_name`, `target_armature_name`, or `source_reference_id` as inputs, even though `source_action_name` is the "exact source action id" the same sentence makes the operation's central contract, and it does not state that the named action must exist in the source file: `.tools/3d_pipeline/adapter/blender_worker.py:5515` reports `"requested_source_action": source_action_name` and `:5505` resolves it with `source_action = next((action for action in source_actions if action.name == source_action_name), None)`. For the BVH variant the doc also omits that `source_action_name` must equal the verified file stem: `blender_worker.py:6074` "source_action_name must exactly match the verified BVH filename stem."

### M3. The mandatory Text-to-Motion root-scale reference is undocumented

`.tools/3d_pipeline/adapter/blender_worker.py:5624` raises "Text-to-Motion requires explicit measured root_scale_reference joint-head pairs." and `:5627` restricts it with "root_scale_reference requires source_head_bones and target_head_bones only." The skill lists `meshy_text_to_motion` as part of the verified route (`.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:117`) and requires "the preset-action and Text-to-Motion animation tasks" (`:276`), but the operations paragraph at `:153` never mentions `root_scale_reference`, and no document states that a Text-to-Motion ingestion fails closed without the measured joint-head pairs. `docs/plans/3d_model_workflow_plans/2026-09-06_adapter_recovery_handoff.md:263` describes it for adapter 1.10.41, which is not a worker-facing document.

### M4. Provider rig and animation credit estimates are absent from the documented preflight

`.tools/3d_pipeline/run_pilot.py:1303-1306` carries `"remesh_estimate_credits": 5`, `"rig_estimate_credits": 5`, `"animation_estimate_credits": 3`, `"planned_total_credits": 61`, and `:1446` falls back to `44 if spec.get("asset_kind") == "humanoid" else 30` when a total is not declared.

The documents state only the generation charge and the remesh charge: `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:286` "The documented textured Meshy-7 charge is 30 credits" and `.tools/3d_pipeline/README.md:94` "Textured Meshy 7 image-to-3D generation is estimated at 30 credits, and the remesh of a source above 300,000 triangles is estimated at 5 credits." No document states a rig estimate, an animation estimate, or the humanoid tranche total, even though `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:284` makes the rig task and its animation tasks part of the pre-authorized planned paid path and `:284` requires recording estimates before each paid tranche.

### M5. The durable system pages do not carry the re-authoring disposition

Covered as S12. As a coverage gap: no page under `docs/systems/3d_model_pipeline/` names `docs/plans/3d_model_workflow_plans/rig_reauthoring_queue.md`, and no page tells a reader that an apparently accepted rig or action may be listed for re-authoring.

### M6. `overview.md` never describes the current provider, item, or no-shortcut policy

`docs/systems/3d_model_pipeline/README.md:7` advertises `overview.md` as the workflow description. In fact `overview.md:53-99` describes provider generation, the adapter's seven steps, scale calibration, textures, and job contents, and it never mentions the Meshy rig and animation route, the separated equipped-item route, the 32-operation surface, the no-shortcuts rule, or the attempt limits. The only provider-route sentence is the artifact-transport note at `:70-76`. A reader who starts from `docs/systems` gets the pre-provider-rig description of the pipeline.

### M7. The runner's own firearm-bearing spec plans no separate firearm input

`.tools/3d_pipeline/run_pilot.py:1257` describes the `alien_infantry` brief as "One reusable generic bald green alien infantry soldier generated as a clean weapon-free true T-pose humanoid, plus one separately retained rigid retro-futurist laser rifle attached to the Meshy rig without Blender-authored body motion."

`required_components` at `run_pilot.py:1264` includes "separate rigid retro-futurist laser rifle with trigger grip, fore-end, shoulder stock, and forward muzzle", so this is a firearm-bearing spec under the current policy. The policy requires each required firearm to be generated "through its own Meshy 7 geometry task from exactly one item-only image" (`.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:91`) from `refs/firearms/<firearm_id>/meshy_input.png`, and to be attached in the live Blender session. The spec instead says "separately retained", and the job root `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/` contains no `refs/firearms/` directory and no `refs/original/` directory (its only reference file is `refs/derived/20260906_weaponfree_body.png`). Either the spec is under-specified or the rifle is intended to come from the source artwork, and no document resolves which.

### M8. The production MCP subset and the required static-building operations are unreconciled

Covered as U3. As a coverage gap, no in-scope document states which of the 32 operations are reachable through the configured MCP server and which require the wrapper or `BlenderAdapterClient.call`. `README.md:114` and `SKILL.md:153` mention the 16-operation subset only as a fact about `.codex/config.toml`, not as a constraint a worker must route around.

### M9. The legacy declarative-spec provenance kind is undocumented

`.tools/3d_pipeline/adapter/blender_worker.py:4917` still accepts `fields["source_kind"] == "manual_blender_gpt6_astra"` in `action_provenance`, requiring a retained declarative-spec hash and reporting `processing_policy="manual_blender_gpt6_astra_hash_bound_declarative_action"` (`:4922`). The paths that *wrote* that provenance belonged to removed modules, and only stale `__pycache__` artifacts for `fitted_humanoid_repair` and `manual_creature_rig` remain in `.tools/3d_pipeline/adapter/__pycache__/`.

No audited document mentions this kind. `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:153` states "`source_kind` is one of `meshy_animate`, `meshy_text_to_motion`, or `professional_source`", and `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:14` forbids generating keyframes from a declarative spec. The read path means an action carrying declarative-spec provenance can still be exported and promoted by the current surface, which is a deliberate legacy allowance or an oversight, and the documents give a worker no way to tell which.

## 6. Checks that came back clean

These were specifically requested or are load-bearing for the findings above, and no defect was found.

- `init_pilot_jobs.py` and `config/pilot_jobs.json`: neither exists (`.tools/3d_pipeline/init_pilot_jobs.py exists: False`, `.tools/3d_pipeline/config/pilot_jobs.json exists: False`). No audited document references them, and `docs/systems/3d_model_pipeline/overview.md:62` correctly states "There is no separate job generator and no repository pilot job list." The remaining references are in dated `docs/testing/live_qa` baseline captures and in `docs/plans/repo_cleanup`, both outside this audit's scope.
- `specialized-zombie` / `--specialized-zombie-batch`: no audited document offers it as a route, and the runner refuses it by design (`.tools/3d_pipeline/run_pilot.py:1466-1477`, raising "--specialized-zombie-batch is not a route of this runner."). The only in-scope mention is the correct historicization at `docs/systems/3d_model_pipeline/chaosx_zombie_unit_sound_design.md:91`.
- `dual_source`: no audited document mentions `dual_source` or `dual_source_base_rig`. The only in-scope occurrence of the concept is absent, and the code rejects the payload key at `.tools/3d_pipeline/adapter/blender_worker.py:2229-2248`. See C8 for the out-of-scope schema evidence.
- The "provider supplies geometry only" claim: no audited document makes it. The closest text is accurate and current (`.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:378` "Provider work on this route supplies the weapon-free body, its textures, its humanoid rig, its preset or Text-to-Motion actions, and the separate firearm geometry"), and `.tools/3d_pipeline/README.md:341` correctly limits its claim to the runner ("The pilot runner is a provider-generation, static-mesh, and export orchestrator, and it is not a rigging or animation route.").
- Adapter version and operation count: `.tools/3d_pipeline/config/blender_hoi4_adapter.json:4` records `"adapter_version": "1.10.51"`, its `operations` array at `:101-134` has exactly 32 entries, the dependency lock agrees at `:87` and `:151-184`, and `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:141` and `.tools/3d_pipeline/README.md:112` both say 32 at 1.10.51. The authoritative statements are correct; only the stale plan prose (S4, S5) disagrees.
- The 16-operation production subset: `.codex/config.toml:66-83` has exactly 16 entries, matching `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:153` and `.tools/3d_pipeline/README.md:114`, and it does include all three ingestion operations (`:76-78`) and `author_locator` (`:72`).
- The `prepare_candidate` anti-shortcut guard: `.tools/3d_pipeline/adapter/blender_worker.py:2248` "prepare_candidate does not bind geometry to a rig:" matches `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:338` "Every rig-binding payload key is rejected outright".
- Blender and io_pdx_mesh versions: `.tools/3d_pipeline/config/dependencies.lock.json:72` records Blender `5.1.2` and `:188-190` records io_pdx_mesh `0.91.0`; `docs/systems/3d_model_pipeline/overview.md:38` and `.codex/agents/chaosx_3d_model_pipeline.toml:37` agree.
- The building calibration constants are stated identically in four places: `.tools/3d_pipeline/config/asset_profiles.json:43-46`, `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:78`, `.tools/3d_pipeline/README.md:349`, and `docs/systems/3d_model_pipeline/chaosx_3d_runtime_contract.md:9` all give `facility_land.mesh`, `building_land_facility`, source height `3.4697628021`, entity scale `0.6`, effective runtime height `2.0818576813`, and a `4.0` m runtime footprint ceiling.
- The `verified_image_models` gate: `.tools/3d_pipeline/config/dependencies.lock.json:54-57` contains only `meshy-7`, matching `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md:119` and `.tools/3d_pipeline/README.md:20`.

## 7. Could not determine

- Whether the in-flight working-tree edits to `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` and the five adapter sources are complete. The skill edit is internally inconsistent at audit time (S14), and the lock has not been regenerated for the five changed sources (0.1).
- Whether `.codex/agents/chaosx_3d_model_pipeline.toml` and its four generated copies are expected to be regenerated from a single source, or maintained by hand. No in-scope document states the generation relationship; `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md:51` says the Qoder and Cursor definitions "were synchronized from the canonical TOML", which implies generation, but `.claude` and `.opencode` copies are not named there.
- Whether entity-state aliasing of one action across `training`, `retreat`, `defend`, and `support_attack` is permitted for a package that is otherwise complete (C6). The skill's "no reuse or light retiming of one role's action for another role" and the documented packages cannot both be binding without a scope statement, and no document supplies one.
- Whether the legacy `manual_blender_gpt6_astra` provenance read path (M9) is an intentional allowance for already-shipped packages or a leftover. The writers are deleted, so no current operation can create it, but nothing in the documents says it may still be exported.
- Whether `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/` is meant to receive a separate Meshy firearm task (M7). The job root currently has no `refs/firearms/` directory, and the runner spec says the rifle is "separately retained" rather than separately generated.
- The current runtime state of the `anomaly_signal_beacon` showcase. `docs/systems/3d_model_pipeline/overview.md:121` reports renderer geometry corruption and a missing building from an undated "latest user-run session"; this audit did not launch the game, and live consumer validation belongs to the user.

## 8. Suggested authoritative homes

Short routing guidance only; no rewrite of correct text is proposed.

- Skeleton, skinning, action policy, the no-shortcuts rules, attempt limits, and the adapter operation contract: `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` owns the rule text; `.tools/3d_pipeline/README.md`, `.agents/skills/chaos-redux-subagents/SKILL.md:161-169`, and `.codex/agents/chaosx_3d_model_pipeline.toml` should link to it and keep only their unique content.
- Deterministic job layout, provider credit preflight values, and the entry-point commands: `.tools/3d_pipeline/README.md` owns them because it is the wrapper-facing reference; the skill should link.
- Adapter version, operation count, and the enabled production subset: `.tools/3d_pipeline/config/dependencies.lock.json` and `.tools/3d_pipeline/config/blender_hoi4_adapter.json` are the machine-readable source; no prose should restate a version or count as current.
- Firearm-bearing route and equipped-item separations: one home in the skill, with `.agents/skills/chaos-redux-subagents/SKILL.md:161` reduced to a pointer so it cannot drift from `:165`.
- Building scale, footprint, placement, and runtime consumer contract: `docs/systems/3d_model_pipeline/chaosx_3d_runtime_contract.md` already owns this and is consistent; `overview.md` should link to it instead of describing the pilot.
- Re-authoring status of already-shipped rigs and actions: `docs/plans/3d_model_workflow_plans/rig_reauthoring_queue.md` owns the queue, and each durable page in `docs/systems/3d_model_pipeline/` whose package is listed there should carry the queue reference and its disposition.
- Dated adapter tranche history: `docs/plans/3d_model_workflow_plans/2026-09-06_adapter_recovery_handoff.md` should be treated as an append-only log, and its `Status:` line and "Current ..." lines should be read as of their tranche dates rather than as live state. No content is proposed for deletion.
