# Mengele Cloning Special Project

## Overview

`sp_mengele_cloning` is a biowarfare special project tied to the Germany Mengele chain and the Angelic Directorate special-project registry. It represents a sealed biomedical replication program that converts controlled biowarfare facilities into transferable clone-equipment production.

The project is not part of the standard disease payload set. It becomes visible when Germany authorizes the full Auschwitz program and receives `germany_mengele.23`, or when the post-revolt Directorate unlocks hidden projects through `make_random_directorate_special_project_researchable` or `make_all_directorate_special_projects_researchable`.

## Flow

1. Full authorization schedules `germany_mengele.23`.
2. Accepting the proposal sets `germany_mengele_cloning_project_available` and `directorate_special_project_cloning_available`.
3. The `sp_mengele_cloning` project becomes visible in the biowarfare specialization.
4. Completion calls `germany_mengele_complete_cloning_project`.
5. The effect sets completion flags, selects the Mengele refinement of the shared clone API, and produces the first facility-derived clone-equipment batch.
6. If Germany completes the project while the Mengele program is still active, `germany_mengele.24` fires and calls `germany_mengele_start_coup`.

## Manpower Scaling

The completed project calls `germany_mengele_produce_clone_equipment` every week. Each controlled `biowarfare_facility` produces one physical `clone_equipment_1` unit per weekly pulse.

The shared `clone_refresh_reserve_manpower` effect reads the holder's physical stockpile and applies `10` weekly manpower for every clone-equipment unit held in reserve. Equipment assigned to deployed battalions does not count, while captured or transferred stockpiles immediately serve their new holder.

- one controlled biowarfare facility = one new clone-equipment unit per week
- one clone-equipment unit held in reserve = `10` weekly manpower
- clone equipment committed to a battalion no longer contributes reserve manpower

The production effect is called by the dedicated Mengele weekly on-action after project completion and immediately after relevant scripted facility additions.

## Integration

The project is registered in:

- `common/special_projects/projects/mengele_cloning_projects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `common/scripted_effects/germany_mengele_effects.txt`
- `events/germany_mengele.txt`

The shared reserve modifier is defined in `common/dynamic_modifiers/clone_system_dynamic_modifiers.txt`, and the provider-neutral effects are defined in `common/scripted_effects/clone_system_effects.txt`.

## Assets

The project icon is:

- sprite: `GFX_sp_mengele_cloning`
- DDS: `gfx/interface/special_project/project_icons/sp_mengele_cloning.dds`
- GFX definition: `interface/special_projects/biowarfare.gfx`
- manifest: `docs/assets/mengele_cloning_special_project/manifest.md`

## Future Plans

- Add unique prototype reward events if the cloning project needs more mid-research narrative.
- Add clone-equipment recovery choices to future laboratory capture events when they need outcomes more specific than ordinary equipment seizure.
