# Spent one-shot generator. Its output is committed in common/ (camp tranche commit 72aa7ba5)
# and later hand edits supersede it, so rerunning it would duplicate or revert committed source.
raise SystemExit('Spent one-shot camp generator: output already committed in common/; do not rerun.')
from pathlib import Path
def replace(source,name,repl):
 a=source.index(name+' = {'); z=source.index('{',a)+1; depth=1
 while depth: depth+=(source[z]=='{')-(source[z]=='}'); z+=1
 return source[:a]+repl.strip()+source[z:]
p=Path('common/scripted_effects/camp_administration_effects.txt'); s=p.read_text(); s=s.replace('\t\t\tcamp_origin_observe_host = yes\n\t\t\tcamp_origin_observe_host = yes','\t\t\tcamp_origin_observe_host = yes')
s=replace(s,'camp_admin_close_site','''camp_admin_close_site = {
	if = {
		limit = { has_state_flag = camp_admin_initialized }
		camp_origin_reconcile_host_membership = yes
		if = {
			limit = { camp_admin_site_rows_reconciled = yes }
			camp_admin_release_survivors = yes
			set_state_flag = camp_admin_closed
		}
		else_if = {
			limit = { OR = { has_state_flag = camp_origin_ambiguous has_state_flag = camp_origin_single_origin_reconciliation_pending has_state_flag = camp_origin_records_unresolved } }
			# Terminal administration stops without fabricating survivor releases.
			set_state_flag = camp_admin_closed
			set_state_flag = camp_origin_ambiguity_terminal
		}
		if = {
			limit = { has_state_flag = camp_admin_closed }
			set_variable = { camp_admin_support_ratio = 0 }
			camp_admin_clear_state_output = yes
			if = {
				limit = { has_variable = camp_admin_responsible_country }
				set_temp_variable = { camp_admin_closing_state_id = THIS.id }
				var:camp_admin_responsible_country = {
					if = { limit = { check_variable = { camp_admin_economy_state_id = camp_admin_closing_state_id } } camp_admin_cancel_economy_project = yes }
					if = {
						limit = { check_variable = { camp_admin_institution_state_id = camp_admin_closing_state_id } }
						clr_country_flag = camp_admin_institution_slot_active
						set_variable = { camp_admin_institution_progress = 0 }
						clear_variable = camp_admin_institution_state_id
					}
					camp_admin_refresh_country_economy = yes
				}
			}
		}
	}
}''')
with p.open('w',encoding='utf-8',newline='') as f:f.write(s)
p=Path('common/scripted_effects/camp_administration_occupation_effects.txt'); s=p.read_text()
s=replace(s,'camp_occ_close_state','''camp_occ_close_state = {
	camp_occ_backfill_cohort_origin = yes
	if = {
		limit = { has_state_flag = camp_occ_registered NOT = { has_state_flag = camp_occ_closed } }
		camp_occ_reconcile_external_population = yes
		if = {
			limit = { camp_origin_host_provenance_ready = yes }
			set_temp_variable = { camp_occ_release_k = camp_occ_remaining_k }
			camp_occ_release_rows_at_host = yes
			add_to_variable = { camp_occ_total_released_k = camp_occ_release_k }
			var:camp_occ_responsible_country = { add_to_variable = { camp_occ_total_released_k = camp_occ_release_k } }
			set_variable = { camp_occ_remaining_k = 0 }
			camp_origin_observe_host = yes
		}
		else = { set_state_flag = camp_origin_ambiguity_terminal }
		set_state_flag = camp_occ_closed
	}
}''')
# A direct release adapter cannot bypass the host provenance guard.
a=s.index('camp_occ_release_rows_at_host = {'); z=s.index('\ncamp_occ_close_country',a)
v=s[a:z]; start=v.index('\n')+1; end=v.rfind('}')
content=v[start:end]; v=v[:start]+'\tif = {\n\t\tlimit = { camp_origin_host_provenance_ready = yes }\n'+''.join('\t'+line+'\n' for line in content.splitlines())+'\t}\n}'+v[end+1:]; s=s[:a]+v+s[z:]
s=s.replace('limit = { NOT = { check_variable = { camp_occ_last_month = camp_admin_month_key } } }','limit = { NOT = { has_country_flag = camp_occ_country_closed } NOT = { check_variable = { camp_occ_last_month = camp_admin_month_key } } }',1)
with p.open('w',encoding='utf-8',newline='') as f:f.write(s)
