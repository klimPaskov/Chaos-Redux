"""Production-source regression for native national policy laws.

Usage: python .tools/test_national_policy_laws.py
Inputs: committed native law, helper, trigger, constants and Event 003 source.
Outputs: .tmp/national_policy_panels/laws_test_results.json.
Models both native replacement callback orders and conservative temporary helper frames.
Subsystem consequences and tested panel lifecycle callbacks are recorded at their approved seams.
Actual panel lifecycle bodies execute in test_national_policy_panel_updates.py.
No native engine timing, AI selection frequency or live game validation is claimed.
"""
from pathlib import Path
import re, importlib.util, sys, json, hashlib
ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / '.tmp' / 'national_policy_panels'
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location('policy_parser', ROOT / '.tools/test_event035_center_projects.py')
P = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = P
spec.loader.exec_module(P)

def parse(path):
    s = (ROOT / path).read_text(encoding='utf-8-sig')
    s = re.sub('add_ideas\\s*=\\s*\\{([^{}=]+)\\}', lambda m: ' '.join(('add_ideas = ' + v for v in m[1].split())), s)
    ts = P.lex(P.uncomment(s))
    (rows, end) = P.parse_nodes(ts, 0, path)
    assert end == len(ts)
    return rows

def first(rows, key, default=None):
    return P.first(rows, key, default)

def read_named(path, name):
    source = (ROOT / path).read_text(encoding='utf-8-sig')
    match = re.search('(?m)^' + re.escape(name) + '\\s*=\\s*\\{', source)
    assert match, name
    tokens = P.lex(P.uncomment(source[match.end():]))
    (body, end) = P.parse_nodes(tokens, 0, name)
    assert tokens[end].text == '}'
    return body
E = {n.key: n.value for n in parse('common/scripted_effects/national_policy_effects.txt')}
T = {n.key: n.value for n in parse('common/scripted_triggers/national_policy_triggers.txt')}
for name in ('migration_decision_set_policy',):
    E[name] = read_named('common/scripted_effects/migration_decision_owner_effects.txt', name)
for name in ('holy_realm_open_refuge_reception', 'holy_realm_register_refuge_reception', 'holy_realm_close_refuge_reception'):
    E[name] = read_named('common/scripted_effects/003_holy_realm_effects.txt', name)
T['migration_decision_reception_policy_request_is_valid'] = read_named('common/scripted_triggers/migration_decision_owner_triggers.txt', 'migration_decision_reception_policy_request_is_valid')
C = {}
for path in ['common/script_constants/national_policy_constants.txt', 'common/script_constants/migration_core_constants.txt', 'common/script_constants/humanitarian_runtime_constants.txt', 'common/script_constants/civilian_transfer_constants.txt']:
    for group in parse(path):
        for n in group.value:
            if not isinstance(n.value, list):
                try:
                    C['constant:' + group.key + '.' + n.key] = float(n.value)
                except ValueError:
                    pass
I = {}
S = {}
for slot in next((n.value for n in parse('common/ideas/national_policy_laws.txt') if n.key == 'ideas')):
    for n in slot.value:
        if isinstance(n.value, list):
            I[n.key] = n.value
            S[n.key] = slot.key

