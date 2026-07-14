# Stage 6 chemical-air module GFX handoff

The parent has wired all nine final runtime files in `interface/chaosx_equipment.gfx`. Aircraft equipment-module icons use the engine naming convention `GFX_EMI_<module_id>` and the verified `56x42` surface.

| Module ID | Sprite ID | Runtime DDS |
|---|---|---|
| `chem_air_bomb_chlorine` | `GFX_EMI_chem_air_bomb_chlorine` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_chlorine.dds` |
| `chem_air_bomb_phosgene` | `GFX_EMI_chem_air_bomb_phosgene` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_phosgene.dds` |
| `chem_air_bomb_mustard` | `GFX_EMI_chem_air_bomb_mustard` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_mustard.dds` |
| `chem_air_bomb_lewisite` | `GFX_EMI_chem_air_bomb_lewisite` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_lewisite.dds` |
| `chem_air_bomb_tabun` | `GFX_EMI_chem_air_bomb_tabun` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_tabun.dds` |
| `chem_air_bomb_sarin` | `GFX_EMI_chem_air_bomb_sarin` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_sarin.dds` |
| `chem_air_bomb_soman` | `GFX_EMI_chem_air_bomb_soman` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_soman.dds` |
| `chem_air_bomb_malodor` | `GFX_EMI_chem_air_bomb_malodor` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_malodor.dds` |
| `chem_air_bomb_behavioral` | `GFX_EMI_chem_air_bomb_behavioral` | `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_behavioral.dds` |

Equivalent declaration pattern:

```txt
spriteType = {
    name = "GFX_EMI_chem_air_bomb_chlorine"
    texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air/chem_air_bomb_chlorine.dds"
}
```

The other declarations use the exact ID/path pairs in the table. No `.gui` change is required. No generic bomb-lock icon, placeholder, or cross-type substitute remains on these nine module IDs.

Parent validation should retain the manifest's dimension/header/hash checks and include live aircraft-designer readability in the later package scenarios.
