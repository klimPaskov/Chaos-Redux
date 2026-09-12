# Event 018 cave monster Meshy 7 animation recovery blocker

> Superseded recovery notice, 2026-09-12: The parent task for the current exhaustive audit accepts the installed four-action contract and the state aliases `defend` and `support_attack` to `attack`, `retreat` to `move`, and `training` to `idle` as intentional. This document therefore does not govern the current package disposition. Retain its provider-capability finding only as conditional evidence if an eight-distinct-Meshy-action requirement is explicitly accepted again; the current status and actual remaining source/job blocker are recorded in `../cave_monster_current_package_manifest.md`.

Date: 2026-08-22

Owner: `chaosx_3d_model_pipeline`

Status: `blocked`

Scope: Event 018 cave monster 3D package and runtime candidate only. No gameplay, GFX, entity, sound, counter, or runtime wiring was changed.

## Outcome

The requested eight-role recovery cannot be produced through the currently locked provider route without violating the user's constraints.

The cave monster is a low-slung four-legged creature and therefore a `nonhumanoid_creature`, not a clear standard humanoid biped. The locked Meshy route does not expose a quadruped rig type, custom skeleton, bone map, or locally prepared rig input. `meshy_animate` accepts only a completed Meshy `rig_task_id` and an animation-library `action_id`. It cannot consume the repository adapter's custom creature rig.

The only repository-locked rig route for this anatomy is Blender `author_creature_rig`, with `author_creature_action` as the corresponding local action route. The user explicitly forbids manual, simple, procedural, transform-only, semantic-reuse, and other locally authored final body motion, and requires a genuine Meshy 7 rig plus distinct `meshy_animate` actions for all eight roles. A humanoid Meshy armature on this quadruped is also forbidden by the pipeline skill and would not be a compliant substitute.

No Meshy or Blender operation was called. No credits were spent. Geometry regeneration was not attempted because a replacement quadruped would encounter the same missing provider rig capability and would spend credits without opening a compliant animation path.

## Exact capability blocker

The verified `meshy_rig` schema exposes only these inputs:

- mutually exclusive source inputs: `input_task_id` or `model_url`;
- optional `height_meters`, `texture_image_url`, and `response_format`;
- no anatomy or rig-family selector;
- no quadruped or creature skeleton option;
- no custom bone map;
- no upload or adoption of a locally authored armature.

The verified `meshy_animate` schema requires:

- `rig_task_id` from a completed Meshy rig task;
- one integer `action_id`;
- optional FPS or format post-processing.

This creates a closed prerequisite chain: every compliant action requires a Meshy rig task, but the locked provider rig route is approved only for a clear standard humanoid biped. The repository's nonhumanoid custom-rig route cannot become a Meshy `rig_task_id` and is disallowed as the source of final motion by the user's acceptance rule.

All eight requested semantic roles are therefore blocked at the same provider-rig prerequisite:

| Role | Required final source | Status | Exact reason |
| --- | --- | --- | --- |
| `idle` | distinct Meshy 7 rig plus `meshy_animate` action | blocked | no compliant Meshy quadruped rig task can be produced |
| `move` | distinct Meshy 7 rig plus `meshy_animate` action | blocked | no compliant Meshy quadruped rig task can be produced; rig-included humanoid walking is not an accepted substitute |
| `attack` | distinct articulated Meshy 7 action | blocked | no compliant rig task; aim/lunge, impact, recoil, and recovery preview cannot be generated |
| `defend` | distinct Meshy 7 action | blocked | no compliant rig task; semantic reuse of attack is forbidden |
| `support_attack` | distinct Meshy 7 action | blocked | no compliant rig task; semantic reuse of attack is forbidden |
| `retreat` | distinct Meshy 7 action | blocked | no compliant rig task; semantic reuse of move is forbidden |
| `training` | distinct Meshy 7 action | blocked | no compliant rig task; semantic reuse of idle is forbidden |
| `death` | distinct articulated Meshy 7 action | blocked | no compliant rig task; collapse, impact, and settling preview cannot be generated |

Action-library IDs previously verified for humanoid jobs are deliberately not proposed here. Their existence does not make the cave monster eligible for the humanoid-only provider rig prerequisite.

## Existing runtime candidate retained but not accepted

The installed runtime candidate was left byte-for-byte unchanged. It remains useful only as preserved geometry/material evidence and as a visual identity reference. Its current local 17-bone actions do not meet the requested provider-action provenance standard.

