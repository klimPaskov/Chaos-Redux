---
name: chaos-redux-event-assets
description: Use when creating, sourcing, processing, converting, organizing, wiring, or documenting visual assets for Chaos Redux, including complete character portrait production for grounded and fictional subjects.
---

# Chaos Redux Event Assets

Turn accepted visual requirements into source art, processed PNG previews, engine-ready files, runtime placement, manifests, and a reviewable wiring handoff. Loose generated or downloaded images are not finished assets.

## Scope and routing

Asset coverage is authorization-bounded. Do not infer a custom asset merely because its gameplay object exists. Create an asset family only when an accepted spec row, asset manifest row, or explicit user instruction requests it. Apply the same rule to optional portraits, route emblems, animation, and other asset families not present in the accepted requirement set.

Never infer an advisor, high-command, officer-corps, dossier-card, or other small-portrait family from a character, idea, trait, or `portraits = { ... }` consumer. Create that family only when the accepted requirement explicitly asks for it, otherwise leave the family absent and report the authorization boundary.

### Custom subagent split

Route file production through narrow project subagents. The main agent provides the bounded brief, reviews the output, and performs final wiring:

- `chaosx_asset_source_researcher` for non-portrait real or archival image sourcing, historical flag-design research, historically attested symbols, user-provided source photos, archival decision category pictures, and report/news/super-event images that must depict real photographed material
- `chaosx_portrait_creator` for every character portrait, including explicitly authorized fictional advisor masters: grounded source research, durable archival storage, crops and placeholders, fictional native ImageGen production, user-supplied styled-result validation, processing, DDS conversion, portrait-specific wiring, manifests, and handoffs, following [references/portrait-production.md](references/portrait-production.md)
- `chaosx_generated_event_art` for generated non-icon event art, including fictional or alternate-history report images, news images, super-event images, ImageGen-created flat flag designs, faction emblems, UI panels, generated decision category pictures, and progression-state base art. It does not own character portrait masters or finals.
- `chaosx_icon_artist` for focus, idea, national-spirit, officer-corps, decision, decision-category, mission, achievement, technology, intelligence-agency, intelligence-operation, commander-trait, medal, military-raid, state-modifier, MIO, faction, building, modifier icons, and exact state-piece graphics derived from verified map geometry

