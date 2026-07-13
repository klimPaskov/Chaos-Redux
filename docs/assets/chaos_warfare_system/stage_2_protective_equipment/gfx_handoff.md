# Stage 2 protective-equipment GFX handoff

Parent wiring only. No `.gfx` or `.gui` file was edited in this asset package.

Closure: the parent implementation has copied and reconciled all 51 declarations into `interface/cbrn_protection.gfx`; every listed runtime texture exists, and the national-reserve, priority-state, and emergency-state sprite names follow the implemented decision identifiers. The separate defective-reconditioned-batch report sprite is wired in the same GFX file.

The declarations below are copy-ready `spriteType` blocks. Paths are the runtime DDS paths and should be copied into the intended parent GFX files. The equipment cards use the verified runtime-equivalent path under `gfx/interface/technologies/.../equipment/`.

## Intended files and framing

- Technologies: `interface/cbrn_protection.gfx`, `64x64`.
- Equipment cards and archetype summaries: `interface/cbrn_protection.gfx`, `131x52`.
- Decision categories and decisions: `interface/cbrn_protection.gfx`, categories `52x40`, decisions `32x32`.
- State dynamic modifiers: `interface/cbrn_protection.gfx`, idea-style `64x64`.
- Names marked exact below were supplied by the parent request. Other sprite names are stable lowercase-ID-derived proposals and should be retained unless an existing parent contract already fixes a different name.

## Technology declarations

```text
spriteType = {
	name = "GFX_sealed_assault_protection_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/sealed_assault_protection.dds"
}
spriteType = {
	name = "GFX_field_decontamination_kits_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/field_decontamination_kits.dds"
}
spriteType = {
	name = "GFX_mobile_wash_columns_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/mobile_wash_columns.dds"
}
spriteType = {
	name = "GFX_rapid_decontamination_plants_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/rapid_decontamination_plants.dds"
}
spriteType = {
	name = "GFX_chemical_detection_paper_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/chemical_detection_paper.dds"
}
spriteType = {
	name = "GFX_mobile_sampling_laboratories_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/mobile_sampling_laboratories.dds"
}
spriteType = {
	name = "GFX_theater_cbrn_command_set_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/theater_cbrn_command_set.dds"
}
spriteType = {
	name = "GFX_military_filter_standardization_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/military_filter_standardization.dds"
}
spriteType = {
	name = "GFX_civil_defence_fitting_and_registration_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/civil_defence_fitting_and_registration.dds"
}
spriteType = {
	name = "GFX_rapid_filter_replacement_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/rapid_filter_replacement.dds"
}
spriteType = {
	name = "GFX_vehicle_overpressure_and_sealed_compartments_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/vehicle_overpressure_and_sealed_compartments.dds"
}
```

## Equipment card and archetype declarations

```text
spriteType = {
	name = "GFX_gas_mask_equipment_1_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/gas_mask_equipment_1.dds"
}
spriteType = {
	name = "GFX_gas_mask_equipment_2_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/gas_mask_equipment_2.dds"
}
spriteType = {
	name = "GFX_gas_mask_equipment_3_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/gas_mask_equipment_3.dds"
}
spriteType = {
	name = "GFX_gas_mask_equipment_4_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/gas_mask_equipment_4.dds"
}
spriteType = {
	name = "GFX_gas_mask_equipment_reconditioned_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/gas_mask_equipment_reconditioned.dds"
}
spriteType = {
	name = "GFX_decontamination_equipment_1_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/decontamination_equipment_1.dds"
}
spriteType = {
	name = "GFX_decontamination_equipment_2_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/decontamination_equipment_2.dds"
}
spriteType = {
	name = "GFX_decontamination_equipment_3_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/decontamination_equipment_3.dds"
}
spriteType = {
	name = "GFX_cbrn_instrument_equipment_1_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/cbrn_instrument_equipment_1.dds"
}
spriteType = {
	name = "GFX_cbrn_instrument_equipment_2_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/cbrn_instrument_equipment_2.dds"
}
spriteType = {
	name = "GFX_cbrn_instrument_equipment_3_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/cbrn_instrument_equipment_3.dds"
}
spriteType = {
	name = "GFX_archetype_gas_mask_equipment_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/archetype_gas_mask_equipment.dds"
}
spriteType = {
	name = "GFX_archetype_decontamination_equipment_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/archetype_decontamination_equipment.dds"
}
spriteType = {
	name = "GFX_archetype_cbrn_instrument_equipment_medium"
	texturefile = "gfx/interface/technologies/stage_2_protective_equipment/equipment/archetype_cbrn_instrument_equipment.dds"
}
```

