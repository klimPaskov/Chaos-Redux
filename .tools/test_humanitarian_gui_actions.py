"""Execute production action dispatch, gates, receipts, payment and callbacks.

Only native engine commands and unrelated presentation/initialization consumers
are fixtures. Documented meta expansion executes the actual replacement text.
This source model does not assert native event scheduling or native UI timers.
"""
from pathlib import Path
import sys,re,importlib.util,unittest
from decimal import Decimal
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools'))
import test_famine_takeover_20261006 as F
P=F._PARSER;Node=F.Node;Definition=F.Definition
TOKEN_SOURCE_FILES=(
    'common/scripted_effects/humanitarian_gui_action_effects.txt',
    'common/scripted_effects/famine_gui_action_effects.txt',
    'common/scripted_effects/migration_gui_action_effects.txt',
    'common/scripted_effects/famine_decision_owner_effects.txt',
    'common/scripted_effects/migration_decision_owner_effects.txt',
    'common/scripted_effects/migration_transport_cost_effects.txt',
    'common/scripted_effects/migration_reception_preparation_effects.txt',
    'common/scripted_triggers/famine_gui_action_triggers.txt',
    'common/scripted_triggers/migration_gui_action_triggers.txt',
    'common/scripted_triggers/famine_decision_owner_triggers.txt',
    'common/scripted_triggers/migration_decision_owner_triggers.txt',
    'common/scripted_triggers/migration_decision_cost_triggers.txt',
    'common/scripted_triggers/migration_priority_triggers.txt',
    'common/scripted_triggers/migration_transport_cost_triggers.txt',
    'common/scripted_triggers/migration_reception_preparation_triggers.txt',
)
def read_defs(path):
    p=ROOT/path;nodes,_=P.parse_nodes(P.lex(P.uncomment(p.read_text(encoding='utf-8-sig'))),0,str(p))
    return {n.key:Definition(n.key,p,n.line,F.adapt_nodes(n.value)) for n in nodes if isinstance(n.value,list)}

class ScriptToken(str):
    """Model the engine's token flag, without inventing numeric token indices."""

def native_token_registry():
    path=ROOT/'common/script_enums.txt'
    tokens=P.lex(P.uncomment(path.read_text(encoding='utf-8-sig')))
    enums={};cursor=0
    while cursor<len(tokens):
        name=tokens[cursor].text
        if not name.startswith('script_enum_') or [x.text for x in tokens[cursor+1:cursor+3]]!=['=','{']:
            raise F.SourceContractError('invalid native script enum header: '+name)
        cursor+=3;members=[]
        while cursor<len(tokens) and tokens[cursor].text!='}':
            member=tokens[cursor].text
            if not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*',member):
                raise F.SourceContractError('invalid bare script enum member: '+member)
            members.append(member);cursor+=1
        if cursor>=len(tokens):raise F.SourceContractError('unclosed native script enum: '+name)
        if name in enums:raise F.SourceContractError('duplicate native script enum: '+name)
        enums[name]=frozenset(members);cursor+=1
    decisions=set()
    for system in ['famine','migration']:
        categories=read_defs('common/decisions/'+system+'_decisions.txt')
        decisions.update(n.key for n in categories[system+'_decision_category'].body if isinstance(n.value,list))
    return enums,frozenset(decisions)

