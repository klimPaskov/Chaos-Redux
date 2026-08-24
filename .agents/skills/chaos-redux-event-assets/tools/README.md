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

## `process_achievement_icons.py`

Preserves existing Chaos Redux achievement triplets while placing the supplied state backgrounds underneath them.
Each source triplet must contain a base, `_grey`, and `_not_eligible` state, and every decoded state layer must be exactly 64x64.
The processor does not resize, crop, alpha-trim, grayscale, recolor, redraw, filter, or otherwise preprocess any source layer.
Completed output is the supplied completed background beneath the unchanged completed layer; grey output is the supplied grey background beneath the unchanged `_grey` layer; and not-eligible output is the supplied grey background beneath the unchanged `_not_eligible` layer.
Only normal alpha compositing occurs between each background and its source layer, so an opaque custom source background may hide the new bottom layer.
The existing `overlay.png` remains available as an unchanged future source-triplet overlay, but this preservation workflow never derives or rebuilds a not-eligible state from grey plus overlay.

PNG and current runtime DDS inputs are accepted.
DDS inputs are checked with the strict canonical BGRA parser first, then noncanonical, compressed, mipped, or truncated source files use Pillow's DDS decoder with `ImageFile.LOAD_TRUNCATED_IMAGES = True` enabled only during that decode.
The source fallback does not weaken the strict canonical parser used for every final output and audit.
The base filename is the achievement id unless `--achievement-id` is supplied for one selected directory triplet or explicit triplet.

The processor uses the skill-owned `assets/vanilla_reference/icons/achievements/achievement_template.png` completed background and `achievement_template_grey.png` grey/not-eligible background by default.
The two user-provided background inputs are excluded from reference counts and contact sheets; their SHA-256 values are `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA` and `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`.
The unchanged overlay is also excluded from reference counts and contact sheets.

Always keep source triplets and outputs in separate directories unless replacement is explicitly intended with `--in-place --force`.
The processor requires a complete triplet, refuses non-64x64 states, refuses a source triplet whose unchanged outer template border is detected, refuses existing output files without `--force`, and never silently derives missing state layers.
Use `--allow-templated-sources` only when intentionally reprocessing a source that the border guard identifies as already templated.

Directory triplet command with optional review PNGs:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py `
    --input <source_triplet_directory> `
    --achievement-id <achievement_id> `
    --output-dir <separate_output_directory> `
    --write-png
```

Bulk directory pass, explicit triplet, and non-writing checks:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py `
    --input <source_directory> --output-dir <separate_output_directory>
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py `
    --completed <completed.png-or-dds> `
    --grey <grey.png-or-dds> `
    --not-eligible <not-eligible.png-or-dds> `
    --achievement-id <achievement_id> `
    --output-dir <separate_output_directory>
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py `
    --input <source_directory> --output-dir <separate_output_directory> --dry-run
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py `
    --audit --input <source_directory> --output-dir <separate_output_directory>
```

Final filenames are `<achievement_id>.dds`, `<achievement_id>_grey.dds`, and `<achievement_id>_not_eligible.dds` directly under the output directory.
The processor imports `write_bgra_dds` from `convert_to_dds.py`, validates the legacy 128-byte header, 64x64 dimensions, exact 16512-byte length, BGRA masks, alpha range, and exact background-underlay composition for every final output and audit.

## Advisor and high-command dossier portraits

Advisor, theorist, military-high-command, officer-corps, and army-small portraits are a separate, explicitly authorized asset family.

