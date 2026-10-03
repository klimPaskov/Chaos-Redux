// Read-only bounded cost caller inventory and declaration patch proposal.
// No shared algorithm, engine emulator, or gameplay provider is implemented.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '../../../..');
const files = [
  'common/scripted_localisation/cbrn_protection_cost_scripted_localisation.txt',
  'common/scripted_localisation/cbrn_decontamination_cost_scripted_localisation.txt',
  ...['cbrn_protective_aid_decision_effects','cbrn_doctrine_effects','001_communism_spread_effects',
    '007_fury_effects','016_alien_infantry_api_effects','017_random_faction_effects','germany_mengele_effects']
    .map(n => `common/scripted_effects/${n}.txt`),
  ...['cbrn_protective_aid_decision_triggers','cbrn_protection_triggers','cbrn_occupation_triggers',
    'cbrn_doctrine_triggers','017_random_faction_triggers','germany_mengele_triggers']
    .map(n => `common/scripted_triggers/${n}.txt`),
  ...['001_communism_spread_decisions','007_fury_decisions','012_africa_elephant_operations_decisions',
    '016_alien_infantry_landing_decisions','biowarfare_disease_containment_decisions',
    'cbrn_diplomacy_decisions','cbrn_protection_decisions'].map(n => `common/decisions/${n}.txt`),
];
const readOnlyFiles = ['common/scripted_effects/026_black_friday_effects.txt',
  'common/scripted_triggers/026_black_friday_triggers.txt',
  'common/scripted_localisation/026_black_friday_scripted_localisation.txt',
  'common/scripted_effects/chaosx_universal_cost_effects.txt',
  'common/scripted_triggers/chaosx_universal_cost_triggers.txt',
  'common/scripted_triggers/chaosx_universal_cost_exact_triggers.txt',
  'common/scripted_effects/012_africa_rsa_purchase_effects.txt',
  'common/scripted_triggers/012_africa_rsa_purchase_triggers.txt',
  'common/scripted_effects/cbrn_protection_decision_effects.txt',
  'common/scripted_triggers/condemnation_sanctions_triggers.txt',
  'common/scripted_effects/cbrn_hq_effects.txt'];
