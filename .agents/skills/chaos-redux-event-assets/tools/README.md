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

## `advisor_icon_processing.py`

The reusable advisor/high-command dossier processor composes an approved portrait
master into the native `65x67` HOI4 card footprint. It is a finishing and
validation tool, not a source generator and not a card-art drawing fallback. Advisor
mode requires an explicit source crop and face box, a schema-1 portrait-provenance
manifest, the schema-4 reusable overlay manifest, both retained generated
frame/paper sources, and both alpha-processed overlays. The processor validates the
canonical six-reference style family and writes a candidate that still requires
independent visual approval.

Run it from the mod root only after the accepted requirement authorizes the advisor
family:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py advisor `
	<portrait_master.png> <advisor_icon.png> --source-kind fictional `
	--crop <left> <top> <right> <bottom> `
	--face-box <left> <top> <right> <bottom> `
	--portrait-provenance-manifest <portrait_provenance_manifest.json> `
	--advisor-overlay-manifest .agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/advisor_dossier_overlay_manifest.json `
	--advisor-frame-source .agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/v3/advisor_frame_shadowless_imagegen_source.png `
	--advisor-frame-overlay .agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/v3/advisor_frame_shadowless_overlay.png `
	--advisor-paper-source .agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/v3/advisor_paper_shadowless_imagegen_source.png `
	--advisor-paper-overlay .agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/v3/advisor_paper_shadowless_overlay.png `
	--review-sheet <advisor_review.png> `
	--metadata <advisor_icon.json>
```

Keep the generated source/overlay pairs and manifests immutable. Do not draw,
repair, recolour, paperless-compose, or directly resize a `156x210` leader or
commander into an advisor card. Convert to DDS only after the separate review
record approves the native PNG.

## `process_report_event_image.py`

Processes report-event source art according to the report-event workflow
documented in the skill. It is not a portrait, flag, icon, or generic-image
fallback.

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py `
	<input.png> <processed_report_event.png>
```
