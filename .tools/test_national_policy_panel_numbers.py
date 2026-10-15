"""Regression checks for national policy panel number presentation.

Usage from the repo root: python .tools/test_national_policy_panel_numbers.py.
An absolute script path also works from any directory.
Inputs: production number getters, unit constants and their English localisation.
Output: stdout JSON containing resolved thresholds and named scenario results.
Runner is also importable by preview fixtures. No temporary directory is required.

This bounded source evaluator reuses the repository's Clausewitz parser and
executes only the formatter's declared command subset, failing on unknown
commands. It checks units, source selection, rounding, registry iteration and
absence of persistent writes. Temporary arrays and all_of_scopes follow the
documented scope-array iteration and first-false behavior. Native engine callbacks,
rendering and fixed-point limits are not
emulated, and predicate fixtures are explicit assumptions rather than live QA.
"""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import importlib.util, sys, json, re, hashlib, copy

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('number_parser',ROOT/'.tools/test_event035_center_projects.py')
P=importlib.util.module_from_spec(spec);sys.modules[spec.name]=P;spec.loader.exec_module(P)
def parse(path):
    return P.parse_nodes(P.lex(P.uncomment(path.read_text(encoding='utf-8-sig'))),0,str(path))[0]
nodes=parse(ROOT/'common/scripted_localisation/national_policy_panel_numbers.txt')
defs={P.first(n.value,'name'):n.value for n in nodes}
constants={}
for file in ('national_policy_panel_number_constants.txt', 'camp_administration_constants.txt'):
    for group in parse(ROOT/'common/script_constants'/file):
        for n in group.value:
            if isinstance(n.value,str) and P.NUMBER.fullmatch(n.value):
                constants['constant:'+group.key+'.'+n.key]=Decimal(n.value)
loc={}
for path in (ROOT/'localisation/english/camp_administration_ui_l_english.yml', ROOT/'localisation/english/humanitarian_panel_values_l_english.yml'):
    loc.update(dict(re.findall(r'^([^:#\s]+): "(.*)"$',path.read_text(encoding='utf-8-sig'),re.M)))
