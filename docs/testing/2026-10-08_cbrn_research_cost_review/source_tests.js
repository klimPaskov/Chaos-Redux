// Bounded actual-source CBRN research cost checks. No native engine or research simulation.
// Parser follows the existing 2026-10-07_doctrine_reward_budget_source_tests.js.
// Run from the mod root: node docs/testing/2026-10-08_cbrn_research_cost_review/source_tests.js
const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict'), crypto = require('node:crypto');
const root = path.resolve(__dirname, '../../..');
const main = 'common/technologies/chaosx_technologies.txt', regimental = 'common/technologies/cbrn_regimental_support_technologies.txt';
const expectedBeforeHashes = {
 [main]: 'd52d48eb5796c120e5bd465dddcd5527a6597f7a60cf68f871c6240d05b1f5c1',
 [regimental]: '45826eb81040942fdc2fe9b32c61fdb9be09f625ce37ae655ac6e761415c6cb4',
};
const bands = [
 {days: 50, oldFactor: '0.5', factor: '0.45454', ids: ['pathogen_handling_protocols','bio_surveillance_networks','livens_projector_tech','chlorine_gas','basic_gas_masks','field_decontamination_kits','chemical_detection_paper']},
 {days: 75, oldFactor: '0.75', factor: '0.68181', ids: ['sealed_containment_laboratories','rapid_outbreak_response','phosgene','mustard_gas','dimercaprol','improved_livens_projector','improved_gas_masks','mobile_wash_columns','mobile_sampling_laboratories','field_epidemiology_teams']},
 {days: 100, oldFactor: '1', factor: '0.90909', ids: ['fail_safe_containment_facilities','integrated_epidemic_control','lewisite','tabun','advanced_livens_projector','advanced_gas_masks','sealed_assault_protection','rapid_decontamination_plants','theater_cbrn_command_set','mobile_cbrn_hospitals']},
];
const grantedBasic = ['civil_defence_fitting_and_registration','military_filter_standardization','rapid_filter_replacement','vehicle_overpressure_and_sealed_compartments','portable_anemometer','meteorological_stations','upper_air_soundings'];
const grantedAdvanced = ['sarin','soman'];
const tests = [], costEvidence = [], preservationEvidence = [], revisions = [];
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const readJSON = p => JSON.parse(fs.readFileSync(path.join(root, p), 'utf8'));
const get = (nodes, key) => {const m = nodes.filter(n => n.key === key); assert.equal(m.length, 1, `expected one ${key}`); return m[0].value;};
const optional = (nodes, key) => nodes.find(n => n.key === key)?.value;
const walk = nodes => nodes.flatMap(n => [n, ...(Array.isArray(n.value) ? walk(n.value) : [])]);
const omitCost = nodes => nodes.filter(n => n.key !== 'research_cost');
function test(name, fn) {try {fn(); tests.push({name, status: 'passed'});} catch (error) {tests.push({name, status: 'failed', reason: error.message});}}
function parse(text) {
 const tokens = (text.match(/#[^\r\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>#]+/g) || []).filter(t => !t.startsWith('#')); let i = 0;
 function body(nested = false) {
  const nodes = [];
  while (i < tokens.length && tokens[i] !== '}') {
   const key = tokens[i++];
   if (key === '{') {nodes.push({key: null, op: null, value: body(true)}); continue;}
   if (!['=', '<', '>'].includes(tokens[i])) {nodes.push({key, op: null, value: key, atom: true}); continue;}
   const op = tokens[i++]; let value = tokens[i++]; assert(value !== undefined, `missing value after ${key}`);
   if (value === '{') value = body(true); nodes.push({key, op, value});
  }
  if (nested) assert.equal(tokens[i++], '}', 'unterminated block'); return nodes;
 }
 const result = body(); assert.equal(i, tokens.length); return result;
}
function document(file, before = false) {
 const absolute = before ? path.join(__dirname, 'before_source', path.basename(file)) : path.join(root, file);
 const bytes = fs.readFileSync(absolute), raw = parse(bytes.toString('utf8'));
 const locals = new Map(walk(raw).filter(n => n.key?.startsWith('@')).map(n => [n.key, n.value]));
 const resolveRaw = v => {if (typeof v === 'string' && v.startsWith('@')) {assert(locals.has(v), `unknown ${v}`); return resolveRaw(locals.get(v));} return v;};
 const normalize = nodes => nodes.filter(n => !n.key?.startsWith('@')).map(n => ({...n, value: Array.isArray(n.value) ? normalize(n.value) : n.atom ? n.value : resolveRaw(n.value)}));
 return {raw, normalized: normalize(raw), locals, resolveRaw, sha256: hash(bytes), bytes: bytes.length};
}
const docs = new Map([main, regimental].map(file => [file, {before: document(file, true), after: document(file)}]));
const inventory = readJSON('docs/testing/2026-10-08_cbrn_research_cost_review/research_cost_inventory.json');
const probability = readJSON('docs/testing/2026-10-08_cbrn_research_cost_probability/baseline_manifest.json');
const capturedRoot = path.resolve(path.dirname(inventory.revisions[0].path), '../..');
const capturedRelative = file => path.relative(capturedRoot, file).split(path.sep).join('/');
// Installed files remain external inputs. Repository inputs also check the candidate tree;
// exact captured hashes guard the comparison, allowing only checkout newline conversion.
function checkCapturedInput(file, expectedHash) {
 const captured = fs.readFileSync(file); assert.equal(hash(captured), expectedHash, file);
 const relative = capturedRelative(file);
 if (relative !== '..' && !relative.startsWith('../') && !path.isAbsolute(relative)) {
  const candidate = fs.readFileSync(path.join(root, relative));
  assert.equal(candidate.toString('utf8').replace(/\r\n/g, '\n'), captured.toString('utf8').replace(/\r\n/g, '\n'), relative);
 }
}
const expectedIds = bands.flatMap(b => b.ids).sort();
test('exact 27 unique IDs match the frozen inventory and MCP 25+2 candidate baseline', () => {
 assert.equal(expectedIds.length, 27); assert.equal(new Set(expectedIds).size, 27);
 assert.deepEqual(inventory.records.filter(r => r.researchableSurface).map(r => r.id).sort(), expectedIds);
 assert.deepEqual(probability.sourceFiles.flatMap(f => f.candidateIds).sort(), expectedIds);
 for (const f of probability.sourceFiles) {assert.equal(f.sha256, expectedBeforeHashes[f.path]); assert.equal(f.researchableCandidates, f.path === main ? 25 : 2);}
});
test('installed base cost and all captured define files remain unchanged', () => {
 const defineEvidence = readJSON('docs/testing/2026-10-08_cbrn_research_cost_review/effective_defines.json'); assert.equal(defineEvidence.effectiveBaseTechCost, 110);
 for (const f of defineEvidence.files) checkCapturedInput(f.path, f.sha256);
 const game = defineEvidence.files.find(f => f.path.endsWith('00_defines.lua')); assert(game);
 assert.match(fs.readFileSync(game.path, 'utf8'), /BASE_TECH_COST\s*=\s*110\s*,/);
});
for (const [file, pair] of docs) {
 const beforeTech = get(pair.before.normalized, 'technologies'), afterTech = get(pair.after.normalized, 'technologies');
 const beforeRawTech = get(pair.before.raw, 'technologies'), afterRawTech = get(pair.after.raw, 'technologies');
 revisions.push({path: file, beforeSHA256: pair.before.sha256, afterSHA256: pair.after.sha256, beforeBytes: pair.before.bytes, afterBytes: pair.after.bytes});
 test(`${file}: frozen snapshot retains its exact pre-patch bytes`, () => assert.equal(pair.before.sha256, expectedBeforeHashes[file]));
 test(`${file}: every technology ID and its source order are unchanged`, () => assert.deepEqual(afterTech.map(n => n.key), beforeTech.map(n => n.key)));
 for (const b of bands) for (const id of b.ids.filter(id => beforeTech.some(n => n.key === id))) {
  test(`${id}: effective source cost and below-target tolerance`, () => {
   const old = get(beforeTech, id), current = get(afterTech, id), rawCurrent = get(afterRawTech, id);
   assert.equal(get(old, 'research_cost'), b.oldFactor); assert.equal(get(current, 'research_cost'), b.factor);
   assert.equal(pair.after.resolveRaw(get(rawCurrent, 'research_cost')), b.factor);
   const units = BigInt(b.factor.replace('.', '').padEnd(6, '0')), targetUnits = BigInt(b.days) * 100000n, baseUnits = units * 110n;
   const shortfall = targetUnits - baseUnits; assert(shortfall >= 0n && shortfall < 100n, `${id}: source shortfall must be below .001 day`);
   assert.equal(units, targetUnits / 110n, 'literal must be the downward five-decimal ratio');
   assert(Number(b.oldFactor) * 110 > b.days, 'frozen before source must reproduce the over-cost');
   costEvidence.push({path: file, id, targetBaseDays: b.days, beforeFactor: b.oldFactor, afterFactor: b.factor, sourceBaseDays: Number(baseUnits) / 100000, shortfallDays: Number(shortfall) / 100000});
  });
 }
 test(`${file}: every normalized technology body differs only at approved research costs`, () => {
  for (const n of beforeTech) {
   const current = get(afterTech, n.key);
   assert.deepEqual(expectedIds.includes(n.key) ? omitCost(current) : current, expectedIds.includes(n.key) ? omitCost(n.value) : n.value, n.key);
  }
 });
 test(`${file}: every AI block is preserved byte-token-wise and after constant resolution`, () => {
  for (const n of beforeTech) {
   assert.deepEqual(optional(get(afterTech, n.key), 'ai_will_do'), optional(n.value, 'ai_will_do'), n.key);
   assert.deepEqual(optional(get(afterRawTech, n.key), 'ai_will_do'), optional(get(beforeRawTech, n.key), 'ai_will_do'), n.key);
  }
 });
 test(`${file}: exact raw AST patch, no collateral constant or field edit`, () => {
  const expected = structuredClone(pair.before.raw), techs = get(expected, 'technologies');
  const setLocal = (key, value) => {const nodes = techs.filter(n => n.key === key); assert.equal(nodes.length, 1); nodes[0].value = value;};
  const rebind = (id, token) => {const fields = get(techs, id).filter(n => n.key === 'research_cost'); assert.equal(fields.length, 1); fields[0].value = token;};
  if (file === main) {
   setLocal('@CBRN_TECH_COST_BASIC', '0.45454'); setLocal('@CBRN_PROTECTION_TECH_COST_STANDARD', '0.68181'); setLocal('@CBRN_PROTECTION_TECH_COST_ADVANCED', '0.90909');
   const i = techs.findIndex(n => n.key === '@CBRN_PROTECTION_TECH_COST_ADVANCED');
   techs.splice(i + 1, 0, {key: '@CBRN_GRANTED_TECH_COST_BASIC', op: '=', value: '0.5'}, {key: '@CBRN_GRANTED_TECH_COST_ADVANCED', op: '=', value: '1'});
   for (const id of grantedBasic) rebind(id, '@CBRN_GRANTED_TECH_COST_BASIC');
   for (const id of grantedAdvanced) rebind(id, '@CBRN_GRANTED_TECH_COST_ADVANCED');
  } else {
   setLocal('@CBRN_REGIMENTAL_TECH_COST_NORMAL', '0.68181'); const i = techs.findIndex(n => n.key === '@CBRN_REGIMENTAL_TECH_COST_NORMAL');
   techs.splice(i + 1, 0, {key: '@CBRN_REGIMENTAL_RESEARCH_COST_ADVANCED', op: '=', value: '0.90909'});
   rebind('mobile_cbrn_hospitals', '@CBRN_REGIMENTAL_RESEARCH_COST_ADVANCED');
  }
  assert.deepEqual(pair.after.raw, expected);
 });
 preservationEvidence.push({path: file, technologyCount: beforeTech.length, correctedCostCount: beforeTech.filter(n => expectedIds.includes(n.key)).length, fullyUnchangedBodyCount: beforeTech.filter(n => !expectedIds.includes(n.key)).length});
}
test('all 21 excluded cost-bearing markers retain their full resolved AST and costs', () => {
 const hidden = inventory.records.filter(r => !r.researchableSurface); assert.equal(hidden.length, 21);
 for (const r of hidden) {
  const file = capturedRelative(r.path);
  if (!docs.has(file)) {checkCapturedInput(r.path, inventory.revisions.find(x => x.path === r.path).sha256); continue;}
  const pair = docs.get(file); assert.deepEqual(get(get(pair.after.normalized, 'technologies'), r.id), get(get(pair.before.normalized, 'technologies'), r.id), r.id);
 }
});
const failed = tests.filter(t => t.status === 'failed');
const result = {status: failed.length ? 'failed' : 'passed_source_calibration_native_precision_unproved', testsRun: tests.length, failures: failed.length, tests, sourceRevisions: revisions, candidateIds: expectedIds, costs: costEvidence, preservation: preservationEvidence, limits: ['Native research_cost field precision is not documented by these checks.', 'Native research-calendar rounding and AI selection remain outside this source test.', 'The parent owns final MCP technology and probability comparisons.']};
fs.writeFileSync(path.join(__dirname, 'source_test_results.json'), JSON.stringify(result, null, 2) + '\n', 'utf8');
console.log(JSON.stringify({status: result.status, testsRun: result.testsRun, failures: result.failures, correctedRecipients: costEvidence.length, preservation: preservationEvidence}, null, 2));
if (failed.length) {console.error(JSON.stringify(failed, null, 2)); process.exitCode = 1;}