Inspect the canonical native `65x67` references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/`.

Use `create_advisor_icon.py` when the accepted design calls for the shared `advisor_template.png` dossier surface.

The tool loads the complete approved source canvas without pre-cropping or pre-warping it. It measures the canonical opening center, rotated width and height, and angle directly from the template on every run. Never clip the portrait to the exact visible opening: the canonical frame has translucent antialiased inner-edge pixels, and exact-opening clipping exposes alpha seams when those pixels lack underlying portrait coverage. This supersedes the older exact-opening clipping language because the visible opening is the audit region, while the portrait must extend beneath the antialiased edge inside a verified mask.

Use one uniform aspect-preserving cover scale with no anisotropic resize or stretching. The tool expands the measured opening-fill plane by `2 * (UNDER_FRAME_BLEED_PIXELS + PORTRAIT_EDGE_GUARD_PIXELS)` before cover fitting; the centralized constants are currently `UNDER_FRAME_BLEED_PIXELS = 2` px and `PORTRAIT_EDGE_GUARD_PIXELS = 1` px. The safe bleed mask expands the opening beneath the frame and rejects any expanded pixel that reaches a fully transparent exterior template pixel. Do not copy these constants into per-person or event-specific commands. Mask the covering portrait with this verified bleed mask and keep the canonical template untouched as the final top layer.

The covering scale is `max(under_frame_fill_width / source_width, under_frame_fill_height / source_height)`, so the source aspect ratio remains unchanged. The aspect-ratio excess is recorded in `frame_clip_pixels`; it is not permission to clip the portrait to the exact visible opening. `source_pre_crop=false` means no pre-scale source crop, not that the portrait may stop at the visible opening. Misaligned fill planes, gaps, matte pixels, padded strips, and stretched portraits are rejected.

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

The native preview, nearest-neighbour `4x` review preview, per-person placement study, `8x` alignment overlay, transform metadata, and staged DDS are all required outputs. In the overlay, red is the measured opening, green is the opening-fill plane, and yellow is the uniformly scaled covering portrait; yellow may extend beyond green by the centralized bleed/guard allowance and recorded symmetric cover excess, but the runtime portrait must remain inside the verified safe bleed mask. The compositor will not run when any review artifact is omitted.

Negative `--portrait-offset` values move left or up.

Use `--study-candidate` to retain the exact template-derived placement as a per-person visual study. The selected transform must appear in the supplied study, so the runtime card cannot silently diverge from the reviewed placement.

The compositor rejects rotations between `-0.25` and `0.25` degrees by default because a neutral transform recreates the frame-only failure mode. `--allow-zero-rotation` exists only for a documented, independently reviewed alternative template whose measured opening is actually unrotated; it cannot bypass canonical-template alignment.

Use a separate placement study for every person. The measured opening-fill size, center, and rotation belong to the shared frame and must match across canonical cards, while the source-specific visual review confirms that the yellow covering-portrait bounds remain readable and preserve the source aspect ratio. `--metadata` records the measured opening geometry, source and template hashes, `opening_fill_size`, `under_frame_fill_size`, `covering_content_size`, `covering_content_center`, `frame_clip_pixels`, `under_frame_bleed_pixels`, `resampling_edge_guard_pixels`, and the explicit fit flags `source_pre_crop=false`, `frame_clip=true`, and `stretch=false`, plus selected placement and alignment error, study candidate, and output hashes. The alpha-coverage record must report `opening_alpha_gap_pixels=0`, `inner_edge_alpha_gap_pixels=0`, and `exterior_alpha_leak_pixels=0`. Review the native card and nearest-neighbour `4x` enlargement against contrasting solid backgrounds and checker backgrounds, and compare subject scale and frame integrity with the vanilla advisor/high-command references.

Keep the complete head and shoulders readable, keep the face clear of the paper, prevent portrait pixels from appearing outside the verified bleed mask, and retain the exact template as the final top layer.

Record the source hash, template hash, complete-source resize, selected dimensions, center, offset, rotation, sepia strength, candidate grids, independent review, processed PNG hash, and runtime DDS hash.

For grounded real people, complete the shared sourced identity gate through an independently approved `156x210` candidate first; fictional high-chaos or impossible or supernatural subjects may use an approved generated master.

Review the candidate at native size and at `4x` nearest-neighbour size against contrasting solid backgrounds, checker backgrounds, and the canonical advisor and high-command family.

Keep this workflow generic. Do not hard-code event-specific advisor names into the reusable skill; record those names in the event manifest or handoff instead.

The producer may not approve the candidate.

## `process_report_event_image.py`

Processes report-event source art according to the report-event workflow
documented in the skill. It is not a portrait, flag, icon, or generic-image
fallback.

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py `
	<input.png> <processed_report_event.png>
```
