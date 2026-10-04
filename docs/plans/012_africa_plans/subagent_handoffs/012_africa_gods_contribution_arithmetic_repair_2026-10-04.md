# Event 012 contribution arithmetic repair evidence

Disposition: implemented bounded source repair, native exactness and full integration remain blocked or unresolved.
Acceptance basis: the 2026-10-04 bounded repair instruction, corrected 1000 total pre-debit capacity, and subsequent primary-evidence clarification.
The conservative arithmetic model below is a source audit, not an observed engine width or precision.
Fixture inputs are declared stocks and native getters, not save observations.
Parent independent review is required before integration or publication.

## Reproducible bounded source fixture

Run this Python block from the repository root.
It parses the current helper source and executes the receipt path with native stocks supplied as fixture data.
Only external history, roster, contract and ordinary reserve predicates are mocked.
Payment and ledger arithmetic operations are checked at conservative three-decimal precision and magnitude 2147483.647.
Modulo tests used only to classify native snapshot or prior-ledger precision retain their exact Decimal remainder so unsupported precision can be quarantined rather than truncated by the fixture.
Native snapshot assignments may retain wider or more precise values as evidence, and that does not establish that the real native getter provides them.

```python
from pathlib import Path
from decimal import Decimal as D
import re
P='gods_of_africa_'; R=P+'material_transfer_'
CAP=D('2147483.647'); Q=D('.001')
def parse(text):
    toks=re.findall(r'"[^"\n]*"|[{}=<>]|[^\s{}=<>]+',re.sub(r'#[^\n]*','',text)); pos=0
    def block(nested=False):
        nonlocal pos
        out=[]
        while pos<len(toks) and toks[pos]!='}':
            key=toks[pos];pos+=1;op=toks[pos];pos+=1
            assert op in ['=','<','>'],(key,op)
            if toks[pos]=='{':
                pos+=1;value=block(True)
            else: value=toks[pos];pos+=1
            out.append((key,op,value))
        if nested: assert toks[pos]=='}';pos+=1
        return out
    return block()
def read(path): return parse(Path(path).read_text(encoding='utf-8-sig'))
E={k:v for k,o,v in read('common/scripted_effects/012_africa_gods_contribution_effects.txt')}
T={k:v for k,o,v in read('common/scripted_triggers/012_africa_gods_contribution_triggers.txt')}
K={}
for path in ['common/script_constants/012_africa_gods_constants.txt','common/script_constants/012_africa_gods_contribution_constants.txt']:
    for group,o,entries in read(path):
        for key,o,v in entries:
            if isinstance(v,str):
                try: K['constant:'+group+'.'+key]=D(v)
                except Exception: pass
external={P+n for n in ['full_grade_history_is_valid','full_grade_ledger_is_present','participant_generation_is_current','participant_host_is_active','participant_epoch_is_current','contract_ledger_can_close','demand_contract_is_current','participant_has_capacity_for_family','mobile_payment_matches_contract']}
class Fixture:
    def __init__(self,kind='infantry',amount='100',vol=False):
        self.a={10:{},20:{}};self.flags={10:set(),20:set()};self.stocks={10:{},20:{}};self.tmp={};self.targets={'africa_host':20};self.native={10:{'fuel_k':D('3000'),'manpower_k':D('3000'),'max_fuel_k':D('6000'),'political_power':D('2000')},20:{'fuel_k':D('2500'),'manpower_k':D('2500'),'max_fuel_k':D('6000'),'political_power':D('2000')}}
        for actor in [10,20]:
            for eq in ['infantry_equipment','support_equipment','motorized_equipment','artillery_equipment','fighter_equipment_1','convoy_1','train_equipment']+[c+'_tank_chassis' for c in ['light','medium','heavy','modern','super_heavy','amphibious']]: self.stocks[actor][eq]=D('400000')
        self.kind=kind;self.wars=set()
        self.tmp.update({P+'contribution_kind':K['constant:'+P+'contribution_kind.'+kind],P+'contribution_native_emit_kind':K['constant:'+P+'contribution_kind.'+kind],P+'contribution_requested':D(amount),P+'contribution_voluntary':D(int(vol))})
        self.a[20].update({P+'authority_epoch':D(4),'africa_host_generation':D(1),'africa_origin_host_id':D(20),P+'restoration_generation':D(1),P+'need_land_equipment':D(1),P+'need_fuel':D(1),'africa_emergency_rule_debt':D(100)})
        self.a[10].update({P+'participant_authority_epoch':D(4),P+'demand_authority_epoch':D(4),P+'demand_host':D(20),P+'demand_host_id':D(20),P+'demand_origin_host_id':D(20),P+'contract_ledger_generation':D(1),P+'contract_ledger_origin_id':D(20),P+'contract_ledger_id':D(1),R+'sequence':D(0),P+'last_consumed_material_transfer_id':D(0),P+'payment_amount':D(amount),P+'capacity_requirement':D(amount),P+'payment_mobile_type':K['constant:'+P+'mobile_type.trucks'],P+'payment_family':K['constant:'+P+'demand_family.'+{'infantry':'land_equipment','support':'support_equipment','trucks':'mobile_artillery','artillery':'mobile_artillery','armor':'armor','aircraft':'aircraft','fuel':'fuel','convoys':'transport','trains':'transport','manpower':'manpower','emergency_pp':'emergency_relief'}[kind]]})
        if kind=='artillery':self.a[10][P+'payment_mobile_type']=K['constant:'+P+'mobile_type.artillery']
        if kind=='trains':self.stocks[10]['convoy_1']=D(0)
        for k in ['infantry','support','trucks','artillery','armor','aircraft','fuel','convoys','trains','manpower']:
            for prefix in ['paid_','voluntary_paid_','campaign_paid_','emergency_paid_']:self.a[10][P+prefix+k+'_k']=D(0)
        self.a[10][P+'emergency_paid_pp']=D(0)
        if kind=='emergency_pp':
            self.flags[10].update([P+'contract_emergency_proof_frozen',P+'contract_emergency_qualified'])
            for k,v in {'host':20,'host_id':20,'generation':1,'origin_id':20,'contract_id':1}.items():self.a[10][P+'contract_emergency_'+k]=D(v)
            self.a[10][P+'contract_emergency_band']=K['constant:'+P+'demand.emergency_band']
    def val(self,x,actor):
        if x in K:return K[x]
        if x=='THIS':return D(actor)
        if x in ['THIS.id','id']:return D(actor)
        if x=='global.num_days':return D(100)
        if x.startswith('event_target:'):
            v=x[13:].split('.',1);who=self.targets[v[0]]
            return self.val(v[1],who) if len(v)>1 else D(who)
        if x.startswith('num_equipment@'):return self.stocks[actor][x.split('@')[1]]
        if x in self.tmp:return self.tmp[x]
        if x in self.native[actor]:return self.native[actor][x]
        if x in self.a[actor]:return self.a[actor][x]
        try:return D(x)
        except Exception:return D(0)
    def scope(self,k,a):
        if k.startswith('event_target:'):return self.targets.get(k[13:])
        if k.startswith('var:'):return int(self.val(k[4:],a))
        return None
    def checked(self,x):
        assert abs(x)<=CAP and x%Q==0,('conservative arithmetic unsupported',x)
        return x
    def cmp(self,l,r,op):return {'=':l==r,'<':l<r,'>':l>r,'equals':l==r,'greater_than_or_equals':l>=r,'less_than_or_equals':l<=r}[op]
    def test(self,b,a=10,mode='AND'):
        vals=[self.pred(k,o,v,a) for k,o,v in b]
        return any(vals) if mode=='OR' else not any(vals) if mode in ['NOT','NOR'] else all(vals)
    def pred(self,k,o,v,a):
        if k in ['AND','OR','NOT','NOR']:return self.test(v,a,k)
        if k in external:return True
        if k in T:return self.test(T[k],a)
        who=self.scope(k,a)
        if who is not None:return self.test(v,who)
        if k=='exists':return a in self.a
        if k=='has_variable':return v in self.a[a] or v in self.tmp
        if k=='has_event_target':return v in self.targets
        if k=='has_country_flag':return v in self.flags[a]
        if k=='has_war':return a in self.wars
        if k in ['has_global_flag','has_war_with']:return False
        if k=='check_variable':
            if v[0][0]=='var':
                q={x:y for x,o,y in v};return self.cmp(self.val(q['var'],a),self.val(q['value'],a),q.get('compare','equals'))
            x,op,y=v[0];return self.cmp(self.val(x,a),self.val(y,a),op)
        if k=='has_equipment':
            x,op,y=v[0];return self.cmp(self.stocks[a][x],self.val(y,a),op)
        if k in ['has_fuel','has_manpower']:return self.cmp(self.native[a][k[4:]+'_k']*D(1000),self.val(v,a),o)
        if 'temp_variable' in k:self.effect(k,v,a);return True
        raise AssertionError(('unsupported fixture predicate',k))
    def effect(self,k,v,a):
        if k in E:self.run(E[k],a);return
        who=self.scope(k,a)
        if who is not None:self.run(v,who);return
        if k=='save_event_target_as':self.targets[v]=a;return
        if k=='set_country_flag':self.flags[a].add(v);return
        if k=='clr_country_flag':self.flags[a].discard(v);return
        if k=='clear_variable':self.a[a].pop(v,None);return
        table=self.tmp if 'temp_variable' in k else self.a[a]
        q={x:y for x,o,y in v};name=q.get('var',v[0][0]);operand=self.val(q.get('value',v[0][2]),a);old=table.get(name,D(0))
        if k.startswith('set_'):table[name]=operand;return
        if k.startswith('add_to_'):result=old+operand
        elif k.startswith('subtract_from_'):result=old-operand
        elif k.startswith('multiply_'):result=old*operand
        elif k.startswith('modulo_'):result=old%operand
        elif k.startswith('clamp_'):result=min(max(old,self.val(q['min'],a)) if 'min' in q else old,self.val(q['max'],a)) if 'max' in q else max(old,self.val(q['min'],a))
        else:raise AssertionError(('unsupported fixture effect',k))
        table[name]=result if k.startswith('modulo_') and name in [P+'native_read_fraction',P+'ledger_read_fraction'] else self.checked(result)
    def run(self,b,a=10):
        chain=False
        for k,o,v in b:
            if k in ['if','else_if','else']:
                if k=='if':chain=False
                take=not chain and (k=='else' or self.test(next(y for x,o,y in v if x=='limit'),a))
                if take:self.run([(x,o,y) for x,o,y in v if x!='limit'],a);chain=True
            else:self.effect(k,v,a)
    def call(self,name):self.run(E[P+name])
    def flag(self,name):return P+name in self.flags[10]
    def begin(self):self.call('begin_material_transfer');return self.flag('material_transfer_begin_ready')
    def mutate(self,debit,credit):
        token={'infantry':'infantry_equipment','support':'support_equipment','trucks':'motorized_equipment','artillery':'artillery_equipment','aircraft':'fighter_equipment_1','convoys':'convoy_1','trains':'train_equipment'}.get(self.kind)
        if token:self.stocks[10][token]-=D(debit);self.stocks[20][token]+=D(credit)
        else:
            name={'fuel':'fuel_k','manpower':'manpower_k','emergency_pp':'political_power'}[self.kind];scale=D(1000) if self.kind!='emergency_pp' else D(1)
            self.native[10][name]-=D(debit)/scale;self.native[20][name]+=D(credit)/scale
    def complete(self):self.call('complete_material_transfer')
def test_cases():
    passed=[]
    for kind in ['infantry','support','trucks','artillery','aircraft','fuel','convoys','trains','manpower','emergency_pp']:
        f=Fixture(kind);assert f.begin();f.mutate('100','100');f.complete();assert f.flag('material_transfer_completion_consumed');assert f.flag('material_transfer_full_match')
        count=f.a[10].get(P+'paid_'+kind+'_k',f.a[10][P+'emergency_paid_pp']);f.complete();assert not f.flag('material_transfer_completion_consumed');assert f.a[10].get(P+'paid_'+kind+'_k',f.a[10][P+'emergency_paid_pp'])==count
    passed.append('typed full delivery and replay')
    for d,c,actual in [(100,100,100),(70,60,60),(0,0,0),(200,200,100),(0,100,0),(100,0,0)]:
        f=Fixture();assert f.begin();f.mutate(str(d),str(c));f.complete();assert f.a[10][R+'actual_amount']==D(actual);assert f.flag('material_transfer_completion_consumed');assert f.flag('material_transfer_full_match')==(d==c==100)
    passed.append('full partial zero excess one-sided')
    for pool in ['2500','3000']:
        for kind in ['fuel','manpower']:
            f=Fixture(kind,'10000');f.native[10][kind+'_k']=D(pool);assert f.begin();f.mutate('10000','10000');f.complete();assert f.a[10][R+'actual_amount']==D(10000);assert f.a[10][P+'paid_'+kind+'_k']==D(10)
    passed.append('2500k and 3000k pools, safe 10k differences')
    f=Fixture('fuel','10000');f.native[20]['fuel_k']=D('3000');assert f.begin();assert f.a[10][P+'contribution_fuel_headroom_k']==D(3000)
    f=Fixture('fuel','10000');f.native[20]['max_fuel_k']=D('2500.020');assert not f.begin()
    passed.append('fuel room stays k and insufficient room denied')
    f=Fixture('armor','120');assert f.begin()
    for c in ['light','medium','heavy','modern','super_heavy','amphibious']:f.stocks[10][c+'_tank_chassis']-=D(20);f.stocks[20][c+'_tank_chassis']+=D(20)
    f.complete();assert f.a[10][R+'actual_amount']==D(120);assert f.a[10][P+'paid_armor_k']==D('.120');assert f.flag('material_transfer_full_match')
    passed.append('six 400000 chassis stocks, aggregate actual 120 without 2400000 pool sum')
    for stock,ok in [(999,False),(1000,True),(1499,True),(1500,True)]:
        f=Fixture('infantry','500',True);f.stocks[10]['infantry_equipment']=D(stock);assert f.begin()==ok
        if ok:f.mutate('500','500');f.complete();assert f.stocks[10]['infantry_equipment']==D(stock-500);assert f.a[10][P+'voluntary_paid_infantry_k']==D('.5')
    passed.append('999 denied, 1000/1499/1500 allowed, exact 500 shipment')
    f=Fixture('fuel','499',True);assert not f.begin();f=Fixture('fuel','500',True);assert f.begin()
    for kind,amount,emit in [('infantry','99','infantry'),('trucks','100','artillery'),('convoys','100','trains')]:
        f=Fixture(kind);f.tmp[P+'contribution_requested']=D(amount);f.tmp[P+'contribution_native_emit_kind']=K['constant:'+P+'contribution_kind.'+emit];assert not f.begin()
    f=Fixture('artillery');f.a[10][P+'payment_mobile_type']=K['constant:'+P+'mobile_type.trucks'];assert not f.begin()
    passed.append('wrong request/kind/selected subtype denied before emission')
    f=Fixture();assert f.begin();assert not f.begin();f.a[20][P+'authority_epoch']=D(5);f.complete();assert not f.flag('material_transfer_completion_consumed');assert R+'receipt_source_before' in f.a[10]
    passed.append('duplicate begin and same-tuple epoch drift retained')
    f=Fixture('infantry','.5');assert f.begin();f.mutate('.5','.5');f.complete();assert f.a[10][R+'receipt_amount']==D('.5');assert f.a[10][P+'paid_infantry_k']==D(0);assert f.flag('material_transfer_receipt_pending');assert not f.flag('material_transfer_completion_consumed');assert f.flag('material_receipt_representation_blocked');f.call('abandon_pending_material_transfer');assert R+'receipt_amount' in f.a[10]
    passed.append('fractional raw .5 contract unchanged, accounting blocked, exact pending evidence')
    f=Fixture('infantry','1000');f.a[10][P+'paid_infantry_k']=D('2147483');assert f.begin();f.mutate('1000','1000');f.complete();assert f.a[10][P+'paid_infantry_k']==D('2147483');assert f.a[10][R+'receipt_amount']==D(1000);assert f.a[10][P+'last_consumed_material_transfer_id']==D(0);assert f.flag('material_transfer_receipt_pending');f.call('clear_material_transfer_work');assert R+'receipt_source_after' in f.a[10]
    passed.append('counter overflow checked before consumption, measured pending preserved')
    f=Fixture();assert f.begin();f.call('abandon_pending_material_transfer');assert f.a[10][R+'gap_id']==D(1);assert f.a[10][R+'gap_epoch']==D(4);f.call('abandon_pending_material_transfer');assert f.a[10][R+'gap_id']==D(1)
    passed.append('unemitted reservation gap current host session recorded once')
    f=Fixture('fuel','10000');assert f.begin();f.mutate('20000','20000');f.complete();assert f.a[10][R+'actual_amount']==D(10000);assert f.a[10][R+'source_debit_native']==D(20);assert f.a[10][R+'source_debit']==D(10000);assert not f.flag('material_transfer_full_match')
    f=Fixture('armor','100');assert f.begin()
    for c in ['light','medium','heavy','modern','super_heavy','amphibious']:f.stocks[10][c+'_tank_chassis']-=D(20);f.stocks[20][c+'_tank_chassis']+=D(20)
    f.complete();assert f.a[10][R+'actual_amount']==D(100);assert not f.flag('material_transfer_full_match');assert f.flag('material_transaction_unresolved')
    passed.append('fuel native excess and armor aggregate excess cannot fake full match')
    f=Fixture('fuel','.5');assert f.begin();f.mutate('.5','.5');f.complete();assert f.flag('material_transfer_receipt_pending');assert f.flag('material_transfer_native_read_blocked');assert f.a[10][R+'receipt_source_after']==D('2999.9995');assert not f.flag('material_transfer_completion_consumed')
    f=Fixture('infantry','100');f.stocks[10]['infantry_equipment']=D('3000000');assert f.begin();f.mutate('100','100');f.complete();assert f.flag('material_transfer_receipt_pending');assert f.a[10][R+'receipt_source_before']==D(3000000);assert f.a[10][R+'receipt_source_after']==D(2999900);assert not f.flag('material_transfer_completion_consumed')
    passed.append('unverified fractional-k and wide raw-getter evidence retained without rejecting quoted price')
    for kind in ['infantry','support','trucks','artillery','armor','aircraft','fuel','convoys','trains','manpower']:
        f=Fixture(kind,'100');f.wars.add(20);assert f.begin()
        if kind=='armor':f.stocks[10]['light_tank_chassis']-=D(100);f.stocks[20]['light_tank_chassis']+=D(100)
        else:f.mutate('100','100')
        f.complete();assert f.a[10][P+'campaign_paid_'+kind+'_k']==D('.1');assert f.a[10][P+'paid_'+kind+'_k']==D('.1')
        f=Fixture(kind,'1000');f.wars.add(20);f.a[10][P+'campaign_paid_'+kind+'_k']=D('2147483');assert f.begin()
        if kind=='armor':f.stocks[10]['light_tank_chassis']-=D(1000);f.stocks[20]['light_tank_chassis']+=D(1000)
        else:f.mutate('1000','1000')
        f.complete();assert f.flag('material_transfer_receipt_pending');assert f.a[10][P+'paid_'+kind+'_k']==D(0);assert f.a[10][P+'last_consumed_material_transfer_id']==D(0)
    passed.append('all ten campaign subset writes and overflow guard atomicity')
    f=Fixture('emergency_pp','500');f.a[10][P+'emergency_paid_pp']=D('2147483');assert f.begin();f.mutate('500','500');f.complete();assert f.flag('material_transfer_receipt_pending');assert f.a[10][R+'actual_amount']==D(500);assert f.a[10][P+'emergency_paid_pp']==D('2147483');assert not f.flag('material_transfer_completion_consumed')
    passed.append('actual emergency PP preserved when exact lifetime accumulation is unsupported')
    return passed
for result in test_cases(): print('PASS',result)

```

