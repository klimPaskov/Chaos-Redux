# Chaos Redux Event-Asset Tools

These are the canonical reusable tools for the `chaos-redux-event-assets` skill. Call them from the repository root. Do not restore or document duplicate working copies under `.tools/`; active callers must reference these skill-local paths so the implementation and the skill contract cannot drift apart.

## `advisor_icon_processing.py`

Processor/render v5.0 deterministically finishes approved portrait masters for HOI4 leader portraits or exact native `65x67` advisor dossier icons. Advisor mode requires:

- an explicit source-pixel crop and face box
- a repo-contained schema-1 portrait-provenance manifest passed with `--portrait-provenance-manifest`; the reusable 16-source package keeps all 16 approved records together, while each run must match exactly one record by source path
- a retained full-resolution ImageGen frame source and its alpha overlay
- a retained full-resolution ImageGen paper source and its alpha overlay
- shadowless, unrotated ImageGen frame and paper sources; the paper must be opaque, textured, and free of holes or fringe
- overlays derived from those retained ImageGen sources by alpha extraction/despill only, with no locally altered or primitive-drawn visible RGB
- all six canonical vanilla advisor references under `../assets/vanilla_reference/portraits/advisors/`
- the self-contained provenance-schema-4 `../assets/advisor_dossier_overlays/advisor_dossier_overlay_manifest.json`, which pins ImageGen handles, role records, prompts, generation inputs, source/overlay paths and hashes, alpha-extraction provenance, and exact style-reference hashes without depending on an event package or user-specific generated-image store

The portrait manifest record pins source kind/hash/dimensions, exact-source-copy status, approved crop/face box, prompt section and hash, generation mode and inputs, and ImageGen or archival provenance. A 16-record package is provenance for that batch, not a hard-coded processor size; never bypass the manifest by processing an unpinned individual source.

The tool only crops, grades, resizes, angles, derives soft RGB shadows from authored alpha, composites, validates, writes metadata, and creates review sheets. It never draws visible dossier artwork or provides paperless/procedural fallbacks. Its v5 native composition pins the frame to `40x58` at `(1,1)` with a `5` degree angle and the paper to `25x30` at `(29,26)` with a `-4.25` degree angle. It validates frame/paper geometry and palette, paper opacity, face placement, portrait window, overlap, alpha coverage, Jaccard, row/column occupancy, and visible-RGB support.

The frozen execution contract is Python `3.9.12`, Pillow `11.1.0`, processor SHA-256 `e248979f21784c016e69c5458b9925c32177d6af29f2cca1a82bfaaffbe1f23c`, and advisor render-configuration SHA-256 `e9f8d54d1ea7fc8845bf22675c09686acc7196556a56f96f5a1b46268b134637`. The content-based seed also pins decoded portrait RGBA, crop, face box, source kind, mode/render version, overlay hashes, both manifest hashes, configuration hash, runtime, and processor hash; paths and filenames are not seed inputs.

V5 uses a two-stage identity-preservation search: an authored-edge-preserving unsmoothed stage before a face-protected background-smoothing last resort. Every retained candidate passes background structure checks and two face-identity gates: candidate versus its post-grade baseline and candidate versus the mapped original source. It must also land inside nine exact frozen native-style bands with at least `0.03` normalized interior margin: `top_frame_variation`, `left_rail_variation`, `left_rail_mean`, `left_rail_std`, `paper_mean`, `paper_std`, `paper_samples`, `portrait_mean`, and `bottom_area_variation`. These are mechanical family gates, not one-to-one visual approval.

At runtime, v5 derives and verifies both six-reference families. The rounded per-pixel mean alpha envelope must hash to `5d33afdd1adc0349e33b52bb141ddd1449107fd34727d19fcc45bcd7809d2993`; the aggregate paper-family record must hash to `c751cbe5f1178c8b894c56a4cebe01bb4dae88ae859b7238c2c68f39a6224dbc`. Vanilla alpha supplies opacity only. Visible RGB may come only from the approved portrait, ImageGen frame/paper, permitted authored-alpha-derived shadows, and the faint black low-alpha fringe backing. The support proof must report zero unsupported visible, substantive, and high-alpha pixels.

Advisor output is always an exact `65x67` candidate with transparent corners. Its paper support must remain visibly opaque and textured, without transparent holes, chroma fringe, white matte, or fake translucency. The generated review sheet must show the candidate and all six references at native size and `4x` nearest-neighbour size.

Candidate PNG, review PNG, and metadata JSON must use distinct repo-contained paths and may not alias any immutable source, manifest, prompt, generation input, keyer, processor, overlay, or vanilla reference. The tool verifies exact PNG decode equality and metadata integrity before transactionally committing all three artifacts with rollback; existing targets require explicit `--force`.

The processor deliberately writes `status: candidate_requires_visual_approval`. It is an automated validator and must never self-stamp visual approval. Before DDS conversion, a human, parent agent, or separately spawned reviewer who is not the producing agent must approve the exact candidate hash in a separate manifest-linked record. That record must identify producer and reviewer, link and hash the candidate and review sheet, record native and `4x` all-six-reference verdicts, and include the approval decision and notes.

Run `python -B .agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py --help` for the CLI. The complete invocation contract is in `../SKILL.md`, section 21.1.

## `convert_to_dds.py`

Converts an approved PNG to the legacy one-level uncompressed BGRA DDS layout used by the relevant vanilla HOI4 UI assets.

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py `
	--input <approved.png> --output <runtime.dds> `
	--width <pixels> --height <pixels>
```

This skill-local path is canonical; `.tools/convert_to_dds.py` is obsolete and must not be restored or used by active workflows. For advisor dossiers, run this converter only after separate visual approval, pass `--width 65 --height 67`, then decode the DDS and prove exact RGBA pixel equality with the approved PNG. Other asset families must follow their own cataloged dimensions and compression precedent.

## `process_report_event_image.py`

Processes report-event source art according to the report-event workflow documented in the skill. It is not a portrait, flag, icon, or generic-image fallback.

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py `
	<input.png> <processed_report_event.png>
```
