# Prompt: Event 037 visual asset package

Create the complete authorized visual asset package for Chaos Redux Event 037, Mysterious People.

Read the full Event 037 specification pack, especially Part 7, the event-assets skill, the subagent skill, and the relevant source-manifest and acceptance files. Inspect the canonical skill-local reference library, each matching contact sheet, installed vanilla consumers, and existing Chaos Redux precedents before producing files.

Split actual production by asset owner:

- `chaosx_generated_event_art` for the report image and static decision-category picture
- `chaosx_icon_artist` for category, decision, modifier, state, and achievement art

Each subagent receives a fully explicit prompt with no inherited context. The parent owns final non-portrait sprite wiring and runtime review.

## Visual rule

The anomaly must look documentary, domestic, municipal, and credible. Show people, homes, roads, schools, factories, farms, and established settlements that appear to have existed for years.

Do not imply a canonical explanation. Avoid portals, aliens, cloning equipment, laboratories, time machines, supernatural beams, science-fiction machinery, readable generated text, modern clothing, modern vehicles, maps as the main scene, hostile caricature, disease symbolism, or criminal symbolism.

## Generated full-canvas art

### Report-event image

Working basename:

```text
mysterious_people_report
```

Final event folder:

```text
gfx/event_pictures/037_mysterious_people/
```

Inspect the active report-event family and verify the final canvas. The planning reference is `210x176`.

Create a period-authentic 1936 to 1945 documentary scene showing a newly populated settlement with families, complete homes, ordinary local work, and physical signs of an established community. Use monochrome or restrained sepia treatment matching the verified report precedent.

The image must remain useful for baseline and evolved manifestations.

### Decision-category picture

Working basename:

```text
mysterious_people_category
```

Final event folder:

```text
gfx/interface/decisions/037_mysterious_people/
```

Inspect the canonical decision-category picture family and the exact runtime consumer. The reference family uses `114x101`, which is not an automatic final size.

Show a crowded district, settlement office, or local service scene. Do not paint controls, buttons, values, labels, or meters into the image.

Both full-canvas assets keep the opaque or painted background treatment required by their consumers.

## Transparent icon package

Request genuine native transparency in the first ImageGen call for every alpha-backed icon. Preserve alpha through processing and DDS conversion. Reject white matte, fake checkerboard, halo, opaque square, clipped edge, or internal transparent hole.

Create separate source art for every asset type. A resized report image, focus icon, category icon, or other icon cannot satisfy another surface.

### Category icon

Working basename:

```text
mysterious_people_category_icon
```

Direction: a compact civilian group beside a house, registry book, or settlement marker.

### Decision icons

Create separate source art for:

- `mysterious_people_population_office`
- `mysterious_people_housing_program`
- `mysterious_people_services_program`
- `mysterious_people_planned_settlement`
- `mysterious_people_workforce_integration`
- `mysterious_people_military_logistics`
- `mysterious_people_foreign_relief`
- `mysterious_people_restrictive_registry`
- `mysterious_people_closed_zone`
- `mysterious_people_origin_classification`

Inspect the exact decision-icon consumer and final size. Keep one strong subject and readable silhouette.

Shared Famine, Migration, Camp, and Condemnation actions should reuse established art only after a semantic consumer audit. Do not create neutral Event 037 replacements for forced relocation, forced labor, extermination, or other actions owned by those systems.

### Modifier icons

Create separate source art for:

- `mysterious_people_demographic_dividend`
- `mysterious_people_state_pressure`

Inspect whether each consumer is an idea, dynamic modifier, state modifier, or another verified family. Do not assume one canvas for both.

Dividend direction: integrated workforce, active settlement, factory and farm capacity.

Pressure direction: compressed housing, crowded road, strained utilities.

## Achievement triplets

Create full achievement triplets in `gfx/achievements/` using filenames matching these exact achievement IDs:

- `chaos_redux_037_room_for_everyone`
- `chaos_redux_037_a_billion_more`
- `chaos_redux_037_three_censuses`

For each, provide normal, grey, and not-eligible DDS files according to the established suffix convention and overlay workflow.

Use separate source art:

- Room for Everyone: orderly dense settlement and open civic capacity
- A Billion More: immense integrated population across city, farm, and industry
- Three Censuses: three layered household records paired with growing settlement

Do not generate readable lettering.

## Evidence and packaging

Use the temporary workspace:

```text
docs/assets/037_mysterious_people/
```

Keep source PNGs, prompts, processed previews, contact sheets, transparency checks, dimensions, manifests, provenance, and `gfx_handoff.md`.

Place final DDS files in verified runtime folders. The handoff must list:

- asset type
- source mode
- exact prompt
- source and final paths
- native dimensions
- alpha treatment
- DDS format
- proposed sprite name
- target `.gfx` consumer
- contact-sheet path
- review status
- unresolved blockers

Before final event completion, the parent must promote durable provenance and crosswalk facts, verify no runtime reference points into `docs/assets/`, and delete the complete temporary event workspace. Keep it when work remains blocked or under review.

Do not create portraits, flags, focus icons, animation, 3D models, sound, or additional assets outside the accepted inventory.
