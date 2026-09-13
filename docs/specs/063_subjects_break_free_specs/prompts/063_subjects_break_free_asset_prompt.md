# Asset prompt: Event 063 Subjects Break Free

Use `chaos-redux-event-assets` for the complete Event 063 visual package. Use `chaosx_generated_event_art` for fictional period documentary scenes and `chaosx_icon_artist` for icons. Follow `AGENTS.md`, the event specs in this folder, and the permanent asset coverage rules.

## Read first

- `docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_6_presentation_assets_achievements_and_acceptance.md`
- `docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_3_network_and_pact.md`
- `docs/specs/063_subjects_break_free_specs/prompts/063_subjects_break_free_achievement_prompt.md`
- `chaos-redux-event-assets`
- the `chaosx_generated_event_art` and `chaosx_icon_artist` role definitions

Inspect the matching canonical reference catalogs, contact sheets, and live consumers before production. If a required contact sheet is missing, create it, label filenames and native dimensions, and update the reference README and catalog before making the new asset family.

For decision-category pictures, inspect:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference\icons\decision_categories\pictures`

The reference family uses `114x101`, but verify the actual consumer before choosing the final canvas.

## Art direction

The event concerns existing governments taking full control from former overlords. Use period documentary scenes, ministries, rail offices, guarded crossings, staff maps, depots, delegates, and formal congress settings. Keep all scenes plausible for the Hearts of Iron IV period without tying the event to one country or one ideology.

Do not generate readable text, real flags as the main subject, modern clothing, modern buildings, fake UI controls, fake meters, or a staged globe covered in national banners. Avoid generic broken-chain clip art for large scene images. Broken chains can appear in small symbolic icons when integrated into a readable composition.

Generated people should be fictional and non-identifiable. Keep uniforms and civilian dress period-appropriate without copying a specific real leader.

## Report and news images

Create these four scene assets:

1. `report_event_063_subjects_break_free`
   - Surface: main Event 063 report
   - Final size: `210x176`
   - Source mode: generated fictional period documentary photograph
   - Direction: local command changing hands at a border post, ministry, rail office, barracks, or port authority. The scene should read as a transfer of authority without requiring text.
   - Process through the standard black-and-white, sepia, grain, paper-border, tilt, transparent-margin, and shadow report-card workflow.
   - Preserve the generated source and the processed RGBA PNG.

2. `news_event_063_coordinated_breakaway`
   - Surface: first coordinated cohort news
   - Final size: `397x153`
   - Source mode: generated fictional period-news photograph
   - Direction: delegates or officers from several newly independent governments coordinating around dispatches and maps.
   - Final treatment: black and white.

3. `news_event_063_independence_war`
   - Surface: first compound independence-war news
   - Final size: `397x153`
   - Source mode: generated fictional period-news photograph
   - Direction: mobilization and divided command at a frontier, rail junction, depot, or port. Show preparation and pressure, not a modern battle montage.
   - Final treatment: black and white.

4. `news_event_063_liberation_pact`
   - Surface: first successful Pact congress
   - Final size: `397x153`
   - Source mode: generated fictional period-news photograph
   - Direction: several delegations exchanging or signing a charter. Keep papers unreadable and do not invent national seals.
   - Final treatment: black and white.

For every scene, inspect crop behavior at final size and reject subjects that become unreadable after conversion.

## Decision-category assets

Create:

- `decision_category_063_liberation_affairs`
  - Small category icon
  - Use the exact native canvas and consumer pattern from the canonical reference
  - Direction: an open chain link combined with a diplomatic document, border seal, or command mark

- `decision_category_picture_063_liberation_affairs`
  - Static category picture
  - Verify the consumer canvas, expected reference family is `114x101`
  - Direction: one strong documentary scene of delegates, border officials, or national command transfer
  - No painted buttons, values, progress bars, labels, or fake interaction

The category picture remains static. Do not create an animation package for it.

## Decision icons

Create one distinct `32x32` icon for each accepted row:

- `decision_063_recognition`
- `decision_063_settlement`
- `decision_063_command`
- `decision_063_frontier`
- `decision_063_guarantee`
- `decision_063_material_aid`
- `decision_063_advisers`
- `decision_063_supply_corridor`
- `decision_063_mediation`
- `decision_063_independence_support`
- `decision_063_congress`
- `decision_063_membership`
- `decision_063_collective_defense`
- `decision_063_ultimatum`

Use the icon directions in Part 6 of the spec. Build a coherent family through shared edge treatment and contrast. Preserve distinct silhouettes so recognition, aid, mediation, frontier preparation, and war entry cannot be confused at native size.

Do not resize one large illustration into all fourteen icons. Each icon needs purpose-built source art or a validated family workflow.

## Idea and cohesion-state icons

Create these `64x64` idea icons:

- `idea_063_contested_sovereignty`
- `idea_063_former_authority_disputed`
- `idea_063_independence_war_mobilization`
- `idea_063_pact_charter_fractured`
- `idea_063_pact_charter_consultative`
- `idea_063_pact_charter_coordinated`
- `idea_063_pact_charter_united`

The four Pact Charter icons are one progression family. Keep the same central composition, camera, palette logic, and framing. Change the degree of connection and completeness across the four states. The progression must remain readable without text.

## Faction emblem

Create `faction_063_liberation_pact` using the canonical faction-emblem consumer and dimensions.

Direction: several open links arranged around a shield or charter. Keep it politically neutral and geographically neutral. Do not use one ideology's emblem, a named country's symbol, or a specific continent outline.

## Achievement triplets

Create completed, grey, and not-eligible `64x64` assets for:

- `chaosx_achievement_063_independence_secured`
- `chaosx_achievement_063_pact_founder`
- `chaosx_achievement_063_independence_war_victory`
- `chaosx_achievement_063_peaceful_release`

Use the icon directions and tracking meaning in the achievement prompt. Treat existing achievement triplets as authoritative state layers. Use:

- `achievement_template.png` for completed state
- `achievement_template_grey.png` for grey and not-eligible state
- the unchanged `overlay.png` for not-eligible state

Record the SHA-256 of the three workflow inputs used.

## Source and processing rules

- Use ImageGen for generated scene and icon source art as required by the asset skill.
- Keep untouched source files.
- Do only deterministic crop, resize, padding, monochrome, sepia, grain, template composition, alpha cleanup, and DDS conversion locally.
- Do not use scripts to create the central artwork from primitive shapes.
- Request genuine transparency for alpha-backed icon families in the initial generation.
- Reject fake checkerboards, matte edges, clipped silhouettes, generated letters, and opaque backgrounds where alpha is required.
- Convert through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.
- Validate final DDS dimensions, alpha behavior, header layout, and live registration.

## Required working evidence

Use the temporary event workspace while production is active:

`docs/assets/063_subjects_break_free/`

Include source art, processed PNGs, previews, contact sheets, manifest, and handoff notes. Before claiming the event fully complete, promote durable source, provenance, hash, runtime-path, sprite, consumer, and review facts into permanent documentation. Verify that no runtime file points into `docs/assets/`, then remove the temporary event workspace.

## Manifest and coverage crosswalk

Create a row for every requirement ID from the Part 6 asset matrix. Each row must record:

- requirement ID
- purpose and surface
- source mode
- ImageGen workflow or source record
- untouched source path and hash
- processed PNG path and hash
- final DDS path and hash
- native and final dimensions
- alpha mode
- sprite or engine registration
- live consumer file and ID
- current status
- review evidence

Build the crosswalk from the accepted requirement list, not from whatever files happen to exist. Extra assets cannot replace a missing accepted row without an explicit design amendment.

## Review gates

Reject or redo any asset when:

- the subject is unclear at native size
- several icons share an ambiguous silhouette
- a scene contains modern or country-specific material that makes it unusable globally
- report-card corners are not transparent
- a news image is left in color
- generated text or fake interface elements remain
- a Pact progression icon does not visibly change state
- an achievement triplet uses the wrong template or altered red overlay
- a final file lacks runtime registration or a live consumer
- the coverage crosswalk has an unresolved accepted row

Do not claim completion with placeholder art, source-only PNGs, missing DDS files, missing hashes, or unwired sprites.