## Results and reference evidence

The fifteen case groups printed PASS on the final owned source.
The actual cases, mocked proof predicates, finite arithmetic checks and expected outputs are retained in the fixture above.
No engine/native observation is claimed.
Original 24 fixtures remain historical, unbounded and unretained as executable proof, with the wrong 1500 gate interpretation.
They are not substituted for this repair evidence.

Native snapshot setters are deliberately allowed to retain declared wider/more precise fixture inputs.
Only modeled transaction/payment arithmetic and counters are required to fit the conservative domain.
The declared 3000000 raw equipment fixture does not prove that num_equipment can supply that value in game.
The declared 2999.9995 k after snapshot does not prove native fractional-k precision.
Both stay pending and uncredited instead of being floored, price-rejected or silently capped.
For a 2147483k lifetime total plus a 1k measured contribution, prospective room fails before consumption, old history is unchanged, and the complete measured receipt/snapshots remain pending.

| Source path | Read line spans / relevant rule | Read method and SHA-256 source revision |
| --- | --- | --- |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md | 385-387 fuel_k, 469-471 manpower_k, 483-485 max_fuel_k, 557-559 num_equipment | Live reference_read for fuel/manpower/equipment, direct local max_fuel_k, 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md | 184-195 Math Expressions and 216-222 Script Constants | Live reference_read, fixed-point wording does not establish every native type, 884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7 |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md | 1-34 schema first and int/fixed_point access | Direct local read, e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md | 6476-6485 round_temp_variable, 6550-6558 send_equipment | Live round reference_read, direct local send documentation, 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md | 3835-3849 native equipment/target checks, 3957-3966 has_fuel, 4121-4128 has_manpower, 6442-6453 modulo_temp_variable | Direct local reads, 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29 |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_effects/USA_scripted_effects.txt | 402-418 native send_equipment equipment spelling and native stock preflight | Direct vanilla precedent, 9da33cb6e469906d7c8353b88d3957945f35ae12d81e1134d294b78b14f76f75 |
| paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md | 303-327 event targets, 425-433 variable precision paragraph, 435-443 temp scope, 1516-1517 fuel units, 1591-1597 manpower deprecation, 1613-1622 stockpile equipment versus armies | Live variable types and stockpile section reads, direct local other sections, 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4 |
| paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md | 303-311 display precision wording | Direct local, different native types remain possible, fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f |
| paradox_wiki/Effects - Hearts of Iron 4 Wiki.md | 2246-2263 native equipment send and stockpile effects, 4683-4697 boolean scripted effects | Direct local reads, 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c |
| paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md | 2359-2371 boolean scripted triggers | Direct local read, abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06 |
| paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md | 526-539 country-owned/core/controlled state iterators | Direct local, retained conduct pattern, 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49 |
| common/scripted_effects/chaosx_dynamic_effects.txt | 810-814 existing native fuel debit helper | Direct local, reusable helper inspected, f9591fe2beab4ac7570813ba76d1b4dbf63fc9ff10dc3315adfffccab2a895c2 |
| common/scripted_effects/chaosx_dynamic_effects.md | 1-29 owner-owned API boundary and registry | Direct local, no registry write authorized, b0563a54ff850b631c23aa0ae1f6ab18ce8b6f8e4189a5fced2e4b2581088e4e |

