# Event 016 private Cloning production core handoff

Date: 2026-10-07.
Disposition: implemented bounded helper core, with parent-installed direct wiring and constants verified; final parent acceptance and event-wide audits pending.
Parent disposition, 2026-10-08: the bounded core and integration are accepted at source level in `../016_mengele_cloning_deployment_throughput_2026-10-07.md`, following independent integration review and a parent rerun of the final retained driver.
The dated worker findings below retain their original evidence limits; this acceptance does not establish event-wide or live-engine completion.
Acceptance basis: the parent task explicitly accepts the existing-consumer approach from `016_private_clone_existing_production_review_2026-09-08.md`, with baseline 1 preserved, bonus 4 only for owned and controlled facility-bearing states on the existing weekly invocation, and all five private gates required.
Preserved baseline means the intended one-per-controlled-state rate; the preinitialized count also corrects cold nested-helper output loss, and explicit THIS corrects foreign-ROOT attribution.
The older review's alternative `sp_mengele_cloning` admission proposal is not accepted and is not implemented.
The exact source stays `sp_brilliant_scientist_cloning`; the existing native hook and no-DLC paid Prototype settlement stay unchanged.
This implements the private supplemental-production component of `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md:76`; it does not claim the whole Event 016 contract is complete.
The accepted parent plan is `docs/plans/016_brilliant_scientist_plans/016_mengele_cloning_deployment_throughput_2026-10-07.md`, read after the parent's integration follow-up.

## Owned delivery and integration map

Only these four new files are written:

- `common/scripted_effects/016_mengele_clone_production_effects.txt`.
- `common/scripted_effects/016_mengele_clone_production_effects.md`.
- `common/scripted_triggers/016_mengele_clone_production_triggers.txt`.
- This handoff.

All four were absent on disk and absent from `git ls-tree HEAD` before creation.
No Git mutation or HOI4/model/asset operation is performed.
Helper purpose, COUNTRY scopes, inputs, caller-owned outputs, defaults, side effects, cleanup and usage are documented in the matching markdown file.
No neutral shared helper or central routing layer is introduced; the existing dynamic registry already directs owner-specific APIs to their owner documentation.

| Helper | Scope/input | Output and side effects | Direct consumers |
| --- | --- | --- | --- |
| `germany_mengele_baseline_clone_equipment_production` | COUNTRY; parameter-free literal entry, forcibly sets baseline mode | Shared kernel transaction, clears mode | Parent's old producer wrapper |
| `germany_mengele_weekly_clone_equipment_production` | COUNTRY; parameter-free literal entry, forcibly sets weekly mode | Shared kernel transaction, clears mode | Parent's existing weekly hook only |
| `germany_mengele_calculate_clone_equipment_production` | COUNTRY; temporary mode consumed on all paths | Three temporary outputs; no persistent writes, stockpile/refund/flag/refresh effects | Kernel and parent CXT read-only probe |
| `germany_mengele_apply_clone_equipment_production` | COUNTRY; exact supported internal mode | At most one combined positive equipment write, exactly one reserve refresh under existing latch and supported mode including zero facilities | Both literal wrappers |
| `germany_mengele_clone_production_mode_is_supported` | COUNTRY; exact baseline/weekly temporary input | Pure boolean, no writes; absent/invalid mode fails closed | Calculator and kernel entry guards |
| `brilliant_scientist_mengele_cloning_deployment_production_is_active` | COUNTRY; pure strict provider + Prototype + Deployment + access technology + legacy latch | Boolean only | Calculator weekly gate |

The calculator owns `mengele_biowarfare_facility_count` before calling the unchanged legacy controlled-state counter.
The kernel owns all three nested output slots before calculation.
The bonus iterator is `every_owned_state`, limited by `is_controlled_by = PREV` and `biowarfare_facility > constant:brilliant_scientist_value.zero`; it increments once per state, not per level.
The producer uses explicit `producer = THIS`, supported by the installed vanilla precedent and independently confirmed by the parent.
Temporary mode returns `none` through calculator, kernel and wrapper boundaries; baseline entry defeats stale weekly input even after an earlier weekly transaction.

## Constants, cleanup and migration

Parent owns mode constants `constant:germany_mengele_clone_production_mode.none = 0`, `.baseline = 1`, `.weekly = 2`, with schema-first integer registration.
Existing `constant:germany_mengele_cloning_project.clone_equipment_per_facility_per_week = 1` is preserved.
Parent adds `.deployment_bonus_per_owned_facility_per_week = 4` to that existing category.
Existing `constant:brilliant_scientist_value.zero/one` are reused.
No constants are added by this subagent.

Parent replaces only the old producer body with the baseline wrapper call, replaces only its existing weekly call with the weekly wrapper, and retains the old weekly latch filter.
No existing direct call site is edited by this subagent.
Completion, successful construction and inheritance retain their old producer call and baseline-only output.
The shared counter and its coup-pressure and revolt consumers remain unchanged.
The CXT probe preinitializes the three outputs, sets mode weekly, calculates and copies to parent debug vars; it never calls the production kernel.
Parent retains ownership of localisation, accepted spec/plan alignment, final audits, and commits.

There are no new event targets, flags, persistent variables, site ledgers or schedulers.
Mode is unscoped temporary scratch and is set to none on every exit.
Private provider loss suppresses only bonus; old-latch baseline behavior remains intact.
No direct manpower, division, payment, refund, alternate project admission or second production subsystem is introduced.

## References and MCP evidence

Live reference context for `surface = event` reported both offline wiki and installed documentation included, no missing or omitted required source kinds.
Targeted live searches and reads established the sections below; a context result alone is not treated as a detailed read.
References use Windows native paths under the repository or `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.

| Source and lines | Revision | Answering rule |
| --- | --- | --- |
| Installed `documentation\effects_documentation.md:1252-1266` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | COUNTRY stockpile effect; variable amount; producer argument |
| Offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:2253` | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` | Equipment output syntax; read live by parent, parent evidence supplied in follow-up |
| Installed `common\scripted_effects\SIA_scripted_effects.txt:1374-1378` | Local source hash in driver output | Actual stockpile `producer = THIS`; direct source read and parent confirmation |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:435-443` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | Caller-preinitialized temporary storage survives nested helpers; temporaries unscoped |
| Installed `documentation\effects_documentation.md:4076-4095` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | COUNTRY `every_owned_state` and STATE child scope |
| Offline `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md:532` | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` | Owned-state iterator; read live |
| Offline same Scopes file:261-262, 811-818 | Same revision | THIS/PREV targets and iterator parent; exact local sections read |
| Installed `documentation\triggers_documentation.md:5381-5389` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` | STATE `is_controlled_by` explicitly supports PREV; read live |
| Installed `documentation\script_concept_documentation.md:216-222` | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` | Shared script constants and variable access |
| Installed `common\script_constants\documentation.md:1-34` | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` | Required schema-first category structure |

