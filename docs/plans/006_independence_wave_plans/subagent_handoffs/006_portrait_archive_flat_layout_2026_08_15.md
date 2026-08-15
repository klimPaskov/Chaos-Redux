# Event 006 portrait archive layout handoff

Status: COMPLETE for the requested archive layout. This is an asset-organization receipt only; it does not promote any portrait to a runtime consumer, central package admission, or Join.

## Canonical paths

- Original source files belong directly under `docs/assets/portraits/006_independence_wave/`.
- Processed evidence and outputs belong under the single child directory `docs/assets/portraits/006_independence_wave/processed/`.
- No other child directory is permitted under the Event 006 portrait parent.

## Current layout receipt

- Direct parent files: 53.
- Direct child directories: `processed` only.
- Nested directories below `processed`: 0.
- Files below `processed`: 169.
- Files whose names contain `156x210`: 0.
- Duplicate SHA-256 hashes among direct parent source files: 0.

The parent is therefore the ComfyUI source shelf, while `processed/` is the only location for crops, review images, manifests, provenance records, and other derived evidence. No 156x210 derivative is retained in this archive.

## Workflow boundary

ComfyUI source selection must read original masters from the parent directory and must not select a file from `processed/` as an immutable source master. Processed outputs remain review/evidence material until the owning portrait handoff independently clears identity, rights, framing, role, consumer ownership, and runtime wiring. This organization change does not authorize DDS, GFX, character, central-admission, or Join edits.

## Validation

The layout was checked from the repository root after the move: parent file count, direct-child directory set, recursive child-directory count, processed-file count, filename scan for `156x210`, and direct-parent SHA-256 duplicate scan all produced the receipt above.
