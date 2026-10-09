# Icon, counter, and UI asset families

Read the complete section for each requested icon, counter, decision picture, UI panel, formable visual, or animated sprite family before production. Use the main skill for source selection, generation, conversion, and final review.

## Icon creation rules

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
- commander traits, medals, military raids, state modifiers, MIOs, factions, buildings, and modifier icons must follow the matching canonical folder and owning vanilla definition; do not force these families onto a blanket 32x32 or 64x64 canvas
- frame strips, indexed building sprites, and multi-state modifier art must retain their frame order and frame count rather than being treated as a single standalone icon

If a mechanic needs matching focus, idea, and decision visuals, build them as a coordinated icon family. A coordinated family can share subjects, symbols, colors, and lore cues, but each member still needs separate source art or a separate generated output designed for its target size and UI role.

The manifest must record the exact asset type for every icon and should note when icons are part of a coordinated family. Do not mark an icon complete if it only exists as a resized version of another icon type.

The idea and national spirit, focus, and decision icon families below all apply the shared generation, text, transparency, and separate-source rules; for each, a user-provided or specifically requested source takes precedence.

### Idea and national spirit icons

Use compact HOI4 symbolic art with aged texture, strong contrast, a clear silhouette, and readable meaning at `64x64`, usually without a full focus frame. Use `idea_` and inspect `icons/ideas/` plus its catalog row.

Trace the consumer's actual prefix contract and default override before wiring: idea `picture = my_icon` resolves to `GFX_idea_my_icon`, while an existing `GFX_idea_<idea_id>` takes precedence even over explicit `picture`.
Do not pass `GFX_idea_my_icon` as the picture value; it requests `GFX_idea_GFX_idea_my_icon`.
Verify the exact expected alias, any automatic idea-id override, and its texture path across mod and vanilla definitions, and record the resolved consumer-to-alias mapping in the handoff while preserving stable identifiers unless a lookup correction requires a change.
Check each consumer independently: decision and category `icon` fields accept both suffixes and full `GFX_decision_`/`GFX_decision_category_` names, so never apply blanket `GFX_` stripping.

Inspect `assets/visual_components/national_spirit_backgrounds/contact_sheet.png` for matching background treatment. A catalog `background_template` may sit beneath original ImageGen subject art when the exact idea or national-spirit consumer fits; keep the template source as a separate layer.

### Focus icons

Use HOI4 focus art with a strong central symbol, clear silhouette, aged texture, painterly detail, and readable contrast tied to the focus tree story, ideology, or gameplay purpose; avoid generic thumbnails. Use `goal_` and nominal `94x86`, inspecting `icons/national_focus/`, its catalog row, and the owning sprite/current vanilla precedent before selecting the actual canvas.

Inspect `assets/visual_components/focus_pieces/contact_sheet.png` and `assets/visual_components/focus_backgrounds/contact_sheet.png` for optional subject scale, framing, and composition cues in the ImageGen prompt. These components are references; create the icon's subject as original ImageGen art.

### Decision icons

Compose decision icons for `32x32` readability with simple central symbols, strong contrast, and limited interior detail. Use `decision_` or `decision_category_` for category icons, and inspect `icons/decisions/`, `icons/missions/`, or `icons/decision_categories/` with the owning consumer. Missions use the decision pipeline with mission-specific semantic readability.

For a decision-category icon, inspect `assets/visual_components/national_spirit_backgrounds/decision_category_background_blue_roundel.png` as a cataloged background candidate. Composite it only when the exact category consumer fits, beneath an original ImageGen subject. Do not transfer that background to ordinary decision or mission icons by resizing it.

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

Inspect `assets/gfx_references/icons/achievements/contact_sheet.png` and the matching individual references before creating an achievement icon. The contact sheet and reference examples are review material, while the `template/` folder below is a separate workflow-input folder excluded from the achievement reference count.

#### Supplied templates

Use these exact supplied workflow inputs and do not invent, rename, move, resize, crop, trim, recolor, redraw, filter, or replace them:

