# Event 007 Fury Asset Plan

## Source mode summary

Fury is a dynamic fictional or alternate-history event. Most assets should be generated symbolic assets. Do not source or generate real leader portraits for existing selected countries. Existing country flags are preserved.

## Required assets

| Asset | Type | Size | Source mode | Direction |
| --- | --- | --- | --- | --- |
| `idea_fury_impetus` | idea icon | 64x64 | generated | crossed border posts, urgent arrows, dark military seal |
| `idea_fury_veteran_impetus` | idea icon | 64x64 | generated | worn campaign banner and veteran stripe motif |
| `idea_fury_joint_command` | idea icon | 64x64 | generated | linked campaign maps or two small flags bound by orders |
| `idea_fury_all_front_command` | idea icon | 64x64 | generated | several arrows leaving one map table |
| `idea_fury_continental_mandate` | idea icon | 64x64 | generated | continent outline, command stamp, guarded border |
| `decision_category_fury_campaign` | category icon | 32x32 or repo pattern | generated | small war-room seal, readable at small size |
| `decision_fury_next_war` | decision icon | 32x32 | generated | sealed order crossing a border |
| `decision_fury_depot` | decision icon | 32x32 | generated | crates, rail marker, military stamp |
| `decision_fury_administration` | decision icon | 32x32 | generated | desk stamp and occupied province map |
| `decision_fury_core` | decision icon | 32x32 | generated | map pin becoming a state seal |
| `decision_fury_coordination` | decision icon | 32x32 | generated | linked arrows between two command tables |
| `decision_fury_world_end` | decision icon | 32x32 | generated | borderless map with warning seal |
| `faction_fury_pact` | faction emblem | repo pattern | generated | stark pact emblem with map arrows, no text |
| `news_event_fury_first_victory` | news event image | 397x153 black and white | generated | troops entering a small capital or border checkpoint |
| `super_event_fury_major` | super-event image | 457x328 | generated | small-state command room becoming a major war office |
| `super_event_fury_world_end` | super-event image | 457x328 | generated | several continents marked by military arrows, no readable text |
| `leader_fury_staff_council` | optional portrait | 156x210 | generated | fictional council portrait for high-chaos staff rule |

## Focus icon families

A shared focus tree can use family icon reuse if documented. Required motifs:

- border mobilization
- surprise orders
- military staff takeover
- civil administration
- depot seizure
- captured industry
- rail and supply expansion
- occupation integration
- partner coordination
- all-front assault
- no-neighbor consolidation
- world-end export branch

Focus icons should be 94x86 and follow HOI4 focus icon style.

## Animation optional note

No final animated asset is required for the baseline spec. If implementation adds a scripted GUI or animated Fury emblem, animation must use real planned source frames, a horizontal frame sheet, a static fallback, and a GIF only as preview.

## Asset acceptance rules

- Preserve existing country flags.
- Do not create flags for every possible Fury country.
- Do not generate portraits for real existing leaders.
- Generated report, news, and super-event images should use period documentary composition and avoid readable text.
- Every final asset needs source PNG, processed PNG, DDS, manifest entry, and sprite handoff.
