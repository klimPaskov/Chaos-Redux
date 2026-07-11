# Camp repression rework icon GFX handoff

## Ownership boundary

This handoff records the live sprite registrations for the completed static icon tranche. All blocks below are present inside the named `spriteTypes = { ... }` registries and resolve to the delivered DDS files.

- All 37 decision and 30 idea sprites are registered in `interface/camp_repression_rework.gfx`.
- All 5 special-project sprites are registered in `interface/special_projects/biowarfare.gfx`.
- All 30 achievement aliases are registered in `interface/chaosx_achievements.gfx`.
- These are single-frame static sprites; do not add `noOfFrames`.
- Keep the sprite names and texture paths exact. The scripted decisions, ideas, special projects, and achievement IDs already use these names/file stems.

## Decision sprite inventory

| Sprite ID | Exact runtime DDS | Dimensions | Registration file |
| --- | --- | --- | --- |
| `GFX_decision_bel_colonial_inspection` | `gfx/interface/camp_repression/icons/GFX_decision_bel_colonial_inspection.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_bel_congo_concession_quota` | `gfx/interface/camp_repression/icons/GFX_decision_bel_congo_concession_quota.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_bel_congo_transport_corridor` | `gfx/interface/camp_repression/icons/GFX_decision_bel_congo_transport_corridor.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_camp_dismantlement` | `gfx/interface/camp_repression/icons/GFX_decision_camp_dismantlement.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_camp_evidence_destruction` | `gfx/interface/camp_repression/icons/GFX_decision_camp_evidence_destruction.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_camp_guard_allocation` | `gfx/interface/camp_repression/icons/GFX_decision_camp_guard_allocation.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_fr_camp_legacy_review` | `gfx/interface/camp_repression/icons/GFX_decision_fr_camp_legacy_review.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_fr_north_africa_labor` | `gfx/interface/camp_repression/icons/GFX_decision_fr_north_africa_labor.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_generic_destroy_evidence` | `gfx/interface/camp_repression/icons/GFX_decision_generic_destroy_evidence.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_generic_dismantle_network` | `gfx/interface/camp_repression/icons/GFX_decision_generic_dismantle_network.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_generic_expand_labor_network` | `gfx/interface/camp_repression/icons/GFX_decision_generic_expand_labor_network.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_generic_guard_allocation` | `gfx/interface/camp_repression/icons/GFX_decision_generic_guard_allocation.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_germany_auschwitz_transfer` | `gfx/interface/camp_repression/icons/GFX_decision_germany_auschwitz_transfer.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_germany_military_review` | `gfx/interface/camp_repression/icons/GFX_decision_germany_military_review.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_germany_ss_camp_administration` | `gfx/interface/camp_repression/icons/GFX_decision_germany_ss_camp_administration.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_germany_ss_laboratory_annex` | `gfx/interface/camp_repression/icons/GFX_decision_germany_ss_laboratory_annex.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_ita_camp_closure` | `gfx/interface/camp_repression/icons/GFX_decision_ita_camp_closure.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_ita_colonial_road_labor` | `gfx/interface/camp_repression/icons/GFX_decision_ita_colonial_road_labor.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_ita_desert_camp_admin` | `gfx/interface/camp_repression/icons/GFX_decision_ita_desert_camp_admin.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_japan_army_medical_review` | `gfx/interface/camp_repression/icons/GFX_decision_japan_army_medical_review.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_japan_epidemic_containment` | `gfx/interface/camp_repression/icons/GFX_decision_japan_epidemic_containment.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_japan_pingfang_bureau` | `gfx/interface/camp_repression/icons/GFX_decision_japan_pingfang_bureau.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_japan_pingfang_records` | `gfx/interface/camp_repression/icons/GFX_decision_japan_pingfang_records.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_japan_prisoner_experiment` | `gfx/interface/camp_repression/icons/GFX_decision_japan_prisoner_experiment.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_sov_famine_relief` | `gfx/interface/camp_repression/icons/GFX_decision_sov_famine_relief.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_sov_grain_confiscation` | `gfx/interface/camp_repression/icons/GFX_decision_sov_grain_confiscation.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_sov_gulag_dismantlement` | `gfx/interface/camp_repression/icons/GFX_decision_sov_gulag_dismantlement.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_sov_gulag_expansion` | `gfx/interface/camp_repression/icons/GFX_decision_sov_gulag_expansion.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_sov_nkvd_review` | `gfx/interface/camp_repression/icons/GFX_decision_sov_nkvd_review.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_sov_prisoner_transfer` | `gfx/interface/camp_repression/icons/GFX_decision_sov_prisoner_transfer.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_sov_records_retreat` | `gfx/interface/camp_repression/icons/GFX_decision_sov_records_retreat.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_uk_colonial_labor_works` | `gfx/interface/camp_repression/icons/GFX_decision_uk_colonial_labor_works.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_uk_raj_detention` | `gfx/interface/camp_repression/icons/GFX_decision_uk_raj_detention.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_usa_court_review` | `gfx/interface/camp_repression/icons/GFX_decision_usa_court_review.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_usa_emergency_relocation` | `gfx/interface/camp_repression/icons/GFX_decision_usa_emergency_relocation.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_usa_redress_commission` | `gfx/interface/camp_repression/icons/GFX_decision_usa_redress_commission.dds` | `32x32` | `interface/camp_repression_rework.gfx` |
| `GFX_decision_vichy_internment_admin` | `gfx/interface/camp_repression/icons/GFX_decision_vichy_internment_admin.dds` | `32x32` | `interface/camp_repression_rework.gfx` |

