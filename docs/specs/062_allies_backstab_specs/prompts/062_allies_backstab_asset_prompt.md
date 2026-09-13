# Event 062 asset production prompt

Work on Chaos Redux Event 62, Allies Backstab.

Read these source files first:

- `docs/specs/062_allies_backstab_specs/README.md`
- every file under `docs/specs/062_allies_backstab_specs/specs/`
- `docs/specs/062_allies_backstab_specs/quality/062_allies_backstab_acceptance_scenarios.md`
- `AGENTS.md`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation` only to confirm that no animation is authorized
- `chaos-redux-subagents`

Use project subagents with no inherited parent context. In Codex, set `fork_context=false`.

## Accepted asset boundary

Create only the assets listed here. Do not invent portraits, flags, focus icons, country art, technologies, equipment art, units, 3D models, counters, unit audio, scripted GUI panels, or animation.

Character portrait work is absent. Do not route anything to `chaosx_portrait_creator`.

## Split of work

Route full-canvas generated scene art to `chaosx_generated_event_art`:

1. main Event 62 report image
2. static Event 62 decision-category picture
3. conditional Evolution III super-event image

Route alpha-backed gameplay icons to `chaosx_icon_artist`:

1. decision icons
2. mission icons
3. idea and national-spirit icons
4. achievement completed icons and their standard variants

Asset workers may create source files, processed PNG files, final DDS files, contact sheets, manifests, and a GFX handoff. They must not edit gameplay, localisation, event, decision, GUI, focus, country, or spreadsheet files.

## Mandatory reference inspection

Before production, inspect:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`
- the matching contact sheet for every asset family
- exact installed vanilla and current Chaos Redux sprite consumers

Use the consumer inspection to lock sizes and DDS formats. The planning sizes below are expected references, not permission to skip inspection.

## Full-canvas scene art

### Main report image

- planned canvas: `210x176`
- source mode: generated
- visual mode: 1936 to 1945 documentary photograph
- subject: allied liaison officers, military guards, and removed partner insignia at a faction headquarters or checkpoint
- physical evidence: a gate being sealed, insignia coming down, liaison officers escorted out, documents and access passes surrendered
- composition: one clear betrayal scene with readable people and military setting
- avoid: maps as the main subject, generic conference tables, modern uniforms, modern weapons, cinematic color grading, readable generated text, flags that require exact historical reconstruction, gore, caricature
- full-canvas opaque treatment

### Decision category picture

- planned reference canvas: `114x101`, verify the active consumer
- source mode: generated
- subject: a war council or alliance headquarters after a rupture, with empty chairs, removed insignia, guarded doors, and severed liaison presence
- use: static category identity only
- avoid: fake buttons, fake meters, ledger columns, interface labels, readable text, map arrows, decorative UI controls
- full-canvas opaque treatment

### Evolution III super-event image

- planned canvas: `457x328`
- source mode: generated
- visual mode: period documentary or grounded alternate-history press photograph
- subject: several military delegations and alliance symbols separating into rival armed groups in one coherent scene
- meaning: simultaneous collapse of several major alliances
- avoid: one small bilateral quarrel, abstract geometry, a world map as the main composition, modern equipment, readable text, spectacle without people or institutions
- full-canvas opaque treatment

## Decision icon list

Create distinct source art for each icon:

- broken alliance emblem
- war council commitment
- emergency mobilization
- expelled-governments liaison
- foreign guarantee
- conditional readmission
- recognized separation
- faction defection
- neutral withdrawal
- successor compact

Use the exact current decision-icon canvas, expected around `32x32` only after consumer inspection. Request native transparent background in the first ImageGen call. Preserve alpha. Use one clear subject, strong silhouette, dark outline, subtle shadow, and no opaque square.

## Mission icon list

Create distinct mission-specific art:

- capital and supply-spine defense
- punitive offensive
- co-victim connection
- prevent a second defection
- armistice conference

Inspect the mission icon family separately. Do not resize decision icons into mission icons.

## Idea icon list

Create distinct `64x64` style idea art after exact consumer inspection:

- betrayed by the bloc
- war council purge
- expelled-governments liaison
- coordinated defense
- isolated government

The icons should read as national-spirit art, not decision icons with extra padding.

## Achievement icon list

Create completed icons for:

- The Weak Link Holds
- Council of the Cast Out
- No Second Betrayal
- A Seat of Our Own

Each achievement needs the current completed, grey, and not-eligible triplet. Follow root-only achievement placement and exact achievement IDs supplied by the implementation parent. Use separate source art for each achievement.

## Working paths

Use the temporary workspace:

`docs/assets/062_allies_backstab/`

Recommended subdivisions:

- `event_art/`
- `decision_category/`
- `icons/decisions/`
- `icons/missions/`
- `icons/ideas/`
- `icons/achievements/`
- `super_event/`
- `manifests/`

Final runtime files must move to event-scoped engine folders according to the asset skill. Achievement files remain in the required achievement root.

## Output requirements

For every asset provide:

- source PNG or source atlas
- prompt and source mode
- processed PNG
- final DDS
- exact native dimensions
- alpha validation for transparent families
- contact sheet
- manifest row
- proposed sprite name and runtime path
- review status
- unresolved blocker

Write `gfx_handoff.md` with ready-to-review sprite names and paths. Do not wire the sprites.

## Quality gates

Reject any asset with:

- opaque square background where alpha is required
- white halo, fake checkerboard, or clipped silhouette
- unreadable small detail
- modern or era-incompatible scene elements
- generated text
- wrong asset-family style
- one source image resized across different icon types
- primitive local geometry used as final art
- visual drift from the accepted Event 62 identity

Retain the temporary workspace while implementation is active or blocked. Before the parent claims full completion, durable provenance and coverage must be promoted into permanent documentation, runtime references must be verified, and the event workspace must be deleted according to project rules.
