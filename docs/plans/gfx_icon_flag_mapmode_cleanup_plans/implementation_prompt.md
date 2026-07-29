# Chaos Redux GFX, Icon, Flag, Map Mode, and Division Symbol Implementation Prompt

Work inside the Chaos Redux repository.

This is not a new event spec. This is a visual asset, UI wiring, and GFX integrity pass for existing Chaos Redux systems.

Before editing, fully read and apply:

- `AGENTS.md`
- every repo skill under `.agents/skills/*/SKILL.md`
- `CHAOS_REDUX_MECHANICS.md`
- the current event, cluster, and scenario catalog files
- relevant existing docs for chemical warfare, biological warfare, zombie outbreak, genocide or Japan decisions, map modes, division templates, and GFX systems
- relevant offline Paradox wiki pages from `paradox_wiki/`
- relevant vanilla HOI4 documentation and vanilla examples from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`

This task touches assets, flags, GFX, GUI, map modes, decision categories, and division template symbols. Do not rely on memory for HOI4 asset wiring. Inspect the exact vanilla and existing Chaos Redux pattern before changing anything.

## Main goal

Finish the missing Chaos Redux visual and GFX work requested below:

1. Add biological operation icons.
2. Fix custom flags that show white lines or bad edge artifacts.
3. Fix custom map modes that are not showing the icons already created.
4. Add two new division template symbols:
   - biowarfare symbol
   - chemical warfare symbol
5. Analyze the project for missing custom GFX.
6. List every missing custom sprite or texture that still needs to be added.
7. Add and wire a Japan chemical campaign against China decision category icon.
8. Add and wire custom zombie outbreak decision category icons.

## Asset routing

Use `chaos-redux-event-assets` as the main asset standard.

For generated icons, use `chaosx_icon_artist` with `fork_context=false` when available. Give it exact asset names, target sizes, source mode, final DDS folders, proposed sprite names, and reference folders.

If icon generation tooling is unavailable, stop and report the blocker. Do not create primitive placeholder icons from local shapes, recolors, resized unrelated assets, or copied focus icons.

Decision icons, decision category icons, idea icons, focus icons, tech icons, and division template symbols must be treated as separate asset types. Do not satisfy one type by resizing another type.

For every new icon or symbol, create or update:

- source PNG
- processed PNG preview
- final DDS
- manifest entry
- contact sheet when useful
- `gfx_handoff.md` when a sprite definition is needed
- final `.gfx` sprite definition
- final gameplay, GUI, map mode, decision category, or division template reference

Use transparent backgrounds where the target UI expects transparency. Validate that final icons have no fake checkerboard, no white halo, no opaque square background, and readable small-size silhouettes.

## Exact icon work

### Biological operation icons

Find the existing biological warfare, bioweapon operation, outbreak operation, strike, raid, stockpile, and containment surfaces. Search the repo for terms such as:

- `bio`
- `biological`
- `bioweapon`
- `outbreak`
- `pathogen`
- `operation`
- `raid`
- `strike`

Create and wire dedicated biological operation icons for existing biological operations that currently use default, missing, or generic icons. At minimum, there must be a generic biological operations icon ready for the system.

Use a period-compatible HOI4 style. Good visual direction: pathogen vial, biohazard-like military stencil, sealed case, laboratory flask, field medical mask, or quarantine seal. Avoid modern flat app-style icons, readable generated text, gore, meme styling, and white outlines.

### Japan chemical campaign against China decision category icon

Find the exact decision category ID for the Japan chemical campaign against China. Add a dedicated decision category icon and wire it to that category.

Use symbolic military chemical warfare imagery. Good visual direction: gas mask, chemical shell, sealed canister, field map of the China theater, or warning-marked military crate. Avoid atrocity photos, gore, readable generated text, modern propaganda style, and generic skull imagery.

Do not create a new decision category unless the existing implementation truly requires it. The target is the icon and GFX wiring for the category.

### Zombie outbreak decision category custom icons

Find all Event 002 Zombie Outbreak decision categories. Add custom decision category icons for every zombie outbreak category that uses a default, missing, or generic icon.

Likely categories to inspect include outbreak management, containment, cure research, horde response, Anti-Zombie League, and world-threat response. Use the exact existing category IDs found in the repo.

Visual direction: zombie hand silhouette, quarantine barricade, infected state marker, broken biohazard seal, cure vial, anti-zombie coalition emblem, or outbreak warning sign without readable generated text.

Do not use one icon for every zombie category unless the repo only has one category. Each distinct category should have a readable visual identity.

## Flag repair

Inspect custom flags in:

- `gfx/flags/`
- `gfx/flags/medium/`
- `gfx/flags/small/`

Find flags with white edge lines, bad borders, upside-down output, malformed TGA origin, wrong dimensions, or damaged ideology variants.

Repair the actual flag files. Do not hide the issue with UI overlays, DDS display copies, scripted localisation, or alternate flag routing.

For every repaired flag, validate:

- normal flag is `82x52`
- medium flag is `41x26`
- small flag is `10x7`
- file output reports Targa data at the correct size
- `file` output does not show `- top`
- no white line is visible in a contact sheet
- base flags are not replaced unless this task specifically requires that flag to be repaired
- ideology variants are not byte-identical unless intentionally shared and documented

Prefer regenerating medium and small flags from a clean normal source when the edge artifact comes from bad resizing.

## Map mode icon fix

Find every custom Chaos Redux map mode and every map mode icon the project expects to show.

Audit:

- map mode definitions
- `.gui` files
- `.gfx` sprite definitions
- texture paths
- localisation keys
- icon references
- the already-created icon files

Fix the reason the created icons are not showing. Likely causes include missing sprite definitions, wrong sprite names, wrong texture paths, wrong file type, wrong dimensions, wrong target `.gfx` file, or map mode definitions pointing at old names.

Use existing created icons where they already exist and are usable. Do not regenerate them unless the file is broken or not game-ready.

## Division template symbols

Add two new division template symbols to the same surface used by HOI4 division template icon selection:

- biowarfare
- chemical warfare

Inspect vanilla division template symbol assets and registry wiring first. Then add Chaos Redux symbols in the correct folder and sprite registry.

Visual direction:

- biowarfare symbol: pathogen vial, biohazard-like seal, quarantine mark, or microscope and flask motif
- chemical warfare symbol: gas mask, chemical shell, gas canister, or toxic cloud shell motif

Both symbols must be separate assets with separate identity. They must be readable in the division template picker and on division template displays.

Wire localisation or tooltip text if the symbol picker uses it.

## Missing custom GFX audit

Analyze the whole project for missing custom GFX.

Build an audit that compares:

- every referenced `GFX_` sprite name
- every `.gfx` sprite definition
- every `.gui` sprite usage
- every decision category icon usage
- every decision icon usage
- every idea, focus, tech, achievement, map mode, and division symbol reference
- every `texturefile` path
- every final DDS or TGA file path
- every texticon reference in localisation where relevant

Report these groups separately:

1. Referenced sprite has no `.gfx` definition.
2. `.gfx` definition points to a missing texture file.
3. Texture exists but has wrong dimensions or wrong type for its UI surface.
4. Asset exists but is not wired to the gameplay or GUI surface that should use it.
5. Custom icon exists but is still not shown due to bad map mode, GUI, or category wiring.
6. Asset is unused and may be stale.
7. Missing sprite or asset is outside this task and must be created later.

Fix every missing or broken GFX item that is clearly in scope for this task. For anything outside scope, list the exact sprite name, expected file path, source file that references it, and recommended asset type.

## Documentation and reports

Create or update asset manifests and handoff notes. Use existing docs folders when the repo already has the correct place. For shared chemical and biological assets, use a clear shared asset docs folder. For zombie outbreak assets, use the Event 002 asset or docs area if it exists.

Update docs that describe the affected systems, especially chemical and biological warfare, zombie outbreak, map mode visuals, or GFX asset coverage.

Do not update the event catalog spreadsheet unless a gameplay-facing player description changed. This task is mostly asset and wiring work.

## Subagents and audits

Use `chaosx_repo_explorer` with `fork_context=false` only if file locations, map mode wiring, or division symbol wiring are unclear.

Use `chaosx_icon_artist` with `fork_context=false` for generated icons and symbols.

Use `chaosx_localisation_auditor` with `fork_context=false` if you add or change visible localisation.

Use `chaosx_event_completion_auditor` only for Event 002 zombie outbreak if the zombie category work reveals broader Event 002 implementation gaps.

Near completion, run a focused final pass against the requested items. If the task has expanded into a meaningful design change instead of asset and wiring cleanup, spawn `chaosx_improvement_loop_planner` with `fork_context=false` and resolve its handoff before completion. If no design change was made, state that this remained a bounded GFX and asset maintenance pass.

## Completion standard

Do not claim completion until:

- all requested icons and division symbols exist as final DDS files
- every new icon and symbol is wired through the correct `.gfx` and gameplay or GUI reference
- map mode icons actually reference the correct sprite names and texture paths
- repaired flags have no white edge artifacts in normal, medium, and small sizes
- the missing custom GFX audit was performed
- the missing sprite list is included in the final report
- asset manifests and handoffs are updated
- relevant docs are updated
- no placeholder, fallback, resized unrelated icon, or primitive local drawing is used
- all simplifications, omissions, and blockers are reported clearly

Final report must include:

- files changed
- assets created or repaired
- sprite names added or fixed
- flag names repaired
- map modes fixed
- division template symbols added
- missing custom GFX list
- meaningful validation performed
- simplifications, omissions, and blockers
