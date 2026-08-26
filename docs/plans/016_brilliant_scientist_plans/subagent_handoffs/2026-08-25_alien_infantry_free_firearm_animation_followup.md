# Alien Infantry free firearm animation follow-up

> Superseded by the Meshy V13 package and static runtime promotion recorded in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_meshy_runtime_promotion_2026-08-26.md`; retain this file for free-package rejection evidence only.

Date: 2026-08-25  
Owner: `chaosx_3d_model_pipeline`  
Asset: reusable `alien_infantry` package  
Outcome: blocked; no additional eligible action or muzzle locator was found

## Result

The already approved Quaternius Universal Animation Library Standard remains the only verified free humanoid firearm package that produced valid Alien Infantry exports. Its accepted source actions remain `Rig|Rig|Pistol_Shoot`, `Rig|Rig|Pistol_Idle_Loop`, and `Rig|Rig|Walk_Loop`. Their `.anim` files and actual-byte reimport proofs were not changed.

One additional clearly free and redistributable package, Quaternius Universal Animation Library 2 Standard, was retrieved and audited. Its free Standard tier contains no firearm aim, fire, recoil, reload, death/collapse, armed retreat, or pistol-compatible defensive action and no firearm or muzzle locator. No action qualified for retargeting. Defend, support attack, retreat, and death remain blocked. The accepted firing action's frame 6 / 0.1667-second discharge phase remains provisional for runtime use because no stable muzzle locator exists.

No gameplay, entity, GFX, `.asset`, sound-definition, or localisation file was edited. No weapon was attached or reparented. No local, procedural, transform-only, static, or semantic-alias animation was created.

## Free package and provenance

- Title: Quaternius Universal Animation Library 2.
- Creator/publisher: Quaternius.
- Official source: `https://quaternius.com/packs/universalanimationlibrary2.html`.
- Creator-uploaded distribution: `https://opengameart.org/content/universal-animation-library-2`.
- Direct download: `https://opengameart.org/sites/default/files/universal_animation_library_2standard.zip`.
- Retrieved: 2026-08-25.
- License: CC0 1.0 Universal/Public Domain Dedication, confirmed by the official page, OpenGameArt entry, and embedded `License.txt`.
- Archive: `evidence/professional_animation/quaternius_universal_animation_library_2_standard/universal_animation_library_2standard.zip`, SHA-256 `EC0E40D6D78FE9AAAD59E322F40865A8675C22F0745E291622E54520391A9217`.
- Embedded license: `evidence/professional_animation/quaternius_universal_animation_library_2_standard/extracted/Universal Animation Library 2 [Standard]/License.txt`, SHA-256 `F9B1DE4E8FEFF135555AC1C7D2EEC65035A05FD74E4D632A3F826AC985C3F22C`.
- Unity FBX: SHA-256 `D4A2DD67BB12BF0C01891BC59EE697E04DB679D26883D30BD937C2F3FB6FEC90`.
- Unreal/Godot GLB: SHA-256 `0815DD05531CAE9BC313FC9C0BA81330BC72F8E19EC45F73738E74DDC5796A43`.
- Short-path adapter copy: `provider/downloads/quaternius_ual2_standard_audit.fbx`, exact-byte FBX SHA-256 `D4A2DD67BB12BF0C01891BC59EE697E04DB679D26883D30BD937C2F3FB6FEC90`.
- Source status: retained as non-shipping provenance and inspection evidence.

The full action-name inventory is in `evidence/professional_animation/quaternius_universal_animation_library_2_standard/audit.md`. It includes 42 substantive melee, shield, traversal, work, idle, hit, and zombie clips. It includes no `Pistol`, `Gun`, `Shoot`, `Fire`, `Reload`, `Aim`, `Death`, or `Collapse` action. `Hit_Knockback`, `LayToIdle`, shield, sword, and zombie actions were not relabelled as requested roles.

The Quaternius Animated Guns Pack was also researched at `https://quaternius.com/packs/animatedguns.html`. It is CC0 and advertises six animated gun models, but it is weapon-only rather than a humanoid firearm-action source. It was not downloaded or used because this task forbids attaching or reparenting a weapon and the package does not establish a compatible Alien Infantry muzzle locator.

## Locked route and validation evidence