class Runtime(F.FamineRuntime):
    EXTERNAL_EFFECTS=F.FamineRuntime.EXTERNAL_EFFECTS|{'famine_initialize_state','famine_show_report_relief_arrival','famine_refresh_national_food_crisis','famine_refresh_decision_phase_from_country','famine_clear_national_food_crisis','humanitarian_initialize_runtime','humanitarian_project_legacy_cost_quote','migration_project_reception_preparation_cost_quote','migration_panel_refresh','famine_panel_refresh','national_policy_panel_refresh_open','national_policy_panel_begin_update','national_policy_panel_end_update','national_policy_panel_publish_state'}
    EXTERNAL_FIXTURES=EXTERNAL_EFFECTS
    def __init__(self):
        self.enum_tokens,self.decision_tokens=native_token_registry()
        self.registered_tokens=self.decision_tokens|frozenset().union(*self.enum_tokens.values())
        super().__init__()
        files=['humanitarian_gui_action_effects','famine_gui_action_effects','migration_gui_action_effects','famine_decision_owner_effects','migration_decision_owner_effects']
        for name in files:self.effect_defs.update(read_defs('common/scripted_effects/'+name+'.txt'))
        for name in ['famine_gui_action_triggers','migration_gui_action_triggers','famine_decision_owner_triggers','migration_decision_owner_triggers','migration_decision_cost_triggers','humanitarian_legacy_cost_triggers','migration_priority_triggers','migration_pressure_triggers']:
            self.trigger_defs.update(read_defs('common/scripted_triggers/'+name+'.txt'))
        self.effect_defs['chaosx_convert_date_offset_to_days']=F.read_one('common/scripted_effects/chaosx_dynamic_effects.txt','chaosx_convert_date_offset_to_days')
        self.effect_defs['migration_register_active_country']=F.read_one('common/scripted_effects/migration_core_effects.txt','migration_register_active_country')
        self.trigger_defs['famine_to_migration_food_safety_is_valid']=F.read_one('common/scripted_triggers/migration_core_triggers.txt','famine_to_migration_food_safety_is_valid')
        for path in (ROOT/'common/script_constants').glob('*.txt'):
            for group,d in F.read_parseable_definitions(str(path.relative_to(ROOT))).items():
                for n in d.body:
                    if isinstance(n.value,str) and F.NUMBER.fullmatch(n.value):self.constants['constant:'+group+'.'+n.key]=Decimal(n.value)
        raw=P.uncomment((ROOT/'events/humanitarian_action_bridge_events.txt').read_text())
        nodes,_=P.parse_nodes(P.lex(raw),0,'bridge events')
        self.event_bodies={P.first(n.value,'id'):P.first(n.value,'immediate') for n in nodes if n.key=='country_event'}
        self.bridge_visits=[]
        self.panel_refresh_requests=[]
        self.panel_update_depth={}
        self.panel_update_pending=set()
        self.effects=self.effect_defs;self.triggers=self.trigger_defs
    def _value(self,t):
        if isinstance(t,ScriptToken):return t
        if isinstance(t,str) and t.startswith('token:'):
            token=t[6:]
            if token not in self.registered_tokens:raise F.SourceContractError('unregistered native token: '+token)
            return ScriptToken(token)
        if t=='FROM.id':return self.from_scope.id
        return super()._value(t)
    def _path_exists(self,path):
        if any(path in x for x in self.temp_frames):return True
        return super()._path_exists(self._targeted_variable_name(path))
    def _array_value(self,container,path):
        if container is not None:return super()._array_value(container,path)
        name,_,index=path.partition('^');arr=self.global_arrays.get(name,[])
        if index=='num':return len(arr)
        if index:
            i=int(self._value(index));return arr[i] if 0<=i<len(arr) else 0
        return arr
    def _meta(self,node):
        params={}
        for n in node.value:
            if n.key=='text':continue
            m=re.fullmatch(r'"\[\?([\w]+)\.GetTokenKey\]"',n.value)
            if not m:raise F.SourceContractError('unsupported reached meta input '+n.value)
            token=self._value(m[1])
            if not isinstance(token,ScriptToken) or token not in self.registered_tokens:
                raise F.SourceContractError('GetTokenKey requires a registered native token: '+m[1])
            params[n.key]=str(token)
        def expand(nodes):
            def s(t):
                for k,v in params.items():t=t.replace('['+k+']',v)
                return t
            return [Node(s(n.key),n.op,expand(n.value) if isinstance(n.value,list) else s(n.value),n.line) for n in nodes]
        return expand(P.first(node.value,'text'))
    def _condition(self,n,scope):
        if n.key=='humanitarian_corridor_operation_is_valid':return False
        if n.key=='NOT':
            predicates=[]
            for x in n.value:
                if x.key=='set_temp_variable':self._condition(x,scope)
                else:predicates.append(x)
            return not any(self._condition(x,scope) for x in predicates)
        if n.key in self.trigger_defs and isinstance(n.value,list):raise F.SourceContractError('HOI4 helper cannot take named arguments: '+n.key)
        if n.key=='meta_trigger':return self._conditions(self._meta(n),scope)
        if n.key in ['uses_normal_civilian_systems','is_holy_realm_country','is_special_chaos_country']:
            return bool(scope.values.get(n.key,n.key=='uses_normal_civilian_systems'))==(n.value=='yes')
        if n.key=='has_government':return scope.values.get('government','neutrality')==n.value
        if n.key=='num_of_civilian_factories':return scope.resources.get('civilian_factories',0)>self._value(n.value)
        if n.key=='has_equipment' and isinstance(n.value,list):
            c=n.value[0];resource='convoy_1' if c.key=='convoy' else c.key
            return self._compare(scope.resources.get(resource,0),c.op,self._value(c.value))
        if n.key=='always':return n.value=='yes'
        return super()._condition(n,scope)
    def _effects(self,nodes,scope):
        i=0
        while i<len(nodes):
            n=nodes[i]
            if n.key in ['if','else_if','else']:
                j=i+1
                while j<len(nodes) and nodes[j].key in ['else_if','else']:j+=1
                super()._effects(nodes[i:j],scope);i=j;continue
            if n.key in self.effect_defs and isinstance(n.value,list):raise F.SourceContractError('HOI4 helper cannot take named arguments: '+n.key)
            elif n.key=='while_loop_effect':
                count=0
                while self._conditions(P.first(n.value,'limit'),scope):
                    count+=1
                    if count>1000:break
                    self._effects([x for x in n.value if x.key!='limit'],scope)
            elif n.key=='meta_effect':self._effects(self._meta(n),scope)
            elif n.key=='remove_from_array' and P.first(n.value,'value') is not None:
                arr=self._array_values(P.first(n.value,'array'));item=self._value(P.first(n.value,'value'))
                if item in arr:arr.remove(item)
            elif n.key=='set_state_flag' and isinstance(n.value,list):
                flag=P.first(n.value,'flag');days=self._value(P.first(n.value,'days'))
                scope.flags.add(flag);self.timed_flag_writes.append((scope.id,flag,days))
            else:super()._effects([n],scope)
            i+=1
    def _native_effect(self,key,value,scope,line):
        if key=='country_event':
            event_id=P.first(value,'id');previous=(self.root,self.scope_stack,self.temp_frames)
            self.bridge_visits.append((event_id,scope.values.get('humanitarian_action_callback_id')))
            self.root=scope;self.scope_stack=[scope];self.temp_frames=[{}]
            try:self._effects(self.event_bodies[event_id],scope)
            finally:self.root,self.scope_stack,self.temp_frames=previous
            return
        return super()._native_effect(key,value,scope,line)
    def _call_effect(self,name,scope):
        if name in ['migration_panel_refresh','famine_panel_refresh']:
            self.panel_refresh_requests.append((name,scope.id))
        if name=='national_policy_panel_begin_update':
            if scope.kind=='country' and any(flag in scope.flags for flag in ('famine_panel_open','migration_panel_open')):
                key=id(scope);self.panel_update_depth[key]=self.panel_update_depth.get(key,0)+1
            return
        if name=='national_policy_panel_end_update':
            key=id(scope);depth=self.panel_update_depth.get(key,0)
            if depth>0:
                depth-=1
                if depth==0:
                    self.panel_update_depth.pop(key,None)
                    if key in self.panel_update_pending:
                        self.panel_update_pending.discard(key)
                        self._refresh_open_panels(scope)
                else:self.panel_update_depth[key]=depth
            return
        if name=='national_policy_panel_refresh_open':
            if scope.kind=='country' and any(flag in scope.flags for flag in ('famine_panel_open','migration_panel_open')):
                key=id(scope)
                if self.panel_update_depth.get(key,0)>0:self.panel_update_pending.add(key)
                else:self._refresh_open_panels(scope)
            return
        if name=='national_policy_panel_publish_state' and scope.kind=='state':
            if scope.owner is not None:self._call_effect('national_policy_panel_refresh_open',scope.owner)
            if scope.controller is not None and scope.controller is not scope.owner:self._call_effect('national_policy_panel_refresh_open',scope.controller)
            return
        return super()._call_effect(name,scope)
    def _refresh_open_panels(self,scope):
        if 'migration_panel_open' in scope.flags:self._call_effect('migration_panel_refresh',scope)
        if 'famine_panel_open' in scope.flags:self._call_effect('famine_panel_refresh',scope)