Geometry and material identity:

- one low-slung slate-and-ochre armored quadruped with head, four limbs, carapace, and tail;
- 30,000 triangles and 14,998 welded vertices according to the prior handoff;
- PDX axes: forward `-Y`, up `+Z`;
- entity scale: `0.8`, applied once;
- recorded pre-export vertical height: `7.3518247977`;
- recorded effective runtime height: `5.8814598382`;
- parsed PDX AABB minimum: `[-4.1943497658, -0.0031263828, -6.5398874283]`;
- parsed PDX AABB maximum: `[4.1915650368, 7.3532309532, 6.5516967773]`;
- parsed dimensions: `[8.3859148026, 7.3563573360, 13.0915842056]`;
- effective dimensions at entity scale `0.8`: `[6.7087318421, 5.8850858688, 10.4732673645]`.

Current runtime hashes:

| File | Bytes | SHA-256 | Acceptance status |
| --- | ---: | --- | --- |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster.mesh` | 1,876,278 | `60C256EC1D958F77A93B6F9019A4B7C60072EA2F6B13E69C3672B84C474A491C` | geometry evidence only |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_diffuse.dds` | 4,194,432 | `A876F57B87A36A79FE7A320D4445BD112CBA957474028E1E5680C0439626FE11` | retained |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_normal.dds` | 4,194,432 | `9EF36A184A57A7BD451A6F90C6CB23D50CFC884EE6EE7FBF0958ABB0F3309D19` | retained |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_spec.dds` | 4,194,432 | `9CFC7A88676CE46E4F017381DB38860BDBF84555C1BC59020C2D0FE4D2B88CDF` | retained |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_idle.anim` | 25,276 | `A8EA9301744231054D3DA131AAF7D2EF264E13FD48A5F737325BA531DC9762D0` | rejected local action |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_move.anim` | 14,367 | `077D8ADCB45484215DB7BA6F4F45D95B184785358441DA67980B0D061EB52246` | rejected local action |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_attack.anim` | 17,798 | `13D54654770BD0E82846F847F4CDD14535755F061BA83DB2254F821FD2BB19AA` | rejected local action |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_death.anim` | 20,660 | `5A4677B24D0CB4ED3F506DDB1666B263AABF6D3CDB098255560DF6F773E1601A` | rejected local action |

The current GFX file has only `idle`, `move`, `attack`, and `death`. The entity file aliases `defend` and `support_attack` to attack, `retreat` to move, and `training` to idle. These files were not changed:

- `gfx/entities/018_resources_found_cave_monster.gfx`: SHA-256 `99E2196F8EA4A5A7E7FB483E631EA429C3BFA8D225FC83AF3B2E69CB6D5F2931`;
- `gfx/entities/018_resources_found_cave_monster.asset`: SHA-256 `72F8AD8EEACB9770727D9A4B488E4117326F614153F7AAEAFE0DDBF018B7548A`.

## Source and provider lineage

- historical geometry task: `019fd394-e30c-7fbb-b0da-ee8078b86c38`;
- historical provider model version: legacy, not accepted as proof of a Meshy 7 rig or animation source;
- historical source image path: `docs/assets/018_resources_found/models_3d/cave_monster/refs/original/meshy_input.png`;
- historical source image SHA-256: `F04C5C4B934959D436A1888A3AB0F520D054ECE9CBE56A58D95C5CD22967A361`;
- current source image status: absent;
- declared job root: `docs/assets/018_resources_found/models_3d/cave_monster/`;
- current job-root status: absent;
- provider rig task: none;
- provider animation tasks: none;
- provider response IDs for this recovery: none;
- new or downloaded provider artifacts: none;
- selected source-to-runtime synchronization: no new selection was made; installed bytes remain unchanged.

The prior handoff `docs/plans/018_resources_found_plans/subagent_handoffs/cave_monster_3d_model_handoff.md` has SHA-256 `DC388A4415DC493782DF2A5840D9F30F60E778229B529CD5DBECD3FFA085A534`. The repository-wide animation inventory used for the provenance verdict has SHA-256 `A29E4ED250A4E3B8511BCD183810B414C0B08B9D92126B9940AD840813D5C615`.

## Dependency and route evidence

