// Bounded actual-source lifetime fixtures. Native equipment and lifecycle storage
// boundaries are modeled observations, not HOI4 execution evidence.
// Run: node docs/testing/2026-10-08_bio_doomsday_lifetime_source_tests.js
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const basePath = '../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js';
const { VM: BaseVM, S, ticks, parse, definitions, constants, root } = require(basePath);
const archive = path.join(root, 'docs/testing/2026-10-08_bio_doomsday_lifetime');
const effectFile = 'common/scripted_effects/biological_doomsday_effects.txt';
const bridgeFile = 'events/cbrn_doomsday_raid_bridge.txt';
const inputFiles = JSON.parse(fs.readFileSync(path.join(archive, 'after_manifest.json'), 'utf8')).map(x => x.path);
const baseBytes = fs.readFileSync(path.join(root, 'docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js'));
const normalizedText = bytes => bytes.toString('utf8').replace(/\r\n/g, '\n');
assert.equal(normalizedText(baseBytes), normalizedText(fs.readFileSync(path.join(archive, 'before/docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js'))), 'BaseVM changed');
const read = (side, f) => fs.readFileSync(path.join(archive, side, f), 'utf8');
const unsupportedConstants = [];
function loadConstants(nodes, prefix = 'constant:') {
  for (const n of nodes) {
    if (n.key === 'schema') continue;
    if (Array.isArray(n.value)) loadConstants(n.value, prefix + n.key + '.');
    else if (/^-?\d+(\.\d+)?$/.test(n.value)) {
      if ((n.value.split('.')[1] || '').replace(/0+$/,'').length <= 5) constants.set(prefix + n.key, ticks(n.value.replace(/(\.\d*?)0+$/, '$1').replace(/\.$/,'')));
      else unsupportedConstants.push({name:prefix+n.key,value:n.value,reason:'not representable by unchanged BaseVM; not used by these bounded paths'});
    }
  }
}
// Constant schemas contain anonymous nested blocks unsupported by BaseVM's
// assignment parser. Exclude schema metadata only, preserving all value tables.
function constantSource(source) {
  let result = source, match;
  while ((match = /\bschema\s*=\s*\{/.exec(result))) {
    let end = match.index + match[0].length, depth = 1;
    while (depth && end < result.length) { const c = result[end++]; if(c === '{')depth++;if(c === '}')depth--; }
    assert.equal(depth,0); result = result.slice(0,match.index) + result.slice(end);
  }
  return result;
}
for (const f of inputFiles.filter(f => f.startsWith('common/script_constants/'))) loadConstants(parse(constantSource(read('after', f))));
const bodies = new Map();
for (const f of inputFiles.filter(f => f.startsWith('common/scripted_'))) {
  for (const n of parse(read('after', f))) bodies.set(n.key, n.value);
}
const testedLifecycle = ['reset_seed_record', 'prepare_agent_profile', 'prepare_route_profile', 'prepare_actor_doctrine_snapshot',
  'prepare_result_multipliers', 'finalize_seed_values', 'apply_biosecurity_designer_seed_modifiers', 'dispatch_seed',
  'grant_integrated_operations_release_command_recovery', 'seed_record_is_valid', 'deliberate_seed_record_is_valid',
  'accident_seed_record_is_valid', 'spread_seed_record_is_valid', 'doomsday_seed_record_is_valid',
  'state_is_eligible_ordinary_pathogen_target'];
for (const name of testedLifecycle) definitions.set('bio_lifecycle_' + name, bodies.get('bio_lifecycle_' + name));
for (const [name, body] of bodies) if (name.startsWith('bio_doomsday_')) definitions.set(name, body);
const savedDoomsday = new Map([...definitions].filter(([name]) => name.startsWith('bio_doomsday_')));
const contracts = {
  bio_doomsday_collect_target_states: { vars: ['bio_doomsday_target_count'], arrays: ['bio_doomsday_target_states'] },
  bio_doomsday_capture_and_consume_arsenal: { vars: ['bio_doomsday_stock_anthrax', 'bio_doomsday_stock_plague',
    'bio_doomsday_stock_tularemia', 'bio_doomsday_stock_smallpox', 'bio_doomsday_arsenal_consumed_total'], arrays: [] },
  bio_lifecycle_dispatch_seed: { vars: ['bio_seed_dispatch_status'], arrays: [] },
  bio_lifecycle_prepare_actor_doctrine_snapshot: { vars: ['bio_seed_doctrine_condemnation_mult'], arrays: [] },
};
// BaseVM.run is inherited unchanged: all scripted calls delete newly created
// temporary scalars/arrays on return. Scoped regular state is selected separately.
class DoomsdayVM extends BaseVM {
  constructor(options = {}) {
    super(); this.options = options; this.current = { type: 'country', id: 'ACT', vars: new Map(), flags: new Set(),
      ideas: new Set(options.doctrine ? [options.doctrine] : []), exists: true, wars: new Set(['ENM']) };
    this.actor = this.current;
    this.enemy = { type: 'country', id: 'ENM', vars: new Map(), flags: new Set(), ideas: new Set(), exists: true, wars: new Set(['ACT']) };
    this.neutral = { type: 'country', id: 'NEU', vars: new Map(), flags: new Set(), ideas: new Set(), exists: true, wars: new Set() };
    this.targets = new Map(); this.states = []; this.globalFlags = new Set(); this.debits = []; this.seeded = [];
    this.condemnations = []; this.fallout = []; this.news = []; this.boundaryCalls = {}; this.stack = [];
    this.stock = new Map(['anthrax', 'plague', 'tularemia', 'smallpox'].map((x, i) => [x + '_bomb_1', ticks((options.stocks || [0,0,0,0])[i])]));
    this.regularVars = this.current.vars;
    if (options.committed) this.actor.flags.add('bio_doomsday_raid_committed');
    if (options.integrated) this.actor.flags.add(options.integrated);
  }
  addState(id, controller = this.actor, opts = {}) {
    const state = { type: 'state', id, controller, vars: new Map(), flags: new Set(), neighbors: [], population: 100,
      category: 'rural', zombie: false, ...opts };
    this.states.push(state); return state;
  }
  inScope(scope, body) {
    assert(scope && scope.vars, 'fixture needs typed scope pointer');
    const previous = this.current; this.current = scope; this.regularVars = scope.vars;
    try { return this.eval(body); } finally { this.current = previous; this.regularVars = previous.vars; }
  }
  value(token) {
    if (token === 'THIS') return this.current;
    if (token === 'ROOT') return this.actor;
    if (token.startsWith('event_target:')) return this.targets.get(token.slice(13));
    if (token.startsWith('num_equipment@')) return this.stock.get(token.slice(14));
    if (token === 'global.num_days') return ticks(300);
    if (token === 'global.chaos_meter_value') return ticks(this.options.chaos || 0);
    return super.value(token);
  }
  write(name, value, temporary = true) {
    if (!temporary && value && typeof value === 'object') { this.regularVars.set(name, value); return; }
    super.write(name, value, temporary);
  }
  run(name, ...args) {
    if (this.options.checkContracts !== false && contracts[name]) {
      for (const x of contracts[name].vars) assert(this.vars.has(x), `missing owner ${x} before ${name}`);
      for (const x of contracts[name].arrays) assert(this.tempArrays.has(x), `missing owner array ${x} before ${name}`);
    }
    this.stack.push(name);
    try { return super.run(name, ...args); } finally { this.stack.pop(); }
  }
  boundary(name) { this.boundaryCalls[name] = (this.boundaryCalls[name] || 0) + 1; }
  eval(nodes) {
    for (let i = 0; i < nodes.length; i++) {
      const node = nodes[i], {key:k, value:v, op} = node;
      // Let BaseVM own all control flow and arithmetic it already implements.
      if (k === 'if') {
        const chain = [node]; while (nodes[i+1] && ['else_if','else'].includes(nodes[i+1].key)) chain.push(nodes[++i]);
        if (!super.eval(chain)) return false; continue;
      }
      if (k === 'hidden_effect') { if (!this.eval(v)) return false; }
      else if (k === 'meta_effect') {
        const bindings = new Map(v.filter(x => x.key !== 'text').map(x => {
          const match = x.value.match(/^"\[\?([\w]+)\|\.0\]"$/); assert(match, `unsupported interpolation ${x.value}`);
          return [x.key, String(this.value(match[1]) / S)];
        }));
        const replace = ns => ns.map(x => ({ ...x, key: x.key.replace(/\[([A-Z_]+)\]/g, (_, b) => bindings.get(b)),
          value: Array.isArray(x.value) ? replace(x.value) : x.value.replace(/\[([A-Z_]+)\]/g, (_, b) => bindings.get(b)) }));
        if (!this.eval(replace(this.field(v,'text')))) return false;
      }
      else if (k.startsWith('event_target:')) { if (!this.inScope(this.value(k), v)) return false; }
      else if (k === 'CONTROLLER') { if (!this.inScope(this.current.controller, v)) return false; }
      else if (['every_controlled_state','every_neighbor_state','any_neighbor_state'].includes(k)) {
        const scopes = k === 'every_controlled_state' ? this.states.filter(s => s.controller === this.current) : this.current.neighbors;
        const body = v.filter(x => x.key !== 'limit'), limit = this.field(v, 'limit', []);
        let found = false;
        for (const scope of scopes) {
          if (this.inScope(scope, limit)) {
            const yes = this.inScope(scope, body); found ||= yes;
            if (k === 'any_neighbor_state' && yes) break;
          }
        }
        if (k === 'any_neighbor_state' && !found) return false;
      }
      else if (k === 'for_each_scope_loop') {
        const a = [...this.array(this.field(v,'array'))], breakName = this.field(v,'break','break');
        for (const scope of a) {
          if (this.value(breakName) !== 0n) break;
          if (!this.inScope(scope, v.filter(x => !['array','break','tooltip'].includes(x.key)))) return false;
        }
      }
      else if (k === 'add_to_temp_array' || k === 'is_in_array') {
        const name = this.field(v,'array',v[0].key), token = this.field(v,'value',v[0].value), a = this.array(name);
        if (k === 'is_in_array') { if (!a.includes(this.value(token))) return false; }
        else { const copy = [...a]; copy.push(this.value(token)); this.tempArrays.set(name,copy); }
      }
      else if (k === 'save_event_target_as') this.targets.set(v,this.current);
      else if (k === 'has_event_target') { if (!this.targets.has(v)) return false; }
      else if (k === 'is_controlled_by') { if (this.current.controller !== this.value(v)) return false; }
      else if (k === 'tag') { if (this.current !== this.value(v)) return false; }
      else if (k === 'exists') { if (this.current.exists !== (v === 'yes')) return false; }
      else if (k === 'has_war_with') { if (!this.current.wars.has(this.value(v).id)) return false; }
      else if (k === 'has_capitulated') { if (Boolean(this.options.capitulated) !== (v === 'yes')) return false; }
      else if (k === 'surrender_progress') { if (!(ticks(this.options.surrender ?? 0.9) > this.value(v))) return false; }
      else if (k === 'state_population_k') {
        const rejected = this.current.reject && this.stack.includes('bio_lifecycle_dispatch_seed');
        if (!((rejected ? 0n : ticks(this.current.population)) > this.value(v))) return false;
      }
      else if (k === 'has_state_category') { if (this.current.category !== v) return false; }
      else if (k === 'is_zombie_controlled_state') { if (this.current.zombie !== (v === 'yes')) return false; }
      else if (k === 'has_idea') { if (!this.current.ideas.has(v)) return false; }
      else if (k === 'has_idea_with_trait') { return false; } // fixtures have no historical advisor trait
      else if (k === 'has_country_flag' || k === 'has_state_flag') { if (!this.current.flags.has(v)) return false; }
      else if (k === 'set_country_flag' || k === 'set_state_flag') this.current.flags.add(v);
      else if (k === 'clr_country_flag' || k === 'clr_state_flag') this.current.flags.delete(v);
      else if (k === 'set_global_flag') this.globalFlags.add(v);
      else if (k === 'has_global_flag') { if (!this.globalFlags.has(v)) return false; }
      else if (k === 'add_to_variable') { this.write(v[0].key, this.value(v[0].key) + this.value(v[0].value), false); }
      else if (k === 'round_temp_variable') {
        const x = this.value(v); this.write(v, (x + S/2n)/S*S);
      }
      else if (k === 'clamp_temp_variable') {
        const name = this.field(v,'var'), x = this.value(name), min = this.value(this.field(v,'min')), max = this.value(this.field(v,'max'));
        this.write(name,x<min?min:x>max?max:x);
      }
      else if (k === 'divide_temp_variable') {
        // Native fixed point division, truncating to five decimal places before
        // the source's round command. BaseVM exact-division rule stays unchanged.
        const name = v[0].key, divisor = this.value(v[0].value); assert(divisor !== 0n); this.write(name,this.value(name)*S/divisor);
      }
      else if (k === 'add_equipment_to_stockpile') {
        const type = this.field(v,'type'), amount = this.value(this.field(v,'amount'));
        assert(amount <= 0n); this.stock.set(type,this.stock.get(type)+amount); this.debits.push({type,amount:String(amount/S)});
      }
      else if (k === 'cbrn_ai_route_allows_unrestricted_use' || k === 'cbrn_policy_allows_extreme_use') {
        if (this.options.policy === false) return false;
      }
      else if (k.startsWith('cbrn_designer_has_')) return false; // explicit no-designer fixture
      else if (k === 'bio_lifecycle_apply_historical_actor_advisor_modifiers') this.boundary(k);
      else if (k === 'bio_stockpile_safety_capture_agent_stockpiles') this.boundary(k);
      else if (k === 'cbrn_diplomacy_classify_biological_seed_retaliation') this.boundary(k);
      else if (k === 'bio_lifecycle_store_seed_in_current_agent_record') {
        this.boundary(k); this.seeded.push({state:this.current.id,agent:Number(this.value('bio_seed_agent')/S),
          payload:Number(this.value('bio_seed_payload_consumed')/S),intensity:String(this.value('bio_seed_intensity_final')),
          concealment:String(this.value('bio_seed_concealment')),weaponization:String(this.value('bio_seed_weaponization_mult'))});
      }
      else if (['bio_lifecycle_schedule_incubation_for_current_agent','bio_lifecycle_mark_current_agent_detected',
        'bio_lifecycle_record_internal_deliberate_use','brilliant_scientist_krg_record_confirmed_offensive_biological_use',
        'air_cleanliness_treaty_on_unconventional_use'].includes(k)) this.boundary(k);
      else if (k === 'condemnation_add_source') { this.boundary(k); this.condemnations.push(String(this.value('condemnation_base_gain')/S)); }
      else if (k === 'fallout_request_aftermath') { this.boundary(k); this.fallout.push({actor:this.targets.get('fallout_request_actor_input').id,
        source:String(this.value('fallout_request_source_input')/S),intensity:String(this.value('fallout_request_intensity_input')/S)}); }
      else if (k === 'news_event') this.news.push(this.field(v,'id'));
      else if (k === 'add_war_support') this.boundary(k);
      else if (!super.eval([node])) return false;
    }
    return true;
  }
}
const results = [];
function check(id, test) { test(); results.push({id,passed:true}); }
check('byte-exact-archives-and-current-executed-definitions',()=>{
  for(const side of ['before','after'])for(const item of JSON.parse(fs.readFileSync(path.join(archive,side+'_manifest.json'),'utf8'))){
    const bytes=fs.readFileSync(path.join(archive,side,item.path));assert.equal(bytes.length,item.bytes);
    assert.equal(crypto.createHash('sha256').update(bytes).digest('hex'),item.sha256);
    if(side==='after' && [effectFile,bridgeFile,'docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js'].includes(item.path))
      assert.equal(normalizedText(bytes),normalizedText(fs.readFileSync(path.join(root,item.path))),'current owned source differs: '+item.path);
  }
  for(const f of ['common/scripted_effects/biological_lifecycle_effects.txt','common/scripted_triggers/biological_lifecycle_triggers.txt']){
    const current=new Map(parse(fs.readFileSync(path.join(root,f),'utf8')).map(x=>[x.key,x.value]));
    for(const name of testedLifecycle.map(x=>'bio_lifecycle_'+x))if(current.has(name))assert.deepEqual(current.get(name),bodies.get(name),'executed dependency changed: '+name);
  }
});
function world(options = {}, count = 1) {
  const vm = new DoomsdayVM(options);
  for (let i=0;i<count;i++) vm.addState('D'+i);
  if (count) { vm.targets.set('bio_doomsday_raid_target',vm.states[0]); vm.targets.set('bio_doomsday_raid_actor',vm.actor); }
  return vm;
}
function outer(vm) {
  vm.eval(parse('set_temp_variable = { bio_doomsday_release_status = 0 } set_temp_variable = { bio_doomsday_full_resolution_status = 0 }'));
  vm.run('bio_doomsday_resolve_release'); return vm;
}
const n = (vm,name) => Number(vm.value(name)/S);
const bridgeBody = side => {
  const event = parse(read(side,bridgeFile)).find(x => x.key === 'country_event' && x.value.some(x => x.key === 'id' && x.value === 'chaosx_cbrn_doom_raid.2'));
  return event.value.find(x => x.key === 'immediate').value;
};
check('unchanged-original-command-subsequence', () => {
  const before = parse(read('before',effectFile)), after = parse(read('after',effectFile));
  function subsequence(a,b) {
    let j=0; for (const x of a) {
      while(j<b.length && (b[j].key!==x.key || b[j].op!==x.op || Array.isArray(b[j].value)!==Array.isArray(x.value) ||
        (Array.isArray(x.value) ? !subsequence(x.value,b[j].value) : b[j].value!==x.value))) j++;
      if(j===b.length)return false; j++;
    } return true;
  }
  assert(subsequence(before,after),'original command or order changed');
  assert(!read('after',effectFile).includes('set_temp_variable = { bio_active_agent'));
});
check('empty-eligible-targets-no-commit-no-debit',()=>{
  const vm=outer(world({},0)); assert.equal(n(vm,'bio_doomsday_release_status'),0); assert.equal(n(vm,'bio_doomsday_full_resolution_status'),0);
  assert.equal(vm.debits.length,0); assert(!vm.actor.flags.has('bio_doomsday_raid_committed')); assert.equal(vm.fallout.length,0);
});
for (const count of [1,3,8]) check(`eligible-${count}-states-four-stocks-exact-receipts`,()=>{
  const vm=outer(world({stocks:[5,4,2,0]},count));
  assert.equal(n(vm,'bio_doomsday_release_status'),1); assert.equal(n(vm,'bio_doomsday_full_resolution_status'),1);
  assert.equal(vm.seeded.reduce((a,b)=>a+b.payload,0),15); assert.deepEqual(vm.debits.map(x=>x.amount),['-5','-4','-2','0']);
  for (const [agent,total] of [[1,6],[2,5],[3,3],[4,1]]) assert.equal(vm.seeded.filter(x=>x.agent===agent).reduce((a,b)=>a+b.payload,0),total);
  assert.equal(vm.actor.vars.get('bio_doomsday_payload_consumed_total'),ticks(15));
  assert.equal(vm.condemnations.length,1); assert.equal(vm.condemnations[0],'300'); assert.equal(vm.fallout.length,1);
  assert.equal(vm.actor.vars.get('bio_deliberate_use_count'),ticks(1));
  assert(!vm.vars.has('bio_doomsday_stock_anthrax')); assert(!vm.tempArrays.has('bio_doomsday_target_states'));
});
check('collector-domestic-first-unique-front-excludes-neutral-wasteland-zombie',()=>{
  const vm=world({},2), front=vm.addState('F',vm.enemy), neutral=vm.addState('N',vm.neutral), wasteland=vm.addState('W',vm.actor,{category:'wasteland'}), zombie=vm.addState('Z',vm.actor,{zombie:true});
  vm.states[0].neighbors=[front,neutral,wasteland,zombie];vm.states[1].neighbors=[front];
  vm.targets.set('bio_doomsday_actor',vm.actor);vm.eval(parse('clear_temp_array = bio_doomsday_target_states set_temp_variable = { bio_doomsday_target_count = 0 }'));
  vm.run('bio_doomsday_collect_target_states');assert.deepEqual(vm.array('bio_doomsday_target_states').map(x=>x.id),['D0','D1','F']);assert.equal(n(vm,'bio_doomsday_target_count'),3);
});
check('all-zero-remaining-stocks-four-native-reserved-lots',()=>{
  const vm=outer(world({},4));assert.equal(vm.seeded.reduce((a,b)=>a+b.payload,0),4);assert.deepEqual(vm.debits.map(x=>x.amount),['0','0','0','0']);assert.equal(n(vm,'bio_doomsday_full_resolution_status'),1);
});
check('mixed-accepted-rejected-seeds-exact-partial-receipt',()=>{
  const vm=world({stocks:[1,1,1,1]},2);vm.states[1].reject=true;outer(vm);
  assert.equal(vm.seeded.reduce((a,b)=>a+b.payload,0),4);assert.equal(n(vm,'bio_doomsday_release_status'),1);assert.equal(n(vm,'bio_doomsday_full_resolution_status'),0);
  assert(vm.actor.flags.has('bio_doomsday_partial_resolution_history'));assert.equal(vm.fallout.length,1);assert(!vm.states[1].flags.has('bio_doomsday_release_target_history'));
});
check('all-rejected-seeds-reset-stale-positive-dispatch-receipt',()=>{
  const vm=world({stocks:[1,1,1,1]},2);for(const state of vm.states)state.reject=true;vm.set('bio_seed_dispatch_status',1);vm.set('bio_active_agent',3);outer(vm);
  assert.equal(vm.seeded.length,0);assert.equal(n(vm,'bio_doomsday_release_status'),0);assert.equal(n(vm,'bio_doomsday_full_resolution_status'),0);
  assert.equal(n(vm,'bio_seed_dispatch_status'),0);assert.equal(n(vm,'bio_active_agent'),3);assert.equal(vm.fallout.length,0);assert.equal(vm.condemnations.length,0);
});
check('existing-commit-prevents-repeat-debit-consequence-and-seed',()=>{
  const vm=outer(world({stocks:[4,4,4,4]},2));const first=[vm.debits.length,vm.seeded.length,vm.condemnations.length,vm.fallout.length];outer(vm);
  assert.deepEqual([vm.debits.length,vm.seeded.length,vm.condemnations.length,vm.fallout.length],first);
  assert.equal(n(vm,'bio_doomsday_release_status'),0);assert.equal(n(vm,'bio_doomsday_full_resolution_status'),0);
});
for(const options of [{policy:false},{capitulated:true},{surrender:0,chaos:0}])check(`final-gate-${Object.keys(options)[0]}-rejects`,()=>{
  const vm=outer(world(options,1));assert.equal(vm.debits.length,0);assert.equal(vm.seeded.length,0);assert.equal(n(vm,'bio_doomsday_release_status'),0);
});
check('stale-outer-and-private-break-one-reset-complete-traversal-repeat',()=>{
  const vm=world({stocks:[5,5,5,5]},3);vm.set('break',1);vm.set('bio_doomsday_dispatch_break',1);outer(vm);
  assert.equal(vm.seeded.length,12);assert.equal(n(vm,'break'),1);assert.equal(n(vm,'bio_doomsday_dispatch_break'),0);
  vm.actor.flags.delete('bio_doomsday_raid_committed');vm.set('bio_doomsday_dispatch_break',1);outer(vm);assert.equal(vm.seeded.length,16);
});
check('stale-reset-only-inputs-clear-before-actual-route-finalize-dispatch',()=>{
  const vm=world({},1);for(const key of ['concealment','intensity_override','exposed_share_override','evidence_override','condemnation_override'])vm.set('bio_seed_'+key,99);
  vm.set('bio_seed_weaponization_mult',9);outer(vm);assert.equal(vm.seeded.length,4);
  for(const seed of vm.seeded){assert.equal(seed.concealment,'0');assert.equal(seed.weaponization,String(S));}
  assert.equal(n(vm,'bio_seed_intensity_override'),0);assert.equal(n(vm,'bio_seed_condemnation_override'),0);
});
for(const [doctrine,gain] of [['cbrn_theater_contamination_doctrine_spirit','300'],['cbrn_terminal_hazard_doctrine_spirit','200']])check('actual-doctrine-multiplier-return-'+doctrine,()=>{
  const vm=outer(world({doctrine},1));assert.deepEqual(vm.condemnations,[gain]);assert.equal(vm.actor.vars.get('bio_deliberate_use_count'),ticks(1));
});
check('actual-bridge-owned-release-receipt-publishes-one-news',()=>{
  const vm=world({},1);vm.eval(bridgeBody('after'));assert.deepEqual(vm.news,['chaosx_cbw_doom.2']);assert.equal(n(vm,'bio_doomsday_release_status'),1);
  assert(!vm.vars.has('bio_doomsday_full_resolution_status'),'unused resolver output must stay local to its frame');
});
check('actual-bridge-rejection-clears-stale-release-receipt-no-news',()=>{
  const vm=world({committed:true},1);vm.set('bio_doomsday_release_status',1);vm.eval(bridgeBody('after'));assert.equal(vm.news.length,0);assert.equal(n(vm,'bio_doomsday_release_status'),0);
});
// Frozen before-source regressions establish that fixtures do not repair source.
check('before-source-loses-collected-targets-and-never-commits',()=>{
  for(const node of parse(read('before',effectFile)))definitions.set(node.key,node.value);
  try { const vm=outer(world({checkContracts:false},1));assert.equal(vm.debits.length,0);assert.equal(n(vm,'bio_doomsday_release_status'),0); }
  finally { for(const [name,body]of savedDoomsday)definitions.set(name,body); }
});
check('before-bridge-loses-release-receipt-despite-patched-resolver',()=>{
  const vm=world({},1);vm.eval(bridgeBody('before'));assert.equal(vm.seeded.length,4);assert.equal(vm.news.length,0);assert(!vm.vars.has('bio_doomsday_release_status'));
});
check('capture-helper-returns-exact-four-stock-outputs-only-with-caller-storage',()=>{
  const vm=world({stocks:[7,0,4,2]},1);
  vm.eval(parse(contracts.bio_doomsday_capture_and_consume_arsenal.vars.map(x=>`set_temp_variable = { ${x} = 0 }`).join('\n')));
  vm.run('bio_doomsday_capture_and_consume_arsenal');
  assert.deepEqual(contracts.bio_doomsday_capture_and_consume_arsenal.vars.map(x=>n(vm,x)),[8,1,5,3,17]);
  assert.deepEqual(vm.debits.map(x=>x.amount),['-7','0','-4','-2']);assert([...vm.stock.values()].every(x=>x===0n));
  const unowned=world({stocks:[7,0,4,2],checkContracts:false},1);unowned.run('bio_doomsday_capture_and_consume_arsenal');
  for(const key of contracts.bio_doomsday_capture_and_consume_arsenal.vars)assert(!unowned.vars.has(key));
  assert.equal(unowned.debits.length,4,'native-model debit is separate from temporary return values');
});
function directDispatch(vm) {
  vm.targets.set('bio_doomsday_actor',vm.actor);vm.tempArrays.set('bio_doomsday_target_states',vm.states.slice());
  vm.eval(parse('set_temp_variable = { bio_doomsday_active_agent = 1 } set_temp_variable = { bio_doomsday_active_stock = 2 }\n'+
    'set_temp_variable = { bio_doomsday_seeded_payload_total = 0 } set_temp_variable = { bio_doomsday_seeded_state_agent_count = 0 }'));
  vm.run('bio_doomsday_dispatch_current_agent');return vm;
}
check('dispatch-status-is-result-receipt-and-does-not-block-a-fresh-accepted-seed',()=>{
  const vm=world({},2);vm.set('bio_seed_dispatch_status',1);directDispatch(vm);
  assert.equal(vm.seeded.length,2);assert.equal(n(vm,'bio_doomsday_seeded_payload_total'),2);
  directDispatch(vm);assert.equal(vm.seeded.length,4);assert.equal(n(vm,'bio_doomsday_seeded_payload_total'),2);
});
check('before-dispatch-loses-positive-receipt-and-fails-to-mark-accepted-seeds',()=>{
  const name='bio_doomsday_dispatch_current_agent', before=parse(read('before',effectFile)).find(x=>x.key===name).value;
  definitions.set(name,before);
  try {const vm=world({checkContracts:false},2);vm.set('bio_seed_weaponization_mult',1);directDispatch(vm);assert.equal(vm.seeded.length,2);assert.equal(n(vm,'bio_doomsday_seeded_payload_total'),0);
    for(const state of vm.states)assert(!state.flags.has('bio_doomsday_release_target_history'));
  }finally{definitions.set(name,savedDoomsday.get(name));}
});
check('before-default-break-inherits-true-stale-outer-break',()=>{
  const name='bio_doomsday_dispatch_current_agent', before=parse(read('before',effectFile)).find(x=>x.key===name).value;
  definitions.set(name,before);
  try {const vm=world({checkContracts:false},2);vm.set('break',1);directDispatch(vm);assert.equal(vm.seeded.length,0);assert.equal(n(vm,'break'),1);}
  finally{definitions.set(name,savedDoomsday.get(name));}
});
check('doctrine-output-caller-lifetime-and-original-300-times-multiplier-floor',()=>{
  const vm=world({doctrine:'cbrn_terminal_hazard_doctrine_spirit'},1);vm.targets.set('bio_seed_actor',vm.actor);
  vm.eval(parse('set_temp_variable = { bio_seed_actor_proof = 1 } set_temp_variable = { bio_seed_doctrine_condemnation_mult = 1 }'));
  vm.run('bio_lifecycle_prepare_actor_doctrine_snapshot');assert.equal(vm.value('bio_seed_doctrine_condemnation_mult'),ticks('0.55'));
  const unowned=world({doctrine:'cbrn_terminal_hazard_doctrine_spirit',checkContracts:false},1);unowned.targets.set('bio_seed_actor',unowned.actor);
  unowned.set('bio_seed_actor_proof',1);unowned.run('bio_lifecycle_prepare_actor_doctrine_snapshot');assert(!unowned.vars.has('bio_seed_doctrine_condemnation_mult'));
});
check('before-batch-missing-doctrine-owner-falls-to-floor-on-ordinary-profile',()=>{
  const name='bio_doomsday_register_batch_consequence', before=parse(read('before',effectFile)).find(x=>x.key===name).value;
  definitions.set(name,before);
  try {const vm=outer(world({checkContracts:false},1));assert.deepEqual(vm.condemnations,['200']);}
  finally{definitions.set(name,savedDoomsday.get(name));}
});
const summary={passed:results.length,failed:0,results,lifetimeModel:'BaseVM.run unchanged; all scripted calls discard newly created temporaries, retain caller-preinitialized names, and scoped regular maps stay separate',
  nativeModel:'Exact fixture stock counts; modeled negative equipment debit and reserved-lot accounting. No engine execution claim.',
  actualSourceCoverage:[...savedDoomsday.keys(),...testedLifecycle.map(x=>'bio_lifecycle_'+x),'chaosx_cbrn_doom_raid.2 immediate'],
  boundaries:['native equipment stock reads/debits','stockpile safety recapture','lifecycle persistent slot storage and scheduling','retaliation classification',
    'historical advisor absent','designer absent','policy predicates supplied as explicit fixture booleans','condemnation submission','Fallout coordinator','science/treaty callbacks','native news publication'],
  unsupportedUnusedConstants:unsupportedConstants,
  inputHashes:Object.fromEntries(inputFiles.map(f=>[f,crypto.createHash('sha256').update(fs.readFileSync(path.join(archive,'after',f))).digest('hex')])),
  currentFullFileHashes:Object.fromEntries(inputFiles.map(f=>[f,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,f))).digest('hex')])),
  limits:['No native preparation/reserved lots observed in engine','No real lifecycle persistence, incubation, detection, tick or Fallout execution',
    'No RNG executed or changed','No foreach ceiling assumed; tested small explicit scope pools','Parent owns event inspect/render/compare and final integration review']};
fs.writeFileSync(path.join(root,'docs/testing/2026-10-08_bio_doomsday_lifetime_source_tests.result.json'),JSON.stringify(summary,null,2)+'\n');
console.log(JSON.stringify({passed:summary.passed,failed:summary.failed,results},null,2));
