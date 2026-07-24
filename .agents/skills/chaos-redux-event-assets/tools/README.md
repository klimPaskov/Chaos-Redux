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

`advisor_icon_processing.py leader` remains the processor's full-size `156x210` export mode for both country leaders and commanders; the positional mode name does not classify the character as a political leader. The full-size role family defaults to `leader` for backward compatibility.

Commanders must pass `--role-family commander` on the full-size command. That selector uses the canonical `assets/vanilla_reference/portraits/commanders/` directory and the deterministic land-command references `eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png`. Country leaders retain the canonical leader directory and `den_thorvald_stauning.png` / `fin_carl_mannerheim.png` defaults. A custom `--reference-dir` must still contain the exact selected filenames and remain inside the repository.

The review sheet's first panel is labelled `processor input crop`; it is the crop of the supplied processed source or ImageGen result, not the immutable archival crop. Use the role-family references for style review only. An independent auditor must separately compare the archival master, explicit archival crop, raw ImageGen result, processed candidate, and role-specific references; the processor sheet cannot replace provenance evidence or the independent likeness/style/provenance audit.

The commander boundary is explicit in the full-size invocation:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py leader `
	<processed_source_or_imagegen_result.png> <candidate.png> --role-family commander `
	--source-kind real --crop <left> <top> <right> <bottom> --review-sheet <review.png>
```

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
