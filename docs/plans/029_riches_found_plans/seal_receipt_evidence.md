# Event 029 sealing receipt evidence

Archived verbatim from [the sealing receipt contract](../../events/029_riches_found/seal_receipt_contract.md). The historical blocker, the counterexample, the source diagnostic, the 2026-10-08 native-lifecycle follow-up and the helper source cases are records. The contract is the current implemented API and parent callsite contract in the events file.

## Historical initial blocked report

The bounded assignment dated 2026-10-08 authorizes only `gold_seal_depths` and `demons_permanent_seal` and explicitly requires a blocker instead of executable substitute logic when native callback identity cannot be established.
No sealing receipt effects, triggers, or constants are installed by this sidecar.
The proposed interface below is not an implemented API.
The existing transport receipt module is unintegrated and its documented callback identity limitation applies here too.

## Blocking counterexample

Retaining a payer/mine/family slot until its native callback closes is necessary, but does not establish safety after reuse.
Consider this sequence for country A, mine M with immutable sequence S, and either sealing family F:

1. A pays project P1 at controller epoch E1.
2. Control changes to B and then to A, advancing the state epoch to E3.
3. P1's native callback rejects the mismatched epoch, refunds P1's exact saved quote, and closes its pending slot.
4. A pays P2 for the same M/S/F at E3.
5. A late duplicate callback belonging to P1 runs after P2 has been paid, potentially at P2's due time.

The late P1 callback and the legitimate P2 callback expose the same documented actor ROOT, target FROM, current mine sequence, current controller epoch, family selected by the static decision, and current actor-owned pending receipt.
Even a saved due date or a scripted generation counter does not distinguish them at P2's due time because neither callback carries its own immutable copy.
The old callback can consume P2, complete P2 early if no due gate exists, or refund P2 if a finish requirement fails.
A subsequent P2 callback then lacks its receipt.
This is an indistinguishability counterexample under explicitly allowed duplicate delivery, not evidence that HOI4 actually delivers duplicate native callbacks.

The missing evidence is either a native immutable invocation identity accessible in the callback, or an authoritative guarantee that a closed native targeted-decision timer cannot deliver an older callback after the same actor/target/family is restarted.
Installed `activate_targeted_decision` documentation says an entry cannot be activated while active in the interface.
That establishes an active-entry restriction, not the required post-closure delivery guarantee.
The timer documentation and vanilla `AST_union_strike` establish selection, removal, cancellation, and modifier structure, but do not answer this identity question.
No virtual timeout, receipt erasure on transfer, permanent ban on retries, alternative currency, factory refund, or replacement mission is used to evade it.

## Source diagnostic, separate from receipt implementation tests

The following runnable diagnostic parses the actual current decision gates and recursively evaluates their production scripted triggers.
It extracts actual discrete payment/refund instructions and resolves the current constants.
It executes no successful mine effects, native timers, reservations, or whole-world iterators.
It intentionally fails on an unsupported gate token and pins the exact shared decision bytes.
Its last assertion compares identical callback-visible inputs for the late-old and valid-new cases.
There are no production receipt helpers to test because implementation is blocked.

