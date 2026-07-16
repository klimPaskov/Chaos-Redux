# Chaos Redux Event-Asset Tools

These are the canonical reusable tools for the `chaos-redux-event-assets` skill. Call them from the repository root. Do not restore or document duplicate working copies under `.tools/`; active callers must reference these skill-local paths so the implementation and the skill contract cannot drift apart.

## `advisor_icon_processing.py`

Deterministically finishes approved portrait masters for HOI4 leader portraits or native `65x67` advisor dossier icons. Advisor mode requires:

- an explicit source-pixel crop and face box
- a retained full-resolution ImageGen frame source and its alpha overlay
- a retained full-resolution ImageGen paper source and its alpha overlay
- shadowless, unrotated generated overlays; the processor owns the calibrated angle and alpha-derived shadows
- all six canonical vanilla advisor references under `../assets/vanilla_reference/portraits/advisors/`
- the self-contained `../assets/advisor_dossier_overlays/advisor_dossier_overlay_manifest.json`, which pins the approved overlay and exact style-reference hashes without depending on an event package or user-specific generated-image store

The tool only crops, grades, resizes, angles, derives shadows from authored alpha, composites, validates, writes metadata, and creates review sheets. It never draws visible dossier artwork or provides paperless/procedural fallbacks. Advisor output is always `65x67` with transparent corners and must pass face, palette, window, overlap, alpha-envelope, Jaccard, and row/column occupancy gates before DDS conversion.

Run `python -B .agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py --help` for the CLI. The complete invocation contract is in `../SKILL.md`, section 21.1.

## `convert_to_dds.py`

Converts an approved PNG to the legacy one-level uncompressed BGRA DDS layout used by the relevant vanilla HOI4 UI assets.

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py `
	--input <approved.png> --output <runtime.dds> `
	--width <pixels> --height <pixels>
```

For advisor dossiers, pass `--width 65 --height 67`, then decode the DDS and prove pixel equality with the approved PNG. Other asset families must follow their own cataloged dimensions and compression precedent.

## `process_report_event_image.py`

Processes report-event source art according to the report-event workflow documented in the skill. It is not a portrait, flag, icon, or generic-image fallback.

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py `
	<input.png> <processed_report_event.png>
```
