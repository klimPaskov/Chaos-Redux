/* Actual-source Event 012 foreach-break regression. Run from the mod root:
 * node .tools/tests/test_012_gods_iterator_isolation.js
 * Imports are silent and write-free. CLI emits finite JSON, no archive writes.
 * The mechanical before comparison uses the parent's raw .tmp snapshots and
 * patch_inventory.json in .tmp/012_gods_iterator_isolation when present.
 * Fresh checkouts derive the exact private-binding inventory and compare the
 * unchanged remaining AST against the pinned pre-fix Git commit 9cafe7cd2.
 * Evidence is SourceNoNativeProof. Typed objects, getters, native decisions,
 * state flags, equipment sends and rounding are declared host fixtures.
 * References already read by the parent: installed effects_documentation.md
 * 4279-4311; offline Data structures wiki 440-442 and 1216-1217. Foreach reads
 * an unscoped temporary break before each row. No foreach ceiling is imposed.
 */
'use strict';
const fs = require('node:fs'), path = require('node:path'), crypto = require('node:crypto');
const {spawnSync, execFileSync} = require('node:child_process');
const assert = require('node:assert/strict');
const { unhide } = require('./test_012_gods_industry_helpers.js');
const { InputsVM, parse, effects, triggers, constants, fixed, state, namedBlock, C, addCountry, P, F } = require('./test_012_gods_strength_inputs.js');
const { IntegrationVM, runSuite: strengthSuite, worldCensus, stageScalars, stageArrays, decorate, invoke, executeRetained, assertPrivateReset } = require('./test_012_gods_strength_integration.js');
const root = path.resolve(__dirname, '../..'), defaultBaseline = path.join(root, '.tmp/012_gods_iterator_isolation');
const main = 'common/scripted_effects/012_africa_gods_effects.txt';
const transfer = 'common/scripted_effects/012_africa_host_transfer_effects.txt';
const walk = ns => ns.flatMap(n => [n, ...(Array.isArray(n.value) ? walk(n.value) : [])]);
const field = (ns, key) => { const n = ns.find(x => x.key === key); assert(n, 'Missing source field ' + key); return n.value; };
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');

// Whole-file preservation includes native token lists (for example resources).
// The execution parser intentionally accepts only assignment bodies, so retain
// bare atoms here instead of removing or projecting unrelated source content.
function auditParse(text) {
	const tokens = (text.match(/"(?:\\.|[^"\\])*"|#[^\r\n]*|[{}=<>]|[^\s{}=<>#]+/g) || []).filter(t => !t.startsWith('#'));
	let at = 0;
	function block(nested) {
		const out = [];
		while (at < tokens.length && tokens[at] !== '}') {
			const key = tokens[at++];
			if (!['=', '<', '>'].includes(tokens[at])) { out.push({atom: key}); continue; }
			const op = tokens[at++]; let value = tokens[at++];
			if (value === '{') value = block(true);
			out.push({key, op, value});
		}
		if (nested) assert.equal(tokens[at++], '}');
		return out;
	}
	const ast = block(false); assert.equal(at, tokens.length); return ast;
}

