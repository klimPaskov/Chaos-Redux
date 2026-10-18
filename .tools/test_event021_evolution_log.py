"""Execute Event 021's actor selector on bounded, declared source fixtures.

This model covers only selector predicates, array traversal, and conservative
temporary-helper lifetime. It does not emulate HOI4 or certify live log output.
"""
from dataclasses import dataclass, field
from pathlib import Path
import operator
import os
import re
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r'#[^\n]*|"[^"\n]*"|[{}=]|[^\s{}=]+')


def parse(text):
    tokens = [m.group() for m in TOKEN.finditer(text) if not m.group().startswith('#')]
    cursor = 0

    def body():
        nonlocal cursor
        result = []
        while cursor < len(tokens) and tokens[cursor] != '}':
            if tokens[cursor] == '{':
                cursor += 1
                nested = body()
                if cursor >= len(tokens) or tokens[cursor] != '}':
                    raise AssertionError('Unclosed anonymous schema block')
                cursor += 1
                result.append(('_anonymous', nested))
                continue
            key = tokens[cursor]
            cursor += 1
            if cursor >= len(tokens) or tokens[cursor] != '=':
                result.append((key, None))
                continue
            cursor += 1
            value = tokens[cursor]
            cursor += 1
            if value == '{':
                value = body()
                if cursor >= len(tokens) or tokens[cursor] != '}':
                    raise AssertionError('Unclosed source block')
                cursor += 1
            result.append((key, value))
        return result

    return body()


def load(path):
    revision = os.environ.get('CHAOSX_EVENT021_TEST_REVISION')
    if revision:
        source = subprocess.run(['git', 'show', revision + ':' + path], cwd=ROOT,
                                check=True, capture_output=True, encoding='utf-8').stdout
        return parse(source)
    return parse((ROOT / path).read_text(encoding='utf-8-sig'))


CORE = dict(load('common/scripted_effects/021_random_civil_war_effects.txt'))
PARENT = dict(load('common/scripted_effects/021_random_civil_war_parent_effects.txt'))
SELECTOR = dict(load('common/scripted_effects/021_random_civil_war_evolution_log_effects.txt'))
TRIGGERS = dict(load('common/scripted_triggers/021_random_civil_war_triggers.txt'))
SPONSOR = dict(load('common/scripted_triggers/021_random_civil_war_sponsor_receipt_triggers.txt'))
CONSTANTS = dict(load('common/script_constants/021_random_civil_war_constants.txt'))
CONSTANTS.update(dict(load('common/script_constants/chaos_meter_constants.txt')))
LOGGER = dict(load('common/scripted_effects/chaosx_events_log_effects.txt'))['record_events_log_evolution_entry']


@dataclass
class Country:
    id: int
    exists: bool = True
    nonhuman: bool = False
    values: dict = field(default_factory=dict)
    flags: set = field(default_factory=set)


