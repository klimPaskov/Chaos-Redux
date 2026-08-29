# Event 020 plague-rat animation recovery handoff — 2026-08-22

## Result

The shared plague-rat geometry and five installed runtime animation files remain untouched. The requested eight-role provider-action replacement is `blocked` by the verified production route, not accepted as complete and not replaced with local or aliased motion.

The missing production root `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/` is absent from the worktree, absent from `HEAD`, and has no path history in the local Git repository. The retained handoff identifies one legacy geometry task, `019fd39c-3f8e-7f96-bd04-214ccbb7d64f`, and response group `d60d46ca-ef2d-43f4-ab50-84b883e9e946`, but no action-specific provider task ids survive. The five installed `.anim` files therefore remain lineage-unverifiable.

No provider, Blender, adapter, runtime-wiring, gameplay, GFX, entity, sound-definition, counter, or commit operation was performed in this pass. The shared Meshy/Blender lane was reserved by the Alien Infantry job during the recovery audit.

## Scope and identity lock

- Owner: `020_black_plague`.
- Asset slug: `rat_ground_unit_shared`.
- Intended evidence root: `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/`.
- One shared identity only: `black_plague_rat_mesh` and `black_plague_rat_entity`.
- Consumers retained: `rat_swarm`, `rat_brutes`, `rat_burrowers`, `rat_carrion_guard`, `rat_dock_stowaways`, and `rat_tunnelers`, across `RTA` and `RTX`.
- Forbidden identity changes retained: no bipedal rat substitute, human anatomy, subtype mesh, Rat King mesh, weapon, armor, uniform, crown, or second creature.

## Recovered runtime evidence

| Artifact | Size | SHA-256 | Status |
| --- | ---: | --- | --- |
| `gfx/models/units/020_black_plague_rat/black_plague_rat.mesh` | 2,994,782 | `52C4C6B5E4EB41D6726DDD5EA7271E8FD486C1136B5F4CF7E496E3FED639EBA4` | Installed geometry; source lineage incomplete because the job root is absent |
| `black_plague_rat_idle.anim` | 22,528 | `894A84BD75294AE56F245885E76AD034C3687F8100DBA564F0821D6B98821B9C` | Installed; provider-action lineage unverifiable |
| `black_plague_rat_move.anim` | 12,862 | `F53FA3DE5D12000988DD61EE2DC2DC5491B4D6B56CF1E2237B386976E54BA5CF` | Installed; provider-action lineage unverifiable |
| `black_plague_rat_attack.anim` | 15,946 | `BFF4D999BF778B6B5CE802C15754D600815F864A61A312548BD87B900F90AE82` | Installed; provider-action lineage unverifiable |
| `black_plague_rat_retreat.anim` | 12,862 | `CB4DC54FC89D7CB20E1481FFD3337950AC4D42F66AF8D49A8AD7B780A6C22529` | Installed; provider-action lineage unverifiable |
| `black_plague_rat_death.anim` | 19,770 | `95195F3BFADB2E796F354EADDAADBD585C53258D6D6F94D8387EEF98FF3C4601` | Installed; provider-action lineage unverifiable |

The installed entity currently maps `defend` and `support_attack` to `attack`, and maps `training` to `idle`. Those three aliases fail the dedicated-role rule even if the referenced files later receive valid lineage.

## Eight-role disposition

| Role | Current state | Required recovery result |
| --- | --- | --- |
| `idle` | Present file; lineage unverifiable | Dedicated provider/professional breathing, ear, whisker, and tail motion; looping and in place |
| `move` | Present file; lineage unverifiable | Dedicated articulated quadruped locomotion; looping and in place |
| `attack` | Present file; lineage unverifiable | Dedicated lunge, bite, or claw motion with wind-up, strike, contact/recoil, and recovery; non-looping and in place |
| `defend` | Alias to `attack` | Dedicated bracing, guarding, or evasive quadruped motion; no semantic reuse |
| `support_attack` | Alias to `attack` | Dedicated secondary bite/claw or flanking-support motion; no semantic reuse |
| `retreat` | Present file; lineage unverifiable | Dedicated withdrawal locomotion; looping and in place |
| `training` | Alias to `idle` | Dedicated alert drill, stalking practice, or pounce-practice motion; no semantic reuse |
| `death` | Present file; lineage unverifiable | Dedicated articulated collapse, impact, and settling; non-looping and in place |

None of the eight roles is accepted by this pass. Existing bytes are preserved only as runtime evidence and may not be relabelled as genuine provider actions.

## Scale and vanilla precedent

- Installed vanilla mesh: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`, SHA-256 `F00FBADFDACDD1046F7119E62E2C47D644EA7A92D0F686B71D230BC843AEF8BA`.
- Installed vanilla entity file: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset`, `infantry_rifle_entity`, SHA-256 `6AB4BE22BC0757C93F8132F7E247910592A5D8595EAF431D33F23DF03F32AA2D`.
- Vanilla measured source height: `7.3518242835`.
- Vanilla entity scale: `0.8` exactly once.
- Vanilla effective runtime height: `5.8814594268`.
- Required forward/up axes: `-Y` / `+Z`.
- Retained rat working-height record: `7.3518247604`.
- Retained rat entity scale: `1.35` exactly once.
- Retained rat effective runtime height: `9.9249627827`, approximately `1.6875x` the vanilla effective height.
- Ground/root policy: creature root at ground origin; every action in place.

The absent source root prevents recovery of the original full X/Y/Z provider dimensions, conversion factor, rig map report, weight report, and parsed exported-runtime AABB. Those values must be remeasured through the locked adapter before any regenerated package can pass the creature crosswalk gate.

