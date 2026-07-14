# Stage 6 Chemical Air Rack-Variant GFX Handoff

Target file: `interface/chaosx_equipment.gfx`
All textures below are exact `64x64` uncompressed BGRA DDS files and are ready to wire. No `.gfx` file was edited by this asset package.

The final processed-preview folder `docs/assets/chaos_warfare_system/stage_6_chemical_air_variants/processed_png_64x64/` is a proposed non-destructive package path; the parent prompt did not prescribe a processed-preview subfolder, and the existing `processed_png/` evidence was left untouched.

Copy the following sprite definitions into the existing `spriteTypes` block in `interface/chaosx_equipment.gfx`:

```text
spriteType = { name = GFX_EMI_chem_air_bomb_chlorine_lightweight texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_chlorine_lightweight.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_chlorine_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_chlorine_long_range.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_chlorine_lightweight_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_chlorine_lightweight_long_range.dds" }

spriteType = { name = GFX_EMI_chem_air_bomb_phosgene_lightweight texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_phosgene_lightweight.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_phosgene_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_phosgene_long_range.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_phosgene_lightweight_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_phosgene_lightweight_long_range.dds" }

spriteType = { name = GFX_EMI_chem_air_bomb_mustard_lightweight texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_mustard_lightweight.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_mustard_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_mustard_long_range.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_mustard_lightweight_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_mustard_lightweight_long_range.dds" }

spriteType = { name = GFX_EMI_chem_air_bomb_lewisite_lightweight texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_lewisite_lightweight.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_lewisite_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_lewisite_long_range.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_lewisite_lightweight_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_lewisite_lightweight_long_range.dds" }

spriteType = { name = GFX_EMI_chem_air_bomb_tabun_lightweight texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_tabun_lightweight.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_tabun_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_tabun_long_range.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_tabun_lightweight_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_tabun_lightweight_long_range.dds" }

spriteType = { name = GFX_EMI_chem_air_bomb_sarin_lightweight texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_sarin_lightweight.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_sarin_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_sarin_long_range.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_sarin_lightweight_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_sarin_lightweight_long_range.dds" }

spriteType = { name = GFX_EMI_chem_air_bomb_soman_lightweight texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_soman_lightweight.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_soman_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_soman_long_range.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_soman_lightweight_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_soman_lightweight_long_range.dds" }

spriteType = { name = GFX_EMI_chem_air_bomb_malodor_lightweight texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_malodor_lightweight.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_malodor_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_malodor_long_range.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_malodor_lightweight_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_malodor_lightweight_long_range.dds" }

spriteType = { name = GFX_EMI_chem_air_bomb_behavioral_lightweight texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_behavioral_lightweight.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_behavioral_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_behavioral_long_range.dds" }
spriteType = { name = GFX_EMI_chem_air_bomb_behavioral_lightweight_long_range texturefile = "gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/chem_air_bomb_behavioral_lightweight_long_range.dds" }
```

Sprite count: 27. All names follow the exact requested `GFX_EMI_chem_air_bomb_<agent>_<variant>` pattern. Related runtime interface is the Stage 6 chemical-air equipment module family; no localisation or gameplay files are part of this handoff.

Review note: the retained sarin long-range icon has a cyan release effect inherited from its authoritative source. It remains a transparent, readable physical pod icon; this is documented as a minor stylistic variance rather than a blocker.
