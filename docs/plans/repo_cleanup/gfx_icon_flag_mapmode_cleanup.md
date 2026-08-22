# GFX, Icon, Flag, Map Mode, and Division Symbol Registry

## Overview

This package keeps several previously disconnected visual surfaces aligned with their gameplay references. It covers biological operations and raids, Event 002 decision categories, the Japan chemical campaign category, scripted map-mode buttons, custom flags, division-template picker symbols, and the repository GFX reference audit.

The work is intentionally bounded to visual identity, asset correctness, and sprite wiring. It does not change the balance or design of the underlying mechanics.

## Biological operations and containment

The three covert outbreak operations share a dedicated generic biological-operation identity:

- `GFX_operations_plant_bioweapon`
- `GFX_operations_plant_bioweapon_map`

Their operation phases use dedicated large and small sprites:

- `GFX_phase_bioweapon_plant_reservoir` / `GFX_phase_bioweapon_plant_reservoir_small`
- `GFX_phase_bioweapon_seed_medical_chain` / `GFX_phase_bioweapon_seed_medical_chain_small`
- `GFX_phase_bioweapon_contaminate_transport_hub` / `GFX_phase_bioweapon_contaminate_transport_hub_small`

Five existing raid map icons are wired through `custom_map_icon` for anthrax, plague, tularemia, smallpox, and zombie-cure strikes. Dedicated decision icons also identify the smallpox vaccination program, the emergency biological stockpile action, and biological stockpile destruction.

Sprite definitions are split between `interface/chaosx_operations.gfx` and `interface/chaosx_gfx_cleanup.gfx`. Final assets live under `gfx/interface/operations/chaosx_bioweapon/` and `gfx/interface/decisions/biowarfare/`.

## Event 002 categories

The existing cure icon remains assigned to the two cure categories. The ten categories that previously used generic crisis or civil-war art have dedicated `52x40` category sprites:

- outbreak prevention
- weaponized-zombie operations
- Anti-Zombie League
- infected creator profile
- rabid creator profile
- parasitic creator profile
- mutant creator profile
- undead creator profile
- necrotic creator profile
- demonic creator profile

Final DDS files live under `gfx/interface/decisions/002_zombie_outbreak/categories/`. The related migration-restriction decision uses `GFX_decision_zombie_lift_migration_restrictions` instead of a nonexistent generic-democracy sprite.

## Japan chemical campaign

The existing category ID `japan_chemical_campaign_category` uses `GFX_decision_category_japan_chemical_campaign`. Its final DDS lives at `gfx/interface/decisions/japan_chemical_campaign/decision_category_japan_chemical_campaign.dds`.

## Scripted map modes

The civilian-deaths and contamination map modes follow the official scripted-map-mode sprite contract:

- `GFX_mapmode_buttons_deselected_small_deaths_state_map_mode`
- `GFX_mapmode_buttons_selected_small_deaths_state_map_mode`
- `GFX_mapmode_buttons_deselected_small_contaminated_states_map_mode`
- `GFX_mapmode_buttons_selected_small_contaminated_states_map_mode`

The dedicated `20x18` textures are extracted from the existing selected and deselected strip artwork and live under `gfx/interface/mapmode/custom/`. The shared strips remain `19` frames wide: Chaos Redux uses vanilla's blank frame `18` and the appended frame `19`.

## Division-template picker

Vanilla defines picker indices `0-43` and resumes at `65`, leaving `44-64` available for mod symbols. Chaos Redux uses:

- `44`: biowarfare
- `45`: chemical warfare

Each index has a `76x42` large sprite and a `30x12` small sprite in the vanilla-compatible `division_templates_large` and `division_templates_small` folders. `interface/chaosx_gfx_cleanup.gfx` registers the four `GFX_div_templ_*` names consumed by the division designer picker.

## Flags

The real ANX flag TGAs are repaired at all three required sizes:

- normal `82x52`
- medium `41x26`
- small `10x7`

The full-height white column is removed from the left edge of `ANX` and the right edge of `ANX_neutrality`. All custom flag triplets are stored as 32-bit, bottom-origin TGA files. The filenames and orientation remain unchanged.

## Asset records

- Shared source PNGs, processed PNGs, contact sheets, manifest, and handoff: `docs/assets/shared_gfx_cleanup/`
- Event 002 source PNGs, processed PNGs, contact sheet, manifest, and handoff: `docs/assets/002_zombie_outbreak/`
- Remaining missing reference report: `docs/assets/shared_gfx_cleanup/missing_gfx_audit.md`

## Future plans

- Give the remaining generic disease-containment decisions a broader bespoke icon family if that system receives a dedicated UI expansion.
- Resolve the unrelated Event 003 scripted-GUI and Event 014 decision-asset gaps recorded by the GFX audit in their own event asset packages.
- Consolidate inherited full-interface copies after verifying which historical texture paths are supplied through packaged DLC archives.
