# Spent one-shot generator. Its output is committed in common/ (camp tranche commit 72aa7ba5)
# and later hand edits supersede it, so rerunning it would duplicate or revert committed source.
raise SystemExit('Spent one-shot camp generator: output already committed in common/; do not rerun.')
from pathlib import Path
p=Path('common/scripted_effects/camp_administration_occupation_effects.txt')
s=p.read_text()
def body(name):
 start=s.index(name+' = {'); pos=s.index('{',start)+1; depth=1
 while depth:
  depth+=(s[pos]=='{')-(s[pos]=='}'); pos+=1
 return start,pos,s[start:pos]
def update(name,fn):
 global s
 a,b,v=body(name); s=s[:a]+fn(v)+s[b:]
def once(v,old,new):
 if v.count(old)!=1: raise AssertionError((old,v.count(old)))
 return v.replace(old,new,1)
def generic(v):
 v=once(v,'\tif = {\n\t\tlimit = {\n\t\t\tcheck_variable = { camp_occ_transfer_route_proven', '\tcamp_occ_reconcile_external_population = yes\n\tif = { limit = { has_event_target = camp_occ_transfer_destination } event_target:camp_occ_transfer_destination = { camp_origin_reconcile_host_membership = yes } }\n\tif = {\n\t\tlimit = {\n\t\t\tcamp_origin_host_provenance_ready = yes\n\t\t\tcheck_variable = { camp_occ_transfer_route_proven')
 v=once(v,'\t\t\t\t\t\tis_controlled_by = var:camp_occ_transfer_authority','\t\t\t\t\t\tcamp_origin_host_provenance_ready = yes\n\t\t\t\t\t\tis_controlled_by = var:camp_occ_transfer_authority')
 v=once(v,'\t\t\t\tset_temp_variable = { camp_occ_transfer_preflight_valid = constant:camp_occ_value.transfer_valid }','''				set_temp_variable = { camp_occ_transfer_preflight_valid = constant:camp_occ_value.transfer_valid }
				set_temp_variable = { camp_occ_transfer_open_source_sequence = camp_origin_observation_sequence }
				set_temp_variable = { camp_occ_transfer_open_source_population_k = state_population_k }
				set_temp_variable = { camp_occ_transfer_open_source_deaths_people = chaos_state_civilian_deaths_total }
				event_target:camp_occ_transfer_destination = {
					set_temp_variable = { camp_occ_transfer_open_destination_sequence = camp_origin_observation_sequence }
					set_temp_variable = { camp_occ_transfer_open_destination_population_k = state_population_k }
					set_temp_variable = { camp_occ_transfer_open_destination_deaths_people = chaos_state_civilian_deaths_total }
				}''')
 marker='\t}\n\tset_temp_variable = { camp_occ_transfer_route_proven = 0 }'
 addition='''		if = {
			limit = { has_state_flag = camp_occ_transfer_rollback_failed }
			set_variable = { camp_occ_failed_source_debit_people = camp_occ_transfer_source_debit_people }
			set_variable = { camp_occ_failed_destination_credit_people = camp_occ_transfer_destination_credit_people }
			set_variable = { camp_occ_failed_source_restored_people = camp_occ_transfer_source_restored_people }
			set_variable = { camp_occ_failed_destination_undone_people = camp_occ_transfer_destination_undone_people }
			set_variable = { camp_occ_failed_destination_state = event_target:camp_occ_transfer_destination }
			camp_origin_quarantine_transaction = yes
			event_target:camp_occ_transfer_destination = {
				set_variable = { camp_occ_failed_source_state = camp_occ_transfer_source_state }
				set_variable = { camp_occ_failed_source_debit_people = camp_occ_transfer_source_debit_people }
				set_variable = { camp_occ_failed_destination_credit_people = camp_occ_transfer_destination_credit_people }
				set_variable = { camp_occ_failed_source_restored_people = camp_occ_transfer_source_restored_people }
				set_variable = { camp_occ_failed_destination_undone_people = camp_occ_transfer_destination_undone_people }
				camp_origin_quarantine_transaction = yes
			}
		}
		else = {
			camp_occ_finish_generic_movement_observations = yes
		}
'''
 return once(v,marker,addition+marker)
