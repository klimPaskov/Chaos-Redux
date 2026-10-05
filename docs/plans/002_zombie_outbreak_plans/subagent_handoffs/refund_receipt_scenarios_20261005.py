"""Bounded actual-source receipt scenarios, not an HOI4 engine emulator.

Executes receipt APIs, their credit/count/eligibility dependencies, and the
financial projection of each owner's selection/refund/completion blocks.
Native political-power charge is a fixture debit before complete_effect.
Country eligibility primitives and owner reward conditions are fixture inputs.
Nonfinancial owner gameplay, timers, UI, and achievements are not certified.
"""
from pathlib import Path
import ast
import operator
import re
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'AGENTS.md').exists())
# Reuse only the existing parser function without importing unrelated fixtures.
tree = ast.parse((ROOT / '.tools/test_event021_evolution_log.py').read_text(encoding='utf-8-sig'))
function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'parse')
namespace = {'TOKEN': re.compile(r'#[^\n]*|"[^"\n]*"|[{}=]|[^\s{}=]+')}
exec(compile(ast.Module(body=[function], type_ignores=[]), '<repo-Clausewitz-parser>', 'exec'), namespace)
parse = namespace['parse']


def load(path):
    return dict(parse((ROOT / path).read_text(encoding='utf-8-sig')))


EFFECTS = load('common/scripted_effects/026_black_friday_effects.txt')
TRIGGERS = load('common/scripted_triggers/026_black_friday_triggers.txt')
CONSTANTS = load('common/script_constants/026_black_friday_constants.txt')
CONSTANTS.update(load('common/script_constants/chaosx_universal_cost_constants.txt'))
DECISIONS = {k: dict(v) for category in load('common/decisions/002_zombie_outbreak_decisions.txt').values()
             for k, v in category if isinstance(v, list)}
CREDIT = 'black_friday_credit_political_power_purchase_with_receipt'
WITHDRAW = 'black_friday_withdraw_political_power_purchase_with_receipt'
OUT_FLAG = 'black_friday_political_power_receipt_credited'
OUT_SEQ = 'black_friday_political_power_receipt_sale_sequence'
SEQ = 'global.black_friday_sale_sequence'
INDEX = 'black_friday_achievement_indexed_sale_sequence'


def contains(nodes, token):
    return any(k == token or (isinstance(v, list) and contains(v, token)) for k, v in nodes)


OWNERS = {k: v for k, v in DECISIONS.items() if contains(v['complete_effect'], CREDIT)}


