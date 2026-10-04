"""Historical first-pass hunk writer, retained as task evidence.
The final owned_source.patch also includes reviewed direct follow-up hunks for
opening last-state provenance and preserved rapid/managed/mobile bonus order.
Use the final patch/manifest as implementation evidence, not this intermediate
writer as a replay tool. Its before-byte guard rejects the current workspace.
"""
from pathlib import Path
import re,json,hashlib,sys,difflib
ROOT=Path.cwd()
EV=ROOT/'docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-04_larder_logistics_implementation/evidence'
EV.mkdir(parents=True,exist_ok=True)
FILES=['common/scripted_effects/014_cannibalism_effects.txt','common/script_constants/014_cannibalism_constants.txt','common/scripted_triggers/014_cannibalism_triggers.txt','localisation/english/014_cannibalism_l_english.yml','common/scripted_effects/chaosx_dynamic_effects.md']
before={}
for n in FILES:
 p=ROOT/n;b=EV/'before'/n
 if not b.exists():b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
 before[n]=b.read_bytes()
 assert p.read_bytes()==before[n],('Concurrent source change',n)
def get(t,n):
 m=re.search(r'(?ms)^'+re.escape(n)+r' = \{.*?^\}',t);assert m,n
 return m.group(),m.start(),m.end()
def repl(t,o,n,count=1):
 p=r'\r?\n'.join(re.escape(x) for x in o.split('\n'));ms=list(re.finditer(p,t))
 assert len(ms)==count,(o[:120],len(ms),count)
 for m in reversed(ms):t=t[:m.start()]+n.replace('\n','\r\n' if '\r\n' in m.group() else '\n')+t[m.end():]
 return t
def edit(t,n,f):
 b,a,z=get(t,n);return t[:a]+f(b)+t[z:]
def entry(b,s):
 i=b.index('\n')+1;return b[:i]+s.replace('\n','\r\n')+b[i:]
