# Asset requirements

## Authorized visual package

Event 036 requires a bounded static visual package that supports the opening conference, the decision system, doctrine states, and achievements.

All generated assets use the Chaos Redux asset workflow, matching vanilla references and preserving source evidence, processed previews, final DDS files, manifests, and sprite handoffs.

## Report event image

Working basename: `036_chemical_biological_convention_report`.

Target consumer: Event 036 opening report or country event.

Target canvas: `210x176` when confirmed by the active report-event consumer.

Source mode: generated period-authentic documentary scene.

Visual direction:

- a 1930s or 1940s international conference chamber
- delegates from several governments
- gas masks, sealed chemical cylinders, laboratory cases, protective equipment, and military folders used as real objects in the scene
- a visible separation between diplomatic ceremony and military preparation
- restrained black-and-white or muted period photographic treatment
- one clear focal group

Avoid:

- readable generated treaty text
- modern conference technology
- modern suits, weapons, laboratory equipment, or signage
- a generic map table as the main subject
- science-fiction interfaces
- gore
- a nuclear explosion dominating the image
- flags whose geometry cannot be controlled accurately

The image should communicate that forbidden weapons are being discussed openly as treaty policy.

## Decision category picture

Working basename: `036_cbrn_convention_category_picture`.

Reference family: the canonical decision-category picture references under the event-assets skill.

Expected reference canvas: `114x101`, subject to the active consumer inspection.

Source mode: generated full-canvas scene.

Visual direction:

- treaty table, protective masks, sealed folders, laboratory glass, and delivery-system silhouettes
- clear central treaty seal without readable text
- enough negative space for the category consumer
- distinct from the report event image

The picture is presentation only.

It must not contain fake buttons, fake meters, raw values, or UI controls.

## Decision category icon

Working basename: `036_cbrn_convention_category_icon`.

Source mode: generated transparent icon.

Visual direction: a compact treaty folio combined with a gas mask and laboratory flask, framed as one readable silhouette.

Use genuine native transparency, a dark outline, and a subtle shadow.

Inspect the active category icon consumer for final dimensions.

## Decision icon family

Create separate transparent decision icons for these authorized actions:

1. `036_full_ratification`
2. `036_chemical_accession`
3. `036_retaliation_reservation`
4. `036_public_rejection`
5. `036_covert_preparation`
6. `036_sponsor_agenda`
7. `036_organize_opposition`
8. `036_protective_assistance`
9. `036_inspection_protocol`
10. `036_industrial_contribution`
11. `036_research_contribution`
12. `036_equipment_contribution`
13. `036_facility_contribution`

Each icon must be designed for the decision surface, with simple silhouettes and limited interior detail.

Do not create them by resizing the category icon or report art.

## Idea and doctrine icon family

Create separate `64x64` transparent idea or dynamic-modifier icons when the implementation uses visible ideas for these states:

1. `036_convention_member`
2. `036_retaliation_reservation_member`
3. `036_strategic_wmd_doctrine`
4. `036_exposed_covert_program`

If implementation presents a state entirely through scripted localisation and no visible idea consumes an icon, remove that asset row before production.

Do not produce unused idea art.

## Achievement asset family

Create one original achievement master for each technical achievement ID in `13_achievements.md`:

- `chaosx_036_the_reservation_holds`
- `chaosx_036_a_convention_against_the_convention`
- `chaosx_036_small_state_large_ledger`
- `chaosx_036_without_the_incident`
- `chaosx_036_the_secret_article`
- `chaosx_036_masks_before_missiles`
- `chaosx_036_all_articles_invoked`

Each master produces the normal, grey, and not-eligible triplet through the approved achievement workflow.

The achievement art must remain distinct from decision and idea icons.

## Palette and style

Use a coherent family based on:

- dull brass
- blackened steel
- institutional paper
- mask rubber
- laboratory glass
- muted military green
- restrained red warning accents

The palette should fit HOI4’s period interface and remain readable at small sizes.

Do not use bright modern hazard graphics as the main identity.

## Source and alpha rules

The report image and category picture are full-canvas opaque assets.

Decision, category, idea, and achievement icon families follow the background and alpha treatment of their exact vanilla consumers.

Alpha-backed icons request native transparent backgrounds in the first ImageGen call.

Preserve alpha through processing and DDS conversion.

Background removal is a recorded fallback only when native transparency fails.

## File placement

Place final event-owned assets under event-scoped runtime folders where the consumer accepts explicit paths.

Recommended paths:

```text
gfx/event_pictures/036_chemical_biological_weapons_convention/
gfx/interface/decisions/036_chemical_biological_weapons_convention/
gfx/interface/ideas/036_chemical_biological_weapons_convention/
```

Achievement DDS files remain directly under `gfx/achievements/` and use the full achievement IDs.

Temporary source evidence belongs under:

```text
docs/assets/036_chemical_biological_weapons_convention/
```

Before full event completion, promote durable provenance and runtime crosswalk facts into permanent documentation, verify that no runtime reference points into `docs/assets/`, and remove the complete temporary event workspace.

## Sprite handoff

Register stable sprite names before final production when possible.

The asset handoff must list:

- source PNG
- processed PNG
- final DDS
- final dimensions
- alpha mode
- sprite name
- target `.gfx` file
- gameplay consumer
- source prompt or source URL
- review status
- remaining blockers

## Quality gates

Review every asset at native size and enlarged nearest-neighbor scale.

Check:

- silhouette readability
- centered composition
- correct canvas
- no generated text
- no modern detail
- no opaque square behind transparent icons
- no white halo
- no clipped edges
- no reused icon masquerading as another asset type
- no runtime path into documentation folders
- correct normal, grey, and not-eligible achievement variants
