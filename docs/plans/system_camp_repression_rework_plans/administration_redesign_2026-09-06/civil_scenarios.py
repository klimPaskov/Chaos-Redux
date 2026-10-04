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
for filename in ('camp_administration_constants.txt', 'camp_administration_civil_constants.txt', 'camp_administration_ui_constants.txt'):
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
def authority(tag, gate, before, after, **kwargs):
    country = Scope(tag, **kwargs)
    vm = VM(country, before)
    assert not vm.check(triggers[gate], country)
    vm.date = after
    assert vm.check(triggers[gate], country)
    country.war = False
    if tag in ('ENG', 'USA', 'RAJ', 'ITA'): assert not vm.check(triggers[gate], country)
    results.append({'scenario': gate, 'before': before, 'after': after, 'passed': True})

authority('ENG', 'camp_administration_civil_british_authority', '1940.5.15', '1940.5.16')
authority('USA', 'camp_administration_civil_usa_authority', '1942.2.18', '1942.2.19')
authority('RAJ', 'camp_administration_civil_raj_authority', '1939.9.2', '1939.9.3', subject='ENG')
authority('ITA', 'camp_administration_civil_italian_authority', '1940.6.9', '1940.6.10', government='fascism')
for category, _, entries in load('common/script_constants/camp_repression_rework_constants.txt'):
    if category in ('camp_rework_burden', 'camp_rework_country_value', 'camp_rework_threshold', 'camp_rework_cost', 'camp_rework_equipment_cost', 'camp_rework_colonial'):
        for key, _, value in entries:
            if isinstance(value, str):
                try: constants[f'{category}.{key}'] = float(value)
                except ValueError: pass
effects.update({key: value for key, _, value in load('common/scripted_effects/camp_repression_rework_effects.txt')
                if key == 'camp_rework_recalculate_burdens'})
italy_guard = Scope('ITA', 'fascism', values={'camp_active_site_count':3, 'camp_radicalized_site_count':0,
    'camp_overstretch':0, 'camp_contaminated_site_count':0, 'camp_active_site_states':[]})
italy_vm = VM(italy_guard, '1942.5.1')
italy_vm.run(effects['camp_rework_recalculate_burdens'], italy_guard)
base_guard = italy_guard.values['camp_guard_burden']
italy_guard.flags.add('camp_rework_italy_security_battalions_active')
italy_vm.run(effects['camp_rework_recalculate_burdens'], italy_guard)
active_guard = italy_guard.values['camp_guard_burden']
italy_vm.run(effects['camp_rework_recalculate_burdens'], italy_guard)
assert italy_guard.values['camp_guard_burden'] == active_guard
italy_guard.flags.add('camp_admin_civil_initialized')
italy_vm.run(effects['camp_rework_recalculate_burdens'], italy_guard)
assert italy_guard.values['camp_guard_burden'] == base_guard
italy_guard.flags.remove('camp_admin_civil_initialized')
italy_guard.flags.remove('camp_rework_italy_security_battalions_active')
italy_vm.run(effects['camp_rework_recalculate_burdens'], italy_guard)
assert italy_guard.values['camp_guard_burden'] == base_guard
assert active_guard == base_guard + constants['camp_rework_country_value.overstretch_minor']
results.append({'scenario':'italian_security_guard_burden_survives_recalculation_without_stacking',
    'baseline':base_guard,'active':active_guard,'after_cutover':base_guard,'passed':True})