def case():
    r=Runtime();a=F.country('FRA');host=F.country('ENG');s=F.state(42,a);s.values['is_in_home_area']=True
    a.resources.update(fuel=100000,infantry_equipment=10000,support_equipment=10000,convoy_1=100,political_power=100)
    a.values.update(owned_states=[s],famine_panel_selected_state=s)
    s.flags.update(['famine_food_security_active','famine_food_stage_famine','famine_food_reserve_initialized'])
    s.values.update(famine_food_pressure=10,famine_food_reserve_amount=1000,famine_food_reserve_daily_need=10)
    r.global_arrays['famine_active_countries']=[]
    return r,a,s,host

def start(r,a,action):r.run_effect('famine_gui_start_action',a,caller_temps={'famine_gui_action':action})
def pulse(r,a,root):r.run_effect('famine_action_process_pending',a,root=root)

class ContractTests(unittest.TestCase):
    def test_owned_meta_and_receipt_tokens_are_native_database_or_enum_members(self):
        r=Runtime();sources={path:P.uncomment((ROOT/path).read_text(encoding='utf-8-sig')) for path in TOKEN_SOURCE_FILES}
        combined='\n'.join(sources.values())
        families=set(re.findall(r'humanitarian_action_system_token\s*=\s*token:(\w+)',combined))
        suffixes=set(re.findall(r'humanitarian_action_suffix_token\s*=\s*token:(\w+)',combined))
        names=set(re.findall(r'humanitarian_action_name_token\s*=\s*token:(\w+)',combined))
        legacy={'migration_open_departure_routes','migration_restrict_departure','migration_close_border'}
        self.assertEqual(families,{'famine','migration'})
        self.assertEqual(len(suffixes),27)
        self.assertEqual(len(names),27)
        self.assertTrue(names<=r.decision_tokens)
        self.assertTrue(legacy.isdisjoint(r.decision_tokens))
        self.assertEqual(r.enum_tokens['script_enum_humanitarian_action_part'],families|suffixes|legacy)
        for path,source in sources.items():
            for token in set(re.findall(r'\btoken:([A-Za-z_][A-Za-z0-9_]*)',source)):
                with self.subTest(path=path,token=token):
                    self.assertIn(token,r.registered_tokens)
                    self.assertIsInstance(r._value('token:'+token),ScriptToken)
    def test_undefined_token_literal_cannot_name_a_scripted_helper(self):
        r=Runtime()
        self.assertIn('humanitarian_action_begin',r.effect_defs)
        with self.assertRaisesRegex(F.SourceContractError,'unregistered native token'):
            r._value('token:humanitarian_action_begin')
        with self.assertRaisesRegex(F.SourceContractError,'unregistered native token'):
            r._value('token:undefined_action_metadata_fixture')
    def test_actual_meta_dispatch_rejects_unregistered_or_unflagged_token_values(self):
        for token in [ScriptToken('undefined_action_metadata_fixture'),'famine']:
            with self.subTest(token=token):
                r,a,s,host=case();before_values=dict(a.values);before_resources=dict(a.resources)
                with self.assertRaisesRegex(F.SourceContractError,'GetTokenKey requires a registered native token'):
                    r.run_effect('humanitarian_action_find_pending',a,caller_temps={'humanitarian_action_system_token':token})
                self.assertEqual(a.values,before_values)
                self.assertEqual(a.resources,before_resources)
                self.assertEqual(a.arrays,{})
                self.assertEqual(r.resource_writes,[])
    def test_scope_pay_once_and_receipt_replay(self):
        r,a,s,host=case();start(r,a,9)
        self.assertEqual(len(a.arrays['famine_action_ids']),1)
        self.assertIs(s.values['famine_conceal_crisis_operation_actor'],a)
        self.assertEqual(a.resources['infantry_equipment'],10000-r.constants['constant:humanitarian_legacy_cost.infantry_light'])
        writes=list(r.resource_writes);start(r,a,9);self.assertEqual(r.resource_writes,writes)
        oldid=a.arrays['famine_action_ids'][0];r.advance_days(100);pulse(r,a,host)
        self.assertIn('famine_crisis_concealed',s.flags)
        self.assertNotIn('famine_crisis_concealed',host.flags)
        once=len(r.timed_flag_writes)
        a.values['humanitarian_action_callback_id']=oldid;r.run_effect('famine_action_resolve_callback',a,root=host)
        self.assertEqual(len(r.timed_flag_writes),once)
    def test_due_selection_and_cooldown(self):
        r,a,s,host=case();start(r,a,9);pulse(r,a,host)
        self.assertNotIn('famine_crisis_concealed',s.flags)
        other=F.state(43,a);a.values['famine_panel_selected_state']=other
        due=a.arrays['famine_action_dates'][0];r.globals['date']=due;pulse(r,a,host)
        self.assertIn('famine_crisis_concealed',s.flags);self.assertNotIn('famine_crisis_concealed',other.flags)
        s.flags.discard('famine_crisis_concealed');a.values['famine_panel_selected_state']=s
        self.assertFalse(r.run_trigger('famine_gui_can_start_conceal_crisis',a))
        r.globals['date']=a.values['famine_action_cooldown_conceal_crisis_42']
        self.assertTrue(r.run_trigger('famine_gui_can_start_conceal_crisis',a))
    def test_lost_control_cancels_original_receipt(self):
        r,a,s,host=case();start(r,a,9);s.controller=host;pulse(r,a,host)
        self.assertEqual(a.arrays['famine_action_ids'],[])
        self.assertNotIn('famine_conceal_crisis_cost_paid',s.flags)
        self.assertNotIn('famine_crisis_concealed',s.flags)
    def test_new_generation_cannot_be_cleared_by_old_callback(self):
        r,a,s,host=case();start(r,a,9);old=a.arrays['famine_action_ids'][0]
        s.values['famine_conceal_crisis_operation_generation']=old+1
        a.values['famine_action_generation_conceal_crisis_42']=old+1
        pulse(r,a,host)
        self.assertEqual(s.values['famine_conceal_crisis_operation_generation'],old+1)
        self.assertIn('famine_action_due_conceal_crisis_42',a.values)
    def test_zero_reserve_refund_runs_production_payment_and_refund(self):
        r,a,s,host=case();before=dict(a.resources);start(r,a,1)
        self.assertEqual(len(a.arrays['famine_action_ids']),1)
        s.values['famine_food_reserve_amount']=0;r.advance_days(100);pulse(r,a,host)
        self.assertEqual(a.resources,before)
        self.assertNotIn('famine_action_cooldown_release_reserves_42',a.values)
        writes=list(r.resource_writes);pulse(r,a,host);self.assertEqual(r.resource_writes,writes)
    def test_opening_status_does_not_register(self):
        r,a,s,host=case();r.run_effect('famine_gui_refresh_selected_action_status',a)
        self.assertEqual(r.global_arrays['famine_active_countries'],[])
        self.assertNotIn('famine_action_sequence',a.values)
    def test_quiet_law_change_refreshes_only_open_panels_without_gameplay_activation(self):
        for open_panels in [(),('migration',),('famine',),('migration','famine')]:
            with self.subTest(open_panels=open_panels):
                r,a,s,host=case();s.flags.clear()
                a.flags.update(panel+'_panel_open' for panel in open_panels)
                a.values.update(migration_reception_policy=4,migration_departure_policy=2,migration_border_policy=4)
                before_values=dict(a.values);before_flags=set(a.flags);before_resources=dict(a.resources)
                before_global_arrays={key:list(values) for key,values in r.global_arrays.items()}
                r.run_effect('migration_national_policy_changed',a,root=host,caller_temps={
                    'national_policy_changed_civilian_slot':1,
                    'national_policy_previous_value':2,
                    'national_policy_new_value':4,
                })
                self.assertEqual(r.panel_refresh_requests,[(panel+'_panel_refresh',a.id) for panel in ['migration','famine'] if panel in open_panels])
                self.assertEqual(a.values,before_values)
                self.assertEqual(a.flags,before_flags)
                self.assertEqual(a.resources,before_resources)
                self.assertEqual(r.global_arrays,before_global_arrays)
                self.assertEqual(a.arrays,{})
                self.assertEqual(r.resource_writes,[])
                self.assertEqual(r.bridge_visits,[])
                self.assertEqual(set(r.external_calls),{panel+'_panel_refresh' for panel in open_panels})
    def test_migration_overload_blocks_evacuation(self):
        r,a,s,host=case();a.values.update(migration_reception_load=101,migration_reception_capacity=100)
        self.assertFalse(r.run_trigger('migration_reception_has_room_for_evacuation',a))
        a.values['migration_reception_load']=100
        self.assertTrue(r.run_trigger('migration_reception_has_room_for_evacuation',a))
    def test_pending_paid_work_survives_crisis_retirement(self):
        r,a,s,host=case();start(r,a,9);s.flags.discard('famine_food_stage_famine')
        r.run_effect('famine_process_registered_country',a,root=host)
        self.assertIn(a,r.global_arrays['famine_active_countries'])
        self.assertEqual(len(a.arrays['famine_action_ids']),1)
        r.advance_days(100);r.run_effect('famine_process_registered_country',a,root=host)
        self.assertNotIn(a,r.global_arrays['famine_active_countries'])
        self.assertIn('famine_crisis_concealed',s.flags)
    def test_exact_quote_boundaries(self):
        for delta in [-1,0,1]:
            r,a,s,host=case();fee=r.constants['constant:migration_transport_cost.light_fuel_land']
            a.resources['fuel']=fee+delta
            self.assertEqual(r.run_trigger('famine_gui_can_start_conceal_crisis',a),delta>=0)
            start(r,a,9)
            self.assertEqual(len(a.arrays.get('famine_action_ids',[])),int(delta>=0))
    def test_paid_cohort_is_not_retargeted_by_selector_changes(self):
        r,a,s,host=case();s.values['migration_current_cohort_id']=12;start(r,a,9)
        s.values['migration_current_cohort_id']=13;r.advance_days(100);pulse(r,a,host)
        self.assertEqual(a.arrays['famine_action_ids'],[])
        self.assertNotIn('famine_crisis_concealed',s.flags)
    def test_mission_deadlines_keep_converted_days(self):
        r,a,s,host=case();r.globals['date']=Decimal('7')
        for name,field,const in [
            ('migration_set_mission_evacuation_deadline','migration_mission_evacuation_deadline','constant:migration_mission_timing.evacuation_protection_days'),
            ('migration_set_mission_reception_observation_deadline','migration_mission_reception_observation_deadline','constant:migration_mission_timing.reception_observation_days'),
            ('migration_set_mission_return_deadline','migration_mission_return_deadline','constant:migration_mission_timing.return_route_observation_days')]:
            r.run_effect(name,s)
            self.assertEqual(s.values[field],Decimal('7')+r.constants[const]*Decimal('0.00024'))
    def test_zero_transfer_refunds_exact_paid_tuple(self):
        r,a,s,host=case();a.resources['train_equipment']=100
        a.values['migration_panel_selected_state']=s
        s.flags.update(['migration_displacement_active','migration_evacuation_prepared','migration_persecution_active'])
        s.values.update(migration_flight_pressure=100000,migration_trapped_population=100000)
        before=dict(a.resources)
        r.run_effect('migration_gui_start_action',a,caller_temps={'migration_gui_action':2})
        self.assertEqual(len(a.arrays['migration_action_ids']),1)
        # A previously selected route has expired. The production callback must
        # reject movement and refund, without calling the transfer core.
        s.flags.add('humanitarian_corridor_accepted')
        r.advance_days(100);r.run_effect('migration_action_process_pending',a,root=host)
        self.assertEqual(a.resources,before)
        self.assertNotIn('migration_action_cooldown_evacuate_vulnerable_42',a.values)
        writes=list(r.resource_writes);r.run_effect('migration_action_process_pending',a,root=host)
        self.assertEqual(r.resource_writes,writes)
    def test_pending_batch_above_engine_loop_limit_preserves_unvisited_rows(self):
        r,a,s,host=case();states=[];ids=list(range(1,1202));due=Decimal('1')
        for identity in ids:
            target=F.state(2000+identity,a)
            target.values.update(famine_conceal_crisis_operation_generation=identity,famine_conceal_crisis_operation_actor=a,famine_conceal_crisis_operation_cohort_id=0)
            a.values['famine_action_generation_conceal_crisis_'+str(target.id)]=identity
            a.values['famine_action_due_conceal_crisis_'+str(target.id)]=due
            states.append(target)
        a.arrays.update(famine_action_ids=ids[:],famine_action_types=[9]*len(ids),famine_action_states=states,famine_action_dates=[due]*len(ids),famine_action_starts=[Decimal(0)]*len(ids))
        pulse(r,a,host)
        self.assertEqual(a.arrays['famine_action_ids'],ids)
        self.assertEqual(a.values['famine_action_process_cursor'],201)
        first={identity for event,identity in r.bridge_visits if event=='humanitarian_actions.2'}
        self.assertEqual(len(first),1000)
        pulse(r,a,host)
        visits={identity for event,identity in r.bridge_visits if event=='humanitarian_actions.2'}
        self.assertEqual(visits,set(ids))
        self.assertEqual(a.arrays['famine_action_ids'],ids)
        self.assertNotIn('famine_action_process_cursor',a.values)
    def test_deep_legacy_wrapper_preserves_explicit_actor_and_state(self):
        r,a,s,host=case();s.values.update(migration_state_reception_load=100,migration_state_live_cohort_amount=100)
        a.values['migration_reception_load']=100
        r.root=a;r.scope_stack=[s];r.from_scope=host
        r.temp_frames=[dict(humanitarian_action_context_proven=1,humanitarian_action_actor=a,humanitarian_action_target=s)]
        self.assertTrue(r._run_trigger('migration_local_integration_host_can_settle',s))
        self.assertIs(r.temp_frames[0]['humanitarian_action_actor'],a)
        self.assertIs(r.temp_frames[0]['humanitarian_action_target'],s)
    def test_nonexistent_actor_retires_exact_proof_without_event_or_refund(self):
        r,a,s,host=case();start(r,a,9);writes=list(r.resource_writes);events=len(r.bridge_visits)
        a.exists=False;pulse(r,a,host)
        self.assertEqual(a.arrays['famine_action_ids'],[])
        self.assertNotIn('famine_conceal_crisis_cost_paid',s.flags)
        self.assertNotIn('famine_conceal_crisis_operation_generation',s.values)
        self.assertNotIn('famine_action_due_conceal_crisis_42',a.values)
        self.assertEqual(r.resource_writes,writes)
        self.assertEqual(len(r.bridge_visits),events)

if __name__=='__main__':unittest.main(verbosity=2)