- official Meshy MCP package: `@meshy-ai/meshy-mcp-server` `0.4.0`;
- Meshy wrapper: `.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd`;
- locked Meshy compatibility revision: `meshy-7-v4`;
- only approved image-to-3D model identifier: `meshy-7`;
- Blender HOI4 adapter: `chaosx_blender_hoi4` `1.7.0`;
- Blender: `5.1.2`, build commit `ec6e62d40fa9`;
- Blender MCP addon: `1.0.0`, configured socket port `9876`;
- `io_pdx_mesh`: release `0.91`, manifest version `0.91.0`, locked archive SHA-256 `A683DF09F30155201D63612127427BD40D018C5C2D19EF98272A129C5B5FF7C2`.

Configuration hashes inspected on disk:

- `.tools/3d_pipeline/config/dependencies.lock.json`: `B5D0D00099F33BDB5C896760A333EFE0B1FED4C6B1287842995904B7BB821C5C`;
- `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`;
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`: `0F4A0E916FF37E1C91EA142D6DC3554A13ED98BFCC0687BC85502C2094F66C23`.

The configuration files and locked source hashes matched the installed repository files during read-only inspection. Live route bootstrap, provider task inspection, balance inspection, Blender socket probing, and adapter operations were deliberately not performed because the shared provider/Blender lane was reserved by the parent and the capability gate already fails before paid work.

## Vanilla reference

The retained scale precedent is the installed western European infantry package:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`: 201,966 bytes, SHA-256 `F00FBADFDACDD1046F7119E62E2C47D644EA7A92D0F686B71D230BC843AEF8BA`;
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/infantry.gfx`: SHA-256 `6439FB7FC1A94E9B2F20368F18BD73526B2ABB9A559B62E58A2C2768396E71D4`;
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset`: SHA-256 `6AB4BE22BC0757C93F8132F7E247910592A5D8595EAF431D33F23DF03F32AA2D`;
- measured vanilla mesh height: `7.3518242835`;
- vanilla entity scale: `0.8`;
- effective vanilla runtime height: `5.8814594268`.

The vanilla entity precedent demonstrates distinct semantic state bindings, but its humanoid skeleton and actions are not valid motion sources for the cave monster.

## Costs

- estimated compliant paid tranche: none, because no compliant provider rig route exists;
- credits consumed: `0`;
- balance checks: none, because no paid tranche was initiated;
- failed paid operations: none;
- recovery confirmation requested: none.

## Validation performed

- confirmed the installed cave monster mesh, texture, animation, GFX, and entity files and recomputed their SHA-256 hashes;
- confirmed the missing deterministic source/job root and missing original input image;
- reconciled the prior handoff against the repository-wide custom-model animation inventory;
- inspected the locked Meshy rig and animation argument schemas;
- inspected the `nonhumanoid_creature` profile and its custom-creature rig route;
- confirmed that the pipeline skill requires a custom rig for quadrupeds and rejects humanoid-armature substitution;
- confirmed that the only available nonhumanoid action-authoring route is local Blender authoring, which the user forbids for final motion;
- confirmed the installed vanilla mesh/entity scale precedent and checksums.

## Validation not performed

- no provider geometry, rig, animation, status, download, or balance call;
- no Blender import, mutation, render, preview, export, or reimport;
- no role-specific previews, because no compliant source actions exist;
- no PDX export/reimport, because exporting the rejected local actions or an invalid humanoid substitution would not advance acceptance;
- no in-game validation, which remains parent/user-owned in all cases.

## Required unblock condition

Work may resume only if the official, version-pinned Meshy MCP route exposes and the repository dependency/schema locks verify a genuine quadruped or custom-skeleton rig endpoint whose completed task can be consumed by `meshy_animate`. That route must support eight distinct role actions and preserve articulated quadruped attack and death motion.

Any alternative based on the existing Blender custom creature rig, locally authored creature actions, a humanoid Meshy rig, semantic aliases, transform-only clips, copied vanilla animations, or geometry regeneration without a compliant rig endpoint is a forbidden simplification and must not be used.

## Remaining parent work

- carry this blocker into the Event 018 completion status;
- do not promote the existing four local actions or four semantic aliases as provider-compliant;
- leave current runtime bindings unchanged unless and until a compliant eight-action package exists;
- if the user changes the acceptance rule, obtain an explicit decision naming the newly approved professional quadruped rig/action source before reopening production;
- if Meshy adds a verified quadruped/custom-rig route, rerun the dependency and schema gates, check the live balance before the paid tranche, reconstruct the deterministic job root, preserve all provider artifacts immediately, and complete role-specific preview plus PDX export/reimport evidence.

No simplification or fallback was used in this recovery attempt.
