# Chaos Redux Event-Asset Tools

These are the active reusable tools for the `chaos-redux-event-assets` skill.
Call them from the mod root. Canonical engine-surface reference lookups use:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference`

For leader/commander style review, inspect the canonical role-specific references.
Advisor dossier cards use the separate canonical references under
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/`.

The portrait source tool owns deterministic source-placeholder preparation. It
does not approve identity, rights, role fit, likeness, or runtime wiring. Inspect
the canonical role family (`leaders/`, `commanders/`, or `operatives/`), retain
the source/crop/processed evidence, and obtain independent identity, framing,
and provenance review before DDS or runtime promotion.

Use the canonical role-specific references as style-family controls only. An
independent auditor must compare the archival master, explicit archival crop, raw
ImageGen result, processed candidate, and role-specific references separately.

## `extract_portrait_source_crop.py`

This is the only accepted immutable crop/package stage for a grounded real-person archival photograph. Automatic mode uses the bundled official OpenCV Zoo YuNet model (`tools/models/face_detection_yunet_2026may.onnx`) to detect exactly one face, computes a portrait-aspect head-and-shoulders crop, preserves the unchanged source bytes, proves exact decoded-pixel equality with Pillow, writes a deterministic RGB `156x210` PNG, and commits JSON evidence plus a co-located provenance `.txt` contract. Zero or multiple faces, missing OpenCV `FaceDetectorYN`, missing model, unsafe crop geometry, or any write collision fails closed; provide `--model` or use manual `--crop` recovery. The detector is a framing aid, never identity approval. Illustrations and generated reconstructions cannot be used as real-person identity masters.

The vendored model is from the MIT-licensed OpenCV Zoo `face_detection_yunet` directory. Source: `https://github.com/opencv/opencv_zoo/tree/main/models/face_detection_yunet`. File SHA-256: `ebafce4e3c118d6554634be5c27ab333b4c047a9a8c3faf1d7cf93101c22f0f0` (229738 bytes); the upstream license is retained at `tools/models/LICENSE`. Keep this model with the skill; do not replace it with an unverified detector.

Automatic mode is the default when `--crop` is omitted. Run it from the mod root with the output crop path inside the durable event package (for example `docs/assets/portraits/<event_id>_<event_slug>/<subject>/`):

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py `
	<archival_master.jpg> <subject_source_crop.png>
```

For `<runtime_basename>_source_crop.png`, the command writes
`<runtime_basename>_source_crop.json`, `<runtime_basename>.txt`,
`<runtime_basename>_156x210.png`, and an unchanged
`<runtime_basename>_original.<source_suffix>`
in the same folder. Pass `--processed`, `--source-copy`, or `--provenance` only
when explicit co-located filenames are needed. The `.txt` file is a contract:
complete subject/source/attribution/license and independent-review fields before
claiming a grounded portrait is admissible. `source_placeholder` remains valid
when that mode is explicitly selected; `styled_final` and `replacement_pending`
are separate, user-requested provider branches. The agent never operates RunPod.

For a known boundary or a detector miss, retain the exact manual recovery path:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py `
	<archival_master.jpg> <archival_crop.png> `
	--crop <left> <top> <right> <bottom> `
	--metadata <archival_crop.json>
```

Manual `--crop` uses the same complete package transaction and naming defaults;
the JSON labels `mode: manual_crop_override` and does not claim a face box or
YuNet detection. The older `crop_source()` Python API remains available for
callers that intentionally need only the two historical crop/evidence files.

Keep the unchanged original, lossless crop, JSON evidence, resized PNG, and
provenance `.txt` together under `docs/assets/portraits/<event_id>_<event_slug>/`
(a subject subfolder is allowed). The JSON records tool/model versions and
hashes, source/crop/processed dimensions, face box, crop rectangle, equality
result, and normalized command. `ffmpeg` or ImageMagick crops are not immutable
source evidence unless an independent check proves exact decoded-pixel equality
against the same decoded master rectangle and retains equivalent evidence.