<!-- seal-source-diagnostic:start -->
```javascript
const fs = require('node:fs');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const read = p => fs.readFileSync(p, 'utf8');
const path = 'common/decisions/029_riches_found_decisions.txt';
assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path)).digest('hex'),
  '88b2f6716f401657251bc79c8c144b081953d71725b81f693f630f28aee36b8d');
function parse(text) {
  const tokens = text.match(/"(?:\\.|[^"\\])*"|#[^\r\n]*|[{}=<>]|[^\s{}=<>]+/g)
    .filter(t => !t.startsWith('#'));
  let i = 0;
  function block(nested = false) {
    const rows = [];
    while (i < tokens.length && tokens[i] !== '}') {
      const key = tokens[i++], op = tokens[i++];
      assert(['=', '<', '>'].includes(op), `unsupported syntax at ${key}`);
      let value = tokens[i++];
      if (value === '{') value = block(true);
      rows.push({key, op, value});
    }
    if (nested) assert.equal(tokens[i++], '}');
    return rows;
  }
  return block();
}
const decisions = parse(read(path));
const triggers = parse(read('common/scripted_triggers/029_riches_found_triggers.txt'));
const constants = parse(read('common/script_constants/029_riches_found_constants.txt'));
function find(rows, key) {
  for (const row of rows) {
    if (row.key === key) return row.value;
    if (Array.isArray(row.value)) { const value = find(row.value, key); if (value !== undefined) return value; }
  }
  return undefined;
}
function direct(rows, key) {
  const matches = rows.filter(r => r.key === key);
  assert.equal(matches.length, 1, `expected one ${key}`);
  return matches[0].value;
}
function number(token) {
  if (!token.startsWith('constant:')) return Number(token);
  const [category, key] = token.slice(9).split('.');
  return Number(direct(direct(constants, category), key));
}
function testRow(row, ctx) {
  const {key, value} = row;
  if (key === 'FROM' || key === 'AND') return value.every(r => testRow(r, ctx));
  if (key === 'OR') return value.some(r => testRow(r, ctx));
  if (key === 'NOT') return !value.some(r => testRow(r, ctx));
  if (key === 'has_state_flag') return ctx.flags.has(value);
  if (key === 'has_variable') return Object.hasOwn(ctx.vars, value);
  if (key === 'is_controlled_by') { assert.equal(value, 'ROOT'); return ctx.controller === ctx.actor; }
  const helper = triggers.find(r => r.key === key);
  assert(helper && value === 'yes', `unsupported gate ${key}`);
  return helper.value.every(r => testRow(r, ctx));
}
function quote(rows) {
  return rows.filter(r => ['add_manpower', 'add_equipment_to_stockpile'].includes(r.key)).map(r => {
    if (r.key === 'add_manpower') return number(r.value);
    assert.equal(direct(r.value, 'type'), 'support_equipment');
    return number(direct(r.value, 'amount'));
  });
}
let checks = 0;
for (const [family, mp] of [['gold_seal_depths', 300], ['demons_permanent_seal', 600]]) {
  const decision = find(decisions, `decision_riches_found_${family}`);
  const removal = direct(decision, 'remove_effect');
  const gate = direct(direct(removal, 'if'), 'limit');
  const flags = new Set(['riches_found_mine_registered',
    family.startsWith('gold') ? 'riches_found_layer_gold' : 'riches_found_layer_demons',
    family.startsWith('gold') ? 'riches_found_gold_quarantine' : 'riches_found_demons_military_purge']);
  const ctx = {actor: 'A', controller: 'A', flags, vars: {riches_found_mine_sequence: 1}};
  const valid = () => gate.every(r => testRow(r, ctx));
  assert.deepEqual(quote(direct(decision, 'complete_effect')), [-mp, -150]); checks++;
  assert(valid()); checks++;
  ctx.controller = 'B'; assert(!valid()); checks++;
  ctx.controller = 'A'; assert(valid()); checks++;
  flags.add('riches_found_mine_terminal'); assert(!valid()); checks++;
  assert.deepEqual(quote(direct(removal, 'else')), [mp, 150]); checks++;
  flags.delete('riches_found_mine_terminal');
  if (family.startsWith('gold')) {
    flags.delete('riches_found_gold_quarantine'); assert(!valid()); checks++;
    flags.add('riches_found_gold_quarantine');
  } else {
    flags.add('riches_found_contract_active'); assert(!valid()); checks++;
    flags.delete('riches_found_contract_active');
  }
  const original = direct(direct(constants, 'riches_found_decision_cost'),
    family.startsWith('gold') ? 'manpower_standard' : 'manpower_heavy');
  const costRow = direct(constants, 'riches_found_decision_cost').find(r => r.value === original &&
    r.key === (family.startsWith('gold') ? 'manpower_standard' : 'manpower_heavy'));
  costRow.value = String(mp + 1);
  assert.deepEqual(quote(direct(removal, 'else')), [mp + 1, 150]); checks++;
  costRow.value = original;
  const visibleInput = {actor: 'A', state: 'M', family, sequence: 1, epoch: 3,
    pending: true, paidManpower: mp, paidSupport: 150, now: 200, due: 200};
  const lateOld = {...visibleInput}, legitimateNew = {...visibleInput};
  assert.deepEqual(lateOld, legitimateNew); checks++;
}
console.log(JSON.stringify({checks, evidence: 'source gates and instruction extraction only',
  awayAndBackRejected: false, refundsUseStoredQuote: false,
  invocationIdentityProven: false, nativeReservationProven: false}));
```
<!-- seal-source-diagnostic:end -->

Run from the repository root without creating a test file:

```powershell
$taskContract = Get-Content -Raw -Encoding UTF8 -LiteralPath 'docs/events/029_riches_found/seal_receipt_contract.md'
$taskCode = [regex]::Match($taskContract, '(?s)<!-- seal-source-diagnostic:start -->\s*```javascript\s*(.*?)\s*```').Groups[1].Value
$taskCode | & 'C:/Program Files/nodejs/node.exe' -
```

