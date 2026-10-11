// Execute real owner selectors, outcomes, exact quotation, payment, allocator,
// typed receipts, settlement, refunds and achievement proof/family accounting.
// Native primitives and the out-of-scope sanctions publication are modeled.
// Every scripted return conservatively drops newly created temporary storage.
const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict'), crypto = require('node:crypto');
const core = require('./exact_quote_source_tests.js');
const {VM, S, MAX, ticks, parse, root, definitions, constants, helperOutputs} = core;
const sources = new Map(core.sources), loc = new Map(), texts = new Map();
function load(p) {
  const raw = fs.readFileSync(path.join(root, p), 'utf8'); sources.set(p, raw);
  if (p.endsWith('.yml')) {
    for (const m of raw.matchAll(/^([^\s:#][^:]*):\s*"(.*)"\s*$/gm)) loc.set(m[1], m[2]);
    return;
  }
	const macros = new Map([...raw.matchAll(/^(@\w+)\s*=\s*(-?\d+(?:\.\d+)?)/gm)].map(m => [m[1], m[2]]));
	// The shared arithmetic parser intentionally omits complex schema atom lists.
	// Read numeric data from the real file, excluding only non-executable schema.
	let input = raw;
	if (p.includes('/script_constants/')) {
		input = raw.replace(/#[^\r\n]*/g, '');
		for (;;) {
			const m = /schema\s*=\s*\{/.exec(input); if (!m) break;
			let j = m.index + m[0].length, depth = 1;
			for (; j < input.length && depth; j++) { if (input[j] === '{') depth++; if (input[j] === '}') depth--; }
			assert.equal(depth, 0); input = input.slice(0, m.index) + input.slice(j);
		}
	}
	let ast;
	try { ast = parse(input.replace(/@\w+/g, token => macros.get(token) ?? token)); }
	catch (error) { throw new Error(`loading ${p}: ${error.message}`, {cause:error}); }
  if (p.includes('/script_constants/')) {
    function descend(nodes, prefix) {
      for (const n of nodes) {
        if (n.key === 'schema') continue;
        const name = prefix ? `${prefix}.${n.key}` : n.key;
        if (Array.isArray(n.value)) descend(n.value, name);
        else if (/^-?\d+(\.\d+)?$/.test(n.value)) constants.set(`constant:${name}`, ticks(n.value));
      }
    }
    descend(ast, '');
  } else if (p.includes('/scripted_localisation/')) {
    for (const n of ast) if (n.key === 'defined_text') texts.set(n.value.find(x => x.key === 'name').value, n.value.filter(x => x.key === 'text').map(x => x.value));
  } else for (const n of ast) if (Array.isArray(n.value)) definitions.set(n.key, n.value);
}
for (const p of ['cbrn_system_constants.txt','cbrn_occupation_constants.txt','cbrn_occupation_coverup_cost_constants.txt','cbrn_diplomacy_constants.txt','condemnation_sanctions_constants.txt','026_black_friday_constants.txt','chemical_warfare_constants.txt']) load(`common/script_constants/${p}`);
load('common/script_constants/cbrn_chemical_delivery_constants.txt');
for (const p of [
  'common/scripted_triggers/chaosx_universal_cost_triggers.txt',
  'common/scripted_triggers/condemnation_sanctions_triggers.txt',
  'common/scripted_triggers/cbrn_occupation_triggers.txt',
  'common/scripted_triggers/cbrn_occupation_coverup_cost_triggers.txt',
  'common/scripted_triggers/026_black_friday_triggers.txt',
  'common/scripted_effects/026_black_friday_effects.txt',
  'common/scripted_effects/cbrn_occupation_effects.txt',
  'common/scripted_effects/cbrn_occupation_coverup_cost_effects.txt',
  'common/scripted_effects/cbrn_exposure_effects.txt',
  'common/scripted_effects/cbrn_doctrine_effects.txt',
  'common/scripted_localisation/cbrn_occupation_value_localisation.txt',
  'localisation/english/cbrn_occupation_l_english.yml',
  'localisation/english/026_black_friday_l_english.yml',
]) load(p);
// Audit only outputs the actual owner consumes, never preseed internal scratch.
helperOutputs.universal_cost_quote_exact = {vars: ['universal_cost_quote_final_cost', 'universal_cost_quote_valid', 'universal_cost_quote_primary_source_id'], arrays: []};
const quoteOut = ['cbrn_occupation_coverup_pp_quote', 'cbrn_occupation_coverup_pp_ordinary', 'cbrn_occupation_coverup_pp_quote_valid', 'cbrn_occupation_coverup_pp_source_id'];
for (const n of ['cbrn_occupation_prepare_seal_state_pp_quote', 'cbrn_occupation_prepare_destroy_records_pp_quote', 'cbrn_occupation_can_pay_seal_state_pp', 'cbrn_occupation_can_pay_destroy_records_pp']) helperOutputs[n] = {vars: quoteOut, arrays: []};
for (const [n, vars] of Object.entries({
  universal_cost_pay_component: ['universal_cost_payment_result'],
  universal_cost_credit_component: ['universal_cost_credit_result'],
  universal_cost_record_transaction: ['universal_cost_record_transaction_result', 'universal_cost_recorded_component_index'],
  universal_cost_find_transaction_row: ['universal_cost_transaction_found_index', 'universal_cost_transaction_is_indexed', 'universal_cost_transaction_lookup_result', 'universal_cost_transaction_pointer'],
  universal_cost_find_component_row: ['universal_cost_component_found_index', 'universal_cost_component_lookup_result'],
  universal_cost_settle_transaction: ['universal_cost_settle_transaction_result'],
  universal_cost_refund_transaction: ['universal_cost_refund_transaction_result', 'universal_cost_refund_total', 'universal_cost_refund_unhandled_total'],
  universal_cost_validate_component_chain: ['universal_cost_chain_valid'],
  universal_cost_refund_component_at_cursor: ['universal_cost_refund_total', 'universal_cost_refund_unhandled_total', 'universal_cost_refund_all_complete'],
  black_friday_allocate_owner_transaction: ['black_friday_owner_transaction_id'],
  cbrn_occupation_apply_requested_coverup_action: ['cbrn_occupation_coverup_proof'],
  cbrn_occupation_apply_coverup_seal: ['cbrn_occupation_coverup_proof'],
  cbrn_occupation_apply_coverup_destroy_records: ['cbrn_occupation_coverup_proof'],
  cbrn_occupation_suppress_exact_chemical_record_evidence: ['cbrn_occupation_exact_record_suppression_proof'],
  cbrn_occupation_select_exact_chemical_record: ['cbrn_diplomacy_selected_chemical_row'],
  cbrn_occupation_coverup_can_retry_refund: ['cbrn_occupation_coverup_target', 'cbrn_occupation_coverup_receipt_id'],
  cbrn_set_doctrine_condemnation_mult_from_country: ['cbrn_action_doctrine_condemnation_mult'],
  black_friday_scan_receipt_political_power_only: ['black_friday_purchase_receipt_proof_valid', 'black_friday_purchase_has_non_political_paid_component'],
  black_friday_validate_ordinary_receipt_proof: ['black_friday_purchase_receipt_proof_valid', 'black_friday_purchase_has_non_political_paid_component'],
})) helperOutputs[n] = {vars, arrays: []};
const C = name => constants.get(`constant:${name}`);
const all = [];
class CoverupVM extends VM {
  constructor() {
    super(); this.country = {id: 7n*S, type: 'country', tag: 'GER', vars: this.regularVars, arrays: this.arrays, flags: new Set(), pp: ticks(1000), modifiers: new Map()};
    this.global = {vars: new Map(), arrays: new Map()}; this.scopes = new Map([[7n*S, this.country]]);
    this.current = this.country; this.previous = []; this.target = null; this.nativeWrites = []; this.calls = new Map(); this.fault = null; this.ai = false; this.debug = false; this.special = false;
    all.push(this);
  }
  state(id = 64, uid = 101) {
    const state = {id: ticks(id), type: 'state', vars: new Map(), arrays: new Map(), flags: new Set(), modifiers: new Map(), controller: this.country.id, resistance: 0n};
    this.scopes.set(state.id, state); this.target = state;
    state.vars.set('cbrn_occupation_responsible_country', this.country.id);
    state.vars.set('cbrn_occupation_last_action_date', S);
    state.vars.set('cbrn_occupation_last_action_route', C('cbrn_delivery_route.nerve_suppression'));
    state.vars.set('cbrn_occupation_last_record_uid', ticks(uid));
    state.vars.set('cbrn_evidence_quality', ticks(80));
    for (const [n, a] of [['uid', [ticks(uid)]], ['evidence', [ticks(80)]], ['status', [C('cbrn_chemical_record_status.open')]]]) state.arrays.set(`cbrn_chemical_record_${n}_entries`, a);
    state.vars.set('cbrn_chemical_open_forensic_record_count', S); return state;
  }
  enter(scope, nodes) {
    assert(scope, 'missing native scope'); const before = this.current;
    this.previous.push(before); this.current = scope; this.regularVars = scope.vars; this.arrays = scope.arrays;
    try { return this.eval(nodes); } finally { this.current = before; this.regularVars = before.vars; this.arrays = before.arrays; this.previous.pop(); }
  }
  pointer(token) { return token === 'ROOT' ? this.country : token === 'FROM' ? this.target : token === 'PREV' ? this.previous.at(-1) : token === 'THIS' ? this.current : this.scopes.get(this.value(token.replace(/^var:/, ''))); }
  array(name) { return name.startsWith('global.') ? this.global.arrays.get(name) ?? [] : super.array(name); }
  value(token) {
    if (['THIS','ROOT','FROM','PREV'].includes(token)) return this.pointer(token)?.id ?? 0n;
    if (token.startsWith('global.') && !token.includes('^')) return this.global.vars.get(token) ?? 0n;
    const scoped = token.match(/^(ROOT|FROM|PREV)\.(.+)$/);
    if (scoped) return this.pointer(scoped[1])?.vars.get(this.key(scoped[2])) ?? 0n;
    return super.value(token);
  }
  write(name, value, temporary = true) {
    if (name.startsWith('global.') && !name.includes('^')) { assert(value <= MAX && value >= -MAX); this.global.vars.set(name, value); return; }
    return super.write(name, value, temporary);
  }
  run(name, ...args) {
    this.calls.set(name, (this.calls.get(name) ?? 0) + 1);
    // Faults alter persistent fixture inputs before the REAL shared helper runs.
    // They never replace receipt, refund, settlement or action proof bodies.
    if (this.fault === 'record' && name === 'universal_cost_record_transaction') {
      this.regularVars.delete(this.key('universal_cost_allocated_transaction_id_@var:universal_cost_transaction_id')); this.fault = null;
    }
    if ((this.fault === 'refund' && name === 'universal_cost_refund_transaction' || this.fault === 'settle' && name === 'universal_cost_settle_transaction') && (this.faultTransaction === undefined || this.value('universal_cost_transaction_id') === this.faultTransaction)) {
      this.regularVars.set(this.key('universal_cost_transaction_row_plus_one_@var:universal_cost_transaction_id'), ticks(999)); this.fault = null;
    }
    return super.run(name, ...args);
  }
  eval(nodes) {
    for (let i=0; i<nodes.length; i++) {
      const n=nodes[i], k=n.key, v=n.value;
      if (['ROOT','FROM','PREV','THIS'].includes(k) || k.startsWith('var:')) { if (!this.enter(this.pointer(k), v)) return false; }
      else if (k === 'exists') { if ((this.current.type === 'country') !== (v === 'yes')) return false; }
      else if (k === 'tag') { if (this.current.id !== this.pointer(v)?.id) return false; }
      else if (k === 'is_controlled_by') { if (this.current.controller !== this.pointer(v)?.id) return false; }
      else if (k === 'is_ai' || k === 'is_debug' || k === 'is_special_chaos_country') {
        const val = k === 'is_ai' ? this.ai : k === 'is_debug' ? this.debug : this.special; if (val !== (v === 'yes')) return false;
      } else if (k === 'has_country_flag' || k === 'has_state_flag') { if (!this.current.flags.has(v)) return false; }
      else if (k === 'set_country_flag' || k === 'set_state_flag') {
        const flag = Array.isArray(v) ? this.field(v, 'flag') : v;
        const days = Array.isArray(v) ? this.value(this.field(v, 'days').replace(/^var:/,'')) : 0n;
        this.current.flags.add(flag); this.nativeWrites.push({effect:k,scope:String(this.current.id/S),flag,days:String(days/S)});
      } else if (k === 'clr_country_flag' || k === 'clr_state_flag') this.current.flags.delete(v);
      else if (k === 'has_political_power' || k === 'political_power') {
        const lhs=this.current.pp, rhs=this.value(v); if (!(n.op === '<' ? lhs < rhs : n.op === '>' ? lhs > rhs : lhs === rhs)) return false;
      } else if (k === 'add_political_power') {
        const delta=this.value(v); this.current.pp+=delta; this.nativeWrites.push({effect:k,scope:String(this.current.id/S),delta:String(delta)});
      } else if (k === 'add_resistance') { this.current.resistance += this.value(v); this.nativeWrites.push({effect:k,delta:String(this.value(v)),scope:String(this.current.id/S)}); }
      else if (k === 'add_dynamic_modifier') { this.current.modifiers.set(this.field(v,'modifier'), this.value(this.field(v,'days'))); }
      else if (k === 'force_update_dynamic_modifier') { /* native refresh only */ }
      else if (k === 'condemnation_add_source') {
        // Out-of-scope downstream sanction publication. Capture actual supplied
        // non-cost inputs after real owner/context/doctrine helper execution.
        this.nativeWrites.push({effect:k,base:String(this.value('condemnation_base_gain')),scope:String(this.current.id/S)});
      } else if (k === 'remove_from_array' && this.field(v,'value') !== undefined) {
        // Documented native value removal, distinct from index/front popping.
        const a=this.array(this.field(v,'array')), index=a.indexOf(this.value(this.field(v,'value')));
        if(index>=0)a.splice(index,1);
      } else if (k === 'for_each_loop') {
        const snapshot=[...this.array(this.field(v,'array'))], value=this.field(v,'value','v'), index=this.field(v,'index','i');
        const body=v.filter(x=>!['array','value','index','break'].includes(x.key));
        for(let j=0;j<Math.min(snapshot.length,1000);j++){this.write(value,snapshot[j]);this.write(index,BigInt(j)*S);if(!this.eval(body))return false;}
        assert.deepEqual(this.array(this.field(v,'array')),snapshot,'live iterator array mutated');
      } else if (['clamp_variable','clamp_temp_variable'].includes(k)) {
        const name=this.field(v,'var'), low=this.value(this.field(v,'min')), high=this.value(this.field(v,'max')), a=this.value(name);
        this.write(name,a<low?low:a>high?high:a,k==='clamp_temp_variable');
      } else if (['add_to_variable','subtract_from_variable','multiply_variable','divide_variable','multiply_temp_variable','divide_temp_variable'].includes(k)) {
        const name=this.field(v,'var',v[0].key), b=this.value(this.field(v,'value',v[0].value)), a=this.value(name);
        const result=k.startsWith('add_')?a+b:k.startsWith('subtract_')?a-b:k.startsWith('multiply_')?a*b/S:a*S/b;
        this.write(name,result,k.includes('temp_'));
      } else if (k==='is_in_array' && this.field(v,'array')===undefined) { if(!this.array(v[0].key).includes(this.value(v[0].value)))return false; }
      else {
        const group=[n]; if(k==='if')while(nodes[i+1]&&['else_if','else'].includes(nodes[i+1].key))group.push(nodes[++i]);
        if(!super.eval(group))return false;
      }
    } return true;
  }
  render(name) {
    const inherited=new Set(this.vars.keys()), arrays=new Set(this.tempArrays.keys());
    try {
      assert(texts.has(name),`unknown getter ${name}`);
      for(const text of texts.get(name)) {
        if(!this.eval(this.field(text,'trigger',[])))continue;
        const key=this.field(text,'localization_key'); assert(loc.has(key),`missing loc ${key}`);
        return this.renderText(loc.get(key));
      } throw Error(`no selected text ${name}`);
    } finally {
      for(const k of this.vars.keys())if(!inherited.has(k))this.vars.delete(k);
      for(const k of this.tempArrays.keys())if(!arrays.has(k))this.tempArrays.delete(k);
    }
  }
  renderText(text) {
    return text.replace(/\$([^$]+)\$/g,(_,key)=>{assert(loc.has(key));return this.renderText(loc.get(key));})
      .replace(/\[This\.(\w+)\]/g,(_,name)=>this.render(name))
      .replace(/\[\?([\w.]+)\|(0|5)\]/g,(_,name,precision)=>{
        const a=this.value(name), whole=a/S, frac=(a%S).toString().padStart(5,'0'); return precision==='0'?String(whole):`${whole}.${frac}`;
      });
  }
}
function fresh(score=0, rows=[]) {
  const v=new CoverupVM();v.state();v.write('condemnation_total',ticks(score),false);
  v.write('global.num_days',ticks(500),false);v.write('global.black_friday_sale_sequence',S,false);v.write('global.black_friday_discount_percent',ticks(50),false);
  for(const [suffix,key] of [['ids','id'],['ratios','ratio'],['priorities','priority'],['eligibility_masks','mask']])v.global.arrays.set(`global.universal_cost_source_${suffix}`,rows.map(r=>ticks(r[key])));
  if(rows.some(r=>r.id===26))v.flags.add('black_friday_active');v.flags.add('black_friday_natural_activation');
  v.write('black_friday_achievement_active_sale_sequence',S,false);v.write('black_friday_achievement_indexed_sale_sequence',S,false);return v;
}
const sale=(ratio=5000,id=26,priority=50,mask=0)=>({ratio,id,priority,mask});
function quote(v,action=1) {for(const n of quoteOut)v.set(n,0);assert(v.run(action===1?'cbrn_occupation_prepare_seal_state_pp_quote':'cbrn_occupation_prepare_destroy_records_pp_quote'));return v.value(quoteOut[0]);}
function click(v,action=1) {v.set('cbrn_occupation_coverup_payment_action',action);assert(v.run('cbrn_occupation_execute_paid_coverup'));}
function writes(v,effect){return v.nativeWrites.filter(w=>w.effect===effect);}
function pending(v){return v.country.arrays.get('cbrn_occupation_coverup_pending_receipts')??[];}
function phase(v,id=1){return v.country.vars.get(`cbrn_occupation_coverup_receipt_phase_@${id}`);}
function row(v,name,index=0){return v.country.arrays.get(`universal_cost_${name}`)?.[index];}
const results={scenarios:[],limitations:['native resources, scope resolution, timed flags and modifiers modeled','sanctions publication downstream of condemnation_add_source captured as out-of-scope','fixed-point native arithmetic modeled at 5 fractional places with signed truncation','no engine execution, GUI rendering, timer expiry, serialization or multiplayer proof'],hashes:{}};
function test(id,fn){fn();results.scenarios.push(id);}
for(const score of [0,500,1000,'500.12345','1.6665'])for(const action of [1,2])for(const ratio of [null,5000,2500])test(`price-gate-debit-${score}-${action}-${ratio??'ordinary'}`,()=>{
  const v=fresh(score,ratio===null?[]:[sale(ratio)]), base=action===1?40n:60n, ordinary=base*(ticks(score)+ticks(500))/500n;
  const expected=ratio===null?ordinary:((ordinary*BigInt(ratio)+10000n*S-1n)/(10000n*S))*S;
  assert.equal(quote(v,action),expected);assert.equal(v.value(quoteOut[1]),ordinary);assert.equal(v.value(quoteOut[2]),S);assert.equal(v.value(quoteOut[3]),ratio===null?0n:ticks(26));
  v.country.pp=expected-1n;assert.equal(v.run(action===1?'cbrn_occupation_can_pay_seal_state_pp':'cbrn_occupation_can_pay_destroy_records_pp'),false);
  v.country.pp=expected;assert(v.run(action===1?'cbrn_occupation_can_pay_seal_state_pp':'cbrn_occupation_can_pay_destroy_records_pp'));
  click(v,action);assert.equal(v.country.pp,0n);assert.equal(writes(v,'add_political_power').length,1);
  assert.equal(row(v,'transaction_states'),ticks(4));assert.equal(row(v,'component_actual_paid_costs'),expected);assert.equal(row(v,'component_ordinary_costs'),ordinary);
  assert.equal(row(v,'component_achievement_family_ids'),S);assert.equal(row(v,'transaction_achievement_primary_component_ids'),C('black_friday_event.owner_component_political_power'));
  assert.equal(row(v,'transaction_achievement_cost_bases'),C('universal_cost_achievement_basis.primary_component'));assert.equal(row(v,'component_achievement_primary_members'),S);
  assert.equal(v.target.vars.has('cbrn_occupation_requested_coverup_action'),false);assert.equal(phase(v),undefined);
  assert(v.target.flags.has(action===1?'cbrn_occupation_state_sealed':'cbrn_occupation_records_destroyed'));
  const nativeFlags=writes(v,'set_state_flag');assert.equal(nativeFlags.filter(w=>w.flag===(action===1?'cbrn_occupation_state_sealed':'cbrn_occupation_records_destroyed')).length,1);
  if(action===1){assert.equal(nativeFlags.find(w=>w.flag==='cbrn_occupation_state_seal_active').days,String(C('cbrn_occupation_timing.sealed_state_days')/S));assert.equal(v.target.modifiers.get('cbrn_occupation_state_sealed_modifier'),C('cbrn_occupation_timing.sealed_state_days'));}
  assert(writes(v,'condemnation_add_source')[0].base!=='0','preserve hidden non-cost liability');
  const paidWrites=writes(v,'add_political_power').length;click(v,action);assert.equal(writes(v,'add_political_power').length,paidWrites);
});
test('composable-source-primary-and-small-fraction',()=>{
  for(const rows of [[sale(5000),sale(2500,99,1)],[sale('0.00001',99,1)],[sale(10000,99,1)],[sale(5000,99,1,2)]]) {
    const v=fresh('500.12345',rows), p=quote(v);const o=core.oracle('80.00987','1',1,rows);assert.equal(p,o.price);assert.equal(v.value(quoteOut[3]),ticks(o.primary));
    click(v);assert.equal(row(v,'component_source_ids'),ticks(o.primary));assert.equal((v.country.arrays.get('black_friday_achievement_transaction_ids')??[]).length,0,'non-26 source must not claim BF');
  }
});
test('fresh-click-expiry-and-score-change',()=>{const v=fresh(0,[sale()]);assert.equal(quote(v),ticks(20));v.global.arrays.get('global.universal_cost_source_ids').length=0;for(const suffix of ['ratios','priorities','eligibility_masks'])v.global.arrays.get(`global.universal_cost_source_${suffix}`).length=0;v.flags.delete('black_friday_active');v.write('condemnation_total',ticks('500.12345'),false);click(v);assert.equal(row(v,'component_actual_paid_costs'),ticks('80.00987'));});
for(const defect of ['control','responsible','route','discovered','action','funds','malformed-sources'])test(`reject-before-payment-${defect}`,()=>{
  const v=fresh(0,[sale()]);if(defect==='control')v.target.controller=ticks(8);if(defect==='responsible')v.target.vars.set('cbrn_occupation_responsible_country',ticks(8));
  if(defect==='route')v.target.vars.set('cbrn_occupation_last_action_route',0n);if(defect==='discovered')v.target.flags.add('cbrn_occupation_discovery_recorded');
  if(defect==='funds')v.country.pp=ticks(19);if(defect==='malformed-sources')v.global.arrays.get('global.universal_cost_source_ratios').length=0;
  // Other responsible country is a real native scope, not a guessed record.
  v.scopes.set(ticks(8),{id:ticks(8),type:'country',tag:'ENG',vars:new Map(),arrays:new Map(),flags:new Set()});
  click(v,defect==='action'?4:1);assert.equal(writes(v,'add_political_power').length,0);assert.equal(writes(v,'set_state_flag').length,0);
});
for(const action of [1,2])test(`exact-missing-UID-refund-${action}`,()=>{
  const v=fresh(0,[sale()]);v.target.vars.set('cbrn_occupation_last_record_uid',ticks(999));click(v,action);
  assert.equal(v.country.pp,ticks(1000));assert.deepEqual(writes(v,'add_political_power').map(w=>w.delta),[String(ticks(action===1?-20:-30)),String(ticks(action===1?20:30))]);
  assert.equal(row(v,'transaction_states'),ticks(2));assert.equal(writes(v,'set_state_flag').length,0);assert.equal(v.target.arrays.get('cbrn_chemical_record_evidence_entries')[0],ticks(80));
  assert.equal(v.target.vars.has('cbrn_occupation_requested_coverup_action'),false);assert.equal((v.country.arrays.get('black_friday_achievement_transaction_ids')??[]).length,0);
  v.run('cbrn_occupation_recover_paid_coverups');assert.equal(writes(v,'add_political_power').length,2);assert.equal(pending(v).length,0);
});
test('real-record-rejection-direct-paid-refund',()=>{const v=fresh(0,[sale()]);v.fault='record';click(v);assert.equal(v.country.pp,ticks(1000));assert.equal(writes(v,'add_political_power').length,2);assert.equal(writes(v,'set_state_flag').length,0);assert.equal(phase(v),undefined);});
test('refund-rejection-persists-and-retries-on-click-without-new-debit',()=>{
  const v=fresh(0,[sale()]);v.target.vars.set('cbrn_occupation_last_record_uid',ticks(999));v.fault='refund';click(v);
  assert.equal(v.country.pp,ticks(980));assert.equal(phase(v),C('cbrn_occupation_coverup_receipt_phase.recorded_refund'));assert.equal(v.country.vars.get('cbrn_occupation_coverup_open_receipt_@64'),S);
  v.country.pp=0n;for(const key of quoteOut)v.set(key,0);assert(v.run('cbrn_occupation_can_pay_seal_state_pp'));assert(v.run('cbrn_occupation_can_pay_destroy_records_pp'));
  v.country.vars.set('universal_cost_transaction_row_plus_one_@1',S);click(v);assert.equal(v.country.pp,ticks(20));assert.equal(writes(v,'add_political_power').length,2);assert.equal(phase(v),undefined);assert.equal(pending(v).length,0);
});
test('applied-settlement-rejection-unlocks-state-and-owner-recovery-never-replays',()=>{
  const v=fresh(0,[sale()]);v.fault='settle';click(v);assert.equal(v.country.pp,ticks(980));assert.equal(phase(v),C('cbrn_occupation_coverup_receipt_phase.applied_settlement'));assert.equal(v.country.vars.has('cbrn_occupation_coverup_open_receipt_@64'),false);
  assert.deepEqual(v.country.arrays.get('cbrn_occupation_coverup_achievement_eligible_receipts'),[S]);
  assert.equal((v.country.arrays.get('black_friday_achievement_transaction_ids')??[]).length,0);v.country.vars.set('universal_cost_transaction_row_plus_one_@1',S);
  const stateWrites=writes(v,'set_state_flag').length;v.run('cbrn_occupation_recover_paid_coverups');assert.equal(row(v,'transaction_states'),ticks(4));assert.equal(phase(v),undefined);assert.equal(writes(v,'add_political_power').length,1);assert.equal(writes(v,'set_state_flag').length,stateWrites);
  assert.deepEqual(v.country.arrays.get('black_friday_achievement_transaction_family_ids'),[S]);v.run('cbrn_occupation_recover_paid_coverups');assert.equal(v.country.arrays.get('black_friday_achievement_transaction_ids').length,1);
  assert.deepEqual(v.country.arrays.get('cbrn_occupation_coverup_achievement_eligible_receipts'),[]);
});
test('applied-recovery-after-expiry-no-family-credit',()=>{const v=fresh(0,[sale()]);v.fault='settle';click(v);v.country.vars.set('universal_cost_transaction_row_plus_one_@1',S);v.flags.delete('black_friday_active');v.run('cbrn_occupation_recover_paid_coverups');assert.equal(phase(v),undefined);assert.equal((v.country.arrays.get('black_friday_achievement_transaction_ids')??[]).length,0);});
test('payer-and-state-target-receipts-do-not-overwrite',()=>{
  const v=fresh(0,[sale()]);v.target.vars.set('cbrn_occupation_last_record_uid',ticks(999));v.fault='refund';click(v);const firstTarget=v.target;
  v.state(65,102);click(v,2);assert.equal(v.country.pp,ticks(950));assert.equal(phase(v),C('cbrn_occupation_coverup_receipt_phase.recorded_refund'));assert.equal(row(v,'component_actual_paid_costs',1),ticks(30));
  assert.equal(v.country.vars.get('cbrn_occupation_coverup_receipt_target_@1'),ticks(64));assert.equal(v.country.vars.has('cbrn_occupation_coverup_open_receipt_@65'),false);
  const other=fresh(0,[sale()]);click(other);assert.equal(other.country.pp,ticks(980));assert.equal(other.country.vars.has('cbrn_occupation_coverup_open_receipt_@64'),false);
  v.country.vars.set('universal_cost_transaction_row_plus_one_@1',S);v.run('cbrn_occupation_recover_paid_coverups');assert.equal(v.country.pp,ticks(970));assert.equal(firstTarget.flags.size,0);
});
for(const getter of ['GetCbrnOccupationSealStatePpQuote','GetCbrnOccupationDestroyRecordsPpQuote','GetCbrnOccupationSealStateCostDetails','GetCbrnOccupationDestroyRecordsCostDetails'])for(const mode of ['ordinary','sale','invalid'])test(`parent-getter-${getter}-${mode}`,()=>{
  const v=fresh('500.12345',mode==='ordinary'?[]:[sale()]);if(mode==='invalid')v.global.arrays.get('global.universal_cost_source_ratios').length=0;
  const actual=v.render(getter), seal=getter.includes('SealState');
  if(mode==='invalid')assert(actual.includes('Price unavailable'));else {assert(actual.includes(mode==='ordinary'?(seal?'80.00987':'120.01481'):(seal?'41':'61')));assert.equal(actual.includes('Black Friday'),mode==='sale'&&getter.endsWith('CostDetails'));}
  for(const key of quoteOut)assert(!v.vars.has(key),'localisation newly created outputs expire after entire getter');
});
test('caller-output-loss-negative-control',()=>{const v=fresh(0,[sale()]);assert(v.run('cbrn_occupation_prepare_seal_state_pp_quote',true));for(const key of quoteOut)assert(!v.vars.has(key));});
test('1001-pending-native-loop-limit-retains-unvisited-suffix',()=>{
  const v=fresh();v.country.pp=0n;const ids=Array.from({length:1001},(_,i)=>ticks(i+1));v.country.arrays.set('cbrn_occupation_coverup_pending_receipts',[...ids]);
  // Persistent unpaid-ledger owner proof is an explicit fixture input. The real
  // credit API handles all 1001 entries and the native while loop stops at 1000.
  for(let id=1;id<=1001;id++) {
    v.country.vars.set(`cbrn_occupation_coverup_receipt_phase_@${id}`,C('cbrn_occupation_coverup_receipt_phase.unrecorded_refund'));
    v.country.vars.set(`cbrn_occupation_coverup_receipt_paid_@${id}`,S);
    v.country.vars.set(`cbrn_occupation_coverup_receipt_target_@${id}`,ticks(64));
  }
  v.run('cbrn_occupation_recover_paid_coverups');assert.equal(v.country.pp,ticks(1000));assert.deepEqual(pending(v),[ticks(1001)]);assert.equal(phase(v,1001),C('cbrn_occupation_coverup_receipt_phase.unrecorded_refund'));
  v.run('cbrn_occupation_recover_paid_coverups');assert.equal(v.country.pp,ticks(1001));assert.equal(pending(v).length,0);assert.equal(writes(v,'add_political_power').length,1001);
});
test('1001-rejected-recorded-refunds-rotate-without-ID-loss',()=>{
  const v=fresh();const ids=Array.from({length:1001},(_,i)=>ticks(i+1));v.country.arrays.set('cbrn_occupation_coverup_pending_receipts',[...ids]);
  // Missing shared rows deliberately reject/no-op through the actual lookup
  // and refund helpers. Owner proof must survive, not be guessed or credited.
  for(let id=1;id<=1001;id++) {
    v.country.vars.set(`cbrn_occupation_coverup_receipt_phase_@${id}`,C('cbrn_occupation_coverup_receipt_phase.recorded_refund'));
    v.country.vars.set(`cbrn_occupation_coverup_receipt_target_@${id}`,ticks(64));
    v.country.vars.set(`cbrn_occupation_coverup_receipt_paid_@${id}`,S);
  }
  v.run('cbrn_occupation_recover_paid_coverups');assert.deepEqual(pending(v),[ticks(1001),...ids.slice(0,1000)]);assert.equal(writes(v,'add_political_power').length,0);
  v.run('cbrn_occupation_recover_paid_coverups');assert.deepEqual(new Set(pending(v)),new Set(ids));assert.equal(pending(v).length,1001);assert.equal(writes(v,'add_political_power').length,0);
});
for(const getter of ['GetCbrnOccupationSealStatePpQuote','GetCbrnOccupationDestroyRecordsPpQuote','GetCbrnOccupationSealStateCostDetails','GetCbrnOccupationDestroyRecordsCostDetails'])test(`parent-pending-clear-normal-${getter}`,()=>{
  const v=fresh('500.12345',[sale()]);v.target.vars.set('cbrn_occupation_last_record_uid',ticks(999));v.fault='refund';click(v);v.country.pp=0n;
  const before=v.render(getter);if(getter.endsWith('CostDetails')){assert(before.includes('41.00000'));assert(before.includes('no new purchase'));}else assert.equal(before,'Payment recovery');
  for(const key of quoteOut)v.set(key,0);assert(v.run('cbrn_occupation_can_pay_seal_state_pp'));assert(v.run('cbrn_occupation_can_pay_destroy_records_pp'));
  v.country.vars.set('universal_cost_transaction_row_plus_one_@1',S);click(v);assert.equal(v.country.pp,ticks(41));assert.equal(writes(v,'add_political_power').length,2);
  const after=v.render(getter);assert(!after.includes('Payment recovery'));assert(!after.includes('no new purchase'));assert(after.includes(getter.includes('SealState')?'41':'61'));
  assert.equal(v.country.vars.has('cbrn_occupation_coverup_open_receipt_@64'),false);
});
for(const mode of ['ai','manual','forced','debug','expired'])test(`achievement-disqualifier-${mode}`,()=>{
  const v=fresh(0,[sale()]);if(mode==='ai')v.ai=true;if(mode==='debug')v.debug=true;if(mode==='manual')v.flags.add('black_friday_manual_disqualified');if(mode==='forced')v.flags.add('black_friday_force_disqualified');if(mode==='expired')v.flags.delete('black_friday_active');
  click(v);assert.equal(row(v,'transaction_states'),ticks(4));assert.equal((v.country.arrays.get('black_friday_achievement_transaction_ids')??[]).length,0);
});
test('ordinary-score-clamp-and-inclusive-display-colour',()=>{
  for(const [score,price] of [[-1,40],[1001,120]])assert.equal(quote(fresh(score)),ticks(price));
  for(const getter of ['GetCbrnOccupationSealStateCostDetails','GetCbrnOccupationDestroyRecordsCostDetails'])for(const delta of [-1n,0n,1n]) {
    const v=fresh('500.12345'), price=getter.includes('SealState')?ticks('80.00987'):ticks('120.01481');v.country.pp=price+delta;
    const text=v.render(getter);assert(text.includes(delta<0n?'§R':'§Y'));
  }
});
test('legacy-exact-UID-beyond-native-loop-limit-refunds-without-fallback',()=>{
  const v=fresh(0,[sale()]);v.target.vars.set('cbrn_occupation_last_record_uid',ticks(1001));
  v.target.arrays.set('cbrn_chemical_record_uid_entries',Array.from({length:1001},(_,i)=>ticks(i+1)));
  v.target.arrays.set('cbrn_chemical_record_evidence_entries',Array(1001).fill(ticks(80)));
  v.target.arrays.set('cbrn_chemical_record_status_entries',Array(1001).fill(C('cbrn_chemical_record_status.open')));
  click(v);assert.equal(v.country.pp,ticks(1000));assert.equal(row(v,'transaction_states'),ticks(2));assert.equal(writes(v,'set_state_flag').length,0);assert(v.target.arrays.get('cbrn_chemical_record_evidence_entries').every(x=>x===ticks(80)));
});
for(const defect of ['zero-ID','unknown-ID','missing-paid','zero-paid','wrong-target','wrong-phase'])test(`malformed-pending-preflight-and-UI-${defect}`,()=>{
  const v=fresh(0,[sale()]);v.target.vars.set('cbrn_occupation_last_record_uid',ticks(999));v.fault='refund';click(v);
  if(defect==='zero-ID')v.country.vars.set('cbrn_occupation_coverup_open_receipt_@64',0n);
  if(defect==='unknown-ID')v.country.vars.set('cbrn_occupation_coverup_open_receipt_@64',ticks(99));
  if(defect==='missing-paid')v.country.vars.delete('cbrn_occupation_coverup_receipt_paid_@1');
  if(defect==='zero-paid')v.country.vars.set('cbrn_occupation_coverup_receipt_paid_@1',0n);
  if(defect==='wrong-target')v.country.vars.set('cbrn_occupation_coverup_receipt_target_@1',ticks(65));
  if(defect==='wrong-phase')v.country.vars.set('cbrn_occupation_coverup_receipt_phase_@1',ticks(9));
  v.set('cbrn_occupation_coverup_target',0).set('cbrn_occupation_coverup_receipt_id',0);assert.equal(v.run('cbrn_occupation_coverup_can_retry_refund'),false);
  for(const key of quoteOut)v.set(key,0);assert.equal(v.run('cbrn_occupation_can_pay_seal_state_pp'),false);assert.equal(v.run('cbrn_occupation_can_pay_destroy_records_pp'),false);
  for(const getter of ['GetCbrnOccupationSealStatePpQuote','GetCbrnOccupationDestroyRecordsPpQuote','GetCbrnOccupationSealStateCostDetails','GetCbrnOccupationDestroyRecordsCostDetails'])assert(v.render(getter).includes('Price unavailable'));
  const debits=writes(v,'add_political_power').filter(x=>BigInt(x.delta)<0n).length;click(v);assert.equal(writes(v,'add_political_power').filter(x=>BigInt(x.delta)<0n).length,debits);
  assert.equal(writes(v,'set_state_flag').length,0);assert.equal((v.country.arrays.get('black_friday_achievement_transaction_ids')??[]).length,0);
});
test('failed-refund-stays-recoverable-after-every-target-is-blocked',()=>{
  const v=fresh(0,[sale()]);v.target.vars.set('cbrn_occupation_last_record_uid',ticks(999));
  assert.equal(v.run('cbrn_occupation_coverup_has_pending_receipt'),false);
  v.fault='refund';click(v);assert.equal(v.country.pp,ticks(980));
  // The state is now blocked for any further cover-up; only the payer-level entry remains.
  assert.equal(v.run('cbrn_occupation_coverup_has_pending_receipt'),true);
  v.country.vars.set('universal_cost_transaction_row_plus_one_@1',S);v.run('cbrn_occupation_recover_paid_coverups');
  assert.equal(v.country.pp,ticks(1000));assert.equal(pending(v).length,0);
  assert.equal(v.run('cbrn_occupation_coverup_has_pending_receipt'),false);
});
test('valid-private-refund-preflight-does-not-guess-broken-core-row',()=>{
  const v=fresh(0,[sale()]);v.target.vars.set('cbrn_occupation_last_record_uid',ticks(999));v.fault='refund';click(v);v.country.pp=0n;
  v.set('cbrn_occupation_coverup_target',0).set('cbrn_occupation_coverup_receipt_id',0);assert(v.run('cbrn_occupation_coverup_can_retry_refund'));assert.equal(v.value('cbrn_occupation_coverup_receipt_id'),S);
  const debits=writes(v,'add_political_power').length;click(v);assert.equal(writes(v,'add_political_power').length,debits);assert.equal(v.country.pp,0n);assert.equal(phase(v),C('cbrn_occupation_coverup_receipt_phase.recorded_refund'));assert.deepEqual(pending(v),[S]);
});
for(const mode of ['ai-to-human','debug-to-normal'])test(`pending-payment-eligibility-snapshot-${mode}`,()=>{
  const v=fresh(0,[sale()]);if(mode==='ai-to-human')v.ai=true;else v.debug=true;
  v.fault='settle';click(v);assert.equal(v.country.pp,ticks(980));assert.equal(phase(v),C('cbrn_occupation_coverup_receipt_phase.applied_settlement'));
  assert.equal((v.country.arrays.get('cbrn_occupation_coverup_achievement_eligible_receipts')??[]).length,0);
  v.ai=false;v.debug=false;v.country.vars.set('universal_cost_transaction_row_plus_one_@1',S);
  const outcomeWrites=writes(v,'set_state_flag').length;v.run('cbrn_occupation_recover_paid_coverups');
  assert.equal(row(v,'transaction_states'),ticks(4));assert.equal(phase(v),undefined);assert.equal(v.country.pp,ticks(980));assert.equal(writes(v,'set_state_flag').length,outcomeWrites);
  assert.equal((v.country.arrays.get('black_friday_achievement_transaction_ids')??[]).length,0,'initially ineligible payment cannot become an eligible claim on recovery');
  assert.equal(v.calls.get('black_friday_record_achievement_transaction')??0,0);
});
for(const mode of ['human-to-ai','human-to-debug'])test(`pending-payment-recovery-still-requires-current-public-gates-${mode}`,()=>{
  const v=fresh(0,[sale()]);v.fault='settle';click(v);assert.deepEqual(v.country.arrays.get('cbrn_occupation_coverup_achievement_eligible_receipts'),[S]);
  if(mode==='human-to-ai')v.ai=true;else v.debug=true;v.country.vars.set('universal_cost_transaction_row_plus_one_@1',S);
  v.run('cbrn_occupation_recover_paid_coverups');assert.equal(row(v,'transaction_states'),ticks(4));assert.equal(phase(v),undefined);assert.equal((v.country.arrays.get('black_friday_achievement_transaction_ids')??[]).length,0);
  assert.deepEqual(v.country.arrays.get('cbrn_occupation_coverup_achievement_eligible_receipts'),[]);v.ai=false;v.debug=false;v.run('cbrn_occupation_recover_paid_coverups');assert.equal((v.country.arrays.get('black_friday_achievement_transaction_ids')??[]).length,0);
});
test('eligibility-snapshot-cleanup-is-exact-receipt-ID-not-array-tail',()=>{
  const v=fresh(0,[sale()]);v.fault='settle';click(v);v.state(65,102);v.fault='settle';v.faultTransaction=ticks(2);click(v,2);
  assert.deepEqual(v.country.arrays.get('cbrn_occupation_coverup_achievement_eligible_receipts'),[S,ticks(2)]);
  assert.equal(phase(v,1),C('cbrn_occupation_coverup_receipt_phase.applied_settlement'));assert.equal(phase(v,2),C('cbrn_occupation_coverup_receipt_phase.applied_settlement'));
  v.country.vars.set('universal_cost_transaction_row_plus_one_@1',S);v.run('cbrn_occupation_recover_paid_coverups');
  assert.equal(phase(v,1),undefined);assert.equal(phase(v,2),C('cbrn_occupation_coverup_receipt_phase.applied_settlement'));assert.deepEqual(v.country.arrays.get('cbrn_occupation_coverup_achievement_eligible_receipts'),[ticks(2)]);
  assert.deepEqual(v.country.arrays.get('black_friday_achievement_transaction_ids'),[S]);
  v.country.vars.set('universal_cost_transaction_row_plus_one_@2',ticks(2));v.run('cbrn_occupation_recover_paid_coverups');
  assert.deepEqual(v.country.arrays.get('cbrn_occupation_coverup_achievement_eligible_receipts'),[]);assert.deepEqual(v.country.arrays.get('black_friday_achievement_transaction_ids'),[S,ticks(2)]);
  assert.equal(writes(v,'add_political_power').length,2);assert.equal(v.country.pp,ticks(950));
});
test('eligible-snapshot-is-cleared-on-real-record-rejection-and-refund',()=>{
  for(const failure of ['record','missing-UID']) {
    const v=fresh(0,[sale()]);if(failure==='record')v.fault='record';else v.target.vars.set('cbrn_occupation_last_record_uid',ticks(999));click(v);
    assert.equal(v.country.pp,ticks(1000));assert.deepEqual(v.country.arrays.get('cbrn_occupation_coverup_achievement_eligible_receipts'),[]);assert.equal((v.country.arrays.get('black_friday_achievement_transaction_ids')??[]).length,0);
  }
});
test('missing-payment-eligibility-proof-cannot-be-inferred-at-recovery',()=>{
  const v=fresh(0,[sale()]);v.fault='settle';click(v);v.country.arrays.delete('cbrn_occupation_coverup_achievement_eligible_receipts');v.country.vars.set('universal_cost_transaction_row_plus_one_@1',S);
  v.run('cbrn_occupation_recover_paid_coverups');assert.equal(row(v,'transaction_states'),ticks(4));assert.equal(phase(v),undefined);assert.equal(v.country.pp,ticks(980));assert.equal((v.country.arrays.get('black_friday_achievement_transaction_ids')??[]).length,0);
});
for(const [p,raw] of sources)results.hashes[p]=crypto.createHash('sha256').update(raw).digest('hex');
results.scenarioCount=results.scenarios.length;results.helperReturns=all.reduce((n,v)=>n+v.helperReturns,0);results.discardedHelperTemps=all.reduce((n,v)=>n+v.droppedTemps,0);
console.log(JSON.stringify(results,null,2));