```text
assets/gfx_references/icons/achievements/template/achievement_template.png
assets/gfx_references/icons/achievements/template/achievement_template_grey.png
assets/gfx_references/icons/achievements/template/overlay.png
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

Apply `template/achievement_template.png` beneath the completed source and `template/achievement_template_grey.png` beneath both grey and not-eligible sources. Normal alpha compositing is the only pixel interaction. Every final state must pass the strict one-level 64x64 legacy BGRA checks in [DDS conversion](../SKILL.md#dds-conversion), with decoded pixels exactly equal to its supplied background beneath its exact decoded source layer. All three runtime states are required; source-decoding tolerance never weakens final validation.

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

## Decision category pictures

A decision category picture is a larger visual surface used inside or beside a decision category. It is not a `32x32` decision icon, a small category icon, a custom-window background, or a substitute for an interactive scripted GUI.

### Eligibility before production

Use a static or animated category picture only for a simple category with a description, an ordinary decision list, and at most basic formatted value tables.
Ordinary decision-list action buttons and basic formatted value tables are allowed; additional category GUI buttons or controls are not.
Do not add a picture to a category that already has complex UI, meters, additional custom buttons or controls, rich interactive panels, or other animations.
An animated category picture itself is supported when this same gate passes, but it must not accompany existing animated GUI.

Within this gate, a category picture may provide strong identity, historical context, propaganda, territorial orientation, or a readable theme while the normal decision list carries the gameplay actions.
Those themes alone do not override eligibility or require a picture.

### Subjects, sources, and production

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

`assets/gfx_references/icons/decision_categories/pictures/contact_sheet.png`

Also inspect the exact active consumer to confirm canvas, crop, alpha, frame behavior, and runtime path. The reference family uses `114x101`, but the consumer decides the final target.

The asset manifest and handoff must state whether the output is:

- small category icon
- static category picture
- animated category picture
- compact scripted GUI display
- full mechanic-window asset

Do not let one asset satisfy several of these surfaces by resizing or relabeling it.

## UI panels and custom windows

Use ImageGen for illustrated backgrounds, thematic decorations, symbolic seals, propaganda, and report-board art, with the shared alpha/background rules. Use native UI editing for exact slicing, cropping, button/state variants, meter fills, and final export preparation. Generated art does not decide interactive layout; follow HOI4 UI rules and repository patterns.

After generating the compositional reference, decompose it into individually implementable and independently reviewable elements and layers. Map every panel, frame, tab, button, popup, icon, meter, text field, state, and click region separately to generated art or a native control. A composite reference may show the assembled design, but no functional button, fake popup window, label, hover/selected state, or click target may be baked into a flattened runtime background.

## Decision category and scripted GUI visual packs

When an improvement addendum asks for richer presentation, the asset handoff should name the visual states instead of asking for generic polish. A good asset request says what the player sees before activation, while active, when locked, when dangerous, when complete, and when the route has failed.

For scripted GUI, plan coordinated families for the actual mechanic states, including value icons and any required pulse layers. The main agent owns `.gui` and `.gfx` wiring; provide clear sprite names, sizes, frame counts, static fallbacks, and contact sheets.

Do not build a full scripted GUI visual pack for every important category. First follow the presentation hierarchy in `chaos-redux-decisions-missions`. A simple category may need only its small icon and one static or animated category picture, subject to [Decision category pictures](#decision-category-pictures)' eligibility gate. Do not add a category picture alongside the rich GUI assets or other animations listed below.

For new or redesigned scripted GUIs, follow `chaos-redux-scripted-gui` for reference images before native implementation, acceptance evidence, and image-to-element mapping. Produce a compositional reference with ChatGPT Images 2.5 Sunburst through native ImageGen (subject to the generated-art execution-path truthfulness rule) or an applicable supplied image, then separate final decorative art from real controls, live labels, meters, and lists; never deliver a flattened fake interface as functional UI. Include painted bounds, transparent padding, usable interior regions, intended dimensions, frame/state order, native element consumers, and justified engine/style adaptations in the asset handoff. When a full scripted GUI or mechanic window is justified, the asset handoff should cover the interface state set that the actual mechanic uses. Do not create unused tabs, button states, meters, frames, or decorative controls only to fill the background.

Select only required assets: category icon/header plate, background, tabs, normal/hover/selected/locked/disabled/warning button states, progress bars/fills, meter frames, target cards, status seals, warning overlays, animated glow/particle/float layers with static fallbacks, tooltip icons, open/close buttons, and authorized mechanic-specific leader/council/envoy portraits.

The asset prompt should state which sprites are decorative and which represent mechanic state. State-driven sprites need clear names that match the mechanic value or route state.

## Progression-state variants

Keep progression variants at the base asset target size. Accepted states may include selected, dim, active, inactive, locked, completed, rejected, damaged, corrupted, urgent, meter-fill, and bar-fill.

## Formable nation asset coverage

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

## Formable state-puzzle visual assets

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

## Animated sprites, scripted GUI assets, and animated portraits

Use `chaos-redux-frame-animation` for every final animated visual asset. Some Chaos Redux mechanics should have animated visual layers when motion improves readability, atmosphere, or feedback. Examples include floating seals, glowing route emblems, particle drift, meter pulses, warning frames, active-button glows, occult pressure effects, sponsor influence networks, and final formable proclamations.

Animated leader portraits should be handled as major identity assets. Complete [Country-leader, commander, operative, and named-officeholder portraits](portrait-production.md#country-leader-commander-operative-and-named-officeholder-portraits) through `chaosx_portrait_creator` before frame animation for both grounded and fictional subjects. The asset handoff must say whether the animation is subtle, such as breathing light or smoke, or symbolic, such as eye glow, map shadow, glitch, or spectral overlay. The portrait should still read clearly at in-game size.

Final animated assets must be built from planned source frames. Do not create final animation by taking one still image and shifting, scaling, rotating, warping, blurring, recoloring, brightening, or pulsing it with a script. Local scripts may normalize, align, crop, resize, assemble sheets, create previews, and convert frames after the real frames exist.

Apply the Sunburst route and execution-path rule in [Generate and refine source art](../SKILL.md#generate-and-refine-source-art) throughout frame production.

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

## 2D icon and counter generation contract

Every new custom unit or subunit requires bespoke counter art for every runtime counter surface it uses. Before production, inspect the exact installed-vanilla counter definition and DDS plus the matching skill-local family under `assets/gfx_references/units/`. Match the sampled vanilla green palette, canvas, frame order, alpha/background treatment, border, silhouette, shading, contrast, and state behavior. Reused counters, renamed existing counters, generic placeholders, arbitrary green, and final art made without recorded vanilla inspection are forbidden. Route production to `chaosx_icon_artist`, and block when the exact references are unavailable.

Apply this contract to every small template, facility, or unit icon, including large land counters and division-template emblems.

Before generation, inspect the actual installed-vanilla consumer definition and DDS, plus the exact matching reference family and contact sheet under `assets/gfx_references/`. Record the owning `.gfx`, `.gui`, unit, building, or template definition, runtime token or sprite, native canvas, frame count and order, frame or state semantics, alpha and background treatment, border, sampled palette, silhouette footprint, shading, and contrast. If the consumer, DDS, or matching reference family cannot be inspected, mark the asset `blocked` instead of guessing.

Use the built-in ImageGen tool for each distinct final asset and retain its exact prompt and native source PNG in the evidence package. Generate the icon or glyph as real raster source art with a genuine transparent background in the initial call. Pixel art, pixel-grid or nearest-neighbor final scaling, primitive local drawings, SVG-only reconstruction, resized cross-type substitutes, opaque backgrounds, and generic white duplicates are prohibited. Nearest-neighbor is permitted only for enlarged inspection previews.

Preserve the native ImageGen alpha through processing, then validate transparent corners, no coloured fringe, no fake checkerboard or matte, and no unintended transparent holes. If native transparency fails, follow the fallback route in [Native transparency and background-removal fallback](../SKILL.md#native-transparency-and-background-removal-fallback): first a targeted built-in edit-to-transparency, then an actually installed and verified local removal process only if needed. Downsample smoothly with bicubic or Lanczos to the inspected native runtime canvas, preserve the intended transparent bounds, and record the visible alpha bounding box, centered footprint, frame boundaries, and per-frame footprint against the vanilla reference. Do not promote a candidate whose silhouette is clipped, off-center, too small, too detailed at native size, or damaged by fallback removal.

For a large land division counter, the final file is one transparent `152x42` strip containing two adjacent `76x42` frames with no gap. The left frame is a compact muted vanilla-green silhouette for the normal large-counter state. The right frame is a separate sparse pale or white generic schematic glyph for the alternate or template state and is never a detailed white repaint or duplicate of the left frame. Differentiate each unit by role and silhouette while staying within the same restrained vanilla vocabulary.

For division-template emblems, produce separate transparent large `76x42` and small `30x12` canvases with a centered compact emblem footprint. Keep both sizes simple, smooth, muted green or olive, and within the restrained vanilla vocabulary. A template emblem is a separate asset family from a large counter strip and is not a counter strip.

Follow the shared workspace and candidate-lineage contract: retain source/processed files, prompts, contact sheet, manifest, handoff, and validation evidence until parent review and completion, and synchronize only the explicit final-selected candidate.

Use the mandatory native-size [Contact sheets](../SKILL.md#contact-sheets) comparison and [DDS conversion](../SKILL.md#dds-conversion) checks, including source/processed transparency, enlarged smooth preview, and native-size DDS round-trip with filenames, dimensions, frame labels, and visible-bounds notes. The parent must visually review the sheet before runtime promotion; until then the worker reports `needs_user_review` or `blocked` and never claims in-game completion.