class Runtime:
    def __init__(self):
        self.actor = Country(2, values={'random_civil_war_front_id': 11, 'random_civil_war_crisis_id': 7},
                             flags={'random_civil_war_active', 'random_civil_war_front_registered', 'random_civil_war_theater_registered'})
        self.host = Country(1, values={'random_civil_war_crisis_id': 7},
                            flags={'random_civil_war_active', 'random_civil_war_front_registered', 'random_civil_war_theater_registered'})
        self.actor.values['random_civil_war_crisis_host_scope'] = self.host
        self.sender = Country(99)
        self.globals = {
            'random_civil_war_front_ids': [11], 'random_civil_war_front_actors': [self.actor],
            'random_civil_war_front_hosts': [self.host], 'random_civil_war_front_crisis_ids': [7],
            'random_civil_war_front_statuses': [1], 'random_civil_war_active_theaters': [self.actor, self.host],
            'random_civil_war_current_stage': 0, 'random_civil_war_current_chaos_tier': 1,
        }
        self.temporary = {'events_log_evolution_has_actor': 0}
        self.targets = {'events_log_evolution_actor': self.sender}
        self.previous = None

    def value(self, token, actor):
        if token.startswith('constant:'):
            group, name = token[9:].split('.', 1)
            return int(dict(CONSTANTS[group])[name])
        if token.startswith('global.'):
            name = token[7:]
            if '^' in name:
                name, index = name.split('^', 1)
                rows = self.globals.get(name, [])
                return len(rows) if index == 'num' else rows[int(self.value(index, actor))]
            return self.globals.get(name, 0)
        if token == 'THIS.id':
            return actor.id
        if token == 'ROOT.id':
            return self.sender.id
        if token.startswith('PREV.'):
            name = token[5:]
            return self.previous.id if name == 'id' else self.previous.values.get(name, 0)
        if token in self.temporary:
            return self.temporary[token]
        try:
            return int(token)
        except ValueError:
            return actor.values.get(token, 0)

    def condition(self, nodes, actor):
        comparisons = {'equals': operator.eq, 'greater_than': operator.gt}
        for key, data in nodes:
            if key == 'check_variable':
                values = dict(data)
                result = comparisons[values['compare']](self.value(values['var'], actor), self.value(values['value'], actor))
            elif key == 'exists':
                result = actor.exists == (data == 'yes')
            elif key == 'has_country_flag':
                result = data in actor.flags
            elif key == 'has_variable':
                result = data in actor.values or data in self.temporary
            elif key == 'has_event_target':
                result = data in self.targets
            elif key == 'is_in_array':
                values = dict(data)
                result = (actor if values['value'] == 'THIS' else self.value(values['value'], actor)) in self.value(values['array'], actor)
            elif key == 'NOT':
                result = not any(self.condition([node], actor) for node in data)
            elif key == 'is_actual_nonhuman_country':
                # Declared fixture classification, not an emulation of the shared classifier.
                result = actor.nonhuman
            elif key == 'random_civil_war_is_normal_human_country':
                result = self.condition(TRIGGERS[key], actor)
            elif key.startswith('var:'):
                target = self.value(key[4:], actor)
                saved = self.previous
                self.previous = actor
                try:
                    result = self.condition(data, target)
                finally:
                    self.previous = saved
            else:
                raise AssertionError(f'Unsupported selector predicate {key}')
            if not result:
                return False
        return True

    def run(self, nodes, actor):
        for key, data in nodes:
            if key == 'if':
                if self.condition(dict(data)['limit'], actor):
                    self.run([(k, v) for k, v in data if k != 'limit'], actor)
            elif key == 'set_temp_variable':
                name, token = data[0]
                self.temporary[name] = self.value(token, actor)
            elif key == 'for_each_loop':
                values = dict(data)
                effects = [(k, v) for k, v in data if k not in ('array', 'value', 'index', 'break')]
                for index, row in enumerate(list(self.value(values['array'], actor))):
                    self.temporary[values['value']] = row
                    self.temporary[values['index']] = index
                    self.run(effects, actor)
                    if self.temporary.get(values['break'], 0):
                        break
            elif key.startswith('var:'):
                target = self.value(key[4:], actor)
                self.run(data, target)
            elif key == 'save_event_target_as':
                self.targets[data] = actor
            elif key == 'event021_prepare_evolution_log_context':
                self.call(CORE[key], actor)
            else:
                raise AssertionError(f'Unsupported selector effect {key}')

    def call(self, nodes, actor):
        caller_storage = set(self.temporary)
        self.run(nodes, actor)
        # Conservative documented boundary, not a flat all-temporaries-survive model.
        self.temporary = {k: v for k, v in self.temporary.items() if k in caller_storage}

    def select(self):
        self.call(SELECTOR['event021_select_verified_evolution_log_actor'], self.sender)
        return self.temporary['events_log_evolution_has_actor']


