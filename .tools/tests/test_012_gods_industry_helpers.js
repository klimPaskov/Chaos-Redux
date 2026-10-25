/* Actual-source Event 012 industry contract scenarios. Native operations are
 * modeled, not engine evidence. External parent authorization predicates are
 * explicit fixture inputs. Every local helper executes its parsed source.
 * Helpers discard newly created temps on return, retaining caller-owned temps.
 */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..', '..');
const P = 'gods_of_africa_industry_', R = P + 'program_';
const read = p => fs.readFileSync(path.join(root, p), 'utf8');
function parse(text) {
	const ts = text.replace(/#[^\r\n]*/g, '').match(/"[^"\r\n]*"|[{}=<>]|[^\s{}=<>]+/g) || [];
	let at = 0;
	function block(nested) {
		const out = [];
		while (at < ts.length && ts[at] !== '}') {
			const key = ts[at++], op = ts[at++];
			assert(['=', '<', '>'].includes(op), `Bad operator ${op} after ${key}`);
			let value = ts[at++];
			if (value === '{') value = block(true);
			out.push({key, op, value});
		}
		if (nested) assert.equal(ts[at++], '}');
		return out;
	}
	const result = block(false);
	assert.equal(at, ts.length);
	return result;
}
const effects = Object.fromEntries(parse(read('common/scripted_effects/012_africa_gods_industry_effects.txt')).map(n => [n.key,n.value]));
const triggers = Object.fromEntries(parse(read('common/scripted_triggers/012_africa_gods_industry_triggers.txt')).map(n => [n.key,n.value]));
const constants = {};
for (const f of ['common/script_constants/012_africa_gods_constants.txt','common/script_constants/012_africa_gods_industry_constants.txt']) {
	for (const cat of parse(read(f))) for (const n of cat.value) if (typeof n.value === 'string' && Number.isFinite(Number(n.value))) constants[cat.key+'.'+n.key] = Number(n.value);
}
const external = new Set(['gods_of_africa_demand_contract_is_current','gods_of_africa_demand_epoch_is_current','gods_of_africa_demand_owner_object_is_proven','gods_of_africa_contract_ledger_can_close','gods_of_africa_demand_payment_is_open','gods_of_africa_participant_generation_is_current','gods_of_africa_epoch_permission_is_current']);
const fixed = n => Math.trunc((n + Math.sign(n)*1e-10) * 100000)/100000;
function country(id) { return {type:'country',id,vars:{},flags:new Set(),exists:true,capitulated:false,pp:100,factories:2,states:[]}; }
function state(id, host, damage) { return {type:'state',id,vars:{},flags:new Set(),owner:host,controller:host,core:host,continent:'africa',damage,modifiers:new Map()}; }
class VM {
	constructor() {
		this.host=country(1); this.actor=country(2); this.site=state(275,this.host,1);
		this.host.states=[this.site]; this.host.capital=this.site;
		this.objects=[this.host,this.actor,this.site]; this.targets={africa_host:this.host};
		this.day=100; this.temp={}; this.auth=true; this.failAdd=0; this.failRemove=false;
		this.cap=Infinity; this.debitScale=1; this.nativeWrites=[]; this.moneyWrites=[];
		this.failAddDropsExisting=false; this.afterDebit=null;
		Object.assign(this.host.vars,{africa_host_generation:1,africa_origin_host_id:1,gods_of_africa_authority_epoch:1});
		Object.assign(this.actor.vars,{gods_of_africa_demand_host:this.host,gods_of_africa_demand_host_id:1,gods_of_africa_demand_origin_host_id:1,gods_of_africa_demand_id:11,gods_of_africa_demand_generation:1,gods_of_africa_demand_authority_epoch:1,gods_of_africa_demand_family:constants['gods_of_africa_demand_family.industry_repair'],gods_of_africa_demand_amount:20,gods_of_africa_demand_remaining:20,gods_of_africa_partial_payment_amount:10});
	}
	ctx(scope, prev=null, root=scope) { return {scope,prev,root}; }
	scope(token,c) {
		if(token==='THIS')return c.scope;
		if(token==='PREV')return c.prev?.scope;
		if(token==='ROOT')return c.root;
		if(token.startsWith('event_target:'))return this.targets[token.slice(13)];
		if(token.startsWith('var:'))return this.value(token.slice(4),c);
		return this.objects.find(s=>String(s.id)===token);
	}
	value(token,c) {
		if(typeof token==='number')return token;
		if(token==='global.num_days')return this.day;
		if(token.startsWith('constant:')) { assert(token.slice(9) in constants, 'Unknown constant '+token); return constants[token.slice(9)]; }
		if(token.startsWith('var:'))return this.value(token.slice(4),c);
		if(Number.isFinite(Number(token)))return Number(token);
		const dot=token.indexOf('.');
		if(dot>=0) {
			const head=token.slice(0,dot), tail=token.slice(dot+1);
			const s=this.scope(head,c) || this.value(head,c);
			return s ? this.value(tail,this.ctx(s,c,c.root)) : 0;
		}
		if(token==='THIS'||token==='PREV'||token==='ROOT'||token.startsWith('event_target:'))return this.scope(token,c);
		if(Object.hasOwn(this.temp,token))return this.temp[token];
		if(token==='id')return c.scope.id;
		if(token==='has_political_power')return c.scope.pp;
		if(token==='num_of_civilian_factories_available_for_projects')return c.scope.factories;
		if(token==='damaged_building_level@industrial_complex')return c.scope.damage;
		return c.scope.vars[token] ?? 0;
	}
	cmp(a,b,op) {
		if(op==='='||op==='equals')return a===b;
		if(op==='>'||op==='greater_than')return a>b;
		if(op==='<'||op==='less_than')return a<b;
		if(op==='greater_than_or_equals')return a>=b;
		if(op==='less_than_or_equals')return a<=b;
		throw Error('Unknown comparison '+op);
	}
	call(name,c,trigger=false) {
		const before=new Set(Object.keys(this.temp));
		try { return trigger ? this.test(triggers[name],c) : this.exec(effects[name],c); }
		finally {for(const k of Object.keys(this.temp))if(!before.has(k))delete this.temp[k];}
	}
	variable(n,c) {
		const b=Object.fromEntries(n.value.map(x=>[x.key,x.value]));
		const temp=n.key.includes('temp_variable'), store=temp?this.temp:c.scope.vars;
		if(n.key.startsWith('clamp')) {store[b.var]=Math.min(this.value(b.max,c),Math.max(this.value(b.min,c),store[b.var]??0));return;}
		const key=b.var || n.value[0].key, raw=b.value || n.value[0].value, v=this.value(raw,c), old=store[key]??0;
		if(n.key.startsWith('set_'))store[key]=v;
		else if(n.key.startsWith('add_to_'))store[key]=fixed(old+v);
		else if(n.key.startsWith('subtract_'))store[key]=fixed(old-v);
		else if(n.key.startsWith('multiply_'))store[key]=fixed(old*v);
		else if(n.key.startsWith('divide_')) {assert(v>0,'Nonpositive divisor');store[key]=fixed(old/v);}
		else if(n.key.startsWith('modulo_'))store[key]=fixed(old%v);
		else throw Error('Unknown variable operation '+n.key);
	}
	modifier(n,c) {
		const b=Object.fromEntries(n.value.map(x=>[x.key,x.value]));
		const host=this.scope(b.scope,c), key=host.id+':'+b.modifier, old=c.scope.modifiers.get(key);
		if(old && old.due<=this.day)c.scope.modifiers.delete(key);
		return {b,host,key,active:c.scope.modifiers.has(key)};
	}
	test(nodes,c,mode='AND') {
		const check=n=>{
			if(n.key==='custom_trigger_tooltip')return this.test(n.value.filter(x=>x.key!=='tooltip'),c);
			// hidden_trigger only hides the tooltip; the engine evaluates it like AND.
			if(n.key==='hidden_trigger')return this.test(n.value,c);
			if(['AND','OR','NOT'].includes(n.key))return this.test(n.value,c,n.key);
			if(n.key==='if') {const lim=n.value.find(x=>x.key==='limit');return !this.test(lim.value,c)||this.test(n.value.filter(x=>x!==lim),c);}
			if(n.key==='else')return this.test(n.value,c);
			if(n.key.endsWith('_temp_variable')) {this.variable(n,c);return true;}
			if(n.key==='check_variable') {
				const b=Object.fromEntries(n.value.map(x=>[x.key,x.value]));
				if(b.var)return this.cmp(this.value(b.var,c),this.value(b.value,c),b.compare||'=');
				const x=n.value[0];return this.cmp(this.value(x.key,c),this.value(x.value,c),x.op);
			}
			if(n.key==='has_variable')return Object.hasOwn(c.scope.vars,n.value)||Object.hasOwn(this.temp,n.value);
			if(n.key==='has_country_flag')return c.scope.flags.has(n.value);
			if(n.key==='has_event_target')return !!this.targets[n.value];
			if(n.key==='exists')return c.scope.exists===(n.value==='yes');
			if(n.key==='has_capitulated')return c.scope.capitulated===(n.value==='yes');
			if(n.key==='tag')return c.scope===this.scope(n.value,c);
			if(n.key==='is_owned_by')return c.scope.owner===this.scope(n.value,c);
			if(n.key==='is_controlled_by')return c.scope.controller===this.scope(n.value,c);
			if(n.key==='is_core_of')return c.scope.core===this.scope(n.value,c);
			if(n.key==='is_on_continent')return c.scope.continent===n.value;
			if(n.key==='has_political_power')return this.cmp(c.scope.pp,this.value(n.value,c),n.op);
			if(n.key==='has_dynamic_modifier')return this.modifier(n,c).active;
			if(n.key==='any_owned_state')return c.scope.states.some(s=>this.test(n.value,this.ctx(s,c,c.root)));
			if(n.key in triggers) {const v=this.call(n.key,c,true);return n.value==='no'?!v:v;}
			if(external.has(n.key))return this.auth;
			const s=this.scope(n.key,c);
			if(s)return this.test(n.value,this.ctx(s,c,c.root));
			throw Error('Unsupported source trigger '+n.key);
		};
		// Clausewitz trigger if/else is a chain, not unconditional sibling tests.
		const results=[];
		for(let i=0;i<nodes.length;i++) {
			const n=nodes[i];
			if(n.key==='if') {
				let chosen=false, value=true;
				for(;i<nodes.length;i++) {
					const arm=nodes[i];if(i>0 && arm!==n && !['else_if','else'].includes(arm.key)){i--;break;}
					if(!chosen) {const lim=arm.value.find(x=>x.key==='limit');if(!lim||this.test(lim.value,c)){value=this.test(arm.value.filter(x=>x!==lim),c);chosen=true;}}
					if(i+1>=nodes.length||!['else_if','else'].includes(nodes[i+1].key))break;
				}
				results.push(value);
			} else results.push(check(n));
			if(mode==='AND'&&!results.at(-1))return false;
			if(mode==='OR'&&results.at(-1))return true;
		}
		return mode==='OR'?results.some(Boolean):mode==='NOT'?!results.every(Boolean):results.every(Boolean);
	}
	exec(nodes,c) {
		for(let i=0;i<nodes.length;i++) {
			const n=nodes[i];
			if(n.key==='if') {
				let chosen=false;
				for(;i<nodes.length;i++) {
					const arm=nodes[i],lim=arm.value.find(x=>x.key==='limit');
					if(!chosen&&(!lim||this.test(lim.value,c))){this.exec(arm.value.filter(x=>x!==lim),c);chosen=true;}
					if(i+1>=nodes.length||!['else_if','else'].includes(nodes[i+1].key))break;
				}
				continue;
			}
			if(n.key.endsWith('_variable')&&Array.isArray(n.value)){this.variable(n,c);continue;}
			if(n.key==='clear_variable'){delete c.scope.vars[n.value];continue;}
			if(n.key==='set_country_flag'){c.scope.flags.add(n.value);continue;}
			if(n.key==='clr_country_flag'){c.scope.flags.delete(n.value);continue;}
			if(n.key==='add_political_power') {
				const amount=this.value(n.value,c),before=c.scope.pp;
				c.scope.pp=fixed(Math.min(this.cap,before+amount*(amount<0&&c.scope===this.actor?this.debitScale:1)));
				this.moneyWrites.push({id:c.scope.id,amount,actual:fixed(c.scope.pp-before),inflight:this.host.flags.has(R+'inflight')});
				if(amount<0&&c.scope===this.actor&&this.afterDebit){const fn=this.afterDebit;this.afterDebit=null;fn();}
				continue;
			}
			if(n.key==='add_dynamic_modifier'||n.key==='remove_dynamic_modifier') {
				const {b,host,key}=this.modifier(n,c),due=this.day+this.value(b.days||'0',c);
				this.nativeWrites.push({action:n.key,site:c.scope.id,host:host.id,due});
				if(n.key==='add_dynamic_modifier'){if(this.failAdd>0){this.failAdd--;if(this.failAddDropsExisting)c.scope.modifiers.delete(key);}else c.scope.modifiers.set(key,{due});}
				else if(!this.failRemove)c.scope.modifiers.delete(key);
				continue;
			}
			if(n.key==='capital_scope') {this.exec(n.value,this.ctx(c.scope.capital,c,c.root));continue;}
			if(n.key==='every_owned_state') {for(const s of c.scope.states){const sc=this.ctx(s,c,c.root),lim=n.value.find(x=>x.key==='limit');if(!lim||this.test(lim.value,sc))this.exec(n.value.filter(x=>x!==lim),sc);}continue;}
			if(n.key in effects){this.call(n.key,c);continue;}
			const s=this.scope(n.key,c);if(s){this.exec(n.value,this.ctx(s,c,c.root));continue;}
			throw Error('Unsupported source effect '+n.key);
		}
	}
	run(name,scope=this.actor) {this.call('gods_of_africa_'+name,this.ctx(scope));}
	gate(name,scope=this.actor) {return this.call('gods_of_africa_'+name,this.ctx(scope),true);}
	bind(q=20) {Object.assign(this.actor.vars,{gods_of_africa_demand_amount:q,gods_of_africa_demand_remaining:q,gods_of_africa_partial_payment_amount:q/2});this.run('select_industry_site',this.host);this.run('bind_industry_terms');assert(this.actor.flags.has(P+'terms_bound'));}
	pay(p,consume=true) {
		Object.assign(this.actor.vars,{gods_of_africa_payment_family:constants['gods_of_africa_demand_family.industry_repair'],gods_of_africa_payment_amount:p});
		this.run('pay_industrial_tribute');
		const received=this.actor.vars.gods_of_africa_payment_delivered;
		if(consume)this.actor.vars.gods_of_africa_demand_remaining=fixed(this.actor.vars.gods_of_africa_demand_remaining-received);
		return received;
	}
	retireTuple() {for(const a of ['host_id','generation','origin_host_id','epoch','contract_id'])this.temp[P+'retire_'+a]=this.host.vars[R+a];}
}
// hidden_trigger only hides tooltip text and is evaluated like AND, so AST comparisons against
// pre-wrapper snapshots splice its children into the parent list.
function unhide(ns) {
	if (!Array.isArray(ns)) return ns;
	return ns.flatMap(n => n.key === 'hidden_trigger' && Array.isArray(n.value) ? unhide(n.value) : [Array.isArray(n.value) ? {...n, value: unhide(n.value)} : n]);
}
module.exports = { unhide, parse, VM, effects, triggers, constants, external, fixed, country, state, P, R, root, read };
if (require.main === module) {
let cases=0;
function test(name,fn){fn();cases++;console.log('PASS '+name);}
test('IND_FULL_BASE exact receipt and in-flight-before-debit',()=>{const v=new VM();v.bind();assert.equal(v.host.vars[R+'service_days'],60);assert.equal(v.pay(20),20);assert.equal(v.actor.pp,80);assert.equal(v.host.pp,120);assert.equal(v.host.vars[R+'granted_days'],60);assert.equal(v.host.vars[R+'due_day'],160);assert(v.moneyWrites.every(x=>x.inflight));assert.equal(v.nativeWrites.filter(x=>x.action==='add_dynamic_modifier').length,1);});
test('IND_PARTIAL_CONTIGUOUS adds only newly funded days',()=>{const v=new VM();v.bind();v.pay(10);v.day=110;v.pay(10);assert.equal(v.host.vars[R+'due_day'],160);assert.equal(v.host.vars[R+'granted_days'],60);});
test('IND_PARTIAL_GAP preserves open reservation',()=>{const v=new VM();v.bind();v.pay(10);v.day=140;v.run('review_industry_program',v.host);assert(v.host.flags.has(R+'reserved'));assert(!v.host.flags.has(R+'native_applied'));assert.equal(v.pay(10),10);assert.equal(v.host.vars[R+'due_day'],170);assert.equal(v.host.vars[R+'granted_days'],60);});
test('IND_FRACTIONAL cumulative remainder, exact CPP',()=>{const v=new VM();v.bind(20.5);assert.equal(v.host.vars[R+'service_days'],61);assert.equal(v.pay(10.25),10.25);assert.equal(v.host.vars[R+'granted_days'],30);assert.equal(v.pay(10.25),10.25);assert.equal(v.host.vars[R+'granted_days'],61);assert.equal(v.actor.pp,79.5);});
test('IND_REPLAY unchanged balance blocks duplicate debit',()=>{const v=new VM();v.bind();v.pay(10,false);const money=v.moneyWrites.length,native=v.nativeWrites.length;assert.equal(v.pay(10,false),0);assert.equal(v.moneyWrites.length,money);assert.equal(v.nativeWrites.length,native);});
test('IND_CPP_BOUNDARY preserves legacy CPP reserve',()=>{for(const [pp,ok] of [[20.99999,false],[21,true],[21.00001,true]]){const v=new VM();v.bind();v.actor.pp=pp;assert.equal(v.gate('industry_full_payment_can_execute'),ok);assert.equal(v.pay(20),ok?20:0);}const v=new VM();v.bind();v.actor.pp=10.99999;assert(!v.gate('industry_partial_payment_can_execute'));});
test('IND_PURE_WRAPPERS preserve all normal quote fields',()=>{const v=new VM();v.bind();v.actor.vars.gods_of_africa_payment_amount=999;v.actor.vars.gods_of_africa_payment_family=999;const before=JSON.stringify(v.actor.vars,(k,x)=>k==='gods_of_africa_industry_host'||k==='gods_of_africa_industry_site'||k==='gods_of_africa_demand_host'?x.id:x);assert(v.gate('industry_full_payment_can_execute'));assert(v.gate('industry_partial_payment_can_execute'));assert.equal(JSON.stringify(v.actor.vars,(k,x)=>k==='gods_of_africa_industry_host'||k==='gods_of_africa_industry_site'||k==='gods_of_africa_demand_host'?x.id:x),before);assert.deepEqual(v.temp,{});});
test('IND_NO_SITE and capital/maximum-damage deterministic selection',()=>{const v=new VM();v.site.damage=.49;v.run('select_industry_site',v.host);assert(!v.host.flags.has(P+'candidate_available'));const b=state(276,v.host,2),c=state(277,v.host,2);v.host.states.push(b,c);v.objects.push(b,c);v.run('select_industry_site',v.host);assert.equal(v.host.vars[P+'selected_site'],b);v.site.damage=.5;v.run('select_industry_site',v.host);assert.equal(v.host.vars[P+'selected_site'],v.site);assert(!v.host.flags.has(R+'reserved'));});
test('IND_STALE_TUPLE denies each frozen field mismatch',()=>{for(const f of ['host_id','generation','origin_host_id','epoch','contract_id','quote','service_days']){const v=new VM();v.bind();v.actor.vars[P+f]++;assert.equal(v.pay(20),0);assert.equal(v.moneyWrites.length,0);}});
test('IND_SITE_CAPTURE original scoped effect removed before pointer clear',()=>{const v=new VM();v.bind();v.pay(10);v.site.controller=v.actor;assert.equal(v.pay(10),0);v.run('review_industry_program',v.host);assert(!v.host.flags.has(R+'reserved'));assert.equal(v.host.vars[P+'retired_funded'],10);assert.equal(v.host.vars[P+'retired_unpaid'],10);assert.equal(v.site.modifiers.size,0);assert.equal(v.nativeWrites.at(-1).host,1);});
test('IND_HOST_REPLACEMENT and authority cleanup after revocation',()=>{const v=new VM();v.bind();v.pay(10);v.retireTuple();v.auth=false;v.host.vars.gods_of_africa_authority_epoch=2;v.targets.africa_host=v.actor;v.run('retire_industry_program',v.host);assert.equal(v.site.modifiers.size,0);assert.equal(v.host.vars[P+'retired_funded'],10);});
test('IND_LATE_CALLBACK cannot retire new contract',()=>{const v=new VM();v.bind();v.retireTuple();v.host.vars[R+'contract_id']=12;v.run('retire_industry_program',v.host);assert(v.host.flags.has(R+'reserved'));assert.equal(v.nativeWrites.length,0);});
test('IND_CAP receiver credit cap rollback measures actual credit',()=>{const v=new VM();v.bind();v.host.pp=95;v.cap=100;assert.equal(v.pay(20),0);assert.equal(v.actor.pp,100);assert.equal(v.host.pp,95);assert.equal(v.host.vars[R+'funded'],0);assert.equal(v.nativeWrites.length,0);});
test('IND_SHORT_DEBIT exact receipt rejected and measured refund',()=>{const v=new VM();v.bind();v.debitScale=.5;assert.equal(v.pay(20),0);assert.equal(v.actor.pp,100);assert.equal(v.host.pp,100);assert.equal(v.host.vars[R+'funded'],0);});
test('IND_NATIVE_FAILURE first payment refunds with no receipt',()=>{const v=new VM();v.bind();v.failAdd=1;assert.equal(v.pay(20),0);assert.equal(v.actor.pp,100);assert.equal(v.host.pp,100);assert.equal(v.host.vars[R+'funded'],0);assert.equal(v.host.vars[R+'granted_days'],0);assert(!v.host.flags.has(R+'inflight'));});
test('IND_REFRESH_UNOBSERVABLE SourceNoNativeProof',()=>{const v=new VM();v.bind();v.pay(10);v.day=110;v.failAdd=1;assert.equal(v.pay(10),10);assert.equal(v.host.vars[R+'due_day'],160);assert.equal([...v.site.modifiers.values()][0].due,130);/* Explicit counterexample: presence alone cannot prove refresh duration. */});
test('IND_NATIVE_FAILURE observed replacement failure restores old term only',()=>{const v=new VM();v.bind();v.pay(10);v.day=110;v.failAdd=1;v.failAddDropsExisting=true;assert.equal(v.pay(10),0);assert.equal(v.actor.pp,90);assert.equal(v.host.pp,110);assert.equal(v.host.vars[R+'funded'],10);assert.equal(v.host.vars[R+'granted_days'],30);assert.equal(v.host.vars[R+'due_day'],130);assert.equal([...v.site.modifiers.values()][0].due,130);});
test('IND_INFLIGHT_CLEANUP cannot erase binding',()=>{const v=new VM();v.bind();v.host.flags.add(R+'inflight');v.run('clear_industry_terms');assert(v.actor.flags.has(P+'terms_bound'));assert(!v.host.flags.has(R+'closed'));});
test('IND_SITE_LOSS_AFTER_PREFLIGHT refunds measured new money',()=>{const v=new VM();v.bind();v.afterDebit=()=>{v.site.controller=v.actor;};assert.equal(v.pay(20),0);assert.equal(v.actor.pp,100);assert.equal(v.host.pp,100);assert.equal(v.nativeWrites.length,0);});
test('IND_NATIVE_ABSENCE unresolved evidence blocks further payment',()=>{const v=new VM();v.bind();v.pay(10);v.site.modifiers.clear();v.run('review_industry_program',v.host);assert(v.host.flags.has(R+'unresolved'));assert.equal(v.pay(10),0);assert.equal(v.nativeWrites.filter(x=>x.action==='add_dynamic_modifier').length,1);});
test('IND_EARLY_COMPLETE settles remainder without fresh native timer',()=>{const v=new VM();v.bind();v.pay(10);v.day=110;v.site.damage=0;v.run('review_industry_program',v.host);assert(v.gate('industry_completion_is_proven'));const writes=v.nativeWrites.length;assert.equal(v.pay(10),10);assert.equal(v.nativeWrites.length,writes);assert.equal(v.host.vars[R+'granted_days'],30);assert.equal(v.actor.vars[P+'payment_new_days'],0);assert.equal(v.host.vars[R+'funded'],20);});
test('IND_NO_EARNED_COMPLETION healthy or expired observation denied',()=>{const v=new VM();v.bind();v.site.damage=0;assert.equal(v.pay(20),0);assert(!v.gate('industry_completion_is_proven'));const w=new VM();w.bind();w.pay(10);w.day=140;w.site.damage=0;w.run('review_industry_program',w.host);assert(!w.gate('industry_completion_is_proven'));assert.equal(w.pay(10),0);});
test('IND_CLOSED_TERM_CONSERVATION substitution/default/donor annex/secured Africa',()=>{const v=new VM();v.bind();v.pay(10);v.run('finish_industry_contract');v.run('clear_industry_terms');v.actor.exists=false;v.auth=false;v.run('review_industry_program',v.host);assert(v.host.flags.has(R+'reserved'));assert.equal(v.host.vars[R+'due_day'],130);assert.equal(v.site.modifiers.size,1);v.day=140;v.run('review_industry_program',v.host);assert(!v.host.flags.has(R+'reserved'));assert.equal(v.host.vars[P+'retired_funded'],10);assert.equal(v.host.vars[P+'retired_unpaid'],10);});
test('IND_ONE_SLOT_AND_DURATION_CAP finite native expiry without owner clock',()=>{for(const [q,d]of[[1,30],[20,60],[80,120]]){const v=new VM();v.bind(q);assert.equal(v.host.vars[R+'service_days'],d);assert(!v.gate('industry_candidate_is_available',v.host));v.pay(q);assert.equal(v.host.vars[R+'granted_days'],d);v.day+=d+1;assert(!v.test(parse('has_dynamic_modifier = { modifier = gods_of_africa_industry_repair_program scope = PREV }'),v.ctx(v.site,v.ctx(v.host))));}});
test('IND_REMOVE_FAILURE retains pointer and flags unresolved',()=>{const v=new VM();v.bind();v.pay(10);v.retireTuple();v.failRemove=true;v.run('retire_industry_program',v.host);assert(v.host.flags.has(R+'reserved'));assert(v.host.flags.has(R+'unresolved'));assert.equal(v.host.vars[R+'site'],v.site);});
test('IND_ZERO_DAY_PAYMENT rejects price-only increment',()=>{const v=new VM();v.bind();assert.equal(v.pay(.01),0);assert.equal(v.moneyWrites.length,0);});
test('IND_LOST_CAPACITY and wrong family reject without consumption',()=>{const v=new VM();v.bind();v.host.factories=0;assert.equal(v.pay(20),0);assert.equal(v.moneyWrites.length,0);v.host.factories=1;v.actor.vars.gods_of_africa_payment_amount=20;v.actor.vars.gods_of_africa_payment_family=constants['gods_of_africa_demand_family.fuel'];assert(!v.gate('industry_payment_can_execute'));});
test('IND_CLOSED_EXPIRED_REBIND leaves old receipt and rejects old callback',()=>{const v=new VM();v.bind();v.pay(10);v.retireTuple();const old={...v.temp};v.run('clear_industry_terms');v.day=140;assert(v.gate('industry_candidate_is_available',v.host));v.actor.vars.gods_of_africa_demand_id=12;v.bind();assert.equal(v.host.vars[R+'contract_id'],12);assert.equal(v.host.vars[P+'retired_funded'],10);v.temp=old;v.run('retire_industry_program',v.host);assert.equal(v.host.vars[R+'contract_id'],12);assert(v.host.flags.has(R+'reserved'));});
test('IND_REFUND_CANNOT_RESTORE_NATIVE retains unresolved bounded evidence',()=>{const v=new VM();v.bind();v.pay(10);v.day=110;v.failAdd=2;v.failAddDropsExisting=true;assert.equal(v.pay(10),0);assert.equal(v.actor.pp,90);assert.equal(v.host.pp,110);assert.equal(v.host.vars[R+'funded'],10);assert(v.host.flags.has(R+'unresolved'));assert.equal(v.pay(10),0);});
console.log(JSON.stringify({cases,sourceTests:true,nativeProof:false,externalAuthorizationPredicates:[...external],scope:'owner helpers only'}));
}
