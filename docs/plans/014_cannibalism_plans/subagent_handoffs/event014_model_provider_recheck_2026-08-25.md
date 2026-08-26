# Event 014 Model Provider Recheck

Status date: 2026-08-25 historical read-only Meshy recheck; superseded for Island Reavers by the paid v11 continuation handoff and superseded for Bone Riders and Network Cadre by the 2026-08-26 vanilla-visual reuse decision.

## Scope

This recheck queries only the then-existing Event 014 Meshy task records. Its 10-credit balance and geometry-only disposition are historical evidence, not the current Island Reavers or Scavenger Warband state. The later paid continuations are recorded in `event014_island_reavers_v11_runtime_handoff.md` and `event014_scavenger_warband_v2_runtime_handoff.md`; they supersede those package rows below. The Bone Riders and Network Cadre rows are also historical only because the approved current scope reuses vanilla `cavalry` and `infantry` sprites without custom model gates.

## Live account and task evidence

The live Meshy balance was `10` credits. No paid generation, rigging, remesh, conversion, or animation call was made during this recheck.

| Package | Existing task queried | Provider result | Acceptance consequence |
| --- | --- | --- | --- |
| `cannibal_scavenger_warband` | `01a034b1-aeea-75fc-a862-6442efb39222` | Historical geometry-only query; the current v2 lineage uses the later Meshy 7 image-to-3D, remesh, rig, and provider-action records | Superseded by the source-approved v2 export/reimport/runtime handoff in `event014_scavenger_warband_v2_runtime_handoff.md`. |
| `cannibal_island_reavers` | `01a034bb-7129-716b-bc17-177ca0eb9a1a` | `SUCCEEDED`, 100%, 30 credits consumed; GLB/FBX artifacts were available from the provider record | Historical geometry-only disposition. Superseded by remesh `01a03967-eaff-72d3-a8a9-2ec3efa29a15`, rig `01a0396c-09fc-7026-b5b3-1210dbfa2f1c`, eight provider action receipts, export/reimport proofs, and engine wiring in `event014_island_reavers_v11_runtime_handoff.md`. |
| `cannibal_network_cadre` | `01a0295c-6b81-72c2-96bf-b4fc777dcabe` and `01a02992-4c18-781f-b15e-1fec680e83bd` | Both task IDs returned `not found on any endpoint` | No current provider lease or action artifact can be verified. Accepted geometry remains evidence only; the package remains blocked pending a new verified provider action route. |
| `cannibal_bone_riders` | `01a03404-f74d-7d5b-876d-5f426afe11f6` | Task ID returned `not found on any endpoint` | The manifest's historical geometry checkpoint is not a current compound horse/rider rig or action package. The dedicated nonhumanoid rig route remains blocked; no runtime promotion is allowed. |

At the time of this read-only recheck, the queried success responses exposed provider model artifacts but none provided the required eight semantically distinct skeletal roles with export and reimport evidence. The later Island Reavers continuation closed that package-specific gate; this historical query does not replace its evidence.

## Credit and animation gate

The required roles are `idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death`. At the time of the recheck, eight `meshy_animate` operations alone were estimated at 24 credits with 10 credits available. The later v11 continuation used the replenished balance and recorded the paid tranche; it still required provider-sourced substantive motion, action-specific QA, PDX export/reimport evidence, and a parent-owned runtime consumer before promotion.

## Current disposition

The five previously installed packages were the only Event 014 model packages with runtime mesh, eight action exports, material DDS, entity/GFX, and sound coverage at the time of this recheck. The current disposition is:

- `cannibal_scavenger_warband`: v2 provider/export/reimport/runtime package accepted; see `event014_scavenger_warband_v2_runtime_handoff.md`.
- `cannibal_island_reavers`: v11 provider/remesh/rig/action/export/reimport/runtime package accepted; see `event014_island_reavers_v11_runtime_handoff.md`.
- `cannibal_network_cadre`: provider action lease unavailable and historical task IDs are no longer queryable.
- `cannibal_bone_riders`: compound horse/rider anatomy has no accepted Meshy rig/action route.

This historical recheck did not change runtime files, model aliases, static fallbacks, or gameplay definitions. The Island continuation did add its own runtime handoff; no professional-animation fallback or local motion substitute was used.