def indent(t):return ''.join(('\t'+x if x.strip() else x) for x in t.splitlines(keepends=True))
p=(ROOT/'docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_larder_logistics_owner_plan_evidence/2026-10-04_accepted_code_proposal.md').read_text(encoding='utf-8')
fence=chr(96)*3
constants,capacity,unused,quote=re.findall(fence+r'txt\n(.*?)\n'+fence,p,re.S)[:4]
E=before[FILES[0]].decode('utf-8')
quote=quote.replace('\t\tlimit = {\n\t\t\thas_event_target','\t\tlimit = {\n\t\t\tcannibalism_larder_transfer_context_is_valid = yes\n\t\t\thas_event_target',1)
quote=quote.replace('\n\tset_temp_variable = { cannibalism_transfer_route_fraction = constant:','\n\tset_temp_variable = { cannibalism_transfer_constructor_context = constant:cannibalism_larder_logistics.zero }\n\tset_temp_variable = { cannibalism_transfer_route_fraction = constant:',1)
helpers='''# ============================================================================ 
# Event014 Larder logistics. Contract: docs/events/014_cannibalism/larder_logistics.md
# Consuming owners allocate quote, proof and commit outputs before nested scopes.
# No population, equipment, AI, on-action or GUI data mutations occur here.
# ============================================================================ 

'''
helpers+=capacity+'\n\n'+'''# Donor country. Caller owns the native capture proofs and source generation.
# The transaction owner binds the explicit destination country.
cannibalism_capture_current_larder_transfer_capitals = {
	save_event_target_as = cannibalism_larder_source_country
	set_temp_variable = { cannibalism_transfer_source_generation = cannibalism_actor_generation }
	capital_scope = {
		save_event_target_as = cannibalism_larder_source_capital
		set_temp_variable = { cannibalism_larder_source_capital_captured = constant:cannibalism_larder_logistics.one }
	}
	event_target:cannibalism_larder_destination_country = {
		if = {
			limit = { exists = yes NOT = { has_capitulated = yes } }
			capital_scope = {
				save_event_target_as = cannibalism_larder_destination_capital
				set_temp_variable = { cannibalism_larder_destination_capital_captured = constant:cannibalism_larder_logistics.one }
			}
		}
	}
}

# Country. Finalize only at a completed store/territory boundary.
# Only the current generation-validated host publishes the shared mirror.
cannibalism_clamp_and_publish_current_larder = {
	cannibalism_refresh_larder_effective_capacity = yes
	clamp_variable = { var = cannibalism_larder min = constant:cannibalism_consumption.larder_min max = cannibalism_larder_effective_capacity }
	if = {
		limit = {
			cannibalism_has_valid_unification_destination = yes
			tag = event_target:cannibalism_unification_host
		}
		set_variable = { global.cannibalism_global_larder = cannibalism_larder }
	}
}

# Recipient. One opening assignment after successful runtime migration.
# The owner replaces the snapshot store by its distance-adjusted received quote.
# The post-annex or explicit nonabsorbing human branch owns the clamp.
cannibalism_apply_initial_larder_inheritance = {
	set_variable = { cannibalism_larder = cannibalism_inherited_larder }
	add_to_variable = { cannibalism_larder = constant:cannibalism_unification.starting_global_larder }
	if = {
		limit = { check_variable = { cannibalism_inherited_larder_route = constant:cannibalism_larder_route.managed_herds } }
		add_to_variable = { cannibalism_larder = constant:cannibalism_unification.inherited_managed_larder }
	}
	else_if = {
		limit = { check_variable = { cannibalism_inherited_larder_route = constant:cannibalism_larder_route.mobile_larder } }
		add_to_variable = { cannibalism_larder = constant:cannibalism_unification.inherited_mobile_larder }
	}
}

# Donor. Quote only. Missing context/capture or unwritten distance fails closed.
'''+quote+'\n\n'
anchor='# Country donor snapshot. Inputs: current donor variables and three origin flags.'
assert E.count(anchor)==1;E=E.replace(anchor,helpers.replace('\n','\r\n')+anchor)
commit='''cannibalism_add_current_warlord_larder_to_unified_host = {
	set_temp_variable = { cannibalism_transfer_committed = constant:cannibalism_larder_logistics.zero }
	if = {
		limit = {
			check_variable = { var = cannibalism_transfer_result value = constant:cannibalism_larder_logistics.one compare = equals }
			cannibalism_larder_transfer_context_is_valid = yes
		}
		# Consume success before either mutation to prevent a repeated debit.
		set_temp_variable = { cannibalism_transfer_result = constant:cannibalism_larder_logistics.zero }
		subtract_from_variable = { cannibalism_larder = cannibalism_transfer_dispatch }
		clamp_variable = { var = cannibalism_larder min = constant:cannibalism_consumption.larder_min max = constant:cannibalism_consumption.larder_max }
		event_target:cannibalism_larder_destination_country = {
			add_to_variable = { cannibalism_larder = cannibalism_transfer_received }
		}
		set_temp_variable = { cannibalism_transfer_committed = constant:cannibalism_larder_logistics.one }
	}
}'''
E=edit(E,'cannibalism_add_current_warlord_larder_to_unified_host',lambda _:commit.replace('\n','\r\n'))
def identity(b):
 for o in ['\tset_variable = { cannibalism_larder = cannibalism_inherited_larder }\n','\tadd_to_variable = { cannibalism_larder = constant:cannibalism_unification.starting_global_larder }\n','\t\tadd_to_variable = { cannibalism_larder = constant:cannibalism_unification.inherited_managed_larder }\n','\t\tadd_to_variable = { cannibalism_larder = constant:cannibalism_unification.inherited_mobile_larder }\n']:b=repl(b,o,'')
 return repl(b,'\tclamp_variable = { var = cannibalism_larder min = constant:cannibalism_consumption.larder_min max = constant:cannibalism_unification.global_larder_maximum }\n\tset_variable = { global.cannibalism_global_larder = cannibalism_larder }\n','',2)
