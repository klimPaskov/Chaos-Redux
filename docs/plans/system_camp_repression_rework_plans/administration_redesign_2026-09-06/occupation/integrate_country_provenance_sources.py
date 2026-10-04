# Spent one-shot generator. Its output is committed in common/ (camp tranche commit 72aa7ba5)
# and later hand edits supersede it, so rerunning it would duplicate or revert committed source.
raise SystemExit('Spent one-shot camp generator: output already committed in common/; do not rerun.')
from pathlib import Path
p=Path('common/scripted_effects/camp_administration_country_effects.txt');s=p.read_text()
def transform(name,func):
 global s
 a=s.index(name+' = {');z=s.index('{',a)+1;d=1
 while d:d+=(s[z]=='{')-(s[z]=='}');z+=1
 s=s[:a]+func(s[a:z])+s[z:]
def start(v):
 v=v.replace('camp_admin_site_is_operational = yes\n\t\t\t\tcheck_variable = { camp_admin_detainees_k > 0 }','camp_admin_country_program_site_ready = yes',1)
 v=v.replace('camp_admin_site_is_operational = yes\n\t\t\t\t\tcamp_admin_country_china_geography = yes\n\t\t\t\t\tcheck_variable = { camp_admin_detainees_k > 0 }','camp_admin_country_program_site_ready = yes\n\t\t\t\t\tcamp_admin_country_china_geography = yes',1)
 v=v.replace('limit = { has_variable = camp_admin_institution_state_id }','limit = { has_variable = camp_admin_institution_state_id var:camp_admin_institution_state_id = { camp_admin_country_program_site_ready = yes } }',1)
 v=v.replace('else = { set_variable = { camp_admin_country_program = constant:camp_admin_country_program.none } }','else = { set_variable = { camp_admin_country_program = constant:camp_admin_country_program.none } clear_variable = camp_admin_institution_state_id }',1)
 a=v.index('\n')+1;z=v.rfind('}');content=v[a:z]
 return v[:a]+'\tif = {\n\t\tlimit = { NOT = { has_country_flag = camp_admin_institution_slot_active } NOT = { has_country_flag = camp_admin_country_engineer_release_pending } }\n'+''.join('\t'+x+'\n' for x in content.splitlines())+'\t}\n\tset_temp_variable = { camp_admin_start_program_input = constant:camp_admin_value.zero }\n}'+v[z+1:]
transform('camp_admin_country_start_program',start)
programs=['ger_inspectorate','ger_wvha','ger_auschwitz','jap_transport','jap_army_review','jap_pingfang','sov_design_bureaux','sov_wartime_industry']
for prog in programs:
 def award(v,prog=prog):
  marker='\t\t\tcamp_admin_country_program_still_valid = yes'
  assert marker in v
  v=v.replace(marker,'\t\t\tcheck_variable = { camp_admin_country_program = constant:camp_admin_country_program.'+prog+' }\n\t\t\tcamp_admin_country_program_completion_ready = yes',1)
  # The old repeated engineer branch was unreachable for this exact programme.
  a=v.index('\t\t\tif = {\n\t\t\t\tlimit = { check_variable = { camp_admin_country_program = constant:camp_admin_country_program.sov_engineer_release } }')
  b=v.index('\t\t\tset_variable = { camp_admin_country_last_program',a)
  return v[:a]+v[b:]
 transform('camp_admin_country_award_program_'+prog,award)
# Intentional country reform cancels pending grant state but keeps actual release history.
transform('camp_admin_country_reform',lambda v:v.replace('\t\tcamp_admin_country_halt = yes','\t\tcamp_admin_country_halt = yes\n\t\tcamp_admin_country_clear_engineer_pending_receipt = yes',1))
with p.open('w',encoding='utf-8',newline='') as f:f.write(s)