## Decision category declarations

```text
spriteType = {
	name = "GFX_decision_category_cbrn_program_management"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/categories/cbrn_program_management_category.dds"
}
spriteType = {
	name = "GFX_decision_category_cbrn_civil_defence"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/categories/cbrn_civil_defence_category.dds"
}
```

## Decision declarations

```text
spriteType = {
	name = "GFX_decision_cbrn_establish_national_respirator_reserve"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_establish_respirator_reserve.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_register_and_fit_population"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_register_and_fit_population.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_issue_masks_to_field_army"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_issue_masks_to_field_army.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_priority_state_mask_issue"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_issue_masks_to_priority_state.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_full_state_mask_distribution"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_full_state_mask_distribution.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_emergency_state_mask_distribution"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_emergency_mask_distribution.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_replace_military_mask_filters"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_replace_military_mask_filters.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_replace_state_mask_filters"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_replace_state_mask_filters.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_recondition_old_masks"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_recondition_old_masks.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_supply_occupied_population"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_supply_occupied_population.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_export_protective_equipment"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_export_protective_equipment.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_convert_civilian_mask_industry"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_convert_civilian_mask_industry.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_import_protective_equipment"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_import_protective_equipment.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_license_foreign_respirator_design"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_license_foreign_respirator_design.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_simplify_filters_for_mass_issue"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_simplify_filters_for_mass_issue.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_protect_hospitals_and_utilities"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_protect_hospitals_and_utilities.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_move_civilians_to_shelters"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_move_civilians_to_shelters.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_sound_chemical_alarm"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_sound_chemical_alarm.dds"
}
spriteType = {
	name = "GFX_decision_cbrn_keep_industry_operating"
	texturefile = "gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_keep_industry_operating.dds"
}
```

## State dynamic-modifier declarations

```text
spriteType = {
	name = "GFX_cbrn_chemical_alarm_disruption"
	texturefile = "gfx/interface/ideas/stage_2_protective_equipment/cbrn_chemical_alarm_disruption.dds"
}
spriteType = {
	name = "GFX_cbrn_civilian_shelter_disruption"
	texturefile = "gfx/interface/ideas/stage_2_protective_equipment/cbrn_civilian_shelter_disruption.dds"
}
spriteType = {
	name = "GFX_cbrn_hospitals_utilities_protected"
	texturefile = "gfx/interface/ideas/stage_2_protective_equipment/cbrn_hospitals_utilities_protected.dds"
}
spriteType = {
	name = "GFX_cbrn_industry_kept_operating"
	texturefile = "gfx/interface/ideas/stage_2_protective_equipment/cbrn_industry_kept_operating.dds"
}
spriteType = {
	name = "GFX_cbrn_emergency_distribution_disruption"
	texturefile = "gfx/interface/ideas/stage_2_protective_equipment/cbrn_emergency_distribution_disruption.dds"
}
```

## Changed files and validation handoff

Changed inside the bounded asset package:

- `source_png/`: 51 generated source masters.
- `processed_png/`: 51 exact-size alpha PNGs.
- `dds/`: 51 package DDS archives.
- `contact_sheets/`: technology, equipment, category, decision, and state review sheets.
- `prompts/stage_2_prompts.md`: source mode and composition prompt keys.
- `manifest.md`: 51 complete manifest rows with paths, IDs, dimensions, sprite proposals, GFX targets, and uncertainty.
- `gfx_handoff.md`: this parent wiring handoff.
- Runtime-copy DDS directories under `gfx/interface/technologies/stage_2_protective_equipment/`, `gfx/interface/decisions/stage_2_protective_equipment/`, and `gfx/interface/ideas/stage_2_protective_equipment/`.

Meaningful validation completed:

- Source/processed/final counts agree at 51 per workflow stage.
- Processed PNG dimensions group exactly as `11x64x64`, `14x131x52`, `2x52x40`, `19x32x32`, and `5x64x64`; all are RGBA with visible alpha.
- DDS headers for all 51 package files have the expected dimensions, `DDPF_RGB | DDPF_ALPHAPIXELS`, 32-bit pixels, zero compression FourCC, repository channel masks, and no mip chain; byte lengths match the uncompressed surface size.
- Contact sheets were visually inspected over checkerboards; the two filter-replacement decisions are distinct, the reconditioned card is visibly aged/repaired, archetypes are family summaries, and the four added technologies have distinct compositions.
- No `.gfx`, `.gui`, gameplay, localisation, documentation-spec, or package-spec file was edited, and no commit was created.