class R:

    def __init__(self, tag='FRA', eligible=True, overlap=True, special=None, holy=False):
        self.tag = tag
        self.eligible = eligible
        self.special = not eligible if special is None else special
        self.holy = holy
        self.overlap = overlap
        self.ideas = set()
        self.flags = set()
        self.v = {}
        self.frames = [{'migration_decision_policy_result': 0, 'migration_departure_policy_request': 0, 'migration_reception_policy_request': 0}]
        self.facts = {}
        self.calls = []
        self.pp = 1000

    @property
    def tmp(self):
        return self.frames[0]

    def scratch(self):
        return {k: v for frame in self.frames for (k, v) in frame.items()}

    def temp(self, key, value):
        for frame in reversed(self.frames[:-1]):
            if key in frame:
                frame[key] = value
                return
        self.frames[-1][key] = value

    def num(self, v):
        if v in C:
            return C[v]
        try:
            return float(v)
        except ValueError:
            for frame in reversed(self.frames):
                if v in frame:
                    return frame[v]
            return self.v.get(v, 0)

    def cond(self, rows):
        for n in rows:
            (k, v) = (n.key, n.value)
            if k in ('AND', 'hidden_trigger'):
                ok = self.cond(v)
            elif k == 'OR':
                ok = any((self.cond([x]) for x in v))
            elif k == 'NOT':
                ok = not self.cond(v)
            elif k == 'always':
                ok = v == 'yes'
            elif k == 'exists':
                ok = v == 'yes'
            elif k == 'tag':
                ok = self.tag == v
            elif k == 'uses_normal_civilian_systems':
                ok = self.eligible == (v == 'yes')
            elif k == 'is_special_chaos_country':
                ok = self.special == (v == 'yes')
            elif k == 'is_holy_realm_country':
                ok = self.holy == (v == 'yes')
            elif k == 'cbrn_action_actor_is_valid':
                ok = True
            elif k == 'has_idea':
                ok = v in self.ideas
            elif k == 'has_country_flag':
                ok = v in self.flags
            elif k == 'has_variable':
                ok = v in self.v or any((v in frame for frame in self.frames))
            elif k == 'check_variable':
                if len(v) == 1:
                    a = v[0]
                    x = self.num(a.key)
                    y = self.num(a.value)
                    op = a.op
                else:
                    x = self.num(first(v, 'var'))
                    y = self.num(first(v, 'value'))
                    op = {'equals': '=', 'greater_than': '>', 'less_than': '<'}[first(v, 'compare', 'equals')]
                ok = {'=': x == y, '<': x < y, '>': x > y}[op]
            elif k == 'has_political_power':
                ok = self.pp > self.num(v)
            elif k == 'has_tech':
                ok = v in self.facts.get('techs', set())
            elif k == 'num_of_nukes':
                ok = self.facts.get('nukes', 0) > self.num(v)
            elif k in T:
                ok = self.cond(T[k]) == (v == 'yes')
            elif k in self.facts:
                ok = bool(self.facts[k]) == (v == 'yes')
            else:
                raise AssertionError('Unmodeled trigger ' + k)
            if not ok:
                return False
        return True

    def run(self, name):
        self.frames.append({})
        try:
            self.effect(E[name])
        finally:
            self.frames.pop()

    def effect(self, rows):
        branch = None
        for n in rows:
            (k, v) = (n.key, n.value)
            if k in ('if', 'else_if', 'else'):
                allowed = k == 'if' or branch is False
                take = allowed and (k == 'else' or self.cond(first(v, 'limit', [])))
                if k == 'if':
                    branch = False
                if take:
                    self.effect([x for x in v if x.key != 'limit'])
                    branch = True
                continue
            branch = None
            if k in ('set_variable', 'set_temp_variable'):
                assert len(v) == 1
                a = v[0]
                if k == 'set_temp_variable':
                    self.temp(a.key, self.num(a.value))
                else:
                    self.v[a.key] = self.num(a.value)
            elif k == 'clear_variable':
                self.v.pop(v, None)
            elif k == 'set_country_flag':
                self.flags.add(first(v, 'flag') if isinstance(v, list) else v)
            elif k == 'clr_country_flag':
                self.flags.discard(v)
            elif k == 'remove_ideas':
                self.ideas.discard(v)
            elif k == 'add_ideas':
                self.add(v)
            elif k in E:
                assert v == 'yes', ('Unsupported named-block helper call', k)
                self.run(k)
            elif k in ('national_policy_initialize_cost_modifiers', 'migration_national_policy_changed', 'national_policy_on_warfare_law_changed', 'chaosx_test_country_register_extension_effect', 'national_policy_panel_reconcile_observer_identity', 'national_policy_panel_retire_country'):
                self.calls.append((k, self.scratch()))
            else:
                raise AssertionError('Unmodeled effect ' + k)

    def add(self, idea):
        old = {x for x in self.ideas if S[x] == S[idea]}
        if not self.overlap:
            self.ideas -= old
        self.ideas.add(idea)
        self.frames.append({})
        try:
            self.effect(first(I[idea], 'on_add', []))
        finally:
            self.frames.pop()
        self.ideas -= old - {idea}

    def score(self, idea):
        rows = first(I[idea], 'ai_will_do')
        score = self.num(first(rows, 'factor'))
        for n in rows:
            if n.key == 'modifier' and self.cond([x for x in n.value if x.key != 'factor']):
                score *= self.num(first(n.value, 'factor'))
        return score