update('camp_occ_transfer_survivors_exact',generic)
def source_quote(v):
 return once(v,'\t\t\tcheck_variable = { camp_occ_custody_requested_people > 0 }','\t\t\tcamp_origin_host_provenance_ready = yes\n\t\t\tcheck_variable = { camp_occ_custody_requested_people > 0 }')
update('camp_occ_preflight_custody_source',source_quote)
def custody(v):
 v=once(v,'\tif = {\n\t\tlimit = {\n\t\t\tcheck_variable = { camp_occ_custody_route_proven','\tcamp_occ_reconcile_external_population = yes\n\tif = { limit = { has_event_target = camp_occ_custody_destination } event_target:camp_occ_custody_destination = { camp_origin_reconcile_host_membership = yes } }\n\tif = {\n\t\tlimit = {\n\t\t\tcamp_origin_host_provenance_ready = yes\n\t\t\tcheck_variable = { camp_occ_custody_route_proven')
 v=once(v,'\t\t\t\tset_temp_variable = { camp_occ_custody_preflight_valid = constant:camp_occ_value.transfer_valid }','''				set_temp_variable = { camp_occ_custody_preflight_valid = constant:camp_occ_value.transfer_valid }
				set_temp_variable = { camp_occ_custody_current_source_state = THIS }
				set_temp_variable = { camp_occ_custody_open_source_sequence = camp_origin_observation_sequence }
				set_temp_variable = { camp_occ_custody_open_source_population_k = state_population_k }
				set_temp_variable = { camp_occ_custody_open_source_deaths_people = chaos_state_civilian_deaths_total }
				event_target:camp_occ_custody_destination = {
					set_temp_variable = { camp_occ_custody_open_destination_sequence = camp_origin_observation_sequence }
					set_temp_variable = { camp_occ_custody_open_destination_population_k = state_population_k }
					set_temp_variable = { camp_occ_custody_open_destination_deaths_people = chaos_state_civilian_deaths_total }
				}''')
 marker='\t}\n\tset_temp_variable = { camp_occ_custody_route_proven = 0 }'
 addition='''		if = {
			limit = { has_state_flag = camp_occ_custody_rollback_failed }
			set_variable = { camp_occ_custody_failed_source_debit_people = camp_occ_custody_source_debit_people }
			set_variable = { camp_occ_custody_failed_destination_credit_people = camp_occ_custody_destination_credit_people }
			set_variable = { camp_occ_custody_failed_bind_people = camp_occ_custody_bind_people }
			set_variable = { camp_occ_custody_failed_inverse_people = camp_occ_custody_inverse_people }
			set_variable = { camp_occ_custody_failed_source_restored_people = camp_occ_custody_source_restored_people }
			set_variable = { camp_occ_custody_failed_destination_undone_people = camp_occ_custody_destination_undone_people }
			set_variable = { camp_occ_custody_failed_destination_state = event_target:camp_occ_custody_destination }
			camp_origin_quarantine_transaction = yes
			event_target:camp_occ_custody_destination = {
				set_variable = { camp_occ_custody_failed_source_state = camp_occ_custody_current_source_state }
				set_variable = { camp_occ_custody_failed_source_debit_people = camp_occ_custody_source_debit_people }
				set_variable = { camp_occ_custody_failed_destination_credit_people = camp_occ_custody_destination_credit_people }
				set_variable = { camp_occ_custody_failed_bind_people = camp_occ_custody_bind_people }
				set_variable = { camp_occ_custody_failed_inverse_people = camp_occ_custody_inverse_people }
				set_variable = { camp_occ_custody_failed_source_restored_people = camp_occ_custody_source_restored_people }
				set_variable = { camp_occ_custody_failed_destination_undone_people = camp_occ_custody_destination_undone_people }
				camp_origin_quarantine_transaction = yes
			}
		}
		else = {
			camp_occ_finish_custody_movement_observations = yes
		}
'''
 return once(v,marker,addition+marker)
