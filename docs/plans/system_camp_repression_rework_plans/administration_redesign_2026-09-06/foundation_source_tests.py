"""Execute parsed production helpers; only engine primitives and external consumers are mocks.
This is source-contract evidence, not an HOI4 interpreter or engine/runtime proof.
Run from repository root: python <this file>.
"""
from pathlib import Path
import re, math, json, datetime

ROOT = Path(__file__).resolve().parents[4]
TOKEN = re.compile(r'#[^\n]*|"[^"\n]*"|[{}=<>]|[^\s{}=<>]+')

def parse(text):
    ts = [m.group() for m in TOKEN.finditer(text) if not m.group().startswith('#')]
    def block(i, nested=False):
        out=[]
        while i<len(ts) and ts[i]!='}':
            k,op=ts[i:i+2]; i+=2
            if op not in ('=','<','>'): raise ValueError((k,op))
            if ts[i]=='{': v,i=block(i+1,True)
            else: v=ts[i].strip('"'); i+=1
            out.append((k,op,v))
        return out,i+1 if nested else i
    return block(0)[0]

def get(b,k,default=None):
    return next((v for a,o,v in b if a==k),default)

def substitute(b,params):
    def sub(x):
        for k,v in params.items(): x=x.replace('$'+k+'$',str(v))
        return x
    return [(sub(k),o,substitute(v,params) if isinstance(v,list) else sub(v)) for k,o,v in b]