## Idea and national-spirit sprite inventory

| Sprite ID | Exact runtime DDS | Dimensions | Registration file |
| --- | --- | --- | --- |
| `GFX_idea_bel_congo_extraction_pressure` | `gfx/interface/camp_repression/icons/GFX_idea_bel_congo_extraction_pressure.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_camp_democratic_legitimacy_crisis` | `gfx/interface/camp_repression/icons/GFX_idea_camp_democratic_legitimacy_crisis.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_camp_dismantlement_reform` | `gfx/interface/camp_repression/icons/GFX_idea_camp_dismantlement_reform.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_camp_network_overreach` | `gfx/interface/camp_repression/icons/GFX_idea_camp_network_overreach.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_camp_repression_overstretch` | `gfx/interface/camp_repression/icons/GFX_idea_camp_repression_overstretch.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_camp_repression_reform_pressure` | `gfx/interface/camp_repression/icons/GFX_idea_camp_repression_reform_pressure.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_congo_concession_labor_burden` | `gfx/interface/camp_repression/icons/GFX_idea_congo_concession_labor_burden.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_fr_camp_legacy` | `gfx/interface/camp_repression/icons/GFX_idea_fr_camp_legacy.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_generic_detention_network` | `gfx/interface/camp_repression/icons/GFX_idea_generic_detention_network.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_generic_overextended_repression_network` | `gfx/interface/camp_repression/icons/GFX_idea_generic_overextended_repression_network.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_germany_auschwitz_evidence_pressure` | `gfx/interface/camp_repression/icons/GFX_idea_germany_auschwitz_evidence_pressure.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_germany_dormant_ss_camp_legacy` | `gfx/interface/camp_repression/icons/GFX_idea_germany_dormant_ss_camp_legacy.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_germany_ss_camp_administration` | `gfx/interface/camp_repression/icons/GFX_idea_germany_ss_camp_administration.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_ita_desert_camp_administration` | `gfx/interface/camp_repression/icons/GFX_idea_ita_desert_camp_administration.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_ita_libyan_resistance_pressure` | `gfx/interface/camp_repression/icons/GFX_idea_ita_libyan_resistance_pressure.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_japan_ishii_influence` | `gfx/interface/camp_repression/icons/GFX_idea_japan_ishii_influence.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_japan_kwantung_autonomy` | `gfx/interface/camp_repression/icons/GFX_idea_japan_kwantung_autonomy.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_japan_occupation_apparatus` | `gfx/interface/camp_repression/icons/GFX_idea_japan_occupation_apparatus.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_japan_outbreak_pressure` | `gfx/interface/camp_repression/icons/GFX_idea_japan_outbreak_pressure.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_japan_program_review` | `gfx/interface/camp_repression/icons/GFX_idea_japan_program_review.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_raj_colonial_labor_burden` | `gfx/interface/camp_repression/icons/GFX_idea_raj_colonial_labor_burden.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_sov_famine_pressure` | `gfx/interface/camp_repression/icons/GFX_idea_sov_famine_pressure.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_sov_gulag_authority` | `gfx/interface/camp_repression/icons/GFX_idea_sov_gulag_authority.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_sov_gulag_legacy` | `gfx/interface/camp_repression/icons/GFX_idea_sov_gulag_legacy.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_sov_gulag_reform` | `gfx/interface/camp_repression/icons/GFX_idea_sov_gulag_reform.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_sov_republic_fear` | `gfx/interface/camp_repression/icons/GFX_idea_sov_republic_fear.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_uk_imperial_detention_administration` | `gfx/interface/camp_repression/icons/GFX_idea_uk_imperial_detention_administration.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_usa_civil_liberties_damage` | `gfx/interface/camp_repression/icons/GFX_idea_usa_civil_liberties_damage.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_usa_wartime_security_authority` | `gfx/interface/camp_repression/icons/GFX_idea_usa_wartime_security_authority.dds` | `64x64` | `interface/camp_repression_rework.gfx` |
| `GFX_idea_vichy_collaboration_repression` | `gfx/interface/camp_repression/icons/GFX_idea_vichy_collaboration_repression.dds` | `64x64` | `interface/camp_repression_rework.gfx` |

