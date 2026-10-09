// Event 012 protection relationship source cases. No game execution or file writes.
const fs = require('fs'), assert = require('assert/strict'), cp = require('child_process');
const { parse, assignment, hash } = require('../../docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03.js');
const P = 'gods_of_africa_', sources = new Map(), definitions = new Map(), constants = new Map();
function load(path) { const b = fs.readFileSync(path); sources.set(path, b); return parse(b.toString('utf8')); }
const field = (ns, key) => ns.find(n => n.key === key)?.value;
const block = (ns, key) => { const matches = ns.filter(n => n.key === key); assert.equal(matches.length, 1, key); return matches[0].value; };
for (const p of ['common/scripted_triggers/012_africa_gods_triggers.txt', 'common/scripted_triggers/012_africa_gods_contract_triggers.txt', 'common/scripted_triggers/012_africa_gods_epoch_binding_triggers.txt', 'common/scripted_triggers/012_africa_gods_protection_eligibility_triggers.txt']) for (const n of load(p)) definitions.set(n.key, n.value);
for (const p of ['common/script_constants/012_africa_gods_constants.txt', 'common/script_constants/012_africa_gods_contribution_constants.txt']) for (const cat of load(p)) for (const n of cat.value) if (!Array.isArray(n.value) && Number.isFinite(Number(n.value))) constants.set('constant:' + cat.key + '.' + n.key, Number(n.value));
const before = parse(fs.readFileSync('docs/plans/012_africa_plans/subagent_handoffs/012_gods_protection_eligibility_2026-10-08_evidence/before/common__scripted_triggers__012_africa_gods_triggers.txt', 'utf8'));
const oldGate = block(before, P + 'participant_can_receive_protection');
const newGate = definitions.get(P + 'participant_can_receive_protection');
const canonicalManifest = JSON.parse(fs.readFileSync('docs/plans/012_africa_plans/subagent_handoffs/012_gods_protection_canonical_completion_2026-10-09_evidence/before/manifest.json', 'utf8'));
const canonicalBefore = new Map();
for (const entry of canonicalManifest) {
 const bytes = fs.readFileSync(entry.snapshot); assert.equal(hash(bytes), entry.sha256, 'canonical baseline ' + entry.path);
 canonicalBefore.set(entry.path, parse(bytes.toString('utf8')));
}
const canonicalDefinitions = new Map(definitions);
for (const path of ['common/scripted_triggers/012_africa_gods_protection_eligibility_triggers.txt', 'common/scripted_triggers/012_africa_gods_triggers.txt'])
 for (const node of canonicalBefore.get(path)) canonicalDefinitions.set(node.key, node.value);
