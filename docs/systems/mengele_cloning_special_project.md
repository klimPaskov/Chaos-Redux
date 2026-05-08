# Mengele Cloning Special Project

## Overview

`sp_mengele_cloning` is a biowarfare special project tied to the Germany Mengele chain and the Angelic Directorate special-project registry. It represents a sealed biomedical replication program that converts controlled biowarfare facilities into a manpower pipeline.

The project is not part of the standard disease payload set. It becomes visible when Germany authorizes the full Auschwitz program and receives `germany_mengele.23`, or when the post-revolt Directorate unlocks hidden projects through `make_random_directorate_special_project_researchable` or `make_all_directorate_special_projects_researchable`.

## Flow

1. Full authorization schedules `germany_mengele.23`.
2. Accepting the proposal sets `germany_mengele_cloning_project_available` and `directorate_special_project_cloning_available`.
3. The `sp_mengele_cloning` project becomes visible in the biowarfare specialization.
4. Completion calls `germany_mengele_complete_cloning_project`.
5. The effect sets completion flags and updates `mengele_cloning_facility_manpower`.
6. If Germany completes the project while the Mengele program is still active, `germany_mengele.24` fires and calls `germany_mengele_start_coup`.

## Manpower Scaling

The completed project applies the dynamic modifier `mengele_cloning_facility_manpower`. Its `weekly_manpower` modifier reads the country variable `mengele_cloning_weekly_manpower`.

`germany_mengele_update_cloning_project_manpower` recalculates that variable from controlled `biowarfare_facility` count:

- one controlled biowarfare facility = `10,000` weekly manpower
- two controlled biowarfare facilities = `20,000` weekly manpower
- and so on

The update is called when the project completes and when scripted Mengele or Directorate facility-building effects add a facility. This avoids adding a new daily or weekly world iteration.

## Integration

The project is registered in:

- `common/special_projects/projects/mengele_cloning_projects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `common/scripted_effects/germany_mengele_effects.txt`
- `events/germany_mengele.txt`

The dynamic manpower modifier is defined in `common/dynamic_modifiers/chaosx_dynamic_modifiers.txt`.

## Assets

The project icon is:

- sprite: `GFX_sp_mengele_cloning`
- DDS: `gfx/interface/special_project/project_icons/sp_mengele_cloning.dds`
- GFX definition: `interface/special_projects/biowarfare.gfx`
- manifest: `docs/assets/mengele_cloning_special_project/manifest.md`

## Future Plans

- Add unique prototype reward events if the cloning project needs more mid-research narrative.
- Recalculate the dynamic manpower modifier from a construction-completion hook if a future HOI4-safe on-action is already being used for biowarfare facility construction.