E=edit(E,'cannibalism_apply_inherited_host_identity_to_cbl',identity)
slots=['cannibalism_larder_source_capital_captured','cannibalism_larder_destination_capital_captured','cannibalism_transfer_source_generation','cannibalism_transfer_dispatch','cannibalism_transfer_received','cannibalism_transfer_loss_fraction','cannibalism_transfer_retention','cannibalism_transfer_result','cannibalism_transfer_committed','cannibalism_transfer_route_fraction','cannibalism_transfer_constructor_context']
alloc='\t# Own Larder outputs before helpers and country scopes.\n'+''.join('\tset_temp_variable = { '+v+' = constant:cannibalism_larder_logistics.zero }\n' for v in slots)+'\tset_temp_variable = { cannibalism_transfer_distance = constant:cannibalism_larder_logistics.minus_one }\n'
def absorption(b):
 b=entry(b,alloc)
 q='''		event_target:cannibalism_unification_host = { save_event_target_as = cannibalism_larder_destination_country }
		cannibalism_capture_current_larder_transfer_capitals = yes
		set_temp_variable = { cannibalism_transfer_route_fraction = cannibalism_integration_larder_factor }
		cannibalism_prepare_larder_transfer_quote = yes
'''
 b=repl(b,'\t\tcannibalism_capture_current_warlord_inheritance = yes\n','\t\tcannibalism_capture_current_warlord_inheritance = yes\n'+q)
 a=b.index('\t\tevent_target:cannibalism_unification_host = {\r\n\t\t\tsave_event_target_as = cannibalism_runtime_migration_destination_country')
 z=b.rfind('\t}\r\n}')
 b=b[:a]+'\t\tif = {\r\n\t\t\tlimit = { check_variable = { cannibalism_transfer_result > constant:cannibalism_larder_logistics.zero } }\r\n'+indent(b[a:z])+'\t\t}\r\n'+b[z:]
 o='\t\t\t\tcannibalism_add_current_warlord_larder_to_unified_host = yes\r\n';a=b.index(o)+len(o);z=b.rfind('\t\t\t}\r\n\t\t}\r\n\t}\r\n}')
 b=b[:a]+'\t\t\t\tif = {\r\n\t\t\t\t\tlimit = { check_variable = { cannibalism_transfer_committed > constant:cannibalism_larder_logistics.zero } }\r\n'+indent(b[a:z])+'\t\t\t\t}\r\n'+b[z:]
 return repl(b,'transfer_troops = yes\n\t\t\t\t\t\t}\n','transfer_troops = yes\n\t\t\t\t\t\t}\n\t\t\t\t\t\tcannibalism_clamp_and_publish_current_larder = yes\n')
E=edit(E,'cannibalism_absorb_current_warlord_into_unified_host',absorption)
def autonomy(b):
 b=entry(b,alloc);a=b.index('\t\tclr_country_flag = cannibalism_pending_absorption');z=b.rfind('\t}\r\n}');work=b[a:z]
 i=work.index('\t\tset_temp_variable = { cannibalism_integration_larder_factor');j=work.index('\t\tcannibalism_add_current_warlord_larder_to_unified_host = yes');factors=work[i:j]
 work=work[:i]+work[j:];work=repl(work,'\t\tcannibalism_add_current_warlord_larder_to_unified_host = yes\n','')
 work=repl(work,'\t\tevent_target:cannibalism_unification_host = { puppet = ROOT add_to_variable = { cannibalism_autonomous_warlord_count = 1 } }\n','\t\tevent_target:cannibalism_larder_destination_country = {\n\t\t\tpuppet = event_target:cannibalism_larder_source_country\n\t\t\tadd_to_variable = { cannibalism_autonomous_warlord_count = 1 }\n\t\t\tcannibalism_clamp_and_publish_current_larder = yes\n\t\t}\n')
 pre='''		event_target:cannibalism_unification_host = { save_event_target_as = cannibalism_larder_destination_country }
		cannibalism_capture_current_larder_transfer_capitals = yes
'''+factors.replace('\r\n','\n')+'''		set_temp_variable = { cannibalism_transfer_route_fraction = cannibalism_integration_larder_factor }
		cannibalism_prepare_larder_transfer_quote = yes
		cannibalism_add_current_warlord_larder_to_unified_host = yes
		if = {
			limit = { check_variable = { cannibalism_transfer_committed > constant:cannibalism_larder_logistics.zero } }
'''
 return b[:a]+pre.replace('\n','\r\n')+indent(work)+'\t\t}\r\n'+b[z:]
