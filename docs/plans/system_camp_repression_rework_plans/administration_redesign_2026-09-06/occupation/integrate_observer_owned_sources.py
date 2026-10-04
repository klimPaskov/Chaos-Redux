# Spent one-shot generator. Its output is committed in common/ (camp tranche commit 72aa7ba5)
# and later hand edits supersede it, so rerunning it would duplicate or revert committed source.
raise SystemExit('Spent one-shot camp generator: output already committed in common/; do not rerun.')
from pathlib import Path
root=Path.cwd()
admin_path=root/'common/scripted_effects/camp_administration_effects.txt'
occ_path=root/'common/scripted_effects/camp_administration_occupation_effects.txt'
def replace_block(source,name,replacement):
    start=source.index(name+' = {')
    begin=source.index('{',start); depth=1; pos=begin+1
    while depth:
        depth += (source[pos]=='{')-(source[pos]=='}'); pos+=1
    return source[:start]+replacement.rstrip()+source[pos:]
admin=admin_path.read_text(encoding='utf-8-sig')
admin=replace_block(admin,'camp_admin_consume_outside_rows', '''camp_admin_consume_outside_rows = {
	set_temp_variable = { camp_admin_outside_actual_k = constant:camp_admin_value.zero }
	set_temp_variable = { camp_origin_single_reconciliation_accepted = constant:camp_admin_value.zero }
	if = {
		limit = {
			has_state_flag = camp_origin_single_origin_reconciliation_pending
			NOT = { has_state_flag = camp_origin_ambiguous }
			check_variable = { camp_origin_pending_single_family = constant:camp_origin_family.custody }
			camp_origin_host_rows_valid = yes
		}
		set_temp_variable = { camp_admin_selected_row_id = camp_origin_pending_single_row_id }
		set_temp_variable = { camp_admin_row_consume_kind = @CAMP_ADMIN_ROW_OUTSIDE }
		set_temp_variable = { camp_admin_row_consume_amount_k = camp_origin_pending_single_removal_k }
		camp_admin_consume_rows = yes
		set_temp_variable = { camp_admin_outside_actual_k = camp_admin_row_consumed_k }
		subtract_from_variable = { camp_admin_detainees_k = camp_admin_outside_actual_k }
		add_to_variable = { camp_admin_external_attrition_k = camp_admin_outside_actual_k }
		set_temp_variable = { camp_origin_single_reconcile_contract = constant:camp_admin_value.one }
		set_temp_variable = { camp_origin_single_reconcile_sequence = camp_origin_observation_sequence }
		set_temp_variable = { camp_origin_single_reconcile_amount_k = camp_admin_outside_actual_k }
		camp_origin_acknowledge_single_origin_reconciliation = yes
	}
	set_temp_variable = { camp_admin_selected_row_id = constant:camp_admin_value.zero }
	set_temp_variable = { camp_admin_row_consume_amount_k = constant:camp_admin_value.zero }
}''')
# The common observer/owner receipt replaces headroom-only guessing.
start=admin.index('\t# External population loss cannot leave a cohort larger than its host population.')
end=admin.index('\tclamp_variable = { var = camp_admin_capacity_k',start)
admin=admin[:start]+admin[end:]
admin=admin.replace('\tcamp_admin_initialize_rows = yes\n\tcamp_admin_check_rows = yes\n\tset_temp_variable = { camp_admin_selected_row_id = 0 }\n\tif = { limit = { check_variable = { camp_admin_rows_valid = constant:camp_admin_value.one } } camp_admin_count_live_rows = yes }', '\tcamp_admin_initialize_rows = yes\n\tcamp_origin_reconcile_host_membership = yes\n\tcamp_admin_check_rows = yes\n\tset_temp_variable = { camp_admin_selected_row_id = 0 }\n\tif = { limit = { check_variable = { camp_admin_rows_valid = constant:camp_admin_value.one } } camp_admin_count_live_rows = yes }',1)
admin=admin.replace('\tcamp_admin_initialize_records = yes\n\tcamp_admin_refresh_capacity = yes','\tcamp_admin_initialize_records = yes\n\tcamp_origin_initialize_host = yes\n\tcamp_admin_refresh_capacity = yes',1)
occ=occ_path.read_text(encoding='utf-8-sig')
occ=replace_block(occ,'camp_occ_reconcile_external_population', '''camp_occ_reconcile_external_population = {
	if = { limit = { has_variable = camp_occ_responsible_country } var:camp_occ_responsible_country = { camp_occ_initialize_rows = yes } }
	camp_origin_reconcile_host_membership = yes
	set_temp_variable = { camp_occ_external_removed_k = camp_origin_reconciled_occupation_k }
	# Compatibility mirrors only. The common host baseline owns observation.
	set_variable = { camp_occ_observed_population_k = camp_origin_observed_population_k }
	set_variable = { camp_occ_observed_state_deaths = camp_origin_observed_state_deaths_people }
}''')
occ=replace_block(occ,'camp_occ_distribute_external_removal', '''camp_occ_distribute_external_removal = {
	camp_origin_reconcile_host_membership = yes
	set_temp_variable = { camp_occ_external_removed_k = camp_origin_reconciled_occupation_k }
}''')
occ=replace_block(occ,'camp_occ_distribute_unknown_origin_removal','')
occ=replace_block(occ,'camp_occ_distribute_known_origin_removal', '''camp_occ_distribute_known_origin_removal = {
	set_temp_variable = { camp_occ_known_outside_actual_k = constant:camp_admin_value.zero }
	set_temp_variable = { camp_origin_single_reconciliation_accepted = constant:camp_admin_value.zero }
	if = {
		limit = {
			has_state_flag = camp_origin_single_origin_reconciliation_pending
			NOT = { has_state_flag = camp_origin_ambiguous }
			check_variable = { camp_origin_pending_single_family = constant:camp_origin_family.occupation }
			camp_origin_host_rows_valid = yes
		}
		set_temp_variable = { camp_occ_known_outside_index = camp_origin_pending_single_row_id }
		subtract_from_temp_variable = { camp_occ_known_outside_index = constant:camp_occ_value.row_first_id }
		set_temp_variable = { camp_occ_known_outside_actual_k = camp_origin_pending_single_removal_k }
		var:camp_occ_responsible_country = {
			set_temp_variable = { camp_occ_row_after_k = camp_occ_row_amounts_k^camp_occ_known_outside_index }
			subtract_from_temp_variable = { camp_occ_row_after_k = camp_occ_known_outside_actual_k }
			set_variable = { camp_occ_row_amounts_k^camp_occ_known_outside_index = camp_occ_row_after_k }
			set_temp_variable = { camp_occ_row_removed_after_k = camp_occ_row_removed_k^camp_occ_known_outside_index }
			add_to_temp_variable = { camp_occ_row_removed_after_k = camp_occ_known_outside_actual_k }
			set_variable = { camp_occ_row_removed_k^camp_occ_known_outside_index = camp_occ_row_removed_after_k }
			add_to_variable = { camp_occ_total_exposure_removed_k = camp_occ_known_outside_actual_k }
			add_to_variable = { camp_occ_month_exposure_removed_k = camp_occ_known_outside_actual_k }
		}
		subtract_from_variable = { camp_occ_remaining_k = camp_occ_known_outside_actual_k }
		add_to_variable = { camp_occ_total_exposure_removed_k = camp_occ_known_outside_actual_k }
		add_to_variable = { camp_occ_month_exposure_removed_k = camp_occ_known_outside_actual_k }
		set_temp_variable = { camp_origin_single_reconcile_contract = constant:camp_admin_value.one }
		set_temp_variable = { camp_origin_single_reconcile_sequence = camp_origin_observation_sequence }
		set_temp_variable = { camp_origin_single_reconcile_amount_k = camp_occ_known_outside_actual_k }
		camp_origin_acknowledge_single_origin_reconciliation = yes
	}
}''')
# Admission observation occurs before setting a first occupation host reservation.
occ=occ.replace('camp_occ_register_cohort = {\n\tset_temp_variable = { camp_occ_admitted_k = 0 }','camp_occ_register_cohort = {\n\tset_temp_variable = { camp_occ_admitted_k = 0 }\n\tcamp_origin_reconcile_host_membership = yes',1)
occ=occ.replace('\t\t\tcheck_variable = { camp_occ_source_proven = 1 }','\t\t\tcamp_origin_host_provenance_ready = yes\n\t\t\tcheck_variable = { camp_occ_source_proven = 1 }',1)
# Successful enrollment is ledger-only and preserves the already-established opening.
needle='\t\t\tset_variable = { camp_occ_native_row_id = camp_occ_appended_row_id }'
occ=occ.replace(needle,needle+'\n\t\t\tcamp_origin_observe_host = yes',1)
with admin_path.open('w',encoding='utf-8',newline='') as stream: stream.write(admin)
with occ_path.open('w',encoding='utf-8',newline='') as stream: stream.write(occ)

