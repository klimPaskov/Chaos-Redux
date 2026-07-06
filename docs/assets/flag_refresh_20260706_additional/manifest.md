# Additional Flag Refresh - 2026-07-06

## Overview

This package regenerates four Chaos Redux country flags with `$imagegen` source art, processed PNG previews, final HOI4 TGA outputs, and contact sheets.

Final flag TGAs are root-level HOI4 flag assets:

- `gfx/flags/<tag>.tga` at 82x52
- `gfx/flags/medium/<tag>.tga` at 41x26
- `gfx/flags/small/<tag>.tga` at 10x7

Flags are an engine-facing TGA exception, not DDS-backed interface sprites.

## Contact Sheets

- `docs/assets/flag_refresh_20260706_additional/contact_sheets/additional_flags_contact_sheet.png`
- `docs/assets/flag_refresh_20260706_additional/contact_sheets/additional_flags_all_sizes_contact_sheet.png`

## Assets

| Asset | Type | In-game use | Source mode | Source PNG | Processed previews | Final TGAs | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DSC_fascism` | Fictional country flag | Revenant Staff Directorate | `$imagegen` | `source_png/DSC_fascism_source.png` | `processed_png/DSC_fascism_82x52.png`, `processed_png/DSC_fascism_41x26.png`, `processed_png/DSC_fascism_10x7.png` | `gfx/flags/DSC_fascism.tga`, `gfx/flags/medium/DSC_fascism.tga`, `gfx/flags/small/DSC_fascism.tga` | complete |
| `DSC_communism` | Fictional country flag | Congress of Dead Regiments | `$imagegen` | `source_png/DSC_communism_source.png` | `processed_png/DSC_communism_82x52.png`, `processed_png/DSC_communism_41x26.png`, `processed_png/DSC_communism_10x7.png` | `gfx/flags/DSC_communism.tga`, `gfx/flags/medium/DSC_communism.tga`, `gfx/flags/small/DSC_communism.tga` | complete |
| `ALN` | Fictional country flag | Alan Pass Principality base flag | `$imagegen` | `source_png/ALN_source.png` | `processed_png/ALN_82x52.png`, `processed_png/ALN_41x26.png`, `processed_png/ALN_10x7.png` | `gfx/flags/ALN.tga`, `gfx/flags/medium/ALN.tga`, `gfx/flags/small/ALN.tga` | complete |
| `CFR` | Fictional country flag | Civilian Factory of Russia base flag | `$imagegen` | `source_png/CFR_source.png` | `processed_png/CFR_82x52.png`, `processed_png/CFR_41x26.png`, `processed_png/CFR_10x7.png` | `gfx/flags/CFR.tga`, `gfx/flags/medium/CFR.tga`, `gfx/flags/small/CFR.tga` | complete |

## Prompts

### DSC_fascism

Use case: logo-brand. Asset type: Hearts of Iron IV fictional country flag source art, to be cropped into 82x52 / 41x26 / 10x7 TGA flags. Primary request: Create a clean vexillological flag for DSC_fascism, the Revenant Staff Directorate of the Dead Soldiers' Congress. Subject: fictional militarist dead-regiment state, revenant staff officers, roll-call ledgers, grave regiments, old front roads. Style/medium: flat flag design, bold symbolic heraldry, no fabric folds, no realistic scene, no poster texture. Composition/framing: horizontal 82:52 flag ratio, simple central emblem readable at tiny game sizes: a pale broken regimental spear or staff over a dark memorial shield, with one austere road stripe or chevron suggesting an unfinished campaign order. Color palette: charcoal black, bone white, muted iron gray, dark blood red accent. Constraints: no text, no letters, no numbers, no watermark, no photorealism, no gradients, no tiny details, no swastikas, no SS runes, no real-world fascist insignia, no skulls that become cluttered at small size. Avoid: palette swap of another flag, upside-down composition, ornate illustration, busy medal clusters, readable writing.

### DSC_communism

Use case: logo-brand. Asset type: Hearts of Iron IV fictional country flag source art, to be cropped into 82x52 / 41x26 / 10x7 TGA flags. Primary request: Create a clean vexillological flag for DSC_communism, the Congress of Dead Regiments / Dead Soldiers' Roll-Call Soviets. Subject: dead regiments, roll-call books, veterans' soviets, memorial columns, regimental numbers without showing text. Style/medium: flat flag design, bold symbolic heraldry, no fabric folds, no realistic scene, no poster texture. Composition/framing: horizontal 82:52 flag ratio, simple central emblem readable at tiny game sizes: a red field with a bone-white memorial ledger or roll-call tablet crossed with a dark bayonet/soldier road marker, plus a small plain star-like signal if it stays simple. Color palette: deep red, dark maroon, bone white, soot black, muted brass accent. Constraints: no text, no letters, no numbers, no watermark, no photorealism, no gradients, no tiny details, no hammer and sickle copied from real flags, no skulls that become cluttered. Avoid: palette swap of the fascist version, ornate illustration, busy medal clusters, upside-down composition, readable writing.

### ALN

Use case: logo-brand. Asset type: Hearts of Iron IV fictional country flag source art, to be cropped into 82x52 / 41x26 / 10x7 TGA flags. Primary request: Create a clean vexillological base flag for ALN, the Alan Pass Principality. Subject: Alan highland pass council, Darial road, mountain courts, guarded Caucasus passes, old banner restoration. Style/medium: flat flag design, bold symbolic heraldry, no fabric folds, no realistic scene, no poster texture. Composition/framing: horizontal 82:52 flag ratio, readable at tiny HOI4 sizes: stylized white mountain pass gateway or twin peaks around a narrow road/valley line, with a simple old-principality sun or crown-like notch that is abstract and not monarchist clutter. Color palette: deep mountain green, dark umber, stone white, muted gold accent, small slate-blue shadow if useful. Constraints: no text, no letters, no numbers, no watermark, no photorealism, no gradients, no tiny details, no real national flag copy. Avoid: busy landscape painting, too many peaks, ornate medieval crest, upside-down composition, readable writing.

### CFR

Use case: logo-brand. Asset type: Hearts of Iron IV fictional country flag source art, to be cropped into 82x52 / 41x26 / 10x7 TGA flags. Primary request: Create a clean vexillological base flag for CFR, the Civilian Factory of Russia / Russian Construction Directorate. Subject: construction board state, cranes, concrete, unfinished city, ration-card authority, bridges, rail repair, public works. Style/medium: flat flag design, bold symbolic heraldry, no fabric folds, no realistic scene, no poster texture. Composition/framing: horizontal 82:52 flag ratio, simple central emblem readable at tiny game sizes: an abstract construction crane hook or tower crane silhouette over a concrete block/unfinished city grid, with one strong horizontal foundation stripe. Color palette: concrete gray, off-white, safety ochre, muted worker red, dark slate outline. Constraints: no text, no letters, no numbers, no watermark, no photorealism, no gradients, no tiny details, no real company logo, no Soviet emblem copy. Avoid: busy cityscape, detailed machinery, construction sign text, palette swap of other flags, upside-down composition, readable writing.

## Validation

- `file` reports all final TGAs as Targa image data at the expected dimensions.
- Header check confirms uncompressed 32-bit TGA, 8 alpha bits, and bottom-origin orientation (`top_origin=False`) for all normal, medium, and small files.
- Contact sheets show the final orientation and small-size readability.