## Special-project sprite inventory

| Sprite ID | Exact runtime DDS | Dimensions | Registration file |
| --- | --- | --- | --- |
| `GFX_sp_japan_cherry_blossom_dossier` | `gfx/interface/camp_repression/icons/GFX_sp_japan_cherry_blossom_dossier.dds` | `161x98` | `interface/special_projects/biowarfare.gfx` |
| `GFX_sp_japan_epidemic_mapping_bureau` | `gfx/interface/camp_repression/icons/GFX_sp_japan_epidemic_mapping_bureau.dds` | `161x98` | `interface/special_projects/biowarfare.gfx` |
| `GFX_sp_japan_kwantung_medical_intelligence` | `gfx/interface/camp_repression/icons/GFX_sp_japan_kwantung_medical_intelligence.dds` | `161x98` | `interface/special_projects/biowarfare.gfx` |
| `GFX_sp_japan_occupation_test_ledger` | `gfx/interface/camp_repression/icons/GFX_sp_japan_occupation_test_ledger.dds` | `161x98` | `interface/special_projects/biowarfare.gfx` |
| `GFX_sp_japan_pingfang_records_office` | `gfx/interface/camp_repression/icons/GFX_sp_japan_pingfang_records_office.dds` | `161x98` | `interface/special_projects/biowarfare.gfx` |

## Achievement sprite inventory

All ten achievements have exact normal, grey, and not-eligible aliases. The engine-facing DDS filenames omit the `GFX_achievement_` prefix; the explicit aliases retain it, matching the repository convention.