`hoi4.source_lookup` read the legacy counter at `mod:common/scripted_effects/germany_mengele_effects.txt:77-83`, revision `ebfa1f4e0977307e83ef3b194315cd5a47473fe6ac4dddb2c43961f6fe76bebb`, with complete single-definition coverage.
It read the pre-integration producer at :85-102, revision `21aacc473a5c2c9ae6beae7e73de4de44f336ede4311b82f3cd1fa12ae8126c2`.
Producer references were not complete: zero returned references and 20,096 unresolved references are an index coverage limit, not absence of callers.
The direct source review and snapshot comparison identify the ordinary callers independently.

MCP event inspection and script validation results are recorded below when returned.
No weighted helper, AI score, probability modifier, project admission or shared coup-weight formula is edited, so a probability auditor comparison is outside this bounded change.
No focus, GUI layout, technology definition or geography is edited; parent owns those linked surface audits.

## Reproducible actual-source driver

Run from the repository root with Python 3.
This driver is retained inside the handoff to honor the four-file write boundary; it writes no fixture, source, index or report file.
It parses the actual effect/trigger bodies, retains repeated Clausewitz keys, fails on unsupported commands in the exercised closure, discards temporaries first created in returning helpers, and retains modifications to caller-owned slots.
Country flags, native technology, state ownership/control and facility levels are explicit scenarios; the strict private provider predicate and the reserve-refresh native consumer are external stubs, not claimed as engine execution.
All exercised amounts are exact integers bounded below 10,000; Decimal arithmetic prevents accidental float rounding in the model, but does not establish native variable precision or overflow semantics.
The fixture uses accepted parent constants when they are not registered yet and reports that dependency explicitly; registered values must match the accepted tuning.
It compares the four ordinary production callbacks and every shared-counter consumer against pinned Git blobs verified against the parent's normalized snapshot, and reports other observed baseline deltas separately without attributing them to this patch.
The driver needs the repository Git objects and installed vanilla source, but has no temporary-directory dependency.

PowerShell launcher:

```powershell
$handoff = 'docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_clone_production_core_2026-10-07.md'
$text = Get-Content -Raw -LiteralPath $handoff
$driver = [regex]::Match($text, '(?s)<!-- driver:start -->\s*```python\r?\n(.*?)\r?\n```\s*<!-- driver:end -->').Groups[1].Value
if (-not $driver) { throw 'Missing retained driver' }
$driver | python -
```

