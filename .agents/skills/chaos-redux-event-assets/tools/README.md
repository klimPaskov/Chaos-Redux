# Chaos Redux Event-Asset Tools

These are the active reusable tools for the `chaos-redux-event-assets` skill.
Call them from the mod root. Canonical engine-surface reference lookups use:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference`

For leader/commander style review, also inspect the user-requested male-only
quick-reference pack at
`.agents/skills/chaos-redux-event-assets/assets/leader_portraits/`. Its files
are review-only copies and are never processor or runtime inputs. Advisor dossier
cards use the separate canonical references under
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/`.

There is no bundled full-size portrait processor. After the immutable crop, create
the deterministic `156x210` country-leader, commander, operative, or named-officeholder
candidate with a reproducible task-specific/manual image workflow. Inspect the
canonical role family (`leaders/`, `commanders/`, or `operatives/`) plus the
male-only quick-reference pack where applicable. Retain the processed source or
ImageGen result, candidate PNG, exact dimensions, crop metadata, hashes, role-specific
comparison sheet, and independent likeness/style/provenance review. Do not hand off
a raw, filtered, or merely resized photograph as runtime art.

Use the canonical role-specific references as style-family controls only. An
independent auditor must compare the archival master, explicit archival crop, raw
ImageGen result, processed candidate, and role-specific references separately.

## `extract_portrait_source_crop.py`

This is the only accepted immutable crop stage for a real-person archival photograph. It decodes the photographic master and crops it with Pillow, preserves the decoded source mode in a lossless PNG, reopens that PNG, and proves exact decoded-pixel equality against the same master rectangle in RGBA form before committing the PNG and JSON evidence together. It never resizes, enhances, recolours, retouches, or replaces an existing artifact without `--force`. Illustrations and generated reconstructions cannot be used as real-person identity masters.

Run it before ImageGen with the measured boundary in decoded master pixels:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py `
	<archival_master.jpg> <archival_crop.png> `
	--crop <left> <top> <right> <bottom> `
	--metadata <archival_crop.json>
```

Keep the PNG and JSON together. The JSON records the Pillow/tool versions and hash, master/output hashes and dimensions, decode modes, crop rectangle, equality hashes/result, and a normalized command. `ffmpeg` or ImageMagick crops are not immutable source crops unless an independent check proves exact equality of their decoded output pixels against the same decoded master rectangle and retains equivalent evidence; when that proof is unavailable, reject the crop and return to this utility.

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

Advisor, theorist, military-high-command, officer-corps, and army-small portraits
are a separate, explicitly authorized asset family. Inspect the canonical native
`65x67` references under
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/`
and use them as style precedents only. Do not infer this family from a character or
small-portrait consumer when the accepted requirement does not request it.

There is no bundled dossier compositor or reusable card-art package. Prepare each native `65x67`
PNG with a deterministic, task-specific/manual image workflow. Retain source and
processed PNGs, exact dimensions, crop/composition notes, hashes, provenance,
comparison sheet, stable sprite name, and runtime path in distinct repo-contained
artifacts. For grounded real people, complete the shared sourced identity gate
through an independently approved `156x210` candidate first; fictional high-chaos
or impossible/supernatural subjects may use an approved generated master. Never
directly resize a full portrait into the card, draw replacement card art from
primitive geometry, or advertise a missing shared processor.

Review the candidate against the canonical advisor/high-command references at native
size and at `4x` nearest-neighbour size. Check face readability, frame silhouette and
palette, paper geometry and opacity where present, transparent corners, texture
continuity, and holes or fringe. The producer may not approve the candidate. Convert
only an independently approved PNG with `convert_to_dds.py --width 65 --height 67`
and wire the stable sprite in the appropriate `.gfx` file.

## `process_report_event_image.py`

Processes report-event source art according to the report-event workflow
documented in the skill. It is not a portrait, flag, icon, or generic-image
fallback.

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py `
	<input.png> <processed_report_event.png>
```