| Sprite ID | Exact runtime DDS | Dimensions | Registration file |
| --- | --- | --- | --- |
| `GFX_achievement_000_chaos_redux_60_inherit_the_ledger_close_the_ledger` | `gfx/achievements/000_chaos_redux_60_inherit_the_ledger_close_the_ledger.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_60_inherit_the_ledger_close_the_ledger_grey` | `gfx/achievements/000_chaos_redux_60_inherit_the_ledger_close_the_ledger_grey.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_60_inherit_the_ledger_close_the_ledger_not_eligible` | `gfx/achievements/000_chaos_redux_60_inherit_the_ledger_close_the_ledger_not_eligible.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_61_papers_for_the_liberated` | `gfx/achievements/000_chaos_redux_61_papers_for_the_liberated.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_61_papers_for_the_liberated_grey` | `gfx/achievements/000_chaos_redux_61_papers_for_the_liberated_grey.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_61_papers_for_the_liberated_not_eligible` | `gfx/achievements/000_chaos_redux_61_papers_for_the_liberated_not_eligible.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_62_the_doctor_loses_his_war` | `gfx/achievements/000_chaos_redux_62_the_doctor_loses_his_war.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_62_the_doctor_loses_his_war_grey` | `gfx/achievements/000_chaos_redux_62_the_doctor_loses_his_war_grey.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_62_the_doctor_loses_his_war_not_eligible` | `gfx/achievements/000_chaos_redux_62_the_doctor_loses_his_war_not_eligible.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_63_no_pingfang_shadow` | `gfx/achievements/000_chaos_redux_63_no_pingfang_shadow.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_63_no_pingfang_shadow_grey` | `gfx/achievements/000_chaos_redux_63_no_pingfang_shadow_grey.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_63_no_pingfang_shadow_not_eligible` | `gfx/achievements/000_chaos_redux_63_no_pingfang_shadow_not_eligible.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_64_grain_before_fear` | `gfx/achievements/000_chaos_redux_64_grain_before_fear.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_64_grain_before_fear_grey` | `gfx/achievements/000_chaos_redux_64_grain_before_fear_grey.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_64_grain_before_fear_not_eligible` | `gfx/achievements/000_chaos_redux_64_grain_before_fear_not_eligible.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_65_dominion_without_chains` | `gfx/achievements/000_chaos_redux_65_dominion_without_chains.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_65_dominion_without_chains_grey` | `gfx/achievements/000_chaos_redux_65_dominion_without_chains_grey.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_65_dominion_without_chains_not_eligible` | `gfx/achievements/000_chaos_redux_65_dominion_without_chains_not_eligible.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_66_redress_before_victory` | `gfx/achievements/000_chaos_redux_66_redress_before_victory.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_66_redress_before_victory_grey` | `gfx/achievements/000_chaos_redux_66_redress_before_victory_grey.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_66_redress_before_victory_not_eligible` | `gfx/achievements/000_chaos_redux_66_redress_before_victory_not_eligible.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_67_congo_reformed` | `gfx/achievements/000_chaos_redux_67_congo_reformed.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_67_congo_reformed_grey` | `gfx/achievements/000_chaos_redux_67_congo_reformed_grey.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_67_congo_reformed_not_eligible` | `gfx/achievements/000_chaos_redux_67_congo_reformed_not_eligible.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_68_roads_without_camps` | `gfx/achievements/000_chaos_redux_68_roads_without_camps.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_68_roads_without_camps_grey` | `gfx/achievements/000_chaos_redux_68_roads_without_camps_grey.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_68_roads_without_camps_not_eligible` | `gfx/achievements/000_chaos_redux_68_roads_without_camps_not_eligible.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_69_gurs_closed` | `gfx/achievements/000_chaos_redux_69_gurs_closed.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_69_gurs_closed_grey` | `gfx/achievements/000_chaos_redux_69_gurs_closed_grey.dds` | `64x64` | `interface/chaosx_achievements.gfx` |
| `GFX_achievement_000_chaos_redux_69_gurs_closed_not_eligible` | `gfx/achievements/000_chaos_redux_69_gurs_closed_not_eligible.dds` | `64x64` | `interface/chaosx_achievements.gfx` |

## Ready-to-paste decision and idea blocks

Append these blocks inside `interface/camp_repression_rework.gfx`'s existing `spriteTypes = { ... }` wrapper.

