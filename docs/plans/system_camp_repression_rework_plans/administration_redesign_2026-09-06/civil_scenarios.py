"""Evaluate bounded civil script scenarios from current source, without launching HOI4.
This restricted interpreter rejects unsupported exercised constructs; native effects
for stockpile debit are represented by exact fixture values, not engine evidence.
"""
from pathlib import Path
import json
import re
from dataclasses import dataclass, field

ROOT_DIR = Path(__file__).resolve().parents[4]
TOKEN = re.compile(r'"[^"\n]*"|[{}=<>]|[^\s{}=<>]+')

def parse(text):
    tokens = TOKEN.findall(re.sub(r'#[^\n]*', '', text))
    index = 0
    def block(end=False):
        nonlocal index
        out = []
        while index < len(tokens) and tokens[index] != '}':
            key, op = tokens[index:index+2]
            index += 2
            assert op in ('=', '<', '>'), (key, op)
            if tokens[index] == '{':
                index += 1
                value = block(True)
            else:
                value = tokens[index].strip('"')
                index += 1
            out.append((key, op, value))
        if end:
            assert tokens[index] == '}'
            index += 1
        return out
    return block()

def load(relative):
    return parse((ROOT_DIR / relative).read_text(encoding='utf-8-sig'))

constants = {}
for name, value in re.findall(r'^(@[A-Z_]+)\s*=\s*(-?\d+(?:\.\d+)?)',
        (ROOT_DIR / 'common/scripted_effects/camp_administration_effects.txt').read_text(encoding='utf-8-sig'), re.M):
    constants[name] = float(value)
for filename in ('camp_administration_constants.txt', 'camp_administration_civil_constants.txt', 'camp_administration_ui_constants.txt', '026_black_friday_constants.txt'):
    for category, _, entries in load('common/script_constants/' + filename):
        for key, _, value in entries:
            if key != 'schema':
                constants[f'{category}.{key}'] = float(value)
effects = {}
for filename in ('camp_administration_effects.txt', 'camp_administration_civil_effects.txt', 'camp_administration_ui_effects.txt'):
    effects.update({key: value for key, _, value in load('common/scripted_effects/' + filename)})
triggers = {}
for filename in ('camp_administration_triggers.txt', 'camp_administration_civil_triggers.txt', 'camp_administration_ui_triggers.txt'):
    triggers.update({key: value for key, _, value in load('common/scripted_triggers/' + filename)})

# The origin-observer layer is exercised by the origin_* source suites; this restricted evaluator
# declares every origin helper satisfied (reconciled, provenance-ready host, no ambiguity) so the
# civil flows run on their own.
for _key, _, _value in load('common/scripted_effects/camp_administration_origin_effects.txt'):
    effects[_key] = []
for _key, _, _value in load('common/scripted_triggers/camp_administration_origin_triggers.txt'):
    triggers[_key] = [('always', '=', 'no')] if any(word in _key for word in ('incomplete', 'ambiguous', 'uncertain', 'quarantine', 'frozen', 'paused')) else []

# National war gate read by the civil authorities: the scenario scope's single war field.
triggers['camp_admin_country_major_war'] = [('has_war', '=', 'yes')]
# The scenarios hold no site registry: every country site is treated as ready for reform.
triggers['camp_admin_country_sites_ready_for_reform'] = []


@dataclass
class Scope:
    tag: str = ''
    government: str = 'democratic'
    war: bool = True
    subject: str = ''
    cosmetic: str = ''
    controller: object = None
    values: dict = field(default_factory=dict)
    flags: set = field(default_factory=set)

