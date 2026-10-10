# Reference library and canonical asset paths

Read this reference before generating, sourcing, processing, or wiring any asset: it defines the skill-local visual-reference library, the canonical reference paths for every asset family, and the rules for using reference images and catalogs. The main skill keeps the source, generation, processing, and evidence rules.

## Sources and references

### Reference asset examples

This skill owns its visual-reference library under:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.claude\skills\chaos-redux-event-assets\assets`

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

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.claude\skills\chaos-redux-event-assets\assets\gfx_references\icons\decision_categories\pictures`

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

For matching icon and portrait briefs, inspect `assets/visual_components/CATALOG.md` and the relevant contact sheet after the exact vanilla or Chaos Redux consumer and `assets/gfx_references/` family. The catalog role governs whether a component is only a visual reference or may also be a persistent background layer. Keep every used component source and image-generation source separate from the processed preview and final DDS; record the local catalog entry, role, and layer path in the output manifest. The exact consumer still governs dimensions, alpha, states, and wiring, and achievement templates and state rules still apply.

When validating inherited GUI or GFX references, check both the mod and installed vanilla roots before declaring a DDS or other resource missing. A missing literal `effectFile` `.lua` path alone does not prove a missing asset. Inspect matching installed-vanilla `.gfx` declarations and the associated shader resource before reporting a missing source. Record the exact declaration, resource path, and lookup evidence without assuming a generic `.lua` to `.shader` mapping. Source linkage evidence does not prove rendered behavior or live-game correctness.
