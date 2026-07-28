# Event 006 portrait shelf flattening handoff — 2026-07-28

## Scope

This handoff records the user-directed correction to the Event 006 source portrait shelf. It changes evidence organization only; it does not admit a portrait, change a leader consumer, authorize a DDS, or alter the grounded source and independent-review gates.

## Current layout

The authoritative shelf is:

`docs/assets/006_independence_wave/portraits_generated_png/`

It now contains exactly 49 original-size RGB PNG repaint masters directly in that directory. It has no nested directories and no normalized 156x210 PNGs. The flat filenames and source provenance are recorded in `PRE_RESIZE_MANIFEST.md`; `README.md` and `MANIFEST.md` state the same boundary.

The former normalized shelf copies were removed from the mod workspace after the byte/hash verification, so no processed portrait remains in the user-selected shelf. Originating package workspaces remain authoritative for any needed processed-pipeline evidence; the moved temporary archive has no runtime references.

## Verification

- 49 pre-resize masters were copied byte-for-byte to the flat shelf and hash-checked before the old nested shelf copies were moved.
- Every flat shelf PNG decodes as RGB and remains larger than the 156x210 runtime target.
- The shelf has zero child directories and zero 156x210 PNGs.
- Protected BAY Rupprecht and RHI Matthes masters remain present and unchanged.
- No advisor, dossier, `_small`, or runtime consumer was added.

## Follow-up rule

Future source-derived portrait masters for this user-selected shelf must be placed directly in the same directory with a unique basename. Do not recreate `pre_resize_source_repaints/`, `source_candidates/`, `approved_or_protected/`, or `historical_withdrawn/` beneath it, and do not copy normalized PNGs into it. The event-assets skill now documents this explicit flat-shelf override.
