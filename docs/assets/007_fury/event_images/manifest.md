# Event 007 Fury Report and News Images

## Direction

These assets deliberately avoid map rooms, war-room desks, ledgers, route strings, and other planning-table metaphors. Fury should read as a rogue country overtaken by unnatural rage: soldiers in the streets, civilians fleeing, smoke, sudden neighbor attacks, and visible panic.

## Assets

| Asset | Type | Source mode | Source PNG | Processed PNG | Final DDS | Target size | Sprite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fury takes command | report event image | generated with built-in `image_gen` | `docs/assets/007_fury/report_event_images/source_png/fury_war_office_source.png` | `docs/assets/007_fury/report_event_images/processed_png/fury_war_office.png` | `gfx/event_pictures/fury/fury_war_office.dds` | 210x176 | `GFX_report_event_fury_war_office` |
| Fury first conquest | news event image | generated with built-in `image_gen` | `docs/assets/007_fury/news_event_images/source_png/fury_first_conquest_source.png` | `docs/assets/007_fury/news_event_images/processed_png/fury_first_conquest.png` | `gfx/event_pictures/fury/fury_first_conquest.dds` | 397x153 | `GFX_news_event_fury_first_conquest` |

## Prompts

### Fury takes command

```text
Use case: historical-scene
Asset type: Hearts of Iron IV mod report event image source, will be cropped to 210x176
Primary request: Create a period-authentic 1936-1945 documentary-style image for a fictional event where a small country has gone rogue under mysterious Fury and is preparing to attack its neighbors.
Scene/backdrop: a smoke-dark border town street at night, military trucks and infantry columns surging past frightened civilians, a government building behind them with windows glowing as if something has seized control inside.
Subject: soldiers of a small unnamed country moving with unnatural urgency, faces tense and feverish, one officer shouting orders as if driven by rage, civilians recoil in doorways.
Style/medium: gritty World War II-era documentary photograph with slight painterly strategy-game finish, not cinematic fantasy.
Composition/framing: portrait-friendly crop, strong central soldier/officer figure, visible marching column behind, readable at 210x176.
Lighting/mood: harsh torchlight and vehicle lamps, smoke, panic, violent momentum.
Color palette: muted olive, charcoal, dirty amber, dark red firelight accents.
Text: none.
Constraints: no maps, no war rooms, no desks, no ledgers, no readable text, no letters, no numbers, no logos, no watermarks, no UI frame, no real national flags, no gore, no modern weapons or clothing.
```

### Fury first conquest

```text
Use case: historical-scene
Asset type: Hearts of Iron IV mod news event image source, will be cropped to 397x153 black-and-white
Primary request: Create a period-authentic 1936-1945 newspaper photograph for a fictional event where a Fury country has just seized its first neighbor.
Scene/backdrop: a captured border checkpoint and town square after a sudden assault, smoke, broken barricades, refugees, and soldiers raising no identifiable flag.
Subject: exhausted Fury soldiers standing amid the first conquest with wild, feverish intensity; civilians and prisoners in the foreground show fear and confusion, suggesting a mysterious rage powering the attackers.
Style/medium: old press photograph, black-and-white documentary realism, high contrast, gritty grain.
Composition/framing: wide horizontal composition for 397x153, strong central line of soldiers advancing through smoke, no map or office imagery.
Lighting/mood: smoky daylight, harsh contrast, shock after fast violence.
Color palette: black and white only.
Text: none.
Constraints: no maps, no war rooms, no desks, no ledgers, no readable text, no letters, no numbers, no logos, no watermarks, no UI frame, no real national flags, no gore, no modern weapons or clothing.
```

## Sprite Definitions

- `GFX_report_event_fury_war_office` in `interface/007_fury.gfx`
- `GFX_news_event_fury_first_conquest` in `interface/007_fury.gfx`

## Status

Both assets are generated, processed, converted, wired through existing sprite definitions, and complete.