assert '$' not in (ROOT / 'common/scripted_effects/national_policy_effects.txt').read_text()
assert float(re.search('(?m)^@national_policy_ai_hold_days = ([0-9.]+)$', (ROOT / 'common/scripted_effects/national_policy_effects.txt').read_text())[1]) == C['constant:national_policy_ai.hold_days']
checks = []
for family in ('reception', 'departure', 'chemical', 'biological', 'nuclear'):
    r = R()
    r.run('national_policy_initialize_country')
    before = r.v.copy()
    r.run('national_policy_publish_' + family)
    assert r.v == before
    r.tmp['national_policy_requested_value'] = 99
    r.run('national_policy_publish_' + family)
    assert r.v == before
checks.append('Bare publisher calls reject missing/unsupported input envelopes with conservative temporary call-frame cleanup')

def record(name):
    checks.append(name)

def default_facts(r):
    for k in ('migration_pending_reception_issue_is_valid', 'migration_reception_capacity_is_valid', 'migration_decision_reception_capacity_exhausted_is_valid', 'has_active_biowarfare_outbreak', 'cbrn_country_has_operational_readiness', 'bio_strategic_raid_ai_has_safe_domestic_program', 'bio_strategic_raid_country_has_any_agent_project', 'bio_battlefield_country_has_any_agent_project', 'has_war', 'cbrn_ai_route_allows_first_use', 'cbrn_ai_route_allows_unrestricted_use', 'national_policy_ai_has_chemical_retaliation_right', 'national_policy_ai_has_biological_retaliation_right', 'national_policy_ai_has_nuclear_retaliation_right'):
        r.facts[k] = False
    return r
assert len(I) == 19 and len(set(S.values())) == 5
for date in ('1936.1.1.12', '1939.8.14.12'):
    for tag in ('FRA', 'GER', 'SOV', 'ITA', 'JAP', 'MAN', 'MEN', 'ETH', 'CXT'):
        r = R(tag)
        r.run('national_policy_apply_starting_profile')
        assert len(r.ideas) == 5 and len({S[x] for x in r.ideas}) == 5
        assert r.v['migration_reception_policy'] == 2
        assert r.v['migration_departure_policy'] == (2 if tag in ('GER', 'SOV') else 1)
        assert r.v['cbrn_chemical_use_policy'] == (5 if tag in ('JAP', 'ITA') else 2)
        assert r.v['cbrn_biological_use_policy'] == (5 if tag == 'JAP' else 2)
        assert r.v['nuclear_use_policy'] == (5 if tag == 'JAP' else 0)
        assert not any((x[0].endswith('changed') for x in r.calls))
        snapshot = (r.ideas.copy(), r.v.copy())
        r.run('national_policy_apply_starting_profile')
        assert snapshot == (r.ideas, r.v)