const canonicalOldGate = canonicalDefinitions.get(P + 'participant_can_receive_protection');
assert.equal(newGate.length, 1); assert.equal(newGate[0].key, 'custom_trigger_tooltip');
assert.deepEqual(newGate[0].value.filter(n => !['tooltip', P + 'protection_relationship_is_eligible'].includes(n.key)), oldGate.filter(n => !(n.key === 'has_country_flag' && n.value === P + 'reliable_memory_applied')));
const boundaries = new Set([P + 'participant_generation_is_current', P + 'participant_is_registered', P + 'active_host_is_valid']);
const usedBoundaries = new Set(), rows = [];
function fixture() {
 const country = name => ({ identity: Object.freeze({ country: name }), vars: new Map(), flags: new Set(), wars: new Set(), current: true, registered: true, active: true, eq: 10000, fuel: 10000, pp: 1000 });
 const host = country('host'), actor = country('participant'), third = country('third');
 actor.vars.set(P + 'wrath', 8); actor.vars.set(P + 'compliance_count', 3); actor.vars.set(P + 'demands_fulfilled', 3); actor.vars.set(P + 'voluntary_paid_infantry_k', 0.5); actor.flags.add(P + 'reliable_memory_applied'); host.vars.set('africa_common_defence_stockpile', 10000);
 return { host, actor, third, states: [], day: 100, targets: new Map([['africa_host', host]]) };
}
function evaluate(f, nodes, registry = definitions) {
 const ctx = { current: f.actor, previous: null, root: f.host, from: f.actor, temps: new Map() };
 function scope(token, c) { if (token === 'ROOT') return c.root; if (token === 'FROM') return c.from; if (token === 'PREV') return c.previous; if (token.startsWith('event_target:')) return f.targets.get(token.slice(13)); throw Error('Unsupported scope ' + token); }
 function value(token, c) { if (constants.has(token)) return constants.get(token); assert.ok(!token.startsWith('constant:'), token); if (Number.isFinite(Number(token))) return Number(token); if (token === 'global.num_days') return f.day; if (/^(ROOT|FROM|PREV)\./.test(token)) { const i = token.indexOf('.'); return scope(token.slice(0, i), c).vars.get(token.slice(i + 1)) ?? 0; } return c.temps.get(token) ?? c.current.vars.get(token) ?? 0; }
 function compare(a, b, op) { if (op === '=' || op === 'equals') return a === b; if (op === '<' || op === 'less_than') return a < b; if (op === '>' || op === 'greater_than') return a > b; if (op === 'greater_than_or_equals') return a >= b; throw Error('Unsupported comparison ' + op); }
 function all(ns, c) { return ns.every(n => test(n, c)); }
 function test(n, c) {
  if (['AND', 'custom_trigger_tooltip'].includes(n.key)) return all(n.value.filter(x => x.key !== 'tooltip'), c);
  if (n.key === 'OR') return n.value.some(x => test(x, c));
  if (n.key === 'NOT') return !all(n.value, c);
  if (n.key === 'has_variable') return c.current.vars.has(n.value);
  if (n.key === 'has_country_flag') return c.current.flags.has(n.value);
  if (n.key === 'has_event_target') return f.targets.has(n.value);
  if (n.key === 'has_war_with') return c.current.wars.has(scope(n.value, c).identity);
  if (n.key === 'check_variable') { const [a, b] = assignment(n); return compare(value(a, c), value(b, c), field(n.value, 'compare') ?? n.value[0].op); }
  if (n.key === 'set_temp_variable' || n.key === 'multiply_temp_variable') { const [a, b] = assignment(n), v = value(b, c); c.temps.set(a, n.key === 'set_temp_variable' ? v : c.temps.get(a) * v); return true; }
  if (n.key === 'has_equipment') return n.value.every(x => compare(c.current.eq, value(x.value, c), x.op));
  if (n.key === 'has_fuel') return compare(c.current.fuel, value(n.value, c), n.op);
  if (n.key === 'has_political_power') return compare(c.current.pp, value(n.value, c), n.op);
  if (n.key === 'any_owned_state' || n.key === 'any_controlled_state') return f.states.filter(s => (n.key === 'any_owned_state' ? s.owner : s.controller) === c.current).some(s => all(n.value, { ...c, current: s, previous: c.current }));
  if (n.key === 'is_on_continent') return c.current.continent === n.value;
  if (n.key === 'is_core_of') return c.current.cores.has(scope(n.value, c));
  if (n.key.startsWith('event_target:')) { const s = scope(n.key, c); assert.ok(s); return all(n.value, { ...c, current: s, previous: c.current }); }
  if (boundaries.has(n.key)) { usedBoundaries.add(n.key); const v = n.key.endsWith('generation_is_current') ? c.current.current : n.key.endsWith('is_registered') ? c.current.registered : c.current.active; return v === (n.value === 'yes'); }
  assert.ok(registry.has(n.key), 'Unknown native/helper ' + n.key); return all(registry.get(n.key), c) === (n.value === 'yes');
 }
 return all(nodes, ctx);
}
function scenario(id, mutate, expected) { const f = fixture(); mutate(f); const prior = evaluate(f, oldGate), canonicalPrior = evaluate(f, canonicalOldGate, canonicalDefinitions), after = evaluate(f, newGate); assert.equal(after, expected, id); rows.push({ id, before: prior, beforeCanonicalCorrection: canonicalPrior, after }); return f; }
scenario('STRONG_COOPERATION_AND_DELIVERED_AID', () => {}, true);
scenario('ALL_PARTIAL_CONTRACTS_COMPLETED', f => { f.actor.vars.set(P + 'compliance_count', 0); f.actor.flags.delete(P + 'reliable_memory_applied'); }, true);
scenario('COARSE_FULL_CLICKS_WITHOUT_CLOSED_LEDGER', f => { f.actor.vars.set(P + 'compliance_count', 100); f.actor.vars.set(P + 'demands_fulfilled', 0); }, false);
scenario('ONE_PAYMENT_HIGH_WRATH', f => { f.actor.vars.set(P + 'demands_fulfilled', 1); f.actor.vars.set(P + 'wrath', 90); }, false);
for (const wrath of [0, 29.999, 30, 70, 100]) scenario('WRATH_' + wrath, f => f.actor.vars.set(P + 'wrath', wrath), wrath < 30);
scenario('MISSING_WRATH', f => f.actor.vars.delete(P + 'wrath'), false);
scenario('TWO_COMPLETED_DEMANDS', f => f.actor.vars.set(P + 'demands_fulfilled', 2), false);
scenario('MISSING_CANONICAL_FULFILLMENT', f => f.actor.vars.delete(P + 'demands_fulfilled'), false);
scenario('NO_MEASURED_AID', f => f.actor.vars.delete(P + 'voluntary_paid_infantry_k'), false);
scenario('AID_ON_WRONG_ACTOR', f => { f.actor.vars.delete(P + 'voluntary_paid_infantry_k'); f.host.vars.set(P + 'voluntary_paid_infantry_k', 10); f.third.vars.set(P + 'voluntary_paid_infantry_k', 10); }, false);
scenario('ROOT_HOST_WRATH_DOES_NOT_DISQUALIFY_PARTNER', f => f.host.vars.set(P + 'wrath', 100), true);
for (const amount of [0, 0.001, 0.499, 0.5, 1]) scenario('RIFLE_AID_K_' + amount, f => f.actor.vars.set(P + 'voluntary_paid_infantry_k', amount), amount >= 0.5);
scenario('FUEL_AID', f => { f.actor.vars.delete(P + 'voluntary_paid_infantry_k'); f.actor.vars.set(P + 'voluntary_paid_fuel_k', 0.5); }, true);
scenario('COUNCIL_MEASURED_RIFLE_PLEDGE', f => { f.actor.vars.set(P + 'voluntary_paid_infantry_k', 1); f.actor.vars.delete(P + 'voluntary_aid_count'); }, true);
scenario('COARSE_AID_HISTORY_IS_NOT_DELIVERY', f => { f.actor.vars.delete(P + 'voluntary_paid_infantry_k'); f.actor.vars.set(P + 'aid_count', 100); }, false);
for (const flag of ['defiant', 'unresolved_treaty_break', 'unresolved_major_offense']) scenario(flag.toUpperCase(), f => f.actor.flags.add(P + flag), false);
scenario('WAR_WITH_AFRICA', f => f.actor.wars.add(f.host.identity), false);
scenario('OCCUPIES_AFRICAN_HOST_CORE', f => f.states.push({ continent: 'africa', owner: f.host, controller: f.actor, cores: new Set([f.host]) }), false);
scenario('OWNS_HOST_CORE_OCCUPIED_BY_THIRD_PARTY', f => f.states.push({ continent: 'africa', owner: f.actor, controller: f.third, cores: new Set([f.host]) }), false);
scenario('NON_AFRICAN_HOST_CORE', f => f.states.push({ continent: 'europe', owner: f.actor, controller: f.actor, cores: new Set([f.host]) }), true);
scenario('STALE_GENERATION', f => f.actor.current = false, false);
scenario('UNREGISTERED', f => f.actor.registered = false, false);
scenario('INACTIVE_HOST', f => f.host.active = false, false);
scenario('COOLDOWN_STILL_OPEN', f => f.actor.vars.set(P + 'protection_due_day', f.day + 1), false);
scenario('COOLDOWN_EXACT_END', f => f.actor.vars.set(P + 'protection_due_day', f.day), true);
const poor = scenario('ELIGIBLE_PARTNER_POOR_HOST', f => f.host.eq = 0, true);
assert.equal(evaluate(poor, definitions.get(P + 'protection_package_is_affordable')), false);
assert.deepEqual(rows.find(x => x.id === 'ALL_PARTIAL_CONTRACTS_COMPLETED'), { id: 'ALL_PARTIAL_CONTRACTS_COMPLETED', before: false, beforeCanonicalCorrection: false, after: true });
assert.deepEqual(rows.find(x => x.id === 'COARSE_FULL_CLICKS_WITHOUT_CLOSED_LEDGER'), { id: 'COARSE_FULL_CLICKS_WITHOUT_CLOSED_LEDGER', before: true, beforeCanonicalCorrection: true, after: false });
const currentEffect = load('common/scripted_effects/012_africa_gods_effects.txt');
const committedEffect = parse(cp.execFileSync('git', ['show', 'a2b23f1ef412b6c88e592ccca32a8d93b363064a:common/scripted_effects/012_africa_gods_effects.txt'], { encoding: 'utf8' }));
assert.deepEqual(block(currentEffect, P + 'protect_partner'), block(committedEffect, P + 'protect_partner'), 'Actual protection price and services unchanged');
const hashes = [...sources].map(([path, b]) => ({ path, sha256: hash(b) })); hashes.forEach(x => assert.equal(hash(fs.readFileSync(x.path)), x.sha256));
console.log(JSON.stringify({ evidenceKind: 'bounded_production_predicate_source_model', engineEvaluation: false, cases: rows.length, rows, assumedAuthorityBoundaries: [...usedBoundaries], sourceHashes: hashes, actualProtectionBodyPreserved: true }, null, 2));
