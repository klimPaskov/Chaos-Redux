---
name: chaos-redux-event-assets
description: Use when creating, sourcing, processing, converting, organizing, wiring, or documenting visual assets for Chaos Redux, including complete character portrait production for grounded and fictional subjects.
---

# Chaos Redux Event Assets

Turn accepted visual requirements into source art, processed PNG previews, engine-ready files, runtime placement, manifests, and a reviewable wiring handoff. Loose generated or downloaded images are not finished assets.

## Reference map

Read the reference that matches the asset family before producing it:

- [references/reference-library.md](references/reference-library.md): the visual-reference library, canonical reference paths for every family, and reference-use rules. Read before generating, sourcing, processing, or wiring any asset.
- [references/icon-and-ui-families.md](references/icon-and-ui-families.md): icons, achievements, decision-category art, UI panels, visual packs, progression variants, formable and state-puzzle assets, animated sprites, and the 2D unit icon and counter contract.
- [references/portrait-production.md](references/portrait-production.md): every character portrait, portrait icon, source placeholder, and user-supplied final.
- [references/event-images-and-flags.md](references/event-images-and-flags.md): report, news, and super-event images and every flag.
- [references/unit-visuals.md](references/unit-visuals.md): equipment and technology art, counters, division-template emblems, and the 3D model package handoff.
- [references/manifest-and-lineage.md](references/manifest-and-lineage.md): the asset manifest fields and generated-candidate lineage and review.

Skill-local `assets/` holds the reference and component libraries, and `tools/` holds the bundled converters and processors.

## Image-generation route

This skill owns the image-generation route for the whole repository. Claude Code generates images with the `generate_image` tool of the gptimage MCP server (parameters: `prompt`, `out`, `quality` low|medium|high|auto, `size` WIDTHxHEIGHT, `reference_images`). Codex uses native ImageGen instead. Everywhere else, "image generation" means this route.