<!-- driver:start -->
```python
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import hashlib, json, re, subprocess

root = Path.cwd()
baseline_head = '079cd0180122e3ccce97e5d8d39ea2d74b87656b'
baseline_objects = {
    'common/scripted_effects/germany_mengele_effects.txt': ('a330b9eb10e1cbbb8e71be54a640e9348b014a3d', 'cb1ec54b3bc779237293cf44ae5e81040e9c801b2824ae1e69f05eabe56ec2c6'),
    'common/on_actions/germany_mengele_clone_on_actions.txt': ('26ee994ec767e432de5b1025ffa8fc61e8ffca8e', '164a9ff664031e70d7cd986aae33687f121d033901d33083a3c72fda35bbd466'),
}
baseline_blobs = {}
def git_read(*args):
    return subprocess.run(['git', *args], cwd=root, check=True, capture_output=True,
                          creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0)).stdout
for path, (object_id, sha256) in baseline_objects.items():
    assert git_read('rev-parse', baseline_head+':'+path).decode().strip() == object_id
    data = git_read('cat-file', 'blob', object_id)
    assert hashlib.sha256(data).hexdigest() == sha256, 'Pinned baseline bytes mismatch'
    baseline_blobs[path] = data
effect_path = 'common/scripted_effects/016_mengele_clone_production_effects.txt'
trigger_path = 'common/scripted_triggers/016_mengele_clone_production_triggers.txt'
legacy_path = 'common/scripted_effects/germany_mengele_effects.txt'

def parse(text):
    tokens = re.findall(r'"(?:\\.|[^"\\])*"|#[^\n]*|[{}=<>]|[^\s{}=<>]+', text)
    tokens = [t for t in tokens if not t.startswith('#')]
    pos = 0
    def block():
        nonlocal pos
        out = []
        while pos < len(tokens) and tokens[pos] != '}':
            if pos+1 == len(tokens) or tokens[pos+1] not in ('=', '>', '<'):
                out.append((tokens[pos], 'item', None))
                pos += 1
                continue
            key, op = tokens[pos:pos+2]
            assert op in ('=', '>', '<'), (key, op)
            pos += 2
            value = tokens[pos]
            pos += 1
            if value == '{':
                value = block()
                assert tokens[pos] == '}'
                pos += 1
            out.append((key, op, value))
        return out
    result = block()
    assert pos == len(tokens), 'Unparsed trailing tokens'
    return result

def read(path):
    return parse(path.read_text(encoding='utf-8-sig'))

def definitions(path):
    return {k: v for k, op, v in read(path) if isinstance(v, list)}

def before_definitions(path):
    return {k: v for k, op, v in parse(baseline_blobs[path].decode('utf-8-sig')) if isinstance(v, list)}

def flat(nodes):
    for k, op, v in nodes:
        yield k, op, v
        if isinstance(v, list):
            yield from flat(v)

effects = definitions(root/effect_path)
legacy = definitions(root/legacy_path)
before = before_definitions(legacy_path)
effects['germany_mengele_count_biowarfare_facilities'] = legacy['germany_mengele_count_biowarfare_facilities']
effects['germany_mengele_produce_clone_equipment'] = legacy['germany_mengele_produce_clone_equipment']
effects['germany_mengele_complete_cloning_project'] = legacy['germany_mengele_complete_cloning_project']
triggers = definitions(root/trigger_path)
gate = 'brilliant_scientist_mengele_cloning_deployment_production_is_active'
provider = 'brilliant_scientist_mengele_project_stage_provider_is_valid'
latch = 'germany_mengele_cloning_project_completed'
prototype = 'mengele_event016_cloning_prototype_completed'
deployment = 'mengele_event016_cloning_deployment_completed'
mode = 'mengele_clone_production_mode'
outputs = ['mengele_clone_production_base_output', 'mengele_clone_production_deployment_output', 'mengele_clone_equipment_output']
calculator = 'germany_mengele_calculate_clone_equipment_production'
kernel = 'germany_mengele_apply_clone_equipment_production'
baseline = 'germany_mengele_baseline_clone_equipment_production'
weekly = 'germany_mengele_weekly_clone_equipment_production'
constants = {
    'brilliant_scientist_value.zero': 0, 'brilliant_scientist_value.one': 1,
    'germany_mengele_clone_production_mode.none': 0,
    'germany_mengele_clone_production_mode.baseline': 1,
    'germany_mengele_clone_production_mode.weekly': 2,
    'germany_mengele_cloning_project.clone_equipment_per_facility_per_week': 1,
    'germany_mengele_cloning_project.deployment_bonus_per_owned_facility_per_week': 4,
}
actual_constants = {}
for path in (root/'common/script_constants').glob('*.txt'):
    # Only the two owners of this API's tuning need parsing.
    if path.name not in ('germany_mengele_constants.txt', '016_brilliant_scientist_constants.txt'):
        continue
    for category, body in definitions(path).items():
        for key, op, value in body:
            if not isinstance(value, list):
                actual_constants[category+'.'+key] = value
pending = [key for key in constants if key not in actual_constants]
for key, expected in constants.items():
    if key in actual_constants:
        assert Decimal(actual_constants[key]) == expected, (key, actual_constants[key])

class Model:
    def __init__(self, flags=(), valid=True, tech=True, states=(), effect_table=None, missing_count_is_zero=False):
        self.flags, self.valid, self.tech = set(flags), valid, tech
        self.states = list(states)  # owner, controller, facility levels
        self.temp, self.writes, self.refresh, self.trace = {}, [], 0, []
        self.normal = {}  # country-scoped saved debug values are separate
        self.country, self.outer_root = 'GER', 'ENG'
        self.effect_table = effects if effect_table is None else effect_table
        self.missing_count_is_zero, self.missing_reads = missing_count_is_zero, []
    def value(self, token):
        if token.startswith('constant:'):
            return Decimal(constants[token[9:]])
        try:
            return Decimal(token)
        except Exception:
            if self.missing_count_is_zero and token == 'mengele_biowarfare_facility_count' and token not in self.temp:
                self.missing_reads.append(token)
                return Decimal(0)  # cold-before counterexample's explicit assumption
            assert token in self.temp, ('Undefined temporary', token, self.trace)
            return self.temp[token]
    def truth(self, nodes, state=None):
        for k, op, v in nodes:
            if k == provider:
                answer = self.valid
            elif k == 'NOT':
                answer = not any(self.truth([item], state) for item in v)
            elif k == 'OR':
                answer = any(self.truth([item], state) for item in v)
            elif k == 'germany_mengele_cloning_project_revolt_ready':
                answer = False  # scheduling is outside the production fixture
            elif k in triggers:
                answer = self.truth(triggers[k], state)
            elif k == 'has_country_flag':
                answer = v in self.flags
            elif k == 'has_tech':
                assert v == 'clone_infantry_access_tech'
                answer = self.tech
            elif k == 'is_controlled_by':
                assert v == 'PREV' and state is not None
                answer = state[1] == self.country
            elif k == 'biowarfare_facility':
                assert op == '>' and state is not None
                answer = Decimal(state[2]) > self.value(v)
            elif k == 'check_variable':
                if len(v) == 1:
                    name, compare, val = v[0]
                else:
                    d = {a: c for a, b, c in v}
                    name, compare, val = d['var'], d['compare'], d['value']
                if name == mode and name not in self.temp:
                    answer = False  # absent mode cannot equal a supported mode
                else:
                    a, b = self.value(name), self.value(val)
                    answer = {'>': a > b, '<': a < b, 'equals': a == b}[compare]
            else:
                raise AssertionError(('Unsupported trigger', k))
            if not answer:
                return False
        return True
    def call(self, name):
        incoming = set(self.temp)
        self.trace.append(name)
        self.execute(self.effect_table[name])
        for key in set(self.temp) - incoming:
            del self.temp[key]  # conservative helper-return lifetime
    def execute(self, nodes, state=None):
        for k, op, v in nodes:
            if k == 'limit':
                continue
            if k == 'if':
                limit = next(c for a, b, c in v if a == 'limit')
                if self.truth(limit, state):
                    self.execute(v, state)
            elif k in ('every_owned_state', 'every_controlled_state'):
                for item in self.states:
                    if item[0 if k == 'every_owned_state' else 1] != self.country:
                        continue
                    limit = next(c for a, b, c in v if a == 'limit')
                    if self.truth(limit, item):
                        self.execute(v, item)
            elif k in ('set_temp_variable', 'add_to_temp_variable', 'multiply_temp_variable'):
                assert len(v) == 1
                key, _, val = v[0]
                value = self.value(val)
                if k == 'set_temp_variable':
                    self.temp[key] = value
                elif k == 'add_to_temp_variable':
                    self.temp[key] = self.value(key) + value
                else:
                    self.temp[key] = self.value(key) * value
                assert abs(self.temp[key]) < 10000, 'Fixture arithmetic bound'
            elif k == 'round_temp_variable':
                self.temp[v] = self.value(v).quantize(Decimal(1), rounding=ROUND_HALF_UP)
            elif k == 'add_equipment_to_stockpile':
                d = {a: c for a, b, c in v}
                assert d['type'] == 'clone_equipment_1'
                assert d['producer'] in ('THIS', 'ROOT')
                producer = self.country if d['producer'] == 'THIS' else self.outer_root
                self.writes.append((self.country, self.value(d['amount']), producer))
            elif k == 'clone_refresh_reserve_manpower':
                assert v == 'yes'
                self.refresh += 1
            elif k == 'clone_select_mengele_refinement':
                assert v == 'yes'  # external technology grant stub
                self.trace.append(k)
                self.tech = True  # its confirmed first effect grants access
            elif k == 'set_country_flag':
                self.flags.add(v)
            elif k == 'clr_country_flag':
                self.flags.discard(v)
            elif k == 'set_variable':
                key, _, val = v[0]
                assert key.startswith('chaosx_cxt_event016_clone_')
                self.normal[(self.country, key)] = self.value(val)
            elif k in self.effect_table:
                assert v == 'yes', ('Nonliteral helper call', k)
                self.call(k)
            else:
                raise AssertionError(('Unsupported effect', k))

all_flags = {latch, prototype, deployment}
one = [('GER', 'GER', 1)]
mixed = [('GER', 'GER', 1), ('GER', 'GER', 4), ('FRA', 'GER', 3), ('GER', 'FRA', 2), ('GER', 'GER', 0)]

# Pin the cold and preowned-count counterexamples to the actual old source.
old_producer = 'germany_mengele_produce_clone_equipment'
counter = 'germany_mengele_count_biowarfare_facilities'
old_effects = dict(effects)
old_effects.update({old_producer: before[old_producer], counter: before[counter]})
cold_before = Model({latch}, states=mixed, effect_table=old_effects, missing_count_is_zero=True)
cold_before.call(old_producer)
assert cold_before.missing_reads == ['mengele_biowarfare_facility_count']
assert not cold_before.writes and cold_before.refresh == 1 and not cold_before.temp
cold_after = Model({latch}, states=mixed)
cold_after.call(baseline)
assert cold_after.writes == [('GER', Decimal(3), 'GER')] and cold_after.refresh == 1
assert not cold_after.temp
preowned_before = Model({latch}, states=mixed, effect_table=old_effects)
preowned_before.temp['mengele_biowarfare_facility_count'] = Decimal(777)
preowned_before.call(old_producer)
assert preowned_before.writes == [('GER', Decimal(3), 'ENG')]
assert preowned_before.temp['mengele_biowarfare_facility_count'] == 3
preowned_after = Model({latch}, states=mixed)
preowned_after.temp['mengele_biowarfare_facility_count'] = Decimal(777)
preowned_after.call(baseline)
assert preowned_after.writes == [('GER', Decimal(3), 'GER')]
assert preowned_after.temp['mengele_biowarfare_facility_count'] == 3
count_and_provenance = {'controlled_states': 3, 'cold_before_missing_count_reads': cold_before.missing_reads,
    'cold_before_output': 0, 'cold_after_output': 3, 'preowned_before_output': 3,
    'preowned_after_output': 3, 'outer_root': 'ENG', 'invoking_country': 'GER',
    'old_producer_country': 'ENG', 'new_producer_country': 'GER',
    'missing_count_zero_is_fixture_assumption': True}
cases = [
    ('no_latch', {prototype, deployment}, True, True, one, (0, 0, 0)),
    ('legacy_only', {latch}, True, True, one, (1, 0, 1)),
    ('private_prototype_only', {latch, prototype}, True, True, one, (1, 0, 1)),
    ('private_deployment', all_flags, True, True, one, (1, 4, 5)),
    ('invalid_provider', all_flags, False, True, one, (1, 0, 1)),
    ('invalid_tech', all_flags, True, False, one, (1, 0, 1)),
    ('invalid_predecessor', {latch, deployment}, True, True, one, (1, 0, 1)),
    ('captured_controlled', all_flags, True, True, [('FRA', 'GER', 3)], (1, 0, 1)),
    ('owned_lost_control', all_flags, True, True, [('GER', 'FRA', 3)], (0, 0, 0)),
    ('zero_facilities', all_flags, True, True, [], (0, 0, 0)),
    ('multiple_levels', all_flags, True, True, [('GER', 'GER', 7)], (1, 4, 5)),
    ('multiple_states_mixed', all_flags, True, True, mixed, (3, 8, 11)),
]
results = []
for name, flags, valid, tech, states, expected in cases:
    m = Model(flags, valid, tech, states)
    m.temp = {k: Decimal(777) for k in outputs}
    m.temp[mode] = Decimal(2)
    m.call(calculator)
    got = tuple(int(m.temp[k]) for k in outputs)
    assert got == expected, (name, got, expected)
    assert m.temp[mode] == 0 and not m.writes and not m.refresh and not m.normal
    assert m.flags == set(flags)
    assert set(m.temp) == set(outputs+[mode]), 'Local counter storage leaked'
    for wrapper in (baseline, weekly, 'germany_mengele_produce_clone_equipment'):
        p = Model(flags, valid, tech, states)
        p.temp[mode] = Decimal(2)  # stale caller-owned weekly mode
        p.call(wrapper)
        amount = expected[2] if wrapper == weekly else expected[0]
        assert p.writes == ([('GER', Decimal(amount), 'GER')] if amount else [])
        assert p.refresh == int(latch in flags)
        assert p.temp == {mode: Decimal(0)}, 'Kernel output ownership/leak'
    results.append({'scenario': name, 'outputs': got, 'calculator_read_only': True})

p = Model(all_flags, states=one)
p.temp[mode] = Decimal(2)
p.call(weekly)
p.call('germany_mengele_produce_clone_equipment')
p.temp[mode] = Decimal(2)
p.call('germany_mengele_produce_clone_equipment')
assert [w[1] for w in p.writes] == [5, 1, 1]
assert p.refresh == 3 and p.temp[mode] == 0
mode_cases = (None, 0, 1, 2, 99, -1, '1.5', '2.5')
for input_mode in mode_cases:
    p = Model(all_flags, states=one)
    p.temp = dict.fromkeys(outputs, Decimal(777))
    if input_mode is not None:
        p.temp[mode] = Decimal(input_mode)
    p.call(calculator)
    expected = (1, 4, 5) if input_mode == 2 else (1, 0, 1) if input_mode == 1 else (0, 0, 0)
    assert tuple(p.temp[k] for k in outputs) == expected
    assert p.temp.get(mode, 0) == 0
    if input_mode not in (1, 2):
        assert 'germany_mengele_count_biowarfare_facilities' not in p.trace
    q = Model(all_flags, states=one)
    q.temp = dict.fromkeys(outputs, Decimal(777))
    if input_mode is not None:
        q.temp[mode] = Decimal(input_mode)
    q.call(kernel)
    assert tuple(q.temp[k] for k in outputs) == expected
    assert q.writes == ([('GER', Decimal(expected[2]), 'GER')] if expected[2] else [])
    assert q.refresh == int(input_mode in (1, 2))
    assert q.temp.get(mode, 0) == 0
    if input_mode not in (1, 2):
        assert calculator not in q.trace
    for public, amount in ((baseline, 1), (weekly, 5)):
        w = Model(all_flags, states=one)
        if input_mode is not None:
            w.temp[mode] = Decimal(input_mode)
        w.call(public)
        assert w.writes == [('GER', Decimal(amount), 'GER')] and w.refresh == 1
        assert w.temp.get(mode, 0) == 0

# Real existing completion callback under stale weekly input; repeated receipts
# run its unchanged guard and never select the bonus or replay initial output.
p = Model({prototype, deployment}, tech=False, states=one)
p.temp[mode] = Decimal(2)
for _ in range(3):
    p.call('germany_mengele_complete_cloning_project')
assert [w[1] for w in p.writes] == [1] and p.refresh == 1
assert weekly not in p.trace and p.temp[mode] == 0
assert p.tech and p.trace.index('clone_select_mengele_refinement') < p.trace.index('germany_mengele_produce_clone_equipment')
refinement = definitions(root/'common/scripted_effects/clone_system_effects.txt')['clone_select_mengele_refinement']
assert refinement[0] == ('clone_grant_infantry_access', '=', 'yes')

assert legacy['germany_mengele_produce_clone_equipment'] == [(baseline, '=', 'yes')]
def child(nodes, name):
    return next(v for k, op, v in nodes if k == name)
hook_path = 'common/on_actions/germany_mengele_clone_on_actions.txt'
current_hook = read(root/hook_path)
before_hook = parse(baseline_blobs[hook_path].decode('utf-8-sig'))
def replace_producer(nodes):
    return [(weekly if k == 'germany_mengele_produce_clone_equipment' else k, op, replace_producer(v) if isinstance(v, list) else v) for k, op, v in nodes]
assert current_hook == replace_producer(before_hook), 'Weekly change exceeded literal call replacement'
hook_effect = child(child(child(current_hook, 'on_actions'), 'on_weekly'), 'effect')

cxt_path = 'common/scripted_effects/016_mengele_native_ownership_cxt_effects.txt'
probe = definitions(root/cxt_path)['chaosx_cxt_event016_probe_native_ownership']
probe_body = child(probe, 'if')
assert child(probe_body, 'limit') == [('tag', '=', 'CXT'), ('has_country_flag', '=', 'chaosx_test_country_initialized')]
start = next(i for i, (k, op, v) in enumerate(probe_body) if k == 'set_temp_variable' and v == [(outputs[0], '=', 'constant:brilliant_scientist_value.zero')])
probe_rows = probe_body[start:]
assert len(probe_rows) == 8 and probe_rows[4] == (calculator, '=', 'yes')
debug_keys = ['chaosx_cxt_event016_clone_base_weekly_output', 'chaosx_cxt_event016_clone_deployment_weekly_bonus', 'chaosx_cxt_event016_clone_total_weekly_output']
assert probe_rows[-3:] == [('set_variable', '=', [(debug, '=', output)]) for debug, output in zip(debug_keys, outputs)]
for name, flags, valid, tech, states, expected in cases:
    h = Model(flags, valid, tech, states)
    h.execute(hook_effect)
    assert h.writes == ([('GER', Decimal(expected[2]), 'GER')] if expected[2] else [])
    assert h.refresh == int(latch in flags)
    q = Model(flags, valid, tech, [('CXT' if o == 'GER' else o, 'CXT' if c == 'GER' else c, level) for o, c, level in states])
    q.country = 'CXT'
    q.execute(probe_rows)
    assert tuple(q.normal[('CXT', key)] for key in debug_keys) == expected
    assert not q.writes and not q.refresh and q.flags == set(flags)
    assert q.temp[mode] == 0

assert triggers[gate] == [
    (provider, '=', 'yes'), ('has_country_flag', '=', prototype),
    ('has_country_flag', '=', deployment), ('has_tech', '=', 'clone_infantry_access_tech'),
    ('has_country_flag', '=', latch),
]
ordinary_callers = [k for k in before if k != 'germany_mengele_produce_clone_equipment' and any(a == 'germany_mengele_produce_clone_equipment' for a, b, c in flat(before[k]))]
assert len(ordinary_callers) == 4, ordinary_callers
preserved = sorted(set(ordinary_callers + ['germany_mengele_count_biowarfare_facilities'] + [k for k in before if k != 'germany_mengele_produce_clone_equipment' and any(a == 'germany_mengele_count_biowarfare_facilities' for a, b, c in flat(before[k]))]))
assert all(before[k] == legacy[k] for k in preserved), 'Unexpected ordinary callback/counter mutation'
other_snapshot_deltas = [k for k in before if k not in preserved and k != 'germany_mengele_produce_clone_equipment' and before[k] != legacy.get(k)]
for path in ('common/scripted_effects/016_mengele_project_stage_effects.txt', 'common/scripted_effects/016_mengele_project_bridge_effects.txt'):
    nodes = read(root/path)
    assert not any(k in (weekly, kernel, calculator) for k, op, v in flat(nodes)), 'Private stage invokes bonus/kernel'
calc_commands = {k for k, op, v in flat(effects[calculator])}
assert not calc_commands.intersection({'add_equipment_to_stockpile', 'clone_refresh_reserve_manpower', 'set_variable', 'set_country_flag', 'clr_country_flag', 'add_manpower', 'create_unit'})
assert sum(k == 'add_equipment_to_stockpile' for k, op, v in flat(effects[kernel])) == 1
assert sum(k == 'clone_refresh_reserve_manpower' for k, op, v in flat(effects[kernel])) == 1
for name in (baseline, weekly):
    assert effects[name][1] == (kernel, '=', 'yes')
    assert effects[name][-1][2] == [(mode, '=', 'constant:germany_mengele_clone_production_mode.none')]

hashes = {p: hashlib.sha256((root/p).read_bytes()).hexdigest() for p in (effect_path, trigger_path, legacy_path, hook_path, cxt_path, 'common/script_constants/germany_mengele_constants.txt')}
hashes['pinned_before_germany_effects'] = hashlib.sha256(baseline_blobs[legacy_path]).hexdigest()
hashes['pinned_before_weekly_hook'] = hashlib.sha256(baseline_blobs[hook_path]).hexdigest()
vanilla = Path('C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_effects/SIA_scripted_effects.txt')
hashes['vanilla_SIA_scripted_effects'] = hashlib.sha256(vanilla.read_bytes()).hexdigest()
print(json.dumps({'status': 'PASS', 'scenarios': results, 'wrapper_runs': len(cases)*3+3, 'direct_calculator_and_kernel_mode_cases': len(mode_cases)*2, 'public_wrapper_mode_override_cases': len(mode_cases)*2, 'real_weekly_hook_cases': len(cases), 'real_cxt_slice_cases': len(cases), 'repeated_real_completion_calls': 3, 'refinement_access_precedes_baseline_output': True, 'cold_and_preowned_provenance_cases': 4, 'count_and_provenance': count_and_provenance, 'baseline_head': baseline_head, 'baseline_objects': baseline_objects, 'preserved_legacy_definitions': preserved, 'ordinary_callers': ordinary_callers, 'other_snapshot_deltas': other_snapshot_deltas, 'pending_parent_constants': pending, 'source_hashes': hashes, 'scope_limits': ['Source subset model; strict provider, refinement grant and refresh consumer are stubs', 'Cold-before missing numeric count is explicitly modeled as zero, not observed in game', 'Old construction and inheritance callbacks are compared as complete parsed bodies, not executed', 'Only the actual production observation tail of the CXT probe is executed', 'No native runtime/cadence/engine reserve verification']}, indent=2))
```
<!-- driver:end -->

