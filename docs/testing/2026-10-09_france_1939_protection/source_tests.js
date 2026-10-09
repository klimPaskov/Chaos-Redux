// Bounded startup-tree projection; native production allocation is not executed.
// node docs/testing/2026-10-09_france_1939_protection/source_tests.js
const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict'), crypto = require('node:crypto');
const {execFileSync} = require('node:child_process');
const {parse} = require('../../plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js');
const root = path.resolve(__dirname, '../../..'), file = 'common/scripted_effects/chaosx_startup_history_effects.txt';
const baseline = 'ca6acf248745dc1c8de36f41bd501ad202d0036f';
const beforeBytes = execFileSync('git', ['-C', process.env.CBRN_SOURCE_REPOSITORY || root, 'show', baseline + ':' + file]);
const bytes = fs.readFileSync(path.join(root, file)), before = parse(beforeBytes.toString('utf8')), after = parse(bytes.toString('utf8'));
const get = (body,key) => { const matches = body.filter(n => n.key === key); assert.equal(matches.length,1,key); return matches[0].value; };
const walk = body => body.flatMap(n => [n, ...(Array.isArray(n.value) ? walk(n.value) : [])]);
const number = value => Number(value.startsWith('@') ? get(after,value) : value);
const fraBody = get(get(get(after, 'chaosx_startup_grant_fra'), 'FRA'), 'if');
const queueBranch = fraBody.find(n => n.key === 'if' && n.value.some(c => c.key === 'add_equipment_production'));
assert(queueBranch, 'France production branch');
const queue = get(queueBranch.value, 'add_equipment_production');
const checks = [], scenarios = [];
function check(id, fn) { fn(); checks.push({id, passed:true}); }
check('entire-startup-AST-preserved-except-France-queue-and-two-local-tunings', () => {
 const trimmed = structuredClone(after).filter(n => !['@fra_1939_respirator_factories','@fra_1939_respirator_efficiency'].includes(n.key));
 const body = get(get(get(trimmed,'chaosx_startup_grant_fra'),'FRA'),'if');
 const index = body.findIndex(n => n.key === 'if' && n.value.some(c => c.key === 'add_equipment_production'));
 assert(index >= 0); body.splice(index,1); assert.deepEqual(trimmed,before);
});
check('queue-only-requests-existing-factory-for-unlocked-French-basic-masks', () => {
 assert.deepEqual(queue.map(n => n.key), ['equipment','requested_factories','efficiency']);
 assert.equal(get(get(queue,'equipment'),'type'),'gas_mask_equipment_1'); assert.equal(get(get(queue,'equipment'),'creator'),'FRA');
 assert.equal(number(get(queue,'requested_factories')),1); assert.equal(number(get(queue,'efficiency')),100);
 const techIndex = fraBody.findIndex(n => n.key === 'set_technology');
 assert.equal(get(fraBody[techIndex].value,'basic_gas_masks'),'1'); assert(techIndex < fraBody.indexOf(queueBranch));
 assert.deepEqual(queueBranch.value.map(n => n.key), ['limit','add_equipment_production']);
});
function dateNumber(d) { const p = d.split('.').map(Number); return p[0]*10000+p[1]*100+p[2]; }
function condition(nodes, fixture) {
 return nodes.every(n => {
  if(n.key === 'exists') return fixture.exists === (n.value === 'yes');
  if(n.key === 'date') { assert.equal(n.op,'>'); return dateNumber(fixture.date) > dateNumber(n.value); }
  if(n.key === 'NOT') return !condition(n.value,fixture);
  if(n.key === 'has_global_flag') return fixture.flags.has(n.value);
  throw new Error('Unmodeled condition '+n.key);
 });
}
for (const [date, expected] of [['1936.1.1',false],['1938.12.31',false],['1939.1.1',true],['1939.8.14',true]]) {
 for(const exists of [false,true]) check('France-start-'+date+'-exists-'+exists, () => {
  const fixture={date,exists,flags:new Set()};
  const selected=condition(get(fraBody,'limit'),fixture) && condition(get(queueBranch.value,'limit'),fixture);
  assert.equal(selected,expected && exists); scenarios.push({date,exists,productionRequests:selected ? 1 : 0});
 });
}
check('public-startup-guard-prevents-a-second-France-queue-request', () => {
 const startup = get(get(after,'chaosx_apply_startup_history_grants'),'if'), guard = get(startup,'limit');
 const flagIndex=startup.findIndex(n => n.key === 'set_global_flag'), fraIndex=startup.findIndex(n => n.key === 'chaosx_startup_grant_fra');
 assert(flagIndex > 0 && flagIndex < fraIndex); assert.equal(walk(startup).filter(n => n.key === 'chaosx_startup_grant_fra').length,1);
 const fixture={date:'1939.8.14',exists:true,flags:new Set()}; let calls=0;
 for(let i=0;i<2;i++) if(condition(guard,fixture)) { fixture.flags.add(startup[flagIndex].value); calls++; }
 assert.equal(calls,1);
});
check('English-production-and-civilian-receipts-preserved', () => assert.deepEqual(get(after,'chaosx_startup_grant_eng'),get(before,'chaosx_startup_grant_eng')));
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const report={checks,scenarios,baselineCommit:baseline,baselineGitBlobSha256:sha(beforeBytes),currentSourceSha256:sha(bytes),file,
 limits:['Conditions are evaluated against source fixtures, not an HOI4 campaign. The public startup guard is projected without executing unrelated country grants.', 'One requested factory enters the native queue; actual allocation, efficiency handling and output remain native behavior, not guaranteed by this test.', 'No historical civilian quantity is inferred, and no free stock or factory building is added. All other startup AST content is unchanged.']};
fs.writeFileSync(path.join(__dirname,'source_test_results.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,scenarios,limits:report.limits},null,2));