## `convert_to_dds.py`

Converts an approved PNG to the legacy one-level uncompressed BGRA DDS layout
used by the relevant vanilla HOI4 UI assets.

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py `
	--input <approved.png> --output <runtime.dds> `
	--width <pixels> --height <pixels>
```

The command above is the supported converter; `.tools/convert_to_dds.py` is
obsolete and must not be restored or used by active workflows. Follow the matching vanilla
catalog entry for dimensions and compression.

## Advisor and high-command dossier portraits

Advisor, theorist, military-high-command, officer-corps, and army-small portraits are a separate, explicitly authorized asset family.

Inspect the canonical native `65x67` references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/`.

Use `create_advisor_icon.py` when the accepted design calls for the shared `advisor_template.png` dossier surface.

The tool loads the complete source portrait without cropping or pre-warping it. It derives the canonical opening's center, rotated width and height, and exact angle directly from the template on every run. Canonical cards use that exact measured opening-fill plane, match the angle within `0.05` degrees, and use a `0 0` center offset. The complete portrait is resized uniformly to contain within that plane while preserving its source aspect ratio. Any residual strip is filled with a matte sampled from the source's upper corners, not with stretched or cropped portrait pixels; the contained portrait is bottom-aligned so shoulders remain at the frame base. The fitted composition is safety-clipped to the irregular opening edge and the untouched template is composited once as the top layer. Misaligned fill planes and any workflow that crops or stretches the portrait are rejected.

Run it from the mod root:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py `
	--source <approved_portrait.dds> `
	--portrait-size <width> <height> `
	--rotation <degrees> `
	--portrait-offset <right> <down> `
	--study-candidate <width> <height> <right> <down> <rotation> `
	--placement-study <placement_study.png> `
	--alignment-preview <alignment_8x.png> `
	--preview <review.png> `
	--review-preview <review_4x.png> `
	--metadata <placement_metadata.json> `
	--output <runtime.dds>
```

The native preview, nearest-neighbour `4x` review preview, per-person placement study, `8x` alignment overlay, transform metadata, and staged DDS are all required outputs. In the overlay, red is the measured opening, green is the source-derived fill plane, and yellow is the uniformly contained full portrait. The compositor will not run when any review artifact is omitted.

Negative `--portrait-offset` values move left or up.

Use `--study-candidate` to retain the exact template-derived placement as a per-person visual study. The selected transform must appear in the supplied study, so the runtime card cannot silently diverge from the reviewed placement.

The compositor rejects rotations between `-0.25` and `0.25` degrees by default because a neutral transform recreates the frame-only failure mode. `--allow-zero-rotation` exists only for a documented, independently reviewed alternative template whose measured opening is actually unrotated; it cannot bypass canonical-template alignment.

Use a separate placement study for every person. The measured fill-plane size, center, and rotation belong to the shared frame and must match across canonical cards, while the source-specific visual review confirms that the yellow full-portrait bounds remain readable and preserve the source aspect ratio. `--metadata` records the measured opening geometry, source and template hashes, contained content size, source-derived padding, crop/stretch booleans, selected placement and alignment error, study candidate, and output hashes.

Keep the complete head and shoulders readable, prevent portrait pixels from appearing outside the frame, keep the face clear of the paper, and retain the exact template as the final top layer.

Record the source hash, template hash, complete-source resize, selected dimensions, center, offset, rotation, sepia strength, candidate grids, independent review, processed PNG hash, and runtime DDS hash.

For grounded real people, complete the shared sourced identity gate through an independently approved `156x210` candidate first; fictional high-chaos or impossible or supernatural subjects may use an approved generated master.

Review the candidate at native size and at `4x` nearest-neighbour size against the canonical advisor and high-command family.

The producer may not approve the candidate.

## `process_report_event_image.py`

Processes report-event source art according to the report-event workflow
documented in the skill. It is not a portrait, flag, icon, or generic-image
fallback.

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py `
	<input.png> <processed_report_event.png>
```
