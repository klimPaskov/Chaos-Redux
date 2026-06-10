# Asset prompt for Event 007 Fury

Use `chaos-redux-event-assets` for this package. If any animated asset is requested later, use `chaos-redux-frame-animation` as well. Inspect the relevant reference folders before creating or processing assets.

Event ID: `7`
Event slug: `fury`
Working asset folder: `docs/assets/007_fury/`

## Source mode summary

Fury is a fictional dynamic war mechanic. Most visuals should be generated or symbolic, not sourced from real people.

Use generated art for:

- idea icons.
- focus icons.
- decision icons.
- achievement icons.
- faction emblem.
- optional institutional leader portrait.
- news image for first conquest.
- report images.
- super-event images.

Use real sourced imagery only if the implementation later chooses a real historical quote source that requires an archival image. Do not create real leader portraits for actual people in this package.

## Required reference folders

Inspect these before work:

- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/ideas`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/focuses`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/decisions`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/achievements`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/flags`

## Idea and national spirit icons, 64x64

Create HOI4-style idea icons with strong silhouettes and no generated text.

| Asset | Suggested file | Sprite | Direction |
| --- | --- | --- | --- |
| National Fury | `idea_fury_national_fury.dds` | `GFX_idea_fury_national_fury` | red map pin over a small border table, no text |
| Hardened Fury | `idea_fury_hardened_fury.dds` | `GFX_idea_fury_hardened_fury` | reinforced marching column symbol |
| Fury Overextension | `idea_fury_overextension.dds` | `GFX_idea_fury_overextension` | strained map with too many pins and snapped ruler |
| Compliance Drive | `idea_fury_compliance_drive.dds` | `GFX_idea_fury_compliance_drive` | registry stamp, files, and guarded checkpoint |
| Fury Pact Command | `idea_fury_pact_command.dds` | `GFX_idea_fury_pact_command` | two small flags tied by command wire |
| Rival Fury Doctrine | `idea_fury_rival_doctrine.dds` | `GFX_idea_fury_rival_doctrine` | two arrows colliding over a border |
| World Fury | `idea_fury_world_fury.dds` | `GFX_idea_fury_world_fury` | globe map with many small front arrows |

## Decision category and decision icons

Decision category icon target is 32x32 unless existing pattern requires another size.

| Asset | Suggested file | Sprite | Direction |
| --- | --- | --- | --- |
| Fury War Office category | `decision_category_fury_war_office.dds` | `GFX_decision_category_fury_war_office` | war office desk, map, and stamp |
| Find next weak neighbor | `decision_fury_next_neighbor.dds` | `GFX_decision_fury_next_neighbor` | magnifier over border |
| Cut the border rail | `decision_fury_cut_border_rail.dds` | `GFX_decision_fury_cut_border_rail` | broken rail line |
| Open the depots | `decision_fury_open_depots.dds` | `GFX_decision_fury_open_depots` | crate and rifles |
| Core the first ring | `decision_fury_core_first_ring.dds` | `GFX_decision_fury_core_first_ring` | registry stamp over map |
| Shared war tables | `decision_fury_shared_war_tables.dds` | `GFX_decision_fury_shared_war_tables` | two map tables joined |
| Mark rival Fury | `decision_fury_mark_rival.dds` | `GFX_decision_fury_mark_rival` | crossed arrows |
| Carry orders overseas | `decision_fury_orders_overseas.dds` | `GFX_decision_fury_orders_overseas` | dispatch envelope over globe |
| Border Watch | `decision_fury_border_watch.dds` | `GFX_decision_fury_border_watch` | guard line on border |
| Emergency aid to target | `decision_fury_emergency_aid.dds` | `GFX_decision_fury_emergency_aid` | crate and convoy route |

## Focus icon families, 94x86

The implementation can reuse a family icon across related focuses, but the asset pack should provide enough variety.

| Family | Suggested file | Direction |
| --- | --- | --- |
| Opening trunk | `goal_fury_war_office.dds` | impersonal war office with maps |
| Army branch | `goal_fury_columns.dds` | marching infantry columns |
| Depot branch | `goal_fury_depots.dds` | captured depot and supply crates |
| Expansion branch | `goal_fury_next_border.dds` | border markers and arrows |
| Occupation branch | `goal_fury_registry.dds` | files, stamp, checkpoint |
| Cooperation branch | `goal_fury_pact.dds` | two small war offices connected by radio wire |
| Rivalry branch | `goal_fury_rivalry.dds` | two red arrows crossing |
| Evolution I branch | `goal_fury_hardened_columns.dds` | reinforced columns and heavy boots |
| Evolution III branch | `goal_fury_all_borders.dds` | arrows from all sides into a small map |
| World-end branch | `goal_fury_world_in_fury.dds` | globe covered in front arrows |

## News and report images

### First conquest news image, 397x153, black and white

Suggested file: `news_event_fury_first_conquest.dds`
Sprite: `GFX_news_event_fury_first_conquest`

Direction: 1936 to 1945 documentary-style black and white news image. A small capital building or border office with soldiers, files, and a map being carried inside. No readable generated text. No modern equipment.

### Fury stall report image, 210x176

Suggested file: `report_event_fury_overextension.dds`
Sprite: `GFX_report_event_fury_overextension`

Direction: period documentary image of exhausted soldiers and clerks in a damaged office with maps and supply crates.

### Fury defeated report image, 210x176

Suggested file: `report_event_fury_defeated.dds`
Sprite: `GFX_report_event_fury_defeated`

Direction: abandoned war office, empty map table, border signs being restored.

## Super-event images, 457x328

### Fury major super-event

Suggested file: `super_event_fury_major.dds`
Sprite: `GFX_super_event_fury_major`

Direction: strong central composition. A once-small capital war room filled with maps, dispatch clerks, officers, and border pins. Period documentary realism. No generated text.

### World in Fury world-end super-event

Suggested file: `super_event_world_in_fury.dds`
Sprite: `GFX_super_event_world_in_fury`

Direction: global map room with multiple continents marked, radio operators, dispatch tables, and repeated small flags. Period style, no modern screens, no readable text.

### Fury defeat aftermath super-event

Suggested file: `super_event_fury_aftermath.dds`
Sprite: `GFX_super_event_fury_aftermath`

Direction: quiet aftermath in a border archive or war office, maps sealed and guarded, tired soldiers and officials.

## Faction emblem

Suggested file: `faction_fury_pact.dds`
Sprite: `GFX_faction_fury_pact`

Direction: clean emblem of converging border arrows around a small central map. No readable text. Must remain readable at faction emblem size.

## Optional institutional leader portrait, 156x210

Suggested file: `leader_fury_war_directorate.dds`
Sprite: `GFX_portrait_fury_war_directorate`

Direction: fictional institutional council or impersonal war office leadership portrait. A table of officers partly in shadow with maps and files, no single real person, no generated text. Mark as fictional institutional leader. Do not use gendered personal-name pool.

## Achievement icons, 64x64

Create completed icons first. Grey and not-eligible variants can be produced later if needed.

| Achievement | Icon direction |
| --- | --- |
| Fuse Cut Short | cut fuse over a border map |
| No Minor Shall Be Major | small flag blocked by a large staff marker |
| The Firebreak Holds | soldiers holding a marked border line |
| Break the March Pact | cracked faction seal and split arrows |
| Ten Fires, No Dawn | ten small flames over a world grid |
| The Last Neighbor Stands | lone border marker against a moving map |
| A World Without Fury | burned maps sealed in an archive |
| Let the Fires Fight | two fire arrows colliding |
| Alone Against the Major | lone shield before a large red map marker |
| Paper Borders Hold | intact border papers with official stamp |

## Manifest and handoff

Create:

- source PNGs.
- processed PNG previews.
- final DDS files.
- `docs/assets/007_fury/manifest.md`.
- `docs/assets/007_fury/gfx_handoff.md`.

Every handoff entry must include final DDS path, sprite name, target `.gfx` file, and related idea, decision, focus, event, super-event, faction, leader, or achievement.