Required future production cases are paid once, away, away/back, second payer, same actor pending restart, parallel different mine, consume once, saved quote after tuning change, terminal cleanup with another payer pending, spurious same controller, and late old callback after repayment.
The source diagnostic covers current gate/quote behavior for away, away/back, terminal rejection, route rejection, and tuning changes, plus the identity counterexample.
It does not pass the unimplemented paid-once, pending-restart, parallelism, consume-once, cleanup, or epoch helper cases.
Those cases must execute the actual helpers, model caller-owned temporary frames, and preserve every outstanding native callback before implementation can be claimed complete.

Future work is limited to resolving the native identity and numeric representation evidence, then implementing and reviewing the bounded helpers and parent call sites under this contract.

## Bounded native-lifecycle follow-up, 2026-10-08

This appended finding qualifies the earlier blocker and equal-input diagnostic.
The earlier sections remain the historical sidecar report, and this follow-up does not authorize implementation.
The duplicate-call counterexample does not establish native production reachability or unconditional impossibility of receipts without an exposed nonce.

The primary timer section was reread through live `hoi4.reference_read`: `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:337-356`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
It states that selection starts the timer, `remove_effect` executes when the timer ends, the timer lasts until the decision is removed, and `remove_trigger` removes the decision while executing `remove_effect`.
Cancellation explicitly ends the timer without executing `remove_effect`, then executes `cancel_effect`.
Loss of visibility does not itself cancel the timer by default.

Installed `common/decisions/_documentation.md:1-46` documents actor/target evaluation but supplies no separate effect-delivery guarantee.
Installed `documentation/effects_documentation.md:696-705` rejects activation of an already active targeted entry, `5959-5967` removes an active ordinary decision without `remove_effect`, and `6276-6285` documents targeted removal without specifying its callback side effects.
Those effect sections were read through the live MCP with revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Targeted manual removal must therefore not be substituted for a proven receipt-closing boundary.

Two targeted vanilla precedents were read through live `hoi4.source_lookup`, source-index revision `3a99bda63b31e2c33f5327855ff2e46d33b8c94b060e56094777dbd318c2d628`, and installed source:

- `game:common/decisions/AST.txt:114-178`, `AST_seize_local_leadership_in_state_major`, uses state targeting, a 14-day native timer, and FROM inside inline `remove_effect`.
- `game:common/decisions/AST.txt:433-512`, `AST_organize_in_nation`, is repeatable, sets its pending flag in `complete_effect`, and clears it inline in `remove_effect` after its delayed result.
  Its separate country event is a gameplay consequence, so it is not evidence that native removal itself schedules a second receipt callback.

The second MCP definition page returned lines 433-507 and continuation `nextLine=508`, with its remaining lines 508-512 read directly from installed source.
The first definition was returned in full.
Both reads deliberately excluded references.
Installed AST file SHA-256 remains `AAD50DA745F5A93C5F7470E06ED990A49A5416C81810849C8A2312600E81F4F2`.

For the documented direct native lifecycle, termination supplies the serialization boundary without requiring a script-visible nonce.
A pending actor/mine/family slot retained through that boundary cannot be repaid while A remains pending.
A resolving once after control leaves and returns is a current-source case that an epoch mismatch can reject.
Once A ends and refunds inline, a subsequently started B has a different live native timer.
Invoking A again after B starts requires an additional delivery mechanism or anomalous native duplication that this review has not established.
The injected equal-input test alone cannot make that extra delivery production reachable.

Accordingly, absence of a nonce alone is not an established blocker for the parent's direct-native-boundary design.
This conclusion relies on documented native termination semantics, not observed engine execution or an explicit engine-level exactly-once theorem covering duplicate delivery, reentrancy, or external manual removal.
The current two decision blocks have inline native resolution and no scheduled country-event receipt resolver.
A bounded literal search found no activate/remove-decision commands in Event 029-owned effect/on-action/event files, and the two decision IDs occur in their definitions and tooltip tokens only within the searched gameplay directories.
This is a bounded source result, not exhaustive proof against dynamically constructed external callers.

Normal-variable bounds are documented, rather than absent.
Live MCP search/read of `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:425-434`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, identifies the exact bounds paragraph at line 427.
Its effective range is -2,147,483,648.99999 through 2,147,483,647.99999, with 0.00001 precision, truncation beyond that precision, and overflow wrapping.
The paragraph's introductory signed-integer sentence has an inconsistent positive endpoint, but its stated effective range gives the usual signed 32-bit maximum.
Thus 2,147,483,647 is the cited maximum nonnegative whole-number value for normal-variable identity arithmetic.
The installed math-expression section's fixed-point statement is about math expressions and does not contradict or replace this normal-variable passage.
No 2.1-million normal-variable cap follows from the deprecated raw-manpower getter limit.
Rollover handling remains an implementation requirement, and wrapping or reusing an epoch while a matching old receipt remains pending would need separate protection.

