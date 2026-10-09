// Execute current/before eligibility and scheduling ASTs. Stock transactions,
// native state membership and existing profile/outbreak inputs are boundaries.
const fs=require('node:fs'), path=require('node:path'), assert=require('node:assert/strict'), sandbox=require('node:vm'), crypto=require('node:crypto');
const {VM,S,ticks,parse,definitions,constants,root}=require('../../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const previousDir=path.join(root,'docs/testing/2026-10-09_automatic_protection_repair');
const prefix=fs.readFileSync(path.join(previousDir,'automatic_protection_source_tests.js'),'utf8').split("for (const side of ['before', 'after'])")[0];
const box={exports:{}};sandbox.runInNewContext(prefix+'\nmodule.exports={ProtectionVM};',{require,module:box,__dirname:previousDir});
const {ProtectionVM}=box.exports;
const paths=['common/scripted_triggers/cbrn_protection_triggers.txt','common/scripted_effects/cbrn_protection_decision_effects.txt','common/scripted_effects/cbrn_protection_effects.txt'];
const before=paths.map(p=>fs.readFileSync(path.join(__dirname,path.basename(p)+'.before'),'utf8'));
const after=paths.map(p=>fs.readFileSync(path.join(root,p),'utf8'));
const extra=['common/scripted_triggers/cbrn_triggers.txt','common/scripted_triggers/cbw_triggers.txt'];
const extraNodes=extra.flatMap(p=>parse(fs.readFileSync(path.join(root,p),'utf8')));
const definition=(text,key)=>parse(text).find(n=>n.key===key).value;
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
for(const [file,ids] of [[1,['cbrn_complete_priority_state_distribution','cbrn_complete_state_filter_replacement','cbrn_complete_full_distribution_program','cbrn_complete_occupied_state_distribution']],[2,['cbrn_distribute_priority_masks_to_state','cbrn_distribute_requested_masks_to_state_internal','cbrn_replace_state_civilian_mask_filters','cbrn_replace_military_mask_filters','cbrn_issue_masks_to_field_army','cbrn_apply_historical_uk_1939_civilian_issue']],[0,['cbrn_state_is_valid_distribution_target','cbrn_state_can_receive_occupied_masks','cbrn_state_can_replace_civilian_filters','cbrn_country_has_public_chemical_emergency','cbrn_country_has_urgent_mask_production_need']]]) for(const id of ids) assert.deepEqual(definition(before[file],id),definition(after[file],id),id+' stays unchanged');
function load(side){
  for(const source of [...before,...after]) for(const n of parse(source)) definitions.delete(n.key);
  for(const n of extraNodes) if(Array.isArray(n.value))definitions.set(n.key,n.value);
  for(const source of side==='before'?before:after)for(const n of parse(source))if(Array.isArray(n.value))definitions.set(n.key,n.value);
}
class PriorityVM extends ProtectionVM {
  constructor(){
    super();this.controlled=['state','rural'];this.enemies=[];this.globals=new Set();this.profile='';this.bio=false;this.nonhuman=false;this.actions=[];
    this.scopes.get('state').core=true;this.scopes.get('state').controlled=true;
    this.scopes.set('rural',{vars:new Map(),flags:new Set(),tech:new Set(),stock:new Map(),native:new Map([['state_population_k',ticks(1000)]]),core:true,controlled:true});
    for(const name of this.controlled){const s=this.scopes.get(name);s.issueCost=20;s.serviceCost=10;s.vars.set('cbrn_civilian_mask_effective_coverage',ticks(0));}
    this.scopes.get('country').stock.set('gas_mask_equipment_1',ticks(200));this.scopes.get('country').tech.add('basic_gas_masks');
    this.normal('country','cbrn_military_mask_coverage',100).normal('country','cbrn_ai_military_mask_coverage_target',100).normal('country','cbrn_mask_reserve_crates',200).normal('country','cbrn_ai_mask_reserve_target_crates',200).normal('country','cbrn_mask_replacement_demand',0).normal('country','cbrn_military_mask_filter_condition',100).normal('country','cbrn_military_mask_shortage_crates',0);
  }
  stockLeft(){return Number((this.scopes.get('country').stock.get('gas_mask_equipment_1')||0n)/S);}
  spend(kind,requested){const used=Math.min(this.stockLeft(),requested);this.scopes.get('country').stock.set('gas_mask_equipment_1',ticks(this.stockLeft()-used));this.actions.push({kind,state:this.scope,used});return used;}
  run(name,allow=false){
    if(['cbrn_refresh_country_mask_snapshot','cbrn_refresh_country_civilian_decontamination_pool'].includes(name))return true;
    if(name==='cbrn_replace_military_mask_filters'){this.spend('military-filter',10);this.normal('country','cbrn_military_mask_filter_condition',100);return true;}
    if(name==='cbrn_issue_masks_to_field_army'){this.spend('military-issue',20);this.normal('country','cbrn_military_mask_shortage_crates',0);return true;}
    if(name==='cbrn_replace_state_civilian_mask_filters'){const s=this.scopes.get(this.scope);assert(!s.flags.has('cbrn_protection_project_active'));const n=this.spend('civilian-filter',s.serviceCost);if(n===s.serviceCost)this.normal(this.scope,'cbrn_civilian_mask_filter_condition',100);return true;}
    if(name==='cbrn_distribute_priority_masks_to_state'){const s=this.scopes.get(this.scope);assert(s.core&&!s.flags.has('cbrn_protection_project_active'));const n=this.spend('civilian-issue',s.issueCost);this.normal(this.scope,'cbrn_civilian_mask_effective_coverage',50*n/s.issueCost);return true;}
    if(name.startsWith('cbrn_profile_is_'))return name==='cbrn_profile_is_'+this.profile;
    if(['cbrn_country_has_public_chemical_emergency','cbrn_country_faces_enemy_chemical_capability','cbrn_country_needs_civilian_mask_issue'].includes(name))return VM.prototype.run.call(this,name,allow);
    return super.run(name,allow);
  }
  eval(nodes){
    for(let i=0;i<nodes.length;i++){
      const n=nodes[i],k=n.key,v=n.value;
      if(k==='if'){const chain=[n];while(nodes[i+1]&&['else','else_if'].includes(nodes[i+1].key))chain.push(nodes[++i]);if(!super.eval(chain))return false;}
      else if(k==='any_controlled_state'||k==='every_controlled_state'||k==='any_enemy_country'){
        const names=k==='any_enemy_country'?this.enemies:this.controlled.filter(name=>this.scopes.get(name).controlled);
        const limit=this.field(v,'limit',[]),body=v.filter(n=>n.key!=='limit');let any=false;
        for(const name of names){const yes=this.scoped(name,()=>this.eval(limit)&&this.eval(body));if(yes)any=true;if(yes&&k.startsWith('any'))break;}
        if(k.startsWith('any')&&!any)return false;
      }else if(k==='is_capital'){if((this.scope==='state')!==(v==='yes'))return false;}
      else if(k==='is_core_of'||k==='is_controlled_by'){assert.equal(v,'ROOT');if(!this.scopes.get(this.scope)[k==='is_core_of'?'core':'controlled'])return false;}
      else if(k==='any_province_building_level'){if(!this.scopes.get(this.scope).victoryPoint)return false;}
      else if(['industrial_complex','arms_factory','dockyard','air_base','naval_base','supply_node'].includes(k)){const a=this.scopes.get(this.scope).native.get(k)||0n,b=this.value(v);if(!(n.op==='>'?a>b:n.op==='<'?a<b:a===b))return false;}
      else if(k==='has_global_flag'){if(!this.globals.has(v))return false;}
      else if(k==='is_actual_nonhuman_country'){if(this.nonhuman!==(v==='yes'))return false;}
      else if(k==='has_active_biowarfare_outbreak'){if(this.bio!==(v==='yes'))return false;}
      else if(!super.eval([n]))return false;
    }return true;
  }
  country(name){return this.scoped('country',()=>this.run(name));}
  state(name,helper){return this.scoped(name,()=>this.run(helper));}
  enemy(flag,technology){this.enemies=['enemy'];this.scopes.set('enemy',{vars:new Map(),flags:new Set(flag?[flag]:[]),tech:new Set(technology?[technology]:[]),stock:new Map(),native:new Map()});}
}
const cases=[];function test(id,fn){fn();cases.push({id,passed:true});}
const result=(vm)=>({category:vm.country('cbrn_civil_defence_category_visible'),issue:vm.country('cbrn_country_needs_civilian_mask_issue'),ai:vm.country('cbrn_country_should_produce_masks')});
const scenarioResults=[];
for(const side of ['before','after'])for(const scenario of ['clean','victim-history','retaliation-only','contamination-rural','enemy-technology','enemy-use','post-alert-hospital','biological-only','UK-receipt','orphan-full-target'])test(`${side}-${scenario}`,()=>{
  load(side);const vm=new PriorityVM();
  if(scenario==='victim-history')vm.scopes.get('country').flags.add('cbrn_confirmed_chemical_attack_victim_history');
  if(scenario==='retaliation-only')vm.scopes.get('country').flags.add('cbrn_retaliation_authorized');
  if(scenario==='contamination-rural')vm.normal('rural','cbrn_chemical_contamination',100);
  if(scenario==='enemy-technology')vm.enemy(null,'chlorine_gas');
  if(scenario==='enemy-use')vm.enemy('cbrn_confirmed_chemical_use_history');
  if(scenario==='post-alert-hospital')vm.scopes.get('rural').flags.add('cbrn_hospitals_utilities_secured');
  if(scenario==='biological-only')vm.bio=true;
  if(scenario==='UK-receipt')vm.scopes.get('country').flags.add('cbrn_historical_civilian_mask_issue');
  if(scenario==='orphan-full-target'){vm.profile='mass_civil_defence';vm.scopes.get('country').flags.add('cbrn_population_registered_and_fitted');vm.scopes.get('country').flags.add('cbrn_national_respirator_reserve');for(const n of vm.controlled)vm.normal(n,'cbrn_civilian_mask_effective_coverage',50);}
  const r=result(vm);scenarioResults.push({side,scenario,...r});
  const category=['enemy-technology','enemy-use','biological-only','contamination-rural'].includes(scenario)||(side==='before'&&['victim-history','retaliation-only'].includes(scenario))||(side==='after'&&scenario==='post-alert-hospital');
  const issue=['enemy-technology','enemy-use','contamination-rural','UK-receipt'].includes(scenario)||(side==='before'&&['victim-history','retaliation-only'].includes(scenario))||(side==='after'&&scenario==='post-alert-hospital');
  assert.equal(r.category,category);assert.equal(r.issue,issue);
  if(side==='after')assert.equal(r.ai,['enemy-technology','enemy-use','contamination-rural','post-alert-hospital'].includes(scenario));
  if(scenario==='orphan-full-target')assert.equal(r.ai,side==='before');
  if(scenario==='victim-history')assert(vm.scopes.get('country').flags.has('cbrn_confirmed_chemical_attack_victim_history'));
});
load('after');
for(const flag of ['cbrn_hospitals_utilities_secured','cbrn_civilians_moved_to_shelters','cbrn_chemical_alarm_sounded','cbrn_industry_ordered_to_continue'])test('active-response-'+flag,()=>{const vm=new PriorityVM();vm.scopes.get('rural').flags.add(flag);assert(result(vm).category);assert(result(vm).issue);vm.scopes.get('rural').flags.delete(flag);assert(!result(vm).category);});
for(const coverage of [49,50,51])for(const reserve of [false,true])test(`shared-gap-${coverage}-${reserve}`,()=>{const vm=new PriorityVM();vm.normal('rural','cbrn_chemical_contamination',100).normal('rural','cbrn_civilian_mask_effective_coverage',coverage);vm.normal('state','cbrn_civilian_mask_effective_coverage',50);if(reserve)vm.scopes.get('country').flags.add('cbrn_national_respirator_reserve');assert.equal(vm.state('rural','cbrn_state_has_automatic_priority_mask_gap'),coverage<50);assert.equal(vm.state('rural','cbrn_state_can_receive_priority_masks'),reserve&&coverage<50);assert.equal(result(vm).ai,coverage<50);});
for(const invalid of ['noncore','busy','uncontrolled','empty'])test('priority-excludes-'+invalid,()=>{const vm=new PriorityVM();vm.normal('rural','cbrn_chemical_contamination',100);const s=vm.scopes.get('rural');if(invalid==='noncore')s.core=false;if(invalid==='busy')s.flags.add('cbrn_protection_project_active');if(invalid==='uncontrolled')s.controlled=false;if(invalid==='empty')s.native.set('state_population_k',0n);assert(!vm.state('rural','cbrn_state_has_automatic_priority_mask_gap'));});
function maintenanceFixture(stock){const vm=new PriorityVM();vm.scopes.get('country').stock.set('gas_mask_equipment_1',ticks(stock));vm.normal('country','cbrn_military_mask_filter_condition',90).normal('country','cbrn_military_mask_shortage_crates',20);for(const n of vm.controlled)vm.normal(n,'cbrn_civilian_mask_crates',10).normal(n,'cbrn_civilian_mask_filter_condition',90);vm.normal('rural','cbrn_chemical_contamination',100);return vm;}
const scheduleResults=[];
for(const side of ['before','after'])for(const stock of [0,30,60,90])test(`scheduling-${side}-${stock}`,()=>{load(side);const vm=maintenanceFixture(stock);vm.country('cbrn_run_protection_maintenance_cycle');scheduleResults.push({side,stock,actions:vm.actions,remaining:vm.stockLeft()});assert.equal(vm.actions.reduce((n,a)=>n+a.used,0)+vm.stockLeft(),stock);if(side==='after'&&stock>=60)assert.deepEqual(vm.actions.slice(0,4).map(a=>[a.kind,a.state]),[['military-filter','country'],['military-issue','country'],['civilian-filter','rural'],['civilian-issue','rural']]);if(stock===30)assert.equal(vm.actions.filter(a=>a.state!=='country').length,0);});
load('after');
test('busy-state-project-receipt-survives-cycle',()=>{const vm=maintenanceFixture(200);vm.scopes.get('rural').flags.add('cbrn_protection_project_active');vm.country('cbrn_run_protection_maintenance_cycle');assert(vm.scopes.get('rural').flags.has('cbrn_protection_project_active'));assert(!vm.actions.some(a=>a.state==='rural'));});
test('paid-noncore-has-filter-service-but-no-new-automatic-issue',()=>{const vm=maintenanceFixture(200);vm.scopes.get('rural').core=false;vm.country('cbrn_run_protection_maintenance_cycle');assert(vm.actions.some(a=>a.state==='rural'&&a.kind==='civilian-filter'));assert(!vm.actions.some(a=>a.state==='rural'&&a.kind==='civilian-issue'));});
test('threat-tier-services-all-before-any-issue',()=>{const vm=maintenanceFixture(200);vm.scopes.get('state').flags.add('cbrn_chemical_raid_alert_active');vm.country('cbrn_run_protection_maintenance_cycle');const c=vm.actions.filter(a=>a.state!=='country');assert.deepEqual(c.map(a=>a.kind),['civilian-filter','civilian-filter','civilian-issue','civilian-issue']);});
test('history-only-does-not-order-new-civilian-issue',()=>{const vm=maintenanceFixture(200);vm.scopes.get('rural').vars.delete('cbrn_chemical_contamination');vm.scopes.get('country').flags.add('cbrn_confirmed_chemical_attack_victim_history');vm.country('cbrn_run_protection_maintenance_cycle');assert(!vm.actions.some(a=>a.kind==='civilian-issue'));assert(vm.actions.some(a=>a.kind==='civilian-filter'));});
const report={passed:cases.length,failed:0,cases,scenarioResults,scheduleResults,sourceHashes:paths.map((p,i)=>({path:p,before:sha(Buffer.from(before[i])),after:sha(Buffer.from(after[i]))})),harnessSha256:sha(fs.readFileSync(__filename)),assumptions:['Production trigger and scheduler ASTs execute; existing transaction bodies are unchanged and separately covered by prior source suites.','Native controlled/core/VP/building membership, active flags, outbreak/profile inputs and stock transaction requests are modeled.','Stock boundaries use declared10/20-crate requests to prove ordering and conservation under scarcity, not actual native transaction cost or campaign timing.','No native AI selection, equipment settlement, UI rendering or within-tier fairness claim.']};
fs.writeFileSync(path.join(__dirname,'source_test_results.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:report.passed,failed:0,scenarioResults,scheduleResults},null,2));