```plaintext
	spriteType = {
		name = "GFX_decision_bel_colonial_inspection"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_bel_colonial_inspection.dds"
	}
	spriteType = {
		name = "GFX_decision_bel_congo_concession_quota"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_bel_congo_concession_quota.dds"
	}
	spriteType = {
		name = "GFX_decision_bel_congo_transport_corridor"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_bel_congo_transport_corridor.dds"
	}
	spriteType = {
		name = "GFX_decision_camp_dismantlement"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_camp_dismantlement.dds"
	}
	spriteType = {
		name = "GFX_decision_camp_evidence_destruction"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_camp_evidence_destruction.dds"
	}
	spriteType = {
		name = "GFX_decision_camp_guard_allocation"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_camp_guard_allocation.dds"
	}
	spriteType = {
		name = "GFX_decision_fr_camp_legacy_review"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_fr_camp_legacy_review.dds"
	}
	spriteType = {
		name = "GFX_decision_fr_north_africa_labor"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_fr_north_africa_labor.dds"
	}
	spriteType = {
		name = "GFX_decision_generic_destroy_evidence"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_generic_destroy_evidence.dds"
	}
	spriteType = {
		name = "GFX_decision_generic_dismantle_network"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_generic_dismantle_network.dds"
	}
	spriteType = {
		name = "GFX_decision_generic_expand_labor_network"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_generic_expand_labor_network.dds"
	}
	spriteType = {
		name = "GFX_decision_generic_guard_allocation"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_generic_guard_allocation.dds"
	}
	spriteType = {
		name = "GFX_decision_germany_auschwitz_transfer"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_germany_auschwitz_transfer.dds"
	}
	spriteType = {
		name = "GFX_decision_germany_military_review"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_germany_military_review.dds"
	}
	spriteType = {
		name = "GFX_decision_germany_ss_camp_administration"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_germany_ss_camp_administration.dds"
	}
	spriteType = {
		name = "GFX_decision_germany_ss_laboratory_annex"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_germany_ss_laboratory_annex.dds"
	}
	spriteType = {
		name = "GFX_decision_ita_camp_closure"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_ita_camp_closure.dds"
	}
	spriteType = {
		name = "GFX_decision_ita_colonial_road_labor"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_ita_colonial_road_labor.dds"
	}
	spriteType = {
		name = "GFX_decision_ita_desert_camp_admin"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_ita_desert_camp_admin.dds"
	}
	spriteType = {
		name = "GFX_decision_japan_army_medical_review"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_japan_army_medical_review.dds"
	}
	spriteType = {
		name = "GFX_decision_japan_epidemic_containment"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_japan_epidemic_containment.dds"
	}
	spriteType = {
		name = "GFX_decision_japan_pingfang_bureau"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_japan_pingfang_bureau.dds"
	}
	spriteType = {
		name = "GFX_decision_japan_pingfang_records"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_japan_pingfang_records.dds"
	}
	spriteType = {
		name = "GFX_decision_japan_prisoner_experiment"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_japan_prisoner_experiment.dds"
	}
	spriteType = {
		name = "GFX_decision_sov_famine_relief"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_sov_famine_relief.dds"
	}
	spriteType = {
		name = "GFX_decision_sov_grain_confiscation"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_sov_grain_confiscation.dds"
	}
	spriteType = {
		name = "GFX_decision_sov_gulag_dismantlement"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_sov_gulag_dismantlement.dds"
	}
	spriteType = {
		name = "GFX_decision_sov_gulag_expansion"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_sov_gulag_expansion.dds"
	}
	spriteType = {
		name = "GFX_decision_sov_nkvd_review"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_sov_nkvd_review.dds"
	}
	spriteType = {
		name = "GFX_decision_sov_prisoner_transfer"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_sov_prisoner_transfer.dds"
	}
	spriteType = {
		name = "GFX_decision_sov_records_retreat"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_sov_records_retreat.dds"
	}
	spriteType = {
		name = "GFX_decision_uk_colonial_labor_works"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_uk_colonial_labor_works.dds"
	}
	spriteType = {
		name = "GFX_decision_uk_raj_detention"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_uk_raj_detention.dds"
	}
	spriteType = {
		name = "GFX_decision_usa_court_review"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_usa_court_review.dds"
	}
	spriteType = {
		name = "GFX_decision_usa_emergency_relocation"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_usa_emergency_relocation.dds"
	}
	spriteType = {
		name = "GFX_decision_usa_redress_commission"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_usa_redress_commission.dds"
	}
	spriteType = {
		name = "GFX_decision_vichy_internment_admin"
		texturefile = "gfx/interface/camp_repression/icons/GFX_decision_vichy_internment_admin.dds"
	}
	spriteType = {
		name = "GFX_idea_bel_congo_extraction_pressure"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_bel_congo_extraction_pressure.dds"
	}
	spriteType = {
		name = "GFX_idea_camp_democratic_legitimacy_crisis"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_camp_democratic_legitimacy_crisis.dds"
	}
	spriteType = {
		name = "GFX_idea_camp_dismantlement_reform"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_camp_dismantlement_reform.dds"
	}
	spriteType = {
		name = "GFX_idea_camp_network_overreach"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_camp_network_overreach.dds"
	}
	spriteType = {
		name = "GFX_idea_camp_repression_overstretch"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_camp_repression_overstretch.dds"
	}
	spriteType = {
		name = "GFX_idea_camp_repression_reform_pressure"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_camp_repression_reform_pressure.dds"
	}
	spriteType = {
		name = "GFX_idea_congo_concession_labor_burden"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_congo_concession_labor_burden.dds"
	}
	spriteType = {
		name = "GFX_idea_fr_camp_legacy"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_fr_camp_legacy.dds"
	}
	spriteType = {
		name = "GFX_idea_generic_detention_network"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_generic_detention_network.dds"
	}
	spriteType = {
		name = "GFX_idea_generic_overextended_repression_network"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_generic_overextended_repression_network.dds"
	}
	spriteType = {
		name = "GFX_idea_germany_auschwitz_evidence_pressure"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_germany_auschwitz_evidence_pressure.dds"
	}
	spriteType = {
		name = "GFX_idea_germany_dormant_ss_camp_legacy"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_germany_dormant_ss_camp_legacy.dds"
	}
	spriteType = {
		name = "GFX_idea_germany_ss_camp_administration"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_germany_ss_camp_administration.dds"
	}
	spriteType = {
		name = "GFX_idea_ita_desert_camp_administration"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_ita_desert_camp_administration.dds"
	}
	spriteType = {
		name = "GFX_idea_ita_libyan_resistance_pressure"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_ita_libyan_resistance_pressure.dds"
	}
	spriteType = {
		name = "GFX_idea_japan_ishii_influence"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_japan_ishii_influence.dds"
	}
	spriteType = {
		name = "GFX_idea_japan_kwantung_autonomy"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_japan_kwantung_autonomy.dds"
	}
	spriteType = {
		name = "GFX_idea_japan_occupation_apparatus"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_japan_occupation_apparatus.dds"
	}
	spriteType = {
		name = "GFX_idea_japan_outbreak_pressure"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_japan_outbreak_pressure.dds"
	}
	spriteType = {
		name = "GFX_idea_japan_program_review"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_japan_program_review.dds"
	}
	spriteType = {
		name = "GFX_idea_raj_colonial_labor_burden"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_raj_colonial_labor_burden.dds"
	}
	spriteType = {
		name = "GFX_idea_sov_famine_pressure"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_sov_famine_pressure.dds"
	}
	spriteType = {
		name = "GFX_idea_sov_gulag_authority"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_sov_gulag_authority.dds"
	}
	spriteType = {
		name = "GFX_idea_sov_gulag_legacy"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_sov_gulag_legacy.dds"
	}
	spriteType = {
		name = "GFX_idea_sov_gulag_reform"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_sov_gulag_reform.dds"
	}
	spriteType = {
		name = "GFX_idea_sov_republic_fear"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_sov_republic_fear.dds"
	}
	spriteType = {
		name = "GFX_idea_uk_imperial_detention_administration"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_uk_imperial_detention_administration.dds"
	}
	spriteType = {
		name = "GFX_idea_usa_civil_liberties_damage"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_usa_civil_liberties_damage.dds"
	}
	spriteType = {
		name = "GFX_idea_usa_wartime_security_authority"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_usa_wartime_security_authority.dds"
	}
	spriteType = {
		name = "GFX_idea_vichy_collaboration_repression"
		texturefile = "gfx/interface/camp_repression/icons/GFX_idea_vichy_collaboration_repression.dds"
	}
```

