# Raid icon GFX handoff

Status: all six approved DDS files have been promoted, and parent GFX changes for the scientist category, scientist unit, and portal-facility raid have been confirmed in `interface/chaosx_raids.gfx`.

| Sprite | Runtime texture | SHA-256 | GFX state |
| --- | --- | --- | --- |
| `GFX_raid_type_icon_chemical_sarin_rocket_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_chemical_sarin_rocket_strike.dds` | `43538b3f54708937f76b6bb405e11853c32f120a7b9d01709e1bbaac0557438b` | Existing leaf unchanged; texture replaced. |
| `GFX_raid_type_icon_chemical_soman_rocket_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_chemical_soman_rocket_strike.dds` | `439e4b319dc76abde15897aa9889fcdf1a932e5885fb0e9f0c710557d9447c6e` | Existing leaf unchanged; texture replaced. |
| `GFX_raid_type_icon_chemical_soman_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_chemical_soman_strike.dds` | `ba2cdf646092dfad903fa9c88de0cda795ca6bdb26565e2adafd6cfafd4b81aa` | Existing leaf unchanged; texture replaced. |
| `GFX_raid_category_small_brilliant_scientist_raids` | `gfx/interface/military_raids/map_icons/raid_unit_icon_brilliant_scientist_raids.dds` | `3b51e10f892f90fc2013b11158a8cc5e2f54b522d8fa867f65e74a7d9b6c3113` | Parent leaf points to the new shared texture. |
| `GFX_raid_unit_icon_brilliant_scientist_raids` | `gfx/interface/military_raids/map_icons/raid_unit_icon_brilliant_scientist_raids.dds` | `3b51e10f892f90fc2013b11158a8cc5e2f54b522d8fa867f65e74a7d9b6c3113` | Parent leaf points to the same shared texture. |
| `GFX_raid_type_icon_brilliant_scientist_portal_facility_raid` | `gfx/interface/military_raids/map_icons/raid_type_icon_brilliant_scientist_portal_facility_raid.dds` | `da24224a5dc51f7722ac2728d6056a68fb61de1ff519eb4c55eecb2861293f79` | Parent leaf points to the new unique texture. |
| `GFX_raid_type_icon_zombie_cure_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_zombie_cure_strike.dds` | `005d90b6c8d967dac976d7fcb11cba2d86ced9795a7a3e43f5fb516846316199` | Existing leaf unchanged; texture replaced. |

Native prompts, source and processed PNGs, review sheets, reference evidence, DDS conversion checks, hashes, alpha measurements, and the guarded promotion receipt are in this folder. See `manifest.json` for full prompt text and lineage, and [the group report](../../../plans/gfx_fix_2026-10/shared_chaosx_raids_report.md) for issue dispositions and validation limits.

No raid gameplay definition, cost, outcome, localization entry, or GFX definition was changed by the asset owner. The game was not launched; live consumer review remains with the user.
