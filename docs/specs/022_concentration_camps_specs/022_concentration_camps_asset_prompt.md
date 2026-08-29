# Asset Production Prompt for Event 22 Concentration Camps

## Task

Create, source, process, convert, review, and document the accepted visual assets for Event 22, `Concentration Camps`.

This task uses two bounded subagents:

1. `chaosx_asset_source_researcher` for archival event, news, and decision-category pictures
2. `chaosx_icon_artist` for decision, mission, category, idea, state-modifier, and achievement icons

Use `fork_context=false`. Each subagent prompt must repeat its exact scope, inputs, outputs, exclusions, and handoff path.

Do not generate or edit gameplay, localisation, event, decision, GUI, focus, country, spreadsheet, or shared registry files. Final `.gfx` wiring remains with the parent implementation agent unless the parent explicitly grants one named entry.

## Required reading

Read before asset work:

- repository `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- Event 22 index and all five specification parts
- `022_concentration_camps_asset_manifest.md`
- `022_concentration_camps_achievements.md`
- `022_concentration_camps_research_notes.md`
- current live Event 22 and camp-building assets
- current GFX definitions and consumers for event reports, news, categories, decisions, missions, ideas, state modifiers, and achievements

No animation is authorized. Do not start a frame-animation workflow.

## Visual standard

This is a grounded atrocity and humanitarian-crisis system. Use documentary restraint.

Prohibited:

- graphic bodies or gore
- generated victims or fake archival photographs
- staged killing scenes
- fake quotations or fake archive text
- horror spectacle
- celebratory perpetrator imagery
- decorative animation
- skull-heavy or gamey extermination symbols
- unrelated regime symbols used as generic branding
- white matte around transparent icons

Archival images can show gates, fences, barracks, transport, forced labour with defensible provenance, records, investigators, relief, displaced-person facilities, or tribunals. Every image must be non-graphic and correctly identified.

Generated icons must be symbolic, centered, readable at native size, transparent, text-free, and matched to the correct current vanilla reference family.

## Archival-source subagent scope

### Required outputs

Source and process these required assets:

- main management decision-category picture
- network-activation report image, `210x176`
- forced-labour report image, `210x176`
- extermination-escalation report image, `210x176`
- evidence-discovery report image, `210x176`
- liberation-relief report image, `210x176`
- verified-network news image, `397x153`, black and white
- major-liberation news image, `397x153`, black and white

Recommended if defensible sources are found:

- closure-aftermath report image, `210x176`
- accountability news image, `397x153`, black and white

### Reference inspection

Inspect:

```text
.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/
.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/news/
.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/
```

The decision-category-picture folder must contain `contact_sheet.png` labelled with filenames and native dimensions. If missing, create it and update the reference README and catalog before selecting the Event 22 size.

Inspect one live Chaos Redux decision category that uses a picture. Record the exact native dimensions and layout. Do not guess.

### Source requirements

Use archives, museums, libraries, or government repositories. For every candidate record:

- title or identifying description
- institution
- place and date where known
- source page
- creator where known
- licence or public-domain basis
- download date
- original filename
- checksum
- proposed Event 22 use
- whether the photograph is exact or representative

Reject unidentified, watermarked commercial, low-resolution, miscaptioned, graphic, or legally unclear candidates.

Do not use one named camp photograph as an exact depiction of another named country or state. Generic campaign use can be representative when provenance says so.

### Processing

- preserve the original download
- use crop, resize, tonal correction, and format conversion only
- do not use generative restoration or object replacement
- keep a processed PNG preview
- convert through repository DDS tools
- compare native-size output against reference family
- produce one contact sheet for report and news finals
- produce one category-picture layout preview showing the actual text and control-safe regions

### Handoff

Write:

```text
docs/assets/022_concentration_camps/archival_asset_handoff.md
```

Include final paths, checksums, source facts, licence facts, crop notes, sprite recommendations, runtime consumers, rejected candidates, and remaining blockers.

## Icon subagent scope

### Category icons

Create:

- `022_category_icon_management`
- `022_category_icon_relief`

Target `32x32` unless current repository precedent proves another size.

### Decision and mission icons

Create or deliberately reuse a verified close family for:

- closure
- review and registration
- food and medical relief
- forced labour
- industrial assignment
- construction assignment
- extraction assignment
- logistics and transfer
- network expansion
- guard reinforcement
- evidence preservation
- cover-up
- escape and resistance
- epidemic
- extermination conversion or halt
- restricted chemical site
- retreat and evacuation
- liberation
- resettlement
- tribunal

Target `32x32`.

Do not create one icon for every small button when the same role is clear. Document every reuse.

### Idea icons

Create the eight `64x64` families from the manifest:

- administrative burden
- forced-labour war economy
- security apparatus ascendant
- network under review
- dismantlement program
- publicly exposed atrocities
- survivor relief and resettlement
- tribunal and documentation pressure

### State-modifier icons

Create only the state-status icons required by final implementation. Start from the manifest list. Reuse a decision or idea icon only when it remains unambiguous at the state surface.

### Achievement icons

Create completed `64x64` masters for every accepted achievement in `022_concentration_camps_achievements.md`. Produce grey and not-eligible states through the shared achievement workflow and overlay.

Achievements must remain symbolic. No victim, corpse, gas-chamber, or execution imagery.

### Existing building audit

Audit current runtime icons for:

- `concentration_camp`
- `extermination_camp`
- `gulag_labor_camp_network`

Do not replace them unless they are missing, unreadable, visually identical, or technically invalid. Report findings first. A replacement needs parent approval.

### Icon workflow

- inspect the correct reference folder and contact sheet
- generate the completed master through ImageGen
- preserve source evidence and prompt record
- process mechanically only
- keep transparent background
- inspect native size and `4x`
- verify center, padding, silhouette, frame ownership, and palette
- convert through repository tools
- create labelled contact sheets by asset family
- document exact sprite name recommendations

### Handoff

Write:

```text
docs/assets/022_concentration_camps/icon_asset_handoff.md
```

Include every asset ID, source mode, source evidence, checksums, dimensions, file paths, sprite recommendation, runtime consumer, review result, reuse decision, and blocker.

## Final parent review

The parent agent must review:

- source and licence evidence
- category-picture native dimensions
- non-graphic suitability
- native and `4x` visuals
- report and news crops
- transparent backgrounds
- no white matte
- decision-category layout safety
- building-icon reuse decision
- achievement state ladder
- final DDS paths and checksums

The parent then performs `.gfx` wiring, repository validation, and live runtime checks.

## Completion report

Return:

- assets completed
- assets reused
- rejected candidates and reasons
- source and licence status
- final file paths and checksums
- contact-sheet paths
- handoff paths
- assets blocked
- exact dimension or source issues
- validation completed
- validation skipped and why

Do not claim the Event 22 asset package complete while a required archival source, licence, native dimension, transparent icon, final DDS, or runtime consumer remains unresolved.
