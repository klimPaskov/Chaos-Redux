# Package navigation review

Date: 2026-09-05.
Disposition: navigation repairs implemented.
Acceptance basis: the user's documentation cleanup request and subsequent approval to apply the full-reading prerequisite separately to bounded batches.
The documentation curator completed a read-only review of the 37 package entry files listed below.
The parent reviewed its handoff and integrated their paths into [the specification index](../../../specs/README.md).
No package contents, design decisions, identifiers, catalog records, or implementation statuses were changed.

## Navigation evidence

The specification index previously omitted these 37 direct event package directories.
It links all 76 direct directories after integration: 68 event packages, seven shared packages, and the nested `docs/` tree with an unresolved-authority notice.
The Time Traveler link was also repaired from the missing `030_time_traveler_spec_index.md` to the existing package `README.md`.
The parent checked every relative link in both main indexes against the filesystem.
The [plans index](../../README.md) links all 65 direct plan directories.
Directory coverage does not establish full reading of their interiors.

## Full-read ledger

All paths in this list are relative to `docs/specs/`.

- `012_africa_is_one_gods_of_africa_specs/README.md`
- `022_concentration_camps_specs/022_concentration_camps_index.md`
- `033_acid_rain_specs/README.md`
- `034_industrial_boom_specs/034_industrial_boom_spec_index.md`
- `035_great_depression_specs/035_great_depression_spec_index.md`
- `036_chemical_and_biological_weapons_convention_specs/README.md`
- `037_mysterious_people_specs/README.md`
- `038_malta_crusaders_specs/00_README.md`
- `039_murder_mystery_specs/039_murder_mystery_package_index.md`
- `040_lawrence_of_arabia_specs/README.md`
- `041_disease_in_divisions_specs/README.md`
- `042_equipment_from_heavens_specs/README.md`
- `043_monsters_from_the_deep_specs/README.md`
- `044_yakub_returns_specs/README.md`
- `045_third_balkan_war_specs/README.md`
- `046_the_great_shuffle_specs/README.md`
- `047_boom_specs/README.md`
- `048_old_great_bulgaria_specs/README.md`
- `049_doomsday_specs/README.md`
- `050_the_great_embargo_specs/README.md`
- `051_heat_wave_specs/README.md`
- `052_intel_leaked_specs/README.md`
- `053_mysterious_man_specs/README.md`
- `054_gift_from_scientists_specs/README.md`
- `055_the_great_infrastructure_project_specs/README.md`
- `056_the_navy_specs/README.md`
- `057_the_black_market_specs/README.md`
- `058_random_buildings_specs/README.md`
- `059_the_offensive_specs/README.md`
- `060_research_failure_specs/README.md`
- `061_return_to_peacetime_specs/README.md`
- `062_allies_backstab_specs/README.md`
- `063_subjects_break_free_specs/README.md`
- `064_border_fortifications_specs/README.md`
- `065_random_trait_specs/README.md`
- `066_abundance_specs/README.md`
- `067_generalissimo_specs/README.md`

## Source cautions retained

The entry documents contain planning labels, legacy export comparisons, unavailable-tool reports, and limits on completed work.
Those statements describe the source documents and were not revalidated against current gameplay, the workbook, or MCP output in this navigation review.
Their inclusion in the main index does not approve their design or resolve their status.

The Gods of Africa entry names an intended destination different from its actual direct package location.
The index points to the existing file without moving it or deciding which location should own the design.
The Great Depression entry describes a consolidated `full_spec` copy.
Its contents were not merged or promoted through this review.
Several entries propose `SCN-015`, including Events 043, 044, and 067.
These proposals need a separate acceptance and identifier reconciliation against the current catalog before implementation.

The nested tree was inventoried only, with 62 files and directories recorded at review time.
Its interiors were not read.
The four roots are:

- `docs/specs/docs/plans/046_the_great_shuffle_plans/`
- `docs/specs/docs/plans/047_boom_plans/`
- `docs/specs/docs/specs/046_the_great_shuffle_specs/`
- `docs/specs/docs/specs/047_boom_specs/`

Their relationship to the direct Event 046 and Event 047 packages remains unresolved.
Full content and decision-evidence comparison is required before any consolidation or removal.
No deletion was authorized or performed.

## Completion boundary

The missing navigation entries and broken Time Traveler link are repaired without design simplifications.
The wider package interiors, current engine behavior, acceptance decisions, and nested-tree reconciliation remain outside this completed navigation batch.
The worker performed no gameplay, localisation, asset, spreadsheet, plan-interior, or MCP inspection.
The parent retains final integration and completion responsibility.
