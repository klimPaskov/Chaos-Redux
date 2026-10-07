// Bounded actual-source doctrine regression and budget audit. No HOI4 execution.
// Run from the mod root: node docs/testing/2026-10-07_doctrine_reward_budget_source_tests.js
// Parser follows exact_quote_source_tests.js, adding anonymous database list blocks.
// No shared parser, engine source, index, balance source, or AI source is modified.
const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict'), crypto = require('node:crypto');
const root = path.resolve(__dirname, '../..');
const baseline = 'docs/testing/2026-10-07_doctrine_reward_revision/before/';
const grand = 'common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt';
const grandBaseline = 'docs/testing/2026-10-07_doctrine_revision_probability/before/' + grand;
const shared = 'common/script_constants/cbrn_doctrine_constants.txt';
const tech = 'common/technologies/chaosx_technologies.txt';
const tracks = [
 ['infantry', 'extermination_columns', 12, ['cbrn_gas_mask_decon_detachment', 'cbrn_chemical_recon_detachment', 'cbrn_medical_countermeasure_detachment', 'cbrn_biosecurity_assault_detachment', 'chaos_battalion']],
 ['combat_support', 'contaminant_firebases', 16, ['cbrn_chemical_projector_battery', 'cbrn_chemical_ammunition_train', 'cbrn_medical_countermeasure_detachment']],
 ['armor', 'chemical_suppression', 14, ['cbrn_light_armored_delivery_detachment', 'cbrn_medium_armored_delivery_detachment', 'cbrn_heavy_armored_delivery_detachment']],
 ['operations', 'integrated_chemical_operations', 14, ['cbrn_hq_operations_section', 'cbrn_hq_protective_logistics_section', 'cbrn_hq_medical_countermeasure_directorate', 'cbrn_gas_mask_decon_detachment', 'cbrn_chemical_recon_detachment', 'cbrn_medical_countermeasure_detachment']],
].map(([track, id, multiplier, roster]) => ({track, id, multiplier, roster, file: `common/doctrines/subdoctrines/land/chaos_warfare_${track}_subdoctrines.txt`}));
const hash = b => crypto.createHash('sha256').update(b).digest('hex');
const inputs = new Map(), parsed = new Map(), tests = [];
function parse(text) {
 const tokens = (text.match(/#[^\r\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>#]+/g) || []).filter(t => !t.startsWith('#'));
 let i = 0;
 function body(nested = false) {
  const nodes = [];
  while (i < tokens.length && tokens[i] !== '}') {
   const key = tokens[i++];
   if (key === '{') { nodes.push({key: null, op: null, value: body(true)}); continue; }
   if (!['=', '<', '>'].includes(tokens[i])) { nodes.push({key, op: null, value: key, atom: true}); continue; }
   const op = tokens[i++]; let value = tokens[i++];
   assert(value !== undefined, `missing value after ${key}`);
   if (value === '{') value = body(true);
   nodes.push({key, op, value});
  }
  if (nested) assert.equal(tokens[i++], '}', 'unterminated block');
  return nodes;
 }
 const result = body(); assert.equal(i, tokens.length); return result;
}
function read(file) {
 if (!inputs.has(file)) inputs.set(file, fs.readFileSync(path.join(root, file)));
 return inputs.get(file).toString('utf8');
}
const walk = nodes => nodes.flatMap(n => [n, ...(Array.isArray(n.value) ? walk(n.value) : [])]);
function document(file) {
 if (parsed.has(file)) return parsed.get(file);
 const raw = parse(read(file)), locals = new Map(walk(raw).filter(n => n.key?.startsWith('@')).map(n => [n.key, n.value]));
 const resolve = value => {
  if (typeof value !== 'string') return value;
  if (value.startsWith('@')) { assert(locals.has(value), `${file}: unknown ${value}`); return resolve(locals.get(value)); }
  return /^-?\d+(\.\d+)?$/.test(value) ? Number(value) : value;
 };
 const normalize = nodes => nodes.filter(n => !n.key?.startsWith('@')).map(n => ({...n, value: Array.isArray(n.value) ? normalize(n.value) : n.atom ? n.value : resolve(n.value)}));
 const result = {file, raw, locals, nodes: normalize(raw), resolve}; parsed.set(file, result); return result;
}
const get = (nodes, key) => { const matches = nodes.filter(n => n.key === key); assert.equal(matches.length, 1, `expected one ${key}`); return matches[0].value; };
const optional = (nodes, key) => nodes.find(n => n.key === key)?.value;
const atoms = nodes => nodes.map(n => { assert(n.atom, 'expected a bare token'); return n.key; });
const num = x => { assert.equal(typeof x, 'number', `unresolved numeric source ${x}`); return x; };
const sum = xs => xs.reduce((a, b) => a + b, 0);
const product = xs => xs.reduce((a, b) => a * (1 + b), 1);
const approx = (actual, expected) => assert(Math.abs(actual - expected) < 1e-10, `${actual} != ${expected}`);
function test(name, action) { try { action(); tests.push({name, status: 'passed'}); } catch (error) { tests.push({name, status: 'failed', reason: error.message}); } }
function listFiles(directory) { return fs.readdirSync(path.join(root, directory), {withFileTypes: true}).flatMap(e => e.isDirectory() ? listFiles(directory + '/' + e.name) : [directory + '/' + e.name]); }

const units = new Map(), unitOccurrences = new Map();
for (const file of listFiles('common/units').filter(f => f.endsWith('.txt') && !f.includes('/equipment/') && !f.includes('/names_divisions/'))) {
 const d = document(file), blocks = optional(d.nodes, 'sub_units'); if (!blocks) continue;
 for (const n of blocks) {
  if (!Array.isArray(n.value)) continue;
  if (!unitOccurrences.has(n.key)) unitOccurrences.set(n.key, []);
  unitOccurrences.get(n.key).push(file);
  units.set(n.key, {file, body: n.value, categories: atoms(optional(n.value, 'categories') || []), manpower: optional(n.value, 'manpower'), org: optional(n.value, 'max_organisation'), stats: Object.fromEntries(['soft_attack', 'hard_attack', 'breakthrough', 'defense'].map(s => [s, optional(n.value, s) ?? 0]))});
 }
}
const retained = [...get(document('common/units/cbrn_regimental_support.txt').nodes, 'sub_units'), ...get(document('common/units/cbrn_hq_support.txt').nodes, 'sub_units')].filter(n => Array.isArray(n.value)).map(n => n.key);
const chemical = retained.filter(id => units.get(id).categories.includes('category_chemical_support_companies'));
test('retained roster has exactly 13 unique real definitions', () => { assert.equal(retained.length, 13); assert.equal(new Set(retained).size, 13); for (const id of retained) assert.equal(unitOccurrences.get(id).length, 1, id); });
test('retained chemical membership is only projector plus three armored deliveries', () => assert.deepEqual(chemical.slice().sort(), ['cbrn_chemical_projector_battery', ...tracks.find(t => t.track === 'armor').roster].sort()));
test('Protection Company is not chemical support', () => assert(!units.get('cbrn_gas_mask_decon_detachment').categories.includes('category_chemical_support_companies')));
const categoryTokens = new Set(atoms(get(document('common/unit_tags/chaosx_categories.txt').nodes, 'sub_unit_categories')));
test('retained CBRN category memberships resolve to declared categories', () => { for (const id of retained) for (const c of units.get(id).categories.filter(c => c.startsWith('category_cbrn') || c === 'category_chemical_support_companies')) assert(categoryTokens.has(c), `${id}: ${c}`); });

const doctrines = stage => [
 {id: 'chaos_warfare', file: stage === 'before' ? grandBaseline : grand, body: get(document(stage === 'before' ? grandBaseline : grand).nodes, 'chaos_warfare')},
 ...tracks.map(t => ({id: t.id, file: stage === 'before' ? baseline + t.file : t.file, body: get(document(stage === 'before' ? baseline + t.file : t.file).nodes, t.id)})),
];
const steps = d => [{id: d.id + '/adoption', body: d.body}, ...(optional(d.body, 'rewards') || []).map(r => ({id: d.id + '/rewards/' + r.key, body: r.value}))];
const allowed = {
 infantry: ['mastery/sub_units', 'category_cbrn_assault_battalions/breakthrough', 'category_cbrn_primary_protection/reliability', 'rewards/contagion_assault_drills/category_cbrn_primary_protection/reliability', 'rewards/unlock_chaos_battalion/category_cbrn_assault_battalions/breakthrough', 'rewards/ruinwave_battlecells/category_cbrn_assault_battalions/breakthrough', 'rewards/terminal_contagion_offensive/category_cbrn_assault_battalions/breakthrough', 'rewards/terminal_contagion_offensive/chaos_battalion/breakthrough'],
 armor: ['mastery/sub_units', 'category_cbrn_armored_delivery_support/breakthrough', 'rewards/adamsite_emission_cells/category_cbrn_armored_delivery_support/reliability', 'rewards/sealed_pressure_logistics/category_cbrn_armored_delivery_support/breakthrough', 'rewards/sealed_pressure_logistics/category_cbrn_armored_delivery_support/reliability', 'rewards/catastrophic_shock_breakthrough/category_cbrn_armored_delivery_support/reliability'],
 combat_support: ['mastery/sub_units', 'category_line_artillery/soft_attack', 'category_support_artillery/soft_attack', 'rewards/livens_fire_control_cells/category_support_artillery/soft_attack', 'rewards/livens_fire_control_cells/category_chemical_support_companies/max_organisation', 'rewards/livens_fire_control_cells/cbrn_chemical_projector_battery/max_organisation', 'rewards/counterbattery_gas_synchronization/category_line_artillery/soft_attack', 'rewards/counterbattery_gas_synchronization/category_support_artillery/soft_attack', 'rewards/persistent_agent_distribution/category_line_artillery/soft_attack', 'rewards/deep_contamination_fireplans/category_support_artillery/soft_attack'],
 operations: ['mastery/sub_units', 'recon_factor', 'rewards/operational_recon_grids/recon_factor', 'rewards/theater_intelligence_overmatch/recon_factor'],
};
function omit(nodes, ignored, parent = '') {
 return nodes.flatMap(n => {
  const p = parent ? parent + '/' + n.key : n.key;
  if (ignored.includes(p)) return [];
  if (!Array.isArray(n.value)) return [n];
  const value = omit(n.value, ignored, p);
  return value.length || !n.value.length ? [{...n, value}] : [];
 });
}
const rosterEvidence = [];
for (const t of tracks) {
 const before = get(document(baseline + t.file).nodes, t.id), after = get(document(t.file).nodes, t.id);
 test(t.track + ': entire AST preserved except exact permitted reward/roster fields', () => assert.deepEqual(omit(after, allowed[t.track]), omit(before, allowed[t.track])));
 test(t.track + ': explicit mastery roster, no duplicate, category or equipment filter', () => { const m = get(after, 'mastery'); assert.deepEqual(atoms(get(m, 'sub_units')), t.roster); assert.equal(new Set(t.roster).size, t.roster.length); assert(!optional(m, 'categories')); assert(!optional(m, 'equipment')); assert(t.roster.every(id => retained.includes(id))); });
 test(t.track + ': existing multiplier, 100 XP and five threshold-100 rewards retained', () => { assert.equal(get(get(after, 'mastery'), 'multiplier'), t.multiplier); assert.equal(get(after, 'xp_cost'), 100); const rewards = get(after, 'rewards'); assert.equal(rewards.length, 5); for (const r of rewards) assert.equal(get(r.value, 'mastery'), 100); });
 rosterEvidence.push({track: t.track, multiplier: t.multiplier, before: atoms(get(get(before, 'mastery'), 'sub_units')), after: t.roster});
}
test('all 13 retained roles occur in mastery with no retired contributor', () => assert.deepEqual([...new Set(tracks.flatMap(t => t.roster))].sort(), retained.slice().sort()));
test('grand doctrine AST unchanged against separately captured probability baseline', () => assert.deepEqual(document(grand).nodes, document(grandBaseline).nodes));
test('technology AST unchanged except two numerical tuning mirrors', () => {
 const old = document(baseline + tech), current = document(tech);
 const patchedRaw = structuredClone(old.raw);
 for (const n of walk(patchedRaw)) {
  if (n.key === '@CHAOS_ASSAULT_IMPROVED_BREAKTHROUGH') n.value = '0.04';
  if (n.key === '@CBRN_PROJECTOR_TECH_BREAKTHROUGH') n.value = '0.065';
 }
 assert.deepEqual(patchedRaw, current.raw);
});
test('shared policy, cost, timing, AI, spirit and lifecycle tuning ASTs retained', () => { const old = document(baseline + shared).nodes, current = document(shared).nodes; assert.deepEqual(current.filter(n => n.key !== 'cbrn_doctrine_modifier'), old.filter(n => n.key !== 'cbrn_doctrine_modifier')); });
const modifierTable = get(document(shared).nodes, 'cbrn_doctrine_modifier');
for (const t of tracks) test(t.track + ': shared cost, mastery and AI mirrors agree with actual local fields', () => {
 const d = get(document(t.file).nodes, t.id), mastery = get(document(shared).nodes, 'cbrn_doctrine_mastery'), ai = get(document(shared).nodes, 'cbrn_doctrine_ai');
 approx(get(d, 'xp_cost'), get(get(document(shared).nodes, 'cbrn_doctrine_cost'), 'track_army_xp'));
 approx(get(get(d, 'mastery'), 'multiplier'), get(mastery, t.track + '_multiplier'));
 for (const r of get(d, 'rewards')) approx(get(r.value, 'mastery'), get(mastery, 'reward_threshold'));
 const block = get(d, 'ai_will_do'), modifiers = block.filter(n => n.key === 'modifier');
 approx(get(block, 'base'), get(ai, 'track_base'));
 approx(get(modifiers[0].value, 'factor'), get(ai, 'track_unavailable_factor'));
 approx(get(modifiers[1].value, 'factor'), get(ai, 'track_committed_factor'));
});
const mirror = (file, local, key) => test('mirror: ' + local, () => approx(num(document(file).resolve(local)), num(get(modifierTable, key))));
for (const [file, local, key] of [
 [tracks[0].file, '@CBRN_HAZARD_ASSAULT_ADOPTION_PROTECTION_RELIABILITY', 'infantry_adoption_protection_reliability'],
 [tracks[0].file, '@CBRN_HAZARD_ASSAULT_M3_ASSAULT_BREAKTHROUGH', 'infantry_m3_assault_breakthrough'],
 [tracks[2].file, '@CBRN_TOXIC_ARMOR_ADOPTION_BREAKTHROUGH', 'armor_adoption_breakthrough'],
 [tracks[2].file, '@CBRN_TOXIC_ARMOR_M1_RELIABILITY', 'armor_m1_sealed_reliability'],
 [tracks[1].file, '@CBRN_CONTAMINANT_FIRE_ADOPTION_LINE_ARTILLERY_SOFT_ATTACK', 'combat_support_adoption_line_artillery_soft_attack'],
 [tracks[1].file, '@CBRN_CONTAMINANT_FIRE_ADOPTION_SUPPORT_ARTILLERY_SOFT_ATTACK', 'combat_support_adoption_support_artillery_soft_attack'],
 [tracks[3].file, '@CBRN_INTEGRATED_COMMAND_ACTIVATION_RECON', 'operations_adoption_recon'],
 [tech, '@CHAOS_ASSAULT_IMPROVED_BREAKTHROUGH', 'chaos_battalion_1942_breakthrough'],
 [tech, '@CBRN_PROJECTOR_TECH_BREAKTHROUGH', 'projector_tech_breakthrough'],
]) mirror(file, local, key);
const retiredLocal = tracks.flatMap(t => [...document(baseline + t.file).locals.keys()].filter(k => !document(t.file).locals.has(k)).map(token => ({file: t.file, token})));
test('every retired local constant has no surviving use in its file', () => { for (const {file, token} of retiredLocal) assert(!walk(document(file).raw).some(n => n.value === token), token); });
const retiredShared = get(document(baseline + shared).nodes, 'cbrn_doctrine_modifier').map(n => n.key).filter(k => !modifierTable.some(n => n.key === k));
const commonTextFiles = listFiles('common').filter(f => f.endsWith('.txt'));
test('retired shared modifier tokens have no surviving common-script uses', () => {
 for (const file of commonTextFiles) {
  const text = fs.readFileSync(path.join(root, file), 'utf8').replace(/#[^\r\n]*/g, '');
  for (const key of retiredShared) assert(!text.includes('constant:cbrn_doctrine_modifier.' + key), `${file}: retired ${key}`);
 }
});

const stats = ['soft_attack', 'hard_attack', 'breakthrough', 'defense', 'max_organisation', 'reliability'];
const countryStats = ['army_attack_factor', 'army_org_factor', 'planning_speed', 'coordination_bonus', 'land_reinforce_rate', 'recon_factor'];
const technologyFiles = listFiles('common/technologies').filter(f => f.endsWith('.txt'));
function grants(stage) {
 const unit = [], country = [];
 function collect(file, id, body) {
  for (const n of body) {
   if (countryStats.includes(n.key) && !Array.isArray(n.value)) country.push({file, step: id, stat: n.key, value: num(n.value), cbrnControlled: file.includes('/doctrines/') || /\/(cbrn_[^/]+|chaosx_technologies)\.txt$/.test(file)});
   if (Array.isArray(n.value) && (units.has(n.key) || n.key?.startsWith('category_'))) {
    for (const s of n.value.filter(s => stats.includes(s.key))) unit.push({file, step: id, recipient: n.key, stat: s.key, value: num(s.value)});
   }
  }
 }
 for (const d of doctrines(stage)) for (const s of steps(d)) collect(d.file, s.id, s.body);
 for (const file of technologyFiles) {
  const actual = stage === 'before' && file === tech ? baseline + file : file;
  for (const n of optional(document(actual).nodes, 'technologies') || []) if (Array.isArray(n.value)) collect(actual, n.key, n.value);
 }
 return {unit, country};
}
const beforeGrants = grants('before'), afterGrants = grants('after');
const matches = (g, id) => g.recipient === id || units.get(id).categories.includes(g.recipient);
const collectFor = (grants, id, stat) => grants.unit.filter(g => g.stat === stat && matches(g, id));
const doctrinesOnly = gs => gs.filter(g => g.file.includes('/doctrines/'));
const specificTrack = (gs, id, stat) => gs.unit.filter(g => g.step.startsWith(id + '/') && g.stat === stat);
for (const [id, stat, recipient, expected, step] of [
 ['extermination_columns', 'reliability', 'category_cbrn_primary_protection', 0.10, '/adoption'],
 ['extermination_columns', 'breakthrough', 'category_cbrn_assault_battalions', 0.15, '/rewards/unlock_chaos_battalion'],
 ['chemical_suppression', 'breakthrough', 'category_cbrn_armored_delivery_support', 0.05, '/adoption'],
 ['chemical_suppression', 'reliability', 'category_cbrn_armored_delivery_support', 0.15, '/rewards/adamsite_emission_cells'],
 ['contaminant_firebases', 'soft_attack', 'category_line_artillery', 0.095, '/adoption'],
 ['contaminant_firebases', 'soft_attack', 'category_support_artillery', 0.095, '/adoption'],
]) test(`one concentrated payoff: ${id}/${recipient}/${stat}`, () => { const current = specificTrack(afterGrants, id, stat).filter(g => g.recipient === recipient); assert.equal(current.length, 1); approx(current[0].value, expected); assert.equal(current[0].step, id + step); });
test('infantry lifetime breakthrough retained at 15% in exactly one grant, final soft attack retained', () => { approx(sum(specificTrack(beforeGrants, 'extermination_columns', 'breakthrough').map(g => g.value)), 0.15); const now = specificTrack(afterGrants, 'extermination_columns', 'breakthrough'); assert.equal(now.length, 1); approx(now[0].value, 0.15); const sa = specificTrack(afterGrants, 'extermination_columns', 'soft_attack'); assert.equal(sa.length, 1); approx(sa[0].value, 0.05); assert.equal(sa[0].recipient, 'chaos_battalion'); });
test('armor and conventional artillery lifetime relocated sums retained', () => {
 for (const [id, stat, recipient] of [['chemical_suppression', 'reliability', 'category_cbrn_armored_delivery_support'], ['chemical_suppression', 'breakthrough', 'category_cbrn_armored_delivery_support'], ['contaminant_firebases', 'soft_attack', 'category_line_artillery'], ['contaminant_firebases', 'soft_attack', 'category_support_artillery']]) approx(sum(specificTrack(beforeGrants, id, stat).filter(g => g.recipient === recipient).map(g => g.value)), sum(specificTrack(afterGrants, id, stat).filter(g => g.recipient === recipient).map(g => g.value)));
});
test('operations lifetime recon retained at 25% in one adoption grant', () => { const old = beforeGrants.country.filter(g => g.step.startsWith('integrated_chemical_operations/') && g.stat === 'recon_factor'), current = afterGrants.country.filter(g => g.step.startsWith('integrated_chemical_operations/') && g.stat === 'recon_factor'); approx(sum(old.map(g => g.value)), 0.25); assert.equal(current.length, 1); approx(current[0].value, 0.25); assert.equal(current[0].step, 'integrated_chemical_operations/adoption'); });
test('projector has exactly two upgrade-stat nodes and no base third grant', () => { const gs = afterGrants.unit.filter(g => g.recipient === 'cbrn_chemical_projector_battery' && g.stat === 'breakthrough' && g.file.includes('/technologies/')); assert.deepEqual(gs.map(g => g.step).sort(), ['advanced_livens_projector', 'improved_livens_projector']); for (const g of gs) approx(g.value, 0.065); });
test('Chaos 1942 technology has 4% breakthrough and unchanged flat +11 organization', () => { const gs = afterGrants.unit.filter(g => g.recipient === 'chaos_battalion' && g.file.includes('/technologies/')); assert.equal(gs.length, 2); approx(gs.find(g => g.stat === 'breakthrough').value, 0.04); assert.equal(gs.find(g => g.stat === 'max_organisation').value, 11); });
for (const id of tracks.find(t => t.track === 'armor').roster) test(id + ': two before org grants become one +5 armored grant', () => { const old = collectFor(beforeGrants, id, 'max_organisation'), current = collectFor(afterGrants, id, 'max_organisation'); assert.equal(old.length, 2); assert.equal(current.length, 1); assert.equal(sum(old.map(g => g.value)), 10); assert.equal(current[0].value, 5); assert.equal(current[0].recipient, 'category_cbrn_armored_delivery_support'); });
test('projector keeps exactly its original +5 organization payoff', () => { for (const gs of [beforeGrants, afterGrants]) { const grant = collectFor(gs, 'cbrn_chemical_projector_battery', 'max_organisation'); assert.equal(grant.length, 1); assert.equal(grant[0].value, 5); } });

const spiritFile = 'common/ideas/cbw_spirits.txt', highFile = 'common/country_leader/cbrn_high_command_traits.txt';
const spiritRoot = get(document(spiritFile).nodes, 'ideas');
const spiritModifiers = walk(spiritRoot).filter(n => n.key === 'modifier' && Array.isArray(n.value) && n.value.some(x => countryStats.includes(x.key) || x.key?.startsWith('modifier_army_sub_unit_'))).flatMap(n => n.value.filter(x => countryStats.includes(x.key) || x.key?.startsWith('modifier_army_sub_unit_')).map(x => ({file: spiritFile, stat: x.key, value: num(x.value)})));
// Restrict to actual modifier blocks. AI modifier blocks lack native stat keys.
const highTraits = get(document(highFile).nodes, 'leader_traits');
const advisorOrg = {file: highFile, stat: 'army_org_factor', value: num(get(get(highTraits, 'cbrn_biological_security_director_trait'), 'army_org_factor'))};
const highPlanning = {file: highFile, stat: 'planning_speed', value: Math.max(...highTraits.filter(n => /^cbrn_operations_high_command_[123]$/.test(n.key)).map(n => num(get(n.value, 'planning_speed'))))};
const hqPlanning = {file: units.get('cbrn_hq_operations_section').file, stat: 'planning_speed', value: num(get(get(units.get('cbrn_hq_operations_section').body, 'deployed_leader_modifiers'), 'planning_speed'))};
const countryFor = (gs, stat) => [...gs.country.filter(g => g.cbrnControlled && g.stat === stat), ...spiritModifiers.filter(g => g.stat === stat), ...(stat === 'army_org_factor' ? [advisorOrg] : []), ...(stat === 'planning_speed' ? [highPlanning, hqPlanning] : [])];
const countryEvidence = Object.fromEntries(countryStats.filter(s => s !== 'recon_factor').map(stat => { const sources = countryFor(afterGrants, stat).filter(g => g.value > 0); return [stat, {sources, pooled: sum(sources.map(g => g.value)), independentFactor: stat === 'land_reinforce_rate' ? null : product(sources.map(g => g.value)), ...(stat === 'land_reinforce_rate' ? {semantics: 'additive percentage-point grants, no multiplicative reinterpretation'} : {})}]; }));
for (const [stat, cap] of [['army_attack_factor', 0.05], ['army_org_factor', 0.05], ['planning_speed', 0.15], ['coordination_bonus', 0.08], ['land_reinforce_rate', 0.02]]) test('global pooled source ceiling: ' + stat, () => assert(countryEvidence[stat].pooled <= cap + 1e-10, JSON.stringify(countryEvidence[stat])));
for (const [stat, cap] of [['army_attack_factor', 0.05], ['army_org_factor', 0.05], ['planning_speed', 0.15], ['coordination_bonus', 0.08]]) test('global independent-source guard: ' + stat, () => assert(countryEvidence[stat].independentFactor <= 1 + cap + 1e-10));
const cadres = spiritModifiers.filter(g => g.stat.startsWith('modifier_army_sub_unit_'));
test('Cadres has exactly the four actual unit-specific attack/defence grants', () => { assert.deepEqual(cadres.map(g => g.stat).sort(), ['modifier_army_sub_unit_chaos_battalion_attack_factor', 'modifier_army_sub_unit_chaos_battalion_defence_factor', 'modifier_army_sub_unit_cbrn_gas_mask_decon_detachment_attack_factor', 'modifier_army_sub_unit_cbrn_gas_mask_decon_detachment_defence_factor'].sort()); for (const g of cadres) approx(g.value, 0.10); });
const veteran = get(get(document('common/unit_leader/chaosx_traits.txt').nodes, 'leader_traits'), 'biological_operations_veteran');
const skillPoints = num(get(veteran, 'defense_skill'));
// Read both wiki and installed skill data. The defense-to-breakthrough application
// remains a deliberately reserved pessimistic allowance, not native proof.
const game = 'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV';
const defensePath = path.join(game, 'common/unit_leader/00_defense_skills.txt');
const defenseBytes = fs.readFileSync(defensePath);
const skillTable = get(parse(defenseBytes.toString('utf8')), 'leader_defense_skills').filter(n => optional(n.value, 'type') === 'corps_commander').map(n => ({level: Number(n.key), defence: Number(get(get(n.value, 'modifier'), 'defence'))}));
assert.equal(skillTable.length, 10);
const defensePerPoint = skillTable[0].defence;
for (const row of skillTable) approx(row.defence, row.level * defensePerPoint);
const extraDefense = skillPoints * defensePerPoint;
test('earned Biological Operations Veteran reserves one defense skill point at 2.5%', () => { assert.equal(skillPoints, 1); approx(extraDefense, 0.025); });
test('HQ protective native attack modifiers are penalties, excluded from positive upper bound', () => { const d = document('common/unit_leader/cbrn_hq_traits.txt'); for (const n of walk(d.nodes).filter(n => n.key === 'army_attack_factor')) assert(num(n.value) <= 0); });

const budgetTables = {};
for (const [stage, gs] of [['before', beforeGrants], ['after', afterGrants]]) {
 const armyAttack = countryFor(gs, 'army_attack_factor').filter(g => g.value > 0).map(g => g.value);
 const armyOrg = countryFor(gs, 'army_org_factor').filter(g => g.value > 0).map(g => g.value);
 budgetTables[stage] = retained.map(id => {
  const u = units.get(id), rows = {};
  for (const stat of stats.filter(s => s !== 'reliability')) {
   const direct = collectFor(gs, id, stat), values = direct.map(g => g.value);
   const attack = ['soft_attack', 'hard_attack'].includes(stat);
   const defense = ['defense', 'breakthrough'].includes(stat);
   const specificKey = `modifier_army_sub_unit_${id}_${attack ? 'attack' : 'defence'}_factor`;
   const spiritValues = attack || defense ? cadres.filter(g => g.stat === specificKey).map(g => g.value) : [];
   const reserveSkill = defense ? extraDefense : 0;
   const organization = stat === 'max_organisation';
   const layersPooled = (attack ? 1 + sum(armyAttack) : organization ? 1 + sum(armyOrg) : 1) * (1 + sum(spiritValues)) * (1 + reserveSkill);
   const layersIndependent = (attack ? product(armyAttack) : organization ? product(armyOrg) : 1) * product(spiritValues) * (1 + reserveSkill);
   const pooledStat = organization ? (num(u.org) + sum(values)) / u.org : 1 + sum(values);
   const independentStat = organization ? pooledStat : product(values);
   rows[stat] = {base: organization ? u.org : u.stats[stat], directSources: direct, directSum: sum(values), pooledFactor: pooledStat * layersPooled, independentFactor: independentStat * layersIndependent, countrySourceValues: attack ? armyAttack : organization ? armyOrg : [], specificSpiritValues: spiritValues, reservedEarnedDefenseSkill: reserveSkill, ceiling: 1.35, nominalOnlyWhenBaseZero: !organization && u.stats[stat] === 0};
  }
  return {unit: id, categories: u.categories, manpower: u.manpower, stats: rows};
 });
}
for (const u of budgetTables.after) for (const [stat, row] of Object.entries(u.stats)) test(`retained dedicated bound: ${u.unit}/${stat}`, () => { assert(row.pooledFactor <= 1.35 + 1e-10, 'pooled source bound ' + row.pooledFactor); assert(row.independentFactor <= 1.35 + 1e-10, 'independent source bound ' + row.independentFactor); });
const beforeFailures = budgetTables.before.flatMap(u => Object.entries(u.stats).filter(([,r]) => r.pooledFactor > 1.35 + 1e-10 || r.independentFactor > 1.35 + 1e-10).map(([stat, row]) => ({unit: u.unit, stat, pooledFactor: row.pooledFactor, independentFactor: row.independentFactor})));
test('baseline reproduces the known armored org and Chaos/projector breakthrough failures', () => { for (const id of tracks.find(t => t.track === 'armor').roster) assert(beforeFailures.some(f => f.unit === id && f.stat === 'max_organisation')); for (const id of ['chaos_battalion', 'cbrn_chemical_projector_battery']) assert(beforeFailures.some(f => f.unit === id && f.stat === 'breakthrough')); });
const conventionalArtillery = ['category_line_artillery', 'category_support_artillery'].map(recipient => {
 const grants = afterGrants.unit.filter(g => g.recipient === recipient && g.stat === 'soft_attack');
 const country = countryEvidence.army_attack_factor.sources.map(g => g.value);
 const doctrineSum = sum(doctrinesOnly(grants).map(g => g.value));
 return {recipient, directSources: grants, doctrineSum, pooledFactor: (1 + sum(grants.map(g => g.value))) * (1 + sum(country)), independentFactor: product(grants.map(g => g.value)) * product(country)};
});
for (const a of conventionalArtillery) test('conventional artillery doctrine 10% and combined 15% guard: ' + a.recipient, () => { assert(a.doctrineSum <= 0.10 + 1e-10); assert(a.pooledFactor <= 1.15 + 1e-10); assert(a.independentFactor <= 1.15 + 1e-10); });

const mioFiles = listFiles('common/military_industrial_organization/organizations').filter(f => /\/cbrn_.*\.txt$/.test(f));
const directCombatKeys = new Set(['soft_attack','hard_attack','breakthrough','defense','defence','army_attack_factor','army_defence_factor','army_org_factor','max_organisation']);
const mioNativeBonuses = mioFiles.flatMap(file => walk(document(file).nodes).filter(n => n.key === 'equipment_bonus' || n.key === 'organization_modifier').flatMap(n => n.value.map(v => ({file, key: v.key, value: v.value}))));
test('CBRN MIO native equipment/organization bonuses have no reviewed combat-stat layer', () => { for (const file of mioFiles) for (const n of walk(document(file).nodes)) assert(!directCombatKeys.has(n.key), `${file}: ${n.key}`); });
for (const file of ['common/country_leader/cbrn_historical_advisor_traits.txt', 'common/scripted_effects/cbrn_historical_advisor_effects.txt']) test('no extra direct combat-stat layer in ' + file, () => { for (const n of walk(document(file).nodes)) assert(!directCombatKeys.has(n.key), n.key); });
const dependencyFiles = ['common/scripted_effects/cbrn_doctrine_effects.txt', 'common/scripted_triggers/cbrn_doctrine_triggers.txt', 'common/decisions/cbrn_doctrine_decisions.txt', 'common/decisions/categories/cbrn_doctrine_categories.txt', 'common/characters/cbrn_historical_specialists.txt', 'common/characters/cbrn_historical_scientists.txt'];
for (const file of dependencyFiles) read(file);
const effectDefinitions = new Set(document('common/scripted_effects/cbrn_doctrine_effects.txt').nodes.map(n => n.key));
const recorderCalls = walk(doctrines('after').flatMap(d => d.body)).filter(n => n.key?.startsWith('cbrn_record_')).map(n => n.key);
test('all 28 doctrine recorder calls resolve to current shared effect definitions', () => { assert.equal(new Set(recorderCalls).size, 28); for (const call of recorderCalls) assert(effectDefinitions.has(call), call); });
const inertFlags = ['cbrn_mask_discipline_unlocked', 'cbrn_contaminated_terrain_movement_unlocked', 'cbrn_shock_exploitation_unlocked'];
const flagReferences = inertFlags.map(flag => ({flag, references: commonTextFiles.flatMap(file => {
 const text = fs.readFileSync(path.join(root, file), 'utf8');
 return text.split(/\r?\n/).flatMap((line, index) => line.split('#')[0].includes(flag) ? [{file, line: index + 1, text: line.trim()}] : []);
})}));
test('the three compatibility flags have set calls only and no asserted functional consumer', () => { for (const f of flagReferences) { assert.equal(f.references.length, 1, f.flag); assert(f.references[0].text.startsWith('set_country_flag = '), f.flag); } });
const pacingCases = [
 ['protected_field_company', ['cbrn_gas_mask_decon_detachment','cbrn_chemical_recon_detachment','cbrn_medical_countermeasure_detachment']],
 ['protected_biosecurity_field_company', ['cbrn_gas_mask_decon_detachment','cbrn_chemical_recon_detachment','cbrn_medical_countermeasure_detachment','cbrn_biosecurity_assault_detachment']],
 ['sustained_projector_support', ['cbrn_chemical_projector_battery','cbrn_chemical_ammunition_train','cbrn_medical_countermeasure_detachment']],
 ['single_armored_delivery', ['cbrn_light_armored_delivery_detachment']],
 ['protective_hq_with_field_companies', ['cbrn_hq_protective_logistics_section','cbrn_gas_mask_decon_detachment','cbrn_chemical_recon_detachment','cbrn_medical_countermeasure_detachment']],
 ['existing_chaos_assault_formation', ['chaos_battalion','cbrn_gas_mask_decon_detachment','cbrn_chemical_recon_detachment']],
].map(([id, components]) => ({id, components, perTrack: rosterEvidence.map(t => ({track: t.track, beforeWeightedManpower: sum(components.filter(u => t.before.includes(u)).map(u => units.get(u).manpower)) * t.multiplier, afterWeightedManpower: sum(components.filter(u => t.after.includes(u)).map(u => units.get(u).manpower)) * t.multiplier}))}));
test('wider contributor rosters never reduce pre-existing example mastery numerator', () => { for (const c of pacingCases) for (const t of c.perTrack) assert(t.afterWeightedManpower >= t.beforeWeightedManpower); });

const referenceSections = [
 ['game_doc', path.join(game, 'common/doctrines/subdoctrines/_documentation.md'), 3, 57],
 ['game_doc', path.join(game, 'common/doctrines/grand_doctrines/_documentation.md'), 58, 110],
 ['vanilla_precedent', path.join(game, 'common/doctrines/subdoctrines/land/infantry_subdoctrines.txt'), 384, 401],
 ['wiki', path.join(root, 'paradox_wiki/Technology modding - Hearts of Iron 4 Wiki.md'), 92, 118],
 ['wiki', path.join(root, 'paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md'), 946, 950],
 ['wiki', path.join(root, 'paradox_wiki/Character modding - Hearts of Iron 4 Wiki.md'), 256, 264],
].map(([kind, file, startLine, endLine]) => ({kind, path: file, startLine, endLine, sha256: hash(fs.readFileSync(file))}));
referenceSections.push({kind: 'installed_skill_data', path: defensePath, startLine: 124, endLine: 204, sha256: hash(defenseBytes), perPoint: defensePerPoint, corpsCommanderTable: skillTable});
test('source hashes remain stable during the bounded audit', () => { for (const [file, bytes] of inputs) assert.equal(hash(fs.readFileSync(path.join(root, file))), hash(bytes), file); });
const result = {
 status: tests.some(t => t.status === 'failed') ? 'failed' : 'passed_with_native_semantics_unresolved', scenario: 'FullLegalSourceBudget: controlled CBRN benefit upper bound over an equal conventional baseline', command: 'node docs/testing/2026-10-07_doctrine_reward_budget_source_tests.js', timestamp: new Date().toISOString(),
 tests, sourceHashes: Object.fromEntries([...inputs].map(([f,b]) => [f,hash(b)])), referenceSections,
 baselineProvenance: {rewardRevision: baseline, grandDoctrine: grandBaseline, dependenciesWithoutBeforeSnapshot: 'Current dependency files are hashed. Their bodies are not claimed equal to a captured baseline. Before budget overlays only the captured tracks/constants/technology and separate grand baseline onto the same current dependency sources.'},
 rosterEvidence, retainedRoster: retained, chemicalMembershipAmongRetained: chemical,
 otherDefinedChemicalMembersOutsideRetainedRoster: [...units].filter(([id,u]) => !retained.includes(id) && u.categories.includes('category_chemical_support_companies')).map(([id,u]) => ({unit: id, file: u.file, active: optional(u.body,'active')})),
 retiredConstants: {local: retiredLocal, shared: retiredShared}, countryEvidence, equalBaselineCountryTechnologySourcesExcludedFromCBRNAllowance: afterGrants.country.filter(g => !g.cbrnControlled), cadres, extraDefenseSkill: {points: skillPoints, perPoint: defensePerPoint, reservedFactor: extraDefense}, budgetTables, reproducedBaselineBudgetFailures: beforeFailures, conventionalArtillery, pacingCases, mioNativeBonuses, compatibilityFlagReferences: flagReferences,
 limitations: [
  'Pooled same-stat accumulation and every-positive-source independent products are two conservative source arithmetic models, not a proved native formula.',
  'Defense modifiers and the earned defense skill are reserved against both defense and attacking breakthrough because their exact native breakthrough semantics remain unsupported.',
  'The country upper bound deliberately sums positive mutually exclusive postures. The planning upper bound selects one highest operations high-command rank rather than stacking three ranks.',
  'The 13-row audit covers retained dedicated units and CBRN-authored doctrine/technology/country/Cadres/earned-skill benefits. Ordinary country/commander/design bonuses, intrinsic terrain modifiers, equipment identities/modules, and strengths are the same baseline on both sides. Native equipment aggregation, actual division weighted stats, and mastery calendar pacing are not simulated.',
  'A base stat of zero is labelled nominal only. Source percentages do not establish a meaningful combat stat for that unit.',
  'Legacy inactive Livens definitions remain outside the retained roster. No retirement or consumer-lifecycle completion claim is made for them.',
  'Conditional hazard endpoints, equal-mask baseline correction, protected field cleanup, and public-harm floors are not proved by this narrow doctrine diff.',
  'MCP tech_inspect bonus_coverage and reference_context requests did not return within the worker wait and were cancelled. Parent reports TECHNOLOGY_NOT_FOUND for chaos_warfare and TECH_RENDERED_PARTIAL with zero focused renders and sourceAccurate=false. Source tests are not equivalent engine evidence.',
  'No AI evaluation or probability comparison is performed by this source worker. Exact doctrine AI AST equality is covered. Probability scenario evidence belongs to the separate read-only probability auditor.',
 ],
};
fs.writeFileSync(path.join(__dirname, '2026-10-07_doctrine_reward_budget_source_results.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({status: result.status, tests: tests.length, failedTests: tests.filter(t => t.status === 'failed'), reproducedBaselineBudgetFailures: beforeFailures, dedicatedRows: retained.length}, null, 2));
if (tests.some(t => t.status === 'failed')) process.exitCode = 1;