## Verified dependency and route evidence

- `MESHY_API_KEY`: present and nonblank; the value was never printed or stored.
- `@meshy-ai/meshy-mcp-server` `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`.
- Meshy compatibility revision: `meshy-7-v4`; verified image identifier: exact `meshy-7` only.
- `@modelcontextprotocol/sdk` `1.29.0`, git head `e12cbd7078db388152f6e839abdbe09ba01f3f32`.
- Blender `5.1.2`, build `ec6e62d40fa9`.
- Repository adapter: `chaosx_blender_hoi4` `1.7.0`.
- `io_pdx_mesh` `0.91.0`; locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Dependency-lock SHA-256: `B5D0D00099F33BDB5C896760A333EFE0B1FED4C6B1287842995904B7BB821C5C`.
- Meshy-schema-lock SHA-256: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- Adapter-config SHA-256: `0F4A0E916FF37E1C91EA142D6DC3554A13ED98BFCC0687BC85502C2094F66C23`.
- Environment verification report: `.tools/3d_pipeline/reports/environment_report.json`, hard gate `passed`, Meshy live route deliberately not probed while the shared lane was occupied.

## Capability blocker

The locked `meshy_animate` schema requires `rig_task_id` and `action_id`. Meshy's official Rigging API documentation states that the route supports standard humanoid bipeds, explicitly lists non-humanoid assets as unsuitable, and returns pose-estimation failure for non-humanoid input. The official animation library exposes humanoid actions and no rat, animal, quadruped, or crawl family.

The retained rat uses the custom 17-bone creature rig family (`root`, `body`, `neck`, `head`, `trunk_01`, `trunk_02`, `tail`, four upper/lower limb pairs, `howdah`, and `rider`). The locked `chaosx_blender_hoi4_import_animation_action` operation accepts a provider source only when every driven provider bone name already exists on the target rig. It has no semantic humanoid-to-quadruped map. The current allowlisted adapter therefore cannot transfer a Meshy humanoid action onto the rat rig, while routing the rat through a humanoid armature would violate the nonhumanoid identity and rig gates.

Official route references inspected:

- `https://docs.meshy.ai/en/api/rigging`
- `https://docs.meshy.ai/en/api/animation`
- `https://docs.meshy.ai/en/api/animation-library`

Consequently, spending on a new Meshy 7 rat geometry would not unlock the required animation route. No generation, rigging, or animation credits were spent in this pass.

## Credits

- Historical claimed geometry generation: `30` credits for task `019fd39c-3f8e-7f96-bd04-214ccbb7d64f`; retained handoff claim only, not independently reconciled because the production ledger is missing.
- This recovery pass: estimated `0`, consumed `0`.
- No balance check was made because the creature job lacks a complete recovered crosswalk and the shared provider lane was occupied.

## Acceptable continuation paths

1. Parent explicitly expands scope for a repository-owned, checksum-locked semantic humanoid-action-to-quadruped retarget operation, followed by fresh dependency-lock/schema verification. This is outside this worker's current no-adapter-patch scope and still needs role-specific visual acceptance proving substantive rat motion survived retargeting.
2. Parent/user explicitly approves a professional quadruped animation source with clear licensing and eight dedicated roles, then the locked adapter receives a compatible, allowlisted import/retarget route. This would satisfy the general professional-source rule but not the current parent request for `meshy_animate` specifically.
3. Meshy adds and the repository verifies an official nonhumanoid rig/action route. The worker may then regenerate with Meshy 7 and produce all eight role-specific actions.

A bipedal rat redesign, local creature-action authoring, procedural motion, transform-only motion, static poses, aliasing, or semantic reuse is not an acceptable continuation.

## Files changed

- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-22_event020_plague_rat_animation_recovery.md`
- `.tools/3d_pipeline/reports/environment_report.json` was regenerated by the repository verifier's default non-provider check. It records the current `1.7.0` adapter and passed local dependency hashes but intentionally has `meshy.route = not_probed`; the parent should refresh it with the intended live probe after the reserved Alien Infantry lane is released. It was not reverted because the shared toolchain worktree was already dirty and a blanket restoration could discard concurrent work.

## Meaningful validation and skipped validation

Performed:

- verified the missing job root against the filesystem, `HEAD`, and local path history;
- enumerated the installed mesh, five installed `.anim` files, exact hashes, and current state aliases;
- verified the current dependency lock, schema lock, adapter configuration, installed Blender build, and `io_pdx_mesh` archive checksum;
- compared the official Meshy rig/animation contracts with the locked adapter's exact bone-channel acceptance behavior;
- recovered the numeric vertical scale relationship from the installed entity and named vanilla precedent.

Skipped because blocked or reserved:

- old provider task status/download recovery, live schema probes, balance check, and all paid calls: shared lane reserved by Alien Infantry;
- Blender inspection, multi-view previews, rig/weight audit, source checkpoints, action import/retarget, PDX export, and actual-byte reimport: no acceptable source-action route and shared lane reserved;
- full X/Y/Z creature crosswalk and exported-runtime AABB: original source/checkpoint evidence is absent;
- runtime synchronization and entity/GFX changes: explicitly parent-owned and outside scope;
- in-game consumer validation: parent/user-owned.

## Remaining parent work

- Decide whether to authorize a locked adapter capability expansion, approve a professional quadruped source instead of the requested Meshy route, or retain this package as blocked until Meshy supports nonhumanoid animation.
- Do not wire dedicated `defend`, `support_attack`, or `training` identifiers until eight accepted source actions, exports, and actual-byte reimports exist.
- Preserve one shared rat identity for all six subtypes and both rat countries.

No simplification or fallback was used.
