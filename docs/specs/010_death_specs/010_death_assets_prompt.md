# Event 010 Death - Asset And Animation Prompt

## Asset Goal

Create a complete visual package for Event 010 Death. The art should be austere, period-compatible, and unnerving because of absence. Avoid gore, monster hordes, cartoon skulls, plague-doctor cliches, and pirate flag language.

Death is a black country led by Zol. It starts on a remote island, spreads through empty shores, reveals itself on the mainland, and can become a world-end scenario.

## Source Modes

Use generated fictional/symbolic art for Zol, Death report images, super-events, icons, and flags. Do not use a real portrait for Zol. Real historical source references may inform tone, but final assets should not imply Death is a historical person, state, or cult.

For final implementation, copy stable vanilla placeholder sprites where needed so the game loads, then replace with final generated assets without changing sprite names.

## Required Country Assets

| Asset | Target path | Notes |
| --- | --- | --- |
| large flag | `gfx/flags/DTH.tga` | black field, minimal pale mark or seam for UI readability |
| medium flag | `gfx/flags/medium/DTH.tga` | same composition, readable at medium size |
| small flag | `gfx/flags/small/DTH.tga` | high contrast, no fine detail |
| leader portrait | `gfx/leaders/DTH/portrait_DTH_zol.dds` | symbolic, period-compatible, no real person |
| country emblem | interface sprite if needed | optional for scripted GUI/decision header |

Flag direction: black field with a narrow pale coastline, ledger mark, or extinguished lighthouse geometry. Avoid skull-and-crossbones.

Zol portrait direction: a still administrative figure, unreadable face, dark coat, ledger or harbor-office lighting. No skeleton caricature.

## Report And News Images

| Sprite | Suggested file | Scene |
| --- | --- | --- |
| `GFX_report_event_death_origin` | `gfx/event_pictures/report_event_death_origin.dds` | remote island station, empty harbor, no people |
| `GFX_report_event_death_missing_island` | `gfx/event_pictures/report_event_death_missing_island.dds` | lighthouse tender arriving to no response |
| `GFX_report_event_death_reveal` | `gfx/event_pictures/report_event_death_reveal.dds` | mainland office with black coastline chart |
| `GFX_report_event_death_black_shore` | `gfx/event_pictures/report_event_death_black_shore.dds` | abandoned port, dark waterline |
| `GFX_report_event_death_compact` | `gfx/event_pictures/report_event_death_compact.dds` | grim international conference over coastline maps |
| `GFX_report_event_death_forbidden` | `gfx/event_pictures/report_event_death_forbidden.dds` | black register, unlit archive room |
| `GFX_report_event_death_defeat` | `gfx/event_pictures/report_event_death_defeat.dds` | recovered shore, blank memorial boards |
| `GFX_report_event_death_world_consumed` | `gfx/event_pictures/report_event_death_world_consumed.dds` | black ledger and extinguished lamp |

News images should be scarce. Early disappearance events are local/report style, not world news.

## Super-Event Images

Target size should match existing Chaos Redux super-event image dimensions.

| Super-event | Sprite | Direction |
| --- | --- | --- |
| The Name On The Chart | `GFX_super_event_death_reveal` | map office, empty harbor, coastline inked out |
| The Living Compact | `GFX_super_event_death_compact` | conference room, black shore maps, covered windows |
| No More Shores | `GFX_super_event_death_world_end` | world coastline fading into black sea |
| The Shore Returns Empty | `GFX_super_event_death_defeat` | soldiers/civilians at recovered coast, no triumph |
| The Last Entry | `GFX_super_event_death_world_consumed` | black ledger, final lamp, erased coastline |

No readable generated text. Let localisation carry titles and quotes.

## Focus Icons

Register final sprite names before art delivery.

Required focus icon concepts:

- first shore
- no herald
- no envoy
- no tax ledger
- quiet census
- black tide
- still front
- factories without hands
- ports that receive nothing
- unnamed ranks
- pale companies
- mute regiments
- final muster
- name arrives before army
- last continent
- no more maps

Suggested icon language: lighthouse, blank chart, sealed ledger, black shoreline, empty harbor, white map orders, unmarked ranks.

## Decision And Idea Icons

Decision category icon:

- `GFX_decision_category_death_black_shore`
- black coastal line swallowing a small white island or lighthouse beam

Decision icons:

- send lighthouse tender
- compare admiralty charts
- bury the report
- publish empty harbor story
- establish black cordon
- evacuate the shore
- salt the railheads
- hold the lighthouses
- convene black shore conference
- pool cordon equipment
- forbidden register
- petition Zol
- issue white map orders
- clear footholds

Idea icons:

- not yet a country
- empty administration
- black shore
- the counting
- named by the living
- no more shores

## Achievement Icons

Achievement icons must follow existing custom achievement asset rules with three DDS files and `.gfx` sprite aliases.

Concepts:

- intact island map
- lighthouse still lit
- living compact seal
- black candle victory
- Zol's hand
- world under Zol
- every shore guarded
- last ledger

## Animation Briefs

Animated assets are optional. If produced, use `chaos-redux-frame-animation`.

Allowed animated asset candidates:

1. Decision category seal: black shoreline slowly consuming a pale island.
2. Withering warning pulse: depth 3 black cordon failure indicator.
3. Zol world-end portrait overlay: faint ledger-light pulse after world-end or Death-player route.

Frame-animation requirements:

- real planned/source frames
- horizontal frame sheet
- static fallback sprite
- contact sheet
- preview GIF only as preview, never as final game asset
- `.gfx` handoff using `frameAnimatedSpriteType`
- no final animation built only from moving, scaling, rotating, blurring, recoloring, or warping one still image

## Asset Manifest Requirements

When assets are produced, create a manifest under `docs/assets/010_death/` listing:

- source prompt or source URL
- generated/source file path
- processed PNG path
- final DDS/TGA path
- sprite name
- dimensions
- implementation file that references it
- license/source notes
- remaining replacement needs

## Artist Prompt

Create a cohesive HOI4-style visual package for a Chaos Redux event called Death. Death is a black country led by Zol, beginning as an unnoticed empty island and escalating into black shorelines, withered states, a compact of living countries, forbidden registers, ghost formations, and possible world-end. Use austere 1930s-1940s documentary/symbolic composition: empty lighthouses, blank harbor offices, black coastlines on maps, covered windows, ledgers, evacuation trains, and unlit signal lamps. Avoid gore, zombies, plague-doctor imagery, monsters, cartoon skulls, readable generated text, or real historical portraits for Zol. Deliver registered sprite names, final paths, static fallbacks, and manifests.