- Dependency lock: `.tools/3d_pipeline/config/dependencies.lock.json`, current SHA-256 `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`.
- Meshy schema lock: `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`, SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`; exact generation identifier `meshy-7`, compatibility revision `meshy-7-v5`.
- Blender adapter config: `.tools/3d_pipeline/config/blender_hoi4_adapter.json`, current SHA-256 `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`.
- Official Meshy MCP package: `@meshy-ai/meshy-mcp-server` 0.4.0, SDK 1.29.0, locked git head `d8c77d3fd1ca67955367869fdfe74f7298c9f1b0`.
- Blender: 5.1.2, build `ec6e62d40fa9`.
- Repository Blender HOI4 adapter: `chaosx_blender_hoi4` 1.10.14.
- `io_pdx_mesh`: 0.91.0, locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Adapter health request: `59993fb3e7a24130b77fc10a9a80a3aa`; bridge listening at `127.0.0.1:9876` and io_pdx import/export functions present.
- First long-path audit request: `73076144d8bd414ebde6ca080929465c`, failed before import because the deeply nested extracted source path could not be opened. The byte-identical short-path copy was then used.
- Successful audit request: `8450b7c3d19a4f298e69c220bda462e9`.
- Audit report: `blender/reports/quaternius_universal_2_standard_audit_prepare.json`.
- Audit report SHA-256: `4A77FA0CA3F8BA336338C527EA8D362799053160AAE6E45230DFC054EFE05B88`.
- Source checkpoint: `blender/source/quaternius_universal_2_standard_audit_provider_source.blend`, SHA-256 `28E29E997963F1195F7FCCEBBAB7EF84DA6E5C0AE54EBAE222761DF6D46A74FE`.
- Adapter request/result receipts: `logs/adapter/73076144d8bd414ebde6ca080929465c.json`, `logs/adapter/73076144d8bd414ebde6ca080929465c.result.json`, `logs/adapter/8450b7c3d19a4f298e69c220bda462e9.json`, and `logs/adapter/8450b7c3d19a4f298e69c220bda462e9.result.json`.
- Result-receipt SHA-256 values: health `BC1D091E20047ED1ECC5E37BC7407E0806F5ADFE54E41B4672FA7D552E0FE072`, long-path failure `2C8791352E9F0E98E6288B547506EC610FF3738FCA9E3B7C65135B8B2115692B`, successful audit `EC0395492B9E0B4E3DF135FABAB8D16A973C3819BAF24963597BE4AB5CA6675A`.
- Vanilla reference: installed `gfx/models/units/western_european_infantry.mesh`, package copy `blender/reference/western_european_infantry.mesh`, source height `7.3518242835`, entity scale `0.8`, effective runtime height `5.8814594268`, forward `-Y`, up `+Z`.
- Vanilla entity precedent: `gfx/entities/units_infantry.asset`; its rifle entity uses `node = "muzzle"` for attack/defend/support-attack effects. The Alien Infantry source and locked adapter do not supply an equivalent locator.

The audit FBX contains one 65-bone armature and one closed 13,744-triangle mannequin. This geometry was inspected only to enumerate the animation source; it is not an Alien Infantry runtime candidate. No source action was imported onto the accepted Meshy R2 rig, so no new `.anim` export or actual-byte reimport was appropriate.

## Cost and provider lineage

No paid provider call was made. Meshy credits estimated and consumed for this follow-up: `0`. The existing accepted Meshy R2 rig lineage is unchanged: rig task `01a0380c-df10-7a2c-ab1e-c28d2248b616`, FBX SHA-256 `398E796CF47539FAF7EE4D1AE4C860B73EEA69D4B90C59FF5A0425DADCC54124`. A new Meshy attempt was not materially justified because the supported official actions had already been audited across independent recovery lineages and the newly researched professional package supplied no distinct required action.

## Unchanged accepted exports

- Laser attack: `export/anim/alien_infantry_quaternius_laser_attack.anim`, SHA-256 `5B5260F21FAFC8827275827FF99A6D5BCAC29A02D8EAA99ED7ECEAE8D555C4AC`, actual-byte reimport passed; provisional discharge frame 6.
- Idle: `export/anim/alien_infantry_quaternius_idle.anim`, SHA-256 `710D86BE58C74CC6BCE58A5BB9411D975BE31693B8D6530A1390A2BBE64EE09F`, actual-byte reimport passed.
- Move: `export/anim/alien_infantry_quaternius_move.anim`, SHA-256 `79E561F831D9C40C752D38412CF0C415A1FE03C07914AFE70A52DB58F35D4E79`, actual-byte reimport passed.

## Blockers and parent work

- Muzzle locator: blocked. Neither verified free package provides a usable locator, the accepted R2 rig has no muzzle bone, and the locked adapter exposes no locator-authoring operation.
- Defend: blocked. The first-library `Crouch_Idle_Loop` failed balance review; the additional package has shield-specific motion only.
- Support attack: blocked. No independent substantive firearm action exists; aliasing `Pistol_Shoot` is forbidden.
- Retreat: blocked. No semantically valid armed retreat action exists in either inspected free package.
- Death: blocked. First-library `Death01` loses pistol contact; the additional Standard package has no death/collapse clip.
- Parent runtime wiring: must remain pending. Do not bind the particle, light, or firing sound until a stable muzzle locator exists, and do not claim the entity complete until every required role is valid.

Meaningful validation skipped: no action retarget, export, or actual-byte reimport was run because the source inventory did not contain an eligible semantic action. In-game consumer validation remains parent/user owned and was not performed.

## Files created or updated

- `evidence/professional_animation/quaternius_universal_animation_library_2_standard/` source archive, extracted evidence, and `audit.md`.
- `provider/downloads/quaternius_ual2_standard_audit.fbx` exact-byte short-path audit copy.
- `blender/source/quaternius_universal_2_standard_audit_provider_source.blend` and adapter audit report/previews.
- Adapter request/result receipts for health, failed long-path import, and successful short-path audit.
- `manifest.md`, `runtime/crosswalk.md`, `runtime/handoff.md`, and `history.jsonl` updated with the blocked follow-up.

No simplification or unapproved fallback was used. The package remains incomplete with explicit blockers rather than substituting invalid motion.
