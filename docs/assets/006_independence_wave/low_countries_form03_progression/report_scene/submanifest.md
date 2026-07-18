# FORM-03 charter-convention report-scene submanifest

## Scope

This submanifest owns one child deliverable under accepted Event 006 asset family ASSET-048. It is deliberately separate from the concurrently finalized FORM-03 icon package manifest.

- Asset: report_event_006_form03_charter_convention
- Event: 006 Independence Wave
- Formable family: FORM-03, Confederation of the Low Countries
- Asset type: report event image
- Status: wired
- Animation: not needed

## Requirement-to-runtime coverage

| Requirement | Accepted design source | Purpose | Source package | Runtime registration | Live consumers | Evidence | Status |
|---|---|---|---|---|---|---|---|
| ASSET-048 FORM-03 child: charter convention report scene | docs/plans/006_independence_wave_plans/006_form03_language_industry_progression_addendum_2026_07_15.md, section 17.3 | Show a multilingual constitutional table joined to engineering and transport plans | docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/ | GFX_report_event_006_form03_charter_convention → gfx/event_pictures/006_independence_wave/report_event_006_form03_charter_convention.dds, registered in interface/006_independence_wave_event_pictures.gfx | chaosx.nr6.300 through chaosx.nr6.308 in events/006_independence_wave.txt | metadata JSON, native and enlarged review sheets, decoded DDS, checksums, and dated handoff | wired |

No extra asset is being counted as a substitute for this row.

## Asset record

- Asset name: report_event_006_form03_charter_convention
- Related event ids: chaosx.nr6.300, chaosx.nr6.301, chaosx.nr6.302, chaosx.nr6.303, chaosx.nr6.304, chaosx.nr6.305, chaosx.nr6.306, chaosx.nr6.307, chaosx.nr6.308
- Intended in-game use: shared visual for the FORM-03 provisional charter, language convention, sovereign constitutional answers, corridor protocol, late accession, member result, full compact, compromise, and rupture reports
- Source mode: built-in ImageGen
- Source-mode rationale: the congress is a fictional alternate-history scene with no real-person likeness or specific real photographed event
- Source date: 2026-07-16
- Source PNG: source_png/report_event_006_form03_charter_convention_imagegen_source.png
- Prompt and provenance: prompts/report_event_006_form03_charter_convention_prompt.md
- Processed PNG: processed_png/report_event_006_form03_charter_convention.png
- Decoded runtime PNG: decoded_dds/report_event_006_form03_charter_convention_decoded.png
- Final DDS: gfx/event_pictures/006_independence_wave/report_event_006_form03_charter_convention.dds
- Target size: 210x176
- Sprite: GFX_report_event_006_form03_charter_convention
- Owning GFX file: interface/006_independence_wave_event_pictures.gfx
- Localisation key: not applicable; the picture is consumed directly by the nine event ids above
- Technical metadata: metadata/report_event_006_form03_charter_convention_metadata.json
- Native review: review/report_event_006_form03_charter_convention_native_review.png
- Enlarged nearest-neighbour review: review/report_event_006_form03_charter_convention_enlarged_nearest_review.png
- Checksums: checksums.sha256

## Exact generation prompt

The full exact prompt and original built-in output path are retained in prompts/report_event_006_form03_charter_convention_prompt.md. The prompt requests a fictional 1936-1945 documentary constitutional and public-works congress with delegates, clerks, legal drafters, and railway, canal, port, and flood-control engineers around a central charter ledger and joined technical plans. It forbids readable text, flags, military staging, modern equipment, watermarks, UI, and the finished tilted-card treatment.

## Processing record

The selected 1536x1024 RGB ImageGen source was processed with:

    python .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py <source> <processed> --seed 6048

That standard profile produced the 210x176 RGBA sepia and black-and-white report card with a 192x153 card, 4-degree tilt, soft shadow, deterministic grain, transparent margin, and softened antialiased edges.

The processed PNG was converted with:

    python .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <processed> --output gfx/event_pictures/006_independence_wave/report_event_006_form03_charter_convention.dds --width 210 --height 176

The output is a one-level legacy uncompressed 32-bit BGRA DDS.

## Technical validation

- Declared and decoded dimensions: 210x176.
- DDS magic and header: DDS magic, 124-byte DDS_HEADER, 32-byte DDS_PIXELFORMAT at byte 76.
- Pixel format: flags 65, fourCC 0, 32 bits, BGRA masks 0x00FF0000, 0x0000FF00, 0x000000FF, and 0xFF000000.
- Caps: DDSCAPS_TEXTURE at byte 108; no mipmaps; all reserved dwords are zero.
- Exact file length: 147,968 bytes, matching 128 + 210 × 176 × 4.
- Alpha: minimum 0, maximum 255; 2,932 fully transparent pixels, 6,484 partially transparent pixels, and 27,544 fully opaque pixels.
- All four corner pixels are RGBA 0,0,0,0.
- The DDS-decoded RGBA pixels are identical to the processed PNG.
- The runtime texture path and filename exactly match the registered sprite.
- All nine consumers from chaosx.nr6.300 through chaosx.nr6.308 point to the exact sprite.

## Visual judgment

The source, processed card, and decoded runtime were inspected at native size and through a 4× nearest-neighbour review. The scene reads as a sober interwar or wartime constitutional and engineering congress rather than a war room or modern boardroom. The central charter ledger, clerks, delegate grouping, technical rulers, typewriter, telephone, and rail, canal, port, bridge, and water-control plans survive the small crop. There is no readable generated text, flag artwork, battlefield content, military dominance, celebratory propaganda, modern object, watermark, or UI.

Parent visual review accepted the source, native card, and enlarged decoded comparison.

## Merge notes

- The package-root FORM-03 manifest and the Event 006 root manifest record this ASSET-048 child, its runtime sprite, and all nine live event consumers.
- docs/systems/006_independence_wave_form03_progression.md records the dedicated FORM-03 icon and charter-convention report package. No parent merge action remains.

## Simplifications, omissions, and blockers

No fallback, sourced substitute, primitive local artwork, placeholder, animation, or content simplification was used. There is no asset blocker.
