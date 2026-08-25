# Event 014 Model Provider Recheck

Status date: 2026-08-25 parent read-only Meshy recheck

## Scope

This recheck queries only existing Event 014 Meshy task records. It does not spend credits, download new artifacts, edit runtime model files, or treat a provider preview as a validated HOI4 package.

## Live account and task evidence

The live Meshy balance was `10` credits. No paid generation, rigging, remesh, conversion, or animation call was made during this recheck.

| Package | Existing task queried | Provider result | Acceptance consequence |
| --- | --- | --- | --- |
| `cannibal_scavenger_warband` | `01a034b1-aeea-75fc-a862-6442efb39222` | `SUCCEEDED`, `image-to-3d`, 100%, 30 credits consumed; GLB/FBX artifacts are available from the provider record | Geometry is still a candidate. The current job remains at the adapter 1.10.4 geometry gate and has no accepted rig/action/reimport package, so it remains `needs_user_review`/blocked for runtime promotion. |
| `cannibal_island_reavers` | `01a034bb-7129-716b-bc17-177ca0eb9a1a` | `SUCCEEDED`, 100%, 30 credits consumed; GLB/FBX artifacts are available from the provider record | This does not satisfy the approved v8 acceptance gate or the required rig and eight dedicated actions. The package remains blocked and the earlier HTTP 402 recovery record remains evidence for the superseded attempt. |
| `cannibal_network_cadre` | `01a0295c-6b81-72c2-96bf-b4fc777dcabe` and `01a02992-4c18-781f-b15e-1fec680e83bd` | Both task IDs returned `not found on any endpoint` | No current provider lease or action artifact can be verified. Accepted geometry remains evidence only; the package remains blocked pending a new verified provider action route. |
| `cannibal_bone_riders` | `01a03404-f74d-7d5b-876d-5f426afe11f6` | Task ID returned `not found on any endpoint` | The manifest's historical geometry checkpoint is not a current compound horse/rider rig or action package. The dedicated nonhumanoid rig route remains blocked; no runtime promotion is allowed. |

The queried success responses expose provider model artifacts, but none provides the required eight semantically distinct skeletal roles with export and reimport evidence. The status check therefore does not change any package state.

## Credit and animation gate

The required roles are `idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death`. Eight `meshy_animate` operations alone are estimated at 24 credits, before a missing rig, geometry recovery, or adapter work. With 10 credits available, a partial paid tranche would leave the package incomplete and would not authorize a static, transform-only, aliased, or Blender-authored substitute. The 3D pipeline requires provider-sourced substantive motion, action-specific QA, PDX export/reimport evidence, and a parent-owned runtime consumer before promotion.

## Current disposition

The five previously installed packages remain the only Event 014 model packages with runtime mesh, eight action exports, material DDS, entity/GFX, and sound coverage. The four packages above remain open:

- `cannibal_scavenger_warband`: current geometry candidate awaiting adapter and parent review.
- `cannibal_island_reavers`: current geometry candidate without accepted rig/action coverage; superseded 402 recovery evidence is retained.
- `cannibal_network_cadre`: provider action lease unavailable and historical task IDs are no longer queryable.
- `cannibal_bone_riders`: compound horse/rider anatomy has no accepted Meshy rig/action route.

No runtime files, model aliases, static fallbacks, or gameplay definitions were changed by this recheck. Reopen the packages only after the live route has sufficient balance or an explicitly approved, licensed professional animation fallback has passed the documented Meshy incapability gate.