security_triggers = {key: value for key, _, value in load('common/scripted_triggers/camp_repression_rework_triggers.txt')}
triggers['is_italy_libya_repression_pool_state'] = security_triggers['is_italy_libya_repression_pool_state']
security_ready = security_triggers['camp_rework_italy_security_battalions_resources_ready']
security_stock = Scope('ITA', 'fascism', values={
    'manpower':constants['camp_rework_cost.guard_manpower'],
    'equipment':{
        'infantry_equipment':constants['camp_rework_equipment_cost.infantry_equipment'],
        'support_equipment_1':constants['camp_rework_equipment_cost.support_equipment'],
    },
})
security_vm = VM(security_stock)
assert security_vm.check(security_ready, security_stock)
for stock, key in (('manpower', None), ('equipment', 'infantry_equipment'), ('equipment', 'support_equipment_1')):
    if key is None:
        security_stock.values[stock] -= 1
        assert not security_vm.check(security_ready, security_stock)
        security_stock.values[stock] += 1
    else:
        security_stock.values[stock][key] -= 1
        assert not security_vm.check(security_ready, security_stock)
        security_stock.values[stock][key] += 1
results.append({'scenario':'italian_security_exact_manpower_and_equipment_quote_is_affordable',
    'quote_manpower':security_stock.values['manpower'], 'passed':True})
triggers['camp_rework_italy_security_battalions_site_ready'] = security_triggers['camp_rework_italy_security_battalions_site_ready']
triggers['is_valid_camp_active_site_state'] = []  # Registered active camp fixture; region and responsibility are source checks.
italy_actor = Scope('ITA', 'fascism')
site = Scope('LIB', controller=italy_actor, values={'cores':['LBA'], 'genocide_responsible_country':italy_actor})
site_vm = VM(italy_actor)
assert site_vm.check(triggers['camp_rework_italy_security_battalions_site_ready'], site)
site.values['cores'] = ['ETH']
assert not site_vm.check(triggers['camp_rework_italy_security_battalions_site_ready'], site)
site.values['cores'] = ['LBA']
site.controller = Scope('GER')
assert not site_vm.check(triggers['camp_rework_italy_security_battalions_site_ready'], site)
site.controller = italy_actor
site.values['cores'].append('ITA')
assert not site_vm.check(triggers['camp_rework_italy_security_battalions_site_ready'], site)
results.append({'scenario':'italian_security_site_requires_responsible_direct_control_and_libyan_noncore_state','passed':True})

# Execute the production success effect and the Italy bridge's actual
# local-to-national pressure comparison. A successful paid repeat must give
# real relief when pressures are equal, while preserving evidence and floors.
colonial_effects = {key: value for key, _, value in load('common/scripted_effects/camp_repression_colonial_country_effects.txt')}
effects['camp_rework_complete_italy_security_sweep'] = colonial_effects['camp_rework_complete_italy_security_sweep']
effects['camp_rework_italy_clear_security_sweep_state'] = []  # Local modifier lifecycle has a separate source test.
def italy_branch(entries):
    for key, _, value in entries:
        limit = next((sub for subkey, _, sub in value if subkey == 'limit'), []) if isinstance(value, list) else []
        if key == 'else_if' and any(k == 'original_tag' and v == 'ITA' for k, _, v in limit):
            return value
        if isinstance(value, list):
            found = italy_branch(value)
            if found is not None: return found
    return None
italy_bridge = italy_branch(colonial_effects['camp_rework_update_colonial_country_monthly_bridge'])
assert italy_bridge is not None
pressure_bridge = next(value for key, _, value in italy_bridge if key == 'if' and 'libyan_resistance_pressure' in str(value) and 'camp_policy_resistance_pressure' in str(value))
effects['camp_rework_update_colonial_country_monthly_bridge'] = [('if', '=', pressure_bridge)]
triggers['camp_rework_italy_security_sweep_requirements_met'] = []  # Valid supplied garrison fixture.
for policy_before, local_before, policy_after, local_after in ((12, 12, 9, 9), (1, 1, 0, 0), (15, 10, 10, 7)):
    italy = Scope('ITA', 'fascism', values={'camp_policy_resistance_pressure':policy_before,
        'libyan_resistance_pressure':local_before, 'camp_policy_evidence':0, 'ita_security_sweep_state_id':1})
    vm = VM(italy, '1942.5.1')
    vm.run(effects['camp_rework_complete_italy_security_sweep'], italy)
    assert italy.values['camp_policy_resistance_pressure'] == policy_after
    assert italy.values['libyan_resistance_pressure'] == local_after
    assert italy.values['camp_policy_evidence'] == constants['camp_rework_country_value.evidence_minor']
    assert 'ita_security_sweep_state_id' not in italy.values
