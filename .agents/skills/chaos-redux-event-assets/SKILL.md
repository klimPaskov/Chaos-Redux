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

Flags are a flat graphic-design pipeline, not event artwork. Historical flag research establishes the documented geometry, colours, and symbols, ImageGen still produces the final clean flat design under [Flags](#flags).

For animated work, route by asset type first. Then require the chosen asset subagent to follow `chaos-redux-frame-animation` for frame plans, per-frame source art, normalization, contact sheets, preview GIFs, frame sheets, static fallbacks, and animation handoffs.

Asset subagents may create sources, processed PNG previews, final DDS files, contact sheets, manifests, durable portrait masters under `docs/assets/portraits/`, and `docs/assets/<event_id>_<event_slug>/gfx_handoff.md`.

Asset subagents must not edit `.gfx`, localisation, GUI, event, focus, idea, decision, scripted effect, scripted trigger, on_action, history, country, or spreadsheet files unless the parent explicitly grants that scope. The portrait worker has a standing narrow exception for portrait-specific `.gfx` entries and existing character portrait references.

The main agent owns final non-portrait `.gfx` sprite definitions, gameplay references, docs alignment, spreadsheet alignment, and validation. The portrait worker owns portrait-specific `.gfx` and existing character portrait references. When an asset change requires catalog alignment, update only the authoritative XLSX and run `python .tools/export_event_catalog_csv.py`, the three CSV files are export-only and must not be edited directly.

A good parent prompt to an asset subagent includes the event id, asset list, asset type, target size, source mode, final DDS folder, sprite name if already registered, reference folder, visual direction, source constraints, and anything the subagent must mark blocked instead of substituting.

For one-person country-leader or officeholder portraits, the parent prompt must state the polity's identity classification and why the source mode passes the fail-closed [Portrait source-mode gate](#portrait-source-mode-gate).

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

#### Durable portrait source archive

`chaosx_portrait_creator` owns one durable source package for every grounded portrait and archives it without changing runtime identity. Select the mode in the brief or manifest: `source_placeholder` keeps the unchanged source/crop, deterministic `156x210` PNG, DDS, and wiring. `styled_final` is an optional provider branch that starts only after the user explicitly requests it and supplies the result. Never silently repaint, replace, or overwrite provenance.

Store each package together under `docs/assets/portraits/<event_id>_<event_slug>/` (a subject subfolder is allowed), using the exact runtime basename:

```text
<subject>/
  <runtime_portrait_basename>_original.<original_suffix> # untouched original bytes
  <runtime_portrait_basename>_source_crop.png         # lossless crop, before resize/DDS
  <runtime_portrait_basename>_source_crop.json         # exact crop/equality evidence
  <runtime_portrait_basename>_156x210.png              # deterministic processed candidate
  <runtime_portrait_basename>.txt                     # co-located provenance contract
<runtime_portrait_path>/<runtime_portrait_basename>.dds
```

The original source, lossless crop, processed PNG, JSON, and `.txt` contract are mandatory and must never be split across folders. The contract records subject, source URL/attribution/license, crop coordinates, mode/state, reviewer/date, and separate identity/framing/provenance verdicts. Preserve original-format bytes and a lossless PNG copy when needed. The archive is evidence only: no `.gfx`, character, GUI, event, focus, idea, or decision may reference `docs/assets/portraits/`, and cleanup of temporary event workspaces must not delete it.

## Sources and references

### Reference asset examples

This skill owns its visual-reference library under:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets`

`assets/vanilla_reference/` is the canonical semantic library, with Vanilla HOI4 as the primary source and explicitly marked Chaos Redux examples where needed. Do not route reference work through project-root asset folders or another skill-local copy.

Start with:

- library rules and contact sheets: `assets/vanilla_reference/README.md`
- exact source provenance and dimensions: `assets/vanilla_reference/CATALOG.md`

Unless a path below begins with `assets/`, interpret it relative to `assets/vanilla_reference/`, except the `scripted_guis/` layout paths, which are relative to the skill-local `assets/` root.

Every semantic reference directory contains its own `contact_sheet.png`, there is no shared `contact_sheets/` directory. Contact sheets are labeled with filenames and native dimensions, and are review aids rather than reference examples themselves. Common icon families (focus, ideas, decisions, decision categories, technologies, and achievement states) have at least 15 references, while other tracked texture and icon families have at least 5. The interface library covers complex vanilla scripted GUIs and other native interfaces, with meaningful functional compositions for each distinct layout family. Crop MCP renders to useful UI bounds; full-window images dominated by empty space are unsuitable reference examples. Retain full-render source, source window/files, original resolution and UI scale, and crop bounds in provenance so each crop can be traced back to its native layout.

#### Canonical portrait paths

- country leaders: `assets/vanilla_reference/portraits/leaders/`
- army and navy commanders: `assets/vanilla_reference/portraits/commanders/`
- operatives: `assets/vanilla_reference/portraits/operatives/`
- advisors and high-command dossier cards: `assets/vanilla_reference/portraits/advisors/`

The leader reference shelf at `assets/vanilla_reference/portraits/leaders/` is the direct portrait folder for agents that need one, it holds byte-aligned copies of the curated leader references from `assets/vanilla_reference/portraits/`, and it uses `vanilla_reference/REFERENCE_MANIFEST.md` for the current file list. Do not wire any reference shelf into runtime GFX, and do not infer advisor assets from it. Country leaders, commanders, and operatives are full `156x210` portrait textures. For portrait work, inspect the canonical role-specific contact sheet. Advisor and high-command dossier references are native `65x67` cards and use their own canonical contact sheet, do not substitute full leader, commander, or operative portraits for this family.

#### Canonical flag and event-art paths

- flat flags: `flags/normal/`, `flags/medium/`, and `flags/small/`
- report-event art: `event_art/report/`
- news-event art: `event_art/news/`
- super-event art: `event_art/super_event/`

#### Canonical interface layout paths

- pressure meters: `scripted_guis/meters_and_pressure/`
- institutional boards: `scripted_guis/institutional_boards/`
- faction relations: `scripted_guis/faction_relations/`
- regional investment: `scripted_guis/regional_investment/`
- campaign progress: `scripted_guis/campaign_progress/`
- escalation status: `scripted_guis/escalation_status/`

Read `interface/README.md`, inspect the root and category contact sheets, then inspect the paired installed vanilla `.gui` and `common/scripted_guis` sources before creating a scripted GUI reference. These MCP-derived functional crops provide native layout precedents; they do not replace the new or redesigned window's required Sunburst compositional reference.

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

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference\icons\decision_categories\pictures`

This family contains the larger visual pictures used to establish a decision category's theme or territorial context. It is separate from the small category icon family at `icons/decision_categories/`.

The current reference examples use a native `114x101` canvas. Treat that size as the reference-family canvas, not as a universal runtime assumption. Inspect the active vanilla or Chaos Redux sprite and GUI consumer before choosing the final runtime size.

The picture folder must contain its own `contact_sheet.png`. If the contact sheet is missing, create it before new category-picture work. Label every reference with its filename and native dimensions, record each source as Vanilla, Chaos Redux, or user-provided reference material in `CATALOG.md`, and update the reference library README when the family or workflow changes. The reference images and contact sheet are review-only assets. Never wire, recolour, trace, or ship them as runtime art.

After placing a technology or doctrine icon, use the read-only `mcp__hoi4_agent_tools__hoi4_tech_inspect` in `explain` or `lint` mode to verify the sprite and texture references, then use the `assets` or affected folder view in `mcp__hoi4_agent_tools__hoi4_tech_render` for deterministic review. MCP use is mandatory for this surface. Tool exposure does not establish service health or standalone Technology Tree Viewer installation. Record an unavailable route as a blocker and an absent standalone viewer as a package gap. Missing or ambiguous assets remain implementation findings. This skill still owns source art, processing, DDS conversion, placement, manifests, and sprite handoff.

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

Do not add new reference images outside the skill-local `assets/` root. Add semantic references under `assets/vanilla_reference/` with exact provenance, dimensions, and contact-sheet coverage recorded in its catalog. The `assets/vanilla_reference/portraits/leaders/` shelf is the direct-reference portrait folder: it holds only byte-aligned copies of the curated leader references, and it is never a separate source of truth or a runtime asset folder.

Before generating, sourcing, processing, or wiring an asset, read the library rules, inspect the matching category and contact sheet, and follow the vanilla source path in the catalog to its owning `.gfx`, `.gui`, `.asset`, or `.mesh` definition when engine behavior matters. Reference PNGs are never final assets: do not wire, recolor, trace, or ship them. If no category matches, inspect the closest canonical category plus a direct vanilla or established Chaos Redux precedent before choosing a style.

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
- never use text-only generation, a name, a description, or a substitute face to fabricate a real person's likeness, use [Country-leader, commander, operative, and named-officeholder portraits](#country-leader-commander-operative-and-named-officeholder-portraits) for grounded portraits

Follow the repository web research rules from `AGENTS.md` when searching for source images.

For internet-sourced event photo assets that are meant to represent the World War II era, search for period-matching source imagery from roughly 1936 to 1945 unless the event spec gives a narrower date range. Prefer contemporary photographs, war correspondents' photographs, press agency images, propaganda posters, maps, newspapers, official records, government or military archive images, museum scans, library scans, and period illustrations. Do not use modern photographs, reenactment images, film stills, AI-looking reconstructions, postwar uniforms, streets, weapons, vehicles, buildings, colorized tourist photos, reenactments, or modern props when they do not fit the era. If no suitable period source can be found, either generate a period-authentic fictional/documentary image when the asset does not require a real source, or mark the asset as blocked or `needs_user_review`.

Record the image source, source link, author or archive if available, license or public domain status if available, estimated date or date range, why the image fits the World War II era, and any uncertainty in the manifest.

#### Portrait source-mode gate

Classify every country-leader, commander, operative, named officeholder, or institutional portrait before routing. A grounded identity (`grounded_source_only`) is any real, partly real, restored, separatist, regional, indigenous, dynastic, or otherwise plausibly historical polity/community/institution. It requires `chaosx_portrait_creator` and attributed real-person or authentic institutional source material. If no defensible source exists, mark `blocked` and never invent a grounded face. A generated one-person portrait is allowed only for a truly fictional high-chaos country or impossible/supernatural entity, and must have an extraordinary internally coherent invented motif rather than a generic face, modern prop, meme, gore, mockery, stereotype, or caricature. Record classification, source mode, evidence, and blocked decisions. Missing or contradictory classification fails closed.

#### Portrait subject ownership gate

Before sourcing or wiring a real-person token, search installed vanilla and the project for exact/variant names, transliterations, titles, and name order across `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/`. A person already defined, recruited, or portrait-owned by a live roster cannot be cloned. Reuse requires an explicit guarded transfer that invalidates origin ownership before target ownership and prevents simultaneous ownership. Otherwise fail closed. Incidental prose, ship names, streets, and equipment are not ownership. Record search terms, roots/ids, matches or no-match evidence, disposition, and any transfer guard in the manifest/handoff. This gate never authorizes a generated grounded person.

#### Fictional portraits

Fictional or impossible portraits use native ImageGen through `chaosx_portrait_creator`, never the grounded replacement branch. One-person leaders require `fictional_high_chaos`, full `156x210` HOI4 framing, a memorable invented motif, matching role/gender/name metadata, and no text, watermark, modern UI, meme, gore, stereotype, or caricature. Institutional briefs use an institutional name and may be people-free. A staged group requires explicit authorization and matching constraints. Grounded institutions still require authentic sourced material, and a named person uses one-person rules.

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

For a coordinated asset family, an accepted candidate may anchor only the stated palette, materials, texture, or motif vocabulary; the exact consumer family remains authoritative. Follow [Icon type separation rules](#icon-type-separation-rules) for independent surface art and [Achievement icons](#achievement-icons) for deterministic template composition and state derivation.

#### Native transparency and background-removal fallback

Apply native transparency to icons, counters, emblems, overlays, decorative UI pieces, transparent animation frames, and every family whose inspected consumer leaves unused canvas transparent. Full-canvas scenes, flags, portraits, and painted panels retain the background required by their consumer and reference family. Do not generate an alpha-backed asset on an opaque or chroma background as the normal route. Request a real transparent background in the first built-in ImageGen call, retain that native-alpha source PNG, and preserve its alpha through crop, alignment, resizing, frame assembly, and DDS conversion.

Validate native transparency before processing: unused corners and padding must contain real zero-alpha pixels, the painted subject must retain nonzero alpha and complete edges, and the image must contain no fake checkerboard, matte, halo, key colour, or unintended transparent holes.

Background removal remains a fallback for either of these cases:

- the built-in ImageGen result ignored the transparency request or failed alpha validation
- an inherited, internet-sourced, or user-provided image has an unwanted opaque backdrop and the accepted asset type requires transparency

First use a targeted built-in ImageGen edit that changes only the background to real transparency and preserves the subject, silhouette, colours, internal opacity, framing, and edge detail. If that still fails, use a deterministic local background-removal or chroma-key process only when its tool is actually installed and verified in the current environment. Preserve the untouched source, record the tool and settings, inspect for spill and clipped edges, and compare the repaired candidate with the source. If no verified fallback tool exists or removal damages the subject, mark the asset `blocked` or `needs_user_review`. Do not invent a helper path or silently ship an opaque square.

#### Review each iteration

Inspect every iteration at full source resolution and the final HOI4 native size before accepting it. Check subject and reference fidelity, silhouette, footprint, clipping, unintended additions, and small-size readability; reject fine detail that becomes noise after downsampling. Decode alpha rather than trusting a checkerboard preview: verify transparent unused pixels, intact intended opaque interior, edge continuity, and no matte, halo, colour fringe, or unintended holes. Compare each edit with its accepted parent and original anchor so accumulated drift is visible. Keep the existing contact-sheet, DDS round-trip, frame continuity, independent portrait review, and parent promotion requirements from the owner skills.

## Asset-family contracts

### Icon creation rules

Use a centered silhouette, strong value contrast, and one clear subject readable at native size; avoid interior detail that disappears at 45x45 or 64x64. For variable UI backgrounds, use a slight dark/black outline and subtle drop shadow, with no chroma rim, white outline, glow, sticker border, or oversized medallion fill. Apply the shared transparency and focused-edit rules and inspect on contrasting solid and checker backgrounds. Keep visible ImageGen source evidence, prompt/background mode, processed alpha, and the contact-sheet evidence below; a primitive drawing or resized unrelated icon cannot pass.

### Icon type separation rules

Focus, idea, national-spirit, officer-corps, decision, mission, decision-category, achievement, technology, special-project, balance-of-power, intelligence-agency, intelligence-operation, commander-trait, medal, military-raid, state-modifier, MIO, faction, building, and modifier icons are separate asset types.

Do not create focus icons first and then satisfy idea icons or decision icons by resizing, cropping, shrinking, recoloring, padding, or lightly editing the focus icon. This is not a valid asset workflow.

Each icon type must have its own asset-type-specific brief, reference inspection, source artwork, prompt or source choice, crop, target size, filename prefix, manifest entry, and final DDS output.

Shared visual themes are allowed only when every icon is still designed for its own in-game use:

- focus icons should read as full HOI4 focus art at 94x86 with focus-tree style detail and composition
- idea and national spirit icons should read as compact 64x64 symbolic spirit art without borrowing the full focus icon frame
- decision icons should read clearly at 32x32 with simpler shapes, stronger silhouettes, and less interior detail
- decision category icons should be designed for the category button or scripted GUI surface, not derived from a focus icon
- officer corps spirit icons should follow the vanilla officer corps spirit look and 45x45 transparent style
- achievement icons should follow achievement presentation rules and variant rules
- intelligence-agency and intelligence-operation icons must follow their own agency or operation UI precedent rather than a generic decision treatment
- commander traits, medals, military raids, state modifiers, MIOs, factions, buildings, and modifier icons must follow the matching canonical folder and owning vanilla definition, do not force these families onto a blanket 32x32 or 64x64 canvas
- frame strips, indexed building sprites, and multi-state modifier art must retain their frame order and frame count rather than being treated as a single standalone icon

If a mechanic needs matching focus, idea, and decision visuals, build them as a coordinated icon family. A coordinated family can share subjects, symbols, colors, and lore cues, but each member still needs separate source art or a separate generated output designed for its target size and UI role.

The manifest must record the exact asset type for every icon and should note when icons are part of a coordinated family. Do not mark an icon complete if it only exists as a resized version of another icon type.

### Idea and national spirit icons

Use compact HOI4 symbolic art with aged texture, strong contrast, a clear silhouette, and readable meaning at `64x64`, usually without a full focus frame. Use `idea_` and inspect `icons/ideas/` plus its catalog row. Apply the shared generation, text, transparency, and separate-source rules; a user-provided or specifically requested source takes precedence.

### Focus icons

Use HOI4 focus art with a strong central symbol, clear silhouette, aged texture, painterly detail, and readable contrast tied to the focus tree story, ideology, or gameplay purpose; avoid generic thumbnails. Use `goal_` and nominal `94x86`, inspecting `icons/national_focus/`, its catalog row, and the owning sprite/current vanilla precedent before selecting the actual canvas. Apply the shared generation, text, transparency, and separate-source rules; a user-provided or specifically requested source takes precedence.

### Decision icons

Compose decision icons for `32x32` readability with simple central symbols, strong contrast, and limited interior detail. Use `decision_` or `decision_category_` for category icons, and inspect `icons/decisions/`, `icons/missions/`, or `icons/decision_categories/` with the owning consumer. Missions use the decision pipeline with mission-specific semantic readability. Apply the shared generation, text, transparency, and separate-source rules; a user-provided or specifically requested source takes precedence.

### Additional gameplay icon families

Route additional icon work by the exact UI surface:

- intelligence identity and action: `icons/intelligence_agency/` and `icons/intelligence_operations/`
- commander progression and honours: `icons/commander_traits/` and `icons/medals/`
- operations and world state: `icons/military_raids/` and `icons/state_modifiers/`
- organizations and map/economy identity: `icons/military_industrial_organizations/`, `icons/factions/`, and `icons/buildings/`
- generic or text-linked modifier presentation: `icons/modifiers/`

Read the matching canonical catalog entries and inspect the owning `.gfx`, `.gui`, or database definition before choosing canvas, frame layout, transparency, or filename. These families are not reskinned decision or idea icons. When a source is a strip or contains several UI states, preserve its frame semantics and document them in the manifest and handoff.

### Achievement icons

Achievement icons should be compact and readable at 64x64.

Inspect `assets/vanilla_reference/icons/achievements/contact_sheet.png` and the matching individual references before creating an achievement icon. The contact sheet and reference examples are review material, while the `template/` folder below is a separate workflow-input folder excluded from the achievement reference count.

#### Supplied templates

Use these exact supplied workflow inputs and do not invent, rename, move, resize, crop, trim, recolor, redraw, filter, or replace them:

```text
assets/vanilla_reference/icons/achievements/template/achievement_template.png
assets/vanilla_reference/icons/achievements/template/achievement_template_grey.png
assets/vanilla_reference/icons/achievements/template/overlay.png
```

`achievement_template.png` is the completed-state background, `achievement_template_grey.png` is the grey and not-eligible background, and `overlay.png` is the unchanged red-cross not-eligible overlay. The supplied files are 64x64 workflow inputs. Verify their integrity against SHA-256 `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA`, `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`, and `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD` respectively.

#### New achievement creation

For each new achievement, use `$imagegen` to design one original subject on a genuinely transparent background with the inspected achievement references guiding framing, density, contrast, and readability. Request no achievement frame, square background, red cross, text, or fake checkerboard. Process the result into one centered 64x64 color subject layer, retain the native ImageGen source PNG, prompt, and processed PNG, and do not independently generate three state artworks or borrow another icon type.

Build the three complete source layers deterministically from the one processed color subject, preserving the 64x64 canvas, exact position, and alpha alignment:

1. Completed source: the processed transparent color subject unchanged.
2. Grey source: a deterministic grayscale conversion of that same subject, with its canvas, alignment, and alpha preserved.
3. Not-eligible source: the deterministic grey source with the unchanged `template/overlay.png` composited on top at the exact 64x64 alignment.

Do not derive a new not-eligible source from a completed or runtime grey output, or recolor or resize the red cross.

#### Existing-triplet migration

For an existing achievement, provide the complete `<achievement_id>.{png,dds}`, `<achievement_id>_grey.{png,dds}`, and `<achievement_id>_not_eligible.{png,dds}` source triplet to the processor. Migration preserves each supplied state layer at its native 64x64 canvas and exact position without resizing, cropping, alpha-trimming, grayscale conversion, recoloring, redrawing, filtering, or other preprocessing. It never derives a missing not-eligible state from grey plus the overlay and never replaces a supplied not-eligible layer.

#### Shared processing and validation

Use `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py` for both modes. Supply all three complete source layers; directory mode collects the base, `_grey`, and `_not_eligible` triplet, and a single file is never valid input. Each decoded PNG or DDS state must be exactly 64x64. The processor fails closed on a missing state, a wrong canvas, an already-applied outer template border, or an existing output without `--force`.

Apply `template/achievement_template.png` beneath the completed source and `template/achievement_template_grey.png` beneath both grey and not-eligible sources. Normal alpha compositing is the only pixel interaction. Every final state must pass the strict one-level 64x64 legacy BGRA checks in [DDS conversion](#dds-conversion), with decoded pixels exactly equal to its supplied background beneath its exact decoded source layer. All three runtime states are required; source-decoding tolerance never weakens final validation.

Decode DDS sources with the strict canonical BGRA parser first, then the Pillow fallback for compressed, mipped, noncanonical, or truncated current inputs, enabling `ImageFile.LOAD_TRUNCATED_IMAGES = True` only during that source decode.

Keep source triplets separate from processed outputs and never feed generated outputs back as source layers unless replacement is explicitly intended. Use `--in-place --force` only for an intentional replacement beside the sources, and `--allow-templated-sources` only for an intentional reprocessing exception. Default backgrounds resolve from the supplied `template/` folder above.

Run it from the mod root with an explicit separate output directory:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py `
    --input <source_triplet_directory> `
    --achievement-id <achievement_id> `
    --output-dir <staging_or_runtime_gfx_achievements> `
    --write-png
```

For an explicit one-triplet pass, provide `--completed <completed.png|completed.dds> --grey <grey.png|grey.dds> --not-eligible <not_eligible.png|not_eligible.dds> --achievement-id <achievement_id> --output-dir <separate_output_directory>`. Use `--dry-run` to decode and validate complete source triplets without writing, or `--audit --input <source_triplet_directory> --output-dir <output_directory>` to recompute and validate existing triplets. The processor writes optional review PNGs below `output-dir/review/` and final DDS files directly below `output-dir`.

#### Runtime placement and handoff

Use an `achievement_` prefix for source or intermediate art when it helps distinguish the asset type.

For Chaos Redux final files, achievements are a root-only exception. Put completed, grey, and not-eligible DDS files directly under `gfx/achievements/`, and name them after the exact achievement id registered in `common/achievements/`:

```text
gfx/achievements/<achievement_id>.dds
gfx/achievements/<achievement_id>_grey.dds
gfx/achievements/<achievement_id>_not_eligible.dds
```

When renaming or adding achievement ids, update `common/achievements/`, `localisation/english/chaosx_achievements_l_english.yml`, `interface/chaosx_achievements.gfx`, the three DDS variants in `gfx/achievements/`, and any docs or manifests that list the final DDS paths. If the achievement registry owns a single `unique_id`, keep it as one root-level registry file and group event-owned achievements by event section inside the file instead of splitting it into per-event achievement files.

Retain the complete source triplet: for new art, the original color subject, deterministic grey source, and not-eligible source with the unchanged overlay; for migration, the exact supplied state layers. Keep the generated master/prompt where applicable, all three composited review PNGs, a native-size contact sheet, strict DDS decode and pixel-equality evidence, and final root-only DDS paths. Review PNG export is optional at processor level; the package handoff still retains the required reviews.

Identify the exact achievement id, all three runtime DDS paths, any registered sprite aliases, source/processed paths, and any `needs_user_review` or `blocked` state. The parent must review the contact sheet before wiring or completion.

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

If a super-event needs an audio cue, use `chaos-redux-super-events` and research a suitable public domain or clearly licensed recording. Register the final cue as sound from the event-scoped `sound/<event_id>_<event_slug>/` folder. Never create event or super-event audio from generated test tones, primitive waveforms, beeps, noise beds, or local oscillator output, that includes sine, square, triangle, and sawtooth waveforms.

Document each track's title, composer, performer or recording source where relevant, checked license or public-domain status, source link, thematic fit, suggested in-game use, and editing notes. Do not claim public-domain status without checking; mark an unclear license uncertain or unsuitable.

### Decision category pictures

A decision category picture is a larger visual surface used inside or beside a decision category. It is not a `32x32` decision icon, a small category icon, a custom-window background, or a substitute for an interactive scripted GUI.

#### Eligibility before production

Use a static or animated category picture only for a simple category with a description, an ordinary decision list, and at most basic formatted value tables.
Ordinary decision-list action buttons and basic formatted value tables are allowed; additional category GUI buttons or controls are not.
Do not add a picture to a category that already has complex UI, meters, additional custom buttons or controls, rich interactive panels, or other animations.
An animated category picture itself is supported when this same gate passes, but it must not accompany existing animated GUI.

Within this gate, a category picture may provide strong identity, historical context, propaganda, territorial orientation, or a readable theme while the normal decision list carries the gameplay actions.
Those themes alone do not override eligibility or require a picture.

#### Subjects, sources, and production

Suitable subjects include:

- propaganda posters and public campaigns
- civil-war mobilization, insurgency, and preparedness
- elections, ideology, monarchy, party control, and trade-union politics
- faction management, treaties, naval agreements, and foreign intervention
- formable territory maps
- national symbols, institutions, aerial views, documentary scenes, and period objects

Choose the source route by content:

- use `chaosx_asset_source_researcher` for real propaganda posters, real photographs, archival maps, real documents, and other verifiable historical material
- use `chaosx_generated_event_art` for fictional or alternate-history posters, symbolic category pictures, generated documentary scenes, and non-icon illustrated panels
- use deterministic map data and exact state geometry for formable territory pictures and state-puzzle pieces. Do not ask ImageGen to invent state borders

Generated category pictures must not contain fake interface controls, fake meters, fake buttons, unreadable generated text, modern UI, or decoration that implies a click action. Sourced posters may retain real source text when it is legible and appropriate, but provenance and cropping must remain documented.

A static picture is the normal choice after the eligibility gate passes. Use an animated picture only within that same gate and when motion communicates a changing state or supports an active propaganda, mobilization, crisis, or transformation theme. Animated pictures follow `chaos-redux-frame-animation` and require real source frames, a static fallback, a sheet, preview, manifest, and sprite handoff.

Before production, inspect:

`assets/vanilla_reference/icons/decision_categories/pictures/contact_sheet.png`

Also inspect the exact active consumer to confirm canvas, crop, alpha, frame behavior, and runtime path. The reference family uses `114x101`, but the consumer decides the final target.

The asset manifest and handoff must state whether the output is:

- small category icon
- static category picture
- animated category picture
- compact scripted GUI display
- full mechanic-window asset

Do not let one asset satisfy several of these surfaces by resizing or relabeling it.

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

`chaosx_portrait_creator` owns every portrait from source/brief through runtime handoff. Grounded portraits use an attributed unchanged source and the selected `source_placeholder` or explicitly requested `styled_final` mode. Fictional/impossible portraits use native ImageGen. Automated checks never replace independent visual review. Never generate or reconstruct real-person identity: use an unchanged attributed archival photograph (male subject: archival male photograph), preferably public-domain or clearly licensed and period-compatible. Reject illustrations, statues, reenactors, actors, text descriptions, modern or era-incompatible images, and unverified crops; ffmpeg/ImageMagick cropping alone does not prove decoded-pixel equality. Female-presenting portraits require matching female metadata/name pools, male-presenting portraits matching male metadata/name pools, and councils/boards institutional names. A wired `source_placeholder` remains explicitly pending until the user supplies its HOI4-style replacement; selecting this mode does not complete the portrait.

Run the automatic source package tool from the mod root (or pass `--crop` for measured recovery):

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py `
	<archival_master.jpg> <subject_source_crop.png>
```

Automatic mode uses bundled YuNet to require exactly one face, computes a portrait-aspect head-and-shoulders crop, saves the untouched original, exact lossless crop, `156x210` RGB PNG, JSON equality/model/hash evidence, and a co-located provenance `.txt` contract under `docs/assets/portraits/<event_id>_<event_slug>/` (subject subfolders are allowed). Missing model/OpenCV support, zero/multiple faces, unsafe geometry, or write collisions fail closed. Use `--model` or an explicit `--crop` recovery. Both routes write the complete package. Manual JSON is labelled `manual_crop_override` and reports no face box or YuNet detection. The JSON must retain source/crop/processed dimensions, hashes, exact crop coordinates, equality result, and normalized command (plus detector evidence only for automatic mode). Never accept an alternate crop without equivalent decoded-pixel equality evidence.

Convert and wire a grounded portrait only after an independent audit PASS; a pending or failed identity gate is `needs_user_review` or `blocked`, never wired. Use the processed PNG as `source_placeholder` when selected. `replacement_pending` is allowed only after an explicit styled-final request remains outstanding. When supplied, the user-provided output goes to `chaosx_portrait_creator` for independent validation, DDS conversion, and replacement at the same runtime path. Never operate RunPod.

Before DDS conversion, keep the untouched original, lossless crop, processed PNG, JSON, and provenance contract together under the exact runtime basename. The archive never replaces source evidence and never becomes a runtime reference.

Choose the canonical reference family by role before starting:

- country leader: `portraits/leaders/`
- army or navy commander: `portraits/commanders/`
- operative: `portraits/operatives/`
- named officeholder: the canonical family owned by its consuming leader, commander, operative, advisor, or high-command surface

Use role-specific references as style controls only, never as a face source. Compare unchanged master, exact crop, deterministic candidate, any supplied provider output, runtime candidate, and references at native size and ≥4x nearest-neighbour.

Preserve facial geometry, asymmetry, age, expression, hair, pose, and source-visible clothing. Reject genericization, beautification, symmetrization, face substitution, invented detail, unsupported insignia, weak likeness, or filtered photos. Record source URL/attribution/license, crop coordinates, role references, comparison sheet, reviewer/date, separate likeness/framing/provenance verdicts, mode/state, DDS path, sprite, and gender/name-pool metadata. Missing evidence blocks the portrait.

Country-leader, commander, operative, and named-officeholder candidates are deterministic `156x210` portraits. Commander references remain full `156x210` even when displayed smaller. Advisor/high-command cards use [Advisor and high-command portrait icons](#advisor-and-high-command-portrait-icons)'s separate native `65x67` workflow after the shared identity gate. Operatives use the full pipeline and cataloged owning sprite.

Every portrait follows [references/portrait-production.md](references/portrait-production.md): the five-step portrait sequence, the grounded source-placeholder or explicitly requested provider-backed styled-final branch with its `replacement_pending` state, the fictional/impossible native ImageGen branch, and the separate no-advisor-icons authorization boundary in [Advisor and high-command portrait icons](#advisor-and-high-command-portrait-icons).

### Advisor and high-command portrait icons

Advisor, theorist, military-high-command, and officer-corps portrait icons are a separate asset type. Inspect `assets/vanilla_reference/portraits/advisors/` before work. The final target is native `65x67`, with a recognisable HOI4-styled head-and-shoulders portrait, a dark irregular dossier frame where the approved reference family uses one, and transparent outer corners. Do not infer this family from a character or small-portrait consumer, it must be present in the accepted requirement set.

Apply the fail-closed [Portrait source-mode gate](#portrait-source-mode-gate) to advisor and high-command subjects. For a fictional subject in the allowed class, `chaosx_portrait_creator` uses native ImageGen to create a distinct full-resolution portrait master. Never reuse a leader crop. For real people, complete the shared source and provenance gate before preparing the native card, [Country-leader, commander, operative, and named-officeholder portraits](#country-leader-commander-operative-and-named-officeholder-portraits) governs the portrait handoff and fallback. Institutional or collective briefs must state whether the result is people-free or includes a governing group, never imply that invented faces are sourced historical individuals.

Keep a repo-contained provenance manifest for every native card. Record the source mode, source and candidate dimensions, exact crop or composition notes, generation or editing inputs, attribution or ImageGen record, reviewer, date, and runtime path. Keep each source, processed PNG, review sheet, and metadata file in a distinct path, do not split out or bypass an individual source to weaken provenance.

Use `.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py` for native `65x67` advisor-template composition. Use the canonical `portraits/advisors/advisor_template.png` as one exact, untouched top layer rather than reconstructing its frame, paper, or shadows from separate elements. Load the complete approved source canvas without pre-cropping or pre-warping it. Measure the opening center, rotated width and height, and angle from the actual template. Canonical cards must use that exact opening-fill plane, match the angle within `0.05` degrees, and use a `0 0` center offset.

Never clip the portrait to the exact visible opening. The canonical frame contains translucent antialiased inner-edge pixels, so exact-opening clipping can leave those pixels without underlying portrait coverage and expose an alpha seam. The visible opening is the audit region, not the portrait's final mask boundary.

Use one uniform aspect-preserving cover scale with no anisotropic resize or stretching. Extend the measured opening-fill plane before cover fitting with the tool's centralized `UNDER_FRAME_BLEED_PIXELS` value, currently `2` px, and `PORTRAIT_EDGE_GUARD_PIXELS`, currently `1` px. The tool adds `2 * (bleed + guard)` to each opening dimension. Do not duplicate these values in event-specific or per-person instructions. Build the safe bleed mask by expanding the opening mask with the centralized bleed value, and fail closed if any expanded pixel reaches a fully transparent exterior template pixel. Mask the portrait to this verified safe bleed mask, then composite the canonical template unchanged as the final top layer.

The covering scale is `max(under_frame_fill_width / source_width, under_frame_fill_height / source_height)`, and the source aspect ratio must remain unchanged. The only content-area clipping is the symmetric aspect-ratio excess recorded in `frame_clip_pixels`. Never substitute an exact-opening clip for the under-frame bleed. `source_pre_crop=false` means no pre-scale source crop, not that the portrait may stop at the visible opening.

Generate and retain a separate placement study for every person and inspect the face, head, and shoulders at native size and `4x` nearest-neighbour enlargement. The alignment overlay must show the measured opening in red, the opening-fill plane in green, and the uniformly scaled covering portrait in yellow. The yellow bounds may show the centralized bleed/guard extension and recorded symmetric cover excess, but the runtime portrait must remain inside the safe bleed mask. The selected transform must match the retained study candidate. Near-zero rotation is rejected by default. Use the explicit override only for an independently reviewed alternative template whose measured opening is actually unrotated.

Retain transform metadata for the source, template, measured opening geometry, selected placement, `opening_fill_size`, `under_frame_fill_size`, `covering_content_size`, `covering_content_center`, `frame_clip_pixels`, `under_frame_bleed_pixels`, and `resampling_edge_guard_pixels`, together with the explicit fit flags `source_pre_crop=false`, `frame_clip=true`, and `stretch=false`, plus the study, alignment overlay, processed PNG, and runtime DDS. Automated evidence must report `opening_alpha_gap_pixels=0`, `inner_edge_alpha_gap_pixels=0`, and `exterior_alpha_leak_pixels=0` in the alpha-coverage record. Review the native card and nearest-neighbour enlargement against contrasting solid backgrounds and checker backgrounds, and compare subject scale and frame integrity with the vanilla advisor/high-command references. Keep this workflow generic. Event-specific advisor names belong in the asset manifest or handoff, never in this reusable skill. The reusable command contract and review checklist are documented under `tools/README.md` in the advisor and high-command dossier section.

Do not shrink, pad, or directly wire a `156x210` leader, commander, or operative portrait. Compose the subject independently inside the native card with a deterministic, task-specific/manual workflow and retain the exact crop, face placement, dimensions, and review evidence. Do not draw replacement frame, paper, seal, bevel, patina, emblem, writing, or shadow artwork from primitive geometry, and do not advertise a missing shared processor.

Check the native `65x67` candidate against the canonical advisor and high-command references. Confirm composition, face readability, frame silhouette and palette, paper geometry and opacity where present, transparent corners, texture continuity, and the absence of holes or fringe. Record any deterministic dimension or alpha checks as evidence, but treat visual approval as a separate human gate.

When a character explicitly defines a `portraits = { army = { small = ... } }` sprite, the small slot remains a native `65x67` dossier portrait while `army.large` remains the full `156x210` commander portrait. Do not create a plain `50x67` resize or crop for the army-small slot, and do not replace or downsize the approved full commander texture. Keep the large and small sprite names stable, record both runtime paths and provenance, and validate both textures separately.

The independent visual review must compare the candidate with the canonical advisor and high-command references at native `65x67` and at `4x` nearest-neighbour size. Automated dimension and alpha checks produce evidence only, and the producer cannot self-approve the candidate. Convert only an independently approved PNG with `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <approved.png> --output <runtime.dds> --width 65 --height 67`.

### UI panels and custom windows

Use ImageGen for illustrated backgrounds, thematic decorations, symbolic seals, propaganda, and report-board art, with the shared alpha/background rules. Use native UI editing for exact slicing, cropping, button/state variants, meter fills, and final export preparation. Generated art does not decide interactive layout; follow HOI4 UI rules and repository patterns.

After generating the compositional reference, decompose it into individually implementable and independently reviewable elements and layers. Map every panel, frame, tab, button, popup, icon, meter, text field, state, and click region separately to generated art or a native control. A composite reference may show the assembled design, but no functional button, fake popup window, label, hover/selected state, or click target may be baked into a flattened runtime background.

### Decision category and scripted GUI visual packs

When an improvement addendum asks for richer presentation, the asset handoff should name the visual states instead of asking for generic polish. A good asset request says what the player sees before activation, while active, when locked, when dangerous, when complete, and when the route has failed.

For scripted GUI, plan coordinated families for the actual mechanic states, including value icons and any required pulse layers. The main agent owns `.gui` and `.gfx` wiring; provide clear sprite names, sizes, frame counts, static fallbacks, and contact sheets.

Do not build a full scripted GUI visual pack for every important category. First follow the presentation hierarchy in `chaos-redux-decisions-missions`. A simple category may need only its small icon and one static or animated category picture, subject to [Decision category pictures](#decision-category-pictures)' eligibility gate. Do not add a category picture alongside the rich GUI assets or other animations listed below.

For new or redesigned scripted GUIs, follow `chaos-redux-scripted-gui` for reference images before native implementation, acceptance evidence, and image-to-element mapping. Produce a compositional reference with ChatGPT Images 2.5 Sunburst through native ImageGen (subject to the generated-art execution-path truthfulness rule) or an applicable supplied image, then separate final decorative art from real controls, live labels, meters, and lists; never deliver a flattened fake interface as functional UI. Include painted bounds, transparent padding, usable interior regions, intended dimensions, frame/state order, native element consumers, and justified engine/style adaptations in the asset handoff. When a full scripted GUI or mechanic window is justified, the asset handoff should cover the interface state set that the actual mechanic uses. Do not create unused tabs, button states, meters, frames, or decorative controls only to fill the background.

Select only required assets: category icon/header plate, background, tabs, normal/hover/selected/locked/disabled/warning button states, progress bars/fills, meter frames, target cards, status seals, warning overlays, animated glow/particle/float layers with static fallbacks, tooltip icons, open/close buttons, and authorized mechanic-specific leader/council/envoy portraits.

The asset prompt should state which sprites are decorative and which represent mechanic state. State-driven sprites need clear names that match the mechanic value or route state.

### Progression-state variants

Keep progression variants at the base asset target size. Accepted states may include selected, dim, active, inactive, locked, completed, rejected, damaged, corrupted, urgent, meter-fill, and bar-fill.

### Formable nation asset coverage

Every formable nation needs visible identity assets.

Asset planning should cover:

- formable flag in normal, medium, and small sizes
- ideology variants where relevant
- cosmetic-tag flags where relevant
- leader portrait or council portrait
- animated leader portrait when the formable is a rare dramatic route
- focus icons for the formation route
- decision icon for the formation decision
- a static or animated decision category picture when a territorial overview or formation identity would improve a simple category that passes [Decision category pictures](#decision-category-pictures)' eligibility gate
- exact state-puzzle GUI assets when formation progress depends on current control of named states
- news, report, or super-event image if the formation is globally important
- faction emblem if the formable creates a league, empire, federation, bloc, mandate, compact, or coalition
- achievement icon if the formable has achievement hooks

Historical or culturally attested formable symbols need source review. Fictional, alternate-history, supernatural, and high-chaos variants may use generated art with clear manifest notes.

### Formable state-puzzle visual assets

When a formable uses the reusable state-puzzle presentation from `chaos-redux-decisions-missions`, the asset package must preserve exact state geometry and one shared geographic projection.

Each puzzle package should include:

- a state manifest with formable id, state id, state name, alternate requirement group, counting rule, source map data, projection bounds, anchor, and proposed sprite name
- one exact mask or sprite region for every required state
- a grey unmet state and a green qualifying state, or a verified frame or tint system that produces the same result without losing state boundaries
- borders, texture, labels, or another non-colour distinction between unmet and qualifying states
- a composed preview showing the full territory assembled in real geographic positions
- hover and tooltip region notes for every state piece
- a static category-picture version when the category only needs a territorial overview and passes [Decision category pictures](#decision-category-pictures)' eligibility gate; do not add it alongside the interactive state-puzzle GUI
- final runtime paths, `.gfx` ownership, GUI ownership, and manifest coverage

State shapes must be derived from the installed map's state and province geometry. Do not trace a screenshot by hand, generate borders with ImageGen, simplify the pieces into generic tiles, or substitute a modern political map. All pieces must use one projection, scale, origin, edge treatment, and border width.

A generated or sourced background may frame the map, but it must not alter, cover, or replace the exact state shapes. Keep the territorial layer readable at supported resolutions and verify that neighbouring states meet cleanly without unexplained gaps or overlaps.

Choose one verified runtime structure based on the consumer:

- separate state sprites
- one atlas with documented frame order
- one sheet with documented frame order
- exact mask layers over a shared base

Do not choose a structure only because it is easier to export. The GUI and dynamic eligibility logic must be able to address each required state reliably.

The reusable implementation templates belong under:

`.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/`

The asset handoff must match the template manifest and naming rules. Skill-local template assets are reference scaffolding and must never be runtime consumers.

### Animated sprites, scripted GUI assets, and animated portraits

Use `chaos-redux-frame-animation` for every final animated visual asset. Some Chaos Redux mechanics should have animated visual layers when motion improves readability, atmosphere, or feedback. Examples include floating seals, glowing route emblems, particle drift, meter pulses, warning frames, active-button glows, occult pressure effects, sponsor influence networks, and final formable proclamations.

Animated leader portraits should be handled as major identity assets. Complete [Country-leader, commander, operative, and named-officeholder portraits](#country-leader-commander-operative-and-named-officeholder-portraits) through `chaosx_portrait_creator` before frame animation for both grounded and fictional subjects. The asset handoff must say whether the animation is subtle, such as breathing light or smoke, or symbolic, such as eye glow, map shadow, glitch, or spectral overlay. The portrait should still read clearly at in-game size.

Final animated assets must be built from planned source frames. Do not create final animation by taking one still image and shifting, scaling, rotating, warping, blurring, recoloring, brightening, or pulsing it with a script. Local scripts may normalize, align, crop, resize, assemble sheets, create previews, and convert frames after the real frames exist.

Apply the Sunburst route and execution-path rule in [Generate and refine source art](#generate-and-refine-source-art) throughout frame production.

Leader portraits can be animated for special routes, high-chaos leaders, supernatural leaders, rare formables, major transformations, or dramatic council reveals. They should not be required for every normal country leader.

Animated leader portrait packages must include:

- static fallback portrait
- animated sheet or frame source
- final DDS files
- final sprite names
- character or leader key that will use the portrait
- source mode and source documentation
- whether the leader is real, fictional, symbolic, collective, supernatural, or alternate-history
- note on motion type, such as glow, smoke, flicker, eye-light, flag shadow, slow breathing, office light, map projection, or particle drift

### Unit visual references

Treat every unit visual as a domain-and-surface-specific pipeline. Inspect the matching catalog entries, contact sheet, and owning vanilla definition before deciding what the task needs.

- `units/equipment/technology_art/` contains flat 2D equipment illustrations used by equipment and technology sprites. Native canvases vary, follow the owning `interface/*.gfx` sprite.
- `units/land/counters_large/` contains large frame-aware land-unit strips. Preserve the cataloged `noOfFrames`, frame order, per-frame footprint, and transparent bounds.
- `units/land/map_counters/` contains land map-counter art. It is not a large division-designer strip.
- `units/land/division_template_emblems/` contains division-template identity emblems. It is not equipment art or map-counter art.
- `units/air/map_counters/` and `units/naval/map_counters/` contain domain-specific map-counter art. Do not substitute land counters or resized equipment art.
- `units/models_3d/land_materials/`, `units/models_3d/air_materials/`, and `units/models_3d/naval_materials/` contain UV model materials paired with cataloged `.mesh`, `.asset`, and entity definitions. They are not 2D icons, finished renders, or concept sheets.

Classify the requested deliverable before creating art: equipment/technology illustration, large land counter, land/air/naval map counter, division-template emblem, or land/air/naval 3D model package. Give each class its own brief, source art, native canvas or UV layout, frame metadata, final path, and handoff. A 3D task must keep model geometry, materials, entity wiring, and any separately produced concept reference distinct. Do not derive one unit pipeline by resizing, relabeling, or recoloring another.

#### 2D icon and counter generation contract

Every new custom unit or subunit requires bespoke counter art for every runtime counter surface it uses. Before production, inspect the exact installed-vanilla counter definition and DDS plus the matching skill-local family under `assets/vanilla_reference/units/`. Match the sampled vanilla green palette, canvas, frame order, alpha/background treatment, border, silhouette, shading, contrast, and state behavior. Reused counters, renamed existing counters, generic placeholders, arbitrary green, and final art made without recorded vanilla inspection are forbidden. Route production to `chaosx_icon_artist`, block when the exact references are unavailable.

Apply this contract to every small template, facility, or unit icon, including large land counters and division-template emblems.

Before generation, inspect the actual installed-vanilla consumer definition and DDS, plus the exact matching reference family and contact sheet under `assets/vanilla_reference/`. Record the owning `.gfx`, `.gui`, unit, building, or template definition, runtime token or sprite, native canvas, frame count and order, frame or state semantics, alpha and background treatment, border, sampled palette, silhouette footprint, shading, and contrast. If the consumer, DDS, or matching reference family cannot be inspected, mark the asset `blocked` instead of guessing.

Use the built-in ImageGen tool for each distinct final asset and retain its exact prompt and native source PNG in the evidence package. Generate the icon or glyph as real raster source art with a genuine transparent background in the initial call. Pixel art, pixel-grid or nearest-neighbor final scaling, primitive local drawings, SVG-only reconstruction, resized cross-type substitutes, opaque backgrounds, and generic white duplicates are prohibited. Nearest-neighbor is permitted only for enlarged inspection previews.

Preserve the native ImageGen alpha through processing, then validate transparent corners, no coloured fringe, no fake checkerboard or matte, and no unintended transparent holes. If native transparency fails, follow the fallback route in [Native transparency and background-removal fallback](#native-transparency-and-background-removal-fallback): first a targeted built-in edit-to-transparency, then an actually installed and verified local removal process only if needed. Downsample smoothly with bicubic or Lanczos to the inspected native runtime canvas, preserve the intended transparent bounds, and record the visible alpha bounding box, centered footprint, frame boundaries, and per-frame footprint against the vanilla reference. Do not promote a candidate whose silhouette is clipped, off-center, too small, too detailed at native size, or damaged by fallback removal.

For a large land division counter, the final file is one transparent `152x42` strip containing two adjacent `76x42` frames with no gap. The left frame is a compact muted vanilla-green silhouette for the normal large-counter state. The right frame is a separate sparse pale or white generic schematic glyph for the alternate or template state and is never a detailed white repaint or duplicate of the left frame. Differentiate each unit by role and silhouette while staying within the same restrained vanilla vocabulary.

For division-template emblems, produce separate transparent large `76x42` and small `30x12` canvases with a centered compact emblem footprint. Keep both sizes simple, smooth, muted green or olive, and within the restrained vanilla vocabulary. A template emblem is a separate asset family from a large counter strip and is not a counter strip.

Follow the shared workspace and candidate-lineage contract: retain source/processed files, prompts, contact sheet, manifest, handoff, and validation evidence until parent review and completion, and synchronize only the explicit final-selected candidate.

Use the mandatory native-size [Contact sheets](#contact-sheets) comparison and [DDS conversion](#dds-conversion) checks, including source/processed transparency, enlarged smooth preview, and native-size DDS round-trip with filenames, dimensions, frame labels, and visible-bounds notes. The parent must visually review the sheet before runtime promotion; until then the worker reports `needs_user_review` or `blocked` and never claims in-game completion.

#### 3D model package handoff

Route 3D model production to `chaos-redux-3d-model-pipeline` and `chaosx_3d_model_pipeline`. The 3D worker owns the mandatory custom-unit counter requirement and bounded `chaosx_icon_artist` handoff, while this 2D asset pipeline owns final counter art. Equipment art, division emblems, and frame-sheet animation remain separate production surfaces.

Before any provider or paid work, the 3D route must verify a nonblank `MESHY_API_KEY`, the selected pinned Meshy 7 MCP route with the exact `meshy-7` image-to-3D identifier, the narrow Blender HOI4 adapter, the installed Blender version, and the checksum-locked `io_pdx_mesh` setup.

When a ready reference is absent, the route creates exactly one clean `meshy_input.png` for the asset. Never create or send side-profile sheets, turnaround boards, collages, or multi-view boards to Meshy. Contact sheets and Blender renders are QA evidence only.

Every 3D asset brief must identify the asset profile, deterministic job root, provider task lineage, named vanilla mesh and entity precedent, source geometry height, entity scale, effective runtime height, axes, origin, contact plane, required actions, root-motion policy, PDX material channels, texture dimensions, `.mesh` and `.anim` outputs, reimport proof, and live consumer.

For humanoid units, calibrate against the installed vanilla infantry source mesh and entity rather than an assumed real-world height or arbitrary entity scale. Apply the entity scale exactly once and record the source-height-to-runtime-height crosswalk.

Provider source files are immutable evidence. Working geometry must be repaired so it has no holes, loose or non-manifold geometry, degenerate triangles, missing components, or zero-weight deforming vertices. Use the verified PDX shader and packed specular map convention, never route raw grayscale roughness into the PDX specular channel because that creates chrome-black surfaces.

For animated units, select the route in `chaos-redux-3d-model-pipeline`: firearm bodies are freshly generated weapon-free in Meshy 7 and go directly to Blender rigging, weights, manual animation, and separate equipment modeling; existing non-firearm repairs use Blender directly; other new models receive one Meshy rig/action attempt before Blender fallback. Preserve source evidence and require complete component inventories, anatomy/deformation/contact checks, real articulated semantic motion, FPS/frame/loop/root review, and `.anim` export/reimport proof. Missing required elements must be modeled/restored without renewed approval. Actual unavailable operations remain blockers; static poses, transform-only substitutes, and role aliases cannot pass.

For every firearm-bearing unit, including existing firearm models, prepare exactly one weapon-free body image using source-informed weapon removal and pose/body cleanup, retain source firearm identity for Blender reconstruction, and generate a fresh Meshy 7 body. Skip Meshy rig/animation attempts. Use Blender to rig, weight, animate, model missing required parts and separate firearms/held props, and attach them with weapon bones, parenting, and constraints. Complete trigger-hand, support-hand/foregrip, stock/shoulder, muzzle, aim/fire/recoil/recovery, and ground-contact review on the assembled model and every relevant action. Keep intended identity, non-anime period style, source licensing/provenance, and native-alpha requirements. Modest reduction to fit required added equipment inside calibrated budgets is preauthorized; omission is not.

For every firing runtime state, the 3D handoff must identify the exact discharge frame/time and verified muzzle or weapon locator/node, plus the matching particle/beam/muzzle effect, light where the weapon calls for one, and licensed sourced `soundeffect`. Attack, defend, support_attack, and any other firing state are independent consumers. A silent or particleless firing state is incomplete, and an unrelated vanilla weapon family must not be silently reused. The 3D worker supplies the action → discharge frame/time → locator/node → particle/light → soundeffect → source/license → runtime entity consumer → evidence/status crosswalk. The parent owns final entity, particle, sound-definition, and runtime wiring. Non-firing armed actions do not require particles or gunshot audio merely because the unit is armed.

The asset worker owns source files, checkpoints, processed textures, previews, exports, manifests, reports, reimport evidence, and a runtime handoff. The main implementation agent owns `.asset`, entity, `.gfx`, unit/building/gameplay wiring, final runtime synchronization, and evidence review. The user supplies in-game screenshots and performs live consumer validation.

## Processing and installation

### DDS conversion

Final PNG assets must be converted to DDS using the repository's standard DDS conversion workflow. The converter lives only at `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, `.tools/convert_to_dds.py` is obsolete, and active skills, agents, scripts, and handoffs must not restore or call it.

The output must be compatible with Chaos Redux's expected 32-bit BGRA or B8G8R8A8-style DDS workflow.

Run the bundled converter from the mod root:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <processed.png> --output <final.dds> [--width <pixels> --height <pixels>]
```

If a retained custom mechanical processor must write uncompressed BGRA DDS directly, mirror that converter's `write_bgra_dds` layout exactly instead of inventing another header layout.

For a standard legacy, one-level, uncompressed BGRA DDS, require all of the following:

- a 128-byte file header in total: `DDS ` magic at byte 0, `DDS_HEADER` size `124` at byte 4, and 11 reserved dwords before the pixel-format block
- `DDS_PIXELFORMAT` at byte 76 with size `32`, flags `65` (`RGB | ALPHAPIXELS`), fourCC `0`, bit count `32`, and BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, and `0xFF000000`
- `DDSCAPS_TEXTURE` (`0x1000`) at byte 108
- no mipmaps unless the target asset deliberately requires them

Validate each uncompressed one-level BGRA output by checking the declared width and height, exact file length `128 + width * height * 4`, actual alpha-byte minimum and maximum against the asset's intended transparency, and successful registration of the final path in `.gfx`. Dimension and alpha checks alone are insufficient: reject shifted pixel-format blocks, missing texture caps, or any other malformed header even when an image decoder can report plausible dimensions.

If a processing script is retained as provenance, rerun it after correcting its DDS writer and validate every DDS it produces, not only the asset that exposed the defect.

If conversion fails, stop and report the error. Do not invent another conversion route unless the user approves it.

Achievement triplets additionally follow [Shared processing and validation](#shared-processing-and-validation) for source decoding and exact state-composition equality.

After conversion, verify the actual DDS dimensions and native or fallback-validated transparency, stable filename, event-scoped placement or documented root-only exception, `.gfx` linkage, and manifest path.

For small icon, counter, and emblem packages, decode each final DDS back to pixels at its native size and retain the round-trip comparison evidence with the contact sheet. A header, dimension, and alpha pass alone is not visual QA.

Do not leave only PNG files when the game expects DDS.

### Final asset placement and naming

Event-owned final assets should be grouped under an event-scoped folder whenever the engine surface uses explicit sprite or texture paths.

Use this folder form:

```text
<event_id>_<event_slug>
```

Place the event folder directly under the asset category folder, for example `gfx/event_pictures/014_cannibalism/` or `gfx/interface/ideas/014_cannibalism/`. Do not insert a project namespace layer such as `gfx/event_pictures/chaos_redux/014_cannibalism/`, the mod root already provides the project namespace.

Do not leave new event assets loose in category roots such as `gfx/event_pictures/`, `gfx/super_events/`, `gfx/interface/ideas/`, `gfx/interface/goals/`, `gfx/interface/decisions/`, or `gfx/leaders/` unless that root placement is an engine-facing lookup requirement.

Root-only and engine-convention exceptions:

- `gfx/achievements/` must keep achievement DDS files directly in the root. Do not create `gfx/achievements/<event_id>_<event_slug>/` subfolders unless a new engine behavior has been verified locally. Achievement filenames must match the full achievement ids from `common/achievements/`, so event-owned achievement ids and triplet filenames should use `<event_id>_<event_slug>_<achievement_name>{,_grey,_not_eligible}.dds` or the exact established id if it includes an ordinal.
- `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` must keep HOI4 tag/ideology filenames. Do not put flags into event folders, use cosmetic tags or route-specific tag filenames when an event needs transformed flags.

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

While the asset workspace is active, keep the original generated source and every accepted intermediate immutable at distinct versioned paths. Keep source outputs separate from processed previews and runtime files. In the active manifest or linked prompt record, record for each generated candidate:

- candidate id, parent candidate id or new-generation reason, and input paths with their declared roles
- exact submitted prompt, focused edit delta, invariants, and background mode
- tool-reported output path, retained workspace path, decoded dimensions, and alpha evidence
- source-resolution and final-native-size review results, accepted/rejected status, and remaining defects
- explicit final-selected candidate id, processed PNG path, and final runtime path after conversion

Do not silently overwrite a prior accepted candidate or synchronize an older candidate into runtime. Before normal temporary-workspace cleanup, promote the lineage, prompts, final selection, and review facts into permanent documentation under the existing cleanup contract. Retain active image files until the required package review is complete; this rule does not create a second permanent asset archive.

### Contact sheets

When an asset package contains many generated or sourced images, create a contact sheet for review.

Small template, facility, unit, counter, and emblem packages always require a native-size contact sheet, even when the package contains one final asset.

The canonical decision category picture reference family always requires:

`assets/vanilla_reference/icons/decision_categories/pictures/contact_sheet.png`

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

For every animation family, also record the purpose and the direction or state semantics that distinguish the family, together with its frame, timing, and loop evidence. Frame totals, live animation-family totals, and registered sprite totals are not coverage proof.

For every real-person portrait row, link the unchanged source, explicit crop, wired placeholder, user-supplied final when available, role references, comparison evidence, reviewer, and likeness/framing/provenance verdict. Style quality cannot compensate for identity failure.

Audit exact rows, not counts. An extra asset or animation cannot satisfy an absent accepted row unless an explicit accepted design amendment identifies that row and names the replacement, link that amendment in the crosswalk. Any missing source package, runtime registration, live consumer, required state or visibility binding, or current audit record leaves the row incomplete.

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
