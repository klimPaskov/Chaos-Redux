"""Execute current country/foundation source for finite intake, gates and paid awards.
Engine values and add_tech_bonus are explicit mocks; this is not engine proof.
"""
from pathlib import Path
import datetime, json
from foundation_source_tests import Runtime, parse, get

ROOT = Path(__file__).resolve().parents[4]

class CountryRuntime(Runtime):
    def __init__(self):
        super().__init__()
        for name in ('camp_administration_country_effects','camp_administration_country_census_effects'):
            self.effects.update({k:v for k,o,v in parse((ROOT/f'common/scripted_effects/{name}.txt').read_text())})
        self.effects.update({k:v for k,o,v in parse((ROOT/'common/scripted_effects/camp_administration_ui_effects.txt').read_text())})
        # Read-only GUI projection is outside the payment/policy contract under test.
        self.effects['camp_admin_refresh_interface']=[]
        self.triggers.update({k:v for k,o,v in parse((ROOT/'common/scripted_triggers/camp_administration_ui_triggers.txt').read_text())})
        self.triggers.update({k:v for k,o,v in parse((ROOT/'common/scripted_triggers/camp_administration_country_triggers.txt').read_text())})
        for cat,o,b in parse((ROOT/'common/script_constants/camp_administration_country_constants.txt').read_text()):
            for k,o,v in b:
                if k!='schema': self.constants[cat+'.'+k]=float(v)
        for cat,o,b in parse((ROOT/'common/script_constants/camp_administration_civil_constants.txt').read_text()):
            for k,o,v in b:
                if k!='schema': self.constants[cat+'.'+k]=float(v)
        for cat,o,b in parse((ROOT/'common/script_constants/camp_administration_ui_constants.txt').read_text()):
            for k,o,v in b:
                if k!='schema': self.constants[cat+'.'+k]=float(v)
        self.awards=[]

    def cond(self,b,s,prev=None):
        def one(k,o,v):
            c=self.scopes[s]
            if k in ('AND','OR','NOT'):
                values=[one(a,p,z) for a,p,z in v]
                return all(values) if k=='AND' else any(values) if k=='OR' else not all(values)
            if k in self.triggers: return self.cond(self.triggers[k],s,prev)==(v=='yes')
            if k=='original_tag': return c.get('original_tag',s)==v
            if k=='state': return s==v
            if k=='has_country_leader_ideology': return c.get('leader_ideology','nazism')==v
            if k=='has_war': return c.get('war',False)==(v=='yes')
            if k=='is_ai': return c.get('ai',False)==(v=='yes')
            if k=='is_core_of': return v in c.get('cores',set())
            if k=='has_tech_bonus': return get(v,'category') in c.get('held_bonuses',set())
            if k=='has_equipment': return self.cond([('check_variable','=',[('num_equipment@support_equipment',v[0][1],v[0][2])])],s,prev)
            if k=='any_of_scopes': return any(self.cond([x for x in v if x[0]!='array'],target,s) for target in c['arrays'].get(get(v,'array'),[]))
            if k=='sov_camp_is_reform_route': return ('sov_reform' in c['flags'])==(v=='yes')
            if k=='camp_administration_civil_country_supported': return False
            return super(CountryRuntime,self).cond([(k,o,v)],s,prev)
        return all(one(k,o,v) for k,o,v in b)

    def execute(self,b,s,prev=None):
        # add_tech_bonus is an engine consumer: retain its exact category, name and receipt.
        for i,(k,o,v) in enumerate(b):
            if k=='meta_effect' and get(get(v,'text',[]),'add_tech_bonus') is not None:
                super().execute(b[:i],s,prev)
                bonus=get(get(v,'text'),'add_tech_bonus')
                self.awards.append({'country':s,'name':get(bonus,'name'),'category':get(bonus,'category'),'uses':int(get(bonus,'uses')),'bonus':self.temp['camp_admin_research_award_bonus']})
                self.scopes[s].setdefault('held_bonuses',set()).add(get(bonus,'category'))
                self.execute(b[i+1:],s,prev)
                return
        super().execute(b,s,prev)