## Validation results and limitations

Driver results and final MCP summaries follow below.
The retained driver is meaningful source-model evidence, not live engine proof.
There are no gameplay simplifications in the bounded core.
Parent integration dependencies and unresolved engine/MCP coverage must remain explicit in the final Event 016 report.

### Actual integration verification

The final driver run passed using the parent's installed constants, with no pending constant keys.
The live `germany_mengele_produce_clone_equipment` body is exactly the baseline-wrapper call after comments are parsed away.
The live weekly hook differs from the parent's snapshot only by replacing the old producer token with the weekly-wrapper token; the old latch filter and all surrounding structure are unchanged.
The real CXT production observation tail preinitializes all three result slots, uses exact `mengele_clone_production_mode`, calls the calculator once and copies the results into `chaosx_cxt_event016_clone_base_weekly_output`, `chaosx_cxt_event016_clone_deployment_weekly_bonus` and `chaosx_cxt_event016_clone_total_weekly_output`.
Its CXT/initialized-country enclosing guard is checked as source, and the actual eight-node production tail is executed by the fixture separately from unrelated native-ownership observations.

The source model passed 12 calculator scenarios, 39 public-wrapper/real-producer runs, 16 direct calculator/kernel mode cases, 16 public-wrapper mode-override cases, 12 actual weekly-hook cases and 12 actual CXT observation-tail cases.
Three calls to the real guarded completion callback yielded exactly one baseline equipment batch and one refresh, without invoking the weekly wrapper.
Weekly followed by the real old producer yielded 5 then 1 equipment for one qualifying owned state; reseeding stale weekly mode before another real old-producer call still yielded 1.
Foreign outer ROOT was ENG while invoking country was GER, and every modeled production write attributed equipment to GER via the parsed explicit THIS token.
The fixture proves that kernel preinitialization retains all nested results across conservative call-frame cleanup.
Calculator runs preserve country flags, make no saved-state/debug writes and perform no stockpile grant or refresh.
Zero facilities under the old latch still refresh exactly once; absent old latch never produces or refreshes.

