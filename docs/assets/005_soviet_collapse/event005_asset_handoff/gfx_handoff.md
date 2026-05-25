# Event 005 Portrait and Flag GFX Handoff

No `.gfx` files were edited. This file gives the main agent enough paths and sprite names to wire assets after separate promotion or regeneration.

## Contact Sheets

- Current requested normal flags: `docs/assets/005_soviet_collapse/event005_asset_handoff/contact_sheets/event005_requested_flags_normal_contact.png`
- Current requested flag size/orientation sheet: `docs/assets/005_soviet_collapse/event005_asset_handoff/contact_sheets/event005_requested_flags_size_orientation_contact.png`
- Current requested leaders: `docs/assets/005_soviet_collapse/event005_asset_handoff/contact_sheets/event005_requested_leaders_contact.png`

The contact sheets are audit previews from the current live target files, not new source art.

## Flag Target Paths

For each approved generated or sourced flag variant:

```text
gfx/flags/<TAG>[_<ideology>].tga
gfx/flags/medium/<TAG>[_<ideology>].tga
gfx/flags/small/<TAG>[_<ideology>].tga
```

Requested tags covered by this handoff:

```text
CFR KRS RMC SDZ TSC UDC SOG ALN KHW KZR MFR
```

Use `$imagegen` for `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, and `MFR` fictional ideology/route variants. Use source research for `SOG`, `ALN`, `KHW`, and `KZR` flags when the intended identity is historical restoration or historically grounded symbolism.

## Portrait Target Paths

| Target final DDS | Proposed sprite | Suggested `.gfx` file |
| --- | --- | --- |
| `gfx/leaders/005_soviet_collapse/CFR_leader.dds` | `GFX_portrait_CFR_civilian_works_directorate` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` |
| `gfx/leaders/005_soviet_collapse/MFR_leader.dds` | `GFX_portrait_MFR_arsenal_directorate` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` |
| `gfx/leaders/005_soviet_collapse/KRS_leader.dds` | `GFX_portrait_KRS_kronstadt_council` | `interface/005_soviet_collapse_custom_icons.gfx` |
| `gfx/leaders/005_soviet_collapse/RMC_leader.dds` | `GFX_portrait_RMC_resurrection_cult` | `interface/005_soviet_collapse_custom_icons.gfx` |
| `gfx/leaders/005_soviet_collapse/SDZ_leader.dds` | `GFX_portrait_SDZ_security_directorate` | `interface/005_soviet_collapse_custom_icons.gfx` |
| `gfx/leaders/005_soviet_collapse/TSC_leader.dds` | `GFX_portrait_TSC_tunguska_star_committee` | `interface/005_soviet_collapse_custom_icons.gfx` |
| `gfx/leaders/005_soviet_collapse/UDC_leader.dds` | `GFX_portrait_UDC_union_defense_committee` | `interface/005_soviet_collapse_custom_icons.gfx` |
| `gfx/leaders/005_soviet_collapse/SOG_leader.dds` | `GFX_portrait_SOG_sogdian_council` | `interface/005_soviet_collapse_ancient_icons.gfx` |
| `gfx/leaders/005_soviet_collapse/ALN_leader.dds` | `GFX_portrait_ALN_alan_pass_council` | `interface/005_soviet_collapse_ancient_icons.gfx` |
| `gfx/leaders/005_soviet_collapse/KHW_leader.dds` | `GFX_portrait_KHW_oasis_authority_council` | `interface/005_soviet_collapse_ancient_icons.gfx` |
| `gfx/leaders/005_soviet_collapse/KZR_leader.dds` | `GFX_portrait_KZR_khazar_toll_council` | `interface/005_soviet_collapse_ancient_icons.gfx` |

## Use Notes

- Keep base/no-ideology flags unless the parent explicitly lists a base file for replacement.
- Do not promote generated flags that are filters, recolors, flipped copies, single-shape edits, upside-down variants, or byte-identical copies.
- Use generated portraits only for fictional councils, factory directorates, symbolic authorities, or invented leaders.
- Use sourced portraits for any real person.
- If promoted, each generated portrait package should include source PNG, processed PNG, final DDS, prompt, manifest row, and contact sheet.