## Ready-to-paste special-project blocks

Append these blocks inside `interface/special_projects/biowarfare.gfx`'s existing `spriteTypes = { ... }` wrapper.

```plaintext
	spriteType = {
		name = "GFX_sp_japan_cherry_blossom_dossier"
		texturefile = "gfx/interface/camp_repression/icons/GFX_sp_japan_cherry_blossom_dossier.dds"
	}
	spriteType = {
		name = "GFX_sp_japan_epidemic_mapping_bureau"
		texturefile = "gfx/interface/camp_repression/icons/GFX_sp_japan_epidemic_mapping_bureau.dds"
	}
	spriteType = {
		name = "GFX_sp_japan_kwantung_medical_intelligence"
		texturefile = "gfx/interface/camp_repression/icons/GFX_sp_japan_kwantung_medical_intelligence.dds"
	}
	spriteType = {
		name = "GFX_sp_japan_occupation_test_ledger"
		texturefile = "gfx/interface/camp_repression/icons/GFX_sp_japan_occupation_test_ledger.dds"
	}
	spriteType = {
		name = "GFX_sp_japan_pingfang_records_office"
		texturefile = "gfx/interface/camp_repression/icons/GFX_sp_japan_pingfang_records_office.dds"
	}
```

## Ready-to-paste achievement blocks

Append these blocks inside `interface/chaosx_achievements.gfx`'s existing `spriteTypes = { ... }` wrapper.