record('18 bookmark/tag profiles, five slots each, silent idempotence')
for overlap in (False, True):
    for old in I:
        for new in I:
            if old == new or S[old] != S[new]:
                continue
            r = R(overlap=overlap)
            r.run('national_policy_initialize_country')
            r.add(old)
            r.calls = []
            before = dict(r.v)
            r.add(new)
            family = new.split('_')[2]
            var = {'reception': 'migration_reception_policy', 'departure': 'migration_departure_policy', 'chemical': 'cbrn_chemical_use_policy', 'biological': 'cbrn_biological_use_policy', 'nuclear': 'nuclear_use_policy'}[family]
            expected = first(first(I[new], 'on_add'), 'set_temp_variable')[0].value
            assert r.v[var] == C[expected] and old not in r.ideas and (new in r.ideas)
            callbacks = [x for x in r.calls if x[0].endswith('changed')]
            assert len(callbacks) == 1
            assert callbacks[0][1]['national_policy_previous_value'] == before[var]
            assert callbacks[0][1]['national_policy_new_value'] == r.v[var]
record('132 ordered law transitions, both replacement callback orders, correct old/new publication')
r = R('MAN')
r.run('national_policy_apply_starting_profile')
r.add('national_policy_nuclear_unrestricted')
r.run('national_policy_initialize_country')
assert 'national_policy_nuclear_unrestricted' in r.ideas
r.run('national_policy_initialize_released_country')
assert 'national_policy_nuclear_none' in r.ideas
record('Civil-war reconciliation preserves inherited law, independent release resets to profile')
r = R(eligible=False)
r.ideas = {'national_policy_reception_closed', 'national_policy_departure_permit'}
r.v = {'migration_reception_policy': 5, 'migration_departure_policy': 2, 'migration_border_policy': 5}
r.run('national_policy_initialize_country')
assert len(r.ideas) == 3 and 'migration_border_policy' not in r.v and ('migration_reception_policy' not in r.v)
record('Special/nonhuman civilian exclusion removes laws and derived policy without registration')
for overlap in (False, True):
    r = R('HLY', special=True, holy=True, overlap=overlap)
    r.run('national_policy_initialize_country')
    assert len(r.ideas) == 5
    r.add('national_policy_reception_humanitarian')
    r.v['migration_reception_policy'] = 5
    r.run('national_policy_reconcile_country')
    assert r.v['migration_reception_policy'] == 1 and 'national_policy_reception_humanitarian' in r.ideas
    for (name, option, value) in [('holy_realm_close_refuge_reception', 'closed', 5), ('holy_realm_open_refuge_reception', 'humanitarian', 1), ('holy_realm_register_refuge_reception', 'controlled', 2)]:
        r.run(name)
        assert r.v['migration_reception_policy'] == value and 'national_policy_reception_' + option in r.ideas
        assert r.tmp['migration_decision_policy_result'] == 1 and r.tmp['migration_departure_policy_request'] == r.tmp['migration_reception_policy_request'] == 0
        assert 'national_policy_departure_free' in r.ideas
    r.eligible = False
    r.run('national_policy_reconcile_country')
    assert 'migration_reception_policy' not in r.v
record('Holy Realm native publication/reconciliation and all three actual Event003 refuge request helpers, both callback orders')
for (special, holy) in ((True, False), (False, False)):
    r = R('HLY' if holy else 'FRA', special=special, holy=holy)
    r.run('national_policy_initialize_country')
    old = r.ideas.copy()
    r.tmp.update({'migration_departure_policy_request': 3, 'migration_reception_policy_request': 1})
    r.run('migration_decision_set_policy')
    assert r.ideas == old and r.tmp['migration_decision_policy_result'] == 0
r = R(special=True)
r.tmp.update({'migration_departure_policy_request': 1, 'migration_reception_policy_request': 1})
r.run('migration_decision_set_policy')
assert not r.ideas and r.tmp['migration_decision_policy_result'] == 0
for (dep, idea) in [(1, 'free'), (2, 'permit'), (5, 'prohibited')]:
    for (rec, option) in [(1, 'humanitarian'), (2, 'controlled'), (3, 'transit'), (4, 'quarantine'), (5, 'closed'), (6, 'violent'), (7, 'forced_return')]:
        r = R()
        r.tmp.update({'migration_departure_policy_request': dep, 'migration_reception_policy_request': rec})
        r.run('migration_decision_set_policy')
        assert 'national_policy_departure_' + idea in r.ideas and 'national_policy_reception_' + option in r.ideas and (r.tmp['migration_decision_policy_result'] == 1)
