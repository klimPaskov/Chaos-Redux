# Doctrine-style icon GFX handoff

No `.gfx` file was edited in the asset-production subtask; parent integration is complete in `interface/cbrn_doctrine.gfx`.

Suggested sibling runtime folder: `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/`.

The parent implementation repointed the existing sprite definitions in `interface/cbrn_doctrine.gfx` as follows while keeping sprite names stable:

```text
GFX_doctrine_extermination_columns_medium -> gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_hazard_assault_formations.dds
GFX_doctrine_chemical_suppression_medium -> gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_toxic_armored_warfare.dds
GFX_doctrine_contaminant_firebases_medium -> gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_contaminant_fire_support.dds
GFX_doctrine_integrated_chemical_operations_medium -> gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_integrated_cbrn_command.dds
```

Do not repoint or overwrite the user's original `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds` in this handoff. The four new textures are 64x64, transparent, one-frame legacy BGRA DDS outputs.