def first(ns,key,default=None):return next((n.value for n in ns if n.key==key),default)
class Runner:
    def __init__(self,country=None,states=None):self.country=country or {};self.states=states or {};self.temp={};self.temp_arrays={};self.trace=[]
    def scope_reference(self,scope):
        return next(state_id for state_id,state in self.states.items() if state is scope)
    def array(self,name,scope):
        return self.temp_arrays[name] if name in self.temp_arrays else scope.get(name,[])
    def value(self,token,scope):
        if token in constants:return constants[token]
        if token in self.temp:return self.temp[token]
        try:return Decimal(token)
        except:return Decimal(str(scope.get(token,0)))
    def trigger(self,ns,scope):
        for n in ns:
            key=n.key
            if key=='NOT':
                if self.trigger(n.value,scope):return False
            elif key=='if':
                assert all(x.key!='else' for x in n.value),'else is outside this evaluator subset'
                if self.trigger(first(n.value,'limit',[]),scope):
                    if not self.trigger([x for x in n.value if x.key!='limit'],scope):return False
            elif key=='all_of_scopes':
                for state_id in list(self.array(first(n.value,'array'),scope)):
                    assert state_id in self.states,('missing array scope fixture',state_id)
                    if not self.trigger([x for x in n.value if x.key!='array'],self.states[state_id]):return False
            elif key=='clear_temp_array':self.temp_arrays[n.value]=[]
            elif key=='add_to_temp_array':
                assert first(n.value,'value')=='THIS','only scope-pointer appends are modeled'
                self.temp_arrays.setdefault(first(n.value,'array'),[]).append(self.scope_reference(scope))
            elif key=='is_in_array':
                assert first(n.value,'value')=='THIS','only scope-pointer membership is modeled'
                if self.scope_reference(scope) not in self.array(first(n.value,'array'),scope):return False
            elif key=='has_state_flag':
                if n.value not in scope.get('flags',[]):return False
            elif key.startswith('var:'):
                state_id=int(scope.get(key[4:],0))
                if state_id not in self.states or not self.trigger(n.value,self.states[state_id]):return False
            elif key=='has_variable':
                if n.value not in scope:return False
            elif key=='check_variable':
                if len(n.value)==1:
                    x=n.value[0];a=self.value(x.key,scope);b=self.value(x.value,scope);op=x.op
                else:
                    a=self.value(first(n.value,'var'),scope);b=self.value(first(n.value,'value'),scope);op=first(n.value,'compare')
                if not {'=':a==b,'>':a>b,'<':a<b,'equals':a==b,'greater_than_or_equals':a>=b}.get(op,False):return False
            elif key=='round_temp_variable':self.temp[n.value]=self.value(n.value,scope).quantize(Decimal(1),rounding=ROUND_HALF_UP)
            elif key in ('set_temp_variable','add_to_temp_variable','multiply_temp_variable','divide_temp_variable'):
                x=n.value[0];b=self.value(x.value,scope);a=self.temp.get(x.key,Decimal(0))
                if key=='set_temp_variable':self.temp[x.key]=b
                elif key=='add_to_temp_variable':self.temp[x.key]=a+b
                elif key=='multiply_temp_variable':self.temp[x.key]=a*b
                else:self.temp[x.key]=a/b
            elif key in ('migration_reception_capacity_is_valid','camp_admin_gui_site_has_current_output','migration_state_has_header_trapped_people'):
                if not scope.get('fixture:'+key,False):return False
            else:raise AssertionError(('unhandled command',key))
        return True
    def getter(self,name,scope=None):
        scope=self.country if scope is None else scope
        self.trace.append(name)
        for n in defs[name]:
            if n.key=='text' and self.trigger(first(n.value,'trigger',[]),scope):return self.localize(first(n.value,'localization_key'),scope)
        raise AssertionError(name)
    def localize(self,key,scope=None):
        scope=self.country if scope is None else scope
        def sub(m):
            token=m.group(1)
            if token.startswith('?'):
                var,fmt=token[1:].split('|');return format(self.value(var,scope),'.'+fmt+'f')
            return self.getter(token.removeprefix('This.'),scope)
        return re.sub(r'\[([^\]]+)\]',sub,loc[key])

