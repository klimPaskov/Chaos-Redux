/* Event 012 F1 production caller tests. SourceNoNativeProof.
 * Run: node .tools/validation/test_012_gods_industry_integration.js [--evidence]
 * All industrial money/day arithmetic comes from production ASTs. Native
 * presence/timer models never establish actual refresh, expiry or repair.
 * Import has no writes. --evidence writes only the task-owned evidence folder.
 */
'use strict';
const fs = require('node:fs'), path = require('node:path'), crypto = require('node:crypto');
const assert = require('node:assert/strict');
const h = require('./test_012_gods_industry_helpers');
const {parse} = require('../../docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03');
const {VM, effects, triggers, constants, fixed, country, state, P, R, root} = h;
const G = 'gods_of_africa_';
const evidenceDir = 'docs/plans/012_africa_plans/subagent_handoffs/own_evidence/012_gods_industry_integration_2026-10-09';
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const sources = new Map(), asts = new Map();
function load(p) { const bytes=fs.readFileSync(path.join(root,p));sources.set(p,bytes);const ast=parse(bytes.toString('utf8'));asts.set(p,ast);return ast; }
const effectFiles = ['industry_effects','industry_integration_effects','effects','contract_effects','report_effects','epoch_binding_effects','instalment_effects','lifecycle_effects','public_values_effects','mobile_contract_effects','settlement_effects','recovery_effects','equipment_effects'];
const triggerFiles = ['industry_triggers','industry_integration_triggers','triggers','contract_triggers','epoch_binding_triggers','protection_eligibility_triggers'];
for(const f of effectFiles) for(const n of load('common/scripted_effects/012_africa_gods_'+f+'.txt')) effects[n.key]=n.value;
for(const f of triggerFiles) for(const n of load('common/scripted_triggers/012_africa_gods_'+f+'.txt')) triggers[n.key]=n.value;
// The new normal-settlement cleanup remains actual production code.
const strengthCleanupOwner = load('common/scripted_effects/012_africa_gods_strength_inputs_effects.txt').find(n => n.key === G + 'clear_strength_input_sample');
assert.ok(strengthCleanupOwner); effects[strengthCleanupOwner.key] = strengthCleanupOwner.value;
for(const f of ['012_africa_gods_constants','012_africa_gods_industry_constants','012_africa_constants','012_africa_gods_contract_constants','012_africa_event_log_constants','012_africa_gods_contribution_constants']) {
	for(const cat of load('common/script_constants/'+f+'.txt')) for(const n of cat.value) if(typeof n.value==='string'&&Number.isFinite(Number(n.value)))constants[cat.key+'.'+n.key]=Number(n.value);
}
load('common/decisions/012_africa_gods_decisions.txt');
load('common/scripted_localisation/012_africa_gods_scripted_localisation.txt');
load('localisation/english/012_africa_gods_l_english.yml');
load('common/scripted_localisation/012_africa_gods_industry_scripted_localisation.txt');
load('localisation/english/012_africa_gods_industry_l_english.yml');
load('common/dynamic_modifiers/012_africa_gods_industry_modifiers.txt');
const controlChangeEffect = blockAction(load('common/on_actions/012_africa_gods_industry_on_actions.txt'));
function blockAction(ast) {
	const get=(nodes,key)=>{const found=nodes.filter(n=>n.key===key);assert.equal(found.length,1,'unique callback '+key);return found[0].value;};
	return get(get(get(ast,'on_actions'),'on_state_control_changed'),'effect');
}
const walk = nodes => nodes.flatMap(n=>[n,...(Array.isArray(n.value)?walk(n.value):[])]);
const block = (nodes,key) => {const ns=nodes.filter(n=>n.key===key);assert.equal(ns.length,1,key);return ns[0].value;};
const has = (node,key) => walk([node]).some(n=>n.key===key);

