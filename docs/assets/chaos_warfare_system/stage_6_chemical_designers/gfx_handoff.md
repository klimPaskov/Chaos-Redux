# GFX handoff: Stage 6 chemical designer icons

No `.gfx` file was edited. The parent agent owns final sprite registration and should preserve the exact supplied sprite names and runtime texture paths below.

Suggested target: the existing parent-selected CBRN designer `.gfx` file. The exact filename was not supplied in the asset prompt, so no new `.gfx` file is proposed or created here.

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
| `cbrn_chemical_munitions_combine` | `GFX_cbrn_chemical_munitions_combine` | `gfx/interface/ideas/cbrn_designers/cbrn_chemical_munitions_combine.dds` | 64x64 | complete |
| `cbrn_aerosol_air_delivery_bureau` | `GFX_cbrn_aerosol_air_delivery_bureau` | `gfx/interface/ideas/cbrn_designers/cbrn_aerosol_air_delivery_bureau.dds` | 64x64 | complete |

Parent wiring note: both textures are transparent 64x64 legacy BGRA DDS files. No localisation, gameplay, `.gfx`, or GUI files are part of this asset package.