class VM:
    def __init__(self, root, date='1942.3.1'):
        self.root = root
        self.date = date
        self.temp = {}
        self.targets = {}
        self.previous_scope = None
        self.countries = {root.tag: root, 'ENG': Scope('ENG'), 'GER': Scope('GER', 'fascism')}
        self.globals = set()
    def value(self, token, scope):
        if token == 'ROOT': return self.root
        if token == 'THIS': return scope
        if token.startswith('event_target:'): return self.targets[token[13:]]
        if token.startswith('constant:'):
            return constants[token[9:]]
        if token.startswith('@'): return constants[token]
        if token.endswith('^num'): return len(scope.values.get(token[:-4], []))
        if '^' in token:
            array, index = token.split('^', 1)
            return scope.values[array][int(self.value(index, scope))]
        if token.startswith('ROOT.'):
            return self.root.values.get(token[5:], 0)
        if token.startswith('PREV.'):
            return self.previous_scope.values.get(token[5:], 0)
        if token.startswith('var:'):
            return self.value(token[4:], scope)
        try:
            return float(token)
        except ValueError:
            return self.temp.get(token, scope.values.get(token, token))
    def compare(self, left, op, right):
        return {'=': lambda: left == right, '>': lambda: left > right, '<': lambda: left < right}[op]()
    def check(self, entries, scope):
        return all(self.one(key, op, value, scope) for key, op, value in entries)
    def one(self, key, op, value, scope):
        if key == 'OR': return any(self.one(*entry, scope) for entry in value)
        if key == 'AND': return self.check(value, scope)
        if key == 'NOT': return not self.check(value, scope)
        if key == 'ROOT': return self.check(value, self.root)
        if key == 'CONTROLLER':
            previous = self.previous_scope
            self.previous_scope = scope
            answer = self.check(value, scope.controller)
            self.previous_scope = previous
            return answer
        if key in self.countries: return self.check(value, self.countries[key])
        if key.startswith('var:'): return self.check(value, self.value(key, scope))
        if key in triggers: return self.check(triggers[key], scope) == (value == 'yes')
        if key == 'camp_rework_country_is_eligible': return True
        if key == 'has_active_camp_network': return bool(scope.values.get('network',False))
        if key == 'date': return self.compare(tuple(map(int, self.date.split('.'))), op, tuple(map(int, value.split('.'))))
        if key in ('tag', 'original_tag'):
            target = self.value(value, scope)
            return scope.tag == (target.tag if isinstance(target,Scope) else target)
        if key == 'is_ai': return scope.values.get('is_ai',False) == (value == 'yes')
        if key == 'political_power': return self.compare(scope.values.get('political_power',0),op,self.value(value,scope))
        if key == 'has_political_power': return self.compare(scope.values.get('political_power',0),op,self.value(value,scope))
        if key == 'has_equipment':
            equipment, operator, amount = value[0]
            stock = scope.values.get('equipment', {}).get(equipment, 0)
            if equipment == 'support_equipment_1': stock = scope.values.get('support', stock)
            return self.compare(stock,operator,self.value(amount,scope))
        if key == 'has_manpower': return self.compare(scope.values.get('manpower',0),op,self.value(value,scope))
        if key == 'has_government': return scope.government == value
        if key == 'has_war': return scope.war == (value == 'yes')
        if key == 'has_cosmetic_tag': return scope.cosmetic == value
        if key == 'is_subject_of':
            target = self.value(value, scope)
            return scope.subject == (target.tag if isinstance(target, Scope) else target)
        if key == 'is_controlled_by': return scope.controller == self.value(value, scope)
        if key == 'is_core_of':
            target = self.value(value, scope)
            return (target.tag if isinstance(target, Scope) else target) in scope.values.get('cores', [])
        if key == 'has_global_flag': return value in self.globals
        if key == 'has_dynamic_modifier': return {k: v for k, _, v in value}.get('modifier') in scope.values.get('modifiers', ())
        if key == 'has_capitulated': return scope.values.get('capitulated', False) == (value == 'yes')
        if key == 'exists': return value == 'yes'
        if key in ('has_country_flag', 'has_state_flag'): return value in scope.flags
        if key == 'has_variable': return value in self.temp or value in scope.values
        if key == 'check_variable':
            data = {k: v for k, _, v in value}
            if 'var' in data:
                lhs, rhs = self.value(data['var'], scope), self.value(data['value'], scope)
                cmp = data.get('compare', 'equals')
                return {'greater_than_or_equals': lambda: lhs >= rhs, 'less_than_or_equals': lambda: lhs <= rhs,
                        'greater_than': lambda: lhs > rhs, 'less_than': lambda: lhs < rhs, 'equals': lambda: lhs == rhs}[cmp]()
            k, operator, v = value[0]
            lhs = self.value(k, scope)
            if isinstance(lhs, str): lhs = 0
            return self.compare(lhs, operator, self.value(v, scope))
        raise ValueError(f'Unsupported trigger {key}')
    def run(self, entries, scope):
        previous = False
        for key, _, value in entries:
            if key in ('if', 'else_if', 'else'):
                data = {k: v for k, _, v in value}
                take = (key == 'if' or not previous) and self.check(data.get('limit', []), scope)
                if key == 'if': previous = False
                if take:
                    self.run([row for row in value if row[0] != 'limit'], scope)
                    previous = True
                continue
            if key in ('camp_admin_refresh_interface','camp_admin_record_history'):
                scope.values.setdefault('presentation_calls',[]).append(key)
                continue
            if key == 'hidden_effect':
                # Hidden sale-credit bookkeeping (Event 026) is outside this suite.
                continue
            if key == 'black_friday_price_table_quote':
                # Ordinary price: the sale table is outside this suite (black_friday_sale_prices.py).
                self.temp['black_friday_price_payable'] = self.temp.get('black_friday_price_ordinary', 0)
                continue
            if key in effects:
                self.run(effects[key], scope)
                continue
            if key == 'ROOT': self.run(value, self.root); continue
            if key == 'save_event_target_as': self.targets[value]=scope; continue
            if key == 'for_each_scope_loop':
                args={k:v for k,_,v in value}
                previous_scope=self.previous_scope
                for target in scope.values.get(args['array'],[]):
                    self.previous_scope=scope
                    self.run([row for row in value if row[0]!='array'],target)
                self.previous_scope=previous_scope
                continue
            if key == 'while_loop_effect':
                args = {k:v for k,_,v in value}
                for _ in range(10000):
                    if not self.check(args['limit'], scope): break
                    self.run([row for row in value if row[0] != 'limit'], scope)
                else:
                    raise AssertionError('Unbounded source loop')
                continue
            if key.startswith('var:'): self.run(value, self.value(key, scope)); continue
            if key in ('set_state_flag', 'set_country_flag'): scope.flags.add(value); continue
            if key in ('clr_state_flag', 'clr_country_flag'): scope.flags.discard(value); continue
            if key == 'remove_dynamic_modifier': continue
            if key == 'remove_mission': scope.values.setdefault('removed_missions', []).append(value); continue
            if key == 'clear_variable': scope.values.pop(value, None); continue
            if key == 'clear_temp_variable': self.temp.pop(value, None); continue
            if key == 'clear_array': scope.values[value] = []; continue
            if key == 'add_to_array':
                args = {k:v for k,_,v in value}
                scope.values.setdefault(args['array'], []).append(self.value(args['value'], scope))
                continue
            if key == 'remove_support_equipment_from_stockpile':
                scope.values['num_equipment@support_equipment'] -= self.temp['equipment_stockpile_removal_amount']
                continue
            if key == 'add_political_power': scope.values['political_power'] += self.value(value, scope); continue
            if key.endswith('_variable'):
                target = self.temp if '_temp_' in key else scope.values
                if key.startswith('round_'):
                    target[value] = int(self.value(value, scope) + 0.5)
                elif key.startswith('clamp_'):
                    args = {k: v for k, _, v in value}; var = args['var']
                    target[var] = max(self.value(args.get('min', '-1000000000'), scope), min(target.get(var, 0), self.value(args.get('max', '1000000000'), scope)))
                else:
                    var, _, token = value[0]; number = self.value(token, scope)
                    if isinstance(number, str): number = 0
                    previous_value = self.value(var, scope)
                    if isinstance(previous_value, str): previous_value = 0
                    if key.startswith('set_'): updated = number
                    elif key.startswith('add_to_'): updated = previous_value + number
                    elif key.startswith('subtract_from_'): updated = previous_value - number
                    elif key.startswith('multiply_'): updated = previous_value * number
                    else: raise ValueError(key)
                    if '^' in var and target is scope.values:
                        array, index = var.split('^', 1)
                        target[array][int(self.value(index, scope))] = updated
                    else: target[var] = updated
                continue
            raise ValueError(f'Unsupported effect {key}')

