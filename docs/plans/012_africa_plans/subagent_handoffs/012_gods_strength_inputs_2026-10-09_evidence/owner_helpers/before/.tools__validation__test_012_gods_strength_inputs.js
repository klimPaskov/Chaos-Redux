// Execute the production Strength territorial collector under typed source fixtures.
// Native map membership, engine arithmetic precision and scheduling remain unobserved.
const fs = require('fs'), assert = require('assert/strict');
const { parse, VM, effects, country, state } = require('./test_012_gods_industry_helpers.js');
const P = 'gods_of_africa_';
const file = 'common/scripted_effects/012_africa_gods_strength_inputs_effects.txt';
for (const n of parse(fs.readFileSync(file, 'utf8'))) effects[n.key] = n.value;
const collectionFile = 'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/collections/collections.txt';
const collectionSource = fs.readFileSync(collectionFile, 'utf8');
const start = collectionSource.search(/^states_in_africa\s*=\s*\{/m);
assert.ok(start >= 0);
let end = collectionSource.indexOf('{', start), depth = 0;
do { if (collectionSource[end] === '{') depth++; else if (collectionSource[end] === '}') depth--; end++; } while (depth > 0);
// The named block has no quoted brace or comment brace. Other vanilla blocks
// contain bare collection operators outside this effect parser's grammar.
const collection = parse(collectionSource.slice(start, end))[0].value;
assert.equal(collection.find(n => n.key === 'input').value, 'game:all_states');
const geography = collection.find(n => n.key === 'operators').value.find(n => n.key === 'limit').value;
class InputsVM extends VM {
	constructor() { super(); this.worldStates = []; }
	test(ns, c, mode = 'AND') {
		const mapped = ns.map(n => n.key === 'africa_is_current_host'
			? { key: c.scope === this.targets.africa_host ? 'AND' : 'NOT', value: [] } : n);
		return super.test(mapped, c, mode);
	}
	exec(ns, c) {
		for (const n of ns) {
			if (n.key === 'every_collection_element') {
				assert.equal(n.value.find(x => x.key === 'input').value, 'collection:states_in_africa');
				const body = n.value.filter(x => x.key !== 'input');
				for (const s of this.worldStates) {
					const child = this.ctx(s, c, c.root);
					if (this.test(geography, child)) this.exec(body, child);
				}
			} else super.exec([n], c);
		}
	}
}
const F = P + 'strength_', rows = [];
function test(name, fn) { fn(); rows.push(name); }
function read(v, field) { return v.host.vars[F + field]; }
function measure(v, root = v.host) { v.call(P + 'measure_territorial_control', v.ctx(v.host, null, root)); }
test('home cores are distinct from continental extent', () => {
	const v = new InputsVM();
	v.worldStates = Array.from({ length: 10 }, (_, i) => state(i + 1, i < 2 ? v.host : v.actor, 0));
	measure(v);
	assert.equal(read(v, 'african_state_total'), 10); assert.equal(read(v, 'african_secured_cores'), 2);
	assert.equal(read(v, 'territorial_control'), 20);
});
test('ownership control cores and Africa geography remain independent', () => {
	const v = new InputsVM(), third = country(3);
	const owned = state(1, v.host, 0); owned.controller = v.actor;
	const occupied = state(2, v.actor, 0); occupied.controller = v.host; occupied.core = v.host;
	const noncore = state(3, v.host, 0); noncore.core = v.actor;
	const secured = state(4, v.host, 0);
	const foreign = state(5, third, 0);
	const europe = state(6, v.host, 0); europe.continent = 'europe';
	v.worldStates = [owned, occupied, noncore, secured, foreign, europe]; measure(v);
	assert.equal(read(v, 'african_state_total'), 5); assert.equal(read(v, 'african_owned_states'), 3);
	assert.equal(read(v, 'african_controlled_states'), 3); assert.equal(read(v, 'african_secured_states'), 2);
	assert.equal(read(v, 'african_core_total'), 3); assert.equal(read(v, 'african_secured_cores'), 1);
	assert.equal(read(v, 'territorial_control'), 20);
});
test('capture reduces physical strength input without changing core claims', () => {
	const v = new InputsVM(); v.worldStates = [state(1, v.host, 0), state(2, v.host, 0)]; measure(v);
	assert.equal(read(v, 'territorial_control'), 100);
	v.worldStates[0].controller = v.actor; v.day++; measure(v);
	assert.equal(read(v, 'african_core_total'), 2); assert.equal(read(v, 'territorial_control'), 50);
	assert.equal(read(v, 'territory_observation_day'), v.day);
});
test('foreign native ROOT cannot receive the host measurement', () => {
	const v = new InputsVM(); v.worldStates = [state(1, v.host, 0)]; const root = country(8); measure(v, root);
	assert.equal(read(v, 'territorial_control'), 100); assert.deepEqual(root.vars, {});
});
test('empty geographic input fails to zero without division by zero', () => {
	const v = new InputsVM(); measure(v); assert.equal(read(v, 'african_state_total'), 0);
	assert.equal(read(v, 'territorial_control'), 0);
});
test('unauthorized former host cannot mutate existing measurements', () => {
	const v = new InputsVM(); v.host.vars[F + 'territorial_control'] = 17;
	v.targets.africa_host = v.actor; measure(v); assert.equal(read(v, 'territorial_control'), 17);
	assert.equal(read(v, 'african_state_total'), undefined);
});
console.log(JSON.stringify({ evidenceKind: 'SourceNoNativeProof', cases: rows.length, rows, integration: 'collector staged, owner and world comparison pending' }));
