// Actual incubation/activation/tick source with eager numeric meta arguments.
// Conservative helper frames retained. Native event requests are captured only.
// Run: node docs/testing/2026-10-07_biological_incubation_timing_source_tests.js
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const {VM:BaseVM,S,parse,root,definitions,constants,ticks}=require('../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const dir='docs/testing/2026-10-07_biological_incubation_timing/',file='common/scripted_effects/biological_lifecycle_effects.txt',events='events/biological_lifecycle_events.txt',tuning='common/script_constants/biological_lifecycle_constants.txt';
const queue='bio_lifecycle_queue_incubation_event_internal',scheduler='bio_lifecycle_schedule_incubation_for_current_agent',getter='bio_lifecycle_prepare_incubation_delay',activation='bio_lifecycle_activate_current_agent',tick='bio_lifecycle_schedule_tick_for_current_agent';
const sourceBytes=new Map(),parsed=new Map(),hash=b=>crypto.createHash('sha256').update(b).digest('hex'),norm=s=>s.replace(/\r\n/g,'\n');
const read=f=>{if(!sourceBytes.has(f))sourceBytes.set(f,fs.readFileSync(path.join(root,f)));return sourceBytes.get(f).toString('utf8');};
const tree=f=>{if(!parsed.has(f))parsed.set(f,parse(read(f)));return parsed.get(f);};
const def=(ns,key)=>{const n=ns.find(n=>n.key===key);assert(n,key);return n.value;},walk=ns=>ns.flatMap(n=>[n,...(Array.isArray(n.value)?walk(n.value):[])]);
read('docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
read('docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-07_biological_incubation_timing_review.md');
const manifest=JSON.parse(read(dir+'baseline_manifest.json'));
const patchManifest=JSON.parse(read(dir+'patch_manifest.json'));
// Only the existing simple numeric categories required by these four helpers.
for(const name of ['bio_lifecycle_math','bio_lifecycle_agent','bio_lifecycle_schedule','bio_lifecycle_stage']){const text=read(tuning),block=text.match(new RegExp('^'+name+' = \\{[\\s\\S]*?^\\}','m'));assert(block,name);const category=parse(block[0])[0];for(const n of category.value)if(typeof n.value==='string'&&/^-?\d+(\.\d+)?$/.test(n.value))constants.set('constant:'+name+'.'+n.key,ticks(n.value));}
const old=tree(dir+'before/'+file),current=tree(file),entries=tree(events),agentNames=['anthrax','plague','tularemia','smallpox'],cases=[];
const decode=x=>Number(x)/Number(S),constant=k=>constants.get('constant:bio_lifecycle_schedule.'+k);
function load(stage){for(const name of [scheduler,getter,activation,tick,...(stage==='after'?[queue]:[])])definitions.set(name,def(stage==='before'?old:current,name));
 for(const name of ['bio_lifecycle_mark_current_agent_detected','bio_lifecycle_attempt_detection_for_current_agent','bio_lifecycle_refresh_state_modifiers','bio_lifecycle_update_current_agent_air_contribution_from_slot'])definitions.set(name,parse('timing_hook = '+name));
}
class VM extends BaseVM{
 constructor({day=100,roll=0,state=100}={}){super();this.day=ticks(day);this.roll=ticks(roll);this.scope=state;this.states=new Map([[state,this.regularVars]]);this.stateFlags=new Map([[state,new Set()]]);this.draws=0;this.requests=[];this.hooks=[];this.metaArguments=[];}
 stateFlagSet(){return this.stateFlags.get(this.scope);}
 value(token){if(token==='global.num_days')return this.day;return super.value(token);}
 select(agent){this.write('bio_active_agent',ticks(agent));return this;}
 eval(nodes){let chunk=[];const flush=()=>{if(!chunk.length)return true;const ns=chunk;chunk=[];return super.eval(ns);};
  for(const n of nodes){const k=n.key,v=n.value;if(!['has_state_flag','set_state_flag','clr_state_flag','meta_effect','state_event','set_temp_variable_to_random','round_temp_variable','clamp_temp_variable','add_to_variable','timing_hook'].includes(k)){chunk.push(n);continue;}if(!flush())return false;
   if(k==='has_state_flag'){if(!this.stateFlagSet().has(v))return false;}
   else if(k==='set_state_flag')this.stateFlagSet().add(v);
   else if(k==='clr_state_flag')this.stateFlagSet().delete(v);
   else if(k==='set_temp_variable_to_random'){assert(this.roll>=0n&&this.roll<=S);this.draws++;this.write(this.field(v,'var'),this.roll);}
   else if(k==='round_temp_variable'){const a=this.value(v);assert(a>=0n);this.write(v,((a+S/2n)/S)*S);}
   else if(k==='clamp_temp_variable'){const key=this.field(v,'var'),lo=this.field(v,'min'),hi=this.field(v,'max');let a=this.value(key);if(lo!==undefined&&a<this.value(lo))a=this.value(lo);if(hi!==undefined&&a>this.value(hi))a=this.value(hi);this.write(key,a);}
   else if(k==='add_to_variable'){const name=this.field(v,'var')||v[0].key,amount=this.value(this.field(v,'value')||v[0].value);this.write(name,this.value(name)+amount,false);}
   else if(k==='meta_effect'){
    const args={};for(const n of v.filter(n=>n.key!=='text')){const match=n.value.match(/^"\[\?([^|\]]+)\|\.0\]"$/);assert(match,n.value);const value=this.value(match[1]);assert.equal(value%S,0n,'integer meta field');args[n.key]=String(value/S);}
    const replace=s=>typeof s==='string'?s.replace(/\[([^\]]+)\]/g,(_,key)=>{assert(Object.hasOwn(args,key),key);return args[key];}):s;
    const expand=ns=>ns.map(n=>({...n,key:replace(n.key),value:Array.isArray(n.value)?expand(n.value):replace(n.value)}));this.metaArguments.push({scope:this.scope,args});if(!this.eval(expand(this.field(v,'text'))))return false;
   }else if(k==='state_event'){
    const id=this.field(v,'id'),days=this.field(v,'days');assert(/^\d+$/.test(days),'queued delay is a literal integer');this.requests.push({scope:this.scope,id,delay:Number(days),atDay:decode(this.day),activeAgent:decode(this.value('bio_active_agent')),getterDelay:decode(this.value('bio_incubation_days'))});
   }else if(k==='timing_hook')this.hooks.push({hook:v,scope:this.scope,agent:decode(this.value('bio_active_agent'))});
  }return flush();
 }
}
function test(id,fn){try{const detail=fn();cases.push({id,status:'passed',...detail});}catch(e){cases.push({id,status:'failed',error:e.message});}}
function scheduled(vm,agent){return vm.stateFlagSet().has('bio_agent_'+agent+'_incubation_scheduled');}
const callback=agent=>def(entries.find(n=>n.key==='state_event'&&n.value.some(v=>v.key==='id'&&v.value==='cbrn_bio_lifecycle.'+agent)).value,'immediate');
test('raw before hashes and normalized frozen-after current equality',()=>{for(const f of manifest.files){const before=dir+'before/'+f.path,after=dir+'after/'+f.path;assert.equal(hash(Buffer.from(read(before))),f.sha256);assert.equal(norm(read(f.path)),norm(read(after)),'substantive frozen-source drift');assert.equal(hash(sourceBytes.get(after)),f.path===file?patchManifest.afterSha256:f.sha256);if(f.path!==file)assert.equal(norm(read(f.path)),norm(read(before)),'unrelated source changed');}});
test('only new queue helper and two intended scheduler edits alter source AST',()=>{
 assert.equal(current.filter(n=>n.key===queue).length,1);const expected=structuredClone(old),sched=def(expected,scheduler),meta=sched.find(n=>n.key==='meta_effect');
 const premature=walk(meta.value).filter(n=>n.key==='state_event');assert.equal(premature.length,1);premature[0].key=queue;premature[0].value='yes';assert.equal(meta.value.filter(n=>n.key==='BIO_INCUBATION_DAYS').length,1);meta.value=meta.value.filter(n=>n.key!=='BIO_INCUBATION_DAYS');
 assert.deepEqual(current.filter(n=>n.key!==queue),expected);
 const body=def(current,queue);assert.equal(body.length,1);assert.equal(body[0].key,'meta_effect');const m=body[0].value,text=def(m,'text');assert.equal(text.length,1);assert.equal(text[0].key,'state_event');assert.equal(m.filter(n=>n.key!=='text').length,2);
 const args=new Map(m.filter(n=>n.key!=='text').map(n=>[n.value,n.key]));assert(args.has('"[?bio_active_agent|.0]"'));assert(args.has('"[?bio_incubation_days|.0]"'));assert.equal(def(text[0].value,'id'),'cbrn_bio_lifecycle.['+args.get('"[?bio_active_agent|.0]"')+']');assert.equal(def(text[0].value,'days'),'['+args.get('"[?bio_incubation_days|.0]"')+']');
 return{helper:queue,getterAndActivationAndTickUnchanged:true,queueDrawsOrFlagsAdded:false};
});
for(let agent=1;agent<=4;agent++)for(const roll of [0,0.5,1])test('agent-'+agent+'-roll-'+roll,()=>{
 const name=agentNames[agent-1],startDay=100,base=constant('incubation_'+name+'_days'),range=constant('incubation_'+name+'_random_days'),minimum=constant('minimum_event_delay_days'),raw=base+ticks(roll)*range/S,rounded=((raw+S/2n)/S)*S,expected=rounded<minimum?minimum:rounded;
 load('after');const vm=new VM({day:startDay,roll}).select(agent);vm.stateFlagSet().add('bio_agent_'+agent+'_incubating');assert(vm.run(scheduler));assert.equal(vm.draws,1);assert.equal(vm.requests.length,1);assert.equal(vm.requests[0].id,'cbrn_bio_lifecycle.'+agent);assert.equal(vm.requests[0].delay,decode(expected));assert.equal(vm.requests[0].getterDelay,decode(expected));const due=vm.regularVars.get('bio_agent_'+agent+'_incubation_due_day');assert.equal(due,ticks(startDay)+expected);assert(scheduled(vm,agent));
 // Repeated scheduling preserves the original draw, queue, and due date.
 vm.day+=ticks(1);vm.roll=ticks(1-roll);assert(vm.run(scheduler));assert.equal(vm.draws,1);assert.equal(vm.requests.length,1);assert.equal(vm.regularVars.get('bio_agent_'+agent+'_incubation_due_day'),due);
 // Invoke the real event-entry and real activation guard before/exactly at due.
 vm.day=due-1n;assert(vm.eval(callback(agent)));assert(scheduled(vm,agent));assert(vm.stateFlagSet().has('bio_agent_'+agent+'_incubating'));assert.equal(vm.requests.length,1);vm.day=due;assert(vm.eval(callback(agent)));assert(!scheduled(vm,agent));assert(!vm.stateFlagSet().has('bio_agent_'+agent+'_incubating'));assert(vm.stateFlagSet().has('bio_agent_'+agent+'_active'));assert.equal(vm.requests.length,2);assert.equal(vm.requests[1].id,'cbrn_bio_lifecycle.'+(10+agent));assert.equal(vm.requests[1].delay,decode(constant('weekly_tick_days')));assert.equal(vm.regularVars.get('bio_agent_'+agent+'_tick_due_day'),due+constant('weekly_tick_days'));
 assert(vm.eval(callback(agent)));assert.equal(vm.requests.length,2);assert.equal(vm.draws,1);
 // Before source captures zero, then computes a future due day. An immediate
 // callback fails the real guard and leaves incubation marked as scheduled.
 load('before');const prior=new VM({day:startDay,roll}).select(agent);prior.stateFlagSet().add('bio_agent_'+agent+'_incubating');assert(prior.run(scheduler));assert.equal(prior.requests[0].delay,0);assert.equal(prior.regularVars.get('bio_agent_'+agent+'_incubation_due_day'),ticks(startDay)+expected);assert(prior.eval(callback(agent)));assert(scheduled(prior,agent));assert(prior.stateFlagSet().has('bio_agent_'+agent+'_incubating'));assert.equal(prior.requests.length,1);
 return{agent,name,roll,expectedDelay:decode(expected),afterRequests:vm.requests,beforeRequest:prior.requests[0],baselineEarlyCallbackStranded:true,repeatedSchedulerNoDraw:true,duplicateActivationNoTick:true};
});
for(let agent=1;agent<=4;agent++)test('absent-incubating-'+agent,()=>{load('after');const vm=new VM().select(agent);assert(vm.run(scheduler));assert.equal(vm.draws,0);assert.equal(vm.requests.length,0);assert(!vm.regularVars.has('bio_agent_'+agent+'_incubation_due_day'));return{noDraw:true,noQueue:true};});
test('two agents in one state keep independent due fields flags and event IDs',()=>{
 load('after');const vm=new VM({day:40,roll:0});vm.stateFlagSet().add('bio_agent_1_incubating');vm.stateFlagSet().add('bio_agent_4_incubating');vm.select(1);assert(vm.run(scheduler));const firstDue=vm.regularVars.get('bio_agent_1_incubation_due_day');vm.select(4);vm.roll=ticks(1);assert(vm.run(scheduler));const secondDue=vm.regularVars.get('bio_agent_4_incubation_due_day');assert.equal(vm.draws,2);assert.equal(vm.requests.length,2);assert.deepEqual(vm.requests.map(r=>r.id),['cbrn_bio_lifecycle.1','cbrn_bio_lifecycle.4']);assert.equal(firstDue,ticks(45));assert.equal(secondDue,ticks(61));
 vm.day=firstDue;assert(vm.eval(callback(1)));assert(vm.stateFlagSet().has('bio_agent_1_active'));assert(vm.stateFlagSet().has('bio_agent_4_incubating'));assert(scheduled(vm,4));assert.equal(vm.regularVars.get('bio_agent_4_incubation_due_day'),secondDue);vm.day=secondDue;assert(vm.eval(callback(4)));assert(vm.stateFlagSet().has('bio_agent_4_active'));assert.deepEqual(vm.requests.map(r=>r.id),['cbrn_bio_lifecycle.1','cbrn_bio_lifecycle.4','cbrn_bio_lifecycle.11','cbrn_bio_lifecycle.14']);return{firstDue:decode(firstDue),secondDue:decode(secondDue),requests:vm.requests};
});
test('audited inputs stable through run',()=>{for(const[f,b]of sourceBytes)assert.equal(hash(fs.readFileSync(path.join(root,f))),hash(b),f);});
const refs=[['installed','C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md',4833,4852],['installed','C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md',8096,8128],['wiki',path.join(root,'paradox_wiki/Effects - Hearts of Iron 4 Wiki.md'),4617,4682]].map(([kind,p,startLine,endLine])=>({kind,path:p,startLine,endLine,revision:hash(fs.readFileSync(p))}));
const result={status:cases.some(c=>c.status==='failed')?'failed':'passed_bounded_incubation_timing_source_model',command:'node docs/testing/2026-10-07_biological_incubation_timing_source_tests.js',timestamp:new Date().toISOString(),cases:cases.length,results:cases,sourceHashes:Object.fromEntries([...sourceBytes].map(([f,b])=>[f,hash(b)])),references:refs,limits:[
 'Uses the existing unchanged strict-frame VM/parser. Numeric meta arguments are evaluated eagerly when each actual meta node runs, matching the reviewed source contract. Native meta/event execution is not simulated.',
 'RNG returns deterministic0,0.5,1 fixtures, exercising minimum/midpoint/upper sample boundaries without claiming engine distributions or endpoint reachability. Rounding uses positive half-up to integer, followed by actual source minimum clamp.',
 'Actual getter, scheduler, new queue helper, activation, existing tick scheduler and activation event entries are evaluated. Detection, state-modifier and air hooks are explicit captured no-op stubs.',
 'State flags and regular due fields are scoped to one exact fixture state. Both agents in the shared-state case retain separate keyed records. Scheduled requests are captured, and callbacks are invoked manually at selected days.',
 'Weekly tick IDs/delays and due fields are checked. Actual tick effects, mortality, protection, spread, native callback timing/cardinality and real event queues remain outside scope.',
 'The repair prevents newly queued zero-delay activation under this source model. No recovery for a previously stranded record is introduced or validated.',
 'Current source equality to frozen raw after archives tolerates only CRLF-to-LF conversion. Raw before hashes and complete source AST comparison preserve the intended scope.',
 'No gameplay, old raid tests/archives, shared VM, probability/MCP call, game launch, log search, staging or commit was performed.'
]};
fs.writeFileSync(path.join(__dirname,'2026-10-07_biological_incubation_timing_source_results.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({status:result.status,cases:result.cases,failed:cases.filter(c=>c.status==='failed')},null,2));if(cases.some(c=>c.status==='failed'))process.exitCode=1;