results = []
def authority(tag, gate, **kwargs):
    # War, government and the course of the war open each authority; no calendar date does.
    country = Scope(tag, **kwargs)
    vm = VM(country)
    assert vm.check(triggers[gate], country)
    country.war = False
    assert not vm.check(triggers[gate], country)
    country.war = True
    # The Raj follows its overlord's government; every other authority follows its own.
    changed = vm.countries['ENG'] if tag == 'RAJ' else country
    changed.government = 'communism'
    assert not vm.check(triggers[gate], country)
    results.append({'scenario': gate, 'opens_with': 'war and government', 'passed': True})

authority('ENG', 'camp_administration_civil_british_authority')
authority('USA', 'camp_administration_civil_usa_authority')
authority('RAJ', 'camp_administration_civil_raj_authority', subject='ENG')
authority('ITA', 'camp_administration_civil_italian_authority', government='fascism')
for category, _, entries in load('common/script_constants/camp_repression_rework_constants.txt'):
    if category in ('camp_rework_burden', 'camp_rework_country_value', 'camp_rework_threshold', 'camp_rework_cost', 'camp_rework_equipment_cost', 'camp_rework_colonial'):
        for key, _, value in entries:
            if isinstance(value, str):
                try: constants[f'{category}.{key}'] = float(value)
                except ValueError: pass