function runSuite(baselineDir = defaultBaseline) {
	const results = [], evidence = {}, hashes = new Map(), bodies = new Map();
	const savedEffects = {...effects}, savedTriggers = {...triggers}, savedConstants = {...constants};
	let inventory;
	function read(p) {
		const absolute = path.isAbsolute(p) ? p : path.join(root, p), bytes = fs.readFileSync(absolute);
		hashes.set(absolute, sha(bytes)); return bytes.toString('utf8');
	}
	function test(name, fn) {
		try { fn(); results.push({name, passed: true}); }
		catch (e) { results.push({name, passed: false, error: e.message.slice(0, 1200), location: e.stack.split('\n').find(l => l.includes(__filename))?.trim()}); }
	}
	function install(file, names, store = effects) {
		const source = read(file);
		for (const name of names) { const body = namedBlock(source, name); store[name] = body; bodies.set(name, body); }
	}
	function poison(v) {
		v.temp.break = 1;
		for (const row of inventory) v.temp[row.breakVariable] = 1;
	}
	function foreignRoot() { const c = decorate(C(900000)); c.vars.foreign_marker = 41; c.flags.add('foreign_marker'); return c; }
	function foreignSnapshot(c) { return JSON.stringify({vars: c.vars, arrays: c.arrays, flags: [...c.flags]}); }
	function checkRoot(v, c, before) {
		assert.equal(foreignSnapshot(c), before, 'Foreign ROOT was mutated');
		assert.equal(v.temp.break, 1, 'Private loops changed the inherited default break');
		assert(v.foreachRuns.every(r => r.root === c.id), 'Iterator rebound native ROOT');
	}
	function rows(v, binding) { return v.foreachRuns.filter(r => r.breakVariable === binding).map(r => r.rows); }
	const declaredVariables = new Set(), declaredArrays = new Set();
	function declare() {
		for (const body of bodies.values()) for (const n of walk(body)) {
			if (n.key === 'has_variable' || /^(clear|round)_variable$/.test(n.key)) declaredVariables.add(n.value.replace(/^global\./, ''));
			if (/_variable$/.test(n.key) && Array.isArray(n.value)) declaredVariables.add((n.value.find(x => x.key === 'var')?.value || n.value[0].key).replace(/^global\./, ''));
			if (n.key === 'array' || n.key === 'clear_array') declaredArrays.add(n.value.replace(/^global\./, ''));
		}
	}
	class IteratorVM extends IntegrationVM {
		constructor() { super(); this.nativeOperations = []; this.flagCommits = []; this.executedHelpers = new Set(); }
		value(token, c) {
			if (token === 'num_equipment@infantry_equipment') { assert.equal(c.scope.type, 'country'); assert(Number.isFinite(c.scope.equipment)); return c.scope.equipment; }
			if (typeof token === 'string' && token.includes('^') && !token.includes('.')) {
				const [key, index] = token.split('^');
				if (declaredArrays.has(key)) { const array = c.scope.arrays[key] || []; return index === 'num' ? array.length : array[this.value(index, c)]; }
			}
			if (declaredArrays.has(token)) return c.scope.arrays[token] || [];
			if (declaredVariables.has(token) && !Object.hasOwn(this.temp, token)) return c.scope.vars[token] ?? 0;
			return super.value(token, c);
		}
		call(name, c, trigger = false) { this.executedHelpers.add(name); return super.call(name, c, trigger); }
		variable(n, c) {
			if (n.key.startsWith('clamp')) {
				const b = Object.fromEntries(n.value.map(x => [x.key, x.value])), store = n.key.includes('temp_variable') ? this.temp : c.scope.vars;
				store[b.var] = Math.min(b.max === undefined ? Infinity : this.value(b.max, c), Math.max(b.min === undefined ? -Infinity : this.value(b.min, c), store[b.var] ?? 0)); return;
			}
			return super.variable(n, c);
		}
		test(ns, c, mode = 'AND') {
			return super.test(ns.map(n => {
				let answer;
				if (n.key === 'has_war_with') { assert(c.scope.wars instanceof Set, 'Declared war fixture required'); answer = c.scope.wars.has(this.scope(n.value, c)); }
				if (n.key === 'has_equipment') { const x = n.value[0]; assert.equal(x.key, 'infantry_equipment'); answer = this.cmp(c.scope.equipment, this.value(x.value, c), x.op); }
				return answer === undefined ? n : {key: answer ? 'AND' : 'NOT', value: []};
			}), c, mode);
		}
		exec(ns, c) {
			for (let i = 0; i < ns.length; i++) {
				const n = ns[i];
				if (n.key === 'save_event_target_as') { this.targets[n.value] = c.scope; continue; }
				if (n.key === 'round_temp_variable') { this.temp[n.value] = Math.sign(this.temp[n.value]) * Math.floor(Math.abs(this.temp[n.value]) + 0.5); continue; }
				if (n.key === 'clr_state_flag') {
					assert.equal(c.scope.type, 'state'); this.nativeOperations.push({kind: n.key, id: c.scope.id, flag: n.value, changed: c.scope.flags.delete(n.value)}); continue;
				}
				if (n.key === 'remove_targeted_decision') {
					const target = this.scope(field(n.value, 'target'), c), decision = field(n.value, 'decision');
					assert(c.scope.missions instanceof Set, 'Declared native mission fixture required');
					this.nativeOperations.push({kind: n.key, owner: c.scope.id, target: target.id, decision, changed: c.scope.missions.delete(target.id + ':' + decision)}); continue;
				}
				if (n.key === 'send_equipment') {
					assert.equal(field(n.value, 'equipment'), 'infantry_equipment');
					const receiver = this.scope(field(n.value, 'target'), c), amount = this.value(field(n.value, 'amount'), c);
					assert(amount > 0 && amount <= c.scope.equipment); c.scope.equipment -= amount; receiver.equipment += amount;
					this.nativeOperations.push({kind: n.key, source: c.scope.id, receiver: receiver.id, amount}); continue;
				}
				if (n.key === 'while_loop_effect') {
					const limit = field(n.value, 'limit'), body = n.value.filter(x => x.key !== 'limit');
					// Documented while ceiling only. Foreach has no such fixture ceiling.
					for (let step = 0; step < 1000 && this.test(limit, c); step++) this.exec(body, c); continue;
				}
				if (n.key === 'set_country_flag') this.flagCommits.push({id: c.scope.id, flag: n.value, fresh: !c.scope.flags.has(n.value)});
				let end = i + 1;
				if (n.key === 'if') while (end < ns.length && ['else', 'else_if'].includes(ns[end].key)) end++;
				super.exec(ns.slice(i, end), c); i = end - 1;
			}
		}
	}
	try {
		test('all_144_exact_private_bindings_adjacent_resets_and_raw_before_AST_preservation', () => {
			const scratchInventory = path.join(baselineDir, 'patch_inventory.json');
			inventory = fs.existsSync(scratchInventory) ? JSON.parse(read(scratchInventory)) : [];
			const pinnedBefore = '9cafe7cd2';
			const ownerFiles = [
				'012_africa_gods_effects.txt', '012_africa_gods_focus_payoff_effects.txt',
				'012_africa_gods_punishment_effects.txt', '012_africa_gods_recovery_effects.txt',
				'012_africa_gods_settlement_effects.txt', '012_africa_gods_strength_inputs_effects.txt',
				'012_africa_host_transfer_effects.txt', '012_africa_world_order_effects.txt',
			];
			if (!inventory.length) {
				for (const name of ownerFiles) {
					const file = 'common/scripted_effects/' + name;
					for (const owner of auditParse(read(file))) for (const node of walk(Array.isArray(owner.value) ? owner.value : [])) {
						if (!['for_each_loop', 'for_each_scope_loop'].includes(node.key)) continue;
						const binding = node.value.find(x => x.key === 'break')?.value;
						if (binding && new RegExp('^' + owner.key + '_break_[1-9][0-9]*$').test(binding))
							inventory.push({path: file, owner: owner.key, loop: node.key, breakVariable: binding});
					}
				}
			}
			function beforeSource(file) {
				const rawSnapshot = path.join(baselineDir, path.basename(file) + '.before');
				if (fs.existsSync(rawSnapshot)) return read(rawSnapshot);
				return execFileSync('git', ['show', pinnedBefore + ':' + file], {cwd: root, encoding: 'utf8', maxBuffer: 8 * 1024 * 1024});
			}
			assert.equal(inventory.length, 144); assert.equal(new Set(inventory.map(r => r.breakVariable)).size, 144);
			const seen = new Set(); let previousExplicit = 0;
			for (const file of new Set(inventory.map(r => r.path))) {
				// Owners that 6f37b6085 removed as unreferenced dead code are absent from the current file.
				const removedOwners = new Set(['gods_of_africa_resolve_extension', 'gods_of_africa_terminate_system']);
				const current = auditParse(read(file)), before = auditParse(beforeSource(file)).filter(owner => !removedOwners.has(owner.key));
				for (const name of removedOwners) assert(!current.some(owner => owner.key === name), name + ' stays removed');
				function strip(ns, owner) {
					const result = [];
					for (let i = 0; i < ns.length; i++) {
						const n = ns[i], next = ns[i + 1];
						if (next && ['for_each_loop', 'for_each_scope_loop'].includes(next.key)) {
							const binding = next.value.find(x => x.key === 'break')?.value;
							const descriptor = inventory.find(r => r.path === file && r.owner === owner && r.breakVariable === binding);
							if (descriptor) {
								assert.equal(next.key, descriptor.loop); assertPrivateReset(n, next, owner); assert(!seen.has(binding), 'Duplicate private name ' + binding); seen.add(binding);
								assert.match(binding, new RegExp('^' + owner + '_break_[1-9][0-9]*$'));
								result.push({...next, value: strip(next.value.filter(x => x.key !== 'break'), owner)}); i++; continue;
							}
						}
						result.push(Array.isArray(n.value) ? {...n, value: strip(n.value, owner || n.key)} : n);
					}
					return result;
				}
				// Later intentional additions inside the otherwise unchanged owners. 17520e6b2 appended the Strength
				// refresh hook (test_012_gods_refresh_hooks pins each hook site), and 586ed38d0 made the successor copy
				// of the sponsorship target list reopen the obligation decision for targets that owe something.
				const laterAddition = n => (n.key === 'gods_of_africa_refresh_active_strength' && n.value === 'yes')
					|| (n.key === 'if' && n.value.some(x => x.key === 'activate_targeted_decision' && x.value.some(y => y.key === 'decision' && y.value === 'africa_world_sponsorship_obligation')));
				const withoutRefreshHook = ns => ns.filter(n => !laterAddition(n)).map(n => Array.isArray(n.value) ? {...n, value: withoutRefreshHook(n.value)} : n);
				// africa_world_install_current_package and africa_world_default_current_sponsorship_obligation were rewritten
				// by 586ed38d0 and c041810a8 (sponsorship guarantees, default penalties and the decision merge), so their
				// bodies are no longer comparable with the pinned source. Its loop bindings are still
				// verified by strip, and its ordinal sequence by the final ordinal check.
				const rewrittenAfterPin = new Set(['africa_world_install_current_package', 'africa_world_default_current_sponsorship_obligation']);
				const comparable = owners => owners.filter(owner => owner.key !== 'gods_of_africa_refresh_active_strength' && !rewrittenAfterPin.has(owner.key));
				assert.deepEqual(comparable(withoutRefreshHook(unhide(strip(current, null)))), comparable(unhide(before)), file + ': non-break AST changed');
				previousExplicit += walk(before).filter(n => ['for_each_loop', 'for_each_scope_loop'].includes(n.key) && n.value.some(x => x.key === 'break')).length;
			}
			assert.deepEqual([...seen].sort(), inventory.map(r => r.breakVariable).sort());
			for (const owner of new Set(inventory.map(r => r.owner))) {
				const owned = inventory.filter(r => r.owner === owner);
				assert.deepEqual(owned.map(r => r.breakVariable), owned.map((r, i) => owner + '_break_' + (i + 1)), owner + ': ordinal binding changed');
			}
			evidence.audit = {loops: seen.size, files: new Set(inventory.map(r => r.path)).size, allOtherASTUnchanged: true, previousExplicitForeach: previousExplicit};
		});
		if (results.some(r => !r.passed)) return finish();
		test('all_three_test_imports_silent_and_write_free', () => {
			const script = "const fs=require('node:fs'); for(const n of ['writeFileSync','appendFileSync','mkdirSync','renameSync','unlinkSync','rmSync','createWriteStream','writeFile','appendFile','mkdir','rename','unlink','rm']) fs[n]=()=>{throw Error('Import write: '+n)}; process.stdout.write=process.stderr.write=()=>{throw Error('Import output')}; for(const p of ['strength_inputs','strength_integration','iterator_isolation']) require('./.tools/tests/test_012_gods_'+p+'.js');";
			const child = spawnSync(process.execPath, ['-e', script], {cwd: root, encoding: 'utf8'});
			assert.equal(child.status, 0, child.error?.message || child.stderr); assert.equal(child.stdout, ''); assert.equal(child.stderr, '');
		});
		// Run the preserved 57 cases before adding any new fixture dependencies.
		test('original_57_consumer_cases_preserved_with_actual_adjacent_resets', () => {
			const r = strengthSuite(); assert.equal(r.cases, 57); assert.equal(r.passed, 57, JSON.stringify(r.failures.map(x => ({name: x.name, error: x.error.slice(0, 300)}))));
			evidence.consumer = {cases: r.cases, passed: r.passed};
		});
		install(transfer, ['africa_host_transfer_cancel_active_actions']);
		install('common/scripted_effects/012_africa_gods_settlement_effects.txt', ['refresh_settlement_owed_totals', 'deliver_settlement_obligations', 'measure_settlement_equipment_budget', 'measure_settlement_fuel_budget', 'measure_settlement_fuel_basis', 'send_settlement_equipment', 'send_settlement_fuel'].map(n => P + n));
		install('common/scripted_triggers/012_africa_gods_settlement_triggers.txt', ['final_settlement_value_is_valid', 'settlement_receipt_is_owed_by_source', 'settlement_receipt_can_receive_batch', 'settlement_source_has_pending_delivery'].map(n => P + n), triggers);
		install('common/scripted_effects/012_africa_gods_equipment_effects.txt', [P + 'floor_equipment_amount']);
		install('common/scripted_effects/012_africa_gods_grading_effects.txt', [P + 'floor_temporary_value']);
		for (const file of ['common/script_constants/012_africa_gods_grading_constants.txt', 'common/script_constants/012_africa_gods_contribution_constants.txt']) {
			for (const cat of parse(read(file))) for (const n of cat.value) if (typeof n.value === 'string' && Number.isFinite(Number(n.value))) constants[cat.key + '.' + n.key] = Number(n.value);
		}
		for (const name of ['africa_host_transfer_restore_world_order_state', P + 'close_recovery_requests', P + 'clear_recovery_member_request']) bodies.set(name, effects[name]);
		declare();
		test('actual_census_and_sampler_twice_poisoned_default_and_every_private_break', () => {
			const v = new IteratorVM(), foreign = foreignRoot(), before = foreignSnapshot(foreign);
			const a = decorate(addCountry(v, C(3, 11))), b = decorate(addCountry(v, C(4, 13))); b.exists = false;
			for (let call = 0; call < 2; call++) {
				poison(v); executeRetained(v, worldCensus, v.ctx(v.host, null, foreign)); invoke(v, 'measure_strength_armies', v.host, foreign);
				assert.deepEqual(v.host.arrays[F + 'countries'], v.worldCountries); assert.equal(v.host.arrays[F + 'countries'].length, new Set(v.host.arrays[F + 'countries']).size);
				assert.equal(v.host.vars[F + 'world_army_k'], 20011); assert.equal(v.host.vars[F + 'army_processed_count'], 4);
				assert.equal(v.temp.gods_of_africa_measure_strength_armies_break_1, 0); assert.equal(v.temp.africa_initialize_scramble_and_world_packages_break_1, 0);
				assert(!Object.hasOwn(v.temp, F + 'row_army_k'), 'Helper-created row temporary leaked');
			}
			assert.deepEqual(rows(v, 'africa_initialize_scramble_and_world_packages_break_1'), [[1, 2, a.id, b.id], [1, 2, a.id, b.id]]);
			assert.deepEqual(rows(v, P + 'measure_strength_armies_break_1'), [[1, 2, a.id, b.id], [1, 2, a.id, b.id]]);
			assert.equal(v.host.arrays[P + 'candidate_registry'].length, 3, 'Repeated census duplicated candidate registration');
			checkRoot(v, foreign, before); evidence.census = {calls: 2, rowsPerCall: 4, sumK: 20011, uniqueCensus: 4, uniqueCandidates: 3};
		});
		test('actual_sampler_more_than_1000_retained_objects_twice_without_foreach_ceiling', () => {
			const v = new IteratorVM(), foreign = foreignRoot(), before = foreignSnapshot(foreign);
			for (let id = 3; id <= 1007; id++) decorate(addCountry(v, C(id, 1)));
			poison(v); executeRetained(v, worldCensus, v.ctx(v.host, null, foreign));
			for (let call = 0; call < 2; call++) { poison(v); invoke(v, 'measure_strength_armies', v.host, foreign); assert.equal(v.host.vars[F + 'world_army_k'], 21005); assert.equal(v.host.vars[F + 'army_processed_count'], 1007); }
			assert.deepEqual(rows(v, P + 'measure_strength_armies_break_1').map(x => x.length), [1007, 1007]);
			checkRoot(v, foreign, before); evidence.largeRoster = {objects: 1007, calls: 2, visited: 2014, sumK: 21005, nativeLimitClaim: false};
		});
		test('actual_recognition_two_majors_twice_preserves_foreign_ROOT', () => {
			const v = new IteratorVM(), foreign = foreignRoot(), before = foreignSnapshot(foreign), second = decorate(addCountry(v, C(3)));
			for (const c of [v.actor, second]) { c.major = true; c.flags.add(P + 'recognition_granted'); }
			v.host.arrays[P + 'participants'] = [v.actor, second]; executeRetained(v, worldCensus, v.ctx(v.host, null, foreign)); invoke(v, 'measure_strength_armies', v.host, foreign);
			for (let call = 0; call < 2; call++) { poison(v); invoke(v, 'refresh_strength', v.host, foreign); assert.equal(v.host.vars[P + 'recognising_major_count'], 2); assert.equal(v.componentFrames.at(-1).continent, 75); }
			assert.deepEqual(rows(v, P + 'refresh_strength_break_1'), [[2, 3], [2, 3]]); checkRoot(v, foreign, before);
		});
		test('actual_staging_and_restore_twice_preserve_all_rows_and_successor_identity', () => {
			const v = new IteratorVM(), foreign = foreignRoot(), before = foreignSnapshot(foreign), old = v.host, next = v.actor;
			poison(v); executeRetained(v, worldCensus, v.ctx(old, null, foreign));
			for (let call = 0; call < 2; call++) { poison(v); executeRetained(v, stageScalars, v.ctx(old, null, foreign)); executeRetained(v, stageArrays, v.ctx(old, null, foreign)); assert.deepEqual(v.global.arrays.africa_host_transfer_strength_countries, v.worldCountries); }
			v.globalFlags.add('africa_host_transfer_scramble_state_machine_initialised'); v.targets.africa_host = next; v.targets.africa_host_transfer_new_host = next;
			Object.assign(next.vars, {africa_host_generation: 2, africa_origin_host_id: 1}); next.flags.add('africa_unifier_host'); next.flags.add('africa_host_commit_completed');
			for (let call = 0; call < 2; call++) { poison(v); invoke(v, 'africa_host_transfer_restore_world_order_state', next, foreign); assert.deepEqual(next.arrays[F + 'countries'], v.worldCountries); assert.equal(next.vars[F + 'census_host_id'], 2); assert.equal(next.vars[F + 'census_generation'], 2); assert.equal(next.vars[F + 'world_army_k'], undefined); assert(!next.flags.has(P + 'epoch_authorized')); }
			assert.deepEqual(rows(v, 'africa_host_transfer_stage_arrays_break_3'), [[1, 2], [1, 2]]);
			assert.deepEqual(rows(v, 'africa_host_transfer_restore_world_order_state_break_2'), [[1, 2], [1, 2]]); checkRoot(v, foreign, before);
		});
		test('actual_recovery_cleanup_two_members_twice_no_stale_member_receipts', () => {
			const v = new IteratorVM(), foreign = foreignRoot(), before = foreignSnapshot(foreign), second = decorate(addCountry(v, C(3)));
			v.host.arrays[P + 'recovery_invited_members'] = [v.actor, second];
			for (const c of [v.actor, second]) { c.vars[P + 'recovery_request_host_id'] = 1; c.flags.add(P + 'recovery_invited'); }
			for (let call = 0; call < 2; call++) { poison(v); invoke(v, 'close_recovery_requests', v.host, foreign); for (const c of [v.actor, second]) { assert.equal(c.vars[P + 'recovery_request_host_id'], undefined); assert(!c.flags.has(P + 'recovery_invited')); } }
			assert.deepEqual(rows(v, P + 'close_recovery_requests_break_1'), [[2, 3], []]); checkRoot(v, foreign, before);
		});
		test('actual_host_transfer_nested_two_participants_two_state_receipts_exact_cleanup', () => {
			const v = new IteratorVM(), foreign = foreignRoot(), before = foreignSnapshot(foreign), second = decorate(addCountry(v, C(3))), flag = 'africa_continental_peace_exemption_active';
			v.targets.africa_previous_host = v.host; v.host.missions = new Set(); v.host.arrays.africa_active_action_targets = [];
			v.host.arrays.africa_peace_exemption_countries = [v.actor, second];
			for (const c of [v.actor, second]) {
				const sites = [state(c.id * 100 + 1, c, 0), state(c.id * 100 + 2, c, 0)]; sites.forEach(s => s.flags.add(flag));
				c.arrays.africa_continental_peace_exemption_states = sites; c.flags.add('africa_continental_peace_terms_accepted');
				v.host.missions.add(c.id + ':mission_africa_complete_continental_peace_exemption');
			}
			for (let call = 0; call < 2; call++) { poison(v); invoke(v, 'africa_host_transfer_cancel_active_actions', v.host, foreign); }
			assert.deepEqual(rows(v, 'africa_host_transfer_cancel_active_actions_break_3'), [[2, 3], []]);
			assert.deepEqual(rows(v, 'africa_host_transfer_cancel_active_actions_break_4'), [[201, 202], [301, 302]]);
			assert.equal(v.nativeOperations.filter(x => x.kind === 'clr_state_flag' && x.changed).length, 4);
			assert.equal(v.nativeOperations.filter(x => x.kind === 'remove_targeted_decision' && x.changed).length, 2);
			assert.equal(v.nativeOperations.length, 6, 'Repeated call duplicated native cleanup');
			for (const c of [v.actor, second]) { assert.deepEqual(c.arrays.africa_continental_peace_exemption_states, []); assert(!c.flags.has('africa_continental_peace_terms_accepted')); }
			checkRoot(v, foreign, before); evidence.nested = {calls: 2, participants: 2, receiptsPerParticipant: 2, exactStateClosures: 4, exactMissionClosures: 2};
		});
		test('actual_settlement_four_passes_exact_paid_receipts_and_unresolved_retention_twice', () => {
			const v = new IteratorVM(), foreign = foreignRoot(), before = foreignSnapshot(foreign), second = decorate(addCountry(v, C(3))), unresolved = decorate(addCountry(v, C(4)));
			v.host.flags.add(P + 'final_settlement_committed'); v.host.flags.add(P + 'settlement_delivery_initialized');
			v.host.vars[P + 'reward_equipment_owed_total_k'] = 0.006; v.host.vars.africa_common_defence_stockpile = 10000;
			v.host.equipment = 10000; v.host.getters['num_target_equipment_in_armies_k@infantry_equipment'] = 0; v.host.getters.fuel_k = 0;
			v.host.arrays[P + 'candidate_registry'] = [v.actor, second, unresolved];
			for (const c of [v.actor, second, unresolved]) {
				c.equipment = 0; c.wars = new Set(c === unresolved ? [v.host] : []);
				c.flags.add(P + 'settlement_obligation_committed'); c.flags.add(P + 'settlement_delivery_pending');
				Object.assign(c.vars, {[P + 'final_settlement']: constants['gods_of_africa_settlement.favored'], [P + 'reward_receiver_id']: c.id, [P + 'reward_source_id']: 1, [P + 'reward_source_generation']: 1, [P + 'reward_source_origin_id']: 1, [P + 'reward_equipment_owed']: 2, [P + 'reward_fuel_owed']: 0});
			}
			const pendingBefore = {...unresolved.vars};
			for (let call = 0; call < 2; call++) { poison(v); invoke(v, 'deliver_settlement_obligations', v.host, foreign); }
			for (const c of [v.actor, second]) { assert.equal(c.equipment, 2); assert.equal(c.vars[P + 'reward_equipment_delivered'], 2); assert.equal(c.vars[P + 'reward_equipment_owed'], 0); assert(c.flags.has(P + 'settlement_reward_granted')); }
			assert.equal(v.nativeOperations.filter(x => x.kind === 'send_equipment').length, 2); assert.equal(v.host.equipment, 9996);
			assert.equal(v.flagCommits.filter(x => x.flag === P + 'settlement_reward_granted').length, 2, 'Duplicate settlement receipt');
			assert.equal(v.flagCommits.filter(x => x.flag === P + 'settlement_reward_granted' && x.fresh).length, 2);
			assert.equal(unresolved.vars[P + 'reward_equipment_owed'], pendingBefore[P + 'reward_equipment_owed']); assert(unresolved.flags.has(P + 'settlement_delivery_pending')); assert(!unresolved.flags.has(P + 'settlement_reward_granted'));
			assert.equal(unresolved.vars[P + 'reward_source_id'], pendingBefore[P + 'reward_source_id']); assert.deepEqual(v.host.arrays[P + 'candidate_registry'], [v.actor, second, unresolved]);
			for (let ordinal = 1; ordinal <= 4; ordinal++) assert.deepEqual(rows(v, P + 'deliver_settlement_obligations_break_' + ordinal), [[2, 3, 4], [2, 3, 4]]);
			checkRoot(v, foreign, before); evidence.settlement = {calls: 2, passesPerCall: 4, rowsPerPass: 3, exactShipments: 2, exactReceipts: 2, unresolvedOwed: 2, unresolvedReceiptRetained: true};
		});
		test('actual_before_sampler_detects_inherited_default_break_regression', () => {
			const v = new IteratorVM(), foreign = foreignRoot(); executeRetained(v, worldCensus, v.ctx(v.host, null, foreign)); poison(v);
			const rawPath = path.join(baselineDir, '012_africa_gods_strength_inputs_effects.txt.before');
			const rawText = fs.existsSync(rawPath) ? read(rawPath) : execFileSync('git', ['show', '9cafe7cd2:common/scripted_effects/012_africa_gods_strength_inputs_effects.txt'], {cwd: root, encoding: 'utf8', maxBuffer: 1024 * 1024});
			const raw = namedBlock(rawText, P + 'measure_strength_armies');
			executeRetained(v, raw, v.ctx(v.host, null, foreign)); assert.deepEqual(rows(v, 'break'), [[]]);
			assert.equal(v.host.vars[F + 'army_processed_count'], 0); assert(!v.host.flags.has(F + 'army_sample_valid'));
			// The failed before body marks coverage incomplete. Re-arm through the
			// real owner-boundary finish helper rather than erasing its receipt.
			invoke(v, 'finish_strength_census', v.host, foreign); invoke(v, 'measure_strength_armies', v.host, foreign);
			assert.equal(v.host.vars[F + 'army_processed_count'], 2); assert.equal(v.host.vars[F + 'world_army_k'], 20000);
		});
		test('actual_helper_frame_discards_new_break_storage_retains_preinitialized_inputs', () => {
			const v = new IteratorVM(); executeRetained(v, worldCensus, v.ctx(v.host));
			v.temp.break = 1; invoke(v, 'measure_strength_armies'); assert(!Object.hasOwn(v.temp, P + 'measure_strength_armies_break_1'));
			v.temp[P + 'measure_strength_armies_break_1'] = 1; invoke(v, 'measure_strength_armies'); assert.equal(v.temp[P + 'measure_strength_armies_break_1'], 0); assert.equal(v.temp.break, 1);
			assert(!Object.hasOwn(v.temp, F + 'row_army_k'));
		});
		test('source_identity_stable_during_replay', () => { for (const [file, hash] of hashes) assert.equal(sha(fs.readFileSync(file)), hash, 'Concurrent source edit: ' + file); });
		return finish();
	} finally {
		for (const [store, old] of [[effects, savedEffects], [triggers, savedTriggers], [constants, savedConstants]]) {
			for (const key of Object.keys(store)) if (!Object.hasOwn(old, key)) delete store[key]; Object.assign(store, old);
		}
	}
	function finish() {
		return {evidenceKind: 'SourceNoNativeProof', cases: results.length, passed: results.filter(r => r.passed).length, failures: results.filter(r => !r.passed), results, evidence,
			declaredNativeGetters: ['global.countries', 'global.countries^num', 'global.num_days', 'id', 'deployed_army_manpower_k', 'num_divisions', 'num_target_equipment_in_armies_k@infantry_equipment', 'num_equipment_in_armies_k@infantry_equipment', 'max_fuel_k', 'fuel_k', 'num_equipment@infantry_equipment', 'num_of_civilian_factories', 'num_of_military_factories', 'stability', 'surrender_progress'],
			limitations: ['All 144 changed foreach loops are scope iterators. No numeric foreach or intentional foreach early-exit source exists in the audited owner surface, so neither was manufactured.', 'Equipment stocks, sends, wars, missions, typed retained objects, native getters and rounding are declared fixtures, not engine observations.', 'Only the production census and Strength staging subtrees execute from the larger World and transfer wrappers. The complete restoration, nested cancellation and settlement helpers execute.', 'No native foreach ceiling inferred. No game, GUI, AI, workbook or Git action.'],
			sourceHashes: [...hashes].map(([file, hash]) => ({path: path.relative(root, file).replace(/\\/g, '/'), sha256: hash}))};
	}
}
module.exports = {runSuite};
if (require.main === module) {
	const result = runSuite(); console.log(JSON.stringify({evidenceKind: result.evidenceKind, failures: result.failures, cases: result.cases, passed: result.passed, evidence: result.evidence, limitations: result.limitations}));
	process.exitCode = result.failures.length ? 1 : 0;
}
