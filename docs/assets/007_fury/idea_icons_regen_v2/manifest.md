# Fury idea icon regeneration v2 manifest

Date: 2026-06-11

Status: converted and ready for review.

Scope: Fury idea and national-spirit icons only.

Reference folder inspected: `.agents/skills/chaos-redux-event-assets/assets/ideas`

Source mode summary:

- All 11 icons: `$imagegen` built-in tool
- Transparency workflow: flat `#00ff00` chroma-key source generation, local alpha cleanup, resize to `64x64`, black matte cleanup, DDS conversion

Package paths:

- Source PNGs: `docs/assets/007_fury/idea_icons_regen_v2/source_png/`
- Processed PNG previews: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/`
- Contact sheet: `docs/assets/007_fury/idea_icons_regen_v2/fury_idea_icon_contact_sheet.png`
- Final DDS folder: `gfx/interface/ideas/fury/`

Visual direction:

- Distinct from Fury focus icons and prior paper-heavy idea art
- Compact HOI4 national-spirit presentation
- Strong central symbol, dark outline/shadow, painterly scorch texture, no readable text, no modern logos

## Asset entries

### `idea_fury_national_fury`

- Source mode: `$imagegen`
- Prompt: compact HOI4-style skull engulfed in orange fire, scorched bone and ash, strong centered silhouette, transparent-ready
- Source PNG: `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_national_fury_source.png`
- Processed PNG: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_national_fury.png`
- Final DDS: `gfx/interface/ideas/fury/idea_fury_national_fury.dds`
- Notes: set anchor icon for the visceral Fury side of the family

### `idea_fury_hardened_fury`

- Source mode: `$imagegen`
- Prompt: burned iron military medal with glowing cracks and small flames, painterly WW2 icon treatment, transparent-ready
- Source PNG: `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_hardened_fury_source.png`
- Processed PNG: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_hardened_fury.png`
- Final DDS: `gfx/interface/ideas/fury/idea_fury_hardened_fury.dds`
- Notes: regenerated to avoid formal wax-seal reads

### `idea_fury_overextension`

- Source mode: `$imagegen`
- Prompt: cracked iron command mask split by ember-lit fractures, scorched metal, strong silhouette, transparent-ready
- Source PNG: `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_overextension_source.png`
- Processed PNG: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_overextension.png`
- Final DDS: `gfx/interface/ideas/fury/idea_fury_overextension.dds`
- Notes: kept compact so the facial split still reads at `64x64`

### `idea_fury_compliance_drive`

- Source mode: `$imagegen`
- Prompt: heated branding stamp pressing a scorched border-crown mark, oppressive coercion symbolism, transparent-ready
- Source PNG: `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_compliance_drive_source.png`
- Processed PNG: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_compliance_drive.png`
- Final DDS: `gfx/interface/ideas/fury/idea_fury_compliance_drive.dds`
- Notes: selected over crown-only variants because it reads more forceful and less ceremonial

### `idea_fury_pact_command`

- Source mode: `$imagegen`
- Prompt: blackened world globe tightly gripped by an iron command clasp, grim controlled-force symbolism, transparent-ready
- Source PNG: `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_pact_command_source.png`
- Processed PNG: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_pact_command.png`
- Final DDS: `gfx/interface/ideas/fury/idea_fury_pact_command.dds`
- Notes: regenerated to avoid defensive or ceremonial globe variants

### `idea_fury_rival_doctrine`

- Source mode: `$imagegen`
- Prompt: dark shield with opposing flames split by a harsh diagonal doctrinal slash, painterly WW2 icon style, transparent-ready
- Source PNG: `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_rival_doctrine_source.png`
- Processed PNG: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_rival_doctrine.png`
- Final DDS: `gfx/interface/ideas/fury/idea_fury_rival_doctrine.dds`
- Notes: kept simpler than the anti-Fury coordination icon so the two do not collapse into the same read

### `idea_fury_world_in_fury`

- Source mode: `$imagegen`
- Prompt: blackened world globe split by glowing fractures and surrounded by active flames, apocalyptic but compact, transparent-ready
- Source PNG: `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_fury_world_in_fury_source.png`
- Processed PNG: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_fury_world_in_fury.png`
- Final DDS: `gfx/interface/ideas/fury/idea_fury_world_in_fury.dds`
- Notes: regenerated to remove ring/crown clutter and keep the global-fire read direct

### `idea_anti_fury_border_watch`

- Source mode: `$imagegen`
- Prompt: iron watch ring around a lit emergency lantern, vigilant border-defense symbol, transparent-ready
- Source PNG: `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_anti_fury_border_watch_source.png`
- Processed PNG: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_anti_fury_border_watch.png`
- Final DDS: `gfx/interface/ideas/fury/idea_anti_fury_border_watch.dds`
- Notes: anti-Fury set shifts to warning and containment symbols instead of Fury skull/fire motifs

### `idea_anti_fury_emergency_aid`

- Source mode: `$imagegen`
- Prompt: emergency lantern wrapped with a field bandage and aid pouch clasp, warm relief-light symbol, transparent-ready
- Source PNG: `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_anti_fury_emergency_aid_source.png`
- Processed PNG: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_anti_fury_emergency_aid.png`
- Final DDS: `gfx/interface/ideas/fury/idea_anti_fury_emergency_aid.dds`
- Notes: no red-cross or modern medical branding used

### `idea_anti_fury_staff_talks`

- Source mode: `$imagegen`
- Prompt: two officer batons crossed and bound by a signal-cord knot, liaison and coordination symbol, transparent-ready
- Source PNG: `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_anti_fury_staff_talks_source.png`
- Processed PNG: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_anti_fury_staff_talks.png`
- Final DDS: `gfx/interface/ideas/fury/idea_anti_fury_staff_talks.dds`
- Notes: regenerated to separate it from rival-doctrine knife language

### `idea_anti_fury_supply_denial`

- Source mode: `$imagegen`
- Prompt: broken iron chains around a burning supply flame, sabotage and denial symbol, transparent-ready
- Source PNG: `docs/assets/007_fury/idea_icons_regen_v2/source_png/idea_anti_fury_supply_denial_source.png`
- Processed PNG: `docs/assets/007_fury/idea_icons_regen_v2/processed_png/idea_anti_fury_supply_denial.png`
- Final DDS: `gfx/interface/ideas/fury/idea_anti_fury_supply_denial.dds`
- Notes: strongest anti-Fury destruction motif without falling back to paper crates or logistics ledgers

## Validation

- `identify` confirmed all 11 processed PNG previews are `64x64`.
- `identify` confirmed all 11 final DDS files are `64x64`.
- Contact sheet reviewed after processing to remove residual chroma spill.
- Parent review found a dark rectangular matte behind the icons; near-black semi-transparent matte pixels were removed, all 11 DDS files were reconverted, and the contact sheet was rebuilt.
- No `.gfx`, gameplay, localisation, scripts, spreadsheets, achievement assets, decision assets, or focus DDS files were changed in this package.
