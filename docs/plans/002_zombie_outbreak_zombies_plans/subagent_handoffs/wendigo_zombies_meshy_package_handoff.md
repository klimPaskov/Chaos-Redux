# Wendigo Zombies Meshy package handoff

## Outcome

Status: `blocked`.

No Meshy generation, rigging, animation, balance, download, Blender, export, reimport, runtime synchronization, or runtime-wiring operation was performed.

The accepted visual identity can remain the basis of a creature model, but the required all-Meshy skeletal package cannot be produced through the locked official Meshy MCP/API route. Meshy's programmatic rigging API accepts textured standard humanoid bipeds and explicitly lists non-humanoid assets as unsuitable. The animation API requires the id of a successfully completed API rigging task. The dedicated Wendigo is nonhumanoid, digitigrade, antlered, and quadrupedal or quadrupedal-leaning, so it cannot obtain the provider rig task required by `meshy_animate` without violating the provider's documented endpoint constraints.

The Meshy web application documentation describes quadruped rigging, but the project requires the locked official MCP/API route and forbids substituting an unverified web-app or direct-REST workflow. No web-app action was attempted.

## Files created or changed

- Created this handoff only: `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/wendigo_zombies_meshy_package_handoff.md`.
- No package source, provider, Blender, texture, export, runtime, gameplay, GFX, entity, sound-definition, localisation, spreadsheet, adapter, or dependency file was changed.

## Current runtime and package state

- The live sub-unit remains on the generic zombie visual through `common/units/zombies.txt`: `wendigo_zombies` has `sprite = zombies`.
- No `chaosx_wendigo_zombies` runtime mesh, animation, GFX registration, or entity exists.
- The deterministic evidence root is `docs/assets/002_zombie_outbreak/models_3d/wendigo_zombies/`.
- The intended parent-owned runtime stem is `chaosx_wendigo_zombies` and the intended entity id is `chaosx_wendigo_zombies_entity`.
- No provider task id, response id, downloaded provider artifact, Blender checkpoint, `.mesh`, `.anim`, PDX texture, preview, or reimport receipt exists.

## Source and reference preflight

- Sole provider-input candidate: `docs/assets/002_zombie_outbreak/models_3d/wendigo_zombies/refs/original/meshy_input.png`.
- SHA-256: `5ECDB83B74264F0D33EFDB8C30085B31A8CF3B44C7730B588BB2B7AAEC136B60`.
- Decoded dimensions: `1122x1402`.
- Exactly one image is declared as the provider input.
- Visual identity: antlered, long-muzzled, dark shaggy winter predator with exposed ribs, elongated arms and legs, claws, and a forward stalking posture.
- Pose finding: the image is a digitigrade biped with hanging forelimbs rather than a clean four-foot quadruped stance. It can support a nonhumanoid creature brief, but it does not prove a true quadruped skeleton or four-paw contact layout.
- Alpha finding: the PNG is fully opaque. Sampled alpha minimum and maximum are both `255`, all four corner alpha values are `255`, and no transparent pixels were found. This fails the current native-transparency reference gate. The brief also explicitly requested a light-gray studio background, which conflicts with the current pipeline requirement.
- Required reference recovery: a targeted ImageGen edit must produce a genuine transparent background while preserving the accepted subject exactly, then the repaired image needs a new checksum and explicit review. If the user insists on a true quadruped body rather than the current digitigrade biped silhouette, that is a separate identity/pose revision and requires approval before replacing the accepted reference.

## Job-intake defects that block paid work

The current `job.yaml` is not executable under the current hard gates:

- `provider_model` is `meshy-6`; the locked route requires the exact identifier `meshy-7`.
- `scale_crosswalk` is a descriptive string rather than the required measured numeric crosswalk.
- The job lacks finite numeric provider/Blender target dimensions, effective runtime dimensions, units, and a conversion or fit factor.
- `creature_rig_family: quadruped` is named, but no written quadruped rig map exists.
- The generic pilot runner rejects this family with `pending_creature_rig_route`; only the specialized `winged_biped` creature continuation is enabled.
- `load_pilot_configs()` explicitly excludes `wendigo_zombies` from specialized-zombie discovery.
- The job lists only idle, move, attack, and death. The current runtime quality requirement also mandates distinct defend, support-attack, retreat, and training actions.
- The existing estimate of `47` credits reflects the obsolete four-action plan and cannot represent the eight-role requirement.
- Extra-recovery credit and paid-attempt limits are absent.

The named vanilla comparison remains the installed `western_european_infantry.mesh` and its `generic_western_european_rifle_infantry_mesh` / `infantry_rifle_entity` consumers. The measured source height is `7.351824797689915`, entity scale is `0.8`, and effective runtime height is `5.881459838151932`. This is a comparison baseline only; it does not authorize copying humanoid width, depth, skeleton, or limb proportions to the Wendigo.

## Provider route and exact technical blocker

Verified repository lock evidence:

- Dependency lock SHA-256: `B5D0D00099F33BDB5C896760A333EFE0B1FED4C6B1287842995904B7BB821C5C`.
- Meshy schema lock SHA-256: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- Blender adapter config SHA-256: `0F4A0E916FF37E1C91EA142D6DC3554A13ED98BFCC0687BC85502C2094F66C23`.
- Official package: `@meshy-ai/meshy-mcp-server` `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`.
- Compatibility SDK: `@modelcontextprotocol/sdk` `1.29.0`.
- Compatibility revision: `meshy-7-v4`.
- Verified image model: exact `meshy-7` only.
- Locked tools include `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate`.
- `meshy_rig` accepts one of `input_task_id` or `model_url`; the official API documents textured humanoid GLB/biped input and states that non-humanoid assets are unsuitable.
- `meshy_animate` requires both `rig_task_id` and `action_id`; it cannot accept a local Blender quadruped rig or a raw geometry task.