- Make one image per call. Existing output paths are auto-versioned, so name the final `out` path explicitly and use the path the tool reports.
- State each reference image's role in the prompt, for example "Image 1 is the vanilla style reference, Image 2 the subject to keep".
- For alpha-backed families, request a genuinely transparent background in the prompt. The tool has no explicit alpha parameter, so verify the alpha channel of the saved PNG, and fall back to the documented [background-removal fallback](#native-transparency-and-background-removal-fallback) only when the saved PNG has no usable alpha.
- When a call fails, check authentication with `image_auth_status` before retrying.

## Scope and routing

Asset coverage is authorization-bounded. Do not infer a custom asset merely because its gameplay object exists. Create an asset family only when an accepted spec row, asset manifest row, or explicit user instruction requests it. Apply the same rule to optional portraits, route emblems, animation, and other asset families not present in the accepted requirement set.

Never infer an advisor, high-command, officer-corps, dossier-card, or other small-portrait family from a character, idea, trait, or `portraits = { ... }` consumer. Create that family only when the accepted requirement explicitly asks for it, otherwise leave the family absent and report the authorization boundary.

### Custom subagent split

Route file production through narrow project subagents. The main agent provides the bounded brief, reviews the output, and performs final wiring:

- `chaosx_asset_source_researcher` for non-portrait real or archival image sourcing, historical flag-design research, historically attested symbols, user-provided source photos, archival decision category pictures, and report/news/super-event images that must depict real photographed material
- `chaosx_portrait_creator` for every character portrait, including explicitly authorized fictional advisor masters: grounded source research, durable archival storage, crops and placeholders, fictional image-generation production (see [Image-generation route](#image-generation-route)), user-supplied styled-result validation, processing, DDS conversion, portrait-specific wiring, manifests, and handoffs, following [references/portrait-production.md](references/portrait-production.md)
- `chaosx_generated_event_art` for generated non-icon event art, including fictional or alternate-history report images, news images, super-event images, image-generation-created flat flag designs, faction emblems, UI panels, generated decision category pictures, and progression-state base art. It does not own character portrait masters or finals.
- `chaosx_icon_artist` for focus, idea, national-spirit, officer-corps, decision, decision-category, mission, achievement, technology, intelligence-agency, intelligence-operation, commander-trait, medal, military-raid, state-modifier, MIO, faction, building, modifier icons, and exact state-piece graphics derived from verified map geometry

Flags are a flat graphic-design pipeline, not event artwork. Historical flag research establishes the documented geometry, colours, and symbols, but image generation still produces the final clean flat design under [Flags](#flags).

For animated work, route by asset type first. Then require the chosen asset subagent to follow `chaos-redux-frame-animation` for frame plans, per-frame source art, normalization, contact sheets, preview GIFs, frame sheets, static fallbacks, and animation handoffs.

Asset subagents may create sources, processed PNG previews, final DDS files, contact sheets, manifests, durable portrait masters under `docs/assets/portraits/`, and `docs/assets/<event_id>_<event_slug>/gfx_handoff.md`.

Asset subagents must not edit `.gfx`, localisation, GUI, event, focus, idea, decision, scripted effect, scripted trigger, on_action, history, country, or spreadsheet files unless the parent explicitly grants that scope. The portrait worker has a standing narrow exception for portrait-specific `.gfx` entries and existing character portrait references.

The main agent owns final non-portrait `.gfx` sprite definitions, gameplay references, docs alignment, spreadsheet alignment, and validation. The portrait worker owns portrait-specific `.gfx` and existing character portrait references. When an asset change requires catalog alignment, update only the authoritative XLSX and run `python .tools/export_event_catalog_csv.py`; the three CSV files are export-only and must not be edited directly.

A good parent prompt to an asset subagent includes the event id, asset list, asset type, target size, source mode, final DDS folder, sprite name if already registered, reference folder, visual direction, source constraints, and anything the subagent must mark blocked instead of substituting.

For one-person country-leader or officeholder portraits, the parent prompt must state the polity's identity classification and why the source mode passes the fail-closed [Portrait source-mode gate](references/portrait-production.md#portrait-source-mode-gate).

## Preflight and requirements

### Production sequence

1. Read the accepted spec or brief, enumerate requirements, classify each asset surface, and record the requirement-to-runtime crosswalk.
2. Inspect the exact reference family and consumer, then assign stable names, sprites, sizes, and paths before requesting art.
3. Select the authorized source mode and specialist, apply portrait identity/ownership gates, and prepare the workspace and manifest.
4. Produce source art under the applicable family contract; for animation, plan and obtain real frames and a static fallback before normalization.
5. Preserve original source images and source PNGs, save processed PNG previews, and complete required independent and parent reviews before DDS conversion and promotion.
6. Deliver engine-ready files and the wiring handoff; the parent integrates consumers, aligns documentation/catalog facts, and completes the workspace lifecycle.

### Asset repository preflight and Git LFS hydration

Before processing a large asset set, classify paths by role: `.gfx` files are text registries, while `.png`, `.dds`, `.wav`, and other artwork or audio paths are binary candidates, and modified files outside the requested scope must remain untouched.

- Detect Git LFS pointer stubs from the exact pointer signature, not byte size: the first line is exactly `version https://git-lfs.github.com/spec/v1`, followed by `oid sha256:<hex>` and `size <integer>` lines.
- File size alone is not validity evidence. Legitimate tiny images such as 10x7 flags may be under 1 KB.
- If the required objects are present in `.git/lfs/objects`, run a scoped `git lfs checkout <paths>` first, limited to the requested binary paths. `git lfs checkout` preserves modified files.
- Use `git lfs fetch` or `git pull` only when objects are missing and the task explicitly authorizes network or repository updates. Never broaden the scope or discard local edits.
- For every expected LFS path, compare the working file's SHA-256 to its index OID from `git lfs ls-files -l`, then confirm zero remaining pointer stubs.
- If checkout reports an index-refresh warning after writing real content, retain the content/OID verification as authoritative and record the warning in the handoff.
- After hydration, validate image and audio containers with format-aware decoders or parsers, such as DDS header and pixel checks or WAV metadata checks, rather than size heuristics.

### Standard HOI4 asset sizes

Confirm canvas and frame behavior before requesting art. Use these defaults unless the accepted spec, active consumer, or established repo pattern requires another size:

- report event images: 210x176
- news event images: 397x153, black and white
- country-leader portraits: 156x210
- commander portraits: 156x210 full portrait textures, never a fabricated 50x67 source texture
- operative portraits: 156x210 full portrait textures, still follow the cataloged owning sprite
- flags small: 10x7
- flags medium: 41x26
- flags normal: 82x52
- tech icons small: 64x64
- tech icons medium: 132x52
- achievements: 64x64
- super-event images: 457x328
- decision icons: 32x32
- idea and national spirit icons: 64x64
- focus icons: 94x86

For every icon, counter, emblem, strip, or model material not listed above, take the canvas and frame behavior from the matching canonical catalog entry and owning vanilla definition. Do not infer a universal size from the folder name or from a visually similar asset family.

### Naming rules

Use lowercase snake_case and keep wired names stable.

Recommended filename prefixes:

- idea icons: `idea_`
- focus icons: `goal_`
- decision icons: `decision_`
- decision category icons: `decision_category_`
- report event images: `report_event_`
- news event images: `news_event_`
- super-event images: `super_event_`
- achievement icons: `achievement_`
- country-leader portraits: `leader_`
- commander portraits: `commander_`
- operative portraits: `operative_`

For event-specific assets, include the event id or slug where useful. For example, all idea assets related to an event should go into one folder of that event.

### Temporary event asset workspaces

Use `docs/assets/<event_id>_<event_slug>/` with `manifest.md`, `prompts/`, `source_png/`, `processed_png/`, `contact_sheets/`, `notes/`, and `gfx_handoff.md` as needed. Treat it as a temporary, event-scoped working and evidence folder, not as a shipped asset library. Keep original sources, processed previews, and runtime outputs separate. Use it during active implementation for source files, processed previews, contact sheets, prompts, provenance, manifests, animation plans and previews, source-audio downloads, and handoff notes. Keep it while the event is active, blocked, awaiting review, or undergoing acceptance scenarios.

### Git LFS storage budget

Git LFS holds only files Hearts of Iron IV loads: `.dds`, `.tga`, `.png`, `.mesh` and `.anim` under `gfx/`, `.wav` and `.ogg` under `sound/` and `music/`, map bitmaps under `map/`, and the root `thumbnail.png`. The `.gitattributes` patterns are scoped to those runtime paths, so a PNG, JPG, GIF, PSD, ZIP or XLSX anywhere else is an ordinary Git blob.
Never commit evidence images, plan or spec screenshots, previews, contact sheets, renders, PSD or PNG sources beside a DDS, GIFs, videos, archives, Blender checkpoints, provider downloads or source audio. `.gitignore` rejects those outside the maintained paths (the event-assets skill reference, the mechanics guide media in `docs/images`, the offline wiki snapshot, the two workbooks and the vendored add-on zips); keep them in `docs/assets/<event_id>_<event_slug>/` or `.tmp/`, both ignored.
A runtime file counts as unused only when no `.gfx`, `.gui`, `.asset`, script, history or localisation file names it and no engine convention loads it by name (flags by tag and ideology, achievement icons by id, loading screens, event pictures named by `.gfx`). Binaries removed from the repository because the game never loads them are kept byte for byte in `Documents/chaos_redux_lfs_archive/` at the same relative path, with the LFS OID recorded in its `README.md`; a plan or spec that links a removed file points there. Do not remove files other sessions changed in the last day or hold uncommitted edits for.
Removing a file from HEAD does not free remote LFS storage: its objects stay on the server until history is rewritten and the server prunes them, which is a user decision.

### Durable portrait source archive

Keep grounded portrait sources in the durable attributed archive, outside disposable event workspaces.
Read the complete requirements in [Durable portrait source archive](references/portrait-production.md#durable-portrait-source-archive) before this work.

## Sources and references

### Reference asset examples

This skill owns its visual-reference library under `.claude/skills/chaos-redux-event-assets/assets`, with `assets/gfx_references/` as the canonical semantic library and Vanilla HOI4 as the primary source. Before generating, sourcing, processing, or wiring any asset, read the library rules, inspect the matching category and contact sheet, and follow the cataloged source to its owning definition; reference PNGs are never final assets and must not be wired, recolored, traced, or shipped.
Read the complete requirements in [Reference asset examples](references/reference-library.md#reference-asset-examples) before this work.

### Asset source rules

Prefer a clear actor, force, symbol, ritual, crowd, machine, creature, or strange condition with an event-specific mood over neutral geography. Do not default to maps, arrows, staff tables, conference rooms, or generic war rooms unless they are the strongest visual for the asset; maps may remain secondary props. Fictional, supernatural, symbolic, and high-chaos art should convey active subjects and atmosphere.

#### Choose source mode for event photo assets

Report images, news images, and super-event images may be either internet-sourced or generated.

Use internet-sourced imagery when the asset must show a real photographed person, specific real battle, real place, real object, real newspaper, real poster, real map, real archive item, or other verifiable historical material.

Use image generation (see [Image-generation route](#image-generation-route)) when the event is fictional, alternate-history, symbolic, supernatural, high-chaos, or when a unique scene is more important than matching an existing archive image. Generated event-photo assets should be prompted as period-authentic documentary material, not modern cinematic concept art.

For generated World War II-era report/news/super-event images:

- prompt for 1936-1945 photographic technology, period composition, period clothing, period vehicles, period architecture, and documentary realism
- avoid modern streets, uniforms, props, weapons, vehicles, signage, UI overlays, cinematic color grading, and readable generated text
- keep the source PNG, processed preview, final DDS, prompt, and manifest entry
- record the source mode as generated and explain why generation fit better than sourcing
- never use text-only generation, a name, a description, or a substitute face to fabricate a real person's likeness; use [Country-leader, commander, operative, and named-officeholder portraits](references/portrait-production.md#country-leader-commander-operative-and-named-officeholder-portraits) for grounded portraits

Follow the repository web research rules from `AGENTS.md` when searching for source images.

For internet-sourced event photo assets that are meant to represent the World War II era, search for period-matching source imagery from roughly 1936 to 1945 unless the event spec gives a narrower date range. Prefer contemporary photographs, war correspondents' photographs, press agency images, propaganda posters, maps, newspapers, official records, government or military archive images, museum scans, library scans, and period illustrations. Do not use modern photographs, reenactment images, film stills, AI-looking reconstructions, postwar uniforms, streets, weapons, vehicles, buildings, colorized tourist photos, reenactments, or modern props when they do not fit the era. If no suitable period source can be found, either generate a period-authentic fictional/documentary image when the asset does not require a real source, or mark the asset as blocked or `needs_user_review`.

Record the image source, source link, author or archive if available, license or public domain status if available, estimated date or date range, why the image fits the World War II era, and any uncertainty in the manifest.

#### Portrait source-mode gate

Grounded portraits require an explicit source mode; only the user operates RunPod for their styled finals.
Read the complete requirements in [Portrait source-mode gate](references/portrait-production.md#portrait-source-mode-gate) before this work.

#### Portrait subject ownership gate

Portraits must preserve the approved person and role; route every character portrait to the portrait worker.
Read the complete requirements in [Portrait subject ownership gate](references/portrait-production.md#portrait-subject-ownership-gate) before this work.

#### Fictional portraits

Fictional or impossible portraits use image generation (see [Image-generation route](#image-generation-route)) through the portrait worker, with complete processing and wiring.
Read the complete requirements in [Fictional portraits](references/portrait-production.md#fictional-portraits) before this work.

#### User-provided assets

Treat user-provided images as sources, record that provenance, and complete the same crop, resize, conversion, placement, wiring, and documentation workflow.

## Generation and editing

### Generate and refine source art

Use image generation (see [Image-generation route](#image-generation-route)) for generated symbolic or fictional assets, including icons, flat flags, emblems, UI panels, progression art, and permitted event scenes. Choose ChatGPT Images 2.5 by the work being done:

- **Flare:** quick static new generations, including icons, report/news images, thumbnails, and static concept drafts.
- **Sunburst:** every existing-asset edit, scripted-GUI compositional reference, and every animation seed, draft, source frame, iteration, edit, and final. Never use Flare for an animation draft. Keep canvas, transparent bounds, anchors, silhouette, palette, edges, lighting, proportions, and unchanged regions consistent; model choice does not replace frame validation or drift checks.

Describe the consumer canvas, composition, detail, and background in the prompt whichever tool runs: the Codex built-in tool exposes no model, quality, size, or destination-path selector, and the gptimage `generate_image` tool exposes `quality`, `size`, and `out` but no model selector. Inspect returned dimensions, then process to the exact runtime canvas. When model selection is unavailable, retain the named preference for selectable tools but report only the actual exposed execution path, never an unreported backend or API model name as a built-in control.

Use CLI/API only when explicitly requested, following the installed official skill and verified parameter contract; do not duplicate its runner or silently switch paths. If image generation is unavailable, report the blocker and stop before an alternate route.

Do not create core artwork from simple shapes, placeholders, contact sheets, layout-only mockups, empty UI boxes, or generated charts. Final art must be real generated, sourced, or user-provided artwork, not circles, rectangles, lines, gradients, geometric diagrams, or other primitive-shape stand-ins.

For super-event images, this rule is strict: final art must be a real scene, archival image, painted illustration, or generated documentary-style image. Do not use symbolic diagrams, flat icons, abstract geometry, title cards, or UI-like compositions as the final super-event image unless the user explicitly requests that exact visual approach and the exception is documented.

Keep final artwork clean and correctly framed; review boards and layout drafts are never final source art.

#### Brief and references

State the asset type, exact consumer and canvas, subject, composition, style, intended footprint, readability, reserved space, and forbidden additions. Keep functional labels and controls native; generated text is off by default, and accepted lettering must be specified verbatim and checked character by character at source and native size. Subject anchoring never overrides portrait source-mode gates, historical-design verification, or exact map geometry.

Label each supplied image by index and filename, with its role and the properties that may transfer:

| Role | Allowed transfer | Properties to exclude unless explicitly required |
| --- | --- | --- |
| Edit target | Current accepted image and the named edit region/property | Unrequested changes elsewhere |
| Identity or subject anchor | Authorized fictional subject, object, motif, or other permitted subject properties | A reference person's face, unsupported insignia, extra subjects |
| Style or reference-family anchor | Palette, shading, texture, visual density, edge treatment | Exact artwork, subject identity, frame, text, canvas from another UI surface |
| Geometry or composition anchor | Intended arrangement, silhouette proportions, camera, reserved space | Sketch marks, labels, incidental props, invented map geometry |
| Insert or compositing input | Explicitly named object or layer with its intended placement | Its backdrop, unrelated content, unintended text |

Inspect local edit targets with `view_image` (Read in Claude Code) before editing and attach inputs using the active tool's actual schema. With the gptimage tool, pass the local paths in `reference_images` and state each image's role in the prompt. With the Codex built-in tool, when all targets have local paths, use `referenced_image_paths`; otherwise use the smallest `num_last_images_to_include` covering the required recent images, and never supply both. Do not rely on an unseen path, ambiguous “previous image,” or filenames alone to convey visual references.

#### Focused edits

With Sunburst and the execution-path rule above, when a candidate is close, edit that candidate to correct the specific defect before choosing a fresh composition. Use one coherent change per iteration, then inspect it before proceeding. Use the prior accepted output as the next edit target; if a revision drifts, return to the last accepted candidate and record that branch instead of building on the rejected result. A substantially wrong composition or an explicitly requested alternative can justify a new generation; record the reason and retain accepted candidates.

Restate the invariants in every edit: subject identity where authorized, pose/composition, palette/style, consumer canvas and intended footprint, reserved space, and alpha/background mode. For alpha-backed assets explicitly request preservation of real transparent unused canvas after every edit. For opaque scene art preserve the required painted background instead. State “no added text, symbols, subjects, borders, or UI controls” where applicable; list any deliberately authorized exception precisely. Keep functional UI labels and controls native even when the generated composition follows a complex layout.

For a coordinated asset family, an accepted candidate may anchor only the stated palette, materials, texture, or motif vocabulary; the exact consumer family remains authoritative. Follow [Icon type separation rules](references/icon-and-ui-families.md#icon-type-separation-rules) for independent surface art and [Achievement icons](references/icon-and-ui-families.md#achievement-icons) for deterministic template composition and state derivation.
When subtypes have established colour accents, record the exact sibling references and palette before generation, then compare every candidate at native size against its corresponding subtype rather than assigning arbitrary distinct colours.
Map every alias of a shared texture to its actual consumer before changing dimensions; suffixes such as `_medium` occur on both equipment and technology sprites, so split incompatible canvases into separate stable paths and repoint only the matching consumers.

#### Native transparency and background-removal fallback

Apply native transparency to icons, counters, emblems, overlays, decorative UI pieces, transparent animation frames, and every family whose inspected consumer leaves unused canvas transparent. Full-canvas scenes, flags, portraits, and painted panels retain the background required by their consumer and reference family. Do not generate an alpha-backed asset on an opaque or chroma background as the normal route. Request a real transparent background in the first image-generation call, retain that native-alpha source PNG, and preserve its alpha through crop, alignment, resizing, frame assembly, and DDS conversion.

Validate native transparency before processing: unused corners and padding must contain real zero-alpha pixels, the painted subject must retain nonzero alpha and complete edges, and the image must contain no fake checkerboard, matte, halo, key colour, or unintended transparent holes.

For transparent icon sources, a nonzero-alpha bounding box touching the canvas is not sufficient evidence of a clipped subject.
Inspect boundary coverage at more than one alpha threshold (for example, 1, 8, and 16), together with source-resolution and native-size views.
Isolated alpha-1 residue outside a complete, inset subject may receive bounded exterior-noise cleanup during normalization; preserve the untouched source, all legitimate subject detail, and the chosen threshold/bounds evidence.
If a visible leaf, frame, or other subject part is actually cut off, use a focused image-generation edit to restore it; padding or shrinking the clipped painting does not restore the missing detail.

Background removal remains a fallback for either of these cases:

- the image-generation result ignored the transparency request or failed alpha validation
- an inherited, internet-sourced, or user-provided image has an unwanted opaque backdrop and the accepted asset type requires transparency

First use a targeted image-generation edit that changes only the background to real transparency and preserves the subject, silhouette, colours, internal opacity, framing, and edge detail. If that still fails, use a deterministic local background-removal or chroma-key process only when its tool is actually installed and verified in the current environment. Preserve the untouched source, record the tool and settings, inspect for spill and clipped edges, and compare the repaired candidate with the source. If no verified fallback tool exists or removal damages the subject, mark the asset `blocked` or `needs_user_review`. Do not invent a helper path or silently ship an opaque square.

#### Review each iteration

Inspect every iteration at full source resolution and the final HOI4 native size before accepting it. Check subject and reference fidelity, silhouette, footprint, clipping, unintended additions, and small-size readability; reject fine detail that becomes noise after downsampling. Decode alpha rather than trusting a checkerboard preview: verify transparent unused pixels, intact intended opaque interior, edge continuity, and no matte, halo, colour fringe, or unintended holes. Compare each edit with its accepted parent and original anchor so accumulated drift is visible. Keep the existing contact-sheet, DDS round-trip, frame continuity, independent portrait review, and parent promotion requirements from the owner skills.

## Asset-family contracts

### Icon creation rules

Create final icons using the matching HOI4 family and the required original raster-art workflow.
Read the complete requirements in [Icon creation rules](references/icon-and-ui-families.md#icon-creation-rules) before this work.

### Report event images

Report images are `210x176` period documentary photographs, black and white with sepia (full colour only by a user exception recorded in the manifest), with no modern UI overlays and no generated text. Sourced and generated report images alike receive the local report-card treatment (tilt, transparent edge space, soft shadow) before DDS conversion.
Read the complete requirements in [Report event images](references/event-images-and-flags.md#report-event-images) before this work.

### News event images

News images are `397x153` black-and-white documentary photographs or period press illustrations with clear central subjects, no modern UI overlays, and no generated text. Source mode and era fit follow Asset source rules, and the source link or generation prompt is recorded.
Read the complete requirements in [News event images](references/event-images-and-flags.md#news-event-images) before this work.

### Super-event images

Super-event images are `457x328` real scenes, archival images, painted illustrations, or generated documentary-style images with a strong central composition and no generated text. Audio cues use `chaos-redux-super-events` with checked licensing, never generated tones.
Read the complete requirements in [Super-event images](references/event-images-and-flags.md#super-event-images) before this work.

### Decision category pictures

Use an appropriate category picture or allowed category presentation for the mechanic.
Read the complete requirements in [Decision category pictures](references/icon-and-ui-families.md#decision-category-pictures) before this work.

### Flags

Flags are flat identity assets on the `82x52`, `41x26`, and `10x7` TGA ladder. Every new flag comes from image generation after cited historical research, is never replaced by locally drawn geometry, and must pass the orientation, TGA-header, and ladder-consistency checks before completion.
Read the complete requirements in [Flags](references/event-images-and-flags.md#flags) before this work.

### Country-leader, commander, operative, and named-officeholder portraits

Route every character portrait through the portrait worker and select its grounded-source or fictional production mode.
Read the complete requirements in [Country-leader, commander, operative, and named-officeholder portraits](references/portrait-production.md#country-leader-commander-operative-and-named-officeholder-portraits) before this work.

### Advisor and high-command portrait icons

Treat advisor and high-command portraits as character portraits with their own native canvas, framing, and consumer requirements.
Read the complete requirements in [Advisor and high-command portrait icons](references/portrait-production.md#advisor-and-high-command-portrait-icons) before this work.

### UI panels and custom windows

Match the owning native UI and accepted reference for panel assets.
Read the complete requirements in [UI panels and custom windows](references/icon-and-ui-families.md#ui-panels-and-custom-windows) before this work.

### Decision category and scripted GUI visual packs

Plan and deliver the whole visual pack for the category and its interactive states.
Read the complete requirements in [Decision category and scripted GUI visual packs](references/icon-and-ui-families.md#decision-category-and-scripted-gui-visual-packs) before this work.

### Progression-state variants

Include visual variants when progression requires them.
Read the complete requirements in [Progression-state variants](references/icon-and-ui-families.md#progression-state-variants) before this work.

### Formable nation asset coverage

Cover every visible formation and identity transition with the required asset families.
Read the complete requirements in [Formable nation asset coverage](references/icon-and-ui-families.md#formable-nation-asset-coverage) before this work.

### Formable state-puzzle visual assets

For state-puzzle presentation, produce the state pieces, highlights, and controls required by the mechanic.
Read the complete requirements in [Formable state-puzzle visual assets](references/icon-and-ui-families.md#formable-state-puzzle-visual-assets) before this work.

### Animated sprites, scripted GUI assets, and animated portraits

Use real planned source frames and the frame-animation skill for 2D animation; skeletal actions belong to the 3D skill.
Read the complete requirements in [Animated sprites, scripted GUI assets, and animated portraits](references/icon-and-ui-families.md#animated-sprites-scripted-gui-assets-and-animated-portraits) before this work.

### Unit visual references

Every unit visual is a domain-and-surface-specific pipeline: classify the deliverable (equipment or technology art, large land counter, land, air, or naval map counter, division-template emblem, or 3D model package), inspect the matching catalog entries and owning vanilla definition, and never derive one unit pipeline by resizing, relabeling, or recoloring another.
Read the complete requirements in [Unit visual references](references/unit-visuals.md#unit-visual-references) before this work.

#### 2D icon and counter generation contract

Custom unit, template, and facility icons require original art, exact consumer and vanilla-reference inspection, native canvas and frame semantics, and parent visual review.
Read the complete requirements in [2D icon and counter generation contract](references/icon-and-ui-families.md#2d-icon-and-counter-generation-contract) before this work.

#### 3D model package handoff

3D model production routes to `chaos-redux-3d-model-pipeline` and `chaosx_3d_model_pipeline`; the brief and returned package must carry the profile, lineage, scale, action, firing-state, texture, audio, and runtime-consumer evidence the 3D skill requires, and the 3D worker hands counter art to `chaosx_icon_artist`.
Read the complete requirements in [3D model package handoff](references/unit-visuals.md#3d-model-package-handoff) before this work.

## Processing and installation

### DDS conversion

Final 2D PNG assets must be converted to DDS using the repository's standard 2D DDS conversion workflow. Model textures follow the separate compressed full-mip contract in [3D model package handoff](#3d-model-package-handoff). The converter lives only at `.claude/skills/chaos-redux-event-assets/tools/convert_to_dds.py`; `.tools/convert_to_dds.py` is obsolete, and active skills, agents, scripts, and handoffs must not restore or call it.

For these 2D assets, the output must be compatible with Chaos Redux's expected 32-bit BGRA or B8G8R8A8-style DDS workflow.

Run the bundled converter from the mod root:

```powershell
python -B .claude/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <processed.png> --output <final.dds> [--width <pixels> --height <pixels>]
```

If a retained custom 2D mechanical processor must write uncompressed BGRA DDS directly, mirror that converter's `write_bgra_dds` layout exactly instead of inventing another header layout.

For a standard legacy, one-level, uncompressed BGRA DDS, require all of the following:

- a 128-byte file header in total: `DDS ` magic at byte 0, `DDS_HEADER` size `124` at byte 4, and 11 reserved dwords before the pixel-format block
- `DDS_PIXELFORMAT` at byte 76 with size `32`, flags `65` (`RGB | ALPHAPIXELS`), fourCC `0`, bit count `32`, and BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, and `0xFF000000`
- `DDSCAPS_TEXTURE` (`0x1000`) at byte 108
- no mipmaps unless the target asset deliberately requires them

Validate each uncompressed one-level BGRA output by checking the declared width and height, exact file length `128 + width * height * 4`, actual alpha-byte minimum and maximum against the asset's intended transparency, and successful registration of the final path in `.gfx`. Dimension and alpha checks alone are insufficient: reject shifted pixel-format blocks, missing texture caps, or any other malformed header even when an image decoder can report plausible dimensions.

If a processing script is retained as provenance, rerun it after correcting its DDS writer and validate every DDS it produces, not only the asset that exposed the defect.

If conversion fails, stop and report the error. Do not invent another conversion route unless the user approves it.

Achievement triplets additionally follow [Shared processing and validation](references/icon-and-ui-families.md#shared-processing-and-validation) for source decoding and exact state-composition equality.

After conversion, verify the actual DDS dimensions and native or fallback-validated transparency, stable filename, event-scoped placement or documented root-only exception, `.gfx` linkage, and manifest path.

For small icon, counter, and emblem packages, decode each final DDS back to pixels at its native size and retain the round-trip comparison evidence with the contact sheet. A header, dimension, and alpha pass alone is not visual QA.

Do not leave only PNG files when the game expects DDS.

### Final asset placement and naming

Event-owned final assets should be grouped under an event-scoped folder whenever the engine surface uses explicit sprite or texture paths.

Use this folder form:

```text
<event_id>_<event_slug>
```

Place the event folder directly under the asset category folder, for example `gfx/event_pictures/014_cannibalism/` or `gfx/interface/ideas/014_cannibalism/`. Do not insert a project namespace layer such as `gfx/event_pictures/chaos_redux/014_cannibalism/`; the mod root already provides the project namespace.

Do not leave new event assets loose in category roots such as `gfx/event_pictures/`, `gfx/super_events/`, `gfx/interface/ideas/`, `gfx/interface/goals/`, `gfx/interface/decisions/`, or `gfx/leaders/` unless that root placement is an engine-facing lookup requirement.

Root-only and engine-convention exceptions:

- `gfx/achievements/` must keep achievement DDS files directly in the root. Do not create `gfx/achievements/<event_id>_<event_slug>/` subfolders unless a new engine behavior has been verified locally. Achievement filenames must match the full achievement ids from `common/achievements/`, so event-owned achievement ids and triplet filenames should use `<event_id>_<event_slug>_<achievement_name>{,_grey,_not_eligible}.dds` or the exact established id if it includes an ordinal.
- `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` must keep HOI4 tag/ideology filenames. Do not put flags into event folders; use cosmetic tags or route-specific tag filenames when an event needs transformed flags.

Shared or non-event systems may use a clear shared/system folder. Do not force shared assets into an event folder just to avoid a root directory.

When moving or adding an asset, update every `.gfx`, `.gui`, event, idea, decision, focus, localisation, and documentation reference that names the old path or sprite. Keep sprite names stable unless the engine-facing identifier itself has to change, as with achievement ids.

Super-event audio follows the `chaos-redux-super-events` convention. Register the final cue as sound from `sound/<event_id>_<event_slug>/super_event_<super_event_id>_<super_event_name>.wav`. Preserve source downloads under docs/assets source-audio paths.

### `.gfx` handoff and main-agent wiring

Asset subagents do not edit `.gfx` files by default.

When an asset needs a sprite definition, the asset package must include a handoff note for the main agent.

Recommended path while the event asset workspace is active:

```text
docs/assets/<event_id>_<event_slug>/gfx_handoff.md
```

The handoff must include:

1. Final DDS path.
2. Proposed sprite name or the exact sprite name already provided by the parent.
3. Suggested target `.gfx` file.
4. Ready-to-copy sprite definition snippet when useful.
5. Related localisation key, GUI element, event id, focus id, idea id, decision id, achievement id, or super-event slot when known.
6. Any uncertainty about sprite naming or target file placement.
7. Any blocked or needs-review asset.

If the main agent already registered `.gfx` sprites or texture paths before requesting art, the asset subagent must follow those filenames, sprite names, DDS paths, and target sizes exactly. It should only propose names or paths when they were not provided.

The main agent adds the sprite to the correct existing `.gfx` using its naming/formatting pattern, points it to the final DDS, preserves sprite names, updates all localisation/GUI/event/focus/idea/decision consumers, and aligns relevant docs and spreadsheet rows.

When wiring event-owned sprite-backed art, the texture path should point to the event-scoped folder for that asset category. If an asset must stay root-only, document the engine reason in the handoff or manifest.

Do not create a new `.gfx` file if an existing one is clearly the right place. If a new `.gfx` file is needed, the main agent must name it consistently and document why.

`gfx_handoff.md` is temporary evidence while the event asset workspace is active. Before the event goal is fully complete, copy any durable sprite, path, ownership, and uncertainty facts into the event or plan documentation that remains after cleanup, then delete the event-scoped workspace with the rest of `docs/assets/<event_id>_<event_slug>/`.

## Evidence and completion

### Manifest requirements

Every active event asset workspace carries a `manifest.md` listing every asset with its source mode, background mode, paths, sprite, status, and the portrait, animation, and ownership evidence that applies. Generated candidates keep immutable lineage with saved exact requests, input roles, review results, and an explicit final selection, and durable facts are promoted before the workspace is deleted.
Read the complete requirements in [Manifest requirements](references/manifest-and-lineage.md#manifest-requirements) before this work.

### Contact sheets

When an asset package contains many generated or sourced images, create a contact sheet for review.

For replacement work, preserve the pre-edit runtime textures, relevant registry text, and original review sheets with hashes in the owning workspace before generating comparison sheets.
Inspect a contact-sheet script's entry point and configured output paths before running it; do not assume `--help` is read-only when the script has no argument parser.
Write new sheets to an isolated task directory, never over shared baseline sheets; use the preserved runtime snapshots if another session replaces the shared sheets.
For offline sheet-load failures, resolve the actual mod or installed-vanilla texture and use DirectXTex for a review-only PNG decode when Pillow cannot handle its DDS format; record source paths, hashes and decoder limits instead of declaring the asset missing or corrupt.
A sheet that displays only frame 1 does not review a whole strip; inspect every changed frame separately at native size, and keep offline sheet checks distinct from available MCP GUI render/comparison evidence and user-supplied live observations; absent previews are limits under AGENTS.md, not missing artwork.

Small template, facility, unit, counter, and emblem packages always require a native-size contact sheet, even when the package contains one final asset.

The canonical decision category picture reference family always requires:

`assets/gfx_references/icons/decision_categories/pictures/contact_sheet.png`

Create or refresh that sheet whenever reference images are added, removed, renamed, or replaced. Show filenames and native dimensions. Record user-provided reference images as user-provided in the catalog and do not treat them as runtime-ready assets.

Do not use contact sheets as final game assets.

Label asset names, types, selected final versions, and rejected alternatives where relevant.

For the small-icon and counter contract, the sheet must also show the native-alpha image-generation source, processed transparency, enlarged smooth preview, and decoded DDS round-trip with dimensions, frame labels, and visible-bounds notes. If fallback removal was used, include the untouched opaque source and repaired edge comparison.

### Requirement-to-runtime coverage audit

Before any asset completion claim, create or refresh a row-level coverage crosswalk from every accepted asset requirement in the current specs, manifest plans, and animation plans. Do not start from the assets that happen to be live. Each accepted row must identify:

- its requirement id and accepted design source
- its intended in-game purpose
- the exact source package and manifest entry
- the exact runtime registration: final asset path plus the `.gfx` sprite or texture, engine lookup id, or other owning definition as applicable
- the live consumer file and id
- the state or visibility binding when the asset is conditional or state-driven
- the current audit record path, evidence, and row status

Before changing asset or portrait wiring or completion counts, audit the full current required logical slot -> registered alias -> actual runtime path matrix, including conditional or regional variants and aliases sharing a path. Preserve the audited requirement, registry, and consumer source revisions/hashes, runtime file hashes, and declared coverage bounds in the audit record before making the change. A partial receipt or historical count must never stand in for the current consumer inventory.

Report file inventory, registered aliases and actual consumption, source provenance/archive packages, and accepted final coverage separately. Count unique consumed runtime paths, unique whole-file hashes, and unique decoded-pixel hashes as separate measures. File presence or alias consumption does not prove source provenance or final acceptance.

For every animation family, also record the purpose and the direction or state semantics that distinguish the family, together with its frame, timing, and loop evidence. Frame totals, live animation-family totals, and registered sprite totals are not coverage proof.

For every real-person portrait row, link the unchanged source, explicit crop, wired placeholder, user-supplied final when available, role references, comparison evidence, reviewer, and likeness/framing/provenance verdict. Style quality cannot compensate for identity failure.

Audit exact rows, not counts. An extra asset or animation cannot satisfy an absent accepted row unless an explicit accepted design amendment identifies that row and names the replacement; link that amendment in the crosswalk. Any missing source package, runtime registration, live consumer, required state or visibility binding, or current audit record leaves the row incomplete.

After a late user correction or accepted spec, manifest-plan, or animation-plan change, rebuild the crosswalk against the current repository and attach a fresh coverage diff listing added, removed or replaced, changed, and still-uncovered rows. Do not reuse the prior audit or its totals for the completion claim.

### Documentation updates

Keep event or mechanic docs aligned with existing assets, final DDS paths, owning or proposed `.gfx` files and sprite names, placeholders, and outstanding final art. Remove descriptions of obsolete or missing assets.

### Handling blocked assets

Mark an asset `blocked` when it cannot be created or processed cleanly. Record its name, reason, attempts, required user input, and whether implementation can continue without it.

Do not invent a substitute asset unless the user explicitly approves it.

### Completion review

Require a complete [Requirement-to-runtime coverage audit](#requirement-to-runtime-coverage-audit), every applicable family contract, source/native-size and independent reviews, contact sheets, candidate lineage, strict DDS/round-trip evidence, runtime registrations and consumers, and aligned documentation. Real animation frames require continuity/drift review and static fallbacks. The parent owns integration and the user owns live-game validation.

Retain active evidence until package review, then follow [Workspace cleanup](#workspace-cleanup) at full event completion. A missing accepted row, failed review, unsupported source mode, missing consumer, or unresolved blocker leaves the goal incomplete. Report every omission and approved exception; if none were made, say so explicitly.

### Workspace cleanup

Before declaring the event goal fully complete:

1. Confirm that every accepted asset row has a final runtime consumer and that no runtime reference points into `docs/assets/`.
2. Promote durable provenance, licensing, attribution, requirement-to-runtime crosswalks, review results, accepted handoff facts, and blocker or exception notes into permanent `docs/events/`, `docs/plans/`, `docs/specs/`, `docs/super_events/`, or another appropriate documentation surface.
3. Move final runtime assets into engine-facing folders and verify their `.gfx`, `.gui`, audio, or gameplay references.
4. Delete the complete event-scoped temporary workspace, including empty subfolders, and verify that it is absent. Never delete the separate durable portrait source archive under `docs/assets/portraits/` as part of this cleanup.

An absent event-scoped `docs/assets/` folder is expected after a fully complete goal and is not an asset blocker. If the event is incomplete or blocked, retain the workspace and report the blocker. Never delete skill-local `assets/` reference libraries or an unrelated event workspace.