| Scenario | Base / bonus / total |
| --- | --- |
| no_latch | 0 / 0 / 0 |
| legacy_only | 1 / 0 / 1 |
| private_prototype_only | 1 / 0 / 1 |
| private_deployment | 1 / 4 / 5 |
| invalid_provider | 1 / 0 / 1 |
| invalid_tech | 1 / 0 / 1 |
| invalid_predecessor | 1 / 0 / 1 |
| captured_controlled | 1 / 0 / 1 |
| owned_lost_control | 0 / 0 / 0 |
| zero_facilities | 0 / 0 / 0 |
| multiple_levels | 1 / 4 / 5 |
| multiple_states_mixed | 3 / 8 / 11 |

The exact parsed bodies of seven snapshot definitions were preserved: the legacy counter, coup-pressure calculator, laboratory-unit counter consumer, completion callback, both construction callbacks and coup/inheritance callback.
The four ordinary producer callers remain `germany_mengele_complete_cloning_project`, `germany_mengele_add_requested_biowarfare_facility`, `mengele_clone_army_add_biowarfare_facility` and `germany_mengele_start_coup_internal`.
The shared snapshot also differs in unrelated `mengele_clone_world_order_launch`, where the current body contains `acid_rain_interrupt_for_world_end`; this subagent did not write that existing file or review that separate change.
It is recorded as an observed shared-tree delta rather than covered by this throughput validation.
Private stage and bridge sources contain no direct weekly-wrapper, calculator or kernel invocation; complete private-stage replay is not emulated by this fixture and remains under the parent's stage audits.

