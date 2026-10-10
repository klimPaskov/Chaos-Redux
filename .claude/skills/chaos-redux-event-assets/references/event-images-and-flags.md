# Event images and flags

Read this reference for report, news, and super-event images and for every flag. It holds the canvas, source-mode, card-treatment, and verification contracts for those families. Use the main skill for source selection, generation, conversion, and final review.

## Asset-family contracts

### Report event images

Report images are period documentary photographs or field material with clear subjects, natural period framing, no modern UI overlays, and no generated text. Apply Asset source rules for archival versus fictional imagery and era fit. The final image is `210x176`, black and white with sepia; full colour requires an explicit user exception recorded in the manifest.

#### Report-event card treatment

Report-event images use a finished `210x176` RGBA canvas. The source photograph is processed as a slightly tilted documentary card with transparent edge space and a soft drop shadow. The transparent corners are part of the style.

Do not ask image generation to create the tilted card. Generate or source the documentary photograph first, then apply the card treatment locally. This keeps the tilt, shadow, and margins consistent.

```powershell
python -B .claude/skills/chaos-redux-event-assets/tools/process_report_event_image.py source.png processed_report_event.png
python -B .claude/skills/chaos-redux-event-assets/tools/process_report_event_image.py source_folder processed_folder
```

The script performs cover crop, black-and-white conversion, sepia application, grain, paper border, deterministic tilt, transparent canvas margin, and soft shadow. It writes RGBA PNG output. Convert the processed PNG to DDS through the normal repo workflow.

Validation:

- processed PNG is exactly `210x176`
- final DDS is exactly `210x176`
- corner pixels are transparent
- no hard photo pixels are clipped
- tilt is visible but subtle
- shadow is soft and not a thick border
- edge space is transparent, not black padding
- source remains readable after crop, tilt, shadow, and DDS conversion

Generated report images must still receive this local report-card treatment.

### News event images

News images are `397x153` black-and-white documentary photographs or period press illustrations with clear central subjects, strong contrast, period composition, no modern UI overlays, and no generated text. Apply Asset source rules for archival versus fictional imagery and era fit. Convert generated sources to black and white with period press contrast/grain and no modern colour remnants. Record the source link/license or generation prompt and source-mode rationale.

### Super-event images

Super-event images are `457x328` scenes with strong central composition, a dramatic theme, readable subjects, enough contrast for HOI4 UI, and no generated text or small-detail clutter. Apply Asset source rules for archival versus fictional imagery and era fit, and Generate and refine source art for scene-art requirements and documented user exceptions.

If a super-event needs an audio cue, use `chaos-redux-super-events` and research a suitable public domain or clearly licensed recording. Register the final cue as sound from the event-scoped `sound/<event_id>_<event_slug>/` folder. Never create event or super-event audio from generated test tones, primitive waveforms, beeps, noise beds, or local oscillator output, including sine, square, triangle, and sawtooth waveforms.

Document each track's title, composer, performer or recording source where relevant, checked license or public-domain status, source link, thematic fit, suggested in-game use, and editing notes. Do not claim public-domain status without checking; mark an unclear license uncertain or unsuitable.

### Flags

Flags should use clean symbolic designs that look like intentional flag designs, not simple-shape placeholders, palette swaps, ugly filters, or flipped/recolored variants. Treat flags as flat identity assets, not artwork or illustrated scenes.

Inspect the complete flat flag ladders in `flags/normal/`, `flags/medium/`, and `flags/small/` before creating or processing flags. Compare all three sizes together in `flags/contact_sheet.png`.

Keep the design readable across the required normal `82x52`, medium `41x26`, and small `10x7` ladder.

HOI4 flag TGAs must use the same origin/header convention as vanilla flags. Validate with `file`, completed flag TGAs should read as Targa image data at the correct size and must not end with `- top`. If a flag displays upside down in-game while the artwork looks correct in an image viewer, fix the TGA encoding/origin on the flag files themselves. Do not add custom UI sprites, scripted-localisation routing, DDS display copies, or other workarounds for flag orientation.

Use enough heraldic detail to prove that the design is authored rather than a basic-shape placeholder, while keeping the principal emblem readable at `10x7`. Prefer a layered civic, heraldic, industrial, botanical, maritime, or institutional emblem with a clear outer silhouette over an isolated circle, star, arrow, stripe, or geometric blob.

Avoid generated text unless the design absolutely requires it and the final output is manually checked.

Always use image generation (see [Image-generation route](../SKILL.md#image-generation-route)) for every new flag, including historically attested and real-world designs. Historical research still comes first: save and cite a reliable design reference, then use it as an image input and strict design constraint for image generation. The generated result must be a clean, flat flag reconstruction, not an illustration of a flag. Reject waving fabric, folds, flagpoles, skies, lighting, gradients, painterly texture, vignettes, fake lettering, invented seals, perspective, shadows, or any scene around the flag. Manually compare geometry, colour fields, symbol count, symbol orientation, and heraldic details with the cited reference before resizing it. Image generation is not permission to reinterpret a documented historical design.

For existing countries that already have game-provided or repository-approved base flags, do not replace the no-suffix base flag as part of an ideology pass. Keep the base flag unchanged, or restore it from the approved prior asset if an asset pass damaged it, unless the user explicitly asks for that base flag to be redone or the country receives a deliberate focus/event/cosmetic-tag transformation. Ideology variants should be separate assets for `_communism`, `_democratic`, `_fascism`, and `_neutrality`, not mutations of the base flag with one small shape, a palette swap, a color filter, a vertical flip, or a copied emblem.

For focus-tree or event route flag changes, use explicit cosmetic tags or route-specific flag files and document the trigger/focus that changes the flag. Do not create default flag overrides or new base flags for vanilla-supported or already-existing countries just because they participate in an event.

Historical or historically grounded flags must use sourced motifs, documented heraldry, period symbols, or clearly explained alternate-history synthesis. If no directly attested flag exists, state that in the manifest and produce a historically grounded design from relevant motifs instead of inventing unrelated symbols.

Generated fictional or alternate-history flag variants must come from a separate image-generation result for each visually distinct design and then be processed into final flag sizes. Preserve the generated emblem geometry, internal heraldic construction, and identifying details through export. Do not replace the generated design with local rectangles, circles, stars, arrows, traced silhouettes, or other programmatically drawn geometry. Do not use a solid-fill normalizer, aggressive palette quantizer, vector trace, or edge simplifier that reduces generated detail to primitive shapes. Mechanical cropping, colour management, edge cleanup, orientation correction, resizing, and TGA export are allowed, but they must not become the source of the design.

Keep the full image-generation source master and create a comparison sheet containing that master plus the normal, medium, and small exports. Reject a flag when its normal export no longer contains the distinctive generated emblem or when its small export reads as an accidental blob. The flat-design restrictions apply to both source and exports.

Before marking any flag complete, verify normal, medium, and small TGA files:

- correct dimensions across the required size ladder
- correct visual orientation in a contact sheet
- TGA origin/header convention consistent with vanilla HOI4 flags, `file` output must not show `- top`
- no byte-identical ideology variants unless the design is intentionally shared and documented
- no upside-down copies
- no accidental no-suffix base-flag replacement for countries that were only meant to receive ideology variants