Official documentation consulted on 2026-08-22:

- Meshy Rigging API: `https://docs.meshy.ai/en/api/rigging`.
- Meshy Animation API: `https://docs.meshy.ai/en/api/animation`.
- Meshy Animation Library: `https://docs.meshy.ai/en/api/animation-library`.

Consequently, the provider route cannot create a valid quadruped rig task, and without that task it cannot create any genuine Meshy action for this model. A local `author_creature_rig` skeleton cannot be submitted to `meshy_animate`, and local `author_creature_action` output is forbidden as final motion. Generating geometry alone would not resolve the user's required animation provenance.

## Required semantic action crosswalk

Every role below remains `blocked`; no semantic aliases are permitted.

| Role | Intended motion evidence | Loop policy | Status and blocker |
| --- | --- | --- | --- |
| `idle` | Four-contact or deliberate stalking rest, breathing and head/ear/antler motion without a static pose. | Loop | Blocked: no successful supported Meshy quadruped rig can supply `rig_task_id`. |
| `move` | In-place stalking gait with a genuine limb cycle and stable ground contacts. | Loop | Blocked: same provider-rig prerequisite. |
| `attack` | Distinct crouch/aim, pounce or swipe discharge, recoil/impact, and recovery phases. | Non-loop | Blocked: same provider-rig prerequisite. |
| `defend` | Distinct braced threat posture and reactive guard motion, not `attack`. | Loop or bounded hold according to accepted source | Blocked: same provider-rig prerequisite. |
| `support_attack` | Distinct lateral or secondary lunge/harry sequence, not `attack`. | Non-loop | Blocked: same provider-rig prerequisite. |
| `retreat` | Distinct withdrawing/backward or turn-and-flee locomotion, not `move`. | Loop | Blocked: same provider-rig prerequisite. |
| `training` | Distinct predatory practice/stalk-pounce rehearsal, not `idle`. | Non-loop | Blocked: same provider-rig prerequisite. |
| `death` | Articulated collapse, impact, antler/body settling, and terminal hold. | Non-loop | Blocked: same provider-rig prerequisite. |

The locked schema records verified action ids only for `idle = 0`, `attack = 4`, and `death = 8`. The official library contains many humanoid actions but does not cure the missing quadruped API rig prerequisite, and the locked schema does not approve ids for the remaining five required roles. No action id was guessed or called.

## Credits

- Estimated credits before blocker: textured Meshy 7 geometry `30`; rig `5`; eight required animations at `3` each = `24`; planned total `59`, or `64` if a conditional `5`-credit remesh were needed. Conversion/retexture would add only their separately verified planned costs if actually required.
- Consumed credits: `0`.
- No balance check was made because no paid tranche could pass the nonhumanoid intake and provider-capability gates.

## Blender and export state

- Locked Blender: `5.1.2`, build commit `ec6e62d40fa9`.
- Locked Blender HOI4 adapter: `chaosx_blender_hoi4` `1.7.0`.
- Locked `io_pdx_mesh`: `0.91.0`, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- No Blender or adapter request was issued.
- Geometry, material, topology, rig, weight, grounding, action, export, and reimport results are absent because no accepted provider source or provider animation route exists.
- No final file paths or artifact checksums exist beyond the reference evidence listed above.

## Parent decision required

The package can proceed only after one of these conditions changes:

1. The locked official Meshy MCP/API route exposes and verifies quadruped rigging plus quadruped-compatible `meshy_animate` actions for all eight roles.
2. The user explicitly changes the requirement and approves a professional quadruped rig/action source for every role. This would no longer be an all-Meshy animation package and therefore does not satisfy the present instruction.

Do not route this creature through the humanoid rig, do not use the web application as an undocumented substitute, do not author final actions locally, and do not alias roles. Parent-owned runtime wiring must remain unchanged until a complete accepted mesh, eight distinct provider/professional actions, textures, `.mesh`/`.anim` exports, actual-byte reimport proofs, sourced sound package, bespoke counter package, and final synchronization receipts exist.

## Meaningful validation and skipped validation

Performed:

- Inspected the exact accepted reference visually and checked its dimensions, checksum, image count, and alpha behavior.
- Confirmed the live sub-unit still resolves `sprite = zombies`.
- Compared the eight required runtime states with installed vanilla `units_infantry.asset` and `infantry.gfx` precedents.
- Inspected the locked Meshy schema, dependency lock, adapter route, generic creature-runner gate, and official Meshy rigging/animation documentation.

Skipped because the provider capability gate fails and the shared lane was not entered:

- Live Meshy schema/balance probes, geometry generation, rigging, and animation.
- Provider downloads and lineage hashes.
- Blender bridge probe, scene inspection, creature segmentation, custom-rig work, texture processing, phase previews, PDX export, and actual-byte reimport.
- Runtime synchronization and in-game validation, which remain parent-owned in all cases.

## Simplifications, omissions, and blockers

No simplification or fallback was used. The model, all eight actions, PDX exports, phase previews, sound synchronization, counter completion, and runtime handoff remain incomplete and explicitly blocked by the unsupported official programmatic quadruped rig/animation route and the defective current reference/job intake described above.