class EvolutionLogTests(unittest.TestCase):
    def test_verified_participant_instead_of_scheduler(self):
        rt = Runtime()
        self.assertEqual(rt.select(), 1)
        self.assertIs(rt.targets['events_log_evolution_actor'], rt.actor)
        self.assertEqual(set(rt.temporary), {'events_log_evolution_has_actor'})

    def test_invalid_receipts_cannot_reuse_stale_target(self):
        changes = {
            'dead actor': lambda r: setattr(r.actor, 'exists', False),
            'dead host': lambda r: setattr(r.host, 'exists', False),
            'nonhuman actor': lambda r: setattr(r.actor, 'nonhuman', True),
            'nonhuman host': lambda r: setattr(r.host, 'nonhuman', True),
            'wrong front': lambda r: r.actor.values.update(random_civil_war_front_id=12),
            'wrong actor crisis': lambda r: r.actor.values.update(random_civil_war_crisis_id=8),
            'wrong host crisis': lambda r: r.host.values.update(random_civil_war_crisis_id=8),
            'missing ID': lambda r: r.actor.values.pop('random_civil_war_front_id'),
            'inactive row': lambda r: r.globals['random_civil_war_front_statuses'].__setitem__(0, 2),
            'inactive actor': lambda r: r.actor.flags.remove('random_civil_war_active'),
            'missing registration': lambda r: r.actor.flags.remove('random_civil_war_theater_registered'),
            'missing actor front registration': lambda r: r.actor.flags.remove('random_civil_war_front_registered'),
            'missing host front registration': lambda r: r.host.flags.remove('random_civil_war_front_registered'),
            'missing host theater registration': lambda r: r.host.flags.remove('random_civil_war_theater_registered'),
            'missing host membership': lambda r: r.globals['random_civil_war_active_theaters'].remove(r.host),
            'missing canonical pointer': lambda r: r.actor.values.pop('random_civil_war_crisis_host_scope'),
            'missing membership': lambda r: r.globals['random_civil_war_active_theaters'].clear(),
            'misaligned arrays': lambda r: r.globals['random_civil_war_front_hosts'].clear(),
            'zero crisis': lambda r: r.globals['random_civil_war_front_crisis_ids'].__setitem__(0, 0),
        }
        for name, change in changes.items():
            with self.subTest(name=name):
                rt = Runtime()
                change(rt)
                self.assertEqual(rt.select(), 0)
                self.assertIs(rt.targets['events_log_evolution_actor'], rt.sender)

    def test_same_crisis_participant_cannot_replace_canonical_host(self):
        rt = Runtime()
        substitute = Country(3, values={'random_civil_war_crisis_id': 7}, flags=set(rt.host.flags))
        rt.globals['random_civil_war_front_hosts'][0] = substitute
        rt.globals['random_civil_war_active_theaters'].append(substitute)
        self.assertEqual(rt.select(), 0)

    def test_proved_host_pointer_rebinding_agrees_with_registry(self):
        rt = Runtime()
        successor = Country(3, values={'random_civil_war_crisis_id': 7}, flags=set(rt.host.flags))
        rt.globals['random_civil_war_front_hosts'][0] = successor
        rt.globals['random_civil_war_active_theaters'].append(successor)
        rt.actor.values['random_civil_war_crisis_host_scope'] = successor
        self.assertEqual(rt.select(), 1)

    def test_human_event006_package_is_not_immune(self):
        rt = Runtime()
        rt.actor.flags.update({'random_civil_war_event6_origin_recorded', 'independence_wave_event021_adapter_setup_proven'})
        self.assertEqual(rt.select(), 1)

    def test_empty_prefire_pool_is_no_actor(self):
        rt = Runtime()
        for name in list(rt.globals):
            if isinstance(rt.globals[name], list):
                rt.globals[name] = []
        self.assertEqual(rt.select(), 0)

    def test_shared_logger_ignores_stale_actor_target(self):
        actor_branch = next(data for key, data in LOGGER if key == 'if' and
                            ('has_event_target', 'events_log_evolution_actor') in dict(data).get('limit', []))
        rt = Runtime()
        rt.globals['random_civil_war_front_statuses'][0] = 2
        self.assertEqual(rt.select(), 0)
        self.assertFalse(rt.condition(dict(actor_branch)['limit'], rt.sender))
        rt.globals['random_civil_war_front_statuses'][0] = 1
        self.assertEqual(rt.select(), 1)
        self.assertTrue(rt.condition(dict(actor_branch)['limit'], rt.sender))

    def test_all_callbacks_initialize_indicator_before_selector_and_record(self):
        selector = ('event021_select_verified_evolution_log_actor', 'yes')
        recorder = ('record_events_log_evolution_entry', 'yes')
        seed = ('set_temp_variable', [('events_log_evolution_has_actor', 'constant:random_civil_war_value.zero')])

        def find(nodes):
            for key, data in nodes:
                if isinstance(data, list):
                    if selector in data:
                        yield data
                    yield from find(data)

        for suffix in ('i', 'ii'):
            with self.subTest(stage=suffix):
                branches = list(find(PARENT['event021_parent_apply_evolution_' + suffix]))
                self.assertEqual(len(branches), 1)
                branch = branches[0]
                at = branch.index(selector)
                self.assertEqual(branch[at - 1], seed)
                self.assertEqual(branch[at + 1], recorder)

    def test_evolution_iii_keeps_only_its_hidden_lifecycle_state(self):
        # 0645862e1a: Evolution III is a hidden lifecycle state with no public log row,
        # so its wrapper must neither select an actor nor record an Event Log entry.
        def calls(nodes):
            for key, data in nodes:
                yield key
                if isinstance(data, list):
                    yield from calls(data)

        used = set(calls(PARENT['event021_parent_apply_evolution_iii']))
        self.assertNotIn('event021_select_verified_evolution_log_actor', used)
        self.assertNotIn('record_events_log_evolution_entry', used)
        self.assertIn('event021_apply_evolution_iii', used)

    def test_last_valid_row_beyond_numeric_loop_ceiling(self):
        rt = Runtime()
        for name in ('ids', 'actors', 'hosts', 'crisis_ids', 'statuses'):
            key = 'random_civil_war_front_' + name
            rt.globals[key] = rt.globals[key] * 1002
        rt.globals['random_civil_war_front_statuses'][:1001] = [2] * 1001
        self.assertEqual(rt.select(), 1)

    def test_each_callback_preserves_its_event_identity_across_helper_return(self):
        for stage in range(1, 4):
            with self.subTest(stage=stage):
                rt = Runtime()
                callback = PARENT['event021_parent_apply_evolution_' + 'i' * stage]
                prefix = []
                for key, data in callback:
                    if key == 'if':
                        break
                    if key.startswith('event021_parent_apply_evolution_'):
                        continue  # Earlier-stage delivery is outside this metadata-only model.
                    prefix.append((key, data))
                rt.run(prefix, rt.sender)
                self.assertEqual(rt.temporary['events_log_evolution_event_id'], 21)
                self.assertEqual(rt.temporary['events_log_evolution_type'], 21)
                self.assertEqual(rt.temporary['events_log_evolution_stage'], stage)