effects.update({key: value for key, _, value in load('common/scripted_effects/camp_repression_rework_effects.txt')
                if key == 'camp_rework_recalculate_burdens'})
usa = Scope('USA', flags={'camp_rework_usa_authority_terminated'}); vm = VM(usa); assert not vm.check(triggers['camp_administration_civil_usa_authority'], usa)
raj = Scope('RAJ'); vm = VM(raj); assert not vm.check(triggers['camp_administration_civil_raj_authority'], raj)
results.append({'scenario': 'USA_end_authority_and_RAJ_independence', 'passed': True})
france = Scope('FRA'); vm = VM(france)
assert not vm.check(triggers['camp_administration_civil_french_refugee_authority'], france)
vm.globals.add('nationalist_victory'); assert vm.check(triggers['camp_administration_civil_french_refugee_authority'], france)
france.values['capitulated'] = True; assert not vm.check(triggers['camp_administration_civil_french_refugee_authority'], france)
france.values['capitulated'] = False
france.government = 'neutrality'; france.cosmetic = 'FRA_VICHY'; assert vm.check(triggers['camp_administration_civil_french_collaboration'], france)
france.cosmetic = 'FRA_FREE'; assert not vm.check(triggers['camp_administration_civil_french_collaboration'], france)
results.append({'scenario': 'French_refugee_Vichy_Free_France_distinction', 'passed': True})
usa = Scope('USA', values={'camp_admin_civil_admitted_k': 120}, flags={'camp_rework_usa_authority_terminated', 'camp_admin_civil_review_complete'})
vm = VM(usa); assert not vm.check(triggers['camp_administration_civil_action_two_visible'], usa)
usa.war = False; assert vm.check(triggers['camp_administration_civil_action_two_visible'], usa)
usa.government = 'fascism'; assert not vm.check(triggers['camp_administration_civil_action_two_visible'], usa)
results.append({'scenario': 'property_claims_open_after_authority_ends_and_war_over', 'passed': True})
early_usa = Scope('USA'); vm = VM(early_usa)
assert not vm.check(triggers['camp_administration_civil_action_two_visible'], early_usa)
early_usa.values['camp_admin_civil_admitted_k'] = 120
assert vm.check(triggers['camp_administration_civil_action_two_visible'], early_usa)
results.append({'scenario': 'usa_review_needs_a_detained_cohort_or_relocation_authority', 'passed': True})

country = Scope('ENG'); vm = VM(country)
site = Scope(controller=country, values={'camp_admin_responsible_country': country, 'state_population_k': 100,
    'building_level@concentration_camp': 1, 'building_level@gulag_labor_camp_network': 0,
    'building_level@extermination_camp': 0, 'camp_admin_detainees_k': 0}, flags={'camp_admin_initialized','camp_rework_site_active'})
total = 0
for _ in range(12):
    vm.temp.update(camp_admin_admission_requested_k=2, camp_admin_admission_source_k=max(0,10-total), camp_admin_admission_proven=1)
    vm.run(effects['camp_admin_admit_detainees'],site)
    total += vm.temp['camp_admin_admission_accepted_k']
