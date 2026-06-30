# Event 011 Secret Alliance Asset Prompt

Use this prompt with the Chaos Redux event asset workflow. Inspect the matching reference folders before creating or processing any asset. Do not derive focus, idea, decision, or achievement icons by resizing another asset type.

## Asset package path

Recommended working package:

`docs/assets/011_secret_alliance/`

Final DDS files should be placed in the appropriate gameplay asset folders, not left only under docs.

## Visual identity

The visual identity is covert diplomacy, a hidden hostile compact, intercepted evidence, and a public pact reveal. Use period-authentic 1936 to 1945 documentary mood for event images. Use clean symbolic icons for decisions and ideas. Avoid modern spy gadgets, modern computer screens, readable generated text, and generic map-only compositions.

## Report event images

| Asset working name | Type | Target size | Source mode | Direction |
| --- | --- | ---: | --- | --- |
| report_event_secret_alliance_first_meeting | Report event image | 210x176 | Generated period documentary | A hotel corridor, quiet diplomatic reception, or small back-room table with several minor delegations. No readable text. The emotional subject is secrecy and shared glances, not a map. |
| report_event_secret_alliance_courier | Report event image | 210x176 | Generated or sourced if a suitable public-domain courier image is found | A courier case, rail platform, embassy car, or intercepted diplomatic pouch in period style. |
| report_event_secret_alliance_sabotage | Report event image | 210x176 | Generated period documentary | Damaged factory floor, missing parts, and investigators. Avoid gore and avoid modern machinery. |
| report_event_secret_alliance_border_incident | Report event image | 210x176 | Generated period documentary | Border guards, roadblock, or rural checkpoint with tension. No final war scene. |
| report_event_secret_alliance_public_compact | Report event image | 210x176 | Generated period press style | Public diplomatic signing or press hall with several flags implied. Use no readable text. |

All report images must receive the repository report-card treatment and final DDS conversion.

## Super-event image

| Asset working name | Type | Target size | Source mode | Direction |
| --- | --- | ---: | --- | --- |
| super_event_secret_alliance_public_reveal | Super-event image | 457x328 | Generated | A dramatic period press photograph or painted documentary scene of a public anti-target pact reveal. Several delegations stand behind a table, lights and cameras face them, and the scene feels like secrecy becoming public military coordination. No readable text. Avoid generic apocalypse framing. |

## Decision category and decision icons

Inspect decision references before generating.

| Asset working name | Type | Target size | Source mode | Direction |
| --- | --- | ---: | --- | --- |
| decision_category_secret_alliance_dossier | Decision category icon | Existing category pattern | Generated icon | Sealed dossier, crossed diplomatic cords, and a small shadowed pact seal. Strong silhouette. |
| decision_secret_alliance_trace_couriers | Decision icon | 32x32 | Generated icon | Courier pouch or envelope under a magnifying lens. |
| decision_secret_alliance_guard_factories | Decision icon | 32x32 | Generated icon | Guard helmet over factory gear. |
| decision_secret_alliance_expose_member | Decision icon | 32x32 | Generated icon | Broken seal or spotlight on a mask. |
| decision_secret_alliance_split_member | Decision icon | 32x32 | Generated icon | Snapped chain link beside two small flags without text. |
| decision_secret_alliance_border_patrol | Decision icon | 32x32 | Generated icon | Border post and patrol helmet. |
| decision_secret_alliance_war_cabinet | Decision icon | 32x32 | Generated icon | War room folder with crossed pens and a small shield. |

## Idea and national spirit icons

Inspect idea references before generating.

| Asset working name | Type | Target size | Source mode | Direction |
| --- | --- | ---: | --- | --- |
| idea_secret_alliance_shadow_pressure | National spirit icon | 64x64 | Generated icon | Shadowed hands around a small diplomatic seal. |
| idea_secret_alliance_counterintelligence_desk | National spirit icon | 64x64 | Generated icon | Desk lamp, files, and intercepted cord. |
| idea_secret_alliance_public_isolation | National spirit icon | 64x64 | Generated icon | Diplomatic door closing with a flag outside. |
| idea_secret_alliance_prepared_state | National spirit icon | 64x64 | Generated icon | Shield over rail and factory symbols. |
| idea_secret_alliance_pact_coordination | National spirit icon | 64x64 | Generated icon | Three clasped hands around a concealed blade, no gore. |

## Faction emblem and UI assets

| Asset working name | Type | Target size | Source mode | Direction |
| --- | --- | ---: | --- | --- |
| secret_alliance_faction_emblem | Faction emblem | Existing faction emblem pattern | Generated symbolic art | A generic anti-target compact seal with three points around an empty center. It must not include generated letters. |
| secret_alliance_dossier_panel | Scripted GUI panel background | Existing custom UI size from implementation | Generated UI art with later UI slicing | Dossier board with pinned photographs, cords, stamp marks, and empty card zones. No readable text. |
| secret_alliance_member_card_unknown | Scripted GUI card | Implementation target size | Generated or UI authored | Masked country card state for unknown member. |
| secret_alliance_member_card_identified | Scripted GUI card | Implementation target size | Generated or UI authored | Identified card state with clear border, no text baked in. |
| secret_alliance_warning_frame | Scripted GUI frame | Implementation target size | Generated frame art | Warning border for high aggression or war timer. |

## Animated assets

Use the frame animation skill. Every animated asset needs real source frames, static fallback DDS, horizontal sheet DDS, contact sheet, and preview GIF for review only.

| Animated asset | Surface | Target | Frames | Loop | Direction |
| --- | --- | --- | ---: | --- | --- |
| secret_alliance_dossier_warning_frame_animated | Dossier GUI warning frame | Implementation size | 6 to 8 | Slow loop | Period paper edge and faint warning pulse drawn in separate source frames. State-driven when pact aggression or war readiness is high. |
| secret_alliance_faction_emblem_animated | Public compact reveal UI or super-event adjacent UI | Existing emblem size | 8 | Slow loop | Emblem seal gains visible pressure and ink-darkening across real frames. Static fallback must remain readable. |
| secret_alliance_member_card_new_evidence_animated | Dossier selected target card | Implementation card size | 6 | Short loop | Evidence tabs, strings, or stamp marks become visibly active. Use only when a member has new evidence. |

Do not create final animation by shifting, recoloring, blurring, or pulsing one still image.

## Achievement icons

Create completed 64x64 achievement icons first. Grey and not-eligible variants can be derived according to the achievement workflow.

| Working key | Icon direction |
| --- | --- |
| secret_alliance_paper_trail | Dossier thread connecting three hidden seals |
| secret_alliance_no_public_war | Broken pact seal without weapons |
| secret_alliance_lonely_crown | Lone shield facing three small hostile banners |
| secret_alliance_turn_the_room | One hand pulling a chair away from a pact table |
| secret_alliance_open_files | Open cabinet with every file lit |
| secret_alliance_against_the_wall | Fortified capital silhouette under converging arrows |
| secret_alliance_border_spark | Border marker with contained sparks and a shield |

## Manifest requirements

The manifest must list source mode, prompt, source path, processed PNG path, final DDS path, target size, sprite name, GFX target, related event id, related decision or idea id, and animation frame metadata where relevant.
