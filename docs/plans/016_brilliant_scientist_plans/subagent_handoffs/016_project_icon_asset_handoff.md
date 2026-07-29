# Event 016 project-icon asset handoff

Status: complete for the bounded 76-asset project-icon tranche.

## Counts and runtime paths

The package contains exactly 60 decision DDS files, one for each of 15 project families at Theory, Prototype, Deployment, and Weaponization or Autonomy stages.

The decision runtime folder is `gfx/interface/decisions/016_brilliant_scientist/projects/`.

The package contains exactly 16 dedicated special-project DDS files, one for every live `sp_brilliant_scientist_*` definition in `common/special_projects/projects/016_brilliant_scientist_projects.txt`.

The special-project runtime folder is `gfx/interface/special_project/project_icons/016_brilliant_scientist/`.

Decision assets are 32x32 and special-project assets are 161x98, matching the verified vanilla special-project project-icon footprint.

## Evidence package

Source atlases and raw source quadrant PNGs are under `docs/assets/016_brilliant_scientist/project_icons/source_atlas/` and `source_special_atlas/`.

Processed PNG previews are under `processed_decisions/` and `processed_special_projects/`.

DDS staging copies are under `dds_decisions/` and `dds_special_projects/`.

DDS-decoded evidence PNGs for all 76 runtime files are under `evidence_decoded/`.

Review contact sheets are `contact_sheets/decision_project_icons_contact_sheet.png` and `contact_sheets/special_project_icons_contact_sheet.png`.

The complete machine-readable manifest is `manifest.json`.

The complete validation and SHA-256 record is `validation.json`.

The exact consumer assignment ledger is `assignment_ledger.csv`.

Generation and processing provenance is `prompt_provenance.md`.

The parent wiring note is `gfx_handoff.md`.

## Consumer mapping

Every live `brilliant_scientist_advance_<family>_theory`, `brilliant_scientist_advance_<family>_deployment`, and `brilliant_scientist_advance_<family>_weaponization` decision is mapped to its matching family-stage icon.

Every live `brilliant_scientist_integrate_*_prototype` decision is mapped to the matching family Prototype icon, including `brilliant_scientist_integrate_computation_prototype` to `computational_mathematics_prototype`.

Every live special-project ID maps to an exact `GFX_sp_brilliant_scientist_*` sprite name and same-stem DDS filename in the special-project runtime folder.

The parent agent owns final `.gfx`, decision, special-project, localisation, and consumer edits. This tranche does not modify those files.

## Validation summary

All 76 records in `validation.json` are `complete` with the expected dimensions, non-empty alpha, exact DDS byte lengths, legacy DDS header fields, BGRA masks, texture caps, and decoded evidence.

DDS conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` for every final file.

The verified vanilla reference sample is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/special_project/project_icons/sp_air_axial_jet_engine.dds`, which declares 161x98 and a 63240-byte file.

## Parent visual checklist

- [x] 15 family rows are distinct at native 32x32 and are not recolors of one base icon.
- [x] All four stage compositions exist per family, including Prototype.
- [x] 16 special-project icons are separately composed from the decision atlases.
- [x] Special-project icons preserve family motifs while using the 161x98 wide composition.
- [x] Green chroma-key backgrounds were removed with an alpha matte and spill cleanup.
- [x] Contact sheets were reviewed at native-sized previews.
- [x] No readable text, flags, modern digital electronics, atom-only motif, watermark, or placeholder/fallback was intentionally used.
- [x] Runtime filenames and event-scoped paths are stable and collision-safe.

## Blockers and needs_user_review

No asset is blocked and no asset is marked `needs_user_review` by the production validation. Parent visual review remains appropriate before final consumer wiring, but no fallback or simplification was used.

## Parent consumer wiring

The parent wiring pass created `interface/016_brilliant_scientist_project_icons.gfx`, changed the 60 ledger-listed consumers in `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, and changed both icon fields for all 16 live definitions in `common/special_projects/projects/016_brilliant_scientist_projects.txt`.

Row-level validation found 60 of 60 decision consumers on their exact ledger sprites, 16 of 16 top-level special-project icons and 16 of 16 unique-reward icons on their exact dedicated sprites, and 76 unique sprite registrations matching all 76 ledger name/path pairs. All 76 registered runtime DDS paths exist. The three wired script files have balanced braces, and the scoped diff check reports no whitespace errors.

No localisation or gameplay logic changed in this wiring pass. No fallback, placeholder, or simplification was introduced.