if __name__=='__main__':
    checks=[]
    # All threshold checks execute parsed branches, constants, precision helper and real YML.
    for people,want in [(0,'0'),(74,'74'),(999,'999'),(1000,'1K'),(1240,'1.2K'),(10000,'10K'),(998000,'998K'),(1000000,'1M'),(1240000,'1.2M'),(1000000000,'1B'),(1240000000,'1.2B'),(2000000000,'2B')]:
        r=Runner({'camp_admin_total_detainees_k':777,'camp_active_site_states':[1]}, {1:{'camp_admin_detainees_k':Decimal(people)/1000}});got=r.getter('GetCampAdminNumberDetainees');assert got==want,(people,got,want);checks.append({'people':people,'source_k':str(Decimal(people)/1000),'display':got})
    for people,want in [(74,'74'),(999,'999'),(1000,'1K'),(1240,'1.2K'),(1000000,'1M')]:
        assert Runner({'migration_panel_fleeing':people}).getter('GetMigrationPanelNumberFleeing')==want
    r=Runner({'camp_selected_state_id':64,'camp_admin_gui_site_detainees_k':999,'camp_admin_gui_site_month_deaths_people':999999},{64:{'camp_admin_detainees_k':1.24,'camp_admin_month_deaths_k':0.074}})
    assert r.getter('GetCampAdminNumberSelectedDetainees')=='1.2K'
    assert r.getter('GetCampAdminNumberSelectedMonthDeaths')=='74'
    r.states[64]['camp_admin_detainees_k']=1000
    assert r.getter('GetCampAdminNumberSelectedDetainees')=='1M'
    r=Runner({'migration_panel_selected_state':1,'migration_panel_selected_fleeing':999999},{1:{'migration_state_flight_population':1240}})
    assert r.getter('GetMigrationPanelNumberSelectedFleeing')=='1.2K'
    r=Runner({'camp_admin_month_deaths_k':1.1,'camp_occ_month_deaths_k':0.14,'camp_admin_gui_month_deaths_people':888888})
    assert r.localize('camp_admin_deaths_value')=='\u00a7R1.2K\u00a7!'
    r=Runner({'camp_admin_total_deaths_k':1000,'camp_occ_total_deaths_k':240})
    assert r.getter('GetCampAdminNumberTotalDeaths')=='1.2M'
    r=Runner({'camp_selected_state_id':1},{1:{'camp_admin_industry_k':1,'camp_admin_works_k':0.2,'camp_admin_extraction_k':0.04,'fixture:camp_admin_gui_site_has_current_output':True}})
    assert r.getter('GetCampAdminNumberSelectedWorkforce')=='1.2K'
    r.states[1]['fixture:camp_admin_gui_site_has_current_output']=False
    assert r.getter('GetCampAdminNumberSelectedWorkforce')=='0'
    before=copy.deepcopy(r.states);r.getter('GetCampAdminNumberSelectedWorkforce');assert r.states==before
    # Deliberately stale national census. Registries overlap and repeat entries.
    # A closed active-only site is excluded, but a closed civilian site is included.
    r=Runner({'camp_admin_total_detainees_k':777,'camp_admin_total_workforce_k':888,'camp_active_site_states':[1,2,2,4],'camp_admin_civilian_states':[2,3,3]}, {
        1:{'camp_admin_detainees_k':10,'camp_admin_industry_k':1,'camp_admin_works_k':2,'camp_admin_extraction_k':3,'fixture:camp_admin_gui_site_has_current_output':True},
        2:{'camp_admin_detainees_k':20,'camp_admin_industry_k':4,'fixture:camp_admin_gui_site_has_current_output':True},
        3:{'camp_admin_detainees_k':5,'camp_admin_works_k':2,'flags':['camp_admin_closed'],'fixture:camp_admin_gui_site_has_current_output':True},
        4:{'camp_admin_detainees_k':999,'camp_admin_industry_k':999,'flags':['camp_admin_closed'],'fixture:camp_admin_gui_site_has_current_output':True},
    })
    snapshot=copy.deepcopy((r.country,r.states))
    assert r.getter('GetCampAdminNumberDetainees')=='35K'
    assert r.getter('GetCampAdminNumberWorkforce')=='12K'
    assert (r.country,r.states)==snapshot
    r.states[1]['camp_admin_detainees_k']=15 # Admission while paused, census unchanged.
    r.states[1]['camp_admin_industry_k']=2
    assert r.getter('GetCampAdminNumberDetainees')=='40K'
    assert r.getter('GetCampAdminNumberWorkforce')=='13K'
    assert r.country['camp_admin_total_detainees_k']==777
    assert r.country['camp_admin_total_workforce_k']==888
    r.states[2]['fixture:camp_admin_gui_site_has_current_output']=False
    assert r.getter('GetCampAdminNumberWorkforce')=='9K'
    assert r.getter('GetCampAdminNumberDetainees')=='40K'
    assert Runner().getter('GetCampAdminNumberDetainees')=='0'
    assert Runner().getter('GetCampAdminNumberWorkforce')=='0'
    tokens=[n for n in re.findall(r'\[(?:This\.)?(Get(?:NationalPolicyPanelNumber|CampAdminNumber|MigrationPanelNumber)[^\]]*)\]', '\n'.join(loc.values()))]
    assert all(n in defs for n in tokens)
    output={'thresholds':checks,'checks':['Migration unit conversion','selected live counts defeat stale GUI copies','paused selected source change appears on second getter call','national combined monthly/cumulative deaths','workforce gate','registry overlap and repeated entries counted once','closed active site excluded and civilian membership retained','paused admission and assignments defeat stale national census','national workforce current-output gate','empty registries stay zero without initialization','no persistent writes','all new getter tokens resolve'],'source_sha256':hashlib.sha256((ROOT/'common/scripted_localisation/national_policy_panel_numbers.txt').read_bytes()).hexdigest()}
    print(json.dumps(output, separators=(',', ':')))