assert total == 10 and site.values['state_population_k'] == 100
results.append({'scenario':'twelve_month_finite_local_cohort','admitted_k':total,'population_k':site.values['state_population_k'],'passed':True})
site.controller = Scope('GER','fascism'); vm.temp.update(camp_admin_admission_requested_k=2,camp_admin_admission_source_k=10,camp_admin_admission_proven=1)
vm.run(effects['camp_admin_admit_detainees'],site); assert vm.temp['camp_admin_admission_accepted_k'] == 0
results.append({'scenario':'capture_prevents_admission','passed':True})
site.controller = Scope('COG', subject='ENG')
vm.temp.update(camp_admin_admission_requested_k=2,camp_admin_admission_source_k=2,camp_admin_admission_proven=1)
vm.run(effects['camp_admin_admit_detainees'],site)
assert vm.temp['camp_admin_admission_accepted_k'] == 0
results.append({'scenario':'unapproved_subject_control_rejected','passed':True})
site.controller = Scope('RAJ', subject='ENG')
site.flags.add('camp_admin_subject_authority')
vm.temp.update(camp_admin_admission_requested_k=2,camp_admin_admission_source_k=2,camp_admin_admission_proven=1)
vm.run(effects['camp_admin_admit_detainees'],site)
assert vm.temp['camp_admin_admission_accepted_k'] == 2
results.append({'scenario':'legitimate_subject_control','passed':True})
site.values['camp_admin_total_deaths_k'] = 3
before_population = site.values['state_population_k']
vm.run(effects['camp_admin_release_survivors'],site)
assert site.values['camp_admin_detainees_k'] == 0 and site.values['camp_admin_total_released_k'] == 12
assert site.values['camp_admin_total_deaths_k'] == 3 and site.values['state_population_k'] == before_population
vm.run(effects['camp_admin_release_survivors'],site)
assert site.values['camp_admin_total_released_k'] == 12
results.append({'scenario':'survivor_release_idempotent_no_population_or_death_reversal','passed':True})
integration_source = (ROOT_DIR / 'common/scripted_effects/camp_administration_integration_effects.txt').read_text(encoding='utf-8-sig')
terminal_close = integration_source.split('camp_admin_integration_close_country = {', 1)[1].split('# State scope, literal history-kind constant.', 1)[0]
assert 'camp_rework_usa_cancel_security_sunset = yes' in terminal_close
colonial_source = (ROOT_DIR / 'common/scripted_effects/camp_repression_colonial_country_effects.txt').read_text(encoding='utf-8-sig')
usa_cancel = colonial_source.split('camp_rework_usa_cancel_security_sunset = {', 1)[1].split('# -----', 1)[0]
assert 'clr_country_flag = camp_rework_usa_authority_active' in usa_cancel
assert 'clr_country_flag = camp_rework_democratic_emergency_authorized' in usa_cancel
civil_source = (ROOT_DIR / 'common/scripted_effects/camp_administration_civil_effects.txt').read_text(encoding='utf-8-sig')
assert civil_source.count('camp_rework_usa_cancel_security_sunset = yes') == 2
rework_source = (ROOT_DIR / 'common/scripted_effects/camp_repression_rework_effects.txt').read_text(encoding='utf-8-sig')
assert 'camp_admin_integration_close_country = yes' in rework_source.split('camp_rework_exclude_special_country = {', 1)[1][:1500]
assert 'camp_admin_integration_close_country = yes' in rework_source.split('camp_rework_on_country_annexed = {', 1)[1]
results.append({'scenario':'usa_terminal_cleanup_clears_authority_flags','passed':True})
country.flags.add('camp_admin_civil_policy_authorized')
country.values.update(camp_admin_civil_intake_ceiling_k=27,camp_admin_civil_admitted_k=26.5)
site.controller = country
site.flags.add('camp_admin_civil_host_membership_declared')
site.values.update(cores=['ENG'],camp_admin_civil_host_remaining_k=10)
vm.run(effects['camp_administration_civil_admit_host_cohort'],site)
assert country.values['camp_admin_civil_admitted_k'] == 27
assert site.values['camp_admin_detainees_k'] == 0.5 and site.values['camp_admin_civil_host_remaining_k'] == 9.5
vm.run(effects['camp_admin_release_survivors'],site)
vm.run(effects['camp_administration_civil_admit_host_cohort'],site)
assert country.values['camp_admin_civil_admitted_k'] == 27 and site.values['camp_admin_detainees_k'] == 0
results.append({'scenario':'national_ceiling_survives_release_and_reentry','passed':True})

