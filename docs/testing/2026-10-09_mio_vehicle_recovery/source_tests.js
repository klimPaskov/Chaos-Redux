// Actual MIO callback, trait predicates and state recalculation under modeled native scopes.
// Native MIO completion timing and visible modifier delivery remain separate acceptance.
const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict'), crypto = require('node:crypto');
const root = path.resolve(__dirname, '../../..');
const {VM, parse, ticks, S, definitions, constants} = require(path.join(root, 'docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js'));
const mioFile = 'common/military_industrial_organization/organizations/cbrn_chemical_protection_organizations.txt';
const effectFile = 'common/scripted_effects/cbrn_designer_effects.txt';
const triggerFile = 'common/scripted_triggers/cbrn_designer_triggers.txt';
const nationalFile = 'common/military_industrial_organization/organizations/cbrn_national_organizations.txt';
const trait = 'cbrn_decon_vehicle_recovery_teams', helper = 'cbrn_designer_refresh_contaminated_state_vehicle_attrition';
const read = name => fs.readFileSync(path.join(root, name), 'utf8');
const before = name => fs.readFileSync(path.join(__dirname, 'before', name), 'utf8');
const get = (nodes, key) => {const all = nodes.filter(n => n.key === key); assert.equal(all.length, 1, key); return all[0].value;};
const traitNode = nodes => get(nodes, 'cbrn_chemical_protection_consortium').find(n => n.key === 'trait' && get(n.value, 'token') === trait);
const oldMio = parse(before(mioFile)), newMio = parse(read(mioFile));
const oldCallback = get(traitNode(oldMio).value, 'on_complete'), callback = get(traitNode(newMio).value, 'on_complete');
const sourceFiles = [mioFile, effectFile, triggerFile, nationalFile, 'common/script_constants/chemical_warfare_constants.txt', 'common/script_constants/cbrn_designer_constants.txt', 'common/on_actions/cbrn_designer_on_actions.txt'];
for (const [file, key, token] of [
 ['common/script_constants/chemical_warfare_constants.txt','truck_attrition','constant:chem_state.mult.truck_attrition'],
 ['common/script_constants/cbrn_designer_constants.txt','vehicle_recovery_attrition_mult','constant:cbrn_decontamination_designer_effect.vehicle_recovery_attrition_mult'],
]) {
 const matches=[...read(file).matchAll(new RegExp('^\\s*'+key+'\\s*=\\s*(-?\\d+(?:\\.\\d+)?)\\s*$','gm'))];
 assert.equal(matches.length,1,key); constants.set(token,ticks(matches[0][1]));
}
for (const file of [effectFile, triggerFile]) for (const n of parse(read(file))) definitions.set(n.key, n.value);
class ScopedVM extends VM {
 constructor(country, states) {super(); this.country=country; this.states=states; this.scope=country; this.regularVars=country.vars; this.refreshes=[]; this.tooltips=[];}
 scoped(scope, body) {
  const previous=this.scope, variables=this.regularVars;
  this.scope=scope; this.regularVars=scope.vars;
  try {return this.eval(body);} finally {this.scope=previous; this.regularVars=variables;}
 }
 eval(nodes) {
  const native = new Set(['FROM','CONTROLLER','every_controlled_state','any_military_industrial_organization','is_military_industrial_organization','is_mio_trait_completed','include_invisible','custom_effect_tooltip','hidden_effect','has_dynamic_modifier','force_update_dynamic_modifier']);
  for (let i=0; i<nodes.length; i++) {
   const {key:k,value:v}=nodes[i];
   if (!native.has(k)) {
    let end=i+1; while (end<nodes.length && !native.has(nodes[end].key)) end++;
    if (!super.eval(nodes.slice(i,end))) return false;
    i=end-1; continue;
   }
   if (k==='FROM') {assert.equal(this.scope.kind,'industrial_org'); if (!this.scoped(this.country,v)) return false;}
   else if (k==='CONTROLLER') {assert.equal(this.scope.kind,'state'); if (!this.scoped(this.scope.controller,v)) return false;}
   else if (k==='every_controlled_state') {
    assert.equal(this.scope.kind,'country'); const controller=this.scope;
    for (const state of this.states.filter(s=>s.controller===controller)) {
     this.scoped(state, parseScope(v));
    }
   } else if (k==='any_military_industrial_organization') {
    assert.equal(this.scope.kind,'country');
    if (!this.scope.mios.some(mio=>this.scoped(mio,v))) return false;
   } else if (k==='is_military_industrial_organization') {assert.equal(this.scope.kind,'industrial_org'); if (this.scope.id!==v) return false;}
   else if (k==='is_mio_trait_completed') {assert.equal(this.scope.kind,'industrial_org'); if (!this.scope.traits.has(v)) return false;}
   else if (k==='include_invisible') assert.equal(v,'yes');
   else if (k==='custom_effect_tooltip') this.tooltips.push(v);
   else if (k==='hidden_effect') {if (!this.eval(v)) return false;}
   else if (k==='has_dynamic_modifier') {assert.equal(this.scope.kind,'state'); const id=Array.isArray(v)?get(v,'modifier'):v; if (!this.scope.modifiers.has(id)) return false;}
   else if (k==='force_update_dynamic_modifier') {assert.equal(this.scope.kind,'state'); this.refreshes.push(this.scope.id);}
  }
  return true;
 }
}
function parseScope(nodes) {return [{key:'if',op:'=',value:[{key:'limit',op:'=',value:nodes.find(n=>n.key==='limit')?.value||[]}, ...nodes.filter(n=>n.key!=='limit')]}];}
const country=(id,mios=[])=>({kind:'country',id,vars:new Map(),mios:mios.map(([token,done=true])=>({kind:'industrial_org',id:token,vars:new Map(),traits:new Set(done?[trait]:[])}))});
function state(id,controller,strength,stored,active=true) {
 const vars=new Map(); if (strength!==null) vars.set('cbrn_chemical_effective_strength',ticks(strength));
 if (stored!==null) vars.set('cbrn_chemical_truck_attrition',ticks(stored));
 return {kind:'state',id,controller,vars,modifiers:new Set(active?['chem_state_contamination']:[])};
}
const families=['cbrn_chemical_protection_consortium','cbrn_ici_organization','cbrn_dupont_organization','cbrn_montecatini_organization'];
const results=[];
function test(name,fn) {try {fn(); results.push({name,passed:true});} catch(e) {results.push({name,passed:false,error:e.message});}}
function invoke(vm,body=callback) {return vm.scoped(vm.country.mios[0],body);}
const amount=s=>s.vars.get('cbrn_chemical_truck_attrition');
test('original callback reproduces a stale existing contaminated-state penalty',()=>{
 const c=country('ENG',[[families[1]]]), s=state('1',c,'-0.8','0.6'), vm=new ScopedVM(c,[s]);
 invoke(vm,oldCallback); assert.equal(amount(s),ticks('.6')); assert.equal(vm.refreshes.length,0);
});
for (const id of families) test(id+': completed trait immediately refreshes existing contamination',()=>{
 const c=country('actor',[[id]]), s=state('1',c,'-0.8','0.6'), vm=new ScopedVM(c,[s]);
 invoke(vm); assert.equal(amount(s),ticks('.33')); assert.deepEqual(vm.refreshes,['1']);
 assert.deepEqual(vm.tooltips,[trait+'_tt']);
});
test('only actor-controlled states change, including occupied states',()=>{
 const c=country('actor',[[families[0]]]), foreign=country('other'), own=state('home',c,'-.4','.3'), occupied=state('occupied',c,'-.8','.6'), lost=state('lost',foreign,'-.8','.6');
 const vm=new ScopedVM(c,[own,occupied,lost]); invoke(vm);
 assert.equal(amount(own),ticks('.165')); assert.equal(amount(occupied),ticks('.33')); assert.equal(amount(lost),ticks('.6'));
 assert.deepEqual(vm.refreshes,['home','occupied']);
});
test('a state without contamination input is untouched',()=>{
 const c=country('actor',[[families[0]]]), s=state('clean',c,null,null,false), vm=new ScopedVM(c,[s]); invoke(vm);
 assert.equal(s.vars.size,0); assert.equal(vm.refreshes.length,0);
});
test('cached input without an active modifier does not create or force a modifier',()=>{
 const c=country('actor',[[families[0]]]), s=state('expired',c,'-.4','.3',false), vm=new ScopedVM(c,[s]); invoke(vm);
 assert.equal(amount(s),ticks('.165')); assert.equal(s.modifiers.size,0); assert.equal(vm.refreshes.length,0);
});
test('multiple completed organizations and repeated callbacks do not stack',()=>{
 const c=country('actor',families.map(id=>[id])), s=state('1',c,'-.8','.6'), vm=new ScopedVM(c,[s]);
 invoke(vm); invoke(vm); assert.equal(amount(s),ticks('.33')); assert.equal(vm.refreshes.length,2);
});
for (const [id,done] of [[families[0],false],['cbrn_biomedical_industry_directorate',true]]) test(id+'/'+done+': no qualifying completed recovery trait gives no reduction',()=>{
 const c=country('actor',[[id,done]]), s=state('1',c,'-.8','.6'), vm=new ScopedVM(c,[s]); invoke(vm); assert.equal(amount(s),ticks('.6'));
});
test('control transfer refresh reads the new controller, removing the prior benefit',()=>{
 const c=country('old',[[families[0]]]), newer=country('new'), s=state('1',c,'-.8','.6'), vm=new ScopedVM(c,[s]); invoke(vm);
 s.controller=newer; vm.scoped(s,[{key:helper,op:'=',value:'yes'}]); assert.equal(amount(s),ticks('.6'));
});
test('empty country requires no state action',()=>{
 const c=country('actor',[[families[0]]]), vm=new ScopedVM(c,[]); invoke(vm); assert.equal(vm.refreshes.length,0);
});
test('national organization inheritance retains this common trait callback',()=>{
 const national=parse(read(nationalFile));
 for (const id of families.slice(1)) {
  const body=get(national,id); assert.equal(get(body,'include'),families[0]);
  assert(!body.some(n=>n.key==='override_trait' && get(n.value,'token')===trait));
 }
});
test('all original MIO fields and weights except the callback remain equal',()=>{
 const expected=structuredClone(newMio); const node=traitNode(expected);
 node.value.find(n=>n.key==='on_complete').value=oldCallback;
 assert.deepEqual(expected,oldMio);
 assert.deepEqual(parse(read(effectFile)),parse(before(effectFile)),'helper arithmetic and all effect bodies unchanged');
});
const failed=results.filter(r=>!r.passed);
const receipt={status:failed.length?'failed':'passed_source_native_completion_unproved',testsRun:results.length,failures:failed.length,results,
 sources:sourceFiles.map(file=>({path:file,sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(root,file))).digest('hex')})),
 limits:['Native FROM binding, control iterators, completed-trait predicates and dynamic-modifier refresh are explicit modeled dependencies.', 'The unchanged BaseVM conservative helper temporary lifetime is retained.', 'Source arithmetic verifies 0.6 to 0.33 at strength -0.8 without stacking; no engine attrition tick or MIO UI result is claimed.']};
fs.writeFileSync(path.join(__dirname,'source_results.json'),JSON.stringify(receipt,null,2)+'\n','utf8');
console.log(JSON.stringify({status:receipt.status,testsRun:results.length,failures:failed.length}));
if(failed.length){console.error(JSON.stringify(failed,null,2));process.exitCode=1;}