The initial live event reference_context returned omittedSources Data structures, Effects, Triggers, Scopes, On actions and Localisation.
Targeted relevant reads above resolve the task's data structure, helper, effect, trigger and scope rules.
No on-action or localisation construct is changed, and their omitted detailed sections are not claimed as read by the initial bundle.
Reference_search for the literal mathExpression spelling returned no result, while Math Expressions returned the revision-bound primary section subsequently read.
No online Paradox wiki or web substitute was used.

## MCP evidence and precise route gaps

Connected workspace: mod_chaos_redux_ea3b2d67c2c0.
Schemas were discovered from exposed tool metadata before calling reference_context, reference_search, reference_read, source_lookup, event_inspect, event_render and event_compare.
The source_lookup live schema offers bounded lines and expectedRevision, without view/keyPath.
No unsupported child-structure route was invented.
No script_validate, connected health/version route or negotiated task capability was exposed, so helper_expansion, native tasks and job routes were not used.

Final begin helper source lookup returned one non-overridden definition, complete=true, skippedSourceCount=0, revision 3e3991edf998a8dc8b9cbc362b7a58225e6efc51c8e52e662a5bfe07694d7abc, source path mod:common/scripted_effects/012_africa_gods_contribution_effects.txt, lines 347-495, with narrow lines 347-356 returned.
An earlier repaired completion source lookup returned one non-overridden definition, revision 669a9ad00120f961896461aba9dcc8fff61f7ed2611a7d0578a3718284e7089d, source lines 697-811 and narrow 697-708.
That completion lookup predates the final sequence/gap comments and must not be described as the final source hash.
Both are indexed source identity only, not native receipt execution.
The final owned file hashes appear in the delivery handoff.

