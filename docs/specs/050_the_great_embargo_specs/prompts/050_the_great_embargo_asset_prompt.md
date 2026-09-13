# Event 050 asset-production prompt

Create the complete static visual package for Event 050, The Great Embargo.

Read `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-frame-animation` for the static-versus-animation boundary, the Event 50 presentation spec, asset matrix, achievement matrix, and relevant vanilla reference catalog.

Create exactly the static asset inventory below. Any additional asset family requires an accepted source-spec change.

## Reference inspection

Use the canonical reference root under the event-assets skill and inspect:

- `event_art/report/`
- `icons/decision_categories/`
- `icons/decision_categories/pictures/`
- `icons/decisions/`
- `icons/missions/`
- `icons/ideas/`
- `icons/achievements/`

The category-picture folder needs its own labelled `contact_sheet.png`. If absent, create it from the reference images and update the reference README and catalog before Event 50 production. Reference art is review material and cannot be shipped, traced, recolored, or wired.

## Required report images

Create three generated period documentary scenes at `210x176`:

1. `050_great_embargo_opening_isolation`
   - halted port or freight shipments
   - idle cranes or railcars
   - customs inspection and waiting crews
   - strong visual absence of normal trade

2. `050_great_embargo_secondary_sanctions`
   - neutral cargo under certificate, manifest, insurance, or customs scrutiny
   - pressure on an intermediary route
   - no readable generated documents

3. `050_great_embargo_fragmented_trade`
   - rerouted cargo through crowded neutral transfer points
   - several competing markings or guarded routes
   - overlapping embargo systems without a map diagram

Use 1936 to 1945 photographic technology, clothing, architecture, vehicles, and freight equipment. Avoid modern containers, electronics, clothing, ports, paperwork design, cinematic color grading, readable generated text, flags that imply one fixed target, and map-table compositions.

## Decision category picture

Create one static full-canvas category picture under a stable Event 50 basename. Verify the active consumer dimensions. The reference family near `114x101` is guidance only.

Show an idle port or freight yard with sealed cargo and interrupted movement. Do not paint buttons, meters, labels, maps, or fake controls.

## Native-transparent icons

Create original separate source art for:

- category icon
- Self-Sufficiency decision
- Smuggling Networks decision
- Neutral Intermediaries decision
- Diplomatic Concessions decision
- Defy the World decision
- Resource Seizure decision
- Secure Replacement Supply mission
- active Great Embargo national spirit
- five achievement completed icons

Decision, mission, and category icons target `32x32`. The national spirit and achievement icons target `64x64`.

Request genuine transparency in the initial ImageGen call. Preserve alpha through processing and DDS conversion. Require transparent unused canvas, a readable centered silhouette, dark outline, subtle shadow, no white matte, no checkerboard, no square opaque backdrop, and no transparent holes.

Each asset type needs its own brief and source output. Do not resize a decision icon to satisfy the idea or achievement surface.

## Achievement variants

For each completed `64x64` achievement icon, create grey and not-eligible variants through the approved achievement workflow. Keep the source completed art and variant provenance.

## Working paths and handoff

Use `docs/assets/050_the_great_embargo/` as the temporary evidence workspace while implementation is active. Place final runtime DDS files in event-scoped engine folders with stable names. Do not leave runtime references under `docs/assets/`.

Produce:

- source PNGs
- processed PNGs
- final DDS files
- contact sheets
- manifest with prompt and source mode
- dimension and alpha QA
- proposed sprite names
- `gfx_handoff.md`

Do not edit gameplay, event, decision, GUI, localisation, workbook, or broad GFX files unless the parent grants a narrow exception. Report blocked assets instead of substituting placeholders.