results.append({'scenario':'italian_successful_security_sweep_reduces_local_and_reconciled_policy_pressure_without_negative_stock',
    'equal_pressure_after':9,'floor_after':0,'high_policy_after':10,'passed':True})

# The failure branch may physically harm a site only while Italy still has
# direct control and remains the recorded responsible authority.
triggers['camp_rework_italy_security_sweep_requirements_met'] = [('has_country_flag', '=', 'mock_success')]
effects['camp_rework_colonial_apply_major_harm_to_current_state'] = [('add_to_variable', '=', [('mock_harm', '=', '1')])]
for direct, libya, expected_harm in ((True, True, 1), (False, True, 0), (True, False, 0)):
    italy = Scope('ITA', 'fascism', values={'libyan_resistance_pressure':5, 'camp_policy_evidence':0,
        'camp_policy_resistance_pressure':5})
    site = Scope('LIB', controller=italy if direct else Scope('GER'), values={'genocide_responsible_country':italy, 'cores':['LBA'] if libya else ['ETH']})
    italy.values['ita_security_sweep_state_id'] = site
    vm = VM(italy, '1942.5.1')
    vm.run(effects['camp_rework_complete_italy_security_sweep'], italy)
    assert site.values.get('mock_harm', 0) == expected_harm
    assert italy.values['camp_policy_evidence'] == constants['camp_rework_country_value.evidence_major']
    assert 'ita_security_sweep_state_id' not in italy.values
results.append({'scenario':'italian_failed_security_sweep_harms_site_only_under_direct_responsible_control',
    'direct_libyan_site_harm':1,'captured_site_harm':0,'non_libyan_site_harm':0,'passed':True})
usa = Scope('USA'); vm = VM(usa, '1944.12.18'); assert not vm.check(triggers['camp_administration_civil_usa_authority'], usa)
raj = Scope('RAJ'); vm = VM(raj); assert not vm.check(triggers['camp_administration_civil_raj_authority'], raj)
results.append({'scenario': 'USA_end_authority_and_RAJ_independence', 'passed': True})
france=Scope('FRA');vm=VM(france,'1939.2.1');assert vm.check(triggers['camp_administration_civil_french_refugee_authority'],france)
vm.date='1940.7.10';assert not vm.check(triggers['camp_administration_civil_french_refugee_authority'],france)
france.government='neutrality';france.cosmetic='FRA_VICHY';assert vm.check(triggers['camp_administration_civil_french_collaboration'],france)
france.cosmetic='FRA_FREE';assert not vm.check(triggers['camp_administration_civil_french_collaboration'],france)
results.append({'scenario':'French_refugee_Vichy_Free_France_distinction','passed':True})
usa=Scope('USA',values={'camp_admin_civil_admitted_k':120},flags={'camp_rework_usa_authority_terminated','camp_admin_civil_review_complete'})
vm=VM(usa,'1948.7.1');assert not vm.check(triggers['camp_administration_civil_action_two_visible'],usa)
vm.date='1948.7.2';assert vm.check(triggers['camp_administration_civil_action_two_visible'],usa)
usa.government='fascism';assert not vm.check(triggers['camp_administration_civil_action_two_visible'],usa)
results.append({'scenario':'property_claims_date_and_government','passed':True})
early_usa=Scope('USA',values={'camp_admin_civil_admitted_k':120})
vm=VM(early_usa,'1942.2.18');assert not vm.check(triggers['camp_administration_civil_action_two_visible'],early_usa)
vm.date='1942.2.19';assert vm.check(triggers['camp_administration_civil_action_two_visible'],early_usa)
results.append({'scenario':'usa_review_cannot_terminate_authority_before_historical_start','passed':True})

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
country.values['ita_desert_road_project_state_id'] = 1
vm.run(effects['camp_administration_civil_cancel_routine_projects'],country)
decision_ids = {key for _, _, content in load('common/decisions/camp_repression_colonial_country_decisions.txt') if isinstance(content,list) for key,_,_ in content}
assert set(country.values['removed_missions']) <= decision_ids
assert 'ita_desert_road_project_state_id' not in country.values
results.append({'scenario':'terminal_cancel_ids_and_target_cleanup','passed':True})
integration_source = (ROOT_DIR / 'common/scripted_effects/camp_administration_integration_effects.txt').read_text(encoding='utf-8-sig')
terminal_close = integration_source.split('camp_admin_integration_close_country = {', 1)[1].split('# State scope, literal history-kind constant.', 1)[0]
for mission in ('usa_court_review_period', 'usa_redress_commission_work'):
    assert f'has_active_mission = {mission}' in terminal_close
    assert f'remove_mission = {mission}' in terminal_close
