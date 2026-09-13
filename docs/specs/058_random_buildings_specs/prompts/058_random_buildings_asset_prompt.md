# Asset production prompt for Event 58 Random Buildings

Use this prompt with `chaos-redux-event-assets`, `chaosx_generated_event_art`, and `chaosx_icon_artist`.

Read `AGENTS.md`, the Event 58 specification package under `docs/specs/058_random_buildings_specs/`, the event-assets skill, and only the matching canonical vanilla reference families. Spawn every project subagent with `fork_context=false` and include the exact paths and identifiers below.

## Event report image

Create one generated full-canvas report-event image for Random Buildings.

- Working asset ID: `058_random_buildings_report`
- Intended runtime folder: `gfx/event_pictures/058_random_buildings/`
- Intended source mode: generated period documentary scene
- Target report image treatment: inspect the exact current Chaos Redux report-event precedent and use its verified native canvas and processor
- Proposed sprite role: Event 58 root report image and Event Details image where the shared framework reuses the event picture

### Image direction

Show one coherent 1936 to 1945 landscape undergoing several kinds of construction at once. Useful elements include railway workers, cranes, concrete defenses, a radar mast, an airfield edge, fuel or industrial structures, and a factory skyline. The scene should communicate unexplained simultaneous construction without relying on a map, blueprint overlay, split-screen collage, conference table, or readable sign.

Use period clothing, machinery, vehicles, architecture, photographic technology, contrast, and composition. Avoid modern cranes, hard hats that do not fit the period, contemporary road markings, glass towers, modern military equipment, readable generated text, UI elements, watermarks, and cinematic concept-art color grading.

Keep the source PNG, processed PNG, final DDS, prompt, contact sheet when alternatives are produced, manifest row, and `gfx_handoff.md` entry. The main agent owns final `.gfx` and event wiring.

## Achievement icon set

Create one original completed icon for each planned achievement, plus the exact grey and not-eligible variants required by the existing Chaos Redux achievement system.

Achievement files must follow the root-only `gfx/achievements/` convention and use the full achievement ID as the basename.

### `058_random_buildings_every_plot_accounted_for`

Design direction: a dense period city and industrial landscape divided into orderly construction plots, with every plot visibly completed. Use one strong silhouette. Avoid tiny repeated buildings. No text.

### `058_random_buildings_mixed_use_empire`

Design direction: one coherent construction emblem combining factory, railway, radar or air-defense, and energy or logistics cues. Avoid a grid of unrelated mini-icons. No text.

### `058_random_buildings_the_exceptional_case`

Design direction: one monumental dam, facility, or rare engineered structure framed as a protected prize. Keep the design broad enough to represent several exceptional provider families. No text.

Inspect the canonical achievement reference family and contact sheet before generation. Match the current canvas, border, alpha treatment, contrast, and state-variant workflow. Use native transparency whenever the inspected family requires transparent unused canvas. Preserve alpha through processing and DDS conversion. Background removal is fallback-only and must be documented and edge-validated.

## Ownership limits

Work only on the listed Event 58 asset inventory. Provider-owned structures keep their existing owner assets.

Every building or exceptional provider keeps the assets owned by its source system. If implementation discovers a registered provider with a missing required runtime asset, report it to that owner and mark the provider blocked. Do not invent a generic Event 58 substitute.

## Required handoff

Return:

- every source PNG and prompt
- processed PNG previews
- final DDS files
- dimensions, alpha checks, and hashes
- canonical references inspected
- report-event processor and precedent used
- achievement variant method
- final proposed sprite and texture paths
- manifest and contact-sheet paths
- `gfx_handoff.md`
- completed, blocked, and needs-user-review items
- every simplification or fallback

Do not edit gameplay, event, localisation, GUI, achievement definitions, or spreadsheet files.
