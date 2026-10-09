// Source accounting for the user-approved shared Event 016 endgame exception.
// Run from the repository root: node docs/testing/2026-10-09_shared_project_budget/source_review.js
// No gameplay values are changed; native modifier aggregation is not simulated.
const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict'), crypto = require('node:crypto');
// Same bounded parser as the doctrine audit, including anonymous database lists.
function parse(text) {
 const tokens = (text.match(/#[^\r\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>#]+/g) || []).filter(t => !t.startsWith('#'));
 let i = 0;
 function body(nested = false) {
  const result = [];
  while (i < tokens.length && tokens[i] !== '}') {
   const key = tokens[i++];
   if (key === '{') { result.push({key: null, value: body(true)}); continue; }
   if (!['=', '<', '>'].includes(tokens[i])) { result.push({key, value: key, atom: true}); continue; }
   const op = tokens[i++]; let value = tokens[i++]; assert(value !== undefined, key);
   if (value === '{') value = body(true);
   result.push({key, op, value});
  }
  if (nested) assert.equal(tokens[i++], '}');
  return result;
 }
 const result = body(); assert.equal(i, tokens.length); return result;
}
const root = path.resolve(__dirname, '../../..'), inputs = new Map(), documents = new Map();
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const read = file => { if (!inputs.has(file)) inputs.set(file, fs.readFileSync(path.join(root, file))); return inputs.get(file).toString('utf8'); };
const nodes = file => { if (!documents.has(file)) documents.set(file, parse(read(file))); return documents.get(file); };
const get = (body, key) => { const found = body.filter(n => n.key === key); assert.equal(found.length, 1, key); return found[0].value; };
const walk = (body, prefix = '') => body.flatMap(n => [{...n, location: prefix + n.key}, ...(Array.isArray(n.value) ? walk(n.value, prefix + n.key + '/') : [])]);
const shared = new Map();
for (const row of walk(nodes('common/script_constants/016_brilliant_scientist_project_constants.txt'))) {
 if (!Array.isArray(row.value) && /^-?\d+(\.\d+)?$/.test(row.value)) shared.set('constant:' + row.location.replaceAll('/', '.'), Number(row.value));
}
function numeric(file, value) {
 if (value.startsWith('@')) return numeric(file, get(nodes(file), value));
 if (value.startsWith('constant:')) { assert(shared.has(value), value); return shared.get(value); }
 assert(/^-?\d+(\.\d+)?$/.test(value), value); return Number(value);
}
const caps = {army_attack_factor: .05, army_org_factor: .05, planning_speed: .15, coordination_bonus: .08, land_reinforce_rate: .02};
const ordinary = [];
function collect(file, body, label) {
 for (const n of walk(body, label + '/')) if (Object.hasOwn(caps, n.key) && !Array.isArray(n.value)) ordinary.push({file, location: n.location, stat: n.key, value: numeric(file, n.value)});
}
const doctrineFiles = [
 'common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt',
 ...['infantry', 'combat_support', 'armor', 'operations'].map(t => `common/doctrines/subdoctrines/land/chaos_warfare_${t}_subdoctrines.txt`),
];
for (const f of doctrineFiles) collect(f, nodes(f).filter(n => !n.key.startsWith('@')), 'doctrine');
for (const f of ['common/ideas/cbw_spirits.txt', 'common/ideas/cbw_ideas.txt']) {
 for (const n of walk(nodes(f)).filter(n => n.key === 'modifier' && Array.isArray(n.value))) collect(f, n.value, n.location);
}
const advisorFile = 'common/country_leader/cbrn_high_command_traits.txt', traits = get(nodes(advisorFile), 'leader_traits');
collect(advisorFile, get(traits, 'cbrn_biological_security_director_trait'), 'cbrn_biological_security_director_trait');
const ranks = traits.filter(n => /^cbrn_operations_high_command_[123]$/.test(n.key)).map(n => ({id: n.key, value: numeric(advisorFile, get(n.value, 'planning_speed'))}));
assert.equal(ranks.length, 3);
const rank = ranks.reduce((a, b) => a.value > b.value ? a : b);
ordinary.push({file: advisorFile, location: rank.id, stat: 'planning_speed', value: rank.value});
const hqFile = 'common/units/cbrn_hq_support.txt';
collect(hqFile, get(get(get(nodes(hqFile), 'sub_units'), 'cbrn_hq_operations_section'), 'deployed_leader_modifiers'), 'cbrn_hq_operations_section/deployed_leader_modifiers');
const modifierFile = 'common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt';
const families = ['biomedical', 'cloning', 'paleogenetics', 'xenobiological_synthesis'];
const familyInventory = families.flatMap(family => ['theory', 'prototype', 'deployment', 'weaponization'].map(stage => {
 const id = `brilliant_scientist_${family}_${stage}`, body = get(nodes(modifierFile), id);
 return {family, stage, id, file: modifierFile, fields: body.filter(n => !Array.isArray(n.value) && n.key !== 'icon').map(n => ({stat: n.key, value: numeric(modifierFile, n.value)})), enable: get(body, 'enable')};
}));
const projectCasesPath = 'docs/testing/2026-10-09_cbrn_project_routes/source_test_results.json';
const projectCases = JSON.parse(read(projectCasesPath));
// Use the actually observed source-VM add calls, not an assumed reward list.
const operationalIds = projectCases.cases.find(c => c.id === 'biomedical-source-zero-no-provenance-duplicates').modifierAddCalls;
const weaponizedIds = projectCases.cases.find(c => c.id === 'biomedical-weaponization-repeat-is-one-fourth-modifier').modifierAddCalls;
for (const dependency of projectCases.sourceHashes) assert.equal(sha(Buffer.from(read(dependency.path), 'utf8')), dependency.sha256, dependency.path);
const sum = a => a.reduce((a, b) => a + b, 0), round = v => Number(v.toFixed(12));
const ordinaryTable = Object.entries(caps).map(([stat, cap]) => {
 const sources = ordinary.filter(s => s.stat === stat && s.value > 0);
 return {stat, cap, sources, positivePooledUpperBound: round(sum(sources.map(s => s.value))), independentSourceFactor: stat === 'land_reinforce_rate' ? null : sources.reduce((p,s) => p * (1 + s.value), 1)};
});
function scenario(id, selected) {
 assert.equal(new Set(selected).size, selected.length);
 const rewards = selected.map(id => { const m = familyInventory.find(m => m.id === id); assert(m, id); return m; });
 return {id, selectedModifiers: selected, rows: ordinaryTable.map(o => {
  const sources = rewards.flatMap(m => m.fields.filter(f => f.stat === o.stat).map(f => ({modifier: m.id, ...f})));
  const exceptional = round(sum(sources.map(s => s.value)));
  return {stat: o.stat, ordinaryCap: o.cap, ordinarySubtotalUpperBound: o.positivePooledUpperBound, exemptSources: sources, exemptSubtotal: exceptional, combinedPooledUpperBound: round(o.positivePooledUpperBound + exceptional), independentSourceFactor: o.stat === 'land_reinforce_rate' ? null : sources.reduce((p,s) => p * (1 + s.value), o.independentSourceFactor), exceedsOrdinaryCap: o.positivePooledUpperBound + exceptional > o.cap + 1e-10};
 })};
}
const scenarios = [scenario('ordinary_biomedical_deployment', operationalIds), scenario('separately_authorized_biomedical_weaponization', weaponizedIds)];
const tests = [];
function check(id, f) { f(); tests.push({id, passed: true}); }
for (const row of ordinaryTable) check('ordinary-cap-' + row.stat, () => {
 assert(row.positivePooledUpperBound <= row.cap + 1e-10);
 if (row.independentSourceFactor !== null) assert(row.independentSourceFactor <= 1 + row.cap + 1e-10);
});
const lookup = (scenario, stat) => scenarios.find(s => s.id === scenario).rows.find(r => r.stat === stat);
check('operational-shared-rewards-preserved-and-visible', () => {
 assert.equal(operationalIds.length, 3);
 const org = lookup('ordinary_biomedical_deployment', 'army_org_factor'), reinforce = lookup('ordinary_biomedical_deployment', 'land_reinforce_rate');
 assert.equal(org.exemptSubtotal, .30); assert.equal(org.combinedPooledUpperBound, .345);
 assert.equal(reinforce.exemptSubtotal, 1.10); assert.equal(reinforce.combinedPooledUpperBound, 1.12);
 assert(org.exceedsOrdinaryCap && reinforce.exceedsOrdinaryCap);
});
check('weaponization-is-separate-and-not-inferred-from-ordinary-completion', () => {
 assert.equal(weaponizedIds.length, 4); assert(!operationalIds.some(id => id.endsWith('_weaponization')));
 assert.equal(lookup('separately_authorized_biomedical_weaponization', 'land_reinforce_rate').exemptSubtotal, 2.10);
});
check('four-families-have-four-distinct-stage-inventory-entries', () => assert.equal(new Set(familyInventory.map(m => m.id)).size, 16));
check('exemption-does-not-remove-any-ordinary-source', () => assert(ordinary.every(s => !s.file.includes('/016_'))));
check('input-hashes-stable', () => { for (const [f,b] of inputs) assert.equal(sha(fs.readFileSync(path.join(root, f))), sha(b), f); });
const report = {
 scope: 'Country-stat accounting addendum: ordinary CBRN positive-source upper bound plus separately classified shared Biomedical rewards; other shared stage fields inventoried without assuming their availability or combination.',
 acceptedException: 'User response on 2026-10-09 preserves Event 016 shared endgame project power and explicitly exempts that contribution from the ordinary CBRN caps.',
 tests, ordinaryTable, scenarios, otherOrdinaryNegativeSources: ordinary.filter(s => s.value < 0), familyInventory,
 sourceHashes: Object.fromEntries([...inputs].map(([f,b]) => [f,sha(b)])),
 limits: [
  'The ordinary subtotal follows the prior bounded country-stat audit: positive spirit postures are conservatively pooled; one highest high-command rank and one Operations HQ contribution are included. It is not a claim that all spirit postures coexist.',
  'Pooled sums and independent products are source arithmetic, not proved native formulas. Reinforce rate is reported in authored percentage points, not a realized chance above 100%.',
  'Project source-VM cases establish adapter calls and presence under fixtures. Native callbacks, dynamic modifier activation and actual aggregation remain unproved.',
  'The other three shared families have an explicit stage inventory, not automatic grants. Unit/equipment rewards, temporary actions, conditional hazards and full legal cross-family combinations require their own current selection/activation evidence.',
  'This exception does not settle the existing reconnaissance flat-point versus fractional countermodel. No reward is reduced by this audit.',
 ],
};
fs.writeFileSync(path.join(__dirname, 'source_review.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({checks: tests.length, scenarios: scenarios.map(s => ({id:s.id, rows:s.rows.map(({stat,ordinarySubtotalUpperBound,exemptSubtotal,combinedPooledUpperBound}) => ({stat,ordinarySubtotalUpperBound,exemptSubtotal,combinedPooledUpperBound}))})), limits: report.limits}, null, 2));
