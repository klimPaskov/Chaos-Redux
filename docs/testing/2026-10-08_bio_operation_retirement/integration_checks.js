// Read-only runtime census and exact surviving-definition checks.
// Run: node docs/testing/2026-10-08_bio_operation_retirement/integration_checks.js
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'../../..');
const {parse}=require('../../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const manifest=JSON.parse(fs.readFileSync(path.join(__dirname,'retirement_manifest.json')));
const read=p=>fs.readFileSync(path.join(root,p));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
function files(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?files(path.join(dir,e.name)):[path.join(dir,e.name)]);}
function noSchemas(s){let m;while((m=/\bschema\s*=\s*\{/.exec(s))){let i=m.index+m[0].length,d=1;while(d&&i<s.length){if(s[i]==='{')d++;else if(s[i]==='}')d--;i++;}assert.equal(d,0);s=s.slice(0,m.index)+s.slice(i);}return s;}
const runtime=['common','events','interface','localisation','history','gfx'].flatMap(p=>files(path.join(root,p))).filter(f=>/\.(txt|gui|gfx|yml|asset|lua)$/.test(f));
const obsolete=/bio_operative_release_|bio_operation_plant_outbreak|bio_lifecycle_confirm_operative_release_from_capture|bio_set_integrated_operations_bw_modifiers_from_(actor_country|operation_actor)|bio_operation_calculate_plant_success_chance|bio_operation_apply_weaponized_zombie_consequences|bio_execute_weaponized_zombie_plant_operation|operation_plant_|bioweapon_plant_reservoir|bioweapon_seed_medical_chain|bioweapon_contaminate_transport_hub|GFX_operations_plant_bioweapon|GFX_phase_bioweapon_/;
const leftovers=runtime.filter(f=>obsolete.test(fs.readFileSync(f,'utf8'))).map(f=>path.relative(root,f));
assert.deepEqual(leftovers,[]);
for(const x of [...manifest.deletedFiles,...manifest.retiredAssets])assert(!fs.existsSync(path.join(root,x.path)),x.path);
for(const x of manifest.deletedFiles)assert.equal(hash(fs.readFileSync(path.join(__dirname,'before',x.path))),x.beforeSha256);
for(const x of manifest.editedFiles){
 const before=fs.readFileSync(path.join(__dirname,'before',x.path));
 const archivedAfter=fs.readFileSync(path.join(__dirname,'after',x.path));
 assert.equal(hash(before),x.beforeSha256);assert.equal(hash(archivedAfter),x.afterSha256);
 const expected=parse(noSchemas(before.toString('utf8'))).filter(n=>!x.removedBlocks.some(b=>b.id===n.key));
 assert.deepEqual(parse(noSchemas(read(x.path).toString('utf8'))),expected,x.path);
}
const native=[];
for(const f of files(path.join(root,'common/raids')).filter(f=>f.endsWith('.txt'))){
 for(const top of parse(fs.readFileSync(f,'utf8'))){
  if(top.key!=='types'||!Array.isArray(top.value))continue;
  for(const n of top.value){
   if(!Array.isArray(n.value))continue;const c=n.value.find(x=>x.key==='category');
   if(c&&['chemical_raids','biological_raids'].includes(c.value))native.push({id:n.key,category:c.value,path:path.relative(root,f).replaceAll('\\','/')});
  }
 }
}
assert.deepEqual([...new Set(native.map(x=>x.category))].sort(),['biological_raids','chemical_raids']);
const covert=['anthrax','plague','tularemia','smallpox'].flatMap(a=>['base','theater','terminal'].map(t=>'bio_sabotage_'+a+'_'+t));
const zombies=['low','medium','high'].flatMap(t=>['weaponized_zombie_strike_'+t,'weaponized_zombie_strike_'+t+'_friendly']);
for(const id of [...covert,...zombies])assert.equal(native.filter(x=>x.id===id).length,1,id);
assert(read('common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt').toString('utf8').includes('constant:bio_lifecycle_route.operative_release'));
const report={kind:'parent runtime retirement census and source-preservation checks',deletedSourceFiles:manifest.deletedFiles.length,retiredAssets:manifest.retiredAssets.length,obsoleteRuntimeConsumers:leftovers,scannedRuntimeFiles:runtime.length,nativeCbrnTypeCount:native.length,categoryCounts:Object.fromEntries(['chemical_raids','biological_raids'].map(c=>[c,native.filter(n=>n.category===c).length])),retainedCovertNativeTypes:covert,retainedZombieTypes:zombies,event016SharedRoutePreserved:true,survivingLifecycleEffectAndConstantAstsPreserved:true,condemnationAdapterAstPreserved:true,native,limits:['No native panel/callback/payment/spawn execution.','Literal and prefix/constructor-fragment scan is bounded to active runtime source; documentation and archives are intentionally excluded.','Constant schemas are excluded from the AST comparison; exact archived source bytes and hashes remain separately verified.']};
fs.writeFileSync(path.join(__dirname,'integration_census.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,native:undefined},null,2));