// Existing campaign authorization inputs. Local financial ledger, owner tuple,
// receiver, capacity, quote, payment, closure and report bodies are NOT mocked.
const authorization = new Map([
	['africa_is_current_host',true], [G+'participant_generation_is_current',true],
	[G+'participant_epoch_is_current',true], [G+'epoch_permission_is_current',true],
	[G+'demand_contract_is_current',true], [G+'demand_contract_can_resolve',true],
	[G+'demand_epoch_is_current',true], [G+'participant_can_receive_demand',true],
	[G+'participant_is_losing_war',false], [G+'participant_is_at_war_elsewhere',false],
	[G+'participant_is_near_capitulation',false], [G+'demand_transfer_is_clear',true],
	[G+'frozen_territory_is_lost',false], [G+'armor_capacity_is_sufficient',false],
	[G+'family_transfer_is_clear',true], [G+'substitute_transfer_is_clear',true],
	[G+'authority_owner_object_is_current',true], [G+'continent_is_secured',true],
	[G+'participant_can_register',true], [G+'active_host_is_valid',false],
	[G+'participant_has_settlement_history',true], [G+'final_settlement_value_is_valid',true],
	[G+'has_current_host',true]
]);
// Exact out-of-scope consumers, never an unknown-helper fallback.
const consumerBoundaries = new Set([
	G+'build_mobile_need_profile',
	G+'freeze_contract_emergency_proof',G+'remember_demand_repetition',
	G+'freeze_demand_burden',G+'build_substitute_set',G+'record_milestone',
	G+'clear_contract_emergency_proof',G+'clear_mobile_quote',G+'clear_instalment_terms',
	G+'clear_substitute_slots',G+'achievement_record_provision',
	G+'observe_public_wrath_commit',G+'observe_public_wrath',G+'clear_public_wrath_values',
	G+'refresh_strength',G+'clear_response_view',G+'clear_public_strength_observation',
	G+'settlement_classify_participant',G+'initialize_settlement_obligation',
	G+'initialize_settlement_delivery',G+'deliver_settlement_obligations',
	G+'remember_candidate',G+'withdraw_protection_package',G+'clear_council_pledge',
	G+'clear_final_ultimatum',G+'refresh_participant_floors',G+'achievement_complete_survive_defiance',
	G+'observe_public_strength',G+'reset_public_strength_values'
]);
const executed = new Set(), usedBoundaries = new Set();
for(const name of authorization.keys()) if(!Object.hasOwn(triggers,name))triggers[name]=[];
for(const name of [...consumerBoundaries,G+'begin_payment_receipt',G+'complete_payment_receipt',G+'sync_demand_mission_timeout',G+'revoke_current_epoch']) if(!Object.hasOwn(effects,name))effects[name]=[];
class IntegrationVM extends VM {
	constructor() {
		super();this.host.name='original African host';this.actor.name='donor';this.site.name='frozen repair state';
		for(const o of this.objects)o.arrays={};this.calls=[];this.events=[];this.missions=new Set();this.missionWrites=[];
		this.authInputs=new Map(authorization);this.globalFlags=new Set();this.trace=[];this.failBinding=false;this.beforeBalance=null;this.materialLimit=Infinity;
		this.host.vars[G+'active_demand_count']=0;this.host.vars[G+'demand_sequence']=10;
		Object.assign(this.actor.vars,{[G+'history_owner_id']:this.actor.id,[G+'history_origin_host_id']:1,[G+'participant_authority_epoch']:1,[G+'wrath']:25});
		for(const f of ['history_initialized','contract_history_initialized'])this.actor.flags.add(G+f);
		this.targets[G+'demand_participant']=this.actor;
	}
	// Native callback bindings stay independent of PREV scope transitions.
	// ROOT = new controller, FROM = old controller, FROM.FROM = changed state.
	ctx(scope,prev=null,rootScope=scope,fromChain=prev?.fromChain||[]) {
		return {...super.ctx(scope,prev,rootScope),fromChain};
	}
	scope(token,c) {
		if(/^FROM(?:\.FROM)*$/.test(token))return c.fromChain[token.split('.').length-1];
		return super.scope(token,c);
	}
	call(name,c,trigger=false) {
		this.calls.push({name,scope:c.scope.name||c.scope.type,root:c.root.name,prev:c.prev?.scope.name});
		if(trigger&&this.authInputs.has(name)){usedBoundaries.add(name);return this.auth&&this.authInputs.get(name);}
		if(!trigger&&consumerBoundaries.has(name)){usedBoundaries.add(name);return;}
		if(!trigger&&name===G+'begin_payment_receipt'){usedBoundaries.add(name);c.scope.flags.add(G+'material_transfer_begin_ready');return;}
		if(!trigger&&name===G+'complete_payment_receipt'){usedBoundaries.add(name);assert(this.materialMoved>0);c.scope.vars[G+'payment_delivered']=this.materialMoved;c.scope.vars[G+'payment_received']=this.materialMoved;return;}
		if(!trigger&&name===G+'sync_demand_mission_timeout'){usedBoundaries.add(name);this.missionWrites.push({kind:'sync',deadline:c.scope.vars[G+'demand_deadline']});return;}
		if(!trigger&&name===G+'revoke_current_epoch'){usedBoundaries.add(name);this.auth=false;this.trace.push({revoke:true,nativeWrites:this.nativeWrites.length,retirementPublished:this.actor.vars[G+'last_industry_retired_contract_id']});return;}
		assert(Object.hasOwn(trigger?triggers:effects,name),'Unknown production helper '+name);
		executed.add(name);
		if(!trigger&&name===G+'review_industry_program')this.trace.push({review:true,scope:c.scope.name,cppWrites:this.moneyWrites.length});
		if(!trigger&&name===G+'bind_industry_terms'&&this.failBinding)this.site.damage=0;
		if(!trigger&&name===G+'apply_partial_delivery'&&this.beforeBalance){const fn=this.beforeBalance;this.beforeBalance=null;fn();}
		return super.call(name,c,trigger);
	}
	value(token,c) {
		if(token===undefined)throw Error('Missing value token');
		const from=/^(FROM(?:\.FROM)*)(?:\.(.+))?$/.exec(token);
		if(from){const s=this.scope(from[1],c);assert(s&&typeof s==='object','Unbound native callback scope '+from[1]);return from[2]?this.value(from[2],this.ctx(s,c,c.root)):s;}
		if(token.includes('.')&&/^(ROOT|THIS|PREV)\./.test(token)) {
			const [head,...tail]=token.split('.'); const s=this.scope(head,c);assert(s&&typeof s==='object','Opaque scope required '+head);
			return this.value(tail.join('.'),this.ctx(s,c,c.root));
		}
		if(token.startsWith('event_target:')&&token.includes('.')){const dot=token.indexOf('.'),s=this.scope(token.slice(0,dot),c);return s?this.value(token.slice(dot+1),this.ctx(s,c,c.root)):0;}
		if(token.endsWith('^num'))return c.scope.arrays[token.slice(0,-4)]?.length||0;
		if(token==='max_fuel_k')return c.scope.maxFuel||100;
		if(token==='fuel_k')return c.scope.fuel||0;
		return super.value(token,c);
	}
	variable(n,c) {
		if(n.key.startsWith('clamp')) {
			const b=Object.fromEntries(n.value.map(x=>[x.key,x.value]));const store=n.key.includes('temp_variable')?this.temp:c.scope.vars;
			store[b.var]=Math.min(b.max===undefined?Infinity:this.value(b.max,c),Math.max(b.min===undefined?-Infinity:this.value(b.min,c),store[b.var]??0));return;
		}
		return super.variable(n,c);
	}
	test(nodes,c,mode='AND') {
		assert(Array.isArray(nodes),'Missing trigger body');
		const mapped=nodes.map(n=>{
			if(['custom_trigger_tooltip','hidden_trigger'].includes(n.key))return {key:'AND',op:'=',value:n.value.filter(x=>x.key!=='tooltip')};
			let v;
		if(n.key==='has_global_flag')v=this.globalFlags.has(n.value);
			else if(n.key==='has_war')v=false;
			else if(n.key==='has_war_with'||n.key==='has_offensive_war_with')v=false;
			else if(n.key==='has_active_mission')v=this.missions.has(n.value);
			else if(n.key==='any_controlled_state')v=(c.scope.states||[]).filter(s=>s.controller===c.scope).some(s=>this.test(n.value,this.ctx(s,c,c.root)));
			else if(n.key==='is_major')v=false;
			else if(n.key==='has_fuel')v=this.cmp(c.scope.fuel||0,this.value(n.value,c),n.op);
			else if(n.key==='has_equipment'){const e=n.value[0];v=this.cmp(c.scope.equipment||10000,this.value(e.value,c),e.op);}
			else if(n.key==='is_in_array'){const b=Object.fromEntries(n.value.map(x=>[x.key,x.value]));v=(c.scope.arrays[b.array]||[]).includes(this.value(b.value,c));}
			else if(n.key.startsWith('var:')&&Array.isArray(n.value)&&!this.scope(n.key,c))v=false;
			if(v!==undefined)return v?{key:'AND',value:[]}:{key:'NOT',value:[]};
			return n;
		});
		return super.test(mapped,c,mode);
	}
	exec(nodes,c) {
		for(let i=0;i<nodes.length;i++) {
			const n=nodes[i],b=Array.isArray(n.value)?Object.fromEntries(n.value.map(x=>[x.key,x.value])):{};
			if(n.key==='if'){const chain=[n];while(['else_if','else'].includes(nodes[i+1]?.key))chain.push(nodes[++i]);super.exec(chain,c);continue;}
			if(n.key==='save_event_target_as'){this.targets[n.value]=c.scope;continue;}
			if(n.key==='activate_mission'||n.key==='remove_mission'){this.missionWrites.push({kind:n.key,id:n.value,slot:this.host.vars[G+'active_demand_count']});if(n.key==='activate_mission')this.missions.add(n.value);else this.missions.delete(n.value);continue;}
			if(n.key==='country_event'){this.events.push(b.id);continue;}
			if(n.key==='add_opinion_modifier'){this.trace.push({opinion:true,scope:c.scope.name});continue;}
			if(n.key==='add_to_array'){(c.scope.arrays[b.array]||=([])).push(this.value(b.value,c));continue;}
			if(n.key==='clear_array'){c.scope.arrays[n.value]=[];continue;}
			if(n.key==='remove_from_array'){c.scope.arrays[b.array]=(c.scope.arrays[b.array]||[]).filter(x=>x!==this.value(b.value,c));continue;}
			if(n.key==='for_each_scope_loop'){const stop=b.break||'break';for(const s of c.scope.arrays[b.array]||[]){if(this.value(stop,c)!==0)break;this.exec(n.value.filter(x=>!['array','break','tooltip'].includes(x.key)),this.ctx(s,c,c.root));}continue;}
			if(n.key==='send_equipment'){this.materialMoved=Math.min(this.value(b.amount,c),this.materialLimit);this.trace.push({material:this.materialMoved,equipment:b.equipment});continue;}
			if(n.key==='round_variable'){c.scope.vars[n.value]=Math.round(c.scope.vars[n.value]);continue;}
			if(n.key.startsWith('var:')&&Array.isArray(n.value)&&!this.scope(n.key,c))continue;
			super.exec([n],c);
		}
	}
	create(q=20) {
		for(const k of Object.keys(this.actor.vars))if(k.startsWith(G+'demand_'))delete this.actor.vars[k];
		Object.assign(this.host.vars,{[G+'selected_family']:constants['gods_of_africa_demand_family.industry_repair'],[G+'contract_amount']:q,[G+'contract_deadline']:this.day+45,[G+'contract_band']:1});
		Object.assign(this.actor.vars,{[G+'payment_family']:constants['gods_of_africa_demand_family.industry_repair'],[G+'payment_amount']:q});
		this.run('set_payment_capacity_requirement');this.run('prepare_industry_candidate',this.host);this.run('create_demand_contract',this.host);
	}
	partial(){this.run('resolve_partial_compliance');}
	full(){this.run('resolve_full_compliance');}
	nativeIndustryEnable(sourceCountry=this.host,rootState=this.site) {
		const ast=asts.get('common/dynamic_modifiers/012_africa_gods_industry_modifiers.txt');
		return this.test(block(block(ast,G+'industry_repair_program'),'enable'),this.ctx(sourceCountry,null,rootState));
	}
	controlChanged(changedState,newController=this.actor,oldController=this.host) {
		const c=this.ctx(newController,null,newController,[oldController,changedState]);
		assert.equal(this.scope('ROOT',c),newController);assert.equal(this.scope('FROM',c),oldController);assert.equal(this.scope('FROM.FROM',c),changedState);
		this.exec(controlChangeEffect,c);
	}
}

