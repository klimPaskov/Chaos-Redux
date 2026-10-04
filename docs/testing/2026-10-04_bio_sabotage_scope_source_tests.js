// Bounded source execution, not an HOI4 engine emulator or live-game result.
// Parser shape follows exact_quote_source_tests.js, with bare-list tokens and source locations.
// Run from any directory: node docs/testing/2026-10-04_bio_sabotage_scope_source_tests.js
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '../..');
const baselineRoot = path.join(root, 'docs/testing/2026-10-04_bio_sabotage_scope_probability/baseline_source');
const primary = ['common/scripted_triggers/biological_sabotage_triggers.txt',
  'common/scripted_triggers/biological_sabotage_raid_triggers.txt', 'common/raids/biological_sabotage_raids.txt'];
const dependencies = ['common/scripted_triggers/cbrn_diplomacy_triggers.txt',
  'common/scripted_triggers/cbrn_triggers.txt', 'common/scripted_triggers/biological_lifecycle_triggers.txt',
  'common/scripted_triggers/002_zombie_outbreak_triggers.txt',
  'common/script_constants/biological_sabotage_constants.txt',
  'common/script_constants/biological_lifecycle_constants.txt', 'common/script_constants/cbrn_system_constants.txt'];
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const field = (nodes, key) => nodes.find(n => n.key === key)?.value;
function parse(source, file) {
  const tokens = [...source.matchAll(/#[^\r\n]*|"[^"\r\n]*"|[{}=<>]|[^\s{}=<>#]+/g)]
    .filter(m => !m[0].startsWith('#')).map(m => ({text:m[0], at:m.index}));
  let i = 0;
  function body(nested = false) {
    const out = [];
    while (i < tokens.length && tokens[i].text !== '}') {
      const token = tokens[i++], key = token.text;
      let op = null, value = null;
      if (key === '{') value = body(true);
      else if (tokens[i] && ['=', '<', '>'].includes(tokens[i].text)) {
        op = tokens[i++].text;
        value = tokens[i++]?.text;
        assert.notEqual(value, undefined, `missing value ${file}:${key}`);
        if (value === '{') value = body(true);
      }
      out.push({key, op, value, file, line:source.slice(0, token.at).split('\n').length});
    }
    if (nested) assert.equal(tokens[i++]?.text, '}');
    return out;
  }
  const out = body(); assert.equal(i, tokens.length, `parse ended early ${file}:${source.slice(0,tokens[i]?.at).split('\n').length} around ${tokens[i]?.text}`); return out;
}
function load(base, files) {
  const sources = new Map(), trees = new Map(), definitions = new Map();
  for (const file of files) {
    const bytes = fs.readFileSync(path.join(base, file));
    sources.set(file, {sha256:hash(bytes), text:bytes.toString('utf8')});
    const tree = parse(bytes.toString('utf8'), file); trees.set(file, tree);
    if (file.includes('/scripted_triggers/')) for (const n of tree) definitions.set(n.key, n.value);
  }
  return {sources, trees, definitions};
}
const current = load(root, [...primary, ...dependencies]);
const baseline = load(baselineRoot, primary);
// Dependencies were not patched by this repair. Record current hashes rather than imply old snapshots exist.
for (const file of dependencies.filter(f=>f.includes('/scripted_triggers/'))) {
  for (const n of current.trees.get(file)) if (!baseline.definitions.has(n.key)) baseline.definitions.set(n.key,n.value);
}
const constants = new Map();
for (const [file, tree] of current.trees) if (file.includes('/script_constants/')) {
  for (const cat of tree) for (const n of Array.isArray(cat.value) ? cat.value : []) {
    if (/^-?\d+(\.\d+)?$/.test(n.value)) constants.set(`constant:${cat.key}.${n.key}`, Number(n.value));
  }
}
const clean = nodes => nodes.map(n => ({key:n.key, op:n.op, value:Array.isArray(n.value) ? clean(n.value) : n.value}));
const cases = [], limitations = [
  'Source interpreter executes only listed primitive triggers and explicit fixture objects. It is not the native engine.',
  'Temporary cleanup is a conservative lexical helper-frame model inherited from exact_quote_source_tests.js, not measured engine behavior.',
  'AI invalid-victim gating and unchanged numeric formula tokens are tested. Full weighted AI scenario evaluation belongs to the separate probability audit.',
  'No HOI4 launch was performed. Absence of native Invalid Scope warnings remains live consumer evidence supplied by the user.',
  'Baseline has immutable copies of the three main files. Policy/lifecycle dependencies use current source and are separately hashed.'
];
function check(name, fn) {
  try { const evidence = fn(); cases.push({name, passed:true, evidence}); }
  catch (error) { cases.push({name, passed:false, error:error.stack}); }
}
const country = (tag, id) => ({type:'COUNTRY',tag,id,exists:true,vars:{},flags:new Set(),tech:new Set()});
function fixture(overrides = {}) {
  const actor = country('ACT', 11), victim = country('VIC', 22), stranger = country('OTHER', 33), zombie = country('ZZZ', 44);
  const state = {type:'STATE',id:101,controller:victim,owner:victim,vars:{},flags:new Set(),population:5000,
    category:'metropolis',buildings:{naval_base:1,supply_node:1,industrial_complex:5,arms_factory:5,biowarfare_facility:1},impassable:false,capital:true,divisions:true};
  actor.vars.cbrn_use_policy = constants.get('constant:cbrn_use_policy.unrestricted_authorization');
  const f = {actor,victim,stranger,zombie,state,root:actor,from:victim,wars:new Set(['ACT:VIC','VIC:ACT']),day:100};
  overrides.configure?.(f); return f;
}
class VM {
  constructor(defs, f) { this.defs=defs; this.f=f; this.temps=new Map(); this.trace=[]; this.writes=[]; this.cleanup=0; }
  scope(token, ctx) {
    switch(token.toUpperCase()) {
      case 'ROOT': return this.f.root;
      case 'FROM': return this.f.from;
      case 'PREV': return ctx.prev;
      case 'CONTROLLER': return ctx.this.controller;
      case 'OWNER': return ctx.this.owner;
      case 'VAR:TARGET_STATE': return this.f.state;
      case 'ZZZ': return this.f.zombie;
      default: throw Error(`unsupported scope ${token}`);
    }
  }
  value(token, ctx) {
    if (/^-?\d+(\.\d+)?$/.test(token)) return Number(token);
    if (constants.has(token)) return constants.get(token);
    if (token === 'id') return ctx.this.id;
    if (token === 'global.num_days') return this.f.day;
    return this.temps.get(token) ?? ctx.this.vars[token] ?? 0;
  }
  call(name, ctx = {this:this.f.actor,prev:null}) {
    assert(this.defs.has(name), `missing actual helper ${name}`);
    const inherited = new Set(this.temps.keys());
    try { return this.eval(this.defs.get(name),ctx); }
    finally { for (const key of this.temps.keys()) if (!inherited.has(key)) {this.temps.delete(key);this.cleanup++;} }
  }
  eval(nodes,ctx) { for (const n of nodes) if (!this.node(n,ctx)) return false; return true; }
  node(n,ctx) {
    const {key:k,value:v,op} = n; this.trace.push({key:k,scope:ctx.this.type,tag:ctx.this.tag,file:n.file,line:n.line});
    const need = type => assert.equal(ctx.this.type,type,`Invalid Scope ${k}: ${ctx.this.type} at ${n.file}:${n.line}`);
    if (k === 'AND' || k === 'hidden_trigger') return this.eval(v,ctx);
    if (k === 'NOT') return !v.some(item => this.node(item,ctx));
    if (k === 'OR') return v.some(item => this.node(item,ctx));
    if (k === 'custom_trigger_tooltip') return this.eval(v.filter(item=>item.key!=='tooltip'),ctx);
    if (['ROOT','FROM','PREV','CONTROLLER','OWNER','var:target_state','controller'].includes(k)) {
      const target=this.scope(k,ctx); assert(target,`absent ${k}`);return this.eval(v,{this:target,prev:ctx.this});
    }
    if (this.defs.has(k)) return this.call(k,ctx) === (v !== 'no');
    if (k === 'always') return v==='yes';
    if (k === 'exists') {need('COUNTRY');return ctx.this.exists===(v==='yes');}
    if (['tag','is_in_faction_with','is_subject_of','has_war_with'].includes(k)) {
      need('COUNTRY');const target=this.scope(v,ctx);assert.equal(target.type,'COUNTRY',`Invalid target ${k}:${v}`);
      if (k==='tag') return ctx.this.tag===target.tag;
      if (k==='is_in_faction_with') return Boolean(ctx.this.faction && ctx.this.faction===target.faction);
      if (k==='is_subject_of') return ctx.this.overlord===target.tag;
      return this.f.wars.has(`${ctx.this.tag}:${target.tag}`);
    }
    if (k==='set_temp_variable') {
      const key=field(v,'var')??v[0].key, val=this.value(field(v,'value')??v[0].value,ctx);
      this.temps.set(key,val);this.writes.push({key,value:val,scope:ctx.this.type,tag:ctx.this.tag});return true;
    }
    if (k==='has_variable') return this.temps.has(v)||Object.hasOwn(ctx.this.vars,v);
    if (k==='check_variable') {
      const long=field(v,'var'), left=this.value(long??v[0].key,ctx),right=this.value(long?field(v,'value'):v[0].value,ctx);
      const comp=field(v,'compare')??v[0].op;
      const answer={'=':left===right,equals:left===right,not_equals:left!==right,'<':left<right,'>':left>right,
        less_than:left<right,greater_than:left>right,less_than_or_equals:left<=right,greater_than_or_equals:left>=right}[comp];
      assert.notEqual(answer,undefined,`unsupported compare ${comp}`);return answer;
    }
    if (k==='meta_trigger') {
      assert.equal(field(v,'TARGET_ID'),'"[?cbrn_retaliation_target_id|.0]"');
      const id=this.value('cbrn_retaliation_target_id',ctx);assert(Number.isInteger(id));
      const replace=nodes=>nodes.map(x=>({...x,key:x.key.replaceAll('[TARGET_ID]',String(id)),
        value:Array.isArray(x.value)?replace(x.value):x.value?.replaceAll('[TARGET_ID]',String(id))}));
      return this.eval(replace(field(v,'text')),ctx);
    }
    if (k==='has_country_flag') {need('COUNTRY');return ctx.this.flags.has(v);}
    if (k==='has_state_flag') {need('STATE');return ctx.this.flags.has(v);}
    if (k==='has_tech') {need('COUNTRY');return ctx.this.tech.has(v);}
    if (k==='is_controlled_by') {need('STATE');return ctx.this.controller===this.scope(v,ctx);}
    if (k==='impassable') {need('STATE');return ctx.this.impassable===(v==='yes');}
    if (k==='has_state_category') {need('STATE');return ctx.this.category===v;}
    if (k==='is_capital') {need('STATE');return ctx.this.capital===(v==='yes');}
    if (k==='any_state_division') {need('STATE');return ctx.this.divisions&&v.every(x=>x.key==='always'&&x.value==='yes');}
    if (k==='state_population_k'||Object.hasOwn(this.f.state.buildings,k)) {
      need('STATE');const val=k==='state_population_k'?ctx.this.population:ctx.this.buildings[k];
      assert.equal(op,'>');return val>this.value(v,ctx);
    }
    throw Error(`unsupported command ${k} at ${n.file}:${n.line}`);
  }
}
const profiles=['anthrax','plague','tularemia','smallpox'].map(agent=>`bio_sabotage_${agent}_target_state`);
const countryOnly=new Set(['tag','is_in_faction_with','is_subject_of','has_war_with','exists','has_country_flag','has_tech']);
function scopeWalk(defs,name,rootType) {
  const findings=[],unresolved=[],visited=new Set();
  function visit(nodes,here,prev,stack) {
    for (const n of nodes) {
      const k=n.key;
      if (defs.has(k)) {
        const signature=`${k}:${here}:${prev}:${rootType}`;
        if (!visited.has(signature)) {visited.add(signature);visit(defs.get(k),here,prev,[...stack,k]);}
      } else if (['ROOT','FROM','PREV','CONTROLLER','OWNER','controller','var:target_state'].includes(k)) {
        const next={ROOT:rootType,FROM:'COUNTRY',PREV:prev,CONTROLLER:'COUNTRY',OWNER:'COUNTRY',controller:'COUNTRY','var:target_state':'STATE'}[k];
        visit(n.value,next,here,[...stack,k]);
      } else if (['AND','OR','NOT','hidden_trigger'].includes(k)) visit(n.value,here,prev,stack);
      else if (countryOnly.has(k)) {
        if (here!=='COUNTRY') findings.push({key:k,scope:here,file:n.file,line:n.line,stack});
        if (['tag','is_in_faction_with','is_subject_of','has_war_with'].includes(k)&&n.value==='ROOT'&&rootType!=='COUNTRY')
          findings.push({key:k,target:'ROOT',targetScope:rootType,file:n.file,line:n.line,stack});
      } else if (!['impassable','state_population_k','has_state_flag','has_state_category','is_capital','any_state_division',
        'always','is_controlled_by','naval_base','supply_node','industrial_complex','arms_factory','biowarfare_facility',
        'set_temp_variable','check_variable','meta_trigger','has_variable'].includes(k)) unresolved.push({key:k,file:n.file,line:n.line});
    }
  }
  visit(defs.get(name),'STATE',null,[name]);return {findings,unresolved,expanded:[...visited]};
}
for (const profile of profiles) {
  check(`baseline ROOT STATE reproduces ${profile}`,()=>{
    const walk=scopeWalk(baseline.definitions,profile,'STATE');
    assert(walk.findings.some(x=>x.key==='is_in_faction_with'&&x.scope==='STATE'));
    return walk;
  });
  check(`patched raw ROOT STATE physical profile ${profile}`,()=>{
    const walk=scopeWalk(current.definitions,profile,'STATE');assert.deepEqual(walk.findings,[]);assert.deepEqual(walk.unresolved,[]);
    const f=fixture();f.root=f.state;
    const vm=new VM(current.definitions,f);assert(vm.call(profile,{this:f.state,prev:null}));
    return {walk,executedNodes:vm.trace.length};
  });
}
const relationship='bio_sabotage_actor_relationship_with_from_is_valid';
const policy = key => constants.get(`constant:cbrn_use_policy.${key}`);
const relationships = [
  ['war unrestricted',true,()=>{}],
  ['self',false,f=>{f.from=f.actor;}],
  ['victim missing',false,f=>{f.victim.exists=false;}],
  ['same faction',false,f=>{f.actor.faction=f.victim.faction='ALLY';}],
  ['actor subject of victim',false,f=>{f.actor.overlord=f.victim.tag;}],
  ['victim subject of actor',false,f=>{f.victim.overlord=f.actor.tag;}],
  ['war defensive unauthorized',false,f=>{f.actor.vars.cbrn_use_policy=policy('defensive_preparation');}],
  ['war battlefield only',false,f=>{f.actor.vars.cbrn_use_policy=policy('limited_battlefield_authority');}],
  ['war reserved strategic value',false,f=>{f.actor.vars.cbrn_use_policy=policy('strategic_release_authority');}],
  ['war exact retaliation current day',true,f=>{f.actor.vars.cbrn_use_policy=policy('retaliation_only');f.actor.vars.cbrn_retaliation_22_expiry_day=100;}],
  ['war exact retaliation future day',true,f=>{f.actor.vars.cbrn_use_policy=policy('retaliation_only');f.actor.vars.cbrn_retaliation_22_expiry_day=101;}],
  ['war expired exact retaliation',false,f=>{f.actor.vars.cbrn_use_policy=policy('retaliation_only');f.actor.vars.cbrn_retaliation_22_expiry_day=99;}],
  ['war retaliation other opponent',false,f=>{f.actor.vars.cbrn_use_policy=policy('retaliation_only');f.actor.vars.cbrn_retaliation_33_expiry_day=101;}],
  ['peace unrestricted',true,f=>{f.wars.clear();}],
  ['peace exact retaliation',false,f=>{f.wars.clear();f.actor.vars.cbrn_use_policy=policy('retaliation_only');f.actor.vars.cbrn_retaliation_22_expiry_day=101;}],
  ['peace battlefield',false,f=>{f.wars.clear();f.actor.vars.cbrn_use_policy=policy('limited_battlefield_authority');}]
];
for (const [name,expected,configure] of relationships) check(`relationship ${name}`,()=>{
  const f=fixture({configure}), vm=new VM(current.definitions,f), before=JSON.stringify(f.actor.vars);
  const result=vm.call(relationship);assert.equal(result,expected);assert.equal(vm.temps.size,0);
  assert.equal(JSON.stringify(f.actor.vars),before);
  for (const write of vm.writes) {
    assert.equal(write.key,'cbrn_retaliation_target_id');assert.equal(write.scope,'COUNTRY');
    if(write.value===0)assert.equal(write.tag,f.actor.tag);
    else {assert.equal(write.tag,f.from.tag);assert.equal(write.value,f.from.id);}
  }
  return {result,policy:f.actor.vars.cbrn_use_policy,writes:vm.writes,cleanup:vm.cleanup,policyStub:false};
});
for (const [name,expected,configure] of relationships) check(`preserved actor-context authorization ${name}`,()=>{
  const f=fixture({configure});f.state.controller=f.from;
  const oldVM=new VM(baseline.definitions,f),newVM=new VM(current.definitions,f);
  const old=oldVM.call('bio_sabotage_state_relationship_is_valid',{this:f.state,prev:f.actor});
  const next=newVM.call(relationship);assert.equal(old,expected);assert.equal(next,old);
  return {old,new:next,root:'COUNTRY',stateController:f.state.controller.tag,policyStub:false};
});
check('actual old ROOT STATE country command reproduces scope failure',()=>{
  const controller=field(baseline.definitions.get('bio_sabotage_state_relationship_is_valid'),'CONTROLLER');
  const rootBody=field(controller,'ROOT');const command=field(rootBody,'NOT').find(n=>n.key==='is_in_faction_with');
  assert(command);const f=fixture();f.root=f.state;
  const vm=new VM(baseline.definitions,f);let message;
  try {vm.node(command,{this:f.state,prev:f.victim});}catch(error){message=error.message;}
  assert(message?.includes('Invalid Scope is_in_faction_with: STATE'));
  return {error:message,sourceNode:command};
});
check('actor existence is checked before victim policy',()=>{
  const f=fixture();f.actor.exists=false;const vm=new VM(current.definitions,f);
  assert.equal(vm.call(relationship),false);assert.deepEqual(vm.writes,[]);return {actorMissingRejected:true};
});
check('selected state controller must equal FROM',()=>{
  const f=fixture(), vm=new VM(current.definitions,f);assert(vm.call('bio_sabotage_raid_target_from_is_valid'));
  f.state.controller=f.stranger;assert.equal(vm.call('bio_sabotage_raid_target_from_is_valid'),false);
  return {matches:true,mismatchRejected:true};
});
check('helper cleanup preserves inherited scratch and creates no persistent variables',()=>{
  const f=fixture(),vm=new VM(current.definitions,f);vm.temps.set('cbrn_retaliation_target_id',999);
  assert(vm.call(relationship));assert.equal(vm.temps.get('cbrn_retaliation_target_id'),22);
  assert.deepEqual(Object.keys(f.actor.vars),['cbrn_use_policy']);
  return {inheritedScratch:22,newTemporaryNames:[...vm.temps.keys()],regularVars:f.actor.vars};
});
function expandOrder(nodes,here,defs,output,stack=[]) {
  for (const n of nodes) {
    if (defs.has(n.key)) {
      output.push({key:n.key,scope:here,file:n.file,line:n.line});
      if (!stack.includes(n.key)) expandOrder(defs.get(n.key),here,defs,output,[...stack,n.key]);
    } else if (['custom_trigger_tooltip','hidden_trigger','AND','OR','NOT'].includes(n.key)) expandOrder(n.value,here,defs,output,stack);
    else if (['ROOT','FROM','var:target_state'].includes(n.key)) expandOrder(n.value,n.key==='var:target_state'?'STATE':'COUNTRY',defs,output,stack);
  }
}
const raids=current.trees.get(primary[2]).filter(n=>Array.isArray(n.value)).flatMap(n=>['raid_types','types'].includes(n.key)?n.value:[n]).filter(n=>n.key.startsWith('bio_sabotage_'));
check('all twelve native raid types discovered',()=>{assert.equal(raids.length,12);return raids.map(n=>n.key);});
for (const raid of raids) {
  for (const phase of ['show_target','available','launchable']) check(`${raid.key} ${phase} COUNTRY gate before physical profile`,()=>{
    const order=[];expandOrder(field(raid.value,phase),'COUNTRY',current.definitions,order);
    const gate=order.findIndex(n=>n.key===relationship),profile=order.findIndex(n=>profiles.includes(n.key));
    assert(gate!==-1&&profile!==-1&&gate<profile);assert.equal(order[gate].scope,'COUNTRY');assert.equal(order[profile].scope,'STATE');return order;
  });
  check(`${raid.key} raw state target stays actor neutral`,()=>{
    const state=field(field(raid.value,'target_type'),'state');assert(state);
    const profile=state.find(n=>profiles.includes(n.key));assert(profile);
    const walk=scopeWalk(current.definitions,profile.key,'STATE');assert.deepEqual(walk.findings,[]);return {profile:profile.key};
  });
  check(`${raid.key} AI invalid-victim factor precedes later boosts and formula unchanged`,()=>{
    const ai=field(raid.value,'ai_will_do');assert(ai);
    const baselineRaid=baseline.trees.get(primary[2]).flatMap(n=>['raid_types','types'].includes(n.key)?n.value:[n]).find(n=>n.key===raid.key);
    assert(baselineRaid);assert.deepEqual(clean(ai),clean(field(baselineRaid.value,'ai_will_do')));
    const mods=ai.filter(n=>n.key==='modifier'),disabled=mods.findIndex(n=>field(n.value,'factor')==='constant:bio_sabotage_ai.disabled');
    assert(disabled!==-1);assert.equal(constants.get('constant:bio_sabotage_ai.disabled'),0);
    assert(mods.slice(disabled+1).some(n=>field(n.value,'factor')==='constant:bio_sabotage_ai.retaliation_factor'));
    for (const [name,,configure] of relationships.filter(x=>x[1]===false)) {
      const f=fixture({configure}),vm=new VM(current.definitions,f);
      assert(vm.eval(mods[disabled].value.filter(n=>n.key!=='factor'),{this:f.actor,prev:null}),name);
      assert(!vm.trace.some(n=>n.key==='bio_kruger_last_resort_ai_is_valid'),`invalid victim reached later AI rules ${name}`);
    }
    return {unchangedAIFormula:true,disabledFactor:0,disabledModifierIndex:disabled,invalidFixtures:relationships.filter(x=>x[1]===false).map(x=>x[0])};
  });
}
check('shared tuning file unchanged from immutable probability baseline',()=>{
  const f='common/script_constants/biological_sabotage_constants.txt';
  const old=fs.readFileSync(path.join(baselineRoot,f));assert.equal(hash(old),current.sources.get(f).sha256);return {sha256:hash(old)};
});
const results={generatedAt:new Date().toISOString(),kind:'bounded-source-semantic-evidence',
  passed:cases.every(n=>n.passed),caseCount:cases.length,failed:cases.filter(n=>!n.passed).length,
  primarySourceHashes:Object.fromEntries(primary.map(f=>[f,current.sources.get(f).sha256])),
  baselineHashes:Object.fromEntries([...baseline.sources].map(([f,s])=>[f,s.sha256])),
  dependencySourceHashes:Object.fromEntries(dependencies.map(f=>[f,current.sources.get(f).sha256])),
  oldRelationshipBody:baseline.definitions.get('bio_sabotage_state_relationship_is_valid'),cases,limitations};
fs.writeFileSync(path.join(__dirname,'2026-10-04_bio_sabotage_scope_source_tests_results.json'),JSON.stringify(results,null,2)+'\n');
console.log(JSON.stringify({passed:results.passed,caseCount:results.caseCount,failed:results.failed,
  failingCases:cases.filter(n=>!n.passed).map(n=>({name:n.name,error:n.error.split('\n').slice(0,3).join('\n')})),primarySourceHashes:results.primarySourceHashes},null,2));
if(!results.passed)process.exitCode=1;