class SponsorReceiptTests(unittest.TestCase):
    def receipt(self):
        rt = Runtime()
        rt.host.flags.update({'random_civil_war_sponsor_commitment_received', 'random_civil_war_sponsor_evidence_active'})
        rt.host.values.update(random_civil_war_sponsor_scope=rt.actor, random_civil_war_sponsor_id=rt.actor.id)
        rt.actor.flags.add('random_civil_war_sponsor_commitment_active')
        rt.actor.values['random_civil_war_sponsor_recipient_id'] = rt.host.id
        return rt

    def valid(self, rt):
        return rt.condition(SPONSOR['event021_sponsor_repayment_receipt_valid'], rt.host)

    def test_recipient_is_bound_independently_of_root(self):
        rt = self.receipt()
        self.assertNotEqual(rt.sender.id, rt.host.id)
        self.assertTrue(self.valid(rt))

    def test_missing_dead_inactive_and_mismatched_receipts_fail_closed(self):
        changes = {
            'missing pointer': lambda r: r.host.values.pop('random_civil_war_sponsor_scope'),
            'missing recipient sponsor ID': lambda r: r.host.values.pop('random_civil_war_sponsor_id'),
            'missing sponsor recipient ID': lambda r: r.actor.values.pop('random_civil_war_sponsor_recipient_id'),
            'dead sponsor': lambda r: setattr(r.actor, 'exists', False),
            'inactive sponsor': lambda r: r.actor.flags.remove('random_civil_war_sponsor_commitment_active'),
            'no received commitment': lambda r: r.host.flags.remove('random_civil_war_sponsor_commitment_received'),
            'no evidence': lambda r: r.host.flags.remove('random_civil_war_sponsor_evidence_active'),
            'wrong sponsor ID': lambda r: r.host.values.update(random_civil_war_sponsor_id=99),
            'wrong recipient ID': lambda r: r.actor.values.update(random_civil_war_sponsor_recipient_id=99),
        }
        for name, change in changes.items():
            with self.subTest(name=name):
                rt = self.receipt()
                change(rt)
                self.assertFalse(self.valid(rt))


if __name__ == '__main__':
    unittest.main()