E=edit(E,'cannibalism_bargain_current_warlord_autonomy',autonomy)
def cbl(b):
 b=entry(b,alloc+'\tset_temp_variable = { cannibalism_runtime_migration_result = constant:cannibalism_larder_logistics.zero }\n\tset_temp_variable = { cannibalism_spread_queue_validation_result = constant:cannibalism_larder_logistics.zero }\n\tcannibalism_validate_spread_queue = yes\n')
 b=repl(b,'\t\tlimit = { cannibalism_selected_unification_host_is_valid = yes }','\t\tlimit = { cannibalism_selected_unification_host_is_valid = yes check_variable = { cannibalism_spread_queue_validation_result > constant:cannibalism_larder_logistics.zero } }')
 b=repl(b,'\t\t\tcapital_scope = { save_event_target_as = cannibalism_unification_capital_state }\n','''			save_event_target_as = cannibalism_larder_source_country
			set_temp_variable = { cannibalism_transfer_source_generation = cannibalism_actor_generation }
			capital_scope = {
				save_event_target_as = cannibalism_unification_capital_state
				save_event_target_as = cannibalism_larder_source_capital
				save_event_target_as = cannibalism_larder_destination_capital
				set_temp_variable = { cannibalism_larder_source_capital_captured = constant:cannibalism_larder_logistics.one }
				set_temp_variable = { cannibalism_larder_destination_capital_captured = constant:cannibalism_larder_logistics.one }
			}
''')
 a=b.index('\t\t# The public flag is set before CBL');z=b.rfind('\t}\r\n}')
 gate='''		CBL = { save_event_target_as = cannibalism_larder_destination_country }
		set_temp_variable = { cannibalism_transfer_constructor_context = constant:cannibalism_larder_logistics.one }
		set_temp_variable = { cannibalism_transfer_route_fraction = constant:cannibalism_unification.host_larder_transfer_factor }
		event_target:cannibalism_larder_source_country = { cannibalism_prepare_larder_transfer_quote = yes }
		if = {
			limit = { check_variable = { cannibalism_transfer_result > constant:cannibalism_larder_logistics.zero } }
			set_temp_variable = { cannibalism_inherited_larder = cannibalism_transfer_received }
'''
 b=b[:a]+gate.replace('\n','\r\n')+indent(b[a:z])+'\t\t}\r\n'+b[z:]
 o='\t\t\t\tcannibalism_migrate_runtime_references_to_unified_country = yes\r\n';a=b.index(o)+len(o);z=b.rfind('\t\t}\r\n\t}\r\n}')
 tail=repl(b[a:z],'\t\t\t\tset_variable = { cannibalism_integration_name_index','\t\t\t\tcannibalism_apply_initial_larder_inheritance = yes\n\t\t\t\tset_variable = { cannibalism_integration_name_index')
 b=b[:a]+'\t\t\t}\r\n\t\t\tif = {\r\n\t\t\t\tlimit = { check_variable = { cannibalism_runtime_migration_result > constant:cannibalism_larder_logistics.zero } }\r\n\t\t\t\tCBL = {\r\n'+indent(tail)+'\t\t\t}\r\n'+b[z:]
 old='\t\t\t\t\tset_variable = { global.cannibalism_unification_host_generation = cannibalism_actor_generation }\n'
 b=repl(b,old,'')
 b=repl(b,'\t\t\t\t\tsave_global_event_target_as = cannibalism_latest_actor\n','\t\t\t\t\tsave_global_event_target_as = cannibalism_latest_actor\n'+old+'\t\t\t\t\tcannibalism_clamp_and_publish_current_larder = yes\n')
 return b.replace('\t\t\t\t\tadd_country_leader_role = {','\t\t\t\tadd_country_leader_role = {')
E=edit(E,'cannibalism_create_unified_country_from_selected_host',cbl)
def primary(b):
 b=entry(b,'\tset_temp_variable = { cannibalism_primary_larder_inheritance_result = constant:cannibalism_larder_logistics.zero }\n')
 b=repl(b,'\t\t\tcheck_variable = { cannibalism_primary_warlord_donor_can_be_absorbed > 0 }\n','\t\t\tcheck_variable = { cannibalism_primary_warlord_donor_can_be_absorbed > 0 }\n\t\t\tcheck_variable = { cannibalism_transfer_result > constant:cannibalism_larder_logistics.zero }\n\t\t\tcannibalism_has_valid_unification_destination = yes\n')
 b=repl(b,'\t\t\t\tunion_compatible_researched_technologies_from_donor = yes\n','\t\t\t\tcannibalism_apply_initial_larder_inheritance = yes\n\t\t\t\tunion_compatible_researched_technologies_from_donor = yes\n')
 b=repl(b,'\t\t\t\tadd_to_variable = { cannibalism_integrated_warlord_count = 1 }\n','\t\t\t\tcannibalism_clamp_and_publish_current_larder = yes\n\t\t\t\tadd_to_variable = { cannibalism_integrated_warlord_count = 1 }\n')
 return repl(b,'\t\t\t}\n\t\t}\n\t}\n}','\t\t\t}\n\t\t\tset_temp_variable = { cannibalism_transfer_result = constant:cannibalism_larder_logistics.zero }\n\t\t\tset_temp_variable = { cannibalism_primary_larder_inheritance_result = constant:cannibalism_larder_logistics.one }\n\t\t}\n\t}\n}')
