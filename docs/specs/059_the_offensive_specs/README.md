# Event 059: The Offensive

This folder is the source-of-truth planning package for the rework of Event 059.

## Accepted catalog identity

| Field | Accepted value |
| --- | --- |
| Event ID | `59` |
| Event name | The Offensive |
| Slug | `059_the_offensive` |
| Type | Minor Fire-Once |
| Minimum Chaos level | 1 |
| Primary cluster | Diplomacy |
| Member severity | High |
| Cluster role and chance | Authoritative Diplomacy defaults after registry inspection |
| Status after implementation | Needs Testing |

The supplied CSV snapshot still uses the superseded cluster name Diplomatic Panic. A later accepted cluster update merges that identity into Diplomacy and assigns Event 59 to Diplomacy with High member severity. This package follows the later instruction. The numeric cluster ID, required or optional role, participation chance when relevant, and member minimum tier must be read from the authoritative registry during implementation.

## Read order

1. `specs/059_the_offensive_spec_part_1_core.md`
2. `specs/059_the_offensive_spec_part_2_ai_strategy.md`
3. `specs/059_the_offensive_spec_part_3_evolutions.md`
4. `specs/059_the_offensive_spec_part_4_interactions_and_edge_cases.md`
5. `specs/059_the_offensive_spec_part_5_presentation_and_assets.md`
6. The matrices under `matrices/`
7. The implementation prompts under `prompts/`
8. The design and audit records under `quality/`
9. The implementation handoff under `docs/plans/059_the_offensive_plans/`

## Core design in one paragraph

The Offensive is a permanent global change to AI strategic behavior. It does not give direct combat, production, research, organisation, planning, or supply bonuses. AI countries become more willing to prepare, launch, support, and sustain sensible offensive operations. Higher evolutions add operational persistence, predatory use of legal war opportunities, and greater multi-theater risk. Human-controlled countries never use the event's AI strategy layers. The behavior follows current control, including player takeover, handback to AI, hotjoin, released countries, civil-war tags, and countries created later in the campaign.

## Package boundary

This package defines design, balance intent, AI scenarios, evolution pacing, presentation direction, asset requirements, achievement requirements, Chaos feedback, and acceptance criteria. It does not contain gameplay code, final localisation, final art, workbook edits, or live-game validation.