```plaintext
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_60_inherit_the_ledger_close_the_ledger"
		texturefile = "gfx/achievements/000_chaos_redux_60_inherit_the_ledger_close_the_ledger.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_60_inherit_the_ledger_close_the_ledger_grey"
		texturefile = "gfx/achievements/000_chaos_redux_60_inherit_the_ledger_close_the_ledger_grey.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_60_inherit_the_ledger_close_the_ledger_not_eligible"
		texturefile = "gfx/achievements/000_chaos_redux_60_inherit_the_ledger_close_the_ledger_not_eligible.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_61_papers_for_the_liberated"
		texturefile = "gfx/achievements/000_chaos_redux_61_papers_for_the_liberated.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_61_papers_for_the_liberated_grey"
		texturefile = "gfx/achievements/000_chaos_redux_61_papers_for_the_liberated_grey.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_61_papers_for_the_liberated_not_eligible"
		texturefile = "gfx/achievements/000_chaos_redux_61_papers_for_the_liberated_not_eligible.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_62_the_doctor_loses_his_war"
		texturefile = "gfx/achievements/000_chaos_redux_62_the_doctor_loses_his_war.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_62_the_doctor_loses_his_war_grey"
		texturefile = "gfx/achievements/000_chaos_redux_62_the_doctor_loses_his_war_grey.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_62_the_doctor_loses_his_war_not_eligible"
		texturefile = "gfx/achievements/000_chaos_redux_62_the_doctor_loses_his_war_not_eligible.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_63_no_pingfang_shadow"
		texturefile = "gfx/achievements/000_chaos_redux_63_no_pingfang_shadow.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_63_no_pingfang_shadow_grey"
		texturefile = "gfx/achievements/000_chaos_redux_63_no_pingfang_shadow_grey.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_63_no_pingfang_shadow_not_eligible"
		texturefile = "gfx/achievements/000_chaos_redux_63_no_pingfang_shadow_not_eligible.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_64_grain_before_fear"
		texturefile = "gfx/achievements/000_chaos_redux_64_grain_before_fear.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_64_grain_before_fear_grey"
		texturefile = "gfx/achievements/000_chaos_redux_64_grain_before_fear_grey.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_64_grain_before_fear_not_eligible"
		texturefile = "gfx/achievements/000_chaos_redux_64_grain_before_fear_not_eligible.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_65_dominion_without_chains"
		texturefile = "gfx/achievements/000_chaos_redux_65_dominion_without_chains.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_65_dominion_without_chains_grey"
		texturefile = "gfx/achievements/000_chaos_redux_65_dominion_without_chains_grey.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_65_dominion_without_chains_not_eligible"
		texturefile = "gfx/achievements/000_chaos_redux_65_dominion_without_chains_not_eligible.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_66_redress_before_victory"
		texturefile = "gfx/achievements/000_chaos_redux_66_redress_before_victory.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_66_redress_before_victory_grey"
		texturefile = "gfx/achievements/000_chaos_redux_66_redress_before_victory_grey.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_66_redress_before_victory_not_eligible"
		texturefile = "gfx/achievements/000_chaos_redux_66_redress_before_victory_not_eligible.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_67_congo_reformed"
		texturefile = "gfx/achievements/000_chaos_redux_67_congo_reformed.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_67_congo_reformed_grey"
		texturefile = "gfx/achievements/000_chaos_redux_67_congo_reformed_grey.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_67_congo_reformed_not_eligible"
		texturefile = "gfx/achievements/000_chaos_redux_67_congo_reformed_not_eligible.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_68_roads_without_camps"
		texturefile = "gfx/achievements/000_chaos_redux_68_roads_without_camps.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_68_roads_without_camps_grey"
		texturefile = "gfx/achievements/000_chaos_redux_68_roads_without_camps_grey.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_68_roads_without_camps_not_eligible"
		texturefile = "gfx/achievements/000_chaos_redux_68_roads_without_camps_not_eligible.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_69_gurs_closed"
		texturefile = "gfx/achievements/000_chaos_redux_69_gurs_closed.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_69_gurs_closed_grey"
		texturefile = "gfx/achievements/000_chaos_redux_69_gurs_closed_grey.dds"
	}
	spriteType = {
		name = "GFX_achievement_000_chaos_redux_69_gurs_closed_not_eligible"
		texturefile = "gfx/achievements/000_chaos_redux_69_gurs_closed_not_eligible.dds"
	}
```

## Package and review references

- Asset manifest: `docs/assets/system_camp_repression_rework/manifest_icons.md`
- Decision contact sheet: `docs/assets/system_camp_repression_rework/icons/contact_sheets/decision_icons_contact_sheet.png`
- Idea contact sheet: `docs/assets/system_camp_repression_rework/icons/contact_sheets/idea_icons_contact_sheet.png`
- Special-project contact sheet: `docs/assets/system_camp_repression_rework/icons/contact_sheets/special_project_icons_contact_sheet.png`
- Achievement contact sheet: `docs/assets/system_camp_repression_rework/icons/contact_sheets/achievement_triplets_contact_sheet.png`