record('Authorized external request mapping covers all 21 valid dimension pairs, rejects unsupported and special-country requests atomically, resets request inputs, no payment command')
r = R('CXT')
r.flags.add('chaosx_test_country_initialized')
r.run('national_policy_cxt_enable_unrestricted_warfare')
snap = (r.ideas.copy(), r.v.copy())
r.run('national_policy_cxt_extension_apply')
r.run('national_policy_cxt_enable_unrestricted_warfare')
assert snap == (r.ideas, r.v)
assert r.v['nuclear_use_policy'] == 5
record('CXT explicit fixture preserves unrestricted warfare and idempotent extension')
scenarios = {}
r = default_facts(R())
r.run('national_policy_initialize_country')
scenarios['quiet_default'] = {i: r.score(i) for i in I}
assert all((v == 0 or i in r.ideas for (i, v) in scenarios['quiet_default'].items()))
r.facts.update({'migration_pending_reception_issue_is_valid': True, 'migration_reception_capacity_is_valid': True})
r.v.update({'migration_reception_load': 0, 'migration_reception_capacity': 100})
assert r.score('national_policy_reception_humanitarian') == 64
scenarios['offer_with_capacity'] = {i: r.score(i) for i in I if S[i] == 'refugee_reception'}
r.facts['migration_decision_reception_capacity_exhausted_is_valid'] = True
r.v['migration_reception_load'] = 101
r.facts['migration_reception_capacity_is_valid'] = True
assert r.score('national_policy_reception_humanitarian') == 0 and r.score('national_policy_reception_transit') == 64
r.add('national_policy_departure_permit')
r.flags.discard('national_policy_ai_hold_departure')
assert r.score('national_policy_departure_free') == 64 and r.score('national_policy_departure_prohibited') == 0
record('AI quiet preservation, offer/capacity response, overloaded-host departure relief')
r = default_facts(R())
r.run('national_policy_initialize_country')
r.facts.update({'techs': {'nukes'}, 'nukes': 1, 'national_policy_ai_has_nuclear_retaliation_right': True})
assert r.score('national_policy_nuclear_retaliation') == 64 and r.score('national_policy_nuclear_unrestricted') == 0
r.facts['national_policy_ai_has_nuclear_retaliation_right'] = False
assert r.score('national_policy_nuclear_retaliation') == 0
r.facts.update({'has_war': True, 'cbrn_ai_route_allows_unrestricted_use': True})
assert r.score('national_policy_nuclear_unrestricted') == 64
r.pp = 149
assert r.score('national_policy_nuclear_unrestricted') == 0
record('AI nuclear exact-family response, no evidence/capability escalation, explicit route, PP reserve')
r = default_facts(R('JAP'))
r.run('national_policy_apply_starting_profile')
assert r.score('national_policy_chemical_unrestricted') == 160 and r.score('national_policy_nuclear_unrestricted') == 160
record("Japan's explicit unrestricted profile retains a bounded current-law preference")
result = {'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT / 'common/ideas/national_policy_laws.txt', ROOT / 'common/scripted_effects/national_policy_effects.txt', ROOT / 'common/scripted_triggers/national_policy_triggers.txt', ROOT / 'common/script_constants/national_policy_constants.txt', ROOT / 'common/scripted_effects/migration_decision_owner_effects.txt', ROOT / 'common/scripted_effects/003_holy_realm_effects.txt']}, 'checks': checks, 'scenario_scores': scenarios, 'limitations': ['Subsystem callbacks recorded only', 'Native law replacement orders modeled, not executed by engine', 'Native AI selection frequency and timed-flag expiry not modeled', 'Receipt validity remains warfare owner validation']}
(ROOT / '.tmp/national_policy_panels/laws_test_results.json').write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