Event trace for chaosx.nr12.608, depth 1 / nodes 3 / edges 4 / no helper expansion returned EVENT_INSPECTED_PARTIAL, focused analysis, helpers=0, revision d397c49bcd704632e8edc807c7fbaf2d801de75dd4f095a9ee52deac8d3673e5.
Trace artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe020c6fa89437d08c3a354f1b420566bf597f60aac411167d5d303937d0bccf/f23c1d4c919580361518b4a9d4fc39d6238a280a04079c2f979996fd0e47d3ae/event-trace-d397c49bcd70.json.
The final selector schema was corrected to kind=event,eventId after two invalid selector-key requests.
The invalid requests establish no gameplay failure.

Scope render for the same event, depth 1 / nodes 1 / no helper expansion returned EVENT_RENDERED_PARTIAL at that revision, helpers=0 and selectedNodes=0.
No helper or event visual coverage can be inferred from this summary.
Manifest: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ae80276ec9b08d4a78fd294151dd81de5733939a891692a3a39cc60d05a4c00/8f224986336fd323a5fc2f11a1fbfda277777ae7c30c0a3ff7bb27ddac6b363a/event-scope-d397c49bcd70-manifest.json.
JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/902564991e148d79328c4f1cb56ed58613c2318739a5a3b6544a41354ed68ea0/fbe8a0b088e9247a2e1726cc8aa9b5ee4721ad8a93d57786d17c1c79c23f887e/event-scope-d397c49bcd70.json.
PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13ece57bd7c33695cb890198722249e81330a3ad5fb41c9d7808ed4ed9357712/804d758468ad38d4c18109e4bb503c96dc1b540d706c794f407e2b4d3346e39f/event-scope-d397c49bcd70.png.
The bounded manifest resource read offset=0,length=1500 failed with -32603, Artifact provenance manifest is unavailable.
No image review or complete graph diagnostics review is claimed.

Event comparison for the same narrow selector and cached before revision returned EVENT_REVISION_NOT_CACHED, Requested event graph revision is not cached or retained as a graph artifact.
No comparison delta was produced, and the current graph was not compared with itself.
No external tool source or dependencies were edited to conceal these gaps.

## Skipped validation and remaining representation gaps

Primary native getter/normal-field/constant width and precision, observed subtype/variant delivery, and exact fractional or very large lifetime sums are not proven by these source fixtures.
The pending representation protocol has no approved wider exact writer or recovery routine in this bounded assignment.
A known wide-stock or fractional source case therefore remains explicitly unresolved even where captured native fixture values were preserved.
No helper completion or Gods completion claim is made.
All owner hook integration, full native event validation and independent parent review remain queued.
Treaty-breach source proof is still blocked by the missing accepted participant continuing-promise owner, and no generic mark_offender treaty writer was introduced.
