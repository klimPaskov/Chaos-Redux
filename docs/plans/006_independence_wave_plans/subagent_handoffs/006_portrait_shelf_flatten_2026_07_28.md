# Event 006 portrait shelf flattening handoff — 2026-07-28

> Historical shelf-layout snapshot. Its 49-master and no-runtime-promotion
> wording describes the pre-Galimzhan-v2 state. The current shelf is the 51-file
> flat layout recorded by v30 and the parent promotion handoff, with no
> normalized or advisor/small/dossier derivatives. The promoted CHU DDS hash is
> `977e0f8d359930f75e01e380a36893ef6a8f25a5b1ce5bbd8cc3c2f3abf6b5f5`.

## Scope

This handoff records the user-directed correction to the Event 006 source portrait shelf. It changes evidence organization only; it does not admit a portrait, change a leader consumer, authorize a DDS, or alter the grounded source and independent-review gates.

## Current layout

The authoritative shelf is:

`docs/assets/006_independence_wave/portraits_generated_png/`

At this handoff's pre-Galimzhan-v2 snapshot it contained exactly 49 original-size RGB PNG repaint masters directly in that directory. It had no nested directories and no normalized 156x210 PNGs. The flat filenames and source provenance were recorded in `PRE_RESIZE_MANIFEST.md`; `README.md` and `MANIFEST.md` stated the same boundary at that time.

The former normalized shelf copies were removed from the mod workspace after the byte/hash verification, so no processed portrait remains in the user-selected shelf. Originating package workspaces remain authoritative for any needed processed-pipeline evidence; the moved temporary archive has no runtime references.

## Verification

- At the dated snapshot, 49 pre-resize masters were copied byte-for-byte to the flat shelf and hash-checked before the old nested shelf copies were moved.
- Every flat shelf PNG decodes as RGB and remains larger than the 156x210 runtime target.
- The shelf has zero child directories and zero 156x210 PNGs.
- Protected BAY Rupprecht and RHI Matthes masters remain present and unchanged.
- No advisor, dossier, `_small`, or runtime consumer was added.

## Follow-up rule

Future source-derived portrait masters for this user-selected shelf must be placed directly in the same directory with a unique basename. Do not recreate `pre_resize_source_repaints/`, `source_candidates/`, `approved_or_protected/`, or `historical_withdrawn/` beneath it, and do not copy normalized PNGs into it. The event-assets skill now documents this explicit flat-shelf override.
