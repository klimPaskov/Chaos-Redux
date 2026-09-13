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
        for path in ['common/scripted_effects/camp_administration_effects.txt','common/scripted_effects/chaosx_dynamic_effects.txt']:
            self.effects.update({k:v for k,o,v in parse((ROOT/path).read_text(encoding='utf-8-sig'))})
        self.triggers.update({k:v for k,o,v in parse((ROOT/'common/scripted_triggers/camp_administration_triggers.txt').read_text())})
        for path in ['common/script_constants/camp_administration_constants.txt','common/script_constants/chaos_meter_deaths_constants.txt']:
            if not (ROOT/path).exists(): continue
            for cat,o,b in parse((ROOT/path).read_text()):
                if isinstance(b,list):
                    for k,o,v in b:
                        if k!='schema' and not isinstance(v,list): self.constants[cat+'.'+k]=float(v)
        # External reason enum value is immaterial to conservation arithmetic.
        self.constants.setdefault('chaos_meter_deaths_reason.camp_atrocity',1)
        for k,v in [('zero',0),('one',1),('people_per_k',1000),('negative_one',-1)]: self.constants.setdefault('chaos_meter_deaths.'+k,v)
        self.constants.setdefault('chaos_meter_deaths_reason.unknown',0)

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
        if x.endswith('.id'): return self.target(x[:-3],s,prev)
        if x.startswith('PREV.'): return self.val(x[5:],prev,s)
        if x.startswith('event_target:') or x in ('THIS','OWNER','CONTROLLER','PREV'): return self.target(x,s,prev)
        if x.endswith('^num'): return len(self.scopes[s]['arrays'].get(x[:-4],[]))
        if x in self.temp: return self.temp[x]
        if x.startswith(('building_level@','non_damaged_building_level@')): return self.scopes[s].get(x.split('@')[1],0)
        if x=='infrastructure_level': return self.scopes[s].get('infrastructure',0)
        if x=='num_equipment@support_equipment': return self.scopes[s]['support']
        return self.scopes[s].get(x,0)

    def cond(self,b,s,prev=None):
        def one(k,o,v):
            if k in ('AND','OR','NOT'):
                values=[one(a,c,d) for a,c,d in v]
                return all(values) if k=='AND' else any(values) if k=='OR' else not all(values)
            if k in self.triggers: return self.cond(self.triggers[k],s,prev)==(v=='yes')
            if k in ('camp_rework_country_is_eligible','camp_rework_country_can_use_radicalized_route','camp_admin_country_can_radicalize'): return self.scopes[s].get('eligible',True)==(v=='yes')
            if k=='check_variable':
                if get(v,'var') is not None: a=self.val(get(v,'var'),s,prev); c=self.val(get(v,'value'),s,prev); op=get(v,'compare','equals')
                else: key,op,value=v[0]; a=self.val(key,s,prev); c=self.val(value,s,prev)
                return {'=':lambda:a==c,'equals':lambda:a==c,'>':lambda:a>c,'<':lambda:a<c,'greater_than_or_equals':lambda:a>=c,'less_than_or_equals':lambda:a<=c}[op]()
            if k=='has_variable': return v in self.temp or v in self.scopes[s]
            if k=='has_global_flag': return v in self.global_flags
            if k in ('has_state_flag','has_country_flag'): return v in self.scopes[s]['flags']
            if k=='is_controlled_by': return self.scopes[s]['controller']==self.target(v,s,prev)
            if k=='is_subject_of': return self.scopes[s].get('overlord')==self.target(v,s,prev)
            if k=='has_government': return self.scopes[s]['government']==v
            if k=='exists': return self.scopes[s].get('exists',True)==(v=='yes')
            if k=='is_in_array': return self.target(get(v,'value'),s,prev) in self.scopes[s]['arrays'].get(get(v,'array'),[])
            if k=='date':
                d=datetime.date(*map(int,v.split('.'))); return self.date<d if o=='<' else self.date>d
            if k=='tag': return s==self.target(v,s,prev)
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
            elif k=='camp_rework_record_latest_state_deaths': pass # External projection only, not a physical primitive.
            elif k in self.effects: self.run(k,s,{a:c for a,o,c in v} if isinstance(v,list) else {},prev)
            elif k=='meta_effect':
                text=get(v,'text'); year=str(self.date.year)
                def year_replace(z): return [(a,o,year_replace(c) if isinstance(c,list) else c.replace('[YEAR]',year)) for a,o,c in z]
                self.execute(year_replace(text),s,prev)
            elif k=='for_each_scope_loop':
                assert get(v,'limit') is None,'Unsupported direct loop limit'
                for dst in list(self.scopes[s]['arrays'].get(get(v,'array'),[])): self.execute([x for x in v if x[0]!='array'],dst,s)
            elif k=='save_event_target_as': self.targets[v]=s
            elif k in ('set_country_flag','set_state_flag'): self.scopes[s]['flags'].add(v)
            elif k in ('clr_country_flag','clr_state_flag'): self.scopes[s]['flags'].discard(v)
            elif k in ('clear_variable','clear_temp_variable'): (self.temp if k=='clear_temp_variable' else self.scopes[s]).pop(v,None)
            elif k in ('add_dynamic_modifier','remove_dynamic_modifier'):
                getattr(self.scopes[s]['mods'],'add' if k.startswith('add') else 'discard')(get(v,'modifier'))
            elif k=='add_to_array': self.scopes[s]['arrays'].setdefault(get(v,'array'),[]).append(self.target(get(v,'value'),s,prev))
            elif k=='add_equipment_to_stockpile': self.scopes[s]['support']+=self.val(get(v,'amount'),s,prev)
            elif k=='add_political_power': self.scopes[s]['political_power']+=self.val(v,s,prev)
            elif k=='add_building_construction': self.scopes[s][get(v,'type')]=self.scopes[s].get(get(v,'type'),0)+self.val(get(v,'level'),s,prev)
            elif 'variable' in k:
                target=self.temp if 'temp' in k else self.scopes[s]
                if k.startswith('round_'): target[v]=math.floor(self.val(v,s,prev)+.5)
                elif k.startswith('clamp_'):
                    key=get(v,'var'); target[key]=max(self.val(get(v,'min','-1000000000'),s,prev),min(self.val(key,s,prev),self.val(get(v,'max','1000000000'),s,prev)))
                else:
                    key,_,value=v[0]; value=self.val(value,s,prev); old=target.get(key,0)
                    if k.startswith('set_'): target[key]=value
                    elif k.startswith('add_to_'): target[key]=old+value
                    elif k.startswith('subtract_from_'): target[key]=old-value
                    elif k.startswith('multiply_'): target[key]=old*value
                    elif k.startswith('divide_'): target[key]=old/value
                    else: raise NotImplementedError(k)
            elif isinstance(v,list): self.execute(v,self.target(k,s,prev),s)
            else: raise NotImplementedError(k)

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
    qs['camp_occ_remaining_k']=0; qs['camp_admin_detainees_k']=9
    q.temp.update(camp_admin_death_requested_k=99,camp_admin_death_cause=1,camp_admin_death_contract=1)
    q.run('camp_admin_record_deaths','S1'); assert qs['state_population_k']==1 and qs['camp_admin_detainees_k']==0 and q.logged==9
    results.append('Occupation membership is excluded from admission; shared protected floor bounds an oversized loss request')
    q=Runtime(); qc=q.country(support=10000); qs=q.state(population=1000,buildings=4,factories=10)
    qc['camp_admin_mandate']=2; qc['camp_admin_budget']=2; qs['camp_admin_detainees_k']=80
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
    qc['camp_admin_mandate']=2; qc['camp_admin_budget']=2; qs['camp_admin_detainees_k']=5
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
    return results

if __name__=='__main__':
    result=tests()
    print(json.dumps({'status':'passed','source_scenarios':result,'limits':'Engine primitives are deterministic mocks; no live game, native save, GUI, AI or historical calibration proof.'},indent=2))
