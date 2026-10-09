"""Actual-source native callback, cost, selection, fault and CXT integration cases.
Native primitives use the retained core VM. This does not render or run HOI4.
"""
from pathlib import Path
from decimal import Decimal as D
import importlib.util, contextlib, io, json, hashlib, copy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location('paleo_core_tests', HERE/'core_source_tests.py')
core = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
	spec.loader.exec_module(core)
P, H, G = core.P, core.H, core.G
source_paths = [
	'common/decisions/016_mengele_paleogenetics_stage_decisions.txt',
	'common/decisions/016_mengele_paleogenetics_site_selection_decisions.txt',
	'common/scripted_localisation/016_mengele_paleogenetics_deployment_localisation.txt',
	'common/scripted_effects/016_mengele_paleogenetics_deployment_cxt_effects.txt',
]
def read(name): return (ROOT/name).read_text(encoding='utf-8-sig')
decisions = {}
for name in source_paths[:2]:
	for _, _, category in core.parse(read(name)):
		if not isinstance(category, list): continue
		for decision, _, body in category: decisions[decision] = core.fields(body)
for name in source_paths[3:]:
	for key, _, body in core.parse(read(name)): core.defs[key] = body
texts = {}
for _, _, body in core.parse(read(source_paths[2])):
	fields = core.fields(body)
	texts[fields['name']] = [value for key, _, value in body if key == 'text']
class VM(core.VM):
	def testrow(self, key, op, value):
		if key == 'hidden_trigger': return self.test(value)
		if key == 'custom_trigger_tooltip': return self.test([row for row in value if row[0] != 'tooltip'])
		if key == 'always': return value == 'yes'
		if key == 'tag': return (self.this == 10001) == (value == 'CXT')
		return super().testrow(key, op, value)
	def loc(self, name):
		for block in texts[name]:
			fields = core.fields(block)
			if self.test(fields['trigger']): return fields['localization_key']
		raise AssertionError('no localisation branch: '+name)
	def native(self, decision, field):
		self.run(core.fields(decisions[decision][field])['hidden_effect'])

cases = []
def case(name, function): function(); cases.append(name)
def chosen():
	v=VM(); v.frm=20001; v.native('mengele_event016_paleogenetics_select_reserve','complete_effect')
	v.frm=20002; v.native('mengele_event016_paleogenetics_select_hatchery','complete_effect')
	assert v.call(H+'selection_is_valid',True)
	return v
def paid():
	v=chosen(); v.owner['cic']=D(0)
	v.native('mengele_event016_paleogenetics_deployment','complete_effect')
	assert v.call(H+'pending_is_authenticated',True)
	return v
def finish(v): v.native('mengele_event016_paleogenetics_deployment','remove_effect')
def ordinary(v):
	return {k:copy.deepcopy(value) for k,value in v.owner.items() if k not in ('flags','v')}, {k:value for k,value in v.owner['v'].items() if not k.startswith('chaosx_cxt_')}, {k for k in v.owner['flags'] if not k.startswith('chaosx_cxt_')}

for resource, wallet, amount, text_name, stem in [
	('political_power','pp',130,'GetMengelePaleogeneticsDeploymentPoliticalPowerCost','pp'),
	('support','support',975,'GetMengelePaleogeneticsDeploymentSupportCost','support'),
	('fuel','fuel',1500,'GetMengelePaleogeneticsDeploymentFuelCost','fuel')]:
	for difference in [-1,0,1]:
		def colour(wallet=wallet, amount=amount, text_name=text_name, stem=stem, difference=difference):
			v=chosen();v.owner[wallet]=D(amount+difference)
			before=ordinary(v)
			gate=v.call(H+'deployment_decision_can_pay',True)
			assert gate == (difference >= 0)
			assert v.loc(text_name) == 'mengele_event016_paleogenetics_deployment_'+stem+('_ready' if difference >= 0 else '_blocked')
			assert ordinary(v)==before
		case(resource+' quote colour/admission boundary '+str(difference),colour)
for count in [3,4,5]:
	def factory(count=count):
		v=chosen();v.owner['cic']=D(count)
		assert v.call(H+'deployment_decision_can_pay',True)==(count>=4)
	case('full native CIC admission '+str(count),factory)
def source_entry():
	v=paid(); frozen=copy.deepcopy(v.owner['v']); resources=(v.owner['pp'],v.owner['support'],v.owner['fuel'])
	v.native('mengele_event016_paleogenetics_deployment','complete_effect')
	assert v.owner['v']==frozen and resources==(v.owner['pp'],v.owner['support'],v.owner['fuel'])
	assert v.t[P+'native_entry']==0
	finish(v);assert core.completed(v) and len(v.builds)==2
	assert decisions['mengele_event016_paleogenetics_deployment']['cancel_if_not_visible']=='no'
case('literal native callback reserves once and finishes actual paired source',source_entry)
def partial_reset():
	v=VM();v.frm=20001;v.native('mengele_event016_paleogenetics_select_reserve','complete_effect')
	v.scopes[20002]['slots']=D(0)
	assert not v.call(H+'selection_is_valid',True)
	assert v.test(decisions['mengele_event016_paleogenetics_clear_site_selection']['visible'])
	v.native('mengele_event016_paleogenetics_clear_site_selection','complete_effect')
	assert P+'selected_reserve' not in v.owner['v']
	v.frm=20002;v.native('mengele_event016_paleogenetics_select_reserve','complete_effect')
	v.frm=20001;v.native('mengele_event016_paleogenetics_select_hatchery','complete_effect')
	assert v.call(H+'selection_is_valid',True) and not v.builds and v.owner['pp']==1000