class Runtime:
    def __init__(self):
        self.effects={}; self.triggers={}; self.constants={}; self.scopes={}; self.temp={}; self.targets={}
        self.date=datetime.date(1938,1,1); self.global_flags=set(); self.debits=0; self.logged=0
        for path in ['common/scripted_effects/camp_administration_effects.txt','common/scripted_effects/camp_administration_ui_effects.txt','common/scripted_effects/camp_administration_origin_effects.txt','common/scripted_effects/camp_administration_occupation_effects.txt','common/scripted_effects/camp_occ_partner_effects.txt','common/scripted_effects/chaosx_dynamic_effects.txt']:
            source=(ROOT/path).read_text(encoding='utf-8-sig')
            self.effects.update({k:v for k,o,v in parse(source) if not k.startswith('@')})
            for key,value in re.findall(r'(?m)^(@[A-Z0-9_]+)\s*=\s*(-?\d+(?:\.\d+)?)\s*$',source): self.constants[key]=float(value)
        self.triggers.update({k:v for k,o,v in parse((ROOT/'common/scripted_triggers/camp_administration_triggers.txt').read_text())})
        for name in ('camp_administration_origin_triggers','camp_administration_occupation_triggers','camp_administration_ui_triggers','camp_occ_partner_triggers'):
            self.triggers.update({k:v for k,o,v in parse((ROOT/f'common/scripted_triggers/{name}.txt').read_text())})
        for path in ['common/script_constants/camp_administration_constants.txt','common/script_constants/camp_administration_ui_constants.txt','common/script_constants/camp_administration_origin_constants.txt','common/script_constants/camp_administration_occupation_constants.txt','common/script_constants/camp_occ_partner_constants.txt','common/script_constants/chaos_meter_deaths_constants.txt']:
            if not (ROOT/path).exists(): continue
            for cat,o,b in parse((ROOT/path).read_text()):
                if isinstance(b,list):
                    for k,o,v in b:
                        if k!='schema' and not isinstance(v,list): self.constants[cat+'.'+k]=float(v)
        # External reason enum value is immaterial to conservation arithmetic.
        self.constants.setdefault('chaos_meter_deaths_reason.camp_atrocity',1)
        for k,v in [('zero',0),('one',1),('people_per_k',1000),('negative_one',-1)]: self.constants.setdefault('chaos_meter_deaths.'+k,v)
        self.constants.setdefault('chaos_meter_deaths_reason.unknown',0)
        # Existing domain harness subclasses retain their policy mocks. Route
        # the newly required typed state-pointer primitive through one engine
        # primitive adapter rather than dropping its production check.
        domain_cond = self.cond
        def primitive_cond(block, scope, previous=None):
            if scope not in self.scopes: return False
            if len(block)==1 and block[0][0]=='state':
                return self.state_scope_matches(scope,block[0][2],previous)
            return domain_cond(block,scope,previous)
        self.cond = primitive_cond

    def state_scope_matches(self,scope,target,previous=None):
        if scope not in self.scopes or 'state_population_k' not in self.scopes[scope]: return False
        target=self.target(target,scope,previous)
        try: return float(scope)==float(target)
        except (TypeError,ValueError): return str(scope)==str(target)

    def country(self,key='GER',support=10000,factories=100):
        self.scopes[key]={'id':key,'flags':set(),'arrays':{},'mods':set(),'exists':True,'support':support,'political_power':100,'num_of_military_factories':factories,'government':'fascism'}
        self.run('camp_admin_initialize_country',key)
        return self.scopes[key]

    def state(self,key='S1',country='GER',population=1000,buildings=4,factories=10):
        self.scopes[key]={'id':key,'flags':{'camp_rework_site_active','camp_rework_expanded_labor_site'},'arrays':{},'mods':set(),'owner':country,'controller':country,'state_population_k':population,'concentration_camp':buildings,'arms_factory':factories,'industrial_complex':5,'infrastructure':2,'genocide_responsible_country':country,'resource@steel':20}
        self.scopes[country]['arrays'].setdefault('camp_active_site_states',[]).append(key)
        self.run('camp_admin_initialize_site',key)
        return self.scopes[key]

    def target(self,x,s,prev):
        if x=='THIS': return s
        if x=='PREV': return prev
        if x.startswith('PREV.'): return self.val(x,s,prev)
        if x in ('OWNER','CONTROLLER'): return self.scopes[s][x.lower()]
        if x.startswith('event_target:'): return self.targets[x[13:]]
        if x.startswith('var:'): return self.val(x[4:],s,prev)
        return x

    def val(self,x,s,prev=None):
        if isinstance(x,(int,float)): return x
        try: return float(x)
        except (ValueError,TypeError): pass
        if x in ('yes','no'): return x=='yes'
        if x=='global.year': return self.date.year
        if x.startswith('constant:'): return self.constants[x[9:]]
        if x.startswith('var:'): return self.val(x[4:],s,prev)
        if x.startswith('@'): return self.constants[x]
        if x.endswith('.id'): return self.target(x[:-3],s,prev)
        if x.startswith('PREV.'): return self.val(x[5:],prev,s)
        if x.startswith('event_target:') or x in ('THIS','OWNER','CONTROLLER','PREV'): return self.target(x,s,prev)
        if x.endswith('^num'): return len(self.scopes[s]['arrays'].get(x[:-4],[]))
        if '^' in x:
            array,index=x.split('^',1)
            return self.scopes[s]['arrays'][array][int(self.val(index,s,prev))]
        if x in self.temp: return self.temp[x]
        # Native database country tokens resolve to scope pointers, rather than
        # being read as a zero-valued variable in the current state.
        if x in self.scopes: return x
        if x.startswith(('building_level@','non_damaged_building_level@')): return self.scopes[s].get(x.split('@')[1],0)
        if x=='infrastructure_level': return self.scopes[s].get('infrastructure',0)
        if x=='num_equipment@support_equipment': return self.scopes[s]['support']
        return self.scopes[s].get(x,0)

    def cond(self,b,s,prev=None):
        def one(k,o,v):
            if k in ('AND','OR','NOT'):
                values=[one(a,c,d) for a,c,d in v]
                return all(values) if k=='AND' else any(values) if k=='OR' else not all(values)
            if k=='if':
                return not self.cond(get(v,'limit',[]),s,prev) or self.cond([x for x in v if x[0]!='limit'],s,prev)
            if k=='meta_trigger':
                replacements={}
                for name,_,token in v:
                    if name=='text': continue
                    match=re.fullmatch(r'\[\?([^|]+)\|\.0\]',token)
                    replacements[name]=str(int(self.val(match.group(1),s,prev))) if match else token
                def replace(entries):
                    result=[]
                    for name,operator,token in entries:
                        if isinstance(token,list): token=replace(token)
                        else:
                            for key,value in replacements.items(): token=token.replace('['+key+']',value)
                        result.append((name,operator,token))
                    return result
                return self.cond(replace(get(v,'text')),s,prev)
            if k=='all_of':
                body=[x for x in v if x[0] not in ('array','value','index')]
                for index,value in enumerate(self.scopes[s]['arrays'].get(get(v,'array'),[])):
                    self.temp[get(v,'index','i')]=index; self.temp[get(v,'value','v')]=value
                    if not self.cond(body,s,prev): return False
                return True
            if k=='all_of_scopes':
                body=[x for x in v if x[0] not in ('array','tooltip')]
                return all(self.cond(body,dst,s) for dst in self.scopes[s]['arrays'].get(get(v,'array'),[]))
            if k=='any_of_scopes':
                body=[x for x in v if x[0] not in ('array','tooltip')]
                return any(self.cond(body,dst,s) for dst in self.scopes[s]['arrays'].get(get(v,'array'),[]))
            if k in ('set_temp_variable','add_to_temp_variable','subtract_from_temp_variable','multiply_temp_variable','divide_temp_variable','clamp_temp_variable','round_temp_variable'):
                self.execute([(k,o,v)],s,prev)
                return True
            if k in self.triggers: return self.cond(self.triggers[k],s,prev)==(v=='yes')
            if k in ('camp_rework_country_is_eligible','camp_rework_country_can_use_radicalized_route','camp_admin_country_can_radicalize'): return self.scopes[s].get('eligible',True)==(v=='yes')
            if k=='check_variable':
                if get(v,'var') is not None: a=self.val(get(v,'var'),s,prev); c=self.val(get(v,'value'),s,prev); op=get(v,'compare','equals')
                else: key,op,value=v[0]; a=self.val(key,s,prev); c=self.val(value,s,prev)
                if op not in ('=','equals','not_equals'):
                    # Stored scope pointers have numeric engine representations.
                    # Keep identity strings for equality/scoping and model only
                    # their positive ordered value for numeric pointer guards.
                    if isinstance(a,str) and a in self.scopes: a=list(self.scopes).index(a)+1
                    if isinstance(c,str) and c in self.scopes: c=list(self.scopes).index(c)+1
                equal = abs(a-c)<1e-7 if isinstance(a,(int,float)) and isinstance(c,(int,float)) else a==c
                return {'=':lambda:equal,'equals':lambda:equal,'not_equals':lambda:not equal,'>':lambda:a>c,'<':lambda:a<c,'greater_than':lambda:a>c,'less_than':lambda:a<c,'greater_than_or_equals':lambda:a>c or equal,'less_than_or_equals':lambda:a<c or equal}[op]()
            if k=='has_variable': return v in self.temp or v in self.scopes[s]
            if k=='has_event_target': return v in self.targets
            if k=='has_decision': return v in self.scopes[s].get('missions',set())
            if k=='has_global_flag': return v in self.global_flags
            if k in ('has_state_flag','has_country_flag'):
                if isinstance(v,list):
                    # Timed form: { flag = X days > N } counts days since the flag was set.
                    flag=get(v,'flag')
                    if flag not in self.scopes[s]['flags']: return False
                    for dk,dop,dv in v:
                        if dk=='days':
                            since=(self.date-self.scopes[s].get('flag_dates',{}).get(flag,datetime.date.min)).days
                            quoted=self.val(dv,s,prev)
                            return since>quoted if dop=='>' else since<quoted if dop=='<' else since==quoted
                    return True
                return v in self.scopes[s]['flags']
            if k=='has_dynamic_modifier': return get(v,'modifier') in self.scopes[s]['mods']
            if k=='is_controlled_by': return self.scopes[s]['controller']==self.target(v,s,prev)
            if k=='is_subject_of': return self.scopes[s].get('overlord')==self.target(v,s,prev)
            if k=='has_cosmetic_tag': return self.scopes[s].get('cosmetic_tag')==v
            if k=='is_special_chaos_country': return self.scopes[s].get('special_chaos',False)==(v=='yes')
            if k=='is_core_of': return self.target(v,s,prev) in self.scopes[s].get('cores',set())
            if k=='has_government': return self.scopes[s]['government']==v
            if k=='has_manpower':
                amount=self.scopes[s].get('manpower',0); quoted=self.val(v,s,prev)
                return amount<quoted if o=='<' else amount>quoted if o=='>' else amount==quoted
            if k=='has_equipment':
                kind,compare,quoted=v[0]; amount=self.scopes[s].get('equipment',{}).get(kind,0); quoted=self.val(quoted,s,prev)
                return amount<quoted if compare=='<' else amount>quoted if compare=='>' else amount==quoted
            if k=='has_war': return self.scopes[s].get('has_war',False)==(v=='yes')
            if k=='has_war_with': return self.target(v,s,prev) in self.scopes[s].get('wars',set())
            if k=='exists': return self.scopes[s].get('exists',True)==(v=='yes')
            if k=='is_in_array': return self.target(get(v,'value'),s,prev) in self.scopes[s]['arrays'].get(get(v,'array'),[])
            if k=='date':
                d=datetime.date(*map(int,v.split('.'))); return self.date<d if o=='<' else self.date>d
            if k in ('tag','original_tag'): return self.scopes[s].get('original_tag',s)==self.target(v,s,prev)
            if isinstance(v,list): return self.cond(v,self.target(k,s,prev),s)
            a=self.val(k,s,prev); c=self.val(v,s,prev)
            return a<c if o=='<' else a>c if o=='>' else a==c
        return all(one(k,o,v) for k,o,v in b)

    def run(self,name,s,params=None,prev=None):
        self.execute(substitute(self.effects[name],params or {}),s,prev)

    def execute(self,b,s,prev=None):
        chain=False
        for k,o,v in b:
            if k in ('if','else_if','else'):
                okay=(k=='if' or not chain) and (k=='else' or self.cond(get(v,'limit',[]),s,prev))
                if k=='if': chain=False
                if okay: self.execute([x for x in v if x[0]!='limit'],s,prev); chain=True
                continue
            if k=='apply_state_population_loss_without_recruitable_manpower_gain':
                amount=self.temp['state_population_transaction_loss']; self.scopes[s]['state_population_k']-=amount/1000; self.debits+=1
            elif k=='chaos_meter_register_deaths':
                assert self.temp['chaos_deaths_apply_state_pop']==0,'Second physical debit requested'
                self.logged+=self.temp['chaos_deaths_change']/1000
                if self.temp.get('chaos_deaths_record_state_ledger',0) and 'state_population_k' in self.scopes[s]:
                    self.scopes[s]['chaos_state_civilian_deaths_total']=self.scopes[s].get('chaos_state_civilian_deaths_total',0)+self.temp['chaos_deaths_change']
            elif k=='camp_rework_record_latest_state_deaths': pass # External projection only, not a physical primitive.
            elif k in self.effects: self.run(k,s,{a:c for a,o,c in v} if isinstance(v,list) else {},prev)
            elif k=='meta_effect':
                text=get(v,'text'); year=str(self.date.year)
                def year_replace(z): return [(a,o,year_replace(c) if isinstance(c,list) else c.replace('[YEAR]',year)) for a,o,c in z]
                self.execute(year_replace(text),s,prev)
            elif k=='for_each_scope_loop':
                assert get(v,'limit') is None,'Unsupported direct loop limit'
                for dst in list(self.scopes[s]['arrays'].get(get(v,'array'),[])): self.execute([x for x in v if x[0]!='array'],dst,s)
            elif k=='while_loop_effect':
                for _ in range(10000):
                    if not self.cond(get(v,'limit',[]),s,prev): break
                    self.execute([x for x in v if x[0]!='limit'],s,prev)
                else: raise AssertionError('Unbounded source loop')
            elif k=='save_event_target_as': self.targets[v]=s
            elif k in ('set_country_flag','set_state_flag'):
                flag=get(v,'flag') if isinstance(v,list) else v
                if flag not in self.scopes[s]['flags']: self.scopes[s].setdefault('flag_dates',{})[flag]=self.date
                self.scopes[s]['flags'].add(flag)
            elif k in ('clr_country_flag','clr_state_flag'):
                self.scopes[s]['flags'].discard(v); self.scopes[s].get('flag_dates',{}).pop(v,None)
            elif k=='clear_variable': self.scopes[s].pop(v,None)
            elif k in ('add_dynamic_modifier','remove_dynamic_modifier'):
                getattr(self.scopes[s]['mods'],'add' if k.startswith('add') else 'discard')(get(v,'modifier'))
            elif k=='force_update_dynamic_modifier': pass
            elif k=='clear_array': self.scopes[s]['arrays'][v]=[]
            elif k=='add_to_array':
                array,value=(get(v,'array'),get(v,'value')) if get(v,'array') is not None else (v[0][0],v[0][2])
                self.scopes[s]['arrays'].setdefault(array,[]).append(self.val(value,s,prev))
            elif k=='add_equipment_to_stockpile': self.scopes[s]['support']+=self.val(get(v,'amount'),s,prev)
            elif k=='add_political_power': self.scopes[s]['political_power']+=self.val(v,s,prev)
            elif k=='add_breakthrough_progress':
                specialization=get(v,'specialization')
                amount=self.val(get(v,'value'),s,prev)
                stock=self.scopes[s].setdefault('breakthrough',{})
                stock[specialization]=stock.get(specialization,0)+amount
            elif k=='army_experience': self.scopes[s]['army_experience']=self.scopes[s].get('army_experience',0)+self.val(v,s,prev)
            elif k=='activate_mission': self.scopes[s].setdefault('missions',set()).add(v)
            elif k=='add_stability': self.scopes[s]['stability']=self.scopes[s].get('stability',0)+self.val(v,s,prev)
            elif k=='remove_building': self.scopes[s][get(v,'type')]=max(0,self.scopes[s].get(get(v,'type'),0)-self.val(get(v,'level'),s,prev))
            elif k=='add_building_construction': self.scopes[s][get(v,'type')]=self.scopes[s].get(get(v,'type'),0)+self.val(get(v,'level'),s,prev)
            elif 'variable' in k:
                target=self.temp if 'temp' in k else self.scopes[s]
                if k.startswith('round_'): target[v]=math.floor(self.val(v,s,prev)+.5)
                elif k.startswith('clamp_'):
                    key=get(v,'var'); target[key]=max(self.val(get(v,'min','-1000000000'),s,prev),min(self.val(key,s,prev),self.val(get(v,'max','1000000000'),s,prev)))
                else:
                    key,_,value=v[0]; value=self.val(value,s,prev); old=self.val(key,s,prev)
                    if k.startswith('set_'): updated=value
                    elif k.startswith('add_to_'): updated=old+value
                    elif k.startswith('subtract_from_'): updated=old-value
                    elif k.startswith('multiply_'): updated=old*value
                    elif k.startswith('divide_'): updated=old/value
                    else: raise NotImplementedError(k)
                    if '^' in key and target is self.scopes[s]:
                        array,index=key.split('^',1)
                        self.scopes[s]['arrays'][array][int(self.val(index,s,prev))]=updated
                    else: target[key]=updated
            elif k=='custom_effect_tooltip': pass # Presentation-only consumer.
            elif k=='country_event': self.temp['last_country_event']=get(v,'id') # Delivery stub for the report selector.
            elif k=='camp_admin_country_apply_institutional_site_mortality': pass # Country-owned adapter has its own production-source scenarios.
            elif isinstance(v,list): self.execute(v,self.target(k,s,prev),s)
            else: raise NotImplementedError(k)