### Revision-bound results

Final actual-source test identities:

| Source | SHA-256 |
| --- | --- |
| `common/scripted_effects/016_mengele_clone_production_effects.txt` | `005e4c7b2af575808548d20e30c445ee1691b98e5fcb680c19397d83cf7c859c` |
| `common/scripted_triggers/016_mengele_clone_production_triggers.txt` | `39c69f1bc36280644db11e6beb688590292adbdd495e5da7514705abc2c7a80b` |
| `common/scripted_effects/germany_mengele_effects.txt` | `3dd326a79dd57d4f5ae53049c6df72746a9975c8e162044849f41aeef5c6472b` |
| `common/on_actions/germany_mengele_clone_on_actions.txt` | `4c1fb6a6c972520e9ee5d7a5f33e7737dd4518d2806ec54cec854fc1ed71a076` |
| `common/scripted_effects/016_mengele_native_ownership_cxt_effects.txt` | `71286e23f7d2bfecff04f1bae1a93bf3a1b156a0a6eb82de6ed1981cfc94710a` |
| `common/script_constants/germany_mengele_constants.txt` | `1c7b3f5e70190223ae4334c49f5535524f70bc23a8e13a5fc910b8070fcf5393` |
| `parent_snapshot_germany_effects` | `783659c4fc394a007570210acd2d18fe7faad39249faa07f71b2832bb52536ae` |
| `pinned_before_germany_effects` | `cb1ec54b3bc779237293cf44ae5e81040e9c801b2824ae1e69f05eabe56ec2c6` |
| `pinned_before_weekly_hook` | `164a9ff664031e70d7cd986aae33687f121d033901d33083a3c72fda35bbd466` |
| `vanilla_SIA_scripted_effects` | `ac1e86a0ffe5e46f7083318c584993667eaafb3cd1585e15db71fbd51fa276af` |