case('incomplete site selection can reset and invert a two-state pair',partial_reset)
def funded_reset_rejected():
	v=paid();frozen=copy.deepcopy(v.owner)
	assert not v.test(decisions['mengele_event016_paleogenetics_clear_site_selection']['visible'])
	v.native('mengele_event016_paleogenetics_clear_site_selection','complete_effect')
	assert frozen==v.owner
case('free reset cannot change a funded pair',funded_reset_rejected)
def missing_entitlement():
	v=chosen();v.owner['tech']=False
	assert not v.test(decisions['mengele_event016_paleogenetics_deployment']['available'])
	before=ordinary(v);v.native('mengele_event016_paleogenetics_deployment','complete_effect')
	assert ordinary(v)==before and not v.builds
case('native admission and debit reject absent operational entitlement',missing_entitlement)
def lost_entitlement():
	v=paid();v.owner['tech']=False
	assert v.test(decisions['mengele_event016_paleogenetics_deployment']['cancel_trigger'])
	v.native('mengele_event016_paleogenetics_deployment','cancel_effect')
	assert not core.flag(v,'deployment_pending') and not v.builds
	assert (v.owner['pp'],v.owner['support'],v.owner['fuel'])==(D(1000),D(4000),D(9000))
case('entitlement loss cancels unattempted native work with matching refund',lost_entitlement)
def cic_retune():
	v=paid();key='constant:brilliant_scientist_project_stage_cost.paleogenetics_deployment_civilian_factories';old=core.constants[key]
	try:
		core.constants[key]=D(6)
		assert v.owner['v'][P+'paid_cic']==D(4)
		assert v.call(H+'pending_is_authenticated',True)
		finish(v);assert core.completed(v) and len(v.builds)==2
	finally:core.constants[key]=old
case('funded CIC snapshot survives later nominal quote retuning',cic_retune)
def wrong_cic_snapshot():
	v=paid();v.owner['v'][P+'paid_cic']=D(5)
	assert not v.call(H+'pending_is_authenticated',True)
	finish(v);assert not core.completed(v) and not v.builds
case('mismatched frozen CIC receipt cannot authorize construction',wrong_cic_snapshot)
def source_recovery():
	v=paid();v.scopes[20002]['slots']=D(0);finish(v)
	assert v.test(decisions['mengele_event016_paleogenetics_recover_deployment']['visible'])
	assert not v.test(decisions['mengele_event016_paleogenetics_recover_deployment']['available'])
	v.scopes[20002]['slots']=D(1)
	assert v.test(decisions['mengele_event016_paleogenetics_recover_deployment']['available'])
	before=(v.owner['pp'],v.owner['support'],v.owner['fuel'])
	v.native('mengele_event016_paleogenetics_recover_deployment','complete_effect')
	assert core.completed(v) and len(v.builds)==2
	assert before==(v.owner['pp'],v.owner['support'],v.owner['fuel'])
case('actual free recovery callback supplies only missing component',source_recovery)
for fault in ['payment_unverified','refund_unverified','construction_unverified']:
	def fault_visible(fault=fault):
		v=paid();v.owner['flags'].discard(P+'deployment_timer_active');v.owner['flags'].add(P+fault)
		assert v.test(decisions['mengele_event016_paleogenetics_recover_deployment']['visible'])
		assert not v.test(decisions['mengele_event016_paleogenetics_recover_deployment']['available'])
		assert 'uncertain' in v.loc('GetMengelePaleogeneticsConstructionStatus')
		before=ordinary(v);v.native('mengele_event016_paleogenetics_recover_deployment','complete_effect')
		assert ordinary(v)==before and not v.builds
	case('fault visible but no funded output admission '+fault,fault_visible)
for phase in ['unselected','selected','paid','partial','completed','fault']:
	def probe(phase=phase):
		v=VM() if phase=='unselected' else chosen() if phase=='selected' else paid()
		if phase=='partial':v.scopes[20002]['slots']=D(0);finish(v)
		if phase=='completed':finish(v)
		if phase=='fault':v.owner['flags'].add(P+'construction_unverified')
		v.owner['flags'].add('chaosx_test_country_initialized');before=ordinary(v)
		v.call('chaosx_cxt_event016_probe_paleogenetics_deployment')
		assert ordinary(v)==before
		assert ('chaosx_cxt_event016_paleogenetics_pair_completed' in v.owner['flags']) == (phase=='completed')
		assert ('chaosx_cxt_event016_paleogenetics_paid_authenticated' in v.owner['flags']) == (phase in ['paid','partial','fault'])
	case('CXT observer preserves production state '+phase,probe)
for fixture in ['wrong_country','not_initialized']:
	def probe_rejected(fixture=fixture):
		v=paid()
		if fixture=='wrong_country':v.this=10002;v.s['flags'].add('chaosx_test_country_initialized')
		before=copy.deepcopy(v.scopes);v.call('chaosx_cxt_event016_probe_paleogenetics_deployment');assert before==v.scopes
	case('CXT observer rejection '+fixture,probe_rejected)
result={'cases_passed':len(cases),'cases':cases,'core_cases_passed':core.cases,
	'source_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in source_paths},
	'limits':['Core VM native primitives and two external provider fixtures','No native UI render, clock, reservation or callback observation','Cost colour branch selection is source behavior, not displayed glyph or width acceptance']}
(HERE/'parent_frontend_result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
