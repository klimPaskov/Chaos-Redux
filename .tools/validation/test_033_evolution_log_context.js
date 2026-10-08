// Real Event033 bridge execution with conservative temporary frames.
// Shared append fields are read from the actual logger, not native row execution.
const fs = require('fs'), assert = require('assert/strict'), cp = require('child_process');
const { parse, namedBlock, assignment, hash } = require('../../docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03.js');
const path = 'common/scripted_effects/033_acid_rain_effects.txt';
const before = process.argv.includes('--before');
const bytes = before ? cp.execFileSync('git', ['show', '03447df6c5e4226525d2c26dc450f103d2297e78:' + path]) : fs.readFileSync(path);
const body = parse(namedBlock(bytes.toString('utf8'), 'acid_rain_record_evolution'))[0].value;
const constants = new Map();
for (const c of parse(fs.readFileSync('common/script_constants/033_acid_rain_constants.txt', 'utf8')))
  for (const n of Array.isArray(c.value) ? c.value : [])
    if (!Array.isArray(n.value) && Number.isFinite(Number(n.value))) constants.set('constant:' + c.key + '.' + n.key, Number(n.value));
const loggerBytes = fs.readFileSync('common/scripted_effects/chaosx_events_log_effects.txt');
const logger = parse(namedBlock(loggerBytes.toString('utf8'), 'record_events_log_evolution_entry'))[0].value;
const append = name => {
  const n = logger.find(n => n.key === 'add_to_array' && n.value.some(x => x.key === 'array' && x.value === name));
  assert.ok(n, 'actual shared append missing: ' + name);
  return n.value.find(x => x.key === 'value').value;
};
assert.equal(append('global.events_log_evolution_stage_entries'), 'events_log_evolution_stage');
assert.equal(append('global.events_log_evolution_tier_entries'), 'events_log_evolution_tier');
let count = 0;
for (const stage of [1, 2, 3]) for (const ambient of [undefined, 9, 2]) for (const withHost of [false, true]) {
  const parent = new Map([['acid_rain_evolution_stage', stage], ['acid_rain_evolution_tier', stage], ['sentinel', 71]]);
  if (ambient !== undefined) { parent.set('events_log_evolution_stage', ambient); parent.set('events_log_evolution_tier', ambient); }
  const host = { type: 'country', id: 'AST' }, targets = new Map(withHost ? [['acid_rain_runtime_host', host]] : []);
  const child = new Map(parent), inherited = new Set(parent.keys());
  const read = token => constants.get(token) ?? child.get(token) ?? Number(token);
  let observed, calls = 0;
  function run(nodes) {
    for (const n of nodes) {
      if (n.key === 'set_temp_variable') { const [key, value] = assignment(n); child.set(key, read(value)); }
      else if (n.key === 'if') {
        const limit = n.value.find(x => x.key === 'limit');
        assert.ok(limit.value.every(x => x.key === 'has_event_target'));
        if (limit.value.every(x => targets.has(x.value))) run(n.value.filter(x => x.key !== 'limit'));
      } else if (n.key === 'event_target:acid_rain_runtime_host') {
        assert.deepEqual(n.value, [{ key: 'save_event_target_as', op: '=', value: 'events_log_evolution_actor' }]);
        targets.set('events_log_evolution_actor', targets.get('acid_rain_runtime_host'));
      } else if (n.key === 'record_events_log_evolution_entry') {
        calls++;
        observed = Object.fromEntries(['event_id', 'type', 'stage', 'tier', 'has_actor'].map(k => [k, child.get('events_log_evolution_' + k)]));
        if (withHost) assert.equal(targets.get('events_log_evolution_actor'), host);
      } else throw Error('unmodelled bridge effect: ' + n.key);
    }
  }
  run(body);
  for (const key of inherited) parent.set(key, child.get(key));
  assert.equal(calls, 1);
  assert.deepEqual(observed, { event_id: 33, type: 33, stage, tier: stage, has_actor: withHost ? 1 : 0 });
  assert.equal(parent.get('sentinel'), 71);
  assert.equal(parent.get('acid_rain_evolution_stage'), stage);
  if (ambient === undefined) assert.equal(parent.has('events_log_evolution_stage'), false, 'child-created output escaped');
  count++;
}
console.log(JSON.stringify({ status: 'pass', bridge_sha256: hash(bytes), shared_logger_sha256: hash(loggerBytes), cases: count,
  limits: ['Shared logging and native arrays are a call spy plus actual append-field contract', 'Caller impact receipts, evolution eligibility and in-game log UI are not executed'] }));