function runTests() {
	const results=[],failures=[], observations=[];
	function test(name,fn){try{fn();results.push({name,status:'passed'});}catch(e){failures.push({name,error:e.message,stack:e.stack});console.error('FAIL '+name+': '+e.message);}}
	const fixture=(q=20)=>{const v=new IntegrationVM();v.create(q);assert(v.actor.flags.has(P+'terms_bound'),'integrated bind failed');return v;};
	function selectText(v,name) {
		const defs=[...asts].filter(([p])=>p.includes('/scripted_localisation/')).flatMap(([,a])=>a).filter(n=>n.key==='defined_text'&&n.value.find(x=>x.key==='name')?.value===name);
		assert.equal(defs.length,1,name);const arm=defs[0].value.filter(n=>n.key==='text').find(n=>{const t=n.value.find(x=>x.key==='trigger');return !t||v.test(t.value,v.ctx(v.actor));});
		assert(arm,'No source text branch '+name);return arm.value.find(n=>n.key==='localization_key')?.value;
	}
	test('noSite suppresses actual need and selection',()=>{
		const v=new IntegrationVM();v.site.damage=0;const body=block(effects[G+'build_need_profile'],'if');
		const init=body.find(n=>n.key==='set_variable'&&has(n,G+'need_industry'));const need=body.find(n=>n.key==='if'&&has(n,'africa_central_capacity'));
		assert(init&&need);v.run('prepare_industry_candidate',v.host);v.exec([init,need],v.ctx(v.host));assert.equal(v.host.vars[G+'need_industry'],0);
		const ladder=effects[G+'select_demand_family'];const selection=ladder.find(n=>n.key==='if'&&has(n,G+'industry_offer_is_available'));
		assert(selection);v.host.vars[G+'family_candidate']=constants['gods_of_africa_demand_family.industry_repair'];v.host.vars[G+'candidate_amount']=20;v.exec([selection],v.ctx(v.host));assert(!Object.hasOwn(v.host.vars,G+'selected_family'));assert(!v.host.flags.has(R+'reserved'));
	});
	test('successful create reserves slot1 binds after epoch ledger starts mission603 once',()=>{
		const v=fixture();assert.equal(v.host.vars[G+'active_demand_count'],1);assert.equal(v.actor.vars[G+'demands_issued'],1);assert.equal(v.host.vars[R+'contract_id'],11);
		assert(v.missions.has(G+'demand_mission'));assert.deepEqual(v.events,['chaosx.nr12.603']);assert(v.host.flags.has(G+'first_demand_milestone_emitted'));
		const names=v.calls.map(x=>x.name);assert(names.indexOf(G+'bind_demand_epoch')<names.indexOf(G+'open_contract_ledger'));assert(names.indexOf(G+'open_contract_ledger')<names.indexOf(G+'bind_industry_terms'));assert.equal(v.missionWrites[0].slot,1);
	});
	test('failed bind rolls slot back no mission no first milestone',()=>{const v=new IntegrationVM();v.failBinding=true;v.create();assert.equal(v.host.vars[G+'active_demand_count'],0);assert(!v.actor.flags.has(G+'demand_active'));assert(!v.host.flags.has(G+'first_demand_milestone_emitted'));assert.equal(v.events.length,0);assert.equal(v.actor.vars[G+'demands_retired'],1);assert(!v.host.flags.has(R+'reserved'));});
	test('full20 actual CPP60days one financial fulfillment one compliance',()=>{const v=fixture();v.full();assert.equal(v.actor.pp,80);assert.equal(v.host.pp,120);assert.equal(v.host.vars[R+'funded'],20);assert.equal(v.host.vars[R+'granted_days'],60);assert.equal(v.host.vars[R+'due_day'],160);assert.equal(v.actor.vars[G+'demands_fulfilled'],1);assert.equal(v.actor.vars[G+'compliance_count'],1);assert(v.host.flags.has(R+'closed'));assert.equal(v.actor.vars[G+'last_response_industry_new_days'],60);assert.equal(v.host.vars[G+'active_demand_count'],0);v.full();assert.equal(v.actor.pp,80);assert.equal(v.actor.vars[G+'demands_fulfilled'],1);});
	test('partial10plus10 actual30plus30 remaining only and canonical closure',()=>{const v=fixture();v.partial();assert.equal(v.actor.vars[G+'demand_remaining'],10);assert.equal(v.host.vars[R+'granted_days'],30);assert.equal(v.actor.vars[P+'full_new_days'],30);assert.equal(v.actor.vars[P+'partial_new_days'],30);v.day=v.actor.vars[G+'next_partial_payment_day'];v.partial();assert.equal(v.actor.pp,80);assert.equal(v.host.vars[R+'granted_days'],60);assert.equal(v.actor.vars[G+'demands_fulfilled'],1);assert(v.host.flags.has(R+'closed'));assert.equal(v.actor.vars[G+'partial_count'],2);assert.equal(v.actor.vars[G+'compliance_count'],0);assert(!v.actor.flags.has(G+'reliable_memory_applied'));observations.push({finding:'canonical terminal fulfillment distinct from legacy fullclick counters',canonicalFulfilled:1,coarseCompliance:0,reliableMemory:false});});
	test('expiryGap adds only new30 no whole-term refresh',()=>{const v=fixture();v.partial();v.day=140;v.run('prepare_industry_candidate',v.host);assert(v.host.flags.has(R+'reserved'));v.partial();assert.equal(v.host.vars[R+'granted_days'],60);assert.equal(v.host.vars[R+'due_day'],170);assert.equal(v.nativeWrites.filter(x=>x.action==='add_dynamic_modifier').length,2);});
	test('fractional20point5 cumulative61 actualCPP exact',()=>{const v=fixture(20.5);assert.equal(v.host.vars[R+'service_days'],61);v.partial();assert.equal(v.host.vars[R+'granted_days'],30);assert.equal(v.actor.vars[P+'full_new_days'],31);assert.equal(v.actor.vars[P+'partial_new_days'],31);v.day=v.actor.vars[G+'next_partial_payment_day'];v.full();assert.equal(v.actor.pp,79.5);assert.equal(v.host.vars[R+'granted_days'],61);assert.equal(v.actor.vars[G+'last_response_industry_new_days'],31);});
	test('quote rerender pure gates preserve normal fields and agree paid days',()=>{const v=fixture();const before=structuredClone({vars:v.actor.vars,flags:[...v.actor.flags]});for(let i=0;i<3;i++){assert(v.gate('current_demand_can_be_paid'));assert(v.gate('partial_payment_is_affordable'));assert(v.gate('host_can_receive_demand_payment'));}assert.deepEqual({vars:v.actor.vars,flags:[...v.actor.flags]},before);const quoted=v.actor.vars[P+'partial_new_days'];v.partial();assert.equal(v.actor.vars[G+'last_response_industry_new_days'],quoted);});
	test('replay after delivery before balance consumer blocked no second debit',()=>{const v=fixture();v.beforeBalance=()=>{const n=v.moneyWrites.length,w=v.nativeWrites.length;v.actor.vars[G+'payment_family']=constants['gods_of_africa_demand_family.industry_repair'];v.actor.vars[G+'payment_amount']=10;v.run('pay_industrial_tribute');assert.equal(v.actor.vars[G+'payment_delivered'],0);assert.equal(v.moneyWrites.length,n);assert.equal(v.nativeWrites.length,w);/* restore the first receipt output for its existing owner */v.actor.vars[G+'payment_delivered']=10;};v.partial();assert.equal(v.actor.pp,90);assert.equal(v.actor.vars[G+'demand_remaining'],10);});
	test('CPP floor1 inclusive production capacity and both gates',()=>{for(const [pp,yes]of[[20.99999,false],[21,true],[21.00001,true]]){const v=fixture();v.actor.pp=pp;assert.equal(v.gate('current_demand_can_be_paid'),yes);v.full();assert.equal(v.actor.pp,yes?fixed(pp-20):pp);assert.equal(v.host.vars[R+'funded'],yes?20:0);}for(const [pp,yes]of[[10.99999,false],[11,true]]){const v=fixture();v.actor.pp=pp;assert.equal(v.gate('partial_payment_is_affordable'),yes);v.partial();assert.equal(v.actor.pp,yes?fixed(pp-10):pp);}});
	test('material substitute preserves earlier30days no added industrialCPP service',()=>{const v=fixture();v.partial();const cpp=v.actor.pp,n=v.nativeWrites.length;Object.assign(v.actor.vars,{[G+'substitute_family']:constants['gods_of_africa_demand_family.land_equipment'],[G+'substitute_amount']:100});v.actor.flags.add(G+'substitute_offered');v.run('accept_substitute');assert.equal(v.actor.pp,cpp);assert.equal(v.host.vars[R+'funded'],10);assert.equal(v.host.vars[R+'granted_days'],30);assert.equal(v.host.vars[R+'due_day'],130);assert.equal(v.nativeWrites.length,n);assert.equal(v.actor.vars[G+'demands_honored_substitute'],1);assert(v.host.flags.has(R+'closed'));});
	test('invalid recipient neutral deadline no Wrath or failure',()=>{const v=fixture();v.partial();v.site.controller=v.actor;const wrath=v.actor.vars[G+'wrath'];assert(!v.gate('host_can_receive_demand_payment'));v.day=v.actor.vars[G+'demand_deadline'];v.run('fail_demand');assert.equal(v.actor.vars[G+'wrath'],wrath);assert.equal(v.actor.vars[G+'demands_failed']||0,0);assert.equal(v.actor.vars[G+'demands_retired'],1);assert.equal(v.actor.vars[G+'last_response_kind'],constants['gods_of_africa_history_kind.lapsed']);});
	test('donor annex closed finance preserves earned native term',()=>{const v=fixture();v.partial();v.run('clear_demand');v.actor.exists=false;v.auth=false;v.run('review_industry_program',v.host);assert.equal(v.site.modifiers.size,1);assert.equal(v.host.vars[R+'due_day'],130);assert(v.host.flags.has(R+'reserved'));});
	test('host loss original scope removed exacttuple before epoch revoke history durable',()=>{const v=fixture();v.partial();v.host.arrays[G+'participants']=[v.actor];v.host.capitulated=true;v.host.flags.add(G+'active');v.run('cancel_on_unifier_loss',v.host);assert.equal(v.site.modifiers.size,0);assert.equal(v.nativeWrites.at(-1).host,v.host.id);assert.equal(v.actor.vars[G+'last_industry_retired_funded'],10);assert.equal(v.actor.vars[G+'last_industry_retired_unpaid'],10);assert.equal(v.trace.find(x=>x.revoke).retirementPublished,11);assert(!v.actor.flags.has(P+'terms_bound'));assert.equal(v.actor.arrays[G+'history_kinds'].filter(x=>x===23).length,1);});
	test('normal securedAfrica settlement actual participant closure preserves earned time',()=>{const v=fixture();v.partial();v.host.flags.add(G+'active');v.host.vars[G+'candidate_count']=1;v.host.arrays[G+'candidate_registry']=[v.actor];v.actor.flags.add(G+'settlement_pass_pending');v.actor.flags.add(G+'final_outcome_committed');const n=v.nativeWrites.length;v.run('commit_final_settlement',v.host);assert.equal(v.nativeWrites.length,n);assert.equal(v.site.modifiers.size,1);assert.equal(v.host.vars[R+'due_day'],130);assert(v.host.flags.has(R+'reserved'));assert(v.host.flags.has(R+'closed'));assert(!v.actor.flags.has(P+'terms_bound'));assert.equal(v.actor.vars[G+'demands_retired'],1);});
	test('durable retirement once postannex postepoch blocks reclaim if unconsumed',()=>{const v=fixture();v.partial();v.run('clear_demand');v.actor.exists=false;v.auth=false;v.host.vars[G+'authority_epoch']=2;v.day=140;v.run('retire_owned_industry_program',v.host);assert.equal(v.actor.arrays[G+'history_kinds'].filter(x=>x===23).length,1);assert.equal(v.actor.vars[G+'last_industry_retired_site'],v.site);assert(!v.host.flags.has(P+'retirement_recorded'));v.run('capture_industry_retirement',v.host);assert.equal(v.actor.arrays[G+'history_kinds'].filter(x=>x===23).length,1);
		const w=fixture();w.partial();w.run('clear_demand');delete w.actor.vars[G+'history_owner_id'];w.day=140;w.run('prepare_industry_candidate',w.host);assert(w.host.flags.has(P+'retirement_recorded'));assert(!w.gate('industry_offer_is_available',w.host));assert(!w.host.flags.has(P+'candidate_available'));});
	test('reentry clears terms preserves closed earned programme no free duplicate slot',()=>{const v=fixture();v.partial();v.run('clear_demand');assert(!v.actor.flags.has(P+'terms_bound'));assert(!Object.keys(v.actor.vars).some(k=>k===P+'quote'||k===P+'host'));v.run('prepare_industry_candidate',v.host);assert(!v.gate('industry_offer_is_available',v.host));v.day=140;v.run('prepare_industry_candidate',v.host);assert(v.gate('industry_offer_is_available',v.host));assert.equal(v.actor.vars[G+'last_industry_retired_funded'],10);v.create();assert.equal(v.host.vars[R+'contract_id'],12);assert.equal(v.host.vars[R+'funded'],0);assert.equal(v.host.vars[R+'granted_days'],0);});
	test('wrong frozen retirement tuple cannot remove replacement',()=>{const v=fixture();v.partial();v.retireTuple();v.temp[P+'retire_contract_id']=999;const n=v.nativeWrites.length;v.run('retire_industry_program',v.host);assert.equal(v.nativeWrites.length,n);assert(v.host.flags.has(R+'reserved'));});
	test('native refresh presence counterexample retained SourceNoNativeProof',()=>{const v=fixture();v.partial();v.day=110;v.failAdd=1;v.full();assert.equal(v.host.vars[R+'due_day'],160);assert.equal([...v.site.modifiers.values()][0].due,130);observations.push({finding:'presence cannot prove actual timer refresh',sourceDue:160,modeledUnrefreshedNativeDue:130,nativeProof:false});});
	test('unknown helpers and commands fail closed opaque ROOT THIS PREV',()=>{const v=fixture();assert.throws(()=>v.run('unknown_industry_helper'),/Unknown/);assert.throws(()=>v.exec([{key:'invented_native',value:'yes'}],v.ctx(v.actor)),/Unsupported/);const c=v.ctx(v.site,v.ctx(v.host),v.actor);assert.equal(v.scope('ROOT',c),v.actor);assert.equal(v.scope('THIS',c),v.site);assert.equal(v.scope('PREV',c),v.host);assert.equal(v.host.vars[R+'site'],v.site);assert.equal(v.host.vars[R+'participant'],v.actor);});
	test('participant archive clean cancel execute actual owners conserve30days',()=>{for(const owner of ['archive_invalid_participant','clean_participant','cancel_participant']){const v=fixture();v.partial();v.run(owner);assert(!v.actor.flags.has(P+'terms_bound'),owner);assert.equal(v.site.modifiers.size,1,owner);assert.equal(v.host.vars[R+'due_day'],130,owner);assert(v.host.flags.has(R+'closed'),owner);assert.equal(v.host.vars[G+'active_demand_count'],0,owner);}});
	test('register reentry actual owner clears frozen terms without resetting prior history',()=>{const v=fixture();v.partial();v.run('archive_invalid_participant');const history=v.actor.vars[G+'history_count'];v.run('register_participant');assert(!v.actor.flags.has(P+'terms_bound'));assert.equal(v.host.vars[R+'due_day'],130);assert.equal(v.site.modifiers.size,1);assert.equal(v.actor.vars[G+'history_count'],history);});
	test('owner clock retirement publishes after due even with inactive authority',()=>{const v=fixture();v.partial();v.run('clear_demand');v.day=140;v.run('run_owner_tick',v.host);assert.equal(v.actor.vars[G+'last_industry_retired_funded'],10);assert.equal(v.site.modifiers.size,0);});
	test('initialization rearms firstsuccessful demand marker only fresh generation',()=>{const v=new IntegrationVM();v.globalFlags.add('africa_is_one');v.globalFlags.add('africa_evolution_i_logged');v.host.flags.add(G+'first_demand_milestone_emitted');v.run('initialize_system',v.host);assert(!v.host.flags.has(G+'first_demand_milestone_emitted'));v.host.flags.add(G+'first_demand_milestone_emitted');v.run('initialize_system',v.host);assert(v.host.flags.has(G+'first_demand_milestone_emitted'));});
	test('source presentation quote branches match new30or31 days and completed zero',()=>{const v=fixture(20.5);assert.equal(selectText(v,'GetGodsOfAfricaIndustryTermsLine'),G+'industry_terms');assert.equal(selectText(v,'GetGodsOfAfricaIndustryPartialTermsLine'),G+'industry_partial_terms');assert.equal(selectText(v,'GetGodsOfAfricaPartialPaymentValue'),G+'partial_payment_cpp_value');const cpp=v.actor.pp,quoted=v.actor.vars[P+'partial_new_days'];v.partial();assert.equal(v.actor.vars[G+'last_response_industry_new_days'],quoted);assert.equal(selectText(v,'GetGodsOfAfricaIndustryResponseLine'),G+'industry_response_paid');assert.equal(v.actor.pp,cpp-10.25);v.site.damage=0;v.run('prepare_industry_candidate',v.host);assert.equal(selectText(v,'GetGodsOfAfricaIndustryTermsLine'),G+'industry_terms_completed');assert.equal(selectText(v,'GetGodsOfAfricaIndustryPartialTermsLine'),G+'industry_partial_terms_completed');v.day=v.actor.vars[G+'next_partial_payment_day'];v.full();assert.equal(v.actor.vars[G+'last_response_industry_new_days'],0);assert.equal(selectText(v,'GetGodsOfAfricaIndustryResponseLine'),G+'industry_response_completed');});
	test('13 exact observer hooks and raw financial Wrath history AST unchanged',()=>{
		const beforeDir='docs/plans/012_africa_plans/subagent_handoffs/012_gods_industry_implementation_2026-10-08_evidence/before/';
		const before=parse(fs.readFileSync(path.join(root,beforeDir+'common__scripted_effects__012_africa_gods_effects.txt'),'utf8'));const current=asts.get('common/scripted_effects/012_africa_gods_effects.txt');
		const hooks=new Set(['observe_public_strength','observe_public_wrath_commit','clear_public_wrath_values','clear_public_strength_observation','reset_public_strength_values'].map(x=>G+x));
		const inventory=a=>a.flatMap(owner=>walk(owner.value).filter(n=>hooks.has(n.key)).map(n=>({owner:owner.key,key:n.key,value:n.value}))).sort((a,b)=>JSON.stringify(a).localeCompare(JSON.stringify(b)));
		assert.equal(inventory(before).length,13);assert.deepEqual(inventory(current),inventory(before));
		for(const owner of ['apply_wrath','enforce_wrath_floor','record_history','compute_capacity_requirement'])assert.deepEqual(block(current,G+owner),block(before,G+owner),owner+' existing raw transaction changed');
		const allowVars=new Set(['wrath_display','wrath_fill','wrath_frame','wrath_previous_observed'].map(x=>G+x));const allowFlags=new Set(['wrath_trend_rising','wrath_trend_falling','wrath_sample_known'].map(x=>G+x));
		for(const name of ['observe_public_wrath','observe_public_wrath_commit'])for(const n of walk(effects[G+name])){
			assert(!n.key.includes('temp_variable'),'data observer borrows transaction temps');
			if(/^(set|add_to|subtract_from|divide|multiply|clamp)_variable$/.test(n.key)&&Array.isArray(n.value))assert(allowVars.has(n.value.find(x=>x.key==='var')?.value||n.value[0].key),'observer writes raw data');
			if(['round_variable','clear_variable'].includes(n.key))assert(allowVars.has(n.value),'observer raw scalar');
			if(['set_country_flag','clr_country_flag'].includes(n.key))assert(allowFlags.has(n.value),'observer raw flag');
		}
	});
	test('legacy kind8 callback retains fractional raw report and history counter',()=>{const v=fixture();v.actor.vars[G+'history_kind_request']=8;v.run('record_history');assert.equal(v.actor.vars[G+'punishment_count'],1);Object.assign(v.temp,{[G+'report_kind']:8,[G+'report_amount']:20.125,[G+'report_balance']:10.375});v.run('capture_response_report');assert.equal(v.actor.vars[G+'last_response_kind'],8);assert.equal(v.actor.vars[G+'last_response_amount'],20.125);assert.equal(v.actor.vars[G+'last_response_balance'],10.375);assert.equal(v.actor.pp,100);});
	test('failed first native installation refund does not fulfill or create compliance',()=>{const v=fixture();v.failAdd=1;v.full();assert.equal(v.actor.pp,100);assert.equal(v.host.pp,100);assert.equal(v.host.vars[R+'funded'],0);assert.equal(v.actor.vars[G+'demands_fulfilled']||0,0);assert.equal(v.actor.vars[G+'compliance_count']||0,0);assert(v.actor.flags.has(G+'demand_active'));assert.equal(v.actor.vars[G+'last_response_kind'],constants['gods_of_africa_history_kind.undelivered']);});
	test('accepted material substitute report retains original industrial receipt',()=>{const v=fixture();v.partial();Object.assign(v.actor.vars,{[G+'substitute_family']:constants['gods_of_africa_demand_family.land_equipment'],[G+'substitute_amount']:100});v.actor.flags.add(G+'substitute_offered');v.run('accept_substitute');assert(v.actor.flags.has(G+'last_response_industry'),'original industrial report details lost when temporary demand family becomes material');assert.equal(v.actor.vars[G+'last_response_industry_site'],v.site);assert.equal(v.actor.vars[G+'last_response_industry_funded'],10);assert.equal(v.actor.vars[G+'last_response_industry_new_days'],0,'substitute must not report earlier partial increment as new');});
	test('partly delivered material substitute preserves original tuple30days zero extraCPP',()=>{const v=fixture();v.partial();v.materialLimit=50;const cpp=v.actor.pp,hostCpp=v.host.pp,n=v.nativeWrites.length;Object.assign(v.actor.vars,{[G+'substitute_family']:constants['gods_of_africa_demand_family.land_equipment'],[G+'substitute_amount']:100});v.actor.flags.add(G+'substitute_offered');v.run('accept_substitute');assert(v.actor.flags.has(G+'demand_active'));assert(v.actor.flags.has(G+'contract_substitute_terms'));assert(v.actor.flags.has(P+'terms_bound'));assert.equal(v.actor.vars[G+'demand_family'],constants['gods_of_africa_demand_family.land_equipment']);assert.equal(v.actor.vars[G+'demand_remaining'],50);assert.equal(v.actor.pp,cpp);assert.equal(v.host.pp,hostCpp);assert.equal(v.nativeWrites.length,n);assert.equal(v.host.vars[R+'funded'],10);assert.equal(v.host.vars[R+'granted_days'],30);assert.equal(v.host.vars[R+'due_day'],130);assert.equal(v.actor.vars[G+'last_response_industry_site'],v.site);assert.equal(v.actor.vars[G+'last_response_industry_funded'],10);assert.equal(v.actor.vars[G+'last_response_industry_granted_days'],30);assert.equal(v.actor.vars[G+'last_response_industry_new_days'],0);assert.equal(v.actor.vars[G+'last_response_amount'],50);v.materialLimit=Infinity;v.full();assert.equal(v.actor.vars[G+'demands_honored_substitute'],1);assert.equal(v.nativeWrites.length,n);assert.equal(v.actor.pp,cpp);assert(v.host.flags.has(R+'closed'));assert.equal(v.actor.vars[G+'last_response_industry_new_days'],0);});
	test('F2 minimum3 allpartial financial fulfillment plus meaningful aid qualifies without fullclick memory',()=>{const v=fixture();const minimum=constants['gods_of_africa_protection.minimum_completed_demands'];assert.equal(minimum,3);for(let i=0;i<minimum;i++){if(i){v.day=Math.max(v.host.vars[R+'due_day']+1,v.actor.vars[G+'next_demand_date']);v.create();}v.partial();v.day=v.actor.vars[G+'next_partial_payment_day'];v.partial();}assert.equal(v.actor.vars[G+'demands_fulfilled'],minimum);assert.equal(v.actor.vars[G+'demands_full_original'],minimum);assert.equal(v.actor.vars[G+'compliance_count'],0);assert(!v.actor.flags.has(G+'reliable_memory_applied'));v.actor.vars[G+'wrath']=0;v.actor.vars[G+'voluntary_paid_infantry_k']=constants['gods_of_africa_transaction.voluntary_aid_equipment_amount']*constants['gods_of_africa_contribution_measure.k_per_native'];assert(v.gate('protection_has_meaningful_aid'));assert(v.gate('protection_relationship_is_eligible'));v.actor.flags.add(G+'participant');v.host.arrays[G+'participants']=[v.actor];v.host.flags.add(G+'active');v.authInputs.set(G+'active_host_is_valid',true);assert(v.gate('participant_can_receive_protection'));observations.push({finding:'F2 canonical threshold3 correction confirmed',canonicalFulfilled:minimum,canonicalFullOriginal:minimum,coarseCompliance:0,reliableMemory:false,meaningfulAid:true,productionRelationshipGate:true,productionOuterProtectionGate:true});});
	test('lostsite review retire then deadline lapse keeps exact retiredCPP5 days15 neutral',()=>{const v=fixture(10);v.partial();assert.equal(v.host.vars[R+'funded'],5);assert.equal(v.host.vars[R+'granted_days'],15);v.site.controller=v.actor;v.run('prepare_industry_candidate',v.host);assert(!v.host.flags.has(R+'reserved'));assert.equal(v.actor.vars[G+'last_industry_retired_funded'],5);assert.equal(v.actor.vars[G+'last_industry_retired_granted_days'],15);assert.equal(v.actor.arrays[G+'history_kinds'].filter(x=>x===23).length,1);Object.assign(v.actor.vars,{[G+'last_response_industry_funded']:999,[G+'last_response_industry_granted_days']:999,[G+'last_response_industry_new_days']:999});const wrath=v.actor.vars[G+'wrath'],cpp=v.actor.pp;v.day=v.actor.vars[G+'demand_deadline'];v.run('fail_demand');assert.equal(v.actor.vars[G+'last_response_industry_funded'],5);assert.equal(v.actor.vars[G+'last_response_industry_granted_days'],15);assert.equal(v.actor.vars[G+'last_response_industry_new_days'],0);assert.equal(v.actor.vars[G+'last_response_industry_site'],v.site);assert.equal(v.actor.vars[G+'last_response_kind'],constants['gods_of_africa_history_kind.lapsed']);assert.equal(v.actor.vars[G+'wrath'],wrath);assert.equal(v.actor.pp,cpp);assert.equal(v.actor.vars[G+'demands_failed']||0,0);assert.equal(v.actor.vars[G+'compliance_count']||0,0);assert.equal(v.actor.vars[G+'demands_fulfilled']||0,0);assert.equal(v.actor.vars[G+'demands_retired'],1);assert.equal(v.actor.arrays[G+'history_kinds'].filter(x=>x===23).length,1);});
	test('nonpayment refusal capture suppresses previous30newdays and refreshes currentCG',()=>{const v=fixture();v.partial();Object.assign(v.temp,{[G+'report_kind']:constants['gods_of_africa_history_kind.refusal'],[G+'report_amount']:0,[G+'report_balance']:10});Object.assign(v.actor.vars,{[G+'last_response_industry_funded']:999,[G+'last_response_industry_granted_days']:999,[G+'last_response_industry_new_days']:999});const cpp=v.actor.pp,n=v.nativeWrites.length;v.run('capture_response_report');assert.equal(v.actor.vars[G+'last_response_industry_funded'],10);assert.equal(v.actor.vars[G+'last_response_industry_granted_days'],30);assert.equal(v.actor.vars[G+'last_response_industry_new_days'],0);assert.equal(v.actor.pp,cpp);assert.equal(v.nativeWrites.length,n);});
	test('undelivered owner refreshes snapshot zero newdays after earlier paid30',()=>{const v=fixture();v.partial();v.day=v.actor.vars[G+'next_partial_payment_day'];v.site.controller=v.actor;Object.assign(v.actor.vars,{[G+'last_response_industry_funded']:999,[G+'last_response_industry_granted_days']:999,[G+'last_response_industry_new_days']:999});const cpp=v.actor.pp,n=v.nativeWrites.length;v.full();assert.equal(v.actor.vars[G+'last_response_kind'],constants['gods_of_africa_history_kind.undelivered']);assert(v.actor.flags.has(G+'last_response_industry'));assert.equal(v.actor.vars[G+'last_response_industry_funded'],10);assert.equal(v.actor.vars[G+'last_response_industry_granted_days'],30);assert.equal(v.actor.vars[G+'last_response_industry_new_days'],0);assert.equal(v.actor.pp,cpp);assert.equal(v.nativeWrites.length,n);});
	test('historical retirement completed flag durably survives source reclaim',()=>{const v=fixture();v.full();v.site.damage=0;v.run('prepare_industry_candidate',v.host);assert(!v.host.flags.has(R+'reserved'));assert(v.actor.flags.has(G+'last_industry_retired_site_completed'));assert.equal(v.actor.vars[G+'last_industry_retired_funded'],20);assert.equal(v.actor.arrays[G+'history_kinds'].filter(x=>x===23).length,1);});
	test('fresh paid earlycompletion pure UI gate and actual finalpayment without manualreview',()=>{const v=fixture();v.partial();v.day=110;v.site.damage=0;assert(!v.host.flags.has(R+'site_completed'));const before=structuredClone({actor:v.actor.vars,host:v.host.vars,actorFlags:[...v.actor.flags],hostFlags:[...v.host.flags]});assert(v.gate('industry_completion_is_proven'));assert(v.gate('current_demand_can_be_paid'));assert.equal(selectText(v,'GetGodsOfAfricaIndustryTermsLine'),G+'industry_terms_completed');assert.deepEqual({actor:v.actor.vars,host:v.host.vars,actorFlags:[...v.actor.flags],hostFlags:[...v.host.flags]},before,'pure earlycompletion changed durable state');const adds=v.nativeWrites.filter(x=>x.action==='add_dynamic_modifier').length,money=v.moneyWrites.length,reviews=v.trace.length;v.full();assert(v.trace.slice(reviews).some(x=>x.review&&x.cppWrites===money),'payment review must precede any fresh CPP debit');assert.equal(v.actor.pp,80);assert.equal(v.host.pp,120);assert.equal(v.host.vars[R+'funded'],20);assert.equal(v.host.vars[R+'granted_days'],30);assert.equal(v.nativeWrites.filter(x=>x.action==='add_dynamic_modifier').length,adds);assert.equal(v.actor.vars[G+'last_response_industry_new_days'],0);assert(v.actor.flags.has(G+'last_response_industry_completed'));assert.equal(v.actor.vars[G+'demands_fulfilled'],1);assert(v.host.flags.has(R+'site_completed'));});
	test('zeroDamage unfunded and unobservedexpired reject puregate and CPPpayment',()=>{for(const kind of ['unfunded','expired']){const v=fixture();if(kind==='expired'){v.partial();v.day=v.host.vars[R+'due_day'];}v.site.damage=0;assert(!v.gate('industry_completion_is_proven'),kind);assert(!v.gate('current_demand_can_be_paid'),kind);const cpp=v.actor.pp,hostCPP=v.host.pp,adds=v.nativeWrites.filter(x=>x.action==='add_dynamic_modifier').length;v.full();assert.equal(v.actor.pp,cpp,kind);assert.equal(v.host.pp,hostCPP,kind);assert.equal(v.nativeWrites.filter(x=>x.action==='add_dynamic_modifier').length,adds,kind);assert.equal(v.actor.vars[G+'demands_fulfilled']||0,0,kind);}});
	test('retired response fallback each stale identity rejects earlier receipt defaultsCG0',()=>{for(const f of ['host_id','generation','origin_host_id','epoch','contract_id']){const v=fixture(10);v.partial();v.site.controller=v.actor;v.run('prepare_industry_candidate',v.host);v.actor.vars[G+'last_industry_retired_'+f]++;Object.assign(v.actor.vars,{[G+'last_response_industry_funded']:999,[G+'last_response_industry_granted_days']:999,[G+'last_response_industry_new_days']:999,[G+'last_response_kind']:constants['gods_of_africa_history_kind.lapsed']});v.run('capture_industry_response_details');assert.equal(v.actor.vars[G+'last_response_industry_funded'],0,f);assert.equal(v.actor.vars[G+'last_response_industry_granted_days'],0,f);assert.equal(v.actor.vars[G+'last_response_industry_new_days'],0,f);}});
	test('native enable real HOST source ROOT SITE preserves closed finance donor annex paid term',()=>{const v=fixture();v.partial();assert(v.nativeIndustryEnable());v.run('clear_demand');v.actor.exists=false;v.auth=false;const snapshot=structuredClone({host:v.host.vars,flags:[...v.host.flags]});assert(v.nativeIndustryEnable());assert.deepEqual({host:v.host.vars,flags:[...v.host.flags]},snapshot);assert(v.host.flags.has(R+'closed'));assert.equal(v.host.vars[R+'due_day'],130);assert.equal(v.site.modifiers.size,1);});
	test('native enable exact ROOT site and secured physical predicate reject captor before callback',()=>{for(const lost of ['controller','owner','core','continent']){const v=fixture();v.partial();assert(v.nativeIndustryEnable());if(lost==='continent')v.site.continent='europe';else v.site[lost]=v.actor;assert(!v.nativeIndustryEnable(),lost);assert(!v.nativeIndustryEnable(v.actor,v.site),'captor cannot supply original source');assert.equal(v.site.modifiers.size,1,'presence is retained before callback, authorization is false');}const v=fixture();v.partial();const other=state(276,v.host,1);other.name='different affected state';other.arrays={};assert(!v.nativeIndustryEnable(v.host,other),'wrong ROOT object');});
	test('native enable rejects stale source tuple epoch host replacement and capitulation',()=>{for(const stale of ['host_id','generation','origin_host_id','epoch','capitulated','exists','replacement']){const v=fixture();v.partial();if(stale==='capitulated')v.host.capitulated=true;else if(stale==='exists')v.host.exists=false;else if(stale==='replacement')v.targets.africa_host=v.actor;else v.host.vars[R+stale]++;assert(!v.nativeIndustryEnable(),stale);assert.equal(v.site.modifiers.size,1,'enable test does not perform cleanup');}});
	test('control change other state ignores old controller programme without review or writes',()=>{const v=fixture();v.partial();const other=state(276,v.host,1);other.name='other captured state';other.controller=v.actor;other.arrays={};const before=structuredClone({host:v.host.vars,actor:v.actor.vars,hostFlags:[...v.host.flags],actorFlags:[...v.actor.flags],arrays:v.actor.arrays});const calls=v.calls.length,native=v.nativeWrites.length,money=v.moneyWrites.length;v.controlChanged(other);assert.equal(v.calls.length,calls,'different site must not review');assert.equal(v.nativeWrites.length,native);assert.equal(v.moneyWrites.length,money);assert.deepEqual({host:v.host.vars,actor:v.actor.vars,hostFlags:[...v.host.flags],actorFlags:[...v.actor.flags],arrays:v.actor.arrays},before);});
	test('control change same captured site retires exact scoped service and publishes once replay noop',()=>{const v=fixture();v.partial();const native=v.nativeWrites.length,money=v.moneyWrites.length,events=v.events.length;v.site.controller=v.actor;assert(!v.nativeIndustryEnable());v.controlChanged(v.site);assert.equal(v.site.modifiers.size,0);assert.equal(v.nativeWrites.length,native+1);assert.deepEqual(v.nativeWrites.at(-1),{action:'remove_dynamic_modifier',site:v.site.id,host:v.host.id,due:v.day});assert.equal(v.moneyWrites.length,money);assert.equal(v.events.length,events);assert.equal(v.actor.vars[G+'last_industry_retired_funded'],10);assert.equal(v.actor.vars[G+'last_industry_retired_granted_days'],30);assert.equal(v.actor.vars[G+'last_industry_retired_unpaid'],10);assert.equal(v.actor.arrays[G+'history_kinds'].filter(x=>x===23).length,1);assert.equal(v.actor.vars[G+'demands_fulfilled']||0,0);assert.equal(v.actor.vars[G+'demands_failed']||0,0);assert(v.actor.flags.has(G+'demand_active'),'control callback does not close finance');assert.equal(v.host.vars[G+'active_demand_count'],1);const calls=v.calls.length,afterNative=v.nativeWrites.length,count=v.actor.vars[G+'history_count'];v.controlChanged(v.site);assert.equal(v.calls.length,calls);assert.equal(v.nativeWrites.length,afterNative);assert.equal(v.actor.vars[G+'history_count'],count);assert.equal(v.moneyWrites.length,money);});
	test('late control callback old site cannot retire replacement programme at different ROOT site',()=>{const v=fixture();v.partial();const oldSite=v.site;oldSite.controller=v.actor;v.controlChanged(oldSite);v.run('clear_demand');const replacement=state(276,v.host,1);replacement.name='replacement repair site';replacement.arrays={};v.host.states.push(replacement);v.objects.push(replacement);v.create();v.partial();assert.equal(v.host.vars[R+'site'],replacement);assert.equal(v.host.vars[R+'contract_id'],12);assert(v.nativeIndustryEnable(v.host,replacement));const native=v.nativeWrites.length,money=v.moneyWrites.length,count=v.actor.vars[G+'history_count'];v.controlChanged(oldSite);assert.equal(v.host.vars[R+'site'],replacement);assert(v.host.flags.has(R+'reserved'));assert.equal(v.nativeWrites.length,native);assert.equal(v.moneyWrites.length,money);assert.equal(v.actor.vars[G+'history_count'],count);assert.equal(replacement.modifiers.size,1);});
	const sourceHashes=[...sources].map(([p,b])=>({path:p,sha256:hash(b),changedDuringRun:hash(fs.readFileSync(path.join(root,p)))!==hash(b)}));
	const partialOwners=new Set([G+'build_need_profile',G+'select_demand_family']);
	const beforeDir='docs/plans/012_africa_plans/subagent_handoffs/012_gods_industry_implementation_2026-10-08_evidence/before/';
	const ownerCoverage=[];
	for(const [p,a] of asts){if(!p.includes('/scripted_effects/')&&!p.includes('/scripted_triggers/'))continue;const oldPath=path.join(root,beforeDir+p.replaceAll('/','__'));if(!fs.existsSync(oldPath))continue;const bytes=fs.readFileSync(oldPath),old=new Map(parse(bytes.toString('utf8')).map(n=>[n.key,n.value]));for(const n of a)if(JSON.stringify(n.value)!==JSON.stringify(old.get(n.key)))ownerCoverage.push({path:p,owner:n.key,baselineSha256:hash(bytes),execution:executed.has(n.key)?'production body under explicit boundaries':partialOwners.has(n.key)?'production changed industry subtree executed':'not executed'});}
	const testHashes=['.tools/validation/test_012_gods_industry_integration.js','.tools/validation/test_012_gods_industry_helpers.js','docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03.js'].map(p=>({path:p,sha256:hash(fs.readFileSync(path.join(root,p)))}));
	const newSurfaceCoverage=[
		{path:'common/scripted_triggers/012_africa_gods_industry_triggers.txt',owner:G+'industry_native_service_is_authorized',execution:'production trigger body',scope:'targeted recipient COUNTRY',ROOT:'actual affected STATE'},
		{path:'common/dynamic_modifiers/012_africa_gods_industry_modifiers.txt',owner:G+'industry_repair_program.enable',execution:'production enable body'},
		{path:'common/on_actions/012_africa_gods_industry_on_actions.txt',owner:'on_actions.on_state_control_changed.effect',execution:'production callback body',nativeBindings:{ROOT:'new controller COUNTRY',FROM:'old controller COUNTRY','FROM.FROM':'changed STATE'},nativeTimingProof:false}
	];
	const report={generatedAt:new Date().toISOString(),model:'SourceNoNativeProof',nativeProof:false,results,failures,observations,ownerCoverage,newSurfaceCoverage,executedHelpers:[...executed].sort(),authorizationBoundaries:[...authorization.keys()],consumerBoundaries:[...consumerBoundaries],usedBoundaries:[...usedBoundaries].sort(),sourceHashes,testHashes};
	if(process.argv.includes('--evidence')){const dir=path.join(root,evidenceDir);fs.mkdirSync(dir,{recursive:true});fs.writeFileSync(path.join(dir,'source_integration_results.json'),JSON.stringify(report,null,2)+'\n');}
	console.log(JSON.stringify({cases:results.length,failures:failures.map(x=>({name:x.name,error:x.error})),sourceTests:true,nativeProof:false,sourceChangedDuringRun:sourceHashes.filter(x=>x.changedDuringRun),observations}));
	if(failures.length||sourceHashes.some(x=>x.changedDuringRun))process.exitCode=1;
	return report;
}
module.exports={IntegrationVM,runTests,effects,triggers,asts,parse,walk,block};
if(require.main===module)runTests();
