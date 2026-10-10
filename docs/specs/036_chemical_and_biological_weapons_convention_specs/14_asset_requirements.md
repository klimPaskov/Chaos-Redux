# Asset requirements

Production, transparency, processing, DDS conversion, manifests, and handoffs follow [the event-assets skill](../../../.claude/skills/chaos-redux-event-assets/SKILL.md) and the image-generation route in `CLAUDE.md`.
This file owns what Event 036 needs and the visual direction.

The package is static, with no animation, portrait, 3D model, flag, or scripted GUI art.
Every asset row needs a live consumer, and a row whose consumer is cut is removed before production.

## Inventory

| Asset | Working basename | Consumer | Mode |
| --- | --- | --- | --- |
| Opening report image | `036_chemical_biological_convention_report` | Opening and report events | Generated full-canvas scene |
| Decision category picture | `036_cbrn_convention_category_picture` | Decision category | Generated full-canvas scene |
| Decision category icon | `036_cbrn_convention_category_icon` | Decision category | Generated transparent icon |
| Decision and mission icons | See below | Decisions and missions | Generated transparent icons |
| Posture and doctrine idea icons | See below | Ideas | Generated transparent icons |
| Achievement masters and states | Full achievement ids | Achievements | Generated per achievement |

Dimensions come from the inspected consumer: the report image is expected at `210x176`, the category picture at `114x101`, and idea icons at `64x64`.

## Report image

A 1930s or 1940s international conference hall with delegates from several governments, and gas masks, sealed chemical cylinders, laboratory cases, and military folders handled as ordinary objects on the tables.
One clear focal group, muted period photographic treatment.

Avoid readable generated text, modern equipment or clothing, map tables as the subject, science-fiction interfaces, gore, nuclear explosions, and flags whose geometry cannot be controlled.

## Category picture and icon

The picture shows a treaty table with masks, sealed folders, laboratory glass, and delivery-system silhouettes around a central seal without readable text, distinct from the report image, with no painted controls or values.

The icon combines a treaty folio, a gas mask, and a laboratory flask in one readable silhouette.

## Decision and mission icons

1. `036_seek_accession`
2. `036_revise_posture`
3. `036_begin_withdrawal`
4. `036_covert_program`, shared by Begin, Expand, and End Covert Program
5. `036_sponsor_agenda`
6. `036_lobby_ratification`
7. `036_organize_opposition`
8. `036_treaty_obligation`, shared by the Declaration Deadline, Assistance Guarantee, and Doctrine Integration missions
9. `036_industrial_contribution`
10. `036_research_contribution`
11. `036_equipment_contribution`
12. `036_facility_contribution`

Each is drawn for the decision surface with a simple silhouette and limited interior detail, never resized from the category icon or report art.

## Idea icons

1. `036_full_ratification`
2. `036_chemical_accession`
3. `036_retaliation_reservation`
4. `036_integrated_doctrine`

## Achievement assets

One original master per id in [13](13_achievements.md), producing the normal, grey, and not-eligible states with filenames that match the full id directly under `gfx/achievements/`.

## Palette

Dull brass, blackened steel, institutional paper, mask rubber, laboratory glass, muted military green, and restrained red warning accents, readable at small sizes.
No bright modern hazard graphics as the main identity.

## Placement

Runtime files go in event-scoped folders where the consumer accepts explicit paths:

```text
gfx/event_pictures/036_chemical_biological_weapons_convention/
gfx/interface/decisions/036_chemical_biological_weapons_convention/
gfx/interface/ideas/036_chemical_biological_weapons_convention/
```

The `gfx/event_pictures/036_alien_spacecraft/` files move with the alien jet recovery into Event 025 ownership ([01](01_event_identity_and_playable_promise.md#legacy-alien-spacecraft-relocation)).

Temporary source evidence uses `docs/assets/036_chemical_biological_weapons_convention/` and is cleared under the asset skill's workspace rules before completion.