def new_country(tag='GER',date=(1936,1,1)):
    r=CountryRuntime(); r.date=datetime.date(*date); c=r.country(tag)
    c['government']='communism' if tag=='SOV' else 'fascism'
    c.update(camp_admin_country_sponsor=1,camp_admin_country_authority_pressure=0,camp_admin_budget=2,camp_admin_mandate=2,camp_admin_country_program=0)
    return r,c

def tests():
    results=[]
    r,c=new_country(); a=r.state('A',population=100,buildings=2); b=r.state('B',population=100,buildings=2)
    for s in (a,b): s['flags'].discard('camp_rework_expanded_labor_site'); s['cores']={'GER'}
    r.run('camp_admin_country_prepare_census','GER')
    assert a['camp_admin_detainees_k']==2 and b['camp_admin_detainees_k']==2
    before=a['state_population_k']+b['state_population_k']
    r.run('camp_admin_country_prepare_census','GER'); assert c['camp_admin_country_cumulative_intake_k']==4
    a['camp_admin_role']=1; r.run('camp_admin_country_prepare_census','GER'); assert a['camp_admin_role']==1
    r.run('camp_admin_release_survivors','A'); r.run('camp_admin_country_prepare_census','GER')
    assert a['camp_admin_detainees_k']==0 and c['camp_admin_country_cumulative_intake_k']==4
    assert before==a['state_population_k']+b['state_population_k']
    results.append('German finite equal-host enrollment, replay and release conservation')

    r,c=new_country('SOV'); a=r.state('A','SOV',population=100,buildings=0); a.update(gulag_labor_camp_network=2,camp_occ_remaining_k=98)
    a['cores']={'SOV'}; r.run('camp_admin_country_prepare_census','SOV')
    assert a['camp_admin_detainees_k']==1 and c['camp_admin_country_cumulative_intake_k']==1
    results.append('Soviet enrollment excludes the existing noncustodial occupation pool')

    r,c=new_country('JAP',(1939,1,1)); r.country('MAN'); r.scopes['MAN']['overlord']='JAP'
    p=r.state('328','JAP',population=100,buildings=0); p['controller']='MAN'; p['flags'].update({'camp_rework_pingfang_anchor','camp_rework_experiment_site'}); p['cores']={'MAN'}
    assert not r.cond([('camp_admin_site_is_operational','=','yes')],'328')
    r.run('camp_admin_country_prepare_census','JAP')
    assert p['camp_admin_detainees_k']==3 and 'camp_admin_subject_authority' in p['flags']
    r.scopes['MAN'].pop('overlord'); assert not r.cond([('camp_admin_site_is_operational','=','yes')],'328')
    results.append('Named Pingfang subject institution requires a current MAN–JAP relationship')
    r.scopes['MAN']['overlord']='JAP'; c['war']=True
    assert not r.cond([('camp_admin_program_jap_transport_open','=','yes')],'JAP')
    works=r.state('716','JAP',population=1000,buildings=0); works['controller']='MAN'; works['cores']={'MAN'}; works['flags'].add('camp_admin_subject_authority')
    r.run('camp_admin_country_prepare_census','JAP'); assert works['camp_admin_detainees_k']==5
    assert r.cond([('camp_admin_program_jap_transport_open','=','yes')],'JAP')
    r.run('camp_admin_country_start_program','JAP',{'PROGRAM':'constant:camp_admin_country_program.jap_transport'})
    assert c['camp_admin_institution_state_id']=='716'
    works['camp_admin_development_level']=1; r.run('camp_admin_country_prepare_census','JAP')
    assert works['camp_admin_detainees_k']==30 and c['camp_admin_country_ceiling_jap_industry_k']==80
    results.append('Japanese transport selects an industrial labor host rather than Pingfang; completed development grows only bounded project capacity')

    r,c=new_country(); a=r.state('88'); a['camp_admin_detainees_k']=4
    for date,expect in [((1943,5,29),False),((1943,5,30),True)]:
        r.date=datetime.date(*date); assert r.cond([('camp_admin_country_mengele_historical_gate','=','yes')],'GER')==expect
    c['leader_ideology']='conservatism'; assert not r.cond([('camp_admin_country_mengele_historical_gate','=','yes')],'GER')
    c['leader_ideology']='nazism'; a['controller']='OTHER'; assert not r.cond([('camp_admin_country_mengele_historical_gate','=','yes')],'GER')
    results.append('Mengele cutoff, Nazi authority and actual Auschwitz control gate')

    r,c=new_country(); a=r.state('A'); a.update(camp_admin_detainees_k=20,camp_admin_support_ratio=1)
    c['flags'].add('camp_admin_country_programs_authorized')
    r.run('camp_admin_country_start_program','GER',{'PROGRAM':'constant:camp_admin_country_program.ger_inspectorate'})
    for month in range(1,7):
        c.update(camp_admin_budget_support_remaining=100,camp_admin_budget_pp_remaining=20)
        r.run('camp_admin_country_tick_institution','GER')
    assert len(r.awards)==1 and r.awards[0]['uses']==1 and r.awards[0]['category']=='industry' and r.awards[0]['bonus']==.5
    assert c['camp_admin_research_awards_this_year']==1 and 'camp_admin_done_ger_inspectorate' in c['flags']
    assert c['support']==10000-72 and c['political_power']==70
    r.run('camp_admin_country_finish_program','GER'); assert len(r.awards)==1
    results.append('Six paid source months, exact72 equipment/30PP, single-use award and repeat guard')

    r,c=new_country(); a=r.state('A'); a.update(camp_admin_detainees_k=20,camp_admin_support_ratio=1)
    c['flags'].add('camp_admin_country_programs_authorized'); c['held_bonuses']={'industry'}
    r.run('camp_admin_country_start_program','GER',{'PROGRAM':'constant:camp_admin_country_program.ger_inspectorate'})
    c.update(camp_admin_institution_progress=6,camp_admin_budget_support_remaining=100,camp_admin_budget_pp_remaining=20)
    original=(c['support'],c['political_power'])
    r.run('camp_admin_country_tick_institution','GER'); assert not r.awards and original==(c['support'],c['political_power'])
    c['held_bonuses'].clear(); c['camp_admin_research_awards_this_year']=2
    r.run('camp_admin_country_tick_institution','GER'); assert not r.awards and original==(c['support'],c['political_power'])
    r.date=datetime.date(1937,1,1); r.run('camp_admin_country_tick_institution','GER'); assert len(r.awards)==1
    results.append('Existing category bonus and annual cap defer completed work without repeat payment; actual new year releases award')

    r,c=new_country(); a=r.state('A'); a.update(camp_admin_detainees_k=20,camp_admin_support_ratio=.74)
    c['flags'].add('camp_admin_country_programs_authorized'); r.run('camp_admin_country_start_program','GER',{'PROGRAM':'constant:camp_admin_country_program.ger_inspectorate'})
    c.update(camp_admin_budget_support_remaining=100,camp_admin_budget_pp_remaining=20)
    r.run('camp_admin_country_tick_institution','GER'); assert c['camp_admin_institution_progress']==0
    a['camp_admin_support_ratio']=1; c['camp_admin_budget_support_remaining']=0
    r.run('camp_admin_country_tick_institution','GER'); assert c['camp_admin_institution_progress']==0
    c.update(camp_admin_budget_support_remaining=100,camp_admin_country_authority_pressure=60)
    r.run('camp_admin_country_tick_institution','GER'); assert c['camp_admin_institution_progress']==.5
    results.append('Insufficient local support and exhausted shared budget pause work; contested authority halves paid progress')

    r,c=new_country('SOV',(1944,2,1)); a=r.state('A','SOV'); a.update(gulag_labor_camp_network=2,camp_admin_detainees_k=20,camp_admin_support_ratio=1)
    c['flags'].update({'camp_admin_country_programs_authorized','camp_admin_country_oversight_authorized'})
    r.run('camp_admin_country_start_program','SOV',{'PROGRAM':'constant:camp_admin_country_program.sov_engineer_release'})
    c.update(camp_admin_institution_progress=6,camp_admin_budget_support_remaining=100,camp_admin_budget_pp_remaining=20)
    population=a['state_population_k']; r.run('camp_admin_country_tick_institution','SOV')
    assert a['camp_admin_detainees_k']==19.5 and c['camp_admin_country_last_engineers_released_k']==.5
    assert a['state_population_k']==population and c['camp_admin_total_released_k']==.5
    assert r.awards[0]['category']=='engineers_tech' and 'manpower' not in c
    results.append('Soviet technical release removes only its finite0.5k cohort, preserves camp remainder/population and creates no military manpower')

    r,c=new_country(); a=r.state('A'); a.update(camp_admin_detainees_k=20,camp_admin_support_ratio=1)
    c['flags'].add('camp_admin_country_programs_authorized'); r.run('camp_admin_country_start_program','GER',{'PROGRAM':'constant:camp_admin_country_program.ger_inspectorate'})
    c.update(camp_admin_mandate=1,camp_admin_budget_support_remaining=100,camp_admin_budget_pp_remaining=20)
    r.run('camp_admin_country_tick_institution','GER'); assert c['camp_admin_institution_progress']==0
    c['camp_admin_mandate']=2; r.run('camp_admin_country_halt','GER')
    r.run('camp_admin_country_action_1','GER'); assert 'camp_admin_institution_slot_active' in c['flags']
    r.run('camp_admin_country_tick_institution','GER'); assert c['camp_admin_institution_progress']==1
    results.append('Custody mandate pauses institutional work; explicit halt/resume restores only a valid saved institution')

    r,c=new_country('ENG'); c['flags'].add('camp_admin_civil_review_active'); c['camp_admin_civil_review_progress']=3
    r.run('camp_admin_country_refresh_civil_institution_display','ENG')
    assert c['camp_admin_institution_progress']==3 and c['camp_admin_institution_target']==r.constants['camp_admin_civil.review_months']
    c['flags'].discard('camp_admin_civil_review_active'); c['flags'].add('camp_admin_civil_claims_active'); c['camp_admin_civil_claims_progress']=2
    r.run('camp_admin_country_refresh_civil_institution_display','ENG')
    assert c['camp_admin_institution_progress']==2 and c['camp_admin_research_target']==r.constants['camp_admin_civil.claims_months']
    results.append('Civil GUI display copies actual review/claims progress and matching durations without advancing either project')

    r,c=new_country(); a=r.state('A'); a.update(camp_admin_detainees_k=20,camp_admin_support_ratio=1)
    c.update(ai=True,camp_admin_budget=1,camp_active_site_count=1)
    pp=c['political_power']; stock=c['support']; r.run('camp_admin_country_prepare_ai_budget','GER')
    assert c['camp_admin_budget']==2 and c['political_power']==pp-5.25 and c['support']==stock
    next_month=c['camp_admin_country_ai_policy_next_month']; c['support']=100
    r.run('camp_admin_country_prepare_ai_budget','GER'); assert c['camp_admin_budget']==2 and c['camp_admin_country_ai_policy_next_month']==next_month
    r.date=datetime.date(1936,4,1); r.run('camp_admin_country_prepare_ai_budget','GER'); assert c['camp_admin_budget']==1 and c['political_power']==pp-10.5
    r.date=datetime.date(1936,7,1); c['support']=10000; c['flags'].add('camp_admin_development_paused')
    r.run('camp_admin_country_prepare_ai_budget','GER'); assert c['camp_admin_budget']==1
    c['flags'].discard('camp_admin_development_paused'); c['ai']=False
    r.run('camp_admin_country_prepare_ai_budget','GER'); assert c['camp_admin_budget']==1
    results.append('AI budget uses the player command and its exact quoted PP debit, grants no stock, holds policy three months, and respects pause/human control')
    return results

if __name__=='__main__':
    print(json.dumps({'status':'passed','source_scenarios':tests(),'limit':'Parsed-source evaluation; mocked engine primitives; no live-game evidence'},indent=2))
