// Read-only source invariants. This is not a Clausewitz executor or native proof.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const root = __dirname;
const sha = value => crypto.createHash('sha256').update(value).digest('hex');
const read = (role, logical) => fs.readFileSync(path.join(root, role, logical));
const runtimePath = 'common/scripted_effects/033_acid_rain_effects.txt';
const triggerPath = 'common/scripted_triggers/033_acid_rain_triggers.txt';
const constantPath = 'common/script_constants/033_acid_rain_constants.txt';
function span(text, open) {
  let depth = 0, quoted = false, escaped = false, comment = false;
  for (let i = open; i < text.length; i++) {
    const c = text[i];
    if (comment) { if (c === '\n') comment = false; continue; }
    if (quoted) { if (!escaped && c === '"') quoted = false; escaped = !escaped && c === '\\'; continue; }
    if (c === '#') { comment = true; continue; }
    if (c === '"') { quoted = true; continue; }
    if (c === '{') depth++;
    if (c === '}' && --depth === 0) return i + 1;
  }
  throw new Error('Unterminated block');
}
function helper(text, id) {
  const start = text.indexOf('\n' + id + ' = {');
  if (start < 0) throw new Error('Helper not found: ' + id);
  const open = text.indexOf('{', start);
  return text.slice(start + 1, span(text, open));
}
function chanceBody(text, helperId, chanceVar, rollVar) {
  const body = helper(text, helperId);
  const start = body.indexOf('set_temp_variable = { ' + chanceVar + ' =');
  const comparator = body.indexOf('limit = { check_variable = { var = ' + rollVar + ' value = ' + chanceVar + ' compare = less_than_or_equals } }', start);
  if (start < 0 || comparator < 0) throw new Error('Chance body not found');
  return body.slice(start, span(body, body.indexOf('{', comparator)));
}
function draws(text) {
  const result = [];
  const re = /\b(set_(?:temp_)?variable_to_random)\s*=\s*\{/g;
  for (const m of text.matchAll(re)) {
    const open = text.indexOf('{', m.index);
    result.push(text.slice(m.index, span(text, open)).replace(/\s+/g, ' '));
  }
  return result;
}
const before = read('before-source', runtimePath), after = read('after_8b85ebaf', runtimePath);
const a = before.toString('utf8'), b = after.toString('utf8');
const chanceChecks = [
  ['severe', 'acid_rain_try_severe_evolution', 'acid_rain_severe_chance', 'acid_rain_severe_roll'],
  ['third_front', 'acid_rain_try_multiple_fronts', 'acid_rain_third_front_chance', 'acid_rain_third_front_roll'],
].map(([id, helperId, chanceVar, rollVar]) => {
  const oldBody = chanceBody(a, helperId, chanceVar, rollVar), newBody = chanceBody(b, helperId, chanceVar, rollVar);
  return { id, helper: helperId, beforeSha256: sha(oldBody), afterSha256: sha(newBody), exactTextEqual: oldBody === newBody };
});
const unchangedHelperChecks = [
  'acid_rain_compute_region_candidate_weight', 'acid_rain_select_weighted_region',
  'acid_rain_append_state_to_severe_weighted_pool', 'acid_rain_create_severe_cell',
  'acid_rain_append_state_to_superstorm_weighted_pool', 'acid_rain_process_severe_cells',
  'acid_rain_process_superstorms', 'acid_rain_apply_dissipation_step',
  'acid_rain_host_worker', 'acid_rain_try_severe_impact_chaos',
].map(id => { const oldBody = helper(a, id), newBody = helper(b, id); return { helper: id, beforeSha256: sha(oldBody), afterSha256: sha(newBody), exactTextEqual: oldBody === newBody }; });
const oldConstants = read('before-source', constantPath), newConstants = read('after_8b85ebaf', constantPath);
let restoredConstants = newConstants.toString('utf8');
const tierMapping = [['i', 1, 2], ['ii', 2, 3], ['iii', 3, 4]];
for (const [stage, oldValue, newValue] of tierMapping) {
  const re = new RegExp('evolution_' + stage + '_tier = ' + newValue + '(?=\\r?\\n)', 'g');
  if ([...restoredConstants.matchAll(re)].length !== 1) throw new Error('Tier mapping multiplicity');
  restoredConstants = restoredConstants.replace(re, 'evolution_' + stage + '_tier = ' + oldValue);
}
const result = {
  scope: 'Frozen raw source invariants only; no engine/helper-lifetime or native eligibility claim.',
  runtime: { beforeSha256: sha(before), afterSha256: sha(after) },
  triggers: { beforeSha256: sha(read('before-source', triggerPath)), afterSha256: sha(read('after_8b85ebaf', triggerPath)) },
  constants: { beforeSha256: sha(oldConstants), afterSha256: sha(newConstants), onlyThreeDisplayTierChanges: Buffer.from(restoredConstants).equals(oldConstants), tierMapping },
  chanceChecks, unchangedHelperChecks,
  randomDraws: { before: draws(a).length, after: draws(b).length, orderedCommandArgumentsEqual: JSON.stringify(draws(a)) === JSON.stringify(draws(b)) },
};
if (!result.constants.onlyThreeDisplayTierChanges || !chanceChecks.every(x => x.exactTextEqual) || !unchangedHelperChecks.every(x => x.exactTextEqual) || !result.randomDraws.orderedCommandArgumentsEqual) throw new Error(JSON.stringify(result));
console.log(JSON.stringify(result, null, 2));
