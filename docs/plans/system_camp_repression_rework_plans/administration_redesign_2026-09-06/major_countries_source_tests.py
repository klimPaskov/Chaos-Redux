"""Execute current country/foundation source for finite intake, gates and paid awards.
Engine values and add_tech_bonus are explicit mocks; this is not engine proof.
"""
from pathlib import Path
import datetime, json
from foundation_source_tests import Runtime, parse, get, prime_existing_custody
import black_friday_sale_prices as sale

ROOT = Path(__file__).resolve().parents[4]
SALE_RATIO = sale.RATIO_BASIS

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
        # National gates read war and campaign state, not calendar dates. The harness declares
        # each war condition through the country's single war field.
        self.triggers['camp_admin_jap_china_war']=[('has_war','=','yes')]
        self.triggers['camp_admin_ger_war_of_conquest']=[('has_war','=','yes')]
        self.triggers['camp_admin_country_major_war']=[('has_war','=','yes')]
        self.triggers['camp_admin_country_postwar_reckoning']=[('NOT','=',[('has_war','=','yes')])]
        self.awards=[]

    def start_program(self, country, program):
        # The production helper reads a temporary input, not a scripted-effect parameter.
        self.temp['camp_admin_start_program_input']=self.constants['camp_admin_country_program.'+program]
        self.run('camp_admin_country_start_program',country)

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
            if k=='has_political_power':
                amount=self.val(v,s,prev)
                return c['political_power']>amount if o=='>' else c['political_power']>=amount
            if k=='has_equipment':
                equipment,operator,amount=v[0]
                assert equipment=='support_equipment_1'
                amount=self.val(amount,s,prev)
                return c['support']>amount if operator=='>' else c['support']>=amount
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
    r=CountryRuntime(); sale.install(r,SALE_RATIO); r.date=datetime.date(*date); c=r.country(tag)
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

    r,c=new_country('GER',(1943,6,1)); a=r.state('88',population=100,buildings=1); a['flags'].discard('camp_rework_expanded_labor_site')
    a['camp_admin_role']=r.constants['camp_admin_role.killing']; a['extermination_camp']=1
    r.run('camp_admin_country_prepare_census','GER')
    assert a['camp_admin_detainees_k']==0 and c['camp_admin_country_cumulative_intake_k']==0
    a['camp_admin_role']=r.constants['camp_admin_role.custody']; r.run('camp_admin_country_prepare_census','GER')
    assert a['camp_admin_detainees_k']>0
    results.append('German automatic census excludes a killing center but may enroll a separate detention site')

    r,c=new_country('SOV'); a=r.state('195','SOV',population=100,buildings=0); a.update(gulag_labor_camp_network=2)
    # Declared aligned exposure reservation for the accounting contract.
    # This fixture does not claim a historical Soviet occupation campaign.
    r.run('camp_occ_initialize_country','SOV'); r.run('camp_occ_initialize_rows','SOV')
    c['arrays']['camp_occ_states'].append('195')
    a['flags'].add('camp_occ_registered')
    a.update(camp_occ_responsible_country='SOV',camp_occ_remaining_k=98,camp_occ_observed_population_k=100,camp_occ_observed_state_deaths=0)
    r.temp.update(camp_occ_append_origin='195',camp_occ_append_host='195',camp_occ_append_profile=r.constants['camp_occ_profile.germany'],camp_occ_append_amount_k=98,camp_occ_append_root_id=0)
    r.run('camp_occ_append_row','SOV'); a['camp_occ_native_row_id']=r.temp['camp_occ_appended_row_id']
    r.run('camp_origin_observe_host','195')
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
    r.start_program('JAP','jap_transport')
    assert c['camp_admin_institution_state_id']=='716'
    works['camp_admin_development_level']=1; r.run('camp_admin_country_prepare_census','JAP')
    assert works['camp_admin_detainees_k']==30 and c['camp_admin_country_ceiling_jap_industry_k']==80
    results.append('Japanese transport selects an industrial labor host rather than Pingfang; completed development grows only bounded project capacity')

    r,c=new_country(); a=r.state('88'); prime_existing_custody(r,'88',4)
    assert r.cond([('camp_admin_country_mengele_site_gate','=','yes')],'GER')
    c['leader_ideology']='conservatism'; assert not r.cond([('camp_admin_country_mengele_site_gate','=','yes')],'GER')
    c['leader_ideology']='nazism'; a['controller']='OTHER'; assert not r.cond([('camp_admin_country_mengele_site_gate','=','yes')],'GER')
    a['controller']='GER'; a['flags'].add('camp_admin_closed'); assert not r.cond([('camp_admin_country_mengele_site_gate','=','yes')],'GER')
    results.append('Mengele site gate: Nazi authority and an operating state-88 site under German control, with no calendar date')

    r,c=new_country(); a=r.state('A'); prime_existing_custody(r,'A',20); a['camp_admin_support_ratio']=1
    c['flags'].add('camp_admin_country_programs_authorized')
    r.start_program('GER','ger_inspectorate')
    for month in range(1,7):
        c.update(camp_admin_budget_support_remaining=100,camp_admin_budget_pp_remaining=20)
        r.run('camp_admin_country_tick_institution','GER')
    assert len(r.awards)==1 and r.awards[0]['uses']==1 and r.awards[0]['category']=='industry' and r.awards[0]['bonus']==.5
    assert c['camp_admin_research_awards_this_year']==1 and 'camp_admin_done_ger_inspectorate' in c['flags']
    assert c['support']==10000-72 and c['political_power']==70
    r.run('camp_admin_country_finish_program','GER'); assert len(r.awards)==1
    results.append('Six paid source months, exact72 equipment/30PP, single-use award and repeat guard')

    r,c=new_country(); a=r.state('A'); prime_existing_custody(r,'A',20); a['camp_admin_support_ratio']=1
    c['flags'].add('camp_admin_country_programs_authorized'); c['held_bonuses']={'industry'}
    r.start_program('GER','ger_inspectorate')
    c.update(camp_admin_institution_progress=6,camp_admin_budget_support_remaining=100,camp_admin_budget_pp_remaining=20)
    original=(c['support'],c['political_power'])
    r.run('camp_admin_country_tick_institution','GER'); assert not r.awards and original==(c['support'],c['political_power'])
    c['held_bonuses'].clear(); c['camp_admin_research_awards_this_year']=2
    r.run('camp_admin_country_tick_institution','GER'); assert not r.awards and original==(c['support'],c['political_power'])
    r.date=datetime.date(1937,1,1); r.run('camp_admin_country_tick_institution','GER')
    assert len(r.awards)==1 and c['support']==original[0]-12 and c['political_power']==original[1]-5
    results.append('Existing category bonus and annual cap defer completed work without repeat payment; actual new year releases award')

    r,c=new_country(); a=r.state('A'); prime_existing_custody(r,'A',20); a['camp_admin_support_ratio']=.74
    c['flags'].add('camp_admin_country_programs_authorized'); r.start_program('GER','ger_inspectorate')
    c.update(camp_admin_budget_support_remaining=100,camp_admin_budget_pp_remaining=20)
    r.run('camp_admin_country_tick_institution','GER'); assert c['camp_admin_institution_progress']==0
    a['camp_admin_support_ratio']=1; c['camp_admin_budget_support_remaining']=0
    r.run('camp_admin_country_tick_institution','GER'); assert c['camp_admin_institution_progress']==0
    c.update(camp_admin_budget_support_remaining=100,camp_admin_country_authority_pressure=60)
    r.run('camp_admin_country_tick_institution','GER'); assert c['camp_admin_institution_progress']==.5
    results.append('Insufficient local support and exhausted shared budget pause work; contested authority halves paid progress')

    r,c=new_country('SOV',(1942,1,1)); c['war']=True
    a=r.state('A','SOV'); a['gulag_labor_camp_network']=2; prime_existing_custody(r,'A',20); a['camp_admin_support_ratio']=1
    c['flags'].add('camp_admin_country_programs_authorized')
    r.start_program('SOV','sov_wartime_industry')
    c.update(camp_admin_budget_support_remaining=100,camp_admin_budget_pp_remaining=20,held_bonuses={'industry'})
    original=(c['support'],c['political_power'])
    r.run('camp_admin_country_tick_institution','SOV')
    assert c['camp_admin_institution_progress']==0 and original==(c['support'],c['political_power'])
    c['held_bonuses']={'engineers_tech'}
    r.run('camp_admin_country_tick_institution','SOV')
    assert c['camp_admin_institution_progress']==1 and (c['support'],c['political_power'])!=(original)
    results.append('Soviet wartime industry pauses for an industry award and ignores an unrelated engineers award')

    r,c=new_country('SOV',(1944,2,1)); a=r.state('A','SOV'); a['gulag_labor_camp_network']=2; prime_existing_custody(r,'A',20); a['camp_admin_support_ratio']=1
    c['flags'].update({'camp_admin_country_programs_authorized','camp_admin_country_oversight_authorized','camp_admin_done_sov_design_bureaux'})
    r.start_program('SOV','sov_engineer_release')
    c.update(camp_admin_institution_progress=6,camp_admin_budget_support_remaining=100,camp_admin_budget_pp_remaining=20)
    population=a['state_population_k']; r.run('camp_admin_country_tick_institution','SOV')
    assert a['camp_admin_detainees_k']==19.5 and c['camp_admin_country_last_engineers_released_k']==.5
    assert a['state_population_k']==population and c['camp_admin_total_released_k']==.5
    assert r.awards[0]['category']=='engineers_tech' and 'manpower' not in c
    results.append('Soviet technical release removes only its finite0.5k cohort, preserves camp remainder/population and creates no military manpower')

    r,c=new_country(); a=r.state('A'); prime_existing_custody(r,'A',20); a['camp_admin_support_ratio']=1
    c['flags'].add('camp_admin_country_programs_authorized'); r.start_program('GER','ger_inspectorate')
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

    r,c=new_country(); a=r.state('A'); prime_existing_custody(r,'A',20); a['camp_admin_support_ratio']=1
    c.update(ai=True,camp_admin_budget=1,camp_active_site_count=1)
    pp=c['political_power']; stock=c['support']; r.run('camp_admin_country_prepare_ai_budget','GER')
    # The ordered budget change charges the Event 026 sale price of its 5.25 PP quote; monthly work keeps its upkeep.
    order_pp=sale.production_quote(5.25,SALE_RATIO)
    assert c['camp_admin_budget']==2 and c['political_power']==pp-order_pp and c['support']==stock
    next_month=c['camp_admin_country_ai_policy_next_month']; c['support']=100
    r.run('camp_admin_country_prepare_ai_budget','GER'); assert c['camp_admin_budget']==2 and c['camp_admin_country_ai_policy_next_month']==next_month
    r.date=datetime.date(1936,4,1); r.run('camp_admin_country_prepare_ai_budget','GER'); assert c['camp_admin_budget']==1 and c['political_power']==pp-2*order_pp
    r.date=datetime.date(1936,7,1); c['support']=10000; c['flags'].add('camp_admin_development_paused')
    r.run('camp_admin_country_prepare_ai_budget','GER'); assert c['camp_admin_budget']==1
    c['flags'].discard('camp_admin_development_paused'); c['ai']=False
    r.run('camp_admin_country_prepare_ai_budget','GER'); assert c['camp_admin_budget']==1
    results.append('AI budget uses the player command and its exact quoted PP debit, grants no stock, holds policy three months, and respects pause/human control')

    r,c=new_country(); a=r.state('A'); prime_existing_custody(r,'A',10)
    r.triggers['camp_rework_country_can_reform']=[('original_tag','=','GER')]
    c['camp_selected_state_id']='A'
    a['arrays']['camp_admin_row_amounts_k'][0]=9
    status_definitions=parse((ROOT/'common/scripted_localisation/camp_administration_ui_localisation.txt').read_text(encoding='utf-8-sig'))
    selected_status=next(body for name,_,body in status_definitions if name=='defined_text' and get(body,'name')=='GetCampAdminSelectedConditions')
    records_status=next(body for name,_,body in selected_status if name=='text')
    assert get(records_status,'localization_key')=='camp_admin_conditions_records'
    gui_source=parse((ROOT/'common/scripted_guis/camp_repression_ledger_scripted_gui.txt').read_text(encoding='utf-8-sig'))
    gui_window=get(get(gui_source,'scripted_gui'),'camp_repression_ledger_scripted_gui')
    gui_triggers=get(gui_window,'triggers')
    release_active=get(get(gui_triggers,'camp_admin_site_release_visible'),'ROOT')
    release_records_locked=get(get(gui_triggers,'camp_admin_site_release_locked_records_visible'),'ROOT')
    assert r.cond(get(records_status,'trigger'),'GER')
    assert not r.cond(release_active,'GER') and r.cond(release_records_locked,'GER')
    assert not r.cond(r.triggers['camp_admin_can_release_selected_site'],'GER')
    r.run('camp_admin_release_selected','GER')
    assert a['camp_admin_detainees_k']==10 and 'camp_admin_site_suspended' not in a['flags']
    assert not c['arrays'].get('camp_admin_history_ids') and r.temp['camp_admin_release_actual_k']==0

    r,c=new_country(); a=r.state('A'); prime_existing_custody(r,'A',10)
    r.triggers['camp_rework_country_can_reform']=[('original_tag','=','GER')]
    c['camp_selected_state_id']='A'; population=a['state_population_k']
    assert not r.cond(get(records_status,'trigger'),'GER')
    assert r.cond(release_active,'GER') and not r.cond(release_records_locked,'GER')
    assert r.cond(r.triggers['camp_admin_can_release_selected_site'],'GER')
    r.run('camp_admin_release_selected','GER')
    assert a['camp_admin_detainees_k']==0 and a['state_population_k']==population
    assert 'camp_admin_site_suspended' in a['flags'] and len(c['arrays']['camp_admin_history_ids'])==1
    assert r.temp['camp_admin_release_actual_k']==10 and c['camp_admin_total_released_k']==10

    r,c=new_country(); a=r.state('A'); prime_existing_custody(r,'A',10)
    r.triggers['camp_rework_country_can_reform']=[('original_tag','=','GER')]
    c['camp_selected_state_id']='A'
    a['state_population_k']=r.constants['camp_admin_value.minimum_population_k']
    assert not r.cond(r.triggers['camp_admin_can_release_selected_site'],'GER')
    r.run('camp_admin_refresh_capacity','A')
    assert a['camp_admin_detainees_k']==0
    assert not r.cond(r.triggers['camp_admin_can_release_selected_site'],'GER')
    r.run('camp_admin_release_selected','GER')
    assert a['camp_admin_detainees_k']==0 and a['state_population_k']==r.constants['camp_admin_value.minimum_population_k']
    assert r.temp['camp_admin_release_actual_k']==0 and not c['arrays'].get('camp_admin_history_ids')
    assert 'camp_admin_site_suspended' not in a['flags'] and 'camp_admin_census_intake_closed' not in a['flags']
    results.append('Selected release rejects inconsistent or unobserved living rows; accepted survivors get one record without population creation; reconciled zero survivors stay unselectable and get no false release record or success cleanup')
    return results

if __name__=='__main__':
    scenarios={}
    for ratio in sale.SALE_RATIOS:
        SALE_RATIO=ratio
        scenarios[f'payment_ratio_{ratio}']=tests()
    print(json.dumps({'status':'passed','source_scenarios':scenarios,'sale_ratios':list(sale.SALE_RATIOS),'limit':'Parsed-source evaluation; mocked engine primitives; no live-game evidence'},indent=2))