E=edit(E,'cannibalism_absorb_primary_warlord_donor_into_wendigo',primary)
def wendigo(b):
 b=entry(b,alloc+'\tset_temp_variable = { cannibalism_primary_larder_inheritance_result = constant:cannibalism_larder_logistics.zero }\n\tset_temp_variable = { cannibalism_spread_queue_validation_result = constant:cannibalism_larder_logistics.zero }\n\tcannibalism_validate_spread_queue = yes\n')
 b=repl(b,'\t\t\tcannibalism_selected_unification_host_is_valid = yes\n','\t\t\tcannibalism_selected_unification_host_is_valid = yes\n\t\t\tcheck_variable = { cannibalism_spread_queue_validation_result > constant:cannibalism_larder_logistics.zero }\n')
 a=b.index('\t\t# The reveal flag precedes every transformed country');z=b.rfind('\t}\r\n}')
 gate='''		event_target:cannibalism_wendigo_merge_host = { save_event_target_as = cannibalism_larder_destination_country }
		if = {
			limit = { check_variable = { cannibalism_primary_warlord_donor_can_be_absorbed > constant:cannibalism_larder_logistics.zero } }
			set_temp_variable = { cannibalism_transfer_constructor_context = constant:cannibalism_larder_logistics.one }
			set_temp_variable = { cannibalism_transfer_route_fraction = constant:cannibalism_unification.host_larder_transfer_factor }
			event_target:cannibalism_primary_warlord_donor = {
				cannibalism_capture_current_larder_transfer_capitals = yes
				cannibalism_prepare_larder_transfer_quote = yes
			}
			set_temp_variable = { cannibalism_inherited_larder = cannibalism_transfer_received }
		}
		if = {
			limit = {
				OR = {
					check_variable = { cannibalism_transfer_result > constant:cannibalism_larder_logistics.zero }
					check_variable = { cannibalism_primary_warlord_donor_can_be_absorbed < constant:cannibalism_larder_logistics.one }
				}
			}
'''
 b=b[:a]+gate.replace('\n','\r\n')+indent(b[a:z])+'\t\t}\r\n'+b[z:]
 b=repl(b,'\t\t\t\tcannibalism_prepare_wendigo_merge_identity = yes\n','\t\t\t\tcannibalism_prepare_wendigo_merge_identity = yes\n\t\t\t\tset_variable = { global.cannibalism_unification_host_generation = cannibalism_actor_generation }\n')
 b=repl(b,'\t\t\t\tset_variable = { global.cannibalism_unification_host_generation = cannibalism_actor_generation }\n\t\t\t\tset_temp_variable = { cannibalism_evolution_stage_to_record','\t\t\t\tset_temp_variable = { cannibalism_evolution_stage_to_record')
 o='\t\t\tcannibalism_absorb_primary_warlord_donor_into_wendigo = yes\r\n';a=b.index(o)+len(o);z=b.rfind('\t\t}\r\n\t}\r\n}')
 final='''			if = {
				limit = { check_variable = { cannibalism_primary_warlord_donor_can_be_absorbed < constant:cannibalism_larder_logistics.one } }
				event_target:cannibalism_wendigo_merge_host = {
					cannibalism_apply_initial_larder_inheritance = yes
					cannibalism_clamp_and_publish_current_larder = yes
				}
			}
			if = {
				limit = {
					OR = {
						check_variable = { cannibalism_primary_larder_inheritance_result > constant:cannibalism_larder_logistics.zero }
						check_variable = { cannibalism_primary_warlord_donor_can_be_absorbed < constant:cannibalism_larder_logistics.one }
					}
				}
'''
 return b[:a]+final.replace('\n','\r\n')+indent(b[a:z])+'\t\t\t}\r\n'+b[z:]