def prime_existing_custody(runtime,state,amount_k):
    """Model a previously admitted local cohort with aligned source rows."""
    site=runtime.scopes[state]
    site['camp_admin_detainees_k']=amount_k
    site['camp_admin_total_admitted_k']=amount_k
    runtime.temp.update(camp_admin_append_origin=state,camp_admin_append_authority=site['camp_admin_responsible_country'],camp_admin_append_root_id=0,camp_admin_append_amount_k=amount_k)
    runtime.run('camp_admin_append_row',state)

def tests():
    results=[]
    r=Runtime(); c=r.country(); s=r.state()
    assert s['camp_admin_detainees_k']==0
    r.temp.update(camp_admin_admission_requested_k=500,camp_admin_admission_source_k=80,camp_admin_admission_proven=1)
    before=s['state_population_k']; r.run('camp_admin_admit_detainees','S1')
    assert s['camp_admin_detainees_k']==80 and before==s['state_population_k']
    r.run('camp_admin_admit_detainees','S1'); assert s['camp_admin_detainees_k']==80
    results.append('Source membership, capacity, zero initialization and consumed admission proof')
    for cause in range(1,5):
        r.temp.update(camp_admin_death_requested_k=1,camp_admin_death_cause=cause,camp_admin_death_contract=1)
        r.run('camp_admin_record_deaths','S1')
    assert abs(s['camp_admin_detainees_k']-76)<1e-7 and r.debits==4 and r.logged==4
    assert c['camp_admin_total_deaths_k']==4 and sum(c['camp_admin_total_'+x+'_deaths_k'] for x in ['custody','labor','violence','institutional'])==4
    r.run('camp_admin_record_deaths','S1'); assert r.debits==4
    results.append('Four causes: measured population loss equals cohort loss, attribution and one log-only receipt per debit')
    q=Runtime(); qc=q.country(); qs=q.state(population=1000,buildings=4); prime_existing_custody(q,'S1',10)
    row_id=qs['arrays']['camp_admin_row_ids'][0]
    q.temp.update(camp_admin_death_requested_k=2,camp_admin_death_cause=3,camp_admin_death_contract=1,camp_admin_death_row_id=row_id,camp_admin_arrival_phase_contract=1)
    q.run('camp_admin_record_deaths','S1')
    assert qs['state_population_k']==998 and qs['camp_admin_detainees_k']==8 and q.debits==1 and q.logged==2
    assert qs['camp_admin_total_arrival_deaths_k']==2 and qc['camp_admin_total_arrival_deaths_k']==2
    assert qs['arrays']['camp_admin_row_arrival_deaths_k'][0]==2 and qs['arrays']['camp_admin_row_deaths_k'][0]==2
    q.temp.update(camp_admin_death_requested_k=1,camp_admin_death_cause=3,camp_admin_death_contract=1,camp_admin_death_row_id=row_id)
    q.run('camp_admin_record_deaths','S1')
    assert qs['camp_admin_total_arrival_deaths_k']==2 and qc['camp_admin_total_arrival_deaths_k']==2
    assert qc['camp_admin_total_violence_deaths_k']==3 and qs['arrays']['camp_admin_row_deaths_k'][0]==3
    assert q.debits==2 and q.logged==3
    q.global_flags.add('settings_chaos_deaths_disabled')
    q.temp.update(camp_admin_death_requested_k=1,camp_admin_death_cause=3,camp_admin_death_contract=1,camp_admin_death_row_id=row_id,camp_admin_arrival_phase_contract=1)
    q.run('camp_admin_record_deaths','S1')
    assert qs['state_population_k']==997 and qs['camp_admin_total_arrival_deaths_k']==2 and qs['arrays']['camp_admin_row_arrival_deaths_k'][0]==2
    assert q.temp['camp_admin_arrival_phase_contract']==0 and q.debits==2 and q.logged==3
    q.global_flags.remove('settings_chaos_deaths_disabled')
    results.append('Arrival-phase violence is an actual selected-row subset of the existing violence cause, never a second death debit')
    c['camp_admin_mandate']=2; s['camp_admin_support_ratio']=1; s['camp_admin_development_level']=3
    for priority in (1,2,3):
        c['camp_admin_priority']=priority; r.run('camp_admin_refresh_country_economy','GER')
        assert sum(s['camp_admin_'+x+'_k'] for x in ['industry','works','extraction'])<=s['camp_admin_detainees_k']*.65+1e-7
        assert s['camp_admin_construction_factor']<=.4 and s['camp_admin_extraction_factor']<=.4 and c['camp_admin_industrial_factor']<=.25
    results.append('Exclusive allocations and opportunity-based 40/25/40/40 caps')
    c['camp_admin_priority']=2; r.run('camp_admin_refresh_country_economy','GER'); assert s['camp_admin_construction_factor']==0
    c['flags'].add('camp_admin_economy_slot_active'); c['camp_admin_economy_state_id']='S1'; c['camp_admin_economy_project_type']=2
    r.run('camp_admin_refresh_country_economy','GER'); assert abs(s['camp_admin_construction_factor']-.4)<1e-8
    r.run('camp_admin_cancel_economy_project','GER'); r.run('camp_admin_refresh_country_economy','GER'); assert s['camp_admin_construction_factor']==0
    results.append('Construction output requires the supported live works project and disappears when it ends')
    s['flags'].add('camp_admin_site_suspended'); r.run('camp_admin_refresh_country_economy','GER'); assert c['camp_admin_total_workforce_k']==0 and s['camp_admin_detainees_k']==76
    s['flags'].discard('camp_admin_site_suspended')
    c['support']=100; r.run('camp_admin_pay_monthly_maintenance','GER'); assert c['support']==100 and s['camp_admin_support_ratio']==0
    r.temp.update(camp_admin_quote_support=40,camp_admin_quote_pp=0); r.run('camp_admin_try_pay_project','GER'); assert r.temp['camp_admin_payment_accepted']==0
    results.append('Suspension preserves custody, exact reserves reject unfunded maintenance/development without negative stocks')
    c['support']=10000; c['camp_admin_budget']=2; c['camp_admin_priority']=1
    for month in range(1,13):
        r.date=datetime.date(1938,month,1); r.run('camp_admin_monthly_country','GER')
        snapshot=(c['support'],s['camp_admin_detainees_k'],r.debits)
        r.date=datetime.date(1938,month,20); r.run('camp_admin_monthly_country','GER'); assert snapshot==(c['support'],s['camp_admin_detainees_k'],r.debits)
    results.append({'scenario':'Twelve months automatic, duplicate calls on different days same month','remaining_support':round(c['support'],3),'surviving_k':round(s['camp_admin_detainees_k'],3)})
    before=s['state_population_k']; survivors=s['camp_admin_detainees_k']; r.run('camp_admin_reform_site','S1')
    assert s['camp_admin_detainees_k']==0 and s['state_population_k']==before and c['camp_admin_industrial_factor']==0
    r.run('camp_admin_reform_site','S1'); assert s['camp_admin_total_released_k']==survivors
    c['arrays']['camp_active_site_states']=[]
    for month in range(1,13): r.date=datetime.date(1939,month,1); r.run('camp_admin_monthly_country','GER')
    assert s['camp_admin_civilian_replacement']==1 and s['state_population_k']==before
    results.append('Selected reform: one release, immediate national cleanup, twelve-month paid civilian replacement without population creation')
    q=Runtime(); qc=q.country(); qs=q.state(population=1000,buildings=4); prime_existing_custody(q,'S1',80)
    qs['state_population_k']=51 # Unlabelled 949k decline can conservatively retire the entire unique 80k exposure.
    q.run('camp_admin_reform_site','S1')
    assert qs['camp_admin_external_attrition_k']==80 and qs['camp_admin_total_released_k']==0
    assert qs['camp_admin_detainees_k']==0 and qs['state_population_k']==51
    assert qs['camp_admin_civilian_target_k']==0 and q.debits==0 and q.logged==0
    results.append('Unlabelled 949k outside decline conservatively retires the sole 80k exposure without camp cause, physical debit or claimed survivor release')
    q=Runtime(); qc=q.country(); qs=q.state(population=1000,buildings=4); prime_existing_custody(q,'S1',80)
    q.temp.update(camp_admin_death_requested_k=30,camp_admin_death_cause=1,camp_admin_death_contract=1,camp_admin_death_row_id=qs['arrays']['camp_admin_row_ids'][0])
    q.run('camp_admin_record_deaths','S1')
    assert qs['camp_admin_detainees_k']==50 and qs['state_population_k']==970 and qs['chaos_state_civilian_deaths_total']==30000
    assert qs['camp_admin_external_attrition_k']==0 and q.debits==1 and q.logged==30
    before=qs['state_population_k']; q.run('camp_admin_reform_site','S1')
    assert qs['camp_admin_total_released_k']==50 and qs['camp_admin_detainees_k']==0 and qs['state_population_k']==before
    assert abs(qs['camp_admin_civilian_target_k']-32.5)<1e-8
    assert qs['camp_admin_total_custody_deaths_k']==30 and q.debits==1 and q.logged==30
    results.append('A production selected-row 30k custody death leaves 50k proved survivors for one in-place reform release and a 32.5k civilian target without population creation')
    q=Runtime(); q.country(); qs=q.state(population=1000,buildings=4); prime_existing_custody(q,'S1',10)
    qs['arrays']['camp_admin_row_amounts_k'][0]=9
    q.run('camp_admin_reform_site','S1')
    assert qs['camp_admin_detainees_k']==10 and qs['camp_admin_total_released_k']==0
    assert qs['camp_admin_civilian_target_k']==0 and 'camp_admin_closed' not in qs['flags']
    results.append('Shared site reform rejects an inconsistent custody ledger before closure or a civilian replacement target')
    q=Runtime(); qc=q.country(); qs=q.state(population=1000,buildings=4); prime_existing_custody(q,'S1',10)
    qs['arrays']['camp_admin_row_amounts_k'][0]=9
    assert not q.cond(q.triggers['camp_admin_country_sites_ready_for_reform'],'GER')
    q.run('camp_admin_begin_reform','GER')
    assert 'camp_admin_reforming' not in qc['flags'] and 'camp_admin_closed' not in qs['flags']
    assert qs['camp_admin_detainees_k']==10 and qs['camp_admin_civilian_target_k']==0
    qs['arrays']['camp_admin_row_amounts_k'][0]=10
    assert q.cond(q.triggers['camp_admin_country_sites_ready_for_reform'],'GER')
    q.run('camp_admin_begin_reform','GER')
    assert 'camp_admin_reforming' in qc['flags'] and 'camp_admin_closed' in qs['flags']
    assert qs['camp_admin_total_released_k']==10 and qs['camp_admin_detainees_k']==0
    results.append('Country reform leaves policy and custody untouched when a reformable site has bad rows, then completes once its finite rows reconcile')
    q=Runtime(); q.country(); qs=q.state(population=1000,buildings=4); prime_existing_custody(q,'S1',10)
    integration=parse((ROOT/'common/scripted_effects/camp_administration_integration_effects.txt').read_text(encoding='utf-8-sig'))
    q.effects['camp_admin_integration_reform_site']=get(integration,'camp_admin_integration_reform_site')
    q.effects['camp_admin_integration_record_site_history']=[('set_state_flag','=','test_history_written')]
    qs['arrays']['camp_admin_row_amounts_k'][0]=9
    q.run('camp_admin_integration_reform_site','S1')
    assert 'test_history_written' not in qs['flags'] and 'camp_admin_closed' not in qs['flags']
    qs['arrays']['camp_admin_row_amounts_k'][0]=10
    q.run('camp_admin_integration_reform_site','S1')
    assert 'test_history_written' in qs['flags'] and 'camp_admin_closed' in qs['flags']
    assert qs['camp_admin_total_released_k']==10
    results.append('Integration site reform records closure only after its actual authority and row gates allow ten thousand survivors to leave')
    q=Runtime(); qc=q.country(); qs=q.state(population=1000,buildings=4); prime_existing_custody(q,'S1',10)
    country_effects=parse((ROOT/'common/scripted_effects/camp_administration_country_effects.txt').read_text(encoding='utf-8-sig'))
    for category,_,entries in parse((ROOT/'common/script_constants/camp_administration_country_constants.txt').read_text(encoding='utf-8-sig')):
        for key,_,value in entries:
            if key!='schema': q.constants[category+'.'+key]=float(value)
    q.effects['camp_admin_country_reform']=get(country_effects,'camp_admin_country_reform')
    q.effects['camp_admin_country_clear_engineer_pending_receipt']=get(country_effects,'camp_admin_country_clear_engineer_pending_receipt')
    q.effects['camp_admin_country_halt']=[]; q.effects['camp_occ_close_country']=[]
    qs['arrays']['camp_admin_row_amounts_k'][0]=9
    q.run('camp_admin_country_reform','GER')
    assert 'camp_admin_country_reformed' not in qc['flags'] and 'camp_admin_closed' not in qs['flags']
    qs['arrays']['camp_admin_row_amounts_k'][0]=10
    q.run('camp_admin_country_reform','GER')
    assert 'camp_admin_country_reformed' in qc['flags'] and 'camp_admin_closed' in qs['flags']
    assert qs['camp_admin_total_released_k']==10
    results.append('Major-country reform does not advance national flags before an invalid site ledger, then releases survivors once rows reconcile')
    civil_triggers=parse((ROOT/'common/scripted_triggers/camp_administration_civil_triggers.txt').read_text(encoding='utf-8-sig'))
    major_triggers=parse((ROOT/'common/scripted_triggers/camp_administration_country_triggers.txt').read_text(encoding='utf-8-sig'))
    g=Runtime(); gc=g.country('GER'); gs=g.state('G1','GER'); prime_existing_custody(g,'G1',10)
    g.triggers.update({k:v for k,o,v in major_triggers})
    g.triggers['camp_admin_country_action_2_visible']=[]; g.triggers['camp_admin_country_is_major_kit']=[]
    gs['arrays']['camp_admin_row_amounts_k'][0]=9
    assert not g.cond(g.triggers['camp_admin_country_action_2_available'],'GER')
    gc['flags'].add('camp_admin_country_programs_authorized')
    assert g.cond(g.triggers['camp_admin_country_action_2_available'],'GER') # Halt does not release.
    h=Runtime(); hc=h.country('ENG'); hs=h.state('E1','ENG'); prime_existing_custody(h,'E1',10)
    h.triggers.update({k:v for k,o,v in civil_triggers})
    h.triggers['camp_administration_civil_action_two_visible']=[]
    hs['arrays']['camp_admin_row_amounts_k'][0]=9
    assert not h.cond(h.triggers['camp_administration_civil_action_two_available'],'ENG')
    hs['arrays']['camp_admin_row_amounts_k'][0]=10
    assert h.cond(h.triggers['camp_administration_civil_action_two_available'],'ENG')
    u=Runtime(); uc=u.country('USA'); us=u.state('U1','USA'); prime_existing_custody(u,'U1',10)
    u.triggers.update({k:v for k,o,v in civil_triggers})
    u.triggers['camp_administration_civil_action_two_visible']=[]
    u.date=datetime.date(1949,1,1); uc['flags'].add('camp_rework_usa_authority_terminated')
    us['arrays']['camp_admin_row_amounts_k'][0]=9
    assert u.cond(u.triggers['camp_administration_civil_action_two_available'],'USA') # Claims do not release.
    f=Runtime(); fc=f.country('FRA'); fs=f.state('F1','FRA'); prime_existing_custody(f,'F1',10)
    fc['government']='democratic'; f.date=datetime.date(1942,1,1)
    f.triggers.update({k:v for k,o,v in civil_triggers})
    f.triggers['camp_administration_civil_action_one_visible']=[]
    fs['arrays']['camp_admin_row_amounts_k'][0]=9
    assert not f.cond(f.triggers['camp_administration_civil_action_one_available'],'FRA')
    fs['arrays']['camp_admin_row_amounts_k'][0]=10
    assert f.cond(f.triggers['camp_administration_civil_action_one_available'],'FRA')
    results.append('Reform availability blocks bad rows for major and British/French release while leaving major halt and USA property claims reachable')
    q=Runtime(); q.country(); qs=q.state(population=1000,buildings=4); prime_existing_custody(q,'S1',10)
    legacy_effects=parse((ROOT/'common/scripted_effects/camp_repression_rework_effects.txt').read_text(encoding='utf-8-sig'))
    legacy_triggers=parse((ROOT/'common/scripted_triggers/camp_repression_rework_triggers.txt').read_text(encoding='utf-8-sig'))
    q.effects.update({key:get(legacy_effects,key) for key in ('camp_rework_start_dismantlement','camp_rework_complete_dismantlement')})
    q.triggers.update({key:get(legacy_triggers,key) for key in ('camp_rework_site_can_start_dismantlement','camp_rework_site_can_complete_dismantlement')})
    qs['arrays']['camp_admin_row_amounts_k'][0]=9
    q.run('camp_admin_close_site','S1')
    assert 'camp_admin_closed' not in qs['flags'] and qs['camp_admin_detainees_k']==10 and qs['camp_admin_total_released_k']==0
    integration_effects=parse((ROOT/'common/scripted_effects/camp_administration_integration_effects.txt').read_text(encoding='utf-8-sig'))
    q.effects['camp_admin_integration_close_site']=get(integration_effects,'camp_admin_integration_close_site')
    q.run('camp_admin_integration_close_site','S1')
    assert 'camp_admin_closed' not in qs['flags'] and qs['camp_admin_detainees_k']==10
    q.run('camp_rework_start_dismantlement','S1')
    assert 'camp_rework_site_reforming' not in qs['flags'] and 'camp_rework_site_dismantlement_in_progress' not in qs['flags']
    q.run('camp_rework_complete_dismantlement','S1')
    assert q.temp['camp_rework_dismantlement_completion_accepted']==0
    assert qs['concentration_camp']==4 and 'camp_rework_site_dismantled' not in qs['flags']
    good=Runtime(); good.country(); site=good.state(population=1000,buildings=4); prime_existing_custody(good,'S1',10)
    good.triggers.update({key:get(legacy_triggers,key) for key in ('camp_rework_site_can_start_dismantlement','camp_rework_site_can_complete_dismantlement')})
    assert good.cond(good.triggers['camp_rework_site_can_start_dismantlement'],'S1')
    site['flags'].add('camp_admin_closed')
    assert not good.cond(good.triggers['camp_rework_site_can_complete_dismantlement'],'S1') # Closed with live custody cannot skip release.
    good.country('USA')
    good.root='USA'
    old_target=good.target
    good.target=lambda x,s,prev,old_target=old_target,good=good: good.root if x=='ROOT' else old_target(x,s,prev)
    site['flags'].discard('camp_admin_closed')
    site['controller']='USA'
    good.temp['camp_rework_enemy_liberation']=1
    assert good.cond(good.triggers['camp_rework_site_can_complete_dismantlement'],'S1') # Liberation explicitly releases custody.
    site['flags'].add('camp_admin_closed')
    assert not good.cond(good.triggers['camp_rework_site_can_complete_dismantlement'],'S1') # A finished site is not liberated again.
    site['flags'].discard('camp_admin_closed')
    site['controller']='GER'
    assert not good.cond(good.triggers['camp_rework_site_can_complete_dismantlement'],'S1') # The enemy must still control the site.
    good.root='GER'
    good.temp['camp_rework_enemy_liberation']=0
    good.run('camp_admin_release_survivors','S1')
    assert good.cond(good.triggers['camp_rework_site_can_complete_dismantlement'],'S1')
    prime_existing_custody(good,'S1',10)
    good.run('camp_admin_reform_site','S1')
    assert good.cond(good.triggers['camp_rework_site_can_complete_dismantlement'],'S1')
    site['flags'].discard('camp_admin_initialized')
    assert good.cond(good.triggers['camp_rework_site_can_complete_dismantlement'],'S1') # Pre-cutover path remains.
    results.append('Closure and legacy dismantlement refuse inconsistent custody; closed sites with live survivors cannot certify voluntary completion')
    discovery=Runtime(); discovery.country('USA'); discovery.country('GER'); ds=discovery.state(country='GER',buildings=4)
    discovery.root='USA'
    old_target=discovery.target
    discovery.target=lambda x,s,prev,old_target=old_target,discovery=discovery: discovery.root if x=='ROOT' else old_target(x,s,prev)
    discovery.targets.update(genocide_discovered_state='S1',genocide_responsible_country='GER')
    discovery.scopes['USA']['has_war']=True
    discovery.scopes['GER']['wars']={'USA'}
    ds['controller']='USA'
    discovery.triggers['genocide_country_can_liberate_discovered_camp']=get(parse((ROOT/'common/scripted_triggers/genocide_crisis_triggers.txt').read_text(encoding='utf-8-sig')),'genocide_country_can_liberate_discovered_camp')
    prime_existing_custody(discovery,'S1',10)
    assert discovery.cond(discovery.triggers['genocide_country_can_liberate_discovered_camp'],'USA')
    ds['arrays']['camp_admin_row_amounts_k'][0]=9
    assert not discovery.cond(discovery.triggers['genocide_country_can_liberate_discovered_camp'],'USA')
    ds['arrays']['camp_admin_row_amounts_k'][0]=10
    assert discovery.cond(discovery.triggers['genocide_country_can_liberate_discovered_camp'],'USA')
    ds['flags'].add('camp_admin_closed')
    assert not discovery.cond(discovery.triggers['genocide_country_can_liberate_discovered_camp'],'USA')
    ds['flags'].discard('camp_admin_closed')
    ds['controller']='GER'
    assert not discovery.cond(discovery.triggers['genocide_country_can_liberate_discovered_camp'],'USA')
    discovery.effects['genocide_liberate_discovered_camp']=get(parse((ROOT/'common/scripted_effects/genocide_crisis_effects.txt').read_text(encoding='utf-8-sig')),'genocide_liberate_discovered_camp')
    discovery.run('genocide_liberate_discovered_camp','USA')
    assert discovery.temp['camp_liberation_accepted']==0 and 'camp_rework_liberated_enemy_camp' not in discovery.scopes['USA']['flags'] and ds['concentration_camp']==4
    ds['controller']='USA'
    discovery.scopes['GER']['wars'].clear()
    assert not discovery.cond(discovery.triggers['genocide_country_can_liberate_discovered_camp'],'USA')
    discovery.run('genocide_liberate_discovered_camp','USA')
    assert discovery.temp['camp_liberation_accepted']==0 and 'camp_rework_liberated_enemy_camp' not in discovery.scopes['USA']['flags']
    results.append('Enemy discovery option and execution recheck reject invalid custody, closed sites, lost control and ended war without reward or site demolition')
    dispatch_source=parse((ROOT/'common/scripted_effects/genocide_crisis_effects.txt').read_text(encoding='utf-8-sig'))
    for responsible,state_id,cores,markers,expected in [('GER',88,set(),{'genocide_auschwitz_experiment_site'},'chaosx_genocide.56'),('GER',88,set(),set(),'chaosx_genocide.55'),('GER',43,set(),set(),'chaosx_genocide.55'),('JAP',328,set(),{'genocide_japanese_biowarfare_atrocity_site'},'chaosx_genocide.57'),('JAP',328,set(),set(),'chaosx_genocide.55'),('JAP',325,set(),set(),'chaosx_genocide.55'),('ENG',429,{'RAJ'},set(),'chaosx_genocide.50'),('ENG',116,set(),set(),'chaosx_genocide.55'),('ITA',448,{'LBA'},set(),'chaosx_genocide.53'),('ITA',271,{'ETH'},set(),'chaosx_genocide.55'),('BEL',295,{'COG'},set(),'chaosx_genocide.54'),('BEL',6,set(),set(),'chaosx_genocide.55')]:
        report=Runtime(); report.country(responsible); report.country('USA'); rs=report.state(country=responsible)
        rs['state']=state_id; rs['cores']=cores; rs['flags'].update(markers)
        report.targets.update(genocide_responsible_country=responsible,genocide_discovering_country='USA')
        report.effects['genocide_dispatch_discoverer_report_from_state']=get(dispatch_source,'genocide_dispatch_discoverer_report_from_state')
        report.run('genocide_dispatch_discoverer_report_from_state','S1')
        assert report.temp['last_country_event']==expected,(responsible,state_id,cores,markers,report.temp['last_country_event'])
    results.append('Named Raj, Libya and Congo reports require matching regions; Auschwitz and Pingfang reports also require their actual institution marker')
    colonial_effects=parse((ROOT/'common/scripted_effects/camp_repression_colonial_country_effects.txt').read_text(encoding='utf-8-sig'))
    rework_effects=parse((ROOT/'common/scripted_effects/camp_repression_rework_effects.txt').read_text(encoding='utf-8-sig'))
    # The retired national UK and French dismantlement lifecycle (bulk sunset, closure attempts, legacy closure retry)
    # was removed with its decisions; the live closure paths are covered by the administration reform scenarios.
    import black_friday_sale_prices as sale
    tuning=parse((ROOT/'common/script_constants/camp_repression_rework_constants.txt').read_text(encoding='utf-8-sig'))
    # Fixed order stock is checked at the Event 026 sale price: exactly the quoted
    # amount is enough and one unit short is refused, at full, half and quarter price.
    stock_checks={'camp_rework_can_pay_dismantle_manpower':('manpower',None,'dismantle_manpower','camp_rework_cost'),
                  'camp_rework_can_pay_support_equipment':('equipment','support_equipment_1','support_equipment','camp_rework_equipment_cost'),
                  'camp_rework_can_pay_convoys':('equipment','convoy_1','convoys','camp_rework_equipment_cost')}
    decisions=[('common/decisions/camp_repression_major_country_decisions.txt','germany_dismantle_auschwitz_complex',2),('common/decisions/camp_repression_major_country_decisions.txt','japan_shut_down_prisoner_experiments',2),('common/decisions/camp_repression_major_country_decisions.txt','sov_dismantle_overextended_gulags',2),('common/decisions/camp_repression_generic_decisions.txt','camp_repression_close_dormant_legacy_site',2)]
    for ratio in sale.SALE_RATIOS:
        exact=Runtime(); exact.country('TEST'); sale.install(exact,ratio)
        for file,decision_name,expected in decisions:
            source=parse((ROOT/file).read_text(encoding='utf-8-sig'))
            entry=next(get(category,decision_name) for _,_,category in source if isinstance(category,list) and get(category,decision_name) is not None)
            available=get(entry,'available')
            checks=[key for key,_,value in available if key in stock_checks and value=='yes']
            assert len(checks)==expected,(decision_name,len(checks),expected)
            for check in checks:
                field,kind,cost_key,category=stock_checks[check]
                quoted=sale.price(exact,cost_key,category)
                assert ratio==sale.RATIO_BASIS or quoted<float(get(get(tuning,category),cost_key))
                exact.scopes['TEST'][field]={kind:quoted} if kind else quoted
                assert exact.cond([(check,'=','yes')],'TEST')
                exact.scopes['TEST'][field]={kind:quoted-1} if kind else quoted-1
                assert not exact.cond([(check,'=','yes')],'TEST')
    results.append('Four fixed-cost legacy closure decisions accept exactly the quoted manpower/equipment/convoy stock and reject one unit short, at the full, half and quarter sale price')
    activation_runs=[]
    for ratio in sale.SALE_RATIOS:
        activation=Runtime(); activation.country('TEST'); sale.install(activation,ratio)
        activation.triggers['camp_rework_generic_activation_resources_ready']=get(legacy_triggers,'camp_rework_generic_activation_resources_ready')
        actor=activation.scopes['TEST']
        actor['manpower']=sale.price(activation,'activation_manpower')
        actor['command_power']=sale.price(activation,'activation_command')
        actor['equipment']={'support_equipment_1':sale.stock(activation,'support_equipment')}
        ready=[('camp_rework_generic_activation_resources_ready','=','yes')]
        assert activation.cond(ready,'TEST')
        for key,resource in [('manpower',None),('command_power',None),('equipment','support_equipment_1')]:
            if resource:
                actor[key][resource]-=1
            else:
                actor[key]-=1
            assert not activation.cond(ready,'TEST'),key
            if resource:
                actor[key][resource]+=1
            else:
                actor[key]+=1
        activation_runs.append((activation,actor))
    generic=parse((ROOT/'common/decisions/camp_repression_generic_decisions.txt').read_text(encoding='utf-8-sig'))
    activation_decision=next(get(category,'generic_activate_detention_network') for _,_,category in generic if isinstance(category,list) and get(category,'generic_activate_detention_network') is not None)
    assert 'camp_rework_generic_activation_resources_ready' in str(get(activation_decision,'custom_cost_trigger'))
    assert 'camp_rework_generic_activation_resources_ready' in str(get(activation_decision,'available'))
    activation_weights=get(activation_decision,'ai_will_do')
    activation_modifiers=[value for key,_,value in activation_weights if key=='modifier']
    assert get(activation_modifiers[-1],'factor')=='0'
    assert 'camp_rework_country_under_ai_site_cap' in str(activation_modifiers[-1])
    assert all(get(value,'add') is not None for value in activation_modifiers[:2])
    ai_cap=str(get(legacy_effects,'camp_rework_apply_ai_cap'))
    assert "('NOT', '=', [('has_manpower', '<', 'constant:camp_rework_cost.activation_manpower')])" in ai_cap
    activation_loc=parse((ROOT/'common/scripted_localisation/camp_repression_ui_scripted_localisation.txt').read_text(encoding='utf-8-sig'))
    for activation,actor in activation_runs:
        for getter,key,resource in [('GetCampUiActivationManpower','manpower',None),('GetCampUiActivationCommand','command_power',None),('GetCampUiActivationSupportCost','equipment','support_equipment_1')]:
            definition=next(block for name,_,block in activation_loc if name=='defined_text' and get(block,'name')==getter)
            red_trigger=get(get(definition,'text'),'trigger')
            assert not activation.cond(red_trigger,'TEST'),getter
            if resource:
                actor[key][resource]-=1
            else:
                actor[key]-=1
            assert activation.cond(red_trigger,'TEST'),getter
            if resource:
                actor[key][resource]+=1
            else:
                actor[key]+=1
    ui_loc=(ROOT/'localisation/english/camp_repression_ui_l_english.yml').read_text(encoding='utf-8-sig')
    assert '[GetCampUiActivationSupportCost]' in ui_loc.split('camp_ui_cost_activation:',1)[1].split('\n',1)[0]
    assert '[GetCampUiEvidenceManpower]' in ui_loc.split('camp_ui_directive_cost_evidence:',1)[1].split('\n',1)[0]
    rework_loc=(ROOT/'localisation/english/camp_repression_rework_l_english.yml').read_text(encoding='utf-8-sig')
    blocked=rework_loc.split('camp_cost_activation_non_pp_blocked:',1)[1].split('\n',1)[0]
    assert all('['+getter+']' in blocked for getter in ('GetCampUiActivationManpower','GetCampUiActivationCommand','GetCampUiActivationSupportCost'))
    activation_hover=rework_loc.split('camp_cost_activation_non_pp_tooltip:',1)[1].split('\n',1)[0]
    # The hover shows the Event 026 sale price that the decision charges, not the ordinary constant.
    assert all('global.black_friday_price_'+key.replace('.','_') in activation_hover for key in ('camp_rework_cost.activation_pp','camp_rework_cost.activation_manpower','camp_rework_cost.activation_command','camp_rework_equipment_cost.support_equipment')),activation_hover
    results.append('Generic activation accepts exact manpower, command and support sale quotes in decision, Ledger and UI at full, half and quarter price, rejecting one unit short; the AI capacity heuristic keeps the ordinary thresholds')
    ui=Runtime(); ui.country('GER'); selected=ui.state(country='GER')
    ui.root='GER'
    old_target=ui.target
    ui.target=lambda x,s,prev,old_target=old_target,ui=ui: ui.root if x=='ROOT' else old_target(x,s,prev)
    ui.triggers.update({key:value for key,_,value in legacy_triggers if key.startswith('camp_rework_selected_dismantle_') or key in ('camp_rework_can_dismantle_selected_site','camp_rework_legacy_closure_site_can_begin','camp_rework_site_can_start_dismantlement','camp_rework_state_is_actor_or_subject_controlled')})
    ui.triggers['camp_rework_country_can_reform']=[('has_country_flag','=','reform_route_test')]
    ui.triggers['is_valid_camp_dismantlement_state']=[('has_state_flag','=','camp_rework_site_active')]
    ui.triggers['camp_rework_can_pay_site_dismantle']=[('check_variable','=',[('political_power','>','0')])]
    variants=['camp_rework_selected_dismantle_locked_site','camp_rework_selected_dismantle_locked_route','camp_rework_selected_dismantle_locked_progress','camp_rework_selected_dismantle_locked_custody','camp_rework_selected_dismantle_locked_resources','camp_rework_can_dismantle_selected_site']
    def visible_variant(): return [name for name in variants if ui.cond(ui.triggers[name],'GER')]
    assert visible_variant()==['camp_rework_selected_dismantle_locked_site']
    ui.scopes['GER']['camp_selected_state_id']='S1'
    assert visible_variant()==['camp_rework_selected_dismantle_locked_route']
    ui.scopes['GER']['flags'].add('reform_route_test')
    selected['flags'].add('camp_rework_site_reforming')
    assert visible_variant()==['camp_rework_selected_dismantle_locked_progress']
    selected['flags'].discard('camp_rework_site_reforming')
    prime_existing_custody(ui,'S1',10)
    selected['arrays']['camp_admin_row_amounts_k'][0]=9
    assert visible_variant()==['camp_rework_selected_dismantle_locked_custody']
    selected['arrays']['camp_admin_row_amounts_k'][0]=10
    ui.scopes['GER']['political_power']=0
    assert visible_variant()==['camp_rework_selected_dismantle_locked_resources']
    ui.scopes['GER']['political_power']=100
    assert visible_variant()==['camp_rework_can_dismantle_selected_site']
    gui_script=parse((ROOT/'common/scripted_guis/camp_repression_ledger_scripted_gui.txt').read_text(encoding='utf-8-sig'))
    window=get(get(get(gui_script,'scripted_gui'),'camp_repression_ledger_scripted_gui'),'effects')
    assert 'camp_rework_action.dismantle_selected_site' in str(get(window,'camp_admin_site_dismantle_click'))
    layout=(ROOT/'interface/camp_repression_ledger.gui').read_text(encoding='utf-8-sig')
    for key in ('camp_admin_site_dismantle','camp_admin_site_dismantle_locked_site','camp_admin_site_dismantle_locked_route','camp_admin_site_dismantle_locked_progress','camp_admin_site_dismantle_locked_custody','camp_admin_site_dismantle_locked_resources'):
        assert layout.count('name = "'+key+'"')==1,key
    results.append('Locations selected-site dismantlement partitions five locked reasons and one active command, with exactly one native button and dispatcher entry')
    assert 'camp_rework_cancel_selected_dismantlement_on_terminal' in str(get(rework_effects,'camp_rework_exclude_special_country'))
    assert 'camp_rework_cancel_selected_dismantlement_on_terminal' in str(get(rework_effects,'camp_rework_on_country_annexed'))
    results.append('Monthly frozen-policy cleanup leaves selected-site closure mission active; only terminal country cleanup cancels it')
    assert 'camp_rework_timing.dismantle_flag_grace_days' in str(get(rework_effects,'camp_rework_start_dismantlement'))
    assert 'camp_rework_timing.dismantle_flag_grace_days' in str(get(rework_effects,'camp_rework_rearm_dismantlement_site'))
    results.append('The site progress flag lasts beyond the mission deadline on first start and retry, avoiding a same-day cancellation race')
    for year,expected in [(1940,[1,1,0]),(1941,[1])]:
        r.date=datetime.date(year,1,1)
        for ok in expected:
            c['flags'].add('camp_admin_institution_slot_active'); r.temp.update(camp_admin_research_requested_bonus=2,camp_admin_research_contract=1,camp_admin_research_program_valid=1)
            r.run('camp_admin_try_claim_research_award','GER'); assert r.temp['camp_admin_research_award_accepted']==ok
            if ok: assert r.temp['camp_admin_research_award_bonus']==1
    results.append('Independent institution slot, bounded bonus and shared two-per-calendar-year award cap')
    for cohort in (1000,7000):
        q=Runtime(); qc=q.country(support=100000)
        for n in range(int(cohort/200)):
            key='S'+str(n+1); qs=q.state(key,population=1000,buildings=5,factories=20); qs['camp_admin_development_level']=3
            q.temp.update(camp_admin_admission_requested_k=200,camp_admin_admission_source_k=200,camp_admin_admission_proven=1)
            q.run('camp_admin_admit_detainees',key); assert qs['camp_admin_capacity_k']==200
        q.run('camp_admin_pay_monthly_maintenance','GER')
        assert all(q.scopes[key]['camp_admin_support_ratio']==1 for key in qc['arrays']['camp_active_site_states']) and qc['support']==100000-cohort*.5
    results.append('1M/7M obligations distributed over legal five-level, fully developed sites receive full maintenance when stocks cover them')
    q=Runtime(); qc=q.country(support=10000,factories=100)
    for n in range(5):
        key='S'+str(n+1); qs=q.state(key,population=1000,buildings=5,factories=20); qs['camp_admin_development_level']=3
        q.temp.update(camp_admin_admission_requested_k=200,camp_admin_admission_source_k=200,camp_admin_admission_proven=1)
        q.run('camp_admin_admit_detainees',key)
    qc['camp_admin_mandate']=2
    q.run('camp_admin_pay_monthly_maintenance','GER'); q.run('camp_admin_refresh_country_economy','GER')
    assert qc['camp_admin_total_detainees_k']==1000 and qc['camp_admin_industrial_factor']==.25
    results.append('Five legal 200k developed sites, source-admitted 1M people and 100 participating factories reach the 25 percent country cap')
    q.country('ENEMY')
    for key in list(qc['arrays']['camp_active_site_states']):
        qs=q.scopes[key]; qs['controller']='ENEMY'; before=qs['state_population_k']; q.run('camp_admin_close_site',key)
        assert qs['camp_admin_responsible_country']=='GER' and qs['state_population_k']==before
        q.run('camp_admin_reopen_site',key); assert 'camp_admin_closed' in qs['flags']
    assert qc['camp_admin_industrial_factor']==0
    results.append('Capture removes national output immediately, preserves responsibility and rejects foreign reopening')
    q=Runtime(); q.country(); qs=q.state(population=10,buildings=1)
    qs['camp_occ_remaining_k']=9
    q.temp.update(camp_admin_admission_requested_k=2,camp_admin_admission_source_k=2,camp_admin_admission_proven=1)
    q.run('camp_admin_admit_detainees','S1'); assert q.temp['camp_admin_admission_accepted_k']==0
    qs['camp_occ_remaining_k']=0; prime_existing_custody(q,'S1',9)
    q.temp.update(camp_admin_death_requested_k=99,camp_admin_death_cause=1,camp_admin_death_contract=1)
    q.run('camp_admin_record_deaths','S1'); assert qs['state_population_k']==1 and qs['camp_admin_detainees_k']==0 and q.logged==9
    results.append('Occupation membership is excluded from admission; shared protected floor bounds an oversized loss request')
    q=Runtime(); qc=q.country(support=10000); qs=q.state(population=1000,buildings=4,factories=10)
    qc['camp_admin_mandate']=2; qc['camp_admin_budget']=2; prime_existing_custody(q,'S1',80)
    for month in range(1,10): q.date=datetime.date(1938,month,1); q.run('camp_admin_monthly_country','GER')
    assert qs['camp_admin_development_level']==3 and 'camp_admin_economy_slot_active' not in qc['flags']
    assert qc['support']<10000-360 and qs['camp_admin_capacity_k']==175
    results.append('Nine supported automatic months complete three work-based paid upgrades and add capacity without any automatic admission')
    durations={}
    for name,cohort,stage,factories in [('small_workforce',5,0,10),('supported_workforce',80,0,10),('developed_stage',80,2,10),('large_project',80,0,50)]:
        q=Runtime(); qc=q.country(support=10000); qs=q.state(population=1000,buildings=5,factories=factories)
        qc['camp_admin_mandate']=2; qc['camp_admin_budget']=2; qs['camp_admin_development_level']=stage
        q.temp.update(camp_admin_admission_requested_k=cohort,camp_admin_admission_source_k=cohort,camp_admin_admission_proven=1); q.run('camp_admin_admit_detainees','S1')
        target=None
        for tick in range(36):
            q.date=datetime.date(1938+tick//12,tick%12+1,1); q.run('camp_admin_monthly_country','GER')
            if target is None: target=qc['camp_admin_economy_target']
            if qs['camp_admin_development_level']>stage: durations[name]={'months':tick+1,'target_work':round(target,3)}; break
        assert name in durations
    assert durations['small_workforce']['months']>durations['supported_workforce']['months']
    assert durations['developed_stage']['months']>durations['supported_workforce']['months']
    assert durations['large_project']['months']>durations['supported_workforce']['months']
    results.append({'scenario':'Supplied work and frozen physical/stage targets produce distinct durations','outcomes':durations})
    q=Runtime(); qc=q.country(support=10000); qs=q.state(population=1000,buildings=5,factories=10)
    qc['camp_admin_mandate']=2; qc['camp_admin_budget']=2; prime_existing_custody(q,'S1',5)
    q.run('camp_admin_monthly_country','GER'); progress=qc['camp_admin_economy_progress']; target=qc['camp_admin_economy_target']; first_rate=qc['camp_admin_economy_work_rate']
    assert 0<progress<1
    q.temp['camp_admin_release_requested_k']=qs['camp_admin_detainees_k']/2; q.run('camp_admin_release_detainees','S1')
    q.date=datetime.date(1938,2,1); q.run('camp_admin_monthly_country','GER')
    assert progress<qc['camp_admin_economy_progress']<progress+first_rate and qc['camp_admin_economy_target']==target
    progress=qc['camp_admin_economy_progress']; qc['support']=100; q.run('camp_admin_pay_monthly_maintenance','GER'); q.run('camp_admin_progress_economy_project','GER')
    assert qc['camp_admin_economy_progress']==progress and qc['support']==100
    qc['support']=10000; q.run('camp_admin_pay_monthly_maintenance','GER'); q.run('camp_admin_release_survivors','S1'); stock=qc['support']; q.run('camp_admin_progress_economy_project','GER')
    assert qc['camp_admin_economy_progress']==progress and qc['camp_admin_economy_work_rate']==0 and qc['support']==stock
    results.append('Fractional supplied work persists through reduced workforce, shortage and zero-worker interruption; zero work spends nothing')
    qs['camp_admin_development_level']=99; q.run('camp_admin_refresh_capacity','S1'); assert qs['camp_admin_development_level']==3 and qs['camp_admin_capacity_k']==200
    results.append('Development is clamped before capacity arithmetic; a legal five-level site cannot exceed its 200k developed capacity')
    # Execute the production generic order through its row preflight and debit.
    # Only the external occupation/lifecycle consumers are mocked after payment.
    integration=parse((ROOT/'common/scripted_effects/camp_administration_integration_effects.txt').read_text(encoding='utf-8-sig'))
    generic_order=get(integration,'camp_admin_generic_reform')
    assert generic_order is not None
    rows=Runtime(); rows.country('HUN'); site=rows.state('H1','HUN'); prime_existing_custody(rows,'H1',10)
    reconciled=rows.triggers['camp_admin_site_rows_reconciled']
    assert rows.cond(reconciled,'H1')
    site['arrays']['camp_admin_row_amounts_k'][0]=9; assert not rows.cond(reconciled,'H1')
    site['arrays']['camp_admin_row_amounts_k'][0]=10; assert rows.cond(reconciled,'H1')
    site['arrays']['camp_admin_row_authorities'][0]='FOREIGN'; assert not rows.cond(reconciled,'H1')
    site['arrays']['camp_admin_row_authorities'][0]='HUN'; site['arrays']['camp_admin_row_statuses'][0]=0; assert not rows.cond(reconciled,'H1')
    site['arrays']['camp_admin_row_statuses'][0]=1; site['arrays']['camp_admin_row_origins'].pop(); assert not rows.cond(reconciled,'H1')
    gate=Runtime(); gate.country('HUN'); one=gate.state('G1','HUN'); prime_existing_custody(gate,'G1',10)
    integration_triggers=parse((ROOT/'common/scripted_triggers/camp_administration_integration_triggers.txt').read_text(encoding='utf-8-sig'))
    gate.triggers.update({k:v for k,o,v in integration_triggers})
    for helper in ('camp_admin_generic_reform_visible','camp_admin_generic_reform_can_pay','is_valid_camp_dismantlement_state'):
        gate.triggers[helper]=[] # Engine route and quote primitives are outside this row/authority test.
    available=gate.triggers['camp_admin_generic_reform_available']
    assert gate.cond(available,'HUN')
    one['arrays']['camp_admin_row_amounts_k'][0]=9; assert not gate.cond(available,'HUN')
    one['arrays']['camp_admin_row_amounts_k'][0]=10; assert gate.cond(available,'HUN')
    two=gate.state('G2','HUN'); prime_existing_custody(gate,'G2',4)
    two['arrays']['camp_admin_row_amounts_k'][0]=3; assert not gate.cond(available,'HUN')
    two['arrays']['camp_admin_row_amounts_k'][0]=4; assert gate.cond(available,'HUN')
    gate.country('SLO'); gate.scopes['SLO']['overlord']='HUN'; two['controller']='SLO'
    assert not gate.cond(available,'HUN')
    two['flags'].add('camp_admin_subject_authority'); assert gate.cond(available,'HUN')
    # Agent decision 2026-10-04: a sticky provenance host closes with incomplete
    # records, so its ledger no longer gates the national order.
    two['arrays']['camp_admin_row_amounts_k'][0]=3; assert not gate.cond(available,'HUN')
    two['flags'].add('camp_origin_ambiguous'); assert gate.cond(available,'HUN')
    two['flags'].discard('camp_origin_ambiguous'); two['arrays']['camp_admin_row_amounts_k'][0]=4
    import black_friday_sale_prices as sale
    def generic_fixture(corrupt=None,ratio=sale.RATIO_BASIS):
        g=Runtime(); country=g.country('HUN'); first=g.state('H1','HUN'); prime_existing_custody(g,'H1',10)
        sale.install(g,ratio)
        if corrupt=='first': first['arrays']['camp_admin_row_amounts_k'][0]=9
        if corrupt in ('second','sticky'):
            second=g.state('H2','HUN'); prime_existing_custody(g,'H2',4)
            second['arrays']['camp_admin_row_amounts_k'][0]=3
            if corrupt=='sticky': second['flags'].add('camp_origin_counter_regressed')
        country['camp_active_site_count']=len(country['arrays']['camp_active_site_states'])
        g.effects['camp_admin_generic_reform']=generic_order
        # Availability is tested above; the paid effect reads the production sale-priced quote.
        g.triggers['camp_admin_generic_reform_quote']=get(integration_triggers,'camp_admin_generic_reform_quote')
        g.triggers['camp_admin_generic_reform_available']=[('camp_admin_generic_reform_quote','=','yes')]
        for consumer in ('camp_admin_integration_record_site_history','camp_occ_close_country','camp_admin_begin_reform','camp_rework_unregister_inactive_site','camp_rework_refresh_country_specific_ideas','camp_rework_rebuild_display_values'):
            g.effects[consumer]=[]
        g.run('camp_admin_generic_reform','HUN')
        return g,country
    for ratio in sale.SALE_RATIOS:
        one_site=sale.production_quote(15.75,ratio); two_sites=sale.production_quote(16.5,ratio)
        good,gc=generic_fixture(ratio=ratio); assert abs(gc['political_power']-(100-one_site))<1e-8 and good.temp['camp_admin_generic_release_rows_ready']==1 and sale.credits(good)==1
        bad,bc=generic_fixture('first',ratio); assert bc['political_power']==100 and bad.temp['camp_admin_generic_release_rows_ready']==0 and sale.credits(bad)==0
        mixed,mc=generic_fixture('second',ratio); assert mc['political_power']==100 and mixed.temp['camp_admin_generic_release_rows_ready']==0 and sale.credits(mixed)==0
        sticky,sc=generic_fixture('sticky',ratio); assert abs(sc['political_power']-(100-two_sites))<1e-8 and sticky.temp['camp_admin_generic_release_rows_ready']==1 and sale.credits(sticky)==1
    results.append('Generic national reform charges the Event 026 sale price of its site-scaled quote (15.75 PP for one site, 16.5 for two at full price) and credits one purchase only when it pays')
    results.append('Generic national reform availability rejects mismatched, foreign-authority, inactive-live and misaligned custody rows; effect-time checks prevent payment if a one-site or two-site ledger changes before execution')
    results.append('A sticky provenance host does not gate the generic national order: availability and the paid effect accept it because reform closes that host with incomplete records')
    paid=sale.check_native_costs()
    assert len(paid)==18,len(paid)
    results.append('Event 026 sale: all 18 positive native camp costs (16 camp decisions and the two partner halt actions) read a registered price-table global and each order credits one purchase')
    sale.check_stock_prices()
    results.append('Event 026 sale: no camp purchase check compares stock with an ordinary price; only the AI capacity heuristic keeps ordinary thresholds')
    for ratio in sale.SALE_RATIOS:
        for ordinary in (1, 6, 18, 25, 45, 120, 180, 650, 1200, 10000, 15.75):
            mirror=Runtime(); mirror.country('TEST'); sale.install(mirror,ratio)
            mirror.temp.update(camp_sale_ordinary=ordinary)
            assert mirror.cond([('camp_rework_sale_quote','=','yes')],'TEST')
            assert mirror.temp['camp_sale_payable']==sale.production_quote(ordinary,ratio),(ordinary,ratio)
        unbuilt=Runtime(); unbuilt.country('TEST'); sale.install(unbuilt,ratio,table_built=False)
        unbuilt.temp.update(camp_sale_ordinary=45)
        assert unbuilt.cond([('camp_rework_sale_quote','=','yes')],'TEST') and unbuilt.temp['camp_sale_payable']==45
    results.append('The trigger-side camp sale quote equals the production table quote at full, half and quarter price, and charges the full price before the table is first built')
    return results

if __name__=='__main__':
    result=tests()
    print(json.dumps({'status':'passed','source_scenarios':result,'limits':'Engine primitives are deterministic mocks; no live game, native save, GUI, AI or historical calibration proof.'},indent=2))
