# Spent one-shot generator. Its output is committed in common/ (camp tranche commit 72aa7ba5)
# and later hand edits supersede it, so rerunning it would duplicate or revert committed source.
raise SystemExit('Spent one-shot camp generator: output already committed in common/; do not rerun.')
from pathlib import Path
p=Path('common/scripted_effects/camp_administration_country_effects.txt');s=p.read_text()
def put(name,text):
 global s
 a=s.index(name+' = {');z=s.index('{',a)+1;d=1
 while d:d+=(s[z]=='{')-(s[z]=='}');z+=1
 s=s[:a]+text+s[z:]
put('camp_admin_country_award_program_sov_engineer_release','''camp_admin_country_award_program_sov_engineer_release = {
	if = {
		limit = {
			check_variable = { camp_admin_country_program = constant:camp_admin_country_program.sov_engineer_release }
			NOT = { has_country_flag = camp_admin_done_sov_engineer_release }
			camp_admin_country_program_completion_ready = yes
		}
		if = {
			limit = { NOT = { has_country_flag = camp_admin_country_engineer_release_pending } }
			set_temp_variable = { camp_admin_release_requested_k = camp_admin_country_engineer_cohort_k }
			var:camp_admin_institution_state_id = { camp_admin_release_detainees = yes }
			if = {
				limit = { check_variable = { camp_admin_release_actual_k > constant:camp_admin_value.zero } }
				set_country_flag = camp_admin_country_engineer_release_pending
				set_variable = { camp_admin_country_engineer_receipt_k = camp_admin_release_actual_k }
				set_variable = { camp_admin_country_engineer_receipt_state_id = camp_admin_institution_state_id }
				set_variable = { camp_admin_country_engineer_receipt_authority = THIS }
				set_variable = { camp_admin_country_engineer_receipt_program = camp_admin_country_program }
				set_variable = { camp_admin_country_engineer_receipt_progress = camp_admin_institution_progress }
				set_variable = { camp_admin_country_engineer_receipt_target = camp_admin_institution_target }
				set_variable = { camp_admin_country_last_engineers_released_k = camp_admin_release_actual_k }
			}
		}
		# Revalidate the same completed programme/site/authority after the measured
		# release. A zero-held site can use only its own matching positive receipt.
		if = {
			limit = { camp_admin_country_engineer_receipt_identity_valid = yes camp_admin_country_program_completion_ready = yes }
			set_temp_variable = { camp_admin_research_requested_bonus = constant:camp_admin_country.bonus_standard }
			set_temp_variable = { camp_admin_research_contract = constant:camp_admin_value.one }
			set_temp_variable = { camp_admin_research_program_valid = constant:camp_admin_value.one }
			camp_admin_try_claim_research_award = yes
			if = {
				limit = { check_variable = { camp_admin_research_award_accepted = constant:camp_admin_value.one } }
				meta_effect = {
					text = { add_tech_bonus = { name = camp_admin_bonus_sov_engineer_release bonus = [BONUS_VALUE] uses = 1 category = engineers_tech } }
					BONUS_VALUE = "[?camp_admin_research_award_bonus]"
				}
				set_country_flag = camp_admin_done_sov_engineer_release
				set_country_flag = camp_admin_country_engineers_released
				clear_variable = camp_admin_country_engineer_cohort_k
				camp_admin_country_clear_engineer_pending_receipt = yes
				set_variable = { camp_admin_country_last_program = camp_admin_country_program }
				set_variable = { camp_admin_country_program = constant:camp_admin_country_program.none }
				clear_variable = camp_admin_institution_state_id
				clr_country_flag = camp_admin_country_institution_paused
			}
		}
	}
}''')
# Pending release has already completed funded work, so final-grant deferral is
# resolved without paying or releasing the same cohort again.
a=s.index('camp_admin_country_tick_institution = {');z=s.index('\n# Economic ministries',a);v=s[a:z];body_start=v.index('\n\tif = {');body_end=v.rfind('}');original=v[body_start:body_end];replacement='''
	if = {
		limit = { has_country_flag = camp_admin_country_engineer_release_pending }
		if = { limit = { camp_admin_country_program_completion_ready = yes } camp_admin_country_finish_program = yes }
	}
	else = {
'''+''.join('\t'+line+'\n' for line in original.strip('\n').splitlines())+'\t}\n';v=v[:body_start]+replacement+v[body_end:];s=s[:a]+v+s[z:]
# Observe the selected existing host before any payment/grant. A national halt
# deliberately remains independent of this survivor proof.
s=s.replace('camp_admin_country_tick_institution = {\n\tset_country_flag', 'camp_admin_country_tick_institution = {\n\tif = { limit = { has_variable = camp_admin_institution_state_id } var:camp_admin_institution_state_id = { camp_admin_refresh_capacity = yes } }\n\tset_country_flag',1)
s=s.replace('camp_admin_country_finish_program = {\n\tif =', 'camp_admin_country_finish_program = {\n\tif = { limit = { has_variable = camp_admin_institution_state_id } var:camp_admin_institution_state_id = { camp_admin_refresh_capacity = yes } }\n\tif =',1)
with p.open('w',encoding='utf-8',newline='') as f:f.write(s)