const sources = new Map([...files, ...readOnlyFiles].map(f => [f, fs.readFileSync(path.join(root, f), 'utf8')]));
const sha = source => crypto.createHash('sha256').update(source).digest('hex');
function parse(source) {
  const tokens = [...source.matchAll(/#[^\r\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>]+/g)].filter(t => !t[0].startsWith('#'));
  let i = 0;
  function body(nested = false) {
    const out = [];
    while (i < tokens.length && tokens[i][0] !== '}') {
      const t = tokens[i++], key = t[0];
      if (key === '{') { const value = body(true); out.push({key:null, value, start:t.index, end:tokens[i-1].index+1}); continue; }
      const op = tokens[i]?.[0];
      if (!['=', '<', '>'].includes(op)) { out.push({key:null, value:key, start:t.index, end:t.index+key.length}); continue; }
      i++; let value = tokens[i++][0];
      if (value === '{') value = body(true);
      out.push({key, op, value, start:t.index, end:tokens[i-1].index+tokens[i-1][0].length});
    }
    if (nested) assert.equal(tokens[i++][0], '}');
    return out;
  }
  const out = body(); assert.equal(i,tokens.length); return out;
}
const parsed = new Map([...sources].map(([f,s]) => [f,parse(s)]));
const defs = new Map();
for (const [file,nodes] of parsed) if (/scripted_(effects|triggers)/.test(file))
  for (const node of nodes) if (node.key && Array.isArray(node.value)) defs.set(node.key,{file,node});
const field = (nodes,key) => nodes.find(n => n.key === key)?.value;
const variableName = n => field(n.value,'var') || n.value[0]?.key;
const union = (...sets) => new Set(sets.flatMap(s=>[...s]));
const shared = {
  universal_cost_quote_integer: ['universal_cost_quote_final_cost','universal_cost_quote_valid','universal_cost_quote_source_count',
    'universal_cost_quote_displayed_cost','universal_cost_quote_saved_cost','universal_cost_quote_primary_source_id','universal_cost_quote_composed_ratio'],
  universal_cost_check_quote_affordable:['universal_cost_quote_affordable'],
  universal_cost_pay_component:['universal_cost_payment_result'], universal_cost_credit_component:['universal_cost_credit_result'],
  universal_cost_record_transaction:['universal_cost_record_transaction_result','universal_cost_recorded_component_index'],
  universal_cost_settle_transaction:['universal_cost_settle_transaction_result'],
  universal_cost_mark_component_refunded:['universal_cost_mark_component_refunded_result'],
  universal_cost_refund_transaction:['universal_cost_refund_transaction_result','universal_cost_refund_total','universal_cost_refund_unhandled_total'],
  universal_cost_find_transaction_row:['universal_cost_transaction_found_index','universal_cost_transaction_is_indexed','universal_cost_transaction_lookup_result','universal_cost_transaction_pointer'],
  universal_cost_find_component_row:['universal_cost_component_found_index','universal_cost_component_lookup_result'],
  black_friday_quote_custom_cost:['black_friday_quote_final_cost','black_friday_quote_valid','black_friday_quote_composed_ratio','black_friday_quote_rounding_quantum'],
  cbrn_protective_aid_quote_factory_cost:['cbrn_protective_aid_factory_quote','cbrn_protective_aid_factory_quote_valid'],
  cbrn_quote_occupied_program_mask_reservation:['cbrn_mask_reservation_quote','cbrn_mask_reservation_available_stock'],
  condemnation_prepare_scaled_fraction_cost:['condemnation_scaled_cost'],
};
function walk(nodes,fn) { for(const n of nodes){ fn(n); if(Array.isArray(n.value)) walk(n.value,fn); } }
const tempNames = new Set(Object.values(shared).flat()),tempArrays=new Set();
const metadata = new Map();
for(const [name,{node}] of defs){
  const writes = new Set(), reads = new Set(), calls = new Set();
  walk(node.value,n=>{
    if(n.key==='set_temp_variable'){writes.add(variableName(n));tempNames.add(variableName(n));}
    if(n.key==='resize_temp_array'||n.key==='add_to_temp_array') {const a=field(n.value,'array')||n.value[0]?.key;writes.add(a);tempNames.add(a);tempArrays.add(a);}
    if(n.key==='clear_temp_array'){writes.add(n.value);tempNames.add(n.value);tempArrays.add(n.value);}
    if(defs.has(n.key)&&!Array.isArray(n.value)) calls.add(n.key);
  });
  metadata.set(name,{writes,reads,calls});
}
function names(token) {
  if(typeof token!=='string') return [];
  return [...new Set(token.split(/[\^:@?\[\].|"\s]+/).filter(x=>tempNames.has(x)))];
}
function readsOf(nodes) {
  const out = new Set();
  walk(nodes,n=>{
    if(n.key==='set_temp_variable') { for(const x of names(field(n.value,'value')||n.value[0]?.value))out.add(x); }
    else if(!Array.isArray(n.value)){ for(const x of [...names(n.key),...names(n.value)])out.add(x); }
  });
  return out;
}
const outputs = new Map(), inputs = new Map();
for(const [name,m] of metadata){m.reads=readsOf(defs.get(name).node.value);outputs.set(name,new Set(shared[name]||m.writes));inputs.set(name,new Set([...m.reads].filter(x=>!m.writes.has(x))));}
// Public shared fields are explicit. Owner wrapper outputs follow their actual
// temporary writes, never normal scoped writes from ordinary cost providers.
for(let p=0;p<25;p++)for(const [name,m]of metadata){
  if(!shared[name]) {
    const merged=union(m.writes,...[...m.calls].map(c=>outputs.get(c)));
    outputs.set(name,/black_friday_/.test(name)?new Set([...merged].filter(x=>!x.startsWith('universal_cost_'))):merged);
  }
  inputs.set(name,new Set([...union(m.reads,...[...m.calls].map(c=>inputs.get(c)))].filter(x=>!outputs.get(name).has(x))));
}
const costCall = name => shared[name] || /black_friday|^universal_cost_/.test(name) || /(?:quote|cost|payment|afford|debit|transaction)/.test(name);
const demand = new Map([...defs.keys()].map(k=>[k,new Set()])),liveAt=new Map();
const roots=[];
// Cost display values are consumed by the selected localisation key after its
// trigger finishes. Resolve that real key, including direct numeric variables.
const locValues = new Map();
for(const name of fs.readdirSync(path.join(root,'localisation/english'))) if(name.endsWith('.yml')) {
  const text=fs.readFileSync(path.join(root,'localisation/english',name),'utf8');
  for(const m of text.matchAll(/^\s*([^#\s:]+):(?:\d+)?\s*"(.*)"\s*$/gm)) locValues.set(m[1],m[2]);
}
for(const file of files)for(const n of parsed.get(file)){
  if(!Array.isArray(n.value))continue;
  if(n.key==='defined_text')for(const t of n.value.filter(n=>n.key==='text')){
    const loc=field(t.value,'localization_key'), observed=names(locValues.get(loc)||'');
    roots.push({file,owner:field(n.value,'name'),nodes:field(t.value,'trigger')||[],out:new Set(observed)});
  }else if(/scripted_(effects|triggers)/.test(file)) roots.push({file,owner:n.key,nodes:n.value,out:demand.get(n.key)});
  else if(file.includes('/decisions/'))for(const decision of n.value.filter(n=>Array.isArray(n.value)))
    for(const block of decision.value.filter(n=>Array.isArray(n.value)))
      roots.push({file,owner:`${decision.key}.${block.key}`,nodes:block.value,out:new Set()});
}
function live(nodes,outgoing) {
  let set=new Set(outgoing||[]);
  for(const n of [...nodes].reverse()){
    liveAt.set(n,new Set(set));
    if(n.key==='set_temp_variable'){set.delete(variableName(n));set=union(set,readsOf([n]));}
    else if(defs.has(n.key)&&!Array.isArray(n.value)){
      for(const x of outputs.get(n.key))if(set.has(x))demand.get(n.key).add(x);
      set=union(set,inputs.get(n.key));
    }else if(Array.isArray(n.value))set=union(set,live(n.value,set));
    else set=union(set,readsOf([n]));
  }
  return set;
}
for(let p=0;p<25;p++){for(const r of roots)live(r.nodes,r.out);for(const [name,{node}]of defs)live(node.value,demand.get(name));}
const inventory=[],gaps=[],externalCalls=[];
for(const r of roots){
  function inspect(nodes,storage){for(const n of nodes){
    if(n.key==='set_temp_variable')storage.add(variableName(n));
    else if(n.key==='resize_temp_array'||n.key==='add_to_temp_array')storage.add(field(n.value,'array')||n.value[0]?.key);
    else if(defs.has(n.key)&&!Array.isArray(n.value)){
      if(!costCall(n.key))continue;
      const required=[...outputs.get(n.key)].filter(x=>liveAt.get(n)?.has(x));
      const missing=required.filter(x=>!storage.has(x));
      const row={file:r.file,owner:r.owner,helper:n.key,line:sources.get(r.file).slice(0,n.start).split('\n').length,start:n.start,required,missing};
      inventory.push(row);if(missing.length)gaps.push(row);
      if(process.argv.includes('--patch'))for(const x of missing)storage.add(x);
    }else if(!Array.isArray(n.value)&&n.value==='yes'&&costCall(n.key)&&!defs.has(n.key)) {
      externalCalls.push({file:r.file,owner:r.owner,helper:n.key,line:sources.get(r.file).slice(0,n.start).split('\n').length});
    }else if(Array.isArray(n.value)){
      const next=new Set(storage);inspect(n.value,next);
      if(!['if','else_if','else','OR','NOT','while_loop_effect','for_each_loop'].includes(n.key))for(const x of next)storage.add(x);
    }
  }}
  // An append-only helper receives its already-created list as input. Never
  // resize an inherited live list between component appends.
  const inheritedArrays=new Set();
  if(/append/.test(r.owner))for(const x of outputs.get(r.owner)||[])if(tempArrays.has(x))inheritedArrays.add(x);
  inspect(r.nodes,inheritedArrays);
}
const marker='# Existing-owner caller output storage.';
function defaultValue(name){
  if(name.includes('found_index')||name.endsWith('_transaction_index'))return 'constant:universal_cost_framework.invalid_index';
  if(name.endsWith('_result'))return 'constant:universal_cost_framework.result_no_op';
  if(name==='black_friday_quote_final_cost')return 'black_friday_quote_ordinary_cost';
  if(name==='universal_cost_quote_final_cost')return 'universal_cost_quote_ordinary_cost';
  return 'constant:universal_cost_framework.zero';
}
function stripAdded(source){return source.replace(/^[\t ]*# Existing-owner caller output storage\.\r?\n(?:[\t ]*(?:set_temp_variable|resize_temp_array) = \{[^\r\n]*\}\r?\n)+/gm,'');}
const canonical = source => JSON.stringify(parse(source),(key,value)=>['start','end'].includes(key)?undefined:value);
function changes(){
  const out=[];
  for(const file of files)for(const n of parsed.get(file)){
    if(!Array.isArray(n.value))continue;
    const containers=file.includes('/decisions/')?n.value.filter(x=>Array.isArray(x.value)):[n];
    for(const c of containers){
      const text=sources.get(file).slice(c.start,c.end),declarations=[];
      for(const group of text.matchAll(/# Existing-owner caller output storage\.\r?\n((?:[\t ]*(?:set_temp_variable|resize_temp_array) = \{[^\r\n]*\}\r?\n)+)/g))
        for(const line of group[1].trim().split(/\r?\n/))declarations.push(line.trim());
      if(declarations.length)out.push({file,owner:c.key==='defined_text'?field(c.value,'name'):c.key,
        boundaries:(text.match(/# Existing-owner caller output storage\./g)||[]).length,
        declarationCount:declarations.length,declarations:[...new Set(declarations)]});
    }
  }return out;
}
function baseline(){return Object.fromEntries([...sources].map(([file,source])=>[file,{sha256:sha(source),canonicalSha256:sha(canonical(source)),lines:source.split('\n').length}]));}
function proposal(){
  const baselineFile=path.join(__dirname,'existing_owner_caller_baseline.json');
  const saved=JSON.parse(fs.readFileSync(baselineFile,'utf8'));
  const patch=['*** Begin Patch'];
  for(const file of files){
    const rows=gaps.filter(g=>g.file===file);if(!rows.length)continue;
    const source=sources.get(file),lines=source.split(/\r?\n/),edits=new Map();
    assert.equal(sha(source),saved[file].sha256,`concurrent source change: refresh review/baseline for ${file}`);
    for(const r of rows){
      const i=r.line-1,line=lines[i],indent=line.match(/^\s*/)[0],pos=r.start-(source.lastIndexOf('\n',r.start-1)+1);
      const decl=r.missing.map(x=>tempArrays.has(x)?`resize_temp_array = { array = ${x} size = constant:universal_cost_framework.one }`:`set_temp_variable = { ${x} = ${defaultValue(x)} }`);
      assert(!r.missing.some(x=>x.includes('^')||x.includes('global.')),`scoped/array field needs manual contract review ${r.owner}`);
      if(line.slice(0,pos).trim()){
        const tail=line.slice(pos);assert(/\s+\}$/.test(tail),`complex inline call requires manual review ${r.file}:${r.line}`);
        edits.set(i,[line.slice(0,pos).trimEnd(),`${indent}\t${marker}`,...decl.map(x=>indent+'\t'+x),`${indent}\t${tail.replace(/\s+\}$/,'')}`,indent+'}']);
      }else edits.set(i,[indent+marker,...decl.map(x=>indent+x),line]);
    }
    patch.push(`*** Update File: ${path.join(root,file).replaceAll('\\','/')}`);
    const ranges=[];for(const i of [...edits.keys()].sort((a,b)=>a-b)){const lo=Math.max(0,i-2),hi=Math.min(lines.length-1,i+1);if(ranges.length&&lo<=ranges.at(-1)[1]+1)ranges.at(-1)[1]=hi;else ranges.push([lo,hi]);}
    for(const [lo,hi]of ranges){patch.push('@@');for(let i=lo;i<=hi;i++){if(edits.has(i))patch.push('-'+lines[i],...edits.get(i).map(s=>'+'+s));else patch.push(' '+lines[i]);}}
  }
  patch.push('*** End Patch');return patch.join('\n');
}
module.exports={root,files,readOnlyFiles,sources,parsed,defs,roots,inventory,gaps,externalCalls,parse,field,sha,baseline,canonical,stripAdded,shared,defaultValue,liveAt,tempArrays,changes};
if(require.main===module){
  if(process.argv.includes('--baseline'))console.log(JSON.stringify(baseline(),null,2));
  else if(process.argv.includes('--changes'))console.log(JSON.stringify(changes(),null,2));
  else if(process.argv.includes('--pinned-check')) {
    const file='common/scripted_effects/germany_mengele_effects.txt';
    const before=require('node:child_process').execFileSync('git',['show','e64e95aa3bcb9fcab5a38a248cad28aa78bd2294:'+file],{cwd:root,encoding:'utf8'});
    const names=changes().filter(x=>x.file===file).map(x=>x.owner),left=parse(before),right=parse(stripAdded(sources.get(file)));
    console.log(JSON.stringify({file,sha256:sha(before),canonicalSha256:sha(canonical(before)),ownedFunctions:names.map(name=>({name,
      before:sha(JSON.stringify(left.find(n=>n.key===name),(k,v)=>['start','end'].includes(k)?undefined:v)),
      after:sha(JSON.stringify(right.find(n=>n.key===name),(k,v)=>['start','end'].includes(k)?undefined:v))}))}));
  }
  else if(process.argv.includes('--patch'))console.log(proposal());
  else if(process.argv.includes('--inventory'))console.log(JSON.stringify({inventory,gaps,externalCalls},null,2));
  else if(process.argv.includes('--snapshot')) {
    const owners=[...new Set(inventory.map(r=>r.owner))],helpers=[...new Set(inventory.map(r=>r.helper))],fields=[...new Set(inventory.flatMap(r=>r.required))];
    console.log(JSON.stringify({schema:'bounded-caller-inventory-v1',files,owners,helpers,fields,
      columns:['fileIndex','ownerIndex','helperIndex','line','start','requiredFieldIndexes','missingFieldIndexes'],
      calls:inventory.map(r=>[files.indexOf(r.file),owners.indexOf(r.owner),helpers.indexOf(r.helper),r.line,r.start,r.required.map(x=>fields.indexOf(x)),r.missing.map(x=>fields.indexOf(x))]),
      externalCalls,sourceHashes:Object.fromEntries([...sources].map(([f,s])=>[f,sha(s)]))}));
  }
  else console.log(JSON.stringify({files:files.length,knownCostCalls:inventory.length,missingBoundaries:gaps.length,gaps},null,2));
}
