# Shared GFX Cleanup Handoff

## Sprite registries

- `interface/chaosx_operations.gfx`: biological operation main, map, and phase sprites.
- `interface/chaosx_gfx_cleanup.gfx`: biological decision icons, Japan category icon, division-template picker symbols, Event 002 category handoff sprites, and the recovered acid-rain ending news sprite.
- `interface/mapmodes_interface.gfx`: official per-mode scripted-map-mode sprites.

## Gameplay bindings

- `common/operations/chaosx_bioweapon_operations.txt` already references `GFX_operations_plant_bioweapon` and its map variant.
- `common/operation_phases/chaosx_bioweapon_operation_phases.txt` references the six dedicated phase sprites.
- `common/raids/biological_raids.txt` assigns existing dedicated `custom_map_icon` sprites to all five biological raid types.
- `common/decisions/biowarfare_disease_containment_decisions.txt` binds the smallpox vaccination icon.
- `common/decisions/chemical_warfare_decisions.txt` binds the biological stockpile icon.
- `common/decisions/condemnation_sanctions_decisions.txt` binds the biological stockpile-destruction icon.
- `common/decisions/categories/japan_chemical_campaign_categories.txt` binds `GFX_decision_category_japan_chemical_campaign` to the exact existing category ID.
- `common/decisions/categories/002_zombie_outbreak_categories.txt` binds the ten generated Event 002 category icons.
- `common/decisions/002_zombie_outbreak_decisions.txt` binds the migration-restriction icon.

## Division picker indices

- Index `44`: biowarfare (`GFX_div_templ_44_large`, `GFX_div_templ_44_small`).
- Index `45`: chemical warfare (`GFX_div_templ_45_large`, `GFX_div_templ_45_small`).

Vanilla leaves indices `44-64` undefined, so these entries do not override a vanilla symbol.

## Asset review

The final generated assets were selected only after direct comparison with the restored skill examples and vanilla operation/division references. They use the same restrained painterly decision style, sepia operation-phase treatment, circular/square operation framing, and muted sage division-symbol relief. No placeholder, focus-icon copy, unrelated resize, recolor, fake checkerboard, opaque square, or white-halo fallback is present.
