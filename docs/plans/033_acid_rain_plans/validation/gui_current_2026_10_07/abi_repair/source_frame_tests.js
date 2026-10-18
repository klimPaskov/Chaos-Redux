// Bounded real-body Event033 A4-A6 replay. Runs from repository root, writes nothing.
// Conservative helper frames, separate COUNTRY/global saved maps, no native game.
const fs = require('fs'), crypto = require('crypto'), assert = require('assert/strict');
const base = 'docs/plans/033_acid_rain_plans/validation/gui_current_2026_10_07/';
const read = p => fs.readFileSync(p, 'utf8');
const sha = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
function parse(s) {
 const ts = s.replace(/#[^\r\n]*/g,'').match(/"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>]+/g)||[];
 let i=0;
 function block(nested=false) {
  const ns=[];
  while(i<ts.length && ts[i]!=='}') {
   const key=ts[i++], op=ts[i++];
   assert.ok(['=','<','>'].includes(op), 'bad parse '+key+' '+op);
   const t=ts[i++]; ns.push({key,op,value:t==='{'?block(true):t});
  }
  if(nested) assert.equal(ts[i++],'}');
  return ns;
 }
 return block();
}
const val=(ns,k)=>ns.find(n=>n.key===k)?.value;
const constants=new Map();
for(const cat of parse(read('common/script_constants/033_acid_rain_constants.txt')))
 if(Array.isArray(cat.value)) for(const n of cat.value)
  if(!Array.isArray(n.value)&&Number.isFinite(Number(n.value))) constants.set('constant:'+cat.key+'.'+n.key,Number(n.value));
constants.set('constant:chaosx_date_units.zero',0); // explicit date-converter fixture boundary
const triggersPath='common/scripted_triggers/033_acid_rain_triggers.txt';
const trigNodes=parse(read(triggersPath));
const loc=new Map();
for(const line of read('localisation/english/033_acid_rain_l_english.yml').split(/\r?\n/)) {
 const m=line.match(/^([A-Za-z0-9_]+):\s*("(?:\\.|[^"\\])*")/);
 if(m) loc.set(m[1],JSON.parse(m[2]));
}
function build(guiPath,slPath) {
 const guiNodes=parse(read(guiPath)), slNodes=parse(read(slPath));
 const defs=new Map([...guiNodes,...trigNodes].filter(n=>Array.isArray(n.value)).map(n=>[n.key,n.value]));
 const texts=new Map(slNodes.filter(n=>n.key==='defined_text').map(n=>[val(n.value,'name'),n.value]));
 return {guiPath,slPath,defs,texts};
}
function ctx(saved={}) {
 const g=new Map(),c=new Map();
 for(const [k,v] of Object.entries(saved)) (k.startsWith('global.')?g:c).set(k,v);
 return {t:new Map(),g,c,trace:[],flags:new Set(),visits:[]};
}
function keyOf(k,c) {
 if(k.includes('^')) {const [a,b]=k.split('^');return a+'^'+num(b,c);}
 return k;
}
function num(x,c) {
 if(typeof x==='number')return x;
 assert.equal(typeof x,'string');
 if(Number.isFinite(Number(x))) return Number(x);
 if(x.startsWith('constant:')) {assert.ok(constants.has(x),'missing constant '+x);return constants.get(x);}
 x=x.replace(/^var:/,'');
 const k=keyOf(x,c);
 if(x.startsWith('global.'))return c.g.get(k)??0;
 return c.t.get(k)??c.c.get(k)??0;
}
function assign(ns) {
 return val(ns,'var')!==undefined?[val(ns,'var'),val(ns,'value')]:[ns[0].key,ns[0].value];
}
function helper(name,c,b) {
 if(name==='chaosx_convert_date_offset_to_days') {
  // Dates are fixture-relative days, not a claim about native date-unit arithmetic.
  c.t.set('chaosx_date_days',num('chaosx_date_offset',c)); return true;
 }
 assert.ok(b.defs.has(name),'unsupported helper '+name);
 const inherited=new Set(c.t.keys()), parent=c.t, child=new Map(parent);
 c.t=child; const result=run(b.defs.get(name),c,b);
 c.t=parent; for(const k of inherited) if(child.has(k))parent.set(k,child.get(k));
 c.trace.push({helper:name,inherited:[...inherited],discarded:[...child.keys()].filter(k=>!inherited.has(k))});
 return result;
}
function check(n,c,b) {
 if(n.key==='AND')return n.value.every(x=>check(x,c,b));
 if(n.key==='OR')return n.value.some(x=>check(x,c,b));
 if(n.key==='NOT')return !n.value.every(x=>check(x,c,b));
 if(n.key==='always')return n.value==='yes';
 if(n.key==='has_global_flag'||n.key==='has_country_flag')return c.flags.has(n.value);
 if(n.key==='check_variable') {
  const [k,v]=assign(n.value), l=num(k,c),r=num(v,c),op=val(n.value,'compare')??n.value[0].op;
  return ({equals:l===r,not_equals:l!==r,greater_than:l>r,less_than:l<r,greater_than_or_equals:l>=r,less_than_or_equals:l<=r,'=':l===r,'>':l>r,'<':l<r})[op];
 }
 if(b.defs.has(n.key))return helper(n.key,c,b);
 if(n.key==='set_temp_variable') {const[k,v]=assign(n.value);c.t.set(keyOf(k,c),num(v,c));return true;}
 throw Error('unsupported trigger '+n.key);
}
function run(ns,c,b) {
 let chain=false;
 for(const n of ns) {
  const k=n.key;
  if(k==='limit')continue;
  if(k==='if'||k==='else_if'||k==='else') {
   const allowed=k==='if'||!chain, limits=val(n.value,'limit')??[];
   const hit=allowed&&limits.every(x=>check(x,c,b));
   if(k==='if')chain=false;
   if(hit) {run(n.value.filter(x=>x.key!=='limit'),c,b);chain=true;}
   continue;
  }
  chain=false;
  if(['set_temp_variable','add_to_temp_variable','subtract_from_temp_variable','multiply_temp_variable','set_variable'].includes(k)) {
   const [a,v]=assign(n.value), target=keyOf(a,c),x=num(v,c);
   if(k==='set_variable') (a.startsWith('global.')?c.g:c.c).set(target,x);
   else c.t.set(target,k==='set_temp_variable'?x:k==='add_to_temp_variable'?num(a,c)+x:k==='subtract_from_temp_variable'?num(a,c)-x:num(a,c)*x);
  } else if(k==='clamp_temp_variable') {
   const a=val(n.value,'var');c.t.set(keyOf(a,c),Math.max(val(n.value,'min')===undefined?-Infinity:num(val(n.value,'min'),c),Math.min(val(n.value,'max')===undefined?Infinity:num(val(n.value,'max'),c),num(a,c))));
  } else if(k==='clear_array') {
   for(const a of [...c.g.keys()])if(a.startsWith(n.value+'^'))c.g.delete(a);
  } else if(k==='resize_array') {
   const a=val(n.value,'array'),size=num(val(n.value,'size'),c),value=num(val(n.value,'value'),c);
   for(let i=0;i<size;i++)c.g.set(a+'^'+i,value);
  } else if(k==='for_loop_effect') {
   const start=num(val(n.value,'start'),c),end=num(val(n.value,'end'),c),index=val(n.value,'value');
   const stop=val(n.value,'break')??'break';
   assert.ok(end-start<=1000); for(let i=start,iterations=0;i<end&&num(stop,c)===0&&iterations<1000;i++,iterations++) {c.t.set(index,i);c.visits.push({index,i});run(n.value.filter(x=>!['start','end','value','break'].includes(x.key)),c,b);}
  } else if(b.defs.has(k)||k==='chaosx_convert_date_offset_to_days')helper(k,c,b);
  else throw Error('unsupported effect '+k);
 }
 return true;
}
function localize(key,c,b,depth=0) {
 assert.ok(depth<10); assert.ok(loc.has(key),'missing loc '+key);
 return loc.get(key).replace(/\[\?([^\]|]+)(?:\|([^\]]+))?\]/g,(_,v,f)=>num(v,c).toFixed(f==='.1'?1:f==='.2'?2:0))
  .replace(/\[This\.([^\]]+)\]/g,(_,name)=>getter(name,c,b,depth+1));
}
function getter(name,c,b,depth=0) {
 assert.ok(b.texts.has(name),'missing getter '+name);
 for(const text of b.texts.get(name).filter(n=>n.key==='text')) {
  const trigger=val(text.value,'trigger')??[];
  // text.trigger is the real consuming caller frame; only nested helper cleanup occurs here.
  if(trigger.every(n=>check(n,c,b)))return localize(val(text.value,'localization_key'),c,b,depth);
 }
 throw Error('unmatched getter '+name);
}
const before=build(base+'abi_repair/sources_before/033_acid_rain_gui_effects.txt',base+'abi_repair/sources_before/033_acid_rain_scripted_localisation.txt');
const current=build('common/scripted_effects/033_acid_rain_gui_effects.txt','common/scripted_localisation/033_acid_rain_scripted_localisation.txt');
const stage=process.argv.includes('--before')?'before':'after', selected=stage==='before'?before:current;
const anchors=[[0,0],[201,83],[350,126],[368,61],[220,115],[385,175],[148,74],[125,138]];
const results=[];
function record(name,got,expected){assert.deepEqual(got,expected,name);results.push({name,got,expected,status:'passed'});}
if(stage==='after') {
 const allowed=new Set(['acid_rain_gui_marker_shown','acid_rain_gui_anchor_region','acid_rain_gui_anchor_x','acid_rain_gui_anchor_y',...regNamesPlaceholder()]);
 function regNamesPlaceholder(){return ['eligible','touched','untouched','status','front','active','visit','quota','severe','days','shelter_tier','water_tier','medical_tier','transport_tier','shelter_points','water_points','medical_points','transport_points','shelter_max','water_max','medical_max','transport_max','max_tier','preparedness_max'].map(n=>'acid_rain_gui_tt_'+n);}
 function trim(ns) {return ns.filter(n=>n.key!=='break'&&!(n.key==='set_temp_variable'&&(allowed.has(assign(n.value)[0])||/_break$/.test(assign(n.value)[0])))).map(n=>({...n,value:Array.isArray(n.value)?trim(n.value):n.value}));}
 for(const name of [...before.defs.keys()].filter(n=>n.startsWith('acid_rain_gui_')))assert.deepEqual(trim(current.defs.get(name)),trim(before.defs.get(name)),'non-envelope helper change '+name);
 for(const name of before.texts.keys())assert.deepEqual(trim(current.texts.get(name)),trim(before.texts.get(name)),'non-envelope getter change '+name);
 record('non-envelope AST preserved',true,true);
 const loopKinds=['for_loop_effect','while_loop_effect','for_each_loop','for_each_scope_loop'];
 const loopCounts=Object.fromEntries(loopKinds.map(k=>[k,0])),privateNames=new Set();
 function auditLoops(ns) {
  for(let i=0;i<ns.length;i++) {
   const n=ns[i];
   if(loopKinds.includes(n.key)) {
    loopCounts[n.key]++;
    const binding=val(n.value,'break'),previous=ns[i-1];
    assert.ok(binding&&previous?.key==='set_temp_variable','missing immediate loop reset');
    assert.deepEqual(assign(previous.value),[binding,'constant:acid_rain_runtime.zero']);
    assert.ok(!privateNames.has(binding),'shared private break name');privateNames.add(binding);
   }
   if(Array.isArray(n.value))auditLoops(n.value);
  }
 }
 auditLoops(parse(read(current.guiPath)));
 record('all four loop kinds inventoried with immediate unique resets',loopCounts,{for_loop_effect:6,while_loop_effect:0,for_each_loop:0,for_each_scope_loop:0});
}
function front(b,index,region,state=2) {
 const c=ctx({'global.date':100,['global.acid_rain_front_region_entries^'+index]:region,['global.acid_rain_front_state_entries^'+index]:state,['global.acid_rain_front_next_work_day_entries^'+index]:109});
 run(b.defs.get('acid_rain_gui_project_front_'+index),c,b);
 return {x:num('global.acid_rain_gui_front_'+index+'_marker_x',c),y:num('global.acid_rain_gui_front_'+index+'_marker_y',c),visible:num('global.acid_rain_gui_front_'+index+'_visible',c),trace:c.trace};
}
for(let i=1;i<=3;i++) for(let r=1;r<=7;r++) {
 const old=front(before,i,r),actual=front(selected,i,r);
 record('A4 before negative '+i+'/'+r,[old.x,old.y],[0,0]);
 record('A4 '+stage+' '+i+'/'+r,[actual.x,actual.y],stage==='before'?[0,0]:anchors[r]);
}
for(let i=1;i<=3;i++)record('A4 zero region '+i,front(selected,i,0).visible,0);
function storms(b,regions=[1,1,1],states=[0,1,1],layer=1,count=3) {
 const saved={'global.acid_rain_gui_superstorm_list_count':count,'global.acid_rain_gui_global_layer_active':layer};
 for(let i=0;i<3;i++) {
  saved['global.acid_rain_superstorm_ids^'+i]=21+i;
  saved['global.acid_rain_superstorm_region_entries^'+(21+i)]=regions[i];
  saved['global.acid_rain_superstorm_active_entries^'+(21+i)]=states[i];
  saved['global.acid_rain_superstorm_target_count_entries^'+(21+i)]=6-i;
 }
 const c=ctx(saved),body=b.defs.get('acid_rain_gui_refresh_read_only');
 const at=body.findIndex(n=>n.key==='set_variable'&&Array.isArray(n.value)&&n.value[0].key==='global.acid_rain_gui_superstorm_1_visible');
 assert.ok(at>=0);run(body.slice(at),c,b);
 return {c,markers:[1,2,3].map(i=>[num('global.acid_rain_gui_superstorm_'+i+'_marker',c),num('global.acid_rain_gui_superstorm_'+i+'_marker_x',c),num('global.acid_rain_gui_superstorm_'+i+'_marker_y',c)])};
}
record('A5 before nested negative',storms(before).markers,[[0,0,0],[0,0,0],[0,0,0]]);
record('A5 '+stage+' shared region',storms(selected).markers,stage==='before'?[[0,0,0],[0,0,0],[0,0,0]]:[[1,201,83],[1,249,83],[1,297,83]]);
for(const [name,regions,states,layer,count] of [
 ['different regions',[1,3,5],[0,1,1],1,3],['inactive',[1,3,5],[2,2,2],1,3],
 ['aftercare',[1,3,5],[0,1,1],0,3],['empty',[1,3,5],[0,1,1],1,0],
 ['invalid region',[0,3,5],[0,1,1],1,3]]) {
 const a=storms(selected,regions,states,layer,count);
 const flags=a.markers.map(x=>x[0]);
 record('A5 '+stage+' '+name,flags,stage==='before'?[0,0,0]:regions.map((r,i)=>Number(i<count&&r>0&&states[i]<2&&layer>0)));
}
const regNames=['eligible','touched','untouched','status','front','active','visit','quota','severe','days'];
function regionCtx(r,status) {
 const c=ctx(); const vals=[150,37,113,status,3,25,30,40,8,9];
 regNames.forEach((n,i)=>c.g.set('global.acid_rain_gui_region_'+n+'_entries^'+r,vals[i]));return c;
}
for(let r=1;r<=7;r++)for(let status=0;status<=3;status++) {
 const c=regionCtx(r,status),old=regionCtx(r,status);
 getter('GetAcidRainRegion'+r+'Tooltip',old,before);
 record('A6 baseline discarded '+r+'/'+status,regNames.filter(n=>old.t.has('acid_rain_gui_tt_'+n)).length,0);
 const text=getter('GetAcidRainRegion'+r+'Tooltip',c,selected);
 record('A6 '+stage+' retained '+r+'/'+status,regNames.filter(n=>c.t.has('acid_rain_gui_tt_'+n)).length,stage==='before'?0:10);
 if(stage==='after') {assert.ok(text.includes('37 of the 150'));assert.equal(num('acid_rain_gui_tt_status',c),status);assert.ok(text.includes(['No front is over','is on its way','is over this region','global acid layer'][status]));}
}
const prepNames=['shelter','water','medical','transport'];
for(const tier of [-1,0,1,2,3,4,5]) {
 const saved={acid_rain_preparedness:50};prepNames.forEach(n=>saved['acid_rain_'+n+'_tier']=tier);
 const c=ctx(saved);getter('GetAcidRainPreparednessTooltip',c,selected);
 const outs=[...c.t.keys()].filter(k=>k.startsWith('acid_rain_gui_tt_'));
 record('A6 '+stage+' Preparedness outputs tier '+tier,outs.length,stage==='before'?0:14);
 if(stage==='after') prepNames.forEach(n=>record('A6 clamped '+n+'/'+tier,num('acid_rain_gui_tt_'+n+'_tier',c),Math.max(0,Math.min(4,tier))));
}
// Inner-only mutation is an explicit negative control, not an implementation patch.
const innerOnly={...before,defs:new Map(before.defs)};
innerOnly.defs.set('acid_rain_gui_project_superstorm_marker',[...parse('set_temp_variable = { acid_rain_gui_anchor_x = 0 } set_temp_variable = { acid_rain_gui_anchor_y = 0 }'),...before.defs.get('acid_rain_gui_project_superstorm_marker')]);
record('A5 inner-only negative',storms(innerOnly).markers,[[0,0,0],[0,0,0],[0,0,0]]);
function traversal(b,seedPrivate=false) {
 const saved={'global.date':100,'global.acid_rain_phase':2,'global.acid_rain_gui_global_layer_active':0};
 for(let r=1;r<=7;r++) {saved['global.acid_rain_region_valid_entries^'+r]=100+r;saved['global.acid_rain_region_touched_entries^'+r]=10+r;}
 for(let i=1;i<=3;i++) {saved['global.acid_rain_front_state_entries^'+i]=2;saved['global.acid_rain_front_region_entries^'+i]=i;saved['global.acid_rain_front_active_state_count_entries^'+i]=20+i;}
 for(let i=1;i<=32;i++) {saved['global.acid_rain_severe_cell_front_entries^'+i]=(i%3)+1;saved['global.acid_rain_severe_cell_end_entries^'+i]=101;saved['global.acid_rain_severe_cell_target_count_entries^'+i]=1;}
 const c=ctx(saved);c.flags.add('acid_rain_runtime_active');c.t.set('break',1);
 if(seedPrivate) for(const name of ['acid_rain_gui_region_facts_regions_break','acid_rain_gui_region_facts_fronts_break','acid_rain_gui_region_facts_severe_break','acid_rain_gui_front_1_severe_break','acid_rain_gui_front_2_severe_break','acid_rain_gui_front_3_severe_break'])c.t.set(name,1);
 run(b.defs.get('acid_rain_gui_project_region_facts'),c,b);
 for(let i=1;i<=3;i++)run(b.defs.get('acid_rain_gui_project_front_'+i),c,b);
 const firstVisits=c.visits.length;
 run(b.defs.get('acid_rain_gui_project_region_facts'),c,b);
 for(let i=1;i<=3;i++)run(b.defs.get('acid_rain_gui_project_front_'+i),c,b);
 return {firstVisits,secondVisits:c.visits.length-firstVisits,counts:[1,2,3].map(i=>num('global.acid_rain_gui_front_'+i+'_severe_state_count',c)),eligible:[1,2,3,4,5,6,7].map(i=>num('global.acid_rain_gui_region_eligible_entries^'+i,c)),breakValue:num('break',c)};
}
record('loop baseline inherited-break negative',traversal(before).firstVisits,0);
for(const seed of [false,true]) {
 const actual=traversal(selected,seed);
 record('loop '+stage+' inherited/private/repeat '+seed,actual,stage==='before'?{firstVisits:0,secondVisits:0,counts:[0,0,0],eligible:[0,0,0,0,0,0,0],breakValue:1}:{firstVisits:202,secondVisits:202,counts:[10,11,11],eligible:[101,102,103,104,105,106,107],breakValue:1});
}
const fixtures=JSON.parse(read(base+'phase_fixtures.json')).fixtures;
assert.ok(fixtures,'fixture shape');
const projectionFixtures={};
for(const phase of ['regional_one','regional_two','regional_three','global','aftercare_static','global_static','regional_two_static']) {
 const fixture=structuredClone(fixtures[phase]);assert.ok(fixture);
 if(phase.startsWith('regional')) for(let i=1;i<=3;i++) {
  const prefix='global.acid_rain_gui_front_'+i+'_';
  if(fixture.variables[prefix+'visible']) {
   const result=front(selected,i,fixture.variables[prefix+'region'],fixture.variables[prefix+'warning']?1:2);
   for(const [k,v] of Object.entries({marker_x:result.x,marker_y:result.y})) {fixture.variables[prefix+k]=v;fixture.values[prefix+k]=v;}
  }
 }
 if(phase==='global'||phase==='global_static'||phase==='aftercare_static') {
  const projected=storms(selected,[1,1,5],[0,1,1],phase==='aftercare_static'?0:1);
  for(let i=1;i<=3;i++) {
   const prefix='global.acid_rain_gui_superstorm_'+i+'_';
   const [marker,x,y]=projected.markers[i-1];
   for(const[k,v]of Object.entries({marker,marker_x:x,marker_y:y,region:num(prefix+'region',projected.c)})){fixture.variables[prefix+k]=v;fixture.values[prefix+k]=v;}
  }
 }
 const status=phase.startsWith('global')?3:phase==='aftercare_static'?0:2;
 const rc=regionCtx(1,status),pc=ctx();
 rc.g.set('global.acid_rain_gui_region_eligible_entries^1',fixture.variables['global.acid_rain_gui_region_1_eligible']);
 rc.g.set('global.acid_rain_gui_region_touched_entries^1',fixture.variables['global.acid_rain_gui_region_1_touched']);
 rc.g.set('global.acid_rain_gui_region_untouched_entries^1',fixture.variables['global.acid_rain_gui_region_1_eligible']-fixture.variables['global.acid_rain_gui_region_1_touched']);
 rc.g.set('global.acid_rain_gui_region_front_entries^1',phase.startsWith('regional')?1:0);
 rc.g.set('global.acid_rain_gui_region_active_entries^1',fixture.variables['global.acid_rain_gui_front_1_active_states']);
 rc.g.set('global.acid_rain_gui_region_severe_entries^1',fixture.variables['global.acid_rain_gui_front_1_severe_state_count']);
 pc.c.set('acid_rain_preparedness',fixture.variables.acid_rain_preparedness);
 prepNames.forEach(n=>pc.c.set('acid_rain_'+n+'_tier',fixture.variables['acid_rain_'+n+'_tier']));
 fixture.values['This.GetAcidRainRegion1Tooltip']=getter('GetAcidRainRegion1Tooltip',rc,selected);
 fixture.values['This.GetAcidRainPreparednessTooltip']=getter('GetAcidRainPreparednessTooltip',pc,selected);
 projectionFixtures[phase]=fixture;
}
module.exports={before,current,ctx,run,helper,getter,val,num,storms,fixtures,sha};
if(require.main===module)console.log(JSON.stringify({stage,hashes:{guiEffects:sha(selected.guiPath),scriptedLoc:sha(selected.slPath),triggers:sha(triggersPath),constants:sha('common/script_constants/033_acid_rain_constants.txt'),localisation:sha('localisation/english/033_acid_rain_l_english.yml')},caseCount:results.length,results,projectionFixtures,limits:['Conservative source-frame model, not native execution','Front projectors executed complete real bodies; date conversion stub uses fixture-relative days','Superstorm replay executes exact refresh reset-and-three-call tail plus complete marker/anchor bodies, not full refresh prefix','Region and Preparedness getters/loaders/text selectors executed from actual source; fixture facts are declared synthetic inputs','No campaign producers, gameplay costs, callbacks, pointer lifecycle, save/load or native tooltip engine were executed']}));