Flags are a flat graphic-design pipeline, not event artwork. Historical flag research establishes the documented geometry, colours, and symbols, but ImageGen still produces the final clean flat design under [Flags](#flags).

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

### Durable portrait source archive

Keep grounded portrait sources in the durable attributed archive, outside disposable event workspaces.
Read the complete requirements in [Durable portrait source archive](references/portrait-production.md#durable-portrait-source-archive) before this work.

## Sources and references

### Reference asset examples

This skill owns its visual-reference library under:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets`

`assets/gfx_references/` is the canonical semantic library, with Vanilla HOI4 as the primary source and explicitly marked Chaos Redux examples where needed. Do not route reference work through project-root asset folders or another skill-local copy.

Start with:

- library rules and contact sheets: `assets/gfx_references/README.md`
- exact source provenance and dimensions: `assets/gfx_references/CATALOG.md`

Unless a path below begins with `assets/`, interpret it relative to `assets/gfx_references/`.

Every semantic reference directory contains its own `contact_sheet.png`; there is no shared `contact_sheets/` directory. Contact sheets are labeled with filenames and native dimensions, and are review aids rather than reference examples themselves. Common icon families (focus, ideas, decisions, decision categories, technologies, and achievement states) have at least 15 references, while other tracked texture and icon families have at least 5. The interface library covers complex vanilla scripted GUIs and other native interfaces, with meaningful functional compositions for each distinct layout family. Crop MCP renders to useful UI bounds; full-window images dominated by empty space are unsuitable reference examples. Retain full-render source, source window/files, original resolution and UI scale, and crop bounds in provenance so each crop can be traced back to its native layout.

#### Canonical portrait paths

- country leaders: `assets/gfx_references/portraits/leaders/`
- army and navy commanders: `assets/gfx_references/portraits/commanders/`
- operatives: `assets/gfx_references/portraits/operatives/`
- advisors and high-command dossier cards: `assets/gfx_references/portraits/advisors/`

The leader reference shelf at `assets/gfx_references/portraits/leaders/` is the direct portrait folder for agents that need one. It holds only byte-aligned copies of the curated leader references from `assets/gfx_references/portraits/`, is never a separate source of truth or a runtime asset folder, and uses `gfx_references/REFERENCE_MANIFEST.md` for the current file list. Do not wire any reference shelf into runtime GFX, and do not infer advisor assets from it. Country leaders, commanders, and operatives are full `156x210` portrait textures. For portrait work, inspect the canonical role-specific contact sheet. Advisor and high-command dossier references are native `65x67` cards and use their own canonical contact sheet; do not substitute full leader, commander, or operative portraits for this family.

#### Canonical flag and event-art paths

- flat flags: `flags/normal/`, `flags/medium/`, and `flags/small/`
- report-event art: `event_art/report/`
- news-event art: `event_art/news/`
- super-event art: `event_art/super_event/`

#### Canonical interface layout paths

- general settings: `scripted_guis/general_settings/`
- institutional boards: `scripted_guis/institutional_boards/`
- Chaos Redux settings: `scripted_guis/chaos_redux/settings/`
- Chaos Redux event log: `scripted_guis/chaos_redux/event_log/`
- Chaos Redux pressure and deaths: `scripted_guis/chaos_redux/chaos_meter/`

Read `scripted_guis/README.md`, inspect the root and category contact sheets, then inspect the paired installed vanilla or Chaos Redux `.gui`, focus-inlay, and `common/scripted_guis` sources before creating a scripted GUI reference. The in-game captures and source-backed MCP crops have distinct provenance in `REFERENCE_MANIFEST.md`; neither replaces the new or redesigned window's required compositional reference.

Accept only clean interface references rendered under plausible, internally consistent scenarios: no unresolved dynamic localisation tokens, raw localisation keys, placeholder/debug text, contradictory empty/populated messages, simultaneously visible mutually exclusive panes, or meaningless blank fields. When C++-bound text or rows cannot be supplied otherwise, use source fixtures in isolated temporary copies of vanilla layouts, preserving source-equivalent geometry, native hierarchy, fonts, assets, and controls. Record every fixture change and its source/scenario provenance explicitly; never edit installed vanilla or core shared sources, or bake fake labels/buttons into screenshot art. Reject the candidate if clean, faithful output cannot be produced.

#### Canonical gameplay-icon paths

- national focus: `icons/national_focus/`
- ideas and national spirits: `icons/ideas/`
- decisions: `icons/decisions/`
- missions: `icons/missions/`
- decision category icons: `icons/decision_categories/`
- decision category pictures: `icons/decision_categories/pictures/`
- achievement state triplets: `icons/achievements/`
- officer corps spirits: `icons/officer_corps_spirits/`
- technologies: `icons/technologies/`
- special projects: `icons/special_projects/`
- balance of power: `icons/balance_of_power/`
- intelligence agencies: `icons/intelligence_agency/`
- intelligence operations: `icons/intelligence_operations/`
- commander traits: `icons/commander_traits/`
- medals: `icons/medals/`
- military raids: `icons/military_raids/`
- state modifiers: `icons/state_modifiers/`
- military industrial organizations: `icons/military_industrial_organizations/`
- factions: `icons/factions/`
- buildings: `icons/buildings/`
- modifiers: `icons/modifiers/`

The canonical decision category picture family is:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\gfx_references\icons\decision_categories\pictures`

This family contains the larger visual pictures used to establish a decision category's theme or territorial context. It is separate from the small category icon family at `icons/decision_categories/`.

The current reference examples use a native `114x101` canvas. Treat that size as the reference-family canvas, not as a universal runtime assumption. Inspect the active vanilla or Chaos Redux sprite and GUI consumer before choosing the final runtime size.

The picture folder must contain its own `contact_sheet.png`. If the contact sheet is missing, create it before new category-picture work. Label every reference with its filename and native dimensions, record each source as Vanilla, Chaos Redux, or user-provided reference material in `CATALOG.md`, and update the reference library README when the family or workflow changes. The reference images and contact sheet are review-only assets. Never wire, recolour, trace, or ship them as runtime art.

After placing a technology or doctrine icon, use the read-only `mcp__hoi4_agent_tools__hoi4_tech_inspect` in `explain` or `lint` mode to verify the sprite and texture references, then use the `assets` or affected folder view in `mcp__hoi4_agent_tools__hoi4_tech_render` for deterministic review. Apply the AGENTS.md retry limit to these checks. Tool exposure does not establish service health or standalone Technology Tree Viewer installation. If the route remains unavailable, inspect the technology, GFX, DDS, and folder placement directly and report the missing visual check; a standalone viewer is required only when the task needs it. Missing or ambiguous assets remain implementation findings. This skill still owns source art, processing, DDS conversion, placement, manifests, and sprite handoff.

#### Canonical unit-visual paths

- equipment and technology art: `units/equipment/technology_art/`
- large land-unit counters: `units/land/counters_large/`
- land map counters: `units/land/map_counters/`
- division-template emblems: `units/land/division_template_emblems/`
- air map counters: `units/air/map_counters/`
- naval map counters: `units/naval/map_counters/`
- land model materials: `units/models_3d/land_materials/`
- air model materials: `units/models_3d/air_materials/`
- naval model materials: `units/models_3d/naval_materials/`

The semantic tree is not a bank of interchangeable pictures. Use the folder for the exact owning UI or model surface, then follow the cataloged source, native canvas, frame count, transparency, and owning definition.

The reusable achievement creation inputs live under `icons/achievements/template/`. The actual supplied filenames are `achievement_template.png` (completed background), `achievement_template_grey.png` (grey and not-eligible background), and `overlay.png` (unchanged red-cross not-eligible overlay). They are workflow inputs rather than reference examples, so they are excluded from the achievement contact sheet and coverage count. Preserve these supplied files byte-for-byte and at their exact native alignment.

Do not add new reference images outside the skill-local `assets/` root. Add Vanilla HOI4 and Chaos Redux semantic references under `assets/gfx_references/` with exact provenance, dimensions, and contact-sheet coverage recorded in its catalog. Keep reusable source components under `assets/visual_components/` and record their native canvas and role in its catalog.

Before generating, sourcing, processing, or wiring an asset, read the library rules, inspect the matching category and contact sheet, and follow the cataloged source path to its owning `.gfx`, `.gui`, `.asset`, or `.mesh` definition when engine behavior matters. Canonical GFX reference PNGs are never final assets: do not wire, recolor, trace, or ship them. If no category matches, inspect the closest canonical category plus a direct vanilla or established Chaos Redux precedent before choosing a style.

For matching icon and portrait briefs, inspect `assets/visual_components/CATALOG.md` and the relevant contact sheet after the exact vanilla or Chaos Redux consumer and `assets/gfx_references/` family. The catalog role governs whether a component is only a visual reference or may also be a persistent background layer. Keep every used component source and ImageGen source separate from the processed preview and final DDS; record the local catalog entry, role, and layer path in the output manifest. The exact consumer still governs dimensions, alpha, states, and wiring, and achievement templates and state rules still apply.

When validating inherited GUI or GFX references, check both the mod and installed vanilla roots before declaring a DDS or other resource missing. A missing literal `effectFile` `.lua` path alone does not prove a missing asset. Inspect matching installed-vanilla `.gfx` declarations and the associated shader resource before reporting a missing source. Record the exact declaration, resource path, and lookup evidence without assuming a generic `.lua` to `.shader` mapping. Source linkage evidence does not prove rendered behavior or live-game correctness.

### Asset source rules

Prefer a clear actor, force, symbol, ritual, crowd, machine, creature, or strange condition with an event-specific mood over neutral geography. Do not default to maps, arrows, staff tables, conference rooms, or generic war rooms unless they are the strongest visual for the asset; maps may remain secondary props. Fictional, supernatural, symbolic, and high-chaos art should convey active subjects and atmosphere.

#### Choose source mode for event photo assets

Report images, news images, and super-event images may be either internet-sourced or generated.

Use internet-sourced imagery when the asset must show a real photographed person, specific real battle, real place, real object, real newspaper, real poster, real map, real archive item, or other verifiable historical material.

Use `$imagegen` when the event is fictional, alternate-history, symbolic, supernatural, high-chaos, or when a unique scene is more important than matching an existing archive image. Generated event-photo assets should be prompted as period-authentic documentary material, not modern cinematic concept art.

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

Fictional or impossible portraits use native ImageGen through the portrait worker, with complete processing and wiring.
Read the complete requirements in [Fictional portraits](references/portrait-production.md#fictional-portraits) before this work.

#### User-provided assets

Treat user-provided images as sources, record that provenance, and complete the same crop, resize, conversion, placement, wiring, and documentation workflow.

## Generation and editing

### Generate and refine source art

Use the official `$imagegen` skill and built-in `image_gen` for generated symbolic or fictional assets, including icons, flat flags, emblems, UI panels, progression art, and permitted event scenes. Choose ChatGPT Images 2.5 by the work being done:

- **Flare:** quick static new generations, including icons, report/news images, thumbnails, and static concept drafts.
- **Sunburst:** every existing-asset edit, scripted-GUI compositional reference, and every animation seed, draft, source frame, iteration, edit, and final. Never use Flare for an animation draft. Keep canvas, transparent bounds, anchors, silhouette, palette, edges, lighting, proportions, and unchanged regions consistent; model choice does not replace frame validation or drift checks.

The built-in tool exposes no model, quality, size, or destination-path selector: describe the consumer canvas, composition, detail, and background in the prompt, inspect returned dimensions, then process to the exact runtime canvas. When model selection is unavailable, retain the named preference for selectable tools but report only the actual exposed execution path, never an unreported backend or API model name as a built-in control.

Use CLI/API only when explicitly requested, following the installed official skill and verified parameter contract; do not duplicate its runner or silently switch paths. If ImageGen is unavailable, report the blocker and stop before an alternate route.

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

Inspect local edit targets with `view_image` before editing and attach inputs using the actual built-in schema. When all targets have local paths, use `referenced_image_paths`; otherwise use the smallest `num_last_images_to_include` covering the required recent images, and never supply both. Do not rely on an unseen path, ambiguous “previous image,” or filenames alone to convey visual references.

#### Focused edits

With Sunburst and the execution-path rule above, when a candidate is close, edit that candidate to correct the specific defect before choosing a fresh composition. Use one coherent change per iteration, then inspect it before proceeding. Use the prior accepted output as the next edit target; if a revision drifts, return to the last accepted candidate and record that branch instead of building on the rejected result. A substantially wrong composition or an explicitly requested alternative can justify a new generation; record the reason and retain accepted candidates.

Restate the invariants in every edit: subject identity where authorized, pose/composition, palette/style, consumer canvas and intended footprint, reserved space, and alpha/background mode. For alpha-backed assets explicitly request preservation of real transparent unused canvas after every edit. For opaque scene art preserve the required painted background instead. State “no added text, symbols, subjects, borders, or UI controls” where applicable; list any deliberately authorized exception precisely. Keep functional UI labels and controls native even when the generated composition follows a complex layout.

For a coordinated asset family, an accepted candidate may anchor only the stated palette, materials, texture, or motif vocabulary; the exact consumer family remains authoritative. Follow [Icon type separation rules](references/icon-and-ui-families.md#icon-type-separation-rules) for independent surface art and [Achievement icons](references/icon-and-ui-families.md#achievement-icons) for deterministic template composition and state derivation.
When subtypes have established colour accents, record the exact sibling references and palette before generation, then compare every candidate at native size against its corresponding subtype rather than assigning arbitrary distinct colours.
Map every alias of a shared texture to its actual consumer before changing dimensions; suffixes such as `_medium` occur on both equipment and technology sprites, so split incompatible canvases into separate stable paths and repoint only the matching consumers.

#### Native transparency and background-removal fallback

Apply native transparency to icons, counters, emblems, overlays, decorative UI pieces, transparent animation frames, and every family whose inspected consumer leaves unused canvas transparent. Full-canvas scenes, flags, portraits, and painted panels retain the background required by their consumer and reference family. Do not generate an alpha-backed asset on an opaque or chroma background as the normal route. Request a real transparent background in the first built-in ImageGen call, retain that native-alpha source PNG, and preserve its alpha through crop, alignment, resizing, frame assembly, and DDS conversion.

Validate native transparency before processing: unused corners and padding must contain real zero-alpha pixels, the painted subject must retain nonzero alpha and complete edges, and the image must contain no fake checkerboard, matte, halo, key colour, or unintended transparent holes.

For transparent icon sources, a nonzero-alpha bounding box touching the canvas is not sufficient evidence of a clipped subject.
Inspect boundary coverage at more than one alpha threshold (for example, 1, 8, and 16), together with source-resolution and native-size views.
Isolated alpha-1 residue outside a complete, inset subject may receive bounded exterior-noise cleanup during normalization; preserve the untouched source, all legitimate subject detail, and the chosen threshold/bounds evidence.
If a visible leaf, frame, or other subject part is actually cut off, use a focused ImageGen edit to restore it; padding or shrinking the clipped painting does not restore the missing detail.

Background removal remains a fallback for either of these cases:

- the built-in ImageGen result ignored the transparency request or failed alpha validation
- an inherited, internet-sourced, or user-provided image has an unwanted opaque backdrop and the accepted asset type requires transparency

First use a targeted built-in ImageGen edit that changes only the background to real transparency and preserves the subject, silhouette, colours, internal opacity, framing, and edge detail. If that still fails, use a deterministic local background-removal or chroma-key process only when its tool is actually installed and verified in the current environment. Preserve the untouched source, record the tool and settings, inspect for spill and clipped edges, and compare the repaired candidate with the source. If no verified fallback tool exists or removal damages the subject, mark the asset `blocked` or `needs_user_review`. Do not invent a helper path or silently ship an opaque square.

#### Review each iteration

Inspect every iteration at full source resolution and the final HOI4 native size before accepting it. Check subject and reference fidelity, silhouette, footprint, clipping, unintended additions, and small-size readability; reject fine detail that becomes noise after downsampling. Decode alpha rather than trusting a checkerboard preview: verify transparent unused pixels, intact intended opaque interior, edge continuity, and no matte, halo, colour fringe, or unintended holes. Compare each edit with its accepted parent and original anchor so accumulated drift is visible. Keep the existing contact-sheet, DDS round-trip, frame continuity, independent portrait review, and parent promotion requirements from the owner skills.

## Asset-family contracts

### Icon creation rules

Create final icons using the matching HOI4 family and the required original raster-art workflow.
Read the complete requirements in [Icon creation rules](references/icon-and-ui-families.md#icon-creation-rules) before this work.

### Report event images

Report images are period documentary photographs or field material with clear subjects, natural period framing, no modern UI overlays, and no generated text. Apply Asset source rules for archival versus fictional imagery and era fit. The final image is `210x176`, black and white with sepia; full colour requires an explicit user exception recorded in the manifest.

#### Report-event card treatment

Report-event images use a finished `210x176` RGBA canvas. The source photograph is processed as a slightly tilted documentary card with transparent edge space and a soft drop shadow. The transparent corners are part of the style.

Do not ask `$imagegen` to create the tilted card. Generate or source the documentary photograph first, then apply the card treatment locally. This keeps the tilt, shadow, and margins consistent.

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py source.png processed_report_event.png
python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py source_folder processed_folder
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

### Decision category pictures

Use an appropriate category picture or allowed category presentation for the mechanic.
Read the complete requirements in [Decision category pictures](references/icon-and-ui-families.md#decision-category-pictures) before this work.

### Flags

Flags should use clean symbolic designs that look like intentional flag designs, not simple-shape placeholders, palette swaps, ugly filters, or flipped/recolored variants. Treat flags as flat identity assets, not artwork or illustrated scenes.

Inspect the complete flat flag ladders in `flags/normal/`, `flags/medium/`, and `flags/small/` before creating or processing flags. Compare all three sizes together in `flags/contact_sheet.png`.

Keep the design readable across the required normal `82x52`, medium `41x26`, and small `10x7` ladder.

HOI4 flag TGAs must use the same origin/header convention as vanilla flags. Validate with `file`, completed flag TGAs should read as Targa image data at the correct size and must not end with `- top`. If a flag displays upside down in-game while the artwork looks correct in an image viewer, fix the TGA encoding/origin on the flag files themselves. Do not add custom UI sprites, scripted-localisation routing, DDS display copies, or other workarounds for flag orientation.

Use enough heraldic detail to prove that the design is authored rather than a basic-shape placeholder, while keeping the principal emblem readable at `10x7`. Prefer a layered civic, heraldic, industrial, botanical, maritime, or institutional emblem with a clear outer silhouette over an isolated circle, star, arrow, stripe, or geometric blob.

Avoid generated text unless the design absolutely requires it and the final output is manually checked.

Always use `$imagegen` for every new flag, including historically attested and real-world designs. Historical research still comes first: save and cite a reliable design reference, then use it as an image input and strict design constraint for imagegen. The generated result must be a clean, flat flag reconstruction, not an illustration of a flag. Reject waving fabric, folds, flagpoles, skies, lighting, gradients, painterly texture, vignettes, fake lettering, invented seals, perspective, shadows, or any scene around the flag. Manually compare geometry, colour fields, symbol count, symbol orientation, and heraldic details with the cited reference before resizing it. Imagegen is not permission to reinterpret a documented historical design.

For existing countries that already have game-provided or repository-approved base flags, do not replace the no-suffix base flag as part of an ideology pass. Keep the base flag unchanged, or restore it from the approved prior asset if an asset pass damaged it, unless the user explicitly asks for that base flag to be redone or the country receives a deliberate focus/event/cosmetic-tag transformation. Ideology variants should be separate assets for `_communism`, `_democratic`, `_fascism`, and `_neutrality`, not mutations of the base flag with one small shape, a palette swap, a color filter, a vertical flip, or a copied emblem.

For focus-tree or event route flag changes, use explicit cosmetic tags or route-specific flag files and document the trigger/focus that changes the flag. Do not create default flag overrides or new base flags for vanilla-supported or already-existing countries just because they participate in an event.

Historical or historically grounded flags must use sourced motifs, documented heraldry, period symbols, or clearly explained alternate-history synthesis. If no directly attested flag exists, state that in the manifest and produce a historically grounded design from relevant motifs instead of inventing unrelated symbols.

Generated fictional or alternate-history flag variants must come from a separate `$imagegen` result for each visually distinct design and then be processed into final flag sizes. Preserve the generated emblem geometry, internal heraldic construction, and identifying details through export. Do not replace the generated design with local rectangles, circles, stars, arrows, traced silhouettes, or other programmatically drawn geometry. Do not use a solid-fill normalizer, aggressive palette quantizer, vector trace, or edge simplifier that reduces generated detail to primitive shapes. Mechanical cropping, colour management, edge cleanup, orientation correction, resizing, and TGA export are allowed, but they must not become the source of the design.

Keep the full ImageGen source master and create a comparison sheet containing that master plus the normal, medium, and small exports. Reject a flag when its normal export no longer contains the distinctive generated emblem or when its small export reads as an accidental blob. The flat-design restrictions apply to both source and exports.

Before marking any flag complete, verify normal, medium, and small TGA files:

- correct dimensions across the required size ladder
- correct visual orientation in a contact sheet
- TGA origin/header convention consistent with vanilla HOI4 flags, `file` output must not show `- top`
- no byte-identical ideology variants unless the design is intentionally shared and documented
- no upside-down copies
- no accidental no-suffix base-flag replacement for countries that were only meant to receive ideology variants

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

Treat every unit visual as a domain-and-surface-specific pipeline. Inspect the matching catalog entries, contact sheet, and owning vanilla definition before deciding what the task needs.

- `units/equipment/technology_art/` contains flat 2D equipment illustrations used by equipment and technology sprites. Native canvases vary; follow the owning `interface/*.gfx` sprite.
- `units/land/counters_large/` contains large frame-aware land-unit strips. Preserve the cataloged `noOfFrames`, frame order, per-frame footprint, and transparent bounds.
- `units/land/map_counters/` contains land map-counter art. It is not a large division-designer strip.
- `units/land/division_template_emblems/` contains division-template identity emblems. It is not equipment art or map-counter art.
- `units/air/map_counters/` and `units/naval/map_counters/` contain domain-specific map-counter art. Do not substitute land counters or resized equipment art.
- `units/models_3d/land_materials/`, `units/models_3d/air_materials/`, and `units/models_3d/naval_materials/` contain UV model materials paired with cataloged `.mesh`, `.asset`, and entity definitions. They are not 2D icons, finished renders, or concept sheets.

Classify the requested deliverable before creating art: equipment/technology illustration, large land counter, land/air/naval map counter, division-template emblem, or land/air/naval 3D model package. Give each class its own brief, source art, native canvas or UV layout, frame metadata, final path, and handoff. A 3D task must keep model geometry, materials, entity wiring, and any separately produced concept reference distinct. Do not derive one unit pipeline by resizing, relabeling, or recoloring another.

#### 2D icon and counter generation contract

Custom unit, template, and facility icons require original art, exact consumer and vanilla-reference inspection, native canvas and frame semantics, and parent visual review.
Read the complete requirements in [2D icon and counter generation contract](references/icon-and-ui-families.md#2d-icon-and-counter-generation-contract) before this work.

#### 3D model package handoff

Route model production to [chaos-redux-3d-model-pipeline](../chaos-redux-3d-model-pipeline/SKILL.md) and `chaosx_3d_model_pipeline`; read its route selection, intake, and evidence/handoff requirements before briefing or accepting a model package. The 3D skill owns provider/dependency gates, source-image preparation, separate body/item generation, supported rig/action attempts, Blender assembly/fallback, geometry, materials, weights, contacts, and export/reimport. Do not duplicate those procedures in a 2D art brief.

The brief and returned package must identify the profile, requested operation, deterministic job root, source/provider lineage, exact vanilla mesh/entity precedent, source height, entity scale and effective runtime height, axes/origin/contact plane, required actions and root-motion policy, PDX channels and dimensions, `.mesh`/`.anim` outputs, reimport evidence, and exact runtime consumer. For humanoids, use measured installed vanilla infantry geometry and apply entity scale once, never an assumed real-world height. Require all components and real articulated motion; unavailable production capabilities prevent the affected output, while unavailable review tools limit the claims made about it.

For every firing state, require the action → discharge frame/time → verified muzzle/weapon locator → particle/beam/muzzle effect and applicable light → licensed weapon-matched soundeffect → source/license → entity consumer → evidence crosswalk. Attack, defend, support_attack, and other firing states are independent consumers. Silent or particleless firing and unrelated weapon-family substitutes are incomplete. A declared non-firing armed action receives no firing effects merely because it carries a weapon.

Model textures follow the 3D skill's shared `.tools/3d_pipeline/textures/` BC1/BC3 full-mip contract, active `.gfx` overrides, and hash-bound UV/material masks, not the uncompressed 2D DDS recipe below. Unit audio uses `.tools/3d_pipeline/audio/master.py` with source/derivative attribution and hashes. Decoded bytes or a geometry-only reimport do not establish rendered materials, deformation, audio playback, or live-game behavior.

The 3D worker owns sources, checkpoints, textures, previews, exports, manifests, model/audio evidence, and the mandatory bounded counter handoff to `chaosx_icon_artist`; this asset skill owns final counter art. Equipment illustrations, division emblems, and frame sheets remain separate surfaces. The parent owns final `.asset`, entity, `.gfx`, particles, sound definitions, unit/building/gameplay wiring, selected-source runtime synchronization, and final evidence review. The user performs live-game validation; do not request or await it to finish the package.

## Processing and installation

### DDS conversion

Final 2D PNG assets must be converted to DDS using the repository's standard 2D DDS conversion workflow. Model textures follow the separate compressed full-mip contract in [3D model package handoff](#3d-model-package-handoff). The converter lives only at `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`; `.tools/convert_to_dds.py` is obsolete, and active skills, agents, scripts, and handoffs must not restore or call it.

For these 2D assets, the output must be compatible with Chaos Redux's expected 32-bit BGRA or B8G8R8A8-style DDS workflow.

Run the bundled converter from the mod root:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <processed.png> --output <final.dds> [--width <pixels> --height <pixels>]
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

Every active event asset workspace must include a markdown manifest.

Recommended path while work is active:

```text
docs/assets/<event_id>_<event_slug>/manifest.md
```

The manifest must list every asset. Before deleting the temporary workspace, copy any durable provenance, licensing, attribution, coverage, review, and exception facts needed by the event documentation or audit handoff into a permanent documentation surface.

Each asset entry must identify:

- Asset name/type, event id/slug, intended in-game use, exact target size, related focus/idea/event/decision/UI/super-event id, and localisation key where relevant.
- Source mode (`$imagegen`, portrait-production output, internet source, or user-provided source); generated prompt and rationale, or source link, available author/archive/collection, date/range, license/public-domain status, era fit, and uncertainty.
- Background mode (`native_transparent`, `consumer_opaque`, or `fallback_removed`), with the fallback reason, verified edit/tool and settings where applicable.
- Source and processed PNG paths, final DDS path, sprite name, owning `.gfx`, notes, and status.
- Generated candidate lineage and review evidence under [Candidate lineage and review](#candidate-lineage-and-review), including input roles, exact edit deltas, immutable source/intermediate paths, verdicts, and explicit final selection.
- For animation: frame count/timing, loop, anchor, static fallback, sheet or frame-sequence paths, and each frame's source mode and source note.
- For real-person portraits: durable source path/attribution, exact crop evidence, source-placeholder wiring when selected, provider-backed styled final only when explicitly requested and available, role references, review evidence, and exact runtime DDS basename/path. Record the independent reviewer's identity/date, proof they are not the producer, separate likeness/style/framing/provenance verdicts, and gate state.
- For portrait ownership: search terms, roots/files/ids checked, matched owner/consumer or explicit no-match evidence, disposition, and guarded transfer/availability contract where applicable.
- Selected portrait mode/state: `source_placeholder` (accepted unchanged source/crop runtime, explicitly pending HOI4-style replacement), `replacement_pending` (only while an explicit styled-final request remains outstanding), `styled_final` (validated provider-backed output), `not_needed`, or `blocked`.

Use `not_needed`, `planned`, `sourced`, `generated`, `processed`, `converted`, `handed_off`, `wired`, `complete`, `needs_user_review`, or `blocked` as asset statuses.

#### Candidate lineage and review

Before each native ImageGen generation or edit, save the exact request arguments in a repo-contained prompt record: `prompt`, `transparent_background`, and supplied reference paths or recent-image count, with the actual referenced images identified and retained.

While the asset workspace is active, keep the original generated source and every accepted intermediate immutable at distinct versioned paths. Keep source outputs separate from processed previews and runtime files. In the active manifest or linked prompt record, record for each generated candidate:

- candidate id, parent candidate id or new-generation reason, and input paths with their declared roles
- linked exact saved request, focused edit delta, invariants, and background mode
- tool-reported output path, retained workspace path, source SHA-256, decoded dimensions, and alpha evidence
- source-resolution and final-native-size review results, accepted/rejected status, and remaining defects
- explicit final-selected candidate id, processed PNG path, final runtime path after conversion, and each subject's source-to-layer/frame-to-consumer mapping

Before runtime promotion, review every newly generated or edited subject against its actual source and saved request; a correct-looking preview does not establish ImageGen lineage.
Deterministic template/frame geometry and processing remain allowed under the applicable family contract, but cannot replace generated subject art.
If an exact historical request is unavailable, mark it unavailable and preserve known source paths/hashes rather than reconstructing it; fresh generation or editing must remain within existing authorization and portrait/source-mode, provider, and fallback boundaries.

Do not silently overwrite a prior accepted candidate or synchronize an older candidate into runtime. Before normal temporary-workspace cleanup, promote the lineage, prompts, final selection, and review facts into permanent documentation under the existing cleanup contract. Retain active image files until the required package review is complete; this rule does not create a second permanent asset archive.

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

For the small-icon and counter contract, the sheet must also show the native-alpha ImageGen source, processed transparency, enlarged smooth preview, and decoded DDS round-trip with dimensions, frame labels, and visible-bounds notes. If fallback removal was used, include the untouched opaque source and repaired edge comparison.

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
