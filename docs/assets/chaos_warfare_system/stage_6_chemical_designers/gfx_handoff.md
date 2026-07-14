# GFX wiring: Stage 6 chemical designer icons

The parent registration is complete in `interface/cbrn_designers.gfx`. The exact supplied sprite names and runtime texture paths are preserved below.

```text
spriteType = {
	name = "GFX_cbrn_chemical_munitions_combine"
	texturefile = "gfx/interface/ideas/cbrn_designers/cbrn_chemical_munitions_combine.dds"
}

spriteType = {
	name = "GFX_cbrn_aerosol_air_delivery_bureau"
	texturefile = "gfx/interface/ideas/cbrn_designers/cbrn_aerosol_air_delivery_bureau.dds"
}
```

| Stable designer ID | Sprite name | Runtime DDS | Target size | Status |
| --- | --- | --- | --- | --- |
| `cbrn_chemical_munitions_combine` | `GFX_cbrn_chemical_munitions_combine` | `gfx/interface/ideas/cbrn_designers/cbrn_chemical_munitions_combine.dds` | 64x64 | wired |
| `cbrn_aerosol_air_delivery_bureau` | `GFX_cbrn_aerosol_air_delivery_bureau` | `gfx/interface/ideas/cbrn_designers/cbrn_aerosol_air_delivery_bureau.dds` | 64x64 | wired |

Both textures are transparent 64x64 legacy BGRA DDS files. The asset-production commit did not edit localisation or gameplay; parent integration owns those surfaces and the completed `.gfx` registration.
