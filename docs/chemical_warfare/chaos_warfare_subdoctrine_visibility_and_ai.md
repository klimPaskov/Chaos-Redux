# Chaos Warfare Subdoctrine Visibility and AI

## Overview
This update changes how Chaos Warfare land subdoctrines appear in the doctrine interface and how the AI evaluates them.

Affected subdoctrines:

- `extermination_columns`
- `chemical_suppression`
- `contaminant_firebases`
- `integrated_chemical_operations`

## Step by Step Behavior
1. Each Chaos Warfare subdoctrine remains visible in the doctrine interface even when the country does not currently have `chaos_warfare` selected as its land grand doctrine.
2. Each subdoctrine still keeps `available = { has_doctrine = chaos_warfare }`, so the branch is shown but cannot be selected until Chaos Warfare is active.
3. Each subdoctrine AI weight is forced to `0` when the country does not have `chaos_warfare`.
4. Once the country does have `chaos_warfare`, the existing subdoctrine AI weighting applies again, including the major-country bonus already present in the branch definitions.

## Files
- `common/doctrines/subdoctrines/land/chaos_warfare_infantry_subdoctrines.txt`
- `common/doctrines/subdoctrines/land/chaos_warfare_armor_subdoctrines.txt`
- `common/doctrines/subdoctrines/land/chaos_warfare_combat_support_subdoctrines.txt`
- `common/doctrines/subdoctrines/land/chaos_warfare_operations_subdoctrines.txt`
- `docs/chemical_warfare/chaos_warfare_chemical_suppression.md`

## AI Notes
- This does not make non-Chaos countries eligible to pick the branch.
- The explicit zero-weight guard is kept so UI visibility does not create accidental AI pressure toward these subdoctrines.

## Icons
No new icons or sprite registrations are required.

Existing doctrine icons remain:

- `GFX_doctrine_extermination_columns_medium`
- `GFX_doctrine_chemical_suppression_medium`
- `GFX_doctrine_contaminant_firebases_medium`
- `GFX_doctrine_integrated_chemical_operations_medium`

Existing sprite file remains:

- `interface/chaosx_doctrines.gfx`

## Future Extensions
1. Add more detailed AI weighting inside the Chaos branch based on chemical stockpile depth, active doctrine spirits, and frontline template composition.
2. Add a dedicated locked-branch tooltip treatment if clearer player messaging is needed for visible-but-unavailable Chaos subdoctrines.