The supplied snapshot was verified against commit `079cd0180122e3ccce97e5d8d39ea2d74b87656b`, the exact revision recorded in its `head.txt`.
The executable driver pins Git blob identities and SHA-256 hashes, checks their membership at that immutable commit and reads their raw bytes with `git cat-file blob`.
It never reads the temporary snapshot directory, writes/restores a source or mutates Git.
The historical snapshot hash above retains supplied CRLF bytes; Git baseline hashes retain the raw LF blobs, which were verified to match the complete supplied source after UTF-8/BOM and line-ending normalization.

### MCP coverage and unsupported analysis

The read-only Event016 trace returned `EVENT_INSPECTED_PARTIAL`, revision `9d19f7c75482bcc9146c7d3d4cb070da37cd7c88921d63f7530586b227b4e023`, graph hash `1deeb45d7c47dfc9fd023417126b6649927a7ccd772bf3d9338bcb95972e9a85`.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9a63b8af3a25e3455e4b0993a14b822db8e8e139665d0598011a8cebfa4bd57/37a523336412f1fdc2ca38fdbbd6a72384cf86dea03d9f0a0b2f43f41f5e0ffe/event-trace-9d19f7c75482.json`, SHA-256 `e9a63b8af3a25e3455e4b0993a14b822db8e8e139665d0598011a8cebfa4bd57`, 1,081,326 bytes.
Analysis mode is focused, with depth 1, 12 nodes and 12 edges requested, `expandHelpers = false`, indexed helper count zero, skipped-source count zero and helper/lifecycle projection explicitly deferred.
The inline inventory retained only 64 of 403 source paths; the linked report was retained but not fully fetched in this bounded core pass.
This is partial event-surface evidence and does not prove helper lifecycle coverage or live cadence.

Both new whole files were checked with live `hoi4.script_validate`; file roots do not declare scopes, so the file checks returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, unknown root scopes 4/1 and native argument blocks unchecked 24/0 for effects/triggers.
The initial five helper/predicate bodies were then extracted and checked individually under explicit COUNTRY scope before the supported-mode follow-up below.
Those results also returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, `parametersChecked = false`; the performed checks were syntax, command kind and declared scope, against installed documentation revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
No unsupported native kind/scope finding appeared in the returned findings, but unresolved helpers, the mod building trigger and unchecked parameter blocks prevent a complete validation claim.

| Explicit COUNTRY body | Checked commands | Unresolved findings | Unchecked argument blocks | Omitted findings |
| --- | --- | --- | --- | --- |
| `germany_mengele_baseline_clone_equipment_production` | 2 | 3 | 2 | 0 |
| `germany_mengele_weekly_clone_equipment_production` | 2 | 3 | 2 | 0 |
| `germany_mengele_calculate_clone_equipment_production` | 21 | 17 | 14 | 16 |
| `germany_mengele_apply_clone_equipment_production` | 9 | 8 | 6 | 0 |
| `brilliant_scientist_mengele_cloning_deployment_production_is_active` | 4 | 1 | 0 | 0 |

The native-only snippet route does not resolve scripted-helper calls, and treats `biowarfare_facility` as undocumented rather than a known mod building trigger.
The full-file route recognizes helper declarations but cannot infer COUNTRY root scope.
The calculator response omitted 16 findings at the maximum live result limit; no claim is made about those omitted findings.
The existing counter and source model verify the state-building count pattern; existing `common/scripted_triggers/biological_stockpile_safety_triggers.txt:110` also uses a constant-backed positive `biowarfare_facility` check.
Parameter semantics remain source/reference evidence, not proof from this validator.
Live reads additionally covered installed effects:2327-2333, 5012-5018 and 7820-7827 for temporary add/multiply/set, and installed triggers:2110-2135 for explicit and shortened variable comparisons, under their revisions in the reference table above.
Installed effects:6476-6485 was read locally for temporary rounding, and installed script concepts:184-215 was read for the distinction between math-expression precision and normal variable arithmetic.

Event render/compare and full helper/lifecycle closure were not run in this subagent pass because the parent owns the changed scheduler integration and final event audits; the focused trace artifact is not a recovered before-event graph suitable for canonical comparison.
Those remain parent integration evidence, not a substitution by the source fixture.
No required reference or script-validation route was unavailable after correcting live-schema argument rejections.
The initial event-selector and context-question schema rejections were corrected; they are not service blockers.
No native-task, job or helper-expansion route was used without negotiated server-health/version evidence.

### Completed, pending and simplifications

Completed: all four owned files, parameter-free public wrappers, one shared deterministic calculation/production path, strict pure five-gate predicate, conservative nested output ownership, mode consumption, parent-installed direct call-site checks, central tuning checks and reproducible evidence.
No gameplay simplifications, alternative native source, additional paid cycle, new scheduler, world iteration, equipment/technology/project ID, unit, model/audio/asset, persistent registry or direct manpower grant was introduced.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, including the existing helper-output lifetime and loop-isolation reference; no skill was changed.
Parent review remains pending, including localisation/spec alignment and final audits.
The core has no unresolved design input or missing constant dependency at the final source test.
Full provider execution, full stage receipts, native equipment identity, actual weekly cadence, reserve recomputation and live consumer behavior remain unverified by this source subset model.
HOI4 execution was deliberately not performed under the task prohibition.
No Git commit or index mutation was performed under the parent ownership contract.

### Parent review follow-up: supported mode and legacy access order

Disposition: implemented within the same four owned files, under the parent's explicit review request.
Added pure COUNTRY predicate `germany_mengele_clone_production_mode_is_supported`, accepting exact baseline or weekly mode only.
The calculator checks it before facility counting and the kernel checks it before entering calculation/grant/refresh.
The kernel checks mode before the calculator consumes it, so valid transactions retain the zero-facility refresh behavior.
Output initialization and unconditional mode cleanup remain outside the guard; invalid calls leave the three result slots zero and do not invoke the shared counter or reserve consumer.
Literal public wrappers are unchanged.

The retained driver passes absent mode, none 0, baseline 1, weekly 2, unknown 99, negative -1 and fractional 1.5/2.5.
It executes all eight modes against both internal helpers and both public wrappers: 16 direct-helper cases and 16 wrapper-override cases.
Invalid internal calls perform no stockpile write or refresh; invalid calculator calls do not invoke the shared counter, and invalid kernel calls do not invoke the calculator.
The unchanged wrappers replace every malformed/absent input with their supported literal mode.
Conservative temporary lifetime preserves caller-owned output storage and cleanup, including absent input storage.
The previously recorded twelve gameplay scenarios, actual weekly hook, CXT observation tail and callback snapshots still pass.
The final hashes above refer to these guarded scripts.

Read-only source confirms `clone_select_mengele_refinement` begins with `clone_grant_infantry_access = yes` at `common/scripted_effects/clone_system_effects.txt:95-96`.
The access helper grants `clone_infantry_access_tech`, and the unchanged legacy completion callback invokes refinement before `germany_mengele_produce_clone_equipment`.
The retained driver asserts the actual refinement's first child and executes repeated completion starting without operational technology, with the external access grant modeled from that confirmed entry.
No refinement, grant, native project or paid callback source was edited.

The parent's `GetMengeleCloningDeploymentWeeklyBonus` getter reads `constant:germany_mengele_cloning_project.deployment_bonus_per_owned_facility_per_week`.
Its existing deployment tooltip describes the additional weekly equipment for each owned-and-controlled facility; those parent-owned presentation files were read and left untouched.
No new MCP graph calls were made for this guard.
Explicit COUNTRY validation was rerun only for the modified calculator, kernel and supported-mode predicate.
All returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, with the same native-argument/helper limits recorded above.
The calculator reported 21 checked commands, 18 unresolved findings, 14 unchecked argument blocks and 17 omitted findings; the kernel reported 9 checked commands, 9 unresolved findings, 6 unchecked blocks and no omitted findings.
The supported-mode predicate reported 3 checked commands, 2 unchecked comparison argument blocks and no omitted findings.
No unsupported native kind/scope appeared in returned findings; these partial results do not replace the actual-source scenario checks or establish engine runtime validation.
The prior partial event/lifecycle evidence and source-model limits remain unchanged; final integration validation belongs to the parent.

### Reproducibility follow-up: pinned baseline and cold-count counterexample

Disposition: implemented documentation/fixture update only under the parent's explicit pre-commit request.
Only this handoff and `common/scripted_effects/016_mengele_clone_production_effects.md` changed in this follow-up; both gameplay script hashes above remain unchanged.
No temporary file, new source, Git mutation, graph call or gameplay change was introduced.

The supplied snapshot's `head.txt` is `079cd0180122e3ccce97e5d8d39ea2d74b87656b`.
Its complete Germany effects source and weekly hook match the following immutable blobs after decoding UTF-8 with optional BOM and normalizing CRLF/CR to LF; no comments, whitespace, effects or other source content were removed for this comparison.

| Before source | Git blob identity | Raw Git SHA-256 | Supplied snapshot SHA-256 | Normalized equality |
| --- | --- | --- | --- | --- |
| Germany effects | `a330b9eb10e1cbbb8e71be54a640e9348b014a3d` | `cb1ec54b3bc779237293cf44ae5e81040e9c801b2824ae1e69f05eabe56ec2c6` | `783659c4fc394a007570210acd2d18fe7faad39249faa07f71b2832bb52536ae` | Exact |
| Existing weekly hook | `26ee994ec767e432de5b1025ffa8fc61e8ffca8e` | `164a9ff664031e70d7cd986aae33687f121d033901d33083a3c72fda35bbd466` | `83f2b2664723f0dd0911ad060b1244c2a06d0c9adf59bff66718c89f94884cdf` | Exact |

The driver needs these retained repository objects rather than a branch's moving HEAD or the temporary snapshot path.
It verifies both exact object identities and their raw SHA-256 bytes on every run; missing objects fail rather than silently using current source.
No checkout, temporary extraction or external network is involved.
The driver was rerun successfully after removing every temporary-path read from its executable code.

Four additional actual-source executions distinguish rate, lifetime and provenance:

| Case | Caller-owned count slot | Controlled facility states C | Physical output | Invoking country / outer ROOT | Producer attribution |
| --- | --- | --- | --- | --- | --- |
| Pinned old producer, cold | Absent | 3 | 0 under the explicit missing-count-zero fixture assumption | GER / ENG | No write |
| Current baseline wrapper, cold | Absent | 3 | 3 | GER / ENG | GER |
| Pinned old producer, preowned count | Seeded 777, replaced with 3 | 3 | 3 | GER / ENG | ENG through ROOT |
| Current baseline wrapper, preowned count | Seeded 777, replaced with 3 | 3 | 3 | GER / ENG | GER through THIS |

The pinned old counter creates its count only inside its helper frame on a cold invocation; conservative helper-return cleanup discards it before the old producer reads it.
That exact missing read is recorded as `mengele_biowarfare_facility_count`, and the counterexample explicitly models the missing numeric value as zero.
The current calculator owns the count before the nested helper, and the kernel owns its outputs, so a cold baseline correctly produces C without inherited scratch.
When count storage is already caller-owned, both old and current source preserve the intended baseline amount C, isolating the attribution correction from throughput tuning.
Thus baseline intended-rate preservation, cold-count correction and invoking-country provenance are three distinct source claims rather than a blanket old/new behavioral-equivalence claim.
The observed cold case remains conservative source-model evidence, not an in-game observation of how that execution path treats missing numeric variables.

The final driver passes its prior 12 gameplay scenarios, 39 wrapper/real-producer runs, 16 direct mode cases, 16 wrapper override cases, 12 weekly-hook cases, 12 CXT observation-tail cases and three completion calls, plus these four count/provenance executions.
The foreign `mengele_clone_world_order_launch` difference remains reported in `other_snapshot_deltas` and outside this worker's ownership and validation.
No unrelated source was normalized, restored or changed to make the baseline comparison pass.