The receipt package remains unimplemented pending parent acceptance and its required validation.
Factory reservation order/atomicity, complete receipt source cases, and safe epoch rollover remain explicit gaps.
No weaker fallback, virtual deadline, executable file, gameplay edit, Git operation, or game launch is approved or performed by this follow-up.

## Actual helper source cases, accepted implementation

The following source executor loads the production receipt helpers, their constants, the actual four existing route/registration triggers, and the actual shared support-equipment debit helper.
It models only native primitives, typed country/state pointers, and caller-frame temporary cleanup.
It rejects unknown commands and arithmetic outside the documented normal-variable range.
Fixed-point arithmetic uses integer units of 0.00001 with truncation on division.
Native timers, native factory reservation, success gameplay consumers, engine meta parsing, and save persistence remain outside this source executor.
Private native-boundary helpers are exercised only as source transactions, and repeated calls before repayment test idempotence without asserting production duplicate delivery.

<!-- seal-helper-cases:start -->
```javascript
const fs = require('node:fs');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const S = 100000n, MAX = 2147483647n * S, MIN = -2147483648n * S;
const read = p => fs.readFileSync(p, 'utf8');
function parse(text) {
  const t = (text.match(/"(?:\\.|[^"\\])*"|#[^\r\n]*|[{}=<>]|[^\s{}=<>]+/g) || []).filter(x => !x.startsWith('#'));
  let i = 0;
  function block(nested = false) {
    const r = [];
    while (i < t.length && t[i] !== '}') {
      const k = t[i++], op = t[i++];
      assert(['=', '<', '>'].includes(op), `parse ${k} ${op}`);
      let v = t[i++]; if (v === '{') v = block(true);
      r.push({k, op, v});
    }
    if (nested) assert.equal(t[i++], '}');
    return r;
  }
  return block();
}
function extract(text, name) {
  const re = new RegExp('^' + name + '\\s*=\\s*\\{', 'm');
  const m = re.exec(text); assert(m, `missing ${name}`);
  const tokens = text.slice(m.index).match(/"(?:\\.|[^"\\])*"|#[^\r\n]*|[{}]|[^\s{}]+/g);
  let depth = 0, begun = false, selected = [];
  for (const t of tokens) {
    selected.push(t);
    if (t.startsWith('#')) selected[selected.length - 1] += '\n';
    else if (t === '{') { depth++; begun = true; }
    else if (t === '}' && --depth === 0 && begun) break;
  }
  return parse(selected.join(' '))[0];
}
function fp(x) {
  const text = String(x), neg = text.startsWith('-');
  const [a, b = ''] = text.replace(/^-/, '').split('.');
  return (neg ? -1n : 1n) * (BigInt(a) * S + BigInt((b + '00000').slice(0, 5)));
}
const helpers = new Map(), constants = new Map(), hashes = {};
for (const path of ['common/scripted_effects/029_riches_found_seal_receipt_effects.txt',
  'common/scripted_triggers/029_riches_found_seal_receipt_triggers.txt']) {
  hashes[path] = crypto.createHash('sha256').update(fs.readFileSync(path)).digest('hex');
  for (const r of parse(read(path))) helpers.set(r.k, r.v);
}
for (const name of ['riches_found_mine_is_registered', 'riches_found_mine_is_terminal',
  'riches_found_gold_route_is_restricted', 'riches_found_demons_district_cleared']) {
  const r = extract(read('common/scripted_triggers/029_riches_found_triggers.txt'), name); helpers.set(r.k, r.v);
}
const debit = extract(read('common/scripted_effects/chaosx_dynamic_effects.txt'), 'remove_support_equipment_from_stockpile');
helpers.set(debit.k, debit.v);
for (const [path, categories] of [
  ['common/script_constants/029_riches_found_seal_receipt_constants.txt', ['rf_seal_protocol']],
  ['common/script_constants/029_riches_found_constants.txt', ['riches_found_decision_cost', 'riches_found_decision_duration']]]) {
  for (const category of categories) for (const r of extract(read(path), category).v)
    if (!Array.isArray(r.v)) constants.set(`${category}.${r.k}`, fp(r.v));
}
let temps = new Map(), writes = [], tests = [];
const outputs = ['family', 'result', 'mine_seq', 'payer', 'state', 'epoch', 'manpower', 'support',
  'civilian', 'days', 'refund_manpower', 'refund_support', 'closed'].map(x => 'rf_seal_' + x);
function actor(id) { return {type: 'country', id, alive: true, vars: new Map(), flags: new Set(), mp: fp(10000), support: fp(10000)}; }
function mine(seq, controller) { return {type: 'state', id: 'M' + seq, controller,
  vars: new Map([['riches_found_mine_sequence', fp(seq)]]), flags: new Set(['riches_found_mine_registered',
    'riches_found_layer_gold', 'riches_found_gold_quarantine', 'riches_found_layer_demons', 'riches_found_demons_military_purge'])}; }
function scope(token, c) {
  if (token === 'THIS') return c.this;
  if (token === 'ROOT') return c.root;
  if (token === 'FROM') return c.from;
  if (token === 'FROM.FROM') return c.fromFrom;
  throw new Error(`scope ${token}`);
}
function name(token, c) {
  return token.replace(/@var:([a-z0-9_]+)/g, (_, key) => {
    const value = get(key, c); assert(typeof value === 'bigint' && value % S === 0n);
    return '@' + value / S;
  });
}
function get(token, c) {
  if (token.startsWith('var:')) return get(token.slice(4), c);
  if (/^-?\d+(\.\d+)?$/.test(token)) return fp(token);
  if (token.startsWith('constant:')) { assert(constants.has(token.slice(9)), token); return constants.get(token.slice(9)); }
  if (['THIS', 'ROOT', 'FROM', 'FROM.FROM'].includes(token)) return scope(token, c);
  if (token.startsWith('FROM.')) return scope('FROM', c).vars.get(name(token.slice(5), c)) ?? 0n;
  if (temps.has(token)) return temps.get(token);
  if (token === 'manpower_k') { assert.equal(c.this.type, 'country'); return c.this.mp / 1000n; }
  if (token === 'num_equipment@support_equipment') { assert.equal(c.this.type, 'country'); return c.this.support; }
  return c.this.vars.get(name(token, c)) ?? 0n;
}
function put(map, key, value, c, persistent) {
  if (typeof value === 'bigint') assert(value >= MIN && value <= MAX + S - 1n, `overflow ${key}`);
  map.set(key, value); if (persistent) writes.push({scope: c.this.id, key, value});
}
function arithmetic(r, c) {
  const long = r.v.find(x => x.k === 'var');
  const key = long ? long.v : r.v[0].k;
  const operand = get(long ? r.v.find(x => x.k === 'value').v : r.v[0].v, c);
  const temp = r.k.includes('temp_variable'), map = temp ? temps : c.this.vars;
  const target = temp ? key : name(key, c), old = map.get(target) ?? 0n;
  let value = operand;
  if (r.k.startsWith('add_')) value = old + operand;
  if (r.k.startsWith('subtract_')) value = old - operand;
  if (r.k.startsWith('multiply_')) value = old * operand / S;
  if (r.k.startsWith('divide_')) value = old * S / operand;
  if (r.k.startsWith('modulo_')) value = old % operand;
  put(map, target, value, c, !temp); return true;
}
function compare(r, c) {
  const long = r.v.find(x => x.k === 'var');
  const a = get(long ? long.v : r.v[0].k, c), b = get(long ? r.v.find(x => x.k === 'value').v : r.v[0].v, c);
  const op = long ? r.v.find(x => x.k === 'compare').v : ({'=':'equals','<':'less_than','>':'greater_than'}[r.v[0].op]);
  return ({equals: () => a === b, less_than: () => a < b, greater_than: () => a > b,
    less_than_or_equals: () => a <= b, greater_than_or_equals: () => a >= b}[op])();
}
function expand(rows, replacements) {
  const sub = s => s.replace(/\[([A-Z_]+)\]/g, (_, key) => { assert(Object.hasOwn(replacements, key)); return replacements[key]; });
  return rows.map(r => ({k: sub(r.k), op: r.op, v: Array.isArray(r.v) ? expand(r.v, replacements) : sub(r.v)}));
}
function invoke(helper, c, kind) {
  assert(helpers.has(helper), `unknown helper ${helper}`);
  const old = new Set(temps.keys());
  const result = run(helpers.get(helper), c, kind);
  for (const key of [...temps.keys()]) if (!old.has(key)) temps.delete(key);
  return result;
}
function row(r, c, kind) {
  if (helpers.has(r.k)) { assert.equal(r.v, 'yes'); return invoke(r.k, c, kind); }
  if (['FROM', 'ROOT', 'FROM.FROM'].includes(r.k)) return run(r.v, {...c, this: scope(r.k, c)}, kind);
  if (r.k === 'OR') return r.v.some(x => row(x, c, 'trigger'));
  if (r.k === 'NOT') return !r.v.some(x => row(x, c, 'trigger'));
  if (r.k === 'AND') return run(r.v, c, 'trigger');
  if (r.k === 'exists') { assert.equal(c.this.type, 'country'); return c.this.alive; }
  if (r.k === 'is_controlled_by') { assert.equal(c.this.type, 'state'); return c.this.controller === get(r.v, c); }
  if (r.k === 'has_variable') return c.this.vars.has(name(r.v, c));
  if (r.k.startsWith('has_') && r.k.endsWith('_flag')) return c.this.flags.has(r.v);
  if (r.k === 'check_variable') return compare(r, c);
  if (/^(set|add_to|subtract_from|multiply|divide|modulo)_(temp_)?variable$/.test(r.k)) return arithmetic(r, c);
  if (r.k === 'clear_variable') { c.this.vars.delete(name(r.v, c)); writes.push({scope:c.this.id,key:name(r.v,c),clear:true}); return true; }
  if (/^(set|clr)_(country|state)_flag$/.test(r.k)) {
    assert.equal(c.this.type, r.k.includes('country') ? 'country' : 'state');
    if (r.k.startsWith('set_')) c.this.flags.add(r.v); else c.this.flags.delete(r.v);
    writes.push({scope:c.this.id,key:r.v,flag:true}); return true;
  }
  if (r.k === 'meta_effect' || r.k === 'meta_trigger') {
    const replacements = {};
    for (const x of r.v.filter(x => x.k !== 'text')) {
      const match = /^"\[\?([a-z0-9_]+)\|\.0\]"$/.exec(x.v); assert(match, `meta argument ${x.v}`);
      const value = get(match[1], c); assert(typeof value === 'bigint' && value % S === 0n);
      replacements[x.k] = String(value / S);
    }
    return run(expand(r.v.find(x => x.k === 'text').v, replacements), c, r.k === 'meta_trigger' ? 'trigger' : 'effect');
  }
  if (r.k === 'add_manpower') { assert.equal(c.this.type, 'country'); c.this.mp += get(r.v, c); writes.push({scope:c.this.id,key:'manpower',amount:get(r.v,c)}); return true; }
  if (r.k === 'add_equipment_to_stockpile') {
    assert.equal(c.this.type, 'country'); assert.equal(r.v.find(x => x.k === 'type').v, 'support_equipment');
    const amount = get(r.v.find(x => x.k === 'amount').v, c); c.this.support += amount;
    writes.push({scope:c.this.id,key:'support',amount}); return true;
  }
  throw new Error(`unmodelled ${r.k}`);
}
function run(rows, c, kind) {
  for (let i = 0; i < rows.length; i++) {
    const r = rows[i];
    if (r.k === 'if') {
      const condition = run(r.v.find(x => x.k === 'limit').v, c, 'trigger');
      let pass = true;
      if (condition) pass = run(r.v.filter(x => x.k !== 'limit'), c, kind);
      if (rows[i + 1]?.k === 'else') {
        if (!condition) pass = run(rows[i + 1].v, c, kind);
        i++;
      }
      if (kind === 'trigger' && !pass) return false;
    } else if (!row(r, c, kind) && kind === 'trigger') return false;
  }
  return true;
}
function call(helper, a, m, options = {}) {
  temps = new Map(outputs.map(k => [k, 0n])); writes = [];
  const c = {this:a, root:options.root ?? a, from:m};
  const value = invoke(helper, c, helper.includes('_quote') || helper.includes('_can_start') ? 'trigger' : 'effect');
  return {value, result:temps.get('rf_seal_result') / S, refundMP:temps.get('rf_seal_refund_manpower') / S,
    refundSupport:temps.get('rf_seal_refund_support') / S, writes:[...writes]};
}
function transfer(m, next, old = m.controller) {
  m.controller = next; temps = new Map(); writes = [];
  invoke('rf_seal_note_control_change', {this:m, root:next, from:old, fromFrom:m}, 'effect'); return [...writes];
}
const count = m => (m.vars.get('rf_seal_pending_count') ?? 0n) / S;
const epoch = m => (m.vars.get('rf_seal_control_epoch') ?? 0n) / S;
function test(label, body) { body(); tests.push(label); }
for (const [family, mp] of [['gold',300n], ['demons',600n]]) {
  const start = `rf_${family}_seal_start`, resolve = `rf_${family}_seal_resolve`, can = `rf_${family}_seal_can_start_manual`;
  test(`${family}: paid once and pending restart`, () => {
    const a=actor('A'), m=mine(1,a); const receipt=call(start,a,m); assert.equal(receipt.result,1n);
    const debitIndex=receipt.writes.findIndex(w=>w.key==='manpower');
    const publicationIndex=receipt.writes.findIndex(w=>w.key.startsWith('rf_seal_pending_'));
    const countIndex=receipt.writes.findIndex(w=>w.key==='rf_seal_pending_count');
    assert(publicationIndex>=0 && publicationIndex<debitIndex && countIndex<debitIndex);
    assert.equal(a.mp,fp(10000)-mp*S); assert.equal(a.support,fp(9850)); assert.equal(count(m),1n);
    assert.equal(call(can,a,m).value,false); assert.equal(call(start,a,m).result,4n); assert.equal(count(m),1n);
    assert.equal(a.mp,fp(10000)-mp*S); assert.equal(a.support,fp(9850));
  });
  test(`${family}: changed resources rechecked before debit`, () => {
    const a=actor('A'), m=mine(1,a); assert(call(can,a,m).value); a.mp=mp*S-1n;
    const rejected=call(start,a,m); assert.equal(rejected.result,4n); assert.equal(rejected.writes.length,0); assert.equal(count(m),0n);
    a.mp=fp(10000); a.support=fp(149); assert.equal(call(start,a,m).result,4n); assert.equal(count(m),0n);
  });
  test(`${family}: transfer away and exact original payer refund`, () => {
    const a=actor('A'), b=actor('B'), m=mine(1,a); call(start,a,m); transfer(m,b);
    assert.equal(count(m),1n); const r=call(resolve,a,m); assert.equal(r.result,3n); assert.equal(r.refundMP,mp);
    assert.equal(r.refundSupport,150n); assert.equal(a.mp,fp(10000)); assert.equal(b.mp,fp(10000)); assert.equal(count(m),0n);
  });
  test(`${family}: away and back rejected by epoch, then native retry`, () => {
    const a=actor('A'), b=actor('B'), m=mine(1,a); call(start,a,m); transfer(m,b); transfer(m,a);
    assert.equal(epoch(m),2n); assert.equal(call(start,a,m).result,4n); assert.equal(call(resolve,a,m).result,3n);
    assert.equal(call(start,a,m).result,1n); assert.equal(call(resolve,a,m).result,2n);
  });
  test(`${family}: parallel mines and independent second payer`, () => {
    const a=actor('A'), b=actor('B'), m=mine(1,a), n=mine(2,a); call(start,a,m); call(start,a,n);
    assert.equal(count(m),1n); assert.equal(count(n),1n); transfer(m,b); assert.equal(call(start,b,m).result,1n);
    assert.equal(count(m),2n); assert.equal(call(resolve,a,m).result,3n); assert.equal(count(m),1n);
    assert.equal(call(resolve,b,m).result,2n); assert.equal(call(resolve,a,n).result,2n);
  });
  test(`${family}: saved quote survives tuning and receipt consumed once`, () => {
    const a=actor('A'), b=actor('B'), m=mine(1,a); call(start,a,m); transfer(m,b);
    const key=`riches_found_decision_cost.manpower_${family==='gold'?'standard':'heavy'}`;
    const old=constants.get(key), support=constants.get('riches_found_decision_cost.support_heavy');
    constants.set(key,fp(999)); constants.set('riches_found_decision_cost.support_heavy',fp(777));
    const r=call(resolve,a,m); assert.equal(r.refundMP,mp); assert.equal(r.refundSupport,150n);
    assert.equal(call(resolve,a,m).result,0n); assert.equal(a.mp,fp(10000)); assert.equal(a.support,fp(10000));
    constants.set(key,old); constants.set('riches_found_decision_cost.support_heavy',support);
    transfer(m,a); call(start,a,m); assert.equal(call(resolve,a,m).result,2n);
    const paid=a.mp; assert.equal(call(resolve,a,m).result,0n); assert.equal(a.mp,paid); assert.equal(count(m),0n);
  });
  test(`${family}: terminal mine preserves other payer pending`, () => {
    const a=actor('A'), b=actor('B'), m=mine(1,a); call(start,a,m); transfer(m,b); call(start,b,m);
    assert.equal(call(resolve,b,m).result,2n); m.flags.add('riches_found_mine_terminal');
    assert.equal(count(m),1n); assert.equal(call(start,b,m).result,4n);
    assert.equal(call(resolve,a,m).result,3n); assert.equal(a.mp,fp(10000)); assert.equal(count(m),0n);
  });
  test(`${family}: native cancel never consumes finish outcome`, () => {
    const a=actor('A'), m=mine(1,a); call(start,a,m); assert.equal(call(`rf_${family}_seal_cancel`,a,m).result,3n);
    assert.equal(call(`rf_${family}_seal_cancel`,a,m).result,0n); assert.equal(a.mp,fp(10000));
  });
}
test('spurious same controller performs zero epoch writes', () => {
  const a=actor('A'), m=mine(1,a); assert.equal(transfer(m,a,a).length,0); assert.equal(epoch(m),0n);
  call('rf_gold_seal_start',a,m); assert.equal(transfer(m,a,a).length,0); assert.equal(count(m),1n);
});
test('near max: pending receipts prevent rollover until final native boundary', () => {
  const a=actor('A'), b=actor('B'), m=mine(1,a); m.vars.set('rf_seal_control_epoch',MAX-S);
  call('rf_gold_seal_start',a,m); transfer(m,b); assert.equal(epoch(m),2147483647n);
  call('rf_demons_seal_start',b,m); assert.equal(count(m),2n); transfer(m,a);
  assert(m.flags.has('rf_seal_epoch_exhausted')); assert.equal(epoch(m),2147483647n);
  assert.equal(call('rf_gold_seal_start',a,m).result,4n);
  assert.equal(call('rf_gold_seal_resolve',a,m).result,3n); assert.equal(count(m),1n);
  assert(m.flags.has('rf_seal_epoch_exhausted')); assert.equal(epoch(m),2147483647n);
  assert.equal(call('rf_demons_seal_resolve',b,m).result,3n); assert.equal(count(m),0n);
  assert(!m.flags.has('rf_seal_epoch_exhausted')); assert.equal(epoch(m),0n);
  assert.equal(call('rf_gold_seal_start',a,m).result,1n);
});
test('max: idle real change resets safely without overflow', () => {
  const a=actor('A'), b=actor('B'), m=mine(1,a); m.vars.set('rf_seal_control_epoch',MAX);
  transfer(m,b); assert.equal(epoch(m),0n); assert.equal(count(m),0n); assert(!m.flags.has('rf_seal_epoch_exhausted'));
});
test('malformed receipt and foreign ROOT reject without cleanup or credit', () => {
  const a=actor('A'), b=actor('B'), m=mine(1,a); call('rf_gold_seal_start',a,m);
  assert.equal(call('rf_gold_seal_resolve',a,m,{root:b}).result,5n); assert.equal(count(m),1n);
  a.vars.delete('rf_seal_support_1_@1'); const paid=a.mp;
  assert.equal(call('rf_gold_seal_resolve',a,m).result,5n); assert.equal(a.mp,paid); assert.equal(count(m),1n);
});
test('same actor two families have independent receipt fields', () => {
  const a=actor('A'), m=mine(1,a); call('rf_gold_seal_start',a,m); call('rf_demons_seal_start',a,m);
  assert.equal(count(m),2n); assert(a.flags.has('rf_seal_pending_1_1')); assert(a.flags.has('rf_seal_pending_2_1'));
  assert.equal(call('rf_gold_seal_resolve',a,m).result,2n); assert.equal(count(m),1n);
  assert(a.flags.has('rf_seal_pending_2_1')); assert.equal(call('rf_demons_seal_cancel',a,m).result,3n);
  assert.equal(count(m),0n); assert.equal(a.mp,fp(9700));
});
test('missing caller storage disappears on helper return in the conservative model', () => {
  const a=actor('A'), m=mine(1,a); temps=new Map();
  invoke('rf_gold_seal_start',{this:a,root:a,from:m},'effect');
  assert.equal(temps.has('rf_seal_result'),false); assert.equal(count(m),1n);
});
test('fractional sequence and counter reject before payment', () => {
  const a=actor('A'), m=mine(1,a); m.vars.set('riches_found_mine_sequence',fp('1.5'));
  assert.equal(call('rf_gold_seal_start',a,m).result,4n); assert.equal(a.mp,fp(10000));
  m.vars.set('riches_found_mine_sequence',fp(1)); m.vars.set('rf_seal_pending_count',fp('0.5'));
  assert.equal(call('rf_gold_seal_start',a,m).result,4n); assert.equal(a.mp,fp(10000));
});
console.log(JSON.stringify({passed:tests.length,cases:tests,productionHashes:hashes,
  model:'typed pointers, 0.00001 fixed point, conservative helper temporary cleanup',
  nativeTimerExecuted:false,nativeFactoryReservationProven:false}));
```
<!-- seal-helper-cases:end -->

Run this production-helper diagnostic from the repository root:

```powershell
$taskContract = Get-Content -Raw -Encoding UTF8 -LiteralPath 'docs/events/029_riches_found/seal_receipt_contract.md'
$taskCode = [regex]::Match($taskContract, '(?s)<!-- seal-helper-cases:start -->\s*```javascript\s*(.*?)\s*```').Groups[1].Value
$taskCode | & 'C:/Program Files/nodejs/node.exe' -
```

