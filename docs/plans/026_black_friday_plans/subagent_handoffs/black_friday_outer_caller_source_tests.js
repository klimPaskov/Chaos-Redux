// Bounded actual caller scenarios. Reuses architect01a10115's source VM.
// No quote math, receipt algorithm, payment adapter, or engine proof is duplicated.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const cp = require('node:child_process');
const core = require('./exact_quote_source_tests.js');
const audit = require('./black_friday_outer_caller_contract_audit.js');
const { VM, S, ticks, definitions, constants, helperOutputs } = core;
const { root, sources, parsed, defs, field, files } = audit;
// Preserve the actual before-source after the integration has been committed.
const baselineRevision = 'f32aaa4b7acc3621fcb5375743b63bfc7a81f739';
for (const [name, { node }] of defs) definitions.set(name, node.value);
for (const file of ['common/script_constants/026_black_friday_constants.txt',
  'common/script_constants/cbrn_system_constants.txt', 'common/script_constants/007_fury_constants.txt']) {
  // Only numeric tuning entries used by these callers. Broader schema list
  // grammar is outside the quotation VM's deliberately bounded parser.
  const text = fs.readFileSync(path.join(root, file), 'utf8');
  for (const category of text.matchAll(/^([a-z_0-9]+) = \{([\s\S]*?)^\}/gm)) {
    if (!['black_friday_event', 'fury_decision_cost', 'cbrn_protection_decision_cost'].includes(category[1])) continue;
    for (const item of category[2].matchAll(/^\s*([a-z_0-9]+) = (-?\d+(?:\.\d+)?)\s*(?:#[^\r\n]*)?$/gm))
      constants.set(`constant:${category[1]}.${item[1]}`, ticks(item[2]));
  }
}
// Only consumed public returns are required at an OUTER owner call. Internal
// exact producer boundaries keep the original VM's complete assertions.
class CallerVM extends VM {
  constructor() { super(); this.balances = new Map(); }
  run(name, bypass = false) {
    if (name === 'black_friday_quote_custom_cost') {
      assert(this.vars.has('black_friday_quote_final_cost'), 'caller lacks quote final output');
      return super.run(name, true);
    }
    return super.run(name, bypass);
  }
  eval(nodes) {
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i];
      if (n.key === 'has_political_power' || n.key === 'command_power' || n.key === 'has_fuel' || n.key === 'has_equipment') {
        const check = n.key === 'has_equipment' ? n.value[0] : n;
        const resource = n.key === 'has_equipment' ? check.key : n.key;
        const balance = this.balances.get(resource) || 0n, amount = this.value(check.value);
        const accepted = check.op === '<' ? balance < amount : check.op === '>' ? balance > amount : balance === amount;
        if (!accepted) return false;
      } else {
        const group = [n];
        if (n.key === 'if') while (nodes[i+1] && ['else', 'else_if'].includes(nodes[i+1].key)) group.push(nodes[++i]);
        if (!super.eval(group)) return false;
      }
    }
    return true;
  }
}
const scenarios = [];
function scenario(id, f) { f(); scenarios.push(id); }
function quoteFixture(active = true, ratio = 5000) {
  const vm = new CallerVM();
  for (const [key, value] of [['ids', 26], ['ratios', ratio], ['priorities', 500], ['eligibility_masks', 0]])
    vm.arrays.set(`global.universal_cost_source_${key}`, active ? [ticks(value)] : []);
  vm.set('global.universal_cost_custom_quote_cache_valid', 1);
  if (active) vm.flags.add('black_friday_active');
  for (const name of ['has_political_power', 'command_power', 'has_fuel', 'support_equipment_1']) vm.balances.set(name, ticks(100000));
  return vm;
}
function frame(name) { return definitions.get(name); }
function prefixBeforeCall(name, call) {
  const body = frame(name), i = body.findIndex(n => n.key === call);
  assert(i >= 0, `${name} -> ${call}`); return body.slice(0, i + 1);
}
scenario('all-scoped-caller-declarations-and-no-localisation-quote-calls', () => {
  assert.equal(audit.gaps.length, 0);
  assert.equal(audit.inventory.filter(x => x.file === files[2] && /quote|can_pay/.test(x.helper)).length, 0);
});
scenario('cold-and-warm-fury-arrays-before-clear-append-and-spend-wrapper', () => {
  const vm = new VM(), body = frame('black_friday_fury_pay_reinforcement_cost');
  const active = field(body.find(n => n.key === 'if').value, 'limit');
  assert(active);
  const branch = body.find(n => n.key === 'if').value.filter(n => n.key !== 'limit');
  const i = branch.findIndex(n => n.key === 'black_friday_fury_pay_prepared_bundle_active');
  const prepare = branch.slice(0, i);
  for (let repeat = 0; repeat < 2; repeat++) {
    assert(vm.eval(prepare));
    for (const name of ['black_friday_fury_component_ids', 'black_friday_fury_component_resource_kinds',
      'black_friday_fury_component_family_masks', 'black_friday_fury_component_ordinary_costs']) {
      assert.equal(vm.tempArrays.get(name).length, 2, `${name}: placeholder or stale row survived`);
    }
    assert(vm.tempArrays.get('black_friday_fury_component_ordinary_costs').every(x => x > 0n));
  }
  const bare = new VM(); assert(bare.run('black_friday_fury_begin_component_list'));
  assert(!bare.tempArrays.has('black_friday_fury_component_ids'), 'cold undeclared array must die on helper return');
});
scenario('actual-protection-wrapper-chain-cold-warm-and-sale-expiry', () => {
  // Execute the actual owner limit prefix, including its four caller declarations.
  const owner = frame('black_friday_pay_cbrn_recondition_masks');
  const limit = field(owner.find(n => n.key === 'if').value, 'limit');
  for (const active of [true, false]) {
    const vm = quoteFixture(active);
    for (let repeat = 0; repeat < 2; repeat++) {
      assert(vm.eval(limit));
      for (const suffix of ['ordinary_pp', 'ordinary_support', 'pp_cost', 'support_cost'])
        assert(vm.vars.has(`black_friday_cbrn_protection_pair_${suffix}`), `${suffix} lost across can_pay/quote/pair returns`);
      const ordinaryPP = vm.value('black_friday_cbrn_protection_pair_ordinary_pp');
      const ordinarySupport = vm.value('black_friday_cbrn_protection_pair_ordinary_support');
      assert(ordinaryPP > 0n && ordinarySupport > 0n, 'original owner inputs must be positive, not initializer zeros');
      const expected = amount => active ? ((amount + 2n*S-1n)/(2n*S))*S : amount;
      assert.equal(vm.value('black_friday_cbrn_protection_pair_pp_cost'), expected(ordinaryPP));
      assert.equal(vm.value('black_friday_cbrn_protection_pair_support_cost'), expected(ordinarySupport));
    }
  }
});
scenario('protection-required-component-shortage-and-missing-live-source-fail-closed', () => {
  const limit = field(frame('black_friday_pay_cbrn_recondition_masks').find(n => n.key === 'if').value, 'limit');
  const short = quoteFixture(); short.balances.set('support_equipment_1', 0n); assert.equal(short.eval(limit), false);
  const missing = quoteFixture(); missing.arrays.set('global.universal_cost_source_ids', []); assert.equal(missing.eval(limit), false);
});
scenario('negative-control-undeclared-protection-forwarded-prices-do-not-export', () => {
  const limit = field(frame('black_friday_pay_cbrn_recondition_masks').find(n => n.key === 'if').value, 'limit');
  const bare = quoteFixture();
  assert(bare.eval(limit.filter(n => n.key !== 'set_temp_variable')));
  assert.equal(bare.vars.has('black_friday_cbrn_protection_pair_pp_cost'), false);
  assert.equal(bare.vars.has('black_friday_cbrn_protection_pair_ordinary_pp'), false);
});
scenario('preserved-parent-lookup-and-proof-output-storage', () => {
  for (const row of audit.inventory.filter(x => x.file === files[0] && ['universal_cost_find_transaction_row', 'universal_cost_find_component_row'].includes(x.helper)))
    assert.equal(row.missing.length, 0);
  const body = frame('black_friday_record_achievement_transaction');
  const encoded = JSON.stringify(body);
  assert(encoded.includes('black_friday_purchase_receipt_proof_valid'));
  assert(encoded.includes('black_friday_purchase_has_non_political_paid_component'));
});
// Recover pre-patch tokens by removing only our marked declaration groups.
function originalTokens(source) {
  const stripped = source.replace(/^[\t ]*# Caller-owned cost API outputs\.\r?\n(?:[\t ]*(?:set_temp_variable|resize_temp_array) = \{[^\r\n]*\}\r?\n)+/gm, '');
  return stripped.replace(/#[^\r\n]*/g, '').match(/"[^"\r\n]*"|[{}=<>]|[^\s{}=<>]+/g) || [];
}
// EC-A02 compares current production against the committed post-frame/pre-proof
// source, not against an archived copy of current production.
const proofBaselineRevision = 'e64e95aa3bcb9fcab5a38a248cad28aa78bd2294';
const crypto = require('node:crypto');
const proofChanged = new Map([
  ['black_friday_record_achievement_transaction', 'strict receipt validation before append/credit and stored pending claim amounts'],
  ['black_friday_scan_receipt_non_political_payment', 'source/state/unrefunded/typed-family/primary-basis/amount proof'],
  ['black_friday_scan_receipt_political_power_only', 'strict proof plus settled PP-primary and PP-only payment'],
  ['black_friday_confirm_achievement_transaction', 'revalidate persisted pending claims against settled unrefunded receipt']
]);
const proofAdded = new Set(['black_friday_validate_ordinary_receipt_proof']);
const pureHelpers = new Set(['universal_cost_prepare_achievement_receipt_metadata',
  'universal_cost_bind_achievement_receipt_metadata', 'black_friday_prepare_achievement_claim_metadata']);
const roleInputs = ['family_id','primary_component_id','cost_basis','primary_member'].map(x =>
  'universal_cost_transaction_achievement_' + x);
const roleSnapshots = ['family','primary','basis','member'].map(x => 'universal_cost_record_metadata_' + x);
const removableTemps = new Set([...roleInputs,...roleSnapshots]);
const metadataColumns = new Set(['universal_cost_transaction_achievement_family_ids',
  'universal_cost_transaction_achievement_primary_component_ids','universal_cost_transaction_achievement_cost_bases',
  'universal_cost_component_achievement_family_ids','universal_cost_component_achievement_primary_members',
  'black_friday_achievement_transaction_ordinary_costs','black_friday_achievement_transaction_paid_costs']);
const coreFile = 'common/scripted_effects/chaosx_universal_cost_effects.txt';
const preservedFiles = [files[0], coreFile, 'common/scripted_effects/012_africa_rsa_purchase_effects.txt'];
const preservation = { baselineRevision: proofBaselineRevision, historicalFrameBaseline: baselineRevision,
  proofSemanticChanges: Object.fromEntries(proofChanged), addedProofHelpers: [...proofAdded],
  pureMetadataHelpers: [...pureHelpers], sourceHashes: {}, baselineSourceHashes: {},
  comparedFunctions: {}, removedMetadata: {}, purityChecks: [], negativeControls: [] };
const currentTrees = new Map(), baselineTrees = new Map();
for (const file of preservedFiles) {
  const text = sources.get(file) || fs.readFileSync(path.join(root,file),'utf8');
  const before = cp.execFileSync('git',['show',proofBaselineRevision + ':' + file],{cwd:root,encoding:'utf8'});
  preservation.sourceHashes[file] = crypto.createHash('sha256').update(text).digest('hex');
  preservation.baselineSourceHashes[file] = crypto.createHash('sha256').update(before).digest('hex');
  currentTrees.set(file,core.parse(text)); baselineTrees.set(file,core.parse(before));
}
function semantic(nodes) { return nodes.map(n => ({key:n.key,op:n.op,value:Array.isArray(n.value)?semantic(n.value):n.value})); }
const helperTree = new Map([...currentTrees.values()].flat().map(n=>[n.key,n.value]));
function readonlyCondition(nodes) {
  return nodes.every(n => ['AND','OR','NOT'].includes(n.key) ? Array.isArray(n.value) && readonlyCondition(n.value) :
    n.key==='has_variable' ? typeof n.value==='string' : n.key==='check_variable' && Array.isArray(n.value) &&
      n.value.every(arg=>typeof arg.value==='string'));
}
function metadataWrite(n,names=removableTemps) {
  return n.key === 'set_temp_variable' && Array.isArray(n.value) && n.value.length===1 &&
    typeof n.value[0].value==='string' && names.has(n.value[0].key);
}
function metadataOnlyIf(n,names=removableTemps) {
  if(n.key!=='if'||!Array.isArray(n.value))return false;
  const limits=n.value.filter(x=>x.key==='limit'),body=n.value.filter(x=>x.key!=='limit');
  return limits.length===1 && readonlyCondition(limits[0].value) && body.length>0 &&
    body.every(x=>metadataWrite(x,names)||metadataOnlyIf(x,names));
}
function validatePurity(trees=helperTree) {
  const shapes = {
    universal_cost_prepare_achievement_receipt_metadata: [
      ['universal_cost_transaction_achievement_family_ids','universal_cost_transaction_ids^num'],
      ['universal_cost_transaction_achievement_primary_component_ids','universal_cost_transaction_ids^num'],
      ['universal_cost_transaction_achievement_cost_bases','universal_cost_transaction_ids^num'],
      ['universal_cost_component_achievement_family_ids','universal_cost_component_ids^num'],
      ['universal_cost_component_achievement_primary_members','universal_cost_component_ids^num']],
    black_friday_prepare_achievement_claim_metadata: [
      ['black_friday_achievement_transaction_ordinary_costs','black_friday_achievement_transaction_ids^num'],
      ['black_friday_achievement_transaction_paid_costs','black_friday_achievement_transaction_ids^num']]
  };
  for(const [name,rows] of Object.entries(shapes)) {
    const expected=core.parse(rows.map(([array,size])=>'resize_array = { array = '+array+' size = '+size+' }').join('\n'));
    assert.deepEqual(semantic(trees.get(name)),semantic(expected),name+' may only zero-extend/resize declared metadata columns');
  }
  const validTemps = new Set(['universal_cost_record_metadata_valid']);
  function bind(nodes) {
    for(const n of nodes) {
      if(n.key==='universal_cost_prepare_achievement_receipt_metadata')assert.equal(n.value,'yes');
      else if(metadataWrite(n,validTemps))continue;
      else if(n.key==='set_variable'){
        assert.equal(n.value.length,1);
        assert.equal(typeof n.value[0].value,'string','metadata assignment must be scalar');
        assert(metadataColumns.has(n.value[0].key.split('^')[0]),'binding writes nonmetadata '+n.value[0].key);
      } else if(n.key==='if'){
        const limit=n.value.filter(x=>x.key==='limit');assert.equal(limit.length,1);assert(readonlyCondition(limit[0].value));
        bind(n.value.filter(x=>x.key!=='limit'));
      } else if(n.key==='else')bind(n.value);
      else assert.fail('impure metadata helper command '+n.key);
    }
  }
  bind(trees.get('universal_cost_bind_achievement_receipt_metadata'));
}
function normalized(nodes,counters={}) {
  const result=[];
  for(let i=0;i<nodes.length;i++){
    const n=nodes[i];
    let kind=null;
    if(metadataWrite(n))kind='typedTemporaryWrites';
    else if(pureHelpers.has(n.key)){assert.equal(n.value,'yes');kind='verifiedPureCalls';}
    else if(metadataOnlyIf(n)){
      // Do not detach an ELSE or alter an enclosing gameplay condition.
      assert(!['else','else_if'].includes(nodes[i+1]?.key),'metadata branch has gameplay continuation');
      kind='metadataOnlyIfs';
    }
    if(kind){counters[kind]=(counters[kind]||0)+1;continue;}
    result.push({...n,value:Array.isArray(n.value)?normalized(n.value,counters):n.value});
  }
  return result;
}
scenario('effects-core-RSA-preservation-from-pinned-pre-proof-e64', () => {
  validatePurity(); preservation.purityChecks=[...pureHelpers];
  for(const file of preservedFiles){
    const before=new Map(baselineTrees.get(file).map(n=>[n.key,n]));
    const current=new Map(currentTrees.get(file).map(n=>[n.key,n]));
    assert.equal(before.size,baselineTrees.get(file).length,'duplicate baseline helper');
    assert.equal(current.size,currentTrees.get(file).length,'duplicate current helper');
    const allowedNew=file===files[0]?new Set([...proofAdded,'black_friday_prepare_achievement_claim_metadata']):
      file===coreFile?new Set(['universal_cost_prepare_achievement_receipt_metadata','universal_cost_bind_achievement_receipt_metadata']):new Set();
    for(const name of current.keys())if(!before.has(name))assert(allowedNew.has(name),'unexpected added helper '+name);
    for(const name of allowedNew)assert(current.has(name)&&!before.has(name),'required new helper '+name);
    const names=[],counts={};
    for(const [name,n] of before){
      assert(current.has(name),'removed helper '+name);
      if(file===files[0]&&proofChanged.has(name))continue;
      assert.deepEqual(semantic(normalized(current.get(name).value,counts)),semantic(n.value),
        file+' changed nonmetadata cost/control/native payment/outcome/flag/lifecycle semantics in '+name);
      names.push(name);
    }
    preservation.comparedFunctions[file]=names;preservation.removedMetadata[file]=counts;
  }
  for(const name of proofChanged.keys())assert(baselineTrees.get(files[0]).some(n=>n.key===name),'allowlist absent from baseline '+name);
});
scenario('metadata-normalization-rejects-price-flag-control-and-impure-helper-mutations', () => {
  const n=core.parse('add_political_power = 5 set_country_flag = forbidden if = { limit = { check_variable = { x = 1 } } set_temp_variable = { universal_cost_transaction_achievement_primary_member = 1 } add_command_power = 3 }');
  const cleaned=normalized(n);
  assert.equal(cleaned.length,3);assert.equal(cleaned[2].value.some(x=>x.key==='add_command_power'),true);
  const priceMutation=structuredClone(n);priceMutation[0].value='6';
  assert.notDeepEqual(semantic(normalized(priceMutation)),semantic(cleaned));
  const flagMutation=structuredClone(n);flagMutation[1].value='different_flag';
  assert.notDeepEqual(semantic(normalized(flagMutation)),semantic(cleaned));
  preservation.negativeControls.push('native payment and flag changes retained','mixed metadata/gameplay IF retained');
  const altered=new Map(helperTree),body=structuredClone(altered.get('universal_cost_bind_achievement_receipt_metadata'));
  body.push(...core.parse('set_variable = { universal_cost_transaction_total_paid_costs^universal_cost_transaction_found_index = 0 }'));
  altered.set('universal_cost_bind_achievement_receipt_metadata',body);
  assert.throws(()=>validatePurity(altered),/binding writes nonmetadata/);
  preservation.negativeControls.push('metadata helper amount mutation rejected');
});
scenario('allowlisted-proof-semantics-execute-current-public-suite', () => {
  const result=JSON.parse(cp.execFileSync(process.execPath,
    [path.join(__dirname,'2026-10-03_achievement_receipt_proof_source_tests.js'),'--details'],{cwd:root,encoding:'utf8',maxBuffer:8*1024*1024}));
  assert.equal(result.scenarioCount,36);
  for(const file of preservedFiles)assert.equal(result.sourceHashes[file],preservation.sourceHashes[file],'proof suite concurrent source change');
  preservation.publicProof={scenarioCount:result.scenarioCount,sourceHashes:result.sourceHashes,
    externalSourceFinalHashes:result.externalSourceFinalHashes,helperReturns:result.helperReturns,droppedTemps:result.droppedTemps};
});
scenario('trigger-preservation-outside-the-architect-owned-central-block', () => {
  const before = core.parse(cp.execFileSync('git', ['show', `${baselineRevision}:${files[1]}`], { cwd: root, encoding: 'utf8' }));
  const current = core.parse(originalTokens(sources.get(files[1])).join(' '));
  const outside = nodes => nodes.filter(n => n.key !== 'black_friday_quote_custom_cost');
  assert.deepEqual(outside(current), outside(before), 'noninitialization trigger logic changed');
  const central = defs.get('black_friday_quote_custom_cost').node;
  assert(!sources.get(files[1]).slice(central.start, central.end).includes('# Caller-owned cost API outputs.'), 'protected central block was patched');
});
scenario('scoped-localisation-is-byte-identical-to-the-captured-baseline', () => {
  const crypto = require('node:crypto');
  assert.equal(crypto.createHash('sha256').update(sources.get(files[2])).digest('hex'),
    '665dd28b4cb12380ace61fcbbab36a11e035da885ac5fa38b590a4fc2f17098e');
});
console.log(JSON.stringify({ scenarios, scenarioCount: scenarios.length, inspectedBoundaries: audit.inventory.length, preservation,
  evidence: 'actual caller fragments with architect-owned conservative VM, native affordability queries modeled only',
  limitations: 'No engine, full owner payment, save/reload, GUI render, or repository-wide caller acceptance proof' }, null, 2));