class Runtime:
    def __init__(self):
        self.values = {SEQ: 1, INDEX: 1}
        self.temps = {}
        self.flags = set()
        self.global_flags = {'black_friday_active', 'black_friday_natural_activation'}
        self.ai = self.debug = self.special = False
        self.fit = True
        self.pp = 63
        self.native_refunds = 0

    def name(self, token):
        if '@var:' in token:
            key, target = token.split('@var:')
            return key + str(int(self.value(target)))
        return token

    def value(self, token):
        if token.startswith('constant:'):
            category, key = token[9:].split('.')
            return float(dict(CONSTANTS[category])[key])
        try:
            return float(token)
        except ValueError:
            return self.temps.get(self.name(token), self.values.get(self.name(token), 0))

    def check(self, nodes):
        def one(k, v):
            if k == 'AND': return self.check(v)
            if k == 'OR': return any(one(a, b) for a, b in v)
            if k == 'NOT': return not self.check(v)
            if k == 'has_variable': return self.name(v) in self.values or self.name(v) in self.temps
            if k == 'has_country_flag': return v in self.flags
            if k == 'has_global_flag': return v in self.global_flags
            if k == 'exists': return v == 'yes'
            if k == 'is_ai': return self.ai == (v == 'yes')
            if k == 'is_debug': return self.debug == (v == 'yes')
            if k == 'is_special_chaos_country': return self.special == (v == 'yes')
            if k == 'is_major': return False
            if k == 'anti_zombie_league_investment_can_fit': return self.fit
            if k in ('is_in_array',):
                d = dict(v)
                return self.value(d['value']) in self.values.get(d['array'], [])
            if k == 'check_variable':
                d = dict(v)
                if 'var' in d:
                    left, right, compare = d['var'], d['value'], d.get('compare', 'greater_than_or_equals')
                else:
                    keys = [a for a, b in v]
                    if len(keys) == 1: left, right, compare = keys[0], v[0][1], 'equals'
                    else: left, compare, right = keys
                comparisons = {'equals': operator.eq, 'not_equals': operator.ne,
                               'greater_than': operator.gt, 'less_than': operator.lt,
                               'greater_than_or_equals': operator.ge, 'less_than_or_equals': operator.le,
                               '>': operator.gt, '<': operator.lt}
                return comparisons[compare](self.value(left), self.value(right))
            if k in TRIGGERS: return self.check(TRIGGERS[k])
            raise AssertionError(('unsupported predicate', k, v))
        return all(one(k, v) for k, v in nodes)

    def run(self, nodes):
        branch = None
        for k, v in nodes:
            if k in ('if', 'else_if'):
                eligible = k == 'if' or not branch
                hit = eligible and self.check(dict(v)['limit'])
                if hit: self.run([(a, b) for a, b in v if a != 'limit'])
                branch = hit if k == 'if' else branch or hit
            elif k == 'else':
                if not branch: self.run(v)
            elif k == 'hidden_effect': self.run(v)
            elif k in ('set_temp_variable', 'set_variable', 'add_to_variable', 'subtract_from_variable'):
                d = dict(v)
                name, token = (d['var'], d['value']) if 'var' in d else v[0]
                store = self.temps if k == 'set_temp_variable' else self.values
                name = self.name(name)
                amount = self.value(token)
                store[name] = amount if k.startswith('set_') else store.get(name, 0) + (amount if k == 'add_to_variable' else -amount)
            elif k == 'clear_variable': self.values.pop(self.name(v), None)
            elif k == 'set_country_flag': self.flags.add(v)
            elif k == 'clr_country_flag': self.flags.discard(v)
            elif k == 'add_political_power':
                self.pp += self.value(v)
                self.native_refunds += self.value(v) != 0
            elif k in ('add_to_array', 'remove_from_array'):
                d = dict(v)
                array = self.values.setdefault(d['array'], [])
                value = self.value(d['value'])
                if k == 'add_to_array': array.append(value)
                else: array.remove(value)
            elif k in EFFECTS: self.call(k)
            else: raise AssertionError(('unsupported effect', k, v))

    def call(self, key):
        # Conservative helper lifetime: only caller-initialized temps survive.
        previous = set(self.temps)
        self.run(EFFECTS[key])
        self.temps = {k: v for k, v in self.temps.items() if k in previous}

    def family(self):
        self.temps['black_friday_purchase_family_id'] = self.value('constant:universal_cost_family.political_power')
        return self.name('black_friday_achievement_family_committed_count_@var:black_friday_purchase_family_id')

    def set_count(self, count):
        self.values[self.family()] = count
        self.values[self.name('black_friday_achievement_family_generation_@var:black_friday_purchase_family_id')] = self.values[SEQ]

    def project(self, nodes):
        # Retain actual financial/receipt statements and their control blocks.
        result = []
        for k, v in nodes:
            if k in (CREDIT, WITHDRAW, 'add_political_power'):
                result.append((k, v))
            elif k in ('if', 'else_if', 'else', 'hidden_effect'):
                body = self.project([(a, b) for a, b in v if a != 'limit'])
                if body:
                    result.append((k, ([('limit', dict(v)['limit'])] if k in ('if', 'else_if') else []) + body))
            elif k in ('set_temp_variable', 'set_variable', 'clear_variable', 'set_country_flag', 'clr_country_flag'):
                names = str(v)
                if any(t in names for t in ('_paid_pp', '_sale_credit', '_sale_sequence', OUT_FLAG, OUT_SEQ)):
                    result.append((k, v))
        return result

    def owner(self, owner, action):
        nodes = self.project(OWNERS[owner][action])
        for k, v in walk(nodes):
            if k == 'set_variable':
                name, token = v[0]
                if name.endswith('_paid_pp'): self.values[token] = 37
        self.temps = {}
        self.run(nodes)