assert 'camp_rework_usa_cancel_security_sunset = yes' in terminal_close
colonial_source = (ROOT_DIR / 'common/scripted_effects/camp_repression_colonial_country_effects.txt').read_text(encoding='utf-8-sig')
usa_cancel = colonial_source.split('camp_rework_usa_cancel_security_sunset = {', 1)[1].split('camp_rework_usa_begin_relocation_termination = {', 1)[0]
assert 'has_active_mission = usa_security_authority_sunset' in usa_cancel
assert 'remove_mission = usa_security_authority_sunset' in usa_cancel
assert 'clr_country_flag = camp_rework_usa_authority_active' in usa_cancel
assert 'clr_country_flag = camp_rework_democratic_emergency_authorized' in usa_cancel
civil_source = (ROOT_DIR / 'common/scripted_effects/camp_administration_civil_effects.txt').read_text(encoding='utf-8-sig')
assert civil_source.count('camp_rework_usa_cancel_security_sunset = yes') == 2
usa_sunset_decision = (ROOT_DIR / 'common/decisions/camp_repression_colonial_country_decisions.txt').read_text(encoding='utf-8-sig').split('usa_security_authority_sunset = {', 1)[1].split('usa_redress_commission_work = {', 1)[0]
assert 'cancel_trigger = {' in usa_sunset_decision and 'NOT = { has_country_flag = camp_rework_usa_authority_active }' in usa_sunset_decision
usa_timeout = colonial_source.split('camp_rework_complete_usa_security_sunset = {', 1)[1].split('camp_rework_complete_usa_redress_commission = {', 1)[0]
assert 'has_country_flag = camp_rework_usa_authority_active' in usa_timeout
assert 'NOT = { has_country_flag = camp_admin_civil_review_active }' in usa_timeout
rework_source = (ROOT_DIR / 'common/scripted_effects/camp_repression_rework_effects.txt').read_text(encoding='utf-8-sig')
assert 'camp_admin_integration_close_country = yes' in rework_source.split('camp_rework_exclude_special_country = {', 1)[1][:1500]
assert 'camp_admin_integration_close_country = yes' in rework_source.split('camp_rework_on_country_annexed = {', 1)[1]
results.append({'scenario':'usa_terminal_missions_removed_without_timeout_effects','passed':True})
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
    branch=next(v for k,_,v in monthly_body if k=='if' and ('has_country_flag','=',flag) in dict((a,c) for a,_,c in v).get('limit',[]))
    country=Scope('USA',values={'political_power':100,'num_equipment@support_equipment':1000,'camp_admin_budget_support_remaining':100,'camp_admin_budget_pp_remaining':50},flags={flag,'camp_admin_development_paused','camp_rework_usa_authority_terminated'})
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
