# Event 013 idea icon matte fix handoff

Subagent: Chaos Redux icon asset subagent
Date: 2026-07-01
Scope: Event 013 Natural Disasters idea and national-spirit icons only.

## Files changed

- `docs/assets/013_natural_disasters/source_png/idea_013_disaster_aftermath_source.png`
- `docs/assets/013_natural_disasters/source_png/idea_013_refugee_pressure_source.png`
- `docs/assets/013_natural_disasters/source_png/idea_013_famine_pressure_source.png`
- `docs/assets/013_natural_disasters/source_png/idea_013_broken_infrastructure_source.png`
- `docs/assets/013_natural_disasters/source_png/idea_013_disaster_recovery_mobilization_source.png`
- `docs/assets/013_natural_disasters/processed_png/idea_013_disaster_aftermath.png`
- `docs/assets/013_natural_disasters/processed_png/idea_013_refugee_pressure.png`
- `docs/assets/013_natural_disasters/processed_png/idea_013_famine_pressure.png`
- `docs/assets/013_natural_disasters/processed_png/idea_013_broken_infrastructure.png`
- `docs/assets/013_natural_disasters/processed_png/idea_013_disaster_recovery_mobilization.png`
- `docs/assets/013_natural_disasters/dds/idea_013_disaster_aftermath.dds`
- `docs/assets/013_natural_disasters/dds/idea_013_refugee_pressure.dds`
- `docs/assets/013_natural_disasters/dds/idea_013_famine_pressure.dds`
- `docs/assets/013_natural_disasters/dds/idea_013_broken_infrastructure.dds`
- `docs/assets/013_natural_disasters/dds/idea_013_disaster_recovery_mobilization.dds`
- `gfx/interface/ideas/013_natural_disasters/idea_013_disaster_aftermath.dds`
- `gfx/interface/ideas/013_natural_disasters/idea_013_refugee_pressure.dds`
- `gfx/interface/ideas/013_natural_disasters/idea_013_famine_pressure.dds`
- `gfx/interface/ideas/013_natural_disasters/idea_013_broken_infrastructure.dds`
- `gfx/interface/ideas/013_natural_disasters/idea_013_disaster_recovery_mobilization.dds`
- `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_idea_icons_contact.png`
- `docs/assets/013_natural_disasters/prompts/generated_prompts.md`
- `docs/assets/013_natural_disasters/manifest.md`
- `docs/assets/013_natural_disasters/gfx_handoff.md`

## Asset ids

| Asset | Sprite | Live DDS |
| --- | --- | --- |
| `idea_013_disaster_aftermath` | `GFX_idea_013_disaster_aftermath` | `gfx/interface/ideas/013_natural_disasters/idea_013_disaster_aftermath.dds` |
| `idea_013_refugee_pressure` | `GFX_idea_013_refugee_pressure` | `gfx/interface/ideas/013_natural_disasters/idea_013_refugee_pressure.dds` |
| `idea_013_famine_pressure` | `GFX_idea_013_famine_pressure` | `gfx/interface/ideas/013_natural_disasters/idea_013_famine_pressure.dds` |
| `idea_013_broken_infrastructure` | `GFX_idea_013_broken_infrastructure` | `gfx/interface/ideas/013_natural_disasters/idea_013_broken_infrastructure.dds` |
| `idea_013_disaster_recovery_mobilization` | `GFX_idea_013_disaster_recovery_mobilization` | `gfx/interface/ideas/013_natural_disasters/idea_013_disaster_recovery_mobilization.dds` |

## Work performed

- Inspected the Chaos Redux idea icon reference folder at `.agents/skills/chaos-redux-event-assets/assets/ideas`.
- Regenerated all five icons from fresh official `image_gen` source art rather than recoloring or editing the previous matted icons.
- Used solid chroma-key source backgrounds, removed the key with the official imagegen helper, normalized each icon to a centered transparent `64x64` canvas, and exported both package and live DDS copies.
- Preserved all parent-provided sprite names and live DDS paths.
- Did not edit gameplay, localisation, `.gfx`, GUI, events, decisions, scripted files, spreadsheets, or unrelated assets.

## Validation

- Opened the final contact sheet at `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_idea_icons_contact.png`.
- Confirmed all processed PNGs, package DDS copies, and live DDS files are `64x64` with alpha.
- Matte scan on processed PNGs and live DDS files found zero visible green key pixels, zero visible magenta key pixels, zero visible purple key pixels, and zero visible opaque corners.
- Source PNGs are preserved as raw generated source art in the package source folder; processed PNGs and DDS files are the exact in-game-size outputs.

## Remaining risks

- No asset-production blockers remain.
- No `.gfx` handoff uncertainty remains because sprite names and texture paths were already registered and stayed unchanged.