E=edit(E,'cannibalism_create_wendigo_unification_from_selected_hosts',wendigo)

for name in ['cannibalism_consume_current_state','cannibalism_pay_focus_closure_larder_cost','cannibalism_unified_pay_current_larder_cost','cannibalism_unified_execute_convoy_harvest','cannibalism_pay_wendigo_larder_and_command_cost']:
 def finalize(b):
  pat=r'(?m)^(\t+)clamp_variable = \{[^}]*?var = cannibalism_larder[^}]*?max = constant:cannibalism_unification\.global_larder_maximum\s*\}\r?\n\1set_variable = \{ global\.cannibalism_global_larder = cannibalism_larder \}'
  ms=list(re.finditer(pat,b));assert len(ms)==1,(name,len(ms));m=ms[0]
  return b[:m.start()]+m.group(1)+'cannibalism_clamp_and_publish_current_larder = yes'+b[m.end():]
 E=edit(E,name,finalize)
for name in ['cannibalism_process_current_actor_pulse','cannibalism_execute_deliberate_foreign_seed']:
 E=edit(E,name,lambda b:repl(b,'clamp_variable = { var = cannibalism_larder min = constant:cannibalism_consumption.larder_min max = constant:cannibalism_consumption.larder_max }','cannibalism_clamp_and_publish_current_larder = yes'))
for name in ['cannibalism_initialize_new_country_incarnation','cannibalism_setup_current_warlord_country','cannibalism_activate_current_country_from_external_spread']:
 def initialize_capacity(b):
  m=re.search(r'(?m)^(\t+)set_variable = \{ cannibalism_larder = 0 \}',b);assert m,name
  return b[:m.end()]+'\r\n'+m.group(1)+'cannibalism_refresh_larder_effective_capacity = yes'+b[m.end():]
 E=edit(E,name,initialize_capacity)
E=edit(E,'cannibalism_unified_refresh_operational_profiles',lambda b:entry(b,'\tcannibalism_refresh_larder_effective_capacity = yes\n'))
for name in ['cannibalism_unified_initialize_decision_values','cannibalism_unified_focus_finalize_reward','cannibalism_open_wendigo_inherited_cannibal_recruitment']:
 b,_,_=get(E,name)
 if 'cannibalism_unified_refresh_contract_capacities = yes' in b:E=edit(E,name,lambda b:repl(b,'\tcannibalism_unified_refresh_contract_capacities = yes\n',''))