update('camp_occ_transfer_to_custody_exact',custody)
# Validate shape and bounds during post-debit identity recheck without interpreting
# the deliberately in-flight physical change as an outside observation.
def prove(v):
 return once(v,'\t\tlimit = { has_variable = camp_occ_responsible_country check_variable = { camp_occ_active_row_id > 0 } }','\t\tlimit = { has_variable = camp_occ_responsible_country check_variable = { camp_occ_active_row_id > 0 } camp_origin_host_rows_valid = yes }')
update('camp_occ_prove_active_row',prove)
helpers=[]
for family,prefix,target in [('generic','camp_occ_transfer','camp_occ_transfer_destination'),('custody','camp_occ_custody','camp_occ_custody_destination')]:
 source_restored=prefix+'_source_restored_people'
 undone=prefix+'_destination_undone_people'
 helpers.append(f'''# State source after both metadata endpoints committed or the exact inverse completed.
{ 'camp_occ_finish_generic_movement_observations' if family=='generic' else 'camp_occ_finish_custody_movement_observations' } = {{
	set_temp_variable = {{ camp_occ_endpoint_after_source_k = {prefix}_source_debit_people }}
	multiply_temp_variable = {{ camp_occ_endpoint_after_source_k = constant:camp_admin_value.negative_one }}
	add_to_temp_variable = {{ camp_occ_endpoint_after_source_k = {source_restored} }}
	divide_temp_variable = {{ camp_occ_endpoint_after_source_k = constant:camp_occ_value.people_per_k }}
	add_to_temp_variable = {{ camp_occ_endpoint_after_source_k = {prefix}_open_source_population_k }}
	set_temp_variable = {{ camp_occ_endpoint_after_destination_k = {prefix}_destination_credit_people }}
	subtract_from_temp_variable = {{ camp_occ_endpoint_after_destination_k = {undone} }}
	divide_temp_variable = {{ camp_occ_endpoint_after_destination_k = constant:camp_occ_value.people_per_k }}
	add_to_temp_variable = {{ camp_occ_endpoint_after_destination_k = {prefix}_open_destination_population_k }}
	set_temp_variable = {{ camp_origin_known_observation_sequence = {prefix}_open_source_sequence }}
	set_temp_variable = {{ camp_origin_known_before_population_k = {prefix}_open_source_population_k }}
	set_temp_variable = {{ camp_origin_known_before_state_deaths_people = {prefix}_open_source_deaths_people }}
	set_temp_variable = {{ camp_origin_known_after_population_k = camp_occ_endpoint_after_source_k }}
	set_temp_variable = {{ camp_origin_known_after_state_deaths_people = {prefix}_open_source_deaths_people }}
	camp_origin_commit_endpoint_observation = yes
	event_target:{target} = {{
		set_temp_variable = {{ camp_origin_known_observation_sequence = {prefix}_open_destination_sequence }}
		set_temp_variable = {{ camp_origin_known_before_population_k = {prefix}_open_destination_population_k }}
		set_temp_variable = {{ camp_origin_known_before_state_deaths_people = {prefix}_open_destination_deaths_people }}
		set_temp_variable = {{ camp_origin_known_after_population_k = camp_occ_endpoint_after_destination_k }}
		set_temp_variable = {{ camp_origin_known_after_state_deaths_people = {prefix}_open_destination_deaths_people }}
		camp_origin_commit_endpoint_observation = yes
	}}
}}
''')
s+='\n'+'\n'.join(helpers)
with p.open('w',encoding='utf-8',newline='') as stream: stream.write(s)