def walk(nodes):
    for k, v in nodes:
        yield k, v
        if isinstance(v, list): yield from walk(v)


class Receipts(unittest.TestCase):
    def test_all_owners_same_sale_cancel_once(self):
        self.assertEqual(len(OWNERS), 25)
        for owner in OWNERS:
            with self.subTest(owner=owner):
                rt = Runtime(); rt.set_count(3)
                rt.owner(owner, 'complete_effect')
                self.assertEqual(rt.values[rt.family()], 4)
                self.assertIn(owner + '_sale_credit', rt.flags)
                rt.owner(owner, 'cancel_effect')
                self.assertEqual(rt.values[rt.family()], 3)
                self.assertEqual(rt.pp, 100)
                self.assertNotIn(owner + '_sale_credit', rt.flags)
                self.assertNotIn(owner + '_sale_sequence', rt.values)
                rt.owner(owner, 'cancel_effect')
                self.assertEqual((rt.values[rt.family()], rt.pp, rt.native_refunds), (3, 100, 1))

    def test_before_sale_and_older_sale_refunds_preserve_new_credit(self):
        for owner in OWNERS:
            for credited in (False, True):
                with self.subTest(owner=owner, credited=credited):
                    rt = Runtime()
                    if not credited: rt.global_flags.clear()
                    rt.owner(owner, 'complete_effect')
                    rt.values.update({SEQ: 2, INDEX: 2}); rt.set_count(4)
                    rt.owner(owner, 'cancel_effect')
                    self.assertEqual((rt.values[rt.family()], rt.pp), (4, 100))

    def test_excluded_purchases_never_capture_credit(self):
        for owner in OWNERS:
            for exclusion in ('ai', 'debug', 'manual', 'forced', 'awarded', 'unprepared'):
                with self.subTest(owner=owner, exclusion=exclusion):
                    rt = Runtime(); rt.set_count(3)
                    if exclusion in ('ai', 'debug'): setattr(rt, exclusion, True)
                    if exclusion in ('manual', 'forced'): rt.global_flags.add('black_friday_' + ('manual' if exclusion == 'manual' else 'force') + '_disqualified')
                    if exclusion == 'awarded': rt.flags.add('black_friday_achievement_awarded')
                    if exclusion == 'unprepared': rt.values.pop(INDEX)
                    rt.owner(owner, 'complete_effect')
                    self.assertNotIn(owner + '_sale_credit', rt.flags)
                    rt.owner(owner, 'cancel_effect')
                    self.assertEqual((rt.values[rt.family()], rt.pp), (3, 100))

    def test_completion_clears_receipt_and_retains_credit(self):
        for owner in OWNERS:
            with self.subTest(owner=owner):
                rt = Runtime(); rt.set_count(3)
                rt.owner(owner, 'complete_effect'); rt.owner(owner, 'remove_effect')
                self.assertEqual((rt.values[rt.family()], rt.pp), (4, 63))
                self.assertNotIn(owner + '_sale_credit', rt.flags)
                self.assertNotIn(owner + '_sale_sequence', rt.values)

    def test_generation_reset_expiry_and_investment_rejection(self):
        owner = 'invest_in_league_research'
        rt = Runtime(); rt.set_count(7)
        rt.values[self.name_generation(rt)] = 0
        rt.owner(owner, 'complete_effect')
        self.assertEqual(rt.values[rt.family()], 1)
        self.assertIn(owner + '_sale_credit', rt.flags)
        rt.global_flags.discard('black_friday_active'); rt.fit = False
        rt.owner(owner, 'remove_effect')
        self.assertEqual((rt.values[rt.family()], rt.pp, rt.native_refunds), (0, 100, 1))
        self.assertNotIn(owner + '_sale_credit', rt.flags)
        rt.owner(owner, 'remove_effect')
        self.assertEqual((rt.values[rt.family()], rt.pp, rt.native_refunds), (0, 100, 1))

    @staticmethod
    def name_generation(rt):
        return rt.name('black_friday_achievement_family_generation_@var:black_friday_purchase_family_id')


if __name__ == '__main__':
    unittest.main(verbosity=2)
