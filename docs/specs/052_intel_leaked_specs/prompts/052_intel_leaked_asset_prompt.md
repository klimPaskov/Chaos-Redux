# Asset Production Prompt for Event 052 Intel Leaked

Create and process the complete authorized visual asset package for Chaos Redux Event 052, Intel Leaked.

Read `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-events`, the Event 52 specification files, this prompt, and the matching canonical reference folders before producing assets.

Use the event's established runtime source slug `052_intelligence_leak` for engine-facing folders and preserve existing sprite identities where possible. Record any necessary identifier change before production.

## Mandatory preflight

The repository already contains:

- `gfx/event_pictures/052_intelligence_leak/report_event_intel_leak.dds`
- `gfx/event_pictures/052_intelligence_leak/news_intel_leak.dds`
- `GFX_report_event_intel_leak`
- `GFX_news_intel_leak`

GitHub reported both DDS paths as 130 bytes. Do not classify them from size alone.

Inspect the exact Git LFS pointer signature, index OIDs, local LFS object availability, and working-file hashes. Run scoped `git lfs checkout` for these two paths when the matching objects are available. Decode and visually inspect the hydrated DDS files before deciding whether they satisfy the new specification.

Preserve acceptable existing art. Replace an asset only when the audit finds a real mismatch, bad crop, unreadable composition, period error, visual defect, broken container, or missing runtime content.

## Canonical references

Use the single reference root:

```text
C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference
```

Inspect:

- `event_art/report/`
- `event_art/news/`
- `icons/decision_categories/`
- `icons/decision_categories/pictures/`
- `icons/decisions/`
- `icons/ideas/`
- `icons/achievements/`
- `CATALOG.md`

Inspect the active vanilla or Chaos Redux consumer before fixing a runtime canvas. The decision-category picture references use a 114 by 101 family, but the live consumer decides the final size.

## Event images

### Target report image

Runtime sprite: `GFX_report_event_intel_leak`

Preferred runtime path: preserve `gfx/event_pictures/052_intelligence_leak/report_event_intel_leak.dds`.

Visual direction:

- 1936 to 1945 documentary realism
- a government or intelligence office under emergency reorganization
- copied files, courier bags, teleprinter tape, code sheets, empty cabinets, and hurried destruction or replacement work
- one clear scene and readable human activity
- the compromised institution is the main subject
- no readable generated text
- no modern devices, modern tactical equipment, or cinematic colour treatment
- no map-led command-table composition

Use generated period-authentic documentary art when replacement is needed because the event is fictional. Retain the full source prompt and output evidence.

### Foreign news image

Runtime sprite: `GFX_news_intel_leak`

Preferred runtime path: preserve `gfx/event_pictures/052_intelligence_leak/news_intel_leak.dds`.

Visual direction:

- international circulation through embassies, ministries, military headquarters, diplomatic bags, or duplicated archives
- a composition distinct from the target report image
- several institutions handling the same kind of material without using a collage or grid
- period-authentic clothing, furniture, communications, and papers
- no readable generated text
- no modern props

## Decision category presentation

Create one decision category icon with native transparent background.

Proposed runtime path:

```text
gfx/interface/decisions/052_intelligence_leak/intelligence_compromise_category.dds
```

Proposed sprite:

```text
GFX_decision_category_052_intelligence_compromise
```

Create one static decision category picture.

Proposed runtime path:

```text
gfx/interface/decisions/052_intelligence_leak/intelligence_compromise_picture.dds
```

Proposed sprite:

```text
GFX_decision_category_picture_052_intelligence_compromise
```

Picture direction:

- open cipher cabinets
- discarded code cards
- teleprinter tape
- emptied file drawers
- burned cover documents
- hands replacing authentication sheets
- clear visual hierarchy at the actual category-picture size
- no painted buttons, meters, labels, or fake controls

## Decision icons

Create separate native-transparent source art and final DDS output for every implemented action.

Required coordinated family:

1. replace codes and authentication tables
2. recall exposed personnel
3. rewrite compromised plans
4. shut down vulnerable channels
5. rebuild cover identities
6. reconstitute foreign networks
7. compartmentalize the archive
8. restore trusted liaison channels
9. seed contradictory orders
10. poison the leak
11. stage a false deployment
12. trace the source

Proposed runtime folder:

```text
gfx/interface/decisions/052_intelligence_leak/
```

Use one strong subject and a clear silhouette for each icon. Do not resize an idea icon or category icon to satisfy a decision icon.

## Status icon

When the implementation uses a visible temporary Compromised Archive idea or status object, create one separate 64 by 64 idea-family icon.

Proposed runtime path:

```text
gfx/interface/ideas/052_intelligence_leak/compromised_archive.dds
```

Do not create this icon unless the final implementation has a real visible consumer.

## Achievement icons

Create completed, grey, and not-eligible variants for:

- `chaosx_052_before_the_ink_dries`
- `chaosx_052_a_better_falsehood`
- `chaosx_052_everyone_knows_everything`
- `chaosx_052_no_names_left_behind`

Achievement DDS files remain in `gfx/achievements/` and match the full achievement IDs.

Use separate source art for each achievement. Apply the repository achievement-state workflow and the verified not-eligible overlay where appropriate.

Icon directions:

- rapid containment: a wet classified page being sealed or burned before copying finishes
- successful deception: a false order layered over a real code sheet with a recipient following the wrong mark
- mutual Total Compromise: two opposing files or mirrored archives with both sides exposed
- personnel protection: erased identity cards or intact silhouettes behind destroyed records

Working labels are not final image text. Do not place words in generated icons.

## Processing and evidence

For generated alpha-backed assets, request genuine transparency in the initial ImageGen call and preserve alpha through processing and DDS conversion. Validate zero-alpha unused pixels, complete painted edges, no white halo, no matte, no fake checkerboard, and no unintended internal holes.

Keep source art, processed PNGs, contact sheets, prompts, dimensions, and manifest evidence in the temporary Event 52 asset workspace while work remains active. Move final DDS files to runtime folders. Record stable sprite handoffs. Before the event is fully complete, promote durable provenance and coverage facts into permanent event documentation and remove the temporary event workspace after confirming that no runtime reference points into it.

Do not edit gameplay, localisation, event, decision, GUI, or spreadsheet files unless the parent grants that exact scope. Return a handoff listing every source, processed PNG, DDS, sprite name, runtime path, reference family inspected, transparency result, visual review result, blocked asset, and remaining parent wiring task.