for label,stock,pp,budget_s,budget_pp,expected in [('reserves',100,20,150,15,0),('exact_payment',110,25,150,15,1),('exhausted_ceiling',1000,100,0,0,0)]:
    payer = Scope('USA', values={'num_equipment@support_equipment':stock,'political_power':pp,'camp_admin_budget_support_remaining':budget_s,'camp_admin_budget_pp_remaining':budget_pp})
    vm = VM(payer); vm.run(effects['camp_administration_civil_quote_policy'],payer); vm.run(effects['camp_admin_try_pay_project'],payer)
    assert vm.temp['camp_admin_payment_accepted'] == expected
    assert payer.values['num_equipment@support_equipment'] >= 100 and payer.values['political_power'] >= 20
    results.append({'scenario':label,'paid':expected,'passed':True})

for label,ai,paused,pp,initial,wanted,expected in [
    ('AI_paid_budget_command',True,False,100,1,2,2),
    ('AI_unaffordable_budget_command',True,False,0,1,2,1),
    ('human_budget_preserved',False,False,100,1,2,1),
    ('development_pause_preserves_budget',True,True,100,1,2,1),
    ('same_budget_no_second_debit',True,False,100,2,2,2),
]:
    country=Scope('ENG',values={'is_ai':ai,'political_power':pp,'camp_admin_budget':initial,'camp_active_site_count':0,'camp_admin_budget_support_remaining':17,'camp_admin_budget_pp_remaining':3})
    country.flags.add('camp_admin_initialized')
    if paused: country.flags.add('camp_admin_development_paused')
    vm=VM(country);vm.temp['camp_admin_control_requested']=wanted
    vm.run(effects['camp_administration_civil_choose_ai_budget'],country)
    assert country.values['camp_admin_budget']==expected
    expected_debit=constants['camp_admin_command.policy_pp'] if expected!=initial else 0
    assert country.values['political_power']==pp-expected_debit
    assert country.values['camp_admin_budget_support_remaining']==17 and country.values['camp_admin_budget_pp_remaining']==3
    results.append({'scenario':label,'budget':expected,'pp_debit':expected_debit,'allowance_unchanged':True,'passed':True})

def outer_limit(name):
    outer=[v for k,_,v in effects[name] if k=='if'][0]
    return [v for k,_,v in outer if k=='limit'][0]
actor=Scope('ENG');wrong_root=Scope('GER','fascism');vm=VM(wrong_root)
vm.temp['camp_admin_month_key']=100
assert not vm.check(outer_limit('camp_administration_civil_prepare_monthly'),actor)
assert not vm.check(outer_limit('camp_administration_civil_monthly'),actor)
vm.root=actor
assert vm.check(outer_limit('camp_administration_civil_prepare_monthly'),actor)
assert vm.check(outer_limit('camp_administration_civil_monthly'),actor)
results.append({'scenario':'monthly_requires_recipient_country_root','passed':True})

monthly_body=[v for k,_,v in effects['camp_administration_civil_monthly'] if k=='if'][0]
for stage in ('review','claims'):
    flag=f'camp_admin_civil_{stage}_active'
    marker=('camp_administration_civil_review_ready','=','yes') if stage=='review' else ('has_country_flag','=',flag)
    branch=next(v for k,_,v in monthly_body if k=='if' and marker in dict((a,c) for a,_,c in v).get('limit',[]))
    country=Scope('USA',war=False,values={'political_power':100,'num_equipment@support_equipment':1000,'camp_admin_budget_support_remaining':100,'camp_admin_budget_pp_remaining':50},flags={flag,'camp_admin_development_paused','camp_rework_usa_authority_terminated'})
    vm=VM(country,'1948.7.2');vm.run([('if','=',branch)],country)
    assert country.values[f'camp_admin_civil_{stage}_progress']==1
    results.append({'scenario':f'committed_{stage}_continues_during_development_pause','passed':True})

prepare_body=[v for k,_,v in effects['camp_administration_civil_prepare_monthly'] if k=='if'][0]
intake_branch=next(v for k,_,v in prepare_body if k=='if' and ('camp_administration_civil_open_next_host','=','yes') in v)
intake_limit=dict((k,v) for k,_,v in intake_branch)['limit']
country=Scope('ENG',flags={'camp_admin_civil_policy_funded','camp_admin_development_paused'})
vm=VM(country)
assert not vm.check(intake_limit,country)
country.flags.remove('camp_admin_development_paused')
assert vm.check(intake_limit,country)
results.append({'scenario':'development_pause_blocks_expansion_only','passed':True})

output = {'evidence_kind':'restricted current-source evaluator; no HOI4 runtime; GUI refresh/history fixture only', 'scenarios':results}
Path(__file__).with_name('civil_scenario_results.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
