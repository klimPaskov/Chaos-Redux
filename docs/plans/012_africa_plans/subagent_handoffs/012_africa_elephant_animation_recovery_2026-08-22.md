# Event 012 elephant animation recovery handoff — 2026-08-22

> Superseded by the explicit vanilla-elephantry reuse decision dated 2026-08-27: the blocked custom animation recovery below is historical evidence only. `chaosx_elephant` uses vanilla `elephantry`, and retention or deletion of the approximately 340 MB evidence package is an owner decision outside this documentation-only pass.

Status: `superseded_by_vanilla_elephantry_reuse` (historical blocker record; originally blocked before provider spend).

## Outcome

The missing elephant evidence root was recreated as a deterministic blocked intake at `docs/assets/012_africa/models_3d/elephant_shared_base/`. No provider, Blender mutation, runtime wiring, or commit was performed. Credits consumed: `0`; the observed Meshy balance was `894`.

The existing runtime mesh retains its historical SHA-256 `6C3B53731646C3F57F56D26AFE5E4F7215C3E034469AD04179A3F0A70F4D5988`, but the six runtime actions remain unverifiable. Their hashes and exact status are in the recreated manifest.

## Confirmed blocker

The version-pinned MCP route exposes `meshy_animate(rig_task_id, action_id)`. Official Meshy API documentation states that its programmatic rigging endpoint is for standard humanoid bipeds and explicitly lists non-humanoid assets as unsuitable. The approved local adapter can prepare a 17-bone elephant skeleton, but the locked provider schema cannot upload that custom rig or turn it into the required Meshy `rig_task_id`.

Therefore a faithful elephant cannot currently receive policy-compliant `meshy_animate` motion through the approved programmatic route. Meshy's separate interactive web app advertises quadruped rigging, but it is not the approved MCP route and was not used. Spending Meshy 7 geometry credits would not solve this action-source blocker.

## Required action coverage

Eleven distinct roles remain blocked: standard `idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death`, plus bespoke `deploy`, `supply_load`, and `impact`. Existing aliases and the old six `.anim` files do not satisfy the source gate. Final actions require real limb and trunk articulation; attack needs preparation/contact/recoil/recovery evidence and death needs a true quadruped collapse/impact/settling sequence.

## Dependency evidence

The lock selects Meshy MCP `0.4.0`, compatibility revision `meshy-7-v4`, exact model `meshy-7`, adapter `1.7.0`, Blender `5.1.2` build `ec6e62d40fa9`, and `io_pdx_mesh 0.91.0`. Adapter hashes matched the dependency lock and the Blender bridge was listening on `127.0.0.1:9876`. Exact checksums and schema facts are recorded in `evidence/dependency_and_route_preflight.md`.

## Needed decision

Choose one route before resuming paid work:

1. Approve and lock a Meshy MCP/API capability that demonstrably returns a quadruped elephant `rig_task_id` and supports distinct elephant-suitable actions.
2. Explicitly approve a named professional quadruped/elephant animation source with defensible licensing for all eleven roles.

Manual, procedural, transform-only, static-pose, or semantic-alias Blender actions remain forbidden. No simplification or fallback was used.

## Files created

- `docs/assets/012_africa/models_3d/elephant_shared_base/job.yaml`
- `docs/assets/012_africa/models_3d/elephant_shared_base/history.jsonl`
- `docs/assets/012_africa/models_3d/elephant_shared_base/manifest.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/refs/source/source_search.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/dependency_and_route_preflight.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/action_source_feasibility.md`
- `docs/assets/012_africa/models_3d/elephant_shared_base/runtime/handoff.md`
- this handoff

## Skipped validation

Geometry inspection, Blender source/checkpoint creation, rigging, weights, action import/retarget/grounding, PDX export/reimport, and phase previews were skipped because no approved elephant action-source route exists. Temporary shared-lane occupancy was respected and is not the blocker. Runtime files were not changed.