E=edit(E,'cannibalism_reset_current_country_incarnation_state',lambda b:entry(b,'\tclear_variable = cannibalism_larder_effective_capacity\n'))
E=edit(E,'cannibalism_prepare_current_warlord_slot_for_unification',lambda b:entry(b,'\tclear_variable = cannibalism_larder_effective_capacity\n'))
E=edit(E,'cannibalism_complete_current_country_local_victory',lambda b:repl(b,'\t\tclr_country_flag = cannibalism_country_active\n','\t\tclear_variable = cannibalism_larder_effective_capacity\n\t\tclr_country_flag = cannibalism_country_active\n'))
E=edit(E,'cannibalism_complete_global_cleanup',lambda b:repl(b,'\t\tclear_global_event_target = cannibalism_unification_host\n','\t\tfor_each_scope_loop = {\n\t\t\tarray = global.cannibalism_actor_countries\n\t\t\tclear_variable = cannibalism_larder_effective_capacity\n\t\t}\n\t\tclear_variable = global.cannibalism_unification_host_generation\n\t\tclear_global_event_target = cannibalism_unification_host\n'))
T=before[FILES[2]].decode('utf-8')
guard='''cannibalism_has_valid_unification_destination = {
	has_event_target = cannibalism_unification_host
	has_variable = global.cannibalism_unification_host_generation
	check_variable = { global.cannibalism_unification_host_generation > constant:cannibalism_larder_logistics.zero }
	event_target:cannibalism_unification_host = {
		cannibalism_is_valid_unification_destination = yes
		has_variable = cannibalism_actor_generation
		check_variable = { var = cannibalism_actor_generation value = global.cannibalism_unification_host_generation compare = equals }
	}
}'''
T=edit(T,'cannibalism_has_valid_unification_destination',lambda _:guard.replace('\n','\r\n'))
context='''
# Donor-country quote/commit context, including pre-reveal constructors.
# Constructor mode permits the selected donor and exact planned recipient only.
cannibalism_larder_transfer_context_is_valid = {
	exists = yes
	NOT = { has_capitulated = yes }
	has_event_target = cannibalism_larder_source_country
	has_event_target = cannibalism_larder_destination_country
	tag = event_target:cannibalism_larder_source_country
	has_variable = cannibalism_actor_generation
	check_variable = { cannibalism_actor_generation > constant:cannibalism_larder_logistics.zero }
	check_variable = { var = cannibalism_actor_generation value = cannibalism_transfer_source_generation compare = equals }
	OR = {
		AND = {
			cannibalism_has_valid_unification_destination = yes
			event_target:cannibalism_larder_destination_country = { tag = event_target:cannibalism_unification_host }
		}
		AND = {
			check_variable = { var = cannibalism_transfer_constructor_context value = constant:cannibalism_larder_logistics.one compare = equals }
			cannibalism_selected_unification_host_is_valid = yes
			tag = event_target:cannibalism_unification_host
			OR = {
				event_target:cannibalism_larder_destination_country = { tag = CBL }
				AND = {
					cannibalism_selected_wendigo_merge_host_is_valid = yes
					event_target:cannibalism_larder_destination_country = { tag = event_target:cannibalism_wendigo_merge_host }
				}
			}
		}
	}
}
'''
T+='\r\n'+context.replace('\n','\r\n')
C=before[FILES[1]].decode('utf-8')+'\r\n# Event014 capacity and frozen-capital distance tuning.\r\n# Development is the existing administrative contract index, not buildings.\r\n'+constants.replace('\n','\r\n')+'\r\n'
L=before[FILES[3]].decode('utf-8-sig')
L=repl(L,'cannibalism.gui.larder.tt: "Larder is finite. Usable population, captured stores, and exact state transactions supply it."','cannibalism.gui.larder.tt: "Larder is finite. Usable population, captured stores, and exact state transactions supply it. Current capacity: §Y[?cannibalism_larder_effective_capacity|0]§!."')
L=repl(L,'cannibalism.gui.global_larder.tt: "The unified reserve inherits every gathered store and the yield from later population consumption."','cannibalism.gui.global_larder.tt: "The unified reserve receives stores after route and distance losses, plus population-consumption yield. Current capacity: §Y[?cannibalism_larder_effective_capacity|0]§!, supported by controlled territory and completed logistics administration. Stores above capacity are lost."')
I=before[FILES[4]].decode('utf-8')+'\r\nThe Event014 owner API [Larder logistics](../../docs/events/014_cannibalism/larder_logistics.md) documents country effective-capacity calculation, post-transaction clamp/publication, caller-owned exact distance quotes from frozen regular capital targets, one-shot dispatch/receipt commit, opening inheritance, generation guards, cleanup and the fifty-flag administrative development mapping.\r\n'
after={FILES[0]:E.encode('utf-8'),FILES[1]:C.encode('utf-8'),FILES[2]:T.encode('utf-8'),FILES[3]:b'\xef\xbb\xbf'+L.encode('utf-8'),FILES[4]:I.encode('utf-8')}
manifest=[];patch=[]
for name,data in after.items():
 dest=EV/'after'/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
 manifest.append(dict(relativePath=name,beforeSha256=hashlib.sha256(before[name]).hexdigest(),afterSha256=hashlib.sha256(data).hexdigest()))
 patch.extend(difflib.unified_diff(before[name].decode('utf-8-sig').splitlines(keepends=True),data.decode('utf-8-sig').splitlines(keepends=True),fromfile='before/'+name,tofile='after/'+name))
 if '--apply' in sys.argv:(ROOT/name).write_bytes(data)
(EV/'source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
(EV/'owned_source.patch').write_bytes(''.join(patch).encode('utf-8'))
print('Applied owned source hunks.' if '--apply' in sys.argv else 'Review candidates written. Source unchanged.')
print(json.dumps(manifest,indent=2))
