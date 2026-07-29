# Event 016 project-icon GFX handoff

This handoff is for the parent agent to wire without editing consumer files in this asset tranche.

## Decision icons

The 60 final DDS files are under `gfx/interface/decisions/016_brilliant_scientist/projects/`.

Use sprite names `GFX_decision_brilliant_scientist_project_<family>_<stage>` where `<family>` is the lower_snake_case family name and `<stage>` is `theory`, `prototype`, `deployment`, or `weaponization`.

Every stage-to-consumer mapping is recorded in `assignment_ledger.csv` and in `manifest.json`.

The live board decision IDs are mapped as follows: each `brilliant_scientist_advance_<family>_theory`, `brilliant_scientist_advance_<family>_deployment`, and `brilliant_scientist_advance_<family>_weaponization` uses the matching family and stage icon, while each `brilliant_scientist_integrate_*_prototype` uses the matching Prototype icon.

The computation consumer is named `brilliant_scientist_integrate_computation_prototype` and maps to the `computational_mathematics_prototype` DDS.

## Special-project icons

The 16 final DDS files are under `gfx/interface/special_project/project_icons/016_brilliant_scientist/`.

Each special-project sprite name is stable and exact: `GFX_sp_brilliant_scientist_<project_id_suffix>`.

The parent should set each live `sp_brilliant_scientist_*` definition's `icon` to the matching exact sprite name from `assignment_ledger.csv`.

Special-project files are separately composed 161x98 assets and are not resized decision icons.

## Runtime and validation facts

The final DDS outputs are legacy one-level uncompressed BGRA with exact target dimensions, 32-bit alpha, texture caps, and no mipmaps.

`validation.json` records decoded evidence paths, alpha ranges, DDS header checks, dimensions, byte lengths, SHA-256 hashes, and completion status for all 76 files.

`contact_sheets/decision_project_icons_contact_sheet.png` and `contact_sheets/special_project_icons_contact_sheet.png` are review-only and must not be used as runtime textures.
