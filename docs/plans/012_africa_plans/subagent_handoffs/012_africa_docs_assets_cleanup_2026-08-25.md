# Event 012 Africa `docs/assets` storage cleanup — 2026-08-25

## Scope

This cleanup is limited to `docs/assets/012_africa/`. No other event workspace, durable portrait archive, runtime asset folder, gameplay file, or model registry was changed.

## Removed disposable intermediates

- 76 Blender autosave files (`*.blend1`) under the Africa workspace, approximately 3,026.0 MiB.
- 193 Blender snapshots under Africa `provider/rejected/` folders, approximately 7,558.7 MiB. These were rejected-lineage working snapshots; their provider task IDs, hashes, rejection reasons, and QA evidence remain in the job ledgers and handoffs.

The measured reclaim target was approximately 10.3 GiB. The cleanup does not delete accepted provider GLB/FBX files, approved reference inputs, current non-rejected Blender checkpoints, `.mesh` or `.anim` candidates, audio sources or derivatives, manifests, provenance, history, reports, or handoffs.

## Retention boundary

The Africa workspaces remain incomplete or blocked, so the event-scoped evidence roots are retained. This is an intermediate storage trim, not the final event-workspace deletion required after runtime completion.

## Validation

After deletion, remeasure `docs/assets/012_africa`, confirm no `*.blend1` remains there, confirm no Blender file remains below an Africa `provider/rejected/` path, and verify the retained reference, manifest, history, audio, provider-download, and handoff paths still exist.
